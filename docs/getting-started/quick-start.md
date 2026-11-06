# Quick start

Work through this list in order. Each step finishes with a check, so if something goes wrong
you know which step it was.

## What you need

- [ ] The controller, with a **PocketBeagle 2** fitted (see [PocketBeagle 2](../hardware/pocketbeagle2.md))
- [ ] A **microSD card with FPP**, unless you have a PB2 Industrial with FPP on eMMC
- [ ] A **5–24 V DC LED power supply** matched to your pixels (**5 V only** for the PocketScrollers)
- [ ] An **Ethernet cable** to your router or show switch. The K8-PB, K4-PB, K40D-PB and PocketScroller v2
      have no Ethernet jack, so they also need a **USB Ethernet adapter** (or a USB Wi-Fi adapter).
- [ ] Pixels with a pigtail wired to a 3-pin plug (or LED panels for the PocketScroller)
- [ ] A small flat screwdriver

## 1. Bench test with one string

On the **K40D-PB**, which has no pixel ports, wire the string to a differential receiver on the
`1-4` jack instead, and power the K40D-PB from a 5 V supply.

1. [ ] Read [Safety](safety.md).
2. [ ] Insert the SD card into the PocketBeagle 2, unless you are using eMMC.
3. [ ] Wire **one** pixel string to **P1**: ground in **G**, data in **D**, +V in **V**. Check
       the pixel voltage matches your supply.
4. [ ] Check the supply before connecting it: set its **115V/230V** input switch (if it has one) to
       match your mains, then plug it in and measure the DC output with a multimeter. Unplug it
       again before wiring. See [Check the supply](../hardware/power.md#check-the-supply-before-you-connect-it).
5. [ ] Wire the supply to the **terminal that powers the controller**. That's the terminal
       for ports 1–4 on the K16 and K32, and the **right-hand** terminal on the K8 boards. On
       the K8 boards, P1 is fed from the left terminal, so for this test wire both K8 terminals,
       or use P5 instead. The K8-PB and K4-PB have a single terminal for everything.
       See [Power](../hardware/power.md#banks).
6. [ ] Plug in the Ethernet cable (on the K8-PB, K4-PB, K40D-PB or PocketScroller v2, through the USB Ethernet adapter).
7. [ ] Plug the supply into the mains.

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
