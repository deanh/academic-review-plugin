#!/bin/bash
# Sync quiz results from server to local
# Usage: ./scripts/sync_results.sh

# Configuration - UPDATE THESE VALUES
SERVER_USER="your-username"
SERVER_HOST="your-server.com"
REMOTE_PATH="/var/www/quizzes/results/"

# Local paths
LOCAL_RESULTS=".cache/quiz-results/"

# Ensure local directory exists
mkdir -p "$LOCAL_RESULTS"

echo "Pulling quiz results from server..."

# Rsync from server
rsync -avz --progress \
    "${SERVER_USER}@${SERVER_HOST}:${REMOTE_PATH}" \
    "$LOCAL_RESULTS"

if [ $? -eq 0 ]; then
    FILE_COUNT=$(find "$LOCAL_RESULTS" -name "*.json" | wc -l | tr -d ' ')
    echo "✓ Results synced successfully! ($FILE_COUNT result file(s))"
else
    echo "✗ Sync failed. Check your connection and credentials."
    exit 1
fi
