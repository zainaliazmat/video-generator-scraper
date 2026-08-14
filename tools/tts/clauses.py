#!/usr/bin/env python3
"""Clause onsets inside one VO clip, measured from the audio.

Why this exists: `popEach(S.sN + 1.10, ..., 0.45)` is a FIXED OFFSET that ignores the
voice track, so a cascade lands where the template puts it rather than where the words
are. On passive-income-number hi ch1 s6 all three cells finished 0.20s BEFORE the first
noun's clause began, leaving 5.07s of dead air on the chapter's longest scene while the
voice named three things the picture had already shown. en ch1 s6 has the same defect
more mildly. fin-ceo ruled the DEFAULT should derive cascade offsets from measured
clause boundaries — a check would only tell each chapter it got it wrong again.

    tools/tts/clauses.py <slug> --cut en --line 1.6            # onsets, human-readable
    tools/tts/clauses.py <slug> --cut en --line 1.6 --n 3      # force exactly 3 clauses
    tools/tts/clauses.py <slug> --cut en --line 1.6 --offsets  # bare `+2.50 +3.95 +5.10`

`--offsets` prints scene-relative anchors ready to paste into a build: they include the
clip's own `audio_start - scene_start` lead-in from timing.json, because a cascade is
anchored to the SCENE and the audio does not begin at the scene's first frame.

The clip is one sentence, so the boundaries this finds are commas and breath pauses.
That is exactly the granularity a cascade wants: one cell per named thing.

PRECISION, measured against fin-ceo's independent by-hand read of hi 1.6: this lands
within 0.05s and consistently a hair LATE (2.501/3.989/5.147 against 2.50/3.95/5.10).
Late is the safe direction — a cell arriving just after its noun reads as the picture
following the voice, which is what the beat wants; arriving before it is the defect this
tool exists to prevent. Do not "correct" the residual toward zero.
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
    """Synthetic check of onsets(): a built clip with KNOWN clause gaps.

    This used to measure `passive-income-number-hi` 1.6 against fin-ceo's by-hand
    read. That cut was deleted with the Hindi lane (2026-08-15) and the check went
    permanently to SKIP — a check that can no longer fail is not evidence
    (vault/knowledge/evidence-discipline). So the ground truth is now CONSTRUCTED:
    tone/silence/tone at offsets we choose, which exercises the same threshold
    sweep and still fails if the sweep, the lead-in or the tail guard break.

    The tolerance is 0.06s, the residual the real-clip check measured (it landed
    within 0.05s and a hair LATE). Late remains the safe direction — do not
    "correct" the residual toward zero.
    """
    import tempfile
    # speech at 0.00-1.00, 1.60-2.60, 3.40-4.60, then 0.60s of tail
    want = [0.0, 1.60, 3.40]
    filt = ("sine=frequency=440:duration=1.0,apad=pad_dur=0.6[a];"
            "sine=frequency=440:duration=1.0,apad=pad_dur=0.8[b];"
            "sine=frequency=440:duration=1.2,apad=pad_dur=0.6[c];"
            "[a][b][c]concat=n=3:v=0:a=1[out]")
    with tempfile.TemporaryDirectory() as tmp:
        mp3 = os.path.join(tmp, "synthetic.mp3")
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-filter_complex", filt,
                        "-map", "[out]", "-q:a", "2", mp3], check=True)
        got = onsets(mp3, 3)
        assert len(got) == 3, "expected 3 clause onsets, got %s" % got
        assert got == sorted(got), got
        # the tail-guard must not invent a clause out of the trailing silence
        assert got[-1] < duration(mp3) - 0.25, (got, duration(mp3))
        for g, w in zip(got, want):
            assert abs(g - w) < 0.06, "drifted from the built gaps: %s vs %s" % (got, want)
    print("PASS clauses.py --selftest — synthetic cells %s (built at %s)"
          % (" ".join("+%.2f" % c for c in got), " ".join("+%.2f" % w for w in want)))


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
    else:
        main()
