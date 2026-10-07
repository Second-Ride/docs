/*
 * Chat-Button (Typebot "faqs", bot.second-ride.de).
 *
 * Der Bot liest die Bot-Fassung der Doku (/llms-bot.txt, erzeugt von
 * hooks/llms_bot.py) und antwortet nur daraus. Prompt und Einrichtung:
 * chatbot/README.md.
 *
 * Wird nur einmal pro Seitenaufruf gestartet. Dank navigation.instant lädt
 * Material Seiten ohne Neuladen nach; ein Start pro Seitenwechsel würde
 * mehrere Chat-Buttons übereinander setzen.
 *
 * Das Aussehen kommt aus stylesheets/chatbot.css. Der Bubble liegt in einem
 * Shadow-DOM, deshalb wird das Stylesheet nach dem Start dort eingehängt.
 */
(function () {
  var started = false;
  var cssUrl = new URL(
    "../stylesheets/chatbot.css",
    document.currentScript.src
  ).href;

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

  function start() {
    if (started) return;
    started = true;
    import("https://cdn.jsdelivr.net/npm/@typebot.io/js@0/dist/web.js")
      .then(function (module) {
        module.default.initBubble({
          typebot: "faqs",
          apiHost: "https://bot.second-ride.de",
          theme: {
            // Nur Rückfall, falls chatbot.css nicht lädt.
            button: { backgroundColor: "#282828", iconColor: "#ffffff" },
            chatWindow: { backgroundColor: "#ffffff" },
          },
        });
        styleBubble();
      })
      .catch(function () {
        // Der Chat ist optional: ohne CDN bleibt die Doku voll nutzbar.
      });
  }

  start();
})();
