/*
 * Einwilligung direkt auf der Seite erteilen (für Chat und externe Inhalte).
 *
 * Wer einen gesperrten Dienst anklickt, soll nicht zur Cookie-Seite von
 * second-ride.de abspringen, sondern an Ort und Stelle "Akzeptieren" drücken
 * können. Das Skript ruft dafür die Consent-Engine (second-ride.de/consent.js)
 * auf und erlaubt genau die Kategorie, die der Dienst braucht. Bereits
 * getroffene Entscheidungen zu anderen Kategorien bleiben unverändert.
 *
 * Muss vor consent-embeds.js und typebot.js geladen werden.
 */
(function () {
  window.SRConsentAccept = function (category) {
    var api = window.SecondRideConsent;
    if (!api || typeof api.save !== "function") {
      // Engine nicht erreichbar (second-ride.de down): Einstellungen als Rückfall.
      window.open("https://second-ride.de/cookies", "_blank", "noopener");
      return false;
    }
    var current = api.consent || {};
    api.save({
      preferences: current.preferences === true,
      statistics: current.statistics === true,
      marketing: category === "marketing" ? true : current.marketing === true,
    });
    return true;
  };
})();
