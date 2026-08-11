# Druck-PDF-Pipeline

Erzeugt aus der MkDocs-Doku eine druckfertige, fahrzeugspezifische
Montage- und Bedienungsanleitung (A4, mit Titelseite, Revisionsseite und
Rückseite).

## Release auslösen

Im GitHub-Repo unter "Actions" → "PDF Export" → "Run workflow". Fahrzeug
auswählen (S50/S51/S70 oder KR51) und Revisionsnummer eingeben (z.B. "04").
Nach dem Lauf liegt die PDF als Anhang am neu erstellten GitHub Release.

Die Revisionsnummer wird bewusst nicht automatisch hochgezählt, sondern
jedes Mal manuell eingetragen -- eine "Revision" ist eine bewusste
Entscheidung, keine Nebenwirkung eines CI-Laufs.

## Lokal testen

```bash
pip install -r ../requirements.txt -r requirements.txt
mkdocs build -d /tmp/site-current   # im Repo-Root ausfuehren
cd print-pipeline
PRINT_VEHICLE=s50-s51-s70 PRINT_REVISION=04 python release.py
```

Ergebnis liegt danach in `print-pipeline/output/`.

## Dateien

- `build_full.py` -- extrahiert Kapitel aus der gebauten MkDocs-Site,
  normalisiert Bildgrößen (inkl. Goldkreis-/Ring-Blasenerkennung), löst
  Tabs auf, wandelt Links in QR-Codes um, baut das Inhaltsverzeichnis.
- `optimize_pagefill.py` -- iterative Seitenfüllstands-Optimierung
  (erzwingt/verwirft Seitenumbrüche vor H3-Überschriften).
- `build_revision_page.py` -- Revisions-/Datumsseite (Umgebungsvariablen
  `PRINT_REVISION`, optional `PRINT_CREATED_DATE`).
- `assemble_final.py` -- hängt Titelseite (`covers/`), Revisionsseite,
  Inhalt und Rückseite zusammen, füllt mit Leerseiten auf ein Vielfaches
  von 4 auf (Druckerei-Vorgabe).
- `release.py` -- Orchestriert die vier Schritte oben und benennt die
  finale Datei `{fahrzeug}-Rev{revision}-{datum}.pdf`.
- `covers/` -- fertig auf A4 zugeschnittene Titel-/Rückseiten-Vorlagen
  (Original von Second Ride Design-Team, 216×303mm mit 3mm
  Beschnittzugabe pro Kante, hier bereits zugeschnitten).

## Neues Fahrzeug hinzufügen

1. In `build_full.py` einen neuen Eintrag im `VEHICLES`-Dict anlegen
   (Kapitel-Pfad der fahrzeugspezifischen MkDocs-Seite + Cover-Dateiname).
2. Zugeschnittene Titelseiten-PDF (A4, siehe oben) nach `covers/` legen.
3. Fahrzeug-Option in `.github/workflows/pdf-export.yml` ergänzen
   (`inputs.vehicle.options`).
