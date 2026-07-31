---
summary: fin-storyboard, cut en, attempt 1 — 92-scene swiss-band storyboard ported from storyboard-hi.md with 15 declared divergences; 23 SFX cues on bed-resolve; 100 image slots / 93 files.
updated: 2026-07-31
stage: fin-storyboard · cut en · attempt 1 · STATUS ok
---

# fin-storyboard — en, attempt 1

## Inputs read
- `vault/CLAUDE.md`, `tools/format.json` (layout + scene + architectures constants)
- `vault/knowledge/design-finance-blockframe.md` (the dark system — the ONLY design doc for finance)
- `vault/knowledge/finance-audit-2026-07-29/11-swiss-vignelli.md` (D1 `.swiss-band` spec + §8 divergences)
- `vault/templates/storyboard-template-finance.md`
- `vault/videos/first-lakh-first-thousand/{run.json, script-en.md, storyboard-hi.md}`
- `studio/videos/first-lakh-first-thousand-en/assets/voice/timing.json` (measured, 505.561s, 92 lines)
- `studio/videos/first-lakh-first-thousand-hi/assets/img/manifest.json` (for cross-cut repeat avoidance)
- `tools/audio/kit.json`

## Outputs
- `vault/videos/first-lakh-first-thousand/storyboard-en.md`
- `studio/videos/first-lakh-first-thousand-en/assets/img/manifest.json` (93 queries)

## Decisions

**Architecture.** `swiss-band` per `run.json` (creator pick, differs from the
`architecture_lock: blockframe-9` default). The registry entry's `tier: short` /
`lines: 9` are SHORT-tier constants and do not apply at MEDIUM — scene count is
emergent: **92 scenes**, one per VO line.

**Colour semantics (§1).** Derived from this video's thesis, not copied. warn = the
stretch nobody helps you with; fund = the mechanism that works without you once it
exists; target = a rate/threshold under examination; pop = the CTA, once. The
load-bearing trap is restated: **green is NOT "returns doing the work"** — 5.10
exists to deny exactly that, so a green tenth-$10,000 module is fine but a green
"returns" module argues against the script. 17 warn / 15 fund / 10 target / 1 pop /
49 uncoloured.

**Audio.** One bed: `bed-resolve` (the argument is a habit/fix, not a trap/cost).
**23 SFX cues** — the hi cut's 22 plus one, because the BEA 2.7% beat (4.6) is the
strongest US-only HARD number and has no hi counterpart. Closest pair 2.84s (limit
0.8s). Dry beats declared per chapter; the **Munger block (5.7–5.9) is deliberately
dry** because the quote is colour, not evidence — 5.5 reaches ~$96,000 without it,
and punctuating an unsourceable folk attribution sells it as proof.

**Transitions.** 88 wipes (the `.swiss-band` 0.45s hard directional wipe occupying
the `dissolve` slot), **2 shoves** (s50→s51, the "not interest — the habit" turn;
s62→s63, into the fire-pit re-frame), 1 hold (s43→s44), 1 final.

**Cue classes.** The 5-item assembly (band → bar → rule → focal → foot) is declared
as a cascade at 0.15/0.40/0.15/0.40s — below the 0.8s floor, on purpose, with the
Unigrid reason stated. Every non-assembly content cue keeps ≥0.8s. Surplus clip time
goes into the post-assembly hold; the assembly always finishes at +1.50s.

**Images.** 100 slots (92 bg + 8 mosaic minors), **93 files**. The 7 query-free slots
are the one continuous-zoom hold (s44) and six mosaic-minor recalls of in-video files.
Densest scene s38 (4.8) keeps its already-calm empty highway; the one image changed at
this stage is **s78 (8.8)** — the script's "macro on the fine print" became a blank
rate-disclosure sheet in raking light, behind a 200px `0.38%`.

## Findings worth carrying forward

1. **The bed loop dip now lands on the CTA.** `bed-resolve` is 248s; at 505.561s the
   second loop point falls at ≈496s = the s90/s91 boundary, i.e. **on the single
   `--pop` frame in the video**. The hi cut's equivalent dip landed mid-recap. Same
   defect, strictly worse placement — `run.json owed_before_mix` should be widened to
   name the en timestamp too.
2. **Zero corrections needed to the script's `ap` column** — unlike the hi cut, which
   needed five aperture flips and two count fixes. The en script's 18 column scenes
   alternate cleanly from C-R and its prose counts match its table. Stated in §5 so
   the audit does not hunt for a defect that is not there.
3. **No `max_scene_seconds` ambiguity on this cut.** Longest scene is s69 at 8.140s →
   8.590s with the transition, so it passes whether `check_build` measures
   `scene_duration` or `data-duration`. The hi cut's s16 does not (9.191s as
   `data-duration`). Resolve that in `check_build`, but do not carve an exception here.
4. **Cross-cut image collision is the live risk on this pair**, not cross-video. 30+
   subjects overlap the hi cut. The manifest deliberately alternates provider against
   the hi cut on every overlapping subject (`@pexels` where hi used the pixabay
   default and vice versa), because Pixabay's top hit is deterministic. Mitigation,
   not a guarantee — fin-assets must md5 against the ledger including the hi cut.
5. **Left-third luminance measurement still does not exist**, and this cut has two
   `R` scenes over fire (s68 coal bed, s90 night fire) where "reversed type on a dark
   photograph" is least likely to hold. Both queries force a dark surround; the
   declared fallback is to demote either to `B` and ship 8 `R` scenes.

## Guardrail check
- one focal per scene (`stmt` XOR `num`) ✓ · kicker/bar first ✓
- cue spacing ≥0.8s except the declared assembly cascade ✓ (closest non-assembly pair 2.84s)
- ≤6 simultaneous elements ✓ (max 5 content + 2 furniture, furniture declared)
- something on screen by +0.5s ✓ (band opens at +0.00 in all 92 scenes)
- ≤3 chips/row at ≤22 chars ✓ **vacuously — `.swiss` bans chip rows; zero chips in this cut**
- `photo_free_scene_ratio` 0 ✓ — 92/92 scenes carry a photograph
- ken alternates by parity ✓ · track index alternates 1/2 ✓

## Owed / next
- fin-assets: fetch 93 files, md5 against the ledger **and against the hi cut**, measure
  left-third luminance on the 9 `R` scenes, write `.src` prompts + `CREDITS.txt`.
- Before mix: fix the `bed-resolve` loop (trim + crossfade, or a ≥520s bed re-normalised
  to −20 LUFS). Never `sfx.py --kit --music --force`.
- `scdet` on the hard wipe — measure once, apply to both cuts.
