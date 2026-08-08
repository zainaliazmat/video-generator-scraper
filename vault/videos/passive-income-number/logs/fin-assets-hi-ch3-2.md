---
summary: hi ch3 attempt 2, ONE slot. s22 replaced — the carved money-box macro is gone and rung 1 of the container ladder is now a stacked yard of terracotta gullaks, every pot carrying a cut coin slit. The verdict is stated on the SIMULATED COMPOSED FRAME at the opening ken scale, not on the source, because the source read is exactly the check attempt 1 passed and the encode failed. Predicted median 26.6 / p10 15.0 / p90−p50 13.5 — deliberately darker than the 30.97 it replaces, which gains the payoff s27 a rank instead of costing it one. Floor logic untouched.
updated: 2026-08-09
source: 13 contact sheets / ~76 cells over Pixabay, Pexels and Commons; the shipped file read at full resolution and simulated through the full layer stack at ken 1.16 / 1.08 / 1.00; md5 swept against all 141 images in studio/ (both cuts, all chapters)
stage: fin-assets, cut hi, chapter 3, attempt 2
---

# fin-assets · passive-income-number · hi · chapter 3 · attempt 2

VERDICT: **ok** — 1 accepted, ~75 rejected, 0 dropped. One slot touched; the other eight
files, their credit rows and their manifest rows are byte-unchanged.

## 0 · What changed on disk

| Path | Change |
|---|---|
| `assets-ch3/final/s22.jpg` | **REPLACED** — 1880×740 carved-box macro → **1880×1058** terracotta gullak yard. md5 `5a7c7ae7…` |
| `assets-ch3/originals/s22-superseded-attempt1.jpg` | the outgoing shipped crop, archived intact |
| `assets-ch3/originals/s22-original-r2.jpg` | the new file's uncropped fetched parent (1880×1253) |
| `assets-ch3/final/CREDITS.txt` | s22 row **re-keyed** to Tony Wu / Pexels, with the crop geometry and the retirement of the Debraj Chanda row stated in the same line |
| `assets-ch3/final/manifest.json` + `s22.jpg.src` | s22 row rewritten (query, cell, crop, ladder role, composed-frame verdict, geometry note for the build, measures, rejections) |

`python3 tools/pipeline_check.py check assets --slug passive-income-number --cut hi --chapter 3`
→ **PASS assets-hi**.

⚠ **One thing I destroyed and you should know about.** Writing the new parent I overwrote
`originals/s22-original.jpg`, the uncropped parent of the *outgoing* carved-box frame, before
renaming the new one to `-r2`. Nothing shipping depended on it (the shipped crop itself is
archived, and its credit row is retired), and it is one fetch from
`pexels.com/photo/close-up-shot-of-brown-wooden-coin-box-6534325/` if anyone ever wants it back.
Recorded rather than quietly left.

---

## 1 · The one thing this fetch had to guarantee

**The replacement reads as a container ON THE ENCODE, AFTER THE GRADE.** So nothing here was
judged on the source file. I rebuilt the composed-frame simulator (16:9 cover → `.bg` `inset:-8%`
× ken → sRGB `grayscale(.32) brightness(.62) contrast(1.05)` → `.field` at `.38` with `.rules`
and `.glow` → the four `.scrim` layers → BT.601 luma), rendered the result as an actual PNG, and
**looked at it** at the three ken scales — including **1.16, the OPENING scale**, which is the
frame the gate has standing over.

Two calibrations worth stating because they are what makes the numbers usable:

- **Anchor.** The outgoing `s22.jpg` run through the same simulator *with its own inline window*
  gives median 35.8 / p10 22.5, where the encode measured **30.97 / 19.59**. So on this exact
  slot, this simulator reads **+4.83 median / +2.91 p10 high**, and every figure below is quoted
  after subtracting that. Across the four other ch3 frames whose encode medians the editor
  published the residual runs +5.5 / +4.9 / +2.3 / −1.1, so **treat the anchored figures as
  ±3 points**, not as measurements. Only the encode settles.
- **The rendered PNGs are the raw simulation, so they look ~5 points darker than the encode
  will.** The frames below passed the sound-off read at that handicap.

### The verdict, on the composed frame

> **PASS.** Round clay vessels, each with a black slot cut into its shoulder, stacked. Type
> covered, a viewer names a concrete object — a money pot — and names it forty times.

And the reason this is not a coin flip: **the failure being replaced was contrast collapse, and
this frame's legibility does not rest on a silhouette at all.** Attempt 1 was one pale object on
one pale out-of-focus ground, so a single boundary carried the whole read and `brightness(.62)`
took it. Here the read is carried by ~40 near-black slits and the shadow gaps between pots —
*local* contrast, which a brightness multiplier scales but cannot flatten. I also simulated the
frame under the build's **stale inline window** (`background-size:2781.37px auto;
background-position:38.74px 79.00px`, fitted to the old 2.541-aspect file): it passes there too,
if anything more strongly. **The frame is robust to whether the build keeps or drops that
override** — see §4.

## 2 · The measures

Ranked on **median**. `p90` is retired; `p90 − p50` is reported and ranks nothing.

| | median | p10 | p90 − p50 |
|---|---|---|---|
| **s22 (new), anchored** | **26.6** | **15.0** | **13.5** |
| s22 (outgoing, encode) | 30.97 | 19.59 | — |

Simulated at all three ken scales the median moves 31.3 → 31.4 → 31.0 (raw), i.e. the sweep is
flat: there is no framing inside the ken at which this frame is materially darker than another.

**It comes back DARKER on purpose.** The editor's constraint was one-sided — *do not open more
than 1.0 median point over s27 (30.91)* — and at 26.6 the opener drops below the payoff, so
**s27 gains a rank on median rather than losing one**. Consequences, checked rather than assumed:

- **Floor logic untouched, as instructed.** s26 stays the floor at 19.49 and is still 4.98 clear
  of the frame above it (s24, ~24.5). The new s22 sits at 26.6 — **7.1 above the floor and above
  s24** — so it changes neither which frame is bottom nor the size of the bottom gap.
- **Near-zero spread is not claimed as a credit.** `p90 − p50` of 13.5 is mid-pack for this
  chapter and is reported as a fact, not a virtue. A flat pale slab is what is being removed;
  buying a *different* flat frame would have been the same defect in another key.

## 3 · The ladder — rung 1 briefed against s31's actual file

I read `passive-income-number-hi-ch4/assets-ch4/final/s31.jpg` at full resolution first, as
required: **one large domed, iron-banded, hasp-fastened wooden chest with painted floral
cartouches, whole object, filling the frame against a stone wall, with a floor and a broom beside
it for scale.** Rung 1 was then chosen as something s31 *visibly escalates from*:

    s22  a fist-sized clay gullak, one of a yard of them   ->
    s31  one large iron-bound wooden chest, broom for scale ->
    s58  bank locker  ->  s62  safe door

Nothing was briefed as "smaller than s16"; s16 is not on the ladder. The four rungs are the
`run.json` ruling's, not the storyboard's — **§9c, §10 and §12 all still carry the dead five-rung
list starting at s16, and §10 additionally says s22 is "two cash boxes … each visibly bigger than
the last" where the file is one shoot with no predecessor.** Those three copies are still stale
after this fix and ch5's assets agent will read them.

⚠ **Declared, because it is the one place this rung is not a clean match:** rung 1 is **many**
containers where rungs 2–4 are one each. I could not buy a single Indian money pot in isolation —
13 sheets, and the pool answers `gullak` with euro coins and `clay piggy bank` with pink ceramic
pigs. The escalation still reads, because it is carried by **size** and the size difference is
enormous (a fist-sized pot against a chest with a broom leaning on it). If the CEO would rather
rung 1 be a single object, the honest options are to draw it or to accept a near-miss, and I
would take this over a near-miss.

⚠ **For ch5:** the root manifest briefs **s41 as "a hairline crack running across a dry clay
pot"**. That is now the same material and near the same object as the ch3 opener, two chapters
apart. Re-brief s41 before it is fetched.

## 4 · One thing the build must do

The file is now **16:9 (1880×1058)** where the old one was **2.541 (1880×740)**. The inline
`background-size:2781.37px auto;background-position:38.74px 79.00px` on `#s22-bg` was hand-fitted
to the old file's geometry to hold its brass hasp inside the ken sweep union. **Drop it — let
`.bg` take plain `cover`.** This is a tidy-up and not a risk: I simulated the new file both ways
and both pass the gate, so a build that forgets still ships a legible opener. It is in the
manifest row too, so it cannot be lost with this log.

## 5 · Sourcing discipline

- **≥1600 px:** 1880 px wide, full source width — the crop is vertical only, so the ken's
  full-bleed upscale drops from the outgoing 1.479× to 1.185×.
- **Full-resolution read, done separately from the composed-frame read, because they catch
  different things.** At 1:1 the frame carries **no text in any language, no coin of any country,
  no currency, no hand, no face, no brand mark and no crypto prop**. A blue tarp corner top-left
  and a straw mat top-centre are the only non-pottery objects.
- **md5 swept across all 141 images in `studio/`** — both cuts, all four chapters of each, plus
  the sibling chapters' `final/`. **No collision.** (The 13 hashes the sweep reports as repeated
  are all archive pairs of one slot — `superseded-r2/` and `style-a/` copies — not cross-slot
  duplicates.) Both the crop and its parent were hashed.
- **Cross-pool tell:** the shipped file is a Pexels result credited to a Pexels photographer;
  no "by Pixabay" credit anywhere in the promoted set.
- **INR/India reading:** the object *is* the Indian gullak form and the frame carries no signage
  of any country. ⚠ Declared: this is a pottery yard whose nationality is not provable from the
  frame. It is currency-neutral, which per the standing rule beats a wrong-currency frame; it is
  not an identifiable-place claim.

## 6 · What was refused, and the two patterns worth keeping

13 sheets / ~76 cells across Pixabay, Pexels and Commons.

| Family | What it was | Why |
|---|---|---|
| ceramic piggy banks (~14 cells) | pink, blue, red, orange cartoon pigs | **argues with its line** — a cartoon pig under ₹20,00,000 says pocket change; also off-brand for the cut |
| the euro cash-box shoot | grey steel box on gravel, euro coins and €500 notes | the exact shoot ch2 documented, returned *again* on `terracotta money box` |
| **the outgoing shoot itself, 6 further cells across 4 queries** | the Debraj Chanda carved box, 3 of them still carrying the Nepali `2 rupaiyan` coin ch2 killed | re-buying the frame I was sent to replace |
| legible marks | `RONSON Roto-Shine`, `BISCUITS`, `The MYSTERIOUS PLANCHETTE`, `Tout pour LA FAMILLE`, Cyrillic `ПОЧТА`, a kanji offering box | readable brand/title marks |
| wrong currency | Pixabay's euro-coin cutouts (returned for BOTH `gullak` and `coin bank`), a `$20`-in-a-chest series, a stack of ₹500 notes whose serial `908495` repeats across notes | wrong currency; the last is the prop-money tell |
| people | a `दानपात्र` temple box with a sadhu, potters at wheels, a hand placing a coin | a person in a money frame |
| wrong rung | riveted steamer trunks (the subject ch2's editor blocked at s9), a cast-iron safe door | those are s31 and s62 |
| too dark | a carved box on a bar counter — the best single-object candidate found | **the simulator killed it: anchored median 13.3**, which would have taken the floor off s26 and broken the thing I was told not to disturb. It looked fine at full resolution. |

Two things I would carry forward:

1. **The simulator did work no read could have done.** The best-looking single object in 76 cells
   was the one that would have made this chapter's floor worse. A source-side judgement would
   have shipped it — which is the same class of error this whole attempt exists to correct.
2. **`@commons` cannot help here and that is not a surprise.** `gullak` and `money box india`
   returned **zero results**; `hundi donation box` returned Odisha temples and a US supermarket
   self-scan rack. Commons finds *named things*; a gullak is an object, so it is Pexels or
   nothing. Worth writing down so the next slot does not spend a round proving it again.

## 7 · Not touched, deliberately

s23–s30, their crops, their credit rows, their manifest rows and `_cand/`. s27 is unchanged, per
the ruling that the payoff clause is satisfied. No per-scene `filter:` override was added — the
grade is load-bearing and this frame does not need one.
