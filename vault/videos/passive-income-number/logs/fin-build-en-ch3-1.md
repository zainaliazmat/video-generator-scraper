---
summary: fin-build en chapter 3 — 16 scenes / 96.601s, s24–s39, `hyperframes check` clean (0 errors, 14/14 AA), `check_vo_frame` PASS, `cues.py` exit 0 (min gap 1.100s), `pipeline_check check build --chapter 3` PASS. All three rate-assert branches re-proven to throw on this file. One drawn layer (s30 `housing-share`, 33.4% exactly). The chapter's payoff is named as s34 and scores pass · #2 median · #1 p10 · +70.6 step-in — and the chapter's LARGEST figure, s31 ($656,650), is escalated: it sits on the chapter's luminance floor (composed median 7.1, LAST of 16, p10 0.0), which is the s21 shape the CEO blocked in ch2 and is not fixable from this stage.
updated: 2026-08-08
source: fin-build attempt 1, chapter 3, en cut — run.json rulings_binding_on_both_cuts (both) + chapters.en.1/2/3 + storyboard-en.md §1–§13 + script-en.md 3.1–3.16 + timing.json + studio/videos/passive-income-number-en-ch2/build.mjs (structure) + tools/scaffold/assets/chapter-design.css + knowledge/design-chapter-archetypes.md
stage: fin-build, cut en, chapter 3, attempt 1
---

# fin-build — passive-income-number / en / chapter 3 / attempt 1

**Project:** `studio/videos/passive-income-number-en-ch3/`
**Artefacts:** `build.mjs` · `index.html` · `assets/audio.json` · `snapshots/qa/b1…b5`
**16 scenes · 96.601s · offset 151.938s · scenes s24–s39 · lines 3.1–3.16.**

| check | result |
|---|---|
| `npm run check` (`hyperframes check`) | **PASS** — 0 errors, 4 warnings, 13 infos; **14/14 text checks WCAG AA** |
| `python3 tools/check_vo_frame.py … --chapter 3` | **PASS** — 16 scenes cross-checked against their VO lines |
| `python3 tools/audio/cues.py … -en-ch3` | **exit 0** — 24 cues, min gap **1.100s** against the 0.8 floor |
| `python3 tools/pipeline_check.py check build … --chapter 3` | **PASS** |

The four warnings and thirteen infos are the class ch1 and ch2 both carry
(`composition_file_too_large`, two `timeline_track_too_dense`,
`composition_heavy_overlay_count_high`, per-scene `container_overflow` on every
`inset:-8%` `.bg`, and `#s30-plate` 60px off-canvas — which is the `.p-b`
constant `1120 + 860 = 1980`, not a build decision). **`known_benign` is empty
and stays empty**; nothing was edited to satisfy the checker and no design token
was touched.

---

## 1. The scaffold, and what was deliberately NOT copied from ch2

`package.json` + `package-lock.json` copied from `tools/scaffold/`, `npm i -D`
(hyperframes 0.7.66 off the committed lockfile, never `npx --yes`). `assets/` is
the ch1/ch2 layout fin-assets already created: symlinks to the scaffold's
`blockframe.css`, `chapter-design.css`, `fonts`, `img`, and to the cut's
`voice/`. **No CDN or network reference of any kind** — `check_build`'s own
`https?://` sweep is clean.

⚠ **`assets/js/motion.js` was REFRESHED from the scaffold.** fin-assets copied
`js/` from ch2, and ch2's copy predates today's `fade()` change — it still fades
to a hardcoded 1. ch3 now carries the current file, so an authored partial
opacity is live here (verified: the "AUTHORED OPACITY" block is present).
`gsap.min.js` was already byte-identical.
**For the orchestrator, not actioned by me:**
`grep -L "AUTHORED OPACITY" studio/videos/passive-income-number-*/assets/js/motion.js`
still returns `passive-income-number-en-ch2` and `passive-income-number-hi`. ch2
is harmless as it stands (its s14 fix landed on `fill-opacity`, which `fade()`
never touched), but a re-render of ch2 would run the old helper, and the full-cut
assembly needs one motion.js, not two.

Both of ch2's local CSS patches are gone and so is the "SYSTEM GAP" comment.
Verified they are genuinely upstream rather than merely absent: this build's
centred archetype-B focals sit on frame centre in the snapshots (s25, s27, s29,
s31) with the `.measure.under` track — which centres itself at
`left: calc(50% - 460px)` — agreeing with them, and s25/s27/s31's footers use the
full 1500px, which is the `.scene.centred.arch-b` cap doing its job.

The composition's own inline `<style>` holds exactly two things: the four plate
rects, and one `.v-` component (below).

## 2. Timing — generated, never typed

Every `data-start` / `data-duration` / `data-framings`, both JS maps, all sixteen
`<audio>` rows and the root duration come from
`../passive-income-number-en/assets/voice/timing.json`, rebased by ONE constant
(151.938s = timing.json's own `scene_start` for 3.1). Four asserts run at build
and throw rather than ship:

1. every adjacent pair overlaps by **exactly 0.450s** (`data-duration` = own hold
   + T on s24–s38; **s39 carries its bare 3.543s**, because a chapter has no
   successor to dissolve into and `cut_assemble.py` adds the +0.45 back);
2. **the GAP between consecutive `data-start`s equals the shipped cut's own gap
   to 1e-9** — this is the assert that catches the failure mode the storyboard
   warns about, where a chapter's durations sum correctly while every internal
   cut has drifted. Max drift **0.000s** on all fifteen joints;
3. adjacent scenes never share a `data-track-index` (2/1/2/1… by scene parity);
4. `data-framings` partitions its scene and no single framing exceeds 9.0s
   (longest in ch3 is s26 at 7.905s; the cut's only breach is 2.2, in ch2).

Chapter root **96.601s** = s39's start (93.058) + its 3.543. Nothing in this
chapter was re-timed for a layout, and no layout was changed by a timing.

## 3. Anchors are MEASURED, not interpolated

Every figure and every cascade cell is anchored to the voice, with
`faster-whisper base.en` word timestamps on this cut's own clips. Clips start at
scene +0.25 (MEDIUM `lead_in_seconds`).

| line | word | clip | scene anchor | §5's published fallback |
|---|---|---|---|---|
| 3.2 | "$13" | 2.200 | **+2.45** | — |
| 3.3 | "$1" | 1.600 | **+1.85** | — |
| 3.4 | "$333" | 3.320 | **+3.57** | +3.73 |
| 3.6 | "$26" | 0.680 | +0.93 → **FLOORED +1.90** | — |
| 3.7 | "a third" | 0.480 | +0.73 → **FLOORED +1.90** | — |
| 3.8 | "$657" | 2.980 | **+3.23** | +3.32 |
| 3.13 | "30" | 3.940 | **+4.19** | — |

**Two are floored and both are declared.** 3.6 and 3.7 speak their figure inside
the first second of the clip, before cue 2 has put the provenance (3.6's BLS
foot) or the qualifier (3.7's `$2,189 a month`) on screen. §5's +1.90 floor
exists for exactly that; the number lands ~1s after its word rather than on top
of its own foot. The alternative — dropping the foot to cue 3 — would put a BLS
numerator bare on screen for two seconds, which is what the BILL branch of the
assert exists to prevent.

**3.13 lands late by design and will sheet wrong.** `tools/chapter_sheet.py`
samples a non-Lottie scene at +2.6s and s36's focal arrives at +4.19, so the
sheet will show `LIMIT TWO` + a foot and no `30 YEARS`. That is not a defect —
judge s36 from the mp4. Same call ch2 recorded for s16 at +3.33.

### The cascade — new tooling, used, and one place it was overruled

```
python3 tools/tts/clauses.py passive-income-number --cut en --line 3.3 --cells 4 --offsets
  +1.47 +4.50 +5.07 +5.88
```

s26's four chips fire on **four separate `pop()` calls** at **+4.37 / +5.01 /
+5.89 / +6.71**, which are the faster-whisper onsets of `Payment` / `insurance` /
`gas` / `repairs`. `clauses.py` corroborates three of the four within 0.13s and
its cell 1 is 2.9s early — because 3.3's second pause-separated part is *"that is
about eleven hundred and ten dollars a month"*, which is not a named item, and
the sentence only has five detectable boundaries for four things. That is the
tool's own documented limit ("re-read the line rather than anchoring to a number
this did not find"), not a disagreement about method: the requirement is measured
onsets and one call per cell, and both hold. Gaps come out 0.64 / 0.88 / 0.82 —
the shape of the sentence, not a template's 0.6. The last chip settles at +7.16
inside a 7.905s scene.

`cues.py` reads this form and would emit one chip per call; s26 is on the
storyboard's DRY list, so it emits none and the cascade is silent by choice.

## 4. The rate asserts — carried verbatim, all three branches re-proven

The ch2 block is carried **byte-for-byte**, including its third `BILL` branch,
because `check_vo_frame.py` reads `RATE` and `MARKER` back out of it — a
per-chapter copy that drifts is worse than no assert. What goes live in ch3:

| branch | fires on | satisfied by |
|---|---|---|
| CORPUS | s27 `$332,950`, s31 `$656,650` | `#s27-rate` / `#s31-rate`, a 40px `.sub` reading `AT A 4.0% WITHDRAWAL RATE`, on screen at +1.10 — **before** the figure lands |
| DERIVED | s30 `$2,189 a month` | the BLS provenance in the same frame (`MARKER`) |
| BILL | s25 `$13,318`, s26 `$1,110`, s29 `$26,266`, s30 `$2,189` | s25/s29 provenance · s26 derivation (`$13,318 divided by 12`) · s30 both |

**Proven, not assumed.** `$656,650 $2,500 a month $13,318` was planted into
**s33's kicker** — a scene with no rate, no marker and no derivation, so it can
actually fail — and `hyperframes check` returned one hard `page_error` carrying
three separate messages:

```
RATE ASSERT FAILED — s33 renders $656,650 with no #s33-rate carrying a rate ·
s33 renders the derived income $2,500 a month with neither a rate nor an
ILLUSTRATIVE marker in frame · s33 renders the published figure $13,318 with no
rate, no provenance and no derivation in frame
```

Reverted by regenerating from `build.mjs`; the clean run is the one recorded
above. `check_vo_frame` PASS covers the half the in-page assert structurally
cannot see — 3.2, 3.4, 3.6, 3.7 and 3.8 all trip its MAGNITUDE pattern and all
five frames carry a rate or a marker.

## 5. THE PAYOFF CLAUSE — scored, and one escalation

Measured the way ch2's payoff table was: the graded cover-crop of each source
(`grayscale(.32) brightness(.62) contrast(1.05)`, then the central 86.2% that
`inset:-8%` actually shows), with the `background-position` each scene actually
ships. Median ranks; `p90 − p50` reported beside it; near-zero spread claimed as
no credit anywhere.

| scene | p10 | **median** | p90−p50 | med rank | p10 rank | median step in |
|---|---|---|---|---|---|---|
| s24 | 11.8 | 37.7 | 45.1 | 13 | 10 | — |
| s25 | 30.5 | 92.0 | 38.1 | 6 | 3 | +54.3 |
| s26 | 19.6 | 92.4 | 31.9 | 5 | 7 | +0.5 |
| s27 | 0.0 | 25.5 | 50.2 | 14 | 14 | −67.0 |
| s28 | 28.5 | 95.7 | 25.0 | 4 | 6 | +70.2 |
| s29 | 15.2 | 58.5 | 77.4 | 10 | 8 | −37.2 |
| s30 | 13.2 | 59.8 | 15.4 | 9 | 9 | +1.4 |
| **s31** | **0.0** | **7.1** | **95.0** | **16** | **15** | **−52.8** |
| s32 | 29.1 | 90.9 | 35.5 | 7 | 4 | +83.8 |
| s33 | 0.0 | 57.5 | 32.6 | 11 | 16 | −33.4 |
| **s34** | **92.1** | **128.1** | **7.8** | **2** | **1** | **+70.6** |
| s35 | 2.9 | 139.2 | 5.5 | 1 | 13 | +11.0 |
| s36 | 6.9 | 49.8 | 63.5 | 12 | 12 | −89.4 |
| s37 | 7.5 | 21.6 | 102.7 | 15 | 11 | −28.2 |
| s38 | 28.7 | 77.4 | 28.3 | 8 | 5 | +55.9 |
| s39 | 30.7 | 102.5 | 13.0 | 3 | 2 | +25.0 |

**These are PREDICTED, not rendered** — fin-render must settle them from the
encode. Three predictions have already been wrong on this run, and every one was
wrong in the optimistic direction.

### The payoff frame is **s34 (3.11)**, and it satisfies all four clauses

Top quartile = `ceil(16/4)` = **4** (above the floor of 3).

| clause | s34 | verdict |
|---|---|---|
| sound-off pass | a contract page with a pen lying on it | **PASS** |
| top quartile on median | 128.1, **#2 of 16** | **PASS** |
| #1 or #2 on p10 | 92.1, **#1 by 61.6 points** | **PASS** |
| non-negative median step in | s33 57.5 → s34 128.1 = **+70.6** | **PASS** |

**Why s34 is the payoff, argued before it was scored.** ch3 delivers no hero
number and no new method — rungs two and three re-run chapter 2's arithmetic, and
3.16 hands the number the viewer came for to chapter 4 in so many words. What
this chapter uniquely contributes is the papers' criticism **of themselves**, and
3.11 is its one verbatim HARD-primary quotation, the sentence the whole
fine-print run exists to put on screen. The composition serves the clauses by
doing nothing clever: the frame is `.centred` archetype C with `art-off`, so the
quotation sits over the middle of the most legible photograph in the chapter, the
ken is a 1.00→1.16 push that never leaves the lit page, and no scrim, band or
per-scene grade is added — the p10 of 92.1 is the photograph's, not a layout's.

**Checked against the alternative readings, so the designation is not a dodge:**

- **s35 (3.12, "every rung here is a BEFORE-TAX number")** — the consequence, and
  arguably the beat that re-prices every number in the video. Median 139.2 is
  **#1 of 16**, step-in +11.0, sound-off unmistakable — but **p10 2.9 is 13th**.
  White forms on a black ground: high median, no floor. Fails clause 3.
- **s32 (3.9, "say it slowly")** — the chapter's emotional landing. Median 90.9
  (7th) and p10 29.1 (4th). Fails clauses 2 and 3.
- **s31 (3.8)** — the chapter's biggest figure. Below.

### ⚠ ESCALATION: s31 is the s21 shape, and this stage cannot fix it

`$656,650`, the largest figure in the chapter and rung three of the ladder, sits
on **the chapter's luminance floor**: composed median **7.1, LAST of sixteen**,
p10 **0.0** (tied last), `p90 − p50` **95.0**, the chapter's widest spread — and
it *arrives* on the chapter's second-largest drop, **−52.8** out of s30. Scored
against the clause it is pass / 16th / 15th / negative: **three of four fail.**
The photograph is a brass-collared knob on a sunlit door with the right 45% of
the frame in pure black; the high p90 of 102.0 is the specular knob, which is
exactly the artefact p90 was retired for.

**Every composition lever was tried and none of them is honest here.** The source
is 1880×1256 against a 16:9 box, so `cover` matches WIDTH and there is **no
horizontal slack at all**; vertical framing moves the median by half a point
(6.7 / 7.1 / 7.2 for top / centre / bottom), so no `background-position` is set,
because setting one would be theatre. Darkening is forbidden and lightening is
not a lever that exists. The ken runs `o` — it opens tighter and left, on the lit
half, and pulls back — which is the alternation rule already giving the frame the
better of its two seconds. Under the ruling's own words the lever **is** the
photograph, and the photograph is fin-assets' to change. Declared here so the
gate rules on it with the number in hand rather than discovering it in the draft.
Its neighbour **s27** (`$332,950`, rung two, median 25.5 / 14th, p10 0.0) is the
same object family and the same problem one step milder.

## 6. Carry-forwards, each implemented

- **ch3's OPENER SHOWS A SUBJECT.** s24 is a red hatchback at the kerb, not a
  surface. Verified on the frame at +1.85: the car is bottom-left and unmistakable
  under the type. `bgpos: center bottom` spends all 196px of the source's vertical
  slack on the empty night sky — median 26.6 → **37.7** (+11.1) at unchanged p10 —
  and `ken` runs `i`, which ends **tighter and left**, i.e. on the car
  (`ken(zoomIn)` moves the element right, so the window sees content to its left).
  It is still the chapter's darkest opener, which §11 asks for.
- **p90 retired.** No p90 rank appears anywhere in this build's reasoning; the
  table above ranks median and reports `p90 − p50` beside it. Note s34 and s35's
  spreads of 7.8 and 5.5 are *reported*, not claimed as a credit.
- **The tank object family.** No scene in s24–s39 touches the vessel / tap / flow
  family, so nothing here rhymes on it and nothing here constrains s46 / s47 /
  s57 further. The sharpened brief (a **lever in a readable position** plus flow)
  is untouched by this chapter.
- **fin-assets' two build facts.** s26's photograph carries no slips, so the four
  items live only in the chip cascade and the cascade is load-bearing copy — it is
  not cut, and it is speech-anchored so each word arrives with its chip. **No
  per-scene `filter:` override anywhere**; the locked grade stands unamended for
  all sixteen scenes.

## 7. §8 density — one drawn layer, and what was declined

`housing-share` on **s30** — §8's own budget for ch3 is exactly one, and this is
the storyboard's assignment.

```
p-b · viewBox 0 0 800 610 · xMidYMid meet
track x 40..760 (720px) — filled EXACTLY 0.334 (BLS CE 2024) = 240.5px
```

The `SHARE` constant drives both the tick's x position and the `span()` endpoint,
so the drawing and its animation cannot disagree. `meet` on an 860×610 plate
scales 1.0 and centres, putting the whole mechanism at screen x 1190–1910 —
inside the canvas, which is gotcha 8 respected (`.p-b` maps viewBox x 1:1 and
anything past vx 800 does not exist on the encode). 120px tall, **solid fills
only**, ghost track a filled rect at `fill-opacity 0.55` — ch2's s14 value, chosen
there because `--ink` at full weight out-shouts `--target`; `fade()` no longer
clobbers an authored `opacity`, but fill-opacity is still the right lever because
it leaves the entrance fade free to run 0→1. `.art-lift` because the p-b plate
sits on the bright orange sky; **not `.band`**, which is bottom 54% and cannot
reach a rect at y150–760. Assembled by +2.95, inside the +3.3 sheet window.

**Declined, so the choice is on the record:**

- **3.3's four costs** — the count is four chips on ladder C, and the photograph
  was deliberately routed to a subject with nothing countable in it. Drawing four
  boxes duplicates the chips, which is rule 8 one level up.
- **3.13's thirty years** — a drawn clock over a photographed clock is the
  ghost-envelope-over-an-envelope failure by name.
- **3.11 / 3.14's fine print** — a quotation is not a proportion. §8's own test
  ("what does the art assert that the picture cannot") returns nothing.
- **3.4 / 3.8's two corpora** — they already carry the §9a measure bar, which is
  the cut's one climb device and is not a per-chapter drawn layer.

**§9a measure bar, on the two rung frames only.** 920px = $1,963,375, so
$332,950 → scaleX **0.1696** (156.0px) and $656,650 → **0.3345** (307.7px), both
asserted against `corpus / 1,963,375` at build to 5e-4. Rung one was 119.1px in
ch2, so the visible climb is 119 → 156 → 308. Numerator and denominator are one
arithmetic and neither moves without the other.

## 8. Sound — 24 cues, and one reconciliation in the cut's own table

`assets/audio.json` is generated by `tools/audio/cues.py` from the file
`build.mjs` has just written, so the cue list and the markup are the same
derivation of timing.json. **24 cues** over 96.601s (16 joints, 7 `reveal`, 1
`stamp`), min gap **1.100s**, bed **`bed-tension`** (§2 / §13 D12 — cues.py
defaults to `bed-resolve` and the build overrides it, rather than the generated
file being hand-edited). No music or SFX `<audio>` rows in `index.html`; the
composition is voice-only, one row per line on track 10.

⚠ **`studio/videos/passive-income-number-en/assets/cues-tables.json` was edited:
`s27` and `s31` added to `dry`.** The storyboard disagrees with itself. §2's prose
declares *"Rungs two, three and five (s27, s31, s67)"* dry and §7's `sfx` column
prints `—` for both; the JSON block those ids were transcribed into carries only
`s67`. Two sources against one, and the dissenting one contains `s67` from the
same sentence — a transcription drop, not a decision. Fixed in the table file
because that file is the fact's one home, with the reasoning recorded in a
`_dry_s27_s31_reconciled` key beside it. Design reason is §2's own: if every rung
rings, the ladder has no shape, and the measure bar is what gives it one
visually. **Blast radius is ch3 only** — s27 and s31 are ch3 scenes, so ch1's and
ch2's derived lists are byte-unchanged. Left as-is, the two rungs would each have
emitted a `hero`, which is three `hero`s on the ladder's first three rungs.

## 9. The max-density snapshot pass — what was actually looked at

Each scene sampled at its **last cue's settle time** (cue start + its own
duration), which is the frame carrying the most elements it will ever carry.
**One `-o` directory per batch**, never reused:

| batch | dir | times (s) | frames on disk | frames I opened |
|---|---|---|---|---|
| b1 | `snapshots/qa/b1` | 1.85 · 6.64 · 16.27 · 21.87 | 4 | contact sheet + `frame-02` full-res = **5 reads covering 4 frames** |
| b2 | `snapshots/qa/b2` | 25.37 · 33.19 · 39.60 · 47.61 | 4 | contact sheet + `frame-02` full-res = **5 reads covering 4 frames** |
| b3 | `snapshots/qa/b3` | 51.40 · 58.00 · 62.22 · 68.54 | 4 | contact sheet = **4 frames** |
| b4 | `snapshots/qa/b4` | 78.19 · 82.10 · 88.55 · 94.16 | 4 | contact sheet = **4 frames** |
| b5 | `snapshots/qa/b5` | 16.27 (re-shot after the s26 fix) | 1 | full-res = **1 frame** |

**17 frames on disk, all 17 looked at** — 4 contact sheets read as grids (each
cell is 603×339, enough for overflow, collision and safe-area) plus 3 full-res
pulls where the grid could not settle it (s26's cascade, s30's drawn bar, s26
again after the fix). The CLI did not time out on any batch; the retry loop was in
place and unused.

⚠ A first attempt at this pass silently produced the wrong frames: `set -- $spec`
split the batch spec so `--at` never reached the CLI and each dir got five
evenly-spaced defaults instead. Caught by reading the filenames, not the log.
Recorded because it is precisely the "reported N frames eyeballed when 8 survived"
failure in a different costume — **read the emitted filenames, not the exit code.**

### The one defect it caught, and the fix

**s26's `brule` ran straight through the `$1,110` glyphs.** Archetype D's rule is
meant to compress the type band; ch1 uses `top: 252px` on 1.2 and 1.6, but those
scenes' focal is a chip row. Here `.arch-d .stack` starts at y144 (110px scene
padding + 34px margin) and the 112px `.huge` occupies y198–308, so 252 is inside
it. Moved to **400**, which clears the foot's baseline at y361 and still sits
196px above the cascade at y596. Re-shot at 16.27s and confirmed clean. Nothing
else moved; no timing, no copy, no ken.

### What the pass confirmed

All sixteen `.stack`s inside the safe area, nothing overflowing, no element
crossing another, the `cut-en` watermark riding bottom-right on every frame.
Specifically: s25's foot wraps to two lines at the 1500px cap and orphans `2025`
(cosmetic, same shape as ch2's s15 foot); s34 and s37's 76px quotations set to
two and three lines respectively inside the 1500px stack; s27 and s31's measure
bars read as a visible climb; s30's bar shows an amber third against a grey
ghost with the tick on the boundary.

## 10. For fin-editor — flagged before review finds them

1. **s31 (and s27).** §5 above. The chapter's largest figure on the chapter's
   darkest photograph. Not fixable from the build.
2. **s30's `.art-lift` panel edge is visible.** The plate is a lifted panel by
   design, but this still is a smooth sky gradient, so the rect's left edge at
   x1120 reads as a tonal step. The bottom edge is masked by the roof silhouette.
   Removing the lift makes an amber bar sit on graded amber sky and the mechanism
   stops reading — that trade was taken deliberately, and `.art-lift` is the
   corner-plate mechanism ch2's carry-forward says it is. Worth a ruling.
3. **s34's legible words are `9. Insurance` and `10. Assignment`**, under a
   quotation about *taxes or transaction costs*. §10's rule (no legible title,
   figure or agency name) holds and fin-assets cleared it, but the one word a
   viewer reads is not one of the two the sentence names. This is the payoff
   frame, so it is the one to look at hardest.
4. **s35's sticky note reads "Tax time!" in handwriting**, top-right and fairly
   prominent, under *"Every rung here is a BEFORE-TAX number."* The tone is
   jauntier than the line. Also the form is legibly dated `2020` — fin-assets'
   own declared call, and no ch3 line makes a year claim.
5. **s36 will sheet without its focal** (+4.19 against the sheet's +2.6). Judge
   from the mp4.
6. **s26's cascade is now the only place the four costs exist.** If a later pass
   is tempted to thin the frame, the chips are the copy, not decoration.
7. **The curly quotes are verified, not assumed.** `“ ” ‘ ’` are all present in
   the 97-codepoint subset (dumped with fontTools at build), which closes
   storyboard §14 item 6. s34 and s37 therefore render the typographic marks the
   storyboard asked for. ch2's straight quotes stay as they are — those are cited
   paper titles in a 26px foot, not display quotations. Every on-screen glyph in
   this chapter is asserted against the dumped subset at build, so a tofu box is
   now unrepresentable rather than merely unlikely.
8. **`countUp` is money-only here.** `33.4%` and `30 YEARS` take a bare `pop()`.
   `countUp` rounds with `Math.round`, so counting to 33.4 would settle on
   `33%` — a *different* published figure, printed on the settle frame, with every
   check green. Worth carrying to ch4–ch6: any one-decimal focal must not count.

## 11. Nothing I improvised, and one thing I did not build

The archetype row, the grounds, the `centred` flags, the ken alternation, the
focal ladder, the chip count, the drawn layer and the measure values are
storyboard §7/§8/§9a/§11 verbatim; the copy is script-en.md's own cue blocks. The
one component this composition owns is `.v-chiprow` / `.v-chiprow-r` — the same
absolutely-positioned band cascade en ch1 uses on 1.2 and 1.6, with the rows
declared explicitly as 2+2 because `.row` wraps and four chips left to themselves
orphan 3+1 with no checker flagging it. No system helper was redefined inline and
no previous video's `index.html` was read for technique.

**The SHOVE at s39 → s40 is not built here.** It is a chapter boundary: s40 lives
in ch4, so `sceneTransitions` is called with no `acts` argument and s39 carries
its bare duration. `tools/cut_assemble.py` is what puts the two projects next to
each other, and the shove belongs to that step.
