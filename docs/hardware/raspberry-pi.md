# Raspberry Pi

The [K8-Pi](../boards/k8-pi.md), [K2-Pi-Servo](../boards/k2-pi-servo.md) and
[K2-Pi0](../boards/k2-pi0.md) are **hats** for the **Raspberry Pi**. The Pi runs FPP, and the hat
adds the power, outputs and connectors.

## Which Raspberry Pis work

| Board | Raspberry Pi |
|---|---|
| **K8-Pi**, **K2-Pi-Servo** | **Pi 3 B+**, **Pi 4** or **Pi 5**. The hat's mounting holes match these Pis. |
| **K2-Pi0** | **Pi Zero 2 W**, the board it is designed for. It also works on an original Pi Zero W and on the bigger Pis, but see the warning on its [board page](../boards/k2-pi0.md#fitting-it-to-a-pi). |

Kulp Lights sells the boards with or without a Pi, and with or without an SD card with FPP on it.

## Fitting the hat

The hat has a 40-pin socket on its underside that plugs onto the Pi's GPIO header.

1. **Disconnect all power.**
2. Screw M2.5 standoffs, nylon or metal, into the Pi's four mounting holes.
3. Line the socket up with **all 40** of the Pi's header pins, and press the hat down evenly until
   it is fully seated on the header and resting on the standoffs.
4. Fix the hat to the standoffs with M2.5 screws.

!!! warning "Check before you power on"
    A hat that is shifted by a row or a column of pins can damage the Pi. Check that every pin is
    in the socket and none are left over. The standoffs keep the hat from bending down onto the
    Pi's USB and Ethernet ports; don't leave them out.

The hat sits close over the Pi, so a tall heatsink or fan on the Pi may not fit underneath it. Use a
low-profile cooler.

## Storage

FPP runs from a **microSD card** in the Pi. Use a good-quality card of 16–32 GB (A1/A2, U3), and
the Raspberry Pi FPP image. See
[Getting the FPP software](https://manual.falconplayer.com/006-quickstart/#getting-the-fpp-software).
Use **FPP 10 or later**; the current release is best.

## Powering

The hat powers the Pi: its own regulator turns the supply on the power terminal into 5 V and feeds
it to the Pi through the GPIO header.

!!! danger "Don't power the Pi a second way"
    - **Don't plug a supply into the Pi's own USB power socket** while the hat is powered. The two
      supplies end up tied together. (The K8-Pi has a jumper that lets you power the Pi from its
      own supply instead; see its page.)
    - **Don't connect the Pi's USB to a computer** (USB tethering) while the hat is powered. Set
      the controller up over the network instead.

!!! tip "Using a 5 V supply"
    The hats' 5 V regulator can't quite hold 5 V when its input is only 5 V, so the Pi may report
    under-voltage. If you power one from a 5 V supply, turn the supply's output up to about
    **5.3 V** (most LED supplies have an adjustment screw).

There is no power button on the hats. To turn off, use FPP's **Shutdown**, then switch off the
supply.

## Pixel outputs on a Pi

FPP drives the pixel ports through the Pi's display output, with its **DPIPixels** output:

- Each string can have up to **1600 pixels**. The frame rate is set by the **longest string**:
  about **40 fps at 800 pixels** and 20 fps at 1600, and faster for shorter strings.
- That variable frame rate arrived in **FPP 10**. FPP 9.5 runs only at 20 or 40 fps.
- Smart receivers on the K8-Pi's differential ports work in **v1 or v2** mode only.
- The Pi's own audio output still works alongside the pixel outputs.

## Network

The Pi 3 B+, Pi 4 and Pi 5 have built-in **Ethernet** and Wi-Fi. The Pi Zero 2 W has **Wi-Fi
only** (2.4 GHz); set it up with FPP's [Wi-Fi hotspot](../software/first-boot.md#no-ethernet-use-the-wi-fi-hotspot).
