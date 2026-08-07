# fin-assets — passive-income-number / hi / chapter 2 / attempt 2

**Scope: s16 only.** s8–s15 and s17–s19 were verified and locked on attempt 1 and were not
touched (no re-fetch, no re-pick, no manifest edit beyond s16). Chapter 1 untouched.

## The defect, restated

The rejected s16 (`squared graph paper grid texture close up`, Beyzanur K., Pexels 28380283)
was a scanner-flat, axis-aligned, edge-to-edge repeating grid: no perspective, no object
boundary, no shadow, no falloff, no depth of field — a photograph of a *pattern*, not of a
*thing*. Confirmed against the composed frame `snapshots/qa2/b1/frame-02-at-53.95s.png`, where
it reads as a CSS `repeating-linear-gradient` behind the type rather than as film.

**Luma cannot catch this and was not used as the test.** Graded it measured YAVG 58 / spread 19;
s10 (calendar) measures 61.7 / 17 and reads as film. `pipeline_check`'s own comment already says
so ("the opposite failure … is real but luma does not predict it … That one still needs eyes").
The test applied here was: *is there an object, with an edge, in a light*.

## Sheet 1 — the pick

`old ledger book with ruled columns open on a wooden desk@pexels` — **6 of 6 cells** (counted).

Cell luma, measured on the sheet before any full-size fetch (`crop=512:288:x:y,signalstats`):

| cell | YLOW/YAVG/YHIGH | verdict |
|---|---|---|
| **1** | 17 / 159.9 / 223 | **ACCEPT** — open ledger, raking perspective, red+blue ruled columns, page edge and shadowed fold running through the upper-left, real DOF falloff into the far page |
| 2 | 17 / 76.9 / 181 | reject — open book on a rubble floor with a rusty reel; derelict register, no grid |
| 3 | 8 / 68.2 / 151 | reject — printed prose book, legible Vietnamese text; not a ledger, foreign-language type in frame |
| 4 | 17 / 109.0 / 242 | reject — desk of books + mug + glasses; busy, no grid, reads "reading" not "the working" |
| 5 | 17 / 131.6 / 205 | reject — Italian ledger headed **ENTRATA 1813**; asserts a wrong era and place outright |
| 6 | 16 / 86.2 / 214 | reject — antique quill desk, wallpaper, museum register; no grid, busy |

(YLOW ≈ 17 on every cell is the sheet's black padding, not the photograph. Cell 1's interior
crop measures 141 / 189 / 225.)

## Sheet 2 — the place check, run on purpose

This is a Hindi cut about Indian money and cell 1's hand is Western copperplate, so I spent one
extra search testing whether an India-placed ledger exists:
`old account book with handwritten hindi entries on a table@pexels` — **6 of 6 cells**.

- **cell 2 is byte-for-byte the same photograph as sheet 1 cell 1** — the pool has exactly one
  good answer to this concept and both phrasings find it.
- cells 1 + 3 — the same derelict floor ledger as sheet 1 cell 2, twice. Reject.
- cell 4 — handwritten diary with a dried sprig. Calm, real object, good light — but prose on
  plain paper: **no columns, no figures.** The line is arithmetic; sound-off test 3 (is the
  thing the line NAMES in frame) fails. Reject.
- cell 5 — journal by candlelight with lace. Same failure, plus a nostalgia register the chapter
  does not carry. Reject.
- cell 6 — **US dollar bills, a calculator and a notepad.** Hard reject: wrong currency on a ₹
  video, from a query that never mentioned dollars. This is the rule-1 trap arriving unbidden,
  and it is the reason the neutral ledger is the right answer rather than a compromise.

**No Indian ledger exists in either pool.** Per the standing rule, a currency-NEUTRAL object
beats a wrong-currency one: the promoted frame carries no currency symbol, no institution, no
letterhead and no date, so it asserts no place or era — unlike cell 5 (1813 Italy) or cell 6
(USD), which do.

## What shipped

`assets-ch2/final/s16.jpg` ← sheet 1 cell 1
· https://www.pexels.com/photo/close-up-photo-of-ledger-s-list-164686/ · by Pixabay · Pexels License

| check | value |
|---|---|
| resolution | **1880 × 1250** (floor 1732 — Pexels `dpr=2&w=940`) |
| **source YHIGH** | **225** (floor 110) · YAVG 186.4 · YLOW 138 |
| md5 | `8f513cf537f151036c275aa81d21b605` — unique across all 20 images in studio |
| grade | untouched: `grayscale(.32) brightness(.62) contrast(1.05)`, **no per-scene override** |
| graded simulation | YAVG 68, spread 21 (56–77) at 1920×1080 cover + the scrim's centre pull — inside the chapter's 58–62 band |
| full-res read | done. No currency symbol, no brand mark, no face, no screen, no date, no legible institution. Handwritten surnames in Latin cursive and bare figures (4464, 8525, 2000) with no unit |

## Sound-off test, line 2.9

The line is «3.0% of ₹10,00,000 = ₹30,000 a year = ₹2,500 a month» — a division being done.

1. Covering the words: a book of figures kept in ruled columns. *The working.* Yes.
2. Argues? No. The page states no rate, no total and no currency, so it cannot contradict the
   drawn 3.0% sliver or the ₹ figures. The storyboard's own brief for this slot is "a division
   on a ledger page states the sum; it cannot state the proportion" — which is exactly the
   division of labour with the `three-percent-sliver` art.
3. Named thing in frame: the sum, as columns of figures. Yes.
4. Reused in this chapter? No — see the twin check below.
5. Place/era/currency: neutral on all three, deliberately.

### Twin check against the locked images

- **vs s13/s14 (14 s earlier)** — s13 is a *blank* white spiral pad with a red pen on dark brown
  wood, cool and empty. s16 is a *filled* warm cream bound ledger, colour-ruled, no wood, no pen,
  a raking macro instead of a three-quarter still. Different object, colour, scale and angle —
  and the pairing now reads as a progression (the number about to be set down → the sum done),
  which the chapter did not have before.
- **vs s18 (12 s later, s17 between)** — both are paper. s18 is pale beige *closed* bundles
  tied with string, straight-on, fine vertical edges; s16 is an *open* page in raking
  perspective with red/blue rules and blue ink, and roughly 60 % of its frame is covered by the
  art plate and 76 px type. Legible as distinct, but this is now the chapter's closest pair
  alongside s18/s19 — **flagged for fin-editor** in case the draft reads as one paper texture
  across s16–s19.

## Verification

- `python3 tools/pipeline_check.py check assets --slug passive-income-number --cut hi --chapter 2`
  → **PASS assets-hi** (with `--chapter 2`; without it the check reads `-hi/assets/img/`, which
  holds no `s*.jpg` at all, and its licence assertion would reach nothing).
- CREDITS.txt: 13 rows for 13 slots, the s16 row **re-keyed** to the new source in the same move
  (the stale Beyzanur K. row is gone — 0 matches for photo id 28380283).
- `s16.jpg.src` ≡ chapter `manifest.json` ≡ cut-level `assets/img/manifest.json` — all three now
  carry the query that actually found the file, so the second sheet's throwaway query cannot
  survive into the archive as false provenance.
- No lottie work: the storyboard asks for none in chapter 2. `assets/lottie/` untouched.

## Counts

| | |
|---|---|
| slots touched | 1 (s16) |
| Pexels searches | 2 (12 preview downloads, 1 full-res download) |
| Pixabay searches | 0 · Commons | 0 |
| cells viewed | 12 (6 + 6, both sheets full) |
| accepted | 1 |
| rejected | 10 (+1 duplicate of the accepted frame) |
| dropped | nothing — a background was replaced, never dropped |

## For the next run

`--candidates` **overwrites `_cand/<slot>.json`**, so a second exploratory sheet on the same slot
destroys the free re-pick for the first one. It cost nothing here because the winner was already
promoted to disk with its CREDITS row and `.src` written, so backing out was a one-line manifest
edit — but the ordering (promote the leader *before* testing an alternative) is what made the
extra search safe, and is worth doing deliberately.
