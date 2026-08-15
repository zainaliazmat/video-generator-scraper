# fin-assets · financial-freedom-after-50 · en · chapter 2 · attempt 2
STATUS: ok — 3 slots re-picked (s15, s16, s22), 15 kept, 0 dropped

## Ran
- Read `logs/review-en-ch2-1.md`, `vault/CLAUDE.md`, `tools/packs/fin-assets.md`,
  `tools/format/fin-assets.json` (`assets`, `layout`, `vector_art`), the script lines
  2.3–2.5 / 2.11 and `storyboard-en.md` rows s14–s16, s22.
- 6 contact sheets, `--only`, `--candidates 6`: s15 ×3 queries, s16 ×3, s22 ×5.
  One vision pass per sheet, then a full-resolution read of every promoted file.
- `--pick "s15=1,s16=4,s22=6"` then `--pick "s22=4" --force` (first snow-roller cell
  replaced by a better one from a later sheet).
- md5 dedupe across both channels (`find studio/videos vault/videos …| uniq -Dw32`).
- `tools/image_sheet.py … --chapter 2` rebuilt and read (18/18 cells).
- `pipeline_check check assets --slug financial-freedom-after-50 --cut en --chapter 2`.
- No lottie: the storyboard asks for none in ch2 and the s18 icon (inline svg) is
  reviewer-protected. `assets/lottie/` untouched.

## Failed
- **A leaking BUCKET is not sourceable.** 4 sheets / 24 cells, three phrasings on
  Pexels (`water pouring out of a metal bucket`, `water leaking through a hole in a
  rusty bucket`, `water leaking out of a bucket`) plus the earlier `water swirling
  down a drain`. What the pools hold for those words: people emptying buckets into
  rice paddies (non-US, faces), a B&W man bathing, an `ADIDAS` bib on a water-dousing
  crowd (brand mark), rust holes in ship plate with no water at all. Zero cells with
  water leaving a pail. Pixabay was not used for it: `assets.pick_width_px.pixabay`
  1280 < `assets.min_width_px` 1600 and every ch2 slot is a full-bleed ken.
- **Neither stock pool has a snowball with a track.** 4 Pexels sheets (`snowman…`,
  `snowball rolling down a snow covered hill trail`, `rolling a giant snowball…`,
  `rolling snowball`, `giant ball of snow in a snowy field`) = 24 cells of snowball
  fights, hands holding snow, empty landscapes, a dog with a beach ball and a
  Christmas bauble. The ladder's `@commons` rung solved it in two queries.
- Sheet loss, twice, as the pack warns: `two brass garden taps` tiled 4/6 and the
  first `snow roller@commons` sheet tiled 2/6 (upload.wikimedia rate-limiting).
  Both times `_cand/<slot>.json` held all six; cells 1–4 of the commons sheet were
  Köppen climate maps, so nothing usable was hidden by the loss.

## Evidence
Promoted, full-resolution read of each (`assets-ch2/final/`):

| slot | file | source | what it now says sound-off |
|---|---|---|---|
| s15 | 5472×3648, 372,102 b | pexels 4406597, eberhard grossgasteiger | a rusted pipe leaking a **curtain of drips** into a bright green meadow — water *escaping* through the pipe, in daylight colour. Replaces the B&W storm-drain puddle (water *arriving*) |
| s16 | 6240×4160, 111,971 b | pexels 2339722, Luis Quintero | a brass tap with **three drops falling**, hot orange bokeh behind. Replaces the monochrome brick/two-taps wall (supplied *two*, never *leak*) |
| s22 | commons `Snow_Roller_in_Rocky_Mountain_National_Park.jpg`, Perduejn, **CC BY-SA 4.0** | @commons | a snow roller mid-slope with a **long track running back up the hill**, more rollers and tracks in the mid-ground, low sun, pines. Replaces the snowman. US location, as the storyboard's "US winter landscape" asked |

- **P1-5, the 19-second dead run, measured by eye at 1:1:** s14 is *not* monochrome —
  warm browns, galvanized pail, wood — so per the brief it was kept (its fix is the
  build's ken re-frame onto the bucket). s15 and s16 were the two monochrome sources
  and both are now colour: s15 green/rust, s16 orange/brass. The run reads
  brown → green → orange instead of brown → grey → grey. `grayscale(.32)` now has
  saturation to take from all three.
- **Legible text inside the photographs** (the read the sheet cannot do): s15 clean
  bar a sub-pixel photographer watermark in the bottom-left corner, buried by any
  crop; s16 carries a cast `V79-11` on the tap body — a foundry mark, not a brand;
  s22 clean. Also re-read the two frames whose thumbnails showed type, though neither
  was in my brief: **s17** shows `012 324` embossed on a card with **no issuer logo**
  in frame (clean), **s25** is a genuine US $50, one serial visible (`MG 55325144 A`),
  so no repeated-serial prop-money tell.
- **md5 dedupe: empty output** — no collision anywhere on either channel. (The `find`
  form; the old glob form would have read zero files for this chapter layout.)
- **Promoted sheet `IMAGES-ch2.jpg`, 18/18 cells, adjacency read:** no two cells say
  the same thing. The new s15/s16 pair is the only near-echo — both are water leaving
  plumbing — but they differ in colour (green vs orange), scale (wide vs macro) and
  object (pipe vs tap), and s14–s16 is a *declared* same-object run where the rule is
  a visibly different state, not a different noun. s23b (night rain off a roof edge,
  dark, 8 scenes later) does not collide with s15's sunlit meadow. s20 (white
  envelopes, coins, calculator on marble) and s25 (cash stack in a kraft envelope)
  stay distinct.
- `pipeline_check check assets --chapter 2`: **PASS assets-en** — every slot present,
  over `min_image_bytes` 10240, over `min_source_yhigh` 110, over `min_width_px` 1600,
  and every rendered image carries its attribution.
- CREDITS.txt: **18 rows for 18 images**, one per slot — the tool re-keyed s15/s16/s22
  rather than appending, so no stale attribution survives. s22's row is a **licence
  condition** (CC BY-SA 4.0), not a courtesy.

## Changed
- `studio/videos/financial-freedom-after-50-en-ch2/assets-ch2/final/`:
  `s15.jpg`, `s16.jpg`, `s22.jpg` (+ their `.src` sidecars and CREDITS rows),
  `manifest.json` (three queries; `_note` corrected — the s14–s16 run is now the LEAK
  run, not the bucket run, and s22 is the chapter's one @commons file),
  `IMAGES-ch2.jpg` / `.json` rebuilt.
- Untouched, deliberately: s23/s23b and s18 (reviewer-protected), s14 (colour at
  source; its fix is the ken), s28 (grade, build fix), s17 (cue order, build fix),
  and the should-fix slots s21/s24/s25, which were not in this brief.

## Owed
- **The bucket metaphor is still dropped after s14, and that is now a deliberate,
  sourced decision, not an oversight.** The reviewer's first choice (a pail leaking
  from a hole) does not exist in any pool; their fallback (re-frame s14 tight on its
  base and draw the leak in the D plate) keeps two dim frames in the run and so
  fights P1-5, which the brief called the reason the other two matter. I took the
  third path: keep the *leak* legible and put colour and light back. `stmt: Pouring
  faster does not fix a leak.` reads correctly over a leaking pipe; `head: TWO HOLES`
  does not name the bucket either. **If fin-ceo wants the bucket carried through,
  the only honest route left is drawn art over s14/s15 — a fetch will not do it.**
- s16's picture supplies *leak* but not *two*; the two chips carry the count, as the
  reviewer already ruled acceptable (round-1 row 9).
- Still open from round 1 and not mine: s17 cue order, s28 grade/ken, s21 roll-down
  arrow, s25 3-of-6 count, s24 statement frame.
