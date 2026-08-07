---
summary: s4 (ch1, hi) re-sourced on the third try under a new hard gate — source YHIGH ≥ ~130. Promoted a white enamel "275" plaque on a deep-red door (Pexels, YHIGH 203). All other ch1 slots untouched.
updated: 2026-08-07
source: fin-assets attempt 4, chapter 1, hi cut. One slot only.
---

# fin-assets — passive-income-number / hi / chapter 1 / attempt 4

**Scope: s4 only.** s1, s2, s3 (photo + Lottie), s5, s6, s7 were not read, not
re-fetched, not re-picked. `manifest.json` changed on exactly one line.

## The gate this attempt was run under

The parent stage supplied the predictor: **the source's highlight ceiling, not its
average brightness.** Measured across all seven ch1 sources before touching anything:

| slot | YLOW | YAVG | YHIGH | verdict |
|---|---|---|---|---|
| s1 | 40 | 144.1 | **244** | fine |
| s2 | 40 | 92.2 | **162** | fine |
| s3 | 3 | 56.5 | **134** | fine — *darker on average than s4 and survives* |
| s4 *(round 2, rejected)* | 3 | **59.4** | **93** | dead: no highlights to spend |
| s5 | 45 | 109.2 | **160** | fine |
| s6 | 33 | 80.1 | **203** | fine |
| s7 | 10 | 70.9 | **180** | fine |

s3 vs s4 is the whole argument: s3 is the darker photograph on average and reads fine,
because it has a specular ceiling of 134 to spend. s4 had none. Hard gate applied:
**promote nothing measuring YHIGH below ~130.**

```
ffprobe -v error -f lavfi -i "movie=<file>,signalstats" \
  -show_entries frame_tags=lavfi.signalstats.YLOW,lavfi.signalstats.YAVG,lavfi.signalstats.YHIGH -of csv=p=0
```
(csv order is YLOW, YAVG, YHIGH — the tag order in the frame metadata, not the order asked for.)

## The new query and why the object changed

VO 1.4: «आप अमीर नहीं हुए — आप बस एक ख़ास नंबर तक पहुँच गए।» — *you didn't get rich,
you just **reached a specific number***. On-screen: kicker `NOT RICH`, stmt
"You just reached a number".

The envelope was the storyboard's suggestion, not a requirement, and two rounds proved
kraft paper is a matte material — it has no highlight to give, at any exposure. Changed
the *object*, not the lighting adjective:

`brass house number on a dark wooden door close up@pexels`

A door number is the number you arrive at. It is currency-neutral, brand-free, and its
meaning-carrying element (the numeral) is also its brightest element — which is the vault's
rule 3 ("a bright detail that carries the meaning must survive `.62`") satisfied by
construction rather than by luck.

## The sheet — 6 of 6 cells, pre-measured before spending the fetch

Per-cell YHIGH read straight off the contact sheet with a `crop=512:288:x:y` before
`signalstats`, so the gate filtered candidates at **zero fetch cost**. (Cells 1/3/6 are
letterboxed by the tiler, which depresses their reading slightly; 4/5 fill the cell.)

| cell | what it is | YHIGH (sheet) | call |
|---|---|---|---|
| 1 | near-black door, "2 À 1" enamel tiles | 58 | **reject — gate.** Nothing above mid-grey anywhere. |
| 2 | green door, ornate brass knocker, no number | 79 | **reject — gate + meaning.** No number in frame; sound-off it says "fancy door", not "a number". |
| 3 | red door, white enamel **275** plaque | **198** | **PICK** |
| 4 | weathered brown door, brass **505** + iron letter plate | 106 | **reject — gate.** Best sound-off read of the six and the closest match to `#1f1b16`; killed anyway because the brass numerals are mid-tone warm on mid-brown wood, i.e. exactly the round-1 failure with a different prop. Unpadded cell, so 106 is an honest reading. |
| 5 | dark green door, **black** 281 numerals | 63 | **reject — gate.** The meaning-carrying element is the darkest thing in frame; it would vanish under `grayscale(.32) brightness(.62)`. |
| 6 | hand on a brass door handle, red door | 102 | **reject — meaning.** No number. |

Cell 4 losing to cell 3 is the attempt in miniature: **pick for the highlight first,
then for the meaning**, because a frame that reads perfectly ungraded and has no ceiling
is the defect we already shipped twice.

## What was promoted — measured

`s4.jpg` — Pexels, Erik Mclean, "A Door Number Sign on a Red Wooden Door", Pexels License.

| measurement | value | gate |
|---|---|---|
| **source YHIGH** | **203** | ≥ ~130 ✓ (round 2 was 93) |
| source YAVG / YLOW | 101.7 / 28 | — |
| width | **1880 px** | ≥ 1732 ✓ (Pexels `dpr=2&w=940`) |
| YHIGH at ken 1.16 crop | **200** | survives the zoom at both extremes ✓ |
| md5 | `8aaa7d6dbc0d8881191b43e877140b99` | distinct across all 20 studio images ✓ |

Simulated under the locked grade (`colorchannelmixer` ≈ grayscale .32, then contrast 1.05
about mid-grey, then ×0.62): **YLOW 22 · YAVG 63 · YHIGH 119 — tonal spread 97.**
Round 2 encoded at YAVG 24.8 / YHIGH 27, spread **14**. The frame now has a range to live in.

## Sound-off test, all five

1. **Says the point without words?** Yes — a specific number, physically mounted, arrived at.
2. **Argues with the line?** No. "तक पहुँच गए" is literally arrival at a number; a house number is the number you arrive at.
3. **Is the named thing in frame?** The line names «एक ख़ास नंबर». `275` is a specific number, in frame, and it is the brightest object.
4. **Reused in this chapter?** No. ch1 is clock / chai glass / phone / **door** / jars / staircase / scale — seven distinct objects.
5. **Place, era, currency?** Currency-neutral — no money, no denomination, no symbol in frame, so none of the wrong-currency traps apply. No brand mark, no screen, no face, no chart, no legible text but the numeral itself.

## Housekeeping

- `CREDITS.txt`: the stale PNW Production / kraft-envelope row is gone, the Erik Mclean row is in. Verified all 7 photo slots + the Lottie line have rows.
- `s4.jpg.src` rewritten to the new query.
- `manifest.json` updated in the same move — one line.
- `python3 tools/pipeline_check.py check assets --slug passive-income-number --cut hi --chapter 1` → **PASS assets-hi**.

## The reusable finding

**Measure the contact sheet's cells, not just the promoted file.** `crop` + `signalstats`
on the sheet gives a per-candidate YHIGH before any full-resolution fetch, so a
brightness gate becomes a filter on the sheet instead of a retry after the encode. On
this slot it rejected four of six cells — including the one that won on looks — for the
cost of six ffprobe calls and zero downloads. The full-resolution read still happens on
the promoted file, because that is what catches legible text.

**And: matte materials have no ceiling, at any exposure.** Round 1 lit kraft badly,
round 2 lit kraft well against black, and both measured dead, because kraft paper is
diffuse — there is no specular return to grade. When a slot fails twice on brightness,
change the **material** (enamel, glass, glazed ceramic, polished metal, wet stone), not
the lighting adjective in the query.
