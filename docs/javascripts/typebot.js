/*
 * Chat-Button (Typebot "faqs", bot.second-ride.de).
 *
 * Der Bot liest die Bot-Fassung der Doku (/llms-bot.txt, erzeugt von
 * hooks/llms_bot.py) und antwortet nur daraus. Prompt und Einrichtung:
 * chatbot/README.md.
 *
 * Der Chat lädt Code von cdn.jsdelivr.net und spricht mit bot.second-ride.de,
 * also mit externen Diensten. Deshalb startet er erst, wenn der Besucher in
 * der Cookie-Einwilligung (second-ride.de/consent.js) Marketing erlaubt hat.
 * Bis dahin zeigt die Seite einen eigenen Button im selben Look; ein Klick
 * sagt, was fehlt ("Du musst die Cookies akzeptieren ..."), und hat direkt
 * einen "Akzeptieren"-Button (consent-accept.js). Danach startet der Chat und
 * öffnet sich gleich. Nach der Einwilligung wird der Button durch den echten
 * Chat ersetzt, nach einem Widerruf wieder zurück.
 *
 * Wird nur einmal pro Seitenaufruf gestartet. Dank navigation.instant lädt
 * Material Seiten ohne Neuladen nach; ein Start pro Seitenwechsel würde
 * mehrere Chat-Buttons übereinander setzen.
 *
 * Das Aussehen kommt aus stylesheets/chatbot.css. Der Bubble liegt in einem
 * Shadow-DOM, deshalb wird das Stylesheet nach dem Start dort eingehängt. Der
 * Button ohne Einwilligung liegt im normalen DOM, sein Stil steht in
 * stylesheets/theme.css (.sr-chat-gate).
 */
(function () {
  var started = false;
  // Gleiche Versionsnummer wie dieses Skript (?v=, hooks/sr_assets.py),
  // damit nach einem Deploy kein altes chatbot.css aus dem Cache kommt
  var scriptUrl = new URL(document.currentScript.src);
  var css = new URL("../stylesheets/chatbot.css", scriptUrl);
  css.search = scriptUrl.search;
  var cssUrl = css.href;

  function styleBubble() {
    var tries = 0;
    var timer = setInterval(function () {
      var bubble = document.querySelector("typebot-bubble");
      var root = bubble && bubble.shadowRoot;
      if (root) {
        clearInterval(timer);
        var link = document.createElement("link");
        link.rel = "stylesheet";
        link.href = cssUrl;
        root.appendChild(link);
      } else if (++tries > 100) {
        clearInterval(timer);
      }
    }, 100);
  }

  var CATEGORY = "marketing";
  var TEXTS = {
    de: {
      open: "Chat öffnen",
      title: "Chat gesperrt",
      body: "Du musst die Cookies akzeptieren, um den Chat nutzen zu können.",
      cta: "Akzeptieren",
    },
    en: {
      open: "Open chat",
      title: "Chat blocked",
      body: "You have to accept cookies to use the chat.",
      cta: "Accept",
    },
  };
  var CHAT_ICON =
    '<svg viewBox="0 0 24 24" width="24" height="24" fill="#ffffff" stroke="#050505" ' +
    'stroke-width="1.75" stroke-linejoin="round" aria-hidden="true">' +
    '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>';

  var gate = null;
  // Wer im gesperrten Chat "Akzeptieren" drückt, will chatten: nach dem Start öffnen.
  var openAfterStart = false;

  function texts() {
    return document.documentElement.lang.toLowerCase().indexOf("en") === 0 ? TEXTS.en : TEXTS.de;
  }

  function consentGiven() {
    var api = window.SecondRideConsent;
    return !!(api && api.consent && api.consent[CATEGORY] === true);
  }

  function removeGate() {
    if (gate) gate.remove();
    gate = null;
  }

  function showGate() {
    if (gate) return;
    var t = texts();
    gate = document.createElement("div");
    gate.className = "sr-chat-gate";

    var panel = document.createElement("div");
    panel.className = "sr-chat-gate__panel";
    panel.setAttribute("role", "dialog");
    panel.setAttribute("aria-label", t.title);
    panel.hidden = true;
    var title = document.createElement("p");
    title.className = "sr-chat-gate__title";
    title.textContent = t.title;
    var body = document.createElement("p");
    body.className = "sr-chat-gate__body";
    body.textContent = t.body;
    var cta = document.createElement("button");
    cta.type = "button";
    cta.className = "sr-chat-gate__cta";
    cta.textContent = t.cta;
    cta.addEventListener("click", function () {
      openAfterStart = true;
      if (window.SRConsentAccept && !window.SRConsentAccept(CATEGORY)) openAfterStart = false;
    });
    panel.append(title, body, cta);

    var button = document.createElement("button");
    button.type = "button";
    button.className = "sr-chat-gate__button";
    button.setAttribute("aria-label", t.open);
    button.setAttribute("aria-expanded", "false");
    button.innerHTML = CHAT_ICON;
    button.addEventListener("click", function () {
      panel.hidden = !panel.hidden;
      button.setAttribute("aria-expanded", String(!panel.hidden));
    });

    gate.append(panel, button);
    document.documentElement.append(gate);
  }

  function removeBubble() {
    var bubbles = document.querySelectorAll("typebot-bubble");
    for (var i = 0; i < bubbles.length; i++) bubbles[i].remove();
    started = false;
  }

  function start() {
    if (started) return;
    started = true;
    import("https://cdn.jsdelivr.net/npm/@typebot.io/js@0/dist/web.js")
      .then(function (module) {
        // Zwischenzeitlich widerrufen: nichts mehr starten.
        if (!consentGiven()) {
          started = false;
          return;
        }
        module.default.initBubble({
          typebot: "faqs",
          apiHost: "https://bot.second-ride.de",
          theme: {
            // Nur Rückfall, falls chatbot.css nicht lädt.
            button: { backgroundColor: "#FFD269", iconColor: "#ffffff" },
            chatWindow: { backgroundColor: "#ffffff" },
          },
        });
        styleBubble();
        if (openAfterStart) {
          openAfterStart = false;
          setTimeout(function () {
            module.default.open();
          }, 300);
        }
      })
      .catch(function () {
        // Der Chat ist optional: ohne CDN bleibt die Doku voll nutzbar.
        started = false;
      });
  }

  // Einwilligung und Chat in Einklang halten: erlaubt -> Chat, sonst Button.
  function sync() {
    if (consentGiven()) {
      removeGate();
      start();
    } else {
      removeBubble();
      showGate();
    }
  }

  window.addEventListener("SecondRideConsentChange", sync);
  sync();
})();
