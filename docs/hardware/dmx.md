# DMX / serial outputs

The RJ45 jacks labelled **DMX** (or **DMX1** / **DMX2**) are **RS-485 serial outputs**.
FPP can drive them as:

- **DMX512** (DMX-Open), for floods, moving heads and DMX relay boxes
- **Pixelnet**
- **Renard** and **LOR** (Light-O-Rama) networks

| Board | Serial outputs | FPP name | PocketBeagle pin |
|---|---|---|---|
| K8-Pro, K8-Max, K16, K32 | 1 | `DMX` | P2-07 |
| K16-Pro, K16-Max, K32-Pro, K32-Max | 2 | `DMX1`, `DMX2` | P2-07, P1-08 |
| PocketScroller v3, PocketScroller-16 | none | — | — |

## Pinout

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
