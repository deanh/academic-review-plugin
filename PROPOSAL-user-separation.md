# Proposal: User Login & Result Separation

## Problem

All quiz results are stored in a shared `results/` directory with no user identification. The course page shows "best scores" computed globally across all result files. With multiple users, scores intermingle and progress tracking becomes meaningless.

## Current Architecture (relevant parts)

- **Server-side**: Flask app stores `{quiz_id}_result.json` and `{quiz_id}_quiz.json` files in `results/`. Best scores are computed by scanning all `*_result.json` files (`get_best_scores_for_course()`).
- **Client-side**: `localStorage` used for offline queue (`pcv_results_queue`) and question cache (`quiz_cache_{course}`). These are already per-browser/per-device.
- **Deployment**: Flask behind nginx on a Digital Ocean droplet (not yet deployed). Systemd service runs as `www-data` with `ReadWritePaths=/var/www/quizzes/results /var/www/quizzes/data`.
- **Content pipeline**: Quizzes are generated locally (LLM + OCR extraction via Marker), then rsynced to the server's `data/questions/{course}/` directory. Results are rsynced back for local review.

## Options Considered

### Option A: nginx HTTP Basic Auth
- **How**: Add `auth_basic` to the nginx location block, maintain an `htpasswd` file.
- **Pros**: Zero Flask code changes for auth itself; nginx handles it.
- **Cons**: Clunky UX (browser popup, no logout); username available to Flask only via `X-Remote-User` header (requires server changes anyway); managing `htpasswd` on the server for each student is manual; doesn't work well with offline/PWA path since browsers cache credentials inconsistently.
- **Verdict**: Too crude. Login UX is poor and doesn't solve result separation without server changes anyway.

### Option B: Flask Session Auth (simple username/password)
- **How**: Add a `/login` page, store user in Flask session cookie, gate all routes. Store results in `results/{username}/` subdirectories.
- **Pros**: Full control over UX; clean login page; server knows the user on every request; results are cleanly separated on disk; easy to add/remove users via a config file or simple JSON.
- **Cons**: Requires a session secret, cookie handling, and a user store. More code than Option C.
- **Verdict**: Good balance of simplicity and correctness. **Recommended.**

### Option C: Client-side Only (localStorage username)
- **How**: Prompt for a username on first visit, store it in `localStorage`. Tag all submitted results with that username. Filter best scores client-side or send username as a query param.
- **Pros**: No server auth changes; very simple to implement.
- **Cons**: No actual access control — anyone can visit the site; users can trivially impersonate others; server-side `get_best_scores_for_course()` needs a username filter (or scoring moves to client); doesn't prevent one user from seeing another's raw results via the API. Result separation without auth is just decoration.
- **Verdict**: Insufficient. If you want real separation, you need server-side identity.

## Recommendation: Option B — Flask Session Auth

### 1. User Store (`server/users.json`)

A simple JSON file with hashed passwords. No database needed. For <10 users this is fine.

```json
{
  "harry": "$2b$12$...",
  "alice": "$2b$12$..."
}
```

A small CLI helper (`server/manage_users.py`) to add/remove users:
```bash
uv run python server/manage_users.py add alice
uv run python server/manage_users.py remove bob
uv run python server/manage_users.py list
```

Uses `werkzeug.security.generate_password_hash` / `check_password_hash` (already a Flask/Werkzeug dependency — no new packages needed).

### 2. Auth Routes & Middleware

| Route | Purpose |
|-------|---------|
| `GET /login` | Login page (simple form, same mobile-friendly styling) |
| `POST /login` | Validate credentials, set session, redirect to `/` |
| `GET /logout` | Clear session, redirect to `/login` |

All other routes get a `@login_required` decorator that checks `session["user"]` and redirects to `/login` if absent.

Flask's built-in `session` (signed cookie via Werkzeug) is sufficient — no server-side session store needed. Set `app.secret_key` from an environment variable or a generated file.

Sessions set to `permanent = True` with a 30-day lifetime so users aren't constantly re-logging in on their phones.

### 3. Result Separation

**Storage**: Results go into `results/{username}/` instead of flat `results/`.

```
results/
├── harry/
│   ├── pcv_topic_epipolar_20260211_204826_result.json
│   └── pcv_topic_epipolar_20260211_204826_quiz.json
└── alice/
    └── ...
```

**Scoring**: `get_best_scores_for_course()` takes a `username` parameter and only scans that user's subdirectory.

**Quiz files**: The `_quiz.json` files (server-side answer keys for scoring) also move into the user's directory since they're per-session.

### 4. What Changes, What Doesn't

**Changes:**

| Component | Change |
|-----------|--------|
| `server.py` | Add login/logout routes, `@login_required` decorator, pass `session["user"]` to result storage and score lookup functions |
| `server.py` result paths | `RESULTS_DIR / username / filename` instead of `RESULTS_DIR / filename` |
| `get_best_scores_for_course()` | Accept `username` param, scan `results/{username}/` |
| `store_offline_result()` | Write to user subdirectory |
| `submit_quiz()` | Read/write quiz and result files from user subdirectory |
| `templates/` | New `login.html`; minor nav changes (show username, logout link) |
| `sync_results.sh` | Sync `results/` recursively (already does, just subdirs now) |
| `systemd service` | No change — `ReadWritePaths` already covers `results/` recursively |
| `pyproject.toml` | No change — `werkzeug` is already a Flask dependency |

**No changes:**

| Component | Why |
|-----------|-----|
| Question storage (`data/questions/`) | Shared across all users — this is the content pool |
| Quiz generation pipeline (local LLM + OCR) | Generates content, not user-specific |
| `sync_quizzes.sh` | Syncs questions to `data/`, unrelated to users |
| `quiz.js` | `fetch('/quiz/submit')` works unchanged — session cookie sent automatically |
| `course.js` | Offline cache is per-browser already; pending result sync works as-is |
| `validate_quizzes.py` | Validates question format, not results |
| nginx config | Auth is at Flask level, not nginx |
| COURSES dict / topic metadata | Course definitions are global |

### 5. Adding New Courses

When you add 3-4 more courses, the flow is:

1. Generate questions locally (LLM + OCR extraction → quiz JSON)
2. Add course entry to `COURSES` dict in `server.py`
3. Place question files in `server/data/questions/{course_id}/`
4. Rsync to server

User auth is completely orthogonal to this. New courses appear for all users automatically. Each user's results are tracked separately per course in their own `results/{username}/` directory.

### 6. Migration of Existing Results

Since the server hasn't been deployed yet, there's nothing to migrate on the server side. The existing `server/results/` files locally are from your development/testing. When you deploy, you start clean with the new directory structure.

If you want to preserve your local test results for reference, a one-time script can move them into `results/harry/` (or similar).

### 7. Deployment Considerations

The `manage_users.py` CLI needs to run on the server to add users. Two options:

- **Option 1**: Run it locally, rsync `users.json` to the server (simplest — you manage users from your machine).
- **Option 2**: SSH to the server and run it there.

For the secret key, generate one at deploy time:
```bash
python -c "import secrets; print(secrets.token_hex(32))" > /var/www/quizzes/.secret_key
```
The app reads this file on startup. Add `.secret_key` to `.gitignore`.

## Scope Estimate

| Component | Effort |
|-----------|--------|
| `manage_users.py` CLI | Small |
| Login/logout routes + `@login_required` decorator | Small |
| `login.html` template | Small |
| Result directory separation (refactor ~3 functions) | Small |
| Nav updates (username display, logout link) | Trivial |
| **Total** | **~200 lines of new/changed Python, ~50 lines of HTML** |

No new dependencies. No database. No nginx changes.
