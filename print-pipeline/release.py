#!/usr/bin/env python3
"""Orchestriert einen kompletten PDF-Release-Lauf: MkDocs-Site muss bereits
gebaut sein (siehe README.md / GitHub-Actions-Workflow), dann:

  build_full.py         -> article_full.html (Fahrzeugkapitel + gemeinsame Kapitel)
  optimize_pagefill.py  -> article_final.html (Seitenfuellstands-Optimierung)
  build_revision_page.py -> revision_page.pdf
  (wrapper_final.html zusammenbauen, mit WeasyPrint zu proto_final.pdf rendern)
  assemble_final.py     -> Titel + Revision + Inhalt + Leerseiten + Rueckseite

Eingaben ausschliesslich ueber Umgebungsvariablen (so setzt sie der GitHub-
Actions-Workflow direkt aus den workflow_dispatch-Inputs):
  PRINT_VEHICLE       "s50-s51-s70" oder "kr51" (Default: s50-s51-s70)
  PRINT_REVISION      z.B. "04" (Default: "00" -- sollte immer explizit gesetzt werden)
  PRINT_CREATED_DATE  optional, ISO-Datum (Default: heutiges Datum)
  PRINT_SITE_DIR      wo `mkdocs build` abgelegt hat (Default: /tmp/site-current)
"""
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

SCRATCH = Path(__file__).parent
VEHICLE = os.environ.get("PRINT_VEHICLE", "s50-s51-s70")
REVISION = os.environ.get("PRINT_REVISION", "00")


def run(script):
    print(f"\n=== {script} ===")
    subprocess.run([sys.executable, str(SCRATCH / script)], check=True, cwd=SCRATCH)


def build_wrapper_final():
    wrapper = (SCRATCH / "wrapper.html").read_text(encoding="utf-8")
    body_start = wrapper.find("<body>") + len("<body>")
    head = wrapper[:body_start]
    article = (SCRATCH / "article_final.html").read_text(encoding="utf-8")
    (SCRATCH / "wrapper_final.html").write_text(
        head + "\n" + article + "\n</body></html>", encoding="utf-8"
    )


def render_body_pdf():
    from weasyprint import HTML
    HTML(str(SCRATCH / "wrapper_final.html")).write_pdf(str(SCRATCH / "proto_final.pdf"))


def main():
    run("build_full.py")
    run("optimize_pagefill.py")
    build_wrapper_final()
    print("\n=== WeasyPrint: proto_final.pdf ===")
    render_body_pdf()
    run("build_revision_page.py")
    run("assemble_final.py")

    date_str = os.environ.get("PRINT_CREATED_DATE", datetime.now().date().isoformat())
    out_dir = SCRATCH / "output"
    out_dir.mkdir(exist_ok=True)
    final_name = f"{VEHICLE}-Rev{REVISION}-{date_str}.pdf"
    final_path = out_dir / final_name
    (SCRATCH / "proto_final_with_cover.pdf").replace(final_path)
    print(f"\nFertig: {final_path}")


if __name__ == "__main__":
    main()
