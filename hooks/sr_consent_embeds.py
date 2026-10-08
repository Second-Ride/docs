"""
Externe iframes erst nach Einwilligung laden (MkDocs-Hook, in mkdocs.yml unter
`hooks` eingetragen). Das Markdown bleibt unverändert; der Hook schreibt im
fertigen HTML einer Seite bei jedem iframe mit einer https-Adresse eines
fremden Anbieters (3dviewer.net, YouTube, Google Maps, Lucid ...)

    src="https://..."   ->   data-consent-src="https://..." data-consent-category="marketing"

Ohne `src` lädt der Browser nichts. Die Consent-Engine von second-ride.de
(`/consent.js`, siehe overrides/main.html) setzt `src` erst, wenn der Besucher
Marketing erlaubt hat, und entfernt es beim Widerruf wieder.
javascripts/consent-embeds.js baut dazu den Platzhalter mit dem Hinweis auf.

Eigene Dateien (PDFs mit relativer Adresse) und Adressen unter second-ride.de
bleiben unverändert.

Rücksicht auf print-pipeline/build_full.py, das iframes im gebauten HTML per
Regex ersetzt (`\\bsrc="..."`): Die Regex trifft `data-consent-src="..."`
ebenfalls, weil zwischen `-` und `src` eine Wortgrenze liegt.
"""

import re
from urllib.parse import urlparse

IFRAME_RE = re.compile(r"<iframe\b[^>]*>", re.IGNORECASE)
SRC_RE = re.compile(r"""(\s)src=(["'])(https://[^"']+)\2""", re.IGNORECASE)

# Eigene Hosts brauchen keine Einwilligung.
OWN_DOMAIN = "second-ride.de"

CONSENT_CATEGORY = "marketing"


def _is_own_host(host):
    return host == OWN_DOMAIN or host.endswith("." + OWN_DOMAIN)


def gate_iframe(tag):
    """Gibt das iframe-Tag mit data-consent-src zurück, oder unverändert."""
    src = SRC_RE.search(tag)
    if not src:
        return tag
    host = (urlparse(src.group(3)).hostname or "").lower()
    if not host or _is_own_host(host):
        return tag
    return SRC_RE.sub(
        lambda m: (
            f'{m.group(1)}data-consent-src={m.group(2)}{m.group(3)}{m.group(2)}'
            f' data-consent-category="{CONSENT_CATEGORY}"'
        ),
        tag,
        count=1,
    )


def on_post_page(output, page, config):
    return IFRAME_RE.sub(lambda m: gate_iframe(m.group(0)), output)
