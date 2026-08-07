#!/usr/bin/env python3
"""Mix the music bed and SFX under a rendered master. Video is stream-copied.

    tools/audio/mix.py studio/videos/<slug>-<cut>/renders/FINAL-1080p-<cut>.mp4

Reads the cue list the build wrote to `<project>/assets/audio.json`:

    { "music": "bed-tension",
      "sfx": [ {"at": 18.4, "name": "stamp"}, {"at": 116.2, "name": "hero"} ] }

Writes `MIXED-1080p-<cut>.mp4` beside the master, which then goes through
`tools/loudnorm.py` to reach -14 LUFS. Pipeline order is:

    encode -> FINAL -> mix.py -> MIXED -> loudnorm.py -> PUBLISH (upload this)

WHY IN POST, NOT IN THE COMPOSITION. HyperFrames renders by walking frames and
mixing declared audio elements; volume automation inside the page is not
something the renderer guarantees, and a bed that fails to duck silently buries
the voice in a video that still passes every check. ffmpeg's sidechain
compressor is deterministic, inspectable, and runs in seconds on a stream copy.
The composition therefore stays voice-only — one audio row per line, exactly as
today — and every mixing decision lives here.

Missing assets are NOT an error: no `audio.json`, no bed on disk, or an SFX file
that hasn't been generated all degrade to "mix what exists". A pipeline that
refuses to finish a video because a nice-to-have sound is absent is worse than
one that ships the video.

Levels: bed at 0.16 linear, ducked by roughly 6 dB under speech
(threshold 0.03, ratio 6) -> about 18 LU below the voice, which is where a bed
supports a narrator instead of competing with a spoken number. SFX are already
peak-normalised by `sfx.py` per `kit.json`, so they are placed at unity here.
"""
import json
import math
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LIB = os.path.join(ROOT, "studio", "library")
LOOP_XFADE = 3.0   # seconds of crossfade at each bed loop joint
# Creator-approved balance, 2026-08-06, off an A/B on japanese-money-methods
# -en ch1. Was 0.16 / 1.0 / 1.0. The bed now sits 3.5 dB further under the voice.
# VOICE_GAIN does NOT make the narration absolutely louder — loudnorm pins the
# programme to -14 LUFS and the voice dominates that measurement — it makes the
# voice stand prouder over the bed. SFX ride WITH the voice on purpose: leaving
# them at 1.0 while the voice rose would have pushed the kit ~1.6 dB quieter
# against the narration, which is the one thing the creator asked not to change.
BED_GAIN = 0.128
VOICE_GAIN = 1.2
SFX_GAIN = 1.2
DUCK = "threshold=0.03:ratio=6:attack=20:release=400"


def duration(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                        "format=duration", "-of", "csv=p=0", path],
                       capture_output=True, text=True)
    return float(r.stdout.strip())


def plan(src):
    """The cue list next to the composition, or an empty plan."""
    p = os.path.join(os.path.dirname(os.path.dirname(src)), "assets", "audio.json")
    if not os.path.exists(p):
        print(f"  no {os.path.relpath(p, ROOT)} — nothing to mix")
        return {}
    return json.load(open(p, encoding="utf-8"))


def resolve(spec):
    """Turn the plan into (bed_path_or_None, [(seconds, sfx_path)]), dropping
    anything that isn't on disk and saying so."""
    bed = None
    if spec.get("music"):
        cand = os.path.join(LIB, "music", f"{spec['music']}.mp3")
        if os.path.exists(cand):
            bed = cand
        else:
            print(f"  ! bed '{spec['music']}' not on disk — run "
                  f"tools/audio/sfx.py --kit --music, or drop the file in "
                  f"studio/library/music/. Mixing without it.")
    cues = []
    for c in spec.get("sfx", []):
        cand = os.path.join(LIB, "sfx", f"{c['name']}.mp3")
        if os.path.exists(cand):
            cues.append((float(c["at"]), cand))
        else:
            print(f"  ! sfx '{c['name']}' not on disk — skipped "
                  f"(tools/audio/sfx.py --kit)")
    return bed, sorted(cues)


def mix(src, dst=None):
    if not os.path.exists(src):
        sys.exit(f"missing: {src}")
    dst = dst or os.path.join(os.path.dirname(src),
                              os.path.basename(src).replace("FINAL-", "MIXED-"))
    if os.path.abspath(dst) == os.path.abspath(src):
        sys.exit("refusing to overwrite the master in place")

    bed, cues = resolve(plan(src))
    if not bed and not cues:
        print("  nothing to mix — use the master as-is")
        return None

    total = duration(src)
    ins, parts, mixins = ["-i", src], [], []
    n_in = 1                 # count inputs explicitly: -stream_loop/-t on the bed
                             # mean "one -i pair per input" does not hold.

    # The voice is both a signal and the ducking control, so it gets split.
    if bed:
        parts.append("[0:a]asplit=2[vo0][ctl]")
        # The duck's control tap stays at the ORIGINAL level: threshold=0.03 is
        # calibrated against the raw voice, so gaining the control would change
        # how hard the bed ducks as a side effect of a level change.
        parts.append(f"[vo0]volume={VOICE_GAIN}[vo]")
        # -stream_loop makes the bed cover the whole runtime regardless of its
        # own length, so one 4-minute bed serves an 8-minute video.
        bed_dur = duration(bed)
        # acrossfade needs both sides longer than d, so a very short bed clamps it
        xf = min(LOOP_XFADE, bed_dur / 3) if bed_dur else LOOP_XFADE
        laps = math.ceil(total / max(bed_dur - xf, 1)) if bed_dur else 1
        if bed_dur and laps > 1:
            # -stream_loop splices head-to-tail with no crossfade, so the seam is
            # an audible discontinuity mid-phrase. It never showed before because
            # every SHORT cut (165s) was shorter than this 248s bed and looped
            # ZERO times; MEDIUM is the first tier that loops at all. Feed the
            # bed in `laps` times and acrossfade each joint instead.
            for lap in range(laps):
                ins += ["-i", bed]
            tag = f"[{n_in}:a]"
            for lap in range(1, laps):
                nxt = f"[bl{lap}]" if lap < laps - 1 else "[bedloop]"
                parts.append(f"{tag}[{n_in + lap}:a]"
                             f"acrossfade=d={xf:.3f}:c1=tri:c2=tri{nxt}")
                tag = nxt
            parts.append(f"[bedloop]atrim=0:{total:.3f}[bedcut]")
            parts.append(f"[bedcut]volume={BED_GAIN}[bed]")
            n_in += laps
        else:
            ins += ["-stream_loop", "-1", "-t", f"{total:.3f}", "-i", bed]
            parts.append(f"[{n_in}:a]volume={BED_GAIN}[bed]")
            n_in += 1
        parts.append(f"[bed][ctl]sidechaincompress={DUCK}[duck]")
        mixins = ["[vo]", "[duck]"]
    else:
        parts.append(f"[0:a]volume={VOICE_GAIN}[vo]")
        mixins = ["[vo]"]

    for n, (at, path) in enumerate(cues):
        ins += ["-i", path]
        ms = int(round(at * 1000))
        parts.append(f"[{n_in}:a]adelay={ms}|{ms},apad,volume={SFX_GAIN}[s{n}]")
        mixins.append(f"[s{n}]")
        n_in += 1

    # normalize=0: amix would otherwise divide every input by the input count,
    # quietly attenuating the voice by ~9 dB the moment SFX are added.
    parts.append(f"{''.join(mixins)}amix=inputs={len(mixins)}:"
                 f"normalize=0:dropout_transition=0[mixed]")

    cmd = (["ffmpeg", "-y", "-hide_banner", "-nostats"] + ins +
           ["-filter_complex", ";".join(parts),
            "-map", "0:v", "-map", "[mixed]", "-c:v", "copy",
            "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
            "-t", f"{total:.3f}", dst])
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0 or not os.path.exists(dst):
        sys.exit(f"mix failed\n{r.stderr[-2000:]}")

    got = duration(dst)
    print(f"  bed={os.path.basename(bed) if bed else 'none'}  "
          f"sfx={len(cues)}  {got:.2f}s -> {dst}")
    if abs(got - total) > 0.15:
        sys.exit(f"FAIL mixed runtime {got:.2f}s drifted from {total:.2f}s")
    return dst


def _selftest():
    """Build a fake master + bed + two SFX; assert the mix preserves runtime,
    adds energy, keeps the master untouched, and survives missing assets."""
    import shutil
    import tempfile
    global LIB
    real, d = LIB, tempfile.mkdtemp(prefix="mix-")
    try:
        LIB = os.path.join(d, "library")
        os.makedirs(os.path.join(LIB, "sfx"))
        os.makedirs(os.path.join(LIB, "music"))
        proj = os.path.join(d, "proj")
        os.makedirs(os.path.join(proj, "renders"))
        os.makedirs(os.path.join(proj, "assets"))
        src = os.path.join(proj, "renders", "FINAL-1080p-xx.mp4")

        def tone(path, secs, freq, gain="-20dB"):
            subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi",
                            "-i", f"sine=frequency={freq}:duration={secs}",
                            "-af", f"volume={gain}", "-q:a", "4", path], check=True)

        subprocess.run(["ffmpeg", "-y", "-v", "error",
                        "-f", "lavfi", "-i", "color=c=black:s=320x180:r=25:d=12",
                        "-f", "lavfi", "-i", "sine=frequency=200:duration=12",
                        "-af", "volume=-18dB", "-c:v", "libx264", "-preset", "ultrafast",
                        "-c:a", "aac", "-shortest", src], check=True)
        tone(os.path.join(LIB, "music", "bed-tension.mp3"), 5, 110)
        tone(os.path.join(LIB, "sfx", "stamp.mp3"), 1.2, 440, "-16dB")

        # a cue naming an SFX that was never generated must be skipped, not fatal
        json.dump({"music": "bed-tension",
                   "sfx": [{"at": 2.0, "name": "stamp"},
                           {"at": 6.0, "name": "stamp"},
                           {"at": 8.0, "name": "does-not-exist"}]},
                  open(os.path.join(proj, "assets", "audio.json"), "w"))

        before = open(src, "rb").read()
        out = mix(src)
        assert out and os.path.exists(out), "no mixed file"
        assert abs(duration(out) - duration(src)) < 0.15, "runtime drifted"
        assert open(src, "rb").read() == before, "master was modified"

        def rms(p):
            r = subprocess.run(["ffmpeg", "-hide_banner", "-i", p, "-af",
                                "volumedetect", "-f", "null", "-"],
                               capture_output=True, text=True)
            return float([l for l in r.stderr.splitlines()
                          if "mean_volume" in l][0].split(":")[1].strip(" dB"))
        assert rms(out) > rms(src), f"mix quieter than source ({rms(out)} vs {rms(src)})"

        # a 5s bed must have been looped to cover a 12s video
        assert duration(out) > 11.5, "bed did not extend to full runtime"

        # no audio.json at all → clean no-op, not a crash
        os.remove(os.path.join(proj, "assets", "audio.json"))
        assert mix(src, os.path.join(proj, "renders", "M2.mp4")) is None
        print(f"selftest OK  {rms(src):.1f} -> {rms(out):.1f} dB mean, "
              f"{duration(out):.2f}s preserved")
    finally:
        LIB = real
        shutil.rmtree(d, ignore_errors=True)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        _selftest()
    elif len(sys.argv) < 2:
        sys.exit(__doc__)
    else:
        mix(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
