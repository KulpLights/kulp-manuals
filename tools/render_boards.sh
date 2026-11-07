#!/bin/zsh
# Render the top view of each board from the KiCad files into docs/assets/boards/<Name>-top.webp.
# Usage: tools/render_boards.sh <path-to-bbb-capes> [Name ...]   (no names = all boards)
# Needs KiCad 10 and Pillow in .venv. The 3D models resolve through ${KICAD10_3DMODEL_DIR} and
# ${KIPRJMOD}/../components.3d, so no extra KiCad path variables are needed.
K=${KICAD_CLI:-/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli}
T=${0:A:h}
PY=${PYTHON:-$T/../.venv/bin/python}
B=$1; shift
OUT=$T/../docs/assets/boards
TMP=$(mktemp -d)
# Name:project/file. The BeagleBone/PocketBeagle/Pi models leave a semi-transparent ghost in the
# render, so the trim drops every pixel with alpha < 200.
BOARDS=(
  K8-Pro:K8-Pro/K8-Pro K8-Max:K8-Max/K8-Max K8-PB:K8PB/K8PB K4-PB:K4PB/K4PB
  K40D-PB:K40DPB/K40DPB K16:K16/K16 K16-Pro:K16-Pro/K16-Pro K16-Max:K16-Max/K16-Max
  K32:K32/K32 K32-Pro:K32-Pro/K32-Pro K32-Max:K32-Max/K32-Max
  PocketScrollerV2:PocketScroller/PocketScroller PocketScrollerV3:PocketScrollerV3/PocketScroller
  PocketScroller-16:PocketScrollerV3-16/PocketScrollerV3-16
  K8-B:K8B/K8B K8-B-Scroller:K8Scroller/K8Scroller OctoPlus:Octo2/Octo2
  K64D-B:K64D-B/K64D-B K128D-B:K128D-B/K128D-B K16A-B:K16B/K16B K32A-B:K32B/K32B
  K8-Pi:K8-Pi/K8-Pi K2-Pi-Servo:K2-Pi-Servo/K2-Pi-Servo K2-Pi0:K2-Pi0/K2-Pi0
  BBB-OLED:BBB-OLED/BBB-OLED Pi-OLED:Pi-OLED/Pi-OLED PiOLED-Audio:PiOLED-Audio/PiOLED-Audio
)
for e in $BOARDS; do
  n=${e%%:*}; p=${e#*:}
  (( $# )) && (( ! ${@[(Ie)$n]} )) && continue
  "$K" pcb render -o "$TMP/$n-top.png" -w 2400 -h 1800 --zoom 0.85 --side top --quality high \
    --background transparent "$B/$p.kicad_pcb" >/dev/null || { echo "render failed: $n"; continue; }
  "$PY" $T/trim_renders.py --ghost "$TMP/$n-top.png" "$OUT/$n-top.webp"
done
rm -rf "$TMP"
