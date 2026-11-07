# Troubleshooting

Start with the symptom closest to yours. For software problems (playlists, schedules,
sequences), FPP's [troubleshooting guide](https://manual.falconplayer.com/134-troubleshooting/)
goes further.

## Nothing happens at power-up

| Check | Why |
|---|---|
| Is the **logic power terminal** powered? | Only one terminal runs the controller: the **upper-left** one on the K16 and K32, the **right-hand** one on the K8. The other boards have one terminal. See [Power](hardware/power.md#banks). |
| Is the blue LED beside that terminal lit? | If not, there's no voltage at the terminal. Check the supply, the wiring and the polarity. |
| Is the polarity right? | Reversed power is blocked, not damaging, but the board stays off. Swap the wires. |
| Is the second blue LED (5 V) lit? | If the terminal LED is on but this one is off, contact support. |
| PocketScroller (v3 or -16): is the supply **5 V**? | A higher voltage trips its input fuse. Disconnect it, wait a minute, and reconnect with 5 V. |

## Power LEDs on, but the OLED stays blank

- Give it two minutes. The first boot of a new SD card takes longer.
- Re-seat the **SD card**, and try another card or a freshly written image. A worn-out SD card is the
  most common cause.
- Check the **PocketBeagle 2** is seated fully and the right way round
  ([PocketBeagle 2](hardware/pocketbeagle2.md#fitting-the-pocketbeagle-2)), or that the
  **BeagleBone** is fully on its headers ([BeagleBone Black](hardware/beaglebone-black.md#fitting-the-beaglebone)).
- **BeagleBone Black boards:** an older BeagleBone (before about 2019) boots its own eMMC instead
  of the SD card. Hold its **Boot** button while you power up; see
  [Booting from the SD card](hardware/beaglebone-black.md#booting-from-the-sd-card).
- **Raspberry Pi boards:** check the hat is on all 40 header pins, not shifted by a row or column
  ([Raspberry Pi](hardware/raspberry-pi.md#fitting-the-hat)).
- **BeagleBone Black boards:** if FPP was shut down, the BeagleBone stays off until you press the
  cape's **Power** button or switch the supply off and on.
- If FPP is reachable on the network but the OLED is dark, check *Settings → System → Status Display*.

## Can't find the controller on the network

- Read the IP address from the OLED status page. Make sure your computer is on the same network.
- Check the Ethernet jack's LEDs. No link light means a cable or switch problem.
- Make sure the cable is in the **Ethernet** jack (the one with LEDs), not a differential or DMX port.
- No Ethernet? Plug in a USB Wi-Fi adapter and use the [hotspot](software/first-boot.md#no-ethernet-use-the-wi-fi-hotspot).
- FPP's [network troubleshooting](https://manual.falconplayer.com/064-help-troubleshooting/#general-troubleshooting-tips)
  covers subnets, static IPs and multiple interfaces.

## FPP doesn't recognise the board

If *Pixel Strings* shows no board, or *Cape Info* is empty:

- Update FPP to the latest release. Older FPP versions don't know the newest boards.
- Re-seat the PocketBeagle 2 or BeagleBone. The board ID is read over the header pins.
- Make sure the PocketBeagle 2 boards have a **PocketBeagle 2**, not a PocketBeagle 1, and the
  BeagleBone boards a [compatible BeagleBone](hardware/beaglebone-black.md#which-beaglebones-work).

## No pixels light

Work from the controller outwards:

1. **Port LED.** Is the green LED next to the port lit?
    - *Off, and the rest of the bank too:* the bank has no power, or is switched off (Pro/Max) because
      nothing is playing. Run a test (step 2) and check again.
    - *Off, just this port:* blown fuse, or tripped/disabled eFuse (Max). See
      [Port Status](software/current-monitoring.md).
2. **Test pattern.** Press **Test** on the controller. If the string lights, the hardware is fine and
   the problem is in the configuration: pixel count, start channel, or the sequence.
3. **Wiring.** Check **G D V** order against the pigtail, and that the data wire goes to the string's
   **input** end (look for the arrows on the pixels).
4. **Voltage.** Is the bank voltage right for the pixels? 12 V pixels on a 5 V bank stay dark or flicker.
5. **Protocol and count.** In *Pixel Strings*, check the protocol (WS2811 for most pixels) and that the
   pixel count is more than 0.

## Only part of a string lights, or colours are wrong

- **Colours wrong:** set the correct **colour order** (RGB, GRB, …) for that port.
- **Stops partway:** usually a failed pixel. The first dark pixel, or the last working one before it,
  is usually the bad one. On Max boards, *Count Pixels* on Port Status helps find it.
- **Ends dim or turn orange/pink:** voltage drop. Inject power at the far end, from the **same supply**
  (see the [power injection warning](hardware/power.md#efuses-max-boards)).

## Flicker or random colours

- Check that all supplies share a common **ground** with the controller.
- Make sure only **one** source is sending data. Turn off any E1.31/DDP output in xLights while
  FPP is playing.
- Long first run of bare data wire: add a null pixel, or move the string to a differential receiver.
- Turn the brightness down to check whether it's a power problem.

## A fuse keeps blowing / an eFuse keeps tripping

There is a real fault on that port. Unplug the string and see whether the port stays up. Then check
the pigtail, the connectors and the string for shorts or water. On Max boards, look at the current on
Port Status just before the trip. A string drawing close to 6 A on its own is simply too long for one
port: split it or inject power.

## A differential receiver is dark

- Is the receiver powered? The RJ45 carries **no power**.
- Press the receiver's **test** button. If it lights, the problem is the cable or the configuration.
- Swap to a known-good Cat5e/Cat6 cable. A bad crimp on one pair kills one string.
- In *Pixel Strings*, check the pixel counts for that port's four strings, and the receiver chain
  settings for smart receivers.

## Getting help

If you're stuck, email **support@kulplights.com** with:

- the board model and revision (printed on the board)
- the FPP version (*Help → About*)
- a description of the problem and what you've already tried
- photos of the wiring, if it's a wiring question
- an FPP **diagnostic report**: *Help → Troubleshooting*, or press **F8** in the FPP web UI
  ([how](https://manual.falconplayer.com/064-help-troubleshooting/#diagnostic-report))

The [FPP forums and Facebook groups](https://manual.falconplayer.com/122-help/) are also a good
place to ask about software.
