---
summary: en ch5 (s53-s68, lines 5.1-5.16) built as a standalone chapter project from a generator, 106.084s at offset 335.817s, `hyperframes check` PASS with 0 errors and 14/14 WCAG AA, `check build --chapter 5` PASS, `check_vo_frame` PASS, post-build `check assets --chapter 5` PASS. The two derived crops fin-assets could not cut exist and are recorded; BOTH declared swap points were measured against the voice and they came out DIFFERENTLY — s56 is re-cut from 4.100 to 2.500 because the 6c value would have completed 0.43s AFTER its phrase ended, s67 keeps 4.800 because its midpoint already lands on «four percent». The cut's one `.mega` is here and its real width is 1489.7px against a 1500px cap, 100px wider than the storyboard estimated. The invariant is discharged on content at a MEASURED floor (s54, alone at the bottom by 7.66 composed points, bgpos lever = 0.05 points, and the only re-fetch relocates it onto a more substantive beat, which is forbidden). ONE FINDING IS LEFT OPEN AND DECLARED: PEAK 2 (s59) fails three of the four payoff-legibility limbs on my chain and no lever exists at this stage.
updated: 2026-08-12
source: built from vault/videos/passive-income-number/{script-en.md,storyboard-en.md,notes.md,run.json} + studio/videos/passive-income-number-en/assets/voice/timing.json; anchors measured with faster-whisper base.en on this cut's own clips; type measured with fontTools on tools/scaffold/assets/fonts/NotoSansFinance-var.woff2 at wght 900; tone measured on an independently written composed chain; 19 rendered frames in snapshots/qa/b1..b3
stage: fin-build, cut en, chapter 5, attempt 1
---

# fin-build — passive-income-number en ch5, attempt 1

Chapter 5 = VO lines 5.1–5.16 = scenes s53–s68. **The title's promise paid in full**: the
index pays about one percent, so the same $5,000 a month costs roughly four times what a
total-return withdrawal needs — then the middle route, then rung five, the whole BLS
household. It carries the cut's only `.mega`, its second SHOVE, the top of the corpus
ladder, and two of the six derived crops.

---

## Ran

1. Read `vault/CLAUDE.md`, `tools/packs/fin-build.md` and `tools/format/fin-build.json`.
   **No `OPENED-BODY:` line is owed** — the pack's two sliced body sections plus
   `blockframe.css` / `chapter-design.css` answered everything, and neither design note's
   body was opened.
2. Read `notes.md` in full: every `owed.*`, all fifteen `rulings_binding_on_both_cuts`
   entries including `outlier_limb_is_subordinate_to_the_invariant_2026-08-10`,
   `en_tank_becomes_a_drawn_layer_2026-08-10` and
   `separation_not_rank_2026-08-09`; `method_learned.predictions_missed_a_sixth_time_2026-08-10`;
   `chapters.hi.5.s57_swap_point_recut_2026-08-10`; `owed.stamp_warn_red_on_red_upstream`.
3. Read storyboard-en §1 / §1a / §2 / §3 / §4 / §5 / §6a / §6c / §7 rows 53–68 / §8 /
   §9a / §9c / §10 / §11 / §12, and `script-en.md`'s chapter-5 `[arch …]` cue blocks
   (copy has one home and it is the script). Read `logs/fin-assets-en-ch5-1.md` in full
   and `logs/fin-build-hi-ch5-1.md` for the guard set that chapter added.
4. Scaffolded from `tools/scaffold/`: `package.json` + `package-lock.json` copied,
   `npm install` (hyperframes **0.7.66** off the committed lockfile, never `npx --yes`),
   `assets/` as symlinks — `blockframe.css`, `chapter-design.css`, `fonts`, `img` and `js`
   to the scaffold, `voice` to the cut. Nothing copied, nothing inlined,
   `grep -cE 'https?://' index.html` = **0**.
5. **Cut the two derived crops with ffmpeg** — the one thing fin-assets could not do —
   and recorded each in a `.src` sidecar, `manifest.json` and `CREDITS.txt`.
6. **Measured every anchor from the audio.** `faster_whisper` `base.en`, word timestamps,
   on this cut's own clips: 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 5.10, 5.11, 5.12,
   5.13, 5.14, 5.15, 5.16 — every line in the chapter, not a sample. Ran
   `tools/tts/clauses.py --cells N` on both cascade lines as a cross-check; one answer
   taken, one rejected with its own docstring as the reason.
7. **Measured every focal, sub, foot, chip and kicker string** with fontTools against the
   shipped `NotoSansFinance-var.woff2` instanced at `wght 900`, at its ladder size, with
   each class's own letter-spacing applied, against the 1500px `.scene.centred .stack` cap.
   Every line break in the composition is that measurement.
8. **Measured the chapter's composed tone run** on an independently written chain (a
   throwaway script in the scratchpad, written from the CSS rather than from anyone's
   description), plus a five-position `background-position` sweep on the four floor
   candidates.
9. Wrote `build.mjs` (a generator, ported from the ch4 file with hi-ch5's later guards
   folded in) → `index.html` + `assets/audio.json`.
10. `npm run check` · `pipeline_check check build --chapter 5` ·
    `check_vo_frame --chapter 5` · a post-build `pipeline_check check assets --chapter 5` ·
    `tools/audio/cues.py .` against the SHIPPED list.
11. **Max-density snapshot pass: 19 frames across THREE separate `-o` directories**
    (`snapshots/qa/b1`, `b2`, `b3` — never one shared dir, which wipes on each run).
    **All 19 were opened individually at full resolution.** The `Navigation timeout` was
    wrapped in a retry loop; it did not fire on these three invocations.

## Failed

**Nothing is left failing and nothing is owed to make this chapter buildable.** One real
defect was caught by a guard during the build and fixed; one finding is left OPEN and
declared because no lever exists at this stage.

- **F1 — the cascade foot rule was wrong on first pass, and the motion-cue sweep caught
  it.** s56's foot defaulted to variant A's +1.90 and landed **0.60s** before the framing
  swap at +2.50, under `cue_min_gap_seconds`. §5's ladder C puts a cascade foot at **last
  chip + 0.80**, not at +1.90; the default now lives in one function shared by the emitter,
  the settle guard and the gap sweep, so the two cannot disagree. `hyperframes check` would
  have passed this, and `cues.py` validates the SOUND list — the crowding lived entirely in
  the MOTION list, which is the guard hi ch5 built and this chapter is the second scene
  to need.
- **⚠ OPEN, DECLARED, NOT FIXED — the payoff-legibility clause on s59 (PEAK 2).**
  Three of four limbs fail on my chain. Full numbers and the reason no lever exists are in
  Evidence §4; it is handed to fin-review to settle on the encode.

Six things diverge from a literal reading of some source document. Each is declared with
its reason below; three are judgements this stage does not get to make.

---

## Evidence

### 1 · Timings, and the seven homes agree

Root **106.084s**, offset **335.817s** — `timing.json`'s own `scene_start` for 5.1, which
is ch4's offset 248.539 plus ch4's declared root 87.279 to within the 1ms each chapter's
own rounding introduces. The generator asserts, one joint at a time, that (a) every scene
overlaps its successor by exactly `T` (**read from `tools/format.json scene.transition_seconds`**,
never retyped — `owed` item 2 of the hi ch5 log), (b) adjacent scenes alternate track 1/2,
(c) each gap equals the SHIPPED cut's gap to 1e-9, and (d) the last scene lands on the
chapter root. Durations that sum correctly while internal cuts drift cannot be produced.

| id | line | start | own dur | data-duration | trk | arch | ground | ken | focal |
|---|---|---|---|---|---|---|---|---|---|
| s53 | 5.1 | 0.000 | 7.435 | 7.885 | 1 | A | `#2a2113` | o | 88 · target |
| s54 | 5.2 | 7.435 | 5.711 | 6.161 | 2 | A | `#1c2027` | i | 88 · **the floor** |
| s55 | 5.3 | 13.146 | 4.562 | 5.012 | 1 | B | `#2e2411` | o | **`.mega` 300** · target |
| s56 | 5.4 | 17.708 | 7.513 | 7.963 | 2 | C | `#2a2113` | i | 2 chips · **swap +2.50** |
| s57 | 5.5 | 25.221 | 7.670 | 8.120 | 1 | D | `#131f2c` ⚠ | o | 88 · warn |
| s58 | 5.6 | 32.892 | 5.215 | 5.665 | 2 | D | `#0e1c2e` ⚠ | i | 112 · warn |
| s59 | 5.7 | 38.106 | 7.383 | 7.833 | 1 | B | `#0c1a2c` ⚠ | o | num @ +4.95 · **PEAK 2, SHOVE in** |
| s60 | 5.8 | 45.489 | 7.513 | 7.963 | 2 | B | `#2a2113` | i | 88 · **two rate spans** |
| s61 | 5.9 | 53.003 | 7.200 | 7.650 | 1 | B | `#3b1219` | o | num @ +4.55 · warn |
| s62 | 5.10 | 60.203 | 6.495 | 6.945 | 2 | B | `#2a2113` | i | num @ +4.21 · target |
| s63 | 5.11 | 66.697 | 6.364 | 6.814 | 1 | B | `#2e2411` | o | num @ +3.57 · target |
| s64 | 5.12 | 73.061 | 6.913 | 7.363 | 2 | D | `#2a2113` | i | 3 chips · **SPLIT** |
| s65 | 5.13 | 79.974 | 3.909 | 4.359 | 1 | A | `#1c2027` | o | 112 |
| s66 | 5.14 | 83.883 | 6.599 | 7.049 | 2 | C | `#2a2113` | i | num @ +1.99 · target |
| s67 | 5.15 | 90.482 | **8.506** | 8.956 | 1 | B | `#12351f` | o | num @ +5.77 · **swap +4.80 · meas 1.0000** |
| s68 | 5.16 | 98.988 | 7.096 | **7.096** | 2 | B | `#38151a` | i | num @ +4.71 · warn |

Every scene but s68 carries `own + 0.45`; s68 carries its bare `scene_duration`, because a
chapter has no successor to cross-dissolve into. `data-framings` on all sixteen, summing
exactly. The cross-dissolve overlap was confirmed **in the picture, not only in the
attribute**: the snapshot at t = 38.30 — 0.19s into s59's own `data-start` — still shows
s58's type over s59's incoming photograph, which is the shove playing.

### 2 · Every anchor is MEASURED, and all three published fallbacks were LATE

`faster_whisper` `base.en`, word timestamps, on this cut's own clips. Clips start at scene
+0.25 (MEDIUM `lead_in_seconds`), which is the +0.25 in each figure.

| scene | word / clause | clip-local | scene-relative | §5's fallback | built |
|---|---|---|---|---|---|
| s55 | «about» (about one percent) | 2.520 | **+2.77** | +3.07 | **+2.77** (fallback 0.30s late) |
| s56 | «1.04» | 0.720–1.600 | +0.97 … +1.85 | — | chip **+1.10**, inside its own figure |
| s56 | «another reads 1.08» | 2.480–3.920 | **+2.730 … +4.170** | swap +4.100 | **swap +2.500 — RE-CUT** |
| s56 | «1.08» | 2.960–4.170 | +3.21 … +4.42 | — | chip **+3.30** |
| s59 | «5» (five point six million) | 4.700 | **+4.95** | +5.12 | **+4.95** (fallback 0.17s late) |
| s60 | «4%» | 1.060–1.740 | +1.31 … +1.99 | fixed +1.90 | +1.90 — lands inside its own words |
| s60 | «about 1%» | 3.840–4.640 | +4.09 … +4.89 | — | **+4.30**, second pulse |
| s61 | «roughly» (roughly four times) | 4.300 | **+4.55** | +4.86 | **+4.55** (fallback 0.31s late) |
| s62 | «roughly» (roughly 3%) | 3.960 | **+4.21** | — | **+4.21** |
| s63 | «$1» (one point nine million) | 3.320 | **+3.57** | — | **+3.57** |
| s64 | three clauses | — | — | — | **+1.18 / +2.06 / +3.36** (§5 below) |
| s66 | «$78» | 1.740 | **+1.99** | — | **+1.99** |
| s67 | «at four percent» | 4.500–5.220 | **+4.750 … +5.470** | swap +4.800 | **+4.800 — KEPT** |
| s67 | «1» (one point nine six million) | 5.520 | **+5.77** | — | **+5.77** |
| s68 | «$7» | 4.460 | **+4.71** | — | **+4.71** |

**All three published `f` fallbacks were late, by 0.17 to 0.31s**, in the same direction.
Nothing in this chapter needed variant B's +1.90 floor; 5.14 is the closest at +1.99.

**Two durations are shortened and both are forced by the settled-figure floor, not
chosen.** The 1.20s floor (fin-editor's hi-ch2 s18 finding, mechanised by hi ch5) says a
figure still rolling when the cross-dissolve starts has not been READ. s55's pop is 0.50s
(at 0.60 the `.mega` is settled 1.192s, **0.008s under**) and s68's countUp is 1.00s (at
1.20 it is settled 1.186s, **0.014s under**). ⚠ **Neither ANCHOR moved.** A spoken anchor
is not a knob, and on s68 the alternative — anchoring on «over», one word earlier — would
land the figure before it is named.

### 3 · ⚠ THE TWO SWAP POINTS, MEASURED AGAINST THE VOICE — one RE-CUT, one KEPT

This is the finding the brief pointed at, and **the two scenes came out differently under
the same rule**, which is the whole point of measuring instead of applying a template.

**s56 (5.4) is RE-CUT from §6c's 4.100 to 2.500.** «another reads 1.08» runs clip
2.480–3.920 ⇒ scene **+2.730 to +4.170**. At 4.100 the 0.50s cross-dissolve runs
4.100→4.600 with its **midpoint at +4.350 — 0.18s AFTER the phrase it is anchored to has
ended**, and it would only *begin* 0.07s before that end, i.e. the picture would change in
the silence before «and July». That is the same family as
`chapters.hi.5.s57_swap_point_recut_2026-08-10` (which completed 0.02s BEFORE its phrase
began) reflected in the other direction. At **2.500** the midpoint is **+2.750**, inside
«another» (2.730–2.950): the picture changes ON the word that names the second read.
**Independently corroborated** — `tools/tts/clauses.py --cells 2` puts this line's first
clause boundary at scene **+2.77**, 0.02s from the measured word onset. The framings still
partition the scene exactly (2.500 + 5.013 = 7.513), neither exceeds the 9.0 cap, and
framing 1 now covers exactly «One tracker reads 1.04» while framing 2 covers «another reads
1.082, and July was the lowest on record» — **one framing per read**.

**s67 (5.15) KEEPS §6c's 4.800.** «at four percent» runs clip 4.500–5.220 ⇒ scene
**+4.750 to +5.470**. The fade runs 4.800→5.300 with its **midpoint at +5.050, inside «4»**
(+4.850 to +5.070). The hand-off was already correct; the measurement was taken before the
value was trusted, and it agreed. **Deviating from a terminal-accepted hand-off that is
already right is not a trade this stage makes** — that is ch4's s34 reasoning and hi ch5's
s52 reasoning, unchanged. **Same rule, two measurements, two answers.**

### 4 · ⚠ PEAK 2 FAILS THREE OF THE FOUR PAYOFF LIMBS — declared, and no lever exists here

`payoff_clause_and_metric_2026-08-08`, binding on en ch3–6. Measured on this build's own
composed chain (below), s59 scores:

| clause | requirement | result |
|---|---|---|
| sound-off gate (binary, runs FIRST) | type covered, name a concrete object | **PASS** — a loading-dock bay: pallet stack, roller door, EXIT sign, two fluorescent tubes, concrete pillars. Nameable in two words. Confirmed on the rendered frame at 44.61s, not on the jpg |
| top quartile on median | `ceil(16/4)` = top 4 | **FAIL — rank 13 of 16** (25.01), i.e. 4th LOWEST |
| #1 or #2 on p10 | | **FAIL — 4th lowest** at 15.43 |
| non-negative median step in | s58 → s59 | **FAIL — −2.21** |

Near-zero spread is not claimed either way: `p90−p50` is 13.49, 8th of 16.

**NO LEVER EXISTS AT THIS STAGE AND NONE WAS FAKED.** The ruling says the lever is ALWAYS
the photograph, and assets passed a terminal gate. The `background-position` knob was swept
at five positions and moves s59's median 23.83 → 25.46 — **0.45 points at best, inside the
1.0-point tie band**, and even at its best the step-in is still −1.76. The only remaining
way to make the step-in non-negative is to darken s58 on purpose, which is gaming the
metric rather than fixing the frame, and s58 is already on the second-coldest ground in the
video by declaration.

fin-assets saw the shape of this and said so in writing (*"s59 is the chapter's most
substantive beat and is visibly its lowest-key frame … settle this on the encode, not on my
read"*), and its fixes to s60, s63 and s66 raised the floor **around** s59 without touching
it, which is the correct move and is why s59 is no longer the floor. It is also worth
stating that the emptiness is DECLARED design: §9c specifies *"the calmest, emptiest
photograph in the cut … one enormous figure alone in an empty room"* as one of the four
things PEAK 2 gets that PEAK 1 does not.

⚠ Per `predictions_missed_a_sixth_time_2026-08-10` **this is a shortlist, not a verdict**.
en ch4's magnitudes reproduced to within 2.45 while its rank ORDER still moved at ranks
4–11 — which is exactly the band s59 sits in. **The encode settles it.** If it holds there,
the fix is this frame's photograph and nothing else: never the ground, never the scrim,
never the grade.

### 5 · THE INVARIANT — discharged on content, at a measured floor

`separation_not_rank_2026-08-09` §1, live text: **a substantive beat must not be left in
the chapter's darkest frame.** I am not writing *"satisfied by construction"* — that phrase
quotes the retired converse, it is on the record as having been spent by both fin-assets
and fin-build in good faith, and it is not an available answer.

**The instrument.** fin-assets deliberately handed no rank table down (correctly, per
`predictions_missed_a_sixth_time`), so this build measured its own: cover-fit into `.bg`'s
`inset:-8%` box → ken 1.08 at mid-scene → the locked
`grayscale(.32) brightness(.62) contrast(1.05)` → `.field` at `.38` carrying the scene's
`--f1` two-stop ground → the four `.scrim` layers **including the per-scene `--tint`** →
BT.601 percentiles. `.rules`, `.glow` and `.grain` are not modelled — the same omission
the en-ch4 chain made, so the two columns stay comparable.

| scene | line | med | p10 | p90−p50 |
|---|---|---|---|---|
| **s54** | 5.2 | **13.03** | 11.85 | **27.64** |
| s62 | 5.10 | 20.69 | 13.51 | 20.84 |
| s67 | 5.15 | 22.26 | 14.60 | 18.74 |
| s59 | 5.7 | 25.01 | 15.43 | 13.49 |
| s63 | 5.11 | 25.14 | 19.15 | 17.36 |
| s68 | 5.16 | 27.05 | 14.80 | 22.07 |
| s58 | 5.6 | 27.22 | 16.50 | 11.99 |
| s56 | 5.4 | 27.81 | 16.47 | 21.08 |
| s64 | 5.12 | 31.09 | 24.14 | 11.36 |
| s53 | 5.1 | 33.33 | 24.37 | 8.10 |
| s55 | 5.3 | 34.01 | 23.54 | 17.98 |
| s57 | 5.5 | 35.62 | 16.91 | 7.04 |
| s61 | 5.9 | 36.66 | 15.63 | 8.38 |
| s60 | 5.8 | 38.98 | 30.76 | 10.13 |
| s66 | 5.14 | 40.28 | 29.22 | 13.02 |
| s65 | 5.13 | 42.43 | 20.16 | 12.91 |

**s54 is alone at the bottom by 7.66 points** where the next largest adjacent gap in the
chapter is **1.57**, so the §3 OUTLIER LIMB genuinely fires — the same shape as en ch4's
s44 (5.84/6.99), not hi ch4's six-frame cluster.

**Two parts to the discharge, and the second is the one that decides it.**

1. **MECHANISED, and it runs at every build.** `build.mjs` carries an `INVARIANT` block
   that re-derives a LOAD CENSUS — what a viewer has to READ in each frame (`num`, `rate`,
   rate span, `sub`, `foot`, measure bar, drawn layer, cascade) — and throws if the declared
   floor is not at **zero**, if the floor is the payoff, or if the floor is the
   longest-held. s54 scores **0** against a chapter mean of **2.06**, on the
   **second-shortest** scene at 5.711s. It is not the payoff (s59) and not the longest-held
   (s67, 8.506s).
2. **⚠ THAT HALF IS NECESSARY AND NOT SUFFICIENT, and the log says so rather than letting
   the assert stand in for the argument.** **Three scenes tie at zero** — s53, s54, s65 —
   so counting elements cannot pick out the least substantive beat. The discriminator is
   editorial and is stated so it can be argued with: of those three, **5.1 states the
   chapter's PREMISE** (the title's own question, the phrase this format ranks on) and
   **5.13 names a RUNG**, i.e. a structural position in the ladder the whole video is
   building. **5.2 does neither** — it names the route and says it has a price, a hand-off
   sentence whose content the next five scenes actually deliver, asserting no rate, no
   figure and no rung. And there is **no inversion between argumentative weight and
   legibility at the bottom**: s53 sits at rank 10 of 16 and s65 at rank 16.

**NO KNOB WAS SPENT ON s54 AND NOTHING WAS RE-ORDERED TO MAKE IT LOOK SAFER.** The bgpos
lever was swept at five positions and spans **0.05 composed points** (12.99 → 13.04) —
the source is 1880×1253 against `.bg`'s 1.778 box, so `cover` is width-limited and the only
axis is 195 source rows of vertical slack over a frame that is uniform dark navy card above
and below the tag. And the only other lever, a re-fetch, **relocates the floor onto s62 at
7.66 separation**: line 5.10, `ABOUT 3%`, the middle route, a figure frame carrying a
three-line published citation. Under
`outlier_limb_is_subordinate_to_the_invariant_2026-08-10` that fix is not merely optional —
**it is FORBIDDEN**, because §1 is the master clause and §3 serves it.

On the rendered frame (t = 9.20s) s54 is visibly **dark and full, not dark and empty**: the
tag occupies the left third at the chapter's **widest spread, 27.64** — the failure mode the
floor rule actually predicts is contrast collapse and emptiness, not darkness.

### 6 · The cut's one `.mega`, and a measurement the storyboard got 100px wrong

§9c: in a video arguing that the rate is the whole answer, **the RATE is the one enormous
number on screen** and the corpus it produces follows it four scenes later. `ABOUT 1%` at
`.arch-b .mega`:

    raw at 300px                      1601.7 px
    with letter-spacing -14px x 8      1489.7 px
    .scene.centred .stack max-width    1500   px   ->  10.3 px of margin

§3's own estimate was **1392px**; the real figure is **97.7px wider**. 10.3px is inside the
noise of a font rasteriser and `ABOUT 1%` contains a space, so it can break into two 300px
lines and blow the frame. It is pinned with a local **`.v-nowrap`** — a one-off BOX
property, not a type token; nothing about the ladder changes and nothing else in the cut
uses it. Confirmed on the rendered frame at t = 16.75: one line, inside the safe area, and
the contrast pass reports **14/14 AA** with the `.mega` sitting over the NYSE frieze.

⚠ **fin-assets' `.mega`-background flag is carried forward unchanged**: §10 asks this frame
for *"the calmest background in the chapter"* and the facade's top ~55% is a dense
sculptural frieze. Its composed median is 34.01 (rank 11 of 16), so the figure is not on a
dark frame, the institution is real and correctly American, and the gold `STOCK EXCHANGE`
lettering is a real building's own name rather than a fabricated source. **A layout call
for fin-review on the encode; nothing was changed for it.**

### 7 · Two cascades, two instruments, two different answers — and the reason is the same

`owed.cascade_offsets_ignore_the_voice`. Neither cascade uses `popEach` at a fixed offset;
both are separate `pop()` calls at measured onsets.

- **s64 (5.12) — `clauses.py` TAKEN.** `--cells 3` returns **+1.18 / +2.06 / +3.36**, and
  faster-whisper word onsets independently give «three rates» +1.05, «one paycheck» +2.15
  and «and the rate you assume» +3.41 — **agreement to within 0.08 / 0.09 / 0.05 on all
  three cells**, the closest corroboration between the two instruments on this run. Gaps
  0.88 / 0.88 / 1.30, all clearing the 0.80s floor without needing the cascade exemption.
- **s56 (5.4) — `clauses.py` REJECTED, with its own docstring as the reason.** `--cells 2`
  returns **+2.77 / +4.95**, and its first cell is **1.8s late**, because this sentence's
  first named item («One tracker reads 1.04») lives in the opening clause the tool
  deliberately drops. Word onsets win, the same call ch4 made on 4.6. The chips fire at
  **+1.10** and **+3.30**, each inside its own spoken figure.

The difference between the two lines is exactly the condition the tool documents; running
it on both and taking one answer is what makes that visible.

### 8 · The two derived crops — cut here, because ffmpeg is not on the assets allowlist

`logs/fin-assets-en-ch5-1.md` Owed 1 routed these to whoever made `s10b`/`s42`. Both are
1600×900, natively 16:9 so `cover` discards nothing, and both parents are 1880×1253
(1.5004), narrower than 16:9, so `cover` fits them by WIDTH and the horizontal ratio is
the whole story. **Never a self-dissolve back to the same file** (creator rule, firaun
2026-07-23). Asserted against the JPEG SOF markers at every build and printed:

    swap s56: s56b.jpg 1600x900 is a 1.175x push into s56.jpg 1880x1253
    swap s67: s67b.jpg 1600x900 is a 1.175x push into s67.jpg 1880x1253

- **`s56b.jpg` = `crop=1600:900:280:180`.** ⚠ **§10's row for this slot names a file that
  does not ship.** It says *"tighter on the second table"*, and fin-assets' query returned a
  **coiled cloth tape measure**, not two printed tables. The crop is therefore derived
  against the FILE rather than the text — the same move that produced
  `container_ladder_CORRECTION_2026-08-09`. The crop drops the dark left margin and the
  blurred top and lands the tape's **second graduated scale** (the numbered 36/35/34 tail)
  1.175× larger and near frame centre. Two reads, two framings, one object.
- **`s67b.jpg` = `crop=1600:900:200:120`.** The lit window pushed to frame centre and
  1.175× larger, the foreground stone wall and the top sky cut away — §10's *"tighter on
  the lit window"* executed literally.

Both are recorded in a `.src` sidecar, in `manifest.json` and in `CREDITS.txt` (inheriting
their parent's licence row, the hi-ch5 convention). `IMAGES-ch5.jpg` was rebuilt with
`tools/image_sheet.py` — the gate correctly failed on a sheet older than the newest
promoted image — and re-read: **both crops read as a continuous push, not a repeat**, which
is what the sheet's own `HOLDS` line asks a reader to check.

### 9 · Money on screen — five derived/corpus figures, and where each branch fires

`constraints.derived_income_carries_assumption` lives in this build's assert, not in review.
The in-page block is carried forward **VERBATIM** from ch2/ch3/ch4 (including the BILL
branch) so `tools/check_vo_frame.py` can read `RATE` and `MARKER` back out of the same
text; a per-chapter copy that drifts is worse than no assert.

| scene | figure | branch | what pays for it |
|---|---|---|---|
| s59 | `$5,555,556` | CORPUS | `#s59-rate` `.sub` — `AT A 1.08% DIVIDEND YIELD`, up at +1.10, **3.85s before the figure** |
| s60 | `$1,500,000` **and** `$5,555,556` | CORPUS | **two** inline spans, `#s60-rate` `4.0%` + `#s60-rate2` `1.08%` |
| s63 | `$1,929,260` | CORPUS | `#s63-rate` `.sub` — `AT A 3.11% YIELD` |
| s67 | `$1,963,375` | CORPUS | `#s67-rate` `.sub` — `AT A 4.0% WITHDRAWAL RATE` |
| s67 | `$6,545 a month` | **DERIVED** | the same rate element, plus `ILLUSTRATIVE` in frame |
| s67 | `$78,535` | BILL | same |
| s68 | `$7,271,759` | CORPUS | `#s68-rate` `.sub` — `AT A 1.08% DIVIDEND YIELD` |
| s66 | `$78,535` | BILL | **no rate, correctly** — it is a published statistic, not income derived from a corpus. `BLS` in the foot is the MARKER, and deleting that foot line fires the branch |

⚠ **§4 row 8 asked for two spans and gave no colour rule; §1's thesis check does.** *"Amber
never lands on $5,555,556 — it is a price, not a candidate."* So on s60 the **focal takes no
role class at all** and the two spans carry `targetc`: the RATES are what is under
examination and the two corpora print in `--ink`. A build that colours the parent `.huge`
and leaves the spans bare renders amber across a figure the storyboard forbids it on, and
passes every check. Confirmed by eye at t = 50.09. **Both spans take a beat** — the first
at §4's fixed +1.90 (measured inside «4%», +1.31…+1.99) and the second at **+4.30**,
measured inside «about 1%» (+4.09…+4.89) — because a comparator that never pulses is a node
the assert finds and the viewer does not.

**§4's rate-as-focal rule** covers four frames here (s55 `ABOUT 1%`, s56's two chips, s62
`ABOUT 3%`, s64's three chips) and none carries a separate `#sN-rate`; a generator guard
throws if one is added, because printing a rate under itself reads as a defect. None of
those frames prints a dollar figure, so the assert never fires on them — honest behaviour
rather than a suppression.

`check_vo_frame` **PASS on all 16 scenes**, which closes the run's frame-only blind spot on
the five VO lines here that speak a magnitude.

### 10 · The archetype layer, §3c, verified per scene

- **16/16 `has-photo`** and a real full-bleed `.bg`.
  `grep -c 'class="scene clip arch-[a-d] has-photo art-off'` = **16**. No photo-free scene.
  **18 `.bg` layers for 16 scenes** — the two framing swaps.
- **arch / ground / art from §7's rows, not invented.** Sequence **A A B C D D B B B B B D
  A C B B**, matching §7's own rhythm block including the declared `B B B B B` at s59–s63.
- **`art: off` on all sixteen**, so **`.centred` on fifteen**. `0` `<svg>` and `0` `.plate`
  in the emitted document. §8 gives ch5 zero drawn layers and refuses four candidates by
  name; the density assert asserts the LIST, not the count, so an edit that adds one has to
  come back through that line.
- **s64 is the one SPLIT**, and it is §7's own rule rather than an exception: a scene is
  centred *unless something real occupies the archetype's other side*, and its declared
  three-chip cascade owns archetype D's band. The guard now reads exactly that (art-off ⇒
  centred **unless** the scene carries a declared cascade); ch4's s45 was the same shape.
  The chips ride blockframe's own `.row` inside `.arch-d .stack` — not a hand-rolled flex
  row and not ch3's absolutely-positioned `.v-chiprow`.
- ⚠ **`en_tank_becomes_a_drawn_layer_2026-08-10` IS DELIBERATELY NOT APPLIED AT 5.5, and
  the reasoning is on the record rather than an omission.** The ruling says to reuse ch4's
  layer parameterised if a ch5 scene calls the tank back — and 5.5 does. Four reasons it is
  not reused: (i) **§8 refuses 5.5's drawn candidate by name** («one dial moving 4.0 → 1.08
  — the photograph IS a hand on a dial and a thin stream, depictive»), which the ruling does
  not repeal; (ii) the ruling's own scope paragraph is explicit that the layer is built at
  4.7 and applied to 2.2 in the pre-assembly pass, and names no third site; (iii) §8's
  density budget gives ch5 ZERO drawn layers, against an archetype-note calibration of
  three-or-four as the TOP of the range for a fourteen-scene chapter; and (iv) ch4's layer
  asserts a **finite vessel**, which is 4.7's beat, whereas 5.5's beat is **aperture** —
  and drawing a second tap beside the first is precisely what §8 refuses on the script's own
  ⚠, because two apertures side by side say a yield and a withdrawal rate are the same kind
  of thing. **A drawn tank over a photographed tank is the ghost-envelope failure by name.**
- **NO RAIL.** `grep -c 'class="[^"]*\brail\b'` = **0**. No chapter title, no scene counter,
  no slide number. (The three literal `rail` matches in the file are the header comment's
  own *NO RAIL*, the word *tram rails* in a scene note, and *trailing-twelve-month* in
  s62's foot.)
- **Watermark:** `<div id="root" class="cut-en" …>` (1 match), painted on `#root::after`
  and visible bottom-right in **all 19** reviewed frames.
- **The `.stamp.warn` fix is LINKED, NOT RE-PATCHED.** `blockframe.css:192-195` now
  re-states the dark ink on all four `.stamp.<role>` rules at (0,2,0). This composition adds
  **no local copy** — a second local copy is how a fixed bug comes back — and it carries no
  `.stamp` in any case (§8 gives ch5 none; a guard throws if one appears). Checked once more
  for a new member of the centred-override family, because that note asks every chapter to
  look: `.arch-c .stack { width: 880px }` is already covered by `.scene.centred .stack`
  resetting `width: auto` on source order, `.arch-d`'s 1480/1420 caps are line-length rather
  than plate-avoidance and sit inside the centred stack's 1500, and `.sub` carries no
  per-archetype cap at all. **Nothing to patch.**

### 11 · Type — measured, never interpolated, and every break is a measurement

fontTools against the shipped woff2 at `wght 900`, with each class's own letter-spacing
(`.huge` −2px, `.foot` +1px, `.mega` −14px), against the centred stack's 1500px:

| scene | px | line widths | unbroken |
|---|---|---|---|
| s53 | 88 | 1057 / 800 | 1878 |
| s54 | 88 | 669 / 906 | 1598 |
| s55 | **300** | **1489.7**, one line | — |
| s57 | 88 | 1247 / 441 | 1711 |
| s58 | 112 | 1201, one line | — |
| s60 | 88 | 848 / 853 | 1722 |
| s65 | 112 | 1008, one line | — |
| s61 | 112 | 1002 (`ROUGHLY 4 TIMES`) | — |
| every `$` figure | 112 | 593 | — |
| feet @26 | — | s55 994 / 667 (unbroken **1683**) · s56 1344 · s59 767 · **s61 714 / 770** · s62 1029 / 1012 / 1367 · s63 767 · s66 1228 / 1229 · s67 976 · s68 767 | |
| subs @40 | — | s59 568 · s63 352 · s67 615 · s68 568 | |

Every break exists because the string does not fit. **s61's foot is the interesting one**:
unbroken it measures **1494.1px against a 1500px box — 5.9px of margin**, and ch4 already
rejected an 11px margin as *"a frame that re-wraps on a hair"*. 5.9px is half that, so it
ships hard-broken into two measured lines. Sizes come off §3's deterministic ladder keyed on
flattened `stmt` length, computed in the generator; nothing is below 76; the `.mega` is
asserted to exist on s55 and asserted absent everywhere else, in both directions. Counters
use `Intl.NumberFormat("en-US")` (western grouping — `en-IN` would print `$5,55,555`) with
`tabular-nums` from the system.

**Glyph coverage** was swept directly against the face's cmap, because the tofu guard is
documented inert on a chapter project (`uncovered_glyphs()` only fires when the literal
string `FinanceSans` appears in the composition, and the face is named only in the LINKED
stylesheet). Zero missing glyphs, including `&` in `S&P 500`, the em dashes, `·`, the
straight double quotes in s55's and s62's feet, and three apostrophes. `grep` over the whole
emitted document: **0 `₹`, 0 Devanagari, 0 `/`, 0 `?` in any on-screen string, 0 network
references.**

### 12 · Sound — derived, and it reproduces §7's own column with one known exception

`tools/audio/cues.py` reads the file `build.mjs` just wrote, so the cue list and the markup
come from one derivation of `timing.json`. **29 cues over 106.084s** (one per 3.7s; the
reference is en ch4's 24 in 87.3s). Bed overridden to `bed-tension` in the generator, not
hand-edited into the artefact. `assets/audio.json` is deleted before regeneration.
`cues.py` exit **0** on the shipped file; min gap clean. **`cues-tables.json` was NOT
touched** — it already carried s64 on `counted` and seven of these sixteen scenes on `dry`.

Derived cue per scene against §7's `sfx` column: s53 reveal ✓ · s54 reveal ✓ · s55 **hero**
✓ · s56 **swap** ✓ · s57 reveal ✓ · s58 reveal ✓ · s59 **hero** ✓ · s60 **tick** (see
below) · s61 **hero** ✓ · s62 dry ✓ · s63 dry ✓ · s64 **chip ×3** ✓ · s65 dry ✓ · s66 dry ✓
· s67 **swap** ✓ · s68 dry ✓. **Fifteen of sixteen match, and no correction was applied.**

⚠ **No `hero` had to be dropped by hand, unlike hi ch5 and ch3/ch4** — the cut's own dry
table already silences s62, s63, s66, s67 and s68, so the three heroes that survive are
exactly the three §7 names. That is the table doing its job.

⚠ **`owed.cue_rung_5_does_two_jobs` reproduces in BOTH of its forms and neither is
corrected.** (a) s60 emits `tick` at 47.389 where §7 says `reveal`, because cues.py's rung 5
(`span('#sN-mf') or pulse('#sN-.*')`) is reached before the fallback reveal — fin-editor has
already ruled this shape CORRECT where the tick is bound to a real pulse on a rate token,
which it is, on `4.0%`; ch4's s40 and hi ch5's s42 are the same row. (b) **The INVERSE, and
it is sharper here than anywhere else on the run:** s67 carries the cut's one genuine
measure bar, `span('#s67-mf')`, and is on the dry list — so **the one frame in this chapter
that HAS a bar emits nothing at all.** Both are recorded inside `audio.json._tick` so the
next `cues.py` diff is self-explaining.

Both photograph cross-fades emit a `transition` (20.208 and 95.282). ⚠ Both scenes are on
the dry list and both still emit it, because `dry` silences DERIVED CONTENT cues and a
photograph changing is a joint-class event — §6a says so for swaps in as many words.
Flagged rather than suppressed, exactly as hi ch5 flagged s52's.

### 13 · Checks

| check | result |
|---|---|
| `npm run check` | **PASS** — 0 errors, 4 warnings, 2 infos, **14/14 text checks WCAG AA** |
| Lint | 0 errors / 4 warnings — the run's usual family, none new |
| Runtime | 0 / 0 |
| Layout | 0 errors, 0 warnings, **9 `container_overflow` infos** |
| Motion | 0 / 0 |
| `pipeline_check check build --chapter 5` | **PASS build-en** |
| `tools/check_vo_frame.py --chapter 5` | **PASS** — 16 scenes cross-checked against their VO lines |
| `pipeline_check check assets --chapter 5` (post-build) | **PASS assets-en**, 18 promoted images |
| `tools/audio/cues.py .` (shipped list) | exit 0, no gap violation |

The 9 `container_overflow` infos are `.bg` elements reporting that `inset:-8%` extends past
their section — that IS the ken window, on every scene of every locked chapter of this run.
They are **info**, so they change no verdict. **No design token was edited to satisfy
anything** and `format.json known_benign` stays correctly **empty**.

The four warnings: `composition_file_too_large` (646 lines), two ×
`timeline_track_too_dense` (8 per track), and `composition_heavy_overlay_count_high` at
**32** — exactly 16 `.scrim` + 16 `.glow`, two per scene, the arithmetic
`owed.overlay_count_in_the_assembled_master` is tracking. That is below hi ch5's 34 and
above en ch4's 26.

### 14 · The 19 frames, per batch, all opened

One directory per invocation, never reused, because `snapshot` WIPES its `-o` dir.
**Every frame below was opened individually at full resolution — none was judged from a
contact sheet.**

| dir | frames | at (s) | what was checked |
|---|---|---|---|
| `snapshots/qa/b1` | 6 | 2.00 · 9.20 · 16.75 · 19.71 · 22.71 · 26.90 | s53 · **s54 at the floor (dark and FULL)** · **s55's `.mega` on one line** · s56 before the swap (chip 1 only) · s56 after it (both chips + foot) · s57 |
| `snapshots/qa/b2` | 6 | 34.60 · 38.30 · 44.61 · 50.09 · 58.40 · 65.30 | s58 · **the s58→s59 SHOVE mid-play** · **s59 assembled (PEAK 2)** · **s60's two rate spans** · s61 · s62's three-line citation |
| `snapshots/qa/b3` | 7 | 71.90 · 77.16 · 81.50 · 87.48 · 94.48 · 97.88 · 105.29 | s63 · **s64's split cascade** · s65 · s66 · s67 before the swap (empty bar) · **s67 after it, bar at 1.0000** · s68, the chapter tail |

What they establish beyond "nothing overflows":

- **The `.stack` sits inside the safe area on all sixteen scenes** at their own last-cue
  times, including the three-line s62 foot, the two-line s61 and s66 feet, and the 300px
  `.mega`.
- **The `.mega` renders on ONE line** — the `.v-nowrap` guard works and the 10.3px margin
  is not being relied on by accident.
- **Both swaps read as a push into the same picture**, not a cut to a different one
  (19.71 → 22.71 and 94.48 → 97.88).
- **The shove is real and it plays**: at t = 38.30, 0.19s into s59, s58's type is still on
  screen over s59's incoming photograph. Every earlier chapter of this cut had its shove on
  a boundary it did not own.
- **s67's measure bar fills to the full 920px track** and `THE LADDER` sits under it, not
  through it (`.measure-lab.under` at y868/910 — the y742 collision is gone).
- **The last frame (105.29) is complete and settled** — nothing mid-swell, no black.
- **s60's colour construction is correct by eye**: amber on `4.0%` and `1.08%`, ink on both
  corpora.

---

## Changed

- `studio/videos/passive-income-number-en-ch5/` — **new project**, scaffolded from
  `tools/scaffold/` (package.json + package-lock.json pinning hyperframes 0.7.66;
  `assets/{blockframe.css,chapter-design.css,fonts,img,js}` symlinked to the scaffold,
  `assets/voice` to the cut). **No CDN or network reference of any kind.**
- `…/build.mjs` — **new** (the generator).
- `…/index.html` — **new**, generated, 646 lines.
- `…/assets/audio.json` — **new**, derived by `tools/audio/cues.py`, bed overridden to
  `bed-tension`, with both forms of the known cue-rung defect recorded inside the file.
- `…/assets-ch5/final/s56b.jpg`, `s67b.jpg` — **new**, the two derived crops (ffmpeg).
- `…/assets-ch5/final/s56b.jpg.src`, `s67b.jpg.src` — **new**, each recording its crop rect.
- `…/assets-ch5/final/manifest.json` — two entries added for the derived crops.
- `…/assets-ch5/final/CREDITS.txt` — two rows added, each inheriting its parent's licence
  and marked `(derived crop of sNN.jpg)`.
- `…/assets-ch5/final/IMAGES-ch5.jpg` + `.json` — rebuilt (`tools/image_sheet.py`) because
  the gate correctly failed on a sheet older than the newest promoted image; re-read.
- `…/snapshots/qa/{b1,b2,b3}/` — the 19 QA frames.
- This log.

**Nothing else was touched.** No image was fetched, replaced or dropped — all 16 promoted
jpgs and their `.src` sidecars are byte-unchanged from fin-assets. The cut's
`assets/cues-tables.json` was **not** edited. Nothing was written to `tools/`, `.claude/`,
`assets/icons/`, `assets/lottie/`, `run.json` or any other chapter project.
`blockframe.css` and `chapter-design.css` are the scaffold symlinks, **unmodified** — the
`.stamp.warn` fix is upstream and was deliberately NOT re-patched locally. No motion helper
was redefined inline. **No previous video's `index.html` was read**; the two files consulted
are this same video's own ch4 generator and hi ch5 generator.

---

## Owed

1. ⚠ **P1 LOOK FOR fin-review, ON THE DRAFT — PEAK 2 (s59) fails three of the four
   payoff-legibility limbs.** Median rank 13/16 (25.01), p10 4th lowest (15.43), step-in
   −2.21; only the sound-off gate passes. **No lever exists at build**: the bgpos knob moves
   it 0.45 points, inside the tie band, and the ruling's own lever is the photograph, which
   passed a terminal gate. Per `predictions_missed_a_sixth_time_2026-08-10` the rank ORDER
   is the unstable part and s59 sits in exactly the band that moved on en ch4 (ranks 4–11),
   so **the encode settles it**. If it holds, the fix is s59's photograph — never the
   ground, never the scrim, never the grade. Note that §9c *declares* this frame the
   emptiest in the cut, so a fix has to be argued against the storyboard, not just against
   the number.
2. ⚠ **`en_tank_becomes_a_drawn_layer_2026-08-10` was NOT applied at 5.5 and the decision
   should be confirmed rather than assumed.** Four reasons are in Evidence §10; the ruling's
   text says "if any ch5 scene calls the tank back, reuse that layer parameterised", and
   this build reads its scope paragraph and §8's named refusal as controlling. **If the
   orchestrator disagrees, the change is one `art:` key and a `.band`** — s57 is `arch D`
   like s46, so `tank()` transplants with its origin constant unchanged, and `.centred`
   would come off that scene.
3. **`chapters.en.5` should record: build done, draft pending.** The `s58→s59` SHOVE is
   INSIDE this project and needs no assembler handling — unlike hi ch5's `s40→s41`, which
   is still unresolved for `cut_assemble.py`. **The `s52→s53` chapter joint is a plain
   dissolve and belongs to the assembly.**
4. ⚠ **`owed.cue_rung_5_does_two_jobs` is at its worst here** — s67 has the cut's ONE
   measure bar and emits no sound at all, while s60 emits a `tick` where §7 says `reveal`.
   Both are the same one-line cue-model change (a measure bar is a second, non-competing
   event). This is the strongest single argument for making it, and ch6 has three more
   drawn layers coming.
5. **s55's `.mega` sits over a sculptural frieze**, fin-assets' own flag, and the
   measurement makes it sharper: the figure is 1489.7px in a 1500px box. It passes contrast
   14/14 and reads clean at t = 16.75, but it is the frame in this chapter most worth one
   deliberate look on the encode.
6. **s65 ships a cropped part-month under «the whole month, not one slice of it»**
   (fin-assets kept it, all five alternatives worse — foreign-language day names or a
   single-day page). Declared, unresolved, fin-review's call.
7. **s64 shows four-to-five painted arrows under a «three routes» line**, and the tram
   rails read faintly European. Declared by fin-assets; the three chips carry the count.
8. **s66 → s67 are adjacent domestic exteriors** (daylight/dusk, plural/singular, a
   deliberate plural→singular move matching 5.14 → 5.15). One editorial look.
9. **`composition_heavy_overlay_count_high` is 32 on this chapter** — between en ch4's 26
   and hi ch5's 34, against a warn threshold of 25 and a field reproduction of ~40. Another
   data point for `owed.overlay_count_in_the_assembled_master`, which is where ~162 land.
10. ⚠ **§10's derived-crop table names an object that does not ship on s56** ("the second of
    the two printed tables" — the file is a tape measure). Third stale storyboard row this
    run has had to route around, after `container_ladder` and the hi ladder. Worth one
    correction pass on `storyboard-en.md` §10 rather than a fourth work-around.
11. **fin-render should measure comma clearance from the ENCODE at `.huge`**
    (`comma_fix_protects_the_wrong_class`). This chapter's tightest case is s68's
    `$7,271,759` at 112px over its 26px foot; the `.mega` on s55 carries no comma and is
    structurally immune.
