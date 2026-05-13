# Wie man die Drosselung überprüft

Diese Anleitung richtet sich an **amtlich anerkannte Sachverständige**, die gemäß § 19 Abs. 3 Nr. 4 StVZO eine Änderungsabnahme an einem mit dem **MID50 Umbaukit** der Second Ride GmbH elektrifizierten Kleinkraftrad durchführen.

Gemäß Punkt 4 des [Teilegutachtens Nr. 8123697374](../../../modification-approval-and-homologation/docs/Teilegutachten-MID50.pdf) (IFM, Institut für Fahrzeugtechnik und Mobilität) ist bei der Änderungsabnahme zu überprüfen:

- ob die **korrekte Höchstgeschwindigkeit und maximale Nennleistung** konfiguriert wurden
- ob die Konfiguration in den Status **„Endgültig gespeichert"** versetzt wurde

---

## Voraussetzungen

Für die Prüfung werden benötigt:

- Ein **WLAN-fähiges Endgerät** (Smartphone, Tablet oder Laptop)
- Das **[Teilegutachten](../../../modification-approval-and-homologation/docs/Teilegutachten-MID50.pdf)** mit den fahrzeugspezifischen Grenzwerten (liegt dem Fahrzeug bei)
- Die **Fahrzeugpapiere**, wenn Höchstgeschwindigkeit und Leistung nicht im Teilegutachten spezifiziert sind
- Ein **Maßband** von mindestens 2 Meter Länge und ein Stück Kreide o. Ä. zum Markieren von Untergrund und Reifen (benötigt für die Prüfung der konfigurierten Endgeschwindigkeit)

---

## Prüfablauf

### Schritt 1: Fahrzeug einschalten

Drehen Sie den Zündschlüssel in die **eingeschaltete Position**. Der Taster an der Armatur beginnt daraufhin zu pulsieren.

<p align="center">
  <img src="images/System-einschalten.gif" width="400" loading="lazy" alt="Fahrzeug einschalten: Zündschlüssel drehen, Taster beginnt zu pulsieren" />
</p>

### Schritt 2: Konfigurationsmodus aktivieren

Halten Sie den **pulsierenden Taster gedrückt**. Nach ca. 5 Sekunden wechselt das System in den Konfigurationsmodus. Sie erkennen dies an:

- einem charakteristischen **Doppelblinken** des Tasters (Doppelblinken, kurze Pause, Doppelblinken, …)
- einer **lila leuchtenden LED** am Antriebsmodul

### Schritt 3: Mit dem Fahrzeug-WLAN „SR Legal Limits" verbinden

Öffnen Sie auf Ihrem Endgerät die **WLAN-Einstellungen** und verbinden Sie sich mit dem Netzwerk:

!!! info ""
    Netzwerkname: **SR Legal Limits**

Ein Passwort ist nicht erforderlich. Sobald die Verbindung hergestellt ist, öffnet sich der **Legal Limit Konfigurator** automatisch in Ihrem Browser.

!!! tip "Konfigurator öffnet sich nicht automatisch?"
    Geben Sie folgende Adresse in Ihren Browser ein: http://192.168.12.1. Wichtig: Nutzen Sie http:// (nicht https://). Falls Ihr Browser eine Sicherheitswarnung anzeigt, klicken Sie auf „Weiter zur Seite" bzw. „Continue to site". Der Legal Limit Konfigurator sollte sich dann öffnen.

### Schritt 4: Status „Endgültig gespeichert" prüfen

Der entscheidende Prüfschritt ist die Verifikation, ob die Konfiguration **endgültig gespeichert** wurde. Der Konfigurator zeigt den aktuellen Speicherstatus klar an.

**Endgültig gespeichert:** Abnahme kann erteilt werden:

<p align="center">
  <img src="images/Antrieb endgültig gedrosselt.png" width="400" loading="lazy" alt="Ansicht des Konfigurators bei endgültig gespeicherter Konfiguration" />
</p>

**Noch nicht endgültig gespeichert:** Abnahme darf nicht erteilt werden:

<p align="center">
  <img src="images/Antrieb nicht endgültig gedrosselt.png" width="400" loading="lazy" alt="Ansicht des Konfigurators bei noch nicht endgültig gespeicherter Konfiguration" />
</p>

!!! danger "Achtung: Konfiguration nicht endgültig gespeichert"
    Wenn der Konfigurator anzeigt, dass die Konfiguration **noch nicht endgültig gespeichert** wurde, darf die Änderungsabnahme **nicht erteilt** werden. Der Fahrzeughalter muss zunächst die Konfiguration endgültig speichern und das Fahrzeug erneut zur Abnahme vorstellen.

### Schritt 5: Konfigurierte Werte und Kalibrierung prüfen

Im Konfigurator sind die fahrzeugspezifischen Grenzwerte eingetragen. Gleichen Sie diese mit den Angaben im Teilegutachten und den Fahrzeugpapieren ab:

| Parameter | Anforderung |
|---|---|
| Höchstgeschwindigkeit | Gemäß Teilegutachten oder Fahrzeugpapieren |
| Maximale Nennleistung | Gemäß Teilegutachten oder Fahrzeugpapieren; das bis zu 1,4-Fache der eingetragenen Leistung ist zulässig, maximal 4 kW bei Kleinkrafträdern |

Zur physischen Verifikation der Übersetzung und des Abrollumfangs auf **„Kalibrierung überprüfen"** tippen:

<p align="center">
  <img src="images/Kalibrierung prüfen 10.png" width="400" loading="lazy" alt="Button: Kalibrierung überprüfen" />
</p>

!!! warning "Wichtig: Fahrer muss aufgesessen sein"
    Die Messung muss mit aufgesessenem Fahrer durchgeführt werden, damit der Abrollumfang unter realen Bedingungen erfasst wird.

Der Konfigurator führt selbsterklärend durch den Prozess:

- Reifen und Boden an derselben Stelle mit Kreide markieren
- Fahrzeug genau eine Radumdrehung nach vorne schieben, das System erfasst Motorumdrehungen automatisch
- Gemessene Distanz in cm eintragen
- Das System berechnet die tatsächliche Höchstgeschwindigkeit; diese muss mit den Fahrzeugpapieren übereinstimmen

---

## Hintergrund: Manipulationssicherheit

Der Hersteller Second Ride GmbH garantiert, dass nach dem endgültigen Speichern die konfigurierten Werte durch den Nutzer nicht mehr erhöht werden können. Das Schutzpasswort ist auslese- und manipulationssicher in einer **E-Fuse** im Mikroprozessor des Antriebsmoduls gespeichert. Dies entspricht dem aktuellen Stand der Technik zur Manipulationssicherheit ([Teilegutachten Nr. 8123697374](../../../modification-approval-and-homologation/docs/Teilegutachten-MID50.pdf), Punkt 4).
