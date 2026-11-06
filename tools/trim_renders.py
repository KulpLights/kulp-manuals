import sys
from PIL import Image
for f in sys.argv[1:]:
    im = Image.open(f)
    bb = im.getchannel('A').point(lambda a: 255 if a > 8 else 0).getbbox()
    im = im.crop((max(bb[0]-20,0), max(bb[1]-20,0), min(bb[2]+20,im.width), min(bb[3]+20,im.height)))
    im.thumbnail((1800,1800))
    out = f.replace('.png','.webp')
    im.save(out, 'WEBP', quality=88)
    print(out, im.size)
