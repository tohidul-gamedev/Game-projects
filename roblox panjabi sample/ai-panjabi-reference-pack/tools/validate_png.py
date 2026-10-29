"""Read-only PNG checks. Requires Pillow; does not alter the supplied image."""
from pathlib import Path
from PIL import Image, ImageChops
import sys

pack = Path(__file__).resolve().parent.parent
if len(sys.argv) != 2:
    raise SystemExit('Usage: python tools/validate_png.py final.png')
path = Path(sys.argv[1])
im = Image.open(path)
data = path.read_bytes()
assert im.format == 'PNG', 'Wearable file must be a PNG'
assert im.size == (585,559), 'Wrong native canvas size'
assert im.mode == 'RGBA', 'PNG must have actual RGBA channels'
assert data[24] == 8, 'PNG channel depth must be8'
mask = Image.open(pack/'03-shirt-alpha-mask.png').convert('L')
assert ImageChops.difference(im.getchannel('A'), mask).getbbox() is None, 'Alpha differs from the approved neck/hand mask'
for point in [(10,10),(100,30),(580,20),(290,300),(580,540)]:
    assert im.getpixel(point) == (255,255,255,255), f'Unused canvas must be opaque white at{point}'
region = im.crop((40,180,120,215))
pixels = region.load()
ink = sum(1 for y in range(region.height) for x in range(region.width)
          if max(pixels[x,y][:3]) < 40 and pixels[x,y][3] == 255)
assert ink > 100, 'Expected dark2.94 branding in unused left area'
print('PASS:585x559 PNG/RGBA8, exact approved alpha, white unused samples and branding presence.')
print('Also inspect artwork, text spelling, seams, collar scale and sleeve/back continuity visually.')
