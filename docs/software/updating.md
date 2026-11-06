# Updating

There are three things to keep current. FPP handles all of them from its web UI.

| What | How | FPP manual |
|---|---|---|
| **FPP** (the player) | *Help → About → Update* (same major version, e.g. 10.0 → 10.1) | [Update FPP](https://manual.falconplayer.com/064-help-troubleshooting/#update-fpp-software) |
| **Operating system** | *Help → About → Upgrade OS* (needed for major versions, e.g. 9.x → 10.x) | [Upgrade OS](https://manual.falconplayer.com/064-help-troubleshooting/#upgrade-operating-system) |
| **Cape EEPROM** | *Help → About → Cape Info* offers an update when a newer cape definition is available | [Cape info](https://manual.falconplayer.com/064-help-troubleshooting/#cape-info) |

- Back up first (*Status/Control → FPP Backup*).
- Keep the controller powered during an update. A power cut during an OS upgrade may mean
  re-imaging the SD card, or [re-flashing the eMMC](../hardware/pocketbeagle2.md#re-flashing-the-emmc).
- **PB2 Industrial:** FPP and OS updates work in place on the eMMC, the same as on an SD card.
  Updating this way is the recommended approach, because then you never need an SD card at all.
- **Don't update in the middle of your show season** unless a fix you need is in the update.

## Starting over

- **Reset settings:** *Main Menu → Reset* on the OLED, or
  [Reset FPP Config](https://manual.falconplayer.com/020-fpp-settings/#the-reset-fpp-config-dialog) in
  the web UI. You can reset everything, or only networking, outputs, playlists and so on.
- **Re-image:** write a fresh FPP image to the SD card. See
  [Getting the FPP software](https://manual.falconplayer.com/006-quickstart/#getting-the-fpp-software).
  The cape configures itself again on the next boot. On a PB2 Industrial, re-flash the eMMC
  instead. See [Re-flashing the eMMC](../hardware/pocketbeagle2.md#re-flashing-the-emmc).
