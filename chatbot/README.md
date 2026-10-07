# Chat-Assistent der Doku (Typebot "Second Ride FAQs")

Der Chat-Button unten rechts auf docs.second-ride.de öffnet einen Typebot-Bot. Die Einbindung steht in `docs/javascripts/typebot.js`, der Bot selbst in Typebot (typebot.second-ride.de, veröffentlicht unter `bot.second-ride.de`, Public ID `faqs`).

## Wie der Bot arbeitet

1. Beim Start lädt ein Webhook-Block `https://docs.second-ride.de/llms-bot.txt` in die Variable `FAQs`.
2. Der Block "Create chat completion" schickt `system-prompt.txt` (mit der Doku an der Stelle `{{FAQs}}`) plus den Gesprächsverlauf an das Modell.
3. Die Antwort wird als Text-Bubble angezeigt und an den Verlauf (`Chat History`) angehängt.

## Wissensbasis: `llms-bot.txt`

Erzeugt bei jedem `mkdocs build` von `hooks/llms_bot.py` aus den Markdown-Quellen:

- nur Deutsch, Reihenfolge FAQ, Bedienungsanleitung, Umbauanleitung, Entwickler
- pro Seite Titel mit Navigationspfad (zum Beispiel "Umbauanleitung > MID50 > Schwalbe"), Bereich und echte URL
- hinter jeder Überschrift der echte Anker (`[#anker]`), damit der Bot Abschnitte korrekt verlinkt
- ohne Bilder, HTML-Tabellen und Tabellen-Padding

`llms-full.txt` und `/all-docs` bleiben unverändert für andere Nutzer.

## Design

Button und Fenster werden von `docs/stylesheets/chatbot.css` gestaltet. Der Typebot-Bubble liegt in einem Shadow-DOM, `docs/javascripts/typebot.js` hängt das Stylesheet deshalb dort ein. Die Datei nutzt die Variablen `--sr-*` aus `theme.css`, die in den Shadow-DOM vererbt werden. Der Chat folgt dadurch dem Hell/Dunkel-Schalter der Doku und neuen Design-Werten automatisch.

Im Typebot-Theme ist als Schrift "Custom" mit `Nunito Sans Variable` eingetragen (ohne CSS). So lädt der Bot keine Schrift von Google oder bunny.net, sondern nutzt die selbst gehostete der Doku.

## Einrichtung in Typebot

1. **Zugangsdaten anlegen** (Block "Generate Assistant Message", Feld Account, "Add new"): API key aus Google AI Studio, Base URL `https://generativelanguage.googleapis.com/v1beta/openai/`. Das ist die OpenAI-kompatible Schnittstelle von Gemini.
2. Modell im Block auf `gemini-3.5-flash-lite` setzen. Messung am 07.10.2026 mit derselben Frage über denselben Typebot-Weg: `gemini-3.5-flash-lite` 1,8 s (kleine Quelle) bzw. 2,9 s (alte Voll-Doku, ca. 200k Tokens), `gemini-3.8-flash` 35 bis 56 s (denkt lange nach), `gemini-3.1-pro-preview` "429 Too Many Requests" (vermutlich kein bezahltes Kontingent). Die Verzögerung liegt am Modell, nicht an Typebot.
3. System-Prompt: Inhalt von `system-prompt.txt` (die letzte Zeile `{{FAQs}}` bleibt).
4. Dialogue-Variable `Chat History` darf **nicht** mit der Begrüßung beginnen. Der Dialogue-Block vergibt Rollen nach Index (gerade User, ungerade Assistant). Steht die Begrüßung vorn, sind alle Rollen vertauscht.
5. Webhook-URL auf `https://docs.second-ride.de/llms-bot.txt`.
6. Erst testen (Test-Button im Editor), dann Publish.

## Kurztest per Kommandozeile

```bash
SID=$(curl -s -X POST https://bot.second-ride.de/api/v1/typebots/faqs/startChat -H "Content-Type: application/json" -d '{"isOnlyRegistering":false}' | python3 -c "import sys,json;print(json.load(sys.stdin)['sessionId'])")
curl -s -X POST https://bot.second-ride.de/api/v1/sessions/$SID/continueChat -H "Content-Type: application/json" -d '{"message":"Welche Reichweite hat das MID50 Kit?"}'
```

Enthält die Antwort ein Feld `logs`, ist ein Fehler aufgetreten (zum Beispiel ungültiger API-Key).
