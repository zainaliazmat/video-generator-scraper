#!/usr/bin/env python3
"""Two-pass EBU R128 loudness normalisation — the last step before upload.

    tools/loudnorm.py studio/videos/<slug>-<cut>/renders/FINAL-1080p-<cut>.mp4

Writes PUBLISH-1080p-<cut>.mp4 next to the master and prints the measured
result. The master is never touched: pass 1 only measures, and pass 2 writes a
new file, so a bad run costs nothing.

WHY (audit 2026-07-29). ElevenLabs returns clips at about -24 LUFS and nothing
in the pipeline stages gain, so every shipped cut sat at -21 to -22 LUFS.
YouTube normalises toward -14 LUFS by ATTENUATING loud uploads; it applies no
positive gain to quiet ones. A -22 LUFS upload therefore plays at -22 — roughly
8 dB under everything around it in the feed, for the whole video.

A flat +8 dB is not available: the crest factor is ~17.8 dB, so the peak would
land near +3.8 dBTP. Two-pass loudnorm redistributes instead of just amplifying.

TP=-1.5, not -1.0. AAC encoding overshoots the limiter slightly; measured, a
-1.0 target lands at about -0.76 dBTP and fails fin-render's own "below -1 dBTP"
gate. -1.5 measured -1.26 on the first real master, but only -0.98 on
japanese-money-methods-hi (2026-08-01) — a FAIL — because that mix carries 24 SFX
transients and the AAC overshoot scales with them. -2.0 is the ceiling that holds
with a music bed and a full SFX kit under the voice. The ceiling costs nothing
audible: it limits peaks only, while the -14 LUFS integrated target is what
actually sets perceived loudness.

Video is stream-copied (-c:v copy), so this costs ~20 seconds, not a re-encode,
and the picture is bit-identical to the master.
"""
import json
import os
import re
import subprocess
import sys

TARGET_I = -14.0     # YouTube's normalisation target for spoken-word
TARGET_TP = -2.0     # ceiling; see module docstring for why not -1.0 or -1.5
TARGET_LRA = 11.0


def _run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def measure(src):
    """Pass 1 — analyse. loudnorm prints its JSON block to stderr."""
    r = _run(["ffmpeg", "-hide_banner", "-nostats", "-i", src, "-vn",
              "-af", f"loudnorm=I={TARGET_I}:TP={TARGET_TP}:LRA={TARGET_LRA}:print_format=json",
              "-f", "null", "-"])
    m = re.search(r"\{[^{}]*\"input_i\".*?\}", r.stderr, re.S)
    if not m:
        sys.exit(f"loudnorm pass 1 produced no JSON for {src}\n{r.stderr[-2000:]}")
    return json.loads(m.group(0))


def normalize(src, dst=None):
    if not os.path.exists(src):
        sys.exit(f"missing: {src}")
    # MIXED- as well as FINAL-: the pipeline order is FINAL -> mix.py -> MIXED ->
    # here, so MIXED is the NORMAL input and FINAL is only the voice-only case
    # (no audio.json). Handling only FINAL- made dst == src on every real run and
    # the tool refused with "refusing to overwrite the master in place" — a
    # correct guard firing on the correct usage.
    dst = dst or os.path.join(
        os.path.dirname(src),
        re.sub(r"^(FINAL|MIXED)-", "PUBLISH-", os.path.basename(src)))
    if os.path.abspath(dst) == os.path.abspath(src):
        sys.exit("refusing to overwrite the master in place")

    a = measure(src)
    print(f"  in : {a['input_i']} LUFS  {a['input_tp']} dBTP  LRA {a['input_lra']}")

    r = _run(["ffmpeg", "-y", "-hide_banner", "-nostats", "-i", src, "-map", "0",
              "-c:v", "copy",
              "-af", (f"loudnorm=I={TARGET_I}:TP={TARGET_TP}:LRA={TARGET_LRA}:"
                      f"measured_I={a['input_i']}:measured_TP={a['input_tp']}:"
                      f"measured_LRA={a['input_lra']}:measured_thresh={a['input_thresh']}:"
                      f"offset={a['target_offset']}:linear=true"),
              "-c:a", "aac", "-b:a", "192k", "-ar", "48000", dst])
    if r.returncode != 0 or not os.path.exists(dst):
        sys.exit(f"loudnorm pass 2 failed\n{r.stderr[-2000:]}")

    got = measure(dst)
    print(f"  out: {got['input_i']} LUFS  {got['input_tp']} dBTP  -> {dst}")
    # The gate fin-render already enforces on the master; assert it on the
    # thing that actually gets uploaded.
    if float(got["input_tp"]) > -1.0:
        sys.exit(f"FAIL true peak {got['input_tp']} dBTP is above -1")
    if abs(float(got["input_i"]) - TARGET_I) > 1.0:
        sys.exit(f"FAIL landed at {got['input_i']} LUFS, wanted {TARGET_I}")
    return dst


def _selftest():
    """Generate 20s of quiet tone + silence, normalise it, assert it moved."""
    import shutil
    import tempfile
    d = tempfile.mkdtemp(prefix="loudnorm-")
    try:
        src = os.path.join(d, "FINAL-1080p-xx.mp4")
        # -24 dBFS tone under a black frame: a stand-in for a quiet VO master.
        _run(["ffmpeg", "-y", "-hide_banner", "-nostats",
              "-f", "lavfi", "-i", "color=c=black:s=320x180:r=25:d=20",
              "-f", "lavfi", "-i", "sine=frequency=220:duration=20",
              "-af", "volume=-24dB", "-c:v", "libx264", "-preset", "ultrafast",
              "-c:a", "aac", "-shortest", src])
        assert os.path.exists(src), "fixture encode failed"
        before = float(measure(src)["input_i"])
        out = normalize(src)
        after = float(measure(out)["input_i"])
        assert before < -18, f"fixture should start quiet, got {before}"
        assert abs(after - TARGET_I) <= 1.0, f"normalised to {after}, wanted {TARGET_I}"
        assert after > before, "normalisation made it quieter"
        # the master must survive untouched
        assert abs(float(measure(src)["input_i"]) - before) < 0.01, "master was modified"
        print(f"selftest OK  {before:.1f} -> {after:.1f} LUFS")
    finally:
        shutil.rmtree(d, ignore_errors=True)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        _selftest()
    elif len(sys.argv) < 2:
        sys.exit(__doc__)
    else:
        normalize(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
