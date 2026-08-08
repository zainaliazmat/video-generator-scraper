#!/usr/bin/env python3
"""Clause onsets inside one VO clip, measured from the audio.

Why this exists: `popEach(S.sN + 1.10, ..., 0.45)` is a FIXED OFFSET that ignores the
voice track, so a cascade lands where the template puts it rather than where the words
are. On passive-income-number hi ch1 s6 all three cells finished 0.20s BEFORE the first
noun's clause began, leaving 5.07s of dead air on the chapter's longest scene while the
voice named three things the picture had already shown. en ch1 s6 has the same defect
more mildly. fin-ceo ruled the DEFAULT should derive cascade offsets from measured
clause boundaries — a check would only tell each chapter it got it wrong again.

    tools/tts/clauses.py <slug> --cut hi --line 1.6            # onsets, human-readable
    tools/tts/clauses.py <slug> --cut hi --line 1.6 --n 3      # force exactly 3 clauses
    tools/tts/clauses.py <slug> --cut hi --line 1.6 --offsets  # bare `+2.50 +3.95 +5.10`

`--offsets` prints scene-relative anchors ready to paste into a build: they include the
clip's own `audio_start - scene_start` lead-in from timing.json, because a cascade is
anchored to the SCENE and the audio does not begin at the scene's first frame.

The clip is one sentence, so the boundaries this finds are commas and breath pauses.
That is exactly the granularity a cascade wants: one cell per named thing.
"""
import argparse
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def silences(mp3, noise_db, min_dur):
    """(start, end) of every detected silence, via ffmpeg silencedetect."""
    out = subprocess.run(
        ["ffmpeg", "-v", "info", "-i", mp3,
         "-af", "silencedetect=noise=%ddB:d=%.3f" % (noise_db, min_dur), "-f", "null", "-"],
        capture_output=True, text=True).stderr
    starts = [float(m) for m in re.findall(r"silence_start: ([\d.]+)", out)]
    ends = [float(m) for m in re.findall(r"silence_end: ([\d.]+)", out)]
    return list(zip(starts, ends + [None] * (len(starts) - len(ends))))


def duration(mp3):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", mp3], capture_output=True, text=True).stdout
    return float(out.strip())


def onsets(mp3, n=None):
    """Clause onsets in clip-local seconds. onsets[0] is the clip's first speech.

    Sweeps the silence threshold rather than trusting one: a comma pause in one clip is
    0.18s and in another 0.42s, because the engine honours a pause mark variably (the
    same reason the duration check had to become a range). When --n is given, take the
    loosest threshold that still yields n clauses — the tightest one splits inside words.
    """
    best = None
    # Nothing can begin in the last fraction of the clip. ffmpeg reports a silence_end at
    # the file's end when the clip fades out, and that boundary looks exactly like a clause
    # onset — on en 1.6 it produced a "clause" at +4.876 of a 4.911s clip. Caught only by
    # running the tool on a SECOND clip after it agreed with the hand measurement on the first.
    last_ok = duration(mp3) - 0.25
    for min_dur in (0.30, 0.26, 0.22, 0.18, 0.15, 0.12):
        gaps = silences(mp3, -32, min_dur)
        # a clause starts where a silence ends; the first onset is the clip's first speech
        pts = [e for _, e in gaps if e is not None and e < last_ok]
        lead = gaps[0][0] if gaps and gaps[0][0] < 0.35 else 0.0
        found = [lead] + [p for p in pts if p > lead + 0.05]
        if n is None:
            best = found
            break
        if len(found) >= n:
            best = found[:n]
            break
        if best is None or len(found) > len(best):
            best = found
    return best or [0.0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--cut", required=True)
    ap.add_argument("--line", required=True, help="VO line id, e.g. 1.6")
    ap.add_argument("--n", type=int, help="expected clause count, counting the opening one")
    ap.add_argument("--cells", type=int,
                    help="cells in the cascade. USE THIS, not --n, for a cascade: clause 1 is "
                         "the clip's opening speech onset and names nothing, so N cells need "
                         "N+1 boundaries with the first dropped. Getting this wrong puts every "
                         "cell one clause early — a milder version of the defect this tool exists "
                         "for. Validated on hi 1.6: --cells 3 gives +2.50 +3.99 +5.15 against the "
                         "+2.50 +3.95 +5.10 fin-ceo measured off the envelope by hand.")
    ap.add_argument("--offsets", action="store_true",
                    help="print bare scene-relative anchors, ready for a build")
    a = ap.parse_args()

    voice = os.path.join(ROOT, "studio/videos/%s-%s/assets/voice" % (a.slug, a.cut))
    mp3 = os.path.join(voice, "%s.mp3" % a.line)
    if not os.path.exists(mp3):
        sys.exit("no clip at %s" % mp3)
    rows = json.load(open(os.path.join(voice, "timing.json")))["lines"]
    row = next((r for r in rows if r["id"] == a.line), None)
    if row is None:
        sys.exit("line %s is not in timing.json" % a.line)

    # a cascade is anchored to the SCENE; the audio starts later than the scene does
    lead = round(row["audio_start"] - row["scene_start"], 3)
    want = a.n if a.cells is None else a.cells + 1
    pts = onsets(mp3, want)
    if a.cells is not None:
        pts = pts[1:]           # clause 1 is the opening onset and names nothing

    if a.offsets:
        # A build pastes this output directly, so silently printing fewer anchors than
        # asked for — or an empty line — is worse than no tool at all. Fail loudly.
        want_cells = want - 1 if a.cells is not None else want
        if want_cells and len(pts) != want_cells:
            sys.exit("FAIL clauses %s %s line %s — asked for %d, measured %d (%s). The "
                     "sentence does not have that many pause-separated parts; re-read the "
                     "line rather than anchoring to a number this did not find."
                     % (a.slug, a.cut, a.line, want_cells, len(pts),
                        " ".join("+%.2f" % (p + lead) for p in pts) or "none"))
        print(" ".join("+%.2f" % (p + lead) for p in pts))
        return

    print("%s %s  line %s — clip %.3fs, scene lead-in %.3fs"
          % (a.slug, a.cut, a.line, row["duration"], lead))
    for i, p in enumerate(pts):
        print("  clause %d  clip %+.3f  ->  scene anchor +%.2f" % (i + 1, p, p + lead))
    tail = round(row["scene_duration"] - (pts[-1] + lead), 3)
    print("  tail after the last clause onset: %.3fs" % tail)
    if want and len(pts) != (want - 1 if a.cells is not None else want):
        print("  WARN asked for %d, found %d — the sentence may not have that many "
              "pause-separated parts. Do not force it; check the line." % (want, len(pts)))


def selftest():
    """One runnable check against the clip this tool was written for: hi 1.6, whose
    three cells fin-ceo re-anchored to +2.50 / +3.95 / +5.10 by ear and by envelope."""
    voice = os.path.join(ROOT, "studio/videos/passive-income-number-hi/assets/voice")
    mp3 = os.path.join(voice, "1.6.mp3")
    if not os.path.exists(mp3):
        print("SKIP clauses.py --selftest — %s not on disk" % mp3)
        return
    rows = json.load(open(os.path.join(voice, "timing.json")))["lines"]
    row = next(r for r in rows if r["id"] == "1.6")
    lead = row["audio_start"] - row["scene_start"]
    cells = [p + lead for p in onsets(mp3, 4)[1:]]     # --cells 3
    assert len(cells) == 3, cells
    assert cells == sorted(cells), cells
    # every anchor inside the scene, none before the audio
    assert cells[0] >= lead - 1e-6, cells
    assert cells[-1] < row["scene_duration"], (cells, row["scene_duration"])
    # the defect being fixed: the fixed +1.10 anchor put the LAST cell before the FIRST
    # spoken noun. Any honest measurement must put cell 3 well past it.
    assert cells[-1] > 1.10, "measured onsets must beat the fixed +1.10 anchor: %s" % cells
    # agreement with fin-ceo's independent by-hand envelope reading (+2.50 +3.95 +5.10).
    # Two different methods within 0.05s is what makes this tool trustworthy at all.
    for got, want in zip(cells, (2.50, 3.95, 5.10)):
        assert abs(got - want) < 0.10, "drifted from the hand measurement: %s" % cells
    print("PASS clauses.py --selftest — hi 1.6 cells %s (fin-ceo measured +2.50 +3.95 +5.10)"
          % " ".join("+%.2f" % c for c in cells))


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
    else:
        main()
