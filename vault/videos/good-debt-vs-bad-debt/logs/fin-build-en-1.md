---
slug: good-debt-vs-bad-debt
stage: fin-build
cut: en
tier: short
attempt: 1
status: ok
updated: 2026-07-29
scope: Composition build for studio/videos/good-debt-vs-bad-debt-en. Attempt 1 scaffolded + wrote index.html from the storyboard/timing.json (terminated by a usage limit before it could run the checker). Attempt 2 finished the two defects that pass left open — the absent-glyph fallback and a scene-duration tiling overlap — then verified both gates. npm run check clean (0 errors, 18/18 Contrast AA); pipeline_check build PASS.
---

# fin-build — good-debt-vs-bad-debt · en · attempt 1 (completed on attempt 2)

## Result
`npm run check` **passed (exit 0)**: Lint **0 errors** (2 warn, 1 info), Runtime
0/0, Layout 0 errors (12 info), Motion 0/0, **Contrast 18/18 WCAG AA**.
`pipeline_check check build` **PASS**. Total composition duration **178.582s**
(2:58.6) — root `data-duration` = timing.json total = s9 end (161.221 + 17.361).

Attempt 1 wrote index.html and was terminated by a usage limit mid-fix, so this
is its build log. The hero integers, all cue timing, colours, IDs, imagery and
motion are attempt 1's; attempt 2 changed only what is documented below.

## Fix 1 — absent-glyph fallback (the assigned defect)
The self-hosted `FinanceSans` subset (Latin + punctuation + currency) has no
`~` U+007E and no `>` U+003E, so both rendered in a non-deterministic system
fallback. Every **visible** occurrence removed (the one remaining `~` is inside
an HTML comment, line ~281 — not rendered, left as-is):

| where | before | after |
|---|---|---|
| s7setup1 (~L289) | `$6,000 · ~22% APR · minimum only` | `$6,000 · around 22% APR · minimum only` |
| s7setup2 (~L290) | `~22% — illustrative, typical range` | `around 22% — illustrative, typical range` |
| s7r2 static (~L295) | `215 MONTHS · ~18 YRS` | `215 MONTHS · 18 YRS` |
| s7r2 JS setter (~L418) | `… + " MONTHS · ~18 YRS"` | `… + " MONTHS · 18 YRS"` |
| s7h punch (~L299) | `INTEREST &gt; $6,000 BORROWED` | `INTEREST <i class="gt"></i> $6,000 BORROWED` |

- **`around 22%`** matches facts-staging's instruction ("say 'around 22%'").
- **`18 YRS`** (not "NEARLY 18 YRS"): the value lives in a fixed-width 820px
  `.billrow` with `justify-content: space-between`. "18 YRS" is one char *narrower*
  than the passing original `~18 YRS`, so it cannot introduce a new overflow, and
  the exact `215 MONTHS` beside it already carries the precision (215 mo = 17.9 yr).
  The two copies (static span + JS setter, which overwrites it) both changed so
  they agree.
- **`>` → CSS chevron.** Used the `.gt` class attempt 1 had already added to the
  stylesheet (lines ~147-155) for exactly this — same em-based border technique the
  design system uses for `.arr`/`.arrow`/`.tri` ("→/▶ are drawn in CSS, not typed";
  design §4). `color: inherit` + `currentColor`, so it renders in the h1's `warn`
  red. No token touched.

Snapshot-verified at s7's dense cues (139.4s billrow, 141.4s punch, `--zoom #s7h`):
`around 22%` / `18 YRS` render in the real bold face with no fallback; the billrow
value wraps *inside* its panel (no safe-area overflow); the chevron reads as a
clean red ">" between "$9,506 INTEREST" and "$6,000 BORROWED".

## Fix 2 — scene-duration tiling (pre-existing overlap, same class the hi cut fixed)
`npm run check` (which attempt 1 never reached) rejected the build with two
`overlapping_clips_same_track` **errors**: s3 ended 53.102 but s4 started 53.101;
s8 ended 161.222 but s9 started 161.221. Root cause: attempt 1 set three scenes'
`data-duration` from timing.json's raw `scene_duration`, which is 3-dp-rounded
*independently* of the cumulative `scene_start`, so `start[n+1] == start[n] +
dur[n]` is violated by ±0.001. This is the **identical** defect the sibling **hi**
cut hit and resolved (see [[fin-build-hi-1]] §"Timing edge fix"), documented there
as the correct generation rule, not a hand-edit.

Applied the same house-standard derivation: each scene's `data-duration =
next_scene_start − this_scene_start` (last = `total − start`), and synced the
matching `ken()` duration (the hi cut keeps ken == data-duration). Exactly three
scenes moved, `<section>` **and** `ken` each:

```
s2  11.248 → 11.249      s3  23.082 → 23.081      s8  17.1 → 17.099
```

Track 1 now tiles with zero gap/overlap across all 9 (checker-confirmed). The
`scene_start` grid, the JS `S` map, the `<audio>` rows (audio_start = start+0.4,
audio_dur = measured clip), the root duration (178.582) and every hero integer are
**unchanged**. Net perceptual change: three scene backgrounds hold 0.001s
longer/shorter — imperceptible; the pacing grid every cue fires against is byte-identical.

**Deviation flagged for review.** The attempt-2 brief said "keep all scene timing
byte-identical." That was predicated on the timing being clean — it wasn't; it
carried a checker-failing overlap. The brief also required "npm run check 0 errors
with Contrast AA holding," which is impossible while the overlap stands. I resolved
the conflict toward that explicit gate and the mandated reference (the hi cut),
preserving everything the byte-identical rule protects (hero integers, pacing grid,
colours, VO sync). **Bonus:** the invalid contract had been silently skipping the
Layout and Contrast passes (they reported 0/0 before the fix); with the contract
valid they now sample and report **Layout 12/12 clean, Contrast 18/18 AA** — so
"Contrast AA holding" is now genuinely evaluated, not vacuous.

## Non-failing findings (benign — not fixed, no token touched)
- Lint `composition_file_too_large` (408 lines) + `timeline_track_too_dense` (9 on
  track 1): inherent to the single-file blockframe-9 architecture the reference
  ships. Warnings.
- Lint `pointer_events_none` on `.grain`: from the design system (grain must not
  intercept). Info.
- Layout `container_overflow` ×12 on the `.bg` + `s3cutA/s3cutB/s4cut` layers: the
  deliberate `.bg { inset: -8% }` Ken Burns bleed (design §1). Info. No `.stack`/text
  overflow at any sampled frame.
- `format.json known_benign` is still empty; nothing new needed suppressing. No
  colour/size/weight edited to satisfy the checker.

## Determinism / type ladder (unchanged from attempt 1)
s7 amortization runs in-browser: months **215**, interest **$9,506**, 12-mo balance
**$5,318**, month-1 split **$170 / $110 / $60** — orchestrator-verified. Figures via
`Intl.NumberFormat("en-US")` + tabular-nums. Zero `₹` leak. Font sizes only from the
ladder (112/96/88/76/44/40/32/30/26), no focal below 76. No `Date.now`, no
`Math.random`, no render-time / CDN fetch (grep-clean). GSAP vendored, paused, and
registered on `window.__timelines["main"]`.

## Next
Ready for fin-render. If the 3×0.001s duration correction is unwanted, revert Fix 2
and instead add a `known_benign` entry for sub-frame same-track overlaps — but that
ships a red `npm run check` and re-hides the Layout/Contrast passes.
