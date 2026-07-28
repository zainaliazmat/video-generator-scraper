---
summary: fin-build run for pay-yourself-first-hi attempt 1 — composition built from storyboard-hi.md, npm run check clean (0 errors, contrast 24/24), 9-scene max-density snapshot pass eyeballed OK, total 178.896s.
updated: 2026-07-28
source: this build session · storyboard-hi.md + assets/voice/timing.json + design-finance-blockframe.md
---

# fin-build — pay-yourself-first · hi · attempt 1

## Result: OK

- `studio/videos/pay-yourself-first-hi/index.html` — 9 scenes, one paused GSAP
  timeline on `window.__timelines["main"]`, total composition **178.896s** (2:58.9).
- Scaffolded from `needs-vs-wants`: vendored `assets/js/gsap.min.js`, self-hosted
  FinanceSans at `assets/fonts/`, grain.png (already staged by fin-assets),
  hyperframes.json, meta.json. No CDN or network reference anywhere.
- package.json pins **hyperframes 0.7.66 as a devDependency with committed
  package-lock.json** (`npm i -D` pattern per the stage contract — the older
  projects' bare `npx --yes` pattern was NOT copied).

## Timing — generated, never hand-typed

- `gen_timing.mjs` (kept in the project, re-runnable) writes all four timing
  copies from `assets/voice/timing.json`: `<section>` attrs, JS `S`/`D` maps,
  `<audio>` rows, root `data-duration`.
- **Deviation from timing.json verbatim, by necessity:** scene `data-duration`
  is derived as `next_start − start` (last: `total − start`) instead of the
  file's per-scene `scene_duration`. Reason: timing.json's independently rounded
  values overlap the next scene by 0.001s (s4: 52.788 + 16.055 = 68.843 > s5
  start 68.842) and `hyperframes check` rejects overlapping clips on one track.
  Still single-source; scene starts and audio starts/durations are verbatim.
- Cue offsets are the storyboard's char-interpolated values. faster-whisper
  word-timing refinement (storyboard "deliberate placeholder") was NOT done —
  no transcript exists in assets and whisper is outside this stage's toolset.
  Flagging for fin-audit: anchored cues carry char-interpolation drift,
  worst-case on the long h3/h7 clips.

## Storyboard implementation notes

- s1 calendar drain: `.track2` with a 20-tick variant (`.ticks.t20`), red fill
  scaleX 1→0 over 2.8s. Three-bg crossfade (+5.0, +10.0), ken IN.
- s3 strike-through: absolute `.strikeline` in the old formula, fill 0→1 +
  color→warn at «कुछ बचता ही नहीं». ASCII hyphen used as the minus glyph
  (U+2212 not trusted in the subset).
- s7 hero: `countSteps()` — `ease: "steps(12)"` over 3.2s, ₹0 → ₹1,44,000 in
  exact ₹12,000 monthly increments, `Intl.NumberFormat("en-IN")`, tabular-nums;
  parallel 12-tick fill also stepped. Fill and counter recoloured `--fund`
  (saved money = green per the colour table). Verified mid-count zoom snapshot
  at +1.6s: **₹60,000** — clean multiple, lakh grouping correct.
- s8 grade override applied (the ONE permitted, from fin-assets log): inline
  `filter: grayscale(.32) brightness(.9)` on the barn-wood `.bg`.
- Ken order in, out, in, out, in, out, in (s1 s3 s4 s5 s6 s8 s9); drift() on
  s2 + s7 stacks full-scene. Exits per storyboard (s6 kicker+chips, s7 sub,
  s8 stamp, s9 kicker) keep simultaneous elements ≤6.
- Arrows/► all CSS-drawn (`.arrow`/`.arr`/`.tri`) — absent from the font subset.

## Check

`npm run check` (hyperframes 0.7.66): **passed — 0 errors, 0 warnings fatal**.
Contrast 24/24 WCAG AA. No token was edited to satisfy the checker; nothing
new needed `known_benign` (list stays empty). Remaining infos: `.bg` bleed
overflow (intentional inset −8% for ken), grain pointer-events, file-size/track
advisories (single-file layout matches the shipped reference pair).

## Max-density snapshot pass

One frame at each scene's last cue (+~0.9s so the entry lands), computed from
timing.json: 11.50 / 26.44 / 51.37 / 65.29 / 87.24 / 108.77 / 136.69 / 153.90 /
178.32 — all 9 eyeballed in `snapshots/`: `.stack` inside the safe area in every
frame, nothing clipped, no overflow, s7 reads ₹1,44,000 (never ₹144,000),
colour semantics match the table (auto-transfer/flip green, drain/₹7 red,
FIRST/5% amber, CTA orange).

## For fin-render

Project renders from `studio/videos/pay-yourself-first-hi/` with the committed
lockfile (`npm ci && npm run render` — do not use bare `npx --yes`).
