## VESC Motorsteuergerät/Inverter

Der VESC ist mit der Open-Source-Software **[VESC Tool](https://vesc-project.com/)** konfigurierbar. Änderungen an der Konfiguration dürfen ausschließlich innerhalb der gesetzlich zulässigen Grenzen vorgenommen werden! – diese werden durch **Malcolm, eine zus. Platine auf dem Inverter**, überwacht und durchgesetzt.

MID50-spezifische Funktionen (z.B. Leistungsregelung, Verarbeitung von Sensorsignalen und Steuerlogik) sind mittels **LispBM** implementiert – einer Lisp-Variante, die direkt auf dem VESC ausgeführt wird. Die allgemeine Dokumentation dazu findet sich im [LispBM README von Benjamin Vedder auf GitHub](https://github.com/vedderb/bldc/blob/master/lispBM/README.md#gpio).
Das [LispBM Projekt](https://www.lispbm.com/lispbm-reference-manual/html/) ist eine von Benjamin Vedder entwickelte, schlanke Lisp-Implementierung, die speziell für Microcontroller ausgelegt ist. Im VESC-Ökosystem ermöglicht LispBM es Entwicklern, eigene Steuerlogik direkt auf dem Inverter zu scripting – ohne Firmware-Neukompilierung, live über das VESC Tool ladbar und ausführbar. Damit lässt sich das Verhalten des Antriebs flexibel erweitern, z.B. durch benutzerdefinierte Regelkreise, Sensorauswertung oder Schnittstellenlogik.
Außerdem gibt es ein [LispBM GPT](https://chatgpt.com/g/g-6941305180a08191a2ac14a97ffe1bf4-vesc-lispbm-gpt), welches das mit KI unterstützte LispBM Software entwickeln ermöglicht.

### Verbindung mit VESC Tool herstellen

Um das VESC Tool mit dem Steuergerät zu verbinden, muss das Endgerät zunächst mit dem WLAN des Antriebsmoduls verbunden werden:

- **Netzwerkname:** VESC SR WIFI
- **Passwort:** `vescSRwifi`

Anschließend kann im VESC Tool eine Verbindung über WLAN hergestellt werden.