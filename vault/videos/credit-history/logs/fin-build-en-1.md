---
summary: Gate ④ composition build for credit-history en — 9-scene blockframe generated from timing.json by build.mjs, 173.227s. npm run check passes first run (0 errors, 22/22 contrast, 0 layout, 0 motion); the max-density snapshot pass then found 5 defects the checker was green on and all 5 are fixed. Font-subset audit killed two typed glyphs (× and §) before they could silently fall back.
updated: 2026-07-29
source: vault/videos/credit-history/storyboard-en.md + logs/fin-assets-en-1.md (6 dropped cut-ins, 1 filter override) + studio/videos/credit-history-en/assets/voice/timing.json + [[../../knowledge/design-finance-blockframe]] · reference impl studio/videos/needs-vs-wants-en/ via credit-history-hi/build.mjs · hi-cut lessons from logs/fin-build-hi-1.md + fin-render-hi-1.md
---

# fin-build — credit-history · en · attempt 1

**Result: `npm run check` PASSED.** 0 errors · 2 warnings · 1 info ·
Runtime 0/0 · Layout 0 issues / 9 samples · Motion 0/0 · **Contrast 22/22 WCAG AA**.
**Total composition duration: 173.227s (2:53.2)** — exactly `timing.json total`.

## Scaffold

`studio/videos/credit-history-en/` · pinned `hyperframes@0.7.66` as a
`devDependency` with a committed `package-lock.json` (lockfileVersion 3, resolved
`hyperframes 0.7.66` — never `npx --yes`). Vendored `assets/js/gsap.min.js`,
self-hosted `assets/fonts/NotoSansFinance-var.woff2`, `assets/img/grain.png`.
**Zero network references** — verified by regex over the emitted HTML, not by
trust. No `Date.now()`, no `Math.random()`. Timeline paused and registered on
`window.__timelines["main"]`; all 9 scenes `class="scene clip"`
`data-track-index="1"`, all 9 audio rows `data-track-index="10"`.

## `build.mjs` generates `index.html` — the four homes cannot drift

`node build.mjs` reads `assets/voice/timing.json` and emits the `<section>`
attrs, the JS `S` map, the `<audio>` rows and the root `data-duration` from the
one source. Verified programmatically after every regeneration: four copies
agree, every `audio_start − scene_start` is exactly 0.400, every scene
butt-joins the next, root == last scene end == `timing.json total` == **173.227**.

**The rounding trap fires on this cut too**, in both directions: `s6.scene_start
+ s6.scene_duration` = 104.897 against `s7.scene_start` = 104.896 (a 1 ms
*overlap*, which the linter fails as `overlapping_clips_same_track`), and s7→s8
leaves a 1 ms *gap*. Starts are authoritative; durations are derived as
`next.scene_start − this.scene_start`. Ported straight from the hi build.

**s7's four integers are calculator output, not transcribed.**
`EMI = P·i·(1+i)ⁿ/((1+i)ⁿ−1)`, P = $25,000, n = 72, i = APR/12 at 6.30% and
19.42%. Each **payment rounds first**, then subtracts — `$590 − $418 = $172`
(rounding the difference would print $173 and disagree with the screen).
Interest = `round(172 × 72 / 100) × 100` = **$12,400** (raw 12,384).
`Intl.NumberFormat("en-US")`. A four-value assertion in `build.mjs` throws if the
model or the rounding order ever moves, so the VO can never silently disagree
with the screen.

## The font-subset audit — two typed glyphs killed before they could fall back

The subset is **97 codepoints** (full ASCII printable minus `< > \ ^ \` { } ~`,
plus `—` `–` `·` curly quotes `$` `₹`). Decoded the WOFF2 table directory and
cmap directly to check, because a *missing* glyph does not render as tofu — it
silently falls back to `system-ui` at a different weight, which is exactly how
the design doc caught Archivo Black dropping U+20B9.

| Glyph | Verdict | What shipped instead |
|---|---|---|
| `×` U+00D7 | **ABSENT** | `#s9d` reads `WEAK SCORE = 3x RATE` (20 chars, the storyboard's own named fallback). No font substitution. |
| `§` U+00A7 | **ABSENT** | `#s5f` reads `Fair Credit Reporting Act · 15 U.S.C. 1681c(a) · CFPB`. Citation intact without the section mark. |
| `~` U+007E | **ABSENT** | `#s7band1/2` read `ABOUT 6%` / `ABOUT 19%` — a direct rendering of the tilde's meaning, no decimal APR, no quarter label, no lender name. |
| `→` U+2192 · `▶` U+25B6 | absent (known) | CSS-drawn `.arr` / `.arrow` / `.tri`, as the system already specifies. |

Then swept **every** visible character in the generated HTML against the cmap:
**73 distinct glyphs, 73 present.** Nothing on screen can fall back.

## Storyboard divergences (all deliberate, all reasoned)

| # | Change | Why |
|---|---|---|
| 1 | **6 cut-in cues removed** — s1 cues 2/6/10, s3 cue 9, s4 cue 5, s5 cues 5+9, s7 cue 4; `#s1cutA/B`, `#s3cut`, `#s4cut`, `#s5cut`, `#s7cut` never emitted | Dropped at the asset stage. All 9 scenes keep their `.bg` — `photo_free_scene_ratio` 0 held, 9/9 photos. |
| 2 | **s4's dropped cut-in replaced by a `pulse` on `#s4r1` at +9.9** | Exactly fin-assets' prescription for the emptied +8.0→+11.0 window. No unrelated photo substituted. |
| 3 | **s3 exits `#s3ha`/`#s3hb` at +14.0, not +15.4** | The storyboard exits them 1.0s *after* the focal enters; with grid-pinned stacks that renders two 54px heads over the 240px mega. The 0.4s fade now completes exactly as `#s3scale` pops. Same call the hi cut made. |
| 4 | **s6 flow node 3 is `AUTO-PAY or ALERT` (17), not `AUTO-PAY or CALENDAR ALERT` (26)** | Over the 22-char chip cap. Restructured (shortened), not shrunk below the ladder. The VO carries "calendar alert". |
| 5 | **`#s5ctr` reads `YEAR 1 OF 7`, not `YEAR 1 → YEAR 7`** | A `countUp` writes one number into one span; a static arrow form cannot count. Same semantic, same construct as the hi cut's `MONTH 1 OF 36`. |
| 6 | **s8's `#s8disp` exits at +15.6 (with the cut-in), foot rises +16.2** | Storyboard has disp exiting at +17.0 and the foot at +16.0 — a 1.0s overlap inside the shared `.swap` grid cell would double-print. Moved to a clean 0.2s handoff; the reveal gap is still 3.5s. |
| 7 | **s7's punch lives in its own grid-pinned stack** | The hi cut had to lift a single stack by a **measured 290px** to stop the punch stranding in the bottom third. Pinning is deterministic and needs no tuned constant. |
| 8 | **`#s5chip` pinned out of the stack flow** (see snapshot defect 3) | Its exit at +12.6 otherwise left a reserved hole mid-column. |

`#s3g2`, `#s4r3`, `#s4r4`, `#s5grid`, `#s5q`, `#s8free` do not exist in this
cut, per the storyboard's divergence table. No percentage appears anywhere on s6.

## What the max-density snapshot pass caught that `npm run check` did not

The checker was **green on all five**. Frames at each scene's last cue (14.60 ·
25.51 · 47.33 · 65.10 · 80.50 · 102.99 · 131.50 · 151.65 · 171.82) plus the two
cut-in windows (95.59 · 147.65), the s7 densest frame (128.90) and the s5 chip
window (74.60). `snapshots/qa1` → `qa3`.

1. **s1 · the index cards blew out under the filter override.** fin-assets
   specified `brightness(.95)` with the ceiling *"if the white index cards blow
   out, come back toward .78"*. They do: at .95 the card stack bottom-right sat
   brighter than the `--muted` verdict landing over it. **Taken to .78** — still
   a large lift off .62, so the flat black field keeps the tonality `ken` needs.
   Same class as the hi cut's over-bright-paper defect, and the same lever
   (the one permitted filter, inside its recorded ceiling) — **not a token edit**.
2. **s4 · legible German weekday names on a US-market background.**
   `Dienstag` / `Mittwoch` / `Donnerstag` read clearly through the grade in the
   first frame. The image's **subject is right** (a date grid) and only incidental
   text is wrong, so this is the reposition case, not the hi cut's delete case.
   Framed to the bottom-right of the plate (`background-size: 175%;
   background-position: 100% 100%`) — ruled cells and the hour-column numerals,
   **no word in any language**, and softer, which is what the densest scenes want.
3. **s5 · a ~160px hole between the counter and the source line.** `#s5chip`
   exits at +12.6 and its flex row stayed reserved — the hi cut's s8 defect in a
   new place. The bankruptcy caveat is an **aside, not a column item**: pinned to
   the top-right inside the 192–1728 title-safe box, out of the stack flow. Exit
   now leaves nothing behind and the remaining six rows space evenly.
4. **s6 · the wall-clock cut-in fought the scene.** At opacity 1 the high-key
   clock face sat *brighter* than the green `.huge` and the muted subline over it,
   and `ken` enlarged the red second hand well past fin-assets' "hairline at ~1%
   of frame area" — red, in the one scene where red means the miss. **Ghosted to
   0.45** (the hi cut's precedent was 0.55). The scene's own dark bg carries the
   type again and the clock still reads as the due-date cut-in.
5. **s8 · the red-pen cut-in did the same to the dispute line.** The pen sits on
   the brightest paper in the video and the muted `.sub` runs right across it.
   **Ghosted to 0.55**; the lantern keeps the type bed and the red marks still read.

Also carried in from the hi cut *before* the first snapshot, so they never
appeared as defects: the `.counter` panel bed (`#s5ctr` is `--warn` at 96px over
a photograph, which measures ~2.6:1 bare — fixed with an existing component, not
by lightening `--warn`), the `.swap` grid cell on s8, `data-layout-allow-overflow`
on every `.bg`, and grid-pinned phase stacks on s3/s6/s7.

## Design-system conformance

- **Type ladder only:** 240 (`.mega`, s3) · 112 (`.huge`) · 96 (`.counter`) ·
  54 (`.head2`/`.rank`) · 50 (`.billrow.total`) · 46 (`.cta`) · 44 (`.stamp`/
  `.arrow.fx`) · 40 (`.sub`/`.billrow`/`.decision`/`.pct`/`.subline`) · 32
  (`.chip`) · 30 (`.kicker`) · 28 (`.collabel`) · 26 (`.foot`). **Nothing
  interpolated; no focal below 76** — s7's punch stayed at the full 112 because
  the pinned stack gave it the room the hi cut had to buy by dropping to 88.
- **Colour per the storyboard's table, checked frame by frame.** Amber = the
  report / the score / the seven-year clock under examination (`#s1q`, s3 track,
  `#s5fill`). Green = what builds it (both s4 weight bars, `#s4q`, s6's whole
  path, s8's two actions, `#s9b`, `#s7band1`). Red = the miss and its price
  (`#s1stamp`, `#s5mark`, `#s5ctr`, `#s5fix2`, `#s5chip`, `#s7band2`, both s7 cost
  rows, `#s7q`, `#s9c/d`). Orange = CTA only. **`#s6u2`'s "not the minimum"
  renders `--muted`, not `--warn`** — the anti-drift check the storyboard called
  out. The year-zero mark is red; nothing on-time is.
- **STANDING BAN held.** Regexed s7's whole `<section>`: no `670`, no `781`, no
  numeral from the score scale, in copy, in a foot or in an image. The bands are
  named in words (`TOP CREDIT TIER` / `SUBPRIME`) and `#s3g1`'s `670+` lives 78s
  earlier, never co-present.
- **Every scene carries a full-bleed `.bg`**; `ken` alternates
  in/out/in/out/in/out/in/out/in and runs each scene end to end, so no frame is
  ever static. The two surviving cut-ins run `ken` opposite their scene.
- **≤6 simultaneous, ≤3 chips/row, ≤22 chars/chip, ≥0.8s between cues**, no
  cascade declared anywhere (the storyboard retired all three). Every scene opens
  at +0.40. Measured peaks with the dropped cut-ins gone: s1 4 · s2 6 · s3 5 ·
  s4 4 · s5 6 · s6 3 · s7 5 · s8 4 · s9 5.
- **s5 hero built to its invariants:** 7 year-ticks; the amber fill sweeps
  +4.6→+15.5 (linear, `ease:"none"`) as the scene's continuous motion; the warn
  mark slams at **year zero** on «most negative information» (+4.2), sits above
  the fill and stays lit while it passes; it clears only as the fill crosses YEAR
  7 (+15.5); the correction block reveals **after** the mark (+11.2 vs +4.2).
- **Only 35 and 30 reach s4** — no 15/10/10 tail, no ring, no fifth row. The two
  bars are proportional by construction: the *track* width is the datum (350px
  and 300px of a 1000px = 100% reference), so both start at the same x.

## Remaining findings — not defects

| Finding | Judgement |
|---|---|
| `composition_file_too_large` (452 lines) ⚠ | Structural to blockframe-9: one self-contained file per cut is the format. Identical on the shipped pair and on the hi cut. |
| `timeline_track_too_dense` (9 clips on track 1) ⚠ | Same — the architecture *is* nine scenes on one track. |
| `pointer_events_none` on `.grain` ℹ | Studio-editor selectability only. The grain is decorative. |

**Same three as the hi cut; no new finding, and no design token was touched.**
Still worth adding to `format.json known_benign` — that edit is the
orchestrator's, not this stage's.

## Carried forward

- **Every anchored cue is still char-interpolated** from the storyboard; no
  faster-whisper refinement ran (whisper is not on this stage's allowlist). The
  one gate that matters is structurally safe: s1's on-screen payoff `#s1q` lands
  at **+3.0**, 12s inside the audit's ≤15s bound regardless of delivery rate.
- **s5's `QUALITY` seal** is effectively invisible under the grade + scrim in
  every frame checked; the `.counter`'s opaque panel bed covers the area anyway.
  No crop needed.
- **6 dead cut-in JPGs + `.src` sidecars** (`s1-cutA`, `s1-cutB`, `s3-cut`,
  `s4-cut`, `s5-cut`, `s7-cut`) remain on disk, unreferenced and absent from the
  pruned manifest. fin-assets verified none collides with anything, so a future
  md5 ledger sweep stays clean — left in place deliberately.
- **s6-cut and s8-cut are now ghosted overlays**, not opaque plate swaps. If a
  future stage raises either back to opacity 1, the type contrast defect returns.

## Sign-off

- [x] `npm run check` passes — 0 errors, 22/22 contrast, 0 layout, 0 motion
- [x] Four timing copies generated from `timing.json` and verified equal
- [x] Root duration 173.227s == last scene end == `timing.json total`
- [x] No CDN, no network reference, no `Date.now()`, no `Math.random()`; GSAP vendored, font self-hosted, CLI pinned by a committed lockfile
- [x] Every scene carries a `.bg` + `ken`; ken alternates; no static hold > ~2s
- [x] Every on-screen glyph verified present in the font subset (73/73) — `×`, `§` and `~` never typed
- [x] Max-density snapshot pass at all 9 last-cue frames + 4 extra worst-case frames; 5 defects found and fixed; `.stack` inside the safe area on every one
- [x] Exactly one per-scene filter override (`#s1 .bg`), inside fin-assets' recorded ceiling
- [x] No design token edited to satisfy the checker
- [x] STANDING BAN honoured — no FICO band number anywhere near the Experian APRs
- [x] s7's four integers regenerated from the EMI model with an assertion, not transcribed
- [ ] Render (fin-render's stage — not run here)
