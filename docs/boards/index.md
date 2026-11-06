# Boards

All of the boards use the same building blocks, so each board page is short and links
to the shared [Hardware](../hardware/power.md) chapters for details.

## PocketBeagle 2 boards

### Pixel controllers

| | K8-Pro | K8-Max | K16 | K16-Pro | K16-Max | K32 | K32-Pro | K32-Max |
|---|---|---|---|---|---|---|---|---|
| Local pixel ports | 8 | 8 | 16 | 16 | 16 | 32 | 32 | 32 |
| Differential ports (strings) | 4 (16) | 4 (16) | 4 (16) | 8 (32) | 8 (32) | 4 (16) | 8 (32) | 8 (32) |
| **Total strings** | **24** | **24** | **32** | **48** | **48** | **48** | **64** | **64** |
| Port protection | fuse | eFuse | fuse | fuse | eFuse | fuse | fuse | eFuse |
| Port power control | bank | port | — | bank† | port | — | bank† | port |
| Per-port current reading | — | ✔ | — | — | ✔ | — | — | ✔ |
| Two-way differential (Falcon V5 receivers) | ✔ | ✔ | — | ✔ | ✔ | — | ✔ | ✔ |
| Power inputs (5–24 V) | 2 | 2 | 4 | 4 | 4 | 8 | 8 | 8 |
| DMX / serial outputs | 1 | 1 | 1 | 2 | 2 | 1 | 2 | 2 |
| Built-in audio + FM socket | ✔ | ✔ | — | ✔ | ✔ | — | ✔ | ✔ |
| USB-A ports | 3 | 3 | 1 | 3 | 3 | 1 | 3 | 3 |
| Fan header | ✔ | ✔ | — | ✔ | ✔ | — | ✔ | ✔ |
| Expansion header | ✔ | ✔ | — | ✔ | ✔ | — | ✔ | ✔ |
| Size (mm) | 103 × 129 | 103 × 129 | 169 × 139 | 169 × 139 | 169 × 139 | 169 × 203 | 169 × 203 | 169 × 203 |

<small>Fuse = 5 A mini-blade per port. eFuse = electronic fuse, about 6 A per port, switchable and
monitored. †Bank switching on the K16-Pro and K32-Pro starts at board revision v4.1.</small>

#### Which model line?

- **Base (K16, K32):** the most outputs for the money. Fused ports and send-only differential.
- **Pro:** adds two-way differential for Falcon V5 receivers, audio, a second DMX output, three
  USB ports, a fan header and expansion I/O. Bank power switching (K8-Pro, and K16-Pro/K32-Pro from v4.1).
- **Max:** everything in Pro, plus an **eFuse on every port**. FPP can switch each port and read
  its current, and a short is cut in microseconds and reported in FPP instead of blowing a fuse.

### Compact controllers: K8-PB, K4-PB and K40D-PB

| | K8-PB | K4-PB | K40D-PB |
|---|---|---|---|
| Local pixel ports | 8, eFused | 4, eFused | — |
| Differential ports (strings) | 3 (12) | — | **10 (40)** |
| Expansion port | 16 strings | — | — |
| **Total strings** | **36** | **4** | **40** |
| Power input | **5–18 V** | **5 or 12 V** | **5 V** only |
| DMX / serial | 3-pin header | 3-pin header | 3-pin terminal |
| Ethernet | none (USB adapter) | none (USB adapter) | none (USB adapter) |
| Real-time clock | ✔ | — | ✔ |
| Size (mm) | 74 × 97 | 71 × 67 | 83 × 99 |

All three use an older output driver (BBB48String), so their differential ports are send-only with
no Falcon V5 support. The K8-PB's expansion port drives 16 strings through a Falcon F16v4-style
expansion board, and the K4-PB fits a small TA-200 enclosure. See the [K8-PB](k8-pb.md),
[K4-PB](k4-pb.md) and [K40D-PB](k40d-pb.md) pages.

### LED panels

| | PocketScroller v2 | PocketScroller v3 | PocketScroller-16 |
|---|---|---|---|
| HUB75 outputs | 6 | 8 | 16 |
| Power | 5 V only | 5 V only | 5 V only |
| Ethernet | none (USB adapter) | ✔ | ✔ |
| USB-A | 1 | 3 | 3 |
| Real-time clock | — | ✔ | ✔ |
| Expansion header | — | ✔ | ✔ |
| Size (mm) | 61 × 73 | 122 × 101 | 122 × 144 |
| Minimum FPP | 9.5 on PB2 (10+ recommended) | 9.0 | 10.0 |

## BeagleBone Black boards

| | K8-B | K8-B-Scroller | K64D-B | K128D-B | OctoPlus |
|---|---|---|---|---|---|
| Local pixel ports | 8, fused | 8, fused | — | — | — |
| Differential ports (strings) | 3 (12) | 1 (4) | **16 (64)** | **32 (128)** | — |
| Expansion port | 16 strings | — | — | — | — |
| HUB75 panel outputs | — | 3 | — | — | **8** |
| **Total strings** | **36** | **12** | **64** | **128** | — |
| Power input | **5–18 V** | **5–18 V** | **5 V** only | **5 V** only | **5 V** only |
| DMX / serial | 2 (header) | 2 (header) | 2 (RJ45, DMX/LOR) | 2 (RJ45, DMX/LOR) | — |
| Built-in audio + FM socket | — | — | ✔ | ✔ | — |
| Real-time clock | ✔ | ✔ | ✔ | ✔ | ✔ |
| Size (mm) | 86 × 109 | 86 × 109 | 182 × 160 | 182 × 225 | 55 × 99 |

All five are capes for the **BeagleBone Black**, which provides the Ethernet and USB port. Their
differential ports are send-only: smart receivers work in v1, v2 or V4 mode. See
[BeagleBone Black](../hardware/beaglebone-black.md).

## Raspberry Pi boards

| | K8-Pi | K2-Pi-Servo | K2-Pi0 |
|---|---|---|---|
| Local pixel ports | 8, eFused | 2, eFused | 2, eFused |
| Differential ports (strings) | 3 (12) | — | — |
| Expansion port | 16 strings | — | — |
| Servo outputs | — | **16** | — |
| **Total strings** | **36** | **2** | **2** |
| Power input | **5–18 V** | 5–24 V (+ servo supply) | 5–24 V |
| DMX / serial | 1 (header) | — | — |
| Display & buttons | ✔ | ✔ | — |
| Real-time clock | ✔ | — | — |
| Raspberry Pi | 3 B+, 4, 5 | 3 B+, 4, 5 | Zero 2 W |
| Size (mm) | 98 × 106 | 76 × 56 | 65 × 30 |

All three are hats for the **Raspberry Pi**, which provides the network and USB ports. FPP drives
their pixel ports with its DPIPixels output: up to 1600 pixels per string, with smart receivers in
v1 or v2 mode. See [Raspberry Pi](../hardware/raspberry-pi.md).

## All boards

All of them run **FPP**. The boards in the PocketBeagle 2 section need a **PocketBeagle 2**;
the K4-PB, K40D-PB and PocketScroller v2 also work with the original PocketBeagle 1. See
[PocketBeagle 2](../hardware/pocketbeagle2.md), [BeagleBone Black](../hardware/beaglebone-black.md)
and [Raspberry Pi](../hardware/raspberry-pi.md).
