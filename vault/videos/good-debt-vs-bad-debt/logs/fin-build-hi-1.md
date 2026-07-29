---
slug: good-debt-vs-bad-debt
stage: fin-build
cut: hi
tier: short
attempt: 1
status: ok
updated: 2026-07-28
scope: Composition build — scaffold + index.html for studio/videos/good-debt-vs-bad-debt-hi from the storyboard cue tables wired to the measured timing.json map. npm run check clean.
---

# fin-build — good-debt-vs-bad-debt · hi · attempt 1

## Result
`npm run check` **passed** (exit 0): Lint 0 errors, Runtime 0/0, Layout 0
errors, **Motion 0/0, Contrast 18/18 WCAG AA**. Total composition duration
**195.17s** (3:15.2), root `data-duration` = timing.total, last scene ends
exactly at 195.17.

## Artifacts
- `studio/videos/good-debt-vs-bad-debt-hi/index.html` (370 lines, 9 scenes)
- `package.json` (pins `hyperframes@0.7.66` as a devDependency) + `package-lock.json`
  (committed lockfile via `npm i -D` — **not** `npx --yes`), `meta.json`, `hyperframes.json`
- Vendored `assets/js/gsap.min.js` (GSAP 3.15.0), self-hosted `assets/fonts/NotoSansFinance-var.woff2`,
  `assets/img/grain.png` — all copied from the needs-vs-wants reference. **No CDN / http ref anywhere** (grep-verified).
- `snapshots/` + `snapshots/v2/` — the max-density snapshot evidence.

## How the timing map was built (four copies, one source)
Wrote a generator (scratchpad, not committed) that reads `assets/voice/timing.json`
and emits index.html so the section attrs, the JS `S` map, the `<audio>` rows and
the root `data-duration` are all derived from that one file — never hand-typed.
Cross-checked the emitted HTML back against timing.json: all four copies agree
for every scene (section.start==S.sN, audio.start==scene_start+0.4, audio.dur==clip,
root==total). ✓

**Timing edge fix (not a hand-edit).** timing.json rounds each scene_start and
scene_duration to 3 dp independently, so its raw pairs violate the design
invariant `scene_start[n+1] == scene_start[n] + scene_duration[n]` by ±0.001 —
producing a s5→s6 **overlap (112.692 vs 112.691)** that the hyperframes checker
rejects (`overlapping_clips_same_track`). Fix: each scene's `data-duration` is
generated as `next_scene_start − this_scene_start` (last = total − start),
anchored to the measured scene_start grid + total. This enforces the invariant
exactly and tiles track 1 with **no gap/overlap** (verified all 9). Net effect:
s2 15.140→15.141, s5 23.970→23.969, s9 16.864→16.865; audio clips keep their true
measured durations on track 10.

## Cross-stage handoffs applied
1. **HERO INTEGERS (s7).** Ran the ₹ amortization in node (B₀=₹50,000, i=0.40/12,
   P=max(5%·statement, ₹100), stop B≤0). **months-to-clear 208, total interest
   ₹88,614, total repaid ₹1,38,614 — all three match the locked Python check exactly.**
   The generator hard-asserts 208/88,614 (throws otherwise). On-screen figures
   formatted with `Intl.NumberFormat("en-IN")`, tabular-nums.
   - **12-month balance flagged: displayed ₹40,044, NOT the transcribed ₹40,045.**
     Both the iterative model AND the exact closed form give 40044.10 → rounds to
     40,044; even the doc's own factor 0.981667^12 = 40044.26 → 40,044. The
     transcribed ₹40,045 is a hand-rounding artifact. The storyboard/facts-staging
     both **explicitly instruct the build to regenerate this integer from code and
     NOT use the transcribed value** ("build stage recomputes… not false-precise"),
     so I shipped the computed 40,044. VO says only "क़रीब चालीस हज़ार," consistent
     with either. **Audit note: on-screen 40,044 is intended, not a defect.**
2. **DROPPED CUT-INS.** `#s1cut`, `#s5cut`, `#s6cut`, `#s8cut` DOM nodes and all
   their fade/exit cues removed (grep-verified absent). Those scenes keep only
   their bg. Surviving cut-ins retained: `s3-cutA`, `s3-cutB`, `s4-cut`. index.html
   references only the 12 manifest images (+ grain).
3. **s8 brightness override.** `#s8 .bg { filter: grayscale(.32) brightness(.85)
   contrast(1.02); }` — the alarm-clock bg is near-black; snapshot confirms it now
   reads as texture. This is the one permitted per-video grade override (design §1).
4. **s1 reveal.** Month-1 split synced to speech: YOU PAY ₹2,583 (+10.6) → INTEREST
   ₹1,667 (**+13.10**, pop+pulse) → OFF THE DEBT ₹916 (+15.9). Interest row lands
   ≤15s (audit check 3). ✓ Rows sum on screen (1,667 + 916 = 2,583).
5. **Motion rules.** Each scene has ONE `.bg` with ONE continuous `ken` zoom (no
   same-image self-dissolve). Cards/pills/bills are `--panel` overlays on the still
   (never a flat cream/black card). ken alternates in/out/in/out/in/out/in/out/in.
   Cut-ins are different images crossfading over the base — no flicker.

## Layout fix during the snapshot pass
Max-density snapshots at each scene's densest cue exposed off-centre framing in the
four full-swap scenes (s5/s6/s7/s8): elements that had exited (opacity 0) or not yet
appeared still reserved flex space, pushing s7 top-heavy and s6's flow low. Fix: each
of those scenes is now **two `.stack` layers pinned to the same grid cell
(`grid-area: 1/1`)** — phase A and phase B each self-centre, no cross-reserved space.
s7 phase A = the full math, phase B = the punch alone (added s7r3/s7f to the exit).
Re-snapshot confirms every phase centred, inside the safe area, nothing overflowing.
s1/s3/s9 keep a persistent kicker and read fine as single stacks (unchanged).

## Non-failing findings (benign — not fixed, no token touched)
- Lint `composition_file_too_large` (370 lines) + `timeline_track_too_dense` (9 on
  track 1): inherent to the single-file blockframe-9 architecture the reference also
  ships. Warnings, non-failing.
- Lint `pointer_events_none` on `.grain`: from the design system (grain must not
  intercept). Info.
- Layout `container_overflow` ×10 on the `.bg`/cut-in layers: the deliberate
  `.bg { inset: -8% }` Ken Burns bleed (design §1). Info.
- No token (colour/size/weight) was edited to satisfy the checker. `format.json
  known_benign` is empty; nothing new needed suppressing.

## Type ladder / determinism
Font sizes only from the ladder (112/88/76/54/50/46/44/40/32/30/28/26). No focal
below 76. No `Date.now`, no `Math.random`, no render-time fetch. GSAP paused +
registered on `window.__timelines["main"]`.

## For the -en pass
Element IDs held verbatim (`s1r2`, `s3h`, `s4good/s4bad`, `s6f1-3`, `s7h`, …). The
grid-area:1/1 two-stack pattern for s5/s6/s7/s8 and the tiling-duration derivation
should port. -en will recompute its own $ hero math (different clip lengths → offsets).
