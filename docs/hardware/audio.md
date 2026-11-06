# Audio

| Board | Audio |
|---|---|
| K8-Pro, K8-Max, K16-Pro, K16-Max, K32-Pro, K32-Max | Built-in stereo DAC, 3.5 mm line out, FM transmitter socket |
| K64D-B, K128D-B | Built-in stereo DAC, 3.5 mm line out, FM transmitter socket |
| K16, K32, K8-PB, K4-PB, K40D-PB, PocketScroller v2, v3 and -16, K8-B, K8-B-Scroller, OctoPlus | None built in. Use a USB sound card. |
| K8-Pi, K2-Pi-Servo | The Pi 3 B+ or Pi 4's own audio jack (the Pi 5 has none), or a USB sound card. |
| K2-Pi0 | None (the Pi Zero has no audio output). Use a USB sound card on the Pi's USB port. |

## Line output

The built-in audio uses a **PCM5102A** 24-bit DAC on the board, so it has no USB jitter or ground
noise.

- **3.5 mm stereo jack** (tip = left, ring = right, sleeve = ground).
- **Line level** (about 2 V RMS at full volume). It's meant for an amplifier, powered
  speakers or an FM transmitter's line input. It is **not a headphone amplifier**, though
  headphones will work at low volume.
- FPP lists it as the **CapeAudio** sound card and selects it automatically. Volume
  is set in FPP's status page or with the volume commands.
  See the [FPP manual](https://manual.falconplayer.com/020-fpp-settings/#audio-video).

## FM transmitter socket

Boards with built-in audio also have an 11-pin socket marked
`RST SCL SDA 3.3V G L R` for the plug-in
[Si4713 FM transmitter](https://kulplights.com/product/fm-transmitter-si4713/). The module receives
the same audio as the line output, and FPP's FM transmitter plugin controls it over I²C.

| Pin | Signal |
|---|---|
| 1 | RST (module reset) |
| 3 | SCL |
| 4 | SDA |
| 7 | 3.3 V |
| 8 | GND |
| 10 | Left audio |
| 11 | Right audio |
| 2, 5, 6, 9 | not connected |

!!! warning
    Broadcasting on FM is regulated. Check the power and frequency rules where you live.


## USB sound cards

On boards without built-in audio, plug a USB sound card into a USB-A port and select it in
FPP under *Settings → Audio/Video*.
