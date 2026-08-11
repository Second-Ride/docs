#!/usr/bin/env python3
"""Baut die Revisions-/Datum-Seite, die zwischen Titelblatt und
Inhaltsverzeichnis eingefuegt wird. Eigenes, schlankes @page ohne
Kopf-/Fusszeile (kein Seitenzaehler) -- die Seite bleibt wie das Titelblatt
unnummeriert, "Seite 1" beginnt weiterhin beim Inhaltsverzeichnis."""
import base64
import os
from datetime import date, datetime
from pathlib import Path

from weasyprint import HTML

SCRATCH = Path(__file__).parent

GERMAN_MONTHS = [
    "Januar", "Februar", "März", "April", "Mai", "Juni",
    "Juli", "August", "September", "Oktober", "November", "Dezember",
]


def german_date(d):
    return f"{d.day}. {GERMAN_MONTHS[d.month - 1]} {d.year}"


REVISION = os.environ.get("PRINT_REVISION", "00")
# PRINT_CREATED_DATE als ISO-String (YYYY-MM-DD) ueberschreibbar, sonst das
# Datum des Bau-Laufs -- so bleibt ein Release reproduzierbar nachbaubar.
_created_env = os.environ.get("PRINT_CREATED_DATE")
CREATED_DATE = date.fromisoformat(_created_env) if _created_env else datetime.now().date()
CREATED = german_date(CREATED_DATE)

logo_b64 = base64.b64encode((SCRATCH / "assets" / "sr-logo-header.png").read_bytes()).decode("ascii")

HTML_TEMPLATE = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>
@font-face {{ font-family: "Nunito"; font-weight: 300; src: url("fonts/nunito-300.ttf"); }}
@font-face {{ font-family: "Nunito"; font-weight: 400; src: url("fonts/nunito-400.ttf"); }}
@font-face {{ font-family: "Open Sans"; font-weight: 400; src: url("fonts/opensans-400.ttf"); }}
@page {{ size: A4; margin: 0; }}
body {{
  margin: 0;
  width: 595.28pt;
  height: 841.89pt;
  font-family: "Nunito", sans-serif;
  color: #1a1a1a;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}}
img.logo {{ width: 28pt; margin-bottom: 40pt; }}
.revision {{
  font-family: "Open Sans", sans-serif;
  font-weight: 400;
  font-size: 22pt;
  margin-bottom: 8pt;
}}
.created {{ font-size: 11pt; color: #444; }}
</style>
</head>
<body>
<img class="logo" src="data:image/png;base64,{logo_b64}">
<div class="revision">Revision {REVISION}</div>
<div class="created">Erstellt am {CREATED}</div>
</body></html>
"""


def main():
    html_path = SCRATCH / "revision_page.html"
    html_path.write_text(HTML_TEMPLATE, encoding="utf-8")
    HTML(str(html_path), base_url=str(SCRATCH)).write_pdf(str(SCRATCH / "revision_page.pdf"))
    print("revision_page.pdf geschrieben")


if __name__ == "__main__":
    main()
