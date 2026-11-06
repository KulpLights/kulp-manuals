# Network, USB & clock

## Ethernet

Every board except the K8-PB, K4-PB, K40D-PB and PocketScroller v2 has one **Gigabit Ethernet** jack, the RJ45 with built-in LEDs. It connects
to the PocketBeagle 2 over USB 2.0, so real throughput is roughly **300 Mb/s**. That is
far more than a show needs, even with hundreds of E1.31 universes.

- Plug it into your show network switch or router.
- Out of the box FPP uses **DHCP**. The IP address appears on the OLED.
- **K8-PB, K4-PB, K40D-PB and PocketScroller v2:** there's no Ethernet jack. Plug a **USB Ethernet adapter** (or a USB Wi-Fi adapter)
  into its USB-A port.
- For networking topics (static IPs, show networks, reaching receivers or controllers
  behind FPP), see the FPP manual:
  [Network](https://manual.falconplayer.com/016-network/) ·
  [Networking overview](https://manual.falconplayer.com/108-networking-overview/) ·
  [Proxies](https://manual.falconplayer.com/024-proxy/).

!!! danger "Only one RJ45 is Ethernet"
    The DMX and differential RJ45 jacks look the same but are **not** network ports. Never
    plug them into a switch or PC.

The Ethernet jack has two built-in LEDs. Left and right are as seen in the photo at the top of
each board page, with the board laid flat and the Ethernet jack on the top edge:

| LED | Meaning |
|---|---|
| **Left** | **Link.** On when the cable is connected to a working switch or router port. |
| **Right** | **Activity.** Flashes as network traffic passes. |

If the link LED stays off, check the cable and the switch port before anything else.

## Wi-Fi

The PocketBeagle 2 has no built-in Wi-Fi. Plug an FPP-supported **USB Wi-Fi adapter**
into a USB-A port to get:

- Wi-Fi as a second network
- FPP's **hotspot (tethering)** mode, for setup in the field

See the FPP manual's [hardware list](https://manual.falconplayer.com/004-hardware/) for
supported adapters.

## USB tethering

You can also set the controller up over a USB cable, with no network at all. Connect the
PocketBeagle 2's **USB-C** port to a computer, wait for FPP to start, then browse to:

- **192.168.7.2** on Windows
- **192.168.6.2** on macOS or Linux

Over USB-C alone, only the PocketBeagle 2 itself is powered: the cape's Ethernet, USB ports and
outputs stay off until the cape has its own power. That's fine for configuring FPP. On the K8, K16
and K32 boards, the K8-PB, the K4-PB, and all the PocketScrollers it's also safe to keep the USB cable
connected while the cape has its own power.

!!! danger "Not on the K40D-PB, or with a PocketBeagle 1"
    Never connect the PocketBeagle's USB port to a computer on a **K40D-PB**, or on a **K4-PB or
    PocketScroller v2 fitted with an original PocketBeagle 1**. It can permanently damage the board.
    Use a USB network adapter instead. A K4-PB or PocketScroller v2 with a PocketBeagle 2 is fine.

## USB ports

| Board | USB-A host ports |
|---|---|
| K8-Pro, K8-Max, K16-Pro, K16-Max, K32-Pro, K32-Max, PocketScroller v3, PocketScroller-16 | 3 (one vertical, plus a stacked pair) |
| K16, K32, K8-PB, K4-PB, K40D-PB, PocketScroller v2 | 1 |

Each port has its own current-limited power switch, about **0.5 A**. That's plenty
for Wi-Fi adapters, sound cards and USB flash drives. Use a powered hub for anything
hungrier, such as a USB hard drive.

!!! warning "K16 and K32: use the included USB extension cable"
    The K16's and K32's single USB-A port needs the **USB extension cable that comes with the
    board**. Plug the cable into the port, then plug your Wi-Fi adapter or other device into the
    cable, not straight into the port. Keep the cable with the controller.

## Real-time clock (RTC)

Every board except the K4-PB and PocketScroller v2 has a battery-backed **real-time clock** (NXP PCF85263,
or PCF85363 on the K8-PB), so schedules start at the right time even with no internet for NTP.
The K4-PB and PocketScroller v2 have no clock, so set up NTP on them.

- Every board takes a **CR1220** 3 V coin cell. On the K8 boards the holder is on the **underside**
  of the board.
- FPP sets the RTC up automatically from the cape. The *RTC* setting is hidden because
  there is nothing to choose.
- Set the time zone and NTP in FPP under
  [Settings → Time](https://manual.falconplayer.com/020-fpp-settings/#localization).


## Temperature

A **TMP1075** sensor on the board (an analog sensor on the K4-PB and PocketScroller v2) reports the board temperature. FPP shows it with the
other sensors. Boards with a fan header use it to run the fan
(see [Expansion header & fan](expansion.md#fan)).
