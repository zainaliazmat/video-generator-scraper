---
summary: fin-build run for pay-yourself-first-en attempt 1 — composition built from storyboard-en.md, npm run check clean (0 errors, contrast 19/19), 12-frame max-density snapshot pass eyeballed OK, total 177.772s.
updated: 2026-07-28
source: this build session · storyboard-en.md + assets/voice/timing.json (en) + design-finance-blockframe.md + sibling pay-yourself-first-hi build
---

# fin-build — pay-yourself-first · en · attempt 1

## Result: OK

- `studio/videos/pay-yourself-first-en/index.html` — 9 scenes, one paused GSAP
  timeline on `window.__timelines["main"]`, total composition **177.772s** (2:57.8).
- Scaffolded from the sibling `pay-yourself-first-hi` build (itself from
  needs-vs-wants): vendored `assets/js/gsap.min.js`, self-hosted FinanceSans,
  grain.png (staged by fin-assets), hyperframes.json, meta.json,
  `gen_timing.mjs`. **hyperframes 0.7.66 pinned via committed package-lock.json**
  (`npm install`, no bare `npx --yes`). No CDN or network reference anywhere.

## Timing — generated, never hand-typed

- `gen_timing.mjs` (unchanged from hi — it indexes lines positionally, so en ids
  work as-is) wrote all four copies from `assets/voice/timing.json`: `<section>`
  attrs, JS `S`/`D` maps, `<audio>` rows (en1..en9), root `data-duration` 177.772.
  Scene durations derived as `next_start − start` (same rounding-overlap fix as hi).
- Cue offsets are storyboard-en's char-interpolated values. faster-whisper
  refinement (declared placeholder) NOT done — whisper is outside this stage's
  toolset. Flagging for fin-audit: worst-case drift on the long en7 (29.07s) clip.

## The 7-scene divergence list — implemented, not flattened

- **s1**: `#s1stat .statstrip` (1 IN 4 US HOUSEHOLDS) + `#s1f` BofA foot added;
  `.statstrip` CSS ported from needs-vs-wants-en. 6 simultaneous max ✓.
- **s4**: `#s4t` START WITH 10% chip added. **The ONE grade override applied here**
  (per fin-assets-en log, not s8 like the hi cut): inline
  `filter: grayscale(0.32) brightness(1.4)` on the near-black candle `.bg`.
- **s5**: chips DOORDASH / THE SALE / CARD BALANCE; `#s5m` MEDIAN PAY $1,251/WK
  context chip; stat `$1.00 EARNED → 3¢ SAVED` (¢ renders correctly from the
  FinanceSans subset — verified in the snapshot); BLS+BEA foot; kicker exit at
  +14.9 holds the ≤6 cap.
- **s6**: phase order inverted (flow PAYDAY→AUTO-TRANSFER→SAVED BY 9 AM first,
  exits at +7.4; rails HIGH-YIELD SAVINGS / DIFFERENT BANK / FDIC INSURED
  second); `#s6x` "Roughly 10x the interest…" sub (spelled out — no APY number,
  standing rule; ASCII x, not U+00D7, to stay inside the font subset).
- **s7**: `countSteps()` $0 → $4,800 in 12 × $400 steps over 3.2s,
  `Intl.NumberFormat("en-US")`, tabular-nums, parallel 12-tick stepped fill.
  Mid-count snapshot at +10.6s reads **$2,400 / 6 ticks** — clean multiple,
  en-US grouping. `#s7echo` warn→fund flip built as two stacked `.billrow`
  faces cross-faded at +19.3 (seek-safe — no GSAP callback text swap, which
  can be suppressed on renderer seeks). kicker + sub exits keep ≤6.
- **s8**: chips OPEN BANKING APP → SCHEDULE THE TRANSFER → DAY AFTER PAYDAY;
  5% moved into the sub; NO grade override here (that was the hi cut's barn wood).
- s2/s9 structural ports; anchors re-derived from en timing.

## Motion & layout rules

- ken in/out/in/out/in/out/in (s1 s3 s4 s5 s6 s8 s9); `drift()` on s2+s7 stacks.
- Cascades declared: s5 chips ×3 @0.65s, s6 flow ×5 @0.6s, s8 chip-arrow row.
  All other gaps ≥0.8s; something on screen by +0.5s everywhere.
- Arrows/► CSS-drawn; no Date.now/Math.random; counters locale-formatted.

## Check

`npm run check` (hyperframes 0.7.66): **passed — 0 errors**. Contrast 19/19
WCAG AA. No token edited to satisfy the checker; `known_benign` stays empty.
Remaining findings match the shipped-reference pattern: 2 advisory warnings
(file-size / track-density — single-file layout is the channel standard) and
7 infos (`.bg` inset −8% bleed, intentional for ken).

## Max-density snapshot pass

12 frames at each scene's last-cue time (+ mid-count and echo-flip extras):
15.3 / 29.9 / 46.8 / 63.5 / 83.6 / 105.7 / 118.9 / 121.8 / 135.5 / 146.4 /
149.8 / 176.4 — all eyeballed in `snapshots/`: `.stack` inside the safe area
everywhere, nothing clipped; s7 reads $4,800 (never $4800); echo shows both
faces ($400 warn emergency → $400 fund auto-save); colour semantics match the
storyboard table (counter/flip/rails green, drain/3¢/emergency red, FIRST/10%/
DAY AFTER PAYDAY amber, DO THIS TODAY + SUBSCRIBE orange).

## For fin-render

Render from `studio/videos/pay-yourself-first-en/` with the committed lockfile
(`npm ci && npm run render`).
