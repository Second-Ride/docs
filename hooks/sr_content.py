"""
Technische Auszeichnung der Doku beim Bauen (MkDocs-Hook, in mkdocs.yml
unter `hooks` eingetragen). Das Markdown bleibt unverändert; der Hook setzt
nur Spans in das fertige HTML einer Seite, damit theme.css Schritte, Werte
und Positionsnummern technisch darstellen kann:

- Schrittnummer am Anfang von h3 bis h5 ("1.1 Motorhalter montieren")
  -> <span class="sr-step-no">1.1</span>
- Positionsnummer im Text ("Deckel (2)") -> Konturkreis wie im Foto, die
  Klammern bleiben für Suche und Screenreader im Text, nur unsichtbar
- LED-Emoji (rot, grün, gelb, lila ...) -> farbiger Punkt; das Emoji bleibt
  im Span, weil die Druck-Pipeline es dort durch einen Punkt ersetzt
- Werte wie M8x25, SW6, TX25, 24 Nm, 12V -> <span class="sr-val">, bricht
  nicht um
- Mengen am Zeilenanfang wie "1x" -> <span class="sr-qty">

Rücksicht auf print-pipeline/build_full.py, die das gebaute HTML per Regex
liest: keine Attribute an Überschriften (HEADING_RE erwartet die id direkt
nach dem Tag), an <table> oder <li> (rebalance_checklists), und nichts in
Code, Links, SVGs oder Skripten.
"""

import re

# In diesen Elementen bleibt der Text, wie er ist.
SKIP_TAGS = {"code", "pre", "a", "script", "style", "svg", "textarea", "kbd", "title"}

TAG_RE = re.compile(r"(<[^>]+>)")
TAG_NAME_RE = re.compile(r"<\s*(/)?\s*([a-zA-Z][a-zA-Z0-9]*)")
STEP_HEADINGS = {"h3", "h4", "h5"}

# Führende Schrittnummer: "1.", "1.1", "1.2.1" gefolgt von Leerraum und Text
STEP_RE = re.compile(r"^(\s*)(\d{1,2}(?:\.\d{1,2}){0,3}\.?)(\s+)(?=\S)")

LEDS = {
    "\U0001F534": ("red", "rot"),
    "\U0001F7E2": ("green", "grün"),
    "\U0001F7E1": ("yellow", "gelb"),
    "\U0001F7E3": ("purple", "lila"),
    "\U0001F7E0": ("orange", "orange"),
    "\U0001F535": ("blue", "blau"),
    "⚫": ("black", "schwarz"),
    "⚪": ("white", "weiß"),
}

UNITS = r"(?:Nm|mm|cm|kWh|Wh|kW|W|V|Ah|km/h|°C)"
INLINE_RE = re.compile(
    "(?P<led>" + "|".join(re.escape(e) for e in LEDS) + ")"
    r"|(?P<ref>\((?P<refno>\d{1,2})\))"
    r"|(?P<qty>(?<![\w.,])\d{1,3}x(?=\s))"
    r"|(?P<val>(?<![\w-])(?:"
    r"M(?:[3-9]|1\d|2[0-4])(?:[x×]\d{1,3}(?:[.,]\d+)?)?"  # Gewinde M3 bis M24, nicht Baureihen wie M50
    r"|(?:SW|TX)\s?\d{1,2}"
    r"|\d{1,4}(?:[.,]\d+)?\s?" + UNITS +
    r")(?![\w/]))"
)


def _inline(match):
    if match.group("led"):
        color, name = LEDS[match.group("led")]
        return (f'<span class="sr-led sr-led--{color}" role="img" aria-label="LED {name}">'
                f'<span class="sr-led__emoji" aria-hidden="true">{match.group("led")}</span></span>')
    if match.group("ref"):
        no = match.group("refno")
        return (f'<span class="sr-ref"><span class="sr-vh">(</span>{no}'
                f'<span class="sr-vh">)</span></span>')
    if match.group("qty"):
        return f'<span class="sr-qty">{match.group("qty")}</span>'
    return f'<span class="sr-val">{match.group("val")}</span>'


def _mark_step(text):
    return STEP_RE.sub(lambda m: f'{m.group(1)}<span class="sr-step-no">{m.group(2)}</span>{m.group(3)}',
                       text, count=1)


def on_page_content(html, page, config, files):
    parts = TAG_RE.split(html)
    skip_depth = 0
    heading = None          # gerade offene Schritt-Überschrift
    await_step = False      # nächster Textknoten darin trägt die Nummer
    out = []

    for part in parts:
        if not part:
            continue
        if part.startswith("<"):
            m = TAG_NAME_RE.match(part)
            if m:
                closing, name = m.group(1), m.group(2).lower()
                self_closing = part.endswith("/>")
                if name in SKIP_TAGS and not self_closing:
                    skip_depth += -1 if closing else 1
                    skip_depth = max(skip_depth, 0)
                if name in STEP_HEADINGS:
                    if closing:
                        heading, await_step = None, False
                    else:
                        heading, await_step = name, True
            out.append(part)
            continue

        text = part
        if skip_depth == 0:
            if heading and await_step and text.strip():
                text = _mark_step(text)
                await_step = False
                # Rest des Textknotens (nach der Nummer) normal auszeichnen
                head, sep, tail = text.partition("</span>")
                if sep:
                    text = head + sep + INLINE_RE.sub(_inline, tail)
                else:
                    text = INLINE_RE.sub(_inline, text)
            else:
                text = INLINE_RE.sub(_inline, text)
        out.append(text)

    return "".join(out)
