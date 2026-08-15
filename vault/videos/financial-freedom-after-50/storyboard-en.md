---
summary: Storyboard for «The Never Too Late Guide to Financial Freedom After 50» en cut — LONG tier, 123 scenes (one VO line = one clip = one scene), `per-line-chapters` with the chapter archetype layer. Declares the four-role colour table, the per-scene arch/ground/art row, the four-cue ladder, 2 shoves + 11 two-framing scenes forced by `max_scene_seconds`, one music bed + 32 SFX cues, 6 drawn layers + 2 icons + 0 Lotties, and 126 image slots (123 bg + 3 cut-ins). Measured runtime 801.642 s (13:21.6) from timing.json.
updated: 2026-08-15
source: script-en.md (fin-script attempt 2, fin-audit passed) · studio/videos/financial-freedom-after-50-en/assets/voice/timing.json (measured, 801.642 s, 123 lines) · tools/packs/fin-storyboard.md · tools/format/fin-storyboard.json · tools/audio/kit.json · tools/scaffold/assets/{blockframe.css,chapter-design.css} · vault/videos/passive-income-number/storyboard-en.md (precedent for the archetype row)
stage: fin-storyboard, cut en, attempt 1
---

# STORYBOARD — «The Never Too Late Guide to Financial Freedom After 50» · **en** cut

**Project:** `studio/videos/financial-freedom-after-50-en/` · **Script:** `script-en.md`
**Design:** [[../../knowledge/design-finance-blockframe]] (the **dark** system), extended by
[[../../knowledge/design-chapter-archetypes]]. Do **not** use `design-techtooltester` — that is
the bright, non-finance system.
**Channel:** @moneymavens101 ($) · **Tier:** LONG · **Architecture:** **`per-line-chapters`**
(`run.json.architecture` = `format.json tiers.long.architecture`; the `blockframe-9`
`architecture_lock` belongs to the SHORT rotation and does not reach this run).
**What that means here:** there is no centred nine-segment stack and no `.rail`. The
**archetype layer owns the layout** — A/B/C/D per scene, `.has-photo` on all 123, `.centred`
wherever the archetype's other side is empty. **No chapter title, no scene counter** (archetype
box #8).
**Runtime:** **801.642 s (13:21.6)** measured · **Scenes:** 123 · **Image slots:** 126
(123 bg + 3 cut-ins) · **VO:** Brian `nPczCjzI2devNBz1zQrb`.

---

## 1. Colour semantics for THIS video

The thesis: *feeling behind at fifty is a feeling, not a fact — five moves, in order, turn what
is already there into a plan.* Roles are fixed; meanings are per-video and derived here.

| Token | This video means | Because |
|---|---|---|
| `--warn` red `#ef4444` | **what is working against you while you do nothing** — the holes in the bucket (2.4, 2.5), credit-card interest (2.6, 2.7), the surprise that becomes debt (2.12, 2.13), the unclaimed match (3.19), the one health event (4.2, 4.4), income lost to disability (4.12), long-term care (4.13, 4.14), the permanent reduction taken by claiming at 62 (5.11, 5.12) | the obstacle here is **drift**, not a villain. Red is the cost of not acting; it never marks a rule, a limit or a viewer's choice |
| `--fund` green `#22c55e` | **ground the viewer keeps or gains by acting deliberately** — control (1.7), the roadmap steps (1.9–1.11), the snowball and the cushion (2.11, 2.14–2.17), the +1% (3.20, 3.21), the fortress and the HSA (4.1, 4.6, 4.7, 4.9, 4.17, 4.18), earning longer (5.2, 5.5–5.9), the delayed credit and the larger check for life (5.13, 5.14, 5.16, 5.18, 5.19), coordination and conversions (6.9, 6.12–6.15), the recap actions (7.2, 7.4, 7.5, 7.8, 7.9) | green marks **the viewer's own hand and what it locks in**. It never marks a published figure — a limit is not an achievement |
| `--target` amber `#f59e0b` | **a published figure or rule under examination, before any decision is made** — the payoff order (2.9, 2.10), every 2026 IRS limit (3.2–3.17 figure frames), the SIMPLE-IRA exclusion (3.14), the Roth catch-up threshold (3.23–3.25), HSA eligibility and the age-55 catch-up (4.5, 4.8), the LTC option set (4.15, 4.16), the FRA mapping (5.15), the 4% guideline (6.5), the withdrawal order and RMD age (6.7, 6.8, 6.10, 6.11), the recap figures (7.3, 7.6) | amber is the thing being **weighed**. Every IRS/SSA number in the cut is amber precisely because the persona rule forbids the video recommending an action on it |
| `--pop` orange `#ff5c39` | the call to action | fixed — **exactly once**, s119 (7.12), the `.cta` block |

**The inversion trap.** `needs-vs-wants` ran amber = wants; `japanese-money-methods` ran red =
falsity-and-drain and green = the viewer's hand; `passive-income-number` ran amber = the figure
under examination. **Here green is the viewer's hand AND the outcome it locks in, and amber is
every published number without exception.** Any element that renders `$24,500` or `+24%` in
green argues against the script: those are ceilings and formulas, not achievements. Any element
that renders a *step* in amber does the same — the steps are not under examination.

**One role colour visible per scene, ever.** **44 of 123 scenes carry no role colour at all**
(`--ink` kicker, `--ink` focal, `--muted` foot) and that is correct: colour is a signifier here.

**Per-scene `--tint` is NOT used in this cut.** `--f1` (§7, §10) is the temperature carrier under
`.has-photo .field` at 38%; stacking a scrim tint of the same role colour on top double-colours
every role frame. `--tint` stays unset on all 123 sections and scrim layer 1 renders
`transparent`.

**The silent-white trap.** `.fundc` `.targetc` `.warnc` `.popc` are the text classes; `.fund`
`.warn` `.target` are component modifiers. A role token with **no colour class paints `--ink`
white and fails every check silently.** The two icons (§8) are `<svg class="icon warnc">`, not
`.warn`. `s119-cta` is a `.cta` block (it sets its own `background: var(--pop)`) and is
structurally immune.

---

## 2. Audio — one bed, 32 cues

**Music bed: `bed-resolve`.** The argument is **a habit and a fix**, not a trap or a cost.
Chapters 2 and 4 run in a cost register, but the video they serve ends on a login screen and a
sticky note. The bed is chosen for the video, not for a chapter.

**SFX budget: 32 cues across 13:21 — one per 25.1 s**, against `tiers.long.max_sfx_cues` 36.
Not a target; 36 scaled by scene count would be one hit every four scenes, which is the "every
reveal has one, so none of them means anything" failure. **No two cues inside 0.8 s** — each
scene carries at most one, and the closest pair in the cut is 1.10 s (the s72→s73 shove and
s73's own `reveal`).

Anchored times are `audio_start + f × duration` with the target word named; **`f` is a
fallback** — fin-build resolves against faster-whisper word timings and uses the fraction only
if the word fails to align. Fixed times are `scene_start + offset` from §4.

| # | scene | line | sound | helper it fires with | abs t | why this beat |
|---|---|---|---|---|---|---|
| 1 | s1 | 1.1 | `reveal` | `rise` on `s1-stmt` | 1.100 | "The ship has not sailed." — frame one sets the register |
| 2 | s3 | 1.3 | `reveal` | `rise` on `s3-stmt` | 12.156 | the payoff promise, inside the 15 s gate |
| 3 | s10 | 1.10 | `chip` | `pop` on `s10-chip1` | 57.985 | the roadmap completing — one sound for the group, not three |
| 4 | s11 | 1.11 | `stamp` | **`pop` verdict entry** on `s11-stmt` | 66.151 | "Step one." — the chapter's full stop |
| 5 | s15 | 2.4 | `reveal` | `rise` on `s15-stmt` | 90.537 | "Pouring faster does not fix a leak." |
| 6 | s17 | 2.6 | `hero` | `pop` on `s17-num` | ~106.66 (f 0.45, "wealth-killer") | the only figure in ch2 |
| 7 | s22 | 2.11 | `reveal` | `rise` on `s22-stmt` | 132.604 | the snowball — the chapter's one win |
| 8 | s25 | 2.14 | `chip` | `pop` on `s25-stmt` | 154.543 | 3–6 months, the chapter's one instruction |
| 9 | s28→s29 | 2.17→3.1 | `transition` | **SHOVE #1** | 177.332 | defence → offence |
| 10 | s36 | 3.8 | `hero` | `countUp`+`pop` on `s36-num` | ~224.20 (f 0.72, "twenty-four thousand") | the first dollar figure, on the source shot |
| 11 | s38 | 3.10 | `hero` | `pop` on `s38-num` | ~234.60 (f 0.67, "thirty-two thousand") | the first total the viewer can act on |
| 12 | s41 | 3.13 | `chip` | `pop` on `s41-chip1` | 254.279 | which plans — one sound for the row |
| 13 | s45 | 3.17 | `hero` | `pop` on `s45-num` | ~288.15 (f 0.69, "thirty-five thousand") | $35,750, the largest ceiling in the video |
| 14 | s52 | 3.24 | `stamp` | **`pop` verdict entry** on `s52-stmt` | ~334.60 (f 0.45, "must be made on a Roth") | the rule that changed |
| 15 | s55 | 4.1 | `reveal` | `rise` on `s55-stmt` | 350.194 | the fortress — ch4 opens |
| 16 | s61 | 4.7 | `chip` | `pop` on `s61-chip1` | 388.561 | the triple advantage assembling |
| 17 | s62 | 4.8 | `tick` | `pulse` on `s62-num` after arrival | ~399.90 (f 0.58, "one thousand dollar") | +$1,000, small on purpose — a tick, not a hero |
| 18 | s67 | 4.13 | `stamp` | **`pop` verdict entry** on `s67-stmt` | ~432.60 (f 0.60, "astronomical") | the hottest frame in the video, and it has no number |
| 19 | s72→s73 | 4.18→5.1 | `transition` | **SHOVE #2** | 465.319 | "the most powerful lever is not saving more" |
| 20 | s73 | 5.1 | `reveal` | `rise` on `s73-stmt` | 466.419 | the reframe that opens the drop zone |
| 21 | s78 | 5.6 | `reveal` | `rise` on `s78-art` | ~502.30 (f 0.55, "shortens") | the band shortening — the drawn argument arriving |
| 22 | s84 | 5.12 | `hero` | `pop` on `s84-art` | ~542.30 (f 0.64, "thirty percent") | the permanent reduction, on the coldest frame |
| 23 | s86 | 5.14 | `hero` | `pop` on `s86-art` | ~560.00 (f 0.63, "twenty-four to thirty-two") | **the ~70% reward beat (69.9%)** |
| 24 | s88 | 5.16 | `stamp` | **`pop` verdict entry** on `s88-stmt` | 568.855 | "Statutory, permanent, inflation-adjusted." |
| 25 | s91 | 5.19 | `reveal` | `rise` on `s91-art` | ~587.20 (f 0.51, "rest of your life") | the level running off the frame |
| 26 | s92 | 6.1 | `chip` | `pop` on `s92-chip1` | 590.576 | four steps down |
| 27 | s101 | 6.10 | `tick` | `pulse` on `s101-num` | ~654.30 (f 0.57, "Required Minimum") | age 73 |
| 28 | s104 | 6.13 | `reveal` | `rise` on `s104-art` | ~675.60 (f 0.43, "before Social Security") | the window shading |
| 29 | s106 | 6.15 | `reveal` | `rise` on `s106-art` | ~692.30 (f 0.55, "one smooth paycheck") | three inflows becoming one |
| 30 | s108 | 7.1 | `reveal` | `rise` on `s108-stmt` | 703.738 | the whole roadmap in one frame |
| 31 | s114 | 7.7 | `stamp` | **`pop` verdict entry** on `s114-stmt` | ~747.10 (f 0.67, "a feeling, not a fact") | the callback — the video's thesis, said last |
| 32 | s119 | 7.12 | `cta` | the `s119-cta` block landing | 775.154 | the single `--pop` element |

**Why the verdict `pop` exists.** Five scenes carry a `stamp` (s11, s52, s67, s88, s114). The
script writes no stamp copy and inventing some would put a second home under a fact, so **the
slam is at the ladder, not in new markup**: on those scenes the focal enters with `pop`
(`back.out(1.7)`) at its anchored word instead of `rise`. The sound then has the helper
`kit.json` binds it to. Same reasoning binds every `chip` cue to a `pop` on the row's first chip
and the two `tick`s to a `pulse` fired *after* the number has arrived.

**Declared DRY beats** — silence is the choice, not an omission:

- **The disclaimer pair, s32–s33 (3.4–3.5).** A sound on a compliance card turns it into a gag.
- **Six of the nine IRS reveals — s37, s39, s40, s42, s43, s44, s51, s53.** Four of the nine get
  a hit; hitting all nine would make the ninth inaudible as information. The unhit ones are the
  ones the voice already separates.
- **s96 (6.5), the 4% rule.** The whole point of the frame is that no agency stands behind it.
  A `hero` there would sound like authority the storyboard has just declared absent.
- **The long-term-care beat after s67** — s68–s70 run dry so the stamp is the last thing heard
  in that register.
- **s120–s123, the close.** After the `cta` on s119 nothing else is punctuated; the end-card and
  the disclaimer card ride the bed alone.

**Bed length is not flagged.** `tools/audio/mix.py` feeds the ~248 s bed in `laps` with a 3 s
`acrossfade` at each joint and trims to the master; there is no dip at 248 s or 496 s.

---

## 3. Scene DOM and type treatment

```html
<section class="scene clip arch-b has-photo art-forward" id="s86"
         data-track-index="2" data-start="554.060" data-duration="9.452"
         data-framings="4.500 4.502" style="--f1:#0f3a20">
  <div class="field" id="s86-field"></div>
  <div class="bg"    id="s86-bg" style="background-image:url(assets/img/s86.jpg)"></div>
  <div class="scrim" id="s86-scrim"></div>
  <div class="plate" id="s86-plate" style="left:1120px;top:150px;width:860px;height:610px">
    <div class="plate-in"></div>
    <svg class="art" id="s86-art" viewBox="0 0 860 610">…</svg>
  </div>
  <div class="stack">
    <div class="kicker" id="s86-head">WAITING UNTIL 70</div>
    <div class="row"    id="s86-row"><span class="chip fund" id="s86-chip1">+24% if FRA is 67</span>…</div>
    <div class="foot"   id="s86-foot">SSA · as of August 2026</div>
  </div>
  <div class="grain"></div>
</section>
```

**ID scheme: `s<n>-<part>`, n = 1…123 in script order, never renumbered.** Parts: `field`,
`bg`, `scrim`, `plate`, `art`, `head`, `stmt`, `num`, `sub`, `row`, `chip1…4`, `foot`, `icon`,
`cta`, `disc`. Three IDs are one-offs and are named here so a later fix can be pointed at them:
`s36-disc` (the lower-third disclaimer, placement 2 of 4), `s119-cta`, `s123-disc` (the full
disclaimer card over the last 4 s).

**Copy is not restated in this file.** `head:`, `stmt:`/`num:`, `src:` and every chip string
live in each line's `[img: …]` cue in `script-en.md` and have exactly one home. This storyboard
owns the DOM, the archetype row, the cues, the transitions, the audio, the drawn art and the
images.

| type | count | stack | focal size | notes |
|---|---|---|---|---|
| **stmt** | 89 | `kicker` → `stmt` → optional `foot` | `.huge` **76 px** | the default |
| **num** | 15 | `kicker` → `num` → `foot` (source line) | `.huge` **112 px** | every one carries its own agency + date |
| **chips** | 15 | `kicker` → `.row` → optional `foot` | chip **32 px** | rows declared explicitly, never left to `flex-wrap` |
| **arithmetic** | 3 | `kicker` → two `.sub` lines + rule + `num` → `foot` | `.sub` 46 px, `num` 96 px | s38, s40, s45 — the sums are TYPE, not drawn art |
| **cta** | 1 | `s119-cta` `.cta` block → `foot` | `.cta` 46 px | the only `--pop` in the cut |

Every size is on `layout.type_ladder_px` (112 · 96 · 76 · 46 · 32 · 26). Nothing is
interpolated to fit. **Never `stmt` and `num` together** (`one_focal_per_scene`).

**Element budget.** Max content elements per scene: `kicker` + focal + `foot` = **3**; on s36
the disclaimer lower-third makes **4**; a chip row counts as **1** (`cascade.counts_as_elements`).
Ceiling is 6 ✓. `.field`, `.bg`, `.scrim`, `.grain`, `.plate`/`.art` are stage, not elements.

**Chip discipline.** `layout.max_chips_per_row` 3 and `max_chip_chars` 22. Two rows are declared
explicitly and must not be left to wrap: **s41** `401(k) · 403(b) · TSP` / `governmental 457(b)`
and **s92** `1 Stabilize · 2 Maximize · 3 Protect` / `4 Income`. Longest chip in the cut is
`FRA 66 (1943–54): +32%` at 22. **Do not re-lengthen any chip** — `.row` has `flex-wrap` and an
over-long fourth chip orphans silently past every checker (script handoff #10).

---

## 4. The cue ladder — the same four cues on every scene

Offsets are relative to `scene_start` (§6 `start`), so every absolute time is derived.
`audio_start = scene_start + 0.25` (LONG `lead_in_seconds`).

| # | element | offset | class | helper | spec |
|---|---|---|---|---|---|
| — | `sN-bg` | +0.00 → scene end | **anchored** | `ken` | 1.0↔1.16, ∓2.5 xPercent, direction alternates per boundary |
| 1 | `sN-head` (`.kicker`) | **+0.30** | fixed | `rise` | y:24, 0.50 s `expo.out` — on all 123 scenes |
| 2 | `sN-stmt` | **+1.10** | fixed | `rise` | y:40, 0.70 s `expo.out` |
| 2′ | `sN-num` | **anchored** | anchored | `countUp` / `pop` | lands on its own digit |
| 2″ | verdict scenes (s11, s52, s67, s88, s114) | **anchored** | anchored | **`pop`** | scale from 0.6, 0.60 s `back.out(1.7)` |
| 2‴ | `sN-chip1…4` | **+1.10, +1.75, +2.40, +3.05** | fixed | `popEach` | declared cascade, 0.65 s gap |
| 3 | `sN-foot` / `sN-icon` | **+2.10** (chip scenes: **last chip + 0.80**) | fixed | `fade` / `draw` | foot 0.40 s `power1.out` |
| — | `sN-art` | **anchored** | anchored | `rise` / `pop` | 6 scenes only (§8) |

**Spacing.** `first_cue_by_seconds` 0.5 — the kicker is on screen at **+0.30 on all 123
scenes** ✓. `cue_min_gap_seconds` 0.8: +0.30 → +1.10 = **0.80** ✓; +1.10 → +2.10 = **1.00** ✓.
The 0.65 s chip gap is the **declared cascade exemption** (`layout.cascade`, 0.6–0.7 s), never
applied to anything else.

**Anchored vs fixed.** Kicker, `stmt`, chips and foot are **fixed** — constant regardless of
clip length. The `ken` push, every `num` arrival, every verdict `pop` and every `art` beat are
**anchored** — they land on a word and scale with the clip.
**Surplus time from a longer clip goes into the hold after cue 3, never into the cascade.** The
stack always finishes at **+2.50 s** (chip scenes +3.85 s); s41 (10.021 s) then holds a finished
frame for 6.2 s with only the ken push and the second framing running, and that is correct.

**The 15 `num` scenes take an anchored arrival instead of the fixed +1.10** — putting `$35,750`
on screen five seconds before the voice reaches it spoils the line. `stmt` scenes keep the fixed
+1.10 because a statement paraphrases the whole line and cannot spoil it.

**Track index alternates 1 / 2 by scene parity** (odd → 1, even → 2): `hyperframes check`
rejects two overlapping clips on one track and every non-final scene overlaps its successor by
0.45 s.

---

## 5. Transitions, and the eleven scenes that must carry two framings

`dissolve` (0.45 s) is the default on all 122 boundaries. **Two are `shove`**, and they are the
only two genuine reversals in the argument:

- **s28 → s29 (2.17 → 3.1) at 177.332 s (22.1%)** — "now you can go on offense" / "Okay,
  foundation stable? Now we go on offense." The video changes direction from defence to attack
  and says so out loud. A dissolve smuggles a reversal in as a continuation.
- **s72 → s73 (4.18 → 5.1) at 465.319 s (58.1%)** — "the most powerful lever you can pull isn't
  just saving more." This contradicts the video's own Step Two, and it opens the mid-video drop
  zone. It is the one place the script argues against itself on purpose.

Every other chapter boundary is a *step*, not a turn: the roadmap said there would be five, so
arriving at the next one is continuity. **No `hold` pairs in this cut** — no photograph is
shared across two scenes.

### The eleven scenes over `max_scene_seconds`

**`scene.max_scene_seconds` is 9.0 and `check_build` fails a scene holding ONE photograph past
it. Eleven scenes breach it, not one.** The script's handoff #2 flagged only 1.8; the other ten
are visible only once `timing.json` is measured, and every one of them will fail the build
unchecked. Each gets `data-framings` with two values summing to `scene_duration` — a wide frame
and a **tighter crop of the same file** (one continuous move, per the firaun rule: same image
across a boundary is ONE zoom, never a self-dissolve). No second file and no extra image slot.

| scene | line | dur | framings (a / b) | the two framings |
|---|---|---|---|---|
| s8 | 1.8 | 9.473 | 4.600 / 4.873 | wide on the boardwalk → push to the couple *(the script's own required fix)* |
| s12 | 2.1 | 9.525 | 4.700 / 4.825 | the whole slab → the rebar grid at its edge |
| s23 | 2.12 | 9.708 | 4.800 / 4.908 | the driveway wide → the open engine bay |
| s39 | 3.11 | 9.603 | 4.800 / 4.803 | the release page → the IRA paragraph |
| s41 | 3.13 | 10.021 | 5.300 / 4.721 | all four tabs → the three spoken ones |
| s45 | 3.17 | 9.290 | 4.600 / 4.690 | the desk wide → the total under the rule |
| s46 | 3.18 | 9.002 | 4.500 / 4.502 | the empty track → the final straight |
| s85 | 5.13 | 9.159 | 4.600 / 4.559 | the SSA page → the delayed-credit row |
| s86 | 5.14 | 9.002 | 4.500 / 4.502 | all three posts → the tallest one |
| s95 | 6.4 | 9.185 | 4.600 / 4.585 | both questions → the surviving one |
| s115 | 7.8 | 9.185 | 4.600 / 4.585 | the five cards → the hand on the first |

Each second framing starts **≥1.4 s after that scene's last fixed text cue** (+2.50 s, or
+3.85 s on s41's chip row — s41's b framing starts at 5.300 ✓). **Emit `data-framings` on all
123 sections**; on the 112 single-framing scenes it is one value equal to `scene_duration`. That
costs nothing and removes any question about whether an absent attribute means "one framing" or
"not declared".

---

## 6. Scenes — the archetype row

One row per VO line. `start` / `dur` = `scene_start` / `scene_duration`, **verbatim from
`timing.json`, the only home**; `d-dur` = `dur + 0.45` (s123 bare). `arch`: **A** plate ·
**B** figure · **C** ledger · **D** band. `ground` = the scene's `--f1` (§7). `art`: `off` ·
`fwd` (= `art-forward`) · `icon`. `ctr`: `centred` — **deterministic: a scene is `centred`
unless a drawn layer or a declared chip row occupies the archetype's other side**; fin-build
then drops that scene's plate, `crule`, `vrule` and `brule`, because a split with nothing
opposite is a hole. `trans`: `dis` · **`SHOVE`**. `sfx`: the cue this scene emits (§2); `—` is
dry. **Every scene carries `has-photo` and a real `.bg`; there are no exceptions and none may be
added.** `▲` marks a two-framing scene (§5).

| # | line | start | dur | d-dur | trans | arch | ground | art | ctr | focal · role | sfx | bg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| s1 | 1.1 | 0.000 | 4.927 | 5.377 | dis | A | `#131a24` | off | Y | stmt · — | reveal | `s1.jpg` |
| s2 | 1.2 | 4.927 | 6.129 | 6.579 | dis | A | `#101720` | off | Y | stmt · — | — | `s2.jpg` |
| s3 | 1.3 | 11.056 | 5.946 | 6.396 | dis | D | `#241d15` | off | Y | stmt · — | reveal | `s3.jpg` |
| s4 | 1.4 | 17.002 | 6.181 | 6.631 | dis | A | `#1c2027` | off | Y | stmt · — | — | `s4.jpg` |
| s5 | 1.5 | 23.184 | 8.271 | 8.721 | dis | D | `#241d15` | off | Y | stmt · — | — | `s5.jpg` |
| s6 | 1.6 | 31.455 | 5.476 | 5.926 | dis | C | `#1f1e1c` | off | Y | stmt · — | — | `s6.jpg` |
| s7 | 1.7 | 36.931 | 4.588 | 5.038 | dis | C | `#0f2a1a` | off | Y | stmt · **fund** | — | `s7.jpg` |
| s8 ▲ | 1.8 | 41.518 | 9.473 | 9.923 | dis | A | `#291f13` | off | Y | stmt · — | — | `s8.jpg` |
| s9 | 1.9 | 50.991 | 5.894 | 6.344 | dis | D | `#0f2a1a` | off | **N** | 2 chips · **fund** | — | `s9.jpg` |
| s10 | 1.10 | 56.885 | 8.167 | 8.617 | dis | D | `#12351f` | off | **N** | 3 chips · **fund** | chip | `s10.jpg` |
| s11 | 1.11 | 65.051 | 3.621 | 4.071 | dis | D | `#12351f` | off | Y | stmt · **fund** | **stamp** | `s11.jpg` |
| s12 ▲ | 2.1 | 68.673 | 9.525 | 9.975 | dis | A | `#1c2027` | off | Y | stmt · — | — | `s12.jpg` |
| s13 | 2.2 | 78.198 | 5.659 | 6.109 | dis | A | `#171d26` | off | Y | stmt · — | — | `s13.jpg` |
| s14 | 2.3 | 83.856 | 5.580 | 6.030 | dis | D | `#1f1e1c` | off | Y | stmt · — | — | `s14.jpg` |
| s15 | 2.4 | 89.437 | 7.252 | 7.702 | dis | D | `#2b1418` | off | Y | stmt · **warn** | reveal | `s15.jpg` |
| s16 | 2.5 | 96.689 | 6.469 | 6.919 | dis | D | `#301519` | off | **N** | 2 chips · **warn** | — | `s16.jpg` |
| s17 | 2.6 | 103.158 | 8.036 | 8.486 | dis | B | `#38151a` | off | Y | num `north of 20%` · **warn** | **hero** | `s17.jpg` |
| s18 | 2.7 | 111.193 | 3.961 | 4.411 | dis | A | `#301519` | **icon** | Y | stmt · **warn** | — | `s18.jpg` |
| s19 | 2.8 | 115.154 | 5.528 | 5.978 | dis | C | `#1f1e1c` | off | Y | stmt · — | — | `s19.jpg` |
| s20 | 2.9 | 120.682 | 6.599 | 7.049 | dis | C | `#2a2113` | off | Y | stmt · **target** | — | `s20.jpg` |
| s21 | 2.10 | 127.282 | 4.222 | 4.672 | dis | C | `#2a2113` | off | Y | stmt · **target** | — | `s21.jpg` |
| s22 | 2.11 | 131.504 | 8.323 | 8.773 | dis | D | `#0f2a1a` | off | Y | stmt · **fund** | reveal | `s22.jpg` |
| s23 ▲ | 2.12 | 139.827 | 9.708 | 10.158 | dis | A | `#2b1418` | off | Y | stmt · **warn** | — | `s23.jpg` + `s23b.jpg` |
| s24 | 2.13 | 149.535 | 3.909 | 4.359 | dis | C | `#301519` | off | Y | stmt · **warn** | — | `s24.jpg` |
| s25 | 2.14 | 153.443 | 7.017 | 7.467 | dis | D | `#0f2a1a` | off | Y | stmt · **fund** | chip | `s25.jpg` |
| s26 | 2.15 | 160.460 | 7.722 | 8.172 | dis | C | `#0f2a1a` | off | Y | stmt · **fund** | — | `s26.jpg` |
| s27 | 2.16 | 168.183 | 3.151 | 3.601 | dis | A | `#12351f` | off | Y | stmt · **fund** | — | `s27.jpg` |
| s28 | 2.17 | 171.334 | 5.998 | 6.448 | **SHOVE** | A | `#12351f` | off | Y | stmt · **fund** | transition | `s28.jpg` |
| s29 | 3.1 | 177.332 | 7.984 | 8.434 | dis | A | `#1c2027` | off | Y | stmt · — | — | `s29.jpg` |
| s30 | 3.2 | 185.316 | 5.006 | 5.456 | dis | C | `#2a2113` | off | Y | stmt · **target** | — | `s30.jpg` |
| s31 | 3.3 | 190.322 | 5.345 | 5.795 | dis | C | `#2a2113` | off | Y | stmt · **target** | — | `s31.jpg` |
| s32 | 3.4 | 195.667 | 7.566 | 8.016 | dis | A | `#171d26` | off | Y | stmt · — | **dry** | `s32.jpg` |
| s33 | 3.5 | 203.233 | 5.215 | 5.665 | dis | A | `#171d26` | off | Y | stmt · — | **dry** | `s33.jpg` |
| s34 | 3.6 | 208.447 | 4.692 | 5.142 | dis | C | `#2a2113` | off | Y | stmt · **target** | — | `s34.jpg` |
| s35 | 3.7 | 213.140 | 5.528 | 5.978 | dis | D | `#2a2113` | off | Y | stmt · **target** | — | `s35.jpg` |
| s36 | 3.8 | 218.668 | 8.140 | 8.590 | dis | C | `#2e2411` | off | Y | num `$24,500` · **target** · `source-shot` | **hero** | `s36.jpg` |
| s37 | 3.9 | 226.808 | 4.980 | 5.430 | dis | C | `#2e2411` | off | Y | num `+ $8,000` · **target** · `source-shot` | — | `s37.jpg` |
| s38 | 3.10 | 231.788 | 4.640 | 5.090 | dis | B | `#2e2411` | off | Y | arithmetic `$32,500` · **target** | **hero** | `s38.jpg` |
| s39 ▲ | 3.11 | 236.428 | 9.603 | 10.053 | dis | C | `#2a2113` | off | Y | num `$7,500 + $1,100` · **target** · `source-shot` | — | `s39.jpg` |
| s40 | 3.12 | 246.031 | 7.148 | 7.598 | dis | B | `#2e2411` | off | Y | arithmetic `$8,600` · **target** | — | `s40.jpg` |
| s41 ▲ | 3.13 | 253.179 | 10.021 | 10.471 | dis | D | `#1f1e1c` | off | **N** | 4 chips (3+1) · — | chip | `s41.jpg` |
| s42 | 3.14 | 263.200 | 4.039 | 4.489 | dis | D | `#2a2113` | off | Y | stmt · **target** | — | `s42.jpg` |
| s43 | 3.15 | 267.239 | 8.402 | 8.852 | dis | D | `#2e2411` | off | Y | stmt · **target** | — | `s43.jpg` |
| s44 | 3.16 | 275.641 | 6.364 | 6.814 | dis | C | `#2e2411` | off | Y | num `$11,250` · **target** · `source-shot` | — | `s44.jpg` |
| s45 ▲ | 3.17 | 282.005 | 9.290 | 9.740 | dis | B | **`#372a0c`** | off | Y | arithmetic `$35,750` · **target** | **hero** | `s45.jpg` |
| s46 ▲ | 3.18 | 291.295 | 9.002 | 9.452 | dis | A | `#241d15` | off | Y | stmt · — | — | `s46.jpg` |
| s47 | 3.19 | 300.297 | 6.651 | 7.101 | dis | C | `#2b1418` | off | Y | stmt · **warn** | — | `s47.jpg` |
| s48 | 3.20 | 306.949 | 5.998 | 6.448 | dis | C | `#0f2a1a` | off | Y | stmt · **fund** | — | `s48.jpg` |
| s49 | 3.21 | 312.947 | 5.633 | 6.083 | dis | A | `#0f2a1a` | off | Y | stmt · **fund** | — | `s49.jpg` |
| s50 | 3.22 | 318.580 | 5.580 | 6.030 | dis | C | `#1c2027` | off | Y | stmt · — · `source-shot` | — | `s50.jpg` |
| s51 | 3.23 | 324.160 | 6.416 | 6.866 | dis | B | `#2a2113` | off | Y | num `over $150,000` · **target** | — | `s51.jpg` |
| s52 | 3.24 | 330.576 | 8.323 | 8.773 | dis | D | `#2e2411` | off | Y | stmt · **target** | **stamp** | `s52.jpg` |
| s53 | 3.25 | 338.900 | 5.215 | 5.665 | dis | B | `#2a2113` | off | Y | num `$150,000 INDEXED` · **target** | — | `s53.jpg` |
| s54 | 3.26 | 344.114 | 4.980 | 5.430 | dis | A | `#1f1e1c` | off | Y | stmt · — | — | `s54.jpg` |
| s55 | 4.1 | 349.094 | 5.293 | 5.743 | dis | A | `#0f2a1a` | off | Y | stmt · **fund** | reveal | `s55.jpg` |
| s56 | 4.2 | 354.387 | 7.096 | 7.546 | dis | A | `#2b1418` | off | Y | stmt · **warn** | — | `s56.jpg` |
| s57 | 4.3 | 361.482 | 5.345 | 5.795 | dis | D | `#1c2027` | off | Y | stmt · — | — | `s57.jpg` |
| s58 | 4.4 | 366.828 | 6.651 | 7.101 | dis | C | `#301519` | off | Y | stmt · **warn** | — | `s58.jpg` |
| s59 | 4.5 | 373.479 | 7.749 | 8.199 | dis | C | `#2a2113` | off | Y | stmt · **target** | — | `s59.jpg` |
| s60 | 4.6 | 381.228 | 6.233 | 6.683 | dis | D | `#0f2a1a` | off | Y | stmt · **fund** | — | `s60.jpg` |
| s61 | 4.7 | 387.461 | 8.506 | 8.956 | dis | D | `#12351f` | off | **N** | 3 chips · **fund** | chip | `s61.jpg` |
| s62 | 4.8 | 395.967 | 6.469 | 6.919 | dis | C | `#2a2113` | off | Y | num `+ $1,000` · **target** · `source-shot` | tick | `s62.jpg` |
| s63 | 4.9 | 402.436 | 5.293 | 5.743 | dis | A | `#12351f` | off | Y | stmt · **fund** | — | `s63.jpg` |
| s64 | 4.10 | 407.729 | 8.976 | 9.426 | dis | C | `#1f1e1c` | off | Y | stmt · — | — | `s64.jpg` |
| s65 | 4.11 | 416.705 | 3.726 | 4.176 | dis | C | `#1c2027` | off | Y | stmt · — | — | `s65.jpg` |
| s66 | 4.12 | 420.431 | 6.887 | 7.337 | dis | A | `#2b1418` | off | Y | stmt · **warn** | — | `s66.jpg` |
| s67 | 4.13 | 427.318 | 8.454 | 8.904 | dis | A | **`#3b1219`** | off | Y | stmt · **warn** | **stamp** | `s67.jpg` + `s67b.jpg` |
| s68 | 4.14 | 435.771 | 3.569 | 4.019 | dis | A | `#38151a` | off | Y | stmt · **warn** | **dry** | `s68.jpg` |
| s69 | 4.15 | 439.340 | 8.402 | 8.852 | dis | C | `#2a2113` | off | Y | stmt · **target** | **dry** | `s69.jpg` |
| s70 | 4.16 | 447.742 | 7.331 | 7.781 | dis | C | `#2a2113` | off | Y | stmt · **target** | **dry** | `s70.jpg` |
| s71 | 4.17 | 455.073 | 6.260 | 6.710 | dis | A | `#0f2a1a` | off | Y | stmt · **fund** | — | `s71.jpg` |
| s72 | 4.18 | 461.332 | 3.987 | 4.437 | **SHOVE** | A | `#12351f` | off | Y | stmt · **fund** | transition | `s72.jpg` |
| s73 | 5.1 | 465.319 | 7.252 | 7.702 | dis | A | `#1c2027` | off | Y | stmt · — | reveal | `s73.jpg` |
| s74 | 5.2 | 472.571 | 7.513 | 7.963 | dis | A | `#0f2a1a` | off | Y | stmt · **fund** | — | `s74.jpg` |
| s75 | 5.3 | 480.085 | 4.588 | 5.038 | dis | C | `#1f1e1c` | off | Y | stmt · — | — | `s75.jpg` |
| s76 | 5.4 | 484.673 | 7.200 | 7.650 | dis | D | `#1c2027` | off | Y | stmt · — | — | `s76.jpg` |
| s77 | 5.5 | 491.873 | 7.435 | 7.885 | dis | D | `#0f2a1a` | off | **N** | 2 chips · **fund** | — | `s77.jpg` |
| s78 | 5.6 | 499.308 | 4.980 | 5.430 | dis | D | `#12351f` | **fwd `years-band-shorten`** | **N** | stmt · **fund** | reveal | `s78.jpg` |
| s79 | 5.7 | 504.287 | 6.887 | 7.337 | dis | A | `#1c2027` | off | Y | stmt · — | — | `s79.jpg` |
| s80 | 5.8 | 511.174 | 6.547 | 6.997 | dis | D | `#0f2a1a` | off | **N** | 2 chips · **fund** | — | `s80.jpg` + `s80b.jpg` |
| s81 | 5.9 | 517.721 | 6.965 | 7.415 | dis | D | `#12351f` | off | Y | stmt · **fund** | — | `s81.jpg` |
| s82 | 5.10 | 524.686 | 6.834 | 7.284 | dis | C | `#131a24` | off | Y | stmt · — | — | `s82.jpg` |
| s83 | 5.11 | 531.520 | 6.834 | 7.284 | dis | C | `#101720` ⚠ | off | Y | stmt · **warn** · `source-shot` | — | `s83.jpg` |
| s84 | 5.12 | 538.354 | 6.547 | 6.997 | dis | B | **`#0c1a2c`** ⚠ | **fwd `bars-62-vs-fra`** | **N** | 2 chips · **warn** | **hero** | `s84.jpg` |
| s85 ▲ | 5.13 | 544.901 | 9.159 | 9.609 | dis | C | `#0f2a1a` | off | Y | num `+8% a year` · **fund** · `source-shot` | — | `s85.jpg` |
| s86 ▲ | 5.14 | 554.060 | 9.002 | 9.452 | dis | B | **`#0f3a20`** | **fwd `bars-62-fra-70`** | **N** | 2 chips · **fund** | **hero** | `s86.jpg` |
| s87 | 5.15 | 563.063 | 4.692 | 5.142 | dis | D | `#2a2113` | off | **N** | 2 chips · **target** | — | `s87.jpg` |
| s88 | 5.16 | 567.755 | 5.215 | 5.665 | dis | C | `#12351f` | off | Y | stmt · **fund** | **stamp** | `s88.jpg` |
| s89 | 5.17 | 572.970 | 5.293 | 5.743 | dis | A | `#1c2027` | **icon** | Y | stmt · — | — | `s89.jpg` |
| s90 | 5.18 | 578.263 | 6.887 | 7.337 | dis | C | `#0f2a1a` | off | Y | stmt · **fund** | — | `s90.jpg` |
| s91 | 5.19 | 585.149 | 4.327 | 4.777 | dis | B | `#12351f` | **fwd `bar-70-level-runs-off`** | **N** | stmt · **fund** | reveal | `s91.jpg` |
| s92 | 6.1 | 589.476 | 8.976 | 9.426 | dis | D | `#12351f` | off | **N** | 4 chips (3+1) · **fund** | chip | `s92.jpg` |
| s93 | 6.2 | 598.452 | 6.599 | 7.049 | dis | D | `#241d15` | off | Y | stmt · — | — | `s93.jpg` |
| s94 | 6.3 | 605.051 | 6.678 | 7.128 | dis | A | `#1c2027` | off | Y | stmt · — | — | `s94.jpg` |
| s95 ▲ | 6.4 | 611.729 | 9.185 | 9.635 | dis | D | `#1f1e1c` | off | Y | stmt · — | — | `s95.jpg` |
| s96 | 6.5 | 620.914 | 8.924 | 9.374 | dis | B | `#2a2113` | off | Y | num `4%` · **target** · **no source card** | **dry** | `s96.jpg` |
| s97 | 6.6 | 629.838 | 3.856 | 4.306 | dis | C | `#1f1e1c` | off | Y | stmt · — | — | `s97.jpg` |
| s98 | 6.7 | 633.695 | 7.017 | 7.467 | dis | C | `#2a2113` | off | Y | stmt · **target** | — | `s98.jpg` |
| s99 | 6.8 | 640.712 | 3.203 | 3.653 | dis | C | `#2a2113` | off | Y | stmt · **target** | — | `s99.jpg` |
| s100 | 6.9 | 643.915 | 7.252 | 7.702 | dis | D | `#0f2a1a` | off | Y | stmt · **fund** | — | `s100.jpg` |
| s101 | 6.10 | 651.167 | 5.842 | 6.292 | dis | C | `#2e2411` | off | Y | num `age 73` · **target** · `source-shot` | tick | `s101.jpg` |
| s102 | 6.11 | 657.009 | 6.887 | 7.337 | dis | C | `#2a2113` | off | Y | stmt · **target** | — | `s102.jpg` |
| s103 | 6.12 | 663.896 | 7.618 | 8.068 | dis | D | `#0f2a1a` | off | Y | stmt · **fund** | — | `s103.jpg` |
| s104 | 6.13 | 671.513 | 8.924 | 9.374 | dis | D | `#12351f` | **fwd `conversion-window`** | **N** | stmt · **fund** | reveal | `s104.jpg` |
| s105 | 6.14 | 680.438 | 7.905 | 8.355 | dis | A | `#241d15` | off | Y | stmt · — | — | `s105.jpg` |
| s106 | 6.15 | 688.343 | 6.730 | 7.180 | dis | D | `#12351f` | **fwd `three-into-one`** | **N** | stmt · **fund** | reveal | `s106.jpg` |
| s107 | 6.16 | 695.073 | 7.566 | 8.016 | dis | A | `#291f13` | off | Y | stmt · — | — | `s107.jpg` |
| s108 | 7.1 | 702.638 | 5.816 | 6.266 | dis | A | `#241d15` | off | Y | stmt · — | reveal | `s108.jpg` |
| s109 | 7.2 | 708.454 | 7.148 | 7.598 | dis | C | `#0f2a1a` | off | **N** | 2 chips · **fund** | — | `s109.jpg` |
| s110 | 7.3 | 715.602 | 7.566 | 8.016 | dis | C | `#2a2113` | off | **N** | 3 chips · **target** | — | `s110.jpg` |
| s111 | 7.4 | 723.167 | 6.599 | 7.049 | dis | C | `#0f2a1a` | off | **N** | 3 chips · **fund** | — | `s111.jpg` |
| s112 | 7.5 | 729.767 | 7.670 | 8.120 | dis | C | `#12351f` | off | Y | num `+8% a year to 70` · **fund** | — | `s112.jpg` |
| s113 | 7.6 | 737.437 | 6.181 | 6.631 | dis | C | `#2a2113` | off | **N** | 3 chips · **target** | — | `s113.jpg` |
| s114 | 7.7 | 743.618 | 5.633 | 6.083 | dis | A | `#291f13` | off | Y | stmt · — | **stamp** | `s114.jpg` |
| s115 ▲ | 7.8 | 749.251 | 9.185 | 9.635 | dis | D | `#0f2a1a` | off | Y | stmt · **fund** | — | `s115.jpg` |
| s116 | 7.9 | 758.436 | 4.980 | 5.430 | dis | C | `#12351f` | off | Y | stmt · **fund** | — | `s116.jpg` |
| s117 | 7.10 | 763.416 | 4.379 | 4.829 | dis | A | `#241d15` | off | Y | stmt · — | — | `s117.jpg` |
| s118 | 7.11 | 767.794 | 6.260 | 6.710 | dis | C | `#1f1e1c` | off | Y | stmt · — | — | `s118.jpg` |
| s119 | 7.12 | 774.054 | 4.980 | 5.430 | dis | A | **`#33200f`** | off | Y | `.cta` · **pop** | **cta** | `s119.jpg` |
| s120 | 7.13 | 779.033 | 5.110 | 5.560 | dis | D | `#241d15` | off | Y | stmt · — | **dry** | `s120.jpg` |
| s121 | 7.14 | 784.144 | 6.547 | 6.997 | dis | A | `#1c2027` | off | Y | stmt · — · **end-screen safe** | **dry** | `s121.jpg` |
| s122 | 7.15 | 790.691 | 6.965 | 7.415 | dis | A | `#1c2027` | off | Y | 2 chips · — · **end-screen safe** | **dry** | `s122.jpg` |
| s123 | 7.16 | 797.656 | 3.987 | **3.987** | — | A | **`#2d2214`** | off | Y | stmt + `s123-disc` · — | **dry** | `s123.jpg` |

**End-screen safe (s121, s122):** every composition element stays inside `x < 1200` so the right
third of frame is clear for the YouTube end screen. This is a layout constraint, not a
`.centred` exception — both scenes are still centred within that reduced box.

### The archetype sequence, read as a rhythm

```
ch1  A A D A D C C A D D D
ch2  A A D D D B A C C C D A C D C A A
ch3  A C C A A C D C C B C B D D D C B A C C A C B D B A
ch4  A A D C C D D C A C C A A A C C A A
ch5  A A C D D D A D D C C B C B D C A C B
ch6  D D A D B C C C D C C D D A D A
ch7  A C C C C C A D C A C A D A A A
```

Totals **A 47 · B 10 · C 40 · D 26.** C-heavy, because this video's beats are overwhelmingly
**artefacts** — a bucket, a legal pad, five index cards, three account folders, a W-2, an IRS
page. B is only 10 because only ten scenes are *about* a figure; five other figure frames sit on
the document the figure came from and are therefore C.

**Six deliberate holds, each because the scenes are one argument:**

- **ch2 `D D D` (s14–s16)** — the bucket, the leak, the two holes named. One mechanism built in
  three moves; varying it would break the only through-line the chapter has.
- **ch2 `C C C` (s19–s21)** — write the plan → order the list → strike the top row. One legal
  pad, three states of it.
- **ch3 `A A` (s32–s33)** — the spoken disclaimer and its specimen source line are one card
  seen twice, and they share a ground.
- **ch3 `D D D` (s41–s43)** — which plans, which plans do *not* count, which ages. One
  eligibility argument; the tabs change under it.
- **ch4 `A A A` (s66–s68)** — disability, long-term care, "pretending it can't happen". The
  three risks in this video that **cannot be photographed as objects**, so the frame is the
  photograph and the sentence, nothing else. This is the chapter's emotional floor and holding
  the layout is what makes it read as one held breath.
- **ch7 `C C C C C` (s109–s113)** — the five recap cards. Five scenes doing the identical job:
  one step, one card. Varying the layout here would say they were five different kinds of
  thing.

**ch6 opens on `D`, not `A`.** 6.1 is the four-chip recap cascade — the scene *does* a band, and
the archetype is assigned by what the scene does. **ch7 opens on `A`** because 7.1 is the
roadmap standing complete, not assembling.

---

## 7. Ground temperature — the ladder

Values are in the §6 `ground` column; the arc they trace is §10. The ladder used:

```
cool     #131a24  #101720        #0c1a2c (coldest, once)
neutral  #1c2027  #171d26  #1f1e1c
warm     #241d15  #291f13        #2d2214 (warmest, once)
fund     #0f2a1a → #12351f →     #0f3a20 (deepest, once)
target   #2a2113 → #2e2411 →     #372a0c (deepest, once)
warn     #2b1418 → #301519 → #38151a → #3b1219 (hottest, once)
pop      #33200f (once, the CTA)
```

**Role scenes deepen into their role colour; the 44 scenes with no role move only on the
neutral warm↔cool axis**, so no frame asserts a colour it has not earned. Push it harder than
looks right — at document scale the arc reads almost flat and in the encode it is exactly right.

**No ground cross-fade is implemented.** The 0.45 s dissolve already blends both grounds; adding
the animatics' ground melt double-fades.

---

## 8. Vector art — 6 drawn layers, 2 icons, 0 Lotties, 0 emoji

Rule 8 is the test: **if you cannot say what the art asserts that the picture cannot, it is
`off`.** It is `off` on **115 of 123 scenes**, and that is the correct answer for this script:
its beats are objects — buckets, envelopes, folders, forms, index cards — and a photograph
states them better than a drawing. Density against the archetype note's calibration ("three or
four in a 12–14 scene chapter is the TOP of the range"): ch1 **0** · ch2 **1 icon** · ch3 **0**
· ch4 **0** · ch5 **4** (the top of the range, and declared) · ch6 **2** · ch7 **0**.

All six drawn layers are `art-forward` (52%) because the point of each is a **PROPORTION or a
COUNT** and the mechanism still wins; the photograph is there to satisfy `image_per_scene`.
**Each is authored in its own plate's coordinate space, never in 1920×1080.** Plate rects are
the archetype defaults from `format.json chapter_design.archetypes` — there is no `.p-a`/`.p-b`
class in `chapter-design.css`; the rect is given inline on `.plate`:
**B = `1120,150,860,610` → `viewBox="0 0 860 610"`** · **D = `0,424,1920,656` →
`viewBox="0 0 1920 656"`**.

| scene | line | plate (arch · rect) | motif | what it ASSERTS that the photograph cannot | arithmetic (`truth_bar`) |
|---|---|---|---|---|---|
| **s78** | 5.6 | D · `0,424,1920,656` | **`years-band-shorten`** — one solid band = the years the money must cover; its LEFT end retracts by ~18% | **that working longer shortens the span the savings must fund.** A photo of a clock says time passed; only this says the span got shorter | **schematic — NO tick marks, NO numbers, NO axis.** It asserts a direction, not a quantity, and must not read as a published figure |
| **s84** | 5.12 | B · `1120,150,860,610` | **`bars-62-vs-fra`** — two vertical bars, the 62 bar at **0.700** of the FRA bar, ghost track behind at ~.2 | **the size of a permanent reduction.** The SSA page (s83) states a rule exists; it cannot show 70 next to 100 | 0.700 exactly = −30%, the FRA-67 case. The chip row carries **both** FRA cases; the drawing carries one and the chips say which |
| **s86** | 5.14 | B · `1120,150,860,610` | **`bars-62-fra-70`** — three bars, **0.700 / 1.000 / 1.240**, same scale and same FRA-bar height as s84 so nothing moves between the two frames | **that the 70 bar is taller than the FRA bar by as much as the 62 bar is shorter.** The reward beat, seen | 1.240 exactly = +24%, FRA-67. SSA, as of August 2026. **No dollar amounts anywhere on this layer** |
| **s91** | 5.19 | B · `1120,150,860,610` | **`bar-70-level-runs-off`** — the 1.240 bar alone, plus a 12 px rule from its top edge running off the right frame edge | **duration, not amount** — the higher check does not expire. The bar height is unchanged from s86 so the frame cannot be read as "even more money" | same 1.240. **The only element in the cut permitted to leave the frame, and leaving is the assertion** |
| **s104** | 6.13 | D · `0,424,1920,656` | **`conversion-window`** — a horizontal time band, two markers (SOCIAL SECURITY · RMDs), the region before both filled | **a window between two events.** A calendar photo shows dates; it cannot shade the years between two things that have not happened | **schematic — NO ages, NO years, NO widths asserting a duration.** Age 73 lives on s101's card, not here |
| **s106** | 6.15 | D · `0,424,1920,656` | **`three-into-one`** — three solid inflow arrows converging into one thicker outflow | **a COUNT collapsing to one.** The photo of a desk cannot say "three sources, one paycheck" | three in, one out, exactly. **No amounts, no widths proportional to anything** |

**Construction rules all six obey** (they cost two draft rounds on `japanese-money-methods` and
one shipped-invisible funnel on `passive-income-number`'s hi cut):

- **Solid fills and heavy strokes only.** `.has-photo .art` is 30% and `.art-forward` 52%; a
  2–3 px stroke at 0.4 alpha is not on screen. Ghost tracks are **filled rects at ~.2**, never
  outlines. Nothing thinner than 9 px.
- **`stroke-width="N"` as an SVG attribute is a no-op** — `.art .st` sets it in CSS and CSS beats
  a presentation attribute. Use `style="stroke-width:N"`.
- **The per-scene `opacity` on the `<svg>` is a no-op** — `.has-photo .art` and
  `.has-photo.art-forward .art` both carry `!important`. The only levers that reach the screen
  are the weight and alpha of the elements INSIDE it.
- **A plate is a LIFTED PANEL, not a transparent rect**, and `.has-photo` turns it into an
  aperture. s84/s86/s91 sit over dark photographs so no `art-lift` is needed; **if any of those
  three backgrounds comes back pale, add `art-lift` to that scene, never a darker grade** (rule
  9 — the creator rejected exactly that on 2026-08-04).
- **`tools/chapter_sheet.py` samples a non-Lottie scene at +2.6 s.** Every drawn layer must be
  assembled by ~+3.3 s or it sheets as a half-built frame and reads as a defect that is not one.
  All six anchor between +1.8 s and +3.0 s.

**Two icons**, both inline `<svg class="icon warnc">` stroke-drawn by `draw()` at cue 3:

- **s18 (2.7)** — a **downward step arrow**, `warnc`. Asserts direction on a frame whose
  sentence is "a guaranteed negative return"; the photograph (an interest line on a paper
  statement) states the charge, not the direction.
- **s89 (5.17)** — a **market chart line with a diagonal strike through it**, `warnc`. Asserts
  negation: "not a market return". A photograph cannot say *not*.

**Zero Lotties, deliberately.** `lottie.reach_for_it_when` is an abstraction a photograph cannot
take — every abstraction in this script is either a proportion (drawn above) or an object that
can be photographed. Nothing here needs a person or a device illustrated, so nothing is fetched,
nothing is tinted, and there is no `max_per_chapter` pressure anywhere. **Zero emoji** — none is
wanted as a tonal break in a 50+ retirement video.

**Neither an icon nor a Lottie sits on s86**, the scene carrying the video's one big claim: it
already has its focal element, and its drawn proportion IS the argument.

---

## 9. Imagery — 126 slots, zero photo-free scenes

`image_per_scene` is a hard creator rule (2026-07-28, `photo_free_scene_ratio` = 0). All 123
scenes carry `has-photo` and a real full-bleed `.bg` under the locked grade
`grayscale(.32) brightness(.62) contrast(1.05)`. **No per-scene grade override anywhere.**

- **123 bg slots** + **3 cut-ins** = **126 slots**, all in
  `studio/videos/financial-freedom-after-50-en/assets/img/manifest.json` — the single home for
  every query. The 11 two-framing scenes (§5) reuse their own file at a tighter crop and add no
  slot.
- **The three cut-ins**, each anchored to its word's cue:

| slot | scene | the second concrete thing the VO names | anchored to |
|---|---|---|---|
| `s23b.jpg` | s23 (2.12) | "or a leaky roof" — the bg is the car repair | the word *roof*, ≈ `audio_start + 0.55 × dur` |
| `s67b.jpg` | s67 (4.13) | "or in-home care" — the bg is the assisted-living corridor | the word *in-home*, ≈ `audio_start + 0.44 × dur` |
| `s80b.jpg` | s80 (5.8) | "a consulting gig" — the bg is the part-time counter shift | the word *consulting*, ≈ `audio_start + 0.62 × dur` |

**Nine `source-shot` scenes** (`source_screenshot.scene_class`), each a **screen recording of
the real page with the URL bar legible and EXACTLY ONE row highlighted** — never a rebuilt
table: **s36, s37, s39, s44, s50, s62, s83, s85, s101.** Every one clears
`min_hold_seconds` 3.0 (shortest is s37 at 4.980 s), and each must carry motion — the highlight
arriving, or a slow push — or it reads as a dead frame. **s83 and s85 are the two `ssa.gov`
captures the script owes and they cannot be faked** — every pipeline fetch returned 403; they
must come from a network path that actually reaches ssa.gov.

**The densest scene gets the calmest background.** s41 (3.13) carries four chips in two rows and
is the longest scene in the cut at 10.021 s; its background is a **quiet close texture of
manila file-tab card stock in raking side light** — a texture reading of "which plans", not a
photograph competing with four labels. Same rule on s92 (6.1, four chips): the background is the
**worn table surface** the five cards have been sitting on all video, not a fifth arrangement of
the cards.

### Write the LIGHT, not the object

`pipeline_check check assets` fails any promoted image with source **`YHIGH < 110`**, so every
query in the manifest names the lighting. Four rules that cost prior cuts four fetch rounds:

1. **Never buy high-key stock.** A white-dominant subject cannot survive `brightness(.62)`; it
   lands as a flat charcoal slab. Ask for the subject **lit against a dark ground**.
2. **Replacing one white photo with another white photo re-breaks it.** When a frame reads grey,
   the fix is a differently-lit original, not a re-crop.
3. **When a slot fails twice on brightness, change the MATERIAL, not the adjective.** Enamel,
   glass, brass, polished metal and wet stone have a specular ceiling; matte paper, kraft and
   unfinished wood do not. This is why the five index cards are specified as **blank white
   enamel tags on dark walnut** and the envelopes as **kraft on slate**.
4. **Do not reject a candidate on source warmth (`R−B`).** That rule was retired 2026-08-08:
   only ~9% of a photograph's warmth reaches the screen under the layer stack. Warmth is chrome,
   not photograph.

**Photography rule from the script, and it is a rejection criterion, not a preference:** where
people appear they read **50 and older** and the frame is unmistakably **American**. Sweep every
candidate for non-US currency, signage, plugs and vehicles, and for stock that skews 25–35 — a
thirty-year-old's hand under a Social Security card is the same defect class as a non-US
banknote in a US cut.

**Nothing on screen is lettered by the photograph.** The five index cards, the account folders,
the tabs and the bands are fetched **blank**; every word on them is composition type. A stock
photo of a card that already says STABILIZE does not exist, and a near-miss is the failure the
sound-off rule names.

---

## 10. The ground temperature arc, read as a curve

**ch1 opens cold and the promise warms it.** `#131a24` on the kitchen table, then the **coldest
frame in the chapter at s2 `#101720`** — the sinking feeling, deliberately un-roled, because the
video's own thesis is that the feeling is not a fact and painting it red would concede that it
is. The promise at s3 warms to `#241d15`; the first green in the video is s7 (*take back
control*), and the chapter closes green as the five steps assemble.

**ch2 is the video's first red run.** Neutral through the foundation metaphor, then `#2b1418` as
the bucket starts leaking, `#301519` at the two holes, and **`#38151a` at s17** — the
credit-card figure, the chapter's hottest frame and the only figure in it. It cools to amber for
the payoff order (a method under examination, not a recommendation), spikes red once more at the
surprise repair, and **ends green across four scenes** — the cushion, the separate account, the
shock absorber, the porch. The shove out of it lands on offence.

**ch3 is the amber chapter and it has one crest.** The disclaimer pair sits deliberately cold
and neutral at `#171d26` — a compliance card should assert nothing. Amber then climbs through
the nine IRS reveals, dips to `#1f1e1c` on the un-figured plan list (s41), and hits
**`#372a0c` at s45, the deepest amber in the video**, where $35,750 lands. The chapter then
releases: warm at the running track, one red at the unclaimed match, green for the +1%, and out
on neutral.

**ch4 carries the hottest frame in the video, and it has no number.** Green at the fortress,
red at the one event, amber through HSA eligibility, green across the triple advantage, and then
the three unphotographable risks: `#2b1418` at disability, **`#3b1219` at s67 — long-term
care** — and `#38151a` at "pretending it can't happen". *The most exposed beat in the cut is a
temperature event before it is anything else, and it is the one beat the evidence stage refused
to give a figure to.* The chapter recovers amber for the option set and closes green.

**ch5 carries the coldest frame and the deepest green, forty-five seconds apart.**

> ⚠ **s83 and s84 are `--warn` scenes running deep COOL grounds** (`#101720`, `#0c1a2c`). This
> is the only place in the cut where the ground contradicts the role and it is **declared here
> so a later pass cannot "fix" it**: cold asserts nothing, and this is the video's drop — the
> irreversible decision, the permanent reduction. Precedent: `passive-income-number` s57–s59,
> and `japanese-money-methods` ch2 s16.

From `#0c1a2c` at s84 the chapter snaps to `#0f2a1a` at s85 (+8% a year) and to **`#0f3a20` at
s86 — the deepest green in the video, spent once, on the ~70% reward beat at 69.9%.** Amber for
the FRA mapping, green through the formula and the power to wait, and out on the bar that runs
off the frame.

**ch6 climbs home.** Green on the recap, warm at the fifth card, neutral through the reframed
question, amber on the 4% guideline and the withdrawal order, green as coordination and the
conversion window assemble, and `#291f13` on the porch at dusk.

**ch7 ends warmest.** The recap alternates green (what you do) and amber (what is published),
`#291f13` on the callback to the opening question, `#33200f` — the only pop-leaning ground —
under the CTA at s119, cooling to neutral for the two end-screen frames so the YouTube
end-screen furniture has a quiet field, and **`#2d2214` on s123, the warmest frame in the
video**, under the closing disclaimer card.

---

## 11. Timing

```
scene_duration = 0.25 (VO lead-in) + clip_duration + 0.55 (tail)   ← tiers.long
data-duration  = scene_duration + 0.45   (s1–s122; s123 bare)
audio_start    = scene_start + 0.25
root duration  = 801.642
```

`0.25 / 0.55` are `format.json tiers.long`, **not** the `scene.*` 0.4 / 1.0 SHORT defaults.
Generated from `timing.json` — **never hand-edited.** The same numbers live in four places (the
`<section>`, the JS `S` map, the `<audio>` row, root `data-duration`); updating three of four
passes every check and ships a video whose animations fire against the old timeline. Per-scene
figures are the `start` / `dur` / `d-dur` columns of §6 and are not restated.

**Chapter membership** (derived from the VO line id `vo-<chapter>-<line>`, never a second map):
**ch1 s1–s11 · ch2 s12–s28 · ch3 s29–s54 · ch4 s55–s72 · ch5 s73–s91 · ch6 s92–s107 ·
ch7 s108–s123.**

**Pace:** 801.642 / 123 = **6.52 s average scene** against `scene.target_scene_seconds` 6.5.

> **The failure mode to watch for at build.** Durations that sum to exactly 801.642 while every
> internal cut has drifted is what a re-timing produces. `tools/chapter_project.py` asserts
> **GAPS, not totals**, and `tools/cut_assemble.py` verifies every `data-start`,
> `data-duration`, `data-track-index` and framing **individually**. Neither may be weakened.
> **A layout pass may not touch a duration. This file re-times nothing.**

**`hook_gate_en`:** the payoff promise is s3, whose audio starts at **11.306 s** measured —
inside `script.hook_gate_seconds` 15 with 3.7 s of margin. The script's 11.2 s model was right.
Still measure it with silencedetect on the render and record it in `run.json`.

---

## 12. `-en` divergence

**Vacuous by policy.** The Hindi lane and `@cashguruguides` were retired 2026-08-15
(`vault/knowledge/finance-is-us-only`); there is one cut and no counterpart storyboard to
diverge from. This section exists only so a later reader does not go looking for the table the
template asks for.

---

## 13. Owed before publish

1. **Nine source screenshots** (§9) into `vault/screenshots/{source-id}-{YYYYMMDD}.png`. **s83
   and s85 (`ssa.gov`) are the two that cannot be produced from this pipeline** — 403 on every
   fetch. Without them `fact-integrity §4` is unsatisfied and the two strongest claims in the
   video have no captured source.
2. **126 images sourced**, every one passing `YHIGH ≥ 110` and the 50+/US sweep.
3. **Every `src:` line normalised to `AGENCY · as of MONTH YEAR`** (script handoff #9) — the
   script writes some as `IRS · November 2025`. The month is the source's **publication** month,
   never the ship month.
4. **`s36-disc`** (lower-third disclaimer, placement 2 of 4) and **`s123-disc`** (full card,
   holding the last 4 s) are compliance elements, not decoration. Neither may be dropped for
   layout reasons.
5. **`hook_gate_en` measured** and written to `run.json`.

## Sign-off

- [x] Colour semantics table filled and consistent with the script
- [x] Every on-screen number traced to a sourced line in the script's FACT TRACE
- [x] Every scene carries `arch` / `ground` / `art` / `ctr` — 123 rows, no blanks
- [x] `photo_free_scene_ratio` = 0 honoured — 123 of 123 scenes carry a `.bg`
- [x] Cue spacing ≥0.8 s except the one declared cascade; first cue at +0.30 on all 123
- [x] ≤6 simultaneous elements; ≤3 chips per row at ≤22 chars; both 4-chip rows declared 3+1
- [x] 32 SFX cues ≤ `tiers.long.max_sfx_cues` 36; no two inside 0.8 s
- [ ] Creator approved (Gate ②) — date: __
