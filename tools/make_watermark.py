#!/usr/bin/env python3
"""Channel avatar -> the on-video watermark the scaffold ships.

    tools/make_watermark.py hi   # assets/brand/cashguruguides.jpg  -> wm-hi.png
    tools/make_watermark.py en   # assets/brand/moneymavens101.jpg  -> wm-en.png

The avatars arrive as square JPEGs: a circular mark on a white field. Pasted
onto a dark frame that white field is a box, so the circle is cut out into an
alpha channel here rather than trusted to CSS `border-radius` (which cannot
clip the JPEG's own white corners). Run this only when a channel changes its
avatar — the PNGs are committed.
"""
import sys, os
from PIL import Image, ImageDraw

SIZE = 256
SOURCES = {"hi": "cashguruguides.jpg", "en": "moneymavens101.jpg"}
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def build(cut):
    im = Image.open(os.path.join(ROOT, "assets", "brand", SOURCES[cut])).convert("RGB")
    s = min(im.size)
    box = ((im.width - s) // 2, (im.height - s) // 2, (im.width + s) // 2, (im.height + s) // 2)
    im = im.crop(box).resize((SIZE, SIZE), Image.LANCZOS)
    # mask drawn at 4x and downsampled — PIL's ellipse has no antialiasing
    mask = Image.new("L", (SIZE * 4, SIZE * 4), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, SIZE * 4 - 1, SIZE * 4 - 1), fill=255)
    im.putalpha(mask.resize((SIZE, SIZE), Image.LANCZOS))
    out = os.path.join(ROOT, "tools", "scaffold", "assets", "img", f"wm-{cut}.png")
    im.save(out)
    return out


if __name__ == "__main__":
    cuts = sys.argv[1:] or list(SOURCES)
    for cut in cuts:
        print(build(cut))
