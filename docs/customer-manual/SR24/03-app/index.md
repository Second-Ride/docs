# Second Ride App & Updates

<p align="center">
  <img src="https://github.com/user-attachments/assets/c09abfb1-d620-44f7-be86-b7b039f1bf0d" width="500" />
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

<p align="center">
  <img src="https://github.com/user-attachments/assets/8226b8b5-b09e-4b40-840c-e7fbd1f63bec" width="500" />
</p>


# BT-Modul  

Das BT-Modul ist nur dann notwendig, wenn du eine Sitzbank ohne USB-C Anschluss neben dem Sitzbank Anschluss besitzt.   
Solltest du eine Sitzbank mit dem USB-C Port neben dem Logo haben, kannst du dieses Kapitel überspringen.

<h2>Lieferumfang & BT-Modul</h2>
<table>
  <tr>
    <td valign="top">
      <ul style="list-style-type: none; padding-left: 0;">
        <li><input type="checkbox"> 1x BT-Modul</li>
        <li><input type="checkbox"> 7x Kabelbinder</li>
        <li><input type="checkbox"> 2x M4x10 Innensechskantschraube</li>
        <li><input type="checkbox"> 2x M4 Federring</li>
      </ul>
    </td>
    <td valign="top" style="padding-left: 30px;">
      <ul style="list-style-type: none; padding-left: 0;">
        <li><input type="checkbox"> 1x M6x50 Innensechskantschraube</li>
        <li><input type="checkbox"> 2x M6 Sechskantmutter</li>
        <li><input type="checkbox"> 2x M6 Unterlegscheibe</li>
      </ul>
    </td>
  </tr>
</table>

<h2>Benötigte Werkzeuge</h2>
<table>
  <tr>
    <td valign="top">
      <ul style="list-style-type: none; padding-left: 0;">
        <li><input type="checkbox"> 10er Maulschlüssel</li>
        <li><input type="checkbox"> 10er Nuss, Knarre und Verlängerungsstück</li>
        <li><input type="checkbox"> Inbusschlüssel SW3</li>
      </ul>
    </td>
    <td valign="top" style="padding-left: 30px;">
      <ul style="list-style-type: none; padding-left: 0;">
        <li><input type="checkbox"> Inbusschlüssel SW4</li>
        <li><input type="checkbox"> Seitenschneider</li>
        <li><input type="checkbox"> Kreuzschlitz- und Schlitz Schraubendreher</li>
      </ul>
    </td>
  </tr>
</table>


## 3. Montage des BT-Modul 

Mache ein Foto von oder merke dir den 5-stelligen BT-Modul ID auf der Seite deines BT-Moduls. Diesen brauchst du später beim Verbindungsaufbau.

### S50, S51, S70

Öffne den linken Seitendeckel und entferne die obere Lochabdeckung des Gehäusemittelteils. Diese Abdeckung wird nicht mehr benötigt und kann beiseite gelegt werden. Löse anschließend die Mutter am Massepunkt im Herzkasten und entferne sie zusammen mit allen Ringkabelschuhen und Unterlegscheiben. Öffne danach den rechten Seitendeckel. Halte die Schraube des Massenpunktes fest und löse die Mutter auf der linken Seite. Entferne diese Mutter sowie die Unterleg- und Zahnscheibe. Nimm die Schraube heraus und ersetze sie durch die M6x50-Schraube (1). Montiere nun alle zuvor entfernten Teile und Kabel wieder in umgekehrter Reihenfolge und schließe den rechten Seitendeckel. Schraube anschließend eine neue M6-Mutter (2), gefolgt von einer Unterlegscheibe (3), etwa 20 mm auf das Schraubenende.

<p align="center">
  <img src="https://github.com/user-attachments/assets/ed6e013c-6bb6-4144-8f52-4295f0b91efe" width="500" />
</p>

Schiebe das BT-Modul mit der Öse auf die Schraube, gefolgt von der zweiten Unterlegscheibe sowie der Mutter. Achte darauf, dass der Taster des BT-Moduls in Fahrtrichtung zeigt. Das Modul darf nicht über den Herzkasten hinausragen (4), damit der Seitendeckel später wieder problemlos passt.

<p align="center">
  <img src="https://github.com/user-attachments/assets/f4a3f473-6898-439f-8d9e-5d2a5d2d39db" width="500" />
</p>


Sobald die gewünschte Position erreicht ist, hältst du die hintere Mutter (2) mit einem 10er-Schlüssel fest und ziehst die vordere Mutter mit einer 10er-Nuss mit 6 Nm an. Für die Montage des Kabels fahre mit Absatz 4 fort.

### KR51/2, KR51/1, KR51  
Löse die Sternmutter am Motortunnel und nehme ihn ab. Schiebe das BT-Modul von vorne, beginnend vor der Querstrebe (1), zwischen den Rahmenrohren (2) nach hinten, bis es das Wellrohr (3) erreicht. Achte darauf, dass der Taster in Fahrtrichtung zeigt und das Logo nach oben ausgerichtet ist. Ziehe nun für die Befestigung jeweils einen Kabelbinder durch die obere (4) und dann durch die untere Lasche des Moduls und lege sie anschließend um das anliegende Rahmenrohr (2). Für einen sicheren Sitz sollten sich alle Kabelbinder hinter der Querstrebe (1) befinden.

<p align="center">
  <img src="https://github.com/user-attachments/assets/32c05847-3fa7-453c-befa-6f1a0a01522b" width="500" />
</p>

Sobald das BT-Modul in Position ist, ziehe alle Kabelbinder gleichermaßen fest. Für die Montage des Kabels, fahre mit Absatz 4  fort.

### SR4-2, SR4-4

Entferne die Seitenbleche, um Zugang zum Batteriefach zu erhalten. Sollte sich dort noch die alte Batterie befinden, nehme sie heraus, da das BT-Modul an dieser Stelle montiert wird. Schiebe das BT-Modul von der linken Seite in das Batteriefach, bis die Öse (1) am Anschlag (2) vorbeigeht. Achte darauf, dass der Taster nach oben und das Logo nach hinten zeigt. Für die Befestigung ziehe zunächst einen Kabelbinder durch die Lasche (3), lege ihn um den Anschlag (2) und verschließe ihn fest.

<p align="center">
  <img src="https://github.com/user-attachments/assets/905fa588-8c2f-4d8c-9130-dfc1958f38d5" width="500" />
</p>

Dann führe einen weiteren Kabelbinder durch die Laschen (4), ziehe ihn durch das Loch in der Batterieauflagefläche (5) und ziehe ihn ebenfalls fest.

<p align="center">
  <img src="https://github.com/user-attachments/assets/48e161a4-19ac-472a-98e8-0ce0f4b95e62" width="500" />
</p>


Für die Montage des Kabels fahre mit Absatz 4  fort.

### SR50, SR80 
Das Einspannen des Fahrzeugs in eine Motorradhebebühne und das anschließende Hochfahren erleichtert den Einbau des BT-Moduls erheblich. Löse die Sternmutter und entferne die Motor- sowie die Elektrikabdeckung. Unter dem Luftleitblech (1) befinden sich zwei Löcher (2) im Rahmenblech.

<p align="center">
  <img src="https://github.com/user-attachments/assets/e07b44b0-cdb4-4e82-acfb-e88cb74c6094" width="500" />
</p>


Lege das BT-Modul wie gezeigt mit der Unterseite auf das Rahmenblech, sodass die Gewinde auf der Unterseite des Moduls mit den Löchern (2) im Blech übereinstimmen. Ein Blick von unten hilft dabei, die Ausrichtung zu überprüfen.

<p align="center">
  <img src="https://github.com/user-attachments/assets/f15e56cf-13cc-40fa-983b-9c34ccc7c79c" width="500" />
</p>

Stecke nun jeweils eine Ringfeder auf die M4x10-Innensechskantschrauben. Führe jeweils eine Schraube durch eines der Löcher, schraube sie in das BT-Modul und ziehe sie mit 3 Nm fest (handfest, nicht zu fest) . Für die Montage des Kabels fahre mit Absatz 4  fort.

### Duo 4, Duo 4-1, Duo 4-2
Um das BT-Modul hinter dem Aufnahmeblech für den Akku (1) zu befestigen, drücke die Oberseite des Moduls gegen das Aufnahmeblech und stelle es auf die Querstrebe des ehemaligen Bleiakkuhalters (2), wobei der Taster nach oben zeigt. Führe jeweils einen Kabelbinder durch die oberen Laschen (3), lege diese um die Querstrebe (2) und verschließe sie fest. Ein weiterer Kabelbinder wird durch die obere Lasche (4) geführt und um das Aufnahmeblech (1). Der letzte Kabelbinder wird durch die obere und untere Lasche (5) gezogen und am linken Rohr (6) befestigt, das in das Lenkerrohr mündet.

<p align="center">
  <img src="https://github.com/user-attachments/assets/b6201e6f-8626-4883-a724-073784692ac3" width="500" />
</p>

Ziehe zum Schluss alle Kabelbinder gleichmäßig fest, um das Modul sicher zu fixieren. Für die Montage des Kabels fahre mit Absatz 4 fort.

## 4. BT-Modul Anschließen  {#bt-modul-anschließen}

Der Male-Anschluss des BT-Moduls (langes Kabel) wird an das Diagnose-Kabel des Antriebsmoduls angeschlossen. Dadurch entsteht ein neuer Diagnosepunkt, der nun das kurze Kabelende am BT-Modul ist.

### Langes Diagnose-Kabel (ab AM\#00193)

Bei Antriebsmodulen mit der Seriennummer \#00193 und höher sollte ein etwa 40cm langes Kabel unten aus dem Antriebsmodul kommen. Auf dem Stecker befindet sich eine Gummikappe. Ist dies der Fall, fahre mit Schritt 2.b fort.

### Kurzes Diagnose Kabel (bis AM\#00193)

Bei Antriebsmodulen mit den Seriennummern \#00038 bis \#00192 findet ihr das Updatekabel wie folgt:

### Kabelblende abnehmen

Entferne die Kabelblende vom Antriebsmodul, indem du die M4-Zylinderkopf-Schraube (1) an der rechten Seite abnimmst. Dazu brauchst du einen 3 mm Inbus-Schlüssel. Sollte deine Kabelblende auf der Oberseite links in Fahrtrichtung einen ovalen Ausschnitt haben, dann versteckt sich darunter noch eine zweite M4 \-Zylinderkopf-Schraube, welche du nur eine Umdrehung lösen musst, um die Blende abnehmen zu können.

<p align="center">
  <img src="https://github.com/user-attachments/assets/c09abfb1-d620-44f7-be86-b7b039f1bf0d" width="500" />
</p>
  
### Diagnose-Kabel identifizieren

Nun hast du die Vehicle Control Unit (2) gefunden (Wir haben sie aus Liebe zu ihr “Günter” getauft). Von Günter geht ein kurzes Kabel (3) ab, welches nicht weiter verbunden und mit einer Gummikappe abgedeckt ist.

## 5. Montage des Kabels {#montage-des-kabels}

Entferne die Gummikappe und schließe das lange Kabel des BT-Moduls an. **Wichtig: Achte darauf, dass die Pfeile auf dem männlichen und weiblichen Stecker zueinander zeigen, bevor du sie mit Kraft zusammen schiebst.** Nutze nun die mitgelieferten Kabelbinder, um das Kabel zwischen dem BT-Modul und dem Antriebsmodul am Fahrzeugrahmen zu befestigen. Vermeide dabei starke Knicke im Kabel. Sollte das Kabel zu lang sein, lege es zu Schlaufen zusammen und halte diese mit einem Kabelbinder fest.

Nun sollte dein BT-Modul fest an deinem Fahrzeug verbaut und angeschlossen sein.


# Anleitung zum Firmwareupdate {#anleitung-zum-firmwareupdate}

Seit April 2025 werden alle Komponenten des Umbausatzes mit dem neuen Webupdate-Tool programmiert. Das bisherige Programm „DFU Buddy“ wird nicht mehr verwendet. Mit dem Webupdate-Tool kannst du dein Moped bequem und sicher über den Chrome-Browser aktualisieren: [Link zum Webupdatetool](https://second-ride.de/update)		

## Was wird eigentlich aktualisiert?


Die Firmware ist die Software, die das Verhalten deines Fahrzeugs bestimmt – also wie es beschleunigt, bremst, lädt oder den Ladezustand anzeigt. Wir entwickeln diese Software kontinuierlich weiter, um dir ein besseres Fahrerlebnis zu bieten. Über das Update-Tool kannst du diese Verbesserungen ganz einfach selbst installieren.

## Welche Komponenten benötigen Updates?


Je nach Ausstattung deines Umbausatzes betrifft das ein oder zwei Geräte:

- Antriebsmodul („Günter“)  
- Batterie („Gisela“), nur wenn deine Batterie über einen USB-C-Anschluss verfügt  
- Bluetooth-Modul, falls vorhanden

Ob ein neues Update verfügbar ist und was sich geändert hat, findest du in der [Änderungshistorie - Firmware](https://docs.google.com/document/d/16SFpTpeRKDW-OlozgDFcO0iHk5q1t2Q6hK-TyoXaMT0/edit?usp=sharing).

## Update vom Antriebsmodul („Günter“) 

!!! warning "Achtung"
    Verbinde niemals gleichzeitig die Sitzbank und das Antriebsmodul mit deinem Computer über Kabel. Ziehe immer zuerst den Akku-Stecker ab, bevor du deinen Laptop mit der Sitzbank/BT-Modul oder dem Antriebsmodul verbindest.

!!! warning "Achtung"
    Ein Firmware-Update verändert das Fahrverhalten. Es kann zu höherer Beschleunigung, höherer Endgeschwindigkeit, anderem Bremsverhalten, etc. kommen. Sei also bei den ersten Fahrten nach dem Update besonders Aufmerksam und Vorsichtig und verlass Dich nicht auf die bisherige Erfahrung mit dem Antrieb. Ließ Dir        außerdem die Änderungshistorie aufmerksam durch. 

!!! warning "Achtung" 
    Das Aufspielen der Duo-Firmware auf einem anderen Fahrzeug als der Simson Duo führt dazu, dass die Betriebserlaubnis des Fahrzeugs erlischt. Das gleiche gilt, wenn die Nicht-Duo-Firmware auf der Simson Duo installiert wird. 

Zunächst muss das Antriebsmodul an deinen PC angeschlossen werden. Gehe dazu wie folgt vor:

### 1. Suche das Diagnose-Kabel

   #### 1.1 Langes Diagnose-Kabel (ab AM\#00193)

      Bei Antriebsmodulen mit der Seriennummer \#00193 und höher sollte ein drittes. etwa 40cm langes Kabel unten aus dem Antriebsmodul kommen. Auf dem Stecker befindet sich eine Gummikappe. Ist dies der Fall, fahre mit Schritt 2 fort.

   #### 1.2. Kurzes Diagnose Kabel (bis AM\#00193)

      Bei Antriebsmodulen mit den Seriennummern \#00038 bis \#00192 findet ihr das Updatekabel wie folgt:

      1.2.1. Kabelblende abnehmen		 
      
         Entferne die Kabelblende vom Antriebsmodul, indem du die M4-Zylinderkopf-Schraube (1) an der rechten Seite abnimmst. Dazu brauchst du einen 3 mm Inbus-Schlüssel. Sollte deine Kabelblende auf der Oberseite links in Fahrtrichtung einen ovalen Ausschnitt haben, dann versteckt sich darunter noch eine zweite M4         -Zylinderkopf-Schraube, welche Du nur eine Umdrehung lösen musst, um die Blende abnehmen zu können.

<p align="center">
  <img src="https://github.com/user-attachments/assets/f2d34c5d-6cfd-4838-9ac2-75c5c04d5d5b" width="500" />
</p>

      1.1.1 Diagnose-Kabel identifizieren

      Nun hast du die Vehicle Control Unit (2) gefunden (Wir haben sie aus Liebe zu ihr “Günter” getauft). Von Günter geht ein kurzes Kabel (3) ab, welches nicht weiter verbunden und mit einer Gummikappe abgedeckt ist.

### 2. USB-Kabel anschließen

<div style="border: 2px solid orange; background-color: #fff8e1; padding: 15px; border-radius: 8px;">
   Die Batterie darf während des Updates aus Sicherheitsgründen nicht mit dem Antriebsmodul verbunden sein. Stelle sicher, dass die Sitzbank nicht angeschlossen ist.
</div>

   Entferne die Gummikappe und schließe das mitgelieferte USB-Kabel an. Wichtig: Achte darauf, dass die Pfeile auf dem männlichen und weiblichen Stecker zueinander zeigen, bevor du sie mit Kraft zusammen schiebst. Schließe das USB Kabel anschließend an deinen PC an.

### 3. [Webupdatetool öffnen](http://Second-ride.de/update):  → Nur mit Google Chrome verwenden.


### 4. Firmware auswählen:  
   Wähle unter „Antriebsmodul / Günter“ die gewünschte Firmware-Version und klicke auf “Verbinden”  
  
   <p align="center">
  <img src="https://github.com/user-attachments/assets/263f4fd9-54f9-4818-91ee-71439bb3a486" width="500" />
</p>


### 5. Verbindung herstellen:  
   Nun öffnet sich ein Fenster, welches dir die Option bietet aus verschiedenen Geräten auszuwählen. Wähle das STM32… aus und bestätige mit “Verbinden” unten rechts.  
  
  <p align="center">
  <img src="https://github.com/user-attachments/assets/48619cba-1325-434a-9ad0-f54f5b51cba6" width="500" />
</p>

### 6. Firmware-Update starten:  
   Bevor du nun den Updateprozess über “Update ausführen” bestätigst, stelle sicher, dass die Kabelverbindung stabil ist – ein Verbindungsabbruch kann die Elektronik beschädigen.   
   Klicke nun auf “Update ausführen” und lasse den Vorgang vollständig durchlaufen.  

   <p align="center">
  <img src="https://github.com/user-attachments/assets/b6f56cae-6cbb-4822-a888-f3f000b02b1b" width="500" />
</p>

### 7. Abschluss:  
   Nach erfolgreichem Update erscheint eine Bestätigungsmeldung. unter den beiden blauen Updatebalken.   
   Nun kannst du das Kabel wieder von dem Diagnosestecker und deinem Laptop trennen.

## Update von Sitzbank / Bluetooth-Modul {#update-von-sitzbank-/-bluetooth-modul}

Damit die App korrekt funktioniert, muss die Firmware-Version der Sitzbank bzw. des BT-Moduls in der ersten Ziffer mit der App-Version übereinstimmen. Z.b.: Gisela V1.0.0 ist kompatibel mit App V1.1.3. Gisela V1.0.0 ist nicht mit App V2.0.0 kompatibel.  
 Die App-Version findest du in der App unten, wenn du auf das Info-Symbol oben links tippst.

!!! warning "Achtung" 
    Verbinde niemals gleichzeitig die Sitzbank und das Antriebsmodul mit deinem Computer über Kabel. Ziehe immer zuerst den Akku-Stecker ab, bevor du dein Laptop mit der Sitzbank oder dem Antriebsmodul verbindest. 
    

1. Verbinde die Sitzbank bzw. das BT-Modul mit einem USB-C-Kabel über den USB-C Port neben dem Second Ride Logo mit deinem Laptop. Der USB-C Port an dem BT-Modul/Sitzbank sollte jetzt leuchten

<p align="center">
  <img src="https://github.com/user-attachments/assets/272cd4d2-0535-4927-8e30-e2f53e4c697e" width="500" />
</p>

2. Webupdatetool öffnen: → Nur mit Google Chrome oder Edge verwenden.

3. Firmware auswählen:  
   Wähle unter „Sitzbank & BT-Modul updaten“ die passende Firmware-Version aus dem Dropdown-Menü und drücke auf Verbinden. Die Firmware “Gisela V4 Base Version” enthält nur die Basis-Funktionalität ohne jegliche Bluetooth-Funktionen. Wähle daher die andere verfügbare Firmware aus.  
  
   <p align="center">
  <img src="https://github.com/user-attachments/assets/6661c5ee-31d5-40d0-b0bc-c57f402e19b8" width="500" />
</p>

4. Verbindung herstellen:  
   Nun sollte sich ein Fenster öffnen, in dem ein USB Port angezeigt wird (hier blau markiert). Diesen erkennst du daran, dass ein “gekoppelt” daneben steht.    
   Wähle diesen aus und klicke auf “Verbinden”.  
  
   <p align="center">
  <img src="https://github.com/user-attachments/assets/2605475f-150d-4631-b5f4-f1519bebe291" width="500" />
</p>


5. Firmware-Update starten:  
   Nach kurzem Laden sollte folgendes Fenster erscheinen.   
 
<p align="center">
  <img src="https://github.com/user-attachments/assets/42255bed-13c9-417a-913b-fca0c1555864" https://github.com/user-attachments/assets/42255bed-13c9-417a-913b-fca0c1555864 />
</p>

   Bevor du nun auf “install Gisela V4” drückst stelle sicher, dass die Kabelverbindung stabil ist – ein Abbruch kann Schäden verursachen.

   Klicke auf „Installieren“, bestätige das nachfolgende Fenster und lasse den Vorgang vollständig durchlaufen und 

5. Abschluss:  
    Nach erfolgreichem Update erscheint eine Bestätigungsmeldung. Jetzt kannst du die USB-C Verbindung trennen.

Wenn sowohl das Antriebsmodul als auch das Sitzbank-/BT-Modul auf die aktuelle Firmware aktualisiert wurden, kannst du die App wie vorgesehen nutzen und dein Fahrzeug koppeln.

Die nächsten Schritte zur App-Nutzung werden im folgenden Kapitel beschrieben.

# Second Ride App  

## Inbetriebnahme 


### App installieren 

Um dein Fahrzeug mit dem Smartphone zu verbinden, lade dir bitte zunächst die Second Ride App herunter:
[App Store Link](http://www.second-ride.de/app-ios)
[Google Play Store Link](http://www.second-ride.de/app-android) 

!!! warning "Achtung"
    Achte darauf, dass du die aktuellste Version der App verwendest. Nur so ist sichergestellt, dass alle Funktionen zuverlässig arbeiten.


### Erster Verbindungsaufbau 

Um die Sicherheit deiner Daten und Verbindung zu gewährleisten haben wir einen gesicherten Verbindungsaufbau implementiert. Dieser muss nur einmal beim ersten Verbinden mit einem neuen Smartphone, welches dein Fahrzeug noch nicht kennt, durchgeführt werden.   
Halte dafür die Sitzbank ID (unten auf deiner Sitzbank aufgelasert) bzw. die BT-Modul-ID bereit, die auf der Seite deines BT-Moduls steht.

#### BT-Sitzbank:  


Um deine Second Ride App mit deinem Fahrzeug zu verbinden, muss das Fahrzeug eingeschaltet sein, sodass der Taster am Zündschloss pulsiert.   
Halte den Sitzbanktaster für 3s gedrückt, bis ein Piepton erklingt und die Logo LED blau pulsiert.  
Öffne nun die Second Ride App und gehe oben rechts auf Verbinden. Es öffnet sich ein Fenster, welches nun ein Gerät namens “SecondRide” anzeigt. Klicke dieses an und bestätige die Kopplungsanforderung, die evtl. auftritt.  
Nun wirst du aufgefordert die Sitzbank ID einzugeben. Bitte gib die 5-stellige Zahl deiner Sitzbank ID ein und bestätige mit “senden”.  
Nun wird eine Verbindung aufgebaut. Bestätige die evtl. auftretende Kopplungsanforderung.  
Nach einem kurzen Moment sollte Verbindung erfolgreich sein und das Dashboard der App erscheinen.

#### BT-Modul: 


Um deine Second Ride App mit deinem Fahrzeug zu verbinden, muss das Fahrzeug eingeschaltet sein, sodass der Taster am Zündschloss pulsiert.   
Halte den BT-Modultaster für 3s gedrückt, bis ein Piepton erklingt und die Logo LED blau pulsiert.  
Öffne nun die Second Ride App und gehe oben rechts auf Verbinden. Es öffnet sich ein Fenster, welches nun ein Gerät namens “SecondRide” anzeigt. Klicke dieses an und bestätige die Kopplungsanforderung, die evtl. auftritt.  
Nun wirst du aufgefordert die BT-Modul ID einzugeben. Bitte gib die 5-stellige BT-Modul ID ein und bestätige mit “senden”. Achte hierbei darauf, dass das BT groß geschrieben ist.  
Nun wird eine Verbindung aufgebaut. Bestätige die evtl. auftretende Kopplungsanforderung.  
Nach einem kurzen Moment sollte Verbindung erfolgreich sein und das Dashboard der App erscheinen.

### Automatischer Verbindungsaufbau 

Nach dem dein Smartphone ein mal erfolgreich verbunden wurde, verbindet es sich in Zukunft automatisch, wenn du die App öffnest und deine BT-Sitzbank in Recihweite bzw. BT-Modul mit Strom versorgt ist.

### Systemreset 

Ein 10s gedrückthalten des BT-Modultasters im eingeschalteten Zustand bewirkt, dass dieses alle bekannten Smartphones vergisst sowie dass der BT-Name und alle Verstellt Fahrzeugeinstellungen zurückgesetzt werden. Solltest du vorher Fahrzeugeinstellungen verstellt haben, werden diese dadurch wieder auf die Ursprungsparameter zurückgesetzt.

## App Nutzung 

### Dashboard Bildschirm 

Das Dashboard gibt dir einen Digitaltacho, auf dem du alle relevanten Fahrparameter einsehen kannst. Um die einzelnen angezeigten zu verstehen, kannst du unter dem Diagnose Bildschirm in der App nachlesen, was die einzelnen Parameter bedeuten. Dafür musst du dort auf das kleine “i” Info Symbol neben dem Parameternamen klicken. 

### Diagnose Bildschirm 

Der Diagnosebildschirm  liefert dir einen tiefen Einblick in die Systemparameter. Diese sind unterteilt in Statusmeldungen, Akku und Antriebsmodul. Unter Statusmeldungen bekommst du aktuelle Hinweise zum Systemzustand gemeldet.   
Nimm dir den Moment und nutze auch hier wieder die Möglichkeit durch ein Tippen auf die einzelnen Parameternamen eine genauere Beschreibung für den einzelnen Systemparameter aufzurufen.

### Fahrzeug Bildschirm 

Die App ermöglicht es dir, Einstellungen an deinem Fahrzeug durchzuführen. Diese unterscheiden sich als Pro Features bzw. Standard Features. Um zu verstehen, welche Funktion die Verstellung dieser Einstellungen haben, nutze bitte das kleine “i” Info Symbol neben dem Parameternamen auf der “Einstellungen”  
Die Pro Features sind nur verfügbar, wenn auf deiner BT-Sitzbank bzw. BT-Modul Pro freigeschaltet ist. Wie das geht, siehst du im folgenden Abschnitt.

!!! warning "Achtung"
    Durch das Verstellen von Fahrzeugeinstellungen veränderst du aktiv das Fahrverhalten deines Fahrzeuges. Lies dir vorher den Beschreibungstext des jeweiligen Fahreigenschaften durch und fahre  nach dem Verstellen vorsichtig, um das veränderte Fahrverhalten kennenzulernen. 
    

### Freischaltung Pro-Features 

Um die Pro-Features freizuschalten, muss ein 8-stelliger Pro-Code auf der App Seite “Fahrzeug” eingegeben werden. 

**Wo  finde ich den Pro-Code?**

Wenn du ein BT-Modul inkl. Pro-Code bestellt hast, findest du diesen auf dem beigelegten Lieferschein. Falls du einen Pro-Code in unserem Shop erworben hast, wird er dir per Email zugesandt.

Wenn du noch kein Pro feature gekauft hast, diese aber nutzen möchtest, kannst du deinen persönlichen Pro-Code unter [diesem Link](http://www.second-ride.de/pro-code) erwerben:

**Was ist wenn ich zwei Handys habe/ das Handy wechsel / das Fahrzeug wechsle?**

Mit dem Pro-Code schaltest du das BT-Modul bzw deine Sitzbank frei. Das heißt, unabhängig davon, ob du später ein anderes Handy nutzt, oder das BT-Modul bzw. die Sitzbank mit einem anderen Fahrzeug nutzt, sind die Pro-Features nutzbar.

### Infoseite: Probleme Melden, App Info & Rechtliches 

In der App Oben links gibt es einen Infobutton. Dieser führt dich zu der Infoseite der App.   
Dort findest findest du hier das Problem melden Feld. Mit diesem kannst du uns Feedback inkl. Logdatei deiner letzten Fahrt und App Nutzung zukommen lassen. Wenn du Probleme mit der App oder dem System haben solltest, nutze diese Funktion, um uns zu informieren.

Zusätzlich findest du dort alle Informationen zu Datenschutz & dessen Einstellung, dem Impressum, Lizenzen, sowie App-Version.

### Datenschutz 

Wir haben den Datenschutz natürlich sehr Ernst genommen und schützen deine Daten auf uns bestmögliche Weise. Alle Informationen zum Datenschutz findest du in [diesem Link](http://www.second-ride.de/datenschutz):
