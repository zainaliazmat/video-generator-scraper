---
summary: Storyboard SPEC (Gate ②) for «فرعون کا انجام» — one section at a time, creator sign-off per part before mirroring into storyboard.mjs. Part 1 (HOOK segs 01–05) drafted 2026-07-18, scene facts pre-verified. Remaining parts follow the same shot-table format after Part-1 sign-off.
updated: 2026-07-18
source: script [[script-v1-nastaliq]] v2.1 + film rules [[DESIGN]] + template [[../../templates/storyboard-template]]
---

# STORYBOARD — فرعون کا انجام

**Project:** `studio/videos/firaun-ka-anjaam/` · **Script:** [[script-v1-nastaliq]] v2.1 · **Design:** [[DESIGN]]
**Runtime target:** ~22:00 · **VO:** TTS (Nastaliq→Devanagari→ElevenLabs, 1 clip/line) · **Grade:** 4-era system

## Global guardrails (from DESIGN — apply to every row)
- **⚠️ #1 RULE — NEVER a face for a prophet or revered figure:** Musa (AS), Haroon (AS),
  Musa's mother & sister, Aasiya, the old man of Madyan (+ his daughters). Hands / from
  behind / distance / POV / objects / empty lit frame ONLY. A recognizable single-person
  silhouette still counts as a face — don't. Anonymous crowd-scale figures OK. If a shot
  can't be built safely, change the shot. Every image prompt carries the no-face negative clause.
- **Other depiction rules (BINDING):** no divine depiction, no clear Firaun face, mummy = museum-respectful, no Arabic on screen, no gore/nudity.
- 3 layers only (RECON / EVIDENCE / CARD); era grade per DESIGN table; deterministic grain over all.
- Cite chip (Nastaliq) on every Quran/source beat. Timeline ribbon at era jumps.
- Pattern interrupts fixed by the script's loop ledger — do not move them.
- Every scene fact-checked from real references BEFORE its image prompt is written (standing rule).

## Scene fact-checks — Part 1 (done 2026-07-18, before prompting)
- **NMEC royal mummies hall:** dim, dark-walled descending gallery, individual glass cases, per-mummy alcoves (opened Apr 2021; Ramesses II among 22 royals moved there in the Golden Parade — verified via ScienceAlert/Wikipedia 2026-07-18). Recon must show: dark hall, spot-lit cases, NO old-museum crowding.
- **The mummy's look:** wrapped body, exposed head with wisps of reddish hair (natural red verified — Ceccaldi 1987), aquiline profile. We show silhouette/partials only in the hook (withheld-face rule).
- **CT scanning of the mummy:** 2023 J. Archaeological Science study (verified) — modern gantry, body wrapped, lab setting. Recon = generic modern CT suite, no branding.
- **Le Bourget 26 Sept 1976:** military transport, honor guard, officials on tarmac (NYT 28 Sept 1976 verified). Recon in B&W newsreel grade, 1970s uniforms/cars, no legible insignia.

## Part 1 — HOOK (segs 01–05, 0:00–1:30) — beats

| VO | Layer/Era | Shot(s) | Motion (GSAP terms) | SFX / music | Transition | ~t |
|----|-----------|---------|---------------------|-------------|------------|----|
| 01 | RECON/museum | **1a** wide: dark NMEC-style hall, rows of lit cases, one case far-center · **1b** slow approach on that case, contents = dark silhouette behind glass | 1a locked 1.5s → 1b dolly = scale 1.0→1.10 + y-drift, sine.inOut | room tone, distant HVAC hum; single soft piano note | cut-in (same axis) | 0:00 |
| 02 | RECON/museum | **2a** macro: linen-wrapped hands · **2b** macro: reddish hair wisps in raking light · **2c** profile edge in shadow — face NOT readable | each macro locked, 2.5D micro-parallax (fg 3%, bg 1%) | cloth-dry whisper SFX on 2a; «3000» sub-bass pulse on VO word «3000 سال» | 0.8s dissolves between macros | 0:14 |
| 03 | RECON mixed eras | **3a** visitors' reflections on case glass (faces soft) · **3b** CT suite: gantry ring around wrapped body (museum grade) · **3c** ERA FLASH: B&W tarmac, honor guard line, transport plane (1976 grade, 1.2s) | 3a locked · 3b slow push scale 1.0→1.06 · 3c handheld-sim micro-shake (x ±4px noise, seeded) | camera-shutter click into 3c; newsreel projector rattle under 3c | hard cut into 3c (first jolt), dissolve out | 0:30 |
| 04 | KEYWORD-CARD **over** RECON (never flat) | **4a** slow push on **P02c** (withheld mummy head) UNDER «کیا یہ وہی شخص ہے؟» · **4b** cut to darkened **P03d** (France 1976) UNDER «جو سمندر میں ڈوبا» · **4c** the Yunus card is a **lower keyword strip**, not a full paragraph: punch «تیرا **بدن**» then «**نشانی**» + tiny cite chip «یونس 10:92» | bg pushes scale 1.0→1.08; keyword strip: opacity 0→1 power3.out 0.5s on the VO stress word; **cut the bg every ≤4s** | low drone ENTERS (the film's spine); «بدن»/«نشانی» = soft sub-bass thud | cut bg under held lines | 0:50 |
| 05 | KEYWORD-CARD over sea/goat + ribbon strip | **5a** «معجزہ نہیں۔ اُس سے اگلی صبح۔» keyword card OVER **P37c dark aftermath water** (= "the morning after"; P36 kept unspoiled), NOT flat cream · **5b** ⭐ **P05c goat** (new) UNDER «ایک بکری کی وجہ سے» — the payoff shot · ribbon 2026→1881→3000 runs as a **lower-third strip over P05c**, not full-frame numbers on black | 5a card ≤3s over drifting sea · 5b push on P05c; ribbon hops slide in under it, 0.4s bloom per hop | drone swells; whoosh per hop; end on Nile water + birds (pre-lap seg 06) | exposure bloom INTO seg 06 dawn mist | 1:10→1:30 |

**Image-prompt IDs for Part 1** (to be written one-shot in image-prompts.txt after sign-off):
`P01a-hall-wide`, `P01b-case-approach`, `P02a-hands`, `P02b-hair`, `P02c-profile-shadow`,
`P03a-glass-reflections`, `P03b-ct-suite`, `P03c-lebourget-1976`, `P04a` reuses P01a (dimmed in-comp).
`P05c-goat-shaft` (NEW 2026-07-23 — the goat/1881 payoff still; the one new hook generation).

> **REVISION 2026-07-23 — hook retention pass (ch1 draft review).** The rendered ch1-draft
> spends ~40s of its 68s (0:28→1:08) on **three motionless cards on flat cream/black** — including
> the two strongest hooks (the Quran question and the goat). Root cause in `studio/.../build.py`:
> the `is_card` path (~L286) sets `ref="C:"+key` and **drops the background image**, so cards
> *replace* imagery instead of overlaying it. Fixes, ranked by retention:
> 1. **Cards overlay, never replace.** Every card beat (04, 05a, 05b) rides a moving still. Engine:
>    give card lines a bg image ref + z-stacked overlay instead of the image-less `C:` branch.
> 2. **Visualise the goat** (video's best open loop): new **P05c** under «ایک بکری کی وجہ سے»;
>    tease it in the **first 3s as a cold-open bookend** («ایک 3000 سال پرانا بادشاہ — ایک بکری کی وجہ سے دریافت ہوا»).
> 3. **Open on the payload,** not the wide: lead second 1 with the red hair (P02b) or France (P03d);
>    earn the P01a hall *after* the grab. Trim seg-01 hold from ~5s to ~2s.
> 4. **Keyword punch, not paragraphs.** Cards show 2–4 VO-synced words, never the full ayah held 18s.
> 5. **Interleave idea↔image:** face under the Quran question, sea under "the morning after", goat
>    under the goat — stop spending all imagery in 0:00–0:28 and all ideas in 0:28–1:08.
> 6. **No card holds >4s** without the frame changing. Full analysis: [[hook-critique-2026-07-23]].
Cards 4b/5a/5b built in HyperFrames — no generation needed. **9 stills total for the hook.**

## Scene fact-checks — Part 2 (done 2026-07-18, before prompting)
- **Ramesside Egyptian labour / mudbrick:** Bani Israil-era slave labour = **mudbrick making** (Nile
  mud + straw pressed in wooden molds, sun-dried) and hauling stone — the biblical/Quranic "bricks
  and stone" motif. Depict mudbrick pits, straw, wooden molds, drying rows; NOT pyramid-building
  (pyramids were already ~1000 yrs old by Ramesses II). Verified: standard Egyptology on New Kingdom
  corvée labour + mudbrick technique (Wikipedia "Mudbrick", "Ramesses II") 2026-07-18.
- **Setting/architecture:** New Kingdom Egypt = **mudbrick towns + massive stone temples** (Karnak/
  Ramesseum type — pylons, hypostyle columns, colossal statues), the Nile with reed banks, palm,
  feluccas. Warm golden light. NOT Greco-Roman, NOT pyramids-in-every-frame.
- **Wardrobe:** linen kilts/shendyt for workers, bare torsos, headcloths; overseers with staffs.
  Royalty in pleated linen, broad collars, nemes headcloth. **Firaun's face IS shown** (DESIGN rule 3
  + FIRAUN FACE LOCK, creator A-decision 2026-07-23) — a consistent visible tyrant, NOT from-behind.
- **"Groups torn apart / sons killed" (28:4):** implied only — a soldier's shadow over a cradle,
  never an act shown. No violence on screen.

## Part 2 — غلاموں کا شہر (segs 06–10, 1:30–3:45) — beats

| VO | Layer/Era | Shot(s) | Motion (GSAP) | SFX / music | Transition | ~t |
|----|-----------|---------|---------------|-------------|------------|----|
| 06 | RECON/ancient | **P06** dawn Nile mist; an old brickmaker's **weathered hands** pressing mud+straw into a wooden brick mold, drying brick rows behind (HANDS/labour focus, worker's face optional & incidental — NOT a revered figure) | slow push scale 1.0→1.10, sine.inOut; grain in | Nile dawn ambience — reeds, distant birds, a low work-drone; music: warm modal cue enters | bloom-in from seg 05 ribbon | 1:30 |
| 07 | RECON/ancient | **P07** wide: gangs of labourers hauling a great stone block with ropes, overseers' **whip-shadows** stretching across dust, a massive temple pylon under construction behind | Ken Burns pull-back to reveal scale; parallax dust fg | rope-strain, distant crack of a whip (offscreen), crowd murmur; cite-chip sting on «القصص 28:4» | 1.0s dissolve | 1:55 |
| 08 | RECON/ancient | **P08** throne-room interior, colossal columns; **Firaun enthroned, face visible per the FIRAUN FACE LOCK** (the consistent tyrant), a prostrate crowd of courtiers below, broad shafts of golden light | slow push-in on the throne; locked on the bowing crowd | low brass swell; hall reverb; VO «میں تمہارا سب سے بڑا رب ہوں» lands in a beat of near-silence | 1.0s dissolve | 2:20 |
| 09 | RECON/ancient | **P09** a torch-lit palace/mudbrick corridor at night; a **soldier's hard shadow falls across a woven cradle** — the act implied, never shown; then hard cut to black | push-in on the shadow; **hard cut to black** (pattern beat) | torch crackle → sudden silence on the cut; a single low drum | **hard cut to black**, 0.5s hold | 2:50 |
| 10 | RECON/ancient | **P10** a small lamp-lit mudbrick room; a **newborn's tiny hand curled around an adult finger — HANDS ONLY**, warm lamp glow, shallow shadow (mother = never-a-face; baby Musa = no face) | very slow push, locked-feel; soft grain | music softens to solo strings; lamp-flame flicker (seeded) | slow dissolve to seg 11 | 3:15→3:45 |

**Part-2 image IDs (rewritten as stills 2026-07-19):** P06a/b/c (mould-hands macro · brickfield
wide · single-brick macro) · P07a/b/c (stone-haul wide · overseer shadows · rope-hands detail) ·
P08a/b/c (throne, Firaun's face visible per lock · prostrate courtiers floor-level · king's hand on throne arm) ·
P09a/b (soldier+cradle shadow · empty torch corridor) · P10a/b (newborn hand macro · lamp-lit room
with cradle). **13 stills** in image-prompts.txt. Motion = Ken Burns + cutting between the angles.
⚠️ Part 2's bricks are correctly **sun-dried mudbrick** (Rekhmire evidence) — the fired-brick
correction applies ONLY to Haman's tower (28:38, P19). Two different bricks; do not over-correct.

## Part 3 — دریا میں ٹوکری (segs 11–15, 3:45–5:45)
Fact-check (**CORRECTED 2026-07-19 — see fact row 4a**): the Quran's word is **التابوت / tabut
(20:39) = a WOODEN CHEST/box**, not a reed basket. Ibn Kathir: *she took a box and made it into a
cradle*, and tied it with a rope. Plank-built (acacia / sycamore-fig), pegged and lashed, seams
sealed with black pitch, **cradle-sized — a newborn lies full length inside**. The woven
papyrus/reed "ark of bulrushes" is the BIBLICAL image (Exodus 2:3) and must NOT be used. Also:
palace **water-steps (river landing)** with painted lotus-bud columns; wet-nurse = infant refusing
the breast, calmed by the mother. NEVER-A-FACE: mother, baby Musa, Aasiya.
**⚠️ The Urdu chapter title «دریا میں ٹوکری» (= "basket in the river") now contradicts the verse —
creator to decide: retitle to «دریا میں صندوق» / «دریا میں تابوت», and check the VO lines in segs
11–13 for the word «ٹوکری».**

| VO | Layer/Era | Shot(s) | Motion | SFX/music | Trans | ~t |
|----|-----------|---------|--------|-----------|-------|----|
| 11 | RECON/ancient night | **P11** interior, lamp-lit — HANDS ONLY sealing a reed basket, torchlight moving past a window slit | push-in, locked feel | distant boots/torches, tense low drone; card 28:7 | dissolve | 3:45 |
| 12 | RECON/ancient night | **P12** extreme-wide dark Nile, a tiny basket + pin-light drifting on vast water; (mother = far back-turned silhouette at most) | very slow pull-back = scale ↓; parallax water | water lap, one held silence beat | slow dissolve | 4:10 |
| 13 | RECON/ancient dawn | **P13** palace river-steps, attendants' arms lifting a basket between reed columns/spears (dramatic irony); Firaun's realm implied | tilt-up from water to palace | courtly murmur, soft ironic music turn; card 28:8 | dissolve | 4:35 |
| 14 | RECON/ancient | **P14** Aasiya's HANDS ONLY cradling the swaddled infant in a warm shaft of light — the one warm frame | locked, gentle breathing push | tender solo strings; card 28:9 | dissolve | 5:05 |
| 15 | RECON/ancient | **P15** montage: nurses' arms failing to soothe (infant turned away) → mother's arms (back-turned, no face) → infant calm | 3 quick locked cuts | soft sting on the calm; card 28:12-13 | dissolve | 5:25→5:45 |

**IDs:** `P11-basket-hands`, `P12-river-wide`, `P13-palace-steps`, `P14-aasiya-hands`, `P15-nurse-mother` (5)

## Part 4 — مدین سے طُور تک (segs 16–17, 5:45–8:15) — the new v2.1 chapter
Fact-check: Midian = NW Arabian desert/mountains, a communal **well with troughs**, Bedouin flocks;
Mount Tur/Sinai granite. Tuwa scene = light-in-a-tree ONLY (no form). NEVER-A-FACE: Musa, the two
women, the old man (poss. Shu'ayb AS), the family. Staff + sandals are the recurring props (lock design).

| VO | Layer/Era | Shot(s) | Motion | SFX/music | Trans | ~t |
|----|-----------|---------|--------|-----------|-------|----|
| 16 | RECON/ancient | **P16a** street fight from distance/behind, a body falls (implied) · **P16b** a hooded figure from behind leaving a city gate at night | P16a locked → P16b slow push | crowd shout → night wind; tense low | hard-ish cut | 5:45 |
| 16a | RECON/desert day | **P16c** Madyan well: crowd+flocks, HANDS at a trough watering (Musa from behind); two women as distant back-turned figures holding a flock · **P16d** empty shade tree + resting staff (dua VO over it) · **P16e** the old man's tent/hands only, no face | P16c Ken Burns; P16d locked; card 28:24 | well-crowd, sheep, desert wind; dua = music drops | dissolves | 6:20 |
| 16b | RECON/desert night | **P16f** cold rain, a family as distant huddled back-turned shapes, hands striking failed sparks · **P16g** a distant fire-glow on a black mountainside — hold | P16g locked, long hold | rain, wind, failed flint; card 20:10 «ابن کثیر» | slow dissolve | 7:00 |
| 16c | RECON+divine-safe | **P16h** fire-that-is-light within a tree, no smoke, NO figure · **P16i** sandals set aside on rock, light on valley floor (POV) | locked; reverent | drone drops to near-silence; cards 20:12-14 | dissolve | 7:25 |
| 16d | RECON abstract | **P16j** staff dropped → serpent (shadow+motion), hand at frame-edge only · **P16k** radiant white light spilling from a sleeve (hand only) | quick, then locked | low awe swell; card 20:24 | dissolve | 7:50 |
| 17 | CARD + RECON | **P17** two distant back-turned figures on the road to Egypt, palace far on horizon | slow push | card «میں تم دونوں کے ساتھ ہوں…» full-screen; open loop | dissolve | 8:00→8:15 |

**IDs:** P16a–P16k, P17 (12) — heavy chapter; several are card/prop shots (cheap).

## Part 5 — چرواہا اور بادشاہ (segs 18–23, 8:15–10:15)
Fact-check: Egyptian court, colossal columns; Haman "tower" = mudbrick/scaffold rising; the magicians'
duel = ropes/staffs on open festival ground, "snakes" as writhing motion; sujood = a distant MASS
prostrate (anonymous crowd OK). NEVER-A-FACE: Musa, Haroon. Firaun's face IS shown (FACE LOCK).

| VO | Shot(s) | Motion | SFX/music | ~t |
|----|---------|--------|-----------|----|
| 18 | **P18** long throne-room walk, two small BACK-TURNED figures under giant columns (power contrast) | slow push | echoing hall, low tension | 8:15 |
| 19 | **P19** scaffolding/mudbrick tower rising into haze, tiny workers, Firaun (behind) pointing skyward | tilt-up | brass hubris swell; card 28:38 | 8:40 |
| 20-21 | **P20** festival crowd → ropes/staffs writhing as snakes across sand → **ONE** staff-serpent swallowing all; 1 beat total silence | Ken Burns → locked on the swallow (interrupt) | crowd gasp → **silence** | 9:05 |
| 22 | **P22** magicians as a distant MASS falling in sujood, dust rising (top shot, anonymous) | slow pull-back | awe swell; card 20:70 | 9:40 |
| 23 | **P23** defiant anonymous silhouettes against the sun (the believing magicians) | locked | single low note; cards 20:71-72 | 10:00→10:15 |

**IDs:** P18, P19, P20, P22, P23 (5)

## Part 6 — نشانیوں پر نشانیاں (segs 24–32, 10:15–12:30) — the plague chapter
Fact-check: the 6 named signs of 7:133 (drought, flood, locusts, lice, frogs, blood) + 9-signs frame
(17:101). 9-signs tally card fills 1→6 here. Each = one strong environmental frame (no revered
figures). Blood-Nile = the river turned dark red (evidence of judgment, not gore).

| VO | Shot(s) | Motion | SFX/music | ~t |
|----|---------|--------|-----------|----|
| 24 | **P24** 9-signs tally card appears (parchment) over a darkening Nile sky | card in | card 17:101 | 10:15 |
| 25 | **P25** cracked earth, withered palms, empty market baskets (drought) — tally 1 | slow push | dry wind; card 7:130 | 10:30 |
| 26 | **P26** storm walls of rain over the delta, flooded fields, rooftop refuge — tally 2 | pull-back | rain roar | 10:50 |
| 27 | **P27** locust cloud dimming the sun, a field stripped bare — tally 3 | Ken Burns | locust hiss | 11:10 |
| 28 | **P28** infested grain jars, scratching hands (lice) — tally 4 | macro locked | unease drone | 11:30 |
| 29 | **P29** frogs spilling from a doorway, a lifted pot lid with a frog — tally 5 | locked, slight | croaking wall (design) | 11:50 |
| 30 | **P30** the Nile turning dark red at sunset, abandoned water jars — tally 6; card «7:133» list | slow pull-back (interrupt-lite) | water hush, low dread | 12:05 |
| 31 | **P31** court: pleading arms (Firaun behind) → relief → a smirk shadow — the broken-promise loop | 3 quick cuts | cards 7:134-135 | 12:20 |
| 32 | **P32** the shadowed empty throne, emptier than before | slow push | hollow reverb | 12:25→12:30 |

**IDs:** P24–P32 (9)

## Part 7 — رات کا سفر + سمندر (segs 33–37, 12:30–14:50)
Fact-check: night Exodus = a huge ANONYMOUS torchlit column (crowd-scale OK); chariots = New Kingdom
2-horse war chariots; the sea = "each part like a mighty mountain" (26:63) — towering water walls,
dry corridor (20:77). THE money shot = seg 36. NEVER-A-FACE: Musa (back-turned at seg 35).

| VO | Shot(s) | Motion | SFX/music | ~t |
|----|---------|--------|-----------|----|
| 33 | **P33** torchlit column of thousands under stars (crane wide) + intimate cut: a child asleep on a shoulder (anonymous) | crane drift | night wind, muffled march; card 44:23 | 12:30 |
| 34 | **P34** chariots bursting from city gates, dust storm behind | fast Ken Burns | hooves, war horns; cards 26:53-55 | 12:55 |
| 35 | **P35** the trap: anonymous crowd on shore, whip-pan sea↔army; then a lone BACK-TURNED figure facing the water (Musa, no face) | whip pan → locked | crowd fear → **silence**; card 26:62 | 13:20 |
| 36 | **P36** ⭐ sea splitting — towering water walls, dry corridor, light shafts, anonymous people walking, a child touching the wall | tilt-up + slow forward (THE shot) | deep rumble, water suspended; swell | 13:45 |
| 37 | **P37** chariots entering the corridor (high angle) → 1s stillness → walls collapse, churning dark (VO silent 3s) | locked → collapse sim | full sound → **3s nothing** | 14:20→14:50 |

**IDs:** P33a, P33b, P34, P35a, P35b, P36, P37 (7 — P33/P35 split 2026-07-19, one camera move per clip) — **STRONG-motion clips: P34, P36, P37.**

## Part 8 — آخری سانس + تیرا بدن (segs 38–42, 14:50–17:05)
Fact-check: drowning declaration (10:90) + "Now?" (10:91) + 10:92 translation & Ibn Kathir shoreline.
No Arabic on cards — Urdu translation only. Shoreline body = armor glinting at a distance, face never
shown. Match cut seg 42 (shoreline sand → Deir el-Bahari cliffs).

| VO | Shot(s) | Motion | SFX/music | ~t |
|----|---------|--------|-----------|----|
| 38 | **P38** underwater: sinking armor, bubbles, fading light (no face) | slow sink drift | muffled underwater; contrast card 79:24↔10:90 | 14:50 |
| 39 | **P39** «اب؟» single-word card, hard cut; fade to still dawn water | hard cut → locked | silence → one note; card 10:91 | 15:15 |
| 40 | **P40** full-screen parchment: URDU translation of 10:92, word-by-word kinetic («بدن»،«نشانی» punch); cite «یونس 10:92» | word rises (no letter-spacing anim) | reverent bed | 15:55 |
| 41 | **P41** dawn shoreline, a crowd at a DISTANCE around a shape on the sand, armor glinting (face never shown); cite «ابن کثیر» | slow push | wave wash, low awe | 16:25 |
| 42 | **P42** ⭐ MATCH CUT: ancient shoreline sand → same-framing Deir el-Bahari cliffs (1881 sepia); ribbon «3000 سال بعد» | match dissolve | transition whoosh | 16:50→17:05 |

**IDs:** P38, P41, P42 (P39/P40 = cards) (3 stills)

## Part 9 — 1881 + پیرس (segs 43–48, 17:05–19:50)
Fact-check: TT320 shaft/coffins (Deir el-Bahari), plain reused wooden coffin of Ramesses II; 1976
Le Bourget honor guard; 3 myths. EVIDENCE layer here = real licensed photos where possible (mummy
case, cartouche, TT320) — recon only as fallback. NO revered figures in this act. Mummy respectful.

| VO | Layer | Shot(s) | Motion | SFX/music | ~t |
|----|-------|---------|--------|-----------|----|
| 43 | RECON/1881 sepia | **P43** lantern descending a rock shaft, stacked royal coffins, a cobra crown catching light | slow descend | lantern creak, rope; card TT320 | 17:05 |
| 44 | RECON+EVIDENCE | **P44** reveal pan across coffins; parchment card «TT320 — 50+ شاہی ممیاں» | pan | dust, awe | 17:35 |
| 45 | RECON/EVIDENCE | **P45** coffin close-up (plain wood) name card RAMESSES II; barge on the Nile at dusk | locked → dissolve | elegiac cue | 18:00 |
| 46 | 1976 newsreel | **P46** B&W: Le Bourget honor guard/plane → lab → return flight (montage) | newsreel cuts | projector rattle; cards NYT/LA Times | 18:25 |
| 47 | CARD/EVIDENCE | **P47** myth 1 «پاسپورٹ» — viral image pixelated, red «جھوٹ» stamp; cite AFP | stamp slam | stamp thud | 19:00 |
| 48 | CARD | **P48** myth 2 natron diagram «گمراہ کن» + myth 3 CT cross-section «جھوٹ» (rapid) | rapid stamps | double thud; cites | 19:25→19:50 |

**IDs:** P43, P44, P45, P46 (+ evidence sourcing) (4 recon; cards P47/P48). **Evidence-sourcing list built here.**

## Part 10 — نشانی آج بھی + عبرت + ending (segs 49–53, 19:50–22:00)
Fact-check: honest-answer beat (Quran names no pharaoh; Ma'arif caution); 2021 Golden Parade + 2024
Sorbonne sarcophagus; ibrah close; CTA. Museum era grade returns.

| VO | Shot(s) | Motion | SFX/music | ~t |
|----|---------|--------|-----------|----|
| 49 | **P49** candidate row card (رعمسیس دوم · مرنپتاح · «؟», «؟» zoom) over the museum case; cite «معارف القرآن» | slow push on «؟» | thoughtful bed | 19:50 |
| 50 | **P50** thesis wide: the museum mummy hall, 10:92 Urdu translation over it; quick beats Golden Parade night (recon) + granite cartouche (evidence); cites 2021/2024 | slow reveal | resolving theme begins | 20:15 |
| 51 | **P51** return to the frozen underwater frame (desaturated); museum lights dimming case by case; closing phrase of 10:92 | locked, slow dolly out | reverent, sparse | 20:50 |
| 52 | **P52** one lit case alone in darkness — hold 3s | locked | music resolves | 21:20 |
| 53 | **P53** callback montage: shoreline → shaft → Paris → museum; end card + next-video tease (Mada'in Salih silhouette) + subscribe chip | montage → end card | closing theme peak | 21:35→22:00 |

**IDs:** P49–P53 (5; several card/composite)

**Total stills estimate:** Hook 8 · P2 5 · P3 5 · P4 12 · P5 5 · P6 9 · P7 5 · P8 3 · P9 4 · P10 5 ≈ **61 recon stills** + HyperFrames cards + licensed evidence photos. Well within the ~200/day one-shot budget.

## Master timing table (skeleton — rows fill as parts are drafted)
| section | segs | ~duration | storyboard part |
|---|---|---|---|
| Hook | 01–05 | 1:30 | **Part 1 ✅ APPROVED — prompts written** |
| غلاموں کا شہر | 06–10 | 2:15 | **Part 2 ✅ drafted — awaiting sign-off** |
| دریا میں ٹوکری | 11–15 | 2:00 | **Part 3 ✅ drafted** |
| مدین سے طُور تک | 16–17 | 2:30 | **Part 4 ✅ drafted** |
| چرواہا اور بادشاہ | 18–23 | 2:00 | **Part 5 ✅ drafted — 5 video prompts written 2026-07-19** |
| نشانیوں پر نشانیاں | 24–32 | 2:15 | **Part 6 ✅ drafted — 8 video prompts written 2026-07-19 (P24 = card)** |
| رات کا سفر + سمندر | 33–37 | 2:20 | **Part 7 ✅ drafted — 7 video prompts written 2026-07-19 (P33/P35 split)** |
| آخری سانس + تیرا بدن | 38–42 | 2:15 | **Part 8 ✅ drafted — 3 video prompts written 2026-07-19 (P39/P40 = cards)** |
| 1881 + پیرس | 43–48 | 2:45 | **Part 9 ✅ drafted** |
| نشانی آج بھی + عبرت + end | 49–53 | 2:10 | **Part 10 ✅ drafted** |

## Deliberate placeholders (must be real before publish)
- ✅ Evidence-layer licences **VERIFIED 2026-07-19** — result: only the 1881 Brugsch album (Heidelberg, PDM 1.0) is usable; all modern imagery ships as recon. Re-check the Commons files in a browser before publish (see method caveat).
- ✅ Dynamic-scene fork RESOLVED (creator 2026-07-18): ALL stills → image-to-video (Kling/Runway/Veo), prompts in video-prompts.txt; STRONG = P34/P36/P37. No-face rule enforced in every motion prompt.
- TTS timing pass: final per-scene durations lock to actual clip lengths, not estimates.



## ⚠️ APPROACH REVERSED 2026-07-19 (creator) — BACK TO STILL IMAGES
Direct text-to-video is **abandoned**: too expensive, and re-generation burns credits whenever a
clip comes back wrong. **We generate STILL IMAGES per frame — often SEVERAL per scene (different
angles/scales of the same moment)** — and bring them alive in HyperFrames with Ken Burns, 2.5D
parallax and cutting between the angles. New file: **`image-prompts.txt`** (the file the storyboard
originally called for). `video-prompts.txt` is **SUPERSEDED** — kept only as reusable source text
for scene description/wardrobe/light; its "10-second clip" and "over the 10 seconds the camera…"
wording does not apply. Prompt format now: single still frame, composition + lens, **no camera-move
sentence**, same no-face negative clause.
**Still-image rewrite order (creator 2026-07-19): highest-value chapters first, starting from
Chapter 2.** Done: Part 3 corrected (P11a–P13b, 7) · Part 2 (P06a–P10b, 13) · **Part 7 (P33a–P37d, 18)** =
**38 stills.** Part 7 IDs: P33a/b/c (column wide · child from behind · feet+torchlight detail) ·
P34a/b/c/d (migdol-gate burst · ground-level pass · six-spoke wheel macro · rear dust plume) ·
P35a/b/c (trapped crowd · army line 135mm · lone back-turned figure) · P36a/b/c/d (signature wide ·
16mm look UP the wall · in-corridor human level · child's hand at the wall) · P37a/b/c/d (high-angle
pour-in · walls leaning, the instant before · the collapse · flat calm aftermath).
**Cutting note:** P37b→c→d is the pattern-interrupt beat — the instant-before, the collapse, then
stillness. P37d holds under the scripted 3s of VO silence; it is the payoff frame, not filler.
· **Part 5 (P18a–P23b, 15)** = **53 stills.** Part 5 IDs: P18a/b/c (walk from behind · 16mm look UP
the columns · dusty feet on painted floor) · P19a/b/c/d (**FIRED-brick** tower + smoking kilns ·
kiln firebox close · Firaun (face per lock) pointing at empty sky · ramp of brick-haulers) ·
P20a/b/c/d (festival wide · lector priests from behind, leopard pelt + sidelock · the great serpent,
no people · **the empty swept sand — silence frame**) · P22a/b (top-down mass · ground-level across
prostrate backs) · P23a/b (sunset silhouette row · rim-lit pelt/hand detail).
**P19 fired-brick fix APPLIED** (28:38). Kiln accuracy checked 2026-07-19: earthen clamp/mound kilns
and updraft kilns with a firebox below a perforated floor were long established, Egypt had vented
firing chambers by ~3000–2500 BC, fuel = wood and straw (UCLA Encyc. of Egyptology "Kilns and Firing
Structures", africame.factsanddetails, Grokipedia "Kiln"). Fired brick was RARE in Egypt — which is
exactly the point of the ayah (Firaun said to be first to bake hard brick), so the shot shows a
purpose-built brickyard, not routine industry.
· **Part 8 (P38a–P42b, 8)** = **61 stills.** Part 8 IDs: P38a/b/c (sinking figure, face away ·
**the khepresh tumbling alone, no body** · looking up at the surface from deep) · P41a/b/c (dawn
shoreline wide with the distant watching arc · mid, head cropped OUT of composition · **macro of
bronze scales + gilded collar in wet sand, nothing human in frame**) · P42a/b (Deir el-Bahari cliff
bay matched to P41's framing · the black shaft-mouth notch closer).
**Respect rule applied:** the shoreline body is built so the closer we get, the LESS body is in
frame — wide = a shape, mid = head cropped out, macro = objects only. The chapter's emotional peak
(P38b, the crown falling alone) contains no body at all. This is the honest version of Ibn Kathir's
«زرہ» detail without horror grammar.
· **Part 6 (P25a–P32b, 20)** = **81 stills.** Part 6 IDs: P25a/b · P26a/b · P27a/b/c · P28a/b ·
P29a/b/c · P30a/b/c · P31a/b/c · P32a/b. Each sign gets a WIDE (the scale of the judgment) + a
MACRO (the texture that makes it real) — that pairing is the chapter's cutting rhythm and it also
feeds the 9-signs tally card beat cleanly.
**P31b reuses the P08c device** (king's hand on the gilded lion-paw throne arm, no head in frame) —
the dismissive turn of the wrist replaces the storyboard's original "smirk", which would have
required a face. Recurring visual grammar for Firaun: he is a HAND and a BACK, never a portrait.
· **Part 4 (P16a1–P17b, 18)** = **99 stills.** Part 4 IDs: P16a1 (distant scuffle) · P16b1/b2 (gate
from behind · **sandal prints in moonlit sand, no person**) · P16c1/c2/c3 (well wide · hands tipping
the bucket · two women distant from behind) · P16d1 (empty thorn tree + staff — the dua frame) ·
P16e1 (elder's folded hands on staff at the tent, no head) · P16f1/f2 (huddled family from behind ·
**failed sparks macro**) · P16g1 (distant fire on the black mountainside) · P16h1/h2 (light in the
tree · closer study of unburnt branches) · P16i1 (sandals on rock) · P16j1 (staff-serpent, hand at
frame edge only) · P16k1 (radiant hand from a sleeve) · P17a/b (two from behind on the road ·
**their cast shadows only, no bodies**).
**Depiction method for this chapter — the hardest in the film:** where a beat needs a person, the
frame instead carries what the person LEFT (sandal prints, sparks, a staff against a tree, two
shadows on a road). P16d1 and P17b are entirely person-free and still carry their VO. P16h1/h2 have
an explicit triple-negative — no figure, no silhouette, no form of any kind inside or near the light.
· **Parts 9–10 (P43a–P53a, 17)** = **116 stills.** Part 9: P43a/b/c (down the vertical shaft ·
coffin corridor by lantern · gilded cobra lid detail) · P44a/b (chamber wide · **hieratic ink
macro**) · P45a/b (**the stripped cedar coffin** · steamer + barge at dusk) · P46a/b/c (Le Bourget
1976 · 1970s lab, head excluded · 1977 return). Part 10: P49a (single case) · P50a/b/c (gallery wide ·
Golden-Parade-style night convoy · granite cartouche fragment) · P51a (cases dimming) · P52a (one
lit case in blackness) · P53a (Hegra-style rock-cut façade — next-video tease).
**PART 9–10 RESEARCH (verified 2026-07-19):** TT320 = nearly vertical rock-cut shaft/chimney into
the Deir el-Bahari cliff, then corridors running ~23 m into the limestone (total system ~70 m);
Brugsch cleared it in **two days**, 50+ royal mummies and ~6,000 funerary objects, shipped to the
Bulaq Museum by steamer (Wikipedia "Royal Cache", Grokipedia, cesras.org TT320 index).
**Ramesses II's coffin = plain fine imported CEDAR, stripped of its gold plating, and REUSED** —
late-18th-dynasty style, Horemheb a prime candidate as original owner — carrying **three inked
hieratic dockets** recording ancient moves to "repeat the burial" (ARCE, the-past.com, Australian
Museum). That single object carries the chapter's whole irony and is P45a.
**⚠️ Modern-text guard:** the 1881 and museum frames forbid modern text but ALLOW ancient hieratic /
hieroglyphs (P44b, P45a, P50c) — that writing is the evidence, not an anachronism.

## Evidence-layer sourcing list (DESIGN §layer ② — built 2026-07-19, LICENCES TO VERIFY BEFORE USE)
**✅ VERIFIED 2026-07-19 (licence research pass). Verdict: ONE usable source; everything else is
recon.**

**① CLEARED AND USABLE — the 1881 Brugsch album.** Maspero/Brugsch, *La trouvaille de
Deir-el-Bahari* (Cairo 1881), **all 20 mounted original photographs digitised** by Heidelberg
University Library: https://digi.ub.uni-heidelberg.de/diglit/maspero1881bd1 — stated licence
**"Public Domain Mark" (PDM 1.0)**. Cleanest, highest-resolution route. This covers the TT320 shaft,
the site and the cache coffins — i.e. exactly the Part-9 beats, and nothing that breaches the
respect rule. **USE THIS.** (Also at LoC https://www.loc.gov/item/82465142/ and NYPL; Gallica
ark:/12148/btv1b8626666s returned 403 and is unverified.)
⚠️ **Attribution correction:** the famous "men at the mouth of the shaft" photograph is by
**Edward Livingston Wilson** (pub. *In Scripture Lands*, 1890), NOT Brugsch — Commons `{{PD-scan}}`.
Do not caption it as Brugsch.

**② LEGALLY FREE BUT EDITORIALLY BANNED BY OUR OWN RULE — Victorian unwrapped-mummy photographs.**
`File:Ramses II - The mummy.jpg` and `File:Pharaoh Seti I…` (Emil Brugsch, d. 1930) are
`{{PD-old-90-expired}}`; the G. Elliot Smith *The Royal Mummies* (Cat. Gén., 1912) plates are
`{{PD-old-auto-expired|deathyear=1937}}`. **Legally clean — but these are clinical unwrapped-remains
photographs, and DESIGN §4 forbids decay close-ups and horror grammar, with the face withheld until
segs 49–50 and museum framing only even then. So we do NOT use them.** The single category that is
free is the one category the film's ethics rule out. Recorded so this is a decision, not an oversight.
(If ever reconsidered: date them carefully — sources give 1881 and 1889 for the Brugsch mummy shots.)

**③ IN COPYRIGHT — 1976/77 Le Bourget.** No free image exists anywhere; Commons returns zero. AFP
rights-managed (France24's own retrospective credits "AFP/File"); Getty carries the arrival set as
licensable editorial. French term is 70 yrs from publication — protected past 2040. **→ recon
P46a/b/c and P03d ship.**

**④ NOT CLEARED — 2021 Golden Parade.** Commons `File:Pharaohs Golden Parade.jpg` carries
`{{PD-Egypt-official}}`, but that template rests on Art. 141 of Egypt's IP Law 82/2002, which exempts
**official documents only** (laws, regulations, resolutions, conventions, court/arbitral decisions) —
**photographs are not in that list**, and the file's stated date (2019) contradicts the 2021 event.
**Tag appears misapplied; treat as not cleared.** One genuinely reusable item exists: a `{{YouTube
CC-BY}}` parade video (News 360 Tv, ID lyOPdSyJ1DI, reviewed 2021-04-18) — CC BY 3.0 with
attribution, though it re-cuts broadcast footage and the upstream chain is unverified.
**→ recon P50b ships.**

**⑤ IMPOSSIBLE, NOT MERELY UNLICENSED — NMEC Royal Mummies Hall.** **Photography inside the Royal
Mummies Hall is prohibited** (NMEC policy: https://nmec.gov.eg/visitor-tips-and-policies/ — elsewhere
in the museum private photography requires a paid ticket, no flash/tripod; commercial use needs prior
permission and fees). No freely licensed photo of that hall's interior was found, consistent with the
ban. Commons has 100+ free NMEC **exterior/main-hall** shots (e.g. the `National Museum of Egyptian
Civilization 2025_xx.jpg` series, `{{self|cc-by-4.0}}`, attribution to the uploader required).
**→ our museum recon (P01a/b/c, P49a/b, P50a, P51a/b, P52a) is the ONLY route, not a fallback.**

**⑥ ALL RIGHTS RESERVED — 2024 sarcophagus.** The Sorbonne press release (23 May 2024) contains
exactly one photo, captioned "©Kevin Cahail", with no licence grant — press distribution is not a
reuse licence. To clear: Katherine Tyrka katherine.tyrka@sorbonne-universite.fr / Alyssa Perrott
alyssa.perrott@sorbonne-universite.fr / CNRS presse@cnrs.fr; rights likely sit with Cahail directly.
**→ recon P50c ships.**

**⚠️ METHOD CAVEAT:** commons.wikimedia.org was unreachable during this pass; licence tags were read
via the api.wikimedia.org REST endpoint (authoritative for wikitext, but rendered pages, deletion
notices and talk-page disputes were NOT visible). **Re-check each Commons file in a browser before
publish — especially `File:Pharaohs Golden Parade.jpg`, whose tag is believed wrong.**

**BOTTOM LINE:** the evidence layer = **1881 Brugsch album only**. Everything modern ships as recon.
Nothing in the film depends on a licence landing.
· **Hook (P01a–P03d, 10)** = **126 stills — CONVERSION COMPLETE, all 10 chapters.**
Hook IDs: P01a/b/c (gallery wide · single case, head in shadow · **floor-reflection corridor**) ·
P02a/b/c (wrapped hands · reddish hair wisps · rim-lit head silhouette) · P03a (visitors' blurred
glass reflections) · P03b/c (CT gantry · **scan slice on monitor, no face, no interface text**) ·
P03d (Le Bourget 1976). P04/P05 stay HyperFrames cards (parchment + timeline ribbon).
**Withheld-face rule holds through the whole hook** — hands, hair, a rim-lit edge, a shadowed head,
an abstract scan slice. The clean profile is never given until segs 49–50, per DESIGN.

## ✅ IMAGE-PROMPT CONVERSION COMPLETE — 2026-07-19
**126 stills across all 10 chapters** in `image-prompts.txt`. Motion comes from HyperFrames
(Ken Burns + 2.5D parallax + cutting between the angles of each scene), not from generation.
Per-scene density: 1–2 stills for short beats, 3 for weighted scenes, 4 for the peaks (P19, P20,
P34, P36, P37). Cards remain HyperFrames-built: P04, P05, P24, P39, P40, P47, P48, P49-card,
P51-card, P53-card.
## ✅ CREATOR REVISION PASS — 2026-07-19 (title · glow rule · gap-fill)
**1. TITLE RESOLVED → «دریا میں صندوق»** (creator). Applied in script: chapter list (line 37),
chapter heading, and the VO word «ٹوکری» → «صندوق» in segs 12 and 13 — **including the gender
agreement fix in seg 13** (صندوق is masculine: «وہ صندوق بہتا بہتا… رکتا ہے»). Zero «ٹوکری» remain.
**2. THE GLOW RULE (creator) — full rule in [[DESIGN]] §DEPICTION.** Revered figures may now be
shown in frame, front-on, with the **face replaced by a soft radiant white glow** (no eyes/mouth/
nose/features/outline, blending softly at the edges). Applies to **Musa (AS), Haroon (AS), Musa's
mother, Musa's sister, Aasiya**. **NOT Firaun** (creator explicit — he keeps behind/shadow/cropped,
face never clear, NO glow) and not to ordinary characters, who are shown normally.
Rewritten to use the glow (9 prompts): **P11a** (mother over the chest) · **P14a** (Aasiya, NEW) ·
**P15a/P15b** (nurses / the handover, NEW) · **P16b1** (last look back at the city gate) ·
**P16c2** (watering the flock) · **P17a** (two brothers walking TOWARD camera) · **P18a** (walking
INTO the throne hall, upright) · **P35c** (in profile against the sea).
Every glow prompt also negates **halo rings, crowns of rays and religious iconography** — the brief
is a plain soft white glow, not an icon.
Back-turned/hands-only/empty-frame compositions are KEPT where they were simply the better shot
(P17b shadows, P16d1 empty tree, P10a hands, P16f1 rain, P41 shoreline).
**3. GAP-FILL — 6 new prompts.** ⚠️ **P14 and P15 had never been converted at all** — segs 14
(Aasiya) and 15 (wet-nurses → mother) had ZERO images. Now P14a/b + P15a/b. Also thin-coverage
fixes after a segment-by-segment audit: **P49b** (three identical lit cases — the unanswerable
question made visual; seg 49 was 25 s on one still) and **P51b** (a case whose light has just gone
out; seg 51 was 30 s on one still).
**Coverage now verified segment-by-segment for all 53 segments — no gaps remain.**
**File integrity checked:** 132 prompts · 131 separators (correct n−1) · 132/132 carry the photoreal
clause · 132/132 carry a depiction negative.

## ✅ CREATOR DECISIONS 1b / 2b / 3c — APPLIED 2026-07-19
**1b — Madyan household GETS the glow.** P16e1 rewritten: the elder now sits facing camera at the
tent mouth, hands on his staff, white beard visible, face = white glow. P16c3 rewritten: the two
daughters now shown at 85mm (was 135mm back-turned), fully and modestly robed, both faces = white
glow. Part 4 is no longer seven consecutive scenes of indirection.
**2b — FIRAUN'S FACE IS NOW FULLY VISIBLE.** DESIGN §3 rewritten (reverses the 07-18 rule). He gets
NO glow and is treated as an ordinary character.
**⚠️ FACE LOCK — the consistency answer.** A single canonical description is pasted VERBATIM into all
7 prompts he appears in, so the generator produces the same man each time:
*"an Egyptian king of about fifty, the SAME man in every image — a lean hard clean-shaven face, high
flat cheekbones, a strong straight nose with a slight downward hook, heavy-lidded dark eyes, a thin
unsmiling mouth, a short square chin, deep vertical furrows between the brows, bronzed weathered
skin, wearing the striped blue-and-gold nemes headcloth with a rearing golden cobra at the brow."*
Rewritten: **P08a** (enthroned, cold ownership) · **P08b** (sharp on the dais above the prostrate
rows, deep focus) · **P19c** (low angle, front, pointing at the empty sky with total conviction) ·
**P31a** (shot from below past the pleading arms, flat bored contempt) · **P31c** (already looked
away to a scribe, faint satisfaction — this replaces the old "smirk" beat properly) · **P38a**
(sinking, eyes open, mouth parted mid-word, arrogance gone) · **P41b** (on the shore, face intact
and calm, EYES CLOSED, as though asleep).
**P08c and P31b deliberately stay hand-only detail shots** — a hand on the gilded throne arm is
still the better image and carries no consistency cost.
**⚠️ The shoreline stays non-gruesome by explicit negative:** P41b forbids wounds, blood, bloating,
discoloration, decay and all horror grammar. The beat is "the body preserved as a sign", not a corpse.
**QA at generation: check every Firaun image against the face lock; regenerate on mismatch.**
**3c — GLOW EVERYWHERE POSSIBLE. 11 new prompts, added as ALTERNATES** (the quiet object-only frames
are KEPT — you choose at edit time, nothing was destroyed):
**P10c** (mother holding the newborn, lamplit) · **P16a2** (the instant after the blow — hands raised
in horror; the fallen man has no wound, no blood, no face) · **P16b3** (walking the night desert,
front) · **P16d2** (sitting under the thorn tree, hands open in dua — alternate to the empty tree
P16d1) · **P16f3** (family in the rain, faces glowing) · **P16i2** (barefoot before the light,
sandals set aside — **the light source stays OFF-FRAME, nothing divine depicted**) · **P16j2**
(recoiling from the serpent) · **P16k2** (holding up his own radiant hand) · **P17c** (the two
brothers pausing at a rise, hand on shoulder, the city on the horizon) · **P18d** (both standing at
the foot of the dais, unintimidated, king out of focus) · **P36e** (staff still raised at the mouth
of the parted sea — the film's most impossible frame).

**FINAL VERIFIED STATE 2026-07-19:** **143 prompts** · 142 separators (correct n−1) · 143/143 carry
the photoreal clause · 22 glow prompts · 7 Firaun face-lock prompts · 0 stale "composed strictly from
BEHIND" instances left over from the old rule.
**Coverage = all 56 VO blocks.** ⚠️ Numbering note for anyone reading this file: the script's IDs run
01–53, but 16a/16b/16c/16d add four and «20-21» is a single block — so the true count is **56 VO
blocks, not 53**. This matters for TTS (56 clips) and for checking image coverage.

**Open items before generation starts:**
2. Evidence-layer licences UNVERIFIED (list above) — recon assumed for all modern imagery.
3. QA rule at generation: discard + regenerate any image where a face appears on a revered figure,
   Firaun, or the mummy. Cheaper than it was under video — one still, not a clip.
**Two accuracy errors caught by creator/audit 2026-07-19 — MUST carry into the rewrite:**
1. **The tabut (P11–P13):** wooden chest, cradle-sized, NOT a small reed basket — see Part 3
   fact-check + fact row 4a. Creator also flagged that **no proper floating-on-water frame existed**
   → P12a is now that shot, low to the water, box legible.
2. **Haman's tower (P19):** 28:38 = «kindle for me a fire, O Haman, upon the clay» → **FIRED/baked
   bricks**. Ma'arif-ul-Quran: half-baked brick can't carry a tall building; Firaun said to be first
   to bake hard brick. The shot needs **kilns, smoke, glowing stacks of baked brick** — my
   video-prompt P19 wrongly said "sun-dried mud bricks". Verified quran.com 28:38 + Ma'arif, 2026-07-19.

## Text-to-video research log (facts per chapter, verified 2026-07-18) — SUPERSEDED as approach, VALID as research
The per-chapter fact research below stands and feeds the image prompts unchanged.
- HOOK: NMEC Royal Mummies Hall = dark tomb-like rooms + branching corridors evoking the Valley of the Kings, dim spotlights make mummies seem to float, German anti-reflective glass cases, 20 royals (18 kings/2 queens) 17th–20th dyn (nmec.gov.eg). 1976: 26 Sept, French military transport, Le Bourget, red carpet, Garde Républicaine presenting arms, greeted by Sec. of State Alice Saunier-Seïté, live TV; Desroches Noblecourt accompanied (france24, ancient-origins).
- PART 2: mudbrick = Nile mud + chopped straw in open rectangular wooden molds ~30–45cm, sun-dried; workers with baskets/hoes; Rekhmire tomb depicts slaves making bricks; New Kingdom forced-labour cities Pithom & Raamses (biblicalarchaeology.org, africame.factsanddetails). Throne room = alabaster dais + steps, columned audience hall, faience-tiled painted walls, nemes headcloth + brow cobra (metmuseum, wikipedia Egyptian architecture).
- PART 5 (verified 2026-07-19): **Audience hall** — New Kingdom royal palaces (Malkata, Amenhotep III) were MUDBRICK with painted murals; the Grand Hall of Audience had 32 columns, a throne room with baldachin + clerestory lighting, tribute reliefs (exploreluxor.org, ancientegyptonline.co.uk, Wikipedia "Malkata"). So: painted papyrus-bud columns, faience-tiled blue/gold walls, alabaster dais + steps, clerestory light shafts — NOT bare stone temple. **Magicians** — Egyptian "magician" = the chief *lector priest* (ẖry-ḥb ḥry-tp), whose title became the Late-Egyptian word for magician; ritual costume = leopard-skin mantle over a white linen kilt, shaved head with a single plaited sidelock (Wikipedia "Lector priest", "Leopard skin (clothing in Ancient Egypt)", Met 547902/567608). **Snake trick** — the psylli charmers pressed the cobra's neck until it went rigid and could be held out horizontally *like a rod*; Egyptian serpent-cane depictions are read as this trick (Britannica "snake charming", encyclopedia.com "Psylli") — supports ropes/staffs read as snakes without any supernatural staging. **Tower/scaffold** — mudbrick + earth-and-rubble sloping ramps widened at the base as height grew, sledges dragged up; lashed timber scaffolding used for upper work (africame.factsanddetails, Wikipedia "Egyptian pyramid construction techniques", tigonscaffolding). **Festival ground/crowd** — New Kingdom festivals (Opet) filled the streets with all social strata; participants wore FRESH white linen + lotus-blossom floral collars; bread and beer distributed to the populace (worldhistory.org, Wikipedia "Clothing in ancient Egypt", Grokipedia "Opet Festival").
- PART 6 (verified 2026-07-19): **Locusts** — desert-locust swarms really do reach Egypt (Cairo, March 2013): the cloud reads as an ominous black mass that darkens the sky; one swarm eats ~100,000 tons of crops; 1915 Jerusalem plague photos show the sky-darkening scale (nationalgeographic, npr, nbcnews, Library of Congress/American Colony). So: false-dusk brown light + crawling carpets, not a thin scatter. **Blood-Nile** — "red tide" = mass bloom of red algae (diatoms/dinoflagellates) staining water opaque red; note the scientific counter-case (blooms need stagnant water; the pre-1970 flooding Nile was inhospitable) — so the film shows it as a **judgment event, never claimed as an explained natural cause** (livescience, iflscience, biblia.work). Visual: opaque dark red, heavy slow current, dead-still surface. **Village/houses** — New Kingdom villages (Deir el-Medina model) = rows of mudbrick houses, ~4 rooms, internal stair to a **flat usable rooftop terrace**, narrow alleys; rooftops are the authentic flood refuge (Wikipedia "Deir el-Medina", worldhistory.org, historyegypt.org). **Frogs** — the Egyptian species is *Sclerophrys (Bufo) regularis*, the square-marked toad: squat, warty, mottled ochre-brown — NOT a green pond frog. Frogs swarmed after the annual inundation, which is why Egypt had a frog goddess (Heqet) of fertility/rebirth — the sign inverts something they held sacred (Wikipedia "Sclerophrys regularis", "Heqet", Britannica).
- PART 7 (verified 2026-07-19): **Chariots** — Ramesside war chariot = light open wooden body, axle set at the REAR for stability, leather suspension, **six-spoked** wheels (the 4→6 spoke change happened late 18th/early 19th dynasty, ~1300 BC — so six is correct for ~1250 BC), drawn by a PAIR of horses under a yoke, crewed by a driver + an archer with a composite bow (Grokipedia "Chariotry in ancient Egypt", the-past.com, Carney/UMass Lowell PDF). **City gate** — the authentic New Kingdom fortified gateway is the **migdol**: Syrian-inspired twin-tower gatehouse in a massive mudbrick enclosure wall (Medinet Habu: ~35 ft thick, ~60 ft high), Ramesses III c. 1186–1155 BC (Grokipedia "Migdol"/"Medinet Habu"). Used for P34. **Crossing site — DELIBERATELY UNNAMED:** scholarship is split between a northern Bitter Lakes/Reed Sea route and a Gulf of Aqaba crossing, and *yam suph* is itself contested ("Reed Sea"); the Quran names no location either (Wikipedia "Gulf of Aqaba", armstronginstitute, biblearchaeology). So every shore prompt uses a generic wide sea + bare desert mountains — **readable as either candidate, asserting neither.** Same humility principle as the mummy-ID guardrail.
- **Shot-split note (2026-07-19):** storyboard P33 and P35 each carried TWO camera moves; one 10s clip = one move, so they were split into **P33a/P33b** (crane wide / child on shoulder) and **P35a/P35b** (whip-pan trap / lone back-turned figure). Part 7 = 7 clips, not 5.
- PART 8 (verified 2026-07-19): **Royal armour** — bronze/iron scales ARE found in Egypt but body armour was a foreign import and **not commonly worn**; scales were sewn onto a linen or leather backing (Tutankhamun's cuirass = leather scales; 10 scales excavated at Amenhotep III's palace; Met 577187). So P38/P41 show a **leather cuirass sewn with bronze scales** — never European-style plate. The **khepresh** (blue crown, "war crown") is leather or stiffened cloth covered with hundreds of discs/bosses; **no original example survives**, so it is rendered as an impression, not a replica (Wikipedia "Khepresh", Grokipedia, egypt-museum). This matches Ibn Kathir's «زرہ» detail — the body cast ashore in its *recognizable armour* (fact row 22) — without inventing hardware Egypt did not have.
- **Deir el-Bahari (for the seg-42 match cut)** — a natural amphitheatre-like BAY of towering near-vertical Theban limestone cliffs on the Nile's west bank, east of the Valley of the Kings; horizontally bedded Paleogene limestone, heavily fractured/jointed into hanging blocks and rock columns, scree fans at the foot. TT320 = a hidden shaft in a recess in the cliffs south of the temples, 21st-dynasty priests' reburial cache (Wikipedia "Deir el-Bahari", TT320; Theban-cliff geology papers).
- **Match-cut note:** a match cut is an EDIT, not a clip — P42 is generated as the Deir el-Bahari side only, framed to match P41's closing composition; the ancient half of the cut comes from P41's tail. No extra clip needed.
- DONE: HOOK (P01a–P03c), PART 2 (P06–P10), PART 3 (P11–P15), PART 4 (P16a–P17), PART 5 (P18–P23), PART 6 (P25–P32; P24 = card), PART 7 (P33a–P37), PART 8 (P38, P41, P42; P39/P40 = cards). **53 clips written.** NEXT: Part 9 (1881 + پیرس — P43–P46; P47/P48 = cards) → Part 10.

## Sign-off
- [x] Part 1 (Hook) approved by creator — 2026-07-18; 8 prompts written in image-prompts.txt
- [ ] Part 2 (غلاموں کا شہر) approved by creator — date: __
- [ ] Parts 3–10 drafted 2026-07-18 (full shot tables) — approve section-by-section; prompts written per part on approval
- [ ] Parts 2–10 drafted + approved (section by section)
- [ ] Mirrored into `storyboard.mjs`

## VO TIMING TABLE — the edit timeline (generated 2026-07-19)

56 clips in `studio/videos/firaun-ka-anjaam/assets/audio/seg-<ID>.mp3`, 1:1 with script segment
IDs. **Each scene's duration locks to its VO clip.** Start times are exact BY CONSTRUCTION
(sum of prior durations + prior gaps) per [[../../workflows/voiceover-tts]] Rule 0 — no
silencedetect, no drift, no FIX_START overrides. Re-roll one line → only its own clip and the
`start` column below it change.

Engine input: [[script-v1-devanagari-tts]] · voice Vikram S `st8o4LADtfxckX2PH08x`, `eleven_v3`,
seed 42, similarity 0.80, per-zone stability/style/speed. Regenerate: `venv/bin/python
tools/tts/generate_firaun_vo.py` (resumable — skips existing clips; `--only <id> --force` re-rolls one).

Gaps are added at ASSEMBLY, not baked into the TTS. Default 0.5 s; 1.0 s at chapter boundaries;
**3.0 s after seg 37** (the collapse — DESIGN §Sound: full sound then 3 s of nothing, VO silent);
1.5 s after 39 («اب؟» hard cut); 2.0 s after 52 (hold the final case).

| seg | zone | clip dur | START | gap after |
|---|---|---|---|---|
| 01 | default | 0:04.44 | **0:00.00** | 0.5 |
| 02 | default | 0:11.55 | **0:04.94** | 0.5 |
| 03 | default | 0:15.65 | **0:16.99** | 0.5 |
| 04 | default | 0:17.01 | **0:33.13** | 0.5 |
| 05 | default | 0:22.75 | **0:50.64** | 1.0 |
| 06 | warm | 0:15.57 | **1:14.39** | 0.5 |
| 07 | warm | 0:23.48 | **1:30.46** | 0.5 |
| 08 | warm | 0:21.32 | **1:54.45** | 0.5 |
| 09 | warm | 0:19.33 | **2:16.26** | 0.5 |
| 10 | warm | 0:12.67 | **2:36.09** | 1.0 |
| 11 | warm | 0:25.73 | **2:49.76** | 0.5 |
| 12 | warm | 0:20.69 | **3:15.99** | 0.5 |
| 13 | warm | 0:23.25 | **3:37.18** | 0.5 |
| 14 | warm | 0:18.91 | **4:00.93** | 0.5 |
| 15 | warm | 0:29.73 | **4:20.34** | 1.0 |
| 16 | warm | 0:52.69 | **4:51.07** | 0.5 |
| 16a | warm | 1:09.07 | **5:44.26** | 0.5 |
| 16b | warm | 0:45.56 | **6:53.83** | 0.5 |
| 16c | reverent | 0:49.71 | **7:39.88** | 0.5 |
| 16d | warm | 0:33.88 | **8:30.10** | 0.5 |
| 17 | warm | 0:59.01 | **9:04.48** | 1.0 |
| 18 | default | 0:21.79 | **10:04.49** | 0.5 |
| 19 | default | 0:25.23 | **10:26.77** | 0.5 |
| 20-21 | default | 0:27.48 | **10:52.51** | 1.0 |
| 22 | default | 0:21.63 | **11:20.99** | 0.5 |
| 23 | default | 0:24.76 | **11:43.12** | 1.0 |
| 24 | default | 0:16.04 | **12:08.88** | 0.5 |
| 25 | default | 0:22.91 | **12:25.42** | 0.5 |
| 26 | default | 0:18.29 | **12:48.83** | 0.5 |
| 27 | default | 0:21.39 | **13:07.62** | 0.5 |
| 28 | default | 0:24.03 | **13:29.51** | 0.5 |
| 29 | default | 0:19.57 | **13:54.04** | 0.5 |
| 30 | default | 0:21.71 | **14:14.11** | 0.5 |
| 31 | default | 0:24.76 | **14:36.32** | 0.5 |
| 32 | default | 0:14.21 | **15:01.58** | 1.0 |
| 33 | tension | 0:16.59 | **15:16.79** | 0.5 |
| 34 | tension | 0:19.96 | **15:33.88** | 0.5 |
| 35 | tension | 0:28.11 | **15:54.34** | 1.0 |
| 36 | tension | 0:24.35 | **16:23.44** | 0.5 |
| 37 | tension | 0:23.72 | **16:48.29** | 3.0 |
| 38 | tension | 0:21.16 | **17:15.01** | 0.5 |
| 39 | tension | 0:27.09 | **17:36.67** | 1.5 |
| 40 | reverent | 0:21.39 | **18:05.26** | 0.5 |
| 41 | default | 0:22.99 | **18:27.15** | 0.5 |
| 42 | default | 0:16.04 | **18:50.64** | 1.0 |
| 43 | cool | 0:17.55 | **19:07.68** | 0.5 |
| 44 | cool | 0:26.04 | **19:25.73** | 0.5 |
| 45 | cool | 0:19.33 | **19:52.28** | 0.5 |
| 46 | cool | 0:31.01 | **20:12.11** | 1.0 |
| 47 | brisk | 0:19.64 | **20:44.12** | 0.5 |
| 48 | brisk | 0:32.44 | **21:04.26** | 1.0 |
| 49 | cool | 0:30.85 | **21:37.70** | 0.5 |
| 50 | cool | 0:41.40 | **22:09.05** | 1.0 |
| 51 | reverent | 0:22.36 | **22:51.46** | 0.5 |
| 52 | reverent | 0:11.47 | **23:14.32** | 2.0 |
| 53 | default | 0:26.04 | **23:27.79** | 0.5 |

**TOTAL RUNTIME: 23:54.33** (1434.3s).

### ⚠️ Runtime drift vs the script's built-in chapter marks

Target 21:30–22:30 → **over the ceiling by 1:24**. It is NOT spread across the film; one chapter
owns it and the rest of the film is running *under* budget:

| chapter | budget | actual | drift |
|---|---|---|---|
| میوزیم میں ایک لاش | 1:30.00 | 1:14.39 | −0:15.61 |
| غلاموں کا شہر | 2:15.00 | 1:35.37 | −0:39.63 |
| دریا میں صندوق | 2:00.00 | 2:01.31 | +0:01.31 |
| مدین سے طُور تک | 2:30.00 | 5:13.42 | +2:43.42 ⚠️ |
| چرواہا اور بادشاہ | 2:00.00 | 2:04.39 | +0:04.39 |
| نشانیوں پر نشانیاں | 2:15.00 | 3:07.91 | +0:52.91 ⚠️ |
| رات کا سفر | 1:15.00 | 1:06.65 | −0:08.35 |
| سمندر پھٹ گیا | 1:05.00 | 0:51.57 | −0:13.43 |
| آخری سانس کا ایمان | 1:05.00 | 0:50.25 | −0:14.75 |
| «تیرا بدن بچا لیں گے» | 1:10.00 | 1:02.42 | −0:07.58 |
| 3000 سال بعد — ایک بکری | 1:05.00 | 1:04.43 | −0:00.57 |
| پیرس میں ایک بادشاہ | 1:40.00 | 1:25.60 | −0:14.40 |
| نشانی آج بھی | 1:00.00 | 1:13.75 | +0:13.75 |
| عبرت اور آخری بات | 1:10.00 | 1:02.87 | −0:07.13 |

**Responsible segments — «مدین سے طُور تک» (+2:43):** the v2.1 Madyan expansion budgeted 2:30
reads **5:13**. The five longest clips in the entire film are all in this one chapter:
**16a (1:09) · 17 (0:59) · 16 (0:53) · 16c (0:50) · 16b (0:46)**. Secondary: «نشانیوں پر نشانیاں»
(+0:53, segs 24–32 — the v2 per-plague expansion).

Everything else nets **−2:12 under** budget, which already absorbs most of the overrun. Options:
1. **Ship at ~23:54** — the Madyan chapter is a deliberate v2.1 addition and retention loop #6
   («نرمی کا دروازہ») depends on 16c/16d/17. Nothing is padded; the chapter is just bigger than
   its original estimate.
2. **Trim ~90 s from 16a + 17 only** → lands ≈22:24, inside the window, leaving 16c (the kalam)
   and the loop-6 payload untouched. 16a carries the most compressible material (the well
   sequence + the 8/10-year term detail).
3. Trim the plague chapter instead — but that reverses the v2 decision to give each sign 2–3 lines.

Re-generating after a trim costs **only the trimmed clips** — that is the whole point of Rule 0.


## ✅ GATE ③ IMAGE AUDIT — 2026-07-19 (all 141 stills viewed)
Full result + re-gen worklist: **[[image-audit]]**. Headlines:
- **135 / 143 scenes covered.** Files renamed to scene IDs (`P16c2.jpeg`, alternates `-alt1`);
  3 byte-identical dupes moved to `assets/images/_dupes/` (nothing deleted).
- **8 missing:** P13b · P20c · P20d · P22a · P22b · P38a · P41a · P50a.
  ⚠️ P20c/P20d/P22a/P22b = the **whole swallow-and-sujood interrupt (segs 20–22) is uncovered** —
  top re-gen priority. P38a is a face-lock scene, so the sinking↔shoreline match can't be QA'd yet.
- **6 depiction violations:** P10c, P14a-alt1, P16d2, P16e1, P16c2 (glow failures — features or
  face-edges readable) + **P19c (fired-brick error recurred)**.
- **Held:** Tuwa (P16g1/h1/h2) has no figure or form — no-divine-depiction survived intact.
  The صندوق correction held on every P11–P13 frame. P35c/P36e glows are textbook.
- **Open creator decision (blocks P16e1):** does the **old man of Madyan** get the glow, or stay
  hands-only? [[DESIGN]] §DEPICTION still marks this ⚠️ OPEN; the generator assumed the glow.

## 🎬 BUILD STATE — 2026-07-19 (chapter-wise, §5c)

**Scaffold:** `studio/videos/firaun-ka-anjaam/build.py --chapter N` → `index.html`, + `draft-all.sh`.
Adapted from the Pompeii build, but **the whole silencedetect / char-weight / FIX_START relock
stack is GONE** — per-line TTS means each segment's span is just `probe(seg-NN.mp3) + gap`, and
scenes split it by weight. Every chapter's rendered duration reproduces the VO TIMING TABLE to the
centisecond, first try. gsap vendored at `assets/gsap.min.js`; Nastaliq/Archivo/Playfair in
`assets/fonts/`.

| ch | segs | built | render | vs drift table |
|---|---|---|---|---|
| 1 HOOK | 01–05 | ✅ | `renders/ch1-draft.mp4` 1:14.4 | ✔ 1:14.39 |
| 2 غلاموں کا شہر | 06–10 | ✅ | `ch2-draft.mp4` 1:35.4 | ✔ 1:35.37 |
| 3 دریا میں صندوق | 11–15 | ⛔ | — | blocked: **P13b** missing |
| 4 مدین سے طُور تک | 16–17 | ✅ | `ch4-draft.mp4` 5:13.4 | ✔ 5:13.42 |
| 5 چرواہا اور بادشاہ | 18–23 | ⛔ | — | blocked: **P20c·P20d·P22a·P22b** missing + P19c |
| 6 نشانیوں پر نشانیاں | 24–32 | ✅ | `ch6-draft.mp4` 3:07.9 | ✔ 3:07.91 |
| 7 رات کا سفر + سمندر | 33–37 | ✅ | `ch7-draft.mp4` 1:58.2 | ✔ 1:06.65+0:51.57 |
| 8 آخری سانس + تیرا بدن | 38–42 | ⛔ | — | blocked: **P38a·P41a** missing |
| 9 1881 + پیرس | 43–48 | ✅ | `ch9-draft.mp4` 2:30.0 | ✔ 1:04.43+1:25.60 |
| 10 نشانی آج بھی + end | 49–53 | ⛔ | — | blocked: **P50a** missing |

**Ch2 and Ch4 shipped by DROPPING the non-compliant alternates, not by using them:**
Ch2 without P10c; Ch4 without P16c2/P16d2/P16e1/P16f2 — so **seg 16a has no Madyan elder at all**
(P16e1 is the only frame for that beat and has no compliant sibling). Re-check 16a after re-gen.

**Audit items resolved in-comp (no re-generation needed):** P46b's colour-vs-1976-B&W fault is
fixed by the chapter's `grayscale(1)` newsreel grade · the four bar'd frames (P30a/P35b/P11b/P37b)
carry measured static crops · the Ken-Burns-tight set (P45a/P50c/P16f3/P03d) is capped at 1.08.

**Open for creator (found at Gate ③ render, not in the still audit):**
1. **P08a breaks the Firaun face lock on screen** — long striped false beard, rounder softer face;
   demonstrably a different man from P31a two chapters later. Both are on screen in the same film.
   Re-gen against P31a (the audit's "cleanest reference").
2. **P17a's glow is a hard-edged white oval with a readable face OUTLINE** — the rule asks for a
   veil blending softly into hair/headcloth with no outline. Front-on and full-screen for 13 s.
   Not flagged by the still audit; creator's call.
3. **VO peaks −0.6 to −0.9 dBFS**, above the −1 dBTP guard (§3). That's the TTS clips themselves.
   **The final encode needs a limiter** or the music bed will push it into clipping.

**Still absent from every chapter:** SFX, music bed, the 0.5 s exposure bloom at era hops.
Sound design starts at assemble, per §5d.

**Two process learnings for the next video:**
1. **Reconcile by scene coverage, not file count.** 141 files looked like 5 gaps; 3 were second
   takes of scenes that already had one, so the real gap was 8. Count what's *covered*.
2. **A corrected fact row is ~75% effective, not 100%.** The fired-brick fix landed on P19a/b/d
   and regressed on P19c. Re-verify every sibling scene of a corrected error, not just the error.

## ⚠️ RE-LINED TO 307 LINES — 2026-07-22 (creator: fix the timeline/image mismatch at the root)

**Diagnosis (creator, confirmed by the drift table above):** the script was written as **56
paragraphs**, and the pipeline made ONE VO clip per paragraph → clips ran 1–5 min (Madyan = 5:13,
its longest clip 69 s). The timeline therefore anchored only once per paragraph, and 3–4 scene
images under it were split by **guessed weights** → images drift seconds off the words. That is the
mismatch. **Root fix: author the script in single-sentence LINES, one clip per line.**

**What changed:**
- 56 paragraphs → **307 lines** (one line = one spoken sentence ≈ 1–8 s). Nastaliq + Devanagari
  re-lined in lockstep, **byte-reconstruction verified** (no word / citation / guardrail changed —
  only line breaks inserted; the split SLICES the source, never retypes — a retype silently swaps
  لاش↔लाश and corrupts TTS).
- New canonical: [[script-v2-nastaliq-lines]] (human master, 307 lines + `[scene]` cues + inline
  cites) and [[script-v2-devanagari-lines]] (TTS engine input). v1 paragraph scripts kept for
  provenance but SUPERSEDED as the edit master. The old paragraph VO-timing + build-state tables
  above are **superseded** — the live timeline is `generate_firaun_vo.py --table` (307 rows).
- **Tiered gap model** (assembly-time, not baked into TTS): 0.20 s breath within a paragraph,
  0.40 s at a segment boundary, 1.0–3.0 s only at the marked beats. A flat 0.5 s would add ~2.5 min.
- `build.py` is now **line-driven** (one line = one clip = one scene, NO weight-split); old at
  `build-v1-paragraph.py`. `generate_firaun_vo.py` parses the v2 Devanagari master. Note:
  `eleven_v3` rejects previous_text/next_text stitching — continuity is seed+voice only.

**v2 BUILD STATE — 2026-07-22 (all VO regenerated: 307/307 clips, total 23:05.9, in the 21:30–24:00 window):**

| ch | segs | lines | dur | render | held (missing still) |
|---|---|---|---|---|---|
| 1 | 01–05 | 20 | 1:08.1 | ✅ ch1-draft.mp4 | — |
| 2 | 06–10 | 21 | 1:29.7 | 🔄 rendering | — |
| 3 | 11–15 | 33 | 1:55.7 | 🔄 | **P13b** |
| 4 | 16–17 | 55 | 5:00.5 | 🔄 | — |
| 5 | 18–23 | 26 | 2:04.7 | 🔄 | **P20c·P20d·P22a·P22b·P19c** |
| 6 | 24–32 | 48 | 3:01.1 | 🔄 | — |
| 7 | 33–37 | 26 | 1:51.1 | 🔄 | — |
| 8 | 38–42 | 30 | 1:51.7 | 🔄 | **P38a·P41a** + cards P39/P40 unauthored |
| 9 | 43–48 | 20 | 2:25.7 | 🔄 | — |
| 10 | 49–53 | 28 | 2:17.6 | 🔄 | **P50a** + ch10 cards unauthored |

**Timeline sync PROVEN on ch1:** rendered duration 68.1 s = the built span to the centisecond; every
scene sits on its own line's clip. Fully-covered chapters (1,2,4,6,7,9) are proof-quality drafts;
chapters 3/5/8/10 render with **held-image placeholders** for the missing stills (still sync-correct)
and need the 8 missing images + the un-authored cards before final. Image re-gen is the remaining
dependency (semi-manual via the prompt-runner — prompts are one-shot-ready in [[image-prompts]]).
