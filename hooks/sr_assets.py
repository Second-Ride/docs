"""
Versionsnummer für die eigenen Stylesheets und Skripte (MkDocs-Hook, in
mkdocs.yml unter `hooks` eingetragen).

Cloudflare gibt CSS und JS mit `max-age=14400` aus: Browser behalten sie
vier Stunden. Ohne Versionsnummer sahen Besucher nach einem Deploy bis zu
vier Stunden lang das alte Design (so am 08.10.2026 der schwarze statt des
goldenen Chat-Buttons).

Der Hook hängt an jede lokale Datei aus `extra_css` und `extra_javascript`
`?v=` und einen Kurz-Hash über alle eigenen Stylesheets und Skripte an.
Ändert sich eine davon, ändern sich alle Adressen, und Browser wie
Cloudflare laden neu. `javascripts/typebot.js` gibt seine Versionsnummer an
`stylesheets/chatbot.css` weiter, das im Shadow-DOM des Chats hängt.
"""

import hashlib
from pathlib import Path

# Dateien, die nicht in extra_css/extra_javascript stehen, aber mitzählen
EXTRA_ASSETS = ["stylesheets/chatbot.css"]


def _is_local(path):
    return "://" not in path and not path.startswith("//")


def _script_path(script):
    return script.path if hasattr(script, "path") else script


def on_config(config):
    docs = Path(config["docs_dir"])
    paths = [p for p in config["extra_css"] if _is_local(p)]
    paths += [_script_path(s) for s in config["extra_javascript"] if _is_local(_script_path(s))]
    paths += EXTRA_ASSETS

    digest = hashlib.sha256()
    for path in sorted(set(paths)):
        file = docs / path.split("?", 1)[0]
        if file.is_file():
            digest.update(path.encode())
            digest.update(file.read_bytes())
    version = digest.hexdigest()[:10]

    def versioned(path):
        if not _is_local(path) or "?" in path:
            return path
        return f"{path}?v={version}"

    config["extra_css"] = [versioned(p) for p in config["extra_css"]]
    for script in config["extra_javascript"]:
        if hasattr(script, "path"):
            script.path = versioned(script.path)
    config["extra_javascript"] = [
        s if hasattr(s, "path") else versioned(s) for s in config["extra_javascript"]
    ]
    return config
