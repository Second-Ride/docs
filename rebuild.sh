#!/bin/bash
# Auto-Deploy der Doku auf dem Server, per Cron alle 10 Minuten.
#
# Gebaut wird, bis origin/main erfolgreich gebaut ist. Der zuletzt
# erfolgreich gebaute Stand steht in .last-built. Schlägt ein Build fehl,
# versucht es der nächste Lauf erneut; vorher blieb die Seite dann stehen,
# weil HEAD schon gleich origin/main war (so vom 12.08. bis 07.10.2026).
#
# Gebaut wird nach .site-new und erst danach nach site/ übertragen, damit
# ein Fehler die Live-Seite nicht leert. site/ bleibt dasselbe Verzeichnis,
# weil Caddy es eingebunden hat.
#
# Dieses Skript liegt im Repo: git reset --hard unten setzt es bei jedem
# Build auf den Stand von main. Änderungen deshalb hier committen, nicht
# auf dem Server.
set -e
cd /root/docs

# Nicht zwei Läufe gleichzeitig
exec 9>>.rebuild.lock
flock -n 9 || exit 0

git fetch --quiet origin main
REMOTE=$(git rev-parse origin/main)
BUILT=$(cat .last-built 2>/dev/null || true)

if [ "$BUILT" = "$REMOTE" ]; then
    exit 0
fi

git reset --hard origin/main
source venv/bin/activate
rm -rf .site-new
mkdocs build -d .site-new

# Backwards-compatible copy for /all-docs URL
cp .site-new/llms-full.txt .site-new/all-docs

rsync -rlt --delete .site-new/ site/
rm -rf .site-new

echo "$REMOTE" > .last-built
echo "$(date -Iseconds): built ${BUILT:0:7} -> ${REMOTE:0:7}" >> /var/log/docs-build.log
