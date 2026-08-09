---
summary: s29 only, attempt 2. Three more Pexels sheets (18 cells) against the editor's printed-handbill brief, zero passes; no third object substituted, slot escalated to the CEO per the editor's own stopping rule. The blocked horn-loudspeaker file is still on disk and the manifest/.src now say so.
updated: 2026-08-09
source: studio/videos/passive-income-number-hi-ch3/assets-ch3/final/_cand/s29.jpg (3 rounds), assets-ch3/final/s29.jpg.src, logs/editor-hi-ch3-1.md finding 2, storyboard-hi.md §Overrides + §10a
stage: fin-assets, cut hi, chapter 3, attempt 2
---

# fin-assets · passive-income-number · hi · chapter 3 · attempt 2 (s29 only)
VERDICT: FAIL — escalated, not substituted

## Ran

Scope was one slot. s22 (accepted at attempt 1 of this fix pass), s23–s28, s30 were not
touched: no fetch, no `--pick`, no manifest edit against any of them, and the eight other
credit rows are byte-unchanged.

1. Read `vault/CLAUDE.md`, `tools/format/fin-assets.json` `assets` + `layout.image_relevance`,
   the sourcing BOX, the editor log's finding 2, `assets-ch3/final/s29.jpg.src` (attempt 1's
   four killed sheets), storyboard §Overrides (s4, s52), §10a (the ch2 `s17` RJ45 kill),
   script line 3.8 and its `img:` cue.
2. Three contact sheets on s29, `--only s29 --candidates 6`, Pexels throughout
   (`assets.pick_width_px.pexels` 1880 ≥ `min_width_px` 1600; Pixabay's 1280 cannot clear the
   floor and s29 is a `dis`/reveal scene with a ken sweep). Six cells returned and six cells
   tiled on every round — counted, none short.
3. Restored `manifest.json` `s29.jpg` to the string describing the file actually on disk and
   appended the attempt-2 record; wrote the same text to `s29.jpg.src`.
4. `pipeline_check check assets --slug passive-income-number --cut hi --chapter 3` → `PASS assets-hi`.

No `--pick` was run, so nothing was fetched full-size and no image bytes changed anywhere.
The cross-project md5 sweep was therefore not run: it has no new hash to compare, and the
nine ch3 hashes were already swept clean at attempt 1 (editor confirmed nine unique).

## Failed

**All 18 cells. Query strings and the cell-by-cell kill list:**

| round | query (`@pexels`) | cells and why each dies |
|---|---|---|
| r1 | `stack of printed pamphlets on a dark wooden table` | 1,3,4 folded newspaper stacks · 5 an open book/binder · 6 a magazine pile on a stool · 2 a retail rack with legible `MOHICAN`, `LEHMAN'S`, `EXPLORE KENT`, `Cultivate Compdenty` brand covers. **Family verdict: newsprint is not the internet — it is the opposite pole from it**, the same sound-off failure as the horn speaker, plus a brand mark in the one cell with a large object. |
| r2 | `paper flyer with a large printed number on a table` | 1 hands passing leaflets, no numeral legible, hands banned outside s16/s70/s78 · 2 a **€100 flatlay** with a calculator (wrong currency in a ₹ cut) · 3 an **identifiable smiling woman** holding a `CONFIDENCE PROGRAM` brochure — banned outright as the subject of a negative money claim · 4 a fan of **bingo tickets** (gambling read, dense small numerals, still not online) · 5 a `LEADERS` magazine cover over a spreadsheet + reading glasses · 6 a bar chart reading **`SALES VOLUME DURING THE WEEK`** with a **phone in frame**. |
| r3 | `advertising leaflet with big number on a dark surface` | 1 a taped white sheet reading `22` · 2 a blank card on a hexagon, no mark at all · 3 a literal red **`SALE`** placard with a gift box — the exact vocabulary the brief forbids, returned by a query that never says "sale" · 4 an illegible dark blob · 5 paper strips with a legible **`SIGMA`** brand mark · 6 stencilled `614 307 584 3021` on tarmac (paint, not print). |

**r3 cell 1 is the only cell in 18 that satisfies the brief literally** — a printed page, one
large numeral, no other legible mark — and it still fails, on sound-off question 1: with the
type covered, no viewer names *the internet* from a taped page reading `22`. It also comes
back near-white, which is the wrong direction on the brightness constraint (see below).

**The bind, stated for the ruling.** Print can carry *online* by exactly one route: a
recognisable **search-results / webpage layout**. That is precisely why the storyboard's s52
brief works ("a printed search-results page on a desk, no phone screen and no monitor in
frame"), and s29 is explicitly forbidden from being a crop of, or confusable with, that frame.
Remove the layout and the print family collapses back to *newspaper · brochure · sale flyer ·
spreadsheet* — none of which names the internet, which is the defect the editor blocked in the
first place. The brief is not badly written; it is asking the pools for the one thing that is
left over after its own distinguishing feature has been ruled out. Seven sheets and ~42 cells
have now been spent on this slot across two attempts (four in attempt 1, three here).

Per the editor's stopping rule — *"If the pool refuses a third time, escalate rather than
substitute a third object"* — **no third object was substituted.** The horn loudspeakers stay
on disk as the known-blocked frame, not as an accepted one.

## Evidence

- Sheets (overwritten in place, r3 is what is on disk):
  `studio/videos/passive-income-number-hi-ch3/assets-ch3/final/_cand/s29.jpg` + `s29.json`
  (`_cand/s29.json` holds all six r3 candidates with page URLs and authors).
- `assets-ch3/final/s29.jpg` — **unchanged**, md5 unchanged, still Pexels 776153 (Jens Mahnke,
  `megaphone-speakers-on-wooden-post`). CREDITS.txt line 8 still keys that file; 9 rows for 9
  images, no orphan row and no uncredited image.
- `pipeline_check check assets --slug passive-income-number --cut hi --chapter 3` → `PASS assets-hi`
  (run **with** `--chapter 3`; without it the check reads a `-hi/assets/img/` that does not exist
  in this chapter-first run).
- **Brightness, as owed.** No new pick exists, so there is no predicted median/p10 to report.
  The relevant number for the CEO is the one already measured on the outgoing frame: the editor
  puts s29 at **p10 21.96, the chapter's highest, +2.22 clear of s30 and the only frame outside
  the 1.0-point tie band**. The chapter's *foil* is currently its most legible frame on p10 —
  the argumentative inversion the ground/payoff ruling exists to stop, and the same reason
  attempt 1's brighter cyan-sky horn variant (median 35.8 / p10 25.4) was rejected. Whatever
  replaces s29 should come in **below** 21.96 on p10, and the print family pushes the other way:
  white paper flatlays dominate every sheet above (r3 cells 1, 2, 5 are near-white grounds).
- Rules applied and their sources, so the next pass does not re-derive them: never-a-screen
  (storyboard §Overrides s4/s52) killed r2 cell 6 on the phone alone; the negative-money-claim
  licence rule killed r2 cell 3; wrong-currency killed r2 cell 2; readable brand marks killed
  r1 cell 2, r2 cell 5 and r3 cell 5.

## Changed

- `studio/videos/passive-income-number-hi-ch3/assets-ch3/final/manifest.json` — `s29.jpg`
  restored to the attempt-1 string (it had been set to each round's bare query, because the
  fetcher sends the whole manifest value as the query and does not split at `||`) and extended
  with the attempt-2 record: the three query strings, the 18 kills, the r3-cell-1 near-hit and
  the print↔s52 bind.
- `assets-ch3/final/s29.jpg.src` — same text, so the archived prompt record matches the manifest.
- `_cand/s29.jpg` / `_cand/s29.json` — overwritten by the three rounds. Throwaway, not shipped.
- **No image file was written, moved, renamed or deleted.** No `assets/lottie/` write. No git.

## Owed

- **A CEO ruling on line 3.8, and nothing else on this slot.** The collision is the cut's
  never-a-screen rule against the creator's standing sound-off rule; the editor already ranked
  the sound-off rule senior. Three exits, cheapest first:
  1. **Grant s29 the s52 exception it was denied** — a printed webpage/search-results page,
     accepting visual kinship with s52 but at a different scale and framing (s52 is briefed as
     a page *on a desk* with a ringed figure; s29 could be a mass of identical printed sheets).
     Kinship 250 scenes apart is a much smaller defect than a frame that drops its subject.
  2. **Draw it** — `vector_art.lottie.reach_for_it_when` covers "a fact being amplified"; the
     chapter currently spends 1 of its 4 drawn layers (the editor's finding 3 already proposes
     a 2nd for s24, so this would be the 3rd). A drawn beat is the only option that can say
     *online* with no photograph and no screen at all.
  3. **Relax never-a-screen for this one line** — a dark, off, non-brand device is already
     APPROVED elsewhere in this cut (s1/s4/s74/s75 ship a black-screen phone). An off screen
     under "what the internet does" is a weaker read than 1 or 2, and it is listed last for that
     reason.
- Whichever exit is chosen, the fetch brief inherits the brightness constraint above (target
  p10 below 21.96) and the four vocabulary bans that killed attempt 1.
- Not owed by me, recorded so it is not rediscovered: the editor's findings 3 (a 2nd drawn layer
  for s24), 4 (s77 carries the stamp's missing third state) and 6 (ch4's s32/s33 must be paper)
  are unaddressed here by scope.
