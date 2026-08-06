# Firmwareupdate mit dem alten Update-Tool

!!! info "Info"

    Diese Seite dokumentiert die Bedienung des Webupdate-Tools, bevor der Ablauf überarbeitet wurde. Die aktuelle Anleitung findest du unter [Anleitung zum Firmwareupdate](../index.md). Die physische Verbindung von Antriebsmodul bzw. Sitzbank/BT-Modul mit deinem PC ist unverändert geblieben und ebenfalls in der aktuellen Anleitung beschrieben.

## Update vom Antriebsmodul („Günter“)

### 1. [Webupdatetool öffnen](http://Second-ride.de/update):  → Nur mit Google Chrome verwenden.

### 2. Firmware auswählen:  
   Wähle unter „Antriebsmodul / Günter“ die gewünschte Firmware-Version und klicke auf “Verbinden”  

   <p align="center">
  <img src="https://github.com/user-attachments/assets/263f4fd9-54f9-4818-91ee-71439bb3a486" width="500" loading="lazy" />
</p>

### 3. Verbindung herstellen:  
   Nun öffnet sich ein Fenster, welches dir die Option bietet aus verschiedenen Geräten auszuwählen. Wähle das STM32… aus und bestätige mit “Verbinden” unten rechts.  

  <p align="center">
  <img src="https://github.com/user-attachments/assets/48619cba-1325-434a-9ad0-f54f5b51cba6" width="500" loading="lazy" />
</p>

### 4. Firmware-Update starten:  
   Bevor du nun den Updateprozess über “Update ausführen” bestätigst, stelle sicher, dass die Kabelverbindung stabil ist – ein Verbindungsabbruch kann die Elektronik beschädigen.   
   Klicke nun auf “Update ausführen” und lasse den Vorgang vollständig durchlaufen.  

   <p align="center">
  <img src="https://github.com/user-attachments/assets/b6f56cae-6cbb-4822-a888-f3f000b02b1b" width="500" loading="lazy" />
</p>

### 5. Abschluss:  
   Nach erfolgreichem Update erscheint eine Bestätigungsmeldung unter den beiden blauen Updatebalken.   
   Nun kannst du das Kabel wieder von dem Diagnosestecker und deinem Laptop trennen.

## Update von Sitzbank / Bluetooth-Modul

### 1. Webupdatetool öffnen: → Nur mit Google Chrome oder Edge verwenden.

### 2. Firmware auswählen:  
   Wähle unter „Sitzbank & BT-Modul updaten“ die passende Firmware-Version aus dem Dropdown-Menü und drücke auf Verbinden. Die Firmware “Gisela V4 Base Version” enthält nur die Basis-Funktionalität ohne jegliche Bluetooth-Funktionen. Wähle daher die andere verfügbare Firmware aus.  

<p align="center">
  <img src="https://github.com/user-attachments/assets/6661c5ee-31d5-40d0-b0bc-c57f402e19b8" width="500" loading="lazy" />
</p>

### 3. Verbindung herstellen:  
   Nun sollte sich ein Fenster öffnen, in dem ein USB Port angezeigt wird (hier blau markiert). Diesen erkennst du daran, dass ein “gekoppelt” daneben steht.    
   Wähle diesen aus und klicke auf “Verbinden”.  

<p align="center">
  <img src="https://github.com/user-attachments/assets/2605475f-150d-4631-b5f4-f1519bebe291" width="500" loading="lazy" />
</p>

### 4. Firmware-Update starten:  
   Nach kurzem Laden sollte folgendes Fenster erscheinen.   

<p align="center">
  <img src="https://github.com/user-attachments/assets/42255bed-13c9-417a-913b-fca0c1555864" width="500" loading="lazy" />
</p>

   Bevor du nun auf “install Gisela V4” drückst stelle sicher, dass die Kabelverbindung stabil ist – ein Abbruch kann Schäden verursachen.

   Klicke auf „Installieren“, bestätige das nachfolgende Fenster und lasse den Vorgang vollständig durchlaufen.

### 5. Abschluss:  
    Nach erfolgreichem Update erscheint eine Bestätigungsmeldung. Jetzt kannst du die USB-C Verbindung trennen.
