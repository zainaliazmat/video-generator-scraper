# fin-storyboard — en, attempt 1

## Ran

Read `vault/CLAUDE.md`, `tools/format/fin-storyboard.json`, `tools/packs/fin-storyboard.md`,
`tools/audio/kit.json`, `run.json`, `script-en.md` (all 1,026 lines, two pages),
`vault/templates/storyboard-template-finance.md`, and
`studio/videos/financial-freedom-after-50-en/assets/voice/timing.json` (present, 123 lines,
`total` 801.642). Read `vault/videos/passive-income-number/storyboard-en.md` §7/§10/§11/§12 and
`japanese-money-methods/storyboard-en.md` §1–§5 as the two existing precedents for the archetype
row and the cue ladder. Grepped `tools/scaffold/assets/blockframe.css` for the four role tokens
and `chapter-design.css` for the plate/ground mechanics.

Derived, in order: the four-role colour table from the thesis · the archetype (`arch`), ground
(`--f1`) and drawn-art (`art`) row for all 123 scenes · the `centred` flag by the deterministic
rule · the four-cue ladder with anchored/fixed classes · transitions incl. the two shoves ·
the audio bed + 32 SFX cues · the vector-art set · 126 image slots with queries.

Wrote `vault/videos/financial-freedom-after-50/storyboard-en.md` (13 sections) and
`studio/videos/financial-freedom-after-50-en/assets/img/manifest.json` (126 keys).

## Failed

Nothing blocked the stage. Three things went wrong inside it and were corrected before the file
was final:

1. **First pass named plate rects as `p-a` / `p-b` / `p-d`**, copied from
   `passive-income-number/storyboard-en.md` §8. **There is no such class** —
   `grep '\.p-[abcd]' tools/scaffold/assets/chapter-design.css` returns nothing; the file says
   the plate "gets its rect inline (or take an archetype default below)". The same pass carried
   that note's `viewBox="0 0 800 610"` for an archetype-B plate, but `format.json
   chapter_design.archetypes.B.plate` is `[1120, 150, 860, 610]` — **860 wide, not 800**. A
   drawn layer authored 800 wide inside an 860 plate is 60 px short on the right and nothing
   would have failed. Rewritten to name the archetype and its rect, with the viewBox derived
   from it.
2. First pass put `.centred` on the s86 DOM snippet while the same scene's `ctr` column read
   **N**. Corrected to `art-forward` with an explicit `.plate` carrying the inline rect.
3. First pass counted "six scenes carry a `stamp`" against a list of five. Corrected to five
   (s11, s52, s67, s88, s114).

`Edit` is disabled in this session, so both corrections cost a full re-`Write` of the 600-line
file rather than a three-line diff. Noted because it changes the cost of a late fix here: any
correction to this storyboard is a whole-file rewrite of a 123-row table, which is itself a
transcription-risk event.

## Evidence

**Timing is measured, not modelled.** `timing.json` `total` = **801.642 s (13:21.6)** against
`run.json.target_seconds` 746 (+7.5%) and the script's own 797.7 s model (+3.9 s, 0.5% —
the model was good). 123 lines, so 123 scenes, s1…s123. Pace **801.642 / 123 = 6.52 s**
against `scene.target_scene_seconds` 6.5.

**The finding of this stage: ELEVEN scenes breach `scene.max_scene_seconds` 9.0, not one.**
The script's handoff #2 flagged only line 1.8 (152 chars) and instructed a two-framing fix on
that one scene. Measured `scene_duration` from `timing.json`:

| line | scene | scene_duration | over 9.0 by |
|---|---|---|---|
| 1.8 | s8 | 9.473 | +0.473 *(the only one the script knew about)* |
| 2.1 | s12 | 9.525 | +0.525 |
| 2.12 | s23 | 9.708 | +0.708 |
| 3.11 | s39 | 9.603 | +0.603 |
| 3.13 | s41 | **10.021** | **+1.021** — the longest scene in the cut |
| 3.17 | s45 | 9.290 | +0.290 |
| 3.18 | s46 | 9.002 | +0.002 |
| 5.13 | s85 | 9.159 | +0.159 |
| 5.14 | s86 | 9.002 | +0.002 |
| 6.4 | s95 | 9.185 | +0.185 |
| 7.8 | s115 | 9.185 | +0.185 |

Why the script could not see ten of these: it computed from characters at 17.57 c/s, and its
own ceiling arithmetic (144 chars = 8.2 s VO + 0.8 s padding = 9.0 s) is a *character* rule.
`check_build` tests the *measured* scene. Two of the eleven (3.18, 5.14) are over by **2 ms** —
they would still fail, and they are exactly the class of breach no character count can predict.
All eleven now carry `data-framings` with two values summing to `scene_duration`, each second
framing starting ≥1.4 s after that scene's last fixed text cue (s41's chip row pushes its split
to 5.300 s). Same file, tighter crop — no second image slot, and it obeys the firaun rule that
one photograph across a boundary is ONE continuous zoom.

**Nothing else in `timing.json` is near a limit.** Shortest scene s99 (6.8) at 3.203 s, well
over `tts.min_clip_seconds` 1.0. The nine `source-shot` scenes all clear
`source_screenshot.min_hold_seconds` 3.0 — shortest is s37 at 4.980 s.

**Hook gate, measured rather than modelled.** The payoff promise is line 1.3 = s3, whose
`audio_start` is **11.306 s**, inside `script.hook_gate_seconds` 15 with 3.694 s of margin. The
script's two models bracketed it at 11.2 (flat) and ≈12.5 (pause-loaded); reality is 11.306, so
the flat model was right on this cut. Still owed as a silencedetect measurement on the render.

**Reward beat position.** Line 5.14 = s86 starts at 554.060 s = **69.1%** of 801.642, audio at
554.310 = 69.15%. The script placed it at "9:12 = 69.2%" — it lands at **9:14.3**, 2.3 s later
than modelled, still inside the 65–75% reward window.

**Drop zone.** `passive-income`-era window 55–65% = 440.9–521.1 s. Chapter 5 opens at s73 =
**465.319 s = 58.1%**, inside it, and that boundary is SHOVE #2.

**SFX: 32 cues over 801.642 s = one per 25.1 s**, against `tiers.long.max_sfx_cues` **36**.
Per chapter: ch1 4 · ch2 4 · ch3 5 · ch4 4 · ch5 6 · ch6 4 · ch7 3 · shoves 2. Closest pair in
the cut is **1.100 s** (SHOVE #2 at 465.319 and s73's `reveal` at 466.419), clearing
`cue_min_gap_seconds` 0.8. Every other scene carries at most one cue and the scenes are ≥3.2 s
apart, so no other pair can breach. Nine IRS reveals in ch3, **four** of them sounded — s36,
s38, s45 (`hero`) and s52 (`stamp`); the other five declared dry, because a sound on each of
nine consecutive figures makes the ninth inaudible as information.

**Layout constants checked, with the numbers:**
- `first_cue_by_seconds` 0.5 — the kicker fires at **+0.30 on all 123 scenes** (every script
  line carries a `head:` string). ✓
- `cue_min_gap_seconds` 0.8 — ladder gaps are +0.30→+1.10 = **0.80** and +1.10→+2.10 = **1.00**.
  The only sub-0.8 spacing in the cut is the declared chip cascade at **0.65 s**, inside
  `layout.cascade.gap_seconds` [0.6, 0.7]. ✓
- `max_simultaneous_elements` 6 — worst case is s36 (kicker + num + source foot + disclaimer
  lower-third) = **4**. A chip row counts as 1 per `cascade.counts_as_elements`. ✓
- `max_chips_per_row` 3 / `max_chip_chars` 22 — 15 chip scenes measured. Two carry four chips
  (s41 3.13, s92 6.1) and are declared **3+1** explicitly, because `.row` has `flex-wrap` and no
  checker catches an orphan. Longest chip in the cut is `FRA 66 (1943–54): +32%` = **22**,
  exactly at the ceiling; next is `2 More years of growth` = 22. fin-audit already shortened
  seven chip sets on 2026-08-15 and none was re-lengthened here.
- `one_focal_per_scene` — `stmt` and `num` never co-occur; three arithmetic scenes (s38, s40,
  s45) use two `.sub` lines + a rule + one `num`, which is one focal group.
- `photo_free_scene_ratio` 0 — **123 of 123** scenes carry `has-photo` and a real `.bg`. ✓
- `type_ladder_px` — sizes used are 112 · 96 · 76 · 46 · 32 · 26, all on the list, none
  interpolated.

**Archetype distribution: A 47 · B 10 · C 40 · D 26.** C-heavy on purpose — this script's beats
are artefacts (a bucket, a legal pad, five index cards, three account folders, a W-2, an IRS
page), and five of the fifteen figure frames sit on the document the figure came from, so they
are C rather than B. Six runs hold one archetype across consecutive scenes, each because the
scenes are one argument; the two most load-bearing are **ch4 `A A A` (s66–s68)** — disability,
long-term care, "pretending it can't happen", the three risks in this video that cannot be
photographed as objects — and **ch7 `C C C C C` (s109–s113)**, the five recap cards doing the
identical job.

**Ground arc.** Each role's deepest value is spent exactly once: `#0f3a20` on s86 (the reward
beat), `#372a0c` on s45 ($35,750), `#3b1219` on s67 (long-term care), `#0c1a2c` on s84 (the
permanent reduction), `#2d2214` on s123, `#33200f` on s119. **44 of 123 scenes carry no role
colour** and move only on the neutral warm↔cool axis. One declared exception is recorded in the
file so a later pass cannot "fix" it: **s83 and s84 are `--warn` scenes on deep cool grounds** —
the drop is a temperature event before it is a number, and the hottest beat in the cut (s67) has
no number at all, which is precisely why the ground has to carry it.

**Vector art: `off` on 115 of 123.** Six `art-forward` layers (s78, s84, s86, s91, s104, s106)
and two icons (s18, s89). Per-chapter drawn density: ch5 **4** (the top of the archetype note's
range, declared), ch6 **2**, everything else 0 or 1 icon. **Zero Lotties and zero emoji** — every
abstraction in this script is either a proportion (drawn) or an object that can be photographed,
so `lottie.max_per_chapter` never comes into play and nothing needs fetching or tinting.
Rule 8 applied literally: each of the six carries a one-line statement of what it asserts that
the photograph cannot, and the two schematic ones (s78, s104) explicitly forbid tick marks,
numbers and axes so they cannot read as published figures they are not.

**Images: 126 slots = 123 bg + 3 cut-ins.** Cut-ins only where the VO names a *second* concrete
thing one frame cannot hold: s23b (leaky roof, the bg is the car repair), s67b (in-home care,
the bg is assisted living), s80b (consulting, the bg is the part-time counter). The densest
scene, s41 (four chips, 10.021 s), gets the calmest background — a close texture of manila
file-tab card stock, not a competing photograph. Every query names the lighting because
`check assets` fails `YHIGH < 110`, and the lettered objects (five index cards, folders, tabs,
bands) are all specified **blank** — the words on them are composition type, because a stock
photo of a card already reading STABILIZE does not exist and a near-miss is the sound-off
failure by name.

No `MISSING-CONSTANT` and no `OPENED-BODY`: the pack plus `fin-storyboard.json` answered every
question except the plate class name, which the CSS itself answered (see Failed #1).

## Changed

- Created `vault/videos/financial-freedom-after-50/storyboard-en.md` — 13 sections.
- Created `studio/videos/financial-freedom-after-50-en/assets/img/manifest.json` — 126 keys.
- Nothing else touched. No duration re-timed, no script string restated, no chip re-lengthened,
  no run.json edit.

Two decisions that differ from the immediately preceding cut and are deliberate, not drift:

1. **Per-scene `--tint` is not used.** `passive-income-number` derived a scrim tint from each
   scene's role on top of `--f1`. Here `--f1` alone carries the temperature: under
   `.has-photo .field` at 38% plus a role-coloured scrim layer, a role frame is coloured twice.
   `--tint` stays unset on all 123 sections.
2. **`--pop` is spent on s119 (7.12, "write that number down"), not on the final frame.** The
   script names 7.10–7.12 as the video's only CTA and the last three scenes as the next-video
   and subscribe block; putting the one orange element on the physical action rather than on the
   subscribe ask follows the script's own structure. s122's subscribe ask is an ink chip row.

## Owed

1. **The two `ssa.gov` captures (s83, s85) cannot be produced by this pipeline** — every fetch
   returned 403 at evidence stage. They are the sourcing for the video's two strongest claims
   (the permanent reduction at 62 and the +8%/yr delayed credit) and `fact-integrity §4` is
   unsatisfied without them. Nine `source-shot` scenes in total.
2. **126 images**, each passing `YHIGH ≥ 110` and the 50+/US sweep. The 11 two-framing scenes
   need their crop rects recorded in `.src` alongside the query.
3. **Normalise every `src:` line to `AGENCY · as of MONTH YEAR`** at build (script handoff #9) —
   the script mixes `IRS · November 2025` and `IRS Pub 969 · as of January 2026`. The month is
   the source's publication month.
4. **Measure `hook_gate_en` on the render** with silencedetect and write it to `run.json`. The
   11.306 s above is from `timing.json`, which excludes TTS-internal leading silence.
5. **Six drawn layers to author** (§8), each with its arithmetic in a generator comment, and
   **`art-lift` to be added per-scene** if any of s84/s86/s91's backgrounds comes back pale —
   never a darker grade (rule 9).
6. **`fin-editor` should check the ch4 `A A A` run (s66–s68) on the encode, not the sheet.**
   It is the one place a held archetype could read as a stall rather than as one held breath,
   and `chapter_sheet.py` samples at +2.6 s on all three, which will make them look identical
   in a way the moving frames will not.
