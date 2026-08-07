#!/usr/bin/env python3
"""Prove every SFX cue is IN THE ENCODED FILE — never from the mix log.

    python3 tools/audio/verify_cues.py studio/videos/<slug>-<cut>/renders/MIXED-1080p-<cut>.mp4

Builds a REFERENCE mix of the same master with the cue list emptied — same bed,
same gains, same duck, no SFX — then compares a 20 ms RMS envelope of the two at
every cue. The difference is the sound itself and nothing else.

WHY NOT AGAINST THE VOICE-ONLY MASTER. That was the first version of this script
and it reported 188 of 188 cues "raised", including +58 dB lifts. The bed is
continuous and the master has none, so every window in the mix is louder than the
same window in the master whether a cue landed there or not — the test measured
"has a music bed", passed everything, and would have passed a mix with zero SFX
in it. A test that cannot fail is not evidence.

WHY NOT THE MIX LOG. `mix.py` prints what it PLACED. It cannot know whether
ffmpeg's adelay landed the file, whether the cue fell past the runtime, or
whether amix ate it. The only evidence that a sound is in the video is the video.

READING THE OUTPUT. At the creator-approved kit levels roughly HALF the cues read
"flat" and that is CORRECT, not a fault: they land under speech, where a -22 dBFS
whoosh is felt rather than heard. The creator chose those levels over a +6 dB
variant that scored 22/22 on this test (HANDOVER §4c). What IS a failure is a cue
flat where the reference is quiet — nothing was masking it, so it is not there.
"""
import argparse
import array
import json
import math
import os
import re
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mix as mixer                                            # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SR = 8000               # plenty for an energy envelope
WIN = int(SR * 0.020)   # 20 ms


def pcm(path):
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", path, "-map", "a:0", "-ac", "1",
         "-ar", str(SR), "-f", "s16le", "-"],
        capture_output=True, check=True).stdout
    a = array.array("h")
    a.frombytes(raw[:len(raw) // 2 * 2])
    return a


def rms_env(samples):
    env = []
    for i in range(0, len(samples) - WIN, WIN):
        s = 0
        for v in samples[i:i + WIN]:
            s += v * v
        env.append(math.sqrt(s / WIN))
    return env


def envelope(path):
    return rms_env(pcm(path))


def difference(a, b):
    """mixed - reference IS the SFX bus, exactly: both are linear mixes of the
    same voice and the same bed at the same gains, and only the cue list
    differs. So this isolates the sounds from whatever is masking them, which is
    the difference between 'quiet' and 'absent' — the only question that
    matters. (AAC quantisation noise does not survive the subtraction at any
    level near a -22 dBFS cue.)"""
    n = min(len(a), len(b))
    return array.array("i", (a[i] - b[i] for i in range(n)))


def db(x):
    return 20 * math.log10(x + 1e-9)


def peak(env, t0, t1):
    a = max(int(t0 / 0.020), 0)
    b = min(max(int(t1 / 0.020), a + 1), len(env))
    seg = env[a:b]
    return max(seg) if seg else 0.0


def reference(master, spec, out):
    """The same mix with the cue list emptied. mix.py reads audio.json off disk,
    so the plan is swapped in-process rather than by writing a second file next
    to the composition, which a later run would then mix from by mistake."""
    real = mixer.plan
    mixer.plan = lambda src: {"music": spec.get("music"), "sfx": []}
    try:
        mixer.mix(master, out)
    finally:
        mixer.plan = real
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mixed", help="MIXED- or PUBLISH- mp4")
    ap.add_argument("--master", help="the voice-only FINAL- mp4 (default: sibling)")
    ap.add_argument("--lift", type=float, default=0.5, help="dB of local lift that counts")
    ap.add_argument("--keep-reference", action="store_true")
    a = ap.parse_args()

    mixed = os.path.abspath(a.mixed)
    master = a.master or re.sub(r"(MIXED|PUBLISH)-", "FINAL-", mixed)
    proj = os.path.dirname(os.path.dirname(mixed))
    spec = json.load(open(os.path.join(proj, "assets", "audio.json"), encoding="utf-8"))
    cues = spec["sfx"]

    tmp = tempfile.mkdtemp(prefix="verify-cues-")
    ref = os.path.join(tmp, "NOSFX-" + os.path.basename(mixed))
    print(f"  building the no-SFX reference (bed + voice, same gains)…")
    reference(master, spec, ref)

    pm, pr = pcm(mixed), pcm(ref)
    em, er = rms_env(pm), rms_env(pr)
    ed = rms_env(difference(pm, pr))          # the SFX bus, alone
    floor = sorted(ed)[len(ed) // 2]          # its own median = the silence between cues

    raised = masked = ghost = 0
    for c in cues:
        t = float(c["at"])
        # PRESENT: is the sound in the file at all? Measured on the SFX bus.
        d = peak(ed, t - 0.02, t + 0.35)
        present = d > max(floor * 4, 8)
        # AUDIBLE: does it lift the programme over the identical bed-only mix?
        lift = db(peak(em, t - 0.02, t + 0.30)) - db(peak(er, t - 0.02, t + 0.30))
        if not present:
            ghost += 1
            tag = "!! ABSENT — no energy on the SFX bus"
        elif lift >= a.lift:
            raised += 1
            tag = "present · lifts the programme"
        else:
            masked += 1
            tag = "present · sits under speech (expected at kit levels)"
        print(f"  {t:8.3f}  {c['name']:<11} sfx {db(d) - db(floor):+6.1f} dB "
              f"over floor · programme {lift:+5.2f} dB  {tag}")

    n = len(cues)
    print(f"\n{n} cues · {raised + masked} PRESENT on the SFX bus "
          f"({raised} lift the programme, {masked} masked by speech) · {ghost} absent")
    if not a.keep_reference:
        import shutil
        shutil.rmtree(tmp, ignore_errors=True)
    else:
        print(f"reference kept: {ref}")
    if ghost:
        sys.exit(f"FAIL: {ghost} cue(s) put NO energy on the SFX bus — they are "
                 f"not in the file")
    print(f"PASS: all {n} cues are in the encode; {100 * raised // n}% also lift "
          f"the programme over the identical bed-only mix (the rest sit under "
          f"speech by design — HANDOVER 4c)")


if __name__ == "__main__":
    main()
