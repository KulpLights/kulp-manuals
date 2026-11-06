# Current monitoring & eFuses

FPP has a **Port Status** page (*Status/Control → Port Status*) that shows, for each port:

- whether the port is **on**, **off**, or **tripped**
- the **current** it is drawing, in mA, if the port can measure it
- warnings when an eFuse trips or a pixel count looks wrong

Where the readings come from depends on the board:

| Board | Local ports | Differential ports |
|---|---|---|
| **Max** (K8-Max, K16-Max, K32-Max) | current, on/off and eFuse status for every port | from Falcon V5 receivers |
| **K8-PB** | current, on/off and eFuse status for every port | none (send-only) |
| **K4-PB** | current, on/off and eFuse status for every port | — (no differential ports) |
| **K40D-PB** | — (no local ports) | none (send-only) |
| **Pro** (K8-Pro, K16-Pro, K32-Pro) | none (fused ports) | from Falcon V5 receivers |
| K16, K32 | none | none (send-only) |

On Pro boards with no Falcon V5 receivers attached, the Port Status page says no monitoring
is available. That's expected.

See [Port Status](https://manual.falconplayer.com/014-port-status/) in the FPP manual.

## Port icons

| Icon | Meaning | Click to |
|---|---|---|
| :material-check-circle:{ style="color: #2e7d32" } | Port enabled | turn the port off |
| :material-close-circle:{ style="color: #c62828" } | **eFuse tripped** | reset and turn it back on |
| :material-close-circle:{ style="color: #0288d1" } | Port turned off | turn it on |

## When an eFuse trips

1. FPP turns the port off, shows a warning banner, and marks it with a red icon.
2. **Find the cause**: a short in a pigtail or connector, water ingress, a damaged string, or
   a string drawing more than about 6 A (about 5.2 A on the K8-PB and K4-PB).
3. Click the red icon to reset the port. Power-cycling the controller also resets every port.

If the trip happens again straight away, the fault is still there.

### eFuse auto-retry

Under *Settings → Output*, two settings make FPP reset tripped eFuses by itself:

- **eFuse Retry Count**: how many times FPP retries before giving up (default **0** = off, up to 20).
- **eFuse Retry Time Interval**: how long to wait between retries (default 100 ms).

Retrying helps when a port trips only occasionally, such as from the inrush when a large string
powers up. **Don't use it to hide a real short.**

## Checking pixel counts

On boards with current readings, the **Count Pixels** button on Port Status estimates how many
pixels are on each port from the current they draw, and flags ports that don't match the
configured count. It's a quick way to find a dead section partway down a string.

## Automatic power control

Ports and banks power up **on**. Once FPP is running it takes control. With *Settings → Output →
Automatically turn on/off outputs* turned on (the default), FPP powers ports or banks only while
there is data to send, and **switches off ports with no pixels configured**. So on a Max board, a
port that isn't set up in *Pixel Strings* (or by xLights) is live only for the moment between
power-up and FPP starting. That's deliberate.

## Notifications

When an eFuse trips, FPP runs the **`EFUSE_TRIGGERED`** command preset, if you've created one,
with the port name available as `%PORT%`. Use it to send yourself a notification (for example
through an MQTT or URL command). [FPPMon](https://kulplights.com/product-category/accessories/)
can also alert you to trips while you're away.
