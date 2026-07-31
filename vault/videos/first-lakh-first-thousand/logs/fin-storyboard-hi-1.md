# fin-storyboard · hi · attempt 1

**Date:** 2026-07-31 · **Slug:** first-lakh-first-thousand · **Tier:** medium ·
**Architecture:** `swiss-band` (run.json creator pick 2026-07-31, differs from the
`architecture_lock` blockframe-9) · **Status:** ok

## Read
`vault/CLAUDE.md` · `tools/format.json` · `tools/audio/kit.json` ·
`vault/knowledge/design-finance-blockframe.md` (the dark finance system — NOT
design-techtooltester) · `vault/knowledge/finance-audit-2026-07-29/11-swiss-vignelli.md`
(Direction 1 spec + the §8 divergence list) · `vault/templates/storyboard-template-finance.md` ·
`vault/videos/first-lakh-first-thousand/{run.json,script-hi.md}` ·
`studio/videos/first-lakh-first-thousand-hi/assets/voice/timing.json` (present, measured,
514.789s — no timing was estimated).

## Wrote
- `vault/videos/first-lakh-first-thousand/storyboard-hi.md`
- `studio/videos/first-lakh-first-thousand-hi/assets/img/manifest.json` (87 entries)

## Decisions
- **Colour semantics** derived from the thesis, four lines, with the explicit trap
  recorded: `--fund` green marks *the viewer's own mechanism*, not "returns doing the
  work" — reading it as returns makes the palette argue against 5.9, the scene that exists
  to deny returns take over at the first lakh. `--tint` is retired (Swiss: pictorial colour).
- **Cue ladder is canonical, not per-scene.** All 86 scenes assemble identically
  (band iris → bar → rule → focal → foot); absolute times derive as `scene_start + offset`
  with `scene_start` verbatim from timing.json. Restating 344 cue rows would have created a
  second home for the timing.
- **The assembly runs at 0.15–0.40s gaps, below `cue_min_gap_seconds` 0.8 and below
  `cascade.gap_seconds` 0.6–0.7.** Declared as a cascade ("the assembly", 5 items = exactly
  `cascade.max_items`) with its reason, so the audit reads it as a decision. Every non-assembly
  content cue keeps ≥0.8s; closest such pair in the cut is 2.40s.
- **15 `num` scenes take an anchored arrival instead of the fixed +0.70 hang** — a figure on
  screen 4.5s before the voice says it spoils the hook.
- **Transitions:** 83 `wipe` (the `.swiss-band` rendering of `dissolve`, same 0.45s), **2
  `SHOVE`** (5.8→5.9, the "not interest — the habit" turn; 6.10→7.1, into the ~70%
  re-frame), 3 `hold` (matched-frame boundaries inside the continuous-zoom pairs), 1 final.
  `hold` keeps `data-duration = scene_duration + 0.45` on every non-final scene, so the
  blockframe §5 rule-0 assert needs no exception.
- **Audio:** one bed, `bed-resolve` (the argument is a habit/fix, not a trap/cost).
  **22 SFX cues in 8:35** — the kit's ≤10 is a SHORT figure; scaling by runtime would give
  ~57, which is the "none of them means anything" failure. Dry beats declared: all of ch4
  except 4.6, all of ch6 except 6.6, 7.1–7.5, and the whole 9.5–9.7 recap.
- **Images:** 93 slots (86 bg + 7 mosaic minors) from 87 fetched files. Cut-ins live in the
  mosaic **minor rectangle**, not as floating overlays — a floating cut-in dissolves the
  edge, and in this architecture the edge is the design. Densest scene (s37 / 4.10) had its
  script image swapped from "a wall of rate boards" to a weathered painted board texture.

## Findings handed forward
1. **`bed-resolve` is 248s against a 514.789s cut.** `mix.py` stream-loops and the bed fades
   to silence at both ends, so audible dips land at ≈248s (s42, the crossover figure) and
   ≈496s (s83, recap three). Trim + crossfade the loop, or source a ≥520s bed and re-normalise
   to −20 LUFS. Never `sfx.py --kit --music --force` — it destroys the creator-supplied beds.
2. **The script broke its own C-L/C-R alternation twice** (4.9→5.6 and 7.3→8.2). Re-derived
   strictly; five scenes flip: 5.6→C-R, 6.3→C-L, 6.8→C-R, 7.3→C-L, 8.2→C-R.
3. **Two script prose/table count mismatches**: "exactly 9" reversed-field scenes vs 10 in the
   table; "the 8 scenes" mosaic vs 7 listed. Table taken as authoritative (10 R, 7 M).
4. **1.1+1.2 is an 11.736s single-photo pair** — the script's build handoff flagged only
   5.2+5.3. Both are per-scene compliant (max 8.741s), but the ken tween must be phase-matched
   across the `hold` boundary or it flickers.
5. **`check_build` risk:** if `max_scene_seconds` is measured against `data-duration` rather
   than `scene_duration`, s16 reads 9.191s and fails. Fix the check, not a measured clip.
6. **The hard wipe is unproven against `ffmpeg scdet`** — measure chapter 1's master before
   locking chapters 2–9; fallback is `dissolve` at the same 0.45s.
7. **Word-level anchoring not yet wired** — the `f` fractions are fallbacks; run faster-whisper.
8. **Repeat-risk clusters inside this cut** for the md5 ledger: four water tanks (s42/s58/s63/s84),
   four coin jars (s1/s13m/s21/s81), two roadside stone markers (s43/s86).
