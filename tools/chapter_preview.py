#!/usr/bin/env python3
"""Concatenate a cut's chapter drafts into ONE preview mp4, stream-copy.

    python3 tools/chapter_preview.py <slug> --cut hi

Writes studio/videos/<slug>-<cut>-PREVIEW.mp4 and prints the joint table.

This is a PREVIEW, not a master, and it differs from the final assembly in two
ways that get reported as defects every time unless they are said out loud:

1. **The chapter joints are hard cuts.** Each chapter's last scene carries a bare
   `data-duration` and each chapter's first scene never fades in, because inside a
   chapter project there is no successor to dissolve into. The 0.45s
   cross-dissolve comes back in the full assembly.
2. **It is a few frames longer than the master.** Every chapter's frame count
   rounds UP independently (55.909s x 30 = 1677.27 -> 1678), so eight chapters
   accumulate up to eight frames. The single full-length render has one root
   duration and cannot drift; this file is eight files glued together.

Stream copy, so it costs seconds and re-encodes nothing. It refuses to run if the
chapters do not share a codec / resolution / frame rate / audio layout, because a
concat demuxer will happily produce a broken file instead of saying so.
"""
import argparse
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def probe(path):
    """Video and audio read SEPARATELY.

    `-show_entries stream=…` over both streams collapses into one dict where the
    audio row wins every shared key — which is how the first version of this table
    printed the AAC frame count in a column headed `frames`."""
    def one(sel, keys):
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-select_streams", sel,
             "-show_entries", "stream=" + ",".join(keys), "-of", "default=nw=1", path],
            capture_output=True, text=True, check=True).stdout
        return dict(l.split("=", 1) for l in out.strip().split("\n") if "=" in l)

    d = one("v:0", ["codec_name", "width", "height", "r_frame_rate", "pix_fmt", "nb_frames"])
    for k, v in one("a:0", ["codec_name", "sample_rate", "channels"]).items():
        d["a_" + k] = v
    d["duration"] = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", path], capture_output=True, text=True, check=True).stdout.strip()
    return d


def chapters(slug, cut):
    base = os.path.join(ROOT, "studio/videos")
    prefix = f"{slug}-{cut}-ch"
    found = []
    for name in os.listdir(base):
        if not name.startswith(prefix):
            continue
        try:
            n = int(name[len(prefix):])
        except ValueError:
            continue
        rd = os.path.join(base, name, "renders")
        mp4 = next((os.path.join(rd, f) for f in sorted(os.listdir(rd))
                    if f.endswith(".mp4") and ("CD-" in f or "DRAFT" in f)), None) \
            if os.path.isdir(rd) else None
        if not mp4:
            sys.exit(f"ch{n}: no render in {rd} — draft it first")
        found.append((n, mp4))
    if not found:
        sys.exit(f"no chapter dirs for {slug}-{cut}-ch*")
    found.sort()
    missing = [n for n in range(1, found[-1][0] + 1) if n not in {x for x, _ in found}]
    if missing:
        sys.exit(f"chapters missing, refusing a partial preview: {missing}")
    return found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--cut", default="hi")
    ap.add_argument("-o", "--out")
    a = ap.parse_args()

    chs = chapters(a.slug, a.cut)
    out = a.out or os.path.join(ROOT, "studio/videos", f"{a.slug}-{a.cut}-PREVIEW.mp4")

    # Every joint is a stream copy, so a mismatch in any of these produces a file
    # that plays wrong rather than a failure. Check before writing, not after.
    KEYS = ("codec_name", "width", "height", "r_frame_rate", "pix_fmt",
            "a_codec_name", "a_sample_rate", "a_channels")
    ref, total, rows = None, 0.0, []
    for n, mp4 in chs:
        d = probe(mp4)
        sig = tuple(d.get(k) for k in KEYS)
        if ref is None:
            ref = sig
        elif sig != ref:
            sys.exit(f"ch{n} does not match ch{chs[0][0]}: {sig} vs {ref}\n"
                     "re-render it with the same -q/-f as the others")
        dur = float(d["duration"])
        rows.append((n, dur, total, int(d.get("nb_frames") or 0)))
        total += dur

    lst = out + ".txt"
    with open(lst, "w", encoding="utf-8") as f:
        for _, mp4 in chs:
            f.write(f"file '{mp4}'\n")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0",
                    "-i", lst, "-c", "copy", out], check=True)
    os.remove(lst)

    print(f"PREVIEW {out}")
    print(f"{'ch':>3}  {'starts at':>10}  {'duration':>9}  {'frames':>7}")
    for n, dur, start, nf in rows:
        print(f"{n:>3}  {start:>10.3f}  {dur:>9.3f}  {nf:>7}")
    print(f"     {'':>10}  {total:>9.3f}  total")
    print("Joints are HARD CUTS here (the 0.45s dissolve returns in the full "
          "assembly) and the total runs a few frames long (per-chapter frame "
          "rounding). Both are properties of the preview, not defects.")


if __name__ == "__main__":
    main()
