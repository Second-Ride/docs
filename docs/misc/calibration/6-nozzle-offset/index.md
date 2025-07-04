# Top Camera to Nozzle Offset

![](../../calibration/img/lumenpnp-v3-docs-logo-small.png)

Calibrating the nozzle offset ensures precise alignment between the nozzle tips and the top camera. This process involves capturing the exact position of the nozzle tip and aligning the top camera to the same reference point. The calibration is essential for accurate component placement and must be performed carefully.

This guide will calibrate both nozzles, ensuring they share the same focal plane as your datum board, components, and PCBs.

---

## Nozzle: N1 Offset (Left Toolhead)

For these steps, you should be in the `Machine Setup` tab.

!!! danger "🚨 Critical Warning: Level Nozzles 🚨"
    ⚠️ **You must ensure that your nozzles are level**.<br/><br/>
    **Failure to do this can cause crashes and potentially damage your machine.**<br/><br/>
    Use the `P` between the Z-axis up/down arrows to ensure the nozzle tips are out of the way. The `P` stands for **Parking** the nozzle out of the way into a safe height that won’t collide with any objects.<br/><br/>
      ![level nozzles](../../../openpnp/v4/calibration/2-connect-to-machine/images/level-nozzles-gif.gif)

1. **Select the correct nozzle to control**.
    * In the bottom left of OpenPnP, select `Nozzle: N1 - N045 (Head:H1)` from the **machine controls** dropdown. This ensures that movements and adjustments apply to the **left** nozzle equipped with the `N045` nozzle tip.<br/><br/>
     ![Select nozzle from machine control dropdown](../../../openpnp/v4/calibration/6-nozzle-offset/images/01-seleect-nozzle-n1-from-machine-controls.webp)
<br/><br/>

1. **Confirm the correct nozzle tip is installed**.
    * Confirm that the `N045` nozzle tip is securely attached to **Nozzle: N1 (left toolhead)**.
<br/><br/>

1. **Open the Nozzle: N1 settings**.
    * Click through the following path: `Heads > ReferenceHead H1 > Nozzles > ReferenceNozzle N1`.<br/><br/>
     ![Open the Nozzle: N1 settings](../../../openpnp/v4/calibration/6-nozzle-offset/images/02-reference-nozzle-n1-settings.webp)
<br/><br/>

1. **Open the Offset Wizard tab**.
    * Navigate to the `Offset Wizard` tab, where the nozzle offset calibration process will be performed.<br/><br/>
     ![Offset wizard settings](../../../openpnp/v4/calibration/6-nozzle-offset/images/03-offset-wizard-tab.webp)
<br/><br/>

1. **Confirm the ‘Include Z?’ setting**.
    * Ensure that the `Include Z?` checkbox is checked. This ensures that the Z-height is properly factored into the calibration process.<br/><br/>
     ![include z checkbox](../../../openpnp/v4/calibration/6-nozzle-offset/images/04-include-z.webp)
<br/><br/>

1. **Position Nozzle: N1 over the homing fiducial**.
    * Jog Nozzle: N1 (left toolhead) so that the **nozzle tip *barely* touches the datum board** and is perfectly centered over the homing fiducial. **Avoid collisions while jogging the nozzle tip**.<br/><br/>
    * Use the shiny edges of the fiducial that are visible around the nozzle tip to determine proper centering. Accuracy here is crucial to achieving precise placements, so please take your time with this and ensure it is dead center.<br/><br/>
     ![Nozzle almost touching homing fiducial](images/PXL_20220519_181926227.webp)
     ![Nozzle touching the homing fiducial](images/PXL_20220519_181952658.webp)
<br/><br/>

1. **Capture Nozzle: N1’s position**.
    * Click the `Store nozzle mark position` button within the **Offset Wizard** tab to capture the Nozzle: N1's location for calibration purposes.
    * Do not navigate away from the **Offset Wizard tab** while you go through the following steps to capture the nozzle offset.<br/><br/>
     ![Store the nozzle's position](../../../openpnp/v4/calibration/6-nozzle-offset/images/06-store-nozzle-mark-position-n1.webp)
<br/><br/>

1. **Raise Nozzle: N1 off the datum board**.
    * Click the letter `P` between the Z up/down arrows to “**Park**” the nozzle at a safe height. This prevents collisions when moving the top camera into position.<br/><br/>
     ![Level the nozzles](../../../openpnp/v4/calibration/2-connect-to-machine/images/level-nozzles-gif.gif)

    !!! Note
        The nozzles may not be level when clicking the “**Park**” button, which is okay. The nozzle only moves to the point that it reaches the “safe zone” and then stops.
<br/><br/>

1. **Align the top camera over the homing fiducial**.
    * Jog the **X** and **Y** axes to bring the top camera directly over the same homing fiducial used in the previous step so it is in the exact center of the camera feed. **Do not switch away from the Offset Wizard tab**. OpenPnP **will not save** your nozzle mark position.<br/><br/>
     ![bring the top camera over the homing fiducial](../../../openpnp/v4/calibration/6-nozzle-offset/images/07-center-cam-over-homing-fid-to-capture-position.gif)
<br/><br/>

1.  **Calculate the nozzle offset**.
    * Once the homing fiducial is centered in the top camera view, click `Calculate nozzle offset`. This determines the offset distance between the nozzle and the top camera based on their recorded positions.<br/><br/>
     ![calculate the nozzle offset](../../../openpnp/v4/calibration/6-nozzle-offset/images/08-calculate-nozzle-offest.webp)
<br/><br/>

1. **Apply and Save Nozzle offset**.
    * Click `Apply` in the lower right corner to store the calculated offset for the left N045 nozzle tip.<br/><br/>
      ![click the apply button](../../../openpnp/v4/calibration/2-connect-to-machine/images/apply-button.webp)<br/><br/>
    * Save your OpenPnP configuration now. `File > Save Configuration`.<br/><br/>
      ![Save your config now](../../../openpnp/v4/calibration/2-connect-to-machine/images/save-config.webp)<br/><br/>

---

## Nozzle: N2 Offset (Right Toolhead)

For these steps, you should already be in the `Machine Setup` tab.

!!! danger "🚨 Critical Warning: Level Nozzles 🚨"
    ⚠️ **You must ensure that your nozzles are level**.<br/><br/>
    **Failure to do this can cause crashes and potentially damage your machine.**<br/><br/>
    Use the `P` between the Z-axis up/down arrows to ensure the nozzle tips are out of the way. The `P` stands for **Parking** the nozzle out of the way into a safe height that won’t collide with any objects.<br/><br/>
      ![level nozzles](../../../openpnp/v4/calibration/2-connect-to-machine/images/level-nozzles-gif.gif)

1. **Confirm the correct nozzle is installed**.
    * Confirm that the `N24` nozzle tip is still securely attached to **Nozzle: N2 (right toolhead)**.<br/><br/>

2. **Select the correct nozzle to control**.
    * In the bottom left of OpenPnP, select `Nozzle: N2 - N24 (Head:H2)` from the **machine controls** dropdown. This ensures that movements and adjustments apply to the **right** nozzle equipped with the `N24` nozzle tip.<br/><br/>
     ![Select nozzle from machine control dropdown](../../../openpnp/v4/calibration/6-nozzle-offset/images/09-select-nozzle-n2-offset.webp)
<br/><br/>

1. **Open the Nozzle: N2 settings**.
    * Click through the following path: `Heads > ReferenceHead H1 > Nozzles > ReferenceNozzle N2`.<br/><br/>
     ![Open the Nozzle N2 settings](../../../openpnp/v4/calibration/6-nozzle-offset/images/10-nozzle-n2-settings.webp)
<br/><br/>

1. **Open the Offset Wizard tab**.
    * Navigate to the `Offset Wizard` tab if you are not already there.<br/><br/>
     ![Offset wizard settings](../../../openpnp/v4/calibration/6-nozzle-offset/images/11-nozzle-n2-offset-wizard.webp)
<br/><br/>

1. **Confirm the ‘Include Z?’ setting**.
    * Ensure that the `Include Z?` checkbox is checked. This ensures that the Z-height is properly factored into the calibration process.<br/><br/>
     ![use the include z checkbox](../../../openpnp/v4/calibration/6-nozzle-offset/images/12-include-z-for-nozzle-n2.webp)
<br/><br/>

1. **Position the nozzle over the homing fiducial**.
    * Jog Nozzle: N2 (right toolhead) so that it is perfectly centered over the homing fiducial, while *barely* touching the datum board. **Avoid collisions while jogging the nozzle tip**.<br><br/>
     ![Nozzle touching the homing fiducial](../../../openpnp/v4/calibration/6-nozzle-offset/images/13-nozzle-n2-centered-and-touching-homing-fid.webp)<br><br/>
    * This nozzle tip is larger than the last one, which is okay. We will use the circle just outside of the homing fiducial to determine if you've centered it correctly. Please take your time with this and ensure it is dead center.
<br/><br/>

1. **Capture the Nozzle: N2’s position**.
    * Click the `Store nozzle mark position` button within the **Offset Wizard** tab to capture Nozzle: N2's location for calibration purposes.
    * Do not navigate away from the **Offset Wizard tab** while you go through the following steps to capture the nozzle offset.<br/><br/>
     ![Store Nozzle: N2's position](../../../openpnp/v4/calibration/6-nozzle-offset/images/14-store-nozzle-n2-mark-position.webp)
<br/><br/>

1. **Raise Nozzle: N2 off the datum board**.
    * Click the letter `P` between the Z up/down arrows to “**Park**” the nozzle at a safe height. This prevents collisions when moving the top camera into position.<br/><br/>
     ![Level the nozzles](../../../openpnp/v4/calibration/2-connect-to-machine/images/level-nozzles-gif.gif)

    !!! Note
        The nozzles may not be level when clicking the “Park” button, which is okay. The nozzle only moves to the point that it reaches the “safe zone” and then stops.
<br/><br/>

1. **Align the top camera over the homing fiducial**.
    * Jog the top camera to be directly over the homing fiducial so it is in the exact center of the camera feed. **Do not switch away from the Offset Wizard tab**. OpenPnP **will not save** your nozzle mark position if so.<br/><br/>
     ![bring the top camera over the homing fiducial](../../../openpnp/v4/calibration/6-nozzle-offset/images/15-center-top-cam-over-homing-fid-nozzle-n2.gif)
<br/><br/>

1.  **Calculate the nozzle offset**.
    * Once the homing fiducial is centered in the top camera view, click `Calculate nozzle offset`. This determines the offset distance between the nozzle and the top camera based on their recorded positions.<br/><br/>
     ![calculate the nozzle offset](../../../openpnp/v4/calibration/6-nozzle-offset/images/16-calculate-nozzle-offset-button-nozzle-n2.webp)
<br/><br/>

1. **Apply and Save Nozzle offset**.
    * Click `Apply` in the lower right corner to store the calculated offset for the right N24 nozzle tip.<br/><br/>
     ![click the apply button](../../../openpnp/v4/calibration/2-connect-to-machine/images/apply-button.webp)<br/><br/>
    * Save your OpenPnP configuration now. `File > Save Configuration`.<br/><br/>
      ![Save your config now](../../../openpnp/v4/calibration/2-connect-to-machine/images/save-config.webp)<br/><br/>

---

!!! note
    For more information about this step, you can read the OpenPnP docs about it [here](https://github.com/openpnp/openpnp/wiki/Setup-and-Calibration_Nozzle-Setup).

!!! info "Further Adjustment"
    If you find that your placement accuracy is slightly incorrect after performing this calibration, you can fine-tune your part placement by adjusting the X and Y offsets in the relevant nozzle settings, as shown below.
    ![nozzle offsets](../../../openpnp/v4/calibration/6-nozzle-offset/images/17-manually-adjust-nozzle-offset.webp)

---

## Next Steps

Next is [Bottom Camera Position](../7-bottom-camera-position/index.md).
