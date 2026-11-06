# Expansion header & fan

## Expansion header (Exp)

The **Pro** and **Max** boards, the **PocketScroller v3** and the **PocketScroller-16** have a 2×6, 2.54 mm pin header
marked **Exp**. It brings out the cape's I²C bus and **eight general-purpose I/O pins**,
which FPP names `Exp.1` to `Exp.8`.

Use them for:

- **Buttons and switches.** In FPP, set up *GPIO Inputs* to start playlists, run commands
  or trigger effects. See the [FPP manual](https://manual.falconplayer.com/060-gpio-inputs/).
- **Outputs** to relays (through a driver or relay module), such as a "show running"
  light.
- **I²C accessories** such as extra sensors.

The pin positions differ between boards, so check the numbers printed next to the
header.

The **K8-PB** has a different, 24-pin expansion port that drives 16 extra pixel strings through a
Falcon F16v4-style expansion board. See its [board page](../boards/k8-pb.md#expansion-port-strings-2136).

=== "K8, K16 and K32 Pro & Max"

    | Pin | Signal | Pin | Signal |
    |---|---|---|---|
    | 1 | 3.3 V | 2 | Exp.1 |
    | 3 | SDA | 4 | Exp.2 |
    | 5 | SCL | 6 | Exp.3 |
    | 7 | Exp.4 | 8 | Exp.5 |
    | 9 | GND | 10 | Exp.6 |
    | 11 | Exp.7 | 12 | Exp.8 |

=== "PocketScroller v3, PocketScroller-16"

    | Pin | Signal | Pin | Signal |
    |---|---|---|---|
    | 1 | 3.3 V | 2 | Exp.8 |
    | 3 | SDA | 4 | Exp.7 |
    | 5 | SCL | 6 | Exp.6 |
    | 7 | Exp.4 | 8 | Exp.5 |
    | 9 | GND | 10 | Exp.3 |
    | 11 | Exp.1 | 12 | Exp.2 |

!!! warning "Electrical limits"
    The Exp pins come from an I²C I/O expander. They are **3.3 V only**, and they
    **pull up weakly and can only sink current**. Use them with switches to ground, or to
    drive a transistor or an opto-isolated relay module. Do **not** connect 5 V or 12 V
    signals, and don't drive LEDs or relays directly.

The K16 and K32 have no expansion header.

## Fan

The **Pro** and **Max** boards have a 4-pin **5 V PWM fan** header marked **Fan 5V**.
It's the standard PC-fan layout:

| Pin | Signal |
|---|---|
| 1 | GND |
| 2 | +5 V |
| 3 | Tach (speed sense) |
| 4 | PWM (speed control) |

Use a **5 V** 4-pin PWM fan. 12 V PC fans won't spin properly. FPP controls the fan
from the board temperature sensor:

| Board temperature | Fan speed |
|---|---|
| below 40 °C | off |
| 40 °C | about 30 % |
| 50 °C | about 60 % |
| 60 °C and above | 100 % |

A fan is optional. Most installations don't need one, but it helps in a closed
enclosure in direct sun, or with Max boards running many ports near their limit.

Boards from revision **v4.1** also read the fan's tach signal, so FPP can monitor the
fan's speed. Earlier boards control the fan the same way but can't tell whether it is
spinning.
