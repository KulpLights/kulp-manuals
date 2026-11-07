"""Crop a transparent KiCad render to the board and save it as WebP.
usage: trim_renders.py [--ghost] in.png out.webp
--ghost drops pixels with alpha < 200 first (the semi-transparent ghost a BeagleBone or
PocketBeagle model leaves in the render)."""
import sys
from PIL import Image

src, out = [a for a in sys.argv[1:] if a != '--ghost']
im = Image.open(src).convert('RGBA')
if '--ghost' in sys.argv:
    im.putalpha(im.getchannel('A').point(lambda v: 255 if v >= 200 else 0))
bb = im.getchannel('A').point(lambda a: 255 if a > 8 else 0).getbbox()
im = im.crop((max(bb[0]-20, 0), max(bb[1]-20, 0), min(bb[2]+20, im.width), min(bb[3]+20, im.height)))
im.thumbnail((1800, 1800))
im.save(out, 'WEBP', quality=88)
print(out, im.size)
