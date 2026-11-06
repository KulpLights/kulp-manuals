# Configuring outputs

## From xLights (recommended)

1. In xLights' **Controllers** tab, add the controller as an **Ethernet** controller with protocol
   **FPP** (or let xLights discover it).
2. Set the **Vendor** to *Kulp Lights* and the **Model** to your board (for example *K16-Max*).
3. Map your props to ports in the **Visualiser**. Local ports come first (P1, P2, …), then the
   differential ports in the order printed on the board.
4. Click **Upload Outputs**. xLights writes the pixel counts, start channels, colour order and
   brightness to FPP.
5. Upload sequences with **FPP Connect**. See the
   [FPP manual](https://manual.falconplayer.com/128-fpp-connect/).

## In FPP

The same settings are under **Input/Output Setup → Channel Outputs → Pixel Strings**. FPP lists
the board by name, with one row per port, grouped by bank. See
[Pixel strings](https://manual.falconplayer.com/054-channel-outputs/#pixel-strings).

Differential ports appear as groups of four. For smart receivers, use the receiver
settings on each group's first row to set up a chain of receivers on that port.

!!! note "Defaults"
    A new board starts with **50 WS2811 pixels at 50 % brightness** on each local port, so the
    Test button works straight away. Upload your real configuration before the show.

## DMX

DMX outputs are under **Channel Outputs → Other**. See [DMX / serial](../hardware/dmx.md).

## LED panels (PocketScroller)

See [PocketScroller v3 → FPP setup](../boards/pocketscroller-v3.md#fpp-setup). The
[PocketScroller-16](../boards/pocketscroller-16.md#fpp-setup) works the same way, with 16 outputs.
