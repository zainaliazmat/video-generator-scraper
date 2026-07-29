#!/usr/bin/env python3
"""
Build «فرعون کا انجام» -> index.html (HyperFrames), CHAPTER BY CHAPTER.

    python3 build.py --chapter 1     # emits index.html for chapter 1 only, clock from 0

Timing is BY CONSTRUCTION (hyperframes_production §5b): one TTS clip per script
segment, probed with ffprobe; each segment's visual span = clip duration + the
gap that follows it (storyboard VO TIMING TABLE). Scenes inside a segment split
that span by their weights. No silencedetect, no char-weights, no FIX_START —
that stack exists only in the Pompeii build and must not be rebuilt.

Determinism contract (DESIGN §): ONE paused gsap.timeline on
window.__timelines["main"], only x/y/scale/opacity/color animated, no Date.now,
no Math.random, no network. gsap is vendored at assets/gsap.min.js.
"""
import os, sys, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "assets", "images")
AUD = os.path.join(HERE, "assets", "audio")

# ---------------------------------------------------------------------------
# VO TIMING — gap AFTER each segment (storyboard VO TIMING TABLE). Clip
# durations are probed, never hardcoded, so a re-rolled line just works.
# ---------------------------------------------------------------------------
GAP = {"05":1.0, "10":1.0, "15":1.0, "17":1.0, "20-21":1.0, "23":1.0, "32":1.0,
       "35":1.0, "37":3.0, "39":1.5, "42":1.0, "46":1.0, "48":1.0, "52":2.0}
def gap(sid): return GAP.get(sid, 0.5)

# ---------------------------------------------------------------------------
# Known image defects (image-audit.md) handled IN-COMP.
#   crop  : (scale, dx%, dy%) from `ffmpeg cropdetect` — kills baked-in bars
#           BEFORE the Ken Burns move, so bars never ride into frame.
#   tight : Ken Burns headroom is short — cap the punch at 1.08, not 1.14.
# ---------------------------------------------------------------------------
CROP = {                       # measured 2026-07-19 on the 2752x1536 masters
    "P30a": (1.048, 0.0,  0.0),    # letterboxed 24px top/bottom
    "P35b": (1.180, 0.0,  5.47),   # letterboxed, content sits high
    "P11b": (1.255, -3.56, -5.60), # letterboxed + pillarboxed
    "P37b": (1.193, 3.78, 0.0),    # pillarboxed 104px left
}
TIGHT = {"P45a", "P50c", "P16f3", "P03d"}     # image-audit: little headroom, cap the punch

# ---------------------------------------------------------------------------
# EDL.  shots = (ref, weight, motion, trans, opts)
#   ref    : image basename, or "C:<card-id>" for a HyperFrames card scene
#   weight : share of the segment's span (relative)
#   motion : PI push-in · PB pull-back · TU tilt-up · KB drift · H micro-hold · LK locked · '-' card
#   trans  : XD 1s dissolve · CUT hard · BLK cut-to-black+beat · NONE
#   opts   : ov=<card-id> overlay · era=<grade override> · dim=1
# ---------------------------------------------------------------------------
SEG = {
 # ---- CH1 · HOOK (museum grade) -------------------------------------------
 "01": dict(ch=1, era="museum", shots=[
     ("P01a", 1.6, "LK", "NONE", {}),
     ("P01b", 2.8, "PI", "XD",  {}),
 ]),
 "02": dict(ch=1, era="museum", shots=[
     ("P02a", 1, "H",  "XD", {}),
     ("P02b", 1, "KB", "XD", {}),
     ("P02c", 1, "H",  "XD", {}),
 ]),
 "03": dict(ch=1, era="museum", shots=[
     ("P03a", 1.0, "H",  "XD",  {}),
     ("P03b", 1.1, "PI", "XD",  {}),
     ("P03c", 0.9, "LK", "XD",  {}),
     ("P03d", 1.0, "KB", "CUT", {"era": "bw1976"}),   # 1976 era flash — the first jolt
 ]),
 "04": dict(ch=1, era="museum", chip="یونس 10:92", shots=[
     ("P01c", 1.0, "PI", "XD", {}),
     ("P01a", 2.2, "LK", "XD", {"dim": 1, "ov": "C-04"}),
 ]),
 "05": dict(ch=1, era="museum", shots=[
     ("C:C-05a", 1.0, "-", "XD", {}),
     ("C:C-05b", 1.2, "-", "XD", {"ribbon": "ancient"}),
 ]),

 # ---- CH2 · غلاموں کا شہر --------------------------------------------------
 # P10c (the glow alternate) is EXCLUDED — image-audit: offset hard-edged glow,
 # mother's brow and the infant's ear read past it. P10a/P10b are the compliant
 # hands-only frames and carry the beat as the storyboard originally specified.
 "06": dict(ch=2, era="ancient", shots=[
     ("P06a", 1.2, "PI", "NONE", {}),
     ("P06b", 1.3, "PB", "XD",   {}),
     ("P06c", 1.0, "H",  "XD",   {}),
 ]),
 "07": dict(ch=2, era="ancient", chip="القصص 28:4", shots=[
     ("P07a", 1.4, "PB", "XD", {}),
     ("P07b", 1.1, "KB", "XD", {}),
     ("P07c", 1.0, "H",  "XD", {}),
 ]),
 "08": dict(ch=2, era="ancient", chip="النازعات 79:24", shots=[
     ("P08a", 1.2, "PI", "XD", {}),
     ("P08b", 1.2, "PI", "XD", {}),
     ("P08c", 1.0, "H",  "XD", {}),
 ]),
 "09": dict(ch=2, era="ancient", chip="القصص 28:4", shots=[
     ("P09a", 1.3, "PI", "XD", {}),
     ("P09b", 1.0, "LK", "XD", {}),
 ]),
 "10": dict(ch=2, era="ancient", shots=[
     ("P10a", 1.3, "H",  "BLK", {}),      # hard cut to black off seg 09 — the implied act
     ("P10b", 1.0, "LK", "XD",  {}),
 ]),

 # ---- CH4 · مدین سے طُور تک (the hardest chapter for depiction) ------------
 # EXCLUDED pending re-gen: P16c2, P16d2, P16e1, P16f2. The compliant siblings
 # cover every beat except the elder at the tent (P16e1 has no alternate), so
 # seg 16a runs on the walk + well + daughters + the empty-tree dua frame.
 "16": dict(ch=4, era="ancient", chip="القصص 28:15-16 · 28:20-21", shots=[
     ("P16a1", 1.2, "KB", "NONE", {}),
     ("P16a2", 1.0, "H",  "XD",   {}),
     ("P16b1", 1.2, "PI", "XD",   {}),
     ("P16b2", 1.0, "H",  "XD",   {}),
 ]),
 "16a": dict(ch=4, era="ancient", chip="القصص 28:23-27", shots=[
     ("P16b3", 1.0, "KB", "XD", {}),
     ("P16c1", 1.3, "PB", "XD", {}),
     ("P16c3", 1.0, "H",  "XD", {}),
     ("P16d1", 1.3, "LK", "XD", {"ov": "C-16a"}),
 ]),
 "16b": dict(ch=4, era="ancient", chip="القصص 28:29 · طٰہٰ 20:10", shots=[
     ("P16f1", 1.2, "PI", "XD", {}),
     ("P16f3", 1.0, "H",  "XD", {}),      # Ken-Burns tight -> capped at 1.08
     ("P16g1", 1.5, "LK", "XD", {}),      # the long hold on the distant fire
 ]),
 "16c": dict(ch=4, era="ancient", chip="طٰہٰ 20:12-14 · النساء 4:164", shots=[
     ("P16h1", 1.3, "LK", "XD", {}),      # fire-that-is-light: no figure, no form
     ("P16h2", 1.0, "H",  "XD", {}),
     ("P16i1", 1.2, "LK", "XD", {"ov": "C-16c"}),
     ("P16i2", 1.0, "H",  "XD", {}),
 ]),
 "16d": dict(ch=4, era="ancient", chip="طٰہٰ 20:24", shots=[
     ("P16j1", 1.1, "KB", "XD", {}),
     ("P16j2", 1.0, "H",  "XD", {}),
     ("P16k1", 1.1, "PI", "XD", {}),
     ("P16k2", 1.2, "LK", "XD", {"ov": "C-16d"}),
 ]),
 "17": dict(ch=4, era="ancient", chip="طٰہٰ 20:46", shots=[
     ("P17a",    1.2, "PI", "XD", {}),
     ("C:C-17a", 1.2, "-",  "XD", {}),
     ("P17c",    1.0, "H",  "XD", {}),
     ("C:C-17b", 1.1, "-",  "XD", {}),
     ("P17b",    0.9, "LK", "XD", {}),    # their shadows only — the open loop
 ]),

 # ---- CH6 · نشانیوں پر نشانیاں (ancient grade, tally card) -----------------
 # no corner chip on card-only segments — the card carries its own inline cite
 "24": dict(ch=6, era="ancient", shots=[
     ("C:C-24", 1, "-", "NONE", {}),
 ]),
 "25": dict(ch=6, era="ancient", chip="الاعراف 7:130", tally=1, shots=[
     ("P25a", 1.3, "PI", "XD", {}),
     ("P25b", 1.0, "H",  "XD", {}),
 ]),
 "26": dict(ch=6, era="ancient", chip="الاعراف 7:133", tally=2, shots=[
     ("P26a", 1.2, "PB", "XD", {}),
     ("P26b", 1.0, "KB", "XD", {}),
 ]),
 "27": dict(ch=6, era="ancient", tally=3, shots=[
     ("P27a", 1.2, "KB", "XD", {}),
     ("P27b", 1.0, "PI", "XD", {}),
     ("P27c", 1.0, "H",  "XD", {}),
 ]),
 "28": dict(ch=6, era="ancient", tally=4, shots=[
     ("P28a", 1.0, "PI", "XD", {}),
     ("P28b", 1.0, "H",  "XD", {}),
 ]),
 "29": dict(ch=6, era="ancient", tally=5, shots=[
     ("P29a", 1.2, "KB", "XD", {}),
     ("P29b", 1.0, "H",  "XD", {}),
     ("P29c", 1.0, "H",  "XD", {}),
 ]),
 "30": dict(ch=6, era="ancient", chip="الاعراف 7:133", tally=6, shots=[
     ("P30a", 1.3, "PB", "XD", {}),                    # letterboxed -> CROP
     ("P30b", 1.0, "H",  "XD", {}),
     ("P30c", 1.4, "PI", "XD", {"ov": "C-30"}),
 ]),
 "31": dict(ch=6, era="ancient", chip="الاعراف 7:134-135", shots=[
     ("P31a", 1.2, "PI", "XD", {}),
     ("P31b", 1.0, "H",  "XD", {}),
     ("P31c", 1.1, "H",  "XD", {}),
 ]),
 "32": dict(ch=6, era="ancient", shots=[
     ("P32a", 1.2, "PI", "XD", {}),
     ("P32b", 1.0, "LK", "XD", {}),
 ]),

 # ---- CH7 · رات کا سفر + سمندر (ancient grade, night->dawn) ----------------
 "33": dict(ch=7, era="ancient", chip="الدخان 44:23", shots=[
     ("P33a", 1.4, "KB", "NONE", {}),
     ("P33b", 1.0, "H",  "XD",   {}),
     ("P33c", 1.0, "H",  "XD",   {}),
 ]),
 "34": dict(ch=7, era="ancient", chip="الشعراء 26:53-55", shots=[
     ("P34a", 1.3, "PI", "XD", {}),
     ("P34b", 1.1, "KB", "XD", {}),
     ("P34c", 0.8, "H",  "XD", {}),
     ("P34d", 1.0, "KB", "XD", {}),
 ]),
 "35": dict(ch=7, era="ancient", chip="الشعراء 26:62", shots=[
     ("P35a", 1.2, "KB", "XD", {}),
     ("P35b", 1.0, "PI", "XD", {}),                    # letterboxed -> CROP
     ("P35c", 2.0, "LK", "XD", {"ov": "C-35"}),
 ]),
 "36": dict(ch=7, era="ancient", chip="الشعراء 26:63 · طٰہٰ 20:77", shots=[
     ("P36a", 1.4, "TU", "XD", {}),
     ("P36b", 1.1, "TU", "XD", {}),
     ("P36c", 1.2, "PI", "XD", {}),
     ("P36d", 0.9, "H",  "XD", {}),
     ("P36e", 1.2, "LK", "XD", {}),
 ]),
 "37": dict(ch=7, era="ancient", shots=[
     ("P37a", 1.2, "PI", "XD",  {}),
     ("P37b", 0.8, "LK", "XD",  {}),                   # pillarboxed -> CROP
     ("P37c", 1.2, "KB", "CUT", {}),                   # the collapse — hard cut
     ("P37d", 2.2, "LK", "BLK", {}),                   # payoff frame, holds the 3s silence
 ]),

 # ---- CH9 · 1881 + پیرس (sepia -> B&W newsreel) ---------------------------
 "43": dict(ch=9, era="sepia", shots=[
     ("P43a", 1.3, "PI", "NONE", {"ribbon": "1881"}),
     ("P43b", 1.1, "KB", "XD",   {}),
     ("P43c", 1.0, "H",  "XD",   {}),
 ]),
 "44": dict(ch=9, era="sepia", chip="TT320 — 1881", shots=[
     ("P44a", 1.6, "KB", "XD", {"ov": "C-44"}),
     ("P44b", 1.0, "PI", "XD", {}),
 ]),
 "45": dict(ch=9, era="sepia", shots=[
     ("P45a", 1.3, "PI", "XD", {"ov": "C-45"}),        # Ken-Burns tight -> 1.08
     ("P45b", 1.0, "PB", "XD", {}),
 ]),
 "46": dict(ch=9, era="bw1976", chip="NYT 1976 · LA Times 1977", shots=[
     ("P46a", 1.2, "PI", "CUT", {"ribbon": "1976"}),
     ("P46b", 1.0, "KB", "XD",  {}),
     ("P46c", 1.1, "KB", "XD",  {}),
 ]),
 "47": dict(ch=9, era="museum", shots=[
     ("C:C-47", 1, "-", "BLK", {}),
 ]),
 "48": dict(ch=9, era="museum", shots=[
     ("C:C-48a", 1.0, "-", "CUT", {}),
     ("C:C-48b", 1.1, "-", "CUT", {}),
 ]),
}

CHAPTERS = {
 1: ["01", "02", "03", "04", "05"],
 2: ["06", "07", "08", "09", "10"],
 4: ["16", "16a", "16b", "16c", "16d", "17"],
 6: ["24", "25", "26", "27", "28", "29", "30", "31", "32"],
 7: ["33", "34", "35", "36", "37"],
 9: ["43", "44", "45", "46", "47", "48"],
}

# ---------------------------------------------------------------------------
# CARDS.  kind: scene = full parchment · dark = full dark · ov = over the photo
# `u(...)` marks Urdu that gets word-by-word kinetic type (never letter-spacing —
# that breaks Nastaliq joining, DESIGN §Typography).
# ---------------------------------------------------------------------------
def u(text, cls="qr"):
    """Nastaliq line, split into per-word spans for the kinetic reveal.
    The word carries its own trailing nbsp — inline-block spans swallow the
    whitespace between them, and without this the words butt together."""
    words = "".join(f'<span class="kw">{w}&nbsp;</span>' for w in text.split(" "))
    return f'<p class="ur {cls} rl">{words}</p>'

CARDS = {
 "C-04": ("ov",
    '<div class="parch">'
    + u("آج ہم تیرا بدن بچا لیں گے،", "q1")
    + u("تاکہ تُو اپنے بعد والوں کے لیے نشانی بنے۔", "q1")
    + '<p class="cite rl">یونس 10:92</p></div>'),
 "C-05a": ("scene",
    u("معجزہ نہیں۔", "big") + u("اُس سے اگلی صبح۔", "big")),
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
CHAPTER = int(sys.argv[sys.argv.index("--chapter") + 1]) if "--chapter" in sys.argv else None
if CHAPTER not in CHAPTERS:
    raise SystemExit(f"usage: build.py --chapter N   (built: {sorted(CHAPTERS)})")
ORDER = CHAPTERS[CHAPTER]

def resolve(base):
    for ext in (".jpeg", ".jpg", ".png"):
        if os.path.exists(os.path.join(IMG, base + ext)):
            return "assets/images/" + base + ext
    raise SystemExit(f"MISSING ASSET: {base}")

def probe(path):
    return float(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", path]).strip())

OVERLAP = {"XD": 1.0}          # dissolves overlap the outgoing scene; CUT/BLK/NONE do not

# --- lay the chapter out on its own clock ----------------------------------
scenes, audio, t, i = [], [], 0.0, 0
for sid in ORDER:
    S = SEG[sid]
    clip = probe(os.path.join(AUD, f"seg-{sid}.mp3"))
    span = clip + gap(sid)                                  # visuals cover the pause too
    audio.append((sid, round(t, 3), round(clip, 3)))
    tot = sum(sh[1] for sh in S["shots"])
    for k, (ref, w, motion, trans, opts) in enumerate(S["shots"]):
        clean = span * w / tot
        nxt = S["shots"][k + 1][3] if k + 1 < len(S["shots"]) else None
        if nxt is None:                                     # transition of the next SEGMENT
            j = ORDER.index(sid) + 1
            nxt = SEG[ORDER[j]]["shots"][0][3] if j < len(ORDER) else None
        scenes.append(dict(
            i=i, id=f"s{i:02d}", ref=ref, seg=sid, start=round(t, 3),
            dur=round(clean + OVERLAP.get(nxt, 0.0), 3),
            motion=motion, trans=trans, opts=opts,
            era=opts.get("era", S["era"]),
            chip=S.get("chip") if k == 0 else None,
            tally=S.get("tally") if k == 0 else None,
            ribbon=opts.get("ribbon")))
        t += clean
        i += 1
TOTAL = round(t, 3)
scenes[0]["trans"] = "NONE"                                 # standalone chapter: hard in

# ---------------------------------------------------------------------------
# HTML
# ---------------------------------------------------------------------------
def section(sc):
    sid, o = sc["id"], sc["opts"]
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
        dimc = " dim" if o.get("dim") else ""
        body = (f'<div class="scene-inner" id="{sid}-inner">'
                f'<div class="photo g-{sc["era"]}{dimc}" id="{sid}-photo">'
                f'<img src="{resolve(sc["ref"])}" alt=""{st}></div>'
                f'<div class="grade g-{sc["era"]}-tint"></div>')
        if o.get("ov"):
            body += f'<div class="ov" id="{sid}-ov">{CARDS[o["ov"]][1]}</div>'
        body += "</div>"
    return (f'<section id="{sid}" class="scene clip" data-start="{sc["start"]}" '
            f'data-duration="{sc["dur"]}" data-track-index="{(sc["i"] % 2) + 1}">{body}</section>')

sections = "\n      ".join(section(sc) for sc in scenes)

# a cite chip lives for ITS segment only — it must not ride into the next beat
seg_end = {}
for sid, st, du in audio:
    seg_end[sid] = st + du + gap(sid)
chips = [(sc["i"], sc["chip"], sc["start"], seg_end[sc["seg"]]) for sc in scenes if sc["chip"]]
chip_divs = "".join(f'<div class="chip ur" id="chip{i}">{v}</div>' for i, v, _, _ in chips)

ribbon = ('<div id="ribbon">' + "".join(
    f'<span class="rb-seg ur" id="rb-{k}">{RIBBON_LBL[k]}</span>' for k in RIBBON_KEYS) + '</div>')

tally = ('<div id="tally"><div class="tally-in">' + "".join(
    f'<span class="tm" id="tm{n}"></span>' for n in range(1, 10)) + '</div></div>')

audio_html = "\n      ".join(
    f'<audio id="vo-{sid}" src="assets/audio/seg-{sid}.mp3" data-start="{st}" '
    f'data-duration="{du}" data-track-index="20" data-volume="1"></audio>'
    for sid, st, du in audio)

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
    if not sc["ref"].startswith("C:"):
        cap = 1.08 if sc["ref"] in TIGHT else 1.13
        m = sc["motion"]
        if m == "KB":
            js.append(f'kb("#{sid}-photo",{st},{du},{1 if sc["i"] % 2 == 0 else -1},{cap});')
        elif m in PUSH:
            js.append(f'{PUSH[m]}("#{sid}-photo",{st},{du},{cap});')
        # LK = locked, no move
    if sc["opts"].get("ov"):
        js.append(f'rvl("#{sid}-ov",{round(st + 0.8, 3)});')
    if sc["ref"].startswith("C:"):
        js.append(f'rvl("#{sid}-card",{round(st + 0.3, 3)});')
    if sc["tally"]:
        js.append(f'fin("#tm{sc["tally"]}",{round(st + 0.9, 3)},0.5);')
    if sc["ribbon"]:
        js.append(f'rib("#rb-{sc["ribbon"]}",{round(st + 0.4, 3)});')

for idx, v, tm, end in chips:
    js.append(f'fin("#chip{idx}",{round(tm + 0.6, 3)},0.5);')
    js.append(f'fout("#chip{idx}",{round(min(end, TOTAL) - 0.5, 3)},0.4);')
# the tally frame arrives WITH its first mark — an empty box held through the
# intro card read as a broken overlay in the first draft
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
      // --- transitions ---
      function xd(from,to,at){{gsap.set(to,{{opacity:0}});tl.to(to,{{opacity:1,duration:1.0,ease:"power1.inOut"}},at);if(from)tl.to(from,{{opacity:0,duration:1.0,ease:"power1.inOut"}},at);}}
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

      {timeline}

      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
'''

with open(os.path.join(HERE, "index.html"), "w") as f:
    f.write(HTML)

mm, ss = int(TOTAL // 60), TOTAL - int(TOTAL // 60) * 60
print(f"chapter {CHAPTER}: {len(scenes)} scenes · {len(audio)} VO clips · "
      f"{TOTAL}s (~{mm}:{ss:04.1f}) · ~{int(TOTAL*30)} frames")
for sid, st, du in audio:
    print(f"  seg {sid:<5} start {st:>7.2f}  clip {du:>6.2f}  gap {gap(sid)}")
