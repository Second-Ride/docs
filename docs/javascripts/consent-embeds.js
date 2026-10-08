/*
 * Platzhalter für externe iframes (3D-Viewer, YouTube, Karte, Schaltplan).
 *
 * hooks/sr_consent_embeds.py gibt diesen iframes beim Bauen kein `src`, nur
 * `data-consent-src`. Die Consent-Engine von second-ride.de setzt `src` erst
 * nach der Einwilligung in Marketing (und entfernt es beim Widerruf). Dieses
 * Skript setzt jeden solchen iframe in einen Rahmen mit Hinweis und
 * "Akzeptieren"-Button, der direkt die Einwilligung erteilt
 * (consent-accept.js). Der kleine Knopf oben links öffnet danach die
 * Cookie-Einstellungen (`data-consent-renew`). Die Engine blendet den
 * Hinweis aus, sobald die Einwilligung vorliegt
 * (Klasse consent-embed--marketing-accepted, Stil in stylesheets/theme.css).
 *
 * Material lädt Seiten per Instant Navigation nach, daher beobachtet das
 * Skript den DOM statt nur einmal beim Laden zu laufen.
 */
(function () {
  var TEXTS = {
    de: {
      title: "{service} ist blockiert",
      body: "Du musst die Cookies akzeptieren, um das nutzen zu können.",
      cta: "Akzeptieren",
      settings: "Cookie-Einstellungen öffnen",
      generic: "Externer Inhalt",
    },
    en: {
      title: "{service} is blocked",
      body: "You have to accept cookies to use this.",
      cta: "Accept",
      settings: "Open cookie settings",
      generic: "External content",
    },
  };

  var SERVICES = [
    [/(^|\.)youtube(-nocookie)?\.com$/, "YouTube"],
    [/(^|\.)google\.com$/, "Google Maps"],
    [/(^|\.)3dviewer\.net$/, "3D-Viewer (3dviewer.net)"],
    [/(^|\.)lucid\.app$/, "Lucid"],
  ];

  function texts() {
    return document.documentElement.lang.toLowerCase().indexOf("en") === 0 ? TEXTS.en : TEXTS.de;
  }

  function serviceName(src, fallback) {
    var host = "";
    try {
      host = new URL(src).hostname;
    } catch (e) {
      return fallback;
    }
    for (var i = 0; i < SERVICES.length; i++) {
      if (SERVICES[i][0].test(host)) return SERVICES[i][1];
    }
    return host || fallback;
  }

  function cssLength(value) {
    if (!value) return null;
    return /^\d+(\.\d+)?$/.test(value) ? value + "px" : value;
  }

  function element(tag, className, text) {
    var node = document.createElement(tag);
    node.className = className;
    if (text) node.textContent = text;
    return node;
  }

  function wrap(iframe) {
    var t = texts();
    var wrapper = element("div", "consent-embed");
    var height = cssLength(iframe.style.height || iframe.getAttribute("height"));
    var width = cssLength(iframe.getAttribute("width"));
    if (height) wrapper.style.setProperty("--sr-embed-height", height);
    // Feste Breite (z. B. 700) nur als Obergrenze, damit es am Handy passt.
    if (width && width.slice(-2) === "px") wrapper.style.maxWidth = width;
    var parent = iframe.parentElement;
    if (parent && parent.getAttribute("align") === "center") wrapper.classList.add("consent-embed--centered");

    var service = serviceName(iframe.getAttribute("data-consent-src"), t.generic);
    var placeholderTitle = t.title.replace("{service}", service);

    var settings = element("button", "consent-embed__settings-button", t.settings);
    settings.type = "button";
    settings.setAttribute("data-consent-renew", "");

    var optout = element("div", "consent-embed__optout");
    var placeholder = element("div", "consent-embed__placeholder");
    placeholder.setAttribute("role", "note");
    placeholder.setAttribute("aria-label", placeholderTitle);
    var cta = element("button", "consent-embed__button", t.cta);
    cta.type = "button";
    cta.addEventListener("click", function () {
      if (window.SRConsentAccept) window.SRConsentAccept("marketing");
    });
    placeholder.append(
      element("p", "consent-embed__eyebrow", placeholderTitle),
      element("p", "consent-embed__body", t.body),
      cta
    );
    optout.append(placeholder);

    iframe.classList.add("consent-embed__iframe");
    iframe.setAttribute("data-sr-embed", "");
    if (!iframe.getAttribute("title")) iframe.setAttribute("title", service);
    iframe.parentNode.insertBefore(wrapper, iframe);
    wrapper.append(iframe, settings, optout);
  }

  function wrapAll() {
    var frames = document.querySelectorAll("iframe[data-consent-src]:not([data-sr-embed])");
    for (var i = 0; i < frames.length; i++) wrap(frames[i]);
  }

  var pending = false;
  function schedule() {
    if (pending) return;
    pending = true;
    (window.requestAnimationFrame || window.setTimeout)(function () {
      pending = false;
      wrapAll();
    });
  }

  wrapAll();
  new MutationObserver(schedule).observe(document.documentElement, { childList: true, subtree: true });
})();
