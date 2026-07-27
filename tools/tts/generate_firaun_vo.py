#!/usr/bin/env python3
"""Generate the LINE-level Urdu VO for «فرعون کا انجام» + emit the edit timeline.

v2 (2026-07-22): the 56 paragraph-segments were re-lined into 307 single spoken
LINES. One clip per LINE (workflow Rule 0 at line granularity) — the timeline is
correct BY CONSTRUCTION: each line's start = sum of prior durations + prior gaps.
A short line = a short clip = one scene = one exact anchor. No silencedetect, no
drift, and a flubbed line re-generates alone.

    venv/bin/python tools/tts/generate_firaun_vo.py            # generate + table
    venv/bin/python tools/tts/generate_firaun_vo.py --table    # table only, no API
    venv/bin/python tools/tts/generate_firaun_vo.py --chapter 1   # just chapter 1's lines
    venv/bin/python tools/tts/generate_firaun_vo.py --only 16a.3 40.2
    venv/bin/python tools/tts/generate_firaun_vo.py --selftest

Resumable: a line whose .mp3 already exists is skipped unless --force. Re-rolling
one bad take = delete its file (or --only <id> --force) and re-run.
"""
import argparse
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import elevenlabs_tts as tts  # noqa: E402  — reuse its .env parser + API call

ROOT = tts.ROOT
SRC = os.path.join(ROOT, "vault/videos/video-hist-02-firaun/script-v2-devanagari-lines.md")
OUT = os.path.join(ROOT, "studio/videos/firaun-ka-anjaam/assets/audio")

VOICE = "st8o4LADtfxckX2PH08x"   # Vikram S — same as Pompeii, continuity by seed+voice
MODEL = "eleven_v3"
SEED = 42
SIMILARITY = 0.80

N_LINES = 307

# zone -> (stability, style, speed). Creator's zone map for this video (per-segment).
ZONES = {
    "default":  (0.40, 0.50, 0.95),
    "warm":     (0.45, 0.35, 0.95),
    "reverent": (0.50, 0.25, 0.88),
    "tension":  (0.35, 0.55, 1.00),
    "cool":     (0.42, 0.30, 0.95),
    "brisk":    (0.40, 0.50, 1.02),
}

# Zone is a property of the SEGMENT; a line inherits its parent segment's zone.
# Most specific wins (reverent beats warm for 16c; brisk beats cool for 47-48).
ZONE_OF = {}
for _ids, _z in [
    ("06 07 08 09 10 11 12 13 14 15 16 16a 16b 16d 17", "warm"),
    ("33 34 35 36 37 38 39", "tension"),
    ("43 44 45 46 49 50", "cool"),
    ("47 48", "brisk"),
    ("16c 40 51 52", "reverent"),          # last => overrides warm for 16c
]:
    ZONE_OF.update({i: _z for i in _ids.split()})

# --- GAP MODEL (v2) --------------------------------------------------------
# Gaps are added at ASSEMBLY, never baked into the TTS — clips stay reusable.
# Lines flow with a short breath INSIDE a paragraph; the deliberate pauses land
# only at the marked beats / chapter ends. Keyed by SEGMENT (attaches to the
# segment's LAST line).  Everything else: intra-segment 0.20s, seg-boundary 0.40s.
GAP_INTRA = 0.20        # between lines of the same segment
GAP_SEG   = 0.40        # between two segments (default)
SPECIAL_END = {         # after the LAST line of these segments (beats + chapter marks)
    "05": 1.0, "10": 1.0, "15": 1.0, "17": 1.0, "23": 1.0,
    "32": 1.0, "35": 1.0, "42": 1.0, "46": 1.0, "50": 1.0,
    "20-21": 1.0,   # pattern interrupt — 1 beat total silence (DESIGN §Motion)
    "37": 3.0,      # the collapse: full sound, then 3s of nothing (DESIGN §Sound)
    "39": 1.5,      # «اب؟» hard cut to black
    "48": 1.0,      # myth stamps land
    "52": 2.0,      # hold the final case before the CTA
}

BLOCK_RE = re.compile(r"^\*\*([0-9][0-9a-z-]*\.[0-9]+)\*\*\s+—\s+(.+)$", re.M)
CITE_RE = re.compile(r"\s*\(\s*\d+\s*:\s*[\d\s,–-]+\)")   # (28:4) — on-screen chips, never spoken


def parent(line_id):
    return line_id.rsplit(".", 1)[0]


def clean(text):
    """Strip markup-for-humans; KEEP v3 `[audio tags]` — v3 consumes them as directives."""
    text = CITE_RE.sub("", text)      # cite refs are chips (rule 4), not VO
    text = text.replace("`", "")      # audio tags are backticked in the .md for readability
    text = text.replace("**", "")     # bold emphasis is Latin-only — useless in Devanagari
    return re.sub(r"\s+", " ", text).strip()


def blocks():
    with open(SRC, encoding="utf-8") as fh:
        found = BLOCK_RE.findall(fh.read())
    if len(found) != N_LINES:
        sys.exit(f"ERROR: expected {N_LINES} lines in {SRC}, found {len(found)}. Fix the source.")
    return [(sid, clean(txt)) for sid, txt in found]


def gap_after(items, k):
    """Gap after line index k: special-beat > seg-boundary > intra-segment breath."""
    sid = items[k][0]
    last_of_seg = (k + 1 == len(items)) or (parent(items[k + 1][0]) != parent(sid))
    if not last_of_seg:
        return GAP_INTRA
    return SPECIAL_END.get(parent(sid), GAP_SEG)


def duration(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", path],
        capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


def fmt(sec):
    return f"{int(sec // 60)}:{sec % 60:05.2f}"


def table(items):
    """line -> duration -> cumulative start. THIS is the edit timeline."""
    rows, t = [], 0.0
    for k, (sid, _) in enumerate(items):
        path = os.path.join(OUT, f"seg-{sid}.mp3")
        g = gap_after(items, k)
        if not os.path.exists(path):
            rows.append((sid, None, t, g))
            continue
        d = duration(path)
        rows.append((sid, d, t, g))
        t += d + g
    return rows, t


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--table", action="store_true", help="print the timeline only — no API calls")
    p.add_argument("--only", nargs="+", metavar="ID", help="generate just these line IDs")
    p.add_argument("--chapter", type=int, help="generate just one chapter's lines (1..10)")
    p.add_argument("--force", action="store_true", help="regenerate even if the .mp3 exists")
    p.add_argument("--selftest", action="store_true", help="offline checks — no API, no network")
    args = p.parse_args(argv)

    if args.selftest:
        return selftest()

    items = blocks()

    # chapter -> segment ids (must match build.py CHAPTERS)
    CH = {1:"01 02 03 04 05", 2:"06 07 08 09 10", 3:"11 12 13 14 15",
          4:"16 16a 16b 16c 16d 17", 5:"18 19 20-21 22 23",
          6:"24 25 26 27 28 29 30 31 32", 7:"33 34 35 36 37",
          8:"38 39 40 41 42", 9:"43 44 45 46 47 48", 10:"49 50 51 52 53"}
    ch_segs = set(CH[args.chapter].split()) if args.chapter else None

    if not args.table:
        tts.load_env()
        key = tts.api_key()
        todo = []
        for k, (sid, text) in enumerate(items):
            if args.only and sid not in args.only:
                continue
            if ch_segs and parent(sid) not in ch_segs:
                continue
            todo.append((k, sid, text))
        for n, (k, sid, text) in enumerate(todo, 1):
            path = os.path.join(OUT, f"seg-{sid}.mp3")
            if os.path.exists(path) and not args.force:
                print(f"[{n:>3}/{len(todo)}] seg-{sid}: exists, skipping")
                continue
            z = ZONE_OF.get(parent(sid), "default")
            stab, style, speed = ZONES[z]
            # NOTE: eleven_v3 does NOT support previous_text/next_text stitching
            # (400 unsupported_model). Seed+voice carry continuity instead.
            print(f"[{n:>3}/{len(todo)}] seg-{sid} ({z:8}) "
                  f"stab={stab} style={style} speed={speed} · {len(text)} chars")
            tts.synthesize(key, VOICE, text, path, MODEL, stab, SIMILARITY,
                           style=style, speed=speed, seed=SEED)

    rows, total = table(items)
    missing = [r[0] for r in rows if r[1] is None]
    print(f"\n| line | zone | dur | start | gap after |\n|---|---|---|---|---|")
    for sid, d, start, g in rows:
        z = ZONE_OF.get(parent(sid), "default")
        print(f"| {sid} | {z} | {fmt(d) if d else '—'} | {fmt(start)} | {g} |")
    print(f"\nTOTAL RUNTIME: {fmt(total)}  ({total:.1f}s)   target 21:30–24:00")
    if missing:
        print(f"MISSING {len(missing)} clips: {' '.join(missing)}")
    return 0


def selftest():
    """Offline: the things that silently corrupt the 307 clips if they break."""
    items = blocks()
    assert len(items) == N_LINES, len(items)
    ids = [s for s, _ in items]
    assert len(set(ids)) == N_LINES, "duplicate line IDs"
    assert ids[0] == "01.1" and ids[-1] == "53.5", ids[:1] + ids[-1:]
    assert "16a.1" in ids and "20-21.1" in ids, "sub-segment lines lost"

    # every line belongs to a known segment
    segs = {parent(s) for s in ids}
    assert len(segs) == 56, f"{len(segs)} segments, expected 56"

    # cite refs must never reach the engine (creator rule 4: chips, not VO)
    assert clean("बात है (28:4) और") == "बात है और"
    for sid, text in items:
        assert not CITE_RE.search(text), f"cite ref survived in {sid}: {text[:60]}"

    # v3 audio tags must survive (unbackticked); markup must not
    assert clean("`[pause]` ठीक") == "[pause] ठीक"
    assert "`" not in "".join(t for _, t in items)
    assert "**" not in "".join(t for _, t in items)

    # NO ARABIC-ONLY artifacts in VO (diagnostics that only appear if Arabic was pasted)
    for sid, text in items:
        for ch in "ةﷲﷺ۝۞":
            assert ch not in text, f"Arabic artifact {ch!r} in {sid}"

    # zones + gap model
    for z in ZONE_OF.values():
        assert z in ZONES, z
    assert ZONE_OF["16c"] == "reverent", "16c must override warm — the kalam beat"
    assert ZONE_OF["47"] == "brisk", "47 must override cool — the myth stamps"
    # last line of seg 37 gets the 3s collapse; a mid-seg line gets the breath
    i37_last = max(k for k, (s, _) in enumerate(items) if parent(s) == "37")
    assert gap_after(items, i37_last) == 3.0, "seg 37 collapse pause lost"
    i16a = [k for k, (s, _) in enumerate(items) if parent(s) == "16a"]
    assert gap_after(items, i16a[0]) == GAP_INTRA, "intra-segment breath wrong"
    assert gap_after(items, i16a[-1]) == GAP_SEG, "16a is not a special beat — should be seg-boundary"

    print(f"selftest OK — {len(items)} lines, {len(segs)} segments, "
          f"{sum(len(t) for _, t in items)} chars")
    return 0


if __name__ == "__main__":
    sys.exit(main())
