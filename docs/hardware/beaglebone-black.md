# BeagleBone Black

The [K8-B](../boards/k8-b.md), [K8-B-Scroller](../boards/k8-b-scroller.md),
[K64D-B](../boards/k64d-b.md), [K128D-B](../boards/k128d-b.md) and
[OctoPlus](../boards/octoplus.md) are **capes** for the **BeagleBone Black** (BBB). The BBB is a
small computer that runs FPP, and the cape adds the power, outputs and connectors. FPP drives the
outputs from the BBB's two PRUs, small real-time processors beside the main CPU.

## Which BeagleBones work

| Board | Works? | Notes |
|---|---|---|
| **BeagleBone Black** | ✔ | the usual choice |
| **BeagleBone Black Industrial** | ✔ | the same as the BeagleBone Black, with a wider temperature rating |
| **BeagleBone Black Wireless** | ✔ | Wi-Fi instead of Ethernet |
| **BeagleBone Green** | ✔ | no barrel jack (it's powered from the cape anyway) |
| **SanCloud BeagleBone Enhanced** | ✔ | on the OctoPlus, output 5 doesn't work properly |
| BeagleBone Green Wireless | **✘** | not compatible |
| PocketBeagle, PocketBeagle 2, BeagleBone AI | **✘** | different boards. See [PocketBeagle 2](pocketbeagle2.md). |

Kulp Lights sells these boards with or without a BeagleBone Black (or Green) already fitted, and
with or without an SD card with FPP on it.

## Fitting the BeagleBone

The cape connects to the BeagleBone's two 46-pin headers, **P8** and **P9**. How they fit together
depends on the board:

- **K8-B, K8-B-Scroller and OctoPlus:** the cape plugs **on top of** the BeagleBone. The
  BeagleBone's **Ethernet jack** sits in the notch cut out of the cape's edge, so the cape only fits
  one way round.
- **K64D-B and K128D-B:** these capes are much bigger, so the BeagleBone plugs **upside down onto
  the cape**, with its Ethernet jack over the notch in the cape's right-hand edge. Its microSD slot
  then faces up, and its USB-A port is still usable.

If your board came without a BeagleBone fitted:

1. **Disconnect all power.**
2. Line the BeagleBone's Ethernet jack up with the notch in the cape, and both rows of header pins
   with both sockets.
3. Press evenly along both headers, rocking gently end to end, until the two boards are fully
   together.

!!! warning "Check before you power on"
    A cape that is shifted by a row, or fitted the wrong way round, can damage both boards. Check
    that every pin is in its socket and that none are left over at either end.

## Storage: run FPP from an SD card

Run FPP from a **microSD card** in the BeagleBone. Use a good-quality card of 16–32 GB
(A1/A2, U3). Cheap or counterfeit cards are the most common cause of strange problems. You can buy
a card with FPP already installed, or write the BeagleBone Black image yourself. See
[Getting the FPP software](https://manual.falconplayer.com/006-quickstart/#getting-the-fpp-software).
Use **FPP 9.5 or later**; the current release is best.

The BeagleBone also has built-in **eMMC** storage, but on most boards it is only 4 GB, too small
to hold a show's media comfortably, so we recommend the SD card. (BeagleBone Blacks made since late
2025 have 16 GB of eMMC. FPP's *Status/Control → FPP Settings → Storage* page can copy FPP to it.)

### Booting from the SD card

BeagleBones made since about 2019 boot from an SD card on their own: insert the card and power up.

Older boards boot whatever is on their eMMC instead. To boot one of those from the SD card, hold
the **Boot** button while you apply power, and keep holding it until the BeagleBone's LEDs start
flashing. The K64D-B and K128D-B have a **Boot** button on the cape for this. On the other boards,
use the BeagleBone's own Boot button, next to its USB-A port.

## Powering

The BeagleBone is powered **from the cape**: the cape's power terminal feeds the BeagleBone through
its header pins (see [Power](power.md)).

!!! danger "Don't power the BeagleBone a second way"
    - **Don't plug a supply into the BeagleBone's barrel jack** while the cape is powering it. The
      two supplies end up tied together. (The K8-B and K8-B-Scroller have a jumper that lets you
      power the BeagleBone from its barrel jack instead; see their pages.)
    - **Don't connect the BeagleBone's USB port to a computer** (USB tethering) while the cape is
      powered. Set the controller up over the network instead.

### Power button

Each cape has a **Power** button wired to the BeagleBone's own power button, which is hard to reach
once a cape is fitted:

- When FPP is running, a short press shuts the BeagleBone down cleanly, the same as FPP's
  **Shutdown**.
- After a shutdown, the BeagleBone stays off while the cape is still powered. Press **Power** to
  start it again, or switch the supply off and on.
- Holding it down for several seconds forces the BeagleBone off. Use that only if it has hung.

## Network and USB

- **Ethernet:** the BeagleBone's own 10/100 Ethernet jack. The **BeagleBone Black Wireless** has
  Wi-Fi instead.
- **USB:** the BeagleBone has one **USB-A** port, for a USB sound card, Wi-Fi adapter or USB
  storage.
- **Status LEDs:** the BeagleBone's four blue LEDs show it booting and running.
