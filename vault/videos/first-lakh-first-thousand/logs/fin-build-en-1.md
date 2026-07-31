---
summary: fin-build, en cut, attempt 1 — 92-scene swiss-band composition generated from timing.json (505.561s). pipeline_check check build PASSES; `npm run check` has the same ONE system-stylesheet error as the hi cut. Blocking finding from the snapshot pass: s36 carries CANADIAN coins under the video's one hard US statistic, and three more money frames are suspect.
updated: 2026-07-31
source: storyboard-en.md + script-en.md + studio/videos/first-lakh-first-thousand-en/assets/voice/timing.json + tools/format.json + tools/scaffold/ + logs/fin-assets-en-1.md + logs/fin-build-hi-1.md
stage: fin-build, cut en, attempt 1
---

# fin-build — «The First $10,000 Is The Hardest» en, attempt 1

## Result

| | |
|---|---|
| Composition | `studio/videos/first-lakh-first-thousand-en/index.html` (92 scenes, 1722 lines) |
| Generator | `build.mjs` — every duration derived from `assets/voice/timing.json`, nothing hand-typed |
| Duration | **505.561 s** (8:26), root == timing.json total == last scene end |
| `pipeline_check check build` | **PASS** |
| `npm run check` | **1 error, 95 warnings, 1 info** · Runtime 0/0 · Motion 0/0 — the one error is in the linked system stylesheet (below) |
| Snapshots | **92 / 92** scenes captured at their max-density cue, 8 batches, one `-o` dir each |
| Verdict | **fail** — the composition is complete and correct; an image is not (§Blocking) |

## What was built

- Scaffolded from `tools/scaffold/` — pinned `hyperframes 0.7.66` via the committed
  lockfile (`npm i -D`), vendored GSAP, self-hosted FinanceSans, `grain.png`.
  **No network reference of any kind**; `check` confirms.
- `blockframe.css` and `motion.js` are **linked, not copied**. The composition adds only
  `.v-*` one-offs in one inline `<style>` after the link.
- `data-start`/`data-duration`, the JS `S` map, the 92 `<audio>` rows and the root duration
  are emitted from `timing.json` in one pass, so the four homes cannot drift.
- Transitions: `sceneTransitions(..., { acts: ["s51","s63"] })` — 89 dissolves + the two
  shoves the storyboard names (5.9→5.10, 6.10→7.1). Scenes 1–91 carry
  `scene_duration + 0.45`; tracks alternate 1/2. Both asserted by `check build`.
- Continuous-zoom pair 5.2+5.3 (s43+s44): **one `ken` tween across both scenes' `.bg`**,
  so the phase matches and the 0.45 s crossfade is invisible. Verified in the snapshots —
  frames 231.25 s and 236.05 s show the same balance at a continuous zoom phase.
- `assets/audio.json`: `bed-resolve` + the 23 SFX cues, absolute seconds, all names from
  `tools/audio/kit.json`, closest pair 2.84 s. **No music/SFX `<audio>` rows** — voice only,
  track 10.
- The one permitted per-scene grade override is on **s90** (`brightness(1.25)`), per
  fin-assets note 1. No second override.
- **s68 demoted `R` → `B`**, taking storyboard §9's own fallback (fin-assets note 2:
  the coal bed's left third is well above the 25 % luminance ceiling). The cut ships
  **8 reversed-field scenes, not 9**; `R` count is a design choice, not a checked constant.
  Aperture mix as built: 58 B · 18 C · 8 R · 8 M.

## BLOCKING — wrong-currency imagery on a `$` cut

The max-density pass caught what the fetch-time screen did not. fin-assets rejected euro
and złoty cells; **Canadian coinage looks American at contact-sheet size and got through.**

1. **s36 (4.6) — hard fail.** Zoomed to 2× the band reads **`CANADA` `DOLLAR`** on the
   loonie, **`D·G·REGINA`** on a second coin, and a **`5 CENTS`** beaver nickel. This is the
   frame under **`2.7%` — the BEA national personal saving rate**, the single strongest
   US-only number in the packet and the reason this cut runs 23 SFX cues to hi's 22
   (storyboard §8 divergence 6). A Canadian coin tray under a US federal statistic is the
   `us-english-script-style` failure, not a texture quibble.
   Evidence: `snapshots/qa/zoom-s36/frame-00-at-194.66s.png`.
2. **s88 (9.6) — suspect.** A pile of **gold-coloured** coins under
   "The tenth $10,000: the same market buys 6.5". The US has no gold-coloured circulating
   coin at that scale; this reads euro/pound. It is also not the storyboard's subject
   ("the full glass jar from 1.2" — the recall pair with s2 is lost).
3. **s59 (6.7) — suspect.** fin-assets' own watch item, confirmed at 2×: the loose pile
   around the copper stacks is visibly mixed foreign coinage. Dark and low-salience, and the
   VO makes no currency claim on the frame, so this is the weakest of the three.
4. **s12 (2.2) — indeterminate.** Plain milled silver stacks, no legible markings. Passes on
   the evidence available; listed so it is not re-litigated.

**Fix is cheap and does not touch this stage's output:** re-pick from the existing
`_cand/` sheets and keep the filenames — `node build.mjs` then reproduces `index.html`
byte-for-byte around the new images, and `run.json budget.pixabay_calls` stays at 0 if the
existing sheets have a usable cell.

## Second finding — s84's legible credit-card form (fin-assets' own trigger fired)

fin-assets note: *"the grade should bury them, but if the build shows them, re-pick cell 3
of the same sheet."* The build shows them. At 456.65 s the frame reads
**"Credit Card/Debit Card Auth…"** clearly, under "One automatic transfer, dated the day
after payday". The storyboard's hard guard (never a phone) is satisfied, but a credit-card
authorisation under a savings-transfer instruction argues against a persona that makes no
product picks. Same re-pick, same zero cost.

## Watch items (not blocking — for Gate ②)

- **s22 minor** reads **"Platinum Credit Card · Cardmember Agreement"**, where the storyboard
  asked for a rate card. Same off-message class as s84, but it is a 630 px minor rectangle.
- **s71 (8.1)** — three painted seaside doors, teal/yellow/red. The most saturated frame in
  the cut by a distance; the grade does not tame it and it reads Irish/UK, not US.
- **s64 (7.2)** — blue smoke, where the VO says "Matches. Kindling. That's it." The keyword
  rule (design §5.3) is not met by this frame; the chapter's other seven frames carry it.
- **s24 (3.4)** apothecary boxes for "a heavy toolbox"; **s48 (5.7)** a basket rim for
  "a hardback book". Harmless texture, keyword lost.
- **s13 / s38-minor** — the wall calendar is bilingual (`November / Noviembre`). Normal in
  the US; noted only because "foreign-language text in frame" is a standing rejection.
- **s89** keeps the "Hachita / Antelope Wells" place names, as fin-assets decided.

## The one remaining `npm run check` error — a SYSTEM defect, unchanged from the hi cut

```
✗ invalid_parent_traversal_in_asset_path: 2 asset path(s) traversing above the project
  root with "../" (../fonts/, ../img/)
```

Both strings are in `tools/scaffold/assets/css/blockframe.css` (lines 24, 79); the
composition contains no `../`. **This stage may not write `tools/`**, and diverging the
project's copy is what the 2026-07-29 audit forbids, so it is reported, not patched. It is
a false positive for a linked stylesheet — CSS `url()` resolves against the *stylesheet*, so
`assets/css/../fonts/` is `assets/fonts/`. Verified empirically: every one of the 92
snapshots renders in real FinanceSans at weight 900 (not the Arial Black fallback the audit
found on four cuts) and the grain is visible. Runtime check: 0 errors.

Minimal correct fix for whoever owns `tools/`: move `blockframe.css` to
`assets/blockframe.css` and use `fonts/…` / `img/…`. Do **not** take the linter's suggested
`assets/fonts/…` — from `assets/css/` that resolves to `assets/css/assets/fonts/` and 404s
for real. **Second cut in a row reporting this; it is a two-line fix upstream.**

Also unchanged from hi and still worth the system's attention:
1. **swiss-band puts the rule and the statement in different columns** — `.swissrule` and
   `.stack` both declare only `grid-row: 4` and get auto-placed into two implicit columns.
   Worked around here with `.v-col1 { grid-column: 1 }`. Snapshot-confirmed both ways.
2. **`.stamp.warn` paints the verdict red on red** — the fill modifier and the text-colour
   modifier are the same class list, and `.warn` is declared later at equal specificity.
   Worked around with `.stamp.v-stamp { color: #0d1017 }`. All five stamps render correctly
   (s19 red, s29 ink, s51 green, s69 amber, s82 red).
3. **92 `<audio>` rows stall page load past the snapshot CLI's fixed 10 s navigation
   timeout** without `preload="none"`. `check` warns about it 92 times; without it, every
   snapshot fails. `id` on each row is separately required (`media_missing_id` → silent
   render). ⚠ fin-render must confirm the master actually carries voice.

## Storyboard helpers that do not exist in `motion.js`

Identical mapping to the hi cut — none was invented inline:

| storyboard | used | note |
|---|---|---|
| `bandOpen` | *dropped* | the scene's own `dissolve` already is the aperture arriving |
| `hang16` / `hang12` | `rise(sel, at, dur, 16 / 12)` | `rise` already takes the travel distance |
| `ruleDraw` | `fill` | needed `.v-ruledraw { transform-origin: left }` |
| `scaleArrive` | `rise(..., 12)` | §3 retires `back.out` in swiss-band, ruling out `pop` |
| `wipeX` / `wipeY` | `fade` | a hard directional wipe is not in the vocabulary |

Also unavailable: **half-amplitude `ken`** — `ken()` has fixed endpoints (1.0↔1.16, ∓2.5
xPercent), so the storyboard's 1.0↔1.06 inside the band is not expressible without editing
`motion.js`. System amplitude everywhere; the `.v-ap` wrapper gives the photo
`left:-3%; width:106%` so the xPercent move never exposes `--bg`.

## Glyph safety — new in this cut

`build.mjs` now asserts every emitted character against the FinanceSans subset. Verified
absent from the woff2 cmap and therefore rewritten in the scene table rather than trusted:
`→ ~ × ≈ ½ ¼ ¾ … °`. So `½ MONTH` → `0.5 MONTHS`, `6½` → `6.5`, `~10%/yr` → `around
10%/yr`, `~$100,000` → `NEAR $100,000`, `$800 × 12` → `$800 a month for 12 months`,
`≈10%` → `around 10%`. The decimal forms also agree with storyboard §6's rounding rule,
which already renders `12.5` and never `13`. A future copy edit that reintroduces one of
these fails the build instead of silently falling back to a system face.

## Design decisions the audit should look at

- **Grade.** The storyboard asks for `grayscale(.85) brightness(.55) contrast(1.25)` in
  swiss-band; the system ships `.32/.62/1.05` and a grade is a **design token**, so it was
  not edited. Consequence is visible in the snapshots: the saturated frames (s71 doors,
  s21 receipts, s81 jars) are louder than the style intends. If the darker swiss grade is
  wanted it is a deliberate edit to `tools/scaffold/assets/css/blockframe.css`.
- **Type sizes come from the system ladder, not the storyboard's prose.** Bar = `.huge` in
  `.swissbar` (96), focal `num` = `.huge` (112), focal `stmt` = `.head2` (54),
  `stamp` = 44, foot = 26. The storyboard's 84/200/54 are not on the ladder. Bars, nums and
  stamps **step DOWN** when a line will not fit its column; nothing was interpolated and
  nothing went below 76 on a focal. Two bars walk to 76 (`NOT AN ACCOUNT PROBLEM`,
  `THE PART NOBODY SAYS`, both in the 1090 px C-L column) and one to 72
  (`HOW IT ACTUALLY BREAKS`, 1055 px reversed field).
- **One stamp wraps to two lines** — s51 "The first $10,000 is where the HABIT takes over"
  at the 40 px floor in the R column. Snapshot-checked at 277.5 s: the foot still clears the
  frame edge. Same construct the hi cut shipped.
- **Furniture merged into the foot** (`CH 5 · 51 / 92 · …`) instead of two absolutely
  positioned elements, which keeps the 240 px statement zone at bar + one focal + one 26 px
  line — the two-sizes rule — and guarantees every scene carries a foot.
- **Locale.** Figures are pre-formatted `en-US` in the scene table (`$100,000`, `$9,600`,
  `$1,251`); the system already applies `tabular-nums` to `.huge`/`.head2`. No `countUp`
  tween exists in this design, so `Intl.NumberFormat` has no call site — the `en-IN`
  grouping trap is structurally absent rather than avoided.
- **`MUST_FOOT` assert.** The 14 scenes storyboard §6 requires to carry the ILLUSTRATIVE
  foot fail the build if their foot is empty. A months-to-milestone figure without it is a
  model output spoken as a statistic.

## Snapshot method — stated precisely, because the hi cut's claim was wrong

Every scene's LAST cue time is read back **out of the emitted `index.html`**
(`snapshots-at.mjs` greps the `rise("#sN-focal", …)` the build actually wrote), so the
capture time cannot drift from what animates. Times are in `snapshots-at.txt`.

- **One `-o` directory per batch**: `snapshots/qa/b1 … b8`, 12 scenes each except b8 (8).
  Nothing was overwritten; all 92 PNGs are on disk.
- The CLI's `Navigation timeout of 10000 ms exceeded` hit on 4 of 8 batches; the runner
  retries up to 25× per batch. Attempts needed: b1 1, b2 1, b3 5, b4 5, b5 2, b6 1, b7 4,
  b8 3.
- **What I actually looked at: all 92 frames, at contact-sheet resolution** (15 sheets,
  ~605 × 340 per cell — enough for overflow, safe area, colour role, focal presence, and
  gross subject). **Five frames were examined at full or higher resolution**: s5 (full
  1920×1080, reversed-field legibility), s36 (2× zoom on the band — this is what caught the
  Canadian coins), and s12 / s59 / s88 / s2 (band crops upscaled for the currency sweep).
  The blocking finding was **not** visible at contact-sheet size, which is the lesson: a
  currency check needs a zoom on the money frames, not a sheet.
- Layout result: **`.stack` sits inside the safe area on all 92 frames**, nothing overflows,
  every scene carries bar + rule + focal + foot, and no frame shows two focal elements.

## Still open (not this stage's to close)

- **Anchored cues are the storyboard's `f` fallbacks, not word-level timings.**
  faster-whisper is outside this stage's allowlist. All 27 anchored times are asserted at
  build time to fall inside their own scene.
- **The hard directional wipe is unproven against `ffmpeg scdet`** (storyboard §10). Built
  as the system `dissolve` at the same 0.45 s, so the scene arithmetic is identical either
  way and the fallback is already the shipped state.
- **`bed-resolve` is 248 s against a 505.561 s cut and the second loop dip lands on the
  CTA** — `run.json owed_before_mix` stands, and storyboard §8 divergence 15 is right that
  it is strictly worse here than on hi.

## Files

- `index.html`, `build.mjs`, `snapshots-at.mjs`, `snapshots-at.txt`
- `assets/audio.json` (bed-resolve + 23 cues), `assets/css/blockframe.css`,
  `assets/js/{gsap.min.js,motion.js}`, `assets/fonts/NotoSansFinance-var.woff2`,
  `assets/img/grain.png`, `package.json`, `package-lock.json`
- `snapshots/qa/b1…b8` (92 PNGs + 15 contact sheets), `snapshots/qa/zoom-s36`
