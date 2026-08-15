---
summary: fin-assets chapter 1 (s1–s11, VO 1.1–1.11) for financial-freedom-after-50 -en. 11 of 11 background slots promoted from Pexels at 1880 px, all ≥ YHIGH 110, zero md5 collisions, `pipeline_check check assets --chapter 1` PASS. Two hard defects were caught only at full resolution (a Cyrillic keyboard + Cyrillic utility bill on the hook, an Italian no-parking sign on the 9.5 s hero scene) and one repetition pair was caught only on the promoted sheet.
updated: 2026-08-15
source: studio/videos/financial-freedom-after-50-en-ch1/assets-ch1/final/ · storyboard-en.md §9 · script-en.md ch1 · tools/format/fin-assets.json · tools/packs/fin-assets.md
stage: fin-assets, cut en, chapter 1, attempt 1
---

# fin-assets — en, chapter 1, attempt 1

## Ran

- Read `vault/CLAUDE.md`, `tools/packs/fin-assets.md`, `tools/format/fin-assets.json`,
  `storyboard-en.md` §6/§9/§10, `script-en.md` chapter 1 (lines 1.1–1.11 = scenes s1–s11).
- Created the chapter project `studio/videos/financial-freedom-after-50-en-ch1/assets-ch1/final/`
  and wrote its `manifest.json` (11 bg slots, no cut-ins in ch1 — the three cut-ins are s23b,
  s67b, s80b, all in later chapters).
- 23 Pexels searches (`--candidates 6`), 11 contact sheets read + 12 re-query sheets read,
  16 full-resolution `Read`s of promoted or trial images, 2 promoted-chapter sheets read.
- `--pick` promotions, cross-project md5 dedupe (twice), `tools/image_sheet.py --chapter 1`
  (twice), `pipeline_check check assets --slug financial-freedom-after-50 --cut en --chapter 1`.
- Pixabay calls: **0**. Every slot is `@pexels`, because `assets.pick_width_px.pexels` 1880
  clears `assets.min_width_px` 1600 and Pixabay's 1280 does not — and all 123 scenes in this cut
  are full-bleed `.bg` (storyboard §9), so every slot is a "long full-bleed zoom" slot.

## Failed

Nothing blocking. Rejections, all replaced (no slot was dropped — `photo_free_scene_ratio` = 0):

**Caught ONLY at full resolution (invisible at contact-sheet size):**

| slot | rejected candidate | why |
|---|---|---|
| s1 | sheet cell 3 (`.../photo/...-5757219`-shoot, older man top-down with laptop + document) | **Cyrillic keyboard (ЙЦУКЕН layout) and a Cyrillic utility bill with barcode/QR in his hands.** Unmistakably not American — the exact defect class `script-en.md` "Photography rule" names. Cells 1 and 6 are the same shoot and are rejected with it. |
| s8 | park sheet cell 1 (older couple, tree-lined avenue) | **Italian road sign in frame** — blue/red circular no-waiting plate with "…eccetto…" legible. Non-US signage. |
| s8 | beach sheet cell 6 (elderly couple, wide beach) | thatch parasols + karst bay + carried sun umbrellas read as a South-East Asian resort. Place-wrong for a US cut; a neutral frame beats a foreign-reading one. |
| s7 | steering-wheel cell 1 / cell 4 | **Hyundai and Jeep hub emblems, large and dead-centre.** Readable brand marks. |
| s7 | steering-wheel cell 6 | **YHIGH 67 < 110.** The only logo-free wheel in the set had no highlights; direction abandoned rather than settled. |

**Caught on the candidate sheet (whole sheets failed 6/6):**

- `s10` first sheet (`row of wooden blocks on table`): five of six cells were **lettered** blocks —
  `NEW`, `OLD`, `STOCK`, `JOURNEY`, alphabet cubes. Storyboard §9: "Nothing on screen is lettered
  by the photograph." The sixth was a domino line, which *argues* with the line (dominoes = collapse
  under "3 Protect · 4 Income · 5 Transition").
- `s3` retry `blank cards in a row on dark wooden table`: 6/6 fail — legible `ACT 2` card, a phone in
  frame, and high-key 4-card grids on pale plywood.
- `s3` retry `stepping stones path across water`: 6/6 fail — Japanese/Chinese garden, one cell with a
  **giant golden Buddha**, one with a queue of tourists. Place-wrong.
- `s7` retry `hands on wooden ship helm`: rejected — branded crew polos in 4 cells, and the one clean
  cell imports a nautical register nothing else in the chapter carries.
- Individual cells rejected across the other sheets: Turkish newspapers + a `DAILY SABAH` masthead
  (s6), a legible `£1million` line (s6), an iPhone + `BURGLARY SHOCK` tabloid (s6), a **€50 note**
  and two `LEADERS` mastheads (s2), a sticker-covered laptop and a blown-white laptop screen (s2 —
  also the "brightest thing in frame is a screen" trap), an Adidas jersey on a ~30-year-old (s2), a
  suited man at a desk reading as *financial advisor* (s1 — `no_advice_framing`), a 25-year-old at a
  kitchen table (s1), Scandinavian/British/Hungarian streetscapes (s4), a Cyrillic café A-board (s11).

**Caught ONLY on the promoted sheet (`IMAGES-ch1.jpg`, round 1):** s3 and s7 both read as
*white ruled paper, flat top-down, on brown wood*. Neither is wrong alone; side by side they are the
sameness defect. Fixed by re-picking s7 to an angled, window-lit framing (cell 5 instead of cell 1),
which the round-2 sheet confirms.

## Evidence

Promoted, `studio/videos/financial-freedom-after-50-en-ch1/assets-ch1/final/`:

| slot | line | what the frame shows (sound-off) | px | YHIGH | bytes |
|---|---|---|---|---|---|
| s1 | 1.1 "over fifty… ship has sailed?" | man ~60 at a wooden table with laptop, notebook, lamp | 1880×1253 | 222 | 225,726 |
| s2 | 1.2 "sinking feeling" | reading glasses set down on a chart report, dark stone table | 1880×1253 | 243 | 112,636 |
| s3 | 1.3 "five-step game plan" | fan of **blank** ruled index cards on dark walnut | 1880×1253 | 209 | 192,187 |
| s4 | 1.4 "you are not alone" | US suburb at sunrise — brick ranch houses, white split-rail fence, 25 mph sign, snowy range | 1880×1246 | 202 | 542,724 |
| s5 | 1.5 "a few moves, in the right order" | hand moving a chess piece on a reflective board | 1880×1253 | 195 | 186,401 |
| s6 | 1.6 "no magic bullet / Wall St wizard" | newspaper **BUSINESS** section + coffee cup | 1880×1253 | 240 | 93,432 |
| s7 | 1.7 "take back control… a system" | open **blank** notebook + pen, angled, window light | 1880×1251 | 216 | 103,680 |
| s8 | 1.8 "people in their fifties and sixties… building futures" | grey-haired couple from behind, poles, walking up a misty trail | 1880×1255 | 228 | 276,597 |
| s9 | 1.9 "steps one and two" | broad wooden steps against warm brick, raking light | 1880×1253 | 124 | 429,612 |
| s10 | 1.10 "three, four, five" | stone stairway climbing to light | 1880×1250 | 203 | 560,842 |
| s11 | 1.11 "start building… right now" | hand pulling an old wooden door open | 1880×1253 | 129 | 259,275 |

- **Every image 1880 px wide** = `assets.pick_width_px.pexels`, ≥ `assets.min_width_px` 1600.
  s8 is the two-framing scene (§5, 9.473 s) — the couple sits centred in a receding path, so the
  wide→push works without a new slot. No upscale anywhere.
- **YHIGH floor `assets.min_source_yhigh` 110**: min measured 124 (s9), max 243 (s2). The one
  candidate that failed it (s7 steering wheel, 67) was rejected on that number, not by eye.
- **min_image_bytes 10240**: min measured 93,432 (s6), 9× the floor.
- **md5 dedupe, run exactly as specified**, after the initial promotion and again after the
  s1/s3/s7/s8 re-picks: `uniq -Dw32` empty both times, 22 files walked. (Note for the pack: the two
  `-path` filters do **not** exclude `_cand/` — `find`'s `*` matches `/`, so `*/final/*.jpg` also
  matches `assets-ch1/final/_cand/s1.jpg`. Harmless here — sheets are unique JPEGs and no collision
  was reported — but the claim in the agent prompt that the filters keep `_cand/` out is wrong.)
- **`pipeline_check check assets --slug financial-freedom-after-50 --cut en --chapter 1` → `PASS assets-en`.**
- `CREDITS.txt` carries 11 rows, one per promoted file, all `Pexels License` (no attribution
  condition, but the rows ship anyway). 11 `.src` sidecars written. No image was placed by hand, so
  no credit row had to be re-keyed.
- **Deliberate, not a repeat:** s9 and s10 are both stairs. They are adjacent and progressive —
  s9 carries the chips `1 Stabilize · 2 Maximize`, s10 carries `3 Protect · 4 Income · 5 Transition`
  — and they are tonally opposite (warm brick, side-on, close vs cold monochrome, head-on, ascending
  to light). They are not labelled HOLD because the storyboard marks both `trans: dis`.
- **Full-resolution text sweep, per image:** no currency of any kind in any of the 11; no payment
  card, terminal, credit mark or institution logo; no phone screen used as a background. Two
  sub-pixel-at-1080p marks noted and accepted: the pen barrel in s7 reads `Made in Germany` + a
  barcode (~2% of frame height at 1880 px, ≈4 px at 1080p), and s6's newspaper shows the section
  head `BUSINESS` and a partly legible `Richest Fa…` headline — a section head is inherent to the
  object and supports the line; no masthead is visible.

## Changed

- **New:** `studio/videos/financial-freedom-after-50-en-ch1/assets-ch1/final/` — `manifest.json`
  (11 slots), `s1.jpg`–`s11.jpg`, `CREDITS.txt`, 11 `*.src`, `IMAGES-ch1.jpg` + `.json`,
  throwaway `_cand/`.
- **Queries rewritten.** The cut-wide `studio/videos/financial-freedom-after-50-en/assets/img/manifest.json`
  holds *prose art direction* ("a man in his early sixties at a US kitchen table in low morning window
  light, a paper bank statement face-up…"), not stock queries. Pixabay caps `q` at 100 chars and both
  pools score the whole phrase, so those strings return nothing. The chapter manifest carries the
  searchable form of each, with the storyboard's intent preserved where the pool could serve it.
  Where it could not, the object was changed rather than faked (storyboard §9's own rule):
  - s5 "hand placing the third of five cards" → **chess piece being moved** (the pool has no
    partial-row-of-five; chess states *a move, in order* and adds no lettering risk).
  - s9 / s10 "cards two-of-five / row of five complete" → **steps** (the lettered-block pool is
    unusable; stairs state a step list without a photograph having to letter it).
  - s11 "hand squaring up the row of five cards" → **hand opening a door** (START HERE / Step one).
  - The five-index-card motif therefore appears once, at s3, where the promise is made.
- Nothing else touched. No `.env` read, no `.claude/` or `tools/` write, no git.

## Owed

1. **Chapters 2–7 will hit the same manifest problem.** The cut-wide manifest's remaining 115 slots
   are prose prompts, not queries; each chapter's fin-assets must rewrite its slice the same way.
   It was left unmodified on purpose — it is the storyboard's art-direction record and the "write the
   LIGHT" brief for the slots not yet fetched.
2. **The nine `source-shot` scenes are not this stage's output and none is in ch1** (s36, s37, s39,
   s44, s50, s62, s83, s85, s101 — storyboard §9). s83/s85 need a network path that actually reaches
   `ssa.gov`; every pipeline fetch has returned 403.
3. **s10 is a monochrome original.** It passes YHIGH 203 and reads correctly, but it is the only
   desaturated frame in the chapter; if `fin-editor` finds it fights the `--f1` temperature ladder
   (§10), re-pick `s10=4` from `_cand/s10.json` (dark modern staircase with a light shaft, same
   query) — no new API call needed.
4. **No Lottie was sourced.** Storyboard §8 declares **0 Lotties** for this cut (6 drawn layers +
   2 icons), so `assets/lottie/` was neither read nor written.
5. `run.json.budget.pixabay_calls` is still 0 and remains accurate for Pixabay; 23 **Pexels**
   searches were spent on this chapter. There is no `pexels_calls` key to increment.
