## Was ist das MID50-Kit?
Das MID50-Kit ist ein Umbausatz für Mittelmotor-Fahrzeuge (<=125 ccm), der primär auf 50ccm-Fahrzeuge wie Simson ausgelegt ist, um sie in ein straßenlegales Elektromoped umzuwandeln.

## Mit welchen Fahrzeugen ist das MID50-Kit kompatibel?
Aktuell ist das MID50-Kit Plug & Play nur mit der Simson S50, S51 und S70 sowie der Schwalbe KR51/1 und KR51/2 kompatibel. Die passenden Kits findest du im [Shop](https://second-ride.de/de/moped-elektro-umbausatz).

Alle anderen Mittelmotorfahrzeuge kannst du mit dem [Adapt it Yourself Kit](https://second-ride.de/de/moped-elektro-umbausatz/mid50-umbaukit-adapt-it-yourself) selbst adaptieren. Alle dafür nötigen Ressourcen haben wir Open Source in unserer [technischen Dokumentation](../../for-developers/index.md) bereitgestellt.

Du möchtest, dass wir ein Adapterkit für dein Fahrzeug entwickeln? Dann lege eine [Reservierung](https://second-ride.de/reservierungen) an. Damit signalisierst du uns Interesse an deinem Modell und beschleunigst die Entwicklung. Du stehst damit auf der Warteliste für dein Fahrzeug. Sobald wir das Adapterkit entwickelt haben, wird dir die Anzahlung bei der finalen Bestellung angerechnet.

### Was ist mit Fahrzeugen, die die Kette links haben (z.B. Kreidler, Zündapp)?
Der MID50-Motor ist so konstruiert, dass er auch "auf dem Kopf" montiert werden kann. Damit ist er grundsätzlich auch für Fahrzeuge mit Kette auf der linken Seite kompatibel. Spezifische Adapterkits für diese Modelle sind in Planung.

## Was ist alles im MID50 Basiskit enthalten (ausgenommen AIY)?
Das Kit umfasst das Antriebsmodul, den Akku und den Motoradapter. Modellspezifisch sind außerdem Akkuhalterung, Gaszug Sensor, Armaturen, Kabel und ein Teilegutachten (für Simson) enthalten. Die vollständige Liste steht in der Umbauanleitung unter "Lieferumfang": [Schwalbe](../../conversion-manual/MID50/01-schwalbe/index.md#lieferumfang) und [S50/S51/S70](../../conversion-manual/MID50/02-s50-s51-s70/index.md#lieferumfang).

Was du darüber hinaus für den Umbau benötigst (zum Beispiel Seitendeckel, Zylinder und Zylinderkopf vom Originalmotor, 12V Glühbirnen und Werkzeug), steht in der Umbauanleitung unter "Voraussetzungen": [Schwalbe](../../conversion-manual/MID50/01-schwalbe/index.md#voraussetzungen) und [S50/S51/S70](../../conversion-manual/MID50/02-s50-s51-s70/index.md#voraussetzungen).

### Ist eine neue Kette enthalten?
Nein. Der MID50 nutzt die originale Simson Werksnorm (420er Teilung, aber schmaler). Da sich die Position des Ritzels nicht ändert, kannst du deine originale Kette weiterverwenden.

## Was kann ich alles von meinem Verbrennungsmotor weiterverwenden?
Du kannst sowohl die Seitendeckel als auch den Zylinder und den Zylinderkopf weiterverwenden. Es wird lediglich der Motorblock an sich ausgetauscht. So bleibt die originale Optik erhalten.

## Kann ich den MID50-Akku an meinem alten Kit (SR23 oder SR24) nutzen?
Aktuell noch nicht. Wir arbeiten daran, aber die Kompatibilität ist bisher nicht hergestellt. In Zukunft wollen wir MID50-Akkus an SR23- und SR24-Antrieben ermöglichen, sodass du die Reichweite deines Kits mit MID50-Akkus aufstocken kannst.

## Welche maximale Leistung ist mit MID50 möglich?
Maximal sind ca. 14 kW (20 PS) Spitzenleistung und bis zu 2250 U/min an der Abtriebswelle möglich.
Die Dauerleistung liegt bei ca. 3-4 kW (bei 80 km/h Fahrtwindkühlung bis ca. 5 kW).

## Wie funktioniert die Drosselung für die Straßenzulassung?
Das Kit wird mit einer temporären Drosselung ausgeliefert (noch kein endgültig gespeichertes Limit). Die Konfiguration erfolgt über eine WLAN-Verbindung direkt zum Fahrzeug (keine App notwendig). Hier kann die Leistung entweder temporär angepasst oder endgültig (für die Straßenzulassung) festgelegt werden.

## Kann ich die Drosselung später ändern?
Nach der endgültigen Drosselung (z.B. auf 45 oder 60 km/h) kann die Leistung über unsere App (die Unterstützung für MID50 ist für Frühling 2027 geplant) zwar jederzeit weiter **reduziert** werden (z.B. für Fahranfänger), aber **nicht mehr über den gesetzten Grenzwert hinaus gesteigert** werden. Dies ist eine gesetzliche Anforderung.

## Kann ich das Fahrzeug ungedrosselt oder mit 15 PS zulassen (Leichtkraftrad, A1)?
Ja, das geht, solange der Prüfer das Fahrzeug für diese Leistung als geeignet ansieht. Dafür müssen zum Beispiel Fahrwerk und Bremsanlage auf die höhere Leistung ausgelegt sein. Welche Leistung das Teilegutachten abdeckt, steht unter [Antrieb drosseln](../../conversion-manual/MID50/throttling/how-to-throttle-your-drive/index.md). Den Ablauf der Abnahme findest du unter [Zulassung & Abnahme](../../conversion-manual/modification-approval-and-homologation/index.md).

## Wie weit komme ich mit dem MID50 Akku?
Mit einem 2 kWh Akku beträgt die Reichweite für ein Zweirad mit 35km/h Durchschnittsgeschwindigkeit und einem Fahrer ca. 55 km. Mit zwei Akkus (4 kWh) werden bis zu 110 km erreicht. Die Reichweite wurde unter realen Bedingungen im Stadtverkehr getestet.

## Können weitere Akkus nachgerüstet werden?
Ja. Je nach Modell deines Mopeds können mehrere Akkus Platz im Rahmen deines Mopeds finden. Zudem können noch weitere Akkus in Seitentaschen verstaut werden. Rein von dem elektrischen System ließen sich 20 Akkus parallel schalten.

### Besonderheit Schwalbe (KR51)
Aktuell passt in die Schwalbe nur **ein** Akku. Eine Lösung für einen Zweitakku (z.B. Gepäckträgerhalterung) ist für Frühling 2027 geplant.

### Besonderheit S50/S51/S70
Hier können bis zu zwei Akkus direkt im Herzkasten (rechts und links) untergebracht werden.

## Wie lange dauert das Laden?
Die Ladezeit hängt vom Ladegerät ab. Mit einem 350W Ladegerät können ca. 9km die Stunde geladen werden. Mit einem 1200W Ladegerät sind es ca. 25km die Stunde.

## Gibt es Rekuperation (Energierückgewinnung)?
Ja, beim Gaswegnehmen wandelt das System die Energie in Strom um und lädt damit den Akku.

## Was ist das Besondere an der MID50 Akku-Technologie?
In dem MID50 Akku sind Lithium Ionen 21700er Rundzellen mit NMC-Kathoden verbaut. Dank unserer eigens entwickelten Technologie können diese nun im Fall eines Ausfalls einzeln ersetzt werden. So muss nicht der ganzen Akku ausgetauscht werden, nur weil eine Zelle kaputt ist.

## Wie läuft die Zulassung ab?
Im Lieferumfang des Second Ride Umbausatzes ist ein Teilegutachten enthalten. Nach erfolgreichem Umbau gehst du zu deinem örtlichen technischen Dienst oder deiner technischen Prüfstelle (TÜV, Dekra, etc.), welche dein Fahrzeug auf allgemeine Fahrtüchtigkeit hin überprüft (beispielsweise: Ist der Umbausatz fachgerecht verbaut, wie ist der allgemeine Fahrzeugzustand?, ...). Der Umbausatz selbst wird technisch nicht getestet - die für eine Zulassung entscheidenden Tests absolvieren wir und werden in dem Mustergutachten offiziell bestätigt. Nach erfolgter Abnahme steht noch ein formaler Vorgang an: der Gang zur örtlichen Zulassungsstelle, zur Aktualisierung der Betriebserlaubnis.

## Gibt es eine Garantie?
Für die Gewährleistung gelten die in Deutschland üblichen gesetzlichen Bestimmungen. Second Ride bietet zusätzlich eine Garantie für die Umbausätze von 12 Monaten.

## Wird es weiterhin SR24 Umbaukits geben?
Nein, MID50 hat SR24 komplett ersetzt. Wenn du noch ein altes Kit haben willst, frag gerne in der Community nach: [Gehe zu Discord](https://second-ride.de/community-gast)

## Was ist der Unterschied zwischen einem M50 und M500 Adapterkit?
Der M50 ist der ältere Simson Motor, welcher in der S50 und KR51/1 verbaut wurde. Der M500 Motor wurde in der S51 und KR51/2 verwendet. Die Motoren hatten unterschiedliche Seitendeckel und Rahmenanschraubpunkte, weshalb wir unterschiedliche Adapterkits für die jeweiligen Seitenteile anbieten.

## Kann ich meinen Tacho weiterverwenden?
Um den Tachoantrieb direkt im rechten Seitendeckel zu nutzen, muss der Seitendeckel einen Schneckenradantrieb haben, welcher exakt konzentrisch mit der Abtriebswelle liegt. Dies ist nur bei den M500 Seitendeckeln der Fall. Wenn du M50 Seitendeckel verwenden willst, musst du auf einen Nebentachoantrieb oder einen digitalen Tacho mit Abnehmer am Vorderrad umrüsten.

## Ist das Laden direkt am Fahrzeug möglich?
Es wird auch für MID50 einen externen Ladeanschluss geben (Zubehör).

## Muss ich beim Umbau auf 12V die Hupe tauschen?
Nein. Erfahrungsgemäß funktionieren die originalen DDR 6V-Hupen auch problemlos und lautstark mit dem 12V-Bordnetz des MID50-Kits. Ein Austausch ist in der Regel nicht notwendig.

## Wann kommt die App für MID50?
Die App-Unterstützung für MID50 (inkl. Konfiguration und "Laden auf SOC-Ziel") ist für Frühling 2027 geplant. Zum Start können Grundeinstellungen über ein temporäres Interface vorgenommen werden.
