"""Crop/zoom helper for figure reviewers. Usage:
  python crop.py IN.png OUT.png x0 y0 x1 y1 [scale]
Coordinates in pixels of IN.png; scale (default 2) upsamples the crop with nearest-neighbour so small text can be inspected."""
import sys
from PIL import Image
src, dst, x0, y0, x1, y1 = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:7])
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0
im = Image.open(src).crop((x0, y0, x1, y1))
im = im.resize((int(im.width * scale), int(im.height * scale)), Image.NEAREST)
im.save(dst); print(dst, im.size)
