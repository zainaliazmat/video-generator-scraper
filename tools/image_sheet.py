#!/usr/bin/env python3
"""Tile a chapter's PROMOTED full-res photographs into one labelled sheet.

    python3 tools/image_sheet.py <slug> --cut hi --chapter 3
    python3 tools/image_sheet.py --project studio/videos/<slug>-hi-ch3
    python3 tools/image_sheet.py --selftest

Writes `<project>/assets-ch<N>/final/IMAGES-ch<N>.jpg` and a `.json` index.

WHY THIS EXISTS
---------------
The sound-off test ran twice: once at fetch, on a 6-cell candidate preview, and
again after a ~3-minute draft render. A defect caught late costs four invocations
(re-fetch -> rebuild -> re-draft -> re-review); caught at asset time it costs one.
This sheet is what makes the early catch possible on the images that were actually
PROMOTED, rather than on the candidate grid — which `fin-assets.md:237-240` records
as lossy ("sheets have shipped showing 4 of 12 cells", the ffmpeg image2 demuxer
silently dropping to a trailing subset). `montage` fails loudly on a missing file,
which is what a review tool must do.

WHAT THIS SHEET CANNOT DO — READ THIS BEFORE TRUSTING IT
--------------------------------------------------------
**It does not replace reading each promoted image at full resolution**
(`fin-assets.md:94-102`). A cell is a thumbnail however large the source was, and
the defect that rule exists for is legible text inside the photograph — euro or
złoty coins on a rupee hook, a "1 ZŁOTY" struck across a coin face. Those are
invisible at grid size by definition, and a sheet that claimed to catch them would
be the "checker that cannot see the work" failure wearing a new costume.

What the grid catches is the thing NO per-image look can, because it is not a
property of any single image: **repetition and sameness across the chapter.** One
photograph of books behind three different points passed every per-scene review and
was unmissable the moment the frames sat side by side. Two cells that merely look
alike are a finding here and nowhere else.

So the two looks are different questions, and `fin-assets` owes both:
  per image, at full resolution -> is THIS picture true, and does it say its line?
  the sheet, all at once        -> do any two of these say the same thing?

**And the post-render sheet does not go away either.** `chapter_sheet.py:18-22`:
Lottie has two failure modes that render a silent blank and pass every static check,
so only the encoded file proves what a viewer will see. This sheet has no idea what
the composition will do with these files. It judges the image SELECTION, and
`fin-review` still watches the encoded draft, once.
"""
import argparse
import glob
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Deliberately larger and narrower than chapter_sheet's 480x270 x4: a photograph is
# judged on its subject here, and three 640px cells still fit a 1920px-wide sheet.
CELL_W, CELL_H, COLS = 640, 360, 3


def scene_num(path):
    """s9 -> 9, so s9 sorts before s10. Lexicographic order puts s10 first and the
    reviewer then reads the chapter in an order the video never plays."""
    m = re.search(r"s(\d+)", os.path.basename(path))
    return int(m.group(1)) if m else 0


def promoted(project, chapter):
    """The promoted full-res jpgs for this chapter, in scene order.

    `assets-ch<N>/final/` only — never `_cand/`. A candidate is a thing that was
    considered; this sheet exists to show what was CHOSEN."""
    final = os.path.join(project, f"assets-ch{chapter}", "final")
    if not os.path.isdir(final):
        sys.exit(f"ERROR: no {os.path.relpath(final, ROOT)} — promote the images first")
    jpgs = [p for p in glob.glob(os.path.join(final, "*.jpg"))
            if not os.path.basename(p).startswith("IMAGES-")]
    return sorted(jpgs, key=lambda p: (scene_num(p), os.path.basename(p)))


def derived_from(jpg):
    """The scene this image is a deliberate crop OF, or None.

    A HOLD keeps one photograph across two lines as ONE continuous push, so its
    second scene ships a centre crop of the first ("same image across lines = one
    continuous zoom, never a self-dissolve" — the creator rule of 2026-07-23, and
    `storyboard-hi.md` §6b). On a grid those two cells look identical, and they are
    SUPPOSED to. Found on the first real run of this tool: `passive-income-number`
    hi ch2 shows two such pairs (s14/s15, s17/s18) in a chapter that is locked and
    correct. Unlabelled, every hold would read as a repetition finding and cost a
    re-pick round for doing exactly what the storyboard asked — the failure
    `fin-review`'s own last rule names, "a finding that contradicts the storyboard's
    declared device is a finding about the review".

    The `.src` sidecar already records it in its own first words; this only reads it.
    """
    try:
        with open(jpg + ".src", encoding="utf-8", errors="replace") as fh:
            head = fh.read(200)
    except OSError:
        return None
    m = re.match(r"\s*DERIVED CROP of\s+(\S+?)\.jpg", head, re.I)
    return m.group(1) if m else None


def build(project, chapter, out=None):
    cells = promoted(project, chapter)
    if not cells:
        sys.exit(f"ERROR: no promoted jpgs in assets-ch{chapter}/final/")
    final = os.path.join(project, f"assets-ch{chapter}", "final")
    out = out or os.path.join(final, f"IMAGES-ch{chapter}.jpg")

    index, cmd = [], ["montage"]
    for path in cells:
        scene = os.path.splitext(os.path.basename(path))[0]
        src = derived_from(path)
        # plain ASCII labels: montage renders an escape sequence literally and has
        # no Devanagari face, so a VO line as a label would sheet as tofu. The
        # reviewer reads the lines from the script and matches on the scene id.
        cmd += ["-label", f"{scene} (HOLD crop of {src})" if src else scene, path]
        index.append({"scene": scene, "file": os.path.relpath(path, ROOT),
                      "derived_from": src})
    cmd += ["-tile", f"{COLS}x", "-geometry", f"{CELL_W}x{CELL_H}+8+8",
            "-background", "#111111", "-fill", "white", "-pointsize", "28", out]
    subprocess.run(cmd, check=True)

    json.dump(index, open(os.path.splitext(out)[0] + ".json", "w"), indent=1)
    holds = [c["scene"] for c in index if c["derived_from"]]
    print(f"SHEET {os.path.relpath(out, ROOT)}  {len(cells)} promoted images")
    print(f"INDEX {os.path.relpath(os.path.splitext(out)[0] + '.json', ROOT)}")
    if holds:
        print(f"HOLDS {', '.join(holds)} are labelled crops of the cell before them — "
              f"a continuous push, NOT a repeat. Do not raise them as repetition.")
    print("Read the sheet for REPETITION across the chapter. It cannot show legible "
          "text inside a photograph — that is the full-resolution read, per image.")
    return out


def _selftest():
    import shutil
    import tempfile

    tmp = tempfile.mkdtemp(prefix="imgsheet-")
    try:
        final = os.path.join(tmp, "assets-ch3", "final")
        os.makedirs(os.path.join(final, "_cand"))
        for name in ("s10.jpg", "s2.jpg", "s9.jpg"):
            subprocess.run(["ffmpeg", "-v", "error", "-f", "lavfi", "-i",
                            "color=c=blue:s=64x36", "-frames:v", "1", "-y",
                            os.path.join(final, name)], check=True)
        subprocess.run(["ffmpeg", "-v", "error", "-f", "lavfi", "-i",
                        "color=c=red:s=64x36", "-frames:v", "1", "-y",
                        os.path.join(final, "_cand", "s2_a.jpg")], check=True)

        open(os.path.join(final, "s10.jpg.src"), "w").write(
            "DERIVED CROP of s9.jpg (no fetch): centre crop, the framing s9 ends on.")
        open(os.path.join(final, "s9.jpg.src"), "w").write("brass tap close up@pexels")
        assert derived_from(os.path.join(final, "s10.jpg")) == "s9"
        assert derived_from(os.path.join(final, "s9.jpg")) is None
        assert derived_from(os.path.join(final, "s2.jpg")) is None, "no sidecar, no claim"

        got = [os.path.basename(p) for p in promoted(tmp, 3)]
        # scene ORDER, not lexicographic — s10 after s9 is the order the video plays
        assert got == ["s2.jpg", "s9.jpg", "s10.jpg"], got
        # a candidate is a thing that was considered, not a thing that was chosen
        assert not any("_cand" in p for p in promoted(tmp, 3))

        out = build(tmp, 3)
        assert os.path.getsize(out) > 0
        idx = json.load(open(os.path.splitext(out)[0] + ".json"))
        assert [c["scene"] for c in idx] == ["s2", "s9", "s10"], idx
        assert [c["derived_from"] for c in idx] == [None, None, "s9"], idx
        # re-running must not tile its own output back into itself
        assert len(promoted(tmp, 3)) == 3, "the sheet re-entered its own cell list"
        print("selftest OK")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug", nargs="?")
    ap.add_argument("--cut", choices=("hi", "en"))
    ap.add_argument("--chapter", type=int)
    ap.add_argument("--project", help="chapter project dir, instead of slug/cut/chapter")
    ap.add_argument("-o", "--out")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()

    if a.selftest:
        return _selftest()
    project, chapter = a.project, a.chapter
    if project and chapter is None:
        m = re.search(r"-ch(\d+)/?$", project)
        chapter = int(m.group(1)) if m else None
    if not project:
        if not (a.slug and a.cut and a.chapter):
            ap.error("need <slug> --cut --chapter, or --project")
        project = os.path.join(ROOT, "studio", "videos",
                               f"{a.slug}-{a.cut}-ch{a.chapter}")
    if chapter is None:
        ap.error("could not infer the chapter number — pass --chapter")
    build(project, chapter, a.out)


if __name__ == "__main__":
    main()
