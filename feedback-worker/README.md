# Rückmeldeformular der Doku (Cloudflare Worker)

Das Formular "Rückmeldung zu dieser Seite" am Ende jeder Doku-Seite schickt Text, optional einen Namen und die Seite an diesen Worker. Der Worker legt daraus ein Issue in `Second-Ride/docs` an. Besucher brauchen kein GitHub-Konto, das GitHub-Token liegt nur im Worker.

```
Browser (docs/javascripts/feedback.js)
   │  POST /api/feedback  { message, name, page, title, src, ... }
   ▼
Worker (src/index.js)  prüft, baut Titel und Text selbst, legt das Issue an
   │  POST https://api.github.com/repos/Second-Ride/docs/issues
   ▼
Issue mit Label "doku-feedback": Seite, Datei, Name (oder "anonym"), Text als Zitat
```

Das Formular erscheint erst, wenn in `mkdocs.yml` unter `extra.feedback` der `endpoint` gesetzt ist. Bis dahin zeigt jede Seite stattdessen einen Link, der bei GitHub ein vorausgefülltes Issue öffnet.

## Einrichtung (einmalig)

1. **Label anlegen:** In GitHub unter Issues, Labels das Label `doku-feedback` erstellen.
2. **Token anlegen:** Bei GitHub ein Fine-grained Personal Access Token erzeugen, nur für das Repository `Second-Ride/docs`, nur mit der Berechtigung **Issues: Read and write**. Am besten von einem eigenen Bot-Konto statt von einer Person, damit das Token nicht mit einem Mitarbeiter verschwindet. Fine-grained Tokens laufen spätestens nach einem Jahr ab. Ein Kalendereintrag zur Erneuerung lohnt sich.
3. **Worker veröffentlichen** (aus diesem Ordner, Wrangler 4.36 oder neuer):

   ```bash
   npx wrangler secret put GITHUB_TOKEN
   npx wrangler deploy
   ```

   `wrangler.jsonc` hängt den Worker an `docs.second-ride.de/api/feedback`. Das setzt voraus, dass `second-ride.de` im selben Cloudflare-Konto liegt. Wenn nicht, den Block `routes` anpassen oder den Worker unter eigener Adresse veröffentlichen und die Adresse zusätzlich in `ALLOWED_ORIGINS` und im `endpoint` berücksichtigen.
4. **Formular einschalten:** In `mkdocs.yml` unter `extra.feedback` die Zeile `endpoint: /api/feedback` eintragen (nicht mehr auskommentiert). Nach dem nächsten Deploy der Doku erscheint das Formular.
5. **Testen:** Auf einer beliebigen Doku-Seite eine Rückmeldung abschicken. Danach muss in GitHub ein Issue mit dem Label `doku-feedback` stehen.

## Was der Worker prüft

- Herkunft: nur Anfragen von `ALLOWED_ORIGINS` (`https://docs.second-ride.de`).
- Text: 10 bis 2000 Zeichen, höchstens zwei Links, Name höchstens 60 Zeichen.
- Seite: muss unter `SITE_URL` liegen. Suchparameter werden entfernt.
- Bots: verstecktes Feld (Honigtopf) und eine Mindestzeit von 1,5 Sekunden zwischen erstem Klick ins Formular und Absenden.
- Menge: je Absender 3 Rückmeldungen pro Minute, insgesamt 20 pro Minute (je Rechenzentrum gezählt).
- Entschärfung: `@Name` wird so verändert, dass GitHub niemanden benachrichtigt, `<` wird maskiert.

Titel und Text des Issues baut der Worker selbst, ungeprüft übernommen wird nichts.

## Datenschutz

Rückmeldung und Name landen in einem **öffentlichen** Issue. Das steht im Formular. Der Worker speichert nichts außer dem Issue, die IP-Adresse wird nur für den Mengenzähler von Cloudflare genutzt. Wenn ihr statt öffentlicher Issues ein privates Repository nutzen wollt, genügt es, `GITHUB_REPO` in `wrangler.jsonc` zu ändern.

## Tests

```bash
node --test feedback-worker/test/worker.test.mjs
```

Die Tests laufen ohne Netz, GitHub wird nachgebildet. Sie prüfen Herkunft, Pflichtfelder, Spam-Schutz, Entschärfung und Fehlerfälle.

## Ausbau

Naheliegend wäre, markierten Text auf der Seite mitzuschicken ("diese Stelle ist falsch") und im Issue zu zitieren. Das Formular und der Worker müssten dafür nur ein weiteres Feld `quote` kennen.
