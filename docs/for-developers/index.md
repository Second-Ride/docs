# Intro für Entwickler

Willkommen im Entwicklerbereich von **Second Ride**.  
Unsere Mission ist es, bestehende Fahrzeuge durch Elektrifizierung nachhaltig zu machen – und dabei setzen wir bewusst auf **Open Source**.  

Wir glauben, dass Innovation schneller voranschreitet, wenn sie nicht hinter verschlossenen Türen geschieht. Besonders in zwei Bereichen freuen wir uns über aktive Beiträge unserer Community:
- **Integration unserer Umbaukits in neue Fahrzeugmodelle**  
- **Entwicklung von Erweiterungen wie Displays, Soundmodulen, IoT-Funktionen, Schaltgetriebe-Simulatoren ...**  

## Motorsteuergerät des MID50 Antrieb

Beim Motorsteuergerät haben wir bewusst auf das Open Source Projekt [VESC](https://vesc-project.com/) gesetzt. Es ist eines der am weitest entwickelsten und Funktions-rechsten Motorsteuergeräte auf dem Markt. Das VESC Projekt macht vorallem die geniale Software aus. Softwareseitig sind endlose Weiterentwicklungen basierend auf dieser Plattform denkbar.

<p float="left">
  <img src="/docs/for-developers/img/Desktop.jpg" width="45%" />
  <img src="/docs/for-developers/img/VESC Tool_on_phone_316_0.jpg" width="45%" />
</p>

## Mechanische Integration in Fahrzeuge aller Art

Wir haben den MID50 Antrieb und Akku so entwickelt, dass mit einfach zu entwickelnden und fertigenden Adaptern die Module in quasi alle Fahrzeug im Hubraumbereich bis 125ccm und mit Ketten oder Riementrieb integriert werden können. Damit ihr nicht darauf warten müsst, dass wir diese Adapter für eure jeweiligen Fahrzeuge entwickeln, stellen wir alle Ressourcen bereit die es dafür braucht. Dies inkludiert:
- 3D Modelle von Motor und Akku
- 2D Zeichnungen mit Bemaßung des Anschlusspunkte
- Zeichnungen der bereits entwickelten Adapterteile zur Referenz 
- 3D Scans von Fahrzeugen (wenn ihr Zugriff auf einen 3D Scanner habt fügt eure Modelle ebenso hier hinzu)

## Wie wir trotz Open Source straßenverkehrskonform, sicher und haftbar bleiben

Es war eine schwierige Aufgabe MID50 so zu gestalten, dass wir einerseits euch möglichst viele Freiheiten lassen können, andererseits aber 
- keine Gefahr durch gefährliche Modifikation des Akkus ausgehen kann, 
- wir das System sicher gegen Tuning nach der Änderungsabnahme machen (Anforderung für die Zulassung), 
- wir nicht mit Garantiefällen oder Kundensupport überhäuft werden, welche durch Modifikation des System entstehen 

### 1. Sicherheit
Lithium Ionen Akkus sind, wenn man sie innerhalb ihrer elektrischen, thermischen und mechanischen Grenzen betreibt heutzutage sehr sicher. Die Brände von denen man leider immer wieder liesst sind unserer Erfahrung nach oft darauf zurück zu führen, dass mindestens einer dieser drei Grenzen nicht eingehalten wurde. Wir haben uns daher entschieden, den Akku inkl. BMS komplett closed Source zu gestalten und bitten Euch das zu respektieren. 

Auch von falscher Konfiguration des Motors kann eine große Gefahr für dich und andere ausgehen. Unserer Ansicht nach sind diese Risiken aber für Laien aber besser einschätzbar. Trotzdem seit bitte extrem vorsichtig und bedenkt, dass jegliche sicherheitsrelevante Änderungen zum Erlischen der Betriebserlaubnis im Straßenverkehr führen (siehe nächstes Kapitel).

### 2. Straßenverkehrskonformität

Im deutschem und EU-Recht ist vorgeschrieben, dass wenn Fahrzeuge einmal für den Straßenverkehr zugelassen wurden, die Leistung und Geschwindigkeit gegenüber den in den Fahrzeugpapieren angegebenen Werten nicht mehr gesteigert werden dürfen, ohne eine Änderungsabnahme oder Neuzulassung durchzuführen. 

Daher haben wir zusätzlich zu dem Open Source Motorsteuergerät ein weiteres closed source Steuergerät namens "Malcolm" im Antrieb untergebracht, welches genau das sicherstellt. Wie in der Anleitung beschrieben (tbd), kann nach Kauf des Umbaukits die Drosselung frei gewählt werden und entweder vorrübergehend oder endgültig gespeichert werden. Ist deine Drosselung endgültig gespeichert und du versucht eine höhere Drehzahl oder höhere Leistung in dem VESC Motorsteuergerät zu programmieren, wird der Akku die Stromzufuhr des Akkus abschalten. Willst du also zb deinen Antrieb nur für Offroad-Einsatz nutzen, brauchst du deinen Antrieb nie endgültig zu drosseln und hast abgesehen von den Limits des Akkus keine Begrenzungen.

Selbst wenn ihr aber nicht Leistung und Geschwindigkeit verändert, aber sonst irgendeine sicherheitsrelevante Änderung vornehmt, erlischt eure Betriebserlaubnis gemäß StVZO §19 (2) (solang ihr denn vorher überhaut eine hattet). Ggf. könnt ihr die Betriebserlaubnis dann über eine Änderungsabnahme zurück erlangen. Sprecht dafür bitte mit den technischen Sachverständigen eurer Wahl (TÜV, Dekra, KÜS, ...).

### 3. Haftung / Gewährleistung / Garantie

Zu guter letzt müssen wir uns auch noch davor schützen, für Schadensfälle, für die wir gar nichts können, haften zu müssen. Es muss klar sein, dass Modifikationen an Software und Hardware schnell zu Schäden an unserem Produkt, aber auch zu Personen- und Sachschäden führen kann. 
 
- **Jegliche Veränderungen von Software oder Hardware durch Dritte** (außer Second Ride) führen zum **Erlöschen der Haftung und Gewährleistung**.  Solche Änderungen bergen **erhebliche Risiken** für Personen und Sachgüter.  
- **Ausnahme:** Updates, die offiziell von Second Ride stammen, dürfen selbstverständlich auch durch Dritte (z. B. Händler, Werkstätten) aufgespielt werden – außer wir kommunizieren explizit etwas anderes.  

**Software umfasst insbesondere:**
- Firmware  
- Parameter  
- Steuerungs- und Konfigurationssoftware aller elektronischen Steuergeräte (insbesondere VESC-bezogen)

**Hardware umfasst insbesondere:**
- Modifikationen an der Antriebseinheit  
- Anschließen oder paralleles Schalten von Fremdakkus  
- Weitere Änderungen, die sicherheitsrelevante Komponenten betreffen  

## Wenn ihr in die Weiterentwicklung einsteigt

Wir freuen uns sehr über euren Beitrag zur Weiterentwicklung von Second Ride. Bitte seid euch jedoch bewusst, dass ihr mit eigenen Änderungen an Soft- oder Hardware folgende Punkte in Kauf nehmt:

1. **Erlöschen der Haftung bzw. Garantie**  
2. **Erlöschen der Betriebserlaubnis**  
3. **Erhebliche Risiken für Personen und Sachgüter**  
4. **Pflicht, Risiken und Warnungen transparent aufzuzeigen**  