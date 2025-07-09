# SecondRide Documentation

This repository contains the official documentation for SecondRide.

## Live Documentation

Visit our live documentation at: **https://docs.second-ride.de**

## Dokumentation bearbeiten (für Nicht-Techniker)

### Ordnerstruktur verstehen

**Wichtig:** Jeder Ordner benötigt eine `index.md` Datei, damit die Navigation funktioniert.

```
docs/
├── index.md                    # Startseite
├── faq/
│   └── index.md               # FAQ-Hauptseite
├── Umbauanleitung/
│   ├── index.md               # Übersichtsseite für alle Anleitungen
│   └── SR24/
│       ├── index.md           # Übersichtsseite für SR24
│       ├── s50-s51/
│       │   └── index.md       # S50/S51 Anleitung
│       ├── schwalbe/
│       │   └── index.md       # Schwalbe Anleitung
│       └── duo/
│           └── index.md       # Duo Anleitung
└── ...
```

### Neue Seite hinzufügen

**Schritt 1: Ordner erstellen**
- Erstelle einen neuen Ordner mit einem aussagekräftigen Namen (nur Kleinbuchstaben, Bindestriche statt Leerzeichen)
- Beispiel: `s75-anleitung` für eine S75 Anleitung

**Schritt 2: index.md Datei erstellen**
- In dem neuen Ordner muss eine Datei namens `index.md` erstellt werden
- Diese Datei enthält den Inhalt der Seite

**Schritt 3: Navigation aktualisieren**
- Öffne die Datei `mkdocs.yml`
- Füge deine neue Seite in den `nav:` Bereich ein:

```yaml
nav:
    - Home: index.md
    - Umbauanleitung:
        - SR24:
            - S75: Umbauanleitung/SR24/s75-anleitung/index.md  # Neue Zeile
```

### Markdown Dateien bearbeiten

**Was ist eine .md Datei?**
- Markdown ist eine einfache Formatierungssprache
- Text wird mit einfachen Zeichen formatiert

**Grundlegende Formatierung:**
```markdown
# Große Überschrift
## Mittlere Überschrift  
### Kleine Überschrift

**Fett gedruckter Text**
*Kursiver Text*

- Aufzählungspunkt 1
- Aufzählungspunkt 2

[Link Text](https://example.com)

![Bild](pfad/zum/bild.jpg)
```

### Bilder hinzufügen

1. **Ordner erstellen:** Erstelle einen `images` Ordner im gleichen Verzeichnis wie deine `index.md`
2. **Bild hochladen:** Lade dein Bild in diesen `images` Ordner
3. **Bild einbinden:** Verwende in der Markdown-Datei:
   ```markdown
   ![Schritt 1](images/schritt1.jpg)
   ```

**Beispiel-Struktur:**
```
Umbauanleitung/SR24/s50-s51/
├── index.md
└── images/
    ├── schritt1.jpg
    ├── schritt2.jpg
    └── overview.png
```

### Navigation-Regeln

**✅ Richtig:**
- Ordnername: `s50-anleitung` (Kleinbuchstaben, Bindestriche)
- Datei: `index.md` (immer dieser Name)
- Navigation: `- S50: Umbauanleitung/SR24/s50-anleitung/index.md`

**❌ Falsch:**
- Ordnername: `S50 Anleitung` (Großbuchstaben, Leerzeichen)
- Datei: `S50_Anleitung.md` (anderer Name als index.md)
- Navigation ohne `index.md`

### Änderungen testen

Nach dem Bearbeiten:
1. Gehe zu https://docs.second-ride.de
2. Überprüfe, ob deine Änderungen sichtbar sind
3. Teste alle Links in der Navigation

### Häufige Probleme

**Problem:** Link funktioniert nicht
**Lösung:** Überprüfe, ob die `index.md` Datei im richtigen Ordner liegt

**Problem:** Seite wird nicht in der Navigation angezeigt
**Lösung:** Überprüfe die `mkdocs.yml` Datei - ist deine Seite dort eingetragen?

**Problem:** Bild wird nicht angezeigt
**Lösung:** Überprüfe den Pfad zum Bild (relativ zum Ordner der Markdown-Datei)

## Local Development (für Entwickler)

### Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Development Server
```bash
mkdocs serve
```
Opens at: http://localhost:8000

### Build Static Site
```bash
mkdocs build
```
Generates static files in `site/` directory.

## Support

For questions about SecondRide or this documentation:
- Browse the [FAQ section](https://docs.second-ride.de/faq/)
- Contact support through the SecondRide platform
