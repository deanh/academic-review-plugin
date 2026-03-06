#!/usr/bin/env python3
"""
Quiz Server - Flask application for serving academic quizzes.
Deploy to: /var/www/quizzes/server.py

Supports:
- Multiple courses with separate question pools
- Quick Quiz: Random N questions from a course
- Topic Practice: All questions for a specific topic
- Offline caching per course
"""

import functools
import json
import random
import secrets
import uuid
from datetime import datetime, timedelta
from pathlib import Path

from flask import Flask, jsonify, render_template, request, abort, redirect, url_for, session
from werkzeug.security import check_password_hash

app = Flask(__name__)

# Secret key for session signing
SECRET_KEY_FILE = Path(__file__).parent / ".secret_key"
if SECRET_KEY_FILE.exists():
    app.secret_key = SECRET_KEY_FILE.read_text().strip()
else:
    # Generate and persist a secret key on first run
    app.secret_key = secrets.token_hex(32)
    SECRET_KEY_FILE.write_text(app.secret_key)

app.permanent_session_lifetime = timedelta(days=30)

# Configuration
DATA_DIR = Path(__file__).parent / "data"
QUESTIONS_DIR = DATA_DIR / "questions"
RESULTS_DIR = Path(__file__).parent / "results"
USERS_FILE = Path(__file__).parent / "users.json"

# Ensure directories exist
DATA_DIR.mkdir(exist_ok=True)
QUESTIONS_DIR.mkdir(exist_ok=True)
RESULTS_DIR.mkdir(exist_ok=True)


# --- Authentication ---

def load_users() -> dict:
    """Load user credentials from users.json."""
    if USERS_FILE.exists():
        with open(USERS_FILE) as f:
            return json.load(f)
    return {}


def login_required(f):
    """Decorator to require authentication."""
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated


def get_user_results_dir(username: str) -> Path:
    """Get the results directory for a specific user."""
    user_dir = RESULTS_DIR / username
    user_dir.mkdir(exist_ok=True)
    return user_dir

# Course and topic metadata
COURSES = {
    "pcv": {
        "name": "Photogrammetry & Computer Vision",
        "short_name": "PCV",
        "description": "TUM PCV course - multi-view geometry, camera models, reconstruction",
        "topics": {
            "homogeneous_2d": {
                "name": "Homogeneous 2D Coordinates",
                "description": "Points, lines, dual conics in 2D projective space",
                "lectures": ["pcv3", "pcv4"]
            },
            "transformations": {
                "name": "Planar Transformations & Homography",
                "description": "2D transformations, DLT algorithm, concatenation/inversion",
                "lectures": ["pcv4", "pcv5", "pcv6"]
            },
            "homogeneous_3d": {
                "name": "Homogeneous 3D & Spatial Transforms",
                "description": "Points, planes, quadrics, spatial transformations",
                "lectures": ["pcv7"]
            },
            "camera_model": {
                "name": "Camera Model & Projection",
                "description": "Projection matrix, interior/exterior orientation, spatial resection",
                "lectures": ["pcv8", "pcv9"]
            },
            "distortion": {
                "name": "Distortion & Aberrations",
                "description": "Radial distortion, lens aberrations, calibration",
                "lectures": ["pcv10"]
            },
            "epipolar": {
                "name": "Epipolar Geometry",
                "description": "Fundamental matrix, essential matrix, 8-point algorithm",
                "lectures": ["pcv11", "pcv12"]
            },
            "triangulation": {
                "name": "Triangulation & Reconstruction",
                "description": "Spatial intersection, stereo normal case, projective reconstruction",
                "lectures": ["pcv13"]
            },
            "trifocal": {
                "name": "Trifocal Geometry",
                "description": "Trifocal tensor, point/line transfer, tensor estimation",
                "lectures": ["pcv14", "pcv15"]
            },
            "bundle_adjustment": {
                "name": "Bundle Adjustment",
                "description": "Nonlinear optimization, Jacobian structure, sparse systems",
                "lectures": ["pcv17", "pcv19"]
            },
            "calibration": {
                "name": "Calibration & Self-Calibration",
                "description": "Absolute conic, Kruppa equations, DAQ",
                "lectures": ["pcv18", "pcv20"]
            },
            "robust_estimation": {
                "name": "Robust Estimation",
                "description": "RANSAC, M-estimators, LMedS",
                "lectures": ["pcv21"]
            },
            "dof_redundancy": {
                "name": "DOF & Redundancy Drill",
                "description": "Degrees of freedom, constraints, and parameterization across all topics",
                "lectures": ["pcv3", "pcv4", "pcv5", "pcv7", "pcv8", "pcv11", "pcv12", "pcv14", "pcv17", "pcv18"]
            }
        }
    }
}


def get_course_dir(course_id: str) -> Path:
    """Get the questions directory for a course."""
    return QUESTIONS_DIR / course_id


def load_questions_for_topic(course_id: str, topic_id: str) -> list:
    """Load all questions for a specific topic in a course."""
    topic_file = get_course_dir(course_id) / f"{topic_id}.json"
    if topic_file.exists():
        with open(topic_file) as f:
            return json.load(f)
    return []


def load_all_questions_for_course(course_id: str) -> dict:
    """Load all questions from all topic files in a course."""
    course_dir = get_course_dir(course_id)
    all_questions = {}
    if not course_dir.exists():
        return all_questions
    for topic_file in course_dir.glob("*.json"):
        topic_id = topic_file.stem
        try:
            with open(topic_file) as f:
                questions = json.load(f)
                all_questions[topic_id] = questions
        except (json.JSONDecodeError, IOError):
            continue
    return all_questions


def get_topics_with_counts(course_id: str) -> list:
    """Get list of topics with question counts for a course."""
    course = COURSES.get(course_id)
    if not course:
        return []

    course_dir = get_course_dir(course_id)
    topics = []

    for topic_file in course_dir.glob("*.json"):
        topic_id = topic_file.stem
        try:
            with open(topic_file) as f:
                questions = json.load(f)
                info = course["topics"].get(topic_id, {})
                topics.append({
                    "id": topic_id,
                    "name": info.get("name", topic_id.replace("_", " ").title()),
                    "description": info.get("description", ""),
                    "lectures": info.get("lectures", []),
                    "count": len(questions)
                })
        except (json.JSONDecodeError, IOError):
            continue

    # Sort by lecture number (first lecture in list)
    topics.sort(key=lambda t: t.get("lectures", ["zzz"])[0])
    return topics


def get_total_question_count(course_id: str) -> int:
    """Get total number of questions in a course."""
    course_dir = get_course_dir(course_id)
    total = 0
    if not course_dir.exists():
        return 0
    for topic_file in course_dir.glob("*.json"):
        try:
            with open(topic_file) as f:
                questions = json.load(f)
                total += len(questions)
        except (json.JSONDecodeError, IOError):
            continue
    return total


def get_courses_with_counts() -> list:
    """Get list of all courses with question counts."""
    courses = []
    for course_id, course_info in COURSES.items():
        count = get_total_question_count(course_id)
        if count > 0:  # Only show courses that have questions
            courses.append({
                "id": course_id,
                "name": course_info["name"],
                "short_name": course_info["short_name"],
                "description": course_info["description"],
                "count": count
            })
    return courses


def get_best_scores_for_course(course_id: str, username: str) -> dict:
    """Get best score per topic from a user's results files.

    Returns dict mapping topic_id -> {score, total, percentage, attempts}
    """
    best_scores = {}

    user_dir = RESULTS_DIR / username
    if not user_dir.exists():
        return best_scores

    # Get valid topic IDs for this course
    course = COURSES.get(course_id, {})
    valid_topics = set(course.get("topics", {}).keys())

    for result_file in user_dir.glob("*_result.json"):
        try:
            with open(result_file) as f:
                result = json.load(f)

            # Skip offline results without scores
            if result.get("percentage") is None:
                continue

            quiz_id = result.get("quiz_id", "")
            topic_id = None

            # Try new format: {course}_topic_{topic_id}_{timestamp}
            if f"{course_id}_topic_" in quiz_id:
                parts = quiz_id.split(f"{course_id}_topic_")[1]
                topic_parts = parts.split("_")
                # Timestamp is last 2 parts (date and time)
                topic_id = "_".join(topic_parts[:-2]) if len(topic_parts) > 2 else topic_parts[0]

            # Try old format: topic_{topic_id}_{timestamp} (no course prefix)
            elif quiz_id.startswith("topic_") and result.get("course") is None:
                parts = quiz_id[6:]  # Remove "topic_" prefix
                topic_parts = parts.split("_")
                # Timestamp is last 2 parts (date and time)
                candidate = "_".join(topic_parts[:-2]) if len(topic_parts) > 2 else topic_parts[0]
                # Only use if it matches a valid topic for this course
                if candidate in valid_topics:
                    topic_id = candidate

            # Also check explicit course field matches
            elif result.get("course") == course_id and "_topic_" in quiz_id:
                # Generic format with course field
                parts = quiz_id.split("_topic_")[1] if "_topic_" in quiz_id else None
                if parts:
                    topic_parts = parts.split("_")
                    topic_id = "_".join(topic_parts[:-2]) if len(topic_parts) > 2 else topic_parts[0]

            if topic_id and topic_id in valid_topics:
                percentage = result.get("percentage", 0)

                if topic_id not in best_scores:
                    best_scores[topic_id] = {
                        "score": result.get("score", 0),
                        "total": result.get("total", 0),
                        "percentage": percentage,
                        "attempts": 1
                    }
                else:
                    best_scores[topic_id]["attempts"] += 1
                    if percentage > best_scores[topic_id]["percentage"]:
                        best_scores[topic_id]["score"] = result.get("score", 0)
                        best_scores[topic_id]["total"] = result.get("total", 0)
                        best_scores[topic_id]["percentage"] = percentage
        except (json.JSONDecodeError, IOError, KeyError):
            continue

    return best_scores


def store_offline_result(data: dict, username: str):
    """Store an offline quiz result without scoring (no server-side quiz file)."""
    result = {
        "quiz_id": data["quiz_id"],
        "course": data.get("course", "unknown"),
        "quiz_topic": data.get("quiz_topic", "Unknown"),
        "quiz_lecture": data.get("quiz_lecture", "Unknown"),
        "completed": datetime.utcnow().isoformat() + "Z",
        "queued_at": data.get("queued_at"),
        "offline": True,
        "answers": data["answers"],
        "total_time_sec": data.get("total_time_sec", 0),
        "total": len(data["answers"]),
        "score": None,  # Cannot score without correct answers
        "percentage": None
    }

    # Save result to user directory
    user_dir = get_user_results_dir(username)
    result_file = user_dir / f"{data['quiz_id']}_result.json"
    with open(result_file, "w") as f:
        json.dump(result, f, indent=2)

    return jsonify({
        "success": True,
        "offline": True,
        "message": "Result stored for later review"
    })


def strip_answers(questions: list) -> list:
    """Remove correct answers from questions for client.

    Shuffles multiple choice options to prevent position bias.
    """
    client_questions = []
    for q in questions:
        client_q = {
            "id": q["id"],
            "type": q["type"],
            "question": q["question"],
            "topic": q.get("topic", ""),
        }
        if q["type"] == "multiple_choice":
            # Shuffle options to prevent position bias
            options = q["options"][:]
            correct_answer = options[q["correct"]]
            random.shuffle(options)
            client_q["options"] = options
            # Update both options and correct index in original for scoring
            q["options"] = options
            q["correct"] = options.index(correct_answer)
        client_questions.append(client_q)
    return client_questions


# Routes

@app.route("/login", methods=["GET", "POST"])
def login():
    """Login page."""
    if "user" in session:
        return redirect(url_for("index"))

    error = None
    if request.method == "POST":
        username = request.form.get("username", "").strip().lower()
        password = request.form.get("password", "")
        users = load_users()

        if username in users and check_password_hash(users[username], password):
            session.permanent = True
            session["user"] = username
            return redirect(url_for("index"))
        else:
            error = "Invalid username or password."

    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    """Clear session and redirect to login."""
    session.clear()
    return redirect(url_for("login"))


@app.route("/")
@login_required
def index():
    """Home page - list of courses."""
    courses = get_courses_with_counts()
    return render_template("index.html", courses=courses)


@app.route("/course/<course_id>")
@login_required
def course_home(course_id: str):
    """Course home page with quick quiz and topic list."""
    if course_id not in COURSES:
        abort(404, description="Course not found")

    course = COURSES[course_id]
    topics = get_topics_with_counts(course_id)
    total_questions = get_total_question_count(course_id)
    best_scores = get_best_scores_for_course(course_id, session["user"])

    # Add best score info to each topic
    for topic in topics:
        if topic["id"] in best_scores:
            topic["best"] = best_scores[topic["id"]]

    return render_template("course.html",
                         course_id=course_id,
                         course=course,
                         topics=topics,
                         total_questions=total_questions)


@app.route("/course/<course_id>/quick")
@login_required
def quick_quiz(course_id: str):
    """Start a quick quiz with random questions from a course."""
    if course_id not in COURSES:
        abort(404, description="Course not found")

    count = request.args.get("count", 10, type=int)
    count = min(max(count, 5), 50)  # Clamp between 5 and 50

    # Gather all questions for this course
    all_questions = load_all_questions_for_course(course_id)
    question_pool = []
    for topic_id, questions in all_questions.items():
        for q in questions:
            q["topic_id"] = topic_id
        question_pool.extend(questions)

    if not question_pool:
        abort(404, description="No questions available")

    # Random sample
    selected = random.sample(question_pool, min(count, len(question_pool)))

    # Generate quiz ID with course prefix
    quiz_id = f"{course_id}_quick_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}"

    course = COURSES[course_id]
    quiz = {
        "id": quiz_id,
        "course": course_id,
        "mode": "quick",
        "topic": f"Quick Quiz ({len(selected)} questions)",
        "lecture": course["short_name"],
        "questions": strip_answers(selected)
    }

    # Store the full quiz with answers for scoring in user directory
    user_dir = get_user_results_dir(session["user"])
    quiz_file = user_dir / f"{quiz_id}_quiz.json"
    with open(quiz_file, "w") as f:
        json.dump({"id": quiz_id, "course": course_id, "questions": selected}, f)

    return render_template("quiz.html", quiz=quiz, course_id=course_id)


@app.route("/course/<course_id>/topic/<topic_id>")
@login_required
def topic_quiz(course_id: str, topic_id: str):
    """Start a quiz with all questions for a topic."""
    if course_id not in COURSES:
        abort(404, description="Course not found")

    questions = load_questions_for_topic(course_id, topic_id)
    if not questions:
        abort(404, description="Topic not found or has no questions")

    course = COURSES[course_id]
    topic_info = course["topics"].get(topic_id, {})
    quiz_id = f"{course_id}_topic_{topic_id}_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}"

    quiz = {
        "id": quiz_id,
        "course": course_id,
        "mode": "topic",
        "topic": topic_info.get("name", topic_id.replace("_", " ").title()),
        "lecture": ", ".join(topic_info.get("lectures", [])).upper(),
        "questions": strip_answers(questions)
    }

    # Store the full quiz with answers for scoring in user directory
    user_dir = get_user_results_dir(session["user"])
    quiz_file = user_dir / f"{quiz_id}_quiz.json"
    with open(quiz_file, "w") as f:
        json.dump({"id": quiz_id, "course": course_id, "questions": questions}, f)

    return render_template("quiz.html", quiz=quiz, course_id=course_id)


@app.route("/quiz/submit", methods=["POST"])
@login_required
def submit_quiz():
    """Submit quiz answers and return results."""
    data = request.get_json()
    if not data or "quiz_id" not in data or "answers" not in data:
        abort(400, description="Invalid submission")

    quiz_id = data["quiz_id"]
    username = session["user"]
    user_dir = get_user_results_dir(username)

    # Load the stored quiz with answers from user directory
    quiz_file = user_dir / f"{quiz_id}_quiz.json"
    if not quiz_file.exists():
        # This might be an offline submission - store without scoring
        return store_offline_result(data, username)

    with open(quiz_file) as f:
        quiz = json.load(f)

    # Build result with scoring
    result = {
        "quiz_id": quiz_id,
        "course": quiz.get("course", "unknown"),
        "completed": datetime.utcnow().isoformat() + "Z",
        "answers": [],
        "score": 0,
        "total": len(quiz["questions"])
    }

    # Create answer lookup
    answers_by_id = {a["question_id"]: a for a in data["answers"]}

    for q in quiz["questions"]:
        answer_data = answers_by_id.get(q["id"], {})
        answer_record = {
            "question_id": q["id"],
            "topic": q.get("topic", ""),
            "slide_ref": q.get("slide_ref", ""),
            "type": q["type"],
        }

        if q["type"] == "multiple_choice":
            selected = answer_data.get("selected")
            answer_record["selected"] = selected
            answer_record["correct_index"] = q["correct"]
            answer_record["is_correct"] = selected == q["correct"]
            if answer_record["is_correct"]:
                result["score"] += 1

        elif q["type"] == "true_false":
            selected = answer_data.get("selected")
            answer_record["selected"] = selected
            answer_record["correct_value"] = q["correct"]
            answer_record["is_correct"] = selected == q["correct"]
            if answer_record["is_correct"]:
                result["score"] += 1

        elif q["type"] == "short_answer":
            # Keep for backwards compatibility but don't generate new ones
            text = answer_data.get("text", "")
            answer_record["text"] = text
            keywords = q.get("expected_keywords", [])
            found = sum(1 for kw in keywords if kw.lower() in text.lower())
            answer_record["keywords_found"] = found
            answer_record["keywords_expected"] = len(keywords)
            if keywords and found >= len(keywords) // 2:
                result["score"] += 1
                answer_record["is_correct"] = found == len(keywords)
            else:
                answer_record["is_correct"] = False

        answer_record["time_spent_sec"] = answer_data.get("time_spent_sec", 0)
        result["answers"].append(answer_record)

    result["total_time_sec"] = data.get("total_time_sec", 0)
    result["percentage"] = round(result["score"] / result["total"] * 100) if result["total"] > 0 else 0

    # Save result to user directory
    result_file = user_dir / f"{quiz_id}_result.json"
    with open(result_file, "w") as f:
        json.dump(result, f, indent=2)

    # Build per-question details for mastery mode retries
    details = []
    for ans in result["answers"]:
        detail = {"id": ans["question_id"], "correct": ans["is_correct"]}
        if not ans["is_correct"]:
            if ans["type"] == "multiple_choice":
                detail["correct_answer"] = ans["correct_index"]
            elif ans["type"] == "true_false":
                detail["correct_answer"] = ans["correct_value"]
        details.append(detail)

    return jsonify({
        "success": True,
        "score": result["score"],
        "total": result["total"],
        "percentage": result["percentage"],
        "details": details
    })


# API endpoints

@app.route("/api/courses")
@login_required
def api_courses():
    """API endpoint to list courses."""
    return jsonify(get_courses_with_counts())


@app.route("/api/course/<course_id>/topics")
@login_required
def api_topics(course_id: str):
    """API endpoint to list topics for a course."""
    if course_id not in COURSES:
        abort(404)
    return jsonify(get_topics_with_counts(course_id))


@app.route("/api/course/<course_id>/questions/all")
@login_required
def api_all_questions(course_id: str):
    """API endpoint to get all questions for a course (for offline caching)."""
    if course_id not in COURSES:
        abort(404)

    all_questions = load_all_questions_for_course(course_id)
    course = COURSES[course_id]

    # Strip answers for client but include topic_id
    result = {}
    for topic_id, questions in all_questions.items():
        result[topic_id] = []
        for q in questions:
            client_q = {
                "id": q["id"],
                "type": q["type"],
                "question": q["question"],
                "topic": q.get("topic", ""),
                "topic_id": topic_id,
            }
            if q["type"] == "multiple_choice":
                client_q["options"] = q["options"]
            result[topic_id].append(client_q)

    return jsonify({
        "course_id": course_id,
        "course_name": course["name"],
        "topics": course["topics"],
        "questions": result,
        "generated": datetime.utcnow().isoformat() + "Z"
    })


@app.route("/api/course/<course_id>/questions/<topic_id>")
@login_required
def api_topic_questions(course_id: str, topic_id: str):
    """API endpoint to get questions for a specific topic."""
    if course_id not in COURSES:
        abort(404)
    questions = load_questions_for_topic(course_id, topic_id)
    if not questions:
        abort(404)
    return jsonify(strip_answers(questions))


if __name__ == "__main__":
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5050
    app.run(host="0.0.0.0", port=port, debug=True)
