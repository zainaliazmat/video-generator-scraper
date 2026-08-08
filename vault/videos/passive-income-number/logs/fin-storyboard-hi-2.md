---
summary: fin-storyboard hi attempt 2 — full rebuild of the hi storyboard for the style-E restyle on the measured 519.331s Amrut timing. 81 scenes, 87 image slots, 12 photographs reused verbatim from the superseded build, four two-framing breaches resolved, the run's VO-only rate blind spot closed at 6.8.
updated: 2026-08-08
stage: fin-storyboard, cut hi, attempt 2
---

# fin-storyboard · hi · attempt 2 — FULL REBUILD

**Attempt 1 is superseded** (style A, Harsh, 78 lines) and `storyboard-hi.md` has been
overwritten. Written against `script-hi.md` attempt 3 (style E, 81 lines, 7 chapters, fin-audit
PASS) and `assets/voice/timing.json` (MEASURED, 519.331s, Amrut). **Every `data-start` and
`data-duration` in the file is `timing.json` verbatim. Nothing was estimated and nothing was
re-timed.**

## Artifacts

- `vault/videos/passive-income-number/storyboard-hi.md` — 14 sections, 81-row scene table
- `studio/videos/passive-income-number-hi/assets/img/manifest.json` — 87 keys (overwrote the
  stale style-A manifest, which was keyed to a 78-scene numbering)

## Counts

| | |
|---|---|
| scenes | **81** (ch1 8 · ch2 13 · ch3 9 · ch4 10 · ch5 17 · ch6 16 · ch7 8) |
| image slots | **87** = 81 bg + 4 second framings + 2 cut-ins |
| files | 87 — **67 fetched · 8 derived crops · 12 reused from the superseded build** |
| `#sN-rate` frames | **31** |
| archetypes | A 23 · B 32 · C 15 · D 11 (all taken from the script's own `[arch …]` cues, none changed) |
| role colour | amber 14 · red 11 · green 8 · orange 1 · **no role 47** |
| transitions | 79 dissolve · **2 shove** · **5 holds** (mechanically dissolves) |
| vector art | 2 drawn proportions · 1 icon row · 1 Lottie · 0 emoji · `off` on 77 of 81 |
| SFX content cues | 3 hero · 5 stamp · 1 buzz · 1 cta · 1 counted cascade, on `bed-resolve`; the rest derived by `cues.py` with a 47-scene declared dry list |

## The six pre-decided items, each discharged

1. **Four breaches, two `data-framings` each.** In style-E numbering these are **s70 (6.13,
   9.812) · s52 (5.12, 9.603) · s57 (5.17, 9.185) · s34 (4.4, 9.159)**. Framings
   5.210/4.602 · 5.090/4.513 · 5.280/3.905 · 5.020/4.139 — every sum exact, no single framing
   over 5.28s, each swap anchored on a named word and clearing the last text cue by ≥2.3s. Each
   second file is a **derived crop of its own source**, never a self-dissolve.
   **The inverted 2.4 instruction was not carried forward** and is called out in §6a: 2.4 is
   s12, measures 7.853s, one framing.
2. **The two near-cap scenes ruled explicitly (§6c).** **s27 (3.6, 8.976) and s65 (6.8, 8.924)
   get ONE framing each.** Reason: both pass the measured gate; a swap on s27 would hand
   `cues.py` a `transition` to punctuate at the exact moment the frame asserts *nothing changed
   but the corpus*, and pushing in on one of s65's two sheets argues for one side of a
   comparison. Surplus goes into the hold, per the design system's own rule. A trip-wire is
   recorded: both clear by <0.1s, so neither line may be expanded or re-voiced without
   re-measuring.
3. **`--warn` tint aimed, not set (§1b).** s42 and s70 both print India's 3.0% as the
   comparator. Neither `.huge` takes a role class; only `#s42-rate` (`10% OR 12%`) and
   `#s70-rate` (`4%`) carry `.warnc`, and `#s70-rate2` holds the 3.0% at `--muted`. Stated
   mechanically because a build that colours the parent and leaves the spans bare renders red
   across the 3.0% and passes every check.
4. **The retired warmth screen.** No warmth requirement appears in any brief, in the storyboard
   or in the manifest. §10 restates the retirement and the `0.0927 × source − 6.43` fit so a
   later fetch round cannot reinstate it. `YHIGH ≥ 110` is carried and every query names the
   light.
5. **ch1/ch2 photographs reused.** §10a is a per-file ledger: **12 of 20 survive**, 8 discarded
   with a recorded reason each. Two reuses close standing blockers rather than replace them:
   - **s16 ← ch2 `s11b.jpg`** — the cleared current-series stone-grey notes become the bg of the
     cut's first corpus figure, which is the frame the demonetised pre-2016 notes blocked. Zero
     fetches, blocker gone.
   - **s3 ← ch1 `s2.jpg`** — the chai-glass counter was blocked for having no window; **style
     E's 1.3 names no window**, so the restyle retires that blocker outright.
   - **s6 ← ch1 `s5.jpg`** — the last open ch1 blocker (a desk showing none of the three named
     bills) stays closed the way fin-editor ruled on 2026-08-07: the bills are DRAWN as three
     icon cells, ported verbatim from the built ch1.
   - **s5 ← ch1 `s4.jpg`** — the enamel plaque, already ACCEPTED on this exact NOT RICH beat.
     Deliberately **not** re-opened via the en cut's eight-sheet search for the same beat.
6. **`arch` / `ground` / `art` on all 81 rows**, plus `ctr`, `trans`, `sfx`, focal, `#sN-rate`
   and bg. No blanks. `fin-build` chooses nothing.

## The known blind spot, closed

`run.json.owed.derived_income_assert_is_frame_only`: the build's rate assert scans **on-screen
tokens** and is structurally incapable of seeing a VO line that speaks a derived figure over a
bare frame. **6.8 (s65) is exactly that** — the VO says «पच्चीस हज़ार» and the frame carries no ₹
figure by design. §4 row 24 makes it a **real `.sub` `#s65-rate`**, not a `.foot`, so it survives
a density pass and the assert has a node to see. Every other frame where a VO line speaks money
carries the rate or the ILLUSTRATIVE marker in frame — 31 rate elements in total, listed.

## Decisions this stage made that were not handed to it

- **No measure bar (§9c).** The en cut climbs with a `.measure` bar and flags it as a back-port
  candidate. Declined, with a reason: this cut already climbs **photographically** — cash box →
  two cash boxes → steel trunk → bank locker → safe door — and a drawn bar over an already
  escalating photograph is rule 8's depictive failure. Saves a component this cut has never
  rendered and five DOM nodes.
- **The ledger spine (§6b).** The script says *"the same ledger page, carried down"* at every
  rung, and the sound-off rule forbids reusing one photograph across points. Resolved as **five
  different paper artefacts, one per rung**, with the monthly line inside each rung a derived
  crop of that rung's own source under one continuous zoom. Four holds, four saved fetches, and
  the recurring shape becomes the ladder's visual grammar rather than a reuse.
- **The ground rule that forces (§6b).** A hold pair shares one `--f1`, so the four ledger pairs
  run their closing scene's `--fund` ground across both halves. Declared explicitly, because a
  later pass would otherwise read the first half as a colourless scene asserting green.
- **Bed `bed-resolve`**, against the en cut's `bed-tension`. This cut's argument is a habit and
  a ladder; the trap is one chapter of seven. Consistent with the split already recorded at en
  D12, so no churn.
- **The `.mega` is `3.0%` at s14**, 240px, the cut's only one — in a video arguing that the rate
  is the whole answer, the rate is the enormous number and every corpus it produces is smaller.
- **Two shoves: s40→s41 and s61→s62.** Out of the three-rung ladder into the question that can
  break it, and the withheld number arriving. Both are turns; nothing else in the cut is.
- **s4 is a dissolve, not a hold**, against the script's own "ONE continuous zoom across 1.3 and
  1.4" cue. s3 is the reused chai-glass counter and contains no phone, so no crop of it can
  produce 1.4's frame. Declared as an override with the reason, and the fetch is briefed on the
  same counter material so the place still reads as one place.
- **Seven photo overrides** against the script's own `img:` cues, listed in §10 with a reason
  each — four are the never-a-lit-screen rule, one a reuse, two a crop that cannot exist.

## Not done, and why

- **`python3 tools/pipeline_check.py check storyboard --slug passive-income-number --cut hi
  --tier medium` was NOT run.** This stage has no Bash tool (`No Bash, no git` in its own
  contract), so it cannot execute the command its contract asks it to finish with. Same shape as
  the fin-audit defect recorded in `run.json.tool_fixes_this_run`: a stage judged against
  something it has no tool to produce. **The orchestrator must run it.** Both preconditions the
  check tests are satisfied — the storyboard exists and the manifest exists and is valid JSON.
- **One thing the check may legitimately fail on**, flagged so it is not mistaken for a
  storyboard defect: `stale_script_problems` compares the current `script-hi.md` hash against
  `run.json stages.fin-voice-hi.script_sha256`, and the script carries a **post-voice in-place
  edit at 4.9** (fin-audit-hi-3 hedged *"gets less"* → *"may get less"*, +3 chars, cut total
  6,425 vs the 6,422 recorded at voice time). If the check fires, it is a real finding about the
  4.9 clip and is resolved at fin-voice, not by editing the storyboard.

## Carried into fin-assets

1. **The six tank frames are the cut's one sourcing risk** (s11, s12, s37, s38, s44, s45). Brief
   the declared fallback **with** the fetch: buy the wide tank at Pexels `large2x` and source the
   other five as tap/stream macros in the same material family. The tap position carries the
   rhyme, not the tank's silhouette.
2. **`s28` (the reused balance) needs eyes before promotion** — two clearly different weights
   must both be legible, or 3.7's own point fails. If not, the fetch query is in the manifest.
3. **A REUSED file needs its CREDITS.txt line copied across too** — `check_assets` requires an
   attribution line per manifest key and will fail a copied jpg with no credit.
4. **Hash-check against `passive-income-number-en` specifically.** Both cuts are being sourced
   in parallel off the same pools and a shared query collapses to the same deterministic top hit.
5. **Pexels `large2x` is REQUIRED** on all eight derived-crop sources (s17, s23, s32, s34, s52,
   s57, s63, s70) plus s62 and s81 — a crop of a 1280px Pixabay file is drawn at ~2×.

## Carried into fin-build

1. Write `assets/cues-tables.json` **verbatim** from §2 — five holds, one buzz at s4 +3.48, one
   counted cascade (s6), a 47-scene dry list. An absent table silently inherits another video's.
2. **`scene_start` is authoritative; never sum forward.** Thirteen joints in this `timing.json`
   are 1 ms off their predecessor's `start + duration`. Root duration comes from `total`
   (519.331) and **s81 must not be back-solved** to close the books.
3. **Font subset:** no `/` and no `?` in any string; `₹X A MONTH`, never `₹X / MONTH`. Dump
   `subset.txt` and check every string before the render.
4. **Grep the built composition for the banned payout word** before the build gate.
5. `Intl.NumberFormat("en-IN")` on every animated figure, and the comma-descender fix is
   system-side — it recurs on every lakh/crore rung (s16, s22, s31, s58, s62, s69, s70, s76, s79).
6. Three script `foot:` strings are production annotations and must **not** be rendered (§3a):
   s5, s61, s39.
