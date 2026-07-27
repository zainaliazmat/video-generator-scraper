#!/usr/bin/env python3
"""
Build «فرعون کا انجام» -> index.html (HyperFrames), CHAPTER BY CHAPTER, PER LINE.

    python3 build.py --chapter 1     # emits index.html for chapter 1 only, clock from 0

v2 (2026-07-22): the 56 paragraph-segments were re-lined into 307 single spoken
LINES. VO is now ONE clip per LINE (assets/audio/seg-<lineid>.mp3, e.g. 07.4,
16a.3, 20-21.7). So the comp is ONE LINE = ONE CLIP = ONE SCENE = ONE EXACT SPAN.
No weight-splitting — that hand-guessed share is exactly what drifted the images
out of sync, and it is gone.

Timing is BY CONSTRUCTION: each line's visual span = probe(its clip) + the gap
that follows it, and the gap model is copied VERBATIM from
tools/tts/generate_firaun_vo.py (GAP_INTRA 0.20, GAP_SEG 0.40, SPECIAL_END) so
the composition reproduces the VO timeline to the centisecond.

The per-line scene + citation both come from the canonical LINE master
vault/videos/video-hist-02-firaun/script-v2-nastaliq-lines.md — every line carries
its own `[scene: Pxx]` / `[hold Pxx]` / `[card …]` cue and its inline `(NN:NN)`
cite. (Kept in the repo, so build.py has no /tmp dependency.)

Missing stills (P13b, P20c, P20d, P22a, P22b, P38a, P41a, P50a) do NOT crash the
build — the previous resolved image is held and the line is logged.

Determinism contract (DESIGN §): ONE paused gsap.timeline on
window.__timelines["main"], only x/y/scale/opacity/color animated, no Date.now,
no Math.random, no network. gsap is vendored at assets/gsap.min.js.
"""
import os, re, sys, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
IMG = os.path.join(HERE, "assets", "images")
AUD = os.path.join(HERE, "assets", "audio")
MASTER = os.path.join(ROOT, "vault/videos/video-hist-02-firaun/script-v2-nastaliq-lines.md")

# ---------------------------------------------------------------------------
# CHAPTERS — segment grouping, unchanged (matches generate_firaun_vo.py CH map).
# ---------------------------------------------------------------------------
CHAPTERS = {
 1: "01 02 03 04 05", 2: "06 07 08 09 10", 3: "11 12 13 14 15",
 4: "16 16a 16b 16c 16d 17", 5: "18 19 20-21 22 23",
 6: "24 25 26 27 28 29 30 31 32", 7: "33 34 35 36 37",
 8: "38 39 40 41 42", 9: "43 44 45 46 47 48", 10: "49 50 51 52 53",
}

# ---------------------------------------------------------------------------
# GAP MODEL — copied VERBATIM from tools/tts/generate_firaun_vo.py so the comp
# clock == the VO clock. The gap after a line is: special-beat > seg-boundary >
# intra-segment breath.
# ---------------------------------------------------------------------------
GAP_INTRA = 0.20
GAP_SEG   = 0.40
SPECIAL_END = {
    "05": 1.0, "10": 1.0, "15": 1.0, "17": 1.0, "23": 1.0,
    "32": 1.0, "35": 1.0, "42": 1.0, "46": 1.0, "50": 1.0,
    "20-21": 1.0, "37": 3.0, "39": 1.5, "48": 1.0, "52": 2.0,
}
def parent(line_id): return line_id.rsplit(".", 1)[0]
def gap_after(items, k):
    sid = items[k][0]
    last_of_seg = (k + 1 == len(items)) or (parent(items[k + 1][0]) != parent(sid))
    if not last_of_seg:
        return GAP_INTRA
    return SPECIAL_END.get(parent(sid), GAP_SEG)

# ---------------------------------------------------------------------------
# Per-SEGMENT era grade (carried from build-v1). New chapters keep the story's
# ancient bed; ch9 slides sepia -> B&W newsreel; museum bookends the film.
# ---------------------------------------------------------------------------
ERA = {}
for _s in "01 02 03 04 05".split(): ERA[_s] = "museum"
for _s in ("06 07 08 09 10 11 12 13 14 15 16 16a 16b 16c 16d 17 18 19 20-21 22 23 "
           "24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41").split(): ERA[_s] = "ancient"
for _s in "42 43 44 45".split(): ERA[_s] = "sepia"
ERA["46"] = "bw1976"
for _s in "47 48 49 50 51 52 53".split(): ERA[_s] = "museum"
# per-LINE era override: the 1976 era-flash on old seg 03's last beat.
LINE_ERA = {"03.3": "bw1976", "03.4": "bw1976", "03.5": "bw1976"}

REVERENT_SEGS = {"16c", "40", "51", "52"}     # verse/kalam lines -> locked, no punch

# surah number -> Nastaliq name, for the corner cite chip (rule 4).
SURAH = {28: "القصص", 79: "النازعات", 10: "یونس", 7: "الاعراف", 20: "طٰہٰ",
         26: "الشعراء", 44: "الدخان", 17: "بنی اسرائیل", 4: "النساء"}

# a map cue names cards by their scene token; resolve token -> a built CARDS key.
CARD_ALIAS = {"P04": "C-04", "P05a": "C-05a", "P05b": "C-05b", "P24": "C-24",
              "P47": "C-47", "P48": "C-48a", "P40": "C-04",   # 40 re-uses the 10:92 parchment
              "P39": None, "P30c": None}   # P30c is a real still; P39 has no built card
CARD_BY_LINE = {"48.2": "C-48b"}           # 48.1/48.2 share token P48 — split by line

# per-LINE full-parchment overlay quote (carried from build-v1's ov= placements).
OV_BY_LINE = {"16a.6": "C-16a", "16c.3": "C-16c", "16d.8": "C-16d",
              "17.2": "C-17a", "17.6": "C-17b", "30.4": "C-30", "35.6": "C-35",
              "44.1": "C-44", "45.1": "C-45"}

# per-LINE transition overrides (the CUT/BLK beats from build-v1).
LINE_TRANS = {"03.3": "CUT", "10.3": "BLK", "37.6": "CUT", "39.1": "BLK", "46.1": "CUT"}

# HOOK RETENTION PASS (2026-07-23, hook-critique): the hook cards used to REPLACE the
# image and float on flat cream/black for ~40s (59% of the cold open). Now every card
# beat RIDES a moving still and renders as an .ov overlay (the proven verse-card path).
#   line -> (background still token, overlay card key | None)
# None = no card, just the still + the era ribbon (05.4 goat). If a bg still isn't
# generated yet (e.g. P05c goat), the build holds the previous real still and logs it.
CARD_BG = {
    "04.1": ("P02d", "C-04"), "04.2": ("P02d", "C-04"),   # CLEAR mummy face under the Quran question
    "04.3": ("P03d", "C-04"), "04.4": ("P03d", "C-04"),   # cut to France 1976 under "...who drowned"
    "05.1": ("P37c", "C-05a"), "05.2": ("P37c", "C-05a"), # dark aftermath water: "the morning after"
    "05.3": ("P37c", "C-05a"),
    "05.4": ("P05c", None), "05.5": ("P05c", None),       # ⭐ goat under the best hook; ribbon = era strip
    "05.6": ("P05d", None),                               # cut to the dark shaft mouth -> blooms into seg 06 dawn
}

# era-ribbon jumps + plague tally (first line of each plague segment).
RIB_BY_LINE = {"05.4": "ancient", "43.1": "1881", "46.1": "1976", "42.3": None}
TALLY_BY_LINE = {"25.1": 1, "26.1": 2, "27.1": 3, "28.1": 4, "29.1": 5, "30.1": 6}

# per-LINE still override (win over the master cue). 2026-07-23: the mummy FACE must be
# CLEARLY VISIBLE (creator) — swap the withheld-silhouette P02c for the clear museum face
# P02d on the two lines that name the recognisable face + hold it through "3000 years".
SCENE_OVERRIDE = {"02.3": "P02d", "02.4": "P02d",
    # ch3 long-dwell breakers (2026-07-23) — see audit-ch3-2026-07-23.md mapping table
    "11.4": "P11c", "11.5": "P11d",              # seg 11 open: pitch-seal → baby-in-chest
    "13.3": "P13c", "13.5": "P13d",              # seg 13 irony: looming palace → wet-lid macro
    "15.6": "P15e", "15.7": "P15c", "15.8": "P15d"}   # seg 15 reunion: watchers → calm macro → poor hands

# cue-less master lines (their scene lives only in the reline map) -> bake it in.
FALLBACK_SCENE = {
    "16.8": "P16b2", "16b.5": "P16f2", "16d.7": "P16k1", "37.6": "P37c",
    "50.1": "P50a", "50.2": "hold P50a", "50.3": "hold P50a",
    "50.4": "hold P50a", "50.7": "P50a", "50.8": "hold P50a",
}

# ---------------------------------------------------------------------------
# Known image defects (image-audit.md) handled IN-COMP — carried verbatim.
#   crop  : (scale, dx%, dy%) — kills baked-in bars BEFORE the Ken Burns move.
#   tight : short headroom — cap the punch at 1.08, not 1.13.
# ---------------------------------------------------------------------------
CROP = {
    "P30a": (1.048, 0.0,  0.0),
    "P35b": (1.180, 0.0,  5.47),
    "P11b": (1.255, -3.56, -5.60),
    "P37b": (1.193, 3.78, 0.0),
}
TIGHT = {"P45a", "P50c", "P16f3", "P03d"}

# ---------------------------------------------------------------------------
# CARDS — verbatim from build-v1. kind: scene = full parchment · dark = full dark
# · ov = over the photo. `u(...)` marks Urdu that gets word-by-word kinetic type.
# ---------------------------------------------------------------------------
def u(text, cls="qr"):
    words = "".join(f'<span class="kw">{w}&nbsp;</span>' for w in text.split(" "))
    return f'<p class="ur {cls} rl">{words}</p>'

CARDS = {
 "C-04": ("ov",
    '<div class="parch">'
    + u("آج ہم تیرا بدن بچا لیں گے،", "q1")
    + u("تاکہ تُو اپنے بعد والوں کے لیے نشانی بنے۔", "q1")
    + '<p class="cite rl">یونس 10:92</p></div>'),
 "C-05a": ("ov",     # hook retention pass: rides a still now -> parch panel so it reads over a photo
    '<div class="parch">' + u("معجزہ نہیں۔", "big") + u("اُس سے اگلی صبح۔", "big") + '</div>'),
 "C-05b": ("dark",
    '<div class="erafall">'
    '<p class="era-n rl">2026</p><p class="era-n era-mid rl">1881</p>'
    + u("‏3000 سال پہلے", "era-u") + '</div>'),
 "C-16a": ("ov",
    '<div class="parch parch-ov">'
    + u("میرے رب، جو بھلائی بھی تُو مجھ پر اتار دے، میں اس کا محتاج ہوں۔", "q1")
    + '<p class="cite rl">القصص 28:24</p></div>'),
 "C-16c": ("ov",
    '<div class="parch parch-ov">'
    + u("بیشک میں ہی اللہ ہوں، میرے سوا کوئی معبود نہیں —", "q1")
    + u("پس میری عبادت کر، اور میری یاد کے لیے نماز قائم کر۔", "q1")
    + '<p class="cite rl">طٰہٰ 20:14</p></div>'),
 "C-16d": ("ov",
    '<div class="parch parch-ov">'
    + u("فرعون کے پاس جا — اس نے سرکشی کی ہے۔", "q1")
    + '<p class="cite rl">طٰہٰ 20:24</p></div>'),
 "C-17a": ("scene",
    u("میرے رب، میرا سینہ کھول دے،", "q1")
    + u("میرا کام آسان کر دے،", "q1")
    + u("اور میری زبان کی گرہ کھول دے۔", "q1")
    + '<p class="cite rl">طٰہٰ 20:25-28</p>'),
 "C-17b": ("scene",
    u("ڈرو نہیں۔", "big")
    + u("میں تم دونوں کے ساتھ ہوں —", "q1")
    + u("میں سنتا ہوں اور دیکھتا ہوں۔", "q1")
    + '<p class="cite rl">طٰہٰ 20:46</p>'),
 "C-24": ("scene",
    '<div class="tallycard">'
    + u("‏9 نشانیاں", "big")
    + u("اور بےشک ہم نے موسیٰ کو 9 کھلی نشانیاں دیں۔", "q1")
    + '<div class="tally-row">' + "".join(f'<span class="tk tk{i}"></span>' for i in range(1, 10))
    + '</div><p class="cite rl">بنی اسرائیل 17:101</p></div>'),
 "C-30": ("ov",
    '<div class="parch parch-ov">'
    + u("طوفان · ٹڈیاں · جوئیں · مینڈک · خون", "q1")
    + '<p class="cite rl">الاعراف 7:133</p></div>'),
 "C-35": ("ov",
    '<div class="parch parch-ov">'
    + u("ہرگز نہیں۔ میرا رب میرے ساتھ ہے۔", "q1")
    + u("وہ مجھے راستہ دکھائے گا۔", "q1")
    + '<p class="cite rl">الشعراء 26:62</p></div>'),
 "C-44": ("ov",
    '<div class="parch parch-ov parch-sm">'
    + u("‏TT320 — ‏50 سے زیادہ شاہی ممیاں", "q1") + '</div>'),
 "C-45": ("ov",
    '<div class="namecard"><p class="name-en rl">RAMESSES II</p>'
    + u("رعمسیس دوم", "name-ur") + '</div>'),
 "C-47": ("scene",
    '<div class="myth"><p class="myth-n rl">1</p>'
    + u("«ممی کو پاسپورٹ جاری ہوا۔»", "myth-q")
    + '<p class="stamp rl">جھوٹ</p>'
    + u("ایسا کوئی پاسپورٹ نہیں تھا — فرانسیسی کاغذات کو «passeport» کہہ دیا گیا۔", "myth-f")
    + '<p class="cite rl">AFP Fact Check</p></div>'),
 "C-48a": ("scene",
    '<div class="myth"><p class="myth-n rl">2</p>'
    + u("«بدن میں سمندری نمک ملا — ڈوبنے کا ثبوت۔»", "myth-q")
    + '<p class="stamp stamp-amber rl">گمراہ کن</p>'
    + u("نیٹرون خود نمک سے بھرا ہوتا ہے — نمک ہر ممی پر ملتا ہے۔", "myth-f")
    + '<p class="cite rl">J. Plastination</p></div>'),
 "C-48b": ("scene",
    '<div class="myth"><p class="myth-n rl">3</p>'
    + u("«بدن پر کوئی حنوط نہیں — خالص معجزہ۔»", "myth-q")
    + '<p class="stamp rl">جھوٹ</p>'
    + u("‏2023 کی سی ٹی تحقیق: بدن مکمل حنوط شدہ ہے۔", "myth-f")
    + '<p class="cite rl">J. Arch. Science 2023</p></div>'),
}

RIBBON_KEYS = ["ancient", "1881", "1976", "today"]
RIBBON_LBL = {"ancient": "‏3000 سال پہلے", "1881": "1881", "1976": "1976", "today": "آج"}

# ---------------------------------------------------------------------------
# Parse the LINE master: (lineid, spoken, cue) in order.
# ---------------------------------------------------------------------------
BLOCK_RE = re.compile(r"^\*\*([0-9][0-9a-z-]*\.[0-9]+)\*\*\s+—\s+(.+)$")
CITE_RE = re.compile(r"\(\s*(\d{1,3}:\s*[\d\s,–-]+?)\s*\)")
TOK_RE = re.compile(r"P\d+[a-z]?\d*(?:-alt\d+)?")

def parse_master():
    out, cur = [], None
    with open(MASTER, encoding="utf-8") as fh:
        for raw in fh:
            s = raw.strip()
            m = BLOCK_RE.match(s)
            if m:
                if cur: out.append(cur)
                cur = [m.group(1), m.group(2), ""]
            elif cur is not None and not cur[2] and s.startswith("`["):
                cur[2] = s.strip("`")
    if cur: out.append(cur)
    return out

def cite_of(spoken):
    m = CITE_RE.search(spoken)
    if not m: return None
    ref = re.sub(r"\s+", "", m.group(1))
    surah = SURAH.get(int(ref.split(":")[0]))
    return f"{surah} {ref}" if surah else ref

# ---------------------------------------------------------------------------
CHAPTER = int(sys.argv[sys.argv.index("--chapter") + 1]) if "--chapter" in sys.argv else None
if CHAPTER not in CHAPTERS:
    raise SystemExit(f"usage: build.py --chapter N   (1..{max(CHAPTERS)})")
CH_SEGS = set(CHAPTERS[CHAPTER].split())

def resolve_opt(base):
    if not base: return None
    for ext in (".jpeg", ".jpg", ".png"):
        if os.path.exists(os.path.join(IMG, base + ext)):
            return "assets/images/" + base + ext
    return None

def probe(path):
    return float(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", path]).strip())

OVERLAP = {"XD": 1.0}          # dissolves overlap the outgoing scene; CUT/BLK/NONE do not
NEWCYCLE = ["PI", "KB", "PB", "H"]

# --- pick this chapter's lines, in order --------------------------------------
LINES = [(lid, spoken, cue) for lid, spoken, cue in parse_master() if parent(lid) in CH_SEGS]
if not LINES:
    raise SystemExit(f"no lines for chapter {CHAPTER}")

# --- lay the chapter out on its own clock, one scene per line -----------------
scenes, audio, held, t, newimg = [], [], [], 0.0, 0
last_ref = "assets/images/P01a.jpeg"     # safety hold target for a leading miss
last_tok = "P01a"                        # last REAL still token (for card-bg hold fallback)

for k, (lid, spoken, cue) in enumerate(LINES):
    clip = probe(os.path.join(AUD, f"seg-{lid}.mp3"))
    g = gap_after(LINES, k)
    span = clip + g
    audio.append((lid, round(t, 3), round(clip, 3)))

    cue = cue or FALLBACK_SCENE.get(lid, "")
    is_hold = bool(re.search(r"\bhold\b", cue, re.I))
    mt = TOK_RE.search(cue)
    token = SCENE_OVERRIDE.get(lid) or (mt.group(0) if mt else None)
    card_key = CARD_BY_LINE.get(lid) or (CARD_ALIAS.get(token) if token else None)
    img = resolve_opt(token)

    ov = OV_BY_LINE.get(lid)
    is_card = False
    bg = CARD_BG.get(lid)
    if bg:                                     # card RIDES a still (overlay, never flat) — hook retention pass
        bg_tok, ov_key = bg
        if ov_key: ov = ov_key
        if resolve_opt(bg_tok):
            ref, last_tok = bg_tok, bg_tok
            last_ref = "assets/images/" + os.path.basename(resolve_opt(bg_tok))
        else:                                  # bg still not generated yet -> hold previous real still, log it
            ref, is_hold = last_tok, True
            held.append(f"HELD {lid} (card-bg {bg_tok} not generated — see image-prompts.txt)")
    elif img is None and card_key and card_key in CARDS:
        is_card, ref = True, "C:" + card_key
        ov = None                              # a full card carries its own cite
    elif img is None:
        ref, is_hold = last_ref, True          # missing still -> hold the previous
        held.append(f"HELD {lid} (missing {token or '?'})")
    else:
        ref, last_tok = token, token
        last_ref = "assets/images/" + os.path.basename(resolve_opt(token))

    # motion: cards + verse lines lock; holds drift gently; new stills cycle.
    if is_card or parent(lid) in REVERENT_SEGS:
        motion = "LK"
    elif is_hold:
        motion = "H"
    else:
        motion = NEWCYCLE[newimg % 4]; newimg += 1

    era = LINE_ERA.get(lid, ERA.get(parent(lid), "ancient"))
    trans = LINE_TRANS.get(lid, "XD")
    chip = None if ov else cite_of(spoken)     # overlay quote already shows the cite

    scenes.append(dict(
        i=k, id=f"s{k:02d}", lineid=lid, ref=ref, seg=parent(lid),
        start=round(t, 3), span=span, motion=motion, trans=trans, era=era,
        ov=ov, chip=chip, tally=TALLY_BY_LINE.get(lid), ribbon=RIB_BY_LINE.get(lid),
        is_card=is_card, is_hold=is_hold, first_card=(is_card and not is_hold),
        ov_hold=(bg is not None and is_hold)))     # held card-bg overlay: show composed, don't re-punch
    t += span

# ---- FLICKER FIX (2026-07-23) — same still across lines = ONE continuous shot ----
# Re-reading an image as a fresh cross-dissolved scene dips/flickers (two copies of the
# same picture at mismatched zoom, blended = luminance dip + scale jump). Instead: cut
# INVISIBLY between same-image scenes and run ONE continuous zoom across the whole run;
# only a REAL image change gets a dissolve.
def _imgkey(sc): return None if sc["is_card"] else sc["ref"]   # flat cards never group
_gid = 0
for k, sc in enumerate(scenes):
    if k > 0 and _imgkey(sc) is not None and _imgkey(sc) == _imgkey(scenes[k - 1]):
        sc["grp"], sc["grp_first"] = scenes[k - 1]["grp"], False
        if sc["trans"] != "BLK":                # keep hard black beats; else invisible cut
            sc["trans"] = "CUT"
    else:
        _gid += 1
        sc["grp"], sc["grp_first"] = _gid, True

# dur includes the 1s overlap the NEXT scene dissolves over (only XD overlaps; CUT does not)
for k, sc in enumerate(scenes):
    nxt = scenes[k + 1]["trans"] if k + 1 < len(scenes) else None
    sc["dur"] = round(sc["span"] + OVERLAP.get(nxt, 0.0), 3)

TOTAL = round(t, 3)
scenes[0]["trans"] = "NONE"                     # standalone chapter: hard in

# per-group continuous zoom: one slow linear in/out across the whole same-image run, so
# the invisible cuts join into a single smooth move (scale matches at every cut). Single
# scenes keep their own eased Ken Burns (no flicker risk — nothing to dissolve into).
_byg = {}
for sc in scenes: _byg.setdefault(sc["grp"], []).append(sc)
for gi, grp in enumerate(sorted(_byg.values(), key=lambda g: g[0]["i"])):
    gs = grp[0]["start"]; ge = grp[-1]["start"] + grp[-1]["dur"]; D = max(ge - gs, 1e-6)
    Z = 0.06 if any(sc["ref"] in TIGHT for sc in grp) else 0.10   # zoom span (tight imgs = less)
    zin = (gi % 2 == 0)                                           # alternate zoom in / out
    for sc in grp:
        r0 = (sc["start"] - gs) / D; r1 = (sc["start"] + sc["dur"] - gs) / D
        sc["z0"] = round(1.0 + Z * (r0 if zin else 1 - r0), 4)
        sc["z1"] = round(1.0 + Z * (r1 if zin else 1 - r1), 4)
        sc["multi"] = len(grp) > 1

# ---------------------------------------------------------------------------
# HTML
# ---------------------------------------------------------------------------
def section(sc):
    sid = sc["id"]
    if sc["ref"].startswith("C:"):
        kind, inner = CARDS[sc["ref"][2:]]
        cls = {"scene": "card", "dark": "card card-dark", "ov": "card"}[kind]
        body = (f'<div class="scene-inner" id="{sid}-inner">'
                f'<div class="{cls}" id="{sid}-card">{inner}</div></div>')
    else:
        cr = CROP.get(sc["ref"])
        st = ""
        if cr:
            s, dx, dy = cr
            st = f' style="transform:scale({s}) translate({dx}%,{dy}%)"'
        body = (f'<div class="scene-inner" id="{sid}-inner">'
                f'<div class="photo g-{sc["era"]}" id="{sid}-photo">'
                f'<img src="{resolve_opt(sc["ref"]) or ("assets/images/" + sc["ref"] + ".jpeg")}" alt=""{st}></div>'
                f'<div class="grade g-{sc["era"]}-tint"></div>')
        if sc["ov"]:
            body += f'<div class="ov" id="{sid}-ov">{CARDS[sc["ov"]][1]}</div>'
        body += "</div>"
    return (f'<section id="{sid}" class="scene clip" data-start="{sc["start"]}" '
            f'data-duration="{sc["dur"]}" data-track-index="{(sc["i"] % 2) + 1}">{body}</section>')

sections = "\n      ".join(section(sc) for sc in scenes)

# a cite chip lives for ITS line's span only
chips = [(sc["i"], sc["chip"], sc["start"], sc["start"] + sc["dur"]) for sc in scenes if sc["chip"]]
chip_divs = "".join(f'<div class="chip ur" id="chip{i}">{v}</div>' for i, v, _, _ in chips)

ribbon = ('<div id="ribbon">' + "".join(
    f'<span class="rb-seg ur" id="rb-{k}">{RIBBON_LBL[k]}</span>' for k in RIBBON_KEYS) + '</div>')

tally = ('<div id="tally"><div class="tally-in">' + "".join(
    f'<span class="tm" id="tm{n}"></span>' for n in range(1, 10)) + '</div></div>')

audio_html = "\n      ".join(
    f'<audio id="vo-{lid}" src="assets/audio/seg-{lid}.mp3" data-start="{st}" '
    f'data-duration="{du}" data-track-index="20" data-volume="1"></audio>'
    for lid, st, du in audio)

# --- timeline ---------------------------------------------------------------
js = [f'gsap.set([{",".join(chr(34) + "#" + sc["id"] + "-inner" + chr(34) for sc in scenes)}], {{opacity:0}});',
      'gsap.set("#s00-inner", {opacity:1});']
PUSH = {"PI": "pin", "PB": "pback", "TU": "tup", "H": "hold"}
for sc in scenes:
    sid, st, du = sc["id"], sc["start"], sc["dur"]
    prev = f'"#s{sc["i"]-1:02d}-inner"' if sc["i"] > 0 else "null"
    cur = f'"#{sid}-inner"'
    fn = {"XD": "xd", "CUT": "cut", "BLK": "blk"}.get(sc["trans"])
    if fn:
        js.append(f'{fn}({prev},{cur},{st});')
    if sc["ref"].startswith("C:"):
        if sc["first_card"]:
            js.append(f'rvl("#{sid}-card",{round(st + 0.3, 3)});')
        else:
            js.append(f'shw("#{sid}-card",{st});')      # held card: show, don't re-punch
    else:
        if sc["multi"]:                          # continuous zoom across a same-image run
            js.append(f'zc("#{sid}-photo",{st},{du},{sc["z0"]},{sc["z1"]});')
        else:
            cap = 1.08 if sc["ref"] in TIGHT else 1.13
            m = sc["motion"]
            if m == "KB":
                js.append(f'kb("#{sid}-photo",{st},{du},{1 if sc["i"] % 2 == 0 else -1},{cap});')
            elif m in PUSH:
                js.append(f'{PUSH[m]}("#{sid}-photo",{st},{du},{cap});')
            # LK = locked, no move
        if sc["ov"]:
            if sc["ov_hold"]:
                js.append(f'shw("#{sid}-ov",{st});')     # continuation of a held card — already composed
            else:
                js.append(f'rvl("#{sid}-ov",{round(st + 0.8, 3)});')
    if sc["tally"]:
        js.append(f'fin("#tm{sc["tally"]}",{round(st + 0.9, 3)},0.5);')
    if sc["ribbon"]:
        js.append(f'rib("#rb-{sc["ribbon"]}",{round(st + 0.4, 3)});')

for idx, v, tm, end in chips:
    js.append(f'fin("#chip{idx}",{round(tm + 0.6, 3)},0.5);')
    js.append(f'fout("#chip{idx}",{round(min(end, TOTAL) - 0.5, 3)},0.4);')
_first_tally = next((sc for sc in scenes if sc["tally"]), None)
if _first_tally:
    js.append(f'fin("#tally",{round(_first_tally["start"] + 0.5, 3)},0.8);')

timeline = "\n      ".join(js)

HTML = f'''<!DOCTYPE html>
<!-- NOTE: no dir="rtl" on <html> — hyperframes lint: it previews fine but renders a
     fully black video. RTL is scoped to .ur / .cite / .stamp instead. -->
<html lang="ur">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=1920, height=1080">
    <title>فرعون کا انجام — chapter {CHAPTER}</title>
    <script src="assets/gsap.min.js"></script>
    <style>
      @font-face{{font-family:"Nastaliq";font-weight:400;font-display:block;src:url("assets/fonts/NotoNastaliqUrdu-Regular.ttf") format("truetype");}}
      @font-face{{font-family:"Nastaliq";font-weight:700;font-display:block;src:url("assets/fonts/NotoNastaliqUrdu-Bold.ttf") format("truetype");}}
      @font-face{{font-family:"Archivo Black";font-weight:400;font-display:block;src:url("assets/fonts/ArchivoBlack-Regular.woff2") format("woff2");}}
      @font-face{{font-family:"Playfair Display";font-weight:700;font-display:block;src:url("assets/fonts/PlayfairDisplay-Normal.woff2") format("woff2");}}
      :root{{--paper:#0d0f12;--ink:#f4f1ea;--ink-soft:rgba(244,241,234,0.82);--parchment:#e8dcc0;
             --parch-ink:#2b2418;--nile-gold:#c9973f;--river-deep:#1f3a4d;--sepia-1881:#8a6f4d;
             --museum-cool:#9aa8b0;--stamp-red:#9c342a;}}
      *{{box-sizing:border-box;}}
      body{{margin:0;background:#000;}}
      #root{{position:relative;width:1920px;height:1080px;overflow:hidden;background:var(--paper);}}
      .scene{{position:absolute;inset:0;}}
      .scene-inner{{position:absolute;inset:0;will-change:opacity;}}
      .photo{{position:absolute;inset:-7%;background:#0b0d10;will-change:transform;overflow:hidden;}}
      .photo img{{width:100%;height:100%;object-fit:cover;transform-origin:50% 50%;}}
      .photo.dim{{filter:brightness(0.62);}}
      /* --- the 4 era grades (DESIGN §era table) --- */
      .g-ancient{{filter:saturate(1.06) contrast(1.06) brightness(1.00);}}
      .g-sepia{{filter:sepia(0.42) saturate(0.92) contrast(1.10) brightness(0.94);}}
      .g-bw1976{{filter:grayscale(1) contrast(1.20) brightness(0.98);}}
      .g-museum{{filter:saturate(0.90) contrast(1.06) brightness(0.92) hue-rotate(-6deg);}}
      .photo.dim.g-museum{{filter:saturate(0.90) contrast(1.06) brightness(0.58) hue-rotate(-6deg);}}
      .grade{{position:absolute;inset:0;pointer-events:none;mix-blend-mode:multiply;}}
      .g-ancient-tint{{background:radial-gradient(120% 100% at 50% 42%,rgba(201,151,63,0.07),rgba(13,15,18,0.0) 45%,rgba(13,15,18,0.34) 100%);}}
      .g-sepia-tint{{background:radial-gradient(120% 100% at 50% 45%,rgba(138,111,77,0.10),rgba(13,15,18,0.0) 42%,rgba(13,15,18,0.42) 100%);}}
      .g-bw1976-tint{{background:radial-gradient(120% 100% at 50% 45%,rgba(255,255,255,0.0),rgba(13,15,18,0.0) 40%,rgba(13,15,18,0.46) 100%);}}
      .g-museum-tint{{background:radial-gradient(120% 100% at 50% 45%,rgba(154,168,176,0.06),rgba(13,15,18,0.0) 40%,rgba(13,15,18,0.44) 100%);}}
      /* --- persistent film passes (deterministic: static SVG noise, no random) --- */
      #ov-grain{{position:absolute;inset:0;pointer-events:none;opacity:0.085;mix-blend-mode:overlay;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='140' height='140'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>");}}
      #ov-vignette{{position:absolute;inset:0;pointer-events:none;background:radial-gradient(130% 100% at 50% 45%,transparent 54%,rgba(0,0,0,0.46) 100%);}}
      #ov-black{{position:absolute;inset:0;pointer-events:none;background:#000;opacity:0;}}
      /* --- Urdu type: Nastaliq needs vertical room; NEVER animate letter-spacing --- */
      .ur{{font-family:"Nastaliq",serif;direction:rtl;line-height:2.05;}}
      .kw{{display:inline-block;opacity:0;}}
      .rl{{opacity:0;}}
      /* cite chip — the channel's "verified" mark */
      .chip{{position:absolute;right:64px;bottom:56px;opacity:0;font-size:30px;line-height:2.0;
             color:var(--ink);background:rgba(10,13,17,0.58);padding:6px 22px 16px;border-radius:5px;}}
      /* cards */
      .card{{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;
             align-items:center;text-align:center;padding:0 200px;background:var(--parchment);}}
      .card::after{{content:"";position:absolute;inset:0;opacity:0.13;mix-blend-mode:multiply;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><filter id='p'><feTurbulence type='fractalNoise' baseFrequency='0.6' numOctaves='3'/></filter><rect width='100%25' height='100%25' filter='url(%23p)'/></svg>");}}
      .card>*{{position:relative;z-index:1;}}
      .card-dark{{background:#0a0c0f;}}
      .card .ur{{color:var(--parch-ink);}}
      .card-dark .ur{{color:var(--ink);}}
      .ov{{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;align-items:center;padding:0 170px;}}
      .parch{{background:rgba(232,220,192,0.95);padding:54px 86px 30px;border-radius:6px;
              box-shadow:0 24px 90px rgba(0,0,0,.55);max-width:1420px;text-align:center;}}
      .parch .ur{{color:var(--parch-ink);}}
      .parch-sm{{padding:36px 64px 18px;}}
      .q1{{font-size:52px;margin:0 0 10px;}}
      .big{{font-size:86px;font-weight:700;margin:0 0 18px;}}
      .cite{{font-family:"Nastaliq",serif;direction:rtl;font-size:26px;line-height:2.0;
             color:var(--stamp-red);margin:26px 0 0;opacity:0;}}
      .card .cite{{color:var(--stamp-red);}}
      /* era-fall card (hook) */
      .erafall{{text-align:center;}}
      .era-n{{font-family:"Archivo Black";font-size:96px;color:var(--ink);margin:0;opacity:0;}}
      .era-mid{{color:var(--sepia-1881);font-size:112px;margin:22px 0;}}
      .era-u{{font-size:78px;color:var(--nile-gold);margin:18px 0 0;}}
      /* 9-signs tally */
      .tally-row{{display:flex;gap:20px;justify-content:center;margin:44px 0 0;}}
      .tk{{width:12px;height:52px;background:var(--parch-ink);opacity:0.18;border-radius:2px;}}
      #tally{{position:absolute;right:64px;top:56px;opacity:0;background:rgba(232,220,192,0.92);
              padding:20px 26px;border-radius:5px;box-shadow:0 12px 44px rgba(0,0,0,.45);}}
      .tally-in{{display:flex;gap:12px;}}
      .tm{{width:9px;height:40px;background:var(--nile-gold);border-radius:2px;opacity:0;}}
      /* name card */
      .namecard{{background:rgba(10,13,17,0.62);padding:40px 76px;border-radius:6px;text-align:center;}}
      .name-en{{font-family:"Playfair Display";font-size:82px;color:var(--ink);margin:0;letter-spacing:.03em;opacity:0;}}
      .name-ur{{font-size:52px;color:var(--nile-gold);margin:14px 0 0;}}
      /* myth cards */
      .myth{{text-align:center;}}
      .myth-n{{font-family:"Archivo Black";font-size:64px;color:var(--parch-ink);opacity:0;margin:0 0 10px;}}
      .myth-q{{font-size:56px;margin:0;}}
      .myth-f{{font-size:38px;margin:34px 0 0;opacity:.85;}}
      .stamp{{font-family:"Nastaliq",serif;direction:rtl;font-size:74px;line-height:1.9;color:var(--stamp-red);
              border:6px solid var(--stamp-red);padding:4px 46px 22px;border-radius:8px;
              transform:rotate(-7deg);margin:36px 0 0;display:inline-block;opacity:0;}}
      .stamp-amber{{color:#9a6a1e;border-color:#9a6a1e;}}
      /* timeline ribbon */
      /* era marker: hidden by default, surfaces ONLY at an era jump then leaves */
      #ribbon{{position:absolute;left:0;right:0;bottom:0;height:64px;display:flex;
               justify-content:center;align-items:center;gap:80px;opacity:0;
               background:linear-gradient(0deg,rgba(6,8,11,0.72),rgba(6,8,11,0));}}
      .rb-seg{{font-size:26px;line-height:2.0;color:var(--ink-soft);opacity:0.16;}}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-width="1920" data-height="1080" data-duration="{TOTAL}" data-fps="30">

      {sections}

      <div id="ov-grain"></div>
      <div id="ov-vignette"></div>
      <div id="ov-black"></div>
      {tally}
      {ribbon}
      {chip_divs}
      {audio_html}
    </div>

    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});

      // --- motion (deterministic; only transform/opacity/colour animated) ---
      function kb(sel,at,dur,dir,cap){{gsap.set(sel,{{transformOrigin:"50% 50%"}});tl.fromTo(sel,{{scale:1.0,xPercent:dir*-1.3,yPercent:0.5}},{{scale:cap,xPercent:dir*1.3,yPercent:-0.5,duration:dur,ease:"sine.inOut"}},at);}}
      function pin(sel,at,dur,cap){{gsap.set(sel,{{transformOrigin:"50% 50%"}});tl.fromTo(sel,{{scale:1.0}},{{scale:cap,duration:dur,ease:"sine.inOut"}},at);}}
      function pback(sel,at,dur,cap){{gsap.set(sel,{{transformOrigin:"50% 50%"}});tl.fromTo(sel,{{scale:cap}},{{scale:1.0,duration:dur,ease:"sine.inOut"}},at);}}
      function tup(sel,at,dur,cap){{gsap.set(sel,{{transformOrigin:"50% 50%"}});tl.fromTo(sel,{{scale:cap*0.95,yPercent:2.6}},{{scale:cap,yPercent:-2.6,duration:dur,ease:"sine.inOut"}},at);}}
      function hold(sel,at,dur,cap){{gsap.set(sel,{{transformOrigin:"50% 50%"}});tl.fromTo(sel,{{scale:1.0}},{{scale:1.035,duration:dur,ease:"sine.inOut"}},at);}}
      // continuous linear zoom (same-image runs) — matched scale at each invisible cut, so a group reads as ONE smooth move
      function zc(sel,at,dur,s0,s1){{gsap.set(sel,{{transformOrigin:"50% 50%"}});tl.fromTo(sel,{{scale:s0}},{{scale:s1,duration:dur,ease:"none"}},at);}}
      // --- transitions ---
      // dip-free dissolve: the incoming (opaque photo) fades in ON TOP of the outgoing held at full opacity, so no black shows through the mid-point (no luminance dip). Outgoing is dropped once covered.
      function xd(from,to,at){{gsap.set(to,{{opacity:0}});tl.to(to,{{opacity:1,duration:1.0,ease:"power1.inOut"}},at);if(from)tl.set(from,{{opacity:0}},at+1.0);}}
      function cut(from,to,at){{if(from)tl.set(from,{{opacity:0}},at);tl.set(to,{{opacity:1}},at);}}
      function blk(from,to,at){{tl.to("#ov-black",{{opacity:1,duration:0.25,ease:"power2.in"}},Math.max(at-0.25,0));if(from)tl.set(from,{{opacity:0}},at);tl.set(to,{{opacity:1}},at);tl.to("#ov-black",{{opacity:0,duration:0.7,ease:"power2.out"}},at+0.5);}}
      // --- reveals ---
      function fin(sel,at,dur){{gsap.set(sel,{{opacity:0}});tl.to(sel,{{opacity:1,duration:dur,ease:"power2.out"}},at);}}
      function fout(sel,at,dur){{tl.to(sel,{{opacity:0,duration:dur,ease:"power2.in"}},at);}}
      // era jump: the ribbon surfaces, the reached era lights gold, then it leaves
      function rib(sel,at){{
        tl.to("#ribbon",{{opacity:1,duration:0.6,ease:"power2.out"}},at);
        tl.to(sel,{{opacity:1,color:"#c9973f",duration:0.7,ease:"power2.out"}},at+0.3);
        tl.to("#ribbon",{{opacity:0,duration:0.9,ease:"power2.in"}},at+4.5);
      }}
      // card/overlay reveal: container fades, then WORD-BY-WORD y+opacity (Nastaliq-safe)
      function rvl(sel,at){{
        fin(sel,at,0.7);
        tl.to(sel+" .rl",{{opacity:1,duration:0.6,stagger:0.35,ease:"power2.out"}},at+0.15);
        tl.fromTo(sel+" .kw",{{opacity:0,y:26}},{{opacity:1,y:0,duration:0.5,stagger:0.075,ease:"power2.out"}},at+0.25);
      }}
      // held card: same card continues into a new line — show it composed, no re-punch
      function shw(sel,at){{
        tl.set(sel,{{opacity:1}},at);
        tl.set(sel+" .rl, "+sel+" .kw",{{opacity:1,y:0}},at);
      }}

      {timeline}

      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
'''

with open(os.path.join(HERE, "index.html"), "w") as f:
    f.write(HTML)

mm, ss = int(TOTAL // 60), TOTAL - int(TOTAL // 60) * 60
print(f"chapter {CHAPTER}: {len(scenes)} scenes · {len(audio)} VO lines · "
      f"{TOTAL}s (~{mm}:{ss:04.1f}) · ~{int(TOTAL*30)} frames")
for lid, st, du in audio:
    print(f"  line {lid:<7} start {st:>7.2f}  clip {du:>6.2f}  gap {gap_after(LINES, [l[0] for l in LINES].index(lid))}")
if held:
    print("HELD (missing still, previous image held):")
    for h in held:
        print("  " + h)
