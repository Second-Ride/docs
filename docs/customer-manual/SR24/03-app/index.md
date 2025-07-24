# Second Ride App & Updates

<p align="center">
  <img src="https://github.com/user-attachments/assets/56e0947d-9a26-4f11-af30-bf1611215053" />
</p>


# Bevor du mit dem Umbau/App Nutzung beginnst

Der Verwendungszweck der oben genannten Zubehörkomponente ist der Einbau gemäß der vorliegenden Montageanleitung, sowie deren Nutzung im Straßenverkehr gemäß der Bedienungsanleitung. Bitte habe Verständnis dafür, dass wir uns bei der Entwicklung des Umbausatzes und Zubehör nach dem Originalzustand der erwähnten Simson Modelle gerichtet haben. Bei Umbauten mit Bauteilen, die nicht dem Original entsprechen, oder Veränderung der Originalteile durch einen Unfall, Verschleiß, oder beabsichtigte Modifikationen können wir nicht gewährleisten, dass das Umbaukit und Zubehör fehlerfrei und sicher funktioniert, bzw. sich überhaupt einbauen lässt. Solltest du dir bezüglich deines Fahrzeugs unsicher sein, kontaktiere uns gerne.

Das dir vorliegende Dokument wird von der Second Ride GmbH zur Verfügung gestellt und versteht sich als Ergänzung zur Original-Hersteller-Bedienungsanleitung. Beide Dokumente sind als Einheit zu sehen. Sie gehören unmittelbar zusammen, wobei die Erklärungen zum Verbrennungsmotor unberücksichtigt bleiben können.

Bitte lies dieses Dokument zuerst vollständig und genau durch, bevor du mit dem Umbau startest und deine erste Fahrt antrittst. Du findest hier Warnungen und Hinweise, Informationen und Ratschläge sowie Verhaltensmaßnahmen im Notfall und weitere wichtige Anmerkungen zu deinem Fahrzeug. Bei Nichtbeachtung der Anweisungen kann es zu leichten oder schweren Verletzungen sowie Lebensgefahr kommen. Zudem kann die Leistungsfähigkeit des Fahrzeugs eingeschränkt sein. Bitte lies auch die neben den Symbolen aufgeführten Warnungen und Hinweise, insbesondere für den Hochvoltbereich, sorgfältig durch. Nur so kann ein ordnungsgemäßer Einbau des Umbaukits und des Zubehörs sowie eine ordnungsgemäße Nutzung des Fahrzeugs sichergestellt werden. Bei Nichtbeachtung dieser Warnungen und Hinweise nimmst du Personen- bzw. Fahrzeugschäden billigend in Kauf.

Alle hier enthaltenen technischen Daten und Beschreibungen waren zum Zeitpunkt der Drucklegung aktuell. Da aber die kontinuierliche Verbesserung eines der Hauptziele ist, behalten wir uns das Recht vor, jederzeit Veränderungen an den Produkten vorzunehmen. Wenn du Irrtümer oder Auslassungen in diesem Dokument bemerkst, schreib das bitte unbedingt in den Discord-Channel (siehe Kapitel “Nützliche Links”). 


# Kompatibilität  

### Unterstützte Smartphone Modelle 

Die App ist kompatibel mit folgenden Geräten:

- iOS-Geräte ab iOS 15 (mindestens iPhone X oder neuer)

- Android-Geräte, ab Baujahr 2019 und mindestens Android 10

### Unterstützte Umbausätze 

Die App und das Update-Tool funktionieren mit folgenden Umbausätzen:

- SR23 in Verbindung mit unserem Bluetooth-Modul

- SR24 teilweise ohne weitere Hardware und teilweise nur in Verbindung mit unserem Bluetooth-Modul (siehe nächster Abschnitt)

- SR22 ist nicht kompatibel, da die Hardware sich deutlich unterscheidet und nicht unterstützt wird

### Erkennen, ob deine Sitzbank Bluetooth unterstützt 
Wenn deine Sitzbank direkt neben dem Hauptstecker einen USB-C Port besitzt, hat deine Sitzbank bereits ein BT-Modul integriert. Um es zu verwenden, musst du nur noch das Sitzbank-Update machen. Wie das geht, siehst du unter dem Kapitel “Updateprozess”.

![][image16]


# Second Ride App  {#second-ride-app}

## Inbetriebnahme {#inbetriebnahme}

### App installieren {#app-installieren}

Um dein Fahrzeug mit dem Smartphone zu verbinden, lade dir bitte zunächst die Second Ride App herunter:

| ![][image35] | App Store Link [www.second-ride.de/app-ios](http://www.second-ride.de/app-ios)  |
| :---- | :---- |
| ![][image5] | Google Play Store Link [www.second-ride.de/app-android](http://www.second-ride.de/app-android)  |

| Achtung: Achte darauf, dass du die aktuellste Version der App verwendest. Nur so ist sichergestellt, dass alle Funktionen zuverlässig arbeiten.  |
| :---- |

## 

### Erster Verbindungsaufbau {#erster-verbindungsaufbau}

Um die Sicherheit deiner Daten und Verbindung zu gewährleisten haben wir einen gesicherten Verbindungsaufbau implementiert. Dieser muss nur einmal beim ersten Verbinden mit einem neuen Smartphone, welches dein Fahrzeug noch nicht kennt, durchgeführt werden.   
Halte dafür die Sitzbank ID (unten auf deiner Sitzbank aufgelasert) bzw. die BT-Modul-ID bereit, die auf der Seite deines BT-Moduls steht.

**BT-Sitzbank:**  
Um deine Second Ride App mit deinem Fahrzeug zu verbinden, muss das Fahrzeug eingeschaltet sein, sodass der Taster am Zündschloss pulsiert.   
Halte den Sitzbanktaster für 3s gedrückt, bis ein Piepton erklingt und die Logo LED blau pulsiert.  
Öffne nun die Second Ride App und gehe oben rechts auf Verbinden. Es öffnet sich ein Fenster, welches nun ein Gerät namens “SecondRide” anzeigt. Klicke dieses an und bestätige die Kopplungsanforderung, die evtl. auftritt.  
Nun wirst du aufgefordert die Sitzbank ID einzugeben. Bitte gib die 5-stellige Zahl deiner Sitzbank ID ein und bestätige mit “senden”.  
Nun wird eine Verbindung aufgebaut. Bestätige die evtl. auftretende Kopplungsanforderung.  
Nach einem kurzen Moment sollte Verbindung erfolgreich sein und das Dashboard der App erscheinen.

**BT-Modul:**  
Um deine Second Ride App mit deinem Fahrzeug zu verbinden, muss das Fahrzeug eingeschaltet sein, sodass der Taster am Zündschloss pulsiert.   
Halte den BT-Modultaster für 3s gedrückt, bis ein Piepton erklingt und die Logo LED blau pulsiert.  
Öffne nun die Second Ride App und gehe oben rechts auf Verbinden. Es öffnet sich ein Fenster, welches nun ein Gerät namens “SecondRide” anzeigt. Klicke dieses an und bestätige die Kopplungsanforderung, die evtl. auftritt.  
Nun wirst du aufgefordert die BT-Modul ID einzugeben. Bitte gib die 5-stellige BT-Modul ID ein und bestätige mit “senden”. Achte hierbei darauf, dass das BT groß geschrieben ist.  
Nun wird eine Verbindung aufgebaut. Bestätige die evtl. auftretende Kopplungsanforderung.  
Nach einem kurzen Moment sollte Verbindung erfolgreich sein und das Dashboard der App erscheinen.

### Automatischer Verbindungsaufbau {#automatischer-verbindungsaufbau}

Nach dem dein Smartphone ein mal erfolgreich verbunden wurde, verbindet es sich in Zukunft automatisch, wenn du die App öffnest und deine BT-Sitzbank in Recihweite bzw. BT-Modul mit Strom versorgt ist.

### Systemreset {#systemreset}

Ein 10s gedrückthalten des BT-Modultasters im eingeschalteten Zustand bewirkt, dass dieses alle bekannten Smartphones vergisst sowie dass der BT-Name und alle Verstellt Fahrzeugeinstellungen zurückgesetzt werden. Solltest du vorher Fahrzeugeinstellungen verstellt haben, werden diese dadurch wieder auf die Ursprungsparameter zurückgesetzt.

## App Nutzung {#app-nutzung}

### Dashboard Bildschirm {#dashboard-bildschirm}

Das Dashboard gibt dir einen Digitaltacho, auf dem du alle relevanten Fahrparameter einsehen kannst. Um die einzelnen angezeigten zu verstehen, kannst du unter dem Diagnose Bildschirm in der App nachlesen, was die einzelnen Parameter bedeuten. Dafür musst du dort auf das kleine “i” Info Symbol neben dem Parameternamen klicken. 

### Diagnose Bildschirm {#diagnose-bildschirm}

Der Diagnosebildschirm  liefert dir einen tiefen Einblick in die Systemparameter. Diese sind unterteilt in Statusmeldungen, Akku und Antriebsmodul. Unter Statusmeldungen bekommst du aktuelle Hinweise zum Systemzustand gemeldet.   
Nimm dir den Moment und nutze auch hier wieder die Möglichkeit durch ein Tippen auf die einzelnen Parameternamen eine genauere Beschreibung für den einzelnen Systemparameter aufzurufen.

### Fahrzeug Bildschirm {#fahrzeug-bildschirm}

Die App ermöglicht es dir, Einstellungen an deinem Fahrzeug durchzuführen. Diese unterscheiden sich als Pro Features bzw. Standard Features. Um zu verstehen, welche Funktion die Verstellung dieser Einstellungen haben, nutze bitte das kleine “i” Info Symbol neben dem Parameternamen auf der “Einstellungen”  
Die Pro Features sind nur verfügbar, wenn auf deiner BT-Sitzbank bzw. BT-Modul Pro freigeschaltet ist. Wie das geht, siehst du im folgenden Abschnitt.

| Achtung: Durch das Verstellen von Fahrzeugeinstellungen veränderst du aktiv das Fahrverhalten deines Fahrzeuges. Lies dir vorher den Beschreibungstext des jeweiligen Fahreigenschaften durch und fahre  nach dem Verstellen vorsichtig, um das veränderte Fahrverhalten kennenzulernen. |
| :---- |

### Freischaltung Pro-Features {#freischaltung-pro-features}

Um die Pro-Features freizuschalten, muss ein 8-stelliger Pro-Code auf der App Seite “Fahrzeug” eingegeben werden. 

**Wo  finde ich den Pro-Code?**

Wenn du ein BT-Modul inkl. Pro-Code bestellt hast, findest du diesen auf dem beigelegten Lieferschein. Falls du einen Pro-Code in unserem Shop erworben hast, wird er dir per Email zugesandt.

Wenn du noch kein Pro feature gekauft hast, diese aber nutzen möchtest, kannst du deinen persönlichen Pro-Code unter folgendem Link erwerben:

| ![][image36] | Pro Version Shop Link
[www.second-ride.de/pro-code](http://www.second-ride.de/pro-code)  |
| ----: | :---- |

**Was ist wenn ich zwei Handys habe/ das Handy wechsel / das Fahrzeug wechsle?**

Mit dem Pro-Code schaltest du das BT-Modul bzw deine Sitzbank frei. Das heißt, unabhängig davon, ob du später ein anderes Handy nutzt, oder das BT-Modul bzw. die Sitzbank mit einem anderen Fahrzeug nutzt, sind die Pro-Features nutzbar.

### Infoseite: Probleme Melden, App Info & Rechtliches {#infoseite:-probleme-melden,-app-info-&-rechtliches}

In der App Oben links gibt es einen Infobutton. Dieser führt dich zu der Infoseite der App.   
Dort findest findest du hier das Problem melden Feld. Mit diesem kannst du uns Feedback inkl. Logdatei deiner letzten Fahrt und App Nutzung zukommen lassen. Wenn du Probleme mit der App oder dem System haben solltest, nutze diese Funktion, um uns zu informieren.

Zusätzlich findest du dort alle Informationen zu Datenschutz & dessen Einstellung, dem Impressum, Lizenzen, sowie App-Version.

### Datenschutz {#datenschutz}

Wir haben den Datenschutz natürlich sehr Ernst genommen und schützen deine Daten auf uns bestmögliche Weise. Alle Informationen zum Datenschutz findest du unter:

| ![][image8] | Link zu Second Ride Datenschutzrichtlinien
[www.second-ride.de/datenschutz](http://www.second-ride.de/datenschutz) |
| :---- | :---- |

Warnhinweise

| ![][image37] | Die mit “72 V” gekennzeichneten Umbausätze arbeiten mit einer Spannung zwischen 58 V und 84V. Diese Spannung gilt als Hochvoltspannung und kann gesundheitsgefährdend sein. Kabel, die Hochvoltspannung leiten, sind orange und Gehäuse, unter denen Hochvoltkomponenten erreichbar sind, sind mit einem schwarzen Blitz auf gelbem Hintergrund gekennzeichnet. Solltet Ihr irgendwelche Probleme mit dem Umbausatz haben, wendet Euch an uns.  |
| :---- | :---- |
| ![][image37] | Im Antriebsmodul sind große Kondensatoren verbaut, welche die Batteriespannung für einige Minuten speichern können, nachdem die Sitzbank abgesteckt wurde. Es kann also nicht nur auf dem Stecker in der Sitzbank eine Spannung anliegen, sondern auch auf dem Stecker, der vom Antriebsmodul kommt, sowie auf anderen Kabeln und Komponenten, welche mit dem Antriebsmodul verbunden sind. |
| ![][image38] | Der Akku in der Sitzbank sollte nicht in Räumen oder an Orten gelagert werden, die Temperaturen von 60°C übersteigen. Dadurch entsteht ein Brandrisiko. Vermeide es den Akku zum Beispiel in den Innenräumen von Autos oder ähnlichen Räumlichkeiten aufzubewahren, die sich durch Sonneneinstrahlung aufheizen können. |
| ![][image39] | Verwende nur Ladegeräte, die von der Second Ride GmbH für die Verwendung mit dem Umbausatz freigegeben wurden. |
| ![][image40] | Nicht durch tiefes Wasser und nicht ohne vollständige Schutzbleche fahren. Antriebsmodul, Sitzbank, Armaturen und Ladegerät dürfen nicht unter Wasser getaucht werden. Zum Reinigen keinen Hochdruckreiniger verwenden. |
| ![][image40] | Bei Eintauchen von Sitzbank, Ladegerät, Antriebsmodul oder Armaturen in Wasser, Bauteile nicht berühren\! Stromschlag\! Sitzbank und Ladegerät nicht nutzen. Bitte kontaktiere uns\! |
| ![][image41] | Wenn Gase oder Flüssigkeiten aus dem Akku kommen, atme diese nicht ein bzw. berühre diese nicht. Die Gase sind giftig und brennbar. |
| ![][image37] | Bei Schäden am Sitzbankgehäuse oder Antriebsmodul, kontaktiere uns bitte, da Hochvoltsysteme beschädigt sein könnten.  |
| ![][image38] | Beim An- und Abstecken der Sitzbank vom Fahrzeug oder dem Ladegerät können Funken entstehen. Betätige den Stecker daher niemals an explosionsgefährdeten Orten. |
| ![][image40] | Wenn du irgendeine Form von Beschädigung, Materialfehler, Gasaustritt, etc. an einer Sitzbank, Ladegerät oder Antriebsmodul entdeckst, informiere uns, bevor du den Fahrbetrieb oder Ladebetrieb aufnimmst. |
| ![][image38] | Lade den Akku nur unter Beobachtung, da Brandgefahr herrscht. Informiere dich über geeignete Löschmaßnahmen.  |
| ![][image37] | Das Laden über den externen Ladeanschluss mit einem nicht-Second-Ride-Ladegerät mit mehr Leistung als der in diesem Dokument angegebenen maximalen Ladeleistung birgt Brandgefahr\! Lade daher deinen Second Ride Akku ausschließlich mit einem Second Ride Ladegerät. |
| ![][image37] | Bei verbundenen Akku und Antriebsmodul kann das einstecken des Updatekabels für Antriebsmodul, BT-Modul oder Sitzbank zu Schaden an der Elektronik des verbundenen Gerätes führen. Vor jeden Einstecken eines Kabels, welches mit dem Umbaukit oder Zubehör verbunden ist, ist immer vorher der Akku vom Antrisbmodul elektrisch zu trennen |
|  |  |
|  |  |
