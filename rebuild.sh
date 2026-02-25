#!/bin/bash
set -e
cd /root/docs
git fetch origin
git reset --hard origin/main
source venv/bin/activate
mkdocs build

# Backwards-compatible copy for /all-docs URL
cp site/llms-full.txt site/all-docs

echo "$(date): Build successful" >> /var/log/docs-build.log
