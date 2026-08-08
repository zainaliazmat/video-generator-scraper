---
summary: Attempt 7 re-sourced one slot only — s91.jpg (8.7, the .cta SUBSCRIBE frame) replaced with an 1880px Pexels closing-desk still; library stays 93 images, all checks 1:1.
updated: 2026-08-01
source: fin-assets stage run, japanese-money-methods-en, attempt 7
---

# fin-assets — en cut, attempt 7 (single-slot: s91.jpg)

**Scope:** one file. Orchestrator ruling on storyboard-en §9a — of the five 1280px
slots flagged, four ship as-is; `s91.jpg` (scene 8.7, `.cta` SUBSCRIBE, the last full
frame) is re-sourced. Nothing else in the library was touched.

## Result

| | |
|---|---|
| accepted | 1 (`s91.jpg`) |
| rejected | 11 cells across 2 contact sheets |
| dropped | none |
| library | 93 images, unchanged count |

**Old:** Pixabay `notebook-book-leather-leather-cover-420011` by qiye — **1280×853**
(the Pixabay key has no full-HD access, so that pool caps at 1280px; at
blockframe-9's full-bleed `inset:-8%` this was drawn ~1.63×).

**New:** Pexels `black-framed-eyeglasses-163142` (author credited as *Pixabay* on
Pexels, Pexels License) — **1880×1188** from `large2x`, source 3008×1900.
A closed dark-cloth notebook on a wooden desk with reading glasses resting on it,
low side light.

- **width 1880px ✓** (requirement ≥1880) — no upscale at inset −8%.
- **mean luminance 91.9 ✓** (requirement ≤140, measured on the promoted file).
  Comfortably dark for light `.cta` type; no `filter:` override needed, so the
  cut's one luminance override stays unspent.
- **md5 dedupe:** `md5sum studio/videos/*/assets/img/*.jpg | sort | uniq -w32 -D`
  returns nothing — zero collisions across **both** cuts (186 images).
- **Read at FULL RESOLUTION before landing** ✓ (the sheet thumbnail is not the check).

## What was rejected, and why

Sheet A — `closed leather notebook on a wooden desk@pexels` (6/6 cells received):

| cell | verdict |
|---|---|
| 1 | brightest cell on the sheet (white wall behind), embossed cover mark — too light for `.cta` type |
| 2 | **readable brand marks**: `FIELD NOTES` and `BERLIN` printed on the cards |
| 3 | **phone in frame** on the desk + hands/arms — the standing screen rejection |
| 4 | camera body, lens and a second light slab (phone/notebook) — three competing focal points |
| 5 | best of sheet A: tan leather notebook, coffee cup, knit fabric — kept as the fallback, not picked (cup is a second bright focal point beside a CTA block) |
| 6 | glaring gold cover on white — off-palette and the brightest thing in frame |

Sheet B — `closed notebook on a dark wooden desk low light@pexels` (6/6 cells):

| cell | verdict |
|---|---|
| 1 | open notebook, blown-out pages — bright and busy |
| 2 | open planner on a window sill, high-key window behind |
| 3 | **laptop with a visible logo** on the lid |
| 4 | **PICKED** |
| 5 | **laptop** (port close-up) |
| 6 | **laptop** + open notebook |

## Full-resolution notes on the accepted file

- No screen of any kind. No money, no currency symbol, no ₹, no Devanagari, no
  India-specific institution. No person, no face, no hands. No prop money, no
  seasonal prop, no signage (so no AI-signage risk).
- **The one text in frame** is the eyewear spec engraved on the temple arm
  (`50…`, `26…477(32-11)-09`) — a frame-size/model code, **no brand name and no
  logo**. It is faint, off-centre and small; at inset −8% it is sub-pixel noise.
  Recorded here so a later reviewer does not re-litigate it: a model number is
  not the brand mark the standing rejection targets.
- Reads as a *closing* frame against its neighbours: s89 is a bright wood-top
  desk flatlay and s90 is a white handwritten page, so s91 lands dark — the CTA
  arrives on the darkest frame of the closing run, which is what the `.cta`
  block wants.
- Subject still answers the storyboard keyword ("closed notebook on a desk").
  Glasses set down on a shut book reads as *work finished*, which is the beat.

## Files updated

- `studio/videos/japanese-money-methods-en/assets/img/s91.jpg` (1880×1188)
- `…/s91.jpg.src` → `closed notebook on a dark wooden desk low light@pexels`
- `…/manifest.json` — s91 query updated to match `.src` exactly (so a later plain
  `--manifest` run skips rather than clobbers). 93 entries, 1:1 with disk.
- `…/CREDITS.txt` — **93 lines, 1:1 with the 93 jpgs, no duplicate slot**. The
  replace-in-place `write_credit` did its job; verified programmatically, not by eye.

## One process note for the next run

`--candidates` has **no skip rule** — it re-searches and re-downloads previews for
*every* slot in the manifest, so pointing it at a 93-slot manifest to re-do one
slot costs 93 searches + ~560 preview downloads and several minutes. For a
single-slot re-source, run `--candidates` against a **one-slot manifest in a scratch
dir**, then write that sheet's `_cand/<slot>.json` into the real `_cand/` and run
`--pick` against the real manifest — `cmd_pick` reads only `_cand/<slot>.json` and
the manifest *path* (for the output dir), never the manifest's contents. One API
search, one full-res download, real manifest never destabilised. If this pattern
recurs, the proper fix is a `--only <slot>` flag on `--candidates` rather than this
dance.
