#!/usr/bin/env python3
"""Build ONE numbered PNG of every reviewable frame across a run's chapters.

This is the creator's review surface. `chapter_sheet.py` makes a per-chapter
contact sheet with scene labels; that is what the agents read. This makes the
cross-chapter sheet with a big index number on every cell, so the creator can
say "#7 is wrong" and everyone knows exactly which frame that is.

Sampling is not ours: it reuses the SHEET-*.json index chapter_sheet.py already
wrote, which samples one frame per scene PLUS one per declared data-framings
change. That is deliberate — a framing swap that is only cosmetic shows up here
as two near-identical cells, which is exactly the defect worth catching.

Each cell carries the index, the chapter + scene id, and TWO timestamps: one
into the chapter mp4 and one into the concatenated preview, so a note can be
scrubbed against either file.

    tools/frames_sheet.py <slug> --cut hi
    tools/frames_sheet.py <slug> --cut hi --chapters 3,4 -o /tmp/x.png

Exits non-zero if a chapter's render or sheet index is missing, naming it —
never silently produces a partial sheet.
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile

CW, CH, BAND, COLS = 768, 432, 56, 5
FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
]


def _font(size):
    from PIL import ImageFont
    for p in FONT_CANDIDATES:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def discover(slug, cut, chapters):
    """Return [(chapter, mp4, sheet_json)] in chapter order."""
    base = "studio/videos"
    found = []
    for name in sorted(os.listdir(base)):
        prefix = f"{slug}-{cut}-ch"
        if not name.startswith(prefix):
            continue
        try:
            n = int(name[len(prefix):])
        except ValueError:
            continue
        if chapters and n not in chapters:
            continue
        d = os.path.join(base, name, "renders")
        mp4 = next((os.path.join(d, f) for f in sorted(os.listdir(d))
                    if f.endswith(".mp4") and ("DRAFT" in f or "CD-" in f)), None) \
            if os.path.isdir(d) else None
        idx = next((os.path.join(d, f) for f in sorted(os.listdir(d))
                    if f.startswith("SHEET") and f.endswith(".json")), None) \
            if os.path.isdir(d) else None
        found.append((n, mp4, idx))
    return sorted(found)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--cut", default="hi")
    ap.add_argument("--chapters", help="comma list, e.g. 3,4,5 (default: all found)")
    ap.add_argument("-o", "--out")
    a = ap.parse_args()

    if shutil.which("ffmpeg") is None:
        sys.exit("ffmpeg not on PATH")
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        sys.exit("Pillow missing — pip install -r tools/requirements.txt")

    want = {int(x) for x in a.chapters.split(",")} if a.chapters else None
    chapters = discover(a.slug, a.cut, want)
    if not chapters:
        sys.exit(f"no chapter dirs found for {a.slug}-{a.cut}-ch*")

    missing = [f"ch{n}: {'render' if not m else 'sheet index'}"
               for n, m, i in chapters if not m or not i]
    if missing:
        sys.exit("cannot build a partial sheet — missing " + "; ".join(missing) +
                 "\nrun tools/chapter_sheet.py for those chapters first")

    # preview offset = sum of every EARLIER chapter's real duration
    rows, offset = [], 0.0
    for n, mp4, idx in chapters:
        for e in json.load(open(idx)):
            rows.append({"ch": n, "mp4": mp4, "scene": e["scene"],
                         "framing": e.get("framing", 1),
                         "t": e["t"], "pt": e["t"] + offset})
        offset += float(subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", mp4], capture_output=True, text=True).stdout.strip())

    tmp = tempfile.mkdtemp(prefix="frames_sheet_")
    try:
        for i, r in enumerate(rows, 1):
            r["png"] = os.path.join(tmp, f"f{i:03d}.png")
            subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", str(r["t"]),
                            "-i", r["mp4"], "-frames:v", "1", r["png"]], check=True)

        n_rows = (len(rows) + COLS - 1) // COLS
        sheet = Image.new("RGB", (CW * COLS, (CH + BAND) * n_rows), (9, 11, 16))
        d = ImageDraw.Draw(sheet)
        fn, fl, fs = _font(44), _font(22), _font(19)
        for i, r in enumerate(rows):
            x, y = CW * (i % COLS), (CH + BAND) * (i // COLS)
            sheet.paste(Image.open(r["png"]).resize((CW, CH)), (x, y))
            d.rectangle([x, y, x + 96, y + 62], fill=(255, 255, 255))
            lab = str(i + 1)
            d.text((x + 48 - d.textlength(lab, font=fn) / 2, y + 6), lab, font=fn,
                   fill=(10, 12, 18))
            fr = f"  framing {r['framing']}" if r["framing"] > 1 else ""
            d.text((x + 14, y + CH + 8),
                   f"#{i+1}   CH{r['ch']} · {r['scene']}{fr}", font=fl,
                   fill=(240, 240, 235))
            d.text((x + 14, y + CH + 32),
                   f"chapter t={r['t']:.2f}s   ·   preview t={r['pt']:.2f}s",
                   font=fs, fill=(150, 158, 175))
            d.rectangle([x, y, x + CW - 1, y + CH + BAND - 1], outline=(38, 44, 58))

        out = a.out or f"studio/videos/{a.slug}-{a.cut}-FRAMES.png"
        os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
        sheet.save(out)
        print(f"FRAMES {out}  {sheet.size[0]}x{sheet.size[1]}  "
              f"{len(rows)} frames from ch{chapters[0][0]}-ch{chapters[-1][0]}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
