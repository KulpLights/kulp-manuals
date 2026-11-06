# Quick start

Work through this list in order. Each step finishes with a check, so if something goes wrong
you know which step it was.

## What you need

- [ ] The controller, with a **PocketBeagle 2** fitted (see [PocketBeagle 2](../hardware/pocketbeagle2.md))
- [ ] A **microSD card with FPP**, unless you have a PB2 Industrial with FPP on eMMC
- [ ] A **5–24 V DC LED power supply** matched to your pixels (**5 V only** for the PocketScrollers)
- [ ] An **Ethernet cable** to your router or show switch
- [ ] Pixels with a pigtail wired to a 3-pin plug (or LED panels for the PocketScroller)
- [ ] A small flat screwdriver

## 1. Bench test with one string

1. [ ] Read [Safety](safety.md).
2. [ ] Insert the SD card into the PocketBeagle 2, unless you are using eMMC.
3. [ ] Wire **one** pixel string to **P1**: ground in **G**, data in **D**, +V in **V**. Check
       the pixel voltage matches your supply.
4. [ ] Wire the supply to the **terminal that powers the controller**. That's the terminal
       for ports 1–4 on the K16 and K32, and the **right-hand** terminal on the K8 boards. On
       the K8 boards, P1 is fed from the left terminal, so for this test wire both K8 terminals,
       or use P5 instead. See [Power](../hardware/power.md#banks).
5. [ ] Plug in the Ethernet cable.
6. [ ] Plug the supply into the mains.

**Check:** the blue power LEDs light, and within a minute or two the OLED shows the FPP logo and then
the status page with an **IP address**. The first boot of a new SD card can take a few minutes longer.

## 2. Connect to FPP

1. [ ] On a computer on the same network, open a browser to the IP address on the OLED, or to
       `http://fpp.local`.
2. [ ] Work through FPP's first-time setup: hostname, time zone and so on. See
       [Initial configuration](https://manual.falconplayer.com/006-quickstart/#initial-configuration).

**Check:** the FPP status page shows your board under the cape name, and the header shows the
input voltage(s).

## 3. Light the string

1. [ ] Press **Test** on the controller.

**Check:** the string on P1 cycles red, green and blue. Press **Test** until the OLED shows **Off**.

If nothing lights, see [Troubleshooting → No pixels light](../troubleshooting.md#no-pixels-light).

## 4. Configure your show

1. [ ] In xLights, add the controller as an **FPP** controller with your board as the model, map your
       props to its ports, and use **Upload Outputs** to send the port configuration. See
       [Configuring outputs](../software/outputs.md).
2. [ ] Upload sequences and audio with **FPP Connect**, then build a playlist and a schedule in FPP.

## 5. Install

1. [ ] **Main Menu → Shutdown** (or shut down from FPP), then remove power.
2. [ ] Mount the controller in its enclosure. Wire the remaining banks and ports, then the
       differential receivers.
3. [ ] Power up and run the **Test** patterns again to check every port.

!!! tip "Back up"
    Once it's working, save a backup from FPP (*Status/Control → FPP Backup*). See
    [Backup](https://manual.falconplayer.com/022-backup-restore/).
