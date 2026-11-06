import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'docs', 'boards')

COMMON_K8 = dict(size=(103.05, 129.39), holes=6)
COMMON_K16 = dict(size=(168.55, 139.21), holes=8)
COMMON_K32 = dict(size=(168.55, 202.75), holes=11)

def yn(b): return 'yes' if b else '—'

boards = [
 dict(slug='k8-pro', name='K8-Pro', img='K8-Pro', silk='K8-Pro v4.1.0', fam='k8', **COMMON_K8,
      tagline='8 fused pixel ports, 4 two-way differential ports, audio and DMX.',
      local=8, prot='5 A mini-blade fuse per port', switching='per bank of 4 (FPP-controlled)',
      monitor='from Falcon V5 receivers only', diff=['9-12','13-16','17-20','21-24'], diffdir='two-way (pair 1/2)',
      dmx='1 (`DMX`)', audio=True, usb=3, fan=True, exp=True),
 dict(slug='k8-max', name='K8-Max', img='K8-Max', silk='K8-Max v4.1.0', fam='k8', **COMMON_K8,
      tagline='8 eFused pixel ports with per-port current monitoring, 4 two-way differential ports, audio and DMX.',
      local=8, prot='eFuse per port, about 6 A, latching', switching='per port (FPP-controlled)',
      monitor='every local port, plus Falcon V5 receivers', diff=['9-12','13-16','17-20','21-24'], diffdir='two-way (pair 1/2)',
      dmx='1 (`DMX`)', audio=True, usb=3, fan=True, exp=True),
 dict(slug='k16', name='K16', img='K16', silk='K16 v4.1.0', fam='k16', **COMMON_K16,
      tagline='16 fused pixel ports, 4 differential ports and DMX.',
      local=16, prot='5 A mini-blade fuse per port', switching='—',
      monitor='—', diff=['17-20','21-24','25-28','29-32'], diffdir='send-only',
      dmx='1 (`DMX`)', audio=False, usb=1, fan=False, exp=False),
 dict(slug='k16-pro', name='K16-Pro', img='K16-Pro', silk='K16-Pro v4.1.1', fam='k16', **COMMON_K16,
      tagline='16 fused pixel ports with bank switching, 8 two-way differential ports, audio and 2 DMX.',
      local=16, prot='5 A mini-blade fuse per port', switching='per bank of 4, FPP-controlled (v4.1 and later)',
      monitor='from Falcon V5 receivers only', diff=['17-20','21-24','25-28','29-32','33-36','37-40','41-44','45-48'], diffdir='two-way (pair 1/2)',
      dmx='2 (`DMX1`, `DMX2`)', audio=True, usb=3, fan=True, exp=True),
 dict(slug='k16-max', name='K16-Max', img='K16-Max', silk='K16-Max v4.1.0', fam='k16', **COMMON_K16,
      tagline='16 eFused pixel ports with per-port current monitoring, 8 two-way differential ports, audio and 2 DMX.',
      local=16, prot='eFuse per port, about 6 A, latching', switching='per port (FPP-controlled)',
      monitor='every local port, plus Falcon V5 receivers', diff=['17-20','21-24','25-28','29-32','33-36','37-40','41-44','45-48'], diffdir='two-way (pair 1/2)',
      dmx='2 (`DMX1`, `DMX2`)', audio=True, usb=3, fan=True, exp=True),
 dict(slug='k32', name='K32', img='K32', silk='K32 v4.1.0', fam='k32', **COMMON_K32,
      tagline='32 fused pixel ports, 4 differential ports and DMX.',
      local=32, prot='5 A mini-blade fuse per port', switching='—',
      monitor='—', diff=['33-36','37-40','41-44','45-48'], diffdir='send-only',
      dmx='1 (`DMX`)', audio=False, usb=1, fan=False, exp=False),
 dict(slug='k32-pro', name='K32-Pro', img='K32-Pro', silk='K32-Pro v4.1.0', fam='k32', **COMMON_K32,
      tagline='32 fused pixel ports, 8 two-way differential ports, audio and 2 DMX.',
      local=32, prot='5 A mini-blade fuse per port', switching='per bank of 4, FPP-controlled (v4.1 and later)',
      monitor='from Falcon V5 receivers only', diff=['33-36','37-40','41-44','45-48','49-52','53-56','57-60','61-64'], diffdir='two-way (pair 1/2)',
      dmx='2 (`DMX1`, `DMX2`)', audio=True, usb=3, fan=True, exp=True),
 dict(slug='k32-max', name='K32-Max', img='K32-Max', silk='K32-Max v4.2.0', fam='k32', **COMMON_K32,
      tagline='32 eFused pixel ports with per-port current monitoring, 8 two-way differential ports, audio and 2 DMX.',
      local=32, prot='eFuse per port, about 6 A, latching', switching='per port (FPP-controlled)',
      monitor='every local port, plus Falcon V5 receivers', diff=['33-36','37-40','41-44','45-48','49-52','53-56','57-60','61-64'], diffdir='two-way (pair 1/2)',
      dmx='2 (`DMX1`, `DMX2`)', audio=True, usb=3, fan=True, exp=True),
]

POWER = {
 'k8': """| Terminal | Feeds | FPP reading | Also powers the controller? |
|---|---|---|---|
| **Left** (bottom edge) | P1–P4 | VIN1 | no |
| **Right** (bottom edge) | P5–P8 | VIN2 | **yes** |

The blue LED beside the **right** terminal lights when it has power. **The right terminal must
be powered for the controller to boot.**""",
 'k16': """| Terminal | Position | Feeds | FPP reading | Also powers the controller? |
|---|---|---|---|---|
| **V1** | left side, upper | P1–P4 | VIN1 | **yes** |
| **V2** | left side, lower | P5–P8 | VIN2 | no |
| **V3** | right side, upper | P9–P12 | VIN3 | no |
| **V4** | right side, lower | P13–P16 | VIN4 | no |

The blue LED beside **V1** lights when it has power. **V1 must be powered for the controller to boot.**""",
 'k32': """The four terminals down the **left** edge feed the left half of the board, and the
four down the **right** edge feed the right half. FPP's VIN numbers don't follow
reading order:

| Terminal | Position | Feeds | FPP reading | Also powers the controller? |
|---|---|---|---|---|
| **V1** | left, row 1 (top) | P1–P4 | VIN1 | **yes** |
| **V2** | left, row 2 | P5–P8 | VIN2 | no |
| **V5** | left, row 3 | P9–P12 | VIN5 | no |
| **V6** | left, row 4 | P13–P16 | VIN6 | no |
| **V3** | right, row 1 (top) | P17–P20 | VIN3 | no |
| **V4** | right, row 2 | P21–P24 | VIN4 | no |
| **V7** | right, row 3 | P25–P28 | VIN7 | no |
| **V8** | right, row 4 | P29–P32 | VIN8 | no |

The blue LED beside **V1** lights when it has power. **V1 must be powered for the controller to boot.**""",
}

# Mounting drawings and 3D-printable mounts from the kulplights.com product pages.
# Each family shares one set.
MOUNT = {
    'k8':  dict(pdf='https://kulplights.com/wp-content/uploads/2025/12/K8-Max.pdf'),
    'k16': dict(pdf='https://kulplights.com/wp-content/uploads/2025/08/K16.pdf',
                thing='https://www.thingiverse.com/thing:7181496'),
    'k32': dict(pdf='https://kulplights.com/wp-content/uploads/2025/05/K32-Max.pdf',
                svg='https://kulplights.com/wp-content/uploads/2025/05/K32-Max.svg',
                thing='https://www.thingiverse.com/thing:7065715'),
}
FAMNAME = {'k8': 'K8-Pro and K8-Max', 'k16': 'K16, K16-Pro and K16-Max', 'k32': 'K32, K32-Pro and K32-Max'}


def mount_links(b):
    m = MOUNT[b['fam']]
    files = f"[PDF]({m['pdf']})" + (f" · [SVG]({m['svg']})" if 'svg' in m else '')
    out = f"- Mounting drawing: {files}. It is shared by the {FAMNAME[b['fam']]}, which have the same outline and holes.\n"
    if 'thing' in m:
        out += f"- A 3D-printable mount is on [Thingiverse]({m['thing']}).\n"
    return out


LAYOUT = {
 'k8': """The eight pixel ports are in two rows across the lower part of the board:

| | | | | |
|---|---|---|---|---|
| **Top row** | P1 | P3 | P5 | P7 |
| **Bottom row** | P2 | P4 | P6 | P8 |""",
 'k16': """The sixteen pixel ports are in two rows, eight on each side of the board's centre line:

| | Left half | Right half |
|---|---|---|
| **Top row** | P1 P2 P3 P4 | P9 P10 P11 P12 |
| **Bottom row** | P5 P6 P7 P8 | P13 P14 P15 P16 |""",
 'k32': """The 32 pixel ports are in four rows of eight, four ports on each side:

| | Left half | Right half |
|---|---|---|
| **Row 1** | P1–P4 | P17–P20 |
| **Row 2** | P5–P8 | P21–P24 |
| **Row 3** | P9–P12 | P25–P28 |
| **Row 4** | P13–P16 | P29–P32 |""",
}

def page(b):
    mm = b['size']; inch = (mm[0]/25.4, mm[1]/25.4)
    maxb = 'Max' in b['name']; pro = 'Pro' in b['name']
    first_diff = b['local'] + 1; last_diff = b['local'] + 4*len(b['diff'])
    fuse_note = ''
    if maxb:
        fuse_note = """### eFuses and current monitoring

Every local port has its own eFuse (about **6 A**), and FPP reads every port's current.
FPP turns each port on and off as needed. A tripped port shows a red icon on
**Status/Control → Port Status**; click it to reset the port once the fault is fixed.
See [Power → eFuses](../hardware/power.md#efuses-max-boards) and
[Current monitoring](../software/current-monitoring.md)."""
    else:
        fuse_note = """### Fuses

Every local port has a **5 A mini-blade fuse** next to it. If a port's green LED is dark while
the rest of its bank is lit, check that port's fuse first. **Never fit a fuse larger
than 5 A.** See [Power → Fuses](../hardware/power.md#mini-blade-fuses-k16-k32-and-the-pro-boards)."""
        if b['slug'] == 'k8-pro':
            fuse_note += "\n\nOn the K8-Pro all eight fuses sit in one row along the bottom edge, between the two power terminals."
    if pro:
        fuse_note += """

### Bank switching

Each bank of four ports has an electronic power switch that FPP controls, so FPP can turn
pixel power off when nothing is playing. See [Power → Bank switching](../hardware/power.md#bank-switching-pro-boards)."""
        if b['slug'] != 'k8-pro':
            fuse_note += """

Bank switching was added in **v4.1**. On a v4.0 board every bank is on whenever it has
power. See [Board revisions](#board-revisions)."""
    diff_ex = b['diff'][-1]
    rev_intro = ''
    revs = ''
    if b['fan']:
        rev_intro = ' Differences in earlier revisions are listed under [Board revisions](#board-revisions).'
        if b['slug'] in ('k16-pro', 'k32-pro'):
            rows = '''| **v4.0** | Fused ports; banks are always on when powered. Fan speed control. |
| **v4.1** | Adds **bank switching** (FPP turns each bank of 4 on and off) and **fan speed monitoring**. |'''
        elif b['slug'] == 'k8-pro':
            rows = '''| **v4.0** | Fused ports with bank switching. Fan speed control. |
| **v4.1** | Adds **fan speed monitoring**. |'''
        else:
            rows = '''| **v4.0** | eFused ports with current monitoring. Fan speed control. |
| **v4.1** | Adds **fan speed monitoring**. |'''
        revs = f'''## Board revisions

The revision is printed on the board next to the model name. FPP also shows it as the
**Hardware Version** under *Help → About → Cape Info*.

| Revision | Changes |
|---|---|
{rows}

'''
    silk_note = ''
    if b['slug'] in ('k32-pro','k32-max'):
        silk_note = "\n\n!!! note\n    The last differential jack is printed **60-64** on the board. It carries strings **61–64**."
    feats = []
    feats.append(f"| Local pixel ports | {b['local']} (P1–P{b['local']}), 3-pin 3.5 mm pluggable, plugs included |")
    feats.append(f"| Port protection | {b['prot']} |")
    feats.append(f"| Power switching | {b['switching']} |")
    feats.append(f"| Current monitoring | {b['monitor']} |")
    feats.append(f"| Differential ports | {len(b['diff'])} × RJ45 = {4*len(b['diff'])} strings ({first_diff}–{last_diff}), {b['diffdir']} |")
    feats.append(f"| Total strings | {b['local'] + 4*len(b['diff'])} |")
    feats.append(f"| Power inputs | {b['local']//4} terminals rated 30 A, 5–24 V DC, one bank of 4 ports each |")
    feats.append(f"| DMX / serial | {b['dmx']}, RS-485 transmit |")
    feats.append(f"| Audio | {'PCM5102A DAC, 3.5 mm line out, FM transmitter socket' if b['audio'] else 'none (use a USB sound card)'} |")
    feats.append(f"| Ethernet | 1 × Gigabit (USB-attached) |")
    feats.append(f"| USB-A | {b['usb']}{' (via the included extension cable)' if b['usb']==1 else ''} |")
    feats.append(f"| Display & buttons | 128×64 OLED, Up / Down / Enter / Back / Test |")
    feats.append(f"| Real-time clock | yes, CR1220 backup cell |")
    feats.append(f"| Fan header | {'5 V 4-pin PWM, temperature-controlled; speed monitoring on v4.1 and later' if b['fan'] else '—'} |")
    feats.append(f"| Expansion header | {'2×6: I²C + 8 GPIO (Exp.1–Exp.8)' if b['exp'] else '—'} |")
    feats.append(f"| Size | {mm[0]:.1f} × {mm[1]:.1f} mm ({inch[0]:.2f} × {inch[1]:.2f} in), {b['holes']} mounting holes, 3.0 mm |")
    feats.append(f"| Requires | PocketBeagle 2 (not PocketBeagle 1), FPP 9.0 or later |")
    feat = "\n".join(feats)
    diffrow = " · ".join(f"`{d}`" for d in b['diff'])
    return f"""# {b['name']}

{b['tagline']}

![{b['name']}](../assets/boards/{b['img']}-photo.webp){{ .board loading=lazy }}

<small>{b['name']}{' with a PocketBeagle 2 fitted' if b['slug'] != 'k32' else ', shown without a PocketBeagle 2'}. Photos may show an earlier board revision.</small>

This page describes revision **{b['silk'].split()[-1]}** (printed on the board as `{b['silk']}`).{rev_intro}

## Specifications

| | {b['name']} |
|---|---|
{feat}

## Board map

![{b['name']} from above](../assets/boards/{b['img']}-top.webp){{ .board loading=lazy }}

### Power terminals

{POWER[b['fam']]}

See [Power](../hardware/power.md) for supply sizing, wire size and safety.

### Pixel ports

{LAYOUT[b['fam']]}

Each port is **G D V** (ground, data, +V), as printed beside it. See [Pixel outputs](../hardware/pixel-outputs.md).

{fuse_note}

### Differential ports

{diffrow}

Each jack carries four strings, numbered as printed above it. They are {'**two-way**: Falcon V5 smart receivers report their eFuse status and current back over pair 1/2. Other receivers work as send-only' if 'two' in b['diffdir'] else '**send-only**. Any standard receiver works, but receivers cannot report back'}.
See [Differential ports](../hardware/differential.md).{silk_note}

### Other connectors

| Connector | Marking | Details |
|---|---|---|
| Ethernet | (RJ45 with LEDs) | [Network](../hardware/network-usb-rtc.md#ethernet) |
| DMX | {b['dmx'].split('(')[1].rstrip(')')} | [DMX / serial](../hardware/dmx.md) |
| USB-A | — | {b['usb']} port{'s' if b['usb']>1 else ' (use the included USB extension cable)'}, [USB](../hardware/network-usb-rtc.md#usb-ports) |
| OLED | `GND 3.3V SCL SDA` | [Controls & display](../hardware/controls.md) |
""" + ("""| Audio out | 3.5 mm jack | [Audio](../hardware/audio.md) |
| FM transmitter | `RST SCL SDA 3.3V G L R` | [Audio](../hardware/audio.md#fm-transmitter-socket) |
""" if b['audio'] else "") + ("""| Fan | `Fan 5V` | [Fan](../hardware/expansion.md#fan) |
""" if b['fan'] else "") + ("""| Expansion | `Exp` | [Expansion header](../hardware/expansion.md) |
""" if b['exp'] else "") + f"""| RTC battery | coin-cell holder{' (underside)' if b['fam']=='k8' else ''} | [Clock](../hardware/network-usb-rtc.md#real-time-clock-rtc) |

## FPP setup

When FPP detects the {b['name']} it sets itself up automatically. It enables the
**{b['name']}** pixel-string layout, the sensors (input voltages{', port currents' if maxb else ''}, temperature){', the audio output' if b['audio'] else ''}
and a disabled DMX output. Out of the box each local port is set to 50 WS2811 pixels at 50 % brightness.
Set the real counts and start channels from xLights or the FPP *Pixel Strings* page.
See [Configuring outputs](../software/outputs.md).

{revs}## Dimensions & mounting

- **{mm[0]:.2f} × {mm[1]:.2f} mm** ({inch[0]:.2f} × {inch[1]:.2f} in), {b['holes']} plated mounting holes, 3.0 mm, for **M2.5** (or #4) screws and standoffs.
- The mounting holes are connected to ground.
- Use nylon or metal standoffs at least 6 mm (¼ in) tall, so nothing on the underside touches the
  enclosure.
{mount_links(b)}"""

for b in boards:
    open(os.path.join(OUT, b['slug'] + '.md'), 'w').write(page(b))
    print('wrote', b['slug'])
