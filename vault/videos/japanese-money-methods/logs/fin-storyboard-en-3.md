---
summary: fin-storyboard, japanese-money-methods, en cut, attempt 3 — full rewrite of storyboard-en.md for the `blockframe-9` architecture after the creator rejected a rendered ledger-rail frame. 92 scenes, 96 image slots / 93 files (unchanged), 24 SFX on bed-resolve, 5 icons, 0 lotties, 3 data-framings, zero max_scene_seconds breaches.
updated: 2026-08-01
source: run directive (architecture change) + timing.json (fresh, 626.743s) + script-en.md + storyboard-hi.md + design-finance-blockframe.md + format.json + kit.json + tools/scaffold/assets/blockframe.css
---

# fin-storyboard · en · attempt 3

**STATUS: ok.**

## What this attempt was

Not a repair. The creator's 2026-08-01 decision moved `run.json architecture` from
`ledger-rail` to `blockframe-9` for both cuts, so the attempt-1/2 storyboard was replaced
in full. Per the directive I read the old file only for beat structure, SFX placement and
image assignments — all three were sound and all three survive.

## What I re-derived rather than ported

| thing | why it had to be re-derived |
|---|---|
| **Type treatment (§3a)** | `.rail` had two type sizes per scene enforced by an 830px content column. `blockframe-9` is a 1620px centred stack, so I defined four scene types — **A** statement (`.huge`@76, 75 scenes), **B** figure (`.huge` 112, 9), **SOLO** (focal alone @88, or `.mega` 240 on s17, 7 scenes), **C** CTA (s91). Every size is a `type_ladder_px` value; `.mega` is used exactly once in the video |
| **The anti-sameness device** | `RAIL OFF` retracted a rail that no longer exists. Same seven scenes now **empty the stack** instead (no kicker, focal alone) — `SOLO`. Same seven, same job, mechanism re-derived |
| **Per-scene `--tint`** | `.rail` retired it (it lived in a scrim the architecture deleted). Restored, and **derived from the role colour by rule** (fund→green .10, warn→red .12, target→amber .12, pop→orange .13, no role→no tint), so 92 values come from one decision instead of 92 |
| **The cue ladder (§4)** | The 5-item `.rail` assembly (panel→idx→hair→beat→head) was furniture. The new ladder is **4 cues** — kicker +0.30, focal +1.10 fixed or anchored, foot/icon +2.10 — and **needs no declared cascade exception**: every gap is ≥0.8s outright. Fewer moving parts, not more |
| **`data-framings`** | Re-derived under the new timing from zero. Landed on the same three scenes (s32, s36, s79) with the same numbers, because none of those three durations changed. No scene needs one to clear 9.0s; all three are enumeration |

## The one real bug I found and fixed

Three SFX families in the ported cue list were **sounds with no helper**, which
`kit.json _discipline` forbids by name:

- the five `stamp` cues (s31, s33, s43, s65, s90) fired against a `rise` focal — there is no
  `.stamp` element anywhere in this cut because the script writes no stamp copy;
- the three `chip` cues (s38–s40) fired against `draw` on an icon;
- the `tick` on s69 fired against `draw` too.

Inventing stamp copy here would put a second home under a fact the script owns. **Fixed at the
ladder instead** (§4, divergence D0f): on the five verdict scenes the focal enters with `pop`
(`back.out(1.7)`) at its anchored word — that *is* the slam; the three checkbox icons enter
with `pop` rather than `draw`; s69's icon `draw`s then `pulse`s at 465.50. No new copy, no new
elements, every cue now bound to a helper that actually runs.

## Directive compliance

- **`.warnc` / `.popc`.** s24's icon is specified `class="icon warnc"` with the trap spelled
  out (`.warn` is a component modifier and matches nothing on an `<svg>`, painting it white).
  SUBSCRIBE is specified as a **`.cta` block**, not `.popc` text — `.cta` sets its own
  `background:var(--pop); color:#0d1017`, so it is structurally incapable of the white failure
  that shipped last build. `.popc` is named as available for pop-coloured text; this cut has
  none.
- **`cut-en` on `#root`** — stated in §3 with why it is load-bearing.
- **Timing verbatim.** Every `start`/`dur` copied from the fresh `timing.json`. Verified
  620.849 + 5.894 = **626.743** = the file's `total`. 7.4's `scene_start` 517.368 and duration
  **7.304** (was 7.148); rows 78–92 all carry the +0.157s shift. Two SFX cues moved with it:
  #23 608.76→**608.92**, #24 616.45→**616.61**. Nothing else in the cut changed.
- **s77+s78 hold intact** — one file (`s77.jpg`), both scenes push `i`, s78 has no file of its
  own, ken continues rather than self-dissolving. Called out again in the sign-off.
- **7.4 no longer promises a square** — the script's stmt was already correct; what was wrong
  was *this file*, whose old SFX cue 22 read "the empty square at the centre". Deleted and
  recorded as divergence D25.
- **Images not re-spec'd.** §7's `bg` column quotes `assets/img/manifest.json` verbatim.
  **`manifest.json` is NOT rewritten by this attempt** — it is already correct at 93 entries
  and rewriting it risks desyncing the `.src` sidecars fin-assets wrote. Deliberate no-op.
- **Bed length not flagged.** §2 carries a one-line note that `mix.py` crossfade-loops the bed
  and there is no dip; the old §2 hazard table and placeholder #2 are deleted, and the
  retraction is divergence **D23** so the hi cut's copy of the flag gets struck too.

## The 1280px upscale — named, as asked (§9a)

52 of 93 files are 1280px (every Pixabay promotion except `s34.jpg`). Full-bleed at
`inset:-8%` draws them ~1.63× — worse than the `.rail` panel's 1.5×, because the panel was
only 740px wide. Not re-sourced, per directive.

**Good news first: no hero or SOLO frame is affected.** All seven `hero` cues (s13, s16, s17,
s25, s30, s51, s55) and all seven SOLO frames (s1, s17, s33, s43, s65, s77, s90) are Pexels
1880px.

Five 1280px slots carry a punctuated or terminal beat, ranked for the creator:

1. **`s91.jpg`** — the `.cta` frame, last full frame of the video. Highest value per pixel.
2. **`s31.jpg`** — the `stamp` at 3.10, the argument's turn, and a *paper* subject where an
   upscale reads as mushy print.
3. **`s73.jpg`** — `4 IN 10`, dry, 2.0s before SHOVE #2; a receipt is fine print.
4. **`s9.jpg`** — the colander at 1.9; the holes are the whole image and they are small.
5. **`s38.jpg`** — CHECK ONE; price tags are the readable detail. Least critical.

**Recommendation: ship all five.** If exactly one is re-sourced, make it `s91.jpg` — a closed
notebook on a desk is a trivially common Pexels subject. Nothing downstream is blocked; the
files pass the gate today.

## Counts

| | |
|---|---|
| scenes | **92** |
| runtime | **626.743s** (root `data-duration`) |
| image slots | **96** — 92 bg (3 re-using a hold partner's file) + 4 cut-ins |
| image files | **93**, all on disk, manifest unchanged |
| SFX cues | **24** on `bed-resolve`; closest pair 6.31s |
| icons / lotties | **5 / 0** |
| transitions | 86 `dissolve` · **2** `shove` · **3** `hold` |
| `data-framings` | **3** (s32, s36, s79), each partitioning its own scene |
| longest scene | **8.349s** (s79) — zero `max_scene_seconds` breaches, no `known_benign` owed |
| divergences vs hi | **26** rows, one reason each |

## Open

- The five 1280px slots await a creator ruling (default: ship all five).
- `format.json cuts.en.chars_per_second` still owed a raise from 16.1 — third measurement at
  **17.39 c/s flat** (9,619 chars / 553.143s of audio). BOTH-OR-NEITHER: budget formula first.
  `tools/` is not writable from this stage.
- `storyboard-hi.md` is **still the `ledger-rail` version**. D0/D0a–D0f and D23 apply to it
  too; it needs the same rewrite before the hi cut builds.
