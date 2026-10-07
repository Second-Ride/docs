/*
 * Hell/Dunkel-Schalter, wie im Update-Tool (Webupdate-tool, src/ui/theme.ts).
 *
 * Die Seite folgt der Systemeinstellung, solange niemand den Schalter benutzt.
 * Ein Klick speichert die Wahl unter "sr-theme". Landet ein Klick auf dem
 * Schema, das das System ohnehin zeigen würde, wird die Wahl stattdessen
 * gelöscht und die Seite folgt wieder dem System. So bleibt der Schalter ein
 * einfacher Zwei-Zustands-Knopf und es gibt trotzdem einen Weg zurück zu
 * "automatisch", ohne dritten Zustand.
 *
 * Material merkt sich das Schema selbst (unter "__palette") und würde danach
 * der Systemeinstellung nicht mehr folgen. Deshalb setzt ein kleines Skript in
 * partials/header.html vor dem ersten Zeichnen "__palette" aus "sr-theme" bzw.
 * aus der Systemeinstellung; Material wendet dann genau das an.
 */
(function () {
  var STORAGE_KEY = "sr-theme";
  var systemDark = window.matchMedia("(prefers-color-scheme: dark)");

  function systemTheme() {
    return systemDark.matches ? "dark" : "light";
  }

  function storedTheme() {
    try {
      var value = localStorage.getItem(STORAGE_KEY);
      return value === "light" || value === "dark" ? value : null;
    } catch (e) {
      return null;
    }
  }

  function isPaletteInput(el) {
    return el instanceof HTMLInputElement && el.closest("[data-md-component=palette]") !== null;
  }

  // Materials Schalter klickt das jeweils andere Radio-Feld an.
  document.addEventListener("change", function (event) {
    if (!isPaletteInput(event.target)) return;
    var next = event.target.getAttribute("data-md-color-scheme") === "slate" ? "dark" : "light";

    // Gesperrter Speicher (privates Fenster) lässt den Schalter für diesen
    // Besuch funktionieren, die Wahl wird nur nicht gemerkt.
    try {
      if (next === systemTheme()) {
        localStorage.removeItem(STORAGE_KEY);
      } else {
        localStorage.setItem(STORAGE_KEY, next);
      }
    } catch (e) { /* nicht gemerkt */ }
  });

  // Das System kann unter einem offenen Tab wechseln, zum Beispiel automatisch
  // bei Sonnenuntergang. Gefolgt wird nur, solange keine Wahl gespeichert ist.
  systemDark.addEventListener("change", function () {
    if (storedTheme() !== null) return;
    var scheme = systemDark.matches ? "slate" : "default";
    var input = document.querySelector("[data-md-component=palette] input[data-md-color-scheme='" + scheme + "']");
    if (input && !input.checked) input.click();
  });
})();

/*
 * Teile- und Werkzeuglisten.
 *
 * Im Markdown sind das HTML-Tabellen mit Checkbox-Listen in den Zellen. Hier
 * bekommt jede solche Tabelle die Klasse sr-checklist, und der Inhalt jedes
 * Listenpunkts wandert in ein Label: So ist die ganze Zeile antippbar und
 * die Checkbox hat einen zugänglichen Namen. is-checked am Listenpunkt
 * erlaubt dem CSS, abgehakte Zeilen zurückzunehmen.
 *
 * Die Häkchen bleiben pro Gerät gespeichert (je Seite und Liste), damit sie
 * beim Blättern und nach dem Sperren des Handys in der Werkstatt nicht weg
 * sind. Unter jeder Liste mit Häkchen steht "Liste zurücksetzen". Ohne
 * Speicher (privates Fenster) funktioniert alles, nur ohne Gedächtnis.
 *
 * Läuft bei jedem Seitenwechsel, auch ohne Neuladen (navigation.instant).
 * Die Druck-Pipeline liest das gebaute HTML und ist davon nicht betroffen.
 */
(function () {
  var PREFIX = "sr-checklist:";

  function load(key) {
    try {
      var value = JSON.parse(localStorage.getItem(key) || "[]");
      return Array.isArray(value) ? value : [];
    } catch (e) {
      return [];
    }
  }

  function save(key, boxes) {
    var checked = [];
    for (var i = 0; i < boxes.length; i++) {
      if (boxes[i].checked) checked.push(i);
    }
    try {
      if (checked.length) {
        localStorage.setItem(key, JSON.stringify(checked));
      } else {
        localStorage.removeItem(key);
      }
    } catch (e) { /* nicht gemerkt */ }
    return checked.length;
  }

  function enhanceChecklist(table, index) {
    if (table.classList.contains("sr-checklist")) return;
    table.classList.add("sr-checklist");

    var key = PREFIX + location.pathname + ":" + index;
    var stored = load(key);
    var boxes = [];
    var items = table.querySelectorAll("li");

    for (var i = 0; i < items.length; i++) {
      var li = items[i];
      var box = li.querySelector(":scope > input[type=checkbox]");
      if (!box) continue;

      var label = document.createElement("label");
      label.className = "sr-check";
      while (li.firstChild) label.appendChild(li.firstChild);
      li.appendChild(label);

      box.checked = stored.indexOf(boxes.length) !== -1;
      li.classList.toggle("is-checked", box.checked);
      boxes.push(box);
    }

    var reset = document.createElement("button");
    reset.type = "button";
    reset.className = "sr-checklist-reset";
    reset.textContent = "Liste zurücksetzen";
    reset.hidden = stored.length === 0;
    var anchor = table.closest(".md-typeset__scrollwrap") || table;
    anchor.insertAdjacentElement("afterend", reset);

    table.addEventListener("change", function (event) {
      var box = event.target;
      if (!(box instanceof HTMLInputElement) || box.type !== "checkbox") return;
      var item = box.closest("li");
      if (item) item.classList.toggle("is-checked", box.checked);
      reset.hidden = save(key, boxes) === 0;
    });

    reset.addEventListener("click", function () {
      for (var i = 0; i < boxes.length; i++) {
        boxes[i].checked = false;
        var item = boxes[i].closest("li");
        if (item) item.classList.remove("is-checked");
      }
      save(key, boxes);
      reset.hidden = true;
    });
  }

  function enhanceChecklists() {
    var tables = document.querySelectorAll(".md-typeset table");
    var index = 0;
    for (var t = 0; t < tables.length; t++) {
      if (!tables[t].querySelector("input[type=checkbox]")) continue;
      enhanceChecklist(tables[t], index++);
    }
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(enhanceChecklists);
  } else {
    document.addEventListener("DOMContentLoaded", enhanceChecklists);
  }
})();

/*
 * Suche schließen, sobald man woanders hinklickt.
 *
 * Material schließt die Suche nur über die Abdunklung der Seite; ein Klick
 * auf Logo, Schalter oder Bereiche im Header ließ sie offen. Außerdem blieb
 * das Feld fokussiert, sodass ein erneuter Klick hinein sie nicht wieder
 * öffnete. Geschlossen wird über einen Klick auf Materials Schalter (die
 * Checkbox #__search), so bekommt Material die Änderung mit.
 */
(function () {
  function toggle() {
    return document.getElementById("__search");
  }

  document.addEventListener("pointerdown", function (event) {
    var search = toggle();
    if (!search || !search.checked) return;
    var target = event.target;
    if (!(target instanceof Element)) return;
    // Im Suchfeld, in den Ergebnissen und auf Materials eigenen Schaltern
    // (Abdunklung, Lupe) entscheidet Material selbst.
    if (target.closest(".md-search__inner, label[for='__search']")) return;
    search.click();
  });

  document.addEventListener("change", function (event) {
    var search = toggle();
    if (event.target !== search || search.checked) return;
    var input = document.querySelector(".md-search__input");
    if (input && document.activeElement === input) input.blur();
  });
})();

/*
 * Sprünge innerhalb der Seite gleiten immer: Inhaltsverzeichnis rechts,
 * "Auf dieser Seite", Permalinks und Verweise im Text.
 *
 * Ohne das reicht Materials Sofort-Navigation solche Klicks je nach Zustand
 * unterschiedlich weiter, mal sprang die Seite, mal glitt sie. Weich
 * scrollen per CSS (scroll-behavior) geht nicht, dann würde auch jeder
 * Seitenwechsel sichtbar nach oben rollen. Das Gleiten des Browsers selbst
 * reicht auch nicht: Unterwegs laden Fotos nach, die Seite wird länger, und
 * er bliebe vor dem Ziel stehen. Deshalb rechnet die Animation das Ziel in
 * jedem Bild neu und führt danach noch kurz nach.
 *
 * Ausgenommen sind Klicks mit Zusatztaste, der Sprunglink "Zum Inhalt",
 * Materials interne Anker (__...) und die Navigation links, die auf dem
 * Handy Materials Schublade ist. Wer reduzierte Bewegung eingestellt hat,
 * springt direkt. Mausrad, Wischen, Tasten oder ein Klick brechen ab.
 */
(function () {
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  var frame = null;

  function stop() {
    if (frame === null) return;
    cancelAnimationFrame(frame);
    frame = null;
  }

  ["wheel", "touchstart", "keydown", "mousedown"].forEach(function (type) {
    window.addEventListener(type, stop, { passive: true });
  });

  // Ziel so, wie der Browser es selbst ansteuern würde: Überschrift direkt
  // unter der Kopfzeile (scroll-padding-top in theme.css)
  function offsetOf(target) {
    var root = document.documentElement;
    var padding = parseFloat(getComputedStyle(root).scrollPaddingTop) || 0;
    var max = root.scrollHeight - window.innerHeight;
    var top = target.getBoundingClientRect().top + window.scrollY - padding;
    return Math.max(0, Math.min(max, top));
  }

  function easeInOut(t) {
    return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
  }

  function glide(target) {
    stop();
    if (reduceMotion.matches) {
      window.scrollTo(0, offsetOf(target));
      return;
    }
    var from = window.scrollY;
    // 300ms für kurze Wege, höchstens 800ms quer über die ganze Anleitung
    var duration = Math.min(800, 300 + Math.abs(offsetOf(target) - from) / 25);
    var start = null;
    var settleUntil = null;

    function step(now) {
      if (start === null) start = now;
      var t = Math.min(1, (now - start) / duration);
      window.scrollTo(0, from + (offsetOf(target) - from) * easeInOut(t));
      if (t === 1) {
        if (settleUntil === null) settleUntil = now + 600;
        if (now >= settleUntil) {
          frame = null;
          return;
        }
      }
      frame = requestAnimationFrame(step);
    }

    frame = requestAnimationFrame(step);
  }

  document.addEventListener("click", function (event) {
    if (event.defaultPrevented || event.button !== 0) return;
    if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    if (!(event.target instanceof Element)) return;

    // Materials Sofort-Navigation schreibt alle Links zu vollen Adressen um,
    // deshalb zählt nicht das Attribut, sondern ob der Link auf diese Seite
    // zeigt.
    var link = event.target.closest("a[href]");
    if (!link || link.target || !link.hash) return;
    if (link.origin !== location.origin || link.pathname !== location.pathname || link.search !== location.search) return;
    if (link.classList.contains("md-skip") || link.closest(".md-sidebar--primary")) return;

    var id = decodeURIComponent(link.hash.slice(1));
    if (!id || id.indexOf("__") === 0) return;
    var target = document.getElementById(id);
    if (!target) return;

    // Vor Materials eigenem Klick-Handler am body abfangen
    event.preventDefault();
    event.stopPropagation();

    glide(target);
    if (location.hash !== link.hash) history.replaceState(history.state, "", link.hash);

    // Per Tastatur ausgelöst: Fokus an das Ziel, damit Tab dort weitergeht
    if (event.detail === 0) {
      if (!target.hasAttribute("tabindex")) target.setAttribute("tabindex", "-1");
      target.focus({ preventScroll: true });
    }
  }, true);
})();

/*
 * Kurze Seiten: Das schwarze Fußband beginnt genau am unteren
 * Bildschirmrand, ganz oben auf der Seite ist es also gerade nicht zu sehen.
 * Die Vor/Zurück-Karten stehen im Footer über dem Band und bleiben im Bild.
 * Ihre Höhe hängt von Titel und Breite ab, deshalb wird der Abstand vom
 * Footer-Anfang bis zum Band gemessen und als --sr-footer-lead an theme.css
 * gegeben (Mindesthöhe von .md-main). Ohne Skript beginnen die Karten am
 * Rand, die Seite ist dann nur etwas höher.
 */
(function () {
  var observer = null;

  function measure() {
    var footer = document.querySelector(".md-footer");
    var band = footer && footer.querySelector(".sr-footer__band");
    if (!band) return;
    var lead = band.getBoundingClientRect().top - footer.getBoundingClientRect().top;
    document.body.style.setProperty("--sr-footer-lead", Math.max(0, lead) + "px");
  }

  // Materials Sofort-Navigation tauscht den Footer bei jedem Seitenwechsel aus
  function watch() {
    if (observer) observer.disconnect();
    var footer = document.querySelector(".md-footer");
    if (!footer) return;
    if ("ResizeObserver" in window) {
      observer = new ResizeObserver(measure);
      observer.observe(footer);
    }
    measure();
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(watch);
  } else {
    document.addEventListener("DOMContentLoaded", watch);
  }
})();

/*
 * Höhe der Seitenleisten (Navigation links, Inhaltsverzeichnis rechts).
 *
 * Material rechnet die Höhe aus dem Abstand über dem Hauptbereich und zieht
 * unten noch einmal den oberen Innenabstand ab. Weil theme.css die Leisten
 * um diesen Abstand hochzieht (sonst wandern sie beim Scrollen erst mit),
 * endeten die Listen oben auf der Seite 64px über dem Bildschirmrand, wie
 * von einem weißen Kasten abgedeckt. Hier gilt die tatsächliche Lage: vom
 * Anfang der Liste bis 16px über den Bildschirmrand oder, wenn der Footer
 * schon im Bild ist, bis 16px über das Ende des Hauptbereichs. theme.css
 * setzt den Wert (--sr-scrollwrap-h) nur, wo die Leisten kleben.
 */
(function () {
  var GAP = 16;
  var queued = false;

  function update() {
    queued = false;
    var main = document.querySelector(".md-main");
    if (!main) return;
    var bottom = Math.min(window.innerHeight, main.getBoundingClientRect().bottom) - GAP;
    var wraps = document.querySelectorAll(".md-sidebar__scrollwrap");
    for (var i = 0; i < wraps.length; i++) {
      var height = Math.max(0, bottom - wraps[i].getBoundingClientRect().top);
      wraps[i].style.setProperty("--sr-scrollwrap-h", height + "px");
    }
  }

  function queue() {
    if (queued) return;
    queued = true;
    requestAnimationFrame(update);
  }

  window.addEventListener("scroll", queue, { passive: true });
  window.addEventListener("resize", queue);

  // Nachladende Bilder verlängern die Seite, das verschiebt das Ende
  var observer = "ResizeObserver" in window ? new ResizeObserver(queue) : null;

  function watch() {
    var main = document.querySelector(".md-main");
    if (observer) {
      observer.disconnect();
      if (main) observer.observe(main);
    }
    queue();
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(watch);
  } else {
    document.addEventListener("DOMContentLoaded", watch);
  }
})();
