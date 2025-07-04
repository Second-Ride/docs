# Software Update

To enable feeder usage, you'll need to update both your LumenPnP's firmware and OpenPnP.

## Update OpenPnP

LumenPnP feeders require a specific version of OpenPnP (the 2023-04-05 release), **not** the most recent release on the OpenPnP website. You can download the correct version here:

- Linux ([Download .deb](https://openpnp.s3-us-west-2.amazonaws.com/test/2023-04-05_08-24-36.0aa4ae8/OpenPnP-linux-test.deb))([Download .tar.gz](https://openpnp.s3-us-west-2.amazonaws.com/test/2023-04-05_08-24-36.0aa4ae8/OpenPnP-unix-test.tar.gz))
- Windows ([Download 32 Bit .exe](https://openpnp.s3-us-west-2.amazonaws.com/test/2023-04-05_08-24-36.0aa4ae8/OpenPnP-windows-x32-test.exe)) ([Download 64 Bit .exe](https://openpnp.s3-us-west-2.amazonaws.com/test/2023-04-05_08-24-36.0aa4ae8/OpenPnP-windows-x64-test.exe))
- Mac ([Download .dmg](https://openpnp.s3-us-west-2.amazonaws.com/test/2023-04-05_08-24-36.0aa4ae8/OpenPnP-macos-test.dmg))

!!! danger "Mac Users"
    Because of [a bug with how OpenPnP signs their releases](https://github.com/openpnp/openpnp/issues/1559), Mac users with ARM processors might experience a crash on boot. You can still run OpenPnP by navigating to `Applications -> OpenPnP` and right clicking on the OpenPnP app and selecting "Show Package Contents":

    ![Show package contents on the openpnp app](img/opnp-show-package-contents.webp)

    Then navigate to `Contents -> MacOS` and double click on `JavaApplicationStub` to run OpenPnP.

    ![clicking on javaapplicationstub](img/boot-opnp-java-stub.webp)

## Update LumenPnP Firmware

!!! note "Machines Version v3.0.5+"
    If your machine's version number is `v3.0.5` or greater, you already have firmware that supports feeders. You can skip this section.

1. Download the LumenPnP firmware from the latest release [here](https://github.com/opulo-inc/lumenpnp/releases) that matches your machine's version. Firmware file names start with the machine versions they support.

2. Follow the instructions for [updating your LumenPnP's firmware](../..//guides/update-firmware/index.md).

## Update Feeder Firmware **(Optional)**

**All feeders come with firmware pre-programmed. These instructions are for updating to a new version of firmware, or putting custom firmware on the feeder.**

!!! danger "Set Jumper to 3.3v"
    Make sure that the jumper on your programmer is set to 3.3v. On the 3 pin header, make sure the jumper is connecting the center pin to the pin labeled "3.3v". The feeder logic operates at 3.3v, so it should be set to this prior to use.

    ![programmer jumper](img/programmer-jumper.webp)

1. Connect the included programmer to your computer.
   <!-- TODO: Get photo of programmer plugged into computer -->
2. Download the most recent firmware [here](/software-updates/), a specific version from the [Photon releases page](https://github.com/photonfirmware/photon/releases), or [compile it yourself](https://github.com/opulo-inc/feeder).
3. Download and install the [STM32CubeProgrammer application](https://www.st.com/en/development-tools/stm32cubeprog.html#section-get-software-table).
4. Open the STM32CubeProgrammer application
5. On the Blue dropdown next to the connect button, select `UART`.

    ![Select UART](img/uart-dropdown.webp)

6. Click the circular arrow icon to scan for new devices.

    ![stm32 cube software connect panel](img/refresh-button.webp)

7. Click the `Port` drop down and select the new port that appears. On Mac, this port should start with `cu.usbmodem`.
    ![Select Port](img/select-port.webp)

8. Set the following settings:
    1. `Baudrate: 9600`
    2. `Parity: Even`
    3. `Read Unprotect (MCU): Unchecked`
    4. `TZEN Regression (MCU): Unchecked`

    ![All Settings](img/all-settings.webp)

9.  Hold down the BOOT button located here on the feeder:

    ![boot button](img/boot-button.webp)

10. While holding the BOOT button, insert the pins of the programmer into the plated holes on the feeder as shown in the picture below. The holes are slightly offset, so the programmer pins will stay in contact with the through holes. Once connected, release the BOOT button. If the feeder's LED flashes and turns red, it is not ready to be programmed. Try again.

    !!! Note
        The feeder does not need to be mounted on a rail for this step; it can be powered by the programmer.

    ![offset holes](img/offset-pins.webp)
    ![inserting pins](img/inserting-programmer.webp)
    ![programmer inserted](img/programmer-inserted.webp)
    ![Feeder not ready to be programmed](img/feeder-not-ready.webp)

11. Click the green connect button in STM32CubeProgrammer.
    ![stm32 cube software connect panel](img/connect-button.webp)

    !!! Warning "If You Can't Connect"
        If you can't connect to your feeder, check that the programmer is inserted into the pins in the correct orientation. Also, applying gentle pressure to the side of the programmer can help ensure that the pins are making good contact with the plated holes in the feeder PCB.

    !!! Danger "Try the Alternate Method"
        A small batch of feeders have a hard time entering the bootloader using the instructions above. If you cannot connect, try using the instructions below.

        1. Insert the programmer into the programming port, but do NOT press the boot button. The Status light should turn red.

            ![](img/inserting-programmer.gif)
        2. Press and hold both buttons. Some light patterns will display. Wait until you see red and blue lights flashing, then turn off. Release the buttons. Your feeder is now in the bootloader.

            ![](img/enter-bootloader.gif)
        3. Reattempt connection.
        4. If you still have connection issues, [please reach out to us](https://support.opulo.io/), and [check out this page](../../guides/feeder-uart-boot-fix/index.md).

12. Once connected, Switch to the download tab on the left.
![Download Tab](img/download-tab.webp)

1.  Click the "Browse" button and navigate to the provided `firmware.bin` file.

    ![Browse Button](img/browse-button.webp)

2.  Ensure that the “Start address” is `0x08000000`.

    ![Start Address](img/start-address.webp)

3.  Click "Start Programming".

    ![Start Programming](img/start-programming.webp)

4.  Wait until the software prompts that the firmware has been downloaded successfully. You may disconnect the programmer from the feeder.

    ![programming complete pop up](img/programming-complete.webp)

## Checking Current Firmware Version

1. Press and hold both buttons on the feeder.
1. Wait until the light comes on, indicating that you've [switched modes](../1-overview/feeder-overview.md#__tabbed_2_3).
1. Keep the buttons held until the light goes off.

    !!! danger "Firmware versions v1.0.2 and before"
        Earlier versions of firmware will never turn off the light. If the light stays on, you're running v1.0.2 or earlier. [Update your firmware](#update-feeder-firmware-optional) to get the latest features and bugfixes.

1. Watch the indicator light and take note of its color, and how many times it flashes.

    <figure markdown>
        ![checking feeder firmware version](img/version-check.webp)
        <figcaption>The gif above shows the version being checked for a feeder running `v1.0.3`. Both buttons are held and the mode light comes on. The mode light goes off, and the indicator light flashes green once.</figcaption>
    </figure>

1. Once the indicator light is done flashing, release the buttons.
1. Use the table below to identify the firmware version loaded on your feeder.

| Firmware Version      | Flashes            |            |
| :-------------------- | :----------------- | :--------- |
| Any Beta Firmware     | One Red Flash      | 🟥         |
| v1.0.2 or previous    | No Flash           |            |
| v1.0.3 or higher      | One Green Flash    | 🟩         |

## Next Steps

Next, you'll [mount your feeders.](../4-mounting/mounting.md)
