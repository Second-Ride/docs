# Fahrzeug fährt nicht

Stelle sicher, dass folgende Bedingungen vorherrschen:
1. Sitzbank mehr als 10% aufgeladen 
2. Sitzbank ist mit Deinem Antriebsmodul verbunden
3. Armaturen sind mit Deinem Antriebsmodul verbunden


## Fahrzeug fährt nicht - System lässt sich nicht einschalten & Fahrzeuglichter gehen an

Wenn das Zündschloss betätigt wird, sollte die LED des Tasters pulsieren und damit den inaktiven Fahrbetrieb anzeigen, wie in folgender Animation zu sehen:


<p align="center">
  <img src="https://github.com/user-attachments/assets/cea427ac-80f1-4483-a4a7-1f7d34043fc8" width="800">
</p>


Außerdem gehen die Scheinwerfer an wie hier zu sehen:

<p align="center">
  <img src="https://github.com/user-attachments/assets/f007ee1f-0c30-45a7-86ee-67346fe9fd5c" width="800">
</p>


Wenn das nicht der Fall ist, schau welche der folgenden Unterkapitel zutrifft.

### Fahrzeug fährt nicht - System lässt sich aber einschalten aber Fahrzeuglichter gehen nicht an

Deine 12V Versorgung vom Antriebsmodul scheint nicht zu funktionieren. Das könnte auch der Grund sein, warum das Fahrzeug nicht fährt: Um zu erkennen, dass der Fahrer nicht gerade nicht bremst, benötigt das Antriebsmodul nämlich 12V (wenn es über die App nicht anders konfiguriert ist). 

Prüfe mit einem Spannungsmessgerät, ob wenn du die 12V-Leitung absteckst 12V anliegen. Wenn das der Fall ist, dann hast du einen Fehler in deinem Fahrzeugkabelbaum. 

#### Ursache: Kurzschluss im Fahrzeugkabelbaum

Die eine Möglichkeit ist, dass du einen Kurzschluss im Fahrzeugkabelbaum hast. Das ist der Fall wenn 12V vom Antriebsmodul kommt wenn die Versorgung nicht angesteckt ist, die Spannung aber auf 0V einbricht, sobald du den Fahrzeugkabelbaum anschliesst. Ziehe dann einen Verbraucher nach dem anderen ab, bis die 12V Spannung wieder anliegt. Der Verbraucher letzte Verbraucher den du getrennt hast vor dem Wiederkehren der Spannung ist dein Übeltäter mit dem Kurzschluss.

#### Ursache: Anderer Fehler im Fahrzeugkabelbaum

Die andere Möglichkeit ist, dass du einen Fehler oder disfunktionale Verschaltung im Fahrzeugkabelbaum hast. Das ist der Fall wenn 12V vom Antriebsmodul kommt wenn die Versorgung nicht angesteckt ist, die Spannung aber auf 0V einbricht, sobald du den Fahrzeugkabelbaum anschliesst. Ziehe dann einen Verbraucher nach dem anderen ab, bis die 12V Spannung wieder anliegt. Der Verbraucher letzte Verbraucher den du getrennt hast vor dem Wiederkehren der Spannung ist dein Übeltäter mit dem Kurzschluss.

### der Scheinwerfer geht an, nachdem das Zündschloss betätigt wurde

Bordnetz wird mit Spannung versorgt

Dreht der Motor, wenn Du das System in den aktiven Fahrbetrieb versetzt und Gas gibst?

Den aktiven Fahrbetrieb erreichst Du durch Betätigung des Zündschlosses und anschließendes Drücken des pulsierenden Tasters. Der aktive Fahrbetrieb wird dann durch dauerhaftes Leuchten oder schnelles Blinken (->Notlauf) der Ring-LED bestätigt.

Aktivieren des Fahrbetriebs

<p align="center">
  <img src="https://github.com/user-attachments/assets/cea427ac-80f1-4483-a4a7-1f7d34043fc8" width="800">
</p>

#### Der Motor dreht
Kontaktieren Sie uns

#### Der Motor dreht nur wenn die Bremsleuchte leuchtet


Wenn der Motor nur dann dreht, wenn du Gas gibst und gleichzeitig bremst, dann ist dein Bremslichtschalter falsch verkabelt. Damit der Motor die Leistungsabgabe freigibt, müssen am Bremssignalkabel 12V anliegen. Das folgende Schaltbild soll vereinfacht zeigen, wie das Bremssignalkabel angeschlossen werden sollte. Ist der Bremslichtschalter offen, dann wird das Bremssignalkabel über die Bremsleuchte mit 12V versorgt und der Motor wird freigegeben. Ist der Bremslichtschalter geschlossen, dann liegt Fahrzeugmasse bzw. 0V am Bremssignalkabel an.
Bei dir ist das genau umgekehrt, es liegt Fahrzeugmasse an, wenn der Bremslichtschalter offen ist und 12V, wenn der Bremslichtschalter geschlossen ist. 
Deswegen denkt das Antriebsmodul es wird gebremst, obwohl du garnicht bremst.
Dafür musst du nun den Bremslichtschalter nach dem Schaltpan verkabeln.

<p align="center">
  <img src="https://github.com/user-attachments/assets/ff37422f-a6ad-4fac-8d88-767ee41661ef" width="500" />
</p>


#### Der Motor dreht **nicht**
Welches Blinkmuster siehst Du am Antriebsmodul unter der horizontalen Abdeckung?
(Es ist nicht notwendig diese abzuschrauben. Das farbige Licht sollte in einer etwas abgedunkelten Umgebung gut sichtbar sein.)

Das rote Licht unter der Abdeckung zeigt an, dass der Motor das Signal empfängt, es würde gebremst werden. Folglich lässt der Motor es nicht zu, dass Gas gegeben werden kann. 



<p align="center">
  <img src="https://github.com/user-attachments/assets/964ed193-8dcb-4a89-bdaa-3c5fefbcc160" width="800">
</p>

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

##### Kein rotes Licht. Nur grünes Blinken oder grünes Dauerlicht.

Gaszug falsch eingestellt

Wenn beim Einschalten des Systems der Motor erkennt, dass mehr als 0% Gas gegeben werden soll, dann gibt er solang keine Leistung frei, bis die Gaszugstellung einmal zurück auf 0% gebracht wurde. Erst dann ist Gas geben wieder möglich. Wenn Dein Gaszug zu viel Vorspannung haben sollte, dann wäre der Ausgangswert der Gaszugstellung über 0% und folglich ließe sich kein Gas geben. 

Prüfe folgendes um diese Theorie zu bestätigen bzw. zu widerlegen: 

1. System vollständig ausschalten (Taster an den Armaturen leuchtet gar nicht)

2. Fahrzeug so aufbocken, dass das Hinterrad frei drehen kann. Es wird bei den folgenden Schritten zur schlagartigen Beschleunigung des Hinterrads kommen! Für sicheren Stand des Mopeds sorgen.

3. Vergasergehäusekappe vom Gaszugzylinder abschrauben und Vergaserkolben vollständig abnehmen.

4. System in den aktiven Fahrbetrieb bringen (Taster an den Armaturen leuchtet durchgängig)

5. Mit dem Finger in den Gaszugzylinder fühlen und den Stift ertasten. Diesen Stift bis zum Anschlag eindrücken. Wenn Du nun den Stift vorsichtig anhebst, müsste das Hinterrad beschleunigen. 

Ist das der Fall, dann heisst das für Dich die Theorie stimmt und du musst die Stellschraube im Bowdenzug des Gaszugs so einstellen, dass der Gaszug gerade so kein Spiel hat (siehe [Montageanleitung](https://drive.google.com/drive/u/0/folders/1UddQeI-xHepiVfpnFqAwRGtM2oPfappJ). Falls Du dabei Hilfe benötigen solltest, kontaktiere bitte eine unserer [Partnerwerkstätten](https://second-ride.de/service).

### Nein, das Scheinwerferlicht geht nach Betätigung des Zündschlosses nicht an.

Bordnetz wird NICHT mit Spannung versorgt

Wenn ein Kurzschluss in Deinem System vorliegt, dann schaltet die 12V Spannungsversorgung des Antriebmoduls solang ab, bis der Kurzschluss aufgehoben wurde. Um zu prüfen ob es sich bei Dir um einen Kurzschluss handelt, trenne den weißen 2-poligen Stecker zwischen Bordnetz und Antriebsmodul. Miss auf der Seite des Antriebmoduls die Spannung.

Wenn 12V anliegen, heisst dass, dass Du in Deinem Bordnetz einen Kurzschluss hast. Du kannst diesen Suchen in dem Du den Stecker wieder verbindest und Verbraucher für Verbraucher vom Simson-Zündschloss abklemmst. Irgendwann sollte einer der noch angeschlossenen Verbraucher wieder anfangen zu funktionieren und du weisst der zuletzt abgeklemmte Verbraucher ist der Übeltäter. Wenn Du bei dieser Suche Hilfe benötigst, dann kontaktiere bitte eine unserer [Partnerwerkstätten](https://second-ride.de/service).

wenn am demontierten Stecker **ca. 12V (+-1V)** Spannung anliegt, ist das problem gelöst. Andernfalls kontaktieren sie uns.

### Im Antriebsmodul ist rote LED zu sehen


## die LED bleibt aus

1. Prüfe, ob die Steckverbindungen zwischen Zündschloss und Antriebsmodul, sowie Antriebsmodul und Sitzbank richtig verbunden sind. 

2. Weiterhin könnte der Akku zu wenig Ladung haben oder die Temperatur des Akkus außerhalb von -20°C und 60°C sein. Sorge dann zuerst dafür, dass der Akku wieder Raumtemperatur annimmt (was einige Stunden dauern kann) und verbinde ihn dann mit dem Ladegerät.



Trenne das Armaturenkabel vom Antriebsmodul und sieh dir die männlichen Pins im armaturenseitigen Stecker an. Es sollten 8 Pins zu sehen sein.

### Einer der Pins im Armaturenstecker ist verbogen oder abgebrochen.

Kontaktieren uns 

### Keiner der Pins im Armaturenstecker ist verbogen oder abgebrochen.

Es könnte sein, dass Dein Akku zu warm oder zu kalt ist und deshalb komplett abgeschaltet hat. Lass ihn mindestens für 5 Stunden akklimatisieren bevor Du es erneut versuchst. Stecke den Akku außerdem für kurze Zeit ans Ladegerät. Dass kann ihn manchmal "aus einem Tiefschlaf wieder aufwecken".

# Aufladen des Akkus

Überhitzter Akku

Wenn das Ladegerät anzeigt, dass der Akku vollgeladen ist, die Ladestandsanzeige unter Sitzbank jedoch etwas anderes sagt, dann lässt der Akku das Laden nicht zu. Meistens liegt es daran, dass der Akku zu warm oder zu kalt ist. Die Rekuperation ist dann ebenso nicht möglich.

Stelle den Akku für mindestens 5 Stunden bei Raumtemperatur ab und lasse ihn akklimatisieren. Stecke dann das Ladegerät noch einmal erneut an (angesteckt lassen reicht nicht) und sieh ob der Akku sich laden lässt, bzw. die Rekuperation wieder funktioniert. Es wird häufig unterschätzt, wie lang der Akku zur Akklimatisierung benötigt.

# Verhalten während der Fahrt

## Es lässt sich manchmal kein Gas geben.

Bremskontaktsensor


Höchstwahrscheinlich hat Dein Bremslichtschalter einen Wackelkontakt. Ob das die Ursache ist, kannst Du testen, indem Du das "Bremssignalkabel" (schwarz mit weißen Steckern) direkt an eines unserer roten "+12V" Kabel anschließt, welche vom Motor kommen. 

Achtung! Damit umgehst Du den Bremslichtschalter, was dazu führt, dass der Motor auch noch Leistung abgeben kann wenn Du die Bremse betätigst. Damit hast Du keine Möglichkeit mehr falls der Motor ungewollt Leistung abgibt ihn abzuschalten. Diese Maßnahme sollte also nur zu Diagnosezwecken, nicht aber zum dauerhaften Gebrauch umgesetzt werden.

Wenn Die Probleme nun nicht mehr auftreten, ist nachgewiesen, dass dein Bremslichtschalter sporadisch das Signal gibt es würde gebremst werden. Falls Du noch den Bremslichtschalter in der Hinterradnabe verwenden solltest, empfehlen wir Dir dringend einen [externen Bremslichtschalter](https://www.google.com/search?q=simson+externer+bremslichtschalter) zu verbauen. In beiden Fällen sollte das Problem aber behoben werden können, indem Du den Bremslichtschalter neu einstellst. 

Wenn Du Dir das selbst nicht zutraust oder dabei Hilfe benötigst, kontaktiere eine unserer [Partnerwerkstätten](https://second-ride.de/service).

### das Problem tritt auch mit überbrücktem Bremslichtschalter auf.


Wenn beim Einschalten des Systems der Motor erkennt, dass mehr als 0% Gas gegeben werden soll, dann gibt er solang keine Leistung frei, bis die Gaszugstellung einmal zurück auf 0% gebracht wurde. Erst dann ist Gas geben wieder möglich. Wenn Dein Gaszug zu viel Vorspannung haben sollte, dann wäre der Ausgangswert der Gaszugstellung über 0% und folglich ließe sich kein Gas geben. 

Prüfe folgendes um diese Theorie zu bestätigen bzw. zu widerlegen: 

1. System vollständig ausschalten (Taster an den Armaturen leuchtet gar nicht)

2. Fahrzeug so aufbocken, dass das Hinterrad frei drehen kann. Es wird bei den folgenden Schritten zur schlagartigen Beschleunigung des Hinterrads kommen! Für sicheren Stand des Mopeds sorgen.

3. Vergasergehäusekappe vom Gaszugzylinder abschrauben und Vergaserkolben vollständig abnehmen.

4. System in den aktiven Fahrbetrieb bringen (Taster an den Armaturen leuchtet durchgängig)

5. Mit dem Finger in den Gaszugzylinder fühlen und den Stift ertasten. Diesen Stift bis zum Anschlag eindrücken. Wenn Du nun den Stift vorsichtig anhebst, müsste das Hinterrad beschleunigen. 

Ist das der Fall, dann heisst das für Dich die Theorie stimmt und du musst die Stellschraube im Bowdenzug des Gaszugs so einstellen, dass der Gaszug gerade so kein Spiel hat (siehe [Montageanleitung](https://drive.google.com/drive/u/0/folders/1UddQeI-xHepiVfpnFqAwRGtM2oPfappJ). Falls Du dabei Hilfe benötigen solltest, kontaktiere bitte eine unserer [Partnerwerkstätten](https://second-ride.de/service).

# Es fehlt etwas im Lieferumfang bzw. es wurde nicht geliefert wie bestellt.

Am Anfang der beigelegten Montage- und Bedienungsanleitung findest Du eine Liste mit allen Teilen die in Deinem Lieferumfang enthalten sein sollten. Die Quadrate daneben helfen Dir die Teile abzuhaken und so eine Bestandsaufnahme zu machen. 
Unter folgendem Link findest Du nochmal die digitale Version der Anleitung: [second-ride.de/docs](https://www.google.com/url?sa=j&url=http%3A%2F%2Fsecond-ride.de%2Fdocs&uct=1751872144&usg=rJpIP1Esq7dYvK0hTATlM4edfwo.&source=editors)

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

