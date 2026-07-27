#!/usr/bin/env python3
"""
Build the FULL "Pompeii Ka Akhri Din" composition -> index.html (HyperFrames).

This is the single source of truth for the film's assembly. It emits a static,
deterministic index.html from the EDL below (see frame.md) reusing the exact
determinism contract the Hook proved: ONE gsap.timeline paused on
window.__timelines["main"], animate only transform/opacity, no Date.now/random/network.

Silent visual draft: durations are frame.md approximations. When the Roman-Urdu VO
is recorded, relock each scene's `dur` here and re-run:  python3 build.py
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "assets", "images")

def resolve(base):
    """Find images/<base>.{jpeg,jpg,png} regardless of extension."""
    for ext in (".jpeg", ".jpg", ".png"):
        if os.path.exists(os.path.join(IMG, base + ext)):
            return "assets/images/" + base + ext
    raise SystemExit(f"MISSING ASSET: {base}")

# ---------------------------------------------------------------------------
# EDL  (kind, ref, dur, motion, trans_in, chip, overlay)
#   kind : R=recon still  E=evidence  C=card scene
#   motion: PI push-in · PB pull-back · TU tilt-up · PX/DR/KB drift · H hold · LK locked · '-' card
#   trans_in: XD dissolve(default) · CUT hard · BLK cut-to-black+silence · WHITE wash · EMB ember · NONE
#   chip : str value | 'HIDE' | list[str] (ticks across the scene) | None
#   overlay : card id rendered on top of the photo | None
# ---------------------------------------------------------------------------
S = [
 # --- CH1 · HOOK ---------------------------------------------------------
 ("R","S1-01A_bread-man-bakery",5,"PI","NONE",None,None),
 ("R","S1-01B_bread-hands",3,"H","XD",None,None),
 ("R","S1-02A_thermopolium-argument",4,"PX","XD",None,None),
 ("R","S1-02B_stew-ladle",3,"H","XD",None,None),
 ("R","S1-03A_horse-groomed",6,"PI","XD",None,None),
 ("R","S1-03B_horse-head",4,"H","XD",None,None),
 ("R","S1-04A_gladiator",3,"KB","XD",None,None),
 ("R","S1-04B_school-boy",3,"KB","XD",None,None),
 ("R","S1-05A_street-ordinary",5,"PI","XD",None,None),
 ("R","S1-05B_street-vesuvius-first",6,"PI","XD",None,None),
 ("R","S1-06A_epic-establishing",7,"DR","XD",None,"C-06"),
 ("C","C-07",4,"-","XD","6:00 AM",None),
 ("R","S1-07A_fountain-corner",5,"DR","XD",None,None),
 ("R","S1-07B_golden-lane",5,"PI","XD",None,None),
 # --- CH2 · SETUP --------------------------------------------------------
 ("C","C-08",15,"-","XD","HIDE",None),
 ("R","S2-09A_harbour",5,"DR","XD",None,None),
 ("R","S2-09B_seaside-villas",5,"PI","XD",None,None),
 ("R","S2-09C_commercial-street",5,"PX","XD",None,None),
 ("R","S2-10A_vesuvius-over-city",9,"TU","XD",None,None),
 ("R","S2-10B_vineyards",9,"DR","XD",None,None),
 ("R","S2-11A_vesuvius-single-cone",10,"H","XD",None,"C-11"),
 ("R","S2-12A_earthquake-repairs",10,"PI","XD",None,None),
 ("E","EV-12B_earthquake-relief",8,"H","XD",None,"LBL-62"),
 # --- CH3 · THE MORNING --------------------------------------------------
 ("R","S3-13A_street-waking",5,"PI","XD","6:00 AM",None),
 ("R","S3-14A_baker-oven",5,"PI","XD",None,None),
 ("R","S3-14B_loaves-cooling",3,"H","XD",None,None),
 ("E","EV-14C_carbonised-bread",4,"H","XD",None,None),          # recon->evidence match
 ("R","S3-15A_thermopolium-lively",4,"PX","XD","7:00 AM",None),
 ("R","S3-15B_thermopolium-counter",3,"H","XD",None,None),
 ("R","S3-16A_wall-graffiti",6,"PX","XD",None,"C-16"),
 ("R","S3-17A_school-boy",4,"KB","XD","8:00 AM",None),
 ("R","S3-18A_roman-baths",5,"PI","XD","9:00 AM",None),
 ("R","S3-18B_amphitheatre",5,"DR","XD","10:00 AM",None),
 ("R","S3-19A_dry-well",4,"H","XD",None,None),
 ("R","S3-19B_horse-uneasy",4,"H","XD",None,None),
 ("R","S3-19C_cracked-fresco",3,"PI","XD",None,None),
 ("R","S3-20A_street-vesuvius-refrain",5,"PX","XD",None,None),
 ("R","S3-21A_street-bread-vesuvius",5,"H","XD",None,None),
 ("R","S3-22A_noon-street",5,"PX","XD","12:00 PM","C-22"),
 # --- CH4 · THE ERUPTION -------------------------------------------------
 ("R","S4-23A_blast-over-city",6,"H","BLK",None,None),          # interrupt 1
 ("R","S4-23B_summit-blast",3,"H","CUT",None,None),
 ("R","S4-24A_umbrella-column",8,"TU","XD",None,"C-24"),
 ("R","S4-25A_pliny-terrace",7,"PI","XD",None,"C-25"),
 ("E","EV-26A_pliny-letters-manuscript",8,"H","XD",None,None),
 ("R","S4-26B_pliny-writing",4,"H","XD",None,None),
 ("R","S4-27A_ashfall-street",6,"PI","XD",None,None),
 ("R","S4-27B_pumice-hand",3,"H","EMB",None,None),              # ember act-break
 ("R","S4-28A_family-doorway",5,"H","XD",None,"C-28"),
 ("R","S4-29A_refugees-road",6,"PX","XD",None,None),
 ("R","S4-29B_barring-door",6,"PI","XD",None,None),
 ("R","S4-30A_lamplit-home",8,"H","XD",None,None),
 # --- CH5 · AFTERNOON & NIGHT --------------------------------------------
 ("R","S5-31A_street-buried",7,"PI","XD",["2:00 PM","3:00 PM","4:00 PM"],None),
 ("R","S5-31B_door-blocked",4,"H","XD",None,None),
 ("R","S5-32A_harbour-pumice",7,"DR","XD",None,None),
 ("R","S5-33A_rescue-fleet",7,"PX","XD",None,"C-33"),
 ("R","S5-34A_admiral-beach",8,"H","XD",None,None),
 ("R","S5-35A_roof-collapse",6,"PI","XD","7:00 PM",None),
 ("C","C-36",12,"-","XD",None,None),
 ("R","S5-37A_pyroclastic-night",8,"TU","XD",None,"C-37"),
 ("C","C-38",4,"-","EMB",None,None),                            # ember act-break
 ("R","S5-38A_boathouses-night",6,"PI","XD",None,None),
 ("E","EV-38B_herculaneum-boathouses",5,"H","XD",None,None),
 ("E","EV-39A_herculaneum-skeletons",8,"H","XD",None,None),
 # --- CH6 · DAWN / THE END -----------------------------------------------
 ("R","S6-40A_family-vigil",8,"PI","XD","3:00 AM",None),
 ("R","S6-40B_wall-night-surge",6,"DR","XD",None,None),
 ("R","S6-41A_silent-buried-street",15,"LK","BLK",None,None),   # interrupt 2 (silence, held)
 ("R","S6-43A_survivors-emerge",7,"PI","XD","6:30 AM",None),
 ("R","S6-43B_child-shoulders",4,"H","XD",None,None),
 ("R","S6-44A_column-collapse",8,"TU","XD",None,None),
 ("R","S6-45A_surge-crests-wall",10,"LK","XD",None,None),       # peak
 ("R","S6-46A_grey-plain",10,"PB","WHITE",None,None),           # white wash into aftermath
 # --- CH7 · 1700 YEARS / CASTS -------------------------------------------
 ("R","S7-47A_shepherd-plain",5,"H","XD","HIDE",None),   # day's timeline ends -> drop the chip
 ("R","S7-47B_medieval-farmers",5,"H","XD",None,None),
 ("R","S7-47C_1600s-farmers",5,"H","XD",None,None),
 ("R","S7-48A_excavation-1748",7,"PI","XD",None,None),
 ("E","EV-48B_villa-misteri-fresco",5,"H","XD",None,None),      # match: colours blaze
 ("E","EV-51A_garden-fugitives-casts",6,"H","XD",None,"C-49"),
 ("C","C-50",12,"-","XD",None,None),
 ("E","EV-51A-boxer_man-covering-face",14,"H","XD",None,None),  # the covering-face cast + silence
 ("R","S1-03A_horse-groomed",5,"H","XD",None,None),             # callback part 1
 ("E","EV-52B_horse-cast",5,"H","XD",None,None),                # callback part 2 (match)
 ("R","S7-48A_excavation-1748",10,"DR","XD",None,None),         # soft CTA b-roll
 # --- CH8 · 2024-26 DISCOVERIES ------------------------------------------
 ("E","EV-54A_regio-ix-blueroom-1",12,"H","XD","AUG 2024",None),
 ("R","S8-55A_regio-ix-room",8,"PI","XD",None,None),
 ("R","S8-55B_hand-key",4,"H","XD",None,None),
 ("E","EV-57A_golden-bracelet-child",8,"H","XD","NOV 2024",None),
 ("C","C-57",6,"-","BLK",None,None),                            # interrupt 3 (DNA, silence)
 ("C","C-58",10,"-","XD",None,None),                            # the line
 ("E","EV-59A_carbonised-figs",10,"H","XD",None,"C-59"),
 ("E","EV-60A_charcoal-inscription",8,"H","XD",None,"C-60"),
 ("E","EV-61A_victim-skeleton",10,"PI","XD","APR 2026",None),
 # --- CH9 · IBRAH --------------------------------------------------------
 ("R","S9-61a_lupanar-empty",10,"PI","XD","HIDE","RED-18"),
 ("C","C-61b",24,"-","XD",None,None),
 ("R","S9-61c_overturned-ruin",22,"H","XD",None,"C-61c"),
 ("C","C-61d",22,"-","XD",None,None),
 # --- CH10 · ENDING (full circle) ----------------------------------------
 ("R","S1-07B_golden-lane",10,"PI","XD",None,None),
 ("R","S1-01A_bread-man-bakery",4,"KB","XD",None,None),
 ("R","S1-02A_thermopolium-argument",4,"KB","XD",None,None),
 ("R","S1-04A_gladiator",4,"KB","XD",None,None),
 ("R","S1-04B_school-boy",4,"KB","XD",None,None),
 ("R","S1-03A_horse-groomed",4,"KB","XD",None,None),
 ("E","EV-52B_horse-cast",15,"H","XD",None,None),               # final match: cast ...
 ("R","S1-03A_horse-groomed",15,"PI","XD",None,None),           # ... -> living horse (ibrah)
 ("C","C-65",14,"-","XD",None,None),
]

# ---------------------------------------------------------------------------
# CARD / OVERLAY fragments.  kind: scene=full parchment · takeover=full dark ·
# overlay=transparent over photo. `html` = inner content.
# ---------------------------------------------------------------------------
CARDS = {
 "C-06": ("overlay",
    '<div class="text title-scrim"><h1 class="title-main rl">POMPEII KA<br>AKHRI DIN</h1>'
    '<div class="title-rule rl"></div>'
    '<p class="title-sub rl">Jab pura shehar ek raat ma patthar ban gaya</p></div>'),
 "C-07": ("scene",
    '<p class="card-l1 rl">ERUPTION NAHI.</p>'
    '<p class="card-l2 rl">US SA PEHLI SUBAH.</p>'
    '<p class="card-foot rl">— us subah ki kahani</p>'),
 "C-08": ("scene",
    '<div class="cmap"><div class="cmap-t rl">ROMAN EMPIRE</div>'
    '<div class="cmap-bay rl">KHAARI-E-NAPLES · Bay of Naples</div>'
    '<div class="cmap-pin rl"><span class="pin"></span> POMPEII</div>'
    '<div class="cmap-date rl">79 AD</div></div>'),
 "C-11": ("overlay",
    '<div class="voldef"><p class="vd-head rl">volcano</p><p class="vd-lat rl">— Latin, 79 AD —</p>'
    '<p class="vd-line rl"></p><p class="vd-q rl">?</p>'
    '<p class="vd-cap rl">is lafz ka koi wajood hi nahi tha.</p></div>'),
 "C-16": ("overlay",
    '<div class="graff"><p class="gf rl">“C · IVLIVM · POLYBIVM” &nbsp;→&nbsp; “Polybius ko vote do.”</p>'
    '<p class="gf rl">“HIC FVI” &nbsp;→&nbsp; “Ma yahan tha.”</p>'
    '<p class="gf rl">“…ne yahan pyaar likha.”</p>'
    '<p class="gf-foot rl">2000 saal — insan kabhi nahi badla.</p></div>'),
 "C-22": ("scene",
    '<div class="cal"><p class="cal-a rl">24 AUG&nbsp;?</p><p class="cal-b rl">24 OCT&nbsp;?</p>'
    '<p class="stamp rl">AKHIR MA</p></div>'),
 "C-24": ("overlay",
    '<div class="scalec"><div class="bars"><div class="bar bar-plane"><span>JAHAAZ ✈</span><b>~10 km</b></div>'
    '<div class="bar bar-col"><span>ERUPTION COLUMN</span><b>33 km</b></div></div>'
    '<p class="scap rl">Jahan se jahaaz urta ha — us se ~3 guna upar.</p></div>'),
 "C-25": ("overlay",
    '<div class="pquote"><p class="pq-map rl">MISENUM &nbsp;•——~30 km——•&nbsp; VESUVIUS</p>'
    '<p class="pq rl">“Badal ki shakal cheer ke darakht jaisi thi —</p>'
    '<p class="pq rl">lamba tana, upar ja kar phailti hui shakhain.”</p>'
    '<p class="pq-at rl">— Pliny, 17 saal · Misenum</p></div>'),
 "C-28": ("overlay",
    '<div class="decide"><p class="dec rl">BHAAGO … <span>ya CHHUPO?</span></p></div>'),
 "C-33": ("scene",
    '<div class="quote2"><p class="q-lat rl">FORTES FORTUNA IUVAT</p>'
    '<p class="q-ur rl">“Qismat bahadur ka sath hoti ha.”</p>'
    '<p class="q-at rl">— Pliny (Roman navy admiral)</p></div>'),
 "C-36": ("scene",
    '<div class="phys"><div class="roof"><div class="pumice"></div><div class="tiles"></div>'
    '<span class="arw">▼</span><span class="arw">▼</span><span class="arw">▼</span></div>'
    '<p class="phys-big rl">100+ KG / m²</p>'
    '<p class="phys-cap rl">Har square meter par 100 kilo se zyada wazan — chhatain gir gayin.</p></div>'),
 "C-37": ("overlay",
    '<div class="pyro"><p class="py-h rl">PYROCLASTIC FLOW</p><p class="py rl">= aag + gas + raakh</p>'
    '<p class="py rl">· ~500 °C</p><p class="py rl">· 100+ km/h</p>'
    '<p class="py rl">· bhaagna namumkin</p></div>'),
 "C-38": ("scene",
    '<div class="cmap"><div class="cmap-t rl">VESUVIUS</div>'
    '<div class="surge rl">⟶ &nbsp;pehla nishana</div>'
    '<div class="cmap-pin rl"><span class="pin"></span> HERCULANEUM</div></div>'),
 "C-49": ("overlay",
    '<div class="loopres"><p class="lr rl">Wo mashhoor “laashain”…</p>'
    '<p class="lr lr-hi rl">asal ma laashain nahi hain.</p></div>'),
 "C-50": ("scene",
    '<div class="fio"><p class="fio-h rl">FIORELLI METHOD — 1863</p>'
    '<div class="step rl"><b>1</b> Khokhla gap dhoondo <i>(raakh ma jism ka sancha)</i></div>'
    '<div class="step rl"><b>2</b> Plaster daalo</div>'
    '<div class="step rl"><b>3</b> Set hona do</div>'
    '<div class="step rl"><b>4</b> Raakh hatao → shakl saamne</div></div>'),
 "C-57": ("takeover",
    '<div class="dna"><p class="dna-1 rl">DNA: MARD.</p><p class="dna-2 rl">KOI RISHTA NAHI.</p>'
    '<p class="dna-3 rl">“Maa or bacha” — 100 saal ka sach ulat gaya.</p></div>'),
 "C-58": ("takeover",
    '<div class="dna"><p class="dna-line rl">Ek ajnabi mard ne… kisi aur ke bache ko chhupaya.</p></div>'),
 "C-59": ("overlay",
    '<div class="chk"><p class="chk-h rl">24 AUGUST?</p>'
    '<p class="ck rl">Khazaan ka phal — anaar, akhrot, anjeer <span class="x">✗</span></p>'
    '<p class="ck rl">Garam ooni kapre <span class="x">✗</span></p>'
    '<p class="ck-cc rl">→ ya to garmi nahi… ya August nahi.</p></div>'),
 "C-60": ("overlay",
    '<div class="dstamp"><p class="ds-dec rl">“XVI K NOV” &nbsp;→&nbsp; 17 OCTOBER, 79 AD</p>'
    '<p class="ds-stamp rl">17 OCT 79 ✓</p>'
    '<p class="ds-cap rl">Charcoal jaldi mit jata ha → usi saal likha. Case closed — August nahi.</p></div>'),
 "C-61b": ("scene",
    '<div class="quran"><p class="qr-ref rl">Ar-Rum 30:9 · Muhammad 47:10</p>'
    '<p class="qr rl">“Kya ya zameen ma chal phir kar nahi dekhte</p>'
    '<p class="qr rl">ka un se pehle walon ka anjaam kya hua?</p>'
    '<p class="qr rl">Wo in se zyada taaqatwar thay, zyada aabaad —</p>'
    '<p class="qr rl">phir jab hadd paar ki, to mit gaye.</p>'
    '<p class="qr rl">Allah ne un par zulm nahi kiya —</p>'
    '<p class="qr rl">unho ne khud apni jaanon par zulm kiya.”</p></div>'),
 "C-61c": ("overlay",
    '<div class="quran quran-ov"><p class="qr-ref rl">Al-Ankabut 29:34–35 · Hud 11:82</p>'
    '<p class="qr rl">“…phir hum ne us basti ko ulat diya — upar ka hissa neeche —</p>'
    '<p class="qr rl">or un par paki hui mitti ke patthar barsaye.</p>'
    '<p class="qr rl">Or hum ne us ma aql walon ke liye ek khuli nishani chhod di.”</p></div>'),
 "C-61d": ("scene",
    '<div class="sodoma"><p class="sd rl">SODOMA</p><p class="sd rl">GOMORA</p>'
    '<p class="sd-cap rl">— House IX.1.26, Pompeii. Kisi zinda bachne wale ne isi raakh ma likha tha.</p>'
    '<p class="sd-br rl">Us waqt bhi ek insan ne yahan wohi nishani dekhi… jo aaj hum dekh rahe hain.</p></div>'),
 "C-65": ("scene",
    '<div class="outro"><p class="ou-logo rl">POMPEII KA AKHRI DIN</p>'
    '<p class="ou-sub rl">SUBSCRIBE</p>'
    '<p class="ou-teaser rl">Agli video — ek aur subah, ek aur shehar.</p></div>'),
 "LBL-62": ("overlay", '<div class="lbl rl">62 AD — ZALZALA</div>'),
 "RED-18": ("overlay", '<div class="redact"><span class="rb rl"></span><span class="r18 rl">18+</span></div>'),
}

# ---------------------------------------------------------------------------
# Compute start times.  XD/MATCH/EMB overlap 1.0s; hard cuts (CUT/BLK/WHITE) no overlap.
# ---------------------------------------------------------------------------
OVERLAP = {"XD":1.0, "EMB":1.0}          # dissolves overlap; CUT/BLK/WHITE/NONE do not

# --- VO RELOCK (segment-level sync) ---------------------------------------
# The silent draft's `dur`s are frame.md guesses. The film runs to the recorded
# Roman-Urdu VO (~19:55). We sync at SEGMENT granularity (not just per-chapter):
# within each chapter we predict where each script segment's narration ends from
# its Roman-Urdu char length, snap that boundary to a REAL silence pause detected
# in the audio (so dramatic [pause]/[long pause] beats are respected), then split
# each segment's audio span across its scenes by their frame.md ratios. This kills
# the within-chapter drift where visuals lagged the voice. Chapter spans still equal
# their VO clip length exactly, so audio stays back-to-back.
import subprocess
AUDIO_DIR = os.path.join(HERE, "assets", "audio")
VO = [  # (file, first_scene_idx, last_scene_idx)   — contiguous, segment-aligned
    ("pompeii-hook-01-07-v3.mp3",    0,  13),   # segs 01-07
    ("pompeii-ch2-08-12-v3.mp3",    14,  22),   # segs 08-12
    ("pompeii-ch3-13-18-v3.mp3",    23,  32),   # segs 13-18
    ("pompeii-ch4-19-22-B-v3.mp3",  33,  38),   # segs 19-22
    ("pompeii-ch5-23-30-B-v3.mp3",  39,  50),   # segs 23-30
    ("pompeii-ch6-31-39-B-v3.mp3",  51,  62),   # segs 31-39
    ("pompeii-ch7-40-46-B-v3.mp3",  63,  70),   # segs 40-46
    ("pompeii-ch8-47-53-B-v3.mp3",  71,  81),   # segs 47-53
    ("pompeii-ch9-54-61-B-v3.mp3",  82,  90),   # segs 54-61
    ("pompeii-ch10-61a-65-B-v3.mp3",91, 103),   # segs 61a-65
]

# scene index -> script segment id (hand-verified vs storyboard; CH7/8/10 callbacks
# and the collapsed CH6-10 blocks reconciled). "41+42" = the held silence interrupt
# scene that covers two script segments.
SEG = (
    ["01","01","02","02","03","03","04","04","05","05","06","07","07","07"]
  + ["08","09","09","09","10","10","11","12","12"]
  + ["13","14","14","14","15","15","16","17","18","18"]
  + ["19","19","19","20","21","22"]
  + ["23","23","24","25","26","26","27","27","28","29","29","30"]
  + ["31","31","32","33","34","35","36","37","38","38","38","39"]
  + ["40","40","41+42","43","43","44","45","46"]
  + ["47","47","47","48","48","49","50","51","52","52","53"]
  + ["54","55","55","56","57","58","59","60","61"]
  + ["61a","61b","61c","61d","62","63","63","63","64","64","64","64","65"]
)
# --- Optional single-chapter build:  python3 build.py --chapter N  ---------
# Slices the EDL to chapter N (re-indexed from s00, clock from 0) so HyperFrames
# renders just that chapter. Final film = the chapter renders joined in order.
import sys
CHAPTER = int(sys.argv[sys.argv.index("--chapter") + 1]) if "--chapter" in sys.argv else None
if CHAPTER:
    _f, _a, _b = VO[CHAPTER - 1]
    S = [list(sc) for sc in S[_a:_b + 1]]; SEG = SEG[_a:_b + 1]
    S[0][4] = "NONE"                     # standalone chapter: no transition into s00
    VO = [(_f, 0, _b - _a)]

# Roman-Urdu spoken-length per segment (letters only), from script-v1-urdu.md — the
# narration-duration prior. Frozen here to keep the build self-contained; re-derive
# if the VO script changes. (tools note: grep '^\*\*NN\*\*' the urdu master.)
WEIGHTS = {'01':72,'02':77,'03':122,'04':110,'05':105,'06':89,'07':275,'08':137,
 '09':120,'10':174,'11':167,'12':171,'13':55,'14':190,'15':152,'16':204,'17':113,
 '18':200,'19':171,'20':156,'21':98,'22':151,'23':29,'24':142,'25':178,'26':161,
 '27':167,'28':86,'29':207,'30':157,'31':118,'32':120,'33':182,'34':167,'35':128,
 '36':183,'37':250,'38':230,'39':147,'40':171,'41':62,'42':31,'43':138,'44':133,
 '45':153,'46':204,'47':125,'48':167,'49':106,'50':187,'51':152,'52':262,'53':182,
 '54':139,'55':194,'56':98,'57':156,'58':85,'59':252,'60':213,'61':137,'61a':317,
 '61b':282,'61c':203,'61d':286,'62':83,'63':139,'64':286,'65':158}
MIN_SPAN = {"23": 4.0}   # blast interrupt: char-count can't see its silent beat — hold
                         # the eruption until "pahar phat gaya" is spoken.
SNAP_TOL = 1.6           # max s a predicted boundary may snap to a silence pause
# Creator-locked segment starts (audio-local seconds within the chapter), from the
# timeline-v3.md proof-watch (2026-07-17, all 10 chapters). These override
# predict+snap outright. Derived as: creator's global time − the chapter's real
# VO start (cumulative clip durations) — the doc's own chapter-head rows drifted
# where the creator chained them from edited earlier chapters, so they're not used.
FIX_START = {
 '02':7.0,'03':14.5,'04':25.5,'05':37.5,'06':49.0,'07':61.5,                          # CH1
 '09':13.6,'10':25.6,'11':41.4,'12':61.3,                                             # CH2
 '14':6.2,'15':27.1,'16':42.2,'17':64.2,'18':77.4,                                    # CH3
 '20':18.4,'21':36.2,'22':48.1,                                                       # CH4
 '24':4.3,'25':19.1,'26':38.0,'27':55.6,'28':72.8,'29':83.0,'30':106.0,               # CH5
 '32':15.7,'33':30.0,'34':50.5,'35':66.4,'36':78.5,'37':97.2,'38':125.0,'39':146.6,   # CH6
 '41+42':18.6,'43':31.5,'44':45.6,'45':61.7,'46':80.7,                                # CH7
 '48':18.0,'49':39.4,'50':49.6,'51':68.2,'52':88.6,'53':115.2,                        # CH8
 '55':18.5,'56':37.9,'57':48.9,'58':65.6,'59':74.8,'60':102.2,'61':126.1,             # CH9
 '61b':36.1,'61c':66.6,'61d':90.7,'62':120.3,'63':131.6,'64':147.0,'65':179.6,        # CH10
}

def probe_dur(path):
    return float(subprocess.check_output(
        ["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0", path]).strip())

def silence_mids(path, noise="-33dB", mind=0.30):
    """Midpoints of detected silence gaps in `path` (structural pauses)."""
    out = subprocess.run(["ffmpeg","-hide_banner","-nostats","-i",path,
        "-af",f"silencedetect=noise={noise}:d={mind}","-f","null","-"],
        capture_output=True, text=True).stderr
    mids, st = [], None
    for ln in out.splitlines():
        if "silence_start:" in ln:
            st = float(ln.split("silence_start:")[1])
        elif "silence_end:" in ln and st is not None:
            en = float(ln.split("silence_end:")[1].split("|")[0])
            mids.append((st + en) / 2.0); st = None
    return sorted(mids)

def seg_weight(sid):
    return sum(WEIGHTS[s] for s in sid.split("+"))

RAW = [float(sc[2]) for sc in S]                  # frame.md guesses (within-segment ratios)
DUR = [0.0] * len(S)
def _follow_overlap(i):                            # overlap the NEXT scene's transition steals
    nxt = S[i+1][4] if i+1 < len(S) else "NONE"
    return OVERLAP.get(nxt, 0.0)

VO_DUR = {}
for fname, a, b in VO:
    V = probe_dur(os.path.join(AUDIO_DIR, fname)); VO_DUR[fname] = V
    gaps = silence_mids(os.path.join(AUDIO_DIR, fname))
    # ordered segments in this chapter + their scenes
    seg_ids, seg_scene = [], {}
    for i in range(a, b + 1):
        s = SEG[i]
        if not seg_ids or seg_ids[-1] != s:
            seg_ids.append(s); seg_scene[s] = []
        seg_scene[s].append(i)
    weights = [seg_weight(s) for s in seg_ids]; tot = sum(weights)
    pred, acc = [], 0.0
    for w in weights:
        acc += w; pred.append(V * acc / tot)
    # boundary time (audio-local) at the end of each segment: snap to nearest silence
    times, used = [0.0], set()
    for k in range(len(seg_ids) - 1):
        if seg_ids[k + 1] in FIX_START:            # creator-locked boundary wins
            times.append(FIX_START[seg_ids[k + 1]]); continue
        p = pred[k]; span_pred = pred[k] - (pred[k-1] if k else 0.0)
        floor = times[-1] + max(0.3, 0.65 * span_pred, MIN_SPAN.get(seg_ids[k], 0.0))
        best, bd = None, SNAP_TOL
        for gi, mid in enumerate(gaps):
            if gi in used or mid <= floor:
                continue
            if abs(mid - p) < bd:
                bd, best = abs(mid - p), gi
        if best is not None:
            times.append(gaps[best]); used.add(best)
        else:
            times.append(max(p, times[-1] + 0.3))
    times.append(V)
    # split each segment's [t0,t1] span across its scenes by frame.md ratios, then add
    # back each scene's trailing dissolve so the chapter's wall-clock span == V.
    for k, s in enumerate(seg_ids):
        t0, t1 = times[k], times[k + 1]; span = t1 - t0
        sc_idx = seg_scene[s]; rr = [RAW[i] for i in sc_idx]; rs = sum(rr)
        for j, i in enumerate(sc_idx):
            DUR[i] = round(span * rr[j] / rs + _follow_overlap(i), 3)

scenes = []
t = 0.0
for i, sc in enumerate(S):
    kind, ref, dur, motion, trans, chip, ov = sc
    dur = DUR[i]                                   # relocked duration
    scenes.append(dict(i=i, id=f"s{i:02d}", kind=kind, ref=ref, dur=float(dur),
                       motion=motion, trans=trans, chip=chip, ov=ov, start=round(t, 3)))
    # advance clock by this scene, minus the overlap of the NEXT scene's transition
    t += float(dur) - _follow_overlap(i)
TOTAL = round(t, 2)

# --- AUDIO ELEMENTS (direct #root children; HyperFrames muxes at render) ----
# 10 VO clips back-to-back (each starts on its chapter's first scene) + a low
# atmospheric drone bed under the whole film, ducked to silence during the
# pre-dawn pattern-interrupt (scene s65, seg 41-42).
_audio = []
for k, (fname, a, b) in enumerate(VO):
    start = scenes[a]["start"]
    end = scenes[VO[k+1][1]]["start"] if k + 1 < len(VO) else TOTAL
    clip_dur = round(end - start - 0.02, 3)   # 20ms gap → clips never overlap (float-safe, inaudible)
    _audio.append(
        f'<audio id="vo{k}" src="assets/audio/{fname}" data-start="{start}" '
        f'data-duration="{clip_dur}" data-track-index="20" data-volume="1"></audio>')
_audio.append(
    f'<audio id="drone" src="assets/audio/pompeii-drone-bed.mp3" data-start="0" '
    f'data-duration="{TOTAL}" data-track-index="21" data-volume="0.11"></audio>')
audio_html = "\n      ".join(_audio)
_sil = next((sc for sc in scenes if SEG[sc["i"]] == "41+42"), None)   # pre-dawn hush (S6-41A); None in chapter builds without it

# ---------------------------------------------------------------------------
# Emit HTML
# ---------------------------------------------------------------------------
def section_html(sc):
    sid = sc["id"]
    if sc["kind"] == "C":
        kindc, inner = CARDS[sc["ref"]]
        cls = "card" if kindc == "scene" else ("takeover" if kindc == "takeover" else "overlaybox")
        body = f'<div class="scene-inner" id="{sid}-inner"><div class="{cls}" id="{sid}-card">{inner}</div></div>'
    else:
        path = resolve(sc["ref"])
        evcls = " ev" if sc["kind"] == "E" else ""
        body = (f'<div class="scene-inner" id="{sid}-inner">'
                f'<div class="photo{evcls}" id="{sid}-photo"><img src="{path}" alt=""></div>'
                f'<div class="grade"></div>')
        if sc["ov"]:
            okind, oinner = CARDS[sc["ov"]]
            body += f'<div class="ov ov-{sc["ov"].lower()}" id="{sid}-ov">{oinner}</div>'
        body += "</div>"
    ti = (sc["i"] % 2) + 1
    return (f'<section id="{sid}" class="scene clip" data-start="{sc["start"]}" '
            f'data-duration="{sc["dur"]}" data-track-index="{ti}">{body}</section>')

# chip elements: one per (value, time)
chip_events = []   # (idx, value, time)
for sc in scenes:
    if sc["chip"] is None:
        continue
    if sc["chip"] == "HIDE":
        chip_events.append((len(chip_events), None, sc["start"] + 0.2))
    elif isinstance(sc["chip"], list):
        n = len(sc["chip"]); span = max(sc["dur"] - 1.0, 1.0)
        for k, v in enumerate(sc["chip"]):
            chip_events.append((len(chip_events), v, round(sc["start"] + 0.3 + k * span / n, 3)))
    else:
        chip_events.append((len(chip_events), sc["chip"], round(sc["start"] + 0.3, 3)))

chip_divs = "".join(
    f'<div class="chip" id="chip{idx}">{v}</div>' for idx, v, _ in chip_events if v is not None)

# timeline JS
js = []
inner_ids = ",".join(f'"#{sc["id"]}-inner"' for sc in scenes)
js.append(f'gsap.set([{inner_ids}], {{opacity:0}});')
js.append('gsap.set("#s00-inner", {opacity:1});')

MOT = {"PI":"pin","PB":"pback","TU":"tup","H":"hold"}
for sc in scenes:
    sid = sc["id"]; st = sc["start"]; du = sc["dur"]
    # transition INTO this scene
    prev = f'"#s{sc["i"]-1:02d}-inner"' if sc["i"] > 0 else "null"
    cur = f'"#{sid}-inner"'
    tr = sc["trans"]
    if tr in ("XD",):     js.append(f'xd({prev},{cur},{st});')
    elif tr == "EMB":     js.append(f'emb({prev},{cur},{st});')
    elif tr == "CUT":     js.append(f'cut({prev},{cur},{st});')
    elif tr == "BLK":     js.append(f'blk({prev},{cur},{st});')
    elif tr == "WHITE":   js.append(f'wht({prev},{cur},{st});')
    # NONE: first scene already opacity 1
    # motion
    if sc["kind"] in ("R", "E"):
        m = sc["motion"]
        if m in ("KB","PX","DR"):
            js.append(f'kb("#{sid}-photo",{st},{du},{1 if sc["i"]%2==0 else -1});')
        elif m in MOT:
            js.append(f'{MOT[m]}("#{sid}-photo",{st},{du});')
        # LK = locked, no motion
    # overlay reveal
    if sc["ov"]:
        js.append(f'rvl("#{sid}-ov",{round(st+0.6,3)});')
    # card scene reveal
    if sc["kind"] == "C":
        js.append(f'rvl("#{sid}-card",{round(st+0.25,3)});')

# chip cross-fades
prev_chip = None
for idx, v, tm in chip_events:
    if v is None:
        if prev_chip is not None:
            js.append(f'fout("#{prev_chip}",{tm},0.4);'); prev_chip = None
        continue
    js.append(f'fin("#chip{idx}",{tm},0.5);')
    if prev_chip is not None:
        js.append(f'fout("#{prev_chip}",{tm},0.4);')
    prev_chip = f"chip{idx}"

# drone duck: fall to silence for the pre-dawn hush (s65), lift back as it ends
if _sil:
    js.append(f'tl.to("#drone",{{volume:0.0,duration:0.9,ease:"power2.out"}},{round(_sil["start"]+0.4,3)});')
    js.append(f'tl.to("#drone",{{volume:0.11,duration:1.4,ease:"power2.in"}},{round(_sil["start"]+_sil["dur"]-1.2,3)});')

sections = "\n      ".join(section_html(sc) for sc in scenes)
timeline = "\n      ".join(js)

HTML = f'''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=1920, height=1080">
    <title>Pompeii Ka Akhri Din — full composition (silent draft)</title>
    <script src="assets/gsap.min.js"></script>
    <style>
      @font-face{{font-family:"Inter";font-weight:600;font-display:swap;src:url("assets/fonts/Inter-600.woff2") format("woff2");}}
      @font-face{{font-family:"Inter";font-weight:700;font-display:swap;src:url("assets/fonts/Inter-700.woff2") format("woff2");}}
      @font-face{{font-family:"Inter";font-weight:800;font-display:swap;src:url("assets/fonts/Inter-800.woff2") format("woff2");}}
      @font-face{{font-family:"Playfair Display";font-weight:500;font-display:swap;src:url("assets/fonts/PlayfairDisplay-Normal.woff2") format("woff2");}}
      @font-face{{font-family:"Playfair Display";font-weight:700;font-display:swap;src:url("assets/fonts/PlayfairDisplay-Normal.woff2") format("woff2");}}
      @font-face{{font-family:"Playfair Display";font-style:italic;font-weight:500;font-display:swap;src:url("assets/fonts/PlayfairDisplay-Italic.woff2") format("woff2");}}
      :root{{--paper:#0d0f12;--ink:#f4f1ea;--ink-soft:rgba(244,241,234,0.82);--parchment:#e8dcc0;--parch-ink:#2a2118;--pompeii-red:#9c342a;--ash:#8a8578;--ember:#d8863a;}}
      *{{box-sizing:border-box;}}
      body{{margin:0;background:#000;font-family:"Inter",system-ui,sans-serif;}}
      #root{{position:relative;width:1920px;height:1080px;overflow:hidden;background:var(--paper);}}
      .scene{{position:absolute;inset:0;}}
      .scene-inner{{position:absolute;inset:0;will-change:opacity;}}
      .photo{{position:absolute;inset:-7%;background:#15140f;filter:saturate(1.03) contrast(1.06) brightness(0.98);will-change:transform;}}
      .photo img{{width:100%;height:100%;object-fit:cover;}}
      /* EVIDENCE grade: desaturate + slight cool */
      .photo.ev{{filter:grayscale(.35) contrast(1.05) brightness(.96) saturate(.85) hue-rotate(-6deg);}}
      .grade{{position:absolute;inset:0;background:radial-gradient(120% 100% at 50% 42%,rgba(216,134,58,0.05),rgba(13,15,18,0.0) 45%,rgba(13,15,18,0.30) 100%);mix-blend-mode:multiply;pointer-events:none;}}
      #ov-vignette{{position:absolute;inset:0;pointer-events:none;background:radial-gradient(130% 100% at 50% 45%,transparent 55%,rgba(0,0,0,0.42) 100%);}}
      #ov-grain{{position:absolute;inset:0;pointer-events:none;opacity:0.10;mix-blend-mode:overlay;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='140' height='140'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>");}}
      #ov-bloom{{position:absolute;inset:0;pointer-events:none;background:#f7f2e8;opacity:0;}}
      #ov-ember{{position:absolute;inset:0;pointer-events:none;background:radial-gradient(70% 60% at 50% 60%,rgba(216,134,58,0.55),rgba(156,52,42,0.15) 70%,transparent 100%);opacity:0;}}
      #ov-black{{position:absolute;inset:0;pointer-events:none;background:#000;opacity:0;}}
      /* timestamp chip */
      .chip{{position:absolute;left:64px;bottom:60px;opacity:0;font-family:"Inter";font-weight:700;font-size:26px;letter-spacing:.16em;text-transform:uppercase;color:var(--ink);background:rgba(13,19,24,0.55);padding:10px 18px;border-radius:4px;backdrop-filter:blur(1px);}}
      /* title */
      .text{{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;align-items:center;padding:0 180px;}}
      .text.title-scrim{{background:radial-gradient(60% 50% at 50% 50%,rgba(0,0,0,0.66),rgba(0,0,0,0.0) 74%);}}
      .title-main{{font-family:"Playfair Display";font-weight:700;font-size:118px;line-height:.98;color:var(--ink);text-align:center;text-shadow:0 6px 44px rgba(0,0,0,.7);margin:0;}}
      .title-sub{{font-family:"Inter";font-weight:600;font-size:34px;letter-spacing:.02em;color:var(--ink);margin:22px 0 0;text-align:center;text-shadow:0 3px 22px rgba(0,0,0,0.9);}}
      .title-rule{{width:120px;height:3px;background:var(--pompeii-red);margin:26px 0 0;}}
      /* parchment card */
      .card,.overlaybox{{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;background:var(--parchment);background-image:radial-gradient(90% 70% at 50% 40%,rgba(255,255,255,0.25),rgba(156,52,42,0.05) 100%);}}
      .card::after{{content:"";position:absolute;inset:0;opacity:0.12;mix-blend-mode:multiply;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><filter id='p'><feTurbulence type='fractalNoise' baseFrequency='0.6' numOctaves='3'/></filter><rect width='100%25' height='100%25' filter='url(%23p)'/></svg>");}}
      .card>*,.overlaybox>*,.takeover>*{{position:relative;z-index:1;}}
      .card-l1{{font-family:"Inter";font-weight:800;font-size:64px;letter-spacing:.02em;color:var(--parch-ink);opacity:.55;margin:0;}}
      .card-l2{{font-family:"Inter";font-weight:800;font-size:88px;color:var(--pompeii-red);margin:8px 0 0;}}
      .card-foot{{font-family:"Inter";font-weight:600;font-size:30px;color:var(--parch-ink);opacity:.6;margin:34px 0 0;}}
      .rl{{opacity:0;}}
      /* full-dark takeover (DNA / the line) */
      .takeover{{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;background:#0a0c0e;padding:0 220px;}}
      .dna-1{{font-family:"Inter";font-weight:800;font-size:96px;color:var(--ink);margin:0;letter-spacing:.02em;}}
      .dna-2{{font-family:"Inter";font-weight:800;font-size:96px;color:#d65a49;margin:6px 0 0;}}
      .dna-3{{font-family:"Inter";font-weight:600;font-size:34px;color:var(--ink-soft);margin:40px 0 0;}}
      .dna-line{{font-family:"Playfair Display";font-style:italic;font-weight:500;font-size:60px;line-height:1.2;color:var(--ink);margin:0;}}
      /* overlays over photos */
      .ov{{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:0 160px;}}
      .lbl{{position:absolute;left:64px;top:60px;font-family:"Inter";font-weight:700;font-size:24px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink);background:rgba(13,19,24,0.55);padding:9px 16px;border-radius:4px;}}
      .ov-lbl-62{{justify-content:flex-start;align-items:flex-start;}}
      /* map card */
      .cmap{{color:var(--parch-ink);}}
      .cmap-t{{font-family:"Inter";font-weight:800;font-size:40px;letter-spacing:.16em;opacity:.5;}}
      .cmap-bay{{font-family:"Inter";font-weight:700;font-size:30px;letter-spacing:.06em;margin-top:26px;opacity:.7;}}
      .cmap-pin{{font-family:"Inter";font-weight:800;font-size:78px;color:var(--pompeii-red);margin-top:22px;display:flex;align-items:center;gap:22px;justify-content:center;}}
      .pin{{width:26px;height:26px;border-radius:50% 50% 50% 0;background:var(--pompeii-red);transform:rotate(-45deg);display:inline-block;}}
      .cmap-date{{font-family:"Inter";font-weight:700;font-size:28px;letter-spacing:.2em;margin-top:30px;opacity:.55;}}
      .surge{{font-family:"Inter";font-weight:800;font-size:34px;color:var(--ember);letter-spacing:.06em;margin-top:22px;}}
      /* volcano dictionary */
      .voldef{{background:rgba(232,220,192,0.94);padding:70px 90px;border-radius:6px;box-shadow:0 20px 80px rgba(0,0,0,.5);}}
      .vd-head{{font-family:"Playfair Display";font-weight:700;font-size:82px;color:var(--parch-ink);margin:0;}}
      .vd-lat{{font-family:"Inter";font-style:italic;font-weight:600;font-size:26px;color:var(--parch-ink);opacity:.6;margin:4px 0 0;}}
      .vd-line{{width:520px;height:3px;background:var(--parch-ink);opacity:.4;margin:34px auto 0;}}
      .vd-q{{font-family:"Playfair Display";font-weight:700;font-size:70px;color:var(--pompeii-red);margin:18px 0 0;}}
      .vd-cap{{font-family:"Inter";font-weight:600;font-size:28px;color:var(--parch-ink);opacity:.7;margin:22px 0 0;}}
      /* graffiti */
      .graff{{background:rgba(13,15,18,0.5);padding:56px 70px;border-radius:6px;}}
      .gf{{font-family:"Inter";font-weight:700;font-size:38px;color:var(--ink);margin:0 0 20px;}}
      .gf-foot{{font-family:"Inter";font-weight:800;font-size:32px;color:var(--ember);margin:22px 0 0;}}
      /* calendar */
      .cal{{background:rgba(232,220,192,0.94);padding:60px 120px;border-radius:6px;box-shadow:0 20px 80px rgba(0,0,0,.5);}}
      .cal-a{{font-family:"Inter";font-weight:800;font-size:64px;color:var(--parch-ink);opacity:.4;margin:0;}}
      .cal-b{{font-family:"Inter";font-weight:800;font-size:80px;color:var(--parch-ink);margin:14px 0 0;}}
      .stamp{{font-family:"Inter";font-weight:800;font-size:56px;color:var(--pompeii-red);border:5px solid var(--pompeii-red);padding:10px 34px;transform:rotate(-6deg);margin:40px 0 0;border-radius:6px;}}
      /* scale */
      .scalec{{background:rgba(13,15,18,0.5);padding:44px 70px;border-radius:6px;}}
      .bars{{display:flex;gap:90px;align-items:flex-end;justify-content:center;height:420px;}}
      .bar{{display:flex;flex-direction:column;justify-content:flex-end;align-items:center;color:var(--ink);font-family:"Inter";}}
      .bar span{{font-weight:700;font-size:24px;letter-spacing:.05em;margin-bottom:12px;}}
      .bar b{{font-weight:800;font-size:40px;color:var(--ember);}}
      .bar-plane{{width:150px;}}.bar-plane::after{{content:"";width:150px;height:120px;background:rgba(244,241,234,0.35);border-radius:4px;margin-top:12px;}}
      .bar-col{{width:150px;}}.bar-col::after{{content:"";width:150px;height:380px;background:linear-gradient(180deg,#d8863a,#9c342a);border-radius:4px 4px 0 0;margin-top:12px;}}
      .scap{{font-family:"Inter";font-weight:600;font-size:30px;color:var(--ink);margin:26px 0 0;}}
      /* pliny quote */
      .pquote{{background:rgba(13,15,18,0.55);padding:50px 70px;border-radius:6px;max-width:1200px;}}
      .pq-map{{font-family:"Inter";font-weight:700;font-size:28px;letter-spacing:.1em;color:var(--ink-soft);margin:0 0 30px;}}
      .pq{{font-family:"Playfair Display";font-style:italic;font-weight:500;font-size:46px;line-height:1.25;color:var(--ink);margin:0;}}
      .pq-at{{font-family:"Inter";font-weight:600;font-size:26px;color:var(--ink-soft);margin:28px 0 0;}}
      /* decision */
      .dec{{font-family:"Inter";font-weight:800;font-size:110px;color:var(--ink);text-shadow:0 6px 40px rgba(0,0,0,.8);margin:0;}}
      .dec span{{color:var(--pompeii-red);}}
      /* quote card */
      .q-lat{{font-family:"Playfair Display";font-weight:700;font-size:76px;color:var(--ink);margin:0;letter-spacing:.02em;text-shadow:0 4px 30px rgba(0,0,0,.9);}}
      .q-ur{{font-family:"Inter";font-weight:700;font-size:44px;color:#f0b04a;margin:26px 0 0;text-shadow:0 3px 22px rgba(0,0,0,.95);}}
      .q-at{{font-family:"Inter";font-weight:600;font-size:28px;color:var(--ink);opacity:.85;margin:26px 0 0;text-shadow:0 2px 16px rgba(0,0,0,.95);}}
      /* physics */
      .roof{{position:relative;width:520px;height:200px;margin-bottom:20px;}}
      .tiles{{position:absolute;bottom:0;left:0;width:0;height:0;border-left:260px solid transparent;border-right:260px solid transparent;border-bottom:120px solid #9c342a;}}
      .pumice{{position:absolute;top:0;left:60px;right:60px;height:60px;background:#8a8578;border-radius:50%;opacity:.85;}}
      .roof .arw{{position:absolute;top:70px;color:var(--parch-ink);font-size:34px;}}
      .roof .arw:nth-child(3){{left:180px;}}.roof .arw:nth-child(4){{left:250px;}}.roof .arw:nth-child(5){{left:320px;}}
      .phys-big{{font-family:"Inter";font-weight:800;font-size:96px;color:var(--pompeii-red);margin:10px 0 0;}}
      .phys-cap{{font-family:"Inter";font-weight:600;font-size:30px;color:var(--parch-ink);opacity:.75;margin:24px 0 0;}}
      /* pyroclastic */
      .pyro{{background:rgba(13,15,18,0.55);padding:50px 80px;border-radius:6px;}}
      .py-h{{font-family:"Inter";font-weight:800;font-size:60px;color:var(--ember);margin:0 0 24px;letter-spacing:.04em;}}
      .py{{font-family:"Inter";font-weight:700;font-size:40px;color:var(--ink);margin:0 0 12px;}}
      /* loop-resolve */
      .lr{{font-family:"Inter";font-weight:700;font-size:52px;color:var(--ink);margin:0 0 14px;text-shadow:0 4px 30px rgba(0,0,0,.8);}}
      .lr-hi{{color:var(--ember);font-weight:800;font-size:62px;}}
      /* fiorelli */
      .fio-h{{font-family:"Inter";font-weight:800;font-size:48px;color:var(--pompeii-red);letter-spacing:.06em;margin:0 0 36px;}}
      .step{{font-family:"Inter";font-weight:600;font-size:38px;color:var(--parch-ink);margin:0 0 22px;display:flex;align-items:center;gap:22px;}}
      .step b{{display:inline-flex;width:56px;height:56px;border-radius:50%;background:var(--pompeii-red);color:var(--ink);align-items:center;justify-content:center;font-weight:800;font-size:32px;flex:none;}}
      .step i{{font-size:26px;opacity:.6;}}
      /* checklist */
      .chk{{background:rgba(13,15,18,0.55);padding:50px 70px;border-radius:6px;}}
      .chk-h{{font-family:"Inter";font-weight:800;font-size:60px;color:var(--ink);margin:0 0 30px;}}
      .ck{{font-family:"Inter";font-weight:700;font-size:40px;color:var(--ink);margin:0 0 18px;}}
      .ck .x{{color:var(--pompeii-red);font-weight:800;margin-left:14px;}}
      .ck-cc{{font-family:"Inter";font-weight:800;font-size:38px;color:var(--ember);margin:26px 0 0;}}
      /* datestamp */
      .dstamp{{background:rgba(13,15,18,0.55);padding:50px 70px;border-radius:6px;}}
      .ds-dec{{font-family:"Inter";font-weight:700;font-size:44px;color:var(--ink);margin:0 0 26px;}}
      .ds-stamp{{font-family:"Inter";font-weight:800;font-size:72px;color:var(--pompeii-red);border:5px solid var(--pompeii-red);display:inline-block;padding:8px 30px;transform:rotate(-5deg);border-radius:6px;margin:0;}}
      .ds-cap{{font-family:"Inter";font-weight:600;font-size:28px;color:var(--ink-soft);margin:28px 0 0;}}
      /* quran */
      .quran{{max-width:1360px;}}
      .quran-ov{{background:rgba(13,15,18,0.62);padding:50px 80px;border-radius:6px;}}
      .qr-ref{{font-family:"Inter";font-weight:700;font-size:26px;letter-spacing:.14em;color:var(--pompeii-red);margin:0 0 30px;}}
      .qr{{font-family:"Playfair Display";font-weight:500;font-size:44px;line-height:1.3;margin:0 0 8px;}}
      .card .qr{{color:var(--parch-ink);}} .quran-ov .qr{{color:var(--ink);}}
      .qr-note{{font-family:"Inter";font-weight:600;font-size:22px;color:var(--pompeii-red);opacity:.7;margin:30px 0 0;}}
      /* sodoma */
      .sd{{font-family:"Playfair Display";font-weight:700;font-size:96px;color:#3a2c1c;letter-spacing:.06em;margin:0;opacity:.82;}}
      .sd-cap{{font-family:"Inter";font-weight:600;font-size:26px;color:var(--parch-ink);opacity:.6;margin:34px 0 0;}}
      .sd-br{{font-family:"Inter";font-weight:700;font-size:34px;color:var(--pompeii-red);margin:26px 0 0;max-width:1200px;}}
      /* outro */
      .outro{{}}
      .ou-logo{{font-family:"Playfair Display";font-weight:700;font-size:72px;color:var(--parch-ink);margin:0;}}
      .ou-sub{{font-family:"Inter";font-weight:800;font-size:64px;letter-spacing:.1em;color:var(--ink);background:var(--pompeii-red);padding:16px 48px;border-radius:8px;margin:40px 0 0;}}
      .ou-teaser{{font-family:"Inter";font-weight:600;font-size:32px;color:var(--parch-ink);opacity:.7;margin:40px 0 0;}}
      /* redaction (ibrah guardrail) */
      .redact{{position:absolute;inset:0;}}
      .rb{{position:absolute;left:50%;top:52%;transform:translate(-50%,-50%);width:900px;height:200px;background:rgba(10,10,10,0.55);backdrop-filter:blur(26px);border-radius:8px;}}
      .r18{{position:absolute;left:50%;top:52%;transform:translate(-50%,-50%);font-family:"Inter";font-weight:800;font-size:70px;letter-spacing:.1em;color:var(--ink);}}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-width="1920" data-height="1080" data-duration="{TOTAL}" data-fps="30">

      {sections}

      <div id="ov-grain"></div>
      <div id="ov-vignette"></div>
      <div id="ov-ember"></div>
      <div id="ov-bloom"></div>
      <div id="ov-black"></div>
      {chip_divs}
      {audio_html}
    </div>

    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});

      // ---- helpers (deterministic; animate only transform/opacity) ----
      function kb(sel,at,dur,dir){{gsap.set(sel,{{transformOrigin:"50% 50%"}});tl.fromTo(sel,{{scale:1.0,xPercent:dir*-1.4,yPercent:0.6}},{{scale:1.11,xPercent:dir*1.4,yPercent:-0.6,duration:dur,ease:"sine.inOut"}},at);}}
      function pin(sel,at,dur){{gsap.set(sel,{{transformOrigin:"50% 50%"}});tl.fromTo(sel,{{scale:1.02}},{{scale:1.13,duration:dur,ease:"sine.inOut"}},at);}}
      function pback(sel,at,dur){{gsap.set(sel,{{transformOrigin:"50% 50%"}});tl.fromTo(sel,{{scale:1.13}},{{scale:1.0,duration:dur,ease:"sine.inOut"}},at);}}
      function tup(sel,at,dur){{gsap.set(sel,{{transformOrigin:"50% 50%"}});tl.fromTo(sel,{{scale:1.06,yPercent:3.0}},{{scale:1.13,yPercent:-3.0,duration:dur,ease:"sine.inOut"}},at);}}
      function hold(sel,at,dur){{gsap.set(sel,{{transformOrigin:"50% 50%"}});tl.fromTo(sel,{{scale:1.0}},{{scale:1.035,duration:dur,ease:"sine.inOut"}},at);}}
      function xd(from,to,at){{gsap.set(to,{{opacity:0}});tl.to(to,{{opacity:1,duration:1.0,ease:"power1.inOut"}},at);if(from)tl.to(from,{{opacity:0,duration:1.0,ease:"power1.inOut"}},at);}}
      function cut(from,to,at){{if(from)tl.set(from,{{opacity:0}},at);tl.set(to,{{opacity:1}},at);}}
      function blk(from,to,at){{tl.to("#ov-black",{{opacity:1,duration:0.25,ease:"power2.in"}},Math.max(at-0.25,0));if(from)tl.set(from,{{opacity:0}},at);tl.set(to,{{opacity:1}},at);tl.to("#ov-black",{{opacity:0,duration:0.6,ease:"power2.out"}},at+0.45);}}
      function wht(from,to,at){{tl.to("#ov-bloom",{{opacity:1,duration:0.4,ease:"power2.in"}},Math.max(at-0.4,0));if(from)tl.set(from,{{opacity:0}},at);tl.set(to,{{opacity:1}},at);tl.to("#ov-bloom",{{opacity:0,duration:1.3,ease:"power2.out"}},at+0.2);}}
      function emb(from,to,at){{xd(from,to,at);tl.to("#ov-ember",{{opacity:0.5,duration:0.5,ease:"power2.in"}},Math.max(at-0.2,0));tl.to("#ov-ember",{{opacity:0,duration:0.9,ease:"power2.out"}},at+0.4);}}
      function fin(sel,at,dur){{gsap.set(sel,{{opacity:0}});tl.to(sel,{{opacity:1,duration:dur,ease:"power2.out"}},at);}}
      function fout(sel,at,dur){{tl.to(sel,{{opacity:0,duration:dur,ease:"power2.in"}},at);}}
      // reveal a card/overlay container + stagger its .rl lines
      function rvl(sel,at){{fin(sel,at,0.8);tl.to(sel+" .rl",{{opacity:1,duration:0.7,stagger:0.45,ease:"power2.out"}},at+0.2);}}

      {timeline}

      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
'''

out = os.path.join(HERE, "index.html")
with open(out, "w") as f:
    f.write(HTML)

mm = int(TOTAL // 60); ss = TOTAL - mm*60
print(f"wrote {out}")
print(f"scenes: {len(scenes)}  ·  duration: {TOTAL}s  (~{mm}:{ss:04.1f})  ·  fps 30  ·  frames ~{int(TOTAL*30)}")
