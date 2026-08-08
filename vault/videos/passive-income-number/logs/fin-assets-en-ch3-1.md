---
summary: en ch3 sourced from scratch — 16 backgrounds (s24–s39), every file ≥1600px, every source p90 ≥126 against the 110 gate, zero md5 collisions and zero URL collisions across both cuts, `check assets --chapter 3` PASS. 40 contact sheets / ~232 candidate cells; 16 accepted, 216 rejected, 0 dropped. Ten images passed their contact sheet and were killed by the full-resolution read — PEUGEOT on a keyfob, EMCO WHEATON on a fuel nozzle, a German Bible under the Trinity quote, and a MacBook whose lit screen the sheet showed as "a closed laptop". p90 spread widened from ch1's 12 points to 68 (predicted post-grade).
updated: 2026-08-08
source: fin-assets attempt 1, chapter 3, en cut — VO 3.1–3.16, storyboard-en §7/§8/§10/§11.
---

# fin-assets — passive-income-number / en / chapter 3 / attempt 1

**PASS `python3 tools/pipeline_check.py check assets --slug passive-income-number --cut en --chapter 3`.**
Negative control: the same command **without** `--chapter 3` FAILs (it reads `-en/assets/img/`,
ch1's manifest) — the flag is what makes the licence assertion reach these 16 files.

**Accepted 16 · rejected 216 · dropped 0.** Chapters 1 and 2 untouched. `assets/lottie/`
untouched — ch3's only drawn layer is `housing-share` on s30, an SVG the build authors, not a Lottie.

Project created at `studio/videos/passive-income-number-en-ch3/` on the ch1/ch2 layout:
`assets-ch3/final/` (the only place new files landed) plus `assets/` symlinks to the shared
`blockframe.css`, `chapter-design.css`, `fonts`, `img`, and the cut's `voice/`, with `js/` copied
from ch2. No `index.html` yet — that is fin-build's.

| slot | line | subject | W×H | src p90 | YAVG | pool |
|---|---|---|---|---|---|---|
| s24 | 3.1 | cars parked kerbside on a dark rowhouse street, double yellow centre line | 1880×1253 | 126 | 64 | pexels |
| s25 | 3.2 | fuel nozzle in a red car's filler neck, no hand, forecourt blurred out | 1733×1300 | 220 | 157 | pexels |
| s26 | 3.3 | aerial parking lot of ordinary cars, golden hour, painted bays | 1733×1300 | 199 | 127 | pexels |
| s27 | 3.4 | chrome door handle + window trim of a dark old sedan, shallow DOF | 1880×1255 | 131 | 59 | pexels |
| s28 | 3.5 | bank of steel mailboxes receding, red header band | 1880×1251 | 213 | 137 | pexels |
| s29 | 3.6 | US suburban street of two-storey brick houses at dusk, flag, no people | 1880×1256 | 216 | 112 | pexels |
| s30 | 3.7 | roof ridge silhouetted against an orange dusk sky (art-forward, calm) | 1880×1253 | 138 | 81 | pexels |
| s31 | 3.8 | brass-collared door knob with keyhole on a plain wooden door, hard sun | 1880×1256 | 168 | 78 | pexels |
| s32 | 3.9 | American front porch — white balusters, brown door, picket fence | 1880×1253 | 200 | 134 | pexels |
| s33 | 3.10 | hands (no face) leafing a thick stapled document on a glass desk | 1880×1253 | 148 | 90 | pexels |
| s34 | 3.11 | contract fine print with a pen — clauses 9/10, signature line | 1733×1300 | 217 | 183 | pexels |
| s35 | 3.12 | blank IRS **1040** + 1040-SR on a black ground, "Tax time!" sticky | 1880×1253 | 231 | 143 | pexels |
| s36 | 3.13 | black wall clock, plain white dial, on oak slats | 1880×1045 | 181 | 97 | pexels |
| s37 | 3.14 | open book under a desk lamp against a deep blue wall, text illegible | 1880×1245 | 194 | 67 | pexels |
| s38 | 3.15 | empty two-lane highway to the horizon, yellow centre line, flat light | 1733×1300 | 163 | 88 | pexels |
| s39 | 3.16 | closed laptop lid on a pale desk, soft daylight, no logo, no screen | 1880×1253 | 187 | 148 | pexels |

Every file ≥1600px on the long edge. Every source p90 (ffprobe `signalstats.YHIGH`) ≥126 against
the 110 gate. **Zero md5 collisions** across all 128 jpgs in `studio/videos/` (the only duplicate
hashes on disk are the hi cut's own pre-existing `style-a/` ↔ `final/` mirrors and two render
sheets — none is a ch3 file), and **zero source-URL collisions** against ch1/ch2 of both cuts.

---

## 1. TONE — the p90 spread, as a number (ch1 carry-forward)

ch1's CEO note: *"p90 36-48 on all eight scenes, nothing bright in 46 seconds."* That figure was
measured on **rendered** frames (photo + grade + `.field` + scrims); mine are measured on the
**sources**, so the two are not the same scale. Both are given, plus the source figure pushed
through the locked grade arithmetically (`grayscale(.32)` is chroma-only; `brightness(.62)` then
`contrast(1.05)` ⇒ `y' = ((0.62y/255 − 0.5)·1.05 + 0.5)·255`) so the next gate has a comparable
number rather than an impression:

| | min | max | **spread** |
|---|---|---|---|
| source p90 | 126 (s24) | 231 (s35) | **105** |
| predicted post-grade p90 | 76 (s24) | 144 (s35) | **68** |
| ch1, rendered | 36 | 48 | **12** |

Per scene, predicted post-grade p90: s24 **76** · s27 **79** · s30 **83** · s33 **90** · s38 **100** ·
s31 **103** · s36 **111** · s39 **115** · s37 **120** · s26 **123** · s32 **124** · s28 **132** ·
s29 **134** · s34 **135** · s25 **137** · s35 **144**.

The chapter is deliberately shaped, not merely varied: it **opens dark** (s24 at 76, a night
street — the darkest frame in the chapter), climbs through the rung-two block, peaks in the
fine-print run (s34/s35 at 135/144, both white paper), and the two frames flanking the shove are
mid (s38 100 → s39 115). The four darkest are s24, s27, s30, s33; the four lightest are s35, s25,
s34, s29. **Nothing sits in ch1's 36–48 band** and no two adjacent scenes are within 5 points except
s28→s29 (132→134), which is one argument (rung three named, then its yearly figure).

⚠ The one thing to watch in the draft: **s34 (YAVG 183) and s35 (YAVG 143) are the chapter's two
white-paper frames and they are adjacent.** Both have real structure under the grade — s34 is a
raking-light macro with a black pen and a dark wood edge, s35 is white forms on a black ground —
so neither is the flat-charcoal failure. But they are the pair to look at first on the sheet.

## 2. Ten images passed the contact sheet and died at full resolution

This is again where the stage earned its keep. Every one of these was invisible at 512×288.

| slot | what the sheet showed | what the full-resolution read found | fix |
|---|---|---|---|
| **s39** | "a closed laptop, dark room, lamp" | an **open MacBook with the screen glowing white** — the standing no-lit-screen rejection, and p90 **12** because the lit slab is <10% of a black frame (the percentile gate catches exactly this) | re-query ×2 → a genuinely closed lid |
| **s31** | a single brass key on dark wood | **`R.M.I.` engraved on the key bow** — a maker's mark — and p90 **46**, far under the gate | 2 re-queries → door knob |
| **s25** | a black nozzle in a filler neck | **`EMCO WHEATON VAPOR RECOVERY NOZZLE`** logo + wordmark, dead centre, ~15% of frame width | free re-pick → cell 1 |
| **s27** | "black key + brown leather fob, no logo" | **`PEUGEOT`** embossed across the fob in 60px letters — a brand mark *and* a car not sold in the US | re-query → chrome door handle |
| **s34** | reading glasses on an open book, black ground | the book is a **German Bible** — `aus dem Mund des Gottlosen`, `HERRN`, `Gerechten` fully legible. Foreign-language text, and a Bible under a line about the **Trinity** study is the worst available coincidence in this chapter | re-query → contract fine print |
| **s24** (r2) | two ordinary cars in a US driveway at dusk | **`BENTLEY BULLDOG`** on the licence-plate frame + a legible Ford oval — a luxury brand word under a line about the average household's car | re-pick |
| **s24** (r3) | a silver sedan beside a clapboard house at night | a large, clean **VW roundel** centred on the grille | re-query → distance kills legibility |
| **s26** (r4) | a calm empty parking deck | p90 **86**, and its brightest sibling cell measured **81** — the whole family is under the gate | change subject → aerial lot |
| **s36** (r1) | a station clock on an industrial ceiling | **`MOBATIME`** on the dial (faint, ~3% of width, but it is a brand mark and s25/s27 were killed for the same class) | free re-pick → cell 4, dial clean |
| **s35** (r1/r2) | "a 1040 and a pen" ×5 cells | **`1040-NR-EZ — U.S. Income Tax Return for Certain Nonresident Aliens`**, legible, on five of six cells across two sheets. The stock pool's default US tax form is the *nonresident* one | 3rd query → the real 1040 |

**The reusable finding: the fix for a brand mark is DISTANCE, not another synonym.** s24 took four
sheets and 24 candidates because every car photograph carries a badge; the query that finally
worked (`car parked under a street light on a dark empty residential street at night wide`) solved
it by putting the car far enough away that no badge resolves. Same root cause as ch2's
denomination rule — the query, not the filter, is where legibility is decided.

## 3. Slots where the OBJECT had to change, logged so a later pass does not "fix" them back

### s26 (3.3) — the four slips on a dashboard do not exist. 6 sheets, 36 candidates.
Queried: paper slips on a car dashboard · crumpled receipts on dark wood · steering wheel and
dashboard at night · empty concrete parking garage · car wheel and tyre · aerial parking lot.
The pools answer with **high-key white desks** (the same white-desk-with-orange-slips photograph
came back on three different queries), **lit instrument clusters and infotainment screens** (all
six of the steering-wheel sheet, every one carrying a Nissan/Subaru/Mitsubishi logo on the boss),
**wheels with the badge as the subject** (Mercedes, `CIVIC TYPE R`, Ford, GT-R), or **Turkish lira
and euro notes**. The parking-deck family was calm and on-brief and failed the luminance gate at
86 and 81. The resolved object is an **aerial parking lot of ordinary cars at golden hour** —
calm and repetitive (this is a 4-chip cascade, so §10 routes it to the quietest available frame),
bright (p90 199, one of the chapter's lightest), unmistakably "what the car costs", and with **no
countable subject** so it cannot fight the four chips (§7's note that s26 is deliberately *not*
counted). Storyboard §10's "3.3's four slips get no cut-in **because they are in the s26 bg**" is
therefore no longer true of the photograph: the four items live **only** in the chips now. That is
a build fact, not a re-fetch instruction.

### s27 (3.4) + s31 (3.8) — the two keys became two ways IN.
The storyboard asks for a car key (s27) and, by its own override, a brass house key on dark slate
(s31). Three sheets each: every car key in the pool is a **branded fob** (Jeep, Mercedes ×2,
Peugeot, Jaguar) and every "single brass house key" is either a **pile** of keys (which kills the
word *single*), an `IKON`-branded blank, or a white-background macro. Resolved as a matched pair
one step out: **s27 = the chrome door handle of a dark old sedan**, **s31 = the brass-collared
door knob of a plain wooden door**. Both are entry points, both are specular (the material rule —
brass and chrome have the ceiling the gate needs; s31 measures 168 against the rejected key's 46),
both are badge-free and text-free, and they now **rhyme across the two rungs** the way s19/s21 and
s29/s31 rhyme in the type. Sound-off gate 3 holds for each: the thing the line names (the car,
the home) is in frame.
⚠ Provenance note for the editor: s27's Pexels title is *"close up of mercedes w126 livery"*. **No
badge, no lettering and no identifying body panel is in the frame** — only the door skin, chrome
window trim and handle — so nothing on screen names the make. Flagged because the credit line does.

### s37 (3.14) — 6 sheets, 36 candidates, and the pool only sells *books*.
Queried: a report open at its last page · stapled pages with a paper clip · a typewritten
manuscript · a paragraph underlined in red pen · a stapled corner macro · a single sheet under a
desk lamp. Returns were Turkish (`Unutulan`), German, Polish, Vietnamese and Bible pages — five
sheets in which **something legible and foreign, or something legible and religious, sat in the
middle of the frame** — plus one legible `11 %` (a percentage figure, on a video about withdrawal
rates: the worst kind of accidental claim) and one film script titled `THE WIFE`. Resolved as an
**open book under a desk lamp on a deep blue wall**: the text dissolves into grey blocks at full
resolution, there is no title, figure or agency name anywhere (§10's rule for s37), and the blue
ground is the only one of its colour in the chapter.

## 4. The three paper frames, and the ch2 family they sit next to

3.10 / 3.11 / 3.14 are all "a document" and they are four scenes apart. They were chosen to be
legibly three photographs, per the per-line rule:

- **s33** — hands and a thick stapled stack seen along a glass desk, mid-distance, cool grey.
- **s34** — a top-down raking-light macro of one page's clauses with a pen, warm white, no hands.
- **s37** — an open book under a lamp, wide, dark blue, page dissolved.

Different scale, different ground, different subject in each. ⚠ For fin-editor: **en ch2 already
holds s13 (white book page on black) and s15 (a white book)**, so s37 is the fifth
book-or-paper frame in the cut. It is a different photograph and a different statement, but the
family is now the cut's densest and ch4 should not add a sixth.

## 5. Sound-off gate — the two weakest, named before review finds them

1. **s30 (3.7)** is a roof ridge with pigeons on it, not a house. It is the storyboard's own
   override ("a house roofline silhouetted against a warm dusk sky") and this scene is
   `art-forward` — the drawn `housing-share` bar is what states 33.4%, and §10 routes art-forward
   frames to the calmest subject there is. A two-band silhouette with a dark lower half is exactly
   that, and it gives the type a clean field. But covering the words, "housing" is the *second*
   thing you would say after "sunset". Weakest gate-3 fit in the chapter.
2. **s39 (3.16)** is a cropped corner of a closed laptop lid. It reads "the laptop is shut" and
   nothing more, which is all the beat (`kicker only`, 3.5s, straight into the SHOVE) needs — but
   it is abstract, and it is the chapter's second-lightest frame under a ground (`#101720`) that
   the storyboard describes as ending "empty and cold". The cold has to come from the `.field`,
   not from the photograph.

Two frames I checked and cleared rather than assumed:
- **s35's form is legibly dated `2020`** (~55px on the source). No line in ch3 makes a year claim,
  the form is the genuine current-shape 1040, and every tax-form photograph in both pools carries
  some year. Kept deliberately; flagged so the editor is not surprised by it.
- **s32 has a partially cropped red sign at the extreme left edge** (`…LER / …ARM / … 911` — a
  sprinkler-alarm plate) and a house number `1` in the top-right corner. Not a brand, not a
  fabricated source, and both sit in the outer 3% that `inset:-8%` full-bleed pushes off-frame.

## 6. THE TANK OBJECT FAMILY — recorded for ch5 (ch1 carry-forward s10)

**No scene in s24–s39 touches the vessel / tap / flow family**, so nothing in this chapter needed
to rhyme with it and nothing in this chapter constrains it further.

I read `studio/videos/passive-income-number-en-ch2/assets-ch2/final/s10.jpg` at full resolution
before briefing anything. **The object noun, for s46 / s47 / s57 to inherit, is:**

> **a row of seven aged brass tap valves with turned brass lever handles, bolted along a
> horizontal steel manifold above a long copper-brown trough, against a white-tiled wall in raking
> daylight.** Not a tank. There is no vessel in the frame at all — the taps and the trough are the
> whole object. `s10b` is the same photograph cropped tighter on the nearest two taps.

So the recognisable constant that ch5's fetch must match is **aged brass lever tap + steel/copper
industrial plumbing under daylight**, and the beat has to be carried by **tap position and flow**
(§10's own fallback: "the tap is what carries the rhyme, not the tank's silhouette"). A domestic
faucet, a garden spigot or a barrel bung will not read as a callback to this frame; a brass lever
valve on metal pipework will.

## 7. Counts

| | |
|---|---|
| contact sheets built | **40** (16 slots; 8 slots re-queried 1–5 times each) |
| candidate cells actually rendered | ~232 (two sheets came back short — s29 rendered 1 of 6, s34 r1 rendered 3 of 6) |
| accepted | **16** |
| rejected | **216** — 63 legible foreign/brand/agency text · 41 people or faces · 38 wrong object · 34 high-key white-dominant · 18 under the p90 gate · 12 lit screens · 10 off-tone or arguing (a `11 %`, a Bible, a film script, sports cars) |
| dropped | **nothing** — every background was replaced, never dropped |
| promoted then killed at full resolution | 10 |
| Pexels searches | 40 · Pixabay 0 · Commons 0 |
| free re-picks (no fetch) | 4 |
| lottie work | none — ch3 asks for none |

## 8. Verification performed

- `check assets --slug passive-income-number --cut en --chapter 3` → **PASS**; without the flag it
  FAILs on ch1's manifest (negative control run).
- **16 manifest keys ≡ 16 CREDITS rows ≡ 16 `.src` sidecars**, checked programmatically; every
  `.src` byte-equal to its manifest query, so no exploratory query survives as false provenance,
  and every re-pick's credit row was rewritten to the image actually on disk (verified line by
  line against the final files — no stale attribution from a killed candidate).
- **md5 sweep across all 128 jpgs under `studio/videos/`** — no ch3 file collides with anything.
- **Cross-pool duplicate check by hand** (md5 cannot see it — the trap that caught en ch2's s14):
  one of the 16, **s34, is credited "by Pixabay" on Pexels**, which is the tell. Its URL and
  subject were checked against every CREDITS row in hi-ch1, hi-ch2, en-ch1 and en-ch2 — no overlap;
  the two "by Pixabay" images in the hi cut are an adding machine, not a contract.
- `index.html` does not exist yet (fin-build has not run), so pipeline_check's render-time
  attribution half is skipped — expected at this stage.

## 9. For fin-build

- Every scene has a real `.bg`; no scene is photo-free; **no per-scene `filter:` override is needed
  or set** — nothing measured near-black (the darkest source p90 is s24 at 126, sixteen points
  above the gate), so the locked grade stands unamended for the whole chapter.
- **s26's photograph no longer contains the four slips** (see §3) — the `Payment · Insurance ·
  Fuel · Repairs` cascade is the only place those four words appear. Do not cut the chips.
- s30 is the chapter's one `art-forward` scene and its lower ~55% is a near-black silhouette band:
  the `housing-share` bar and `.art-lift` sit well on it, but the `#s30-sub` qualifier will need
  the light half.
