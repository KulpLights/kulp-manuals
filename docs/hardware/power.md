# Power

## Banks

The local pixel ports are grouped in **banks of four**. Each bank gets its power from
one **power input terminal**. Every port in a bank receives that terminal's voltage,
so a bank must be wired to a supply that matches the pixels on all four of its ports.

- Each bank can run its own voltage, so 5 V, 12 V and 24 V pixels can share one
  controller as long as they are on **different banks**.
- All grounds (G/V−) are connected together on the board.
- The [differential ports](differential.md) carry **data only**. Strings on differential
  receivers are powered at the receiver.

The terminals are marked on the board **V+ 5-24V** and **G/V−**. Each board page shows
which terminal feeds which ports.

| Board | Power terminals | Bank size | Terminal that also powers the controller |
|---|---|---|---|
| K8-Pro, K8-Max | 2 | 4 ports | the **right-hand** terminal (ports 5–8) |
| K16, K16-Pro, K16-Max | 4 | 4 ports | **V1**, upper left (ports 1–4) |
| K32, K32-Pro, K32-Max | 8 | 4 ports | **V1**, top left (ports 1–4) |
| PocketScroller v3, PocketScroller-16 | 1 (5 V only) | — | the only terminal |

!!! important "One terminal also runs the controller"
    The PocketBeagle 2, network, USB, OLED and all of the controller's logic run from
    **one** specific power terminal (the last column above). If that terminal has no
    power, the controller won't boot, even with every other bank powered. The other
    terminals power only their own pixel ports.

    A blue LED next to that terminal lights when it has power. A second blue LED shows
    that the controller's internal 5 V supply is running.

## Voltage

- **K-series boards:** each terminal accepts **5 V to 24 V DC** (as printed next to the
  terminal). Use a regulated 5 V, 12 V or 24 V LED power supply. Do not go above
  24 V; there is no extra headroom for 28 V or 36 V supplies.
- **PocketScroller v3 and PocketScroller-16:** **5 V DC only.** See their board pages.
- A 5 V supply on the logic terminal is fine. The controller's internal 5 V regulator
  passes it straight through (about 4.96 V out from 5.0 V in), so 5 V-only setups need no
  separate supply.

### Reverse polarity

Each power input has an *ideal diode* in series. If a supply is wired backwards, that
bank simply stays off; nothing on the controller is damaged. Fix the wiring and the
bank will come up. Pixels have no such protection; see [Safety](../getting-started/safety.md).

### Voltage readings in FPP

FPP shows each input voltage in its status bar and on the OLED status pages
(**VIN1**, **VIN2**, …). The terminals aren't numbered on the board, so each board page has a
map of which **VIN** reading belongs to which terminal. On the K32 boards, for example,
**VIN3** is the *right-hand* top terminal (ports 17–20).

## Choosing power supplies

- Use **regulated, constant-voltage** LED power supplies (often sold as 350 W 5 V/12 V/24 V
  "Meanwell-style" units). Constant-current LED drivers are **not** suitable.
- Size the supply for **the pixels**, not the controller. The controller itself needs only
  a few watts.
- Pixel current depends on brightness and colour. A full-white string draws its full
  rated current; most shows average far less. Common practice is to size each supply
  for about 60–80 % of the pixels' full-white load, and to cap brightness in FPP or
  xLights if needed.
- One supply can feed several banks, as long as each wire run is sized for its current.

### Check the supply before you connect it

Do this for every supply, new or used, **before** you wire it to the controller:

1. **Set the AC input switch.** Many supplies have a small slide switch, often red, marked
   **115V / 230V** (or 110V / 220V). Set it to match your mains: **115 V** in North America,
   **230 V** in most of Europe, Asia and Australia. A supply set to 115 V and plugged into 230 V
   mains is destroyed at once, and can catch fire. One set to 230 V on 115 V mains won't start
   or gives a low output. Supplies without the switch accept either.
2. **Measure the output.** With nothing connected to the DC side, plug the supply in and
   measure across its **V+** and **V−** (COM) terminals with a multimeter. Check it reads the
   voltage your pixels need (5, 12 or 24 V) and that + and − are where you expect. If it is
   slightly off, most supplies have a **V.ADJ** trim pot next to the terminals.
3. **Unplug the supply** and wait for its LED to go out before you wire it to the controller.

### Wire size

Use copper wire sized for the **highest current that wire can carry**. That means the
bank's total for supply-to-terminal wires, and the port fuse or eFuse rating for
pixel leads.

| Current (continuous) | Minimum wire |
|---|---|
| up to 5 A (one port) | 18 AWG (0.75 mm²) |
| up to 10 A | 16 AWG (1.5 mm²) |
| up to 15 A | 14 AWG (2.5 mm²) |
| up to 20 A (a fused bank: 4 ports × 5 A) | 12 AWG (4 mm²) |
| up to 24 A (a Max bank: 4 ports × 6 A) | 10 AWG (6 mm²) |

!!! tip "Bank power wiring"
    Use **12 AWG or 10 AWG** wire from the power supply to each bank terminal. The terminals
    are rated **30 A** each, which is more than a bank can draw: 20 A on a fused bank, 24 A on a
    Max bank.

Keep supply-to-controller runs short. For long runs, go up a wire size so the voltage
drop stays small.

## Port protection: fuses and eFuses

Every local pixel port has its own overcurrent protection. What kind depends on the
model:

| Model | Port protection | Per-port power control | Per-port current reading |
|---|---|---|---|
| **K16, K32** | 5 A mini-blade fuse | no | no |
| **K8-Pro, K16-Pro, K32-Pro** | 5 A mini-blade fuse | yes, **per bank of 4**[^banks] | only from Falcon V5 receivers |
| **K8-Max, K16-Max, K32-Max** | **eFuse, about 6 A** | yes, **per port** | **yes, every port** |

### Mini-blade fuses (K16, K32 and the Pro boards)

- Each port has an automotive **mini-blade** fuse (ATM/APM style). **All of them are 5 A**, on every board. Spares are
  sold as a [10-pack](https://kulplights.com/product-category/accessories/) and at any
  auto-parts store.
- Each port has a green LED. It lights when that port has power, which means the bank
  is powered (and switched on, on Pro boards) and the fuse is intact. **A dark LED on
  a powered bank usually means a blown fuse.**
- **Never fit a fuse larger than 5 A.** Find the cause of a blown fuse (a short in the
  pigtail, a pinched wire, water in a connector) before you replace it.


### eFuses (Max boards)

The Max boards replace each port's fuse with an **eFuse**, an electronic fuse that FPP
can switch on and off and read back.

- **Trip point:** about **6 A** per port (5.6–6.4 A). A hard short trips it at once.
- **When it trips** the port turns off and **stays off** (it latches). The port's LED goes
  dark, FPP shows a warning, and the [Port Status](../software/current-monitoring.md)
  page marks the port as tripped.
- **To reset:** fix the cause, then click the port's red :material-close-circle: icon on
  **Status/Control → Port Status**. Power-cycling the controller also resets it.
- FPP can retry tripped ports automatically. See
  [eFuse auto-retry](../software/current-monitoring.md#efuse-auto-retry).
- FPP reads every port's **current** continuously. See
  [Current monitoring](../software/current-monitoring.md).

!!! warning "Power injection on Max boards"
    If you inject power at the far end of a string, use **the same power supply** that
    feeds that port's bank. A *different* supply at even a slightly higher voltage pushes
    current backwards into the port. The eFuse treats that as a fault and switches the
    port off.

<!-- Keep this warning. It applies to the TPS2663x eFuses, not the TPS1663x alternates, but
eFuse stock varies, so any batch may have either. -->

### Bank switching (Pro boards)

On the Pro boards each bank has an electronic power switch that FPP controls. All four
ports of a bank switch together. The K8-Pro has had bank switching since v4.0. The
K16-Pro and K32-Pro have it from **v4.1**; on v4.0 boards every bank is on whenever it
has power. The revision is printed next to the model name on the board.

- With FPP's **Automatically turn on/off outputs** setting on (the default, under
  *Settings → Output*), FPP turns bank power off when it has no data to send and back
  on when a sequence or test starts. That cuts the idle draw of the pixels.
- The port LEDs show the switch state: a bank that is switched off has all four LEDs
  dark.
- The voltage readings in FPP are taken **before** the switch, so a switched-off bank still
  shows its input voltage.

The Max boards do the same thing for each port separately, using the eFuses.

[^banks]: K8-Pro: all revisions. K16-Pro and K32-Pro: v4.1 and later.

!!! warning "Ports power up on"
    On every board, the ports and banks come up **switched on** as soon as power is applied,
    before FPP has started. FPP then takes over and switches off ports and banks that are
    unused or idle. Treat every port as live whenever its bank's supply is on.
