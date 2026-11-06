# DMX / serial outputs

The RJ45 jacks labelled **DMX** (or **DMX1** / **DMX2**) are **RS-485 serial outputs**.
FPP can drive them as:

- **DMX512** (DMX-Open), for floods, moving heads and DMX relay boxes
- **Pixelnet**
- **Renard** and **LOR** (Light-O-Rama) networks

| Board | Serial outputs | FPP name | Pin |
|---|---|---|---|
| K8-Pro, K8-Max, K16, K32 | 1 | `DMX` | P2-07 |
| K16-Pro, K16-Max, K32-Pro, K32-Max | 2 | `DMX1`, `DMX2` | P2-07, P1-08 |
| K8-PB | 1, on a 3-pin header (FPP 10.3 or later) | `ttyS2` | P1-10 |
| K4-PB | 1, on a 3-pin header | `ttyS4` | P2-07 |
| K40D-PB | 1, on a 3-pin pluggable terminal | `ttyS4` | P2-07 |
| PocketScroller v2, v3 and -16 | none | — | — |
| K8-B, K8-B-Scroller | 2, on a 2×3 header | `ttyS1`, `ttyS2` | P9-24, P9-21 |
| K64D-B, K128D-B | 2, RJ45 with a DMX/LOR switch | `ttyS1`, `ttyS2` | P9-24, P9-21 |
| OctoPlus | none | — | — |
| K8-Pi | 1, on a 3-pin header | `ttyAMA0` | Pi GPIO14 (pin 8) |
| K2-Pi-Servo, K2-Pi0 | none | — | — |

## Pinout

These are the RJ45 jacks on the K8, K16 and K32 boards. The K8-PB, K4-PB and K40D-PB have a 3-pin header or
terminal instead, and the K8-B and K8-B-Scroller a 2×3 header; see their board pages
([K8-PB](../boards/k8-pb.md#dmx), [K4-PB](../boards/k4-pb.md#dmx), [K40D-PB](../boards/k40d-pb.md#dmx),
[K8-B](../boards/k8-b.md#dmx), [K8-B-Scroller](../boards/k8-b-scroller.md#dmx)). The K64D-B and
K128D-B jacks use this pinout with their switch set to **DMX**; set to **LOR**, they suit LOR networks
directly ([K64D-B](../boards/k64d-b.md#dmx-lor), [K128D-B](../boards/k128d-b.md#dmx-lor)).

The pinout follows the ESTA standard for DMX over RJ45 (ANSI E1.27-2):

| RJ45 pin | Signal | DMX XLR pin |
|---|---|---|
| 1 | Data + | 3 |
| 2 | Data − | 2 |
| 7, 8 | Ground | 1 |
| 3–6 | not connected | — |

To connect fixtures with XLR inputs, use an RJ45-to-XLR DMX adapter wired to this
standard.

!!! warning "LOR, Renard and Pixelnet need an adapter"
    The jack is wired for **standard DMX only**. To drive Light-O-Rama, Renard or Pixelnet
    devices, use an adapter cable that takes data + / − (pins 1 and 2) and ground (pins 7 and 8)
    to the pins that device expects. Don't connect them with a plain network cable.

## Notes

- These are **outputs only**. The controller doesn't receive DMX or RDM.
- A **120 Ω termination** resistor is fitted permanently at the controller. Put a
  terminator on the **last** fixture in the DMX chain.
- Set the outputs up in FPP under **Input/Output Setup → Channel Outputs → Other**. FPP
  installs a disabled DMX-Open output on each port. Enable it and set the start channel
  and channel count. See the
  [FPP manual](https://manual.falconplayer.com/054-channel-outputs/#additional-output-groups-add-output-group).
