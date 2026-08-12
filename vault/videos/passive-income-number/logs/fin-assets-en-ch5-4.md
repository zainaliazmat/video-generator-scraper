# fin-assets — passive-income-number — en — ch5 — attempt 4

Executing the asset half (b) of
`rulings_binding_on_both_cuts.s61_ratio_becomes_a_drawn_device_over_a_consenting_photograph_2026-08-12`.
No search was run. One slot touched: **s61**.

## Ran
- Recovered attempt 3's verified candidate record from the session scratchpad
  (`…/scratchpad/probe17/_cand/ue.json`, query
  `four eggs in a bowl and one egg beside it on a dark table@pexels`, provider pexels,
  6 cells) and seeded it as this chapter's `_cand/s61.json` with `slot` re-keyed to
  `s61.jpg`. The crate sheet it replaced is kept beside it as `_cand/s61.json.crate-bak`.
  **This is why no API search was needed**: `cmd_pick` reads only `_cand/<slot>.json`,
  never the manifest, so the recorded full-res URL of cell 3 is promotable directly.
  Zero contact sheets built, zero searches spent on s61.
- `python3 tools/stock/pixabay_fetch.py --manifest …/assets-ch5/final/manifest.json --pick "s61=3"`
- Full-resolution `Read` of the promoted `s61.jpg` (mandatory, per the two
  first-lakh-first-thousand rules — a contact-sheet cell cannot show legible text).
- `find studio/videos vault/videos \( -path '*/final/*.jpg' -o -path '*/assets/img/*.jpg' \) -print0 | xargs -0 md5sum | sort | uniq -Dw32`
- `python3 tools/image_sheet.py passive-income-number --cut en --chapter 5` + `Read` of the sheet.
- `python3 tools/pipeline_check.py check assets --slug passive-income-number --cut en --chapter 5`

## Failed
- `check assets` failed **once, correctly**, before the sheet was rebuilt:
  `✗ IMAGES-ch5.jpg is older than the newest promoted image — it shows the picks BEFORE
  the last change.` The staleness guard did exactly its job; rebuilding the sheet cleared it.
- Nothing else failed. No rejected cells this attempt — there was nothing to reject,
  because the acceptance work was done in attempt 3 and the ruling picked from it.

## Evidence
**The promoted image**
- `s61.jpg` ← cell 3, `https://www.pexels.com/photo/white-raw-eggs-in-bowl-on-table-4488336/`,
  Mateusz Dach, Pexels License. 167,875 b.
- `identify`: **1880×1253** — identical to the chapter norm (s62 1880×1253, s60 1880×1255;
  15 fetched files at 1880 wide, the two derived crops at 1600×900). Clears
  `assets.min_width_px` 1600 and matches `assets.pick_width_px.pexels` 1880 exactly.
  `min_image_bytes` 10240 cleared by 16×.
- `min_source_yhigh` ≥ 110 cleared — asserted by the passing `check assets`, not by eye:
  the bowl's white ceramic is a large specular-lit highlight field, so the locked
  grayscale .32 / brightness .62 grade has something to leave behind. No per-scene
  `filter:` override needed or set; the chapter's one-override budget stays unspent.

**Full-resolution read (the look a grid cell cannot give)**
- Top-down white ceramic bowl on dark wood. **Five eggs**, not four: four ringing the
  bowl (one white top, one pale left, one tan-brown right, one white bottom) with a
  fifth white egg resting on top of them at centre. This matters and is *better* than
  the ruling's own description assumed — the drawn device is **five identical marks,
  four grouped and one apart**, so the photograph now carries the same cardinality as
  the drawing rather than merely failing to contradict it.
- **No competing count is asserted.** Unlike the 14-crate wall, this frame states no
  multiple at all: five like objects, ungrouped. That is the exact property half (b)
  requires — the drawing supplies the separation, the photograph supplies nothing that
  argues with it.
- Trap list, at full resolution: no text of any kind, no brand mark, no logo, no
  packaging, no currency, no chart, no face, no person, no phone screen, no
  reproduction/prop-money concern. Currency-neutral by construction, so the
  wrong-currency failure mode cannot reach this slot.
- Composition note for `fin-build` (not a defect, an affordance): the subject is a
  centred circle occupying the middle ~55% of frame width; the dark wood runs clean
  down both edges (≈ left 0–25% and right 78–100% of width). The drawn marks have
  unbusy ground on either side without overlapping the eggs.

**Ledger / attribution**
- md5 dedupe across BOTH channels and both directory layouts: **empty output — no
  collision.** (`find` form, so `assets-ch<N>/final/` is actually walked; the old
  `md5sum studio/videos/*/assets/img/*.jpg` glob would have read zero files here.)
- `CREDITS.txt`: **18 rows for 18 files.** The crate row (`…/wooden-boxes-by-wall-19746290/`,
  Gene Samit) was *replaced*, not appended — the fix to `write_credit` re-keyed the slot
  cleanly and **no hand repair was needed**. The newline-in-Commons-author bug I
  diagnosed on this chapter did not recur: the one Commons row (s55, Ryan Schwark, CC0)
  survived the rewrite intact on a single line and was not stranded.
  Row/file counts are 18, not the 16 named in the task — 16 fetched slots plus the two
  derived crops s56b/s67b, each of which correctly carries its parent's attribution.
- `.src` sidecar rewritten by the tool:
  `four eggs in a bowl and one egg beside it on a dark table@pexels`.
- `manifest.json` s61 re-keyed to the same query, so manifest, `.src` and CREDITS agree
  and `check assets` sees the licence assertion for what `index.html` renders.

**Chapter sheet — the repetition question**
- `IMAGES-ch5.jpg` rebuilt: **18 cells, all present**, HOLDs correctly labelled
  (`s56b (HOLD crop of s56)`, `s67b (HOLD crop of s67)`) and not counted as repeats.
- The adjacency named in the task, checked: **s60 → s61 → s62 does not collide.**
  s60 is a high-key flatlay on WHITE ground (spiral notebook, two brown envelopes, pen);
  s61 is a low-key top-down on DARK wood with a single centred white circle; s62 is a
  macro of orange numerals on black. Opposite tonality on either side, three different
  object families. The only shared property s60/s61 have is the overhead camera, and
  ground, subject and palette all separate them.
- The kitchen/food object does not echo anything else in ch5: the chapter's other
  interiors are industrial (s57 bucket, s58 control knobs, s59 warehouse, s63 storage
  corridor) and its other domestic frames are exteriors (s66, s67/s67b). No second food
  or kitchen image exists in the chapter.
- s61 no longer rhymes with s59's warehouse pallets — a small gain, since the departing
  crate wall and s59 were the chapter's nearest-neighbour pair.

## Changed
Exactly one slot, in `studio/videos/passive-income-number-en-ch5/assets-ch5/final/`:
- `s61.jpg` — 14-crate wall (Gene Samit) **replaced** by the five-eggs-in-a-bowl frame
  (Mateusz Dach), 1880×1253.
- `s61.jpg.src` — rewritten by the tool to the egg query.
- `manifest.json` — s61's query re-keyed to match.
- `CREDITS.txt` — s61's row re-keyed to the new page/author (crate row gone, 18/18).
- `IMAGES-ch5.jpg` / `IMAGES-ch5.json` — rebuilt.
- `_cand/s61.json` — now the egg candidate record; the crate one preserved as
  `_cand/s61.json.crate-bak` (both throwaway, not shipped, not in the manifest).

**Not touched:** s53–s60, s62–s68 and the derived crops s56b/s67b — built, drafted and
reviewed. No file in ch1–ch4 or ch6 was read for write or modified. No `.env`, no
`tools/`, no `.claude/`, no git.

## Owed
1. **`fin-build` owes half (a):** the minimal drawn device over s61 — five identical
   marks, four grouped and one apart, decorative level, **no scale, no ticks, no
   numerals, no axis** (it states a COUNT, never a magnitude; it is not the §9a measure
   bar). en only — `container_ladder_2026-08-09` forbids porting it to hi. The frame's
   clean ground is the dark wood at both edges; the bowl occupies the centre ~55%.
2. **TEXT CORRECTION, to be made in §10 and not worked around** (re-stating my attempt-3
   finding, now load-bearing): §10 claims a three-beat crate rhyme `s61 → s75/s76 → s77`.
   It was **already one-legged before this attempt** — ch6's s77 shipped as *"large steel
   shipping container standing alone in an empty yard"*, not a crate. With s61 leaving
   the crate family the rhyme is **`s75/s76` only**, and §10 should say so.
   ⚠ No chapter is to "restore" the rhyme by re-fetching toward the description. The
   description is what is wrong; the disk is right. Precedent:
   `container_ladder_CORRECTION_2026-08-09`.
3. ch5 needs a re-build + re-draft for the swapped background and the new drawn layer;
   the rest of the chapter's images are unchanged, so nothing else is re-reviewable.

OPENED-BODY: none.
