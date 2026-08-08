---
summary: fin-build hi chapter 2 — 13 scenes / 81.531s, s9–s21, `hyperframes check` clean (0 errors, 12/12 AA), `check_vo_frame --chapter 2` PASS, `pipeline_check check build --chapter 2` PASS. The rate asserts go live here (first money on screen) and all four branches were proven to throw by planting a violation. Both retired style-A VO-over-bare-frame violations (s18, s19) are closed structurally, not remembered. Fourteen frames eyeballed across three separate `-o` dirs. One real system gap found and patched locally; the five fin-assets caveats are built as briefed and left for the editor.
updated: 2026-08-08
source: studio/videos/passive-income-number-hi-ch2/ · storyboard-hi.md §1–§13 · script-hi.md ch2 (creator-approved verbatim) · assets/voice/timing.json (Amrut, 519.331s) · run.json constraints + chapters.hi.1 editor rulings + chapters.hi.2 caveats · studio/videos/passive-income-number-hi-ch1/build.mjs · studio/videos/passive-income-number-en-ch2/build.mjs · tools/scaffold/assets/chapter-design.css · knowledge/design-chapter-archetypes.md
stage: fin-build, cut hi, chapter 2, attempt 1 (the killed attempt's half-state was treated as a draft of my own work)
---

# fin-build — hi · chapter 2 · attempt 1

**13 scenes · s9–s21 · lines 2.1–2.13 · root 81.531s · chapter offset 42.475s.**
`hyperframes check` **passes**: 0 lint errors, Runtime 0/0, Layout 0/0, Motion 0/0,
**Contrast 12/12 AA**. `check_vo_frame` PASS. `pipeline_check check build --chapter 2` PASS.

## 1. The half-state, resolved

`build.mjs` (11:49) was newer than `index.html` (11:37) and **the newer file did not
run**. `node --check` passed — this was not the ch1 stray-backtick shape — so I read the
whole file against the storyboard before touching it. The defect was in the killed
agent's own final action, exactly where the handoff predicted:

```js
const rateP = `    <p class="sub${rc}" id="${s.id}-rate">${esc(s.rate)}</p>`;
```

Moving s19's rate below its statement required emitting the same `.sub` from two
places, so the string was hoisted to a `const` — **evaluated eagerly for all thirteen
scenes**, and `esc(undefined)` threw on the eight that carry no `rate`. Fixed by making
it a thunk (`const rateP = () => …`, two call sites). That is the only change I made to
the file's logic; everything else in it verified out against the storyboard and I kept
it. `index.html` and `assets/audio.json` are regenerated and current.

The intended edit itself is **correct and live**: `#s19-rate` now sets under the claim
it qualifies, on ladder A's cue 3 (+1.90), because the figure it qualifies is in the
kicker and is a callback to a number s18 has already landed with its rate — variant B's
+1.10 ordering would put an element into a gap above a line that is already up.

## 2. Timing — generated, never typed

Every `data-start` / `data-duration` / `data-framings`, the `S` and `D` maps, the
thirteen `<audio>` rows and the root duration come from one read of
`../passive-income-number-hi/assets/voice/timing.json`, rebased by 42.475s. The build
asserts **gaps, not totals**, one joint at a time against the shipped cut, plus track
alternation, the framings partition, `max_scene_seconds`, and that the last scene lands
on the root. Root = 124.006 − 42.475 = **81.531s**; s21 carries its **bare**
`scene_duration` (8.506) because a chapter has no successor to dissolve into.

| | s9 | s10 | s11 | s12 | s13 | s14 | s15 | s16 | s17 | s18 | s19 | s20 | s21 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| start | 0 | 5.293 | 11.553 | 17.682 | 25.535 | 31.246 | 37.662 | 44.732 | 50.077 | 55.422 | 60.062 | 66.609 | 73.025 |
| dur | 5.293 | 6.260 | 6.129 | 7.853 | 5.711 | 6.416 | 7.069 | 5.345 | 5.345 | 4.640 | 6.547 | 6.416 | 8.506 |
| track | 1 | 2 | 1 | 2 | 1 | 2 | 1 | 2 | 1 | 2 | 1 | 2 | 1 |

No scene exceeds 9.0s, so no `data-framings` split is needed anywhere in this chapter —
the cut's four measured breaches are all downstream (s34, s52, s57, s70). `2.4` in
particular holds **one** photograph at its measured 7.853s, per the script cue's own
2026-08-08 correction of the inverted two-framings instruction.

## 3. THE RATE ASSERTS GO LIVE — four branches, all four proven to throw

ch1 rendered no figure so both asserts were vacuously true. ch2 renders ₹10,00,000,
₹30,000 and ₹2,500. Five `#sN-rate` elements exist: **s15 s16 s17 s18 s19**.

Each branch was proven by planting a violation, running the check, and restoring
(`index.html` verified byte-identical to the clean build afterwards):

| # | branch | poison | what fired |
|---|---|---|---|
| 1 | in-page **CORPUS** | removed `rate:` from s16 | `✗ page_error: RATE ASSERT FAILED — s16 renders ₹10,00,000 with no #s16-rate carrying a rate` |
| 2 | in-page **DERIVED** | s18 → `₹2,500 A MONTH`, rate dropped, `ILLUSTRATIVE` stripped from the foot | `… s18 renders the derived income ₹2,500 A MONTH with neither a rate nor an ILLUSTRATIVE marker in frame` |
| 3 | **build-time token guard** | s16 → `₹11,00,000` | build throws: *"renders ₹11,00,000, which the rate assert's CORPUS list does not carry"* |
| 4 | **`check_vo_frame`** | removed `#s19-rate` | `FAIL check_vo_frame — ch2 s19 (line 2.11) SPEAKS money over a frame carrying neither a rate nor an ILLUSTRATIVE marker` |

Branch 2 cannot be isolated from branch 1 in this chapter: both keys off the same
`rated` boolean, and every `A MONTH`-shaped amount ch2 could render is also in the
CORPUS list, so the poison necessarily trips both. The DERIVED message text firing is
what proves the branch evaluates. Recorded rather than papered over.

**The en cut's third `BILL` branch is deliberately NOT ported.** It exists for published
numerators; this chapter renders none, and the hi cut's one published statistic is
₹24,217 (PLFS, s66/6.9) where §4 states outright that no rate may be demanded beside
someone's wage. **Chapter 6 is where that branch has to be added**, with its own token
list. A branch with an empty token list is worse than no branch — nothing can exercise
it and it reads as covered.

### The two known style-A violations, closed structurally

Both were VO lines speaking money over a bare frame, which the in-page assert is
constitutionally unable to see:

- **s18 (2.10)** — style A said «तीस हज़ार बटा बारह महीने — यानी महीने के ढाई हज़ार रुपये» over
  a frame reading only `ALL TWELVE MONTHS`. Now the frame **prints ₹2,500**, and the
  script's own foot is split so `AT A 3.0% WITHDRAWAL RATE` is a first-class 40px `.sub`
  in the role colour at +1.10 — before the number — instead of a 26px foot a density
  pass can drop. The VO line itself does not speak the rate (creator-approved verbatim);
  2.9 speaks it immediately before and the frame carries it.
- **s19 (2.11)** — style A said «ढाई हज़ार महीने में क्या आता है» over a frame reading only
  `THE FIRST BRICK`. Closed twice over: the kicker names the figure (`WHAT ₹2,500 BUYS`)
  and `#s19-rate` carries `AT A 3.0% WITHDRAWAL RATE · ILLUSTRATIVE`.

`check_vo_frame --cut hi --chapter 2` PASSES on all 13 scenes. **No false positives to
report** — no magnitude word in this chapter's VO is used non-monetarily.

## 4. The archetype layer

Sequence **A C D D A B B B B B C C A**, §7 rows 9–21 verbatim. All thirteen are
`has-photo` + `art-off` + `centred` — §8 gives ch2 **zero drawn layers** by the
storyboard's own count, because rule 8 retires every candidate the script names (the
drawn tank at all six tap positions is the ghost-envelope failure by name; 2.12's twelve
bill stubs are a count the photograph already makes). `.centred` then re-centres each
stack and the plate/crule/vrule/brule go `display:none`, so no split is left as a hole.

**Two continuous zooms, not four scenes.** s14→s15 and s17→s18 each run one photograph
under one push via `plateKen` with explicit endpoints (`1.000→1.090`, then the 91.74%
crop `1.000→1.065`, which is the same 1.00→1.16 visual push across the joint). Neither
joint takes a `transition` SFX. `ken()` cannot do this — its endpoints are fixed and its
xPercent drift would slide the crop sideways at the one frame where the two must
register.

- **NO RAIL.** 0 chapter-title / scene-counter / slide-number tokens in `index.html`;
  `#root` carries `class="cut-hi"` and nothing else.
- **Comma-descender fix — confirmed reachable and confirmed clear.**
  `assets/chapter-design.css` resolves to `tools/scaffold/assets/chapter-design.css`
  (line 142, `.arch-b .mega { … padding-bottom: .11em }`). ⚠ **But note what actually
  protects this chapter:** style E moved the `.mega` to `3.0%` (s14), which has no comma
  and per the CSS comment descends 4.7px, so the fix cannot fire here. The frame that
  carried the original defect is now `₹10,00,000` as a **`.huge`** at s16. I zoomed
  `#s16-stack` at 48.13s (`snapshots/qa/b3/`) rather than assume: the comma ink clears
  the `ILLUSTRATIVE …` foot with a wide margin. **`.huge` is clean at this size and
  needs no fix** — storyboard §3's claim that the defect "recurs on every lakh and crore
  rung" is about `.mega`, and §7 puts exactly one `.mega` in the whole cut. Nothing to
  carry forward.
- **The fill-opacity floor is not reintroduced** — there is no drawn art in this chapter
  at all, so the `.18` funnel cannot come back.

## 5. One real system gap, patched locally and reported

**Not** the en-ch2 patch: I checked, and `.scene.centred .stack { padding-left: 0 }` is
already upstream in the scaffold (line 189), so this build carries **zero** occurrences
of it and none of its now-false "SYSTEM GAP" comment. It inherits the fix.

The gap I did hit is the same *shape*, one rule over:

```css
/* scaffold chapter-design.css */
.arch-b .foot { max-width: 900px; margin-top: 4px; }
.arch-b .huge { max-width: 900px; }
```

`.scene.centred .stack` resets the stack's own geometry but **not the 900px cap on
`.huge` / `.foot`**, and that cap exists only because in the FIGURE archetype the type
shares the frame with the art plate at x1120. On an `art-off` + `centred` B scene the
plate is `display:none`, so the cap is a leftover of a layout that is not on screen: a
36-character statement sets as three short lines in a 900px column with ~500px of empty
frame either side. It hits **five scenes here (2.6–2.10) and every centred B scene of
chapters 3–7**. Patched locally to the centred stack's own `max-width: 1500px` — not a
new value:

```css
.scene.centred.arch-b .huge,
.scene.centred.arch-b .foot { max-width: 1500px; }
```

**Recommend porting to `tools/scaffold/assets/chapter-design.css`** exactly as the
padding-left one was, so ch3–ch7 inherit it instead of each build re-deriving it. I did
not edit the scaffold — that is a deliberate system edit, not a build's improvisation.

## 6. Two declared deviations from the letter of the storyboard

1. **s15's copy.** The script's `stmt:` is *"3.0% is chosen. The reason is in Chapter
   5."* The frame renders *"3.0% is chosen. The reason comes later."* §3's no-rail rule
   is absolute — *"the viewer must never be shown that this video is chapter-based"* —
   and §3a already struck the same reference off s5, s39 and s61. The VO says «इसकी वजह
   आगे आएगी», literally *the reason will come later*, so the frame now agrees with the
   voice instead of contradicting the rule. **Flagged for fin-editor, not settled here.**
2. **s17→s18's ken direction.** §6b prints `o 1.16→1.08, then 1.08→1.00`, but that row
   is internally inconsistent with §5's alternation rule: §6b also fixes s14/s15 as `i`,
   which forces s16 `o` and therefore s17 `i`. Physically it is also the wrong way
   round — both second files are *tighter* crops, and a tighter crop can only continue a
   push **in**. Both pairs push in. That fixes the chapter's parity and the one repeat it
   forces is placed at the **chapter joint** (ch1's s8 pulls back, s9 pulls back) rather
   than inside the chapter — the least visible place for it, between two unrelated
   photographs across a dissolve. Every in-chapter boundary still alternates, and the
   build asserts it.

Also worth one line for the record: **§7 row 15 gives s15 a `span 3.0%` `#sN-rate` that
§4's thirty-one-row table does not list.** I built §7's version (the element exists).
It is an extra rate element on a frame whose whole point is the rate, so it is additive,
not a violation — but the two sections of the storyboard disagree and §4's count is
therefore 32, not 31.

## 7. The five fin-assets caveats — built as briefed, NOT pre-ruled

Each is in its scene's comment in `build.mjs`, so it travels with the frame. All five are
visible on the contact sheets below and are the editor's to rule from the encode:

| # | scene | what to look at |
|---|---|---|
| 1 | **s19** | the telecom cable bundle is a genuinely high-frequency frame under a statement plus a rate line. Legible (AA passed) but it is the busiest frame in the chapter. |
| 2 | **s11** | the pale sky is ~65% of the frame and the amber type sits on it. It is the brightest frame in the chapter by a distance; the tank body itself is near-black, so the recorded high-key failure mode does not strictly apply. |
| 3 | **s17** | numeric keys (`70 50 30 10`) behind a numeric claim — the key reading `30` sits under `AT 3.0%`. It reads as arithmetic made visible, but it is a numeric background under a number. |
| 4 | **s10 / s17** | the adding-machine through-line: s10's office interior carries a small out-of-focus adding machine and s17 is an adding-machine macro. Reads to me as *the office, then the machine that does the sum*, but I did not rule it. |
| 5 | **s9** | two dome-lidded brass-bound chests against the container ladder, which puts a steel trunk at s31 (4.1). **ch4 must pick a trunk that is visibly a different object.** |

One thing not in the caveat list, offered for the same pass: **s10's dome lamp is the
brightest object in that frame and sits directly behind the focal.** Contrast passes AA
and the scrim carries it, but it is the second-brightest frame in the chapter.

## 8. Max-density snapshot pass — 14 frames, three separate `-o` dirs

Sampled at each scene's **last** cue time, deterministic worst case. One directory per
invocation, because `snapshot` wipes its `-o`:

| dir | frames | at |
|---|---|---|
| `snapshots/qa/b1` | **7 looked at** | 2.0 · 7.9 · 13.55 · 19.68 · 27.54 · 36.55 · 40.26 |
| `snapshots/qa/b2` | **6 looked at** | 48.13 · 53.48 · 59.72 · 62.66 · 69.21 · 75.03 |
| `snapshots/qa/b3` | **1 looked at** | 48.13, zoomed to `#s16-stack` (the comma-descender check) |

Every stack sits inside the 150×110 safe area, every frame is centred on frame centre,
nothing overflows, no tofu on any glyph (`₹ · —` all render), and the `cut-hi` watermark
is present bottom-right on all fourteen. The CLI did **not** throw its usual navigation
timeout on any of the three invocations — first attempt each time.

## 9. Sound

`assets/audio.json` is **derived**, not hand-typed: `build.mjs` shells out to
`tools/audio/cues.py` against the file it just wrote, so the cue list and the markup come
from the same derivation of `timing.json`. **17 real cues**, bed `bed-resolve`.

- Both hold joints (s15 at 37.662, s18 at 55.422) carry **no** `transition` — a whoosh
  there announces a change that is not happening.
- The declared DRY scenes (s10–s13, s17, s18, s21) emit their joint and nothing else.
- **One correction the tool cannot make for itself, applied loudly in code rather than
  by hand-editing the output:** `cues.py` derives `hero` from a pop/countUp on any
  `#sN-num`, so it rang s14's `3.0%`. §2 names the hero scenes outright — s16, s62, s64,
  *"no other rung rings"* — so s14 is downgraded to `reveal` in `build.mjs` with the
  reason written into the cue's own `_` field. One downgrade this chapter; s16 keeps its
  `hero` as the video's first corpus.

## 10. Constraint sweep

- `hi_currency_framing` — the banned payout word is grepped over the **whole emitted
  document**, comments included, and throws at build. No `$` anywhere (same guard).
- `no_return_promise` — every figure in the chapter shares its frame with `3.0%`, and
  `ILLUSTRATIVE` appears on s16, s18, s19 and s20.
- §3b font subset — no `/`, no `?`, no `× ≈ → ▶ ¢`, no Devanagari in any on-screen
  string; asserted per string at build.
- `image_per_scene` — 13/13 `has-photo` with a real full-bleed `.bg`, each file existence-
  checked at build. No per-scene grade override anywhere.
- `one_focal_per_scene` — never a `stmt` and a `num` together; `.mega` exactly once.

## 11. What I did not do

- Did not edit `tools/`, `.claude/`, or any design token. The four `hyperframes check`
  warnings (file size, two track-density, heavy-overlay-count 26) are the same set ch1
  and en-ch2 shipped with, and none of them suppresses a pass — Layout, Motion and
  Contrast all ran (12/12 AA).
- Did not render. That is fin-render's stage.
- Did not add an icon to `assets/icons/` — this chapter draws nothing.
</content>
