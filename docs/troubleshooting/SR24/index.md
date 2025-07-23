# Fahrzeug fährt nicht

### Vorraussetzungen:
Stelle sicher, dass folgende Bedingungen vorherrschen:
1. Sitzbank mehr als 10% aufgeladen 
2. Sitzbank ist mit Deinem Antriebsmodul verbunden
3. Armaturen sind mit Deinem Antriebsmodul verbunden

![system-on-or-off (3)](https://github.com/user-attachments/assets/5b0ea9d6-8f0c-41b0-a053-96a9db88a894)


## Fahrzeug fährt nicht - Betätigung des Zündschloss führt aber zu leuchtendem Taster
### der Scheinwerfer geht an, nachdem das Zündschloss betätigt wurde
Dreht der Motor, wenn Du das System in den aktiven Fahrbetrieb versetzt und Gas gibst?

Den aktiven Fahrbetrieb erreichst Du durch Betätigung des Zündschlosses und anschließendes Drücken des pulsierenden Tasters. Der aktive Fahrbetrieb wird dann durch dauerhaftes Leuchten oder schnelles Blinken (->Notlauf) der Ring-LED bestätigt.

#### Der Motor dreht
Kontaktieren Sie uns

#### Der Motor dreht **nicht**
Welches Blinkmuster siehst Du am Antriebsmodul unter der horizontalen Abdeckung?
(Es ist nicht notwendig diese abzuschrauben. Das farbige Licht sollte in einer etwas abgedunkelten Umgebung gut sichtbar sein.)

Das rote Licht unter der Abdeckung zeigt an, dass der Motor das Signal empfängt, es würde gebremst werden. Folglich lässt der Motor es nicht zu, dass Gas gegeben werden kann. 

##### Rotes Licht ist sichtbar

Das rote Licht unter der Abdeckung zeigt an, dass der Motor das Signal empfängt, es würde gebremst werden. Folglich lässt der Motor es nicht zu, dass Gas gegeben werden kann. 

###### Dein Bremslicht leuchtet nur wenn Du bremst

**Bremssignal aktiv trotz funktionierendem Bremslicht**

Um auszuschließen, dass der Fehler in unserem Antriebsmodul und nicht in Deiner Bordelektronik liegt, kannst Du einmal den folgenden Schritt befolgen:

Schließe das "Bremssignalkabel" (schwarz mit weißen Steckern) direkt an eines unserer roten "+12V" Kabel an, welche vom Motor kommen. 

Achtung! Damit umgehst Du den Bremslichtschalter, was dazu führt, dass der Motor auch noch Leistung abgeben kann, wenn Du die Bremse betätigst. Damit hast Du keine Möglichkeit mehr falls der Motor ungewollt Leistung abgibt ihn abzuschalten. Diese Maßnahme sollte also nur zu Diagnosezwecken, nicht aber zum dauerhaften Gebrauch umgesetzt werden.

Wenn Die Probleme nun nicht mehr auftreten, ist nachgewiesen, dass Du entweder den Bremslichtschalter falsch verkabelt hast, oder dein Bremslichtschalter falsch eingestellt ist. sporadisch das Signal gibt es würde gebremst werden. Falls Du noch den Bremslichtschalter in der Hinterradnabe verwenden solltest, empfehlen wir Dir dringend einen [externen Bremslichtschalter](https://www.google.com/search?q=simson+externer+bremslichtschalter) zu verbauen. In beiden Fällen sollte das Problem aber behoben werden können, indem Du den Bremslichtschalter neu einstellst. 

Wenn Du Dir das selbst nicht zutraust oder dabei Hilfe benötigst, kontaktiere eine unserer [Partnerwerkstätten](https://second-ride.de/service).

**Bremssignalkabel falsch angeschlossen**

Es scheint so, als sei Dein Bremssignalkabel (einpoliges schwarzes Kabel welches direkt unter dem Motor angeschlossen wird) falsch angeschlossen. Damit der Motor die Leistungsabgabe freigibt, und die rote LED abschaltet, müssen am Bremssignalkabel 12V anliegen. Das folgende Schaltbild soll vereinfacht zeigen, wie das Bremssignalkabel angeschlossen werden sollte. Ist der Bremslichtschalter offen, dann wird das Bremssignalkabel über die Bremsleuchte mit 12V versorgt und der Motor wird freigegeben. Ist der Bremslichtschalter geschlossen, dann liegt Fahrzeugmasse bzw. 0V am Bremssignalkabel an.


### Im Antriebsmodul ist rote LED zu sehen


## Fahrzeug fährt nicht - Betätigung des Zündschloss führt NICHT zu leuchtendem Taster


# System lässt sich nicht ausschalten

## System an auch ohne Armaturen

Wenn auch mit nicht angeschlossenen Armaturen das System weiterhin anbleibt, ist ausgeschlossen, dass die Armaturen verantwortlich sind. Der Fehler lässt sich also auf Antriebsmodul und Sitzbank eingrenzen.

### Akkuspannung liegt an auch ohne Antriebsmodul

Ziehe den Hauptstecker aus der Sitzbank und miss mit einem Spannungsmessgerät die Ausgangsspannung an dem Sitzbankstecker. Ist diese über 42V bei einem Akku mit 50V Nennspannung (siehe Beschriftung auf Sitzbank) oder über 60V bei einem Akku mit 72V Nennspannung, dann bedeutet das, dass das Batteriemanagementsystem (BMS) die Spannung nicht korrekt abschaltet. Andernfalls liegt eine Spannung über 0V aber unter den besagten Grenzen an.

Wenn das Batteriemanagementsystem (BMS) die Spannung nicht korrekt abschaltet, müssen wir die Sitzbank bei uns reparieren.

### Akkuspannung liegt ohne Antriebsmodul nicht an

Du hast das Problem nun auf das Antriebsmodul eingegrenzt. Es wird entweder an Günther (SRZ00743) liegen, oder an einer defekten Hauptschlagader (SRZ00041 oder SRZ00613 bei Duos).

## System geht aus, wenn Armaturen abgesteckt werden

Wenn das System ohne Betätigung des Zündschlosses an ist und ausgeht sobald du die Armaturen absteckst, dann bedeutet das, auf der Key-Leitung in den Armaturen ist irgendwo ein Kurzschluss.

# Licht geht nicht an


