# Community Erweiterungen für SR23 und SR24 Umbaukits
Es gibt bereits viele tolle Erweiterungen für SR23 und SR24 Umbaukits, die aus der Community entwickelt wurden. Bisher wurden diese nur auf [unserem Discord-Server](https://second-ride.de/community-gast) dokumentiert. Wir bitten die Verantwortlichen in der Community ihre Projekte hier zur besseren Übersicht zu dokumentieren.

!!! info "Projekte aus der Community"
    Die Projekte auf dieser Seite stammen von Mitgliedern der Community. Second Ride hat sie nicht geprüft und pflegt sie nicht. Nachbau auf eigene Verantwortung.

## Touchdisplay in den Armaturen
![Touchdisplay in den Armaturen](touchdisplay-armaturen.jpg)
[Zum Discord Thread  :simple-discord:](https://discord.com/channels/985901178254659615/1351281991332659210){ .md-button .md-button--primary }
[Zur Github Repo  :simple-github:](https://github.com/kilipet75/SRdisplay/tree/main?tab=readme-ov-file){ .md-button .md-button--primary }

## Zusatzanzeige mit Raspberry Pico und OLED
Ein Raspberry Pi Pico liest über die USB-Schnittstelle Daten vom SR24-Steuergerät ein und zeigt sie auf einem kleinen OLED-Display an. Das Projekt stammt von [chrisob111](https://github.com/chrisob111), der auch die Fotos und den Schaltplan auf dieser Seite beigesteuert hat.

![Zusatzanzeige im Tacho einer SR50: das OLED sitzt dort, wo vorher die Leerlaufanzeige war](zusatzanzeige-gesamtansicht.jpg)

Im Beispiel sitzt das Display an der Stelle der Leerlaufanzeige im Tacho einer SR50. Alle Bauteile sind im Tachogehäuse untergebracht.

### Was angezeigt wird
Sobald der Motor läuft, liest der Pico sämtliche Daten mit, die das Steuergerät seriell über USB sendet.

| Bildschirm | Anzeige |
|---|---|
| 1 | Geschwindigkeit, Akkutemperatur, Restreichweite, Akkustand |
| 2 (optional, mit Taster) | Balken für die Momentanleistung, Verbrauch, Momentanleistung |
| 3 (optional, mit Taster) | Spannung, Strom |

Mit einem optionalen GPS-Modul wird zusätzlich die Uhrzeit angezeigt. Mit dem Taster schaltest du zwischen den Bildschirmen um.

### Das brauchst du
- Raspberry Pi Pico (die Version mit dem RP2040-Chip, im Projekt als "Pico 1" bezeichnet), zum Beispiel von [Berrybase](https://www.berrybase.de/raspberry-pi-pico-rp2040-mikrocontroller-board)
- [Waveshare 0,91" OLED](https://www.berrybase.de/0.91-128x32-oled-display-modul-einfarbig-weiss-i2c-interface) (128 x 32 Pixel, I2C)
- [USB-OTG-Adapter](https://www.berrybase.de/usb-2.0-hi-speed-adapterkabel-0-20m-a-buchse-micro-b-stecker) von Micro-USB-Stecker auf USB-Buchse, damit der Pico am USB-Kabel des SR24 hängen kann
- optional: ein Taster
- optional: [M5Stack GPS-Einheit v1.1](https://openelab.de/products/m5stack-gps-bds-einheit-v1-1?_pos=4&_psq=gps&_ss=e&_v=1.0) oder ein anderes GPS-Modul. Bei einem anderen Modul musst du die Baudrate gegebenenfalls anpassen.

Die Links sind Beispiele für die Teile, die im Projekt verbaut wurden.

### Anschluss
Der Pico wird so verdrahtet:

| Bauteil | Anschluss am Bauteil | Anschluss am Pico |
|---|---|---|
| Display | VCC | 3V3 (Pin 36) |
| Display | GND | GND (Pin 8) |
| Display | SDA | GPIO4 (Pin 6) |
| Display | SCL | GPIO5 (Pin 7) |
| GPS (optional) | GND | GND (Pin 38) |
| GPS (optional) | 5V | VBUS (Pin 40) |
| GPS (optional) | RXD | GPIO17 (Pin 22) |
| GPS (optional) | TXD | GPIO16 (Pin 21) |
| Taster (optional) | Pin 1 | GPIO21 (Pin 27) |
| Taster (optional) | Pin 2 | GND (Pin 28) |

![Stromlaufplan: Display, GPS-Modul und Taster am Raspberry Pi Pico](zusatzanzeige-stromlaufplan.png)

Im Original-Schaltplan steht bei der Display-Leitung "SDL". Gemeint ist SCL, die Taktleitung des I2C-Busses.

### Software aufspielen
1. Stecke den Pico mit **gedrückter BOOTSEL-Taste** an deinen PC. Er meldet sich als Massenspeicher.
2. Lade die Datei `SR24_OLED.uf2` aus dem [build-Ordner des Projekts](https://github.com/chrisob111/SR24_oled/tree/SR24_oled/build) herunter. Im Ordnerfenster ist sie auf dem Bild unten rot umrahmt.
3. Ziehe die Datei per Drag and Drop auf den Pico. Sobald sie kopiert ist, startet der Pico neu.
4. Verbinde den Pico mit dem USB-Kabel des SR24.

![Die Datei SR24_OLED.uf2 im build-Ordner, rot markiert](zusatzanzeige-uf2-datei.png)

### Bedienung
Ein kurzer Druck auf den Taster schaltet zwischen den Bildschirmen um. Hältst du den Taster mindestens 2 Sekunden gedrückt, startet der Pico im Bootmodus und meldet sich wieder als Massenspeicher am PC. So kannst du eine überarbeitete Software aufspielen, ohne an die BOOTSEL-Taste am Pico zu müssen.

### Einbau
Im Beispiel sitzen Pico, GPS-Modul und Display im Gehäuse des SR50-Tachos. Befestigt ist alles mit Heißkleber, Schaumstoffstücke polstern die Bauteile.

![Pico, GPS-Modul und OLED im geöffneten Tachogehäuse](zusatzanzeige-einbau.jpg)

### Weiterführende Links
[Zum Discord Thread  :simple-discord:](https://discord.com/channels/985901178254659615/1463626198453059796){ .md-button .md-button--primary }
[Zur Github Repo  :simple-github:](https://github.com/chrisob111/SR24_oled){ .md-button .md-button--primary }

Im GitHub-Projekt findest du außerdem den Quellcode, falls du die Anzeige anpassen möchtest.
