#!/bin/bash
# Sync quiz results from server to local
# Usage: ./scripts/sync_results.sh [username]
#
# Results are stored per-user on the server: results/<username>/
# If username is provided, only sync that user's results.
# Otherwise, sync all users.

# Configuration - UPDATE THESE VALUES
SERVER_USER="your-username"
SERVER_HOST="your-server.com"
REMOTE_PATH="/var/www/quizzes/results/"

# Local paths
LOCAL_RESULTS=".cache/quiz-results/"

# Optional: filter by quiz user
QUIZ_USER="${1:-}"

# Ensure local directory exists
mkdir -p "$LOCAL_RESULTS"

echo "Pulling quiz results from server..."

if [ -n "$QUIZ_USER" ]; then
    # Sync specific user's results
    mkdir -p "${LOCAL_RESULTS}${QUIZ_USER}/"
    rsync -avz --progress \
        "${SERVER_USER}@${SERVER_HOST}:${REMOTE_PATH}${QUIZ_USER}/" \
        "${LOCAL_RESULTS}${QUIZ_USER}/"
else
    # Sync all users' results (preserves subdirectory structure)
    rsync -avz --progress \
        "${SERVER_USER}@${SERVER_HOST}:${REMOTE_PATH}" \
        "$LOCAL_RESULTS"
fi

if [ $? -eq 0 ]; then
    FILE_COUNT=$(find "$LOCAL_RESULTS" -name "*_result.json" | wc -l | tr -d ' ')
    echo "✓ Results synced successfully! ($FILE_COUNT result file(s))"
else
    echo "✗ Sync failed. Check your connection and credentials."
    exit 1
fi
