---
summary: hi ch2 (s9–s21, 13 slots) sourced for style E — 4 reused verbatim from the style-A build under rotated names, 1 derived crop, 8 fetched across 8 contact-sheet rounds. Storyboard §10a's s13 reuse row overridden as factually wrong; the s16 graph-paper defect closed by re-source. PASS on check assets.
updated: 2026-08-08
source: fin-assets, attempt 1
---

# fin-assets — passive-income-number · hi · chapter 2 · attempt 1

**Verdict: PASS.** 13 slots, 13 files, 13 credit rows, zero duplicate md5s across all 45
shipping images in `studio/`, every source ≥1600 px, `pipeline_check check assets --chapter 2`
green.

Assets: `studio/videos/passive-income-number-hi-ch2/assets-ch2/final/`
The style-A set was rotated to `assets-ch2/style-a/` first, matching the ch1 precedent, so the
old numbering survives for any later chapter that needs it.

## Counts

| | |
|---|---|
| slots | 13 (s9–s21, VO 2.1–2.13) |
| REUSED verbatim from style A | **4** (s9, s14, s15, s16) |
| derived crop, no fetch | **1** (s18 ← s17, 91.74 % centre crop, `ffmpeg crop=1725:1031:77:46`) |
| fetched | **8** (s10, s11, s12, s13, s17, s19, s20, s21) |
| contact-sheet rounds | **8** · 47 candidate cells looked at · 8 promoted |
| candidates rejected | **39** |
| dropped from the manifest | **0** — every scene keeps a real background |
| Lotties | **0** — storyboard §8 declares ch2 art density 0; none asked for, none added |

## The reuse ledger, as executed

| new | ← style-A | what it is | ruling |
|---|---|---|---|
| s9 | `s8.jpg` | two dome-lidded brass-bound chests, closed, keyhole, window shaft on brick | REUSE. §10a calls it "old iron safe strongbox"; it is two chests. Same statement (money locked away), so the §10a override on 2.1's "steel almirah" still holds |
| s14 | `s13.jpg` | spiral notepad, blank ruled paper, pen, dark wood | REUSE. Carries the cut's only `.mega` |
| s15 | `s14.jpg` | the 91.74 % crop of s14's own source | REUSE. Its s14→s15 continuous zoom is already render-verified on this cut |
| s16 | `s11b.jpg` | hands (no face) counting CURRENT-SERIES stone-grey ₹500, MAHATMA GANDHI microtext, serial ILR 176177 | REUSE. Serial- and series-checked; this is what kills the demonetised-notes blocker under the cut's first corpus figure |

**§10a's fifth reuse row was overridden — read this before ch3.**
§10a maps new **s13 ← ch2 `s12.jpg`** and describes that file as *"steel bucket under a running
tap — exact match to 2.5's cue"*. **It is not a bucket.** It is a chrome kitchen faucet running
into a stainless sink against **white marble**, already desaturated to monochrome. That is
high-key stock under a locked `grayscale(.32) brightness(.62) contrast(1.05)` with no per-scene
override — the recorded root cause of hi ch1's failure and of ch2's own s16 defect. Reusing it
would have re-shipped the thing this run exists to stop. Same class of ledger error as the
already-corrected §10a `s7` row; recorded here so ch3–ch7 do not trust a §10a description
without opening the file.

## The queued ch2 defect is closed

`s16.jpg` (style A) — "high-key graph paper that reads as a UI panel", queued for re-source —
is **not** in the shipping set. It also actively tried to come back: it is byte-identical
(`8f513cf5…`) to a cell that the Pexels ledger pool promoted on **two separate rounds**. Caught
by md5 against `style-a/`, not by eye. Its slot's brief (2.9's worked sum) now sits on a
completely different photograph.

## The 8 fetched slots, and the overrides declared

| slot | line | what shipped | note |
|---|---|---|---|
| s10 | 2.2 | 1960s office: dark panelling, warm dome lamp, a stack of paper files, an adding machine | **OVERRIDE** vs "a printed mutual-fund transaction form, macro". 4 rounds returned only US credit-card / tax / contract forms with legible English headings, or a lit phone screen. No text, no brand, no person, no currency; arch C is satisfied and the NAME lives in the stmt |
| s11 | 2.3 | ONE rooftop water tank on a steel frame against a pale sky | **OVERRIDE** vs "plain steel tank in workshop light". The steel-tank pool is breweries — *many* tanks, which contradicts «एक टंकी है». Pale sky is ~65 % of frame but the SUBJECT is near-black, so the recorded high-key failure (white subject → charcoal slab) does not apply, and the empty sky is where the centred stack sits |
| s12 | 2.4 | a row of brass taps on a carved stone ablution wall, the near one running a thin stream | More than one tap in one frame, which is what TWO TAPS needs. Round 7's better read (an inlet hopper + an outlet tap on red brick) measured **YHIGH 88** and the gate rejected it |
| s13 | 2.5 | a brass bib tap, macro, warm highlights, dark ground, **no water** | Literally "an empty tap", which is 2.5's question. Replaces the mislabelled §10a reuse. Round 7's red-valve tap measured YHIGH 108, two under the gate |
| s17 | 2.9 | adding-machine keys — 70 50 30 10 / 80 60 40 20 9 | **OVERRIDE** vs "a hand-written division on a ledger page". FOUR ledger rounds returned the same two over-used photographs: one byte-identical to the discarded style-A s16, the other an American depreciation ledger with **"Dodge Pickup" and "New Dodge City" legible at full resolution**. Keys are numbers only — no language, no currency, no brand — and arithmetic made visible |
| s18 | 2.10 | derived crop of s17 | 91.74 %, the framing s17's ken ends on. Never a self-dissolve back to s17 |
| s19 | 2.11 | a dense bundle of telecom cables and fibre splice enclosures | **OVERRIDE** vs "a broadband bill and a recharge receipt overlapping". 5 rounds / 30 candidates on bill-invoice-receipt-statement queries returned US dollars, euros, Turkish lira, a Thai restaurant bill and a legible "CONTRACT" — the paper-money query space is poisoned. The cables are the lines that carry the phone AND the internet, so both named things are present |
| s20 | 2.12 | a drawer of aged manila record dividers in a row, warm amber, dark surround | A run of identical filed records for ALL TWELVE MONTHS. It does not assert a count, which is the fix for the style-A defect (twelve claimed over uncountable bundles) |
| s21 | 2.13 | a brick wall with ONE brick set proud in a recess | **OVERRIDE** vs "ONE brick at the foot of a stone staircase". A lone brick is unbuyable on either pool — 4 rounds returned walls, brickyards, cracked mud and two cats. This frame **singles out** one brick instead of massing them, which is the opposite of the discarded brickyard, and it keeps the keyword |

## What the full-resolution read caught that the contact sheet did not

Every promoted file was opened at full resolution. Five picks died there, not on the grid:

1. **s17 round 1 & 3** — "Custom Feeding Equipment + Trucks", "New DODGE CITY", "Dodge Pickup",
   "Fully depreciated". A car brand and a US place name, invisible at grid size.
2. **s17 round 4** — byte-identical to the DISCARDED style-A s16 (md5 `8f513cf5…`).
3. **s20 round 4** — a Thai restaurant bill: legible Thai script, a handwritten "Beef Curry /
   Gin Ale" order and a circled 1,090. Foreign currency implied, alcohol, off-topic.
4. **s10 round 1** — the form the hands were filling read "INCOME TAX QUESTIONNAIRE", which also
   pre-empts 4.9's tax beat.
5. **s10 round 5 cell 5 / s12 round 8 cell 5** — beer taps in a bar; refused on the same
   off-brand ground both times (consistency was the point).

Also rejected on the trap list across the 39: US dollars (4 cells), euros (3), Turkish lira,
a Nepali २ रुपैयाँ coin sitting in the *style-A* s11 file, "1 ZŁOTY"-class foreign
denominations, a legible tp-link `TL-SG1005P`, an Apple logo in style-A's router, an "NOS"
modem, "Credit Card/Debit Card Authorization", "Koud / Warm" in Dutch (twice), a Chinese phone
number on a garage wall, and one photo captioned VALUEABLE.

## Rule sweep

- **image_per_scene** — 13/13 scenes carry a real full-bleed photograph. Nothing dropped.
- **md5** — 0 duplicates across all 45 `*/final/*.jpg` in `studio/`. The `final ↔ style-a` pairs
  that show up in a whole-tree scan are the intended archive copies, exactly as ch1.
- **Cross-pool duplicate check (credits, not hashes)** — one "by Pixabay" credit on a Pexels
  result: **s17/s18**, `close-up-photography-of-gray-adding-machine-219570`. Grepped every
  `CREDITS.txt` under `studio/`: that photograph appears nowhere else, on either channel. The
  only repeated source URLs anywhere are the four intentional derived-crop pairs (s14/s15 and
  s17/s18 here; s3/s4 and s10/s10b in the en cut).
- **Resolution** — every file ≥1600 px: 1880 on nine, 1818 / 1732 / 1725 / 1724 on the crops and
  the two reuses. Nothing repeats ch1's 1280 px caveat.
- **Warmth** — not measured, not fetched for. The R−B ≥ +40 gate is retired (2026-08-08).
- **High-key** — the reason s13 was re-sourced and the reason s11's pale-sky frame was reasoned
  through explicitly rather than waved past.
- **Ground variety** — wood is the surface in only **3 of 13** (s10, s14, s15), against ch1's
  5 of 8. The rest: brick floor, open sky, carved stone, brass macro, outdoor blur, machine
  metal, cable, drawer card, brick wall.
- **Faces** — none. **Hands** — s16 only, which is the storyboard's declared inventory; no hand
  was added at s10 or s17 even though the best-lit candidates in three rounds had one.
- **Currency** — appears in exactly one frame (s16, current-series ₹500). No `$`, no `€`, no
  demonetised note, no prop money anywhere in the chapter.
- **Phone screens** — zero. Two lit-screen candidates were refused (s10 r4 c2, s19 r3 c3).
- **YHIGH** — `check assets --chapter 2` PASS. Two picks were failed by the gate at 88 and 108
  and replaced with brass, per the storyboard's own "change the MATERIAL, not the adjective".

## Declared for fin-editor, not pre-ruled here

1. **s19 is a high-frequency frame.** A tangle of cables under a `stmt` is legible but busy;
   it was chosen because five rounds could not buy the two named documents without foreign
   money or a brand, and a frame that names the thing beat a bland one. Rule from the encode.
2. **s11's sky.** ~65 % pale field. The subject is dark so it should separate under the grade,
   but it is the one frame in the chapter whose tonality is a genuine judgement call.
3. **s17's keys read 70/50/30/10.** No currency and no contradiction with 3.0 % / ₹30,000, but
   a numeric background under a numeric claim is worth one look on the encode.
4. **s10 contains a small out-of-focus adding machine**, and s17 is an adding-machine macro.
   Read as a through-line (the office → the machine that does the sum) rather than a repeat,
   but it is a deliberate call, not an accident.
5. **s9 is two chests**, and the container ladder puts "a steel trunk" at s31. Not a clash
   today; ch4 should pick a trunk that is visibly a different object.

## For the next chapter run

- `assets-ch2/style-a/` now holds the superseded set. **Match by BRIEF, never by number** — the
  style-E rotation re-keyed the filenames here exactly as it did in ch1, so `style-a/sN.jpg`
  and `final/sN.jpg` are different photographs for every N in this chapter.
- Do not re-fetch `style-a/s11b.jpg` (now `final/s16.jpg`): serial-checked, cleared, and the
  only current-series ₹500 in the project.
- `style-a/s16.jpg` is poisoned — the Pexels ledger query family promotes it repeatedly. If a
  ch3–ch7 ledger slot lands on `close-up-photo-of-ledger-s-list-164686`, it is that file.
- The contact sheet was short once (`s12` round 8 came back **4 of 6**, cells 1–2 missing, with
  no warning). Counted, not assumed.
