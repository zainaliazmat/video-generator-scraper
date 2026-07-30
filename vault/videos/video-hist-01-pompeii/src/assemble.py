#!/usr/bin/env python3
"""Assemble the final film: concat the 10 chapter renders (stream-copy) and mix
the background-music bed over them. Music plan (creator-approved sources,
Incompetech CC-BY 4.0 — credit line required in the YT description):
  CH1-4  Teller of the Tales →(4s crossfade)→ Virtutes Instrumenti
  CH5-7  Long Note Two  (ducked to 0 during the pre-dawn hush, seg 41+42)
  CH8-9  Promises to Keep
  CH10   no music (Islamic coda — bare VO over the fading drone)
Re-run after any chapter re-render:  python3 assemble.py
"""
import os, re, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
CH = [os.path.join(HERE, f"pompeii-ch{n}-fixed-timeline-1080p.mp4") for n in range(1, 11)]
MUS = os.path.join(HERE, "assets", "audio", "music-candidates")
OUT = os.path.join(HERE, "pompeii-ka-akhri-din-FINAL-1080p.mp4")
TARGET = -33.0       # bed mean level, dB (VO means ~-18 → bed ~15 dB under)
HUSH = (18.6, 31.5)  # pre-dawn silence, seconds local to CH7 (seg 41+42 span)

def dur(p):
    return float(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", p]).strip())

def mean_db(p):
    err = subprocess.run(["ffmpeg", "-hide_banner", "-i", p, "-vn",
                          "-af", "volumedetect", "-f", "null", "/dev/null"],
                         capture_output=True, text=True).stderr
    return float(re.search(r"mean_volume: (-?[\d.]+) dB", err).group(1))

def gain(p):
    g = round(TARGET - mean_db(p), 1)     # per-track dB gain to hit TARGET mean
    print(f"  gain {g:+.1f} dB  {os.path.basename(p)}")
    return g

D = [dur(p) for p in CH]
start = [round(sum(D[:i]), 3) for i in range(10)]           # chapter starts, global s
LA = start[4]                                               # slot A = CH1-4
B1L = round(start[6] + HUSH[0] - start[4], 3)               # music before the hush
B2S = round(start[6] + HUSH[1] - start[4], 3)               # file pos after the hush
B2L = round(start[7] - (start[6] + HUSH[1]), 3)             # music after the hush
LC = round(start[9] - start[7], 3)                          # slot C = CH8-9
ms = lambda t: int(round(t * 1000))

# 1. concat (stream copy — no re-encode of video)
lst = os.path.join(HERE, "concat-list.txt")
with open(lst, "w") as f:
    f.writelines(f"file '{p}'\n" for p in CH)
joined = os.path.join(HERE, "pompeii-joined-nomusic.mp4")
subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0",
                "-i", lst, "-c", "copy", joined], check=True)

# 2. music bed + mix (video stream copied straight through). Each track is
# gain-staged from its own measured mean loudness so the bed sits at TARGET.
T1, T2 = os.path.join(MUS, "Teller of the Tales.mp3"), os.path.join(MUS, "Virtutes Instrumenti.mp3")
T3, T4 = os.path.join(MUS, "Long Note Two.mp3"), os.path.join(MUS, "Promises to Keep.mp3")
g1, g2, g3, g4 = gain(T1), gain(T2), gain(T3), gain(T4)
bedwav = os.path.join(HERE, "bed-check.wav")
fc = (
    f"[1:a]volume={g1}dB[a1];[2:a]volume={g2}dB[a2];"
    f"[a1][a2]acrossfade=d=4[a0];"
    f"[a0]atrim=0:{LA},aresample=48000,afade=t=in:d=2,afade=t=out:st={LA-3}:d=3[A];"
    f"[3:a]volume={g3}dB,asplit[b1][b2];"
    f"[b1]atrim=0:{B1L},aresample=48000,afade=t=in:d=3,afade=t=out:st={B1L-1}:d=1,"
    f"adelay={ms(start[4])}|{ms(start[4])}[B1];"
    f"[b2]atrim={B2S}:{B2S+B2L},asetpts=PTS-STARTPTS,aresample=48000,afade=t=in:d=1,"
    f"afade=t=out:st={B2L-3}:d=3,adelay={ms(start[6]+HUSH[1])}|{ms(start[6]+HUSH[1])}[B2];"
    f"[4:a]volume={g4}dB[c0];"
    f"[c0]atrim=0:{LC},aresample=48000,afade=t=in:d=3,afade=t=out:st={LC-5}:d=5,"
    f"adelay={ms(start[7])}|{ms(start[7])}[C];"
    f"[A][B1][B2][C]amix=inputs=4:duration=longest:normalize=0,asplit[bedm][bedv];"
    f"[0:a][bedm]amix=inputs=2:duration=first:normalize=0[aout]"
)
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", joined,
                "-i", T1, "-i", T2, "-i", T3, "-i", T4,
                "-filter_complex", fc, "-map", "0:v", "-map", "[aout]",
                "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                "-movflags", "+faststart", OUT,
                "-map", "[bedv]", bedwav], check=True)
print(f"chapters: {[round(d,1) for d in D]}")
print(f"final: {OUT}  ·  {dur(OUT):.1f}s")
