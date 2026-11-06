# Boards

All of the boards use the same building blocks, so each board page is short and links
to the shared [Hardware](../hardware/power.md) chapters for details.

## Pixel controllers

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

### Which model line?

- **Base (K16, K32):** the most outputs for the money. Fused ports and send-only differential.
- **Pro:** adds two-way differential for Falcon V5 receivers, audio, a second DMX output, three
  USB ports, a fan header and expansion I/O. Bank power switching (K8-Pro, and K16-Pro/K32-Pro from v4.1).
- **Max:** everything in Pro, plus an **eFuse on every port**. FPP can switch each port and read
  its current, and a short is cut in microseconds and reported in FPP instead of blowing a fuse.

## Compact controller: K8-PB

| | K8-PB |
|---|---|
| Local pixel ports | 8, eFused, per-port current reading and power control |
| Differential ports (strings) | 3 (12), send-only |
| Expansion port | 16 strings, through a Falcon F16v4-style expansion board |
| **Total strings** | **36** |
| Power input | 1 terminal, **5–18 V**, for the controller and all ports |
| DMX / serial | 1, on a 3-pin header |
| Ethernet | **none**: add a USB Ethernet or Wi-Fi adapter |
| USB-A | 1 |
| Size (mm) | 74 × 97 |

The K8-PB is the smallest of the pixel controllers. It uses an older output
driver (BBB48String), so it has no Falcon V5 support. See the [K8-PB](k8-pb.md) page.

## LED panels

| | PocketScroller v3 | PocketScroller-16 |
|---|---|---|
| HUB75 outputs | 8 | 16 |
| Power | 5 V only | 5 V only |
| USB-A | 3 | 3 |
| Expansion header | ✔ | ✔ |
| Size (mm) | 122 × 101 | 122 × 144 |
| Minimum FPP | 9.0 | 10.0 |

## All boards

All of them need a **PocketBeagle 2** and run **FPP**. See [PocketBeagle 2](../hardware/pocketbeagle2.md).
