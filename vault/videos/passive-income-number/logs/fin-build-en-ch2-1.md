---
summary: fin-build en chapter 2 — 15 scenes / 105.518s, s9–s23, `hyperframes check` clean (0 errors, 11/11 AA), `check_vo_frame` PASS, `pipeline_check check build --chapter 2` PASS. Both ch1 CEO carry-forwards implemented and measured: the s10 noun is now THE TAP with the tank/tap pair named on screen as the word is spoken, and ch2's opener measures p90 57 against ch1's 45 with a chapter range of 35–60 against ch1's 40–49. The rate assert goes live here and gained a third branch for published numerators; all three proven to fire. Two system gaps reported, not worked around.
updated: 2026-08-08
source: studio/videos/passive-income-number-en-ch2/ · storyboard-en.md §1–§12 · script-en.md ch2 · timing.json · run.json constraints + chapters.en.1 carry-forwards · tools/format.json chapter_design
stage: fin-build, cut en, chapter 2, attempt 1
---

# fin-build — en · chapter 2 · attempt 1

**15 scenes · s9–s23 · lines 2.1–2.15 · 105.518s · chapter offset 46.420s.**
`hyperframes check` **passes**: 0 lint errors, Runtime 0/0, Layout 0/0, Motion 0/0,
**Contrast 11/11 AA**.

## The two rulings from the ch1 CEO gate

### 1. THE TANK — the noun on screen is **THE TAP**

fin-assets could not source a tank in 6 sheets / 36 candidates and resolved s10 as a
receding row of heavy brass taps on a steel manifold over a steel trough. I read both
files at full resolution before deciding: there is no vessel in either frame and no crop
of that source will produce one, so the choice was never "which tank" but "which noun".

Implemented in the COPY, per the ruling, not by re-fetching:

| element | string | cue |
|---|---|---|
| `#s10-kick` | `THE TAP` | +0.30 |
| `#s10-stmt` | `How much can you draw each year without emptying it` (script verbatim) | +1.10 |
| **`#s10-sub`** | **`THE TANK IS WHAT YOU SAVED · THE TAP IS WHAT YOU DRAW`** | **+1.90** |

The sub is variant A's own cue 3 (+1.90 `fade`, 0.5s), so no ladder was invented for it.
**Measured, not argued:** faster-whisper on `2.2.mp3` puts "tank" at 1.960–2.140s into the
clip; the clip starts at scene +0.25, so the word occupies scene **+2.21 to +2.39** and the
sub's fade completes at **+2.40**. The word TANK is legible on screen in the same half
second it is spoken, and the frame simultaneously tells the viewer what the tank is (the
thing you saved, off screen) and what the tap is (this, on screen). That converts the
mismatch into the metaphor's own definition instead of leaving it as a contradiction.

> ⚠ **CARRY FORWARD — the noun s46 / s47 / s57 inherit is THE TAP.** Object family: a
> brass tap on plain steel under workshop light, tap position carrying the beat. Not a
> tank silhouette; those chapters must not be briefed for one, and their on-screen nouns
> must say *tap* / *stream* / *what you draw*, never *tank*. (§10's returning-objects
> table already declares this fallback; this build has now spent it, so it is a fact and
> no longer an option.)

### 2. TONE — ch2 opens measurably lighter, and is not one band

No per-scene grade override exists anywhere in this file and none is permitted. The three
levers used are all inside the locked grade: the **photograph** (fin-assets' own YHIGH:
s9 203, s11 211, s13 211, s19 228), the **ground** (`#2a2113` amber against ch1's
`#161f2b` cool first light), and the **role** — s9/s10/s11 are `--target` scenes carrying
an amber `--tint` on scrim layer 1 and an amber `--gl` glow, where seven of ch1's eight
scenes carry neither.

p90 luma, measured identically on each chapter's own max-density frames (ch1's `qa/b1`,
this chapter's `qa/b1`+`qa/b2`):

| | opener | range | mean |
|---|---|---|---|
| **ch1** (s1–s8) | 45 | **40 – 49** (spread 9) | 44.2 |
| **ch2** (s9–s23) | **57** | **35 – 60** (spread 25) | 48.2 |

The opening frame is **+12** on ch1's opener and above ch1's entire range. The chapter's
spread is **2.8×** ch1's, so the rung-one drop at s21 (p90 44) now lands inside a chapter
that has visibly moved, not inside one temperature. The brightest frame of the video so
far is s16 (60), which is where the finding lands, and the darkest is s20 (35), the ÷12
measurement — that ordering is the argument, not an accident.

## Timing — generated, asserted, nothing re-timed

Every `data-start` / `data-duration` / `data-framings`, the `S` and `D` maps, the fifteen
`<audio>` rows and the root duration come from one derivation of `timing.json` in
`build.mjs`. Re-running `node build.mjs` reproduces `index.html` and `assets/audio.json`
**byte-identically** (md5 `51db52e9…` / `ab9e5c50…` before and after), so the four copies
cannot have drifted apart by hand.

| | s9 | s10 | s11 | s12 | s13 | s14 | s15 | s16 | s17 | s18 | s19 | s20 | s21 | s22 | s23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| start | 0 | 5.162 | 15.758 | 23.924 | 27.781 | 34.667 | 41.737 | 48.806 | 55.17 | 62.658 | 70.276 | 76.822 | 84.31 | 90.387 | 97.769 |
| own | 5.162 | 10.596 | 8.167 | 3.856 | 6.887 | 7.069 | 7.069 | 6.364 | 7.487 | 7.618 | 6.547 | 7.487 | 6.077 | 7.383 | **7.749** |
| track | 1 | 2 | 1 | 2 | 1 | 2 | 1 | 2 | 1 | 2 | 1 | 2 | 1 | 2 | 1 |

All fourteen joints overlap by exactly 0.450s; tracks alternate 1/2 and chain correctly
onto ch1's s8 (track 2); s23 carries its **bare** duration. Root 105.518 = 97.769 + 7.749
= line 3.1's `scene_start` minus the offset. The gap asserts ch1 wired are carried
verbatim, including the one that compares each joint against the SHIPPED cut's own gap at
1e-9 — the ±1 ms roundings in `timing.json` (2.4, 2.6, 2.7, 2.10, 2.12, 2.15) pass
because both sides are computed the same way, and a real re-time would not.

**One assert had to be generalised, not relaxed.** ch1 asserts `scene_duration <= 9.0`;
2.2 is 10.596s, the cut's only breach. The thing that must clear 9.0 is the longest
**single framing**, which is what §6a's resolution buys, so the assert now checks each
declared framing *and* that the framings partition the scene — a cosmetic split cannot
duck it.

### 2.2's framing swap is measured, and it moved

§5 lists the swap as anchored on "draw" with `f 0.62` (+6.324) **as a fallback**, and says
fin-build resolves it against whisper. It aligned: "draw" starts 6.760s into the clip =
scene **+7.010**. The 0.40s cross-dissolve therefore starts at **+6.810** so its midpoint —
the perceptual cut — lands on the word. Framings are **6.810 + 3.786** (was 6.324 + 4.272);
both clear 9.0, they sum to 10.596, and no scene duration changed. Snapshot at 12.172s
confirms the swap reads as a continuation of the push, not a flash.

Every other anchored figure is likewise measured, not interpolated:

| line | word | into clip | scene offset | §5's published fallback |
|---|---|---|---|---|
| 2.8 | "95" | 3.080 | **+3.33** | +3.25 |
| 2.11 | "$10" | 1.960 | **+2.21** | — (not published) |
| 2.12 | "$847" | 2.020 | **+2.27** | — (not published) |
| 2.13 | "$254" | 2.300 | **+2.55** | +2.62 |

All four clear variant B's +1.90 floor.

## The rate asserts — live, extended, and proven to fire

ch1's block is carried forward verbatim (CORPUS / RATE / DERIVED / MARKER) and gained a
**third branch**, because ch1's two are deliberately narrow and this is the first chapter
where that shows:

- **CORPUS** (8 tokens) → needs a `#sN-rate` element carrying `4.0% | 3.11% | 1.08%`.
  Fires on s21 and s22 here, and both carry one — s21 as a 40px `.sub` at +1.10 (on screen
  *before* the figure lands at +2.55), s22 as §4's inline span inside the focal.
- **DERIVED** (`$N a month`) → rate or `ILLUSTRATIVE | BLS | CONSUMER EXPENDITURE`.
- **BILL — new.** `$10,169` and `$847` are published numerators. §4 is right that the
  corpus branch must not fire on them (demanding a withdrawal rate beside a BLS figure
  would be dishonest), but *"must not demand a rate"* is not *"may be bare"* — under ch1's
  block both could have rendered with no foot at all and passed. A BILL must now carry, in
  frame, a rate, the published provenance, or its own derivation. s19 carries `BLS
  Consumer Expenditures`; s20 carries `$10,169 divided by 12`. Extend **BILL**, not CORPUS,
  as chapters 3–6 land their numerators.

**Proven, not assumed.** I planted `$1,500,000 $2,500 a month $13,318` into s12's kicker
(a scene with no `#sN-rate`) and re-ran the gate:

```
✗ page_error: RATE ASSERT FAILED — s12 renders $1,500,000 with no #s12-rate carrying a
  rate · s12 renders the derived income $2,500 a month with neither a rate nor an
  ILLUSTRATIVE marker in frame · s12 renders the published figure $13,318 with no rate,
  no provenance and no derivation in frame
```

All three branches fired and `hyperframes check` turned the throw into a hard error.
Restored with `node build.mjs`, md5 back to `51db52e9…`.

*(A first attempt planted the same string into s21's kicker and correctly produced
nothing — s21 already has a rate in frame, so every branch is satisfied. Worth recording:
a negative control has to be planted in a scene that can actually fail.)*

### `check_vo_frame` — PASS

```
python3 tools/check_vo_frame.py passive-income-number --cut en --chapter 2
PASS check_vo_frame — passive-income-number en, 15 scenes cross-checked against their VO lines
```

Its `MAGNITUDE` pattern fires on three of this chapter's fifteen VO lines — 2.11 ("ten
**thousand**"), 2.13 and 2.14 ("two hundred fifty-four **thousand** dollars") — and all
three frames satisfy it: s19 through `BLS`, s21 and s22 through `4.0%`. `--selftest` also
run and passing. **No `--ack` was used and none was needed.**

One thing worth flagging rather than leaving for the audit to rediscover: **2.12 does not
trip the checker and arguably should.** It speaks "about eight hundred and forty-seven
dollars a month" — a money figure over a frame — but `MAGNITUDE` is
`thousand|lakh|crore|million|billion` and `CURRENCY_FIGURE` needs digits, and "eight
hundred" is neither. The frame is honest anyway (its foot states the derivation, which is
also what my new BILL branch asserts), so this is **not a defect in this build** — it is a
blind spot in the checker that a future chapter could fall into with a bare frame. Adding
`hundred` to `MAGNITUDE` would over-flag heavily; the durable fix is probably to have the
BILL branch's token list drive a VO cross-check too. Not mine to build mid-run.

## The frame pass — 48 frames, seven batches, one `-o` directory each

`hyperframes snapshot` wipes its `-o` directory on every invocation, so every batch has
its own: `snapshots/qa/b1 … b7`. **Frames I actually opened and looked at, per batch:**

| batch | frames | what it samples | opened at full 1920×1080 | via contact sheet |
|---|---|---|---|---|
| b1 | 8 | s9–s15 last-cue (max density), + s10 both framings | **8 of 8** | 8 |
| b2 | 8 | s16–s23 last-cue (max density) | **6 of 8** | 8 |
| b3 | 2 | `--zoom` crop on s19 / s21's figure + foot | **1 of 2** | 2 |
| b4 | 8 | the three re-broken statements, s18 mid-fill and complete, s20/s21/s22/s23 re-checked after the two layout fixes | 2 of 8 (+ 2 measured numerically) | 8 |
| b5 | 8 | first frame at 0.05s, seven joints at +0.38, the 2.2 swap mid-dissolve | 0 of 8 | 8 |
| b6 | 8 | the remaining seven joints at +0.38 | 0 of 8 | 8 |
| b7 | 6 | s16 at the contact-sheet +2.6 sample, s21 at the +4.5 countUp settle, and four tail frames | 0 of 6 | 6 |

That is **17 frames read at full resolution and 48 read on contact sheets**, all 48
reviewed. Batches b1 and b4 are the ones the design decisions were made from.

What the frames establish:

1. **Every scene paints a real photograph.** 16 `.bg` elements, 16 distinct md5s, all
   visibly graded stills. The first frame of the chapter (0.05s) is already a photograph.
2. **Every joint is a live cross-dissolve.** All fourteen sampled at +0.38: the outgoing
   scene's type ghosted over the incoming photograph with the incoming kicker already up.
   Never a fade against black.
3. **The tail is correct for a chapter.** At 102.0 / 105.0 / 105.48 / 105.517 s23 is fully
   painted and not fading — a chapter that faded out would put a black flash inside the
   assembled cut.
4. **The drawn layers assemble and are on canvas.** The survival grid finishes at +2.49
   (95 solid cells, 5 ghosts, the ghosts reading clearly at .22); the division block
   completes at +3.20. Measured numerically off the encode rather than eyeballed: the
   corpus block spans screen x **390–1789 = exactly 1400px = 25.00 × the 56px bill block**,
   and its left edge is **pinned at 390 through the wipe**, so `transform-origin: 0% 50%`
   is reaching gsap on an SVG rect and the 25× resolves rightwards instead of growing out
   of its own middle.
5. **The comma-descender defect is not reintroduced.** The system fix
   (`.arch-b .mega { padding-bottom: .11em }`) is picked up by symlink — `assets/*.css`
   point at `tools/scaffold/`, byte-identical to it. This chapter renders no `.mega`, so
   the fix is inert here; the live question was whether `.huge` at 112px has the same
   collision. It does not: zoomed to 3× device scale on s19, the comma of `$10,169` clears
   the foot line with visible air. Recorded so ch3–ch6 do not re-derive it.

## Two things fixed after looking at the frames, and one of them is a SYSTEM gap

### A. `.scene.centred .stack` does not reset archetype B's `padding-left` — report upstream

`.arch-b .stack` carries `padding-left: 62px` (the air the creator asked for on
2026-08-05) and `.scene.centred .stack` re-centres the stack **without resetting it**, so
every centred archetype-B scene renders its "centred" content **31px right of frame
centre**. Invisible alone. Visible on **s21**, where `.measure.under` is positioned at
`left: calc(50% - 460px)` and is therefore genuinely centred — so the ladder bar and the
figure above it disagreed by 31px on the chapter's hero frame.

Patched locally with one line in the composition's own `<style>`, clearly labelled as a
system gap rather than a `.v-` one-off. **The real home for the fix is
`tools/scaffold/assets/chapter-design.css`** — it affects four scenes here and every
B scene of chapters 3–6, plus every measure-bar frame in the cut (s27, s31, s41, s42,
s67). I did not edit `tools/`; that is outside this stage.

### B. Three statements needed an explicit line break

The browser broke `Four percent is a finding. Not a law.` as *"…Not a"* / *"law."* and
`4.0% — a finding with a date. Not a promise.` as *"…date. Not"* / *"a promise."* — a
four-character orphan and a split noun phrase. `build.mjs` now honours a `\n` in a `stmt`
and renders it as `<br>`, with the newline flattened out before the focal-size rule runs,
so **the type ladder is untouched** (all three stay at their computed size). Used on three
scenes: 2.3, 2.9, and 2.10 — where `annual bill DIVIDED BY 4.0%` / `= the money behind it`
also reads as an equation rather than as a wrapped sentence. A line break is a build
decision; the copy is still the script's, character for character.

## Sound — derived, not hand-typed

`build.mjs` shells out to `tools/audio/cues.py` against the `index.html` it has just
written and overrides one key (`music: bed-tension`, §2/D12 — the generator hardcodes
`bed-resolve`). Deriving inside the build is what guarantees the cue list and the markup
came from the same derivation of `timing.json`; ch1 reproduced the generator's rules by
hand and had to diff them afterwards. `cues-tables.json` already existed from ch1 and was
not touched.

**25 cues over 105.5s, one per 4.1s** — in line with §2's ~3.9s expectation. 15 joints, 1
framing swap, 9 content cues (6 `reveal`, 1 `stamp` on s17, 1 `hero` on s21, 1 `tick`).
The five declared DRY scenes (s12, s14, s16, s19, s20 — the papers' evidence run and both
BLS numerators) emit their joint and nothing else, exactly as §2 asks.

**Two places the generator's own rules diverge from §7's `sfx` column.** Both are cues.py
behaving as documented; I took the generator, which §2 names as the home:

- **s10** — §7 says `reveal + swap`; cues.py emits only the swap `transition`, because a
  scene that changed its photograph mid-line has already had something happen and does not
  take a second cue. This is the shape of ch1's own approved list at s3 and s5.
- **s22** — §7 says `reveal`; cues.py emits `tick`, because the scene's one emphasis call
  is `pulse("#s22-rate")` and `pulse` is bound to `tick` in `kit.json`'s helper column. A
  tick under the spoken rate is defensible — arguably better than a reveal 0.8s earlier —
  but the editor should rule, because **every §4 "span in the focal" scene will do this**
  (s42, s60 with two spans, and s76).

## Findings that are NOT defects in this build

**`composition_heavy_overlay_count_high` — a NEW warning, and it will get worse.**
The composition carries 30 elements with radial-gradient CSS: exactly `.scrim` + `.glow`
× 15 scenes, both system layers on every scene of every chapter. ch1 has 16 and stayed
under the threshold. The linter's field note says ~40 such elements can make the capture
layer return solid black for half a render, reproducing identically through drawElement,
forced screenshot and snapshot. **`tools/cut_assemble.py` folds all 81 scenes into ONE
composition — that is 162.** I cannot fix it here: the only lever is removing a design
token layer from every scene, which is exactly the edit the checker-is-evidence rule
forbids. Flagged for fin-render and for whoever owns the assembly: if the full cut
captures black, this warning is where it was announced. `known_benign` is `[]` and I added
nothing to it; no design token was touched.

The other three warnings (`composition_file_too_large` 521 lines,
`timeline_track_too_dense` ×2 at 8 and 7 elements) and the 11 layout infos are the shape
this pipeline's one-file-per-chapter build always has. Nine of the infos are
`container_overflow` on `#sN-bg` — that IS the ken push scaling the background past the
section that clips it. Two are new and both are the archetype's own geometry:
`#s16-plate` / `#s16-pin` overflow right by **60px**, because `format.json`'s `.p-b` rect
is `left:1120 width:860` on a 1920 frame. I checked what that costs rather than assuming:
the grid is authored in a `0 0 800 610` viewBox with `preserveAspectRatio="xMidYMid meet"`
(not `slice`, which would scale 1.075× and crop 45px of height off a deliberately square
grid), so it renders 1:1 centred at screen x 1150–1950, and the grid itself occupies
x 1150–1846 — **fully on canvas with 74px to spare.** What hangs off the edge is the empty
aperture, which has no background under `.has-photo`. Gotcha 8 respected.

**Contrast is 11/11 AA and Layout ran** — there are 0 lint errors, so neither pass was
skipped, which is the trap that let four earlier cuts ship with WCAG never executed.

## Resolved for later chapters (dumped, not guessed)

**The 97-codepoint font subset was dumped with fontTools at build**, which settles §14's
open item 6 and one of §3's assumptions:

- `“ ” ‘ ’` **are all present.** s34 and s37 (ch3) can use typographic quotation marks;
  the straight-quote fallback is not needed. Straight `"` renders correctly here on s13
  and s15 — verified on the encode, not assumed.
- `/` and `?` **are also present.** §3's ban on them is therefore a COPY rule (`·` is this
  cut's separator, and the cut asks no rhetorical question on screen), not a tofu risk.
  I kept the ban in the build guard for consistency with ch1's rendered copy, so s16's
  foot reads `at 50-50` rather than `at 50/50`. A later chapter may relax it knowingly;
  it must not relax it by accident.
- Also present and used: `—` `·` `%` `$` `:` `;` `(` `)` `=`. Absent and still forbidden:
  `< > ~ × ≈ → ▶ ¢`.

## Deviations and observations for fin-editor

1. **s10's kicker is `THE TAP`, not the script's `THE TANK`** — the CEO ruling, above.
   This is the one place a `head:` string diverges from `script-en.md`, and the divergence
   is the fix.
2. **s10 gains a `#s10-sub`** the storyboard's §7 row does not list. It is variant A's
   own cue 3, it keeps the scene at 3 countable elements + photo, and it is what makes the
   ruling legible.
3. **s22 emits `tick`, not `reveal`** — above; needs a ruling because it generalises to
   every span-in-focal scene.
4. **s20 is the chapter's weakest frame** (fin-assets flagged it): a brown/grey/red plaid
   shirt across ~45% of it and p90 35, the darkest in the chapter. The type reads and the
   figure is legible, but it is the one frame where the photograph is doing least.
5. **s16's number arrives after the contact sheet's +2.6 sample.** The grid is fully
   assembled at +2.6 but `95%` lands at +3.33. `chapter_sheet.py`'s countUp settle (+4.5,
   fixed earlier this run) covers it; I sampled 51.41s to confirm the frame is not
   half-built, only pre-number.
6. **s9's photograph is a large near-flat plane.** It is the brightest frame of the
   chapter and it carries the tone step the CEO asked for, but the notebook fills the
   frame with little internal structure. Fine at 5.2s under a pull-back; worth a look in
   the draft.

## System gaps found (reported, not improvised)

1. **`.scene.centred .stack` must reset `padding-left`** — §A above. Home:
   `tools/scaffold/assets/chapter-design.css`. Affects every centred B scene in the cut.
2. **The system has no class for §4's "span in the focal" rate form.** `pulse` is a
   transform and transforms do not apply to a non-replaced inline box, so a bare `<span>`
   would carry the colour, satisfy the assert, and simply never animate — with every check
   green. Declared here as `.v-rate { display: inline-block }`. Since §4 uses this form on
   s22, s42, s60 (twice) and s76, it is a system component wearing a one-off's clothes and
   belongs in `blockframe.css`.
3. **`check_vo_frame`'s `MAGNITUDE` misses "hundred"** — above, s20's shape. Not a defect
   today; a blind spot for later chapters.

Nothing was missing from the motion vocabulary: `sceneTransitions`, `ken`, `plateKen`,
`rise`, `pop`, `popEach`, `fade`, `fill`, `pulse`, `span`, `countUp`, `draw`(unused),
`register` covered this chapter with **no helper redefined inline**. Three one-off
components live in the composition's own `<style>` after the system links: `.v-rate`,
`.arch-b .v-widefocal`, and the labelled system patch.

## Result

**15 scenes · s9–s23 · 105.518s** — chapter 2 of six, offset 46.420s, concatenates
frame-exact. `hyperframes check` passes; `check_vo_frame` passes;
`pipeline_check check build --slug passive-income-number --cut en --chapter 2` → **PASS
build-en**.
