"""
Weiterleitungen für umgezogene Doku-Seiten (MkDocs-Hook, in mkdocs.yml unter
`hooks` eingetragen). Beim Bauen entsteht für jede alte Adresse eine kleine
HTML-Seite, die auf die neue Adresse weiterleitet.

Die Tabelle steht in mkdocs.yml unter `extra: redirect_maps:` und hat dasselbe
Format wie beim Plugin mkdocs-redirects:

    extra:
      redirect_maps:
        alte/seite/index.md: neue/seite/index.md       # Seite der Doku
        alte/seite2/index.md: https://example.com/     # oder eine fremde Adresse

Links und Schlüssel sind Pfade der Markdown-Dateien relativ zu `docs/`. Die
alte Datei muss es nicht mehr geben, sie darf aber keine bestehende Seite sein.

Warum ein Hook und kein Plugin: rebuild.sh installiert auf dem Server keine
Pakete aus requirements.txt. Ein fehlendes Plugin würde den Build abbrechen und
die Live-Seite stehen lassen. Der Hook braucht nur die Standardbibliothek, wie
llms_bot.py. Wer doch mkdocs-redirects einsetzen will, verschiebt die Tabelle
unverändert unter `plugins: - redirects: redirect_maps:` und entfernt diesen Hook.
"""

import json
import logging
from html import escape
from pathlib import Path

log = logging.getLogger("mkdocs.hooks.redirects")

_page_urls = {}  # src_uri -> URL der Seite ("faq/mid50/")


def _old_url(src):
    """Verzeichnis-URL der alten Seite: a/b/index.md -> a/b/, a/b.md -> a/b/."""
    if src == "index.md":
        return ""
    if src.endswith("/index.md"):
        return src[: -len("index.md")]
    if src.endswith(".md"):
        return src[: -len(".md")] + "/"
    return src


def _page(target):
    # Ohne JavaScript greift die Meta-Weiterleitung. Das Skript hängt zusätzlich den Anker
    # der alten Adresse (#...) an das Ziel an, sofern das Ziel selbst keinen hat. Mit noindex
    # bleibt die Weiterleitung aus dem Suchindex, canonical nennt die neue Adresse als maßgeblich.
    url = escape(target, quote=True)
    js = json.dumps(target)
    return (
        "<!doctype html>\n"
        '<html lang="de">\n<head>\n<meta charset="utf-8">\n'
        "<title>Weiterleitung</title>\n"
        f'<link rel="canonical" href="{url}">\n'
        '<meta name="robots" content="noindex">\n'
        f'<meta http-equiv="refresh" content="0; url={url}">\n'
        f"<script>var t={js};if(t.indexOf('#')<0){{t+=location.hash;}}location.replace(t);</script>\n"
        "</head>\n<body>\n"
        f'<p>Diese Seite ist umgezogen: <a href="{url}">{url}</a></p>\n'
        "</body>\n</html>\n"
    )


def on_files(files, config):
    _page_urls.clear()
    for f in files.documentation_pages():
        _page_urls[f.src_uri] = f.url
    return files


def on_post_build(config):
    maps = (config.get("extra") or {}).get("redirect_maps") or {}
    if not maps:
        return
    site_dir = Path(config["site_dir"])
    live_urls = set(_page_urls.values())
    written = 0
    for old, new in maps.items():
        old_url = _old_url(old)
        if old_url in live_urls:
            log.warning("Weiterleitung übersprungen, %s ist eine bestehende Seite", old)
            continue
        if new.startswith(("http://", "https://")):
            target = new
        elif new in _page_urls:
            target = "/" + _page_urls[new]
        else:
            log.warning("Weiterleitung übersprungen, Ziel %s von %s gibt es nicht", new, old)
            continue
        out = site_dir / old_url / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(_page(target), encoding="utf-8")
        written += 1
    log.info("redirects: %d Weiterleitungen geschrieben", written)
