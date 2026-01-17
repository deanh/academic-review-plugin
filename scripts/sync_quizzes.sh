#!/bin/bash
# Sync quizzes from local to server
# Usage: ./scripts/sync_quizzes.sh

# Configuration - UPDATE THESE VALUES
SERVER_USER="your-username"
SERVER_HOST="your-server.com"
REMOTE_PATH="/var/www/quizzes/data/"

# Local paths
LOCAL_QUIZZES=".cache/web-quizzes/"

# Check if local directory exists
if [ ! -d "$LOCAL_QUIZZES" ]; then
    echo "Error: Local quizzes directory not found: $LOCAL_QUIZZES"
    exit 1
fi

# Count files to sync
FILE_COUNT=$(find "$LOCAL_QUIZZES" -name "*.json" | wc -l | tr -d ' ')
echo "Syncing $FILE_COUNT quiz file(s) to server..."

# Rsync to server
rsync -avz --progress \
    "$LOCAL_QUIZZES" \
    "${SERVER_USER}@${SERVER_HOST}:${REMOTE_PATH}"

if [ $? -eq 0 ]; then
    echo "✓ Quizzes synced successfully!"
else
    echo "✗ Sync failed. Check your connection and credentials."
    exit 1
fi
