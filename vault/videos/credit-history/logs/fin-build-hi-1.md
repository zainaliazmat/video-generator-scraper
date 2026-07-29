---
summary: Gate ④ composition build for credit-history hi — 9-scene blockframe generated from timing.json by build.mjs, 177.642s. npm run check passes (0 errors, 22/22 contrast, 0 layout, 0 motion); 6 defects found and fixed by the max-density snapshot pass that the checker did not flag.
updated: 2026-07-29
source: vault/videos/credit-history/storyboard-hi.md + logs/fin-assets-hi-1.md (3 dropped cut-ins) + studio/videos/credit-history-hi/assets/voice/timing.json + [[../../knowledge/design-finance-blockframe]] · reference impl studio/videos/needs-vs-wants/ via good-debt-vs-bad-debt-hi
---

# fin-build — credit-history · hi · attempt 1

**Result: `npm run check` PASSED.** 0 errors · 2 warnings · 1 info ·
Runtime 0/0 · Layout 0 issues / 9 samples · Motion 0/0 · **Contrast 22/22 WCAG AA**.
**Total composition duration: 177.642s (2:57.6)** — exactly `timing.json total`.

## Scaffold

`studio/videos/credit-history-hi/` · pinned `hyperframes@0.7.66` as a
`devDependency` with the committed `package-lock.json` (never `npx --yes`).
Vendored `assets/js/gsap.min.js`, self-hosted `assets/fonts/NotoSansFinance-var.woff2`,
`assets/img/grain.png`. **Zero network references** — verified by regex over the
emitted HTML, not by trust. No `Date.now()`, no `Math.random()`.

## The one structural decision: `build.mjs` generates `index.html`

The design doc's four-homes rule (`<section>` attrs · JS `S` map · `<audio>` rows ·
root `data-duration`) is enforced *by construction*: `node build.mjs` reads
`assets/voice/timing.json` and emits all four. `index.html` carries a
**GENERATED — edit build.mjs, not this file** banner. Verified after every
regeneration: 4 copies agree, every `audio_start − scene_start` is exactly 0.400,
every scene butt-joins the next, root == last scene end == `timing.json total`.

**The rounding trap this caught.** `timing.json` rounds `scene_start` and
`scene_duration` to 3 dp *independently*, so `s3.scene_start + s3.scene_duration`
= 53.154 while `s4.scene_start` = 53.153 — a 1 ms overlap the linter fails as
`overlapping_clips_same_track` (twice: s3→s4, s5→s6). Fix: **starts are
authoritative** (the audio rows key off them) and durations are derived as
`next.scene_start − this.scene_start`. Every future cut hits this; do not
hand-patch a duration.

`build.mjs` also computes s7's four integers rather than transcribing them —
`EMI = P·i·(1+i)ⁿ/((1+i)ⁿ−1)`, P = 30,00,000, n = 240, Δ = 0.75 / 1.00 pp off a
7.40% top-band card, formatted with `Intl.NumberFormat("en-IN")`. Output
**₹1,390 · ₹1,860 · ₹3.3 lakh · ₹4.5 lakh** — matches the audit's hand
re-derivation exactly. `₹30,00,000` groups lakh-style, not `₹3,000,000`.

## Storyboard divergences (all deliberate, all reasoned)

| # | Change | Why |
|---|---|---|
| 1 | **s3 cue 10, s4 cue 4, s6 cues 6+8 removed** | `#s3cut`/`#s4cut`/`#s6cut` were dropped at the asset stage (brand marks, hash collision). Every scene keeps its bg — 9/9 photos, `photo_free_scene_ratio` 0 held. |
| 2 | **s4's dropped cut-in replaced by a `pulse` on `#s4r2` at +10.0** | Exactly what fin-assets prescribed for the 6.0s r2→r3 window. No unrelated photo substituted. |
| 3 | **s3 exits `#s3ha`/`#s3hb` at +14.2, not +15.6** | The storyboard exits them 1.0s *after* `#s3scale` enters. With grid-pinned stacks that renders two 54px heads on top of the 240px mega. Exited before the focal instead — "one focal per scene" preserved, cue order unchanged otherwise. |
| 4 | **s6 flow node 3 is `AUTO-DEBIT or ALERT`, not `AUTO-DEBIT or CALENDAR ALERT`** | 28 chars > the 22-char chip cap in `format.json`. Restructured (shortened), not shrunk below the ladder. The VO carries «कैलेंडर». |
| 5 | **s5's foot renders as reported speech, no quote marks** | The audit's own recommended option for zero quotation risk. Substance intact. |
| 6 | **s2 gains a `breathe` on row 2 at +6.6** | 4.0s dead gap between chip d (+5.5) and the sub (+9.5); §5.2 no-static-hold. |

## What the snapshot pass caught that `npm run check` did not

Deterministic worst-case frames at each scene's **last cue** (16.80 · 28.80 · 51.50
· 72.30 · 92.95 · 112.70 · 139.05 · 157.00 · 175.40) plus the **6-element peak**
frames (14.00 · 36.96 · 85.64 · 104.88 · 135.21 · 167.90). Check was green through
all six of these:

1. **s1 · the wrong photo under the stamp.** `#s1cutB` crossfades over `#s1cutA`;
   exiting only cutB re-revealed cutA under the verdict stamp. Both now exit at +14.6.
2. **s7 · the punch sat in the bottom third.** k/setup/band1/band2/loan/r1 exit but
   still reserve flex space, so the surviving r2 + foot + q centred at y≈641. The
   stack now lifts 290px on the +21.2 exit — the lift doubles as motion into the punch.
   Value measured off the snapshot, not computed; it is the one tuned constant in the file.
3. **s8 · a ~300px hole mid-frame.** `#s8free`/`#s8disp` exit between the two numbered
   actions. Fixed with a `.swap` grid cell the two notes and `#s8b2` share — **no height
   tween**, so it stays deterministic under non-monotonic seek.
4. **s8 · green 40px type over the brightest paper in the video.** The assets stage's
   `brightness(.95)` override left the document brighter than the type. Pulled to
   `.80`, inside the ceiling that log recorded (`come back down toward .75`).
   **Still the video's only per-scene filter override.**
5. **s1 · legible German form labels.** `s1-cutB` carries `Familienname` /
   `Angaben zum Betrieb` — flagged by fin-assets as the one kept image with foreign
   text. Cropped to the pen and the ruled boxes (`background-size: 195%`), as that log
   suggested. Fragments remain, nothing readable.
6. **s5 · the cut-in fought the hero.** The torn-calendar cut-in is high-key with its
   own large numerals and at opacity 1 competed with the 36-cell grid — two numeric
   systems, one focal. Ghosted to **0.55**: it reads as the three years it means and
   the grid stays the focal.

Also fixed off the first check run: `#s5ctr` measured **2.61:1** (needs 3:1) —
`--warn` at 96px sits over a *photograph*, not over `--bg`. The tool's suggested fix
was `rgb(241,92,92)`. **Not taken.** Lightening `--warn` would degrade every warn
element in this video and the next, and red *is* this video's thesis. Fixed
structurally with a `--bg` panel bed under `.counter` — an existing component of the
system. Contrast then went 22/22.

Also marked the `.bg` `inset: -8%` Ken Burns bleed with `data-layout-allow-overflow`
(the documented marker for intentional overflow). That cleared 12 info findings — so
a *new* layout finding on the next run will be visible instead of buried.

## Remaining findings — not defects

| Finding | Judgement |
|---|---|
| `composition_file_too_large` (426 lines) ⚠ | Structural to blockframe-9: one self-contained file per cut is the format, and splitting into `compositions/` would fragment the diff the vault reviews. Identical on the shipped pair. |
| `timeline_track_too_dense` (9 clips on track 1) ⚠ | Same — the architecture *is* nine scenes on one track. |
| `pointer_events_none` on `.grain` ℹ | Studio-editor selectability only. The grain is decorative. |

**Recommend adding these three to `format.json known_benign`** — they will recur on
every finance cut and there is no structural fix that isn't a format change. That
edit is the orchestrator's, not this stage's (`tools/` is not writable here).

## Design-system conformance

- **Type ladder only.** 290 unused · **240** (`.mega`, s3 — a shipped value) · 112
  (`.huge`) · 96 (`.counter`) · **88** (s7 punch, two lines) · 54 (`.head2`, `.rank`)
  · 50 (`.billrow.total`) · 46 (`.cta`) · 44 (`.stamp`) · 40 (`.sub`/`.billrow`/`.decision`)
  · 32 (`.chip`/`.gloss`) · 30 (`.kicker`) · 28 (`.collabel`) · 26 (`.foot`).
  **Nothing interpolated, nothing below 76 on a focal.** s7's punch went to 88 (not
  112) by *restructuring* the stack, which is the permitted move.
- **Colour per the storyboard's table, checked frame by frame.** Amber = the report /
  the score under examination (s1 `#s1q`, s3 track). Green = what builds it (s4's four
  rows, s6's whole path, s8's two actions, s9b). Red = the miss and its price (s1 stamp,
  s5's one cell + counter + verdict, s7's two cost rows + punch, s9c/d). Orange = CTA only.
  **`not the minimum` renders `--muted`, not `--warn`** — the anti-drift check the
  storyboard called out. The red grid cell is red; no on-time element is.
- **Every scene has a full-bleed `.bg`**; `ken` alternates in/out/in/out/in/out/in/out/in
  and runs each scene end to end, so no frame is ever static. Cut-in overlays run `ken`
  opposite their scene.
- **≤6 simultaneous, ≤3 chips/row, ≤22 chars/chip, ≥0.8s between cues** except the two
  declared cascades (s3 enumeration 0.7s ×3, s6 flow 0.7s ×3). Every scene opens at +0.40.
- **s5 hero built as specified:** 3 × 12 = 36, green fills left→right over +2.6→+17.0
  (0.41s stagger), the `.miss` cell slams `--warn` at +8.0 on «एक चूकी हुई किश्त», never
  clears, and the fill runs past it. Colour tween, not opacity — a filled month stays filled.
- **No percentage weight anywhere on s4** — rows are ranked by position, equal width, and
  `#s4f` says CIBIL publishes none. No bank named and no rate shown on s7, only the spread.

## Carried forward

- **Every anchored cue is still char-interpolated** from the storyboard. No
  faster-whisper refinement ran (whisper is not on this stage's tool allowlist). The
  one gate that matters is structurally safe: s1's on-screen payoff `#s1q` lands at
  **+3.2**, 11.8s inside the audit's ≤15s bound, independent of delivery rate.
- **3 dead asset files** (`s3-cut.jpg`, `s4-cut.jpg`, `s6-cut.jpg` + `.src` sidecars)
  are unreferenced by the composition. `s6-cut.jpg` is byte-identical to
  `needs-vs-wants/s1-bill.jpg` and will show as a false positive in any md5 ledger
  sweep. Worth deleting before the next sweep.
- **`s7-cut` crop** applied as fin-assets asked (`background-position: 22% center`)
  to keep the car fob out of "SAME HOUSE".

## Sign-off

- [x] `npm run check` passes — 0 errors, 22/22 contrast, 0 layout, 0 motion
- [x] Four timing copies generated from `timing.json`, verified equal
- [x] Root duration 177.642s == last scene end == `timing.json total`
- [x] No CDN, no network reference, no `Date.now()`, no `Math.random()`; GSAP vendored, font self-hosted, CLI pinned by lockfile
- [x] Every scene carries a `.bg` + `ken`; ken alternates; no static hold > ~2s
- [x] Max-density snapshot pass at all 9 last-cue frames + 6 peak-simultaneity frames — `.stack` inside the safe area on every one
- [x] No design token edited to satisfy the checker (the one contrast finding was fixed structurally)
- [ ] Render (fin-render's stage — not run here)
