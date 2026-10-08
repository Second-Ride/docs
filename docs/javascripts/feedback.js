/*
 * Rückmeldeformular am Seitenende (overrides/partials/feedback.html).
 *
 * Schickt Text, Name und Seite per POST an den Worker aus feedback-worker/,
 * der daraus ein GitHub-Issue macht. Die Ereignisse hängen am document, damit
 * sie auch nach dem Seitenwechsel von navigation.instant funktionieren, ohne
 * dass etwas neu verbunden werden muss.
 */
(function () {
  "use strict";

  var ISSUE_URL = /^https:\/\/github\.com\/[\w.-]+\/[\w.-]+\/issues\/\d+$/;

  var MESSAGES = {
    message_too_short: "Bitte schreibe etwas mehr, mindestens ein ganzer Satz.",
    message_too_long: "Der Text ist zu lang. Bitte fasse dich auf etwa 2000 Zeichen.",
    too_many_links: "Bitte nenne höchstens zwei Links.",
    too_fast: "Das ging etwas zu schnell. Bitte versuche es gleich noch einmal.",
    rate_limited: "Gerade kommen sehr viele Rückmeldungen an. Bitte versuche es in einer Minute noch einmal.",
  };

  function root(node) {
    return node && node.closest ? node.closest("[data-sr-feedback]") : null;
  }

  // Zeit ab dem ersten Klick ins Textfeld. Der Worker lehnt alles ab, was
  // schneller abgeschickt wird, als ein Mensch schreiben kann.
  document.addEventListener("focusin", function (event) {
    var section = root(event.target);
    if (section && !section.dataset.startedAt) {
      section.dataset.startedAt = String(Date.now());
    }
  });

  document.addEventListener("submit", function (event) {
    var form = event.target;
    var section = root(form);
    if (!section || !form.classList.contains("sr-feedback__form")) return;
    event.preventDefault();
    send(section, form);
  });

  function send(section, form) {
    var status = form.querySelector(".sr-feedback__status");
    var button = form.querySelector("button[type=submit]");
    var message = form.elements.message.value.trim();

    if (message.length < 10) {
      show(status, "Bitte schreibe etwas mehr, mindestens ein ganzer Satz.", true);
      form.elements.message.focus();
      return;
    }

    var started = Number(section.dataset.startedAt) || Date.now();
    var payload = {
      message: message,
      name: form.elements.name.value,
      website: form.elements.website.value,
      elapsed: Date.now() - started,
      page: location.origin + location.pathname + location.hash,
      title: section.dataset.title,
      src: section.dataset.src,
    };

    button.disabled = true;
    show(status, "Wird gesendet …", false);

    fetch(section.dataset.endpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    })
      .then(function (response) {
        return response.json().catch(function () { return {}; }).then(function (data) {
          return { ok: response.ok, data: data };
        });
      })
      .then(function (result) {
        if (result.ok && result.data.ok) {
          thanks(section, form, result.data.issue_url);
        } else {
          failed(section, status, button, result.data.error);
        }
      })
      .catch(function () {
        failed(section, status, button, "network");
      });
  }

  function thanks(section, form, issueUrl) {
    var box = document.createElement("div");
    box.className = "sr-feedback__thanks";
    box.setAttribute("role", "status");

    var text = document.createElement("p");
    text.textContent = "Danke! Deine Rückmeldung ist bei uns angekommen.";
    box.appendChild(text);

    if (ISSUE_URL.test(issueUrl || "")) {
      var link = document.createElement("a");
      link.href = issueUrl;
      link.target = "_blank";
      link.rel = "noopener";
      link.textContent = "Zur Meldung bei GitHub";
      var wrap = document.createElement("p");
      wrap.appendChild(link);
      box.appendChild(wrap);
    }
    form.replaceWith(box);
  }

  function failed(section, status, button, code) {
    button.disabled = false;
    var text = MESSAGES[code] || "Das hat leider nicht geklappt. Bitte versuche es später noch einmal.";
    show(status, text, true);
    if (!MESSAGES[code]) {
      var link = document.createElement("a");
      link.href = section.dataset.fallback;
      link.target = "_blank";
      link.rel = "noopener";
      link.textContent = " Oder melde es direkt bei GitHub.";
      status.appendChild(link);
    }
  }

  function show(status, text, isError) {
    status.textContent = text;
    status.classList.toggle("sr-feedback__status--error", isError);
  }
})();
