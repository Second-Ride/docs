# Accessory: External Charging Port

<p align="center">
  <img src="https://github.com/user-attachments/assets/8fabef5a-67ad-4798-9a29-ee628a3ae56c" width="500" />
</p>

<h2>Requirements</h2>
<table>
  <tr>
    <td valign="top">
      <ul style="list-style-type: none; padding-left: 0;">
        <li><input type="checkbox"> Second Ride Conversion Kit SR23 or SR24</li>
      </ul>
    </td>
    <td></td>
  </tr>
</table>

<h2>Scope of Delivery</h2>
<table>
  <tr>
    <td valign="top">
      <ul style="list-style-type: none; padding-left: 0;">
        <li><input type="checkbox"> 1x External Charging Port</li>
        <li><input type="checkbox"> 1x Charging Plug Cap</li>
        <li><input type="checkbox"> 2x M6x90 Screws</li>
      </ul>
    </td>
    <td valign="top" style="padding-left: 30px;">
      <ul style="list-style-type: none; padding-left: 0;">
        <li><input type="checkbox"> 4x M6x80 Screws</li>
        <li><input type="checkbox"> 1x M8 Screw</li>
        <li><input type="checkbox"> 3x Cable Ties</li>
      </ul>
    </td>
  </tr>
</table>

<h2>Required Tools</h2>
<table>
  <tr>
    <td valign="top">
      <ul style="list-style-type: none; padding-left: 0;">
        <li><input type="checkbox"> 1x 10mm Socket and Ratchet</li>
        <li><input type="checkbox"> Allen Key SW3</li>
        <li><input type="checkbox"> Allen Key SW4</li>
      </ul>
    </td>
    <td valign="top" style="padding-left: 30px;">
      <ul style="list-style-type: none; padding-left: 0;">
        <li><input type="checkbox"> Allen Key SW6</li>
        <li><input type="checkbox"> Phillips and Flathead Screwdriver</li>
        <li><input type="checkbox"> Side Cutters</li>
      </ul>
    </td>
  </tr>
</table>

## Before You Start the Conversion

The purpose of the above-mentioned accessory component is its installation in accordance with this assembly manual, as well as its use on public roads in accordance with the operating manual. Please understand that during the development of the conversion kit and accessories we adhered to the original condition of the mentioned Simson models. In case of conversions with parts that do not correspond to the original, or modifications of original parts due to accidents, wear, or intentional modifications, we cannot guarantee that the conversion kit and accessories will function properly and safely, or even fit at all. If you are unsure about your vehicle, please contact us.  

This document “Accessory: External Charging Port Assembly and Operating Manual” is provided by Second Ride GmbH and is to be understood as a supplement to the original manufacturer’s operating manual. Both documents must be considered as a unit, whereby explanations regarding the combustion engine can be disregarded.  

Please read this document completely and carefully before starting the conversion and before your first ride. Here you will find warnings and notices, information and advice, as well as emergency measures and further important notes regarding your vehicle. Failure to follow the instructions may result in minor or serious injuries, or even danger to life. In addition, the performance of the vehicle may be restricted. Please also carefully read the warnings and notes listed next to the symbols, especially regarding high voltage. Only in this way can proper installation of the conversion kit and accessories, as well as safe operation of the vehicle, be ensured. Ignoring these warnings and notices means you are knowingly accepting potential damage to persons or the vehicle.  

All technical data and descriptions contained here were up to date at the time of printing. However, since continuous improvement is one of our main goals, we reserve the right to make changes to the products at any time. If you notice errors or omissions in this document, please post them in the Discord channel (see chapter “Useful Links”).  

## Installation

### 1. Preparations

!!! warning "Caution"
    Before starting, make absolutely sure that no battery is connected to the drive module or the vehicle, otherwise there is a risk of an electric shock hazardous to health. Please observe the warnings on page 13.

Start by disconnecting the battery pack. Lift the vehicle and make sure the front wheel remains movable, otherwise you cannot access the controller screws. Remove all vehicle parts that are in the way of the installation. On the Schwalbe, these are the cross brace for the leg shield and the motor tunnel, on the SR50 and SR80 the front engine mount. This allows the drive module to be folded down, making installation possible. On SR4-2 and SR4-4 the side panels must be removed. On vehicles with an upper engine mount (KR51, KR51/1, SR4-2, SR4-4), remove the two nuts connecting the M5x engine mount to the drive module.

<p align="center">
  <img src="https://github.com/user-attachments/assets/d4611120-d065-4c8e-be1a-f1c650568955" width="500" />
</p>

### 2. Installation

Using the SW4 Allen key, loosen the four button head screws of the motor controller. The lower two screws also have sleeves, which may fall out during removal. Disconnect the large plug at the bottom of the controller (1) and fold the controller with housing to the side so that it only hangs on the three phase cables. Open the contact cover (2) on the back of the controller by removing the two Phillips screws (3).  

<p align="center">
  <img src="https://github.com/user-attachments/assets/d4611120-d065-4c8e-be1a-f1c650568955" width="500" />
</p>

Loosen the screws at the B+ (red cable) (4) and B- (black cable) (4) terminals. Place the ring terminal of the red cable of the charging adapter (5) onto the screw and screw it back into the thread. Tighten the screw hand-tight and repeat the process with the black cable (5) at the B- terminal.  
Make sure the cables are close together, otherwise the cable cover cannot be reinstalled.  

<p align="center">
  <img src="https://github.com/user-attachments/assets/f8665086-adad-48c8-b7ed-dbde068347e6" width="500" />
</p>

Then reinstall the cable cover (2), ensuring that none of the old or new cables are pinched at the outlets. The two new cables must run to the left of the controller plug (1) in the direction of travel and exit from the bottom of the controller. Plug the controller plug (1) back into the controller. Route the charging adapter along the motor and mount it on the left front face of the motor. The protrusion on the back of the charging adapter defines its position by fitting into a groove on the front face (6). The hole for the M8 screw must align exactly with the thread (7) on the front face. Fasten the charging adapter to the motor using the M8 screw and the SW6 Allen key.  

<p align="center">
  <img src="https://github.com/user-attachments/assets/a91ef741-c7bc-4244-a5e2-01470a533546" width="500" />
</p>

(... full translated installation steps with images as above ...)

## Firmware Update

!!! warning "Caution"
    To use the charging port, Günter (Vehicle Control Unit) must have at least firmware VCU_Firmware_V0.4.0.dfu installed.  
    Higher versions will also be compatible.

Please refer to the update manual that either came with your kit or can be found under [this link](https://www.second-ride.de/docs) in the folder “Firmware Update”.

## Operation of the External Charging Adapter

### 1. Start Charging

!!! warning "Caution"
    To start charging, the charging plug cap must be installed, otherwise the charger will not be recognized, and the charging port will not be enabled.  
    In addition, the system must be switched on so that the charging port is enabled and charging can begin.

Now insert the charging cable into the charging port until it audibly clicks into place. The LED on the vehicle’s button should now change from dim to medium bright to bright. This means the charger is now successfully charging your kit.  

Once charging has started, you can remove the key from the ignition lock and take it with you. This secures your vehicle from unauthorized use.  

### 2. Charging Finished or Interrupted

Once the battery is full, or the charger has stopped charging for another reason, the LED of the button will blink abruptly bright and then dark, without dimming in between. A glance at the charge indicator will show you the battery’s charge level.  
If your charger is disconnected from the power supply during charging, the same behavior occurs.  

As long as the charger is plugged in, active driving mode cannot be enabled, and the vehicle cannot be driven.  

Only when the charging plug is removed from the vehicle can it be operated again. This can be recognized by the LED returning to its familiar dimming pattern.  

### 3. End Charging

The charging process can be interrupted at any time by unplugging the charging plug. Note that turning off the system with the key does not end the charging process.  
