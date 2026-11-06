# Controls & display

Every board has a small **OLED display** and five buttons: **Up**, **Down**, **Enter**,
**Back** and **Test**. From them you can check status, read the IP address, change modes
and run test patterns without a computer.

## The OLED

Every board comes with the OLED fitted. It is a 128×64 I²C display that plugs into a 4-pin socket marked
`GND 3.3V SCL SDA`. FPP sets it up automatically. If the display is ever blank, check
**Status Display** under *Settings → System* in FPP. See the
[FPP manual](https://manual.falconplayer.com/020-fpp-settings/#settingsSystem).

- After a while without a button press, the display turns itself off. Any button wakes it.
- If you mount the controller upside down, choose a *flipped* display type in the same
  setting.

### Status pages

The display normally shows the **status page**: hostname, IP address(es), FPP mode and
what is playing. When the board has sensors, press **Enter** to step through:

1. **Status**: network addresses, mode, playlist and sequence
2. **Sensors**: input voltages (VIN1, VIN2, …), temperature, and on Max boards the
   current per port. Use **Up**/**Down** to scroll.
3. Pressing **Enter** again opens the **Main Menu**.

### Main Menu

| Item | What it does |
|---|---|
| **FPP Mode** | Switch between *Player* and *Remote* mode |
| **Tethering** | Turn FPP's Wi-Fi hotspot to *Automatic*, *On* or *Off* (needs a USB Wi-Fi adapter) |
| **Testing** | Pick a test pattern (white, red, green, blue, cycles, chases) and optionally run it across MultiSync |
| **Reboot** / **Shutdown** | Restart or shut down the PocketBeagle cleanly |
| **Reset** | Factory-reset all FPP settings, or just a part of them (network, outputs, playlists…) |
| **About** | FPP version, cape and serial number |
| **Back** | Return to the status page |

Use **Up**/**Down** to move, **Enter** to choose and **Back** to go back.

!!! tip "Shut down before unplugging"
    Use **Main Menu → Shutdown** (or the FPP web UI) before you remove power. Pulling the
    power while FPP is writing can corrupt the SD card.

## Test button

Pressing **Test** on the status page starts a **test pattern on every output** and steps
through the patterns:

*Off → R-G-B Cycle → R-G-B-W-N Cycle → R-G-B Chase → R-G-B-W-N Chase → Off*

While a test is running, **Up** slows it down and **Down** speeds it up. Press **Test**
until the display shows *Off* to stop.

The test drives every configured port, including the differential ports. It's the
quickest way to check wiring before you build a sequence. On boards with switched
ports (Pro/Max), FPP powers the ports for the test.

!!! note
    The test uses the pixel counts set in FPP's *Pixel Strings* page. A fresh board is set
    to 50 pixels per local port, so on a longer string only the first 50 light up until
    you set the real count.

## Status LEDs

| LED | Colour | Meaning |
|---|---|---|
| Next to the logic power terminal | blue | That terminal has power |
| Near the power section | blue | The controller's internal 5 V supply is on |
| One per local pixel port | green | The port has power. See [Pixel outputs](pixel-outputs.md#port-leds). |
| Ethernet jack | left / right | Link (left) and activity (right). See [Network](network-usb-rtc.md). |
| On the PocketBeagle 2 | various | Boot and activity (see [PocketBeagle 2](pocketbeagle2.md)) |

The PocketScrollers have no power LEDs; check the OLED and the Ethernet LEDs instead.
