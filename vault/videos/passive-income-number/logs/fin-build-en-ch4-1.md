---
summary: en ch4 (s40-s52, lines 4.1-4.13) built as a standalone chapter project from a generator, 87.279s, `hyperframes check` PASS with 0 errors and 12/12 AA, `check build --chapter 4` PASS, `check_vo_frame` PASS. THE TANK IS BUILT AS A DRAWN LAYER over s46's photograph, parameterised so it drops onto en ch2's 2.2 verbatim; the level is decorative and the four things that would make it a measurement are asserted absent. Every timing, cue and cascade offset is measured — three faster-whisper word anchors, three speech-anchored chips — and the whole 13-scene tone run was RE-MEASURED on an independently-written composed chain that reproduces fin-assets attempt 2's COMP table to within ~1.4 points and agrees with it on the payoff, the floor and both bgpos knobs. Two real defects were found and fixed by looking at frames: a GSAP SVG transform-origin that threw the drawn stream ~860px off-target, and a self-check that fired on its own explanatory comment.
updated: 2026-08-10
source: built from vault/videos/passive-income-number/{script-en.md,storyboard-en.md,notes.md} + studio/videos/passive-income-number-en/assets/voice/timing.json; measured from studio/videos/passive-income-number-en-ch4/assets-ch4/final/ and from 15 rendered frames in snapshots/qa/b1..b3
stage: fin-build, cut en, chapter 4, attempt 1
---

# fin-build — passive-income-number en ch4, attempt 1

## Ran

1. Scaffolded `studio/videos/passive-income-number-en-ch4/` from `tools/scaffold/`:
   `package.json` + `package-lock.json` copied, `npm install` (hyperframes **0.7.66** off the
   committed lockfile, never `npx --yes`). `assets/` already carried fin-assets' symlinks to
   `blockframe.css`, `chapter-design.css`, `fonts`, `img` and the cut's `voice`; **`assets/js`
   added as a symlink to `tools/scaffold/assets/js`** rather than as a copy, so gsap and
   motion.js are the live system files. Nothing is copied, nothing is inlined, no network
   reference of any kind (`grep -cE "https?://" index.html` = **0**).
2. Read the ch4 spec out of its own homes and nowhere else: `storyboard-en.md` §2 (audio
   tables), §3 (DOM + the three subset exceptions), §4 (the rate element + the fourteen-frame
   table), §5 (cue ladders + anchors), §6b (the three holds), §7 (the archetype rows for
   40-52), §8 (drawn art + what was refused), §9a/§9b (the measure bar and PEAK 1), §10
   (imagery overrides), §11 (ground arc), §12 (transitions); `script-en.md` 4.1-4.13 for every
   on-screen string. Read `notes.md` in full for the five entries dated today.
3. Wrote `build.mjs` (a generator, structure copied from ch3) and ran it. Every `data-start`,
   `data-duration`, `data-framings`, the `S`/`D` maps, the thirteen `<audio>` rows and the root
   duration are computed from `timing.json` and asserted against the shipped cut's **gaps**.
4. **Measured every anchor from the audio**, `faster_whisper` `base.en` with word timestamps,
   on this cut's own clips: 4.1, 4.2, 4.3, 4.6, 4.7, 4.11. Ran `tools/tts/clauses.py --line 4.6
   --n 3` as the cross-check on the cascade.
5. **Re-measured the whole chapter's composed tone run** on an independently written chain
   (throwaway script outside the repo), reproducing fin-assets attempt 2's COMP instrument from
   the CSS rather than from their description: cover-fit into `.bg`'s `inset:-8%` box at each
   scene's `background-position` → ken 1.08 at mid-scene → the locked
   `grayscale(.32) brightness(.62) contrast(1.05)` → `.field` at `.38` carrying the scene's
   `--f1` two-stop ground → the four `.scrim` layers verbatim → BT.601 percentiles.
6. `npm run check` (`hyperframes check`) — iterated to clean.
   `python3 tools/pipeline_check.py check build --slug passive-income-number --cut en --chapter 4`.
   `python3 tools/check_vo_frame.py passive-income-number --cut en --chapter 4`.
   `python3 tools/audio/cues.py studio/videos/passive-income-number-en-ch4` (the shipped
   `audio.json` re-validated against `cue_min_gap_seconds`).
7. **Max-density snapshot pass — 15 frames, four `-o` directories, every frame opened.**
   One directory per invocation, never reused, because `snapshot` wipes its `-o` dir:
   `snapshots/qa/b1` (5 frames), `b2` (6), `b2zoom` (1 crop-zoom), `b3` (4, of which 1 is the
   re-verified s46). **All 15 were looked at, and 13 of 13 scenes are covered at their own last
   cue time.** The CLI's `Navigation timeout` was wrapped in a retry loop; it did not fire on
   these four invocations.

## Failed

Nothing is left failing. Two real defects were found and fixed, and both are the kind that only
a rendered frame shows:

- **F1 — THE DRAWN STREAM RENDERED ~860px OFF-TARGET.** Authored with
  `style="transform-origin:50% 0%"` and driven by `span()` (scaleX), the tank's stream rect —
  authored at plate x 1244 — rendered at screen **x ≈ 375-430**, a detached red block on the
  far left of the frame with nothing above it. `hyperframes check` passed clean, `check build`
  passed clean, and the linter has no opinion about where an SVG rect lands. It was caught by
  opening `snapshots/qa/b1`… no: by opening `snapshots/qa/b2/frame-02-at-44.22s.png` and then
  cropping it with `--zoom 300,760,1100,340` to confirm the block was drawn and not
  photographic. **Fixed by using `transform-origin: 0% 50%`** — the form every scaled rect in
  this run's ch2 and ch3 uses, and the form the yield-fraction on 4.10 renders correctly with
  **in the same file, in the same frame, under the same GSAP build** (its numerator, ghost,
  denominator and quotient all land exactly where they were authored). So this is not a GSAP
  bug report, it is a house rule with an in-file control: **percentage `transform-origin` on an
  SVG rect is only safe in the `0% 50%` form.** Re-verified on a fresh frame.
- **F2 — THE TANK'S SELF-CHECK FIRED ON ITS OWN COMMENT.** The assert that proves the drawn
  level carries no tick, no scale, no numeral and no ghost scanned the emitted markup
  including its `<!-- -->` comments, and the comment says *"No tick, no scale, no numeral, no
  ghost of the old level."* So it threw on the note that explains the rule and would have been
  silenced by deleting that note. **This is the Lottie-guard failure reproduced in a fresh file
  within the hour** (`tool_fixes_this_run`, 2026-08-08: the guard regex-scanned raw HTML and
  fired on the CSS comment describing the trap it prevents). Fixed the same way the tool was:
  strip comments before matching.

Two things are **declared, not fixed**, and both are decisions rather than defects:

- **The storyboard contradicts itself on s40's ken direction, and it had to be resolved rather
  than papered over.** §5's mechanical rule ("flips at every boundary except a hold") applied
  from s1 through ch1's s3/s4 hold puts s39 on `o`, which forces s40 `i` and s41 `o` — but
  §6b's table says the s41→s42 hold runs `i` 1.00→1.08 then 1.08→1.16, and §5's own sentence
  says *"s75→s76 is the ONE hold that runs OUT."* Two statements against one. **s40 takes `o`**;
  the cost is two consecutive pull-backs across the s39→s40 joint, which is a chapter boundary
  AND the cut's first SHOVE — the one joint in the cut where a direction repeat is least
  visible, and it belongs to the assembly, not to this project. The alternative puts two
  push-ins side by side *inside* the chapter.
- **s46 loses `.centred` (§7 gives it `ctr Y`).** `.scene.centred .plate` is `display: none`,
  so the ruling's drawn layer cannot exist on a centred scene. §7's `ctr Y` was written when
  4.7's art was `off`, and §7's own rule is *centred unless something real occupies the
  archetype's other side* — the tank now does. Archetype D hangs its stack top-left either way,
  so **no type moved**; only the plate came back.

## Evidence

### 1 · The tank, built as a drawn layer — what it asserts, and what it deliberately cannot

`rulings_binding_on_both_cuts.en_tank_becomes_a_drawn_layer_2026-08-10`, implemented at 4.7
(s46). The photograph stays: `image_per_scene` is untouched, s46 keeps its full-bleed `.bg`
(the park standpipe), and nothing was removed from the frame.

**Rule 8 is satisfied the strong way rather than argued around.** A photograph of a tap cannot
state that there is a **finite vessel** behind it, and finiteness is the whole beat — 4.8's
line is *"how long a tank lasts at each rate."* The drawn layer asserts precisely the thing the
picture is structurally incapable of asserting, which is the test the rule sets. It is
`art-forward` (52%) on a `.band` at `z-index: 0` **before** the plate in DOM order, which is
rule 9's lever — `.band`'s own `z-index` is 1 and would otherwise paint *over* a z-0 plate and
darken the art instead of the ground behind it. Construction copied from en ch2's s17/s18,
which is the only other place in this run that does it.

**⚠ THE LEVEL IS DECORATIVE AND ASSERTS NO QUANTITY.** Four things are absent and their absence
is asserted at build time on the emitted markup (not promised in prose): **no tick, no scale,
no numeral, no ghost of the previous level.** The last one is the load-bearing absence — a
before/after marker is exactly what converts a decorative level into a measured drop. The level
also **does not slide**: it is two rects and the upper slice `exit()`s, so the change reads as a
state rather than as a distance travelled down a scale. Nothing in the layer is drawn to a
source's scale and nothing in it is a published figure.

**Reusability at 2.2 is structural, not aspirational.** `owed.en_ch2_s10_tank_layer` applies the
same layer to en ch2's s10 in the pre-assembly pass. s10 is **also `arch D`** (storyboard §7),
so the plate rect and the viewBox are identical there — the function `tank(id, opts)` is
authored in the p-d plate's own space (`0 0 1920 656`) over ONE origin constant and drops in
verbatim with `{drop: false, widen: false}`, which is the correct state for 2.2 (the tank is
being filled; neither the level nor the tap has moved yet).

**Geometry, checked against every boundary it could cross:** the box is 697×356 at plate
(600, 180) ⇒ screen **x 600-1297, y 604-960** — below `.band`'s start at y583 so everything
drawn sits on darkened ground, above the 970px bottom safe line, and clear of the watermark box
(`#root::after` is `right:64 bottom:40`, 84×84 ⇒ x1772-1856, y956-1040). Solid fills only,
nothing thinner than 22px, water at `fill-opacity .5` (a fill-opacity, so the entrance fade is
free to run 0→1 and the `!important` 52% stays the only global lever).

**Timing, measured:** "tank" is spoken at 0.520s into the clip (scene +0.77), "12%" at 1.520
(+1.77). Band +0.90 → vessel +1.00 → stmt +1.10 → stream widens **+1.85, on its own word** →
level slice exits +2.45. Assembled by **+2.95** on a 4.744s scene, inside `chapter_design`'s
"about +3.3", and the `<svg class="art v-tank">` carries the `v-` class the contact sheet's
late-settle keys off — so this scene sheets built rather than half-drawn.

**Density: two drawn layers in a thirteen-scene chapter** (the tank + §8's `yield-fraction`),
against the archetype note's "three or four is the TOP of the range." §8 budgeted ch4 exactly
one; the second is a ruling dated after the storyboard. Eleven of thirteen scenes are `art-off`.

**What was refused, on the record:** 4.8's "how long a tank lasts at each rate" (§8 refuses it —
a balance falling to zero asserts a depletion schedule with no source, the shape
`no_return_promise` forbids; having drawn the tank one scene earlier does not buy it); 4.7's
"a 12% tap beside a 4% tap" (§8 refuses it on the script's own ⚠ — two apertures side by side
say a yield and a withdrawal rate are the same kind of thing, the exact conflation this chapter
exists to avoid, so ONE tank and ONE tap are drawn and no comparison is); 4.11's yield series
since 1871; a drawn layer on s41.

### 2 · The tone run, RE-MEASURED — and the instrument agrees with fin-assets'

Chapter table on **this build's own chain**, with the two bgpos knobs applied. `d-med` is the
composed median step entering the scene; `p90−p50` is reported beside the median and ranks
nothing.

| scene | line | bgpos | med | p10 | p90−p50 | d-med | fin-assets COMP med |
|---|---|---|---|---|---|---|---|
| s40 | 4.1 | `center 35%` | 30.03 | 13.59 | 15.83 | — | 33.23 |
| **s41** | 4.2 | | **32.38** | **24.14** | 14.13 | **+2.35** | 33.92 |
| s42 | 4.3 | | 33.81 | 24.52 | 13.83 | +1.43 | 35.32 |
| s43 | 4.4 | | 28.72 | 14.59 | 14.89 | −5.10 | 30.64 |
| **s44** | 4.5 | | **15.61** | **12.06** | 15.33 | **−13.11** | 14.91 |
| s45 | 4.6 | `center bottom` | 33.89 | 16.34 | 11.54 | +18.28 | (37.82 at `center`) |
| s46 | 4.7 | | 28.33 | 15.67 | 13.27 | −5.56 | 30.19 |
| s47 | 4.8 | | 28.39 | 19.26 | 10.36 | +0.06 | 29.01 |
| s48 | 4.9 | | 21.45 | 14.11 | 16.99 | −6.95 | 21.90 |
| s49 | 4.10 | | 25.15 | 18.22 | 15.85 | +3.70 | 25.83 |
| s50 | 4.11 | | 28.07 | 14.70 | 18.89 | +2.92 | 29.03 |
| s51 | 4.12 | `center bottom` | 26.79 | 14.86 | 12.39 | −1.28 | 27.98 |
| s52 | 4.13 | | 24.69 | 14.34 | 9.52 | −2.10 | 25.62 |

**The two chains agree.** Mine sits a mean **−1.3** low (I do not model `--tint`, `.rules` or
`.grain`, same as theirs on the last two), the largest single disagreement is **1.9** (s51,
`center`), and the ORDER matches on everything that decides a clause: the same top three
(s45 · s42 · s41), the same bottom two (s48 · s44), the same p10 top two (s42 · s41). The only
reshuffles are inside the four-way band fin-assets itself flagged as tied (s43/s46/s47/s50 span
0.65 on my chain). **Downstream should still quote fin-assets §1's table** — it is the
reference instrument and it is the one the ch2/ch3 lineage is comparable to; this column exists
because a build that designs against numbers it did not take should take them.

**PEAK 1 (s41) — all four payoff clauses, scored on measured numbers:**

| clause | requirement | result on this chain |
|---|---|---|
| sound-off gate (binary, first) | type covered, name a concrete object | **PASS** — two bank-vault doors in a brick wall: locking bars, gearwork, rivets, a spoked handwheel, a combination dial. Confirmed on the rendered frame, not the jpg |
| top quartile on median | `ceil(13/4)` floored at 3 ⇒ top 4 | **PASS — #3 of 13**, +2.35 over #4 (s40) |
| #1 or #2 on p10 | | **PASS — #2 of 13** at 24.14; #1 is s42, its own continuation crop |
| non-negative median step in | s40 → s41 | **PASS — +2.35** with the s40 knob; +1.32 without it |

Near-zero spread is **not** claimed as a credit: s41's `p90−p50` is 14.13, 6th of 13, and the
narrowest in the chapter is s52's 9.52. The payoff did not win by being empty.

### 3 · THE INVARIANT — discharged on content, and mechanised where it can be

`separation_not_rank_2026-08-09` §1, live text: **a substantive beat must not be left in the
chapter's darkest frame.** I am not answering it with *"the invariant is satisfied by
construction"*; that phrase quotes the retired converse, it is on the record as having been
spent by this stage once already, and it is not an available answer.

**The floor is s44 on both instruments** — 15.61 here against s48's 21.45 (a 5.84 gap), 14.91
against 21.90 there (6.99). Two parts to the discharge, and the second is the one that decides
it:

1. **MECHANISED, and it runs at every build.** `build.mjs` carries an `INVARIANT` block that
   re-derives a load census — what a viewer has to READ in each frame (`num`, `rate`, `sub`,
   `foot`, measure bar, drawn layer, cascade) — and throws if the declared floor scene is not at
   **zero**, if the floor is the payoff, or if the floor is the longest-held frame. s44 scores
   **0**: no figure, no rate, no foot, no citation, no cascade, no drawn layer, no bar. Three
   countable elements (photo + kicker + statement) against a chapter mean of **3.85**, on the
   **second-shortest** scene at 5.711s (only s46's 4.744s is shorter). It is not the payoff
   (s41 is) and not the longest-held (s50 7.801 · s41 7.749 · s51 7.435 · s49 7.383; s44 is
   12th of 13).
2. **⚠ THAT HALF IS NECESSARY AND NOT SUFFICIENT, and the log says so rather than letting the
   assert stand in for the argument.** **Five scenes tie at zero on that census** — s44, s47,
   s48, s51, s52 — so counting elements cannot pick out the least substantive beat, and an
   earlier draft of this note claimed it could. It was wrong and it is corrected here. The
   discriminator is editorial and is stated so it can be argued with: **of those five, 4.5 is
   the only one whose statement is a SIGNPOST rather than a claim.** *"This is where the ladder
   breaks"* points forward and asserts nothing about a yield, a price, a tank or a rate. 4.8
   states what the papers tested; 4.9 defines the mechanism; 4.12 explains 1932; 4.13 is the
   chapter's verdict. And there is **no inversion anywhere between argumentative weight and
   legibility**: the four frames that must be read sit at **s42 #2, s41 #3, s40 #4, s50 #8 of
   13**, all in the top half of the tone run.

**The §3 outlier limb fires and the fix is forbidden** — `outlier_limb_is_subordinate_to_the_
invariant_2026-08-10`. **No knob was spent on s44 by this build.** The brief is explicit that
seven `background-position` values were already measured to span 1.04 points (the photograph is
wet black asphalt end to end and has no brighter part to point at), and the only other lever
relocates the floor onto **s48** at 2.21 separation — line 4.9, `payout DIVIDED BY price`, the
mechanism beat and the storyboard's declared 5:00 beat. §1 governs and §3 serves it. On the
rendered frame s44 is visibly **dark and full, not dark and empty**: full-width crosswalk bars
with red/teal/amber reflections in the water, spread 15.33, 5th widest in the chapter.

### 4 · The two bgpos knobs, re-measured rather than taken on trust

- **s40 `center 35%` — TAKEN.** fin-assets downgraded it from REQUIRED to recommended because
  on the composed chain the step-in is tied either way. Re-measured here it is **not** tied:
  `center` → `center 35%` moves s40's median 31.06 → 30.03, and the step INTO the payoff goes
  **+1.32 → +2.35**. On fin-assets' chain the same knob moves it −0.78 → +0.69. So the knob is
  the only choice that is correct under both readings, which is the ground the recommendation
  actually stands on. It is also the better layout independently: on the rendered frame the
  black negative space lands under the type stack and the fanned notes under nothing.
- **s51 `center bottom` — TAKEN, and it does two jobs.** Median 23.25 → **26.79**, p10 14.01 →
  14.86, spread 15.02 → 12.39 (fin-assets: 24.11 → 27.98, the same move to within 0.4). And it
  crops the frame's three legible text blocks out: verified on the rendered frame at 75.27s,
  the painted banner `FREE SOUP COFFEE & DOUGHNUTS FOR THE UNEMPLOYED`, the `ALBERT HORAN /
  BAILIFF` sign and `PARKING 25¢` are **all gone**, and the only surviving text is a small
  `FREE SOUP &` on the shop glass. It still reads unmistakably as a breadline.

### 5 · s45 — the framing instruction, executed, and the geometry that decides it

`chapters.en.4.s45_accepted_with_the_sound_off_question_left_open_2026-08-10`: frame it so the
blank screen is not the subject.

**The horizontal knob does not exist and that had to be derived before choosing one.** The
source is 1733×1300 (1.333) against `.bg`'s 1.778 box, so `cover` is **width-limited** — zero
horizontal slack, and no `background-position` can move the phone sideways. What exists is
**325 source rows of vertical slack**: `center` shows source rows 162-1137 and keeps ~96% of the
screen; **`center bottom`** shows 325-1300, cutting the top **195 rows of the screen (~22%)** off
the frame edge and bringing the wrist and sleeve in. `ken` then runs `o`, starting at 1.16, so
it is cropped harder still at the top of the scene where the chips arrive.

**Verified on the rendered frame** (`snapshots/qa/b2/frame-01-at-40.19s.png`): the phone is cut
by the top edge AND the right edge, the hand and sleeve are the largest object, and the frame
reads *a phone in a hand*, not *an empty screen*. The knob also pays twice: median 35.80 →
33.89, p10 19.56 → 16.34, pulling the chapter's brightest frame — the one cell fin-assets
reports jumping out of the composed run — back toward the run, which is where §10 routes a chip
cascade (*near-flat, low-key*).

**Layout: archetype C, NOT centred, and the chips are in the LEFT column.** §7's own rule is
that the artefact occupies the other side; here the artefact is the photograph's phone at screen
x ≈ 1067-1812, so the 880px `.arch-c .stack` column (x150-1030) clears it entirely and the split
is not a hole. The chips ride blockframe's own `.row` inside that stack — not a hand-rolled flex
row, and not ch3's absolutely-positioned `.v-chiprow`, which exists only because archetype D
hangs its stack at the top. **Nothing is drawn on the phone's screen**: chips over that glass
would be fabricating what the feed shows, which is what `never_a_screen_vs_sound_off_2026-08-09`
forbids on an internet beat.

### 6 · Timings, anchors and cascades — all measured, none authored

Rebased on `timing.json`'s own `scene_start` for 4.1 (**248.539s**). Root **87.279s**. The
generator asserts, one joint at a time, that (a) every scene overlaps its successor by exactly
0.45s, (b) adjacent scenes alternate track 1/2, (c) each gap equals the SHIPPED cut's gap to
1e-9, and (d) the last scene lands on the chapter root. Durations that sum correctly while
internal cuts drift cannot be produced by this file.

**`faster_whisper` `base.en`, word timestamps, on this cut's own clips** (clips start at scene
+0.25, MEDIUM `lead_in_seconds`):

| line | anchor word | clip onset | scene offset | §5's fallback |
|---|---|---|---|---|
| 4.1 | `$5` | 0.000 | +0.25 → **FLOORED to +1.90** | — |
| 4.2 | `$1.5` (of "one and a half million") | 4.700 | **+4.95** | +5.18 (0.23s late) |
| 4.3 | `4%` | 1.800 | +2.05 (the rate pulse is a FIXED +1.90, so it leads its word by 0.15s) | — |
| 4.7 | `tank` / `12%` | 0.520 / 1.520 | +0.77 / **+1.77** | — |
| 4.11 | `13` | 2.800 | **+3.05** | — |

4.1 is floored and it is declared: the line opens *on* the figure, which is before cue 2 has put
the provenance on screen, and §5's floor exists for exactly that case.

**The cascade is speech-anchored — `owed.cascade_offsets_ignore_the_voice` is paid, not
inherited.** Three separate `pop()` calls at three measured word onsets, never
`popEach(S.sN + 1.10, …, 0.6)`: `10` at 2.420s into the clip, `12` at 3.320, `shortcut` at 5.060
⇒ **+2.67 / +3.57 / +5.31**. Gaps 0.90 and 1.74 — the shape of this sentence, not a template's
0.6. **`tools/tts/clauses.py --n 3` was run and its answer was rejected with its own docstring
as the reason**: it returned +0.25 / +3.51 / +4.61, and its first cell is **2.4s early** because
this sentence's first pause-separated part is *"Somewhere on your feed there is a payout
advertised at"* and not a named item — the exact failure the tool warns against forcing. Two of
three corroborate within 0.7s. Word onsets win on this line, the same call ch3 made on 3.3. The
third chip is a quoted advertising phrase that is never spoken, so it is bound to *shortcut*.

**The hold, built as one shot the first time** (`chapters._carry_forward_en_ch1_to_ch2_ch6` —
s3/s4 cost three rounds): s41 and s42 are ONE photograph (s42.jpg is the recorded derived crop
`crop=1600:900:280:186` of s41's source), under ONE chained `plateKen` — 1.00→1.08 then
**1.08→1.16, picked up at exactly the value s41 ended on** — sharing ONE ground (`#0f3a20`, the
hottest green in the video, spent here and nowhere else). A generator assert throws if the two
endpoints ever stop matching or if the pair ever acquires two grounds. The joint emits no
`transition` (the cut's `cues-tables.json` already lists the pair under `holds`; that file was
**not** touched). The measure bar is **HELD** at s41's 0.7640 as an inline `scaleX` with no
`span()` call — re-filling a bar that did not change would assert a second climb.

**§9a arithmetic, asserted:** 920px = $1,963,375, so $1,500,000 ⇒ scaleX **0.7640** = 702.9px.
The generator recomputes `corpus / 1,963,375` from the rendered string and throws if either half
of the pair is edited alone (gotcha 7).

### 7 · Sound — derived, and it reproduces §7's own column

`tools/audio/cues.py` reads the file `build.mjs` just wrote, so the cue list and the markup come
from one derivation of `timing.json`. **24 cues over 87.279s** (one per 3.6s; the reference is
en ch1's 22 in 57.2s). The bed is overridden to `bed-tension` in the generator, not hand-edited
into the artefact. `assets/audio.json` is deleted before regeneration, so the run that fixes a
gap cannot die on the artefact it is fixing.

Derived cue per scene against storyboard §7's `sfx` column: s40 **dry** ✓ · s41 **hero** ✓ ·
s42 **dry + no joint (hold)** ✓ · s43 reveal ✓ · s44 reveal ✓ · s45 **chip ×3** ✓ · s46
**reveal** (bound to the band under the drawn layer) ✓ · s47 reveal ✓ · s48 reveal ✓ · s49
**tick** ✓ · s50 **dry** ✓ · s51 reveal ✓ · s52 **stamp** ✓. **Thirteen of thirteen match.**
`cue_min_gap_seconds` re-validated against the shipped file: clean.

The s49 `tick` is derivable because the quotient takes a `pulse` when it finishes doubling —
a real beat on the element that just changed, not a cue invented to satisfy a table.

⚠ **`owed.cue_rung_5_does_two_jobs` has its ch4 instance and it is unchanged, deliberately.**
s41 carries the chapter's one genuine measure bar (`span("#s41-mf")`) and emits **no tick**,
because `hero` matches first in a ladder that picks exactly one cue per scene. `hero` is the
correct cue for s41, so nothing is wrong on this frame; the defect is that the bar is silent.
Not a thing to change with chapters mid-flight.

### 8 · Checks

- **`npm run check` → `Check passed`. Lint 0 errors / 4 warnings / 2 infos · Runtime 0/0 ·
  Layout 0 errors / 9 infos · Motion 0/0 · Contrast 12/12 WCAG AA.** Every warning is the
  family every chapter of this run carries and none is new: `composition_file_too_large`,
  two × `timeline_track_too_dense`, and `composition_heavy_overlay_count_high` at **26** —
  which is exactly 13 `.scrim` + 13 `.glow`, two per scene, i.e. the arithmetic
  `owed.overlay_count_in_the_assembled_master` is tracking. The 9 layout infos are all
  `container_overflow #sN-bg`, which is `.bg`'s declared `inset:-8%` ken box and is by design.
  **No design token was edited to satisfy anything.** `known_benign` is untouched (still empty).
- `pipeline_check check build --chapter 4` → **PASS build-en**.
- `check_vo_frame --chapter 4` → **PASS**, 13 scenes cross-checked against their VO lines.
- **The rate asserts** (carried forward verbatim from ch2/ch3 so `check_vo_frame` can read
  `RATE` and `MARKER` back out of the same block) are live on four branches in this chapter:
  s41's corpus + `.sub` rate; s42's corpus + derived income + the inline `#s42-rate` span;
  **s40's derived `$5,000 A MONTH` with NO rate**, routed by §4 to the explicit-marker branch
  and paid for by `BLS` in its foot; and s40's `$6,545` BILL token, paid for by the same foot.
  One deletion would fire two branches, which is the point of the arrangement.
- **Font subset:** dumped from `tools/scaffold/assets/fonts/NotoSansFinance-var.woff2` with
  fontTools at this build — **97 codepoints**, matching ch3's constant exactly. Every on-screen
  string is checked against it, plus the `/` `?` `₹` and Devanagari bans. §3's exception is
  honoured: **`$5,000 / MONTH` renders as `$5,000 A MONTH`**, and `DIVIDED BY` is used on s43
  and s48 as the same file's own solidus convention.
- **§3c:** all 13 scenes carry `has-photo` and a real full-bleed `.bg`; `arch`/`ground`/`art`
  come from §7's per-scene row; **no rail** — no chapter title, no scene counter, no slide
  number, nothing chapter-aware on screen anywhere. `#root class="cut-en"` present (1 match),
  which is the whole watermark and is visible bottom-right in all 15 reviewed frames.

### 9 · The 15 frames, per batch, all opened

| dir | frames | at (s) | what was checked |
|---|---|---|---|
| `snapshots/qa/b1` | 5 | 3.20 · 13.45 · 17.65 · 23.92 · 30.62 | s40 settle, s41 (countUp caught mid-settle at exactly its end — resampled), s42 hold + held bar, s43, s44 |
| `snapshots/qa/b2` | 6 | 13.60 · 40.19 · 44.22 · 47.91 · 54.15 · 61.69 | s41 settled at `$1,500,000`, s45 framing, **s46 (F1 found here)**, s47, s48, s49 fraction |
| `snapshots/qa/b2zoom` | 1 | 44.22, `--zoom 300,760,1100,340` | confirmed the stray block was drawn, not photographic |
| `snapshots/qa/b3` | 4 | 44.22 · 69.87 · 75.27 · 82.61 | **s46 re-verified after the fix**, s50, s51 (banner crop confirmed), s52 |

Every frame's `.stack` sits inside the safe area; nothing overflows; the watermark is on all 15.
The s49 fraction renders exactly as authored — numerator constant, ghost holding where the price
was, denominator halved from its left edge, quotient doubled from its left edge — which is what
made F1 diagnosable in the first place: two constructions in one file, one right and one wrong.

## Changed

- `studio/videos/passive-income-number-en-ch4/build.mjs` — **new**, the generator.
- `studio/videos/passive-income-number-en-ch4/index.html` — **new**, generated (531 lines).
- `studio/videos/passive-income-number-en-ch4/assets/audio.json` — **new**, derived by
  `tools/audio/cues.py`, bed overridden to `bed-tension`.
- `studio/videos/passive-income-number-en-ch4/package.json`, `package-lock.json` — copied from
  `tools/scaffold/`; `node_modules/` installed.
- `studio/videos/passive-income-number-en-ch4/assets/js` — **new symlink** to
  `tools/scaffold/assets/js` (gsap 3, motion.js, lottie.min.js — the last unused here).
- `studio/videos/passive-income-number-en-ch4/snapshots/qa/{b1,b2,b2zoom,b3}/` — 15 QA frames.
- This log.

**Not touched:** `assets-ch4/` (no image was fetched, replaced, cropped, renamed or deleted;
all 13 jpgs, all 13 `.src` files, `CREDITS.txt`, `manifest.json` and `IMAGES-ch4.jpg` are
byte-unchanged from fin-assets attempt 2), the cut's `assets/cues-tables.json`, `tools/`,
`assets/icons/`, `assets/lottie/`, `.claude/`, and every other chapter project. No icon was
added to the library — the tank is a scene-specific mechanism authored in a plate's coordinate
space, not a reusable colourless glyph, so `assets/icons/` is the wrong home for it.

## Owed

1. **⚠ A MOTION-SYSTEM GAP, DECLARED NOT IMPROVISED AROUND: `motion.js` has `span()` (scaleX)
   and no scaleY equivalent.** A level that genuinely slides down a vessel is not expressible
   with the shipped vocabulary. The exit/fade construction used here is the nearest thing that
   exists AND it is the better reading for a decorative level, so nothing was added to the
   system and nothing was redefined inline — but a `spanY(sel, at, dur, from, to)` is the honest
   gap, and the next drawn layer that needs a vertical proportion will hit it. Adding it is a
   deliberate edit to `tools/scaffold/assets/js/motion.js`, which this stage may not write.
2. **⚠ HOUSE RULE FOR EVERY LATER DRAWN LAYER, from F1: percentage `transform-origin` on an SVG
   rect driven by GSAP is only safe in the `0% 50%` form.** Authored as `50% 0%`, the tank's
   stream rendered ~860px left of its own `x` with every check green. The control is not a
   checker — it is the max-density snapshot pass, which is the only thing that caught it. Worth
   a line in `design-chapter-archetypes`'s gotcha list; it is the ninth of that kind.
3. **`owed.en_ch2_s10_tank_layer` is now cheap and the reason is structural.** s10 is `arch D`
   like s46, so `tank()` transplants with its origin constant unchanged and
   `{drop: false, widen: false}`. The only ch2-side work is the `.band` at `z-index: 0` before
   the plate, dropping `.centred` from s10, and re-checking that scene's cue list — s10 already
   emits a `transition` on its `s10-bg2` framing swap, so the band fade must not create a second
   content cue inside `cue_min_gap_seconds`.
4. **`chapters._carry_forward_en_ch4_to_ch5_s57` is NOT closed by the drawn tank.** The drawn
   stream widens, which is the only part of *"12% is a wider tap"* this chapter can pay; the
   PHOTOGRAPH under it is still a thin trickle, so §10's four-frame flow ladder still has
   nothing left to escalate down to at 5.5. Re-brief s57 against the FILE.
5. **s42's crop is a 1.18× push on the whole frame, not the dial** (fin-assets §4.3, confirmed
   here on the rendered hold). The continuous-push requirement is met and visible; *arriving at
   the dial* is not. Design call for fin-review.
6. **s49 is the chapter's most graphic photograph carrying its only 52% mechanism.** White
   spray-paint diagonals under an orthogonal drawn fraction; the `.band` is what makes it
   survivable and it looks right at 61.69s, but only the encode settles it. Look at it once.
7. **s51's front-row faces are distinct**, against §10's *"faces indistinct"* — unchanged and
   unresolved, declared by fin-assets and visible on the rendered frame. Historical claim,
   1931, NARA public domain. fin-review's call.
8. **s45's sound-off risk is left open on purpose**, as the ruling intends. The framing
   instruction is executed and the frame now reads *a phone in a hand*; whether a switched-off
   screen still argues with *"somewhere on your feed"* is settled on the encode.
9. **s40's `o` ken is a resolution of a storyboard contradiction, not a preference** (see
   Failed). If fin-review prefers the other resolution, the change is one character in
   `build.mjs` and it moves the repeat from a chapter boundary into the middle of the chapter.
10. **The s39→s40 SHOVE is not in this project** and must be added by `tools/cut_assemble.py`;
    s52 correctly carries its bare `scene_duration` with no successor to dissolve into.
