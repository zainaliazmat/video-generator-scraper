---
summary: fin-assets for japanese-money-methods hi cut, attempt 1. All 94 image files sourced, every one viewed at contact-sheet size and the high-risk ones at full resolution. 0 md5 collisions, all 7 RAIL OFF slots ≥1600px. s65 (the four-group flat-lay) escalates as specified — no cell in either pool shows four distinct groups.
updated: 2026-08-01
source: tools/stock/pixabay_fetch.py (Pixabay + Pexels), storyboard-hi.md §7/§9, vault/knowledge/stock-photo-sourcing.md
stage: fin-assets, cut hi, attempt 1
---

# fin-assets — japanese-money-methods-hi, attempt 1

## Result

| | |
|---|---|
| Slots required | 97 (92 bg + 5 cut-in), **94 files** (3 bg re-use a hold partner) |
| Files delivered | **94 / 94** — zero photo-free scenes |
| Contact sheets built | 12 rounds, ~700 previews, one vision pass per sheet |
| Cells rejected | ~470 of ~700 (see traps below) |
| md5 collisions across all projects | **0** |
| RAIL OFF / hold slots ≥1600px | **7 / 7** (17 files total at 1880px, all Pexels) |
| CREDITS.txt | 94 lines, one per kept file; 19 stale lines from re-picks pruned |
| `.src` sidecars | 94, written by the tool from the promoted query |
| `manifest.json` | rebuilt from the `.src` files — 40 slots now carry a revised query |

## The escalation — s65, the four-group flat-lay

**Confirmed not sourceable.** Two Pexels sheets (base query and `#6` offset), twelve cells:
every one is a scatter or a fan of ₹500 notes with loose coins. **No cell shows four
distinct groups, and none carries a handwritten label of any kind.** The storyboard's §12
prediction was right.

Per the run brief I did **not** force a wrong image and did **not** degrade it to a text
card. The slot ships with the closest honest photograph so no scene is photo-free:

- `s65.jpg` — a top-down **radial fan of current-series ₹500 notes with a ₹20 coin centred**
  (Pexels, 1880px, verified at full resolution: three different serials visible, stone-grey
  2016 series, no prop-money repeat). It is a deliberate top-down ₹ arrangement, which is
  the half of the spec that exists; the four groups and the four labels are the half that
  does not.
- The `s65→s66` hold still works mechanically (the wide fan leaves room for s66's tighter
  crop), but **s66's storyboard note — "tighter crop on one handwritten label" — cannot be
  honoured**, because there is no label in the frame. fin-build needs a different s66 crop
  target, or the creator supplies the made photograph.

**Ask for the creator:** one made photograph — ₹ notes and coins in four groups, top down on
wood, four handwritten bilingual labels in frame. This is the Von Restorff beat at 69%.

## Defects caught at FULL RESOLUTION that the contact sheet hid

Seven images passed the grid and failed the full-res read. This is the whole argument for
rule 1 and it earned its keep again on this cut.

| slot | what the thumbnail hid | action |
|---|---|---|
| `s25` | **`$5,990`** legible on the bar-chart printout — the 51.0% JAPAN hero frame | re-picked (clean blue chart) |
| `s13` | a **US IRS withholding table**: dozens of legible `$`, "Head of Household" | re-picked twice (settled on a defocused numeric page) |
| `s26` | first `USD` in a hotel budget table, then **`21.424$`** in a donut chart | re-picked twice |
| `s40` | **`Blue Diamond ALMOND BREEZE`** carton + gallon jugs — a brand mark on the 🇮🇳 fridge frame | replaced with spice jars |
| `s81` | **`Citibank`** + `DOUBLE RL & Co.` on the second try, a Turkish hospital + number plate on the first, a recognisable woman's face on the third | replaced with pure defocused bokeh |
| `s5` | pine cones, fairy lights, **tree-motif wrapping** — a Christmas flatlay in a video for an Indian audience | replaced with an opened parcel |
| `s90` | **`facebook`** written into the handwritten list, on the RAIL OFF act-now frame | re-picked (a checklist with illegible items) |

Two more caught at grid size that belong on the same list because they are the same class:

- **`s11` was AI-generated.** The "Japanese shopfront" had invented pseudo-kanji, mirrored
  glyphs and a melted sushi photo. Replaced with a real shoji-screen interior.
- **`s19b` was Chinese, not Japanese.** Hanging signs read 咸烧白 / 小河鱼 / 农家豆腐 — a
  Sichuan menu, inside the Japan chapter. Replaced with a machiya facade under sakura.

## Currency verification (the five ₹ slots the storyboard flagged)

All read at full resolution. **All five are the current stone-grey 2016 ₹500 series or
current ₹20/₹1/₹2 coins. No demonetised note anywhere in the cut. No `$` glyph survives in
any image.**

- `s21` ₹500 macro + ₹1 coin — serial `6HP 962971`
- `s51` ₹500 spread — four different serials (`4EW 908495`, `2PN 868289`, `20E 773284`)
- `s56` ₹500 pair + ₹20 coin — two different serials
- `s65` ₹500 fan + ₹20 coin — three different serials
- `s86` current green ₹20 + ₹10 coin stack — serial `1IV 082089`

**One prop-money scare, resolved.** The first `s51` pick (hands counting notes) showed
`1LR 176177` apparently twice. Re-picked out of caution; the replacement proved the rule's
edge case — a ₹500 note carries its serial in **two** corners, so one note legitimately
shows one serial twice. The test is *two serials that differ across two sheets*, not *the
same string appearing twice*. Worth adding to the knowledge note.

## The 12 🇮🇳 act-now frames — honest accounting

Six carry an unambiguous India signal: **s50** (steel thali, dal + roti + papad),
**s51** / **s56** / **s86** (current ₹ notes and coins), **s55** (Indian coins, lion capital
visible), **s92** (hanging racks of street-chai glasses — the closing frame).

Four are domestic-neutral **by the storyboard's own design** (the viewer's own wardrobe,
statement, notebook): s38, s39, s89, s90. Their India comes from the VO and the composition
text, not the photograph.

Two are compromises I am flagging rather than hiding:

- **s40** — the fridge does not exist without US branding in this pool. Shipped as glass
  spice jars (red chilli powder, cumin, peppercorns on rustic wood) — reads as an Indian
  pantry, but line 4.7 says *fridge* and the image says *shelf*.
- **s78** — the scooter is right (the Indian first-big-purchase object, no brand, no face)
  but its heavily defocused background is an **East-Asian street, not India**. Three query
  rounds; every India-specific alternative carried a legible brand (YAMAHA, TIANXIN) or a
  posed model. Object-Indian, background-not.

## Grade override — ONE, as capped

`s36c.jpg` (the truck silhouette cut-in) measures **mean luminance 25.1/255**, the darkest
file in the cut. Under the system `brightness(.62)` it lands at ~15 and reads as a black
rectangle mid-panel-swap.

> **fin-build: give scene 36's `s36c` cut-in an inline `filter: grayscale(.32) brightness(1.35)`.**
> This is the only override in the video. Next darkest are s79 (37.8, chalk on asphalt) and
> s14 (47.4, stamp on dark) — both carry a bright subject that survives the grade untouched.

Brightest are s63 (219.4) and s39 (203.5); the standard grade darkens them correctly, no
action.

## Substitutions worth knowing before the audit

- **`s32b`** — no faded campaign poster exists in either pool (two rounds). Shipped as a
  dark blue-green weathered board: still a wall, still visibly a different shot from s32's
  smooth plaster, so the declared panel swap measures. The *poster* idea is gone.
- **`s70`** — "phone lying face down beside a notebook" has no stock equivalent. Shipped as
  a red ruled notebook + fountain pen, top down. The phone-face-down continuity with s1 is
  broken; the "on paper, not the app" reading survives on the notebook alone.
- **`s28`** — no vintage Tokyo. Shipped as a B&W overhead crowd on cobbles with long
  shadows: era-neutral and location-neutral, no legible text. The *1950s Japan* specificity
  is gone; it reads as "a working city, some other time". A Hanoi street was rejected for
  being visibly contemporary and visibly not Japan.
- **`s13`** — after two rounds of US tax tables and euro flatlays, this hero-number frame
  ships as a **defocused open page with faint figures**. Calmest possible bed for a 37.8%
  hero, zero defect surface, but the "statistics table" keyword is now implied rather than
  shown.
- **`s26`** — legible English labels survive (`Revenue report`, `MARKET RESERCH`). No
  currency, no brand. Accepted as the least-bad of six after two rounds; flagging it because
  an auditor will see the words.
- **`s45`** — the worn shoe carries a small yellow tongue tag reading `...MOUS`. Partial
  word, no logo, not a recognisable mark. Accepted.
- **`s88`** — the temple chozuya includes a bilingual *temizu instruction* placard and a
  grey utility box. Kanji in photographs is explicitly allowed by the storyboard; the
  placard is signage, not a brand. Snapshot-grade but it is the only real basin at a
  different framing from s75/s76.

## Pool notes for the next cut

- **Pixabay answers "printed table of figures" with US tax forms and euro flatlays.** Three
  slots (s13, s15, s53) burned four rounds between them. Name the *object* (`spreadsheet
  with rows of numbers` worked, `financial data` did not) and expect to full-res-read
  anything numeric.
- **Charts carry currency glyphs by default.** Every chart cell that had a value on it had
  a `$` or `USD`. The clean ones were the charts with bare axis numbers only.
- **`build_sheet` silently tiled 1-of-6 and 2-of-6 on five slots** (s6, s9, s18, s27, s36b,
  s60, s72, s80). Counted the cells each time; every one went to a re-query. The tool
  reports `6 candidates` from the metadata regardless, so the count must come from looking.
- **`#6` on the same Pexels query is the cheapest escape** from a spent result set — used it
  for s51, s56, s65, s26, s13 and it returned genuinely new, non-overlapping images every
  time.

## Zero Lotties

The storyboard declares 6 icons / 0 Lotties (§8) with the render-cost reasoning. Nothing
fetched, nothing saved back, `assets/lottie/` untouched.
