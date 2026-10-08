"""
Bot-Fassung der Doku für den Chat-Assistenten (MkDocs-Hook, in mkdocs.yml
unter `hooks` eingetragen). Schreibt beim Bauen `site/llms-bot.txt`.

Die Datei ersetzt `llms-full.txt` als Wissensbasis des Typebot-Chatbots. Der
Hook liest die Markdown-Quellen (nicht das HTML), daher entfallen Tabellen-
Padding, Bild-Platzhalter und HTML-Gerüst. Zusätzlich:

- Reihenfolge nach Nutzen für Kundenfragen: FAQ, Bedienungsanleitung,
  Umbauanleitung, zuletzt die Entwicklerseiten.
- Jede Seite beginnt mit Titel, Bereich und der echten URL.
- Jede Überschrift trägt ihre echte Anker-ID aus dem Inhaltsverzeichnis
  (`[#anker]`), damit der Bot nicht selbst Anker berechnen muss.
- Relative Links werden zu absoluten URLs.
- PDF-Viewer (iframe) erscheinen als "(PDF: URL)", Videos als "(Video: URL)".
- Vorn steht der Abschnitt "ZUSATZWISSEN" aus `chatbot/zusatzwissen.md`, falls
  die Datei existiert: Hinweise, die auf keiner Seite stehen, zum Beispiel wohin
  der Bot bei welchem Thema verweist.

Nur Standardbibliothek, damit der Build auf dem Server ohne neue Pakete läuft.
"""

import html
import re
from datetime import date
from pathlib import Path
from urllib.parse import urljoin

# (Ordner in docs/, Bereichsname). Reihenfolge = Reihenfolge in der Datei.
SECTIONS = [
    ("faq/", "FAQ"),
    ("user-manual/", "Bedienungsanleitung"),
    ("conversion-manual/", "Umbauanleitung"),
    ("for-developers/", "Für Entwickler"),
]

_pages = {}  # src_uri -> {"markdown", "title", "url", "toc"}

HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$")
FENCE_RE = re.compile(r"^\s*(```|~~~)")


def _flatten(toc):
    for item in toc:
        yield item
        yield from _flatten(item.children)


def _section_of(src_uri):
    for prefix, name in SECTIONS:
        if src_uri.startswith(prefix):
            return name
    return None


def _add_anchors(markdown, toc):
    """Hängt `[#id]` an jede Markdown-Überschrift, sofern die Zählung passt."""
    ids = [t.id for t in _flatten(toc)]
    lines = markdown.split("\n")
    in_fence = False
    positions = []
    for i, line in enumerate(lines):
        if FENCE_RE.match(line):
            in_fence = not in_fence
        elif not in_fence and HEADING_RE.match(line):
            positions.append(i)
    if len(positions) != len(ids):
        return markdown
    for pos, anchor in zip(positions, ids):
        lines[pos] = f"{lines[pos].rstrip()} [#{anchor}]"
    return "\n".join(lines)


def _resolve(href, page_url, site_url):
    if re.match(r"^(https?:|mailto:|tel:|#)", href):
        return href
    base = urljoin(site_url, page_url)
    target = href
    anchor = ""
    if "#" in target:
        target, anchor = target.split("#", 1)
        anchor = "#" + anchor
    target = re.sub(r"(^|/)index(\.en)?\.md$", r"\1", target)
    target = re.sub(r"\.md$", "/", target)
    return urljoin(base, target) + anchor


def _clean(markdown, page_url, site_url):
    text = markdown

    # HTML-Kommentare, PDF-Viewer und Video-Einbettungen
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    base = urljoin(site_url, page_url)
    text = re.sub(
        r"<iframe\b[^>]*?src=\"([^\"]+?\.pdf)\"[^>]*>.*?</iframe>",
        lambda m: f"\n(PDF: {urljoin(base, m.group(1).strip())})\n",
        text,
        flags=re.S | re.I,
    )
    text = re.sub(
        r"<iframe[^>]*?src=\"([^\"]+)\"[^>]*>\s*</iframe>",
        lambda m: f"\n(Video: {urljoin(base, m.group(1).strip())})\n",
        text,
        flags=re.S | re.I,
    )
    text = re.sub(r"<iframe[^>]*>\s*</iframe>", "", text, flags=re.S | re.I)

    # Bilder (Markdown und HTML) sind für den Bot wertlos
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)(\{[^}]*\})?", "", text)
    text = re.sub(r"<img\b[^>]*>", "", text, flags=re.I)

    # Attributlisten wie {: .class } und Icon-Kürzel wie :material-download:
    text = re.sub(r"\{:?\s*[.#][^}]*\}", "", text)
    text = re.sub(r"[ \t]*:(?:material|fontawesome|octicons|simple)-[a-z0-9-]+:", "", text)

    # Links in HTML zu Markdown
    text = re.sub(
        r"<a\b[^>]*?href=\"([^\"]+)\"[^>]*>(.*?)</a>",
        r"[\2](\1)",
        text,
        flags=re.S | re.I,
    )

    # HTML-Überschriften zu Markdown-Überschriften
    for level in range(1, 7):
        text = re.sub(
            rf"<h{level}\b[^>]*>(.*?)</h{level}>",
            lambda m, n=level: "\n" + "#" * n + " " + m.group(1).strip() + "\n",
            text,
            flags=re.S | re.I,
        )

    # Listen und Tabellengerüst aus HTML
    text = re.sub(r"<input\b[^>]*>", "", text, flags=re.I)
    text = re.sub(r"<li\b[^>]*>", "\n- ", text, flags=re.I)
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.I)
    text = re.sub(r"</?(?:table|tbody|thead|tr|td|th|ul|ol|li|p|div|span|b|strong|em|i)\b[^>]*>", "\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)  # übrige Tags
    text = html.unescape(text)

    # Relative Links absolut machen
    text = re.sub(
        r"\]\(([^)\s]+)\)",
        lambda m: "](" + _resolve(m.group(1), page_url, site_url) + ")",
        text,
    )

    # Markdown-Tabellen: Padding und lange Trennstriche entfernen
    out = []
    for line in text.split("\n"):
        if line.lstrip().startswith("|"):
            line = re.sub(r"\s{2,}", " ", line.strip())
            line = re.sub(r"-{3,}", "---", line)
            if re.fullmatch(r"[|\s:-]+", line):
                continue
        out.append(line.rstrip())
    text = "\n".join(out)

    # Leerzeilen zusammenfassen, führende Einrückung der Listen vereinheitlichen
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"(?m)^([ \t]*)-[ \t]{2,}", r"\1- ", text)
    # Leerzeilen zwischen direkt aufeinanderfolgenden Listenpunkten entfernen
    text = re.sub(r"(?m)^(- [^\n]*)\n\n(?=- )", r"\1\n", text)
    text = re.sub(r"(?m)^(- [^\n]*)\n\n(?=- )", r"\1\n", text)
    return text.strip()


def on_page_markdown(markdown, page, config, files):
    src = page.file.src_uri
    # Englische Übersetzungen nie aufnehmen, auch wenn sie mitgebaut werden
    if _section_of(src) is None or src.endswith(".en.md"):
        return None
    title = page.title
    h1 = re.search(r"^#[ \t]+(.+?)[ \t]*$", markdown, re.M)
    if title == "Index" and h1:  # Ordner-Startseiten ohne eigenen Titel
        title = h1.group(1)
    if title == "Index":  # kein H1: Ordnername verwenden
        parent = Path(src).parent.name
        top = src.split("/")[0]
        title = "Übersicht" if parent == top else f"{parent} (Übersicht)"
    trail = [a.title for a in reversed(page.ancestors)] + [title]
    area = _section_of(src)
    if trail[0] != area:  # nicht in der Navigation: Bereich voranstellen
        trail.insert(0, area)
    _pages[src] = {
        "markdown": markdown,
        "title": page.title,
        "path": " > ".join(trail),
        "url": page.url,
    }
    return None


def on_page_content(content, page, config, files):
    entry = _pages.get(page.file.src_uri)
    if entry is not None:
        entry["toc"] = list(page.toc)
    return None


def _extra_knowledge(config):
    """Abschnitt "ZUSATZWISSEN" aus chatbot/zusatzwissen.md (leer, wenn es die Datei nicht gibt)."""
    path = Path(config["config_file_path"]).parent / "chatbot" / "zusatzwissen.md"
    if not path.is_file():
        return ""
    body = re.sub(r"<!--.*?-->", "", path.read_text(encoding="utf-8"), flags=re.S).strip()
    return f"=== ZUSATZWISSEN ===\n{body}\n" if body else ""


def on_post_build(config):
    site_url = config["site_url"] or ""
    blocks = []
    for prefix, area in SECTIONS:
        for src in sorted(s for s in _pages if s.startswith(prefix)):
            entry = _pages[src]
            body = _add_anchors(entry["markdown"], entry.get("toc", []))
            body = _clean(body, entry["url"], site_url)
            url = urljoin(site_url, entry["url"])
            blocks.append(
                f"=== SEITE: {entry['path']} ===\n"
                f"Bereich: {area}\n"
                f"URL: {url}\n\n"
                f"{body}\n"
            )

    header = (
        "# Second Ride Dokumentation (Bot-Fassung)\n\n"
        f"Stand: {date.today().isoformat()}. Jede Seite beginnt mit "
        "\"=== SEITE: ... ===\", danach Bereich und URL. Hinter jeder "
        "Überschrift steht in eckigen Klammern ihr Anker, zum Beispiel "
        "\"[#details-zum-umbausatz]\". Ein Link auf einen Abschnitt lautet "
        "URL + \"#\" + Anker. Der Abschnitt \"=== ZUSATZWISSEN ===\" enthält "
        "Hinweise, die auf keiner Seite stehen, zum Beispiel wohin du bei "
        "welchem Thema verweist.\n"
    )
    extra = _extra_knowledge(config)
    output = header + "\n" + (extra + "\n" if extra else "") + "\n".join(blocks)
    target = Path(config["site_dir"]) / "llms-bot.txt"
    target.write_text(output, encoding="utf-8")
    print(f"INFO    -  llms-bot.txt: {len(blocks)} Seiten, {len(output):,} Zeichen")
