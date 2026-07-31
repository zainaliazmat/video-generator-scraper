---
summary: fin-assets, en cut, attempt 2 — targeted 6-slot fix. s36/s59/s84/s88 replaced after fin-build's max-density pass found Canadian coinage under the BEA statistic, two foreign coin piles and a legible credit-card authorisation form; s2 and s1 added mid-pass, s2 for Bitcoin props in the cold-open hook and s1 to retire the last 1280 px asset in it. All six verified at full resolution, not at contact-sheet size; 6 accepted, 0 dropped, 0 new duplicate hashes.
updated: 2026-07-31
source: fin-build-en-1 rejection list; tools/stock/pixabay_fetch.py contact sheets + full-res inspection; knowledge/stock-photo-sourcing.md
stage: fin-assets, cut en, attempt 2
---

# fin-assets — en cut, attempt 2 (targeted fix)

## Result

**6 replaced / 6 requested. 87 untouched. 0 dropped. 0 duplicate hashes.**

| slot | was | now | why the old one failed |
|---|---|---|---|
| s1 | US $2 bills + silver dollars on red-brown wood, **1280 px** | a small stack of **worn US $1 bills** on weathered plank wood, raking light, two unbranded iron weights, **1880 px** | nothing wrong with the frame — it was the last 1280 px asset in the cold open and hit ~1.6× on its zoom |
| s2 | glass jar of $100s with two gold **Bitcoin props** in it | a raking macro **fan of four current-series US $100 notes**, `FEDERAL RESERVE NOTE`, serial `JG 12020692 A`, worn paper, pale stone | a crypto prop in the cold-open hook of a savings video — attempt 1 refused the same prop on s91 and s43 |
| s36 | Canadian coin tray (`CANADA` / `DOLLAR` / `D·G·REGINA` / `5 CENTS` at 2×) | macro of two US **$1 bills** — `UNITED STATES OF AMERICA`, `WASHINGTON, D.C.`, Washington portrait, green Treasury seal | wrong country under the BEA 2.7 % national saving rate |
| s59 | copper stacks with mixed foreign coins in the loose pile | a single **rolled US banknote** with a red band, white marble, no denomination legible | foreign coinage in a `$` cut |
| s84 | paper form reading `Credit Card/Debit Card Authorization` | a **hand with a plain blue pen signing an unbranded printed form**, hard side light | a credit-card product on screen under a savings-transfer instruction |
| s88 | pile of gold-coloured (euro/pound) coins | **three glass jars packed full of rice, buckwheat and oats** on pale concrete | no US circulating coin is gold at that scale; also not the storyboard's "full jar" |

Every replacement is **US currency or currency-neutral**. Nothing kept that
carries a foreign denomination, a brand mark, a face, a phone screen or an
off-message product.

## Method change that actually caught things — full-res, not grid

fin-build's finding was that every defect on both cuts was invisible at contact-sheet
size and legible at 1:1. So this pass inverted the default:

1. the sheet is used **only to shortlist** — it can be trusted for subject, never for text;
2. the shortlisted cell is **promoted at full resolution and Read at 1:1** before it counts
   as accepted. Nine full-res inspections, six accepts — s2 alone burned three.

That order is what the next cut should run on any money frame. The grid is a
subject filter; the 1:1 read is the defect filter. Reading the *shipped* images
at 1:1 is also what would have caught all of this at attempt 1 for free — the
files were already on disk.

**The 1:1 read rejected two cells that the grid had already passed.** Both on s2:

- `savings jar with money@pexels#12` cell 1 — a mason jar of coins with a plant
  growing out of it, warm wood, no text. Clean at grid size. At 1:1 the top coin
  reads **`20`** and a second reads **`50` / `SEN`**: no US circulating coin carries
  a bare `20`, so this was the same wrong-currency defect being fixed, one step
  from shipping into the hook.
- `stack of hundred dollar bills@pexels` cell 2 — two tidy stacks on white, which
  is what I picked first. At 1:1 **every note in both stacks carries the same serial,
  `LB45440078L`** — reproduction/prop money. Not on the standing trap list and no
  licence problem, but it is the demonetised-₹500 failure in US clothes: an
  authenticity tell a viewer can catch on a finance channel. Re-picked cell 4 of the
  same sheet at no fetch cost.

**Add repeated serial numbers to the trap list** — it is the one banknote defect
that is invisible until you can read two notes in the same frame, which means it is
invisible at contact-sheet size by construction.

## The sheets: what the pools actually hold

- **s36 old sheet — all six cells failed.** Canadian tray, a branded payment
  terminal, a `NATIONAL`/`Escudos Cts` till, coins on a scale, a euro-note
  arrangement, a curio cabinet of foreign banknotes. Re-queried
  `one dollar bill macro@pexels` → **all six cells US dollars.** Naming the
  currency in the query is the whole fix; "coin tray", "coin pile", "jar of
  coins" are country-blind and Pexels/Pixabay answer them with whatever the
  photographer had in their pocket, which is rarely American.
- **s59 old sheet — all six cells failed** (euro cents ×2, mixed gold, ancient
  gold hoard, the shipped mixed pile, blue bottle caps). Re-queried
  `rolled dollar bills stack@pexels` → six US-dollar cells.
- **s88 needed two re-queries.** `glass jar full of dollar bills@pexels#6`
  returned one photo from **the same shoot as the already-shipped s2** (same jar,
  same scoop, same $100s, same bitcoin props) plus five frames of an *empty* jar
  with one roll in it — the opposite of the scene's meaning. Dropped the money
  jar and kept the **jar**: `glass jar filled to the brim with grain@pexels`.
- **s84 needed no fetch at all** — cell 4 of the attempt-1 sheet was already
  clean. Re-pick, zero API cost.
- **s2 took four sheets.** `us coins and dollar bills in a glass jar@pexels`
  returned the bitcoin shoot itself plus the empty-jar shoot; `savings jar with
  money@pexels#12` added the "Where to next?" travel-fund shoot and the foreign-coin
  jar above; `one glass jar of oats on wooden table@pexels` returned food-blog
  granola styling that reads "healthy breakfast", not "stores laid in".
  `stack of hundred dollar bills@pexels` returned **six US-dollar cells out of six**.

  **The Pexels savings-jar pool is four shoots and that is all it is** — bitcoin
  props, an empty clip-top jar, a pink travel fund, and a foreign coin jar. Any
  future "money jar" slot on either channel should skip straight past it. What
  works is naming the currency and the note: `dollar bill`, `hundred dollar bills`,
  `rolled dollar bills` each returned 6/6 usable US cells on the first try, three
  times out of three.
- **s1 took two sheets, and the first one was a bitcoin minefield.**
  `few dollar bills and coins on a table@pexels` returned **two of six cells with
  gold ₿ props** (cells 1 and 6) — the same defect just removed from s2, from a
  query that never mentions crypto. One cell also carried a smartphone as a prop,
  one was a near-twin of s87 ($100s + coins + a bright accessory on white), and
  two put a black chronograph watch in frame. `two dollar bill on wooden
  table@pexels` returned six clean US cells.

  **Naming the *denomination*, not just the currency, is the sharper version of
  the rule.** `dollar bills and coins` is a generic money-flatlay query, and the
  generic money flatlay is exactly where stock crypto props live; `two dollar
  bill`, `one dollar bill macro`, `hundred dollar bills` name an object that has
  no crypto equivalent — and none of those three sheets contained a single ₿ prop.

## One declared substitution (s88)

The storyboard asks for "the full glass jar (new photograph)" at 9.6 — *"On the
tenth ten thousand, that same market buys you six and a half."* The Pexels
savings-jar pool is one shoot of an **empty** jar, and its only full jar is the
s2 photo. Rather than ship a wrong-currency coin pile (the exact defect being
fixed), the slot keeps the **jar** and changes what is in it: three jars packed
full of staples. It reads the scene's keyword more literally than money did —
six and a half *months* of living is a pantry, and "full to the brim" is the
image the line needs. Currency-neutral by construction.

Smaller: **s59 loses the small-pile/large-pile comparison.** No US-currency
pair-of-piles photo exists in either pool; a single modest roll of cash under
*"if your twenty percent is two hundred dollars, then you start at two hundred
dollars"* carries the same "this is a small amount and that is fine" reading,
and s59 is a mosaic background where the comparison was never going to be read
anyway.

## Resolution

All six came from Pexels, whose `--pick` URL is `dpr=2 · w=940` → **1880 px
wide**, against Pixabay's `largeImageURL` at **1280 px**. That clears the
≥1600 px bar the hi cut's hook missed, and it matters most on **s36**, which
takes a 2× zoom: at 2× the frame still reads `UNITED STATES OF AMERICA`.

**The cold open is now entirely 1880 px** — s1 and s2 were both 1280 px Pixabay
assets and both are now Pexels. The ~1.6× upscale render QA measured on the hi
cut's hook does not exist on this one.

**Standing note for the next cut: prefer `@pexels` on any slot that carries a
zoom or a hero number — it is a 47 % linear resolution gain over Pixabay for
free, independent of the dedupe reason to reach for it.**

## Dedupe

`md5sum studio/videos/*/assets/img/*.jpg` — the six new hashes are unique
against this cut's other 89 files, the 86 files in
`first-lakh-first-thousand-hi`, and every other project on both channels.

One pre-existing duplicate pair exists and is **out of scope, and looks
deliberate**: `first-lakh-first-thousand-hi/assets/img/s5.jpg` and
`first-lakh-first-thousand-thumbs/assets/img/s5.jpg` are byte-identical — the
thumbnail project reusing a scene image, which is the point of a thumbnail.
Flagged so the next md5 sweep does not re-litigate it.

## What the s2 change costs the storyboard

Storyboard §7 pairs **s2 ↔ s88** ("the full glass jar", same object, new
photograph). Neither slot is a money jar any more, so **that pair is now
retired, not re-shot**: s2 is a $100 macro, s88 is full staples jars. The
s1 ↔ s87 pair (small money frame → fuller money frame) is untouched and still
carries the cold-open-to-payoff recall on its own.

Worth saying plainly: the jar was the storyboard's device, and the pools do not
contain an honest US money jar. Faking the recall with a wrong-currency or
prop-money jar would have cost more than losing it.

## The s1 ↔ s87 pair, which the s1 swap had to protect

§7 pairs **s1 ↔ s87** ("the mug, now noticeably fuller"). Neither is a mug — the
attempt-1 substitution made it a money pair instead, *less money on a surface* →
*more money on a surface*. That pair now carries the cold-open-to-payoff callback
alone, so it was the constraint on this swap, not resolution.

It survives, and reads slightly better than before:

- **new s1** — a few worn $1 singles on rough plank wood, dim raking light.
- **s87** (untouched) — a bright white flatlay of $100s, $20s, $10s and a spread
  of coins, with room to spare.

Worn singles in the dark → hundreds in the light is a **wider** gap than the old
s1's $2 bills and big silver dollars, which already looked like a decent handful.
The callback is stronger, not merely preserved. Had it not been, the instruction
was to keep the 1280 px file, and I would have.

All six money frames are checked against each other, since four sit in or near
the hook:

| | frame | denomination | crop |
|---|---|---|---|
| s1 (1.1) | singles on plank wood, dim | $1 ×4-5, worn | raking table shot |
| s2 (1.2) | fan of notes on pale stone | $100 ×4 | tight macro |
| s36 (4.6) | two notes flat, filling frame | $1 ×2 | flat 1:1 macro |
| s59 (6.7) | one banded roll on marble | one rolled note | small object, white field |
| s87 (9.5) | wide flatlay + coins | $100/$20/$10 + coins | wide, bright |
| s88 (9.6) | three jars of staples | none | top-down |

s1 and s36 share the $1 denomination — noted, accepted: 194 seconds apart, one a
dim raking table shot and one a flat macro of two note faces, and "a small amount
of money" is the correct read in both scenes.

## One thing seen in passing, not fixed (out of scope)

Watch items s22 / s71 / s64 / s24 / s48 from fin-build's log are untouched, as
instructed.

## Files

- `assets/img/s1.jpg` `s2.jpg` `s36.jpg` `s59.jpg` `s84.jpg` `s88.jpg` (+ their `.src` sidecars, rewritten by the tool)
- `assets/img/CREDITS.txt` — **93 lines, one per image, verified 1:1 against the 93 jpgs** by a sorted diff of filenames against column 1; the eight stale attribution lines left by the re-picks were deleted (the tool appends and never rewrites, so s2 alone had four)
- `assets/img/manifest.json` — s1 / s2 / s36 / s59 / s88 queries updated to what actually shipped; s84 unchanged (re-picked from its own sheet). 93 entries, unchanged count
- `assets/img/retry2.json`, `retry3.json`, `_cand/` — throwaway, safe to delete at cleanup
