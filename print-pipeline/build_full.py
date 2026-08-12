#!/usr/bin/env python3
"""Assemble the full print document: vehicle montage chapter (heading_shift -1)
plus the shared chapters from chapters-common.yml (heading_shift 0), matching
manifest.yml / chapters-common.yml order. One pass: extract, shift headings,
resolve image paths to absolute, rebalance checklists, wrap compact chapters,
size every image (gold-circle bubble detection), build the TOC."""
import base64
import io
import os
import re
import urllib.request
from collections import deque
from pathlib import Path
from urllib.parse import urljoin

import numpy as np
import segno
from PIL import Image, ImageFilter

SITE = Path(os.environ.get("PRINT_SITE_DIR", "/tmp/site-current"))
SCRATCH = Path(__file__).parent

# Fahrzeugspezifisches erstes Kapitel + passende Titelseite (siehe
# print-pipeline/covers/). Ueber PRINT_VEHICLE steuerbar (release.py /
# GitHub-Actions-Input) -- neues Fahrzeug = neuer Eintrag hier, sobald die
# MkDocs-Quellseite dafuer existiert (AIY z.B. hat noch keine).
VEHICLES = {
    "s50-s51-s70": {
        "chapter": ("conversion-manual/MID50/02-s50-s51-s70", -1, None),
        "cover": "cover-s50-s51-s70.pdf",
        "label": "S50/S51/S70",
    },
    "kr51": {
        "chapter": ("conversion-manual/MID50/01-schwalbe", -1, None),
        "cover": "cover-kr51.pdf",
        "label": "KR51",
    },
}
VEHICLE = os.environ.get("PRINT_VEHICLE", "s50-s51-s70")
if VEHICLE not in VEHICLES:
    raise SystemExit(f"Unbekanntes PRINT_VEHICLE={VEHICLE!r}, erwartet eines von {sorted(VEHICLES)}")

CHAPTERS = [
    VEHICLES[VEHICLE]["chapter"],
    ("conversion-manual/MID50/throttling/how-to-throttle-your-drive", 0, "Digitale Drosselung"),
    ("conversion-manual/modification-approval-and-homologation", 0, "Zulassung & Abnahme"),
    ("user-manual/MID50/01-bedienung", 0, "Bedienung"),
    ("user-manual/MID50/02-firmware-update", 0, None),
    ("user-manual/MID50/03-fehlerbehebung", 0, None),
    ("user-manual/MID50/04-warnhinweise", 0, None),
]
COMPACT_CHAPTERS = {"kleingeschriebenes"}

# -- image sizing constants (rules.py) ------------------------------------
IMAGE_SCALE = 1.4
MIN_PRINT_DPI = 150.0
CONTENT_WIDTH_PT = 451.28
BASE_IMAGE_WIDTH_PT = 236.22
TARGET_CIRCLE_PT = 22.0  # Nutzer-Feedback: Blasenbilder noch etwas groesser (vorher 20.08)
BUBBLE_WIDTH_MIN_PT = 141.7
# War 362.2 (~= CONTENT_WIDTH_PT*BUBBLE_SIZE_FACTOR, s.u.) -- das lag so nah am
# ohnehin schon vorhandenen Sicherheitsdeckel in print_width_pt(), dass auch
# LEGITIME Treffer mit etwas kleinerem Blasenanteil (z.B. die 01-schwalbe
# CAD-Renderbilder mit viel weissem Rand um das Bauteil) ueber die Grenze
# rutschten und komplett verworfen wurden, statt einfach vom bestehenden
# Deckel auf die gleiche Maximalgroesse gebracht zu werden. 650pt laesst
# echte Blasenbilder durch (der Deckel unten begrenzt die Druckgroesse
# ohnehin), faengt aber weiterhin Ausreisser durch Fehlerkennungen ab.
BUBBLE_WIDTH_MAX_PT = 650.0
ICON_LEGEND_WIDTH_PT = 19.5 * 2.0
PICTOGRAM_WIDTH_PT = 28.5
PICTOGRAM_PAGES = {"user-manual/MID50/04-warnhinweise"}
QR_WIDTH_PT = 90.0
GOLD_MASK = dict(r_min=170, g_lo=120, g_hi=210, b_max=90)
MORPH_RADIUS = 6

_remote_cache = {}
img_log = []


# Nutzer-Feedback: normale Fliesstextfotos wirkten zu gross (2/3 Reduktion),
# Blasenbilder sollen aber gerade NICHT mitgeschrumpft werden -- die richten
# sich ausschliesslich nach der Blasengroesse (TARGET_CIRCLE_PT oben).
PHOTO_SIZE_FACTOR = 2 / 3
BUBBLE_SIZE_FACTOR = 0.8


def print_width_pt(base_pt, source_px, factor):
    by_resolution = source_px * 72.0 / MIN_PRINT_DPI
    return round(min(base_pt * IMAGE_SCALE, by_resolution, CONTENT_WIDTH_PT) * factor, 2)


def blob_diameters(mask, w, h, radius):
    visited = np.zeros(mask.shape, dtype=bool)
    out = []
    ys, xs = np.nonzero(mask)
    limit_lo, limit_hi = 0.03 * min(h, w), 0.20 * min(h, w)
    for y0, x0 in zip(ys, xs):
        if visited[y0, x0]:
            continue
        stack = [(y0, x0)]
        visited[y0, x0] = True
        min_y = max_y = y0
        min_x = max_x = x0
        area = 0
        while stack:
            y, x = stack.pop()
            area += 1
            min_y, max_y = min(min_y, y), max(max_y, y)
            min_x, max_x = min(min_x, x), max(max_x, x)
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny, nx = y + dy, x + dx
                if 0 <= ny < mask.shape[0] and 0 <= nx < mask.shape[1] \
                        and mask[ny, nx] and not visited[ny, nx]:
                    visited[ny, nx] = True
                    stack.append((ny, nx))
        bw, bh = max_x - min_x + 1, max_y - min_y + 1
        if bw < 10 or bh < 10:
            continue
        if not 0.7 < bw / bh < 1.4:
            continue
        if area / (bw * bh) <= 0.6:
            continue
        d = (bw + bh) / 2 + 2 * radius
        if limit_lo <= d <= limit_hi:
            out.append(d)
    return out


LINE_STRIP_RADIUS = 10


def circle_width_pt(img):
    w, h = img.size
    if w < 200 or h < 200:
        return None
    rgb = img.convert("RGB")
    arr = np.asarray(rgb, dtype=np.int16)
    r, g, b = arr[..., 0], arr[..., 1], arr[..., 2]
    mask = ((r > GOLD_MASK["r_min"]) & (g > GOLD_MASK["g_lo"])
            & (g < GOLD_MASK["g_hi"]) & (b < GOLD_MASK["b_max"]))
    if mask.sum() < 50:
        return None
    m = Image.fromarray((mask * 255).astype("uint8"))
    k = 2 * MORPH_RADIUS + 1
    closed = m.filter(ImageFilter.MaxFilter(k)).filter(ImageFilter.MinFilter(k)) \
              .filter(ImageFilter.MinFilter(k))
    diameters = blob_diameters(np.asarray(closed) > 127, w, h, MORPH_RADIUS)
    if not diameters:
        # Zeiger-/Leitlinien in derselben Goldfarbe wie der Kreis verschmelzen
        # beim einfachen closing zu einer nicht-runden Flaeche, sobald sie den
        # Kreis beruehren (z.B. akkuherzkasten-vorbereiten-1.png: Kreis "1"
        # mit 3 anliegenden Linien -- ein Blob, Seitenverhaeltnis 1.7, faellt
        # durch den Rundheitsfilter). Ein "opening" (erode+dilate) VOR dem
        # closing entfernt die duennen Linien vollstaendig, laesst den
        # deutlich dickeren Kreis aber unangetastet.
        ko = 2 * LINE_STRIP_RADIUS + 1
        opened = m.filter(ImageFilter.MinFilter(ko)).filter(ImageFilter.MaxFilter(ko))
        diameters = blob_diameters(np.asarray(opened) > 127, w, h, MORPH_RADIUS)
    if not diameters:
        return None
    # Ein einzelner, sauber runder Treffer (Seitenverhaeltnis + Fuellgrad
    # bereits streng gefiltert in blob_diameters) reicht als Beleg -- viele
    # Fotos zeigen nur eine einzige Blase; vorher noetige >=2 Treffer haben
    # genau diese Bilder systematisch auf die generische Fliesstext-Groesse
    # zurueckfallen lassen, statt sie an der Blasengroesse auszurichten.
    diameters.sort()
    median = diameters[len(diameters) // 2]
    if median <= 0:
        return None
    want = TARGET_CIRCLE_PT * w / median
    return want if BUBBLE_WIDTH_MIN_PT <= want <= BUBBLE_WIDTH_MAX_PT else None


def enclosed_light_mask(light):
    """Flutet die 'hell' markierten Pixel vom Bildrand aus (BFS) und liefert
    zurueck, was danach hell aber NICHT erreicht ist -- also von einer
    dunklen Umrandung eingeschlossen. Findet das weisse Innere eines
    schwarz umrandeten Nummernkreises, selbst wenn die Blase am Bildrand
    im ebenfalls weissen Foto-Hintergrund sitzt (die Umrandung trennt die
    beiden Flaechen in der Maske, auch wenn sie farblich identisch sind)."""
    h, w = light.shape
    reached = np.zeros_like(light, dtype=bool)
    dq = deque()
    for x in range(w):
        for y in (0, h - 1):
            if light[y, x] and not reached[y, x]:
                reached[y, x] = True
                dq.append((y, x))
    for y in range(h):
        for x in (0, w - 1):
            if light[y, x] and not reached[y, x]:
                reached[y, x] = True
                dq.append((y, x))
    while dq:
        y, x = dq.popleft()
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and light[ny, nx] and not reached[ny, nx]:
                reached[ny, nx] = True
                dq.append((ny, nx))
    return light & ~reached


def ring_circle_width_pt(img):
    """Zweiter Blasenstil neben der goldgefuellten Variante: weisser Kreis
    mit duenner schwarzer Umrandung und schwarzer Ziffer, wie in den
    01-schwalbe-CAD-Renderbildern verwendet (Antriebsmodul-Montage). Die
    Goldfarbmaskierung findet hier nichts, da kein Gold vorkommt --
    stattdessen: helle Flaechen suchen, die von einer dunklen Umrandung
    eingeschlossen sind. Stichprobenartig gegen mehrere garantiert
    blasenfreie Fotos (u.a. Metallreflexe, glaenzende Schrauben) getestet --
    keine Fehltreffer, deshalb genuegt wie beim Gold-Pfad ein einzelner
    sauber runder Treffer (Seitenverhaeltnis + Fuellgrad bereits streng
    gefiltert in blob_diameters)."""
    w, h = img.size
    if w < 200 or h < 200:
        return None
    rgb = img.convert("RGB")
    arr = np.asarray(rgb, dtype=np.int16)
    r, g, b = arr[..., 0], arr[..., 1], arr[..., 2]
    light = (r > 235) & (g > 235) & (b > 235)
    if light.sum() < 200:
        return None
    enclosed = enclosed_light_mask(light)
    diameters = blob_diameters(enclosed, w, h, 0)
    if not diameters:
        return None
    diameters.sort()
    median = diameters[len(diameters) // 2]
    if median <= 0:
        return None
    want = TARGET_CIRCLE_PT * w / median
    return want if BUBBLE_WIDTH_MIN_PT <= want <= BUBBLE_WIDTH_MAX_PT else None


def open_image(url):
    if url.startswith("file://"):
        path = Path(url[len("file://"):])
        return Image.open(path) if path.exists() else None
    if url in _remote_cache:
        return Image.open(io.BytesIO(_remote_cache[url]))
    req = urllib.request.Request(url, headers={"User-Agent": "secondride-print-proto"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = resp.read()
    _remote_cache[url] = data
    return Image.open(io.BytesIO(data))


IMG_RE = re.compile(r'<img\b([^>]*?)\bsrc="([^"]+)"([^>]*)>')


def qr_figure(url, caption):
    qr = segno.make(url, error="m")
    buf = io.BytesIO()
    qr.save(buf, kind="png", scale=8, border=2, dark="000000")
    b64 = base64.b64encode(buf.getvalue()).decode("ascii")
    return (
        '<p style="text-align:center; break-inside:avoid;">'
        f'<img data-role="qr" src="data:image/png;base64,{b64}" '
        f'style="width:{QR_WIDTH_PT}pt; margin:4pt auto 0 auto;">'
        f'<span class="caption">{caption}</span></p>'
    )


DIV_TAG_RE = re.compile(r'<div\b[^>]*>|</div>')


def find_matching_div_end(text, start):
    """start zeigt auf ein '<div ...>'; liefert den Index direkt hinter dem
    dazu passenden '</div>' (Tiefen-Zaehlung, verschachtelte divs erlaubt)."""
    depth = 0
    pos = start
    while True:
        m = DIV_TAG_RE.search(text, pos)
        if not m:
            return None
        if m.group(0) == "</div>":
            depth -= 1
            if depth == 0:
                return m.end()
        else:
            depth += 1
        pos = m.end()


TABBED_SET_OPEN_RE = re.compile(r'<div class="tabbed-set[^"]*"[^>]*>')
TABBED_BLOCK_OPEN_RE = re.compile(r'<div class="tabbed-block"[^>]*>')
LABEL_RE = re.compile(r'<label\b[^>]*>(.*?)</label>', re.S)
RADIO_INPUT_RE = re.compile(r'<input\b[^>]*\btype="radio"[^>]*>')


TEILEGUTACHTEN_H3_RE = re.compile(r'<h3 id="teilegutachten">.*?</h3>\s*')


def remove_teilegutachten(text):
    """Teilegutachten MID50 + SR24 sollen nicht im Druck erscheinen
    (Nutzer-Feedback) -- ganzer Abschnitt inkl. Ueberschrift raus, da beide
    Tabs die einzigen Inhalte darunter waren."""
    m = TEILEGUTACHTEN_H3_RE.search(text)
    if not m:
        return text
    tab_m = TABBED_SET_OPEN_RE.match(text, m.end())
    if not tab_m:
        return text
    end = find_matching_div_end(text, tab_m.start())
    if end is None:
        return text
    return text[:m.start()] + text[end:]


def linearize_tabs(text):
    """pymdownx.tabbed wird zu einer einfachen Abfolge aus <h4>Tab-Titel</h4>
    + Tab-Inhalt -- Tabs sind eine Web-Interaktion, fuer den Druck gibt es
    ohnehin nur Papier in einer Reihenfolge. Ohne das bleiben die Radio-Buttons
    und Tab-Label als kaputt aussehender Text im PDF stehen."""
    while True:
        m = TABBED_SET_OPEN_RE.search(text)
        if not m:
            break
        end = find_matching_div_end(text, m.start())
        block = text[m.start():end]
        labels = [re.sub("<[^>]+>", "", l).strip() for l in LABEL_RE.findall(block)]

        contents = []
        pos = 0
        while True:
            bm = TABBED_BLOCK_OPEN_RE.search(block, pos)
            if not bm:
                break
            bend = find_matching_div_end(block, bm.start())
            contents.append(block[bm.end():bend - len("</div>")])
            pos = bend

        pieces = [f"<h4>{label}</h4>{content}" for label, content in zip(labels, contents)]
        text = text[:m.start()] + "".join(pieces) + text[end:]
    return RADIO_INPUT_RE.sub("", text)


EMOJI_TO_DOT = {
    "\U0001F7E2": "#3ba55d",   # gruen
    "\U0001F534": "#d13438",   # rot
    "\U0001F7E1": "#e4b854",   # gelb
    "\U0001F7E3": "#8b5cf6",   # violett
    "⚫": "#2f2f2f",       # schwarz
}


def replace_status_emoji(text):
    """Status-Emoji sind nicht farbecht/nicht einheitlich in ihrer Metrik --
    werden zu farbigen Punkten im Fliesstext (FORMAT-RULES.md Abschnitt 9)."""
    for emoji, color in EMOJI_TO_DOT.items():
        text = text.replace(emoji, f'<span style="color:{color};">●</span>')
    return text


P_SPAN_RE = re.compile(r'<p\b[^>]*>.*?</p>', re.S)


def glue_text_to_image(text):
    """break-after:avoid auf dem Text vor einem Bild ist nur ein Hinweis --
    passt Text+Bild nicht mehr auf die Seite, wird das trotzdem getrennt und
    das Bild haengt allein auf der naechsten Seite (siehe Riemenwechsel).
    Hartes break-inside:avoid auf einem gemeinsamen Wrapper erzwingt es."""
    spans = [(m.start(), m.end(), "<img" in m.group(0)) for m in P_SPAN_RE.finditer(text)]
    wraps = []
    i = 0
    while i < len(spans) - 1:
        s1, e1, img1 = spans[i]
        s2, e2, img2 = spans[i + 1]
        if not img1 and img2 and text[e1:s2].strip() == "":
            wraps.append((s1, e2))
            i += 2  # keine Bilderkette: das naechste Bild bekommt keinen neuen Partner
        else:
            i += 1
    for s, e in sorted(wraps, reverse=True):
        text = text[:s] + '<div class="keep-together">' + text[s:e] + "</div>" + text[e:]
    return text


def glue_image_pairs(text):
    """Genau zwei aufeinanderfolgende reine Bild-Absaetze (kein Fliesstext
    dazwischen) werden zusammengehalten -- typischerweise ein Vorher/
    Nachher-Bildpaar wie griff-ummontieren-demontage + -position, das sonst
    auf zwei fast leere Seiten auseinanderreisst. Laengere Bildserien (3+,
    z.B. Einbau in den Rahmen) werden bewusst NICHT geglued: zusammen
    passen sie oft auf keine einzelne Seite mehr und stranden dann
    schlimmer, als die Trennung es tut (dieselbe Lektion wie bei
    Ueberschrift+grosser Tabelle in glue_headings).

    Bild 1 haengt oft schon am Ende eines bestehenden keep-together-Divs
    (glue_text_to_image hat es mit dem Text davor verklebt). Das einfach
    bis nach Bild 2 zu verlaengern haette dann [Text+Bild1+Bild2] gemeinsam
    zu halten -- gemessen (Beispiel griff-ummontieren-demontage+-position)
    passt das oft nur um weniger als 1pt NICHT auf eine volle Seite, direkt
    an der Kante des Fragmentierungsbudgets, und WeasyPrint gibt dann
    komplett auf und trennt trotz break-inside:avoid genau zwischen den
    Bildern. Deshalb wird der bestehende Text-Div-Anteil in diesem Fall
    stattdessen VERKUERZT (schliesst schon vor Bild 1) und [Bild1+Bild2]
    allein in ein neues Div gepackt -- das hat spuerbar mehr Luft (die
    Bilder alleine sind ca. 60pt kuerzer als mit dem Absatz zusammen) und
    reisst im schlimmsten Fall nur den Text vom ersten Bild, nie die
    beiden Bilder voneinander."""
    DIV_CLOSE = "</div>"
    DIV_OPEN = '<div class="keep-together">'
    spans = [(m.start(), m.end(), "<img" in m.group(0)) for m in P_SPAN_RE.finditer(text)]
    two_runs = []
    i = 0
    while i < len(spans):
        if not spans[i][2]:
            i += 1
            continue
        j = i
        while (j + 1 < len(spans) and spans[j + 1][2]
               and text[spans[j][1]:spans[j + 1][0]].replace(DIV_CLOSE, "").strip() == ""):
            j += 1
        if j == i + 1:  # genau 2 Bilder in Folge
            two_runs.append((spans[i][0], spans[i][1], spans[j][1]))
        i = j + 1

    edits = []  # (position, zu entfernende Laenge, einzufuegender Text)
    for wrap_start, img1_end, img2_end in two_runs:
        m = re.match(r"\s*" + DIV_CLOSE, text[img1_end:img1_end + 40])
        open_insert = DIV_OPEN
        if m:
            # Bestehendes Div (Text+Bild1) verkuerzen: schliesst jetzt schon
            # vor Bild 1 statt danach, das neue Div faengt an derselben
            # Stelle direkt wieder an -- beides in EINEM String, sonst ist
            # die Reihenfolge zweier Einfuegungen an derselben Position
            # nicht garantiert.
            close_pos = img1_end + m.end() - len(DIV_CLOSE)
            edits.append((close_pos, len(DIV_CLOSE), ""))
            open_insert = DIV_CLOSE + DIV_OPEN
        edits.append((wrap_start, 0, open_insert))
        edits.append((img2_end, 0, DIV_CLOSE))

    for pos, rm_len, insert in sorted(edits, key=lambda e: e[0], reverse=True):
        text = text[:pos] + insert + text[pos + rm_len:]
    return text


IFRAME_RE = re.compile(r'<iframe\b[^>]*\bsrc="([^"]+)"[^>]*>.*?</iframe>', re.S)
YOUTUBE_RE = re.compile(r'youtube\.com/embed/([\w-]+)')


def replace_video_iframes(text):
    def repl(m):
        src = m.group(1)
        yt = YOUTUBE_RE.search(src)
        if yt:
            url = f"https://youtu.be/{yt.group(1)}"
            return qr_figure(url, f"Video ansehen: {url}")
        if "google.com/maps" in src:
            # Embed-URL taugt nicht als scanbarer Link -- auf die normale Maps-Startseite verweisen.
            return qr_figure("https://www.google.com/maps/d/u/0/viewer?mid=1CDf_Qp0kNb1LnjTww2guJW_Abqq2x08",
                              "Karte ansehen: second-ride.de (siehe Discord/Website)")
        if src.startswith("file://") and src.endswith(".pdf"):
            name = Path(src).name
            return f'<p><em>[Dokument "{name}" -- als separate Anlage beilegen, nicht eingebettet]</em></p>'
        return m.group(0)

    return IFRAME_RE.sub(repl, text)


# -- generische Link-zu-QR-Konvertierung ------------------------------------
# Ein anklickbarer Link ist in einer gedruckten Anleitung tote Tinte -- die
# Funktion ersetzt jeden echten Link im Fliesstext durch reinen (fett
# gesetzten) Text und haengt den QR-Code direkt hinter den Absatz, der den
# Link enthielt -- an der Stelle des Links, nicht gesammelt in einem Anhang.
# Wird generisch auf das gesamte Dokument angewendet, nicht nur auf einzelne
# Kapitel.
LINK_RE = re.compile(r'<a\b([^>]*?)\bhref="([^"]+)"([^>]*)>(.*?)</a>', re.S)
NEARBY_QR_IMG_RE = re.compile(r'<img\b[^>]*src="[^"]*/qr[-_][^"]*"', re.I)
PARA_END_RE = re.compile(r'</p>', re.I)
QR_LOOKAHEAD_MAX_CHARS = 400


def internal_chapter_urls():
    """file://-Basis-URLs aller eigenen Kapitel (siehe extract_chapter) --
    ein Link, der auf eine dieser Seiten zeigt, verweist auf ein Kapitel,
    das im gedruckten Dokument bereits enthalten ist. Dafuer braucht es
    keinen QR-Code, nur den Kapitelnamen im Fliesstext."""
    return {f"file://{SITE / rel_path}/" for rel_path, _, _ in CHAPTERS}


def check_link_reachable(url):
    """Bestmoegliche Erreichbarkeitspruefung beim Bauen -- rein informativ
    fuers Build-Log, taucht nicht im gedruckten Dokument auf und ein
    Netzwerkfehler bricht den PDF-Build nie ab."""
    if url.startswith("file://"):
        return Path(url[len("file://"):]).exists()
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method,
                                          headers={"User-Agent": "secondride-print-proto"})
            with urllib.request.urlopen(req, timeout=6) as resp:
                if 200 <= resp.status < 400:
                    return True
        except Exception:
            continue
    return False


def qrify_links(text):
    internal = internal_chapter_urls()
    out = []
    pos = 0
    pending = []  # (href, label), noch nicht ausgegebene QR-Codes fuer den
                  # gerade zu Ende gehenden Absatz

    def flush(segment):
        """Haengt anstehende QR-Codes direkt hinter das erste '</p>' in
        diesem (unveraenderten) Textabschnitt -- also ans Ende des Absatzes,
        der den zuletzt gefundenen Link enthielt. Kein '</p>' hier drin?
        Dann ist der Absatz noch nicht zu Ende, die QR-Codes bleiben
        anstehend, bis ein spaeterer Abschnitt tatsaechlich schliesst."""
        nonlocal pending
        if not pending:
            return segment
        m = PARA_END_RE.search(segment)
        if not m:
            return segment
        cut = m.end()
        qr_html = "".join(
            qr_figure(href, f"{label} &ndash; {href if href.startswith('http') else Path(href).name}")
            for href, label in pending
        )
        pending = []
        return segment[:cut] + qr_html + segment[cut:]

    for m in LINK_RE.finditer(text):
        out.append(flush(text[pos:m.start()]))
        pos = m.end()
        href, inner = m.group(2), m.group(4)
        plain_label = re.sub(r'<[^>]+>', '', inner).strip()
        if href.startswith(("#", "mailto:")):
            out.append(m.group(0))
            continue
        if not plain_label:
            # Bildlink ohne eigenen Text (z.B. glightbox-Zoom-Wrapper um ein
            # bereits sichtbares Foto) -- kein eigenstaendiger Klicklink.
            out.append(m.group(0))
            continue
        if href.rstrip("/") + "/" in internal or href in internal:
            # Querverweis auf ein anderes Kapitel desselben gedruckten
            # Dokuments -- schon enthalten, kein QR-Code noetig.
            out.append(f"<strong>{plain_label}</strong>")
            continue
        # "In der Naehe" heisst: eigener Absatz plus der unmittelbar
        # folgende (das manuell gepflegte QR-Bild steht im Quelltext direkt
        # als eigener naechster Absatz nach dem Link, siehe
        # 02-firmware-update: Link-<p> gefolgt von QR-Bild-<p>). Ein fester
        # Zeichen-Deckel begrenzt das zusaetzlich, damit ein QR-Bild in
        # einem VOELLIG anderen, spaeteren Absatz nicht faelschlich einen
        # frueheren, unabhaengigen Link mit abdeckt.
        para_ends = list(PARA_END_RE.finditer(text, m.end(), m.end() + QR_LOOKAHEAD_MAX_CHARS))
        lookahead_end = para_ends[1].end() if len(para_ends) >= 2 else m.end() + QR_LOOKAHEAD_MAX_CHARS
        if NEARBY_QR_IMG_RE.search(text, m.end(), lookahead_end):
            # Direkt daneben steht schon ein manuell gepflegter QR-Code fuer
            # denselben Zweck (z.B. update.second-ride.de) -- kein zweiter noetig.
            out.append(m.group(0))
            continue
        print(f"  Link {'OK' if check_link_reachable(href) else 'NICHT ERREICHBAR'}: {href}")
        out.append(f"<strong>{plain_label}</strong>")
        pending.append((href, plain_label))
    out.append(flush(text[pos:]))
    return "".join(out)


def size_image(m):
    pre, src, post = m.group(1), m.group(2), m.group(3)
    attrs_raw = pre + post
    if 'data-role="qr"' in attrs_raw or src.startswith("assets/"):
        return m.group(0)
    if 'data-role="pictogram"' in attrs_raw:
        img_log.append(f"{'Piktogramm':11} {PICTOGRAM_WIDTH_PT:6.1f}pt  {src}")
        attrs = re.sub(r'\bwidth="[^"]*"|\bheight="[^"]*"|\bdata-role="[^"]*"', "", attrs_raw)
        return f'<img{attrs} src="{src}" style="width:{PICTOGRAM_WIDTH_PT}pt">'
    if 'width="50"' in attrs_raw:
        img_log.append(f"{'Warnzeichen':11} {ICON_LEGEND_WIDTH_PT:6.1f}pt  (Legende)  {src}")
        attrs = re.sub(r'\bwidth="[^"]*"', "", attrs_raw)
        return f'<img{attrs} src="{src}" style="width:{ICON_LEGEND_WIDTH_PT}pt">'
    if re.search(r'/qr[-_]', src, re.I):
        # Bereits vorhandene QR-Codes aus der Quelle (nicht die selbst erzeugten
        # Video-QR-Codes) sollen dieselbe feste Groesse haben, nicht die
        # Fliesstext-Formel -- sonst sind sie im Dokument uneinheitlich gross.
        img_log.append(f"{'QR (Quelle)':11} {QR_WIDTH_PT:6.1f}pt  {src}")
        attrs = re.sub(r'\bwidth="[^"]*"', "", attrs_raw)
        return f'<img{attrs} src="{src}" style="width:{QR_WIDTH_PT}pt">'
    img = open_image(src)
    if img is None:
        img_log.append(f"NICHT GEFUNDEN: {src}")
        return m.group(0)
    px_w, _ = img.size
    bubble = circle_width_pt(img) or ring_circle_width_pt(img)
    base = bubble if bubble else BASE_IMAGE_WIDTH_PT
    factor = BUBBLE_SIZE_FACTOR if bubble else PHOTO_SIZE_FACTOR
    width_pt = print_width_pt(base, px_w, factor)
    kind = "Blasenbild" if bubble else "Fliesstext"
    img_log.append(f"{kind:11} {width_pt:6.1f}pt  ({px_w}px)  {src}")
    attrs = re.sub(r'\bwidth="[^"]*"', "", pre + post)
    return f'<img{attrs} src="{src}" style="width:{width_pt}pt">'


# -- per-chapter extraction -------------------------------------------------
ARTICLE_RE = re.compile(r'<article class="md-content__inner[^"]*">(.*?)</article>', re.S)
BUTTON_RE = re.compile(r'<a[^>]*class="md-content__button[^>]*>.*?</a>', re.S)
SRC_ATTR_RE = re.compile(r'\b(src|href)="([^"]+)"')


def resolve_paths(html, page_url):
    def repl(m):
        attr, val = m.group(1), m.group(2)
        if val.startswith(("http://", "https://", "#", "mailto:")):
            return m.group(0)
        return f'{attr}="{urljoin(page_url, val)}"'
    return SRC_ATTR_RE.sub(repl, html)


def extract_chapter(rel_path, shift, title_override):
    html = (SITE / rel_path / "index.html").read_text(encoding="utf-8")
    m = ARTICLE_RE.search(html)
    assert m, f"kein <article> in {rel_path}"
    body = m.group(1)
    body = BUTTON_RE.sub("", body)
    body = re.sub(r'<h1[^>]*id="([^"]*)"[^>]*>(.*?)</h1>', r'<h1 id="\1">\2</h1>', body, count=1)

    page_url = f"file://{SITE / rel_path}/"
    body = resolve_paths(body, page_url)

    if title_override:
        body = re.sub(r'(<h1 id="[^"]*">).*?(</h1>)', rf'\1{title_override}\2', body, count=1)

    if rel_path in PICTOGRAM_PAGES:
        body = re.sub(r'<img\b', '<img data-role="pictogram" ', body)

    if shift == -1:
        first_h1 = re.search(r"<h1(\s[^>]*)?>.*?</h1>", body, re.S)
        # Titel der Webseite komplett weglassen -- der Nutzer will keinen
        # eigenen Titel im Dokument, das Deckblatt kommt separat.
        idx = first_h1.start()
        rest = body[first_h1.end():]
        # Hero-Bild direkt danach ebenfalls weglassen.
        hero = re.match(r'\s*<p>\s*<a[^>]*>\s*<img[^>]*>\s*</a>\s*</p>', rest, re.S)
        if hero:
            rest = rest[hero.end():]
        body = body[:idx] + rest
        shift_map = {"2": "1", "3": "2", "4": "3"}
        body = re.sub(r"<(/?)h([234])\b", lambda mm: f"<{mm.group(1)}h{shift_map[mm.group(2)]}", body)
    # shift == 0: heading levels unchanged.

    return body


LI_RE = re.compile(r"<li>.*?</li>", re.S)
TABLE_RE = re.compile(r"<table>\s*<tbody>.*?</tbody>\s*</table>", re.S)


def rebalance_checklists(text):
    def rebalance(m):
        table_html = m.group(0)
        if "checkbox" not in table_html:
            return table_html
        items = LI_RE.findall(table_html)
        if len(items) < 2:
            return table_html
        left_n = -(-len(items) // 2)
        left, right = items[:left_n], items[left_n:]

        def col(items):
            return '<ul style="list-style-type:none; padding-left:0; margin-top:0;">' + "".join(items) + "</ul>"

        return ('<table class="checklist"><tbody><tr>'
                f'<td valign="top">{col(left)}</td><td valign="top">{col(right)}</td>'
                "</tr></tbody></table>")

    return TABLE_RE.sub(rebalance, text)


def wrap_compact(text):
    # Grenze ist ausschliesslich das naechste h1 -- die Kopfzeilen-Vorlage
    # dieses Kapitels selbst steht jetzt DIREKT NACH seiner eigenen h1 (siehe
    # inject_pageheads) und darf hier nicht mehr als Stopp-Marker dienen,
    # sonst wird nur die Ueberschrift, nicht der Kapitelinhalt gestaucht.
    for cid in COMPACT_CHAPTERS:
        m = re.search(rf'<h1 id="{cid}">.*?(?=<h1\b|$)', text, re.S)
        if m:
            text = text[:m.start()] + '<div class="compact">' + m.group(0) + "</div>" + text[m.end():]
    return text


# Eine Ueberschrift, der ohne jeden Fliesstext direkt eine Tabelle oder eine
# kleinere Ueberschrift folgt, darf nie allein am Seitenende landen (break-after:
# avoid alleine reicht nicht zuverlaessig, siehe Akkuherzkasten/Checkliste) --
# beide zusammen in einen break-inside:avoid-Block packen.
#
# Bewusst kein einzelnes Regex-Match ueber Ueberschrift+Folgeelement: ein
# reluctant ".*?</h\\1>" kann bei fehlgeschlagenem Anschluss beliebig weit
# zurueckspringen und dabei voellig unzusammenhaengende Ueberschriften quer
# durchs Dokument verkoppeln. Stattdessen jede Ueberschrift/Tabelle einzeln,
# exakt begrenzt einsammeln und Nachbarschaft in Python pruefen.
HEADING_SPAN_RE = re.compile(r'<h([1-4])\b[^>]*>.*?</h\1>', re.S)
TABLE_SPAN_RE = re.compile(r'<table\b.*?</table>', re.S)
PAGEHEAD_DIV_RE = re.compile(r'<div class="pagehead">.*?</div>', re.S)


def glue_headings(text):
    spans = []
    for m in HEADING_SPAN_RE.finditer(text):
        spans.append((m.start(), m.end(), "h", int(m.group(1))))
    for m in TABLE_SPAN_RE.finditer(text):
        # Grosse Datentabellen (mit <thead>, z.B. die Warnhinweise-Referenz)
        # koennen laenger als eine Seite sein -- werden sie mit der
        # Ueberschrift verklebt, erzwingt break-inside:avoid trotzdem einen
        # Umbruch (weil es unmoeglich ist), und die Ueberschrift landet allein
        # auf einer fast leeren Seite. Nur kompakte Tabellen (Checklisten)
        # eignen sich fuers Verkleben.
        if "<thead" in m.group(0):
            continue
        spans.append((m.start(), m.end(), "t", None))
    spans.sort()

    runs = []
    current = None
    for start, end, kind, level in spans:
        if current is None:
            current = [start, end, level]
            continue
        # Kopfzeilen-Vorlage (jetzt direkt nach jeder h1, siehe inject_pageheads)
        # zaehlt nicht als "richtiger" Inhalt zwischen zwei Elementen.
        gap = PAGEHEAD_DIV_RE.sub("", text[current[1]:start])
        glue_ok = (
            gap.strip() == ""
            and current[2] is not None  # vorheriges Element war eine Ueberschrift
            and (kind == "t" or (kind == "h" and level >= current[2]))
        )
        if glue_ok:
            current[1] = end
            current[2] = level if kind == "h" else None
        else:
            runs.append(tuple(current))
            current = [start, end, level]
    if current:
        runs.append(tuple(current))

    # Nur Laeufe aus mindestens 2 Elementen (Ueberschrift + etwas) sind interessant.
    runs = [(s, e) for s, e, _ in runs if e - s > 0]
    out = []
    last = 0
    for start, end in runs:
        segment = text[start:end]
        if HEADING_SPAN_RE.match(segment) is None:
            continue  # Lauf aus einer einzelnen Tabelle ohne vorausgehende Ueberschrift
        if segment.count("<h1", 0) + segment.count("<h2") + segment.count("<h3") + segment.count("<h4") < 2 \
                and TABLE_SPAN_RE.search(segment) is None:
            continue  # nur eine einzelne Ueberschrift, nichts zum Verkleben
        out.append((start, end))

    result = []
    last = 0
    for start, end in out:
        result.append(text[last:start])
        result.append(f'<div class="keep-together">{text[start:end]}</div>')
        last = end
    result.append(text[last:])
    return "".join(result)


def build_toc(text):
    HEADING_RE = re.compile(r'<h([123])\s+id="([^"]+)">(.*?)</h\1>')
    entries = [(m.group(1), m.group(2), re.sub("<[^>]+>", "", m.group(3)))
               for m in HEADING_RE.finditer(text)]
    toc_pagehead = ('<div class="pagehead"><img src="assets/sr-logo-header.png">'
                     '<span class="name">Inhaltsverzeichnis</span></div>')
    lines = ['<nav class="toc">', "<h1>Inhaltsverzeichnis</h1>", toc_pagehead]
    for level, hid, title in entries:
        cls = {"1": "toc-h1", "2": "toc-h2", "3": "toc-h3"}[level]
        lines.append(f'<p class="{cls}"><a class="toc-link" href="#{hid}">{title}</a>'
                     f'<span class="toc-fill"></span><a class="toc-page" href="#{hid}"></a></p>')
    lines.append("</nav>")
    return "\n".join(lines), len(entries)


H1_RE = re.compile(r'<h1\b[^>]*>(.*?)</h1>')


def inject_pageheads(text):
    """Kopfzeilen-Vorlage direkt NACH jedem h1 (nicht davor!). position:running()
    hat keine eigene Groesse und "haengt" sich beim Layout an die Seite, auf der
    es im Dokumentfluss steht -- steht die Vorlage VOR einem erzwungenen
    Seitenumbruch (h1{break-before:page}), wird sie noch der vorherigen,
    schon vollen Seite zugerechnet und der Header zeigt das naechste Kapitel
    eine Seite zu frueh. Direkt nach dem h1 platziert, landet sie zuverlaessig
    auf der neuen Seite, die der Umbruch gerade erzeugt hat."""

    def repl(m):
        title = re.sub("<[^>]+>", "", m.group(1))
        head = (f'<div class="pagehead"><img src="assets/sr-logo-header.png">'
                f'<span class="name">{title}</span></div>')
        return m.group(0) + head

    return H1_RE.sub(repl, text)


PAGEFOOT_HTML = (
    '<div class="pagefoot">'
    '<span class="line1">Du hast Verbesserungsvorschläge für die Anleitung oder willst die '
    'aktuelle Version sehen? Besuche die digitale Version auf: docs.second-ride.de</span>'
    '<span class="line2"></span>'
    "</div>"
)


def main():
    bodies = [extract_chapter(rel, shift, title) for rel, shift, title in CHAPTERS]
    text = PAGEFOOT_HTML + "\n" + "\n".join(bodies)
    text = remove_teilegutachten(text)
    text = qrify_links(text)
    text = linearize_tabs(text)
    text = replace_status_emoji(text)
    text = replace_video_iframes(text)
    text = rebalance_checklists(text)
    # Kopfzeilen-Vorlage VOR dem Compact-Wrap einfuegen -- sonst landet sie
    # innerhalb von .compact und wird von dessen "img { width:39pt }"-Regel
    # mitgetroffen (verzerrtes Logo bei Kleingeschriebenes).
    text = inject_pageheads(text)
    text = wrap_compact(text)
    text = glue_headings(text)
    text = glue_text_to_image(text)
    text = glue_image_pairs(text)

    toc_html, n_entries = build_toc(text)
    text = text.replace(PAGEFOOT_HTML, "", 1)
    text = PAGEFOOT_HTML + "\n" + toc_html + "\n" + text

    text = IMG_RE.sub(size_image, text)

    (SCRATCH / "article_full.html").write_text(text, encoding="utf-8")
    print(f"{len(bodies)} Kapitel, {n_entries} TOC-Eintraege, {len(img_log)} Bilder")
    for l in img_log:
        print(" ", l)


if __name__ == "__main__":
    main()
