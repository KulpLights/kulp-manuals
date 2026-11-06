#!/bin/zsh
# Render top and perspective views of each board from the KiCad files.
# Usage: tools/render_boards.sh <path-to-bbb-capes> <out-dir>
K=${KICAD_CLI:-/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli}
B=$1; O=$2; mkdir -p "$O"
for p in K8-Pro/K8-Pro K8-Max/K8-Max K8PB/K8PB K4PB/K4PB K40DPB/K40DPB K16/K16 K16-Pro/K16-Pro K16-Max/K16-Max K32/K32 K32-Pro/K32-Pro K32-Max/K32-Max PocketScroller/PocketScroller PocketScrollerV3/PocketScroller PocketScrollerV3-16/PocketScrollerV3-16; do
  n=${p%%/*}
  "$K" pcb render -o "$O/$n-top.png" -w 2400 -h 1800 --zoom 0.85 --side top --quality high --background transparent "$B/$p.kicad_pcb"
  "$K" pcb render -o "$O/$n-iso.png" -w 2400 -h 1800 --zoom 0.7 --side top --rotate '-35,0,25' --perspective --quality high --background transparent "$B/$p.kicad_pcb"
done
# K8PB, K4PB, K40DPB and PocketScroller render as <dir>-top.png: rename them K8-PB-top.webp,
# K4-PB-top.webp, K40D-PB-top.webp and PocketScrollerV2-top.webp after trimming. Their 3D models leave a
# semi-transparent ghost, so drop alpha < 200 before trimming.
# then: python3 tools/trim_renders.py "$O"/*.png  (needs Pillow), and copy the .webp files into docs/assets/boards/
