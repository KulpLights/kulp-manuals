# K16-Pro

16 fused pixel ports with bank switching, 8 two-way differential ports, audio and 2 DMX.

![K16-Pro](../assets/boards/K16-Pro-photo.webp){ .board loading=lazy }

<small>K16-Pro with a PocketBeagle 2 fitted. Photos may show an earlier board revision.</small>

This page describes revision **v4.1.1** (printed on the board as `K16-Pro v4.1.1`). Differences in earlier revisions are listed under [Board revisions](#board-revisions).

## Specifications

| | K16-Pro |
|---|---|
| Local pixel ports | 16 (P1–P16), 3-pin 3.5 mm pluggable, plugs included |
| Port protection | 5 A mini-blade fuse per port |
| Power switching | per bank of 4, FPP-controlled (v4.1 and later) |
| Current monitoring | from Falcon V5 receivers only |
| Differential ports | 8 × RJ45 = 32 strings (17–48), two-way (pair 1/2) |
| Total strings | 48 |
| Power inputs | 4 terminals rated 30 A, 5–24 V DC, one bank of 4 ports each |
| DMX / serial | 2 (`DMX1`, `DMX2`), RS-485 transmit |
| Audio | PCM5102A DAC, 3.5 mm line out, FM transmitter socket |
| Ethernet | 1 × Gigabit (USB-attached) |
| USB-A | 3 |
| Display & buttons | 128×64 OLED, Up / Down / Enter / Back / Test |
| Real-time clock | yes, CR1220 backup cell |
| Fan header | 5 V 4-pin PWM, temperature-controlled; speed monitoring on v4.1 and later |
| Expansion header | 2×6: I²C + 8 GPIO (Exp.1–Exp.8) |
| Size | 168.6 × 139.2 mm (6.64 × 5.48 in), 8 mounting holes, 3.0 mm |
| Requires | PocketBeagle 2 (not PocketBeagle 1), FPP 9.0 or later |

## Board map

![K16-Pro from above](../assets/boards/K16-Pro-top.webp){ .board loading=lazy }

### Power terminals

The four terminals, two on each side, each power one bank of four ports:

| Terminal | Feeds | FPP reading | Also powers the controller? |
|---|---|---|---|
| **Upper left** | P1–P4 | VIN1 | **yes** |
| **Lower left** | P5–P8 | VIN2 | no |
| **Upper right** | P9–P12 | VIN3 | no |
| **Lower right** | P13–P16 | VIN4 | no |

**Each terminal can have its own supply and voltage.** For example, run 12 V pixels on one bank
and 5 V pixels on another, each from a supply that matches its pixels. Just make sure every port in
a bank uses pixels of that bank's voltage. All the grounds are connected together on the board.

The blue LED beside the **upper-left** terminal lights when it has power. **The upper-left
terminal must be powered for the controller to boot.**

See [Power](../hardware/power.md) for supply sizing, wire size and safety.

### Pixel ports

The sixteen pixel ports are in two rows, eight on each side of the board's centre line:

| | Left half | Right half |
|---|---|---|
| **Top row** | P1 P2 P3 P4 | P9 P10 P11 P12 |
| **Bottom row** | P5 P6 P7 P8 | P13 P14 P15 P16 |

Each port is **G D V** (ground, data, +V), as printed beside it. See [Pixel outputs](../hardware/pixel-outputs.md).

### Fuses

Every local port has a **5 A mini-blade fuse** next to it. If a port's green LED is dark while
the rest of its bank is lit, check that port's fuse first. **Never fit a fuse larger
than 5 A.** See [Power → Fuses](../hardware/power.md#mini-blade-fuses-k16-k32-and-the-pro-boards).

### Bank switching

Each bank of four ports has an electronic power switch that FPP controls, so FPP can turn
pixel power off when nothing is playing. See [Power → Bank switching](../hardware/power.md#bank-switching-pro-boards).

Bank switching was added in **v4.1**. On a v4.0 board every bank is on whenever it has
power. See [Board revisions](#board-revisions).

### Differential ports

`17-20` · `21-24` · `25-28` · `29-32` · `33-36` · `37-40` · `41-44` · `45-48`

Each jack carries four strings, numbered as printed above it. They are **two-way**: Falcon V5 smart receivers report their eFuse status and current back over pair 1/2. Other receivers work as send-only.
See [Differential ports](../hardware/differential.md).

### Other connectors

| Connector | Marking | Details |
|---|---|---|
| Ethernet | (RJ45 with LEDs) | [Network](../hardware/network-usb-rtc.md#ethernet) |
| DMX | `DMX1`, `DMX2` | [DMX / serial](../hardware/dmx.md) |
| USB-A | — | 3 ports, [USB](../hardware/network-usb-rtc.md#usb-ports) |
| OLED | `GND 3.3V SCL SDA` | [Controls & display](../hardware/controls.md) |
| Audio out | 3.5 mm jack | [Audio](../hardware/audio.md) |
| FM transmitter | `RST SCL SDA 3.3V G L R` | [Audio](../hardware/audio.md#fm-transmitter-socket) |
| Fan | `Fan 5V` | [Fan](../hardware/expansion.md#fan) |
| Expansion | `Exp` | [Expansion header](../hardware/expansion.md) |
| RTC battery | coin-cell holder | [Clock](../hardware/network-usb-rtc.md#real-time-clock-rtc) |

## FPP setup

When FPP detects the K16-Pro it sets itself up automatically. It enables the
**K16-Pro** pixel-string layout, the sensors (input voltages, temperature), the audio output
and a disabled DMX output. Out of the box each local port is set to 50 WS2811 pixels at 50 % brightness.
Set the real counts and start channels from xLights or the FPP *Pixel Strings* page.
See [Configuring outputs](../software/outputs.md).

## Board revisions

The revision is printed on the board next to the model name. FPP also shows it as the
**Hardware Version** under *Help → About → Cape Info*.

| Revision | Changes |
|---|---|
| **v4.0** | Fused ports; banks are always on when powered. Fan speed control. |
| **v4.1** | Adds **bank switching** (FPP turns each bank of 4 on and off) and **fan speed monitoring**. |

## Dimensions & mounting

- **168.55 × 139.21 mm** (6.64 × 5.48 in), 8 plated mounting holes, 3.0 mm, for **M2.5** (or #4) screws and standoffs.
- The mounting holes are connected to ground.
- Use nylon or metal standoffs at least 6 mm (¼ in) tall, so nothing on the underside touches the
  enclosure.
- Mounting drawing: [PDF](https://kulplights.com/wp-content/uploads/2025/08/K16.pdf). It is shared by the K16, K16-Pro and K16-Max, which have the same outline and holes.
- A 3D-printable mount is on [Thingiverse](https://www.thingiverse.com/thing:7181496).
