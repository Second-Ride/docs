#!/usr/bin/env python3
"""Iteratively force a page break before any H3 that would otherwise start
past the 50% fill mark of its page -- avoids a heading stranded low on an
already-busy page. Reads article_full.html, writes article_final.html."""
import re
import sys
from pathlib import Path

import fitz
from weasyprint import HTML

SCRATCH = Path(__file__).parent
CONTENT_TOP = 84.0   # @page margin-top
CONTENT_BOTTOM = 841.8897 - 76.0  # page height - margin-bottom
FILL_THRESHOLD = 0.5
# Ein erzwungener Umbruch, dessen neue Seite bis zum naechsten Umbruch trotzdem
# nur duenn gefuellt ist, hat mehr Leerraum erzeugt als er vermieden hat (siehe
# "Fahrbetrieb"/"Riemen Diagnose": kurzer Abschnitt landete allein auf einer
# fast leeren Seite). Solche Umbrueche werden wieder zurueckgenommen.
SPARSE_PAGE_THRESHOLD = 0.4
MAX_ITER = 10

H3_RE = re.compile(r'<h3\b([^>]*)>(.*?)</h3>', re.S)


def build_wrapper(article_path, out_path):
    wrapper = (SCRATCH / "wrapper.html").read_text(encoding="utf-8")
    body_start = wrapper.find("<body>") + len("<body>")
    head = wrapper[:body_start]
    article = article_path.read_text(encoding="utf-8")
    (SCRATCH / out_path).write_text(head + "\n" + article + "\n</body></html>", encoding="utf-8")


def label_h3(text):
    """Give every h3 a stable data-h3idx, unless already labelled."""
    idx = 0

    def repl(m):
        nonlocal idx
        attrs, inner = m.group(1), m.group(2)
        if "data-h3idx=" in attrs:
            idx += 1
            return m.group(0)
        tag = f'<h3{attrs} data-h3idx="{idx}">{inner}</h3>'
        idx += 1
        return tag

    return H3_RE.sub(repl, text)


def find_h3_positions(pdf_path):
    """Return (positions, page_fill): positions={h3idx: fill_ratio an der
    Position, wo die Ueberschrift beginnt}; page_fill={pageno: Fuellstand
    bis zum untersten Inhalt dieser Seite, egal ob Text oder Bild} --
    letzteres dient dazu, erzwungene Umbrueche zu erkennen, die nur eine
    duenn gefuellte neue Seite erzeugt haben (siehe SPARSE_PAGE_THRESHOLD)."""
    doc = fitz.open(pdf_path)
    positions = {}
    page_fill = {}
    idx = 0
    for pno, page in enumerate(doc):
        d = page.get_text("dict")
        spans = []
        max_bottom = 0.0
        for b in d["blocks"]:
            # Die laufende Fusszeile (Trennlinie + Text) sitzt auf JEDER
            # Seite nahe CONTENT_BOTTOM/der Seitenkante -- ohne diesen Filter
            # zaehlt sie faelschlich als "Inhalt" und jede Seite erscheint
            # nahe 100% gefuellt, egal wie leer der eigentliche Textkoerper
            # ist (genau das hat die duenne-Seiten-Erkennung wirkungslos
            # gemacht).
            if b["bbox"][1] >= CONTENT_BOTTOM:
                continue
            max_bottom = max(max_bottom, b["bbox"][3])
            if "lines" not in b:
                continue
            for l in b["lines"]:
                for s in l["spans"]:
                    if s["text"].strip() and 13.5 <= s["size"] <= 14.5 and s["bbox"][1] > CONTENT_TOP - 5:
                        spans.append(s)
        page_fill[pno] = (max_bottom - CONTENT_TOP) / (CONTENT_BOTTOM - CONTENT_TOP)
        # group into heading lines by matching y-start (a heading may wrap 2 lines)
        seen_y = set()
        for s in spans:
            y0 = round(s["bbox"][1], 1)
            if y0 in seen_y:
                continue
            seen_y.add(y0)
            fill = (y0 - CONTENT_TOP) / (CONTENT_BOTTOM - CONTENT_TOP)
            positions[idx] = (fill, pno)
            idx += 1
    doc.close()
    return positions, page_fill


GLUED_PRECEDED_RE = re.compile(r'</h[1-4]>\s*\Z')
DIV_OPEN = '<div class="keep-together">'
DIV_OPEN_FORCED = '<div class="keep-together force-break">'


def apply_forced_breaks(text, forced):
    """H3 mit erzwungenem Umbruch bekommen die Klasse direkt -- ausser sie
    stecken (per glue_headings) mit einer vorausgehenden Ueberschrift in
    einem keep-together-Block: dann muss der Umbruch auf den Block selbst,
    sonst gewinnt der erzwungene Umbruch gegen dessen break-inside:avoid und
    reisst die beiden Ueberschriften trotzdem auseinander.

    Erst NUR ermitteln (keine Textmutation), dann die Div-Ersetzungen VOR
    dem H3_RE.sub() fuer die einfachen Faelle anwenden: die Div-Positionen
    sind Offsets in den unveraenderten Text. Wuerde man zuerst H3_RE.sub()
    laufen lassen (das bei jedem einfachen Fall 20 Zeichen fuer
    class="force-break" einfuegt) und danach die alten Div-Offsets auf den
    LAENGEREN Ergebnistext anwenden, zeigen sie bei jedem vorausgehenden
    einfachen Treffer zu weit nach vorne und die Ersetzung landet mitten im
    Fliesstext (beobachtet bei "Wie man die Drosselung ueberprueft")."""
    div_positions_to_force = set()
    simple_idx = set()

    for m in H3_RE.finditer(text):
        idx = int(re.search(r'data-h3idx="(\d+)"', m.group(1)).group(1))
        if idx not in forced:
            continue
        if GLUED_PRECEDED_RE.search(text[:m.start()]):
            div_start = text.rfind(DIV_OPEN, 0, m.start())
            if div_start != -1 and "</div>" not in text[div_start:m.start()]:
                div_positions_to_force.add(div_start)
                continue
        simple_idx.add(idx)

    for pos in sorted(div_positions_to_force, reverse=True):
        text = text[:pos] + DIV_OPEN_FORCED + text[pos + len(DIV_OPEN):]

    def force_simple(m):
        attrs, inner = m.group(1), m.group(2)
        idx = int(re.search(r'data-h3idx="(\d+)"', attrs).group(1))
        if idx not in simple_idx or "force-break" in attrs:
            return m.group(0)
        return f'<h3{attrs} class="force-break">{inner}</h3>'

    return H3_RE.sub(force_simple, text)


def main():
    text = (SCRATCH / "article_full.html").read_text(encoding="utf-8")
    text = label_h3(text)
    n_h3 = len(H3_RE.findall(text))
    forced = set()
    flip_count = {}   # h3idx -> wie oft schon force/unforce umgeschaltet
    frozen = set()    # h3idx, die nicht mehr umgeschaltet werden (Oszillation)

    for it in range(MAX_ITER):
        working = apply_forced_breaks(text, forced) if forced else text

        (SCRATCH / "article_iter.html").write_text(working, encoding="utf-8")
        build_wrapper(SCRATCH / "article_iter.html", "wrapper_iter.html")
        HTML(str(SCRATCH / "wrapper_iter.html")).write_pdf(str(SCRATCH / "iter.pdf"))

        positions, page_fill = find_h3_positions(SCRATCH / "iter.pdf")
        new_forced = {i for i, (fill, _) in positions.items()
                      if fill > FILL_THRESHOLD and i not in forced and i not in frozen}
        # Ein bereits erzwungener Umbruch, der tatsaechlich ganz oben auf
        # seiner Seite gelandet ist (fill nahe 0 -- sonst hat z.B. ein
        # glue_headings-Div den Umbruch woanders hin verschoben), dessen
        # Seite bis zum naechsten Umbruch aber kaum gefuellt ist: der
        # Umbruch hat mehr Leerraum erzeugt als er vermieden hat.
        new_unforced = {
            i for i in forced
            if i not in frozen and i in positions and positions[i][0] < 0.05
            and page_fill.get(positions[i][1], 1.0) < SPARSE_PAGE_THRESHOLD
        }
        print(f"Durchlauf {it+1}: {len(positions)}/{n_h3} H3 gefunden, "
              f"{len(new_forced)} neu ueber {int(FILL_THRESHOLD*100)}% Fuellstand, "
              f"{len(new_unforced)} duenne erzwungene Seite(n) zurueckgenommen")
        if not new_forced and not new_unforced:
            break
        # Ein H3, das schon einmal umgeschaltet wurde und jetzt ein ZWEITES
        # Mal umschalten will, oszilliert (staendiger Wechsel force<->unforce,
        # da es nach jedem Umbruch die Bedingung fuer den jeweils anderen
        # Zustand wieder erfuellt). Ab dann eingefroren, mit Tendenz zu NICHT
        # erzwingen -- eine Ueberschrift, die etwas tief auf ihrer Seite
        # sitzt, ist optisch weniger schlimm als eine fast leere Folgeseite.
        for i in new_forced | new_unforced:
            flip_count[i] = flip_count.get(i, 0) + 1
            if flip_count[i] >= 2:
                frozen.add(i)
                new_forced.discard(i)
                new_unforced.discard(i)
                forced.discard(i)
        forced = (forced | new_forced) - new_unforced
    else:
        print("Maximale Iterationen erreicht, evtl. nicht vollstaendig konvergiert.")

    text = apply_forced_breaks(text, forced)
    (SCRATCH / "article_final.html").write_text(text, encoding="utf-8")
    print(f"Fertig: {len(forced)} von {n_h3} H3-Ueberschriften bekommen einen Seitenumbruch -> article_final.html")


if __name__ == "__main__":
    main()
