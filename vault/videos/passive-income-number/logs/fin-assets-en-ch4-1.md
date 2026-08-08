---
summary: en ch4 (s40-s52, lines 4.1-4.13) sourced from scratch into a new studio/videos/passive-income-number-en-ch4 project. 13 accepted (12 fetched + the s42 derived crop), ~238 candidate cells rejected across 45 contact sheets, 0 dropped. NINE images were killed only at FULL RESOLUTION (TEXAS INSTRUMENTS TI-606 + STABILO BOSS + a barcode, a ZEPPELIN barrier lamp, PRODUCT OF TAIWAN + lbs/kg on a box, Cyrillic price cards in roubles, a cast `3Kg` on a balance beam, GROUNDS CAFE, VIRGIL ABLOH, FRAGILE stickers, an Apple wordmark) and the cross-project md5 sweep caught TWO MORE that had passed both reads — one of them the hi cut's own LIVE s23. Payoff named as s41 and scored against all four clauses: sound-off PASS, median #3 of 13, p10 #2, step-in +8.5 — but clause 4 DEPENDS on one measured bgpos knob handed to fin-build; without it the step is -4.5 and the clause fails. Chapter floor is s44 (median 11.2), line 4.5, a 5.71s transitional warning that carries no figure, so the invariant's first clause holds.
updated: 2026-08-09
source: fin-assets attempt 1, chapter 4, en cut. Composed-frame method re-validated against fin-assets-en-ch3-3's published table on 11 untouched ch3 files before it was trusted (10 of 11 within 0.5 pt; the one outlier is explained by build.mjs's `bgpos: center bottom` on s24).
stage: fin-assets, cut en, chapter 4, attempt 1
---

# fin-assets — passive-income-number / en / chapter 4 / attempt 1

**Accepted 13 · rejected ~238 cells over 45 contact sheets · dropped 0.**

`python3 tools/pipeline_check.py check assets --slug passive-income-number --cut en --chapter 4`
→ **PASS assets-en**. Negative control without `--chapter`: FAILS (it reads the whole-cut
manifest, which names s1-s81 against an empty dir), so the flag is doing real work.

Project created at `studio/videos/passive-income-number-en-ch4/` following -en-ch2/-en-ch3:
`assets-ch4/final/` holds every new file; `assets/` carries the five symlinks
(`blockframe.css`, `chapter-design.css`, `fonts`, `img`, `voice` → the cut). `assets/js/`
and `assets/audio.json` are fin-build's to create via `tools/chapter_project.py`.

---

## 0. The instrument was validated before it was trusted

Composed = cover-crop the source to 16:9 at the scene's `background-position`, take the
central 86.2% that `inset:-8%` actually shows, apply `brightness(.62)` then
`contrast(1.05)` (`grayscale(.32)` is chroma-only and does not move a neutral's luma),
then Rec.601 luma percentiles. Reproduced against fin-assets-en-ch3-3's published table on
eleven untouched ch3 files:

| ch3 file | published | mine | Δ |
|---|---|---|---|
| s25 | 93.9 | 93.9 | 0.0 |
| s26 | 92.6 | 92.6 | 0.0 |
| s27 | 97.0 | 97.1 | +0.1 |
| s28 | 95.8 | 95.8 | 0.0 |
| s30 | 62.1 | 62.6 | +0.5 |
| s31 | 70.6 | 70.4 | −0.2 |
| s34 | 128.3 | 128.4 | +0.1 |
| s35 | 137.8 | 137.5 | −0.3 |
| s37 | 20.5 | 20.3 | −0.2 |
| s39 | 102.3 | 102.3 | 0.0 |
| **s24** | **36.6** | 26.8 at `center` — **36.6 at `center bottom`** | **0.0 once the real bgpos is used** |

Ten of eleven to a tenth of a point, and the eleventh reproduces exactly once
`build.mjs`'s own `bgpos: "center bottom"` is applied. **These are still PREDICTIONS.**
Everything below is source-side; only the encode settles it, and any margin under ~3
points is flagged unsafe.

---

## 1. The chapter, measured (all at `bgpos: center` unless the row says otherwise)

| scene | line | file | **median** | **p10** | **p90−p50** | src px | source YHIGH | sound-off: the object a viewer names with the type covered |
|---|---|---|---|---|---|---|---|---|
| s40 | 4.1 | s40.jpg | 84.1 (→ **71.1** at `center 35%`) | 2.7 | 42.3 | 1880×1253 | 203 | a fan of **twenty-dollar bills**, macro, on black |
| s41 | 4.2 | s41.jpg | **79.6** | **53.5** | 52.7 | 1880×1253 | 202 | **two bank-vault doors** — a gearwork door and a steel door with a spoked handwheel — set in a brick wall |
| s42 | 4.3 | s42.jpg ⟵ crop of s41 | 85.4 | 57.4 | 51.4 | 1600×900 | 214 | the same vault doors, the **handwheel/dial** ~1.18× larger and pushed to centre-right |
| s43 | 4.4 | s43.jpg | 73.0 | 8.6 | 39.7 | 1880×1253 | 182 | **hands sharpening a pencil** with a blade over a blank sheet, tin of pencils |
| s44 | 4.5 | s44.jpg | **11.2** | 0.0 | 71.6 | 1880×1253 | 144 | a **rain-slick crosswalk at night**, red/amber/blue light reflected in the water |
| s45 | 4.6 | s45.jpg | 102.3 | 28.1 | 28.6 | 1733×1300 | 209 | a **hand holding a phone**, screen off and black |
| s46 | 4.7 | s46.jpg | 72.4 | 15.1 | 50.1 | 1880×1253 | 198 | a **brass tap, handle turned open, water running out** of a cast-iron standpipe in daylight |
| s47 | 4.8 | s47.jpg | 67.2 | 30.7 | 44.9 | 1880×1251 | 180 | an **aged brass gate valve on copper pipework**, mouth open and **dry**, second cut pipe also dry |
| s48 | 4.9 | s48.jpg | 34.6 | 3.4 | 85.9 | 1880×1253 | 180 | a **brass scale pan on chains**, loaded, with the beam counterweight opposite |
| s49 | 4.10 | s49.jpg | 50.9 | 26.8 | 78.1 | 1880×1251 | 212 | a **weathered board wall with peeling paint**, raking light across it |
| s50 | 4.11 | s50.jpg | 73.0 | 9.2 | 59.2 | 1880×1253 | 214 | a **deep stack of folded newspapers**, edge-on macro |
| s51 | 4.12 | s51.jpg | 47.7 (→ **65.2** at `center bottom`) | 4.0 (→ 7.3) | 67.1 (→ 48.8) | 2939×2392 | 212 | a **1931 breadline** — a long queue of men in overcoats and flat caps on a wet Chicago pavement |
| s52 | 4.13 | s52.jpg | 53.5 | 4.7 | 45.6 | 1880×1251 | 163 | **smashed pottery shards** scattered on dry earth, hard sun |

Every file ≥1600 px (min 1600, s42 by construction). Every source YHIGH ≥ 110 against the
gate (min 144, s44). Zero URL collisions, zero `by Pixabay` credit lines on a Pexels
result — the cross-pool tell was checked on all 13.

---

## 2. THE PAYOFF FRAME — **s41 (4.2), PEAK 1, `$1,500,000`, `hero`, ground `#0f3a20`**

It is the chapter's most substantive beat by construction: the rung-four corpus, the
storyboard's own PEAK 1, the only scene in ch4 whose formula completes across an unbroken
shot into s42. Scored against all four clauses of `payoff_clause_and_metric_2026-08-08`,
**with the two bgpos recommendations of §3 applied**:

| clause | result | margin |
|---|---|---|
| **1. sound-off gate (binary, runs first)** | **PASS** — type covered, the frame is two bank-vault doors: locking bars, rivets, a spoked handwheel and a combination dial, in a brick wall. A viewer names "a bank vault" with no help at all. | n/a |
| **2. top quartile on median** = top `ceil(13/4)` = **top 4** | **PASS — #3 of 13** (s45 102.3, s42 85.4, **s41 79.6**, s43/s50 73.0) | **+6.6** over #4 — safe |
| **3. #1 or #2 on p10** | **PASS — #2 of 13** (s42 57.4, **s41 53.5**, s47 30.7) | **+22.8** over #3 — very safe. ⚠ #1 is s42, which is s41's own continuation frame; on the fetched-photograph field s41 is #1. |
| **4. non-negative median step-in** | **PASS — +8.5** (s40 71.1 → s41 79.6) | ⚠ **DEPENDS ON ONE BUILD KNOB — see §3.1.** At `bgpos: center` s40 measures 84.1 and the step is **−4.5, i.e. the clause FAILS.** |

⚠ **Clause 4 is the one thing in this chapter that is not settled by the photograph.**
I tried to settle it with the photograph first: four sheets of "twenty dollar bills on a
dark table" returned nothing darker that was also brand-free and prop-free, and one of the
cells was the promoted file again. The knob is measured, not guessed, and it is the same
channel ch3 used (`build.mjs` already carries three `bgpos` lines annotated as fin-assets
recommendations). **If fin-build does not apply it, the payoff clause fails and this must
come back to assets, not to build.**

### The invariant's FIRST clause — which frame sits on the floor

**The chapter's luminance floor is s44: median 11.2, p10 0.0, line 4.5.** Line 4.5 is
*"Now the warning, and it is the reason most people never reach any of these rungs"* — a
`stmt`-only announcement with **no figure, no mechanism and no citation**, on the
**second-shortest scene in the chapter** (5.711 s). Under the ch3 reading of the invariant
(*"relocating the floor is only a defect if the beat is substantive"*) this is compliant,
and it is deliberate: a rain-slick road at night is what the storyboard asked for on this
beat.

The three frames carrying figures are all well clear of it: `$5,000/MONTH` s40 median #7,
`$1,500,000` s41 #3 / s42 #2, `13.84%` s50 #4=. **No repeat of the s21 / s31 shape.**
Second- and third-darkest are s48 (34.6, the yield-mechanism beat) and s51 (47.7 → 65.2
with the recommended crop); s48 at #12 is the one I would put in front of the gate — the
argument for it is that 4.9 is a definition beat whose mechanism is stated in type, and
the honest counter-argument is that it is still a mechanism. It is declared, not argued
away.

Chapter spread, duration-weighted across the run: floor 11.2 → ceiling 102.3, median band
~50–85. Not near-zero anywhere; the flattest frame is s45 at 28.6 spread and it holds a
phone, a hand and foliage, so it is not a blank field.

---

## 3. What fin-build must do — two measured knobs and one dependency

### 3.1 `bgpos: "center 35%"` on **s40** — REQUIRED, the payoff clause rides on it

| bgpos | median | p10 | p90−p50 | what the frame holds |
|---|---|---|---|---|
| `center 0%` | 21.6 | 2.1 | 104.2 | almost all black — would make a figure frame the floor |
| **`center 35%`** | **71.1** | **2.1** | **55.3** | the fanned notes in the lower right, black negative space upper left |
| `center` (default) | 84.1 | 2.7 | 42.3 | notes fill the frame — **step-in −4.5, clause 4 fails** |
| `center 100%` | 102.3 | 2.7 | 24.1 | notes only |

It is also the better layout: s40 is `arch B`, `ctr Y`, carrying `$5,000 A MONTH` at
`.huge` plus a `foot` — `center 35%` puts the black upper-left under the type stack and
the money under nothing.

### 3.2 `bgpos: "center bottom"` on **s51** — recommended on two grounds at once

Measured 47.7 → **65.2** median, p10 4.0 → 7.3, spread 67.1 → 48.8. **And it crops the
photograph's two largest text blocks out of frame**: the painted banner
`FREE ⟨SO⟩UP COFFEE & DOUGHNUTS FOR THE UNEMPLOYED` and the `ALBERT HORAN / BAILIFF`
sign both sit above the crop line. What survives is the queue, the wet pavement, a small
`FREE SOUP &` on the shop glass and `PARKING 25` clipped at the top edge. Rendered the
crop and looked at it, not only measured it — the frame still reads unmistakably as a
Depression breadline.

### 3.3 s42 is a DERIVED CROP and it has a parent

`ffmpeg crop=1600:900:280:186` on `s41.jpg`. Recorded in `s42.jpg.src` and in
`manifest.json`, and its CREDITS row is s41's row **re-keyed onto s42.jpg in the same
move** (same page URL, same author, annotated as a derived crop). ⚠ **If s41 is ever
re-fetched, s42 must be re-derived with the same rect and its credit row re-keyed again**
— an orphaned crop passes every check and shows an unrelated photograph.

The crop is sized for §9b: s41 `plateKen` 1.00→1.08 and s42 1.08→1.16 read as one
continuous push, and s42's composed median (85.4) sits **+5.8** above s41's, so the hold
does not visibly brighten mid-shot.

---

## 4. NINE full-resolution kills — the contact sheet was a shortlist, never a verdict

Every one of these passed its grid cell and died only when the promoted file was read at
full size:

| slot | what the sheet showed | what full resolution showed |
|---|---|---|
| s43 | "a plain grey pocket calculator and pencils on painted wood" | **`TEXAS INSTRUMENTS TI-606`** on the calculator, **`STABILO BOSS`** and an EAN barcode on the highlighter, **`MARX & PARTNER`** on the pen — three brand marks in one frame |
| s43 (2nd) | "a black calculator on a wooden desk" | **`TEXAS INSTRUMENTS TI-608`** plus a lit display reading digits, against `display illegible` |
| s44 | "a big amber hazard lamp against city bokeh" | **`ZEPPELIN`** on the barrier body, bottom right and inside the composed crop — a brand mark **and** a European barrier lamp in a US-market cut |
| s48 | "an antique two-pan brass balance on a shelf" | **`3Kg`** cast into the beam dead centre, ~52 px wide at 1920 output — a metric capacity mark on an American frame |
| s49 | "a discarded box by a railing" | **`FRAGILE! HANDLE WITH CARE`**, **`PRODUCT OF TAIWAN`**, **`…04 LBS x 4 BTLS / 8.2 KG x 4 BTLS`** |
| s49 (2nd) | "antique glass bottles on a shelf" | **Cyrillic price cards in roubles** — `БУТЫЛКА СТОЛОВАЯ … руб`, `ЧЕРНИЛЬНИЦА … руб` |
| s45 | "a hand holding a phone" (two cells) | an **Apple wordmark + `iPhone`** on the back |
| s52 | "a sale tag" (six cells, two sheets) | studio mock-ups with legible **`SALE`**, **`−50 %`**, **`50 % off`** — a stray percentage next to the chapter's own 13.84% |
| s49 (3rd) | "a box with a peeling label" | **USPS/EMS waybills** and `VIRGIL ABLOH` printed on the carton |

Two more were caught by **crop-zoom at 3–4×** rather than by the plain read and were
**kept**: s41/s42 carry a small brass maker's plaque on the left door and s47 carries a
stamped marking on the copper riser — both resolve to illegible smudges at 4× and are
~1–1.5% of frame width. Declared, not hidden.

### The cross-project md5 sweep caught TWO the eyes did not

172 jpg/png hashed across all of `studio/videos` (`_cand/`, `node_modules/`, `snapshots/`
excluded).

- ⚠ **s43 (the bright soroban abacus) came back byte-identical to
  `passive-income-number-hi-ch3/assets-ch3/final/s23.jpg`** — the sibling cut's **live**
  asset, same Pexels URL. It had passed its contact sheet and its full-resolution read.
  **Replaced.** This is the sibling-chapter sweep earning its place for the fourth time on
  this run.
- ⚠ **s48 collides with `passive-income-number-hi-ch1/assets-ch1/style-a/s7.jpg`** and is
  **KEPT — declared, for the gate to rule.** Evidence: hi ch1 is `status: locked` and its
  build note records that it was *"rebuilt from scratch on style E at attempt 1, retiring
  the style-A composition"*; `style-a/` sits beside `retired-attempt6/` and
  `killed-attempt7/`; hi ch1's **live** `final/s7.jpg` is a different photograph (brick
  stairs, Ravi Kant). So no viewer can see this photograph twice. The alternative was five
  sheets' worth of two-pan balances of which exactly two were landscape enough to reach
  1600 px: the `3Kg` one (an on-screen defect) and a cottonbro frame at composed median
  **9.2** (which would have taken the chapter floor off a transitional beat and put it on
  the yield-mechanism beat). **An identical hash in a retired directory is a smaller defect
  than legible metric type on a rendered frame** — but it is a deviation from "zero
  duplicate md5s across ALL of studio/" and it is the gate's call, not mine.

### The contact sheet is lossy, and the burned label is the truth

**Twelve of the 45 sheets came back short** (1/6, 2/6, 3/6, 4/6 or 5/6) with no warning.
Confirmed the mechanism rather than assuming it: a short sheet tiles only a **trailing**
subset, and the **number burned into the cell is the true candidate index** — the
`bread line@commons` sheet rendered a single cell labelled **6**, and `_cand/s51.json`
held six candidates. Grid position ≠ candidate number on any short sheet. Every pick below
was made against the burned label and cross-read from `_cand/<slot>.json`, which always
holds all N. Wikimedia rate-limiting is the cause on every Commons sheet.

---

## 5. THE TANK FAMILY — the inherited brief, and how it was split

Read `passive-income-number-en-ch2/assets-ch2/final/s10.jpg` at full resolution first, as
instructed. It is **seven aged brass tap valves with turned brass lever handles bolted
along a horizontal steel manifold** above a long copper-brown trough, white tiled wall,
raking daylight through a window. **No vessel in frame, and — the ch2 editor is right —
every lever sits in the same near-horizontal position, so nothing in s10 reads as open or
shut.**

The sharpened brief was *"the lever visible at a different angle PLUS flow"*. **No single
cell out of 24 tank/tap/valve candidates across four sheets carried both.** So the pair
splits the brief and each half is unambiguous:

- **s46 (4.7, "12% is a wider tap")** — a cast-iron standpipe with an **aged brass tap
  whose ornate handle is visibly turned off-axis**, and a **strong stream of water running
  out**, in hard daylight. Flow ✔, handle-in-a-readable-position ✔, brass ✔, daylight ✔.
- **s47 (4.8, "how long a tank lasts")** — an **aged brass gate valve on rusted copper
  pipework** against a grey wall in daylight, **mouth open and completely dry**, with a
  second cut pipe beside it also dry. It is the closer material match to s10 (brass valve
  body + industrial metal pipework) and it states the second half of the beat: *it ran
  out*.

Together the pair says wide-open-and-flowing → open-and-empty, which is exactly the
storyboard's *"tap position alone says the beat"*. **s57 (ch5) still owes the third
statement** — the storyboard's "barely cracked, a thin stream into a tin cup" — and it
now also owes the only thing this pair could not buy: **one frame with a brass LEVER
handle in a plainly different position.** Search note for whoever takes s57: the phrase
that produced a readable lever was `rusty metal water tap thin trickle of water running
out hard sunlight concrete wall@pexels`, cell 5 (Romualdo Segura, a green lever on a
copper riser with a hard cast shadow) — **it was rejected here on resolution only**
(2621×2190 → Pexels `large2x` returns **1555 px**, under the 1600 bar). Any near-square
Pexels source is capped at h=1300 and comes back under 1600 wide; check the aspect before
picking.

---

## 6. Declared deviations from the storyboard, one per line that moved

Each is a case where the declared subject does not exist in either pool without a defect
attached. **Nothing was dropped; every scene has its background.**

1. **s43** — script cue "a pocket calculator, display illegible, a pencil beside it".
   Shipped: **hands sharpening a pencil over a blank sheet.** Three calculator sheets, 18
   cells: every calculator in both pools carries its maker's name on the bezel, and the
   two that did not were a numeric keypad at composed median **0.0** and a children's toy
   with `1…10` printed on it. ⚠ **This adds a HANDS frame** — §10 enumerates s18, s33,
   s45, s53, s58 as the only frames with a hand. No face, no wrist brand, hands only, so
   the *rule* holds and only the enumeration moves. Flagged for the editor.
2. **s44** — "a rain-slick road at night with a single amber hazard light". Shipped: the
   rain-slick road at night, **without the lamp**. The only two amber-lamp cells in twelve
   were the `ZEPPELIN` barrier (§4) and a fog-and-cobbles street that reads European. The
   frame keeps a strong amber reflection in the centre of the water.
3. **s45** — override says "screen turned away, only the glow on the fingers". Shipped: a
   **black, switched-off screen facing camera**, which is the ch1 amendment of 2026-08-08
   applied identically (s1/s3/s4/s79). Twelve cells of "screen turned away" were an Apple
   wordmark on the back, a lit screen, or a face; and a dark-room glow frame cannot clear
   `YHIGH ≥ 110` by construction.
4. **s48** — "a two-pan balance where the right pan has dropped, one pan empty". Shipped:
   **one loaded brass pan on chains with the beam counterweight opposite**, in a
   herbalist's shop. See §4 and the md5 note. The frame still shows the machine that
   compares two quantities, which is what "payout DIVIDED BY price" needs; it does not
   assert equality.
5. **s49** — "a price sticker peeled half off a plain box, the box itself dented".
   Shipped: **a weathered board wall with peeling paint under raking light.** Six sheets:
   every box cell carried legible `FRAGILE` / `PRODUCT OF TAIWAN` / a courier waybill / a
   brand. s49 is the chapter's one `art-forward` frame (`yield-fraction`), and §10 routes
   art-forward frames to the calmest subject, so a quiet surface with real edges and real
   falloff is the correct answer rather than the fallback. ⚠ An earlier pick here was
   **cracked dry earth**, and it was **rejected for colliding with s52** (shards on dry
   earth, three scenes later) under sound-off rule 4 — two brown top-down dry-ground
   textures in one chapter is the "one picture per point" defect even though each is
   defensible alone.
6. **s50** — "a 1930s US newspaper financial page, archival grain, headline out of
   focus". Shipped: **a deep stack of modern newsprint, edge-on, with no legible word
   anywhere.** `@commons` "1932 newspaper stock market" returned **NO RESULTS**; "antique
   stock ticker tape machine" returned five typewriters and an `Underwood` wordmark; every
   archival page in the Pexels pool carried a legible English or foreign headline, which
   is the fabricated-document risk §10 names for this exact beat. **Era-neutral, not
   era-wrong** — the frame says "the record, going back", it does not say a wrong decade.
7. **s51** — "faces indistinct". Shipped: **NARA public-domain, unemployed men queued at
   the Chicago soup kitchen, February 1931** — the correct place, decade and market, and
   the storyboard's declared exception. ⚠ **The faces in the front row are distinct**, and
   two of the archival signs are legible at full size (`FREE SOUP …`, `PARKING 25`). The
   `center bottom` crop of §3.2 removes the two big ones. Licence is not the issue (public
   domain, US government); this is a design ruling for the editor.
8. **s52** — "a discount tag hanging off a cracked item on a shelf". Shipped: **smashed
   pottery shards on dry earth, colour, hard sun.** Two sale-tag sheets returned twelve
   studio mock-ups with legible `SALE` / `−50 %`. An earlier pick, a smashed white bowl on
   concrete, was rejected for being effectively monochrome directly after the archival
   B&W s51 — two greyscale frames in a row dilutes the one archival cue the chapter has.

---

## 7. Standing rules, each actually run

- **≥1600 px** — all 13, min 1600 (s42 by construction). Two candidates were rejected on
  this alone (both near-square Pexels sources returning 1555/1583 px).
- **Source `YHIGH ≥ 110`** — all 13, min 144 (s44). Measured per cell on the sheet before
  any full-size fetch, which killed ~15 cells pre-download.
- **md5 across all of `studio/`, sibling chapters swept** — 172 files; one live-asset
  collision caught and replaced (s43), one retired-directory collision kept and declared
  (s48). §4.
- **Source-URL collisions** — one, the same s48 row, in the retired `style-a/CREDITS.txt`.
  No other en-ch4 URL appears anywhere else on either cut.
- **Cross-pool "by Pixabay" tell** — zero on all 13 credit rows.
- **US market** — no non-US currency, signage, plate, plug or vehicle in any accepted
  frame. `3Kg`, roubles, `PRODUCT OF TAIWAN` and a German barrier lamp were all rejected
  on this ground. s48 is a herbalist's shop with no signage or language in frame; s46's
  standpipe is generic Western with no legible mark. Both declared.
- **Currency** — s40 is genuine current-series US $20 notes (correct intaglio, security
  thread ghost, the Jackson watermark visible in the second note). **Only one serial is in
  frame and it is partial (`JF 1822…`, clipped by the frame edge), so there is no
  two-notes-one-serial to check and no legible serial to be a liability.** One cell was
  rejected for exactly that defect: two visibly separate $20s both reading
  **`MB77999921K`** — reproduction/prop money, and unusually it was legible at contact-sheet
  size.
- **Attribution** — `CREDITS.txt` has **13 rows, 13 distinct keys**, exactly matching the
  13 manifest keys and the 13 files on disk. The one hand-placed file (s42) got its credit
  row re-keyed from s41 in the same move as the crop, and its manifest entry in the same
  move as that.
- **`.src` for every file**, all 13 byte-matching their manifest query.

---

## 8. Handoff

- **ARTIFACTS** — `studio/videos/passive-income-number-en-ch4/assets-ch4/final/` :
  `s40.jpg … s52.jpg` (13), 13 `.src`, `manifest.json`, `CREDITS.txt`.
  Throwaway sheets in `assets-ch4/final/_cand/` (not in the manifest, not shipped).
- **fin-build must apply** `bgpos: "center 35%"` on s40 (payoff clause 4 rides on it) and
  should apply `bgpos: "center bottom"` on s51 (§3.2).
- **For the editor/CEO gate**: the s48 md5 deviation (§4), the s48 floor-adjacency (§2),
  s51's distinct faces and archival signage (§6.7), s43's extra hands frame (§6.1), and
  the split tank brief with s57's outstanding third statement (§5).
