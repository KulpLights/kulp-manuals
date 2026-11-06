# Differential ports

The RJ45 jacks labelled with port ranges (`9-12`, `17-20`, `21-24`, …) are
**differential pixel ports**. Each carries **four pixel strings** as balanced
(RS-422-style) data over a standard network cable. At the far end, a
**differential receiver** turns the data back into four ordinary pixel outputs and powers
them from its own supply.

Differential data travels hundreds of feet. Use it to put pixel outputs where the
props are, instead of running long pixel leads from the controller.

!!! danger "These are not Ethernet ports"
    Do **not** plug the differential ports into a network switch, router or PC. The
    controller's one real Ethernet port is the **metal-shielded** jack with built-in LEDs. The
    differential jacks are all **black plastic**.

## Pinout

All differential ports on all boards use the same pinout. The four strings are called
A–D in the order of the label. On a jack labelled `17-20`, A is string 17 and D is string 20.

| RJ45 pin | Signal | Cable pair (T568B colours) |
|---|---|---|
| 1 | String A + | orange-white |
| 2 | String A − | orange |
| 3 | String B + | green-white |
| 6 | String B − | green |
| 5 | String C + | blue-white |
| 4 | String C − | blue |
| 7 | String D + | brown-white |
| 8 | String D − | brown |

There is **no ground and no power** on the cable; all eight wires are data.

## Receivers

Any receiver that uses the standard four-strings-per-RJ45 differential pinout above will
work. That includes the Kulp Lights receivers and Falcon-compatible receivers.

- [Smart Receiver SRx1](https://kulplights.com/product/smart-receiver-v2/): 4 strings.
- [Long-range SRx2](https://kulplights.com/product/lr-srx2/) and [SRx4](https://kulplights.com/product/lr-srx4/).

### Smart receivers and chaining

*Smart* receivers can be **chained**: up to six receivers on one differential port,
sharing that port's pixel allocation. Give each receiver in the chain its own position
on its selector dial, as described in the receiver's instructions, and turn termination on at
the last receiver only. Set the chain up in FPP on the port's row in the Pixel Strings table. See
the [FPP manual](https://manual.falconplayer.com/054-channel-outputs/#pixel-strings).

#### Pixel budget with smart receivers

FPP drives up to **800 pixels per port at 40 fps**. The smart-receiver protocol shares that time
with the pixels, so it lowers the budget. How much depends on which protocol the receivers use
(set per port in FPP):

| Protocol | Overhead | Does 800 px at 40 fps fit? |
|---|---|---|
| None (dumb receivers) | none | **Yes** |
| v1 | about 12 / 36 / 66 px for 1 / 2 / 3 receivers, every frame | With **1 receiver** only. 3 receivers leave about 757 px. |
| v2 | none for the first receiver, then about 3–4 px for each one after | **Yes**, up to the 6-receiver maximum (about 17 px for 6) |
| V4 | a config packet of about 25 px on 1 frame in 12 | Just: about **798 px** is the safe limit |
| V5 | a status query of up to about 96 px on most frames | **No.** Keep to about **725 px**, or run 800 px at about 36–37 fps |

The budget is **per port**. All the receivers in a chain share it: output 1 of receivers 1, 2
and 3 together get what's left on that port. An empty receiver position in the middle of a
v1/v2 chain also costs one pixel.

V5 costs the most because it is the protocol that **reports back** (see below): on most frames
the controller sends a query and then waits for the receiver to answer. If you don't need the
readings, V4 costs far less.

<!-- Figures computed from the FPP output code (PixelString.cpp, BBShiftString), not
measured on every receiver model. V5 worst-frame figure quoted rather than the average
(~750-775) because 768 px at 40 fps was the marginal case in earlier testing. -->

### Two-way ports (Pro and Max boards)

On the **K8-Pro, K8-Max, K16-Pro, K16-Max, K32-Pro and K32-Max** the differential ports
are **bi-directional**. Pair 1/2 also carries data back from the receiver. **Falcon V5 smart
receivers** use it to report their **eFuse status, current and other readings**, and FPP
shows them on the [Port Status](../software/current-monitoring.md) page next to the local
ports. **Only Falcon V5 receivers report back.** Every other receiver works as a normal,
send-only receiver on these ports.

On the **K16** and **K32** the differential ports are **send-only**. Every receiver
works, but none can report back.

## Cabling tips

- Use solid-core **Cat5e or Cat6** with factory-made or carefully crimped ends. A bad
  crimp on one pair kills one string and is hard to find.
- Outdoors, use outdoor-rated (UV/direct-burial) cable and keep the RJ45 ends dry.
- If a receiver has a terminator setting, turn termination on at the **last** receiver
  in a chain only.
- Each receiver has a **test button** and data LEDs. Use them to tell a cable problem
  from a configuration problem. See the receiver's documentation.
