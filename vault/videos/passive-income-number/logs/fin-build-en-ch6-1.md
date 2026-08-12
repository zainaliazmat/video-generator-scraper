---
summary: en ch6 (s69-s81, lines 6.1-6.13) — the LAST chapter of the cut — built as a standalone chapter project from a generator, 85.973s at offset 441.900s, and 441.900 + 85.973 is timing.json's own 527.873 total, asserted at build. `hyperframes check` PASS with 0 errors and 15/15 WCAG AA, `check build --chapter 6` PASS, `check_vo_frame` PASS (one acked false positive on a YEAR), post-build `check assets --chapter 6` PASS. s75.jpg was derived here with ffmpeg and its rect is a MEASURED choice, not the suggested one. All three forward-referenced drawn layers resolve — the ladder assembling, completing and overrunning — every bar computed from the §9a scale and asserted against the figure it draws. TWO REAL DEFECTS WERE CAUGHT AND FIXED IN BUILD, both invisible to `hyperframes check`: the drawn bars rendered 500px LEFT of their own tracks because of an authored `transform` attribute (caught on a max-density frame), and the cut's ONE cta sound collided with its own joint transition 0.40s earlier (caught by cues.py). A THIRD is reported and not fixed: `fade()` on an `.art` svg is inert in every chapter of this run. The invariant is discharged on content at a measured floor that is a CHAINED CLUSTER, not a stranded outlier; the payoff clause is measured and two of four limbs fail, declared for the encode.
updated: 2026-08-12
source: built from vault/videos/passive-income-number/{script-en.md,storyboard-en.md,notes.md,run.json} + studio/videos/passive-income-number-en/assets/voice/timing.json; anchors measured with faster-whisper base.en on this cut's own clips (all 13 lines); type measured with fontTools on tools/scaffold/assets/fonts/NotoSansFinance-var.woff2 at wght 900; tone measured on an independently written composed chain; 21 rendered frames in snapshots/qa/b1..b4
stage: fin-build, cut en, chapter 6, attempt 1
---

# fin-build — passive-income-number en ch6, attempt 1

Chapter 6 = VO lines 6.1–6.13 = scenes s69–s81. **The last chapter of the cut.** It admits
the rate is not settled *before* it recaps anything, assembles the five-rung ladder in one
breath under a drawn measure, pays peak 2 a second time with the one element permitted to
leave the frame, returns to the morning the video opened on, and ends on the cut's single
CTA.

---

## Ran

1. Read `vault/CLAUDE.md`, `tools/packs/fin-build.md` and `tools/format/fin-build.json`.
   **No `OPENED-BODY:` line is owed** — the pack's two sliced body sections plus
   `blockframe.css` and `chapter-design.css` answered everything; neither design note's body
   was opened. **No `MISSING-CONSTANT:` line either.**
2. Read `notes.md`: every `owed.*`, all the `rulings_binding_on_both_cuts` entries
   (`separation_not_rank_2026-08-09`, `outlier_limb_is_subordinate_to_the_invariant_2026-08-10`,
   `payoff_clause_and_metric_2026-08-08`, `floor_stopping_rule_and_p10_comparator_2026-08-09`,
   `container_ladder_2026-08-09`, `never_a_screen_vs_sound_off_2026-08-09`),
   `method_learned.predictions_missed_a_sixth_time_2026-08-10`,
   `chapters.hi.5.s57_swap_point_recut_2026-08-10`,
   `chapters._carry_forward_en_ch1_to_ch2_ch6`, `owed.stamp_warn_red_on_red_upstream`,
   `owed.cascade_offsets_ignore_the_voice`, `owed.fade_clobbers_authored_opacity`,
   `owed.cue_rung_5_does_two_jobs`, `tool_fixes_this_run` (today's `blockframe.css` fix).
3. Read storyboard-en §1 / §1a / §2 / §3 / §4 / §5 / §6b / §7 rows 69–81 / §8 / §9a / §9c /
   §10 / §11 / §12 / §13 / §14, and `script-en.md`'s chapter-6 `[arch …]` cue blocks (copy has
   one home and it is the script). Read `logs/fin-assets-en-ch6-1.md` in full and
   `logs/fin-build-en-ch5-1.md` for the guards ch5 added.
4. **Scaffolded from `tools/scaffold/`** — `package.json` + `package-lock.json` copied,
   `npm install` (hyperframes **0.7.66** off the committed lockfile, never `npx --yes`),
   `assets/` as symlinks: `blockframe.css`, `chapter-design.css`, `fonts`, `img`, `js` → the
   scaffold, `voice` → the cut. Nothing copied, nothing inlined.
5. **Cut `s75.jpg` with ffmpeg** — the one thing fin-assets could not do — after a
   nine-rect sweep, and recorded it in a `.src` sidecar, `manifest.json` and `CREDITS.txt`.
6. **Measured every anchor from the audio.** `faster_whisper` `base.en`, word timestamps, on
   this cut's own clips: **6.1 through 6.13, every line in the chapter, not a sample.**
7. **Measured every focal, sub, foot and kicker string** with fontTools against the shipped
   `NotoSansFinance-var.woff2` instanced at `wght 900`, at its ladder size, with each class's
   own letter-spacing, against the 1500px centred cap and archetype B's 900px cap. Every line
   break in the composition is that measurement.
8. **Measured the chapter's composed tone run** on an independently written chain (a
   throwaway script in the scratchpad, written from the CSS), plus a nine-rect crop sweep on
   s75 and five-position `background-position` sweeps on s76, s77, s79 and s81.
9. Wrote `build.mjs` (a generator, ported from the ch4 file with ch5's guards folded in and
   four new ones) → `index.html` + `assets/audio.json`.
10. `npm run check` · `pipeline_check check build --chapter 6` · `check_vo_frame --chapter 6` ·
    a post-build `pipeline_check check assets --chapter 6` · `tools/audio/cues.py .` against
    the SHIPPED list · `tools/image_sheet.py` rebuild + re-read.
11. **Max-density snapshot pass: 21 frames across FOUR separate `-o` directories**
    (`snapshots/qa/b1`, `b2`, `b3`, `b4` — never one shared dir, which wipes on each run),
    covering **19 distinct times**. **Every distinct time was opened individually at full
    resolution.** `b2` was captured twice: its first five frames were reviewed, produced
    finding **F1**, and were then deliberately overwritten by the six-frame re-shoot that
    verifies the fix. The `Navigation timeout` was wrapped in a retry loop; it did not fire.

## Failed

**Nothing is left failing and nothing is owed to make this chapter buildable.** Two real
defects were caught and fixed during the build; a third is reported and deliberately not
fixed because it is a system-wide finding, not a chapter one.

- **F1 — THE DRAWN BARS RENDERED 500px LEFT OF THEIR OWN TRACKS, and only a rendered frame
  showed it.** Every ladder bar carried `transform="scale(0,1)"` as an SVG **attribute** so it
  would be invisible before its cue. On the frame at **43.17s** (`snapshots/qa/b2`, first
  capture) the three green bars sat at x≈0–308 while their ghost tracks sat at x=500–1420 —
  the numerators detached from their own denominators, which is gotcha 7 arriving by a route
  nobody has written down. Cause: GSAP bakes `transform-origin` by measuring the element's
  rendered box, and with the collapsed attribute applied that box is at x=0 width 0, so the
  baked translate is wrong by exactly the rect's own x. **The attribute is not needed at all**
  — `span()` is `tl.fromTo(...)` and on a paused timeline `immediateRender` already puts the
  element in its `from` state at frame 0. Dropping it fixes the position and keeps the
  invisibility. `hyperframes check` passed **both** versions, 15/15 AA, 0 errors.
  ⚠ **This is a NEW gotcha and it belongs upstream** — see Owed 1.
- **F2 — THE CUT'S ONE `cta` SOUND COLLIDED WITH ITS OWN JOINT TRANSITION.** §5's ladder D
  puts `s81-cta` at **+0.40**, and `tools/audio/cues.py` correctly failed the chapter:
  `78.407 -> 78.807 is 0.400s (transition -> cta), under the 0.8s floor`. cues.py already
  knows this shape — its `reveal` rung is documented as *"never the kicker at +0.30, which
  collides with its own joint transition"* — and the `cta` rung has no equivalent guard
  because **no chapter of this run before this one carried a CTA**. Fixed by inverting ladder
  D's two cues rather than by breaking either floor: the **foot takes +0.40** (so something
  authored is on screen inside `first_cue_by_seconds` 0.5 and it is not only the photograph)
  and the **block pops at +1.20**, 0.80s later exactly and 1.20s clear of the joint. It also
  lands the block **0.91s before the spoken word «subscribe»** (clip 1.860 ⇒ +2.11) instead of
  1.71s before it. Declared in the s81 note and in the cue emitter.
- **F3 — REPORTED, NOT FIXED: `fade()` on an `.art` svg is INERT, in every chapter of this
  run that has one.** `.has-photo .art { opacity: .30 !important }` and
  `.has-photo.art-forward .art { opacity: .52 !important }` beat any inline opacity GSAP
  writes, so `fade("#sN-art", …)` cannot animate the layer in. en ch4 ships
  `fade("#s46-art", …)` and `fade("#s49-art", …)`; both are no-ops and both chapters are
  locked. It is the same family as `owed.fade_clobbers_authored_opacity` and it is the reason
  **this chapter calls no fade on any `<svg>`**: every bar arrives by TRANSFORM, which is a
  lever the stylesheet does not pin. See Owed 2.

Six things diverge from a literal reading of some source document. Each is declared with its
reason below; three are judgements this stage does not get to make.

---

## Evidence

### 1 · Timings, and the seven homes agree — including the CUT's own total

Root **85.973s**, offset **441.900s** — `timing.json`'s own `scene_start` for 6.1, which is
ch5's offset 335.817 plus ch5's declared root 106.084. **This is the only chapter where the
root can disagree with the cut's total with no later scene to notice, so the generator
asserts it directly: 441.900 + 85.973 = 527.873 = `timing.json.total`.**

The generator also asserts, one joint at a time, that (a) every scene overlaps its successor
by exactly `T` (**read from `tools/format.json scene.transition_seconds`**, never retyped),
(b) adjacent scenes alternate track 1/2, (c) each gap equals the shipped measurement to 1e-9,
and (d) the last scene lands on the chapter root. Durations that sum correctly while internal
cuts drift cannot be produced.

| id | line | start | own dur | data-duration | trk | arch | ground | ken | focal |
|---|---|---|---|---|---|---|---|---|---|
| s69 | 6.1 | 0.000 | 6.469 | 6.919 | 1 | A | `#301519` | o | 88 · warn |
| s70 | 6.2 | 6.469 | 6.469 | 6.919 | 2 | C | `#2a2113` | i | num `3.9%` @ +2.23 · target |
| s71 | 6.3 | 12.938 | 7.148 | 7.598 | 1 | C | `#2e2411` | o | num `4.7%` @ +2.17 · target |
| s72 | 6.4 | 20.085 | 6.312 | 6.762 | 2 | C | `#301519` | i | 76 · warn · 3-line foot |
| s73 | 6.5 | 26.397 | 6.181 | 6.631 | 1 | D | `#38151a` | o | 112 · **verdict pop** |
| s74 | 6.6 | 32.578 | **3.987** | 4.437 | 2 | A | `#0f2a1a` | i | 112 · fund |
| s75 | 6.7 | 36.565 | 7.096 | 7.546 | 1 | D | `#12351f` | **HOLD 1.16→1.08** | 3 `.sub` · **art** |
| s76 | 6.8 | 43.661 | **8.323** | 8.773 | 2 | D | `#12351f` | **HOLD 1.08→1.00** | 2 `.sub` · **art** |
| s77 | 6.9 | 51.984 | 7.905 | 8.355 | 1 | B ⚠`p-a` | `#38151a` | i | num @ +5.59 · **art** |
| s78 | 6.10 | 59.889 | 5.946 | 6.396 | 2 | D | `#1c2027` | o | 88 · no role |
| s79 | 6.11 | 65.836 | 6.913 | 7.363 | 1 | A | `#2d2214` | i | 88 · no role |
| s80 | 6.12 | 72.748 | 5.659 | 6.109 | 2 | A | `#12351f` | o | 88 · fund |
| s81 | 6.13 | 78.407 | 7.566 | **7.566** | 1 | A | `#33200f` | i | `.cta` · **pop** |

Every scene but s81 carries `own + 0.45`; s81 carries its bare `scene_duration`, because there
is nothing after it **in the video at all**, not merely nothing in this project.
`data-framings` on all thirteen, one value each, summing exactly — **no scene in ch6 swaps its
photograph** (the s75/s76 hold is two SCENES, not two framings of one), so the swap-point
family of findings applies here only to the hold hand-off, measured below. Longest single
framing **8.323s**, clear of the 9.0 cap. The cross-dissolve was confirmed **in the picture**:
the frame at 43.89 — 0.23s into s76's own `data-start` — still shows s75's type over s76's
incoming photograph.

**Ken direction.** ch5 ended on s68 `i`, so this chapter opens `o` and alternates to s74;
s75/s76 are the OUT hold; s77 flips back to `i` and alternates to the end. ⚠ **That flip
inverts the odd/even parity for s77–s81 against s69–s74, and it is not a mistake** — it is
what "flips at every boundary except the hold" means when a hold spends two scenes going the
same way. Declared in the spec so a later pass does not "restore" the parity and break the
hold.

### 2 · Every anchor is MEASURED, and the one published fallback was LATE again

`faster_whisper` `base.en`, word timestamps, on this cut's own clips. Clips start at scene
+0.25 (MEDIUM `lead_in_seconds`), which is the +0.25 in each figure.

| scene | word / phrase | clip-local | scene-relative | §5's fallback | built |
|---|---|---|---|---|---|
| s70 | «3» (three point nine) | 1.980 | **+2.23** | — | **+2.23** |
| s71 | «4» (four point seven) | 1.920 | **+2.17** | — | **+2.17** |
| s73 | «three answers» | 0.700–1.140 | +0.95 … +1.39 | fixed +1.10 | +1.10 — **inside its own words** |
| s74 | «all of it at 4%» | 1.520–2.620 | +1.77 … +2.87 | fixed +1.10 | +1.10 (fixed ladder; 0.67s early) |
| s75 | «a quarter of a million» | 1.680 | **+1.93** | — | **+1.93** |
| s75 | «a third of a million» | 3.540 | **+3.79** | — | **+3.79** |
| s75 | «two thirds of a million» | 4.780 | **+5.03** | — | **+5.03** |
| s76 | «5,000 a month» | 1.240–2.740 | +1.49 … +2.99 | — | **+1.90**, floored (still inside the phrase) |
| s76 | «the average household» | 4.500 | **+4.75** | — | **+4.75** |
| s77 | «5» (five point six million) | 5.340 | **+5.59** | **+6.08** | **+5.59** (fallback **0.49s LATE**) |
| s78 | «a division» | 0.860–1.320 | +1.11 … +1.57 | fixed +1.10 | +1.10 — lands on the phrase |
| s79 | «no alarm» | 2.160 | +2.41 | fixed +1.10 | +1.10 (fixed ladder; see the s79 note) |
| s80 | «lifestyle» | 1.100–1.440 | +1.35 … +1.69 | fixed +1.10 | +1.10 — 0.25s ahead of its word |
| s81 | «subscribe» | 1.860 | +2.11 | fixed +0.40 | **+1.20** (F2) |

**The chapter's only published `f` fallback was late by 0.49s**, the same direction as all
three of ch5's. **Nothing here needed variant B's +1.90 floor except s76's first `.sub`**, and
that flooring is declared: the measured onset (+1.49) would have left a 0.39s gap after the
rate at +1.10, so the line takes +1.90 and still lands inside «five thousand a month».

⚠ **The s75 cascade is anchored on the FIGURE, not on the category noun, and that is the whole
difference.** «groceries» is spoken at clip 0.860 ⇒ **+1.11**, which would have crowded the
rate at +1.10 to a **0.01s** gap. Anchoring each line on the moment its own figure is named
(«a quarter of a million», «a third», «two thirds») gives +1.93 / +3.79 / +5.03 — gaps of
**0.83 / 1.86 / 1.24**, all clear of the 0.80s floor without needing the cascade exemption at
all. `owed.cascade_offsets_ignore_the_voice`: neither recap scene uses `popEach` at a fixed
offset.

### 3 · ⚠ THE HOLD HAND-OFF, MEASURED AGAINST THE VOICE

The brief points at `chapters.hi.5.s57_swap_point_recut_2026-08-10` and ch5's own s56 re-cut.
**This chapter has no declared `data-framings` swap** — its hand-off is a HOLD, i.e. a scene
boundary — so the measurement is a check, not a knob:

    s76 data-start   43.661
    cross-dissolve   43.661 -> 44.111,  MIDPOINT 43.886
    6.8 clip starts  43.911  (scene +0.25 lead-in)
    midpoint is clip-local  -0.025s

**The picture changes 25ms before «Both at four percent»** — the phrase that names rungs four
and five — and it changes inside the lead-in silence rather than across an earlier word. hi
ch5's s57 was re-cut for completing **0.02s before** its phrase; here the boundary is already
*on* the phrase, and in any case **a hold joint is a scene boundary and `timing.json` is its
only home** — a build may not re-time one. Measured, recorded beside the number in the scene
comment, nothing moved.

### 4 · s75.jpg — derived here, and the rect is a MEASURED choice

`logs/fin-assets-en-ch6-1.md` Owed 1 routed this to the build stage (ffmpeg is not on the
assets allowlist). The parent is `s76.jpg` 1880×1253; §6b makes this the cut's one **INVERTED**
hold — the wide frame is the fetched one and the crop is the tight one — so the pair runs OUT.

    s75.jpg = ffmpeg crop=1280:720:20:250   (1.469x push, natively 16:9 so `cover` discards nothing)

Nine rects were cut and measured on the composed chain before one was chosen:

| rect | composed median | p90−p50 | what it costs |
|---|---|---|---|
| `1160:653:20:400` | 17.43 | 9.93 | flattest; ground-heavy |
| **fin-assets' `1400:787:60:300`** | 17.63 | **8.51** | the flattest frame in the chapter |
| `1400:787:20:300` | 17.65 | 9.75 | — |
| `1280:720:20:352` | 17.56 | 9.62 | keeps the crate bases, no sky |
| **`1280:720:20:250` ← SHIPPED** | **18.37** | **18.60** | bases clipped at the bottom edge |
| `1400:787:20:180` | 18.68 | 20.09 | bases gone |
| `1280:720:20:160` | 19.31 | 25.21 | bases gone; spends the column top s76 needs |
| `1500:844:20:120` | 19.31 | 21.52 | same, wider |
| `1280:720:20:60` | 22.16 | 28.66 | crates float; mostly sky |

**Why +250 and not fin-assets' suggestion**, in the order the reasons actually decided it:
(i) it keeps the three ascending stacks and still **holds back** the tall column's top and the
two big right-hand stacks, which are what the pull-back to s76 opens up — the reveal 6.8 is
written for; (ii) it is the brightest rect that does not float the crates; (iii) at +352 the
frame measures a **9.62** spread, the flattest in the chapter and the "dark and EMPTY"
signature the floor rule actually predicts, against **18.60** here; (iv) **the tone step across
the hold joint falls from +2.36 to +1.55** — a hold pair should not step, in temperature
(§11 rule 1) or in tone. Recorded in `s75.jpg.src`, `manifest.json` (`derived crop of s76.jpg
(no fetch) — ffmpeg crop=1280:720:20:250`) and `CREDITS.txt` (inheriting Mathias Reding's
Pexels row, marked `(derived crop of s76.jpg)`), the ch2 `s10b` / ch4 `s42` / ch5 `s56b`
convention. **Never a self-dissolve back to the same file** — the generator throws if a hold
pair's two scenes point at one image.

`IMAGES-ch6.jpg` was rebuilt (`tools/image_sheet.py`) because the gate correctly failed on a
sheet older than the newest promoted image, and re-read: **s75 and s76 read as a push into one
picture, not as a repeat**, which is what the sheet's own `HOLDS` line asks a reader to check.

### 5 · The three drawn layers — one scale, one arithmetic, asserted both ways

§8's three forward references resolve here, and they are en's declared device
(`container_ladder_2026-08-09` records hi's photographic container ladder as the thing they
replace). **Three drawn layers in a thirteen-scene chapter is the TOP of the archetype note's
range, not the target, and it is exactly what §8 budgets.**

    the §9a scale, spent for the last time:  920px = $1,963,375  =>  1px = $2,134.10

| rung | corpus | px | printed on |
|---|---|---|---|
| 1 | $254,225 | **119.12** | s75 `Food · $254,225` |
| 2 | $332,950 | **156.01** | s75 `Car · $332,950` |
| 3 | $656,650 | **307.69** | s75 `Housing · $656,650` |
| 4 | $1,500,000 | **702.87** | s76 `$5,000 a month · $1,500,000` |
| 5 | $1,963,375 | **920.00** | s76 `$6,545 a month · $1,963,375` |
| — | $5,555,556 | **×2.8296 = 2,603px** (1,420 visible) | s77 `$5,555,556` |

**Gotcha 7 is mechanised in both directions**: every width is computed from the corpus figure
and the one constant, and the generator then walks back the other way and throws if a rung's
figure is not PRINTED by the scene that draws it. The overrun is asserted to be ~2,603px and
s77 is asserted to print the figure its bar is a ratio of.

⚠ **`no_return_promise`, which is where a drawn bar is most tempting to read as a forecast.**
Every bar is a ratio between two figures the video has already put on screen **with their
rate** — the five rungs at 4.0% and $5,555,556 at 1.08%, both in this chapter's own frames.
**Nothing here is projected.** The art carries no axis, no tick, no scale and no numeral, and
that is asserted on the emitted markup **with comments stripped first**, so the note explaining
the rule can neither satisfy nor trip the guard (ch4's tank-guard lesson, reproduced).

Construction, per the pack's "what a drawn layer has to look like to survive the encode":
solid fills only, **44px** bars and 40px ghosts (nothing near the 9px floor), the denominator
is a **filled** ghost rect at `fill-opacity .2` and never an outline, and everything sits on a
`.band` at `z-index: 0` **before** the plate in DOM order so the band darkens BEHIND the art
and never the photograph (rule 9). Geometry is authored in the **plate's own coordinate
space** — `p-d` rows at plate y160–484 ⇒ screen 584–908, x 500–1420, so the 920px track is
centred on the frame (500 + 460 = 960) and clear of the watermark box (x1772–1856, y956–1040).

⚠ **s77 overrides its plate to `p-a` and that is load-bearing.** `.p-b` maps viewBox x 1:1 to
screen x on an 860px plate, so anything past vx=800 does not exist on the encode — and the
overrun bar is 2,603px by construction. japanese-money-methods ch2 lost the entire point of a
frame to exactly this with every check passing (gotcha 8). Verified on the rendered frame at
59.08: the bar runs off the right edge of the picture.

⚠ **s77 will sheet as a half-built frame and that is structural, not a defect.**
`chapter_sheet.py` samples at +2.6s; s77's figure is anchored at **+5.59** on its own spoken
word. Confirmed by rendering that exact sample (54.58): kicker, rate and the ghosted five-bar
ladder are up, the figure and the overrun are not. §8 already declares s75/s76 sheet
exceptions for the same reason; **s77 joins them — judge it from the mp4.**

### 6 · THE INVARIANT — discharged on content, at a measured floor that is a CLUSTER

`separation_not_rank_2026-08-09` §1 as amended by
`outlier_limb_is_subordinate_to_the_invariant_2026-08-10`. Live text, one direction only: **a
substantive beat must not be left in the chapter's darkest frame.** I am not writing *"satisfied
by construction"* — that phrase quotes the retired converse and is not an available answer.

**The instrument.** fin-assets deliberately handed no rank table down (correctly, per
`predictions_missed_a_sixth_time`), so this build measured its own: cover-fit into `.bg`'s
`inset:-8%` box → ken 1.08 at mid-scene → the locked `grayscale(.32) brightness(.62)
contrast(1.05)` → `.field` at `.38` carrying the scene's `--f1` two-stop ground → the four
`.scrim` layers **including the per-scene `--tint`** → BT.601 percentiles. `.rules`, `.glow`,
`.band` and `.grain` are not modelled — the same omission the en ch4 and ch5 chains made, so
the columns stay comparable.

| scene | line | med | p10 | p90−p50 |
|---|---|---|---|---|
| **s75** | 6.7 | **18.37** | 14.95 | 18.60 |
| s79 | 6.11 | 19.35 | 13.91 | 15.64 |
| s76 | 6.8 | 19.92 | 15.48 | 16.95 |
| s80 | 6.12 | 24.29 | 15.98 | 19.96 |
| s71 | 6.3 | 24.79 | 15.54 | 24.00 |
| s74 | 6.6 | 26.40 | 21.29 | 8.36 |
| s81 | 6.13 | 28.20 | 19.04 | 21.27 |
| s72 | 6.4 | 33.77 | 13.32 | 15.54 |
| s77 | 6.9 | 34.96 | 18.57 | 12.70 |
| s70 | 6.2 | 36.17 | 17.47 | 14.97 |
| s73 | 6.5 | 36.21 | 25.64 | 10.50 |
| s78 | 6.10 | 40.85 | 29.78 | 9.47 |
| s69 | 6.1 | 43.19 | 14.57 | 11.93 |

**THE BOTTOM IS A CHAINED CLUSTER, NOT A STRANDED OUTLIER.** The two adjacent gaps at the
bottom are **0.98** (s75→s79) and **0.57** (s79→s76), *both inside the 1.0 luma-point tie
band*, so no single frame is "the chapter's darkest" in any sense the rule recognises. That is
the shape of the hi ch4 worked example (a four-way tie spanning 1.08, ruled NOT a defect) and
the opposite of en ch4's s44 and en ch5's s54, which were alone at the bottom by 5.84 and 7.66.
**The §3 outlier limb therefore does not fire**, and the generator throws if a later edit
strands the floor (it recomputes the separation and demands ≤ 1.0).

**Why the beat that sits there is acceptable — argued on CONTENT, and open to disagreement,
because s75/s76 are the recap and the recap is substantive.**

1. **§10 routes it there on purpose.** *"The densest scenes get the calmest backgrounds. The
   seven art-forward frames and the five chip cascades are all routed to near-flat, low-key
   subjects. Density is managed by choosing a quieter image, **never** by dropping one."* Two
   of this chapter's three art-forward frames are s75 and s76. A dark, calm crate wall under a
   drawn measure ladder is the storyboard's own instruction, not drift.
2. **The beat is not carried by the photograph's tone.** Both frames state their figures in
   40px `.sub` type over the scrim and in solid bars at 52% over their own `.band` — a lift
   that exists *because* rule 9 forbids darkening the photograph. Verified by eye at 43.17 and
   49.96: five figures and five bars, all legible, `15/15` AA on the contrast pass.
3. **The two beats the brief protects are nowhere near the bottom.** The payoff **s77 is
   34.96 (rank 9 of 13, 16.6 points clear of the floor)** and the CTA **s81 is 28.20 (rank 7 of
   13)**. The brief's requirement — *its payoff frame and the CTA are the two beats that must
   not be at the floor* — is met on the measurement, not by assertion.
4. **The one lever this stage owns was spent, not argued away.** s75's file is derived HERE, so
   its crop rect is a build decision: the nine-rect sweep is in §4, the chosen rect buys +0.81
   median and +8.98 spread, and every rect above it cuts the crate bases out of frame — buying
   a rank with a framing, which is what the rulings forbid.

**And a fix that would move a MORE substantive beat to the bottom is FORBIDDEN**, which is the
other reason nothing further was spent: the next frames up are s79 (the callback) and s76 (the
second half of the same recap). The `background-position` sweep on s76 was measured and NOT
taken — `top` buys +1.08 and widens the hold's tone step to +2.63.

The assert mechanises the premise rather than the argument: the declared floor must match the
measured floor, must not be the payoff, must not be the CTA, must not be the longest-held
frame (s76, 8.323s), and must not become a stranded outlier.

### 7 · ⚠ THE PAYOFF CLAUSE — measured, two limbs of four fail, declared for the encode

`payoff_clause_and_metric_2026-08-08`, binding on en ch3–6. s77 is this chapter's payoff frame
(the hero `$5,555,556` and the ladder-overrun; §9c calls it peak 2 paid a second time).

| clause | requirement | result |
|---|---|---|
| sound-off gate (binary, runs FIRST) | type covered, name a concrete object | **PASS** — a steel shipping container, doors open, alone in a field. Nameable in two words. Confirmed on the rendered frame at 59.08 |
| top quartile on median | `ceil(13/4)` = top 4 | **FAIL — rank 5 of 13** (34.96), **1.21 behind** the 4th place (s70, 36.17) |
| #1 or #2 on p10 | | **FAIL as measured — rank 5** (18.57) |
| non-negative median step in | s76 → s77 | **PASS — +15.04**, the largest step in the chapter |

Spread `p90−p50` is 12.70, 4th narrowest — **near-zero spread is not claimed as a credit**.

**Two things worth putting in front of fin-review rather than burying.** First, the p10 limb
has a live qualifier: `floor_stopping_rule_and_p10_comparator_2026-08-09` §3 says a **near-flat
host frame is not a valid comparator**. Three of the four frames above s77 on p10 are exactly
that shape and carry the three narrowest spreads in the chapter — s78 (29.78, spread 9.47, a
flat ledger page filling the frame), s73 (25.64, 10.50, a flat target face) and s74 (21.29,
**8.36**, a flat stucco wall). The fourth is s81 at 19.04, **0.47 above s77 and therefore TIED**.
Discounting the three host frames, **s77 reads as tied for #1 on p10** — I state the reading
and the raw ranks so a reviewer can reject it. Second, the median miss is **1.21 points**, i.e.
just outside the tie band, on the measure `predictions_missed_a_sixth_time_2026-08-10` says is
the *least* stable thing on this run.

**A lever exists and was rejected on framing, not taken quietly.** s77's `background-position`
sweep spans 32.33 (`bottom`) to **37.47 (`top`)**, and `top` would move it to **rank 3 of 13**,
clearing the median limb outright. It also moves the visible window to source rows 0–964 of
1300, which puts **the container's own base out of frame** — the object would float. That is
buying a rank with a framing. `center` ships. **The encode settles it.**

### 8 · Money on screen — where each assert branch fires

`constraints.derived_income_carries_assumption` lives in this build's assert, not in review.
The in-page block is carried forward **VERBATIM** from ch2/ch3/ch4/ch5 (including the BILL
branch) so `tools/check_vo_frame.py` can read `RATE` and `MARKER` back out of the same text.

| scene | figure(s) | branch | what pays for it |
|---|---|---|---|
| s75 | `$254,225` · `$332,950` · `$656,650` | CORPUS ×3 | `#s75-rate` `.sub` — `EACH AT A 4.0% WITHDRAWAL RATE`, up at +1.10, **0.83s before the first figure** |
| s76 | `$1,500,000` · `$1,963,375` | CORPUS ×2 | `#s76-rate` `.sub` — `BOTH AT A 4.0% WITHDRAWAL RATE` |
| s76 | `$5,000 a month` · `$6,545 a month` | **DERIVED** | the same rate element, plus `ILLUSTRATIVE ARITHMETIC` in frame |
| s76 | `$6,545` | BILL | same, covered twice over |
| s77 | `$5,555,556` | CORPUS | `#s77-rate` `.sub` — `AT A 1.08% DIVIDEND YIELD`, up **4.49s before** the figure |
| s70 · s71 | `3.9%` · `4.7%` | — | §4's rate-as-focal rule: **no separate `#sN-rate`**, and a generator guard throws if one is added. Neither frame prints a dollar figure, so the assert never fires on them — honest behaviour rather than suppression |

§4's row 12/13/14 requirement is met on all three frames. `check_vo_frame` **PASS on 13
scenes**, with one acknowledged false positive:

⚠ **`check_vo_frame` flagged s72 on the words «two thousand ten», which is a YEAR.** The tool's
own docstring says it over-flags a non-money "ten thousand" and that `--ack` exists for exactly
this; the frame's foot prints `December 2010` — the referent is on screen. Acked, with the
reason recorded here rather than in a flag file.

### 9 · The archetype layer, §3c, verified per scene

- **13/13 `has-photo`** and a real full-bleed `.bg`. `grep -c 'class="scene clip arch-[a-d]
  has-photo'` = **13**; 13 `.bg` layers for 13 scenes (no framing swaps). No photo-free scene.
- **arch / ground / art from §7's rows, not invented.** Sequence **A C C C D A D D B D A A A**,
  matching §7's own rhythm block exactly.
- **Ten of thirteen `art-off`, and nine of those `centred`.** The three that are not centred
  are §8's three declared drawn layers; the generator asserts the art set is exactly
  `s75,s76,s77` and throws on a fourth or a missing one — the LIST, not the count.
- **NO RAIL.** `grep -c 'class="[^"]*\brail\b'` = **0**. No chapter title, no scene counter, no
  slide number.
- **Watermark:** `<div id="root" class="cut-en" …>` (1 match), painted on `#root::after` and
  visible bottom-right in **all 21** reviewed frames.
- **The `.stamp` fix is LINKED, NOT RE-PATCHED.** Today's `blockframe.css` change re-states the
  dark ink on all four `.stamp.<role>` rules at (0,2,0). This composition adds **no local
  copy** — a second copy is how a fixed bug comes back — and **s73, the chapter's declared
  `stamp` scene, carries no `.stamp` pill at all**: §13 D10 gives this cut no `.stamp`
  component, and the verdict is a `pop()` on the `stmt` (which is also what makes the `stamp`
  SFX legal without new copy). A guard asserts on the EMITTED markup, comments stripped, that
  no `.stamp` is present. ⚠ For anyone running the sweep `owed.stamp_warn_red_on_red_upstream`
  asks for: the literal string does **not** appear in this chapter's HTML, and the note that
  discusses the bug deliberately does not print it.
- **No per-scene grade override anywhere.** One scene sets `background-position` (s79), which
  moves the photograph inside its own cover box and is not a grade knob.

### 10 · Type — measured, never interpolated, and every break is a measurement

fontTools against the shipped woff2 at `wght 900`, with each class's own letter-spacing
(`.huge` −2px, `.foot` +1px, `.kicker` +4px, `.sub` 0), against the 1500px centred cap and
`.arch-b`'s 900px cap:

| scene | class · px | measured | shipped |
|---|---|---|---|
| s69 | huge 88 | 1127.8 | one line |
| s72 | huge **76** (49 chars) | 2176.7 @88 → 1848 @76 | two lines, 640.7 / 1208.1 |
| s73 | huge 112 | 954.6 | one line |
| s74 | huge 112 | 889.3 | one line |
| **s78** | huge 88 | **1500.2 against a 1500 cap** | **hard-broken**, 446.9 / 1032.5 |
| s79 | huge 88 | 1208.3 | one line |
| s80 | huge 88 | 1109.4 | one line |
| s70 / s71 / s77 | huge 112 | 261.8 · 261.8 · 573.3 | one line each |
| s75 / s76 / s77 rate | sub 40 | 732.2 · 737.7 · 568.2 | one line each |
| s75 subs | sub 40 | 306.7 · 278.1 · 377.6 | one line each |
| s76 subs | sub 40 | 556.6 · 556.6 | one line each |
| s70 foot | foot 26 | 2288.8 | two lines, 1001.5 / 1279.5 |
| s71 foot | foot 26 | 2261.0 | two lines, 1075.1 / 1178.1 |
| s72 foot | foot 26 | 2761.4 | three lines, 914.2 / 1005.2 / 826.5 |
| s77 foot | foot 26 (900px cap) | 1008.3 | two lines, 608 / 383.4 |
| s81 foot | foot 26 | 845.9 | one line |

**s78 is the interesting one: 1500.2px against a 1500px box — 0.2px of margin.** ch4 rejected
an 11px margin as "a frame that re-wraps on a hair" and ch5 rejected 5.9px; 0.2px is not a
margin at all. It ships hard-broken into its own two sentences.

Sizes come off §3's deterministic ladder keyed on flattened `stmt` length, computed in the
generator; nothing is below 76; the `.mega` is asserted absent (the cut's one `.mega` is ch5's
s55). Counters use `Intl.NumberFormat("en-US")` with the system's `tabular-nums`.

**Glyph coverage** was swept directly against the face's cmap, because the tofu guard is inert
on a chapter project (`uncovered_glyphs()` keys off the literal string `FinanceSans`, and the
face is named only in the LINKED stylesheet). **Zero missing glyphs**, including `·`, the em
dashes, the straight double quotes in three feet, and the apostrophes in `Bengen's` and
`Japan's`. `grep` over the whole emitted document: **0 `₹`, 0 Devanagari, 0 `/`, 0 `?` in any
on-screen string, 0 network references.**

### 11 · Sound — derived, and it reproduces §7's own column

`tools/audio/cues.py` reads the file `build.mjs` just wrote, so the cue list and the markup come
from one derivation of `timing.json`. **18 cues over 85.973s** (one per 4.8s; ch5 was 29 over
106.084s, and this chapter has six DRY scenes out of thirteen). Bed overridden to
`bed-tension` in the generator, not hand-edited into the artefact. `assets/audio.json` is
deleted before regeneration. `cues.py` exit **0** on the shipped file, min gap clean.
**`cues-tables.json` was NOT touched** — it already carried this chapter's `holds` pair,
`counted` and six `dry` scenes, and it matches §2 verbatim.

Derived cue per scene against §7's `sfx` column: s69 **reveal** ✓ · s70 dry ✓ · s71 dry ✓ ·
s72 **reveal** ✓ · s73 **stamp** ✓ · s74 dry ✓ · s75 dry ✓ · s76 dry ✓ · s77 **hero** ✓ · s78
dry ✓ · s79 dry ✓ · s80 **reveal** ✓ · s81 **cta** ✓. **Thirteen of thirteen match and no
correction was applied** — the first chapter of this run where that is true.

⚠ **The s75→s76 joint correctly emits NO transition** (the pair is in `holds`), which is the
whole point of a matched-frame hold.
⚠ **`s75` is on BOTH the `counted` and the `dry` list**, which is the storyboard's own state
(§2 lists it in both). `dry` wins — cues.py silences derived content cues — so the three-line
recap cascade emits no clicks. Recorded inside `audio.json._dry_vs_counted` rather than
corrected: the table is the fact's one home and this build does not edit it.
⚠ **`owed.cue_rung_5_does_two_jobs` does not bite here** — this chapter has no measure bar and
no rate-token pulse, so the tick rung never fires in either of its two forms. ch5's log flagged
that ch6's three drawn layers would make the case sharper; they do not, because all three are
on `dry` or already carry a higher-priority cue.

### 12 · Checks

| check | result |
|---|---|
| `npm run check` | **PASS** — 0 errors, 4 warnings, 2 infos, **15/15 text checks WCAG AA** |
| Lint | 0 errors / 4 warnings — the run's usual family, none new |
| Runtime | 0 / 0 (the in-page RATE ASSERT throws on failure, so this is a real pass) |
| Layout | 0 errors, 0 warnings, **9 `container_overflow` infos** |
| Motion | 0 / 0 |
| `pipeline_check check build --chapter 6` | **PASS build-en** |
| `tools/check_vo_frame.py --chapter 6` | **PASS**, 13 scenes, one acked (a year, §8) |
| `pipeline_check check assets --chapter 6` (post-build) | **PASS assets-en**, 13 promoted images |
| `tools/audio/cues.py .` (shipped list) | exit 0, no gap violation |

The 9 `container_overflow` infos are `.bg` elements reporting that `inset:-8%` extends past
their section — that IS the ken window, on every scene of every locked chapter of this run.
They are **info**, so they change no verdict. **No design token was edited to satisfy
anything** and `format.json known_benign` stays correctly **empty**.

The four warnings: `composition_file_too_large` (533 lines), two × `timeline_track_too_dense`
(7 and 6 per track), and `composition_heavy_overlay_count_high` at **26** — 13 `.scrim` + 13
`.glow`, two per scene, the arithmetic `owed.overlay_count_in_the_assembled_master` is
tracking. That equals en ch4's 26 and is below ch5's 32.

### 13 · The 21 frames, per batch, all opened

One directory per invocation, never reused, because `snapshot` WIPES its `-o` dir. **Every
distinct time below was opened individually at full resolution — none was judged from a
contact sheet.**

| dir | frames | at (s) | what was checked |
|---|---|---|---|
| `snapshots/qa/b1` | 5 | 2.20 · 9.67 · 16.14 · 22.99 · 28.60 | s69 · s70's two-line citation · s71 · **s72's three-line foot at 76px** · **s73's verdict slam over the target** |
| `snapshots/qa/b2` (1st) | 5 | 34.78 · 38.80 · 43.17 · 43.89 · 44.90 | **F1 FOUND HERE** — the bars 500px left of their tracks at 43.17 |
| `snapshots/qa/b2` (2nd) | 6 | 38.80 · 43.17 · 43.89 · 44.90 · 49.96 · 54.58 | **F1 fixed and verified**: one bar at 38.80, three at 43.17, **the hold mid-dissolve at 43.89**, **bars 1–3 HELD across the cut at 44.90**, **all five at 49.96** |
| `snapshots/qa/b3` | 6 | 54.58 · 58.10 · 59.08 · 62.09 · 68.04 · 74.95 | **s77 as the contact sheet will sample it** · the countUp mid-roll at $4,042,810 · **s77 assembled, the overrun leaving the frame** · s78 · s79 · s80 |
| `snapshots/qa/b4` | 4 | 34.78 · 74.95 · 80.61 · 85.90 | s74 · s80 · **the CTA block** · **the last frame of the video** |

What they establish beyond "nothing overflows":

- **The `.stack` sits inside the safe area on all thirteen scenes** at their own last-cue
  times, including s72's three-line foot, s70/s71's two-line citations and s77's two-line foot
  inside archetype B's 900px cap.
- **The ladder assembles, holds and completes.** 38.80 shows one bar; 43.17 shows three inside
  their ghost tracks at 119/156/308; 44.90 shows those same three **unchanged** across the
  scene cut with rows four and five waiting empty; 49.96 shows all five with rung five filling
  its whole track.
- **The hold reads as one continuous pull-back**, not as a cut: at 43.89 s75's type is still on
  screen over s76's incoming, wider photograph.
- **The overrun leaves the frame** (59.08) and the ghosted five-bar ladder is legible under it.
- **The CTA renders correctly** — orange block, dark ink, blockframe's own CSS triangle (not a
  `▶` glyph, which this cut bans), foot below.
- **The last frame (85.90) is complete and settled** — nothing mid-swell, no black.
- **The watermark is bottom-right in every frame.**

---

## Changed

- `studio/videos/passive-income-number-en-ch6/` — **new project**, scaffolded from
  `tools/scaffold/` (package.json + package-lock.json pinning hyperframes 0.7.66;
  `assets/{blockframe.css,chapter-design.css,fonts,img,js}` symlinked to the scaffold,
  `assets/voice` symlinked to the cut). **No CDN or network reference of any kind.**
- `…/build.mjs` — **new** (the generator).
- `…/index.html` — **new**, generated, 533 lines.
- `…/assets/audio.json` — **new**, derived by `tools/audio/cues.py`, bed overridden to
  `bed-tension`, with the `dry`-vs-`counted` collision recorded inside the file.
- `…/assets-ch6/final/s75.jpg` — **new**, the derived crop (ffmpeg).
- `…/assets-ch6/final/s75.jpg.src` — **new**, recording the rect, the sweep and the reason.
- `…/assets-ch6/final/manifest.json` — one entry added for the derived crop.
- `…/assets-ch6/final/CREDITS.txt` — one row added, inheriting its parent's licence and marked
  `(derived crop of s76.jpg)`.
- `…/assets-ch6/final/IMAGES-ch6.jpg` + `.json` — rebuilt (`tools/image_sheet.py`) because the
  gate correctly failed on a sheet older than the newest promoted image; re-read.
- `…/snapshots/qa/{b1,b2,b3,b4}/` — the 21 QA frames.
- This log.

**Nothing else was touched.** No image was fetched, replaced or dropped — all 12 promoted jpgs
and their `.src` sidecars are byte-unchanged from fin-assets. The cut's `assets/cues-tables.json`
was **not** edited. Nothing was written to `tools/`, `.claude/`, `assets/icons/`,
`assets/lottie/`, `run.json` or any other chapter project, and
`studio/videos/passive-income-number-en-ch5/` was not touched at all (its draft render was
running). `blockframe.css` and `chapter-design.css` are the scaffold symlinks, **unmodified** —
today's `.stamp` fix is upstream and was deliberately NOT re-patched locally. No motion helper
was redefined inline. **No previous video's `index.html` was read**; the two files consulted
are this same video's own ch4 generator and ch4 composition.

---

## Owed

1. ⚠ **A NEW GOTCHA FOR `design-chapter-archetypes` / the pack, and it cost a render round
   here: an authored `transform=` ATTRIBUTE on a rect that GSAP will scale renders the element
   at the WRONG X.** GSAP bakes `transform-origin` from the element's measured box, and a rect
   carrying `transform="scale(0,1)"` measures as a collapsed box at x=0, so the baked translate
   is wrong by the rect's own x — 500px here, silently, with `hyperframes check` passing 15/15
   AA. **The attribute is never needed**: `fromTo` with `immediateRender` already puts a paused
   timeline's element in its `from` state at frame 0. This sits beside gotcha 1
   (`stroke-width="N"` as an attribute is a no-op) and is the same lesson: on an SVG that GSAP
   will touch, express state in CSS or in the tween, never in a presentation attribute.
2. ⚠ **`fade()` ON AN `.art` SVG IS INERT AND TWO LOCKED CHAPTERS SHIP ONE.**
   `.has-photo .art` (30%) and `.has-photo.art-forward .art` (52%) carry `!important`, which
   beats the inline opacity GSAP writes, so `fade("#sN-art", …)` cannot bring a drawn layer in.
   en ch4's `fade("#s46-art")` and `fade("#s49-art")` are no-ops today. Same family as
   `owed.fade_clobbers_authored_opacity`. **The correct default is either a `fade` that
   animates to the element's authored/effective opacity, or a documented "animate the elements
   INSIDE the svg" rule** — this chapter took the second and calls no fade on any `<svg>`.
   Nothing is broken on screen in ch4 (the layer is simply up from frame 0); it is the
   *declared* motion that does not exist.
3. ⚠ **`cues.py` NEEDS THE SAME GUARD ON ITS `cta` RUNG THAT IT ALREADY HAS ON `reveal`.**
   §5's ladder D (+0.40) puts the cut's one CTA sound 0.40s after that scene's own joint
   transition, under `cue_min_gap_seconds`, and the tool fails the chapter. This chapter fixes
   it by inverting ladder D's two cues (foot +0.40, block +1.20), which keeps both floors — but
   **the storyboard's ladder D is wrong as written for any chapter that owns a CTA**, and the
   hi cut's ch7 will hit it next. Either §5 changes or the rung gains the guard; a per-chapter
   work-around is the third-best answer.
4. **P1 LOOK FOR fin-review, ON THE DRAFT — the payoff clause on s77.** Median rank 5 of 13
   (34.96, **1.21** behind the top-quartile cut), p10 rank 5 as raw (18.57) or **tied #1 once
   the three near-flat host frames are discounted under the p10 qualifier**, step-in **+15.04**,
   sound-off PASS. The `bgpos` lever that would clear the median limb (`top`, +2.51) cuts the
   container's own base out of frame. **The encode settles it**; if it holds, the fix is that
   photograph and nothing else.
5. **P2 — the two document frames, s70 and s71, are adjacent.** §7 asks for exactly that (ONE
   ANSWER = a research report, ANOTHER ANSWER = a hardback), and the sheet shows they are
   legibly different objects (a modern fanned report on pale wood vs an aged blue hardback on
   slate), but they are the chapter's only back-to-back same-family frames and s81 is a third
   book-ish object 11 scenes later. Declared; fin-review's call on the encode.
6. **P2 — s72 ships a GLOBE with country names legible**, against the script's own cue (*"a
   folded world map… no country legible"*). It is not a fabricated source and carries no brand
   or agency; sound-off it says *the world*, which is the line, and the countries in frame
   include Japan, whose 0.26% is the figure in the foot. Declared rather than re-fetched.
7. **Two strings deviate from the script and both are declared in the composition.**
   (a) s72's foot renders `50-50 stocks and bills` because §3 bans `/` in any on-screen string
   in this cut — same replacement family as ch4's `$5,000 / MONTH` → `A MONTH`. The fact is
   unchanged. (b) **s81's foot is the one string in the chapter not lifted from a
   `head:`/`stmt:`/`num:`/`foot:` field**: the script's `foot:` for 6.13 reads *"The only CTA in
   the video, at 98.6%"*, which is a production annotation about the frame rather than copy for
   it. §5's ladder D declares a second cue on `s81-foot`, so the slot is real; what it carries
   is the reason the line itself gives, in the spoken line's own words — *"The next one prices
   the rungs nobody puts on a thumbnail."* **Nothing is promised that the VO does not say.** If
   fin-review disagrees, it is a one-string edit.
8. **Carried from fin-assets, unresolved, all three declared by that stage and not re-opened
   here:** s70's photograph carries ~40 words of legible corporate-governance body prose (no
   title, figure, agency or brand; free re-pick available at `--pick s70=5`); s73's archery
   target rhymes with ch1's s5 target and the rhyme is undeclared in §10; s74 does not show the
   whole ladder against §10's "full height", after four sheets returned no clean whole-ladder
   frame.
9. **`chapters.en.6` should record: build done, draft pending.** The `s68 → s69` chapter joint
   is a plain dissolve and belongs to the assembly; there is no shove in this chapter and no
   successor after s81. **This is the last chapter of the -en cut** — after its draft and
   review, `cut_assemble.py` has all six.
10. **`composition_heavy_overlay_count_high` is 26 on this chapter** — equal to en ch4, below
    ch5's 32, against a warn threshold of 25 and a field reproduction of ~40. Another data
    point for `owed.overlay_count_in_the_assembled_master`, where the six chapters sum to ~168.
11. **fin-render should measure comma clearance from the ENCODE at `.huge`**
    (`comma_fix_protects_the_wrong_class`). This chapter's only case is s77's `$5,555,556` at
    112px over a 26px foot.
