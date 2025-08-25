# Instructions for Firmware Update

Since April 2025, all components of the conversion kit are programmed with the new web update tool. The previous program “DFU Buddy” is no longer used. With the web update tool, you can conveniently and safely update your moped via the Chrome browser: [Link to Web Update Tool](https://second-ride.de/update)  

## What is actually being updated?

The firmware is the software that controls the behavior of your vehicle – how it accelerates, brakes, charges, or displays the charging status. We continuously improve this software to provide you with a better riding experience. With the update tool, you can easily install these improvements yourself.  

## Which components require updates?

Depending on the configuration of your conversion kit, this affects one or two devices:

- Drive module (“Günter”)  
- Battery (“Gisela”), only if your battery has a USB-C port  
- Bluetooth module, if available  

You can find out if a new update is available and what has changed in the [Firmware Changelog](https://docs.google.com/document/d/16SFpTpeRKDW-OlozgDFcO0iHk5q1t2Q6hK-TyoXaMT0/edit?usp=sharing).  

## Updating the Drive Module (“Günter”)

!!! warning "Caution"
    Never connect the seat bench and the drive module to your computer via cable at the same time. Always disconnect the battery plug first before connecting your laptop to the seat bench/BT module or the drive module.

!!! warning "Caution"
    A firmware update changes the driving behavior. It can lead to higher acceleration, higher top speed, different braking behavior, etc. So be especially attentive and careful during the first rides after the update and do not rely on your previous experience with the drive. Also read the changelog carefully.

!!! warning "Caution"
    Installing Duo firmware on a vehicle other than the Simson Duo voids the operating license of the vehicle. The same applies if the non-Duo firmware is installed on the Simson Duo.

First, the drive module must be connected to your PC. Proceed as follows:

### 1. Locate the diagnostic cable

#### 1.1. Long diagnostic cable (from AM#00193)

On drive modules with serial number #00193 and higher, a third cable about 40 cm long should come out of the bottom of the drive module. The plug has a rubber cap. If this is the case, continue with step 2.

#### 1.2. Short diagnostic cable (up to AM#00193)

On drive modules with serial numbers #00038 to #00192, you will find the update cable as follows:

##### 1.2.1. Remove the cable cover
Remove the cable cover from the drive module by unscrewing the M4 cylinder head screw (1) on the right side. You need a 3 mm Allen key for this. If your cable cover has an oval cutout on the top left in the driving direction, then underneath it hides a second M4 cylinder head screw, which only needs to be loosened one turn to remove the cover.

<p align="center">
  <img src="https://github.com/user-attachments/assets/f2d34c5d-6cfd-4838-9ac2-75c5c04d5d5b" width="500" />
</p>

##### 1.2.2. Identify the diagnostic cable

Now you have found the Vehicle Control Unit (2) (we affectionately named it “Günter”). From Günter, a short cable (3) comes out, which is not connected and is covered with a rubber cap.

### 2. Connect USB cable

<div style="border: 2px solid orange; background-color: #fff8e1; padding: 15px; border-radius: 8px;">
   For safety reasons, the battery must not be connected to the drive module during the update. Make sure the seat bench is not connected.
</div>

Remove the rubber cap and connect the supplied USB cable. Important: Make sure the arrows on the male and female connectors align before pushing them together firmly. Then connect the USB cable to your PC.

### 3. [Open the Web Update Tool](http://Second-ride.de/update): → Use only with Google Chrome.

### 4. Select firmware:  
   Under “Drive Module / Günter”, select the desired firmware version and click on “Connect”.  

<p align="center">
  <img src="https://github.com/user-attachments/assets/263f4fd9-54f9-4818-91ee-71439bb3a486" width="500" />
</p>

### 5. Establish connection:  
   A window will open, offering you the option to choose from different devices. Select the STM32… and confirm with “Connect” at the bottom right.  

<p align="center">
  <img src="https://github.com/user-attachments/assets/48619cba-1325-434a-9ad0-f54f5b51cba6" width="500" />
</p>

### 6. Start firmware update:  
   Before confirming the update process with “Execute update”, make sure the cable connection is stable – an interruption can damage the electronics.   
   Now click on “Execute update” and let the process run completely.  

<p align="center">
  <img src="https://github.com/user-attachments/assets/b6f56cae-6cbb-4822-a888-f3f000b02b1b" width="500" />
</p>

### 7. Finish:  
   After a successful update, a confirmation message will appear under the two blue update bars.  
   Now you can disconnect the cable from the diagnostic connector and your laptop.  

## Updating Seat Bench / Bluetooth Module {#update-seat-bench-bluetooth-module}

For the app to work correctly, the firmware version of the seat bench or BT module must match the app version in the first digit. Example: Gisela V1.0.0 is compatible with App V1.1.3. Gisela V1.0.0 is not compatible with App V2.0.0.  
You can find the app version at the bottom of the app when you tap the info icon at the top left.  

!!! warning "Caution"
    Never connect the seat bench and the drive module to your computer via cable at the same time. Always disconnect the battery plug first before connecting your laptop to the seat bench or the drive module.

1. Connect the seat bench or the BT module to your laptop with a USB-C cable via the USB-C port next to the Second Ride logo. The USB-C port on the BT module/seat bench should now light up.  

<p align="center">
  <img src="https://github.com/user-attachments/assets/272cd4d2-0535-4927-8e30-e2f53e4c697e" width="500" />
</p>

2. Open Web Update Tool: → Use only with Google Chrome or Edge.

3. Select firmware:  
   Under “Update Seat Bench & BT Module”, select the appropriate firmware version from the dropdown menu and click Connect. The firmware “Gisela V4 Base Version” only contains the basic functionality without any Bluetooth functions. Therefore, select the other available firmware.  

<p align="center">
  <img src="https://github.com/user-attachments/assets/6661c5ee-31d5-40d0-b0bc-c57f402e19b8" width="500" />
</p>

4. Establish connection:  
   A window should now open displaying a USB port (highlighted in blue here). You can recognize it by the word “paired” next to it.  
   Select this and click “Connect”.  

<p align="center">
  <img src="https://github.com/user-attachments/assets/2605475f-150d-4631-b5f4-f1519bebe291" width="500" />
</p>

5. Start firmware update:  
   After a short loading time, the following window should appear.  

<p align="center">
  <img src="https://github.com/user-attachments/assets/42255bed-13c9-417a-913b-fca0c1555864" width="500" />
</p>

   Before clicking on “Install Gisela V4”, make sure the cable connection is stable – an interruption can cause damage.  

   Click “Install”, confirm the next window, and let the process run completely.  

6. Finish:  
   After a successful update, a confirmation message will appear. You can now disconnect the USB-C connection.  

When both the drive module and the seat bench/BT module have been updated to the latest firmware, you can use the app as intended and pair your vehicle.  

The next steps for app usage are described in the following chapter.  
