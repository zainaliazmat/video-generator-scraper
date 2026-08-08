---
summary: Full rebuild of japanese-money-methods-en on **blockframe-9** — the ledger-rail composition of attempt 1 was discarded, not patched. 92 scenes, 626.743s, `#root class="cut-en"`, SUBSCRIBE as a `.cta` block (verified orange), 3 `data-framings`, the s77+s78 hold on one file, `assets/audio.json` = bed-resolve + the storyboard's re-bound 24 cues. `npm run check` passes with the browser passes ACTUALLY running (0 lint errors / 0 layout errors / 11-11 WCAG AA); `pipeline_check check build` PASS. 100 max-density frames captured across 9 batch dirs and all reviewed. One NEW checker warning is escalated rather than absorbed — `composition_heavy_overlay_count_high` (92 scrims), which is a render-stage risk, not a design defect.
updated: 2026-08-01
source: storyboard-en.md §1–§12 (blockframe-9 rewrite) · script-en.md `[rail …]` / `[RAIL OFF …]` cue blocks · assets/voice/timing.json (626.743s, 92 lines) · tools/format.json · tools/scaffold/assets/{blockframe.css,js/motion.js} · tools/audio/kit.json · assets/icons/
stage: fin-build, cut en, attempt 2 (full rebuild, new architecture)
---

# fin-build — japanese-money-methods-en, attempt 2 (blockframe-9 rebuild)

## Result

| | |
|---|---|
| Artifacts | `studio/videos/japanese-money-methods-en/index.html` · `assets/audio.json` |
| Architecture | **`blockframe-9`** — `<div id="root" class="cut-en">`, **no body class** (`format.json architectures.blockframe-9.body_class` is `""`) |
| Scenes / duration | **92** · **626.743s** = `timing.json total` = s92 end (620.849 + 5.894) |
| `npm run check` | **passed** — lint **0 errors** / 4 warnings / 2 info · runtime 0 · layout **0 errors**, 9 info · motion 0 · contrast **11/11 WCAG AA** |
| `pipeline_check check build` | **PASS build-en** |
| Generator | one node pass over `timing.json` + storyboard §7 + the 92 script cue blocks. **No timing number and no on-screen string typed by hand.** |

Everything timed is generated and cross-asserted before the file is written: the four homes
(`<section data-start/data-duration>`, the JS `S` map, the 92 `<audio>` rows, root
`data-duration`) all come from one pass, and the generator refuses to emit if any of ~10
invariants fail (overlap = 0.45s, track parity, ken alternation, framing sums, focal inside
its scene, cue gaps ≥ 0.8s, every image and mp3 on disk).

**Scaffold**: the cut directory was already correctly scaffolded — `assets/blockframe.css`,
`assets/js/{gsap.min.js,motion.js}`, `assets/fonts/NotoSansFinance-var.woff2`,
`assets/img/{grain.png,wm-en.png}` and `package.json` all **byte-match `tools/scaffold/`**
(checked with `cmp`, not assumed); `package-lock.json` differs only in the project `name`
field and pins the same `hyperframes 0.7.66`. Nothing was re-copied because nothing had
drifted. **0 network references** in the composition.

## What changed against attempt 1 — everything except the words and the photographs

`ledger-rail` is gone. The rail column, `.railno`/`.railcol`/`.raillabel`, the 740px
`.v-panel`, `.v-hair`, `.v-col`, `.v-stmt`/`.md`/`.lg`, `.v-bleed`/`.v-full` and the whole
`RAIL OFF` mechanism were **deleted, not adapted** — `grep -c rail index.html` is **0**. The
composition's inline `<style>` is now a **single rule**:

```css
#root { position: relative; width: 1920px; height: 1080px; overflow: hidden; background: var(--bg); }
```

That is the one thing `blockframe.css` does not own (it styles everything *inside* `#root`
but never sizes the stage, and both `.scene{position:absolute}` and the `#root::after`
watermark need a positioned, sized root). **Still owed to `tools/scaffold/`** — this is the
third cut to write it by hand. No `.v-*` one-off component exists in this build at all; the
system carried every element.

Per scene: `.bg` (full-bleed, `inset:-8%`, the grade) → optional `.bg`#2/#3 → `.scrim` (four
layers, layer 1 takes `--tint`) → `.grain` → `.stack` with at most three content elements
(`kicker`, focal, one of `foot`/`icon`) against the ceiling of 6.

## The two things the run directive singled out — both verified in pixels

1. **`#root` carries `cut-en`.** Confirmed in the rendered frames, not just in the source:
   the mark bottom-right is the **pink-ring @moneymavens101 avatar** (`wm-en.png`), present
   in all 100 captured frames including the SOLO hook. `check build` asserts the class; the
   frames assert the file.
2. **SUBSCRIBE is a `.cta` block.** `<p class="cta" id="s91-cta">SUBSCRIBE</p>` — the
   component sets `background:var(--pop); color:#0d1017` itself, so the white-SUBSCRIBE
   defect of attempt 1 is structurally unrepresentable. **Verified orange-on-dark in the
   617.96s frame.** `.popc` now exists in the scaffold and is available for pop-coloured
   *text*; this cut has none, exactly as the storyboard says.

## Type, colour and the anti-sameness device

- **75 type-A** statements at `.huge` **@76px**, **9 type-B** figures at `.huge` **112px**,
  **7 SOLO** (s1, s17, s33, s43, s65, s77, s90) with the stack emptied — no kicker, focal at
  **88px**, except s17's `.mega` **@240px**, used **exactly once in the video**. **1 CTA**
  at `.cta` 46px. **Every size is a `type_ladder_px` value; nothing interpolated, nothing
  focal below 76.**
- **49 scenes carry a `--tint`**, derived from the role colour by the §1a rule (fund .10 /
  warn .12 / target .12 / pop .13), SOLO scenes at the top of their band (.13). 43 scenes
  have no role and therefore no tint. *(§1a's prose says "47 scenes, no role"; the actual
  count from §7's own focal column is 43. Arithmetic slip in the storyboard, not a design
  question — the per-scene rule is applied exactly as written.)*
- **One role colour per scene, ever.** `--pop` appears once (s91). The one red `num`
  (`23.2%`, s30) and the red `OVER 20%` (s72) are the two declared exceptions.
- **Font subset checked programmatically before writing**: every on-screen character across
  all 203 text nodes against the face's **97 codepoints** — **0 missing**. No CJK anywhere;
  romaji only. The kanji are inside the photographs (s76/s77/s88 — and now also s32's second
  framing, a Japanese street noticeboard; still photographic, never composition text).

## The cue ladder as built

| cue | element | time | helper |
|---|---|---|---|
| — | `sN-bg` (+ `bg2`/`bg3`) | scene start, running `data-duration` | `ken` 1.0↔1.16, direction per §7, **through the dissolve** |
| 1 | `sN-head` `.kicker` | +0.30 (84 scenes) | `rise` y24 0.50s |
| 2 | focal, fixed | +1.10 | `rise` y40 0.70s |
| 2′/2″ | focal, anchored (19 scenes) | the storyboard's absolute time | `pop` 0.60s (`back.out`) — or `rise` on s1/s51/s77 |
| 3 | `sN-foot` / `sN-icon` | +2.10, **or `focal + 0.80` if +2.10 lands inside `cue_min_gap_seconds`** | `fade` 0.40 / `draw` 0.70 / `pop` 0.60 |

**The `+2.10` foot rule needed one derived guard and this is the record of it.** Six scenes
(s25, s30, s31, s51, s73, s91) have an anchored focal within 0.8s of the fixed foot slot;
the foot is pushed to `focal + 0.80` there. The guard is *symmetric*, which is why **s17
still puts its foot at +2.10, ahead of the num at +6.09** — the gap is 3.99s, well clear, and
the citation reading as the set-up for the 240px slam is better than a 1.1s foot crammed into
the scene's tail. Every foot on every scene ends up ≥1.0s before its scene's own end
(asserted, not eyeballed).

**`countUp` is not used, deliberately.** §2 asks for `countUp`+`pop` on s13/s25/s30/s55, but
all four figures are decimals (`37.8%`, `51.0%`, `23.2%`, `62.2%`) and `motion.js countUp`
rounds through `Math.round`, so it would count `0 → 51` and land on `51%`, losing the `.0`
the citation depends on. They arrive with `pop` alone. `.huge`/`.mega` already carry
`tabular-nums`; the `en-US` grouping is baked into the strings the script wrote (no figure in
this cut is ≥1,000 anyway).

**Transitions.** `sceneTransitions([…92 ids…], S, { acts: ["s34", "s74"] })` — 89 dissolves
and the **two** shoves the storyboard names (out of the debunk, into the unpromised fourth).
`data-duration = scene_duration + 0.45` on s1–s91, s92 bare; adjacent scenes alternate track
1/2 by parity (**0 clashes**). *Sixteen boundaries measure 0.451s rather than 0.450s because
`timing.json` rounds `scene_duration` and the next `scene_start` independently; `check_build`
tolerates 0.05 and passes. The alternative — deriving durations from the next start — would
have made the `<section>` disagree with the `<audio>` row, which is worse.*

**The three hold pairs** (s1→s2, s65→s66, s77→s78): the partner scene points at the **same
file**, `background-size:auto 130%` with a re-aimed `background-position`, and its `ken` runs
in the **same direction**. **s78 has no file of its own** — both halves are
`assets/img/s77.jpg`, exactly as the directive requires. Verified visually as a continuous
zoom, not a self-dissolve: s2 at 6.0s is a tighter frame of s1 at 2.65s; s66 at 446.0s lands
on the $100 note's portrait and serial `LD33979666D`; s78 at 527.3s is closer on the basin's
still water than s77 at 520.1s.

**The three `data-framings`**, each partitioning its own scene and each verified firing:
`s32 "5.66,2.48"` (8.140 ✓, swap → the poster noticeboard at 211.10), `s36
"2.74,2.03,3.031"` (7.801 ✓, → cotton field 238.05, → semi truck 240.08), `s79 "5.50,2.849"`
(8.349 ✓, → apartment block 537.37). `bg2`/`bg3` run their **own `ken` over the full scene
span** while at `opacity:0`, so when they cross-dissolve in they are already at the
underlying layer's scale — the push never restarts. Longest single framing anywhere: 8.167s
(s47), against `max_scene_seconds` 9.0.

## Audio

`assets/audio.json` = `{"music": "bed-resolve", "sfx": [24 cues]}`, sorted, **the
storyboard's re-bound ladder** — not the old one. The 11 cues §2 re-bound are honoured at the
ladder rather than dropped: the five `stamp` scenes (s31, s33, s43, s65, s90) enter their
focal with **`pop`**, the three `chip` scenes (s38–s40) **`pop`** their icon instead of
drawing it, and s69's `tick` fires a `pulse` on an icon that `draw`s. Closest pair **6.31s**
(#12→#13); asserted ≥0.8s in the generator. **The composition stays voice-only** — 92
`<audio>` rows on track 10, **no music and no SFX rows**; `mix.py` does the bed and the duck.
Bed length is not flagged (§2/D23 retracts that escalation: `mix.py` crossfade-laps it).

## Vector art — 5 icons, 0 Lotties, nothing new drawn

All three shapes were **already in `assets/icons/`** and were pasted verbatim with their
`i-*` ids namespaced per scene (`s24-i-shackle`, …) so the three repeated checkboxes cannot
collide: `padlock-closed` (s24, **`warnc`**), `checkbox-tick` (s38/s39/s40, `fundc`),
`reorder-rules` (s69, `fundc`). **Nothing was added to the library** — the ladder's rung 2
held. Rendered at `.icon.sm` (130px; the storyboard's "96×96" is not a system size).

Both drawn icons verified **complete and role-coloured** at full resolution: the s24 padlock
is closed and **red** at 149.5s, the s69 rules-and-arrow is **green** and whole (arrowhead
included) at 467.3s.

**One helper timing I could not satisfy exactly, stated rather than smoothed over.** §2 puts
s69's `tick` at **465.50**, and §8 says the `pulse` comes *after* the `draw`. With the icon
in cue slot 3 (+2.10 = 465.395) the four-path draw finishes at 466.635, so 465.50 is 15% into
the stroke. Moving the draw earlier would put it 0.50s from the focal and break
`cue_min_gap_seconds`; moving the pulse later would leave the SFX without its helper, which
is the exact thing §4 D0f fixed. Built as: `draw` at +2.10, `pulse` at 465.50 — GSAP tweens
`strokeDashoffset` and `scale` independently, so both run and the sound has its helper on
that element at that instant. The icon blips while completing its last stroke.

## The browser passes actually ran

`hyperframes check` reported **0 lint errors**, so `runCheckPipeline` did not short-circuit
to `emptyBrowserResult()`. Evidence that the passes executed rather than reporting a vacuous
zero: **Layout produced 9 real findings at 9 sampled times** (34.82s … 591.92s), Contrast
reported **11/11** text checks, Motion and Runtime both reported against real samples. A
skipped pass prints nothing; these printed.

All 9 layout findings are `info`-level `container_overflow` on `#sN-bg` inside its `.scene` —
that is `ken()` scaling a `inset:-8%` layer past the clipping section, which is what a Ken
Burns push is supposed to do. **Zero errors.** `known_benign` in `format.json` is empty and
stays empty: nothing was reclassified, and **no design token was edited to satisfy the
checker.**

## ⚠ NEW checker finding — escalated, not absorbed

```
⚠ composition_heavy_overlay_count_high: 92 elements carrying "heavy overlay" CSS
  (filter:blur, radial-gradient, or clip-path). Field signal: a composition with ~40
  such elements captures solid-black for the first ~half of the render, recovering
  near the end … the capture layer itself is the offender. Independent of duration.
```

The 92 are the 92 `.scrim` divs — four `radial-gradient`s each, straight out of
`blockframe.css`. **This is new to this cut and it is a direct consequence of the
architecture change**: under `ledger-rail`, `.rail .scrim { display: none }` meant attempts 1
and the whole hi cut carried **zero** heavy overlays, and the three shipped `blockframe-9`
cuts were SHORT-tier with **nine** scrims. 92 is the first time this system has been asked
for a scrim on every scene of a LONG cut.

**I did not touch it, and that is the deliberate call.** The scrim is the single reason type
is legible over 92 photographs; deleting or thinning it is a design-token edit made to please
a checker, which this stage is explicitly forbidden to do. The finding is a **warning**, not
an error; `npm run check` passes; the 100 snapshot frames render correctly, and snapshot uses
the same capture layer the warning names.

**Owed to fin-render, and it should be the first thing looked at:** inspect an early frame of
the encode (say t≈30s and t≈200s) before trusting the full master. If black frames do appear,
the fix is at `tools/scaffold/` or in the render pipeline (sub-composition split), not in this
composition — and this stage may write neither.

## QA — the max-density snapshot pass

Timestamps are each scene's **last cue + 0.55s**, clamped 0.10s inside the scene, derived
from the generated cue list rather than guessed. **One `-o` directory per batch, never
shared.**

| batch | scenes | frames on disk | reviewed |
|---|---|---|---|
| b1 | s1–s12 | 12 | 12 |
| b2 | s13–s24 | 12 | 12 |
| b3 | s25–s36 | 12 | 12 |
| b4 | s37–s48 | 12 | 12 |
| b5 | s49–s60 | 12 | 12 |
| b6 | s61–s72 | 12 | 12 |
| b7 | s73–s84 | 12 | 12 |
| b8 | s85–s92 | 8 | 8 |
| b9 | the 3 swap scenes' 2nd/3rd framings, both drawn icons complete, 2 hold partners | 8 | 8 |

**100 of 100 frames captured and reviewed** — nine contact sheets read at full size, plus
four frames opened at 1920×1080 and three cropped (the s24 padlock, the s69 arrow, the s91
CTA block). Nothing overflows; the stack, scrim, grain, tint and watermark are correctly
placed in every frame; both shoves' scenes, all four swaps and all three hold pairs land
where they were declared.

`hyperframes snapshot` threw `Navigation timeout of 10000 ms exceeded` constantly and every
batch was retried until it succeeded (b8 needed **11** tries, b9 six, b7 six, b3 three, b1/b2
one). **No batch was skipped and no frame went unreviewed.**

> **One near-miss worth writing down, because it is the failure this stage's contract exists
> to prevent.** The first batch loop was driven by `while read -r ts` over a file written
> without a trailing newline, so the shell silently dropped the **last line** and **b8 never
> ran** — the loop reported success for b1–b7 and exited. It was caught only by counting
> `frame-*.png` per directory afterwards. b8 was then run on its own (11 tries) and reviewed.
> **Count the frames on disk; never trust the loop's own exit.**

## Verified programmatically over the written file

92 `<section class="scene clip">` · 92 `<audio>` rows on track 10, voice only · root
`data-duration` **626.743** = `timing.json total` = last scene end · **0** adjacent scenes
sharing a track (46 on 1, 46 on 2) · 49 `--tint` declarations · **1** `.cta`, **1** `.mega`,
**5** `.icon` · 3 `data-framings`, each summing to its own scene ✓ · `#root class="cut-en"`,
no body class · **0** `https?://` references · **0** occurrences of `rail`.

## Divergences and judgement calls, all of them

1. **s2's role colour is `--fund`, from storyboard §7, not from the script.** The script's
   `[rail 1.2 …]` block carries no `colour:` field; §7 row 2 reads `stmt · fund`, and §1
   names "the promise" as green — 1.2 *is* the promise after the audit rewrite. Every other
   scene's role matches the script's `colour:` field exactly (diffed: 1 of 92).
2. **`countUp` unused** — decimals, see above.
3. **Foot cue guard** at `focal + 0.80` on six scenes — see above.
4. **s69 `pulse` overlaps the tail of its `draw`** — see above.
5. **The `ken` span is `data-duration`, not `scene_duration`**, so the push keeps moving
   through the 0.45s cross-dissolve instead of freezing under the incoming scene. Small
   improvement over attempt 1; it is also what makes the hold pairs read as continuous.
6. **Hold crops are `auto 130%`** (the directive's figure for s78, applied to all three for
   consistency). Every hold source is ≥1.5 aspect, so `auto 130%` covers the `inset:-8%` box
   horizontally with margin — checked against the real file dimensions, not assumed.

## System gaps — what the storyboard assumes and the system does not have

| Storyboard asks for | In the system? | Used instead |
|---|---|---|
| `#root` stage sizing | **no** (`blockframe.css` never sizes the root) | one inline rule — **owed to `tools/scaffold/`**, third cut in a row |
| `window.__timelines` init visible in the composition | `motion.js` has it, but lint only reads the composition file | one line before `register()` — **also owed to the scaffold** |
| a `countUp` that keeps one decimal | no | `pop` alone |
| `.icon` at 96×96 | no (system sizes are 220 / 130) | `.icon.sm` 130px |

Nothing else was missing. No helper and no component was redefined inline, and no `.v-*`
one-off was needed at all — which is the first time that has been true on this project.

## Owed elsewhere (not this stage's to write)

1. **`tools/scaffold/`**: the `#root` stage rule and the `window.__timelines` line. Both are
   hand-written by every cut and neither is per-video.
2. **`composition_heavy_overlay_count_high`** — see the escalation above. fin-render's call.
3. **`format.json cuts.en.chars_per_second`** is still owed its raise from 16.1; this cut is
   the third flat measurement above 17.3 (17.39 c/s). Both-or-neither: the budget formula
   first, then the key.
4. **Image content for gate ②, unchanged from attempt 1 and not fixable here** — `s79b.jpg`
   is an apartment block with no sedan, so 7.6's "the car, the apartment" anchor is carried
   by half its picture; `s39.jpg` reads screen-adjacent at full resolution and the standing
   rejection asks for a printed invoice. `s32b.jpg` is **fine now** and better than attempt 1
   reported — it is a genuine Japanese street noticeboard covered in posters, not a second
   weathered wall.
