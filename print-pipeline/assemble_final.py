#!/usr/bin/env python3
"""Haengt die fahrzeugspezifische Titelseite vorne und die gemeinsame
Rueckseite hinten an den Inhalt (proto_final.pdf) an. Die Vorlagen in
covers/ liegen bereits fertig auf A4 zugeschnitten im Repo (Original war
216x303mm = Trim + 3mm Beschnittzugabe pro Kante, einmalig zugeschnitten,
siehe covers/README oder Git-Historie)."""
import os
from pathlib import Path

import fitz

SCRATCH = Path(__file__).parent
COVERS = SCRATCH / "covers"

VEHICLE_COVERS = {
    "s50-s51-s70": "cover-s50-s51-s70.pdf",
    "kr51": "cover-kr51.pdf",
}
VEHICLE = os.environ.get("PRINT_VEHICLE", "s50-s51-s70")


def main():
    if VEHICLE not in VEHICLE_COVERS:
        raise SystemExit(f"Unbekanntes PRINT_VEHICLE={VEHICLE!r}, erwartet eines von {sorted(VEHICLE_COVERS)}")

    body = fitz.open(SCRATCH / "proto_final.pdf")
    cover = fitz.open(COVERS / VEHICLE_COVERS[VEHICLE])
    back = fitz.open(COVERS / "back-cover.pdf")
    revision = fitz.open(SCRATCH / "revision_page.pdf")

    # Druckerei-Vorgabe: Gesamtseitenzahl muss ein Vielfaches von 4 sein
    # (..., 56, 60, 64, 68, ...). Passt es nicht, werden Leerseiten VOR der
    # Rueckseite eingefuegt (nie Seiten entfernen).
    total_without_pad = len(cover) + len(revision) + len(body) + len(back)
    pad = (-total_without_pad) % 4
    if pad:
        print(f"{pad} Leerseite(n) vor der Rueckseite eingefuegt, damit die "
              f"Gesamtseitenzahl ({total_without_pad} -> {total_without_pad + pad}) "
              f"ein Vielfaches von 4 ist (Druckerei-Vorgabe).")

    out = fitz.open()
    out.insert_pdf(cover)
    out.insert_pdf(revision)
    out.insert_pdf(body)
    body_rect = body[0].rect
    for _ in range(pad):
        out.new_page(width=body_rect.width, height=body_rect.height)
    out.insert_pdf(back)

    out_path = Path(os.environ.get("PRINT_OUTPUT", str(SCRATCH / "proto_final_with_cover.pdf")))
    out.save(out_path)
    print(f"{len(out)} Seiten total (1 Titel + 1 Revisionsseite + {len(body)} Inhalt + "
          f"{pad} Leerseite(n) + 1 Rueckseite) -> {out_path}")


if __name__ == "__main__":
    main()
