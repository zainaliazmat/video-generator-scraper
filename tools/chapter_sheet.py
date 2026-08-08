#!/usr/bin/env python3
"""Turn a chapter's draft render into ONE labelled contact sheet — a frame per
scene — so a reviewer can judge every image in a single look.

    python3 tools/chapter_sheet.py studio/videos/<slug>-<cut>-ch<N> \\
        [renders/DRAFT-ch<N>.mp4] [-o <sheet.jpg>]

Why this exists
---------------
Reviewing a chapter by scrubbing an mp4 costs one vision call per frame and
tempts a reviewer into judging the two or three frames they happened to sample.
A sheet is one call for the whole chapter, and — the point — it puts every scene
side by side, which is the only way the repetition failures show up. The
"one photo of books behind three different points" defect in
japanese-money-methods ch2 was invisible scene-by-scene and obvious the moment
the frames sat in a grid.

Frames come from the ENCODED mp4, never the browser. Lottie scenes have two
failure modes (absolute-time seeking, and `discover()` overwriting the player)
that render a silent blank and pass every static check; only the encoded file
proves what a viewer will see.

Sampling: each scene is sampled at start + 2.6s, clamped inside the scene. That
is after the cue ladder has landed (kicker 0.30 -> statement 1.10 -> cue 1.90)
so the frame shows the scene fully assembled rather than mid-build. Scenes
shorter than that are sampled at their midpoint.

Notes
-----
* `montage` (ImageMagick), not ffmpeg's tile filter. ffmpeg's image2 demuxer
  silently drops to a trailing subset when any numbered input is missing —
  `_cand` sheets in tools/stock have shipped with 4 of 12 cells and no warning.
  montage fails loudly on a missing file, which is what a review tool must do.
* Multi-framing scenes (`data-framings="5.2,3.9"`) get one frame PER framing,
  because a framing is a different picture and the whole point is to see them.
"""
import argparse
import json
import os
import re
import subprocess
import sys

CELL_W, CELL_H, COLS = 480, 270, 4
SETTLE = 2.6          # cue ladder is done by here (kicker .30 -> stmt 1.10 -> cue 1.90)
SETTLE_VECTOR = 6.0   # a drawn scene is only worth judging once its art has FINISHED
# Keyed off ANY drawn vector art, not off Lottie specifically. It was Lottie-only
# until 2026-08-08, when en ch1 s6 sheeted a tick cascade one third built: the cell
# showed the third checkbox EMPTY, because `.v-ticks` is inline SVG rather than a
# Lottie and nothing matched it, so it fell to the 2.6 default while the last tick
# only lands at +3.116. Same failure as the countUp below and the japanese-money
# stub bar before it, arriving a third time through a fourth kind of art. Matching
# the `v-` family instead of one class name is what stops a fifth kind repeating it —
# over-settling only shows a finished frame, which is what a sheet is FOR; motion is
# what the mp4 is for.
# A counting number is the same failure as a half-drawn Lottie, and worse in kind:
# a partial chart looks broken, but a partial count looks like a REAL NUMBER. On
# passive-income-number ch2 the rung-one corpus counts to Rs 10,00,000 over 1.2s
# from +1.90, so the +2.6 sample sheeted Rs 8,36,874 — plausible, wrong, and the
# figure every downstream reviewer and the CEO would have judged the rung on.
# Five more rungs in ch3-7 would each have shown their own fabricated total.
SETTLE_COUNTUP = 4.5


def scenes(html_path):
    """[(id, start, duration, [framing durations])] in document order."""
    html = open(html_path, encoding="utf-8").read()
    # Split on section starts so each scene's inner markup travels with its tag —
    # needed to know whether it holds a Lottie, which changes when to sample it.
    out = []
    chunks = re.split(r"(?=<section[^>]*class=\"[^\"]*\bscene\b)", html)
    for chunk in chunks:
        tag = re.match(r"<section[^>]*>", chunk)
        if not tag:
            continue
        tag = tag.group(0)
        sid = re.search(r'id="([^"]+)"', tag)
        st = re.search(r'data-start="([\d.]+)"', tag)
        du = re.search(r'data-duration="([\d.]+)"', tag)
        if not (sid and st and du):
            continue
        fr = re.search(r'data-framings="([\d.,\s]+)"', tag)
        framings = [float(x) for x in fr.group(1).split(",") if x.strip()] if fr else []
        markup = chunk.split("</section>")[0]
        has_vector = 'class="lottie' in markup or 'class="v-' in markup
        # countUp lives in the <script>, not in the section markup, so look for a
        # call naming this scene anywhere in the file.
        has_countup = f'countUp("#{sid.group(1)}-' in html
        out.append((sid.group(1), float(st.group(1)), float(du.group(1)), framings,
                    has_vector, has_countup))
    return out


def sample_times(start, duration, framings, has_vector=False, has_countup=False):
    """One time per framing; settle into each, clamped inside it.

    A scene carrying drawn art is sampled LATE. Drawn art typically starts at cue
    slot 3 (+1.90) and runs 3.5-4.5s, so the default +2.6 catches it a third built —
    japanese-money-methods ch2 s17 sheeted as a single stub bar and read as a
    broken frame when the finished chart was fine. Judge the end state; motion
    is what the mp4 is for.

    The settles are a MAX, not a chain of elifs: a scene can hold drawn art AND a
    counting number, and the old `elif` meant whichever test ran first silently won.
    """
    settle = SETTLE
    if has_vector:
        settle = max(settle, SETTLE_VECTOR)
    if has_countup:
        settle = max(settle, SETTLE_COUNTUP)
    spans, t = [], start
    for f in (framings if len(framings) > 1 else [duration]):
        spans.append((t, f))
        t += f
    return [s + (settle if f > settle + 0.4 else f * 0.75) for s, f in spans]


def grab(video, t, out):
    subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", video,
                    "-frames:v", "1", "-y", out], check=True)


def main():
    ap = argparse.ArgumentParser(description="One-frame-per-scene contact sheet for a chapter draft")
    ap.add_argument("project", help="chapter project dir (holds index.html)")
    ap.add_argument("video", nargs="?", help="draft mp4 (default: newest in renders/)")
    ap.add_argument("-o", "--out", help="sheet path (default: <project>/renders/SHEET.jpg)")
    a = ap.parse_args()

    html = os.path.join(a.project, "index.html")
    if not os.path.exists(html):
        sys.exit(f"ERROR: no index.html in {a.project}")

    video = a.video
    if not video:
        rd = os.path.join(a.project, "renders")
        mp4s = [os.path.join(rd, f) for f in os.listdir(rd)] if os.path.isdir(rd) else []
        mp4s = [f for f in mp4s if f.endswith(".mp4")]
        if not mp4s:
            sys.exit("ERROR: no mp4 in renders/ — render a draft first")
        video = max(mp4s, key=os.path.getmtime)
    if not os.path.isabs(video) and not os.path.exists(video):
        video = os.path.join(a.project, video)

    out = a.out or os.path.join(a.project, "renders", "SHEET.jpg")
    tmp = os.path.join(a.project, "renders", "_sheet")
    os.makedirs(tmp, exist_ok=True)

    cells, index = [], []
    for sid, start, dur, framings, has_vector, has_countup in scenes(html):
        for n, t in enumerate(sample_times(start, dur, framings, has_vector, has_countup)):
            # plain ASCII: montage's -label renders an escape sequence literally,
            # so "\u2192" sheeted as the cell name "s19u21922".
            label = sid if n == 0 else f"{sid}.{n + 1}"
            path = os.path.join(tmp, f"{len(cells):02d}.jpg")
            grab(video, t, path)
            cells.append((path, label))
            index.append({"scene": sid, "framing": n + 1, "t": round(t, 3)})

    if not cells:
        sys.exit("ERROR: no .scene sections found — is this a chapter project?")

    cmd = ["montage"]
    for path, label in cells:
        cmd += ["-label", label, path]
    cmd += ["-tile", f"{COLS}x", "-geometry", f"{CELL_W}x{CELL_H}+6+6",
            "-background", "#111111", "-fill", "white", "-pointsize", "26", out]
    subprocess.run(cmd, check=True)

    json.dump(index, open(os.path.splitext(out)[0] + ".json", "w"), indent=1)
    for f in os.listdir(tmp):
        os.remove(os.path.join(tmp, f))
    os.rmdir(tmp)
    print(f"SHEET {out}  {len(cells)} frames from {os.path.basename(video)}")
    print(f"INDEX {os.path.splitext(out)[0]}.json")


def _selftest():
    """Every kind of drawn art must sheet its FINISHED state, not a third of it."""
    # plain scene: the cue ladder is done by +2.6
    assert sample_times(0.0, 8.0, [], False, False) == [2.6]
    # inline-SVG art (`.v-ticks`) is drawn art too — this is the 2026-08-08 bug:
    # en ch1 s6 sampled +2.6 = 28.151 while its last tick only landed at +3.116.
    assert sample_times(25.551, 6.161, [], True, False)[0] > 25.551 + 3.116
    # a Lottie long enough to clear the settle takes it flat
    assert sample_times(14.599, 7.415, [], True, False) == [20.599]
    # a countUp still gets its own 4.5
    assert sample_times(0.0, 8.0, [], False, True) == [4.5]
    # …and a scene holding BOTH takes the LARGER, which the old elif chain did not:
    # whichever branch ran first won, so drawn art next to a counting number could
    # be sheeted at 4.5 with the art still building.
    assert sample_times(0.0, 12.0, [], True, True) == [6.0]
    # short scenes clamp inside themselves rather than sampling past the end
    for span in (1.0, 2.0, 3.5):
        t = sample_times(10.0, span, [], True, True)[0]
        assert 10.0 < t < 10.0 + span, (span, t)
    # one sample per framing, each settled inside its own framing
    ts = sample_times(0.0, 20.0, [8.0, 12.0], False, False)
    assert ts == [2.6, 10.6], ts
    print("selftest OK")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        _selftest()
    else:
        main()
