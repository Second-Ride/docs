# Anleitung zum Firmwareupdate
!!! info "Info"

    Der folgende Prozess gilt nur für die Second Ride Umbaukits SR23 und SR24. Die Umbaukits SR23 und SR24 werden nicht länger produziert und wurden durch das MID50 Umbaukit ersetzt.

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
    Das Aufspielen der Duo-Firmware auf einem anderen Fahrzeug als der Duo führt dazu, dass die Betriebserlaubnis des Fahrzeugs erlischt. Das gleiche gilt, wenn die Nicht-Duo-Firmware auf der Duo installiert wird. 

Zunächst muss das Antriebsmodul an deinen PC angeschlossen werden. Gehe dazu wie folgt vor:

### 1. Suche das Diagnose-Kabel

#### 1.1. Langes Diagnose-Kabel (ab AM\#00193)

Bei Antriebsmodulen mit der Seriennummer \#00193 und höher sollte ein drittes. etwa 40cm langes Kabel unten aus dem Antriebsmodul kommen. Auf dem Stecker befindet sich eine Gummikappe. Ist dies der Fall, fahre mit Schritt 2 fort.

#### 1.2. Kurzes Diagnose Kabel (bis AM\#00193)
Bei Antriebsmodulen mit den Seriennummern \#00038 bis \#00192 findet ihr das Updatekabel wie folgt:

##### 1.2.1. Kabelblende abnehmen		 
Entferne die Kabelblende vom Antriebsmodul, indem du die M4-Zylinderkopf-Schraube (1) an der rechten Seite abnimmst. Dazu brauchst du einen 3 mm Inbus-Schlüssel. Sollte deine Kabelblende auf der Oberseite links in Fahrtrichtung einen ovalen Ausschnitt haben, dann versteckt sich darunter noch eine zweite M4         -Zylinderkopf-Schraube, welche Du nur eine Umdrehung lösen musst, um die Blende abnehmen zu können.

<p align="center">
  <img src="https://github.com/user-attachments/assets/f2d34c5d-6cfd-4838-9ac2-75c5c04d5d5b" width="500" />
</p>

##### 1.1.1 Diagnose-Kabel identifizieren

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
  <img src="https://github.com/user-attachments/assets/42255bed-13c9-417a-913b-fca0c1555864" width="500" />
</p>

   Bevor du nun auf “install Gisela V4” drückst stelle sicher, dass die Kabelverbindung stabil ist – ein Abbruch kann Schäden verursachen.

   Klicke auf „Installieren“, bestätige das nachfolgende Fenster und lasse den Vorgang vollständig durchlaufen und 

5. Abschluss:  
    Nach erfolgreichem Update erscheint eine Bestätigungsmeldung. Jetzt kannst du die USB-C Verbindung trennen.

Wenn sowohl das Antriebsmodul als auch das Sitzbank-/BT-Modul auf die aktuelle Firmware aktualisiert wurden, kannst du die App wie vorgesehen nutzen und dein Fahrzeug koppeln.


Die nächsten Schritte zur App-Nutzung werden im folgenden Kapitel beschrieben.

