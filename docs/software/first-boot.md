# First boot

FPP's own manual covers setup in detail. This page lists what's specific to these boards.

1. **Connect Ethernet.** First setup normally goes over the network. With no Ethernet, use a USB
   Wi-Fi adapter and FPP's hotspot (see below), or a USB cable to the PocketBeagle 2's USB-C port
   ([USB tethering](../hardware/network-usb-rtc.md#usb-tethering)). The K8-PB, K4-PB,
   K40D-PB and PocketScroller v2 have no Ethernet jack: use a USB Ethernet adapter, or a USB Wi-Fi adapter.
   The BeagleBone Black boards use the BeagleBone's Ethernet jack; don't use USB tethering on them
   while the cape is powered.
2. **Power up.** The OLED shows the IP address once the network is up.
3. **Browse to the IP address** (or `http://fpp.local`) and follow FPP's
   [initial configuration](https://manual.falconplayer.com/006-quickstart/#initial-configuration).

## Cape detection

Each board carries an ID chip (the *cape EEPROM*) that tells FPP which board it's on. On first
boot FPP:

- loads the right pin mapping, so the *Pixel Strings* page shows your board by name
- sets up the board's sensors (input voltages, temperature, and port currents on Max boards)
- selects the built-in audio and the RTC, if the board has them
- adds a disabled DMX output for each DMX port
- configures the OLED and buttons

You can see what FPP detected under *Help → About → Cape Info*. If the board isn't recognised, see
[Troubleshooting](../troubleshooting.md#fpp-doesnt-recognise-the-board).

## No Ethernet? Use the Wi-Fi hotspot

With a supported USB Wi-Fi adapter plugged in, FPP starts its own Wi-Fi network when it can't
find another network:

- Join the network named **FPP** (password **Christmas**) and browse to **192.168.8.1**.
- On the OLED, *Main Menu → Tethering* forces the hotspot on or off.

See [WiFi tethering](https://manual.falconplayer.com/016-network/#wifi-tethering).

## Set the time

The board has a battery-backed clock, but set the **time zone** (and NTP if you have internet)
under *Settings → Time* so schedules run at the right local time.
