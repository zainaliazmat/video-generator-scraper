---
summary: Attempt 5 re-sourced two slots — s53 (the 62.2% hero) and s91 (the .cta close) — both now 1880px Pexels files, mean luminance 59.5 and 102.4; library stays 94 images, manifest/CREDITS/.src 1:1.
updated: 2026-08-01
source: fin-assets stage run, japanese-money-methods-hi, attempt 5
---

# fin-assets — hi cut, attempt 5 (two slots: s53.jpg, s91.jpg)

**Scope:** two files. Orchestrator ruling on storyboard-hi §9a — the two 1280px
slots that carry a beat (the `hero` number and the `.cta` close) are re-sourced from
Pexels; the other 92 images were not touched.

## Result

| | |
|---|---|
| accepted | 2 (`s53.jpg`, `s91.jpg`) |
| rejected | 34 cells across 6 contact sheets, + 1 promoted file rejected at full-res |
| dropped | none — both slots kept their background |
| library | 94 images, unchanged count |

| slot | old | new | width | mean-L |
|---|---|---|---|---|
| s53 | Pixabay `accountant-…-1238598`, 1280×853, mean-L 176.5 | Pexels `nighttime-urban-apartment-building-in-kyoto-31359829` by Julien | **1880×1175** | **59.5** ✓ |
| s91 | Pixabay `book-pen-notebook-diary-desk-4806076`, 1280×1021 | Pexels `brown-pen-on-white-notebook-303532` by Lum3n | **1880×1256** | **102.4** ✓ |

Both ≥1880 (requirement) and ≤140 (requirement), measured on the promoted files, not
the sheets. Source resolutions 3840×2399 and 3008×2000 → `large2x` is a downscale, so
neither is upscaled even at full-bleed. Neither is near-black, so the cut's one
`filter:` override stays unspent (still owed to s36c per attempt 1).

## Dedupe

`md5sum studio/videos/*/assets/img/*.jpg | sort | uniq -w32 -D` → **empty** across
**187 files** (94 hi + 93 en). Zero collisions.

- s53 `d61c3f1cb7002cc7678acaaa7c71f245`
- s91 `4cc57a5914a3a9edab98f53cca334fb4`

**The cross-cut collision the brief named was real and was avoided by subject, not by
hash.** en's re-sourced s91 is a tight macro of *reading glasses on a black cloth
notebook*, cool light, no pen. hi's is a *white hardbound notebook with a capped
rosewood pen* on dark warm wood, whole object in frame. Different colour key, different
prop, different framing distance — not the same desk re-cropped. One sheet (s91 sheet A,
"closed leather bound ledger…") did return an open book with glasses on it; it was
rejected partly for that reason.

## ⚠ s53 changed subject — flagging it, not hiding it

The storyboard's image note for 5.7 is *"the FIES table again, the consumption row in
focus"*. **The printed-table genre cannot meet the ≤140 luminance bar.** Measured:
`s13.jpg` (the FIES table it would call back to) is **183.9**, `s39.jpg` is **203.4** —
paper photographed to be readable is bright by construction. Four sheets of
table/calculator/report queries returned nothing both dark and clean; the one dark
option that promoted was rejected at full res (below).

New subject: **a Kyoto apartment block at night, exterior corridors lit, no people.**
It answers the VO's actual keywords — «जापान के उसी सर्वे में **नौकरीपेशा परिवार**…» —
salaried-worker *households*, which is precisely what FIES measures. It is also
currency-neutral, textless, and a calm repeating grid under a 240px number. Scene 5.7
is `RAIL ON`, so the photo sits in the x=1180→1920 panel and the number is on flat
`--bg`; the facade's detail does not fight the type.

If the audit wants the literal table back, it has to come with a luminance waiver.

## What was rejected, and why

Sheet 1 — s53 `calculator on a printed table of numbers close up@pexels` (6/6):
| cell | verdict |
|---|---|
| 1, 3 | blown-out white desks, mean-L far over bar |
| 2 | dark and usable, but the paper under the calculator is engineering drawings, not figures |
| 4 | laptop edge in frame |
| 5 | **phone screen** as the subject + a **US 1040-ES** form — two standing rejections at once |
| 6 | **phone screen** + foreign coins |

Sheet 2 — s53 `printed financial report page with columns of numbers close up@pexels` (6/6):
| cell | verdict |
|---|---|
| 1 | laptop in frame |
| 2, 3, 5, 6 | bright white; 3 and 6 are charts with a direction the VO never claims; 5 carries a readable `LEADERS` masthead |
| 4 | bar chart + people's hands, bright |

Sheet 3 — s53 `vintage adding machine with printed paper tape close up@pexels` (6/6):
**all six were typewriters with loaded words typed into them** — `ELECTION FRAUD`,
`PRIVATE EQUITY`, `DIVERSITY`, `Newspaper`, `turn the page`. Whole sheet dead. Naming a
machine that no longer exists in stock gets you the machine that replaced it in the
photographer's prop box.

Sheet 4 — s53 `printed table of statistics on paper with a pen close up@pexels` (6/6):
| cell | verdict |
|---|---|
| 2 | **EUR 100 notes** in a ₹ cut |
| 1, 3, 6 | people/hands over charts, bright, English chart labels |
| 4 | best content on the sheet (a statement with one row circled red) but mean-L ≈190 |
| 5 | repeat of sheet 2's `Column Chart` |

Sheet 5 — s53 `ledger page with columns of numbers in warm lamplight dark room@pexels` (6/6):
cell 3 was an **1813 Italian** ledger (period mismatch with a 2024 statistic, mean-L 147),
cell 1 measured 173.7, cells 4 and 6 read as nothing at all. **Cell 2 was promoted and
then rejected at full resolution** — see below.

Sheet 6 — s53 `printed paper page of numbers under a desk lamp at night dark room@pexels` (6/6):
cell 3 was **the same photograph already on disk as `s13.jpg`** (a dedupe collision the
grid caught before the fetch); 5 and 6 put a person's face in a statistics frame; 4 had
a phone under the calculator and read as AI-generated (mushy keycaps, wrong fingers).

Sheet 7 — s53 `japanese residential apartment building with lit windows at dusk@pexels`
(6/6): 4 daylight-bright (79.5); 3 and 6 read Eastern-European, not Japanese; 1 and 5
were generic night towers, correct luminance but no country; **2 PICKED** — the Pexels
page title says *Kyoto*, which is why it was chosen over the two anonymous towers.

Sheet A — s91 `closed leather bound ledger book with a fountain pen on top@pexels` (6/6):
the word "leather" pulled the whole sheet into antique-European territory — a quill and
crumpled paper, an *open* 1813 ledger, an open manuscript with glasses (the en
collision), a bookshelf. Cell 4 (closed ornate book, pen on top) was the only close, and
it had playing cards in frame. Wrong century for a CTA.

Sheet B — s91 `closed kraft notebook and a pen flat lay on a dark surface@pexels` (6/6):
cells 2, 4 and 6 all had a **laptop** in frame and 6 added a **phone**; 1 was a bright
white stationery flatlay; 3 was unreadable black; 5 was a product mockup with no pen.

Sheet C — s91 `closed diary with a pen on a wooden table dim light@pexels` (6/6):
2 open (contradicts "finished"), 3 and 5 too shallow-focus to survive a zoom, 6 had a PC
tower in frame, 1 was the same idea as the pick but on a bright light-wood desk with an
embossed cover mark. **4 PICKED.**

## The full-resolution read earned its keep again

`s53` sheet 5 cell 2 promoted cleanly: a dark, aged, open ledger of ruled columns,
mean-L 95.3, exactly the right tone. At 1880px it reads **`New Dodge City`**,
**`Dodge Pickup`**, `Serial #1681 623904` and `STANDARD PROPERTY LEDGER FORM 20-A` — a
readable car brand and a US corporate asset register, in a Hindi cut whose money is ₹.
Invisible at contact-sheet size; fatal at full frame. Re-picked to a different subject
entirely rather than hunting another crop.

## Full-resolution notes on the two accepted files

**s53** — no people, no faces, no text of any kind, no signage, no logo, no screen, no
currency. Fire extinguishers and AC units on the balconies are the only props. Warm
corridor lighting against a black sky; the brightest pixels are small lamp hotspots, so
the frame stays quiet under `--target` type. Neighbours check out: s52 is an empty
wallet, s54 a dusty wall switch — s53 is now the only wide exterior in that run, which
breaks up a stretch of tabletop objects.

**s91** — closed cream hardbound notebook, elastic band and ribbon marker still in
place, one capped pen laid across it, dark warm wood. **No brand mark on the pen or the
cover** (checked at full res specifically). No screen, no person, no money, no text.
Reads "work finished" without repeating s89 (open notebook under a lamp) two scenes
earlier, because this one is shut.

## Files updated

- `studio/videos/japanese-money-methods-hi/assets/img/s53.jpg` (1880×1175)
- `…/s53.jpg.src` → `japanese residential apartment building with lit windows at dusk@pexels`
- `…/s91.jpg` (1880×1256)
- `…/s91.jpg.src` → `closed diary with a pen on a wooden table dim light@pexels`
- `…/manifest.json` — both queries updated to match their `.src` exactly (so a later
  plain `--manifest` run skips instead of clobbering). 94 entries, set-equal to disk.
- `…/CREDITS.txt` — **94 lines, 94 unique slots, set-equal to the 94 jpgs**, verified
  programmatically. The replace-in-place `write_credit` left no stale Pixabay line for
  either slot.

## Process note

`--candidates --only s53 s91` worked exactly as advertised and removes the scratch-manifest
dance that attempt en-7 had to invent — one API search per slot, no risk to the other 92
entries. **The lesson this run adds:** when a slot has a *measured* luminance bar, check
the sheet's cells numerically before promoting anything (the sheet is a 3×2 grid of
512×288 cells — crop and measure). Two of the six sheets above could have been discarded
without a vision pass at all, and cell-level measurement is what identified that the
whole printed-paper genre was out of reach before a fourth query was spent on it.
