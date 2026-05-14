#!/bin/bash
set -e
cd /root/docs

git fetch --quiet origin main
LOCAL=$(git rev-parse HEAD)
REMOTE=$(git rev-parse origin/main)

if [ "$LOCAL" = "$REMOTE" ]; then
    exit 0
fi

git reset --hard origin/main
source venv/bin/activate
mkdocs build

# Backwards-compatible copy for /all-docs URL
cp site/llms-full.txt site/all-docs

echo "$(date -Iseconds): built ${LOCAL:0:7} -> ${REMOTE:0:7}" >> /var/log/docs-build.log
