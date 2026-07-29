---
slug: good-debt-vs-bad-debt
stage: fin-render
cut: en
tier: short
attempt: 1
invocation: 1 of 2 (GATE-TWO FRAME CHECK — pre-encode; orchestrator owns the encode)
status: ok
updated: 2026-07-29
scope: Frame-level QA gate on studio/videos/good-debt-vs-bad-debt-en/index.html before the ~18-min encode. Snapshotted one full-res frame per scene at each scene's last composed cue (plus a 2nd s7 frame so the bill integers and the chevron punch are both captured — they do not co-exist on screen). Looked at all 9 scenes; full-res verified the two hero scenes + the two densest. FRAME GATE PASS. Master QA (transcribe/loudness/black-scan/runtime) is deferred to invocation 2 after renders/FINAL-1080p-en.mp4 exists.
---

# fin-render — good-debt-vs-bad-debt · en · attempt 1 · invocation 1 (FRAME GATE)

## Result — FRAME GATE: PASS
All 9 scenes render composed, in-safe-area, high-contrast, with their photographic
background present (finance "every frame has an image" rule holds — 9 scene bgs +
3 cut-in layers = 12 manifest images, all loaded). No blank / overflow / missing-image
/ contrast failure at any sampled frame. Hero integers and the absent-glyph fix are
pixel-confirmed. Zero currency/imagery/brand/face violations for the US cut.

## Method
`npx hyperframes snapshot . --at <t> -o snapshots/scenes --no-end` at each scene's
last composed cue time (derived from the GSAP cue list in index.html), full 1920×1080:

| frame | t (s) | scene | composed state captured |
|---|---|---|---|
| 00 | 17.6  | s1 | month-1 split + IT'S A TRAP stamp |
| 01 | 28.2  | s2 | 4 roadmap chips + sub |
| 02 | 51.6  | s3 | good/bad "rent" claims (+ s3 cut-in bg) |
| 03 | 74.3  | s4 | GOOD/BAD classifier + CARD BALANCE = WORST + foot |
| 04 | 96.8  | s5 | INTEREST ON INTEREST + compounding sub + foot |
| 05 | 112.9 | s6 | MINIMUM → +$20/MO → CUTS YEARS OFF + sub |
| 06 | 139.3 | s7 | the bill (5,318 / 215mo·18yr / 9,506) — hero |
| 07 | 141.6 | s7 | the chevron punch — hero |
| 08 | 157.4 | s8 | closing rule + sub |
| 09 | 177.8 | s9 | 4 recap chips + ▶ SUBSCRIBE CTA |

Looked at all 10 via the two contact sheets; full-res read on frames 00, 03, 06, 07.
Snapshot emitted a benign "runtime not render-ready within 5000ms" note — the seeks
demonstrably applied (every scene is correctly composed to its cue state), so it is a
tool-timing warning, not a seek failure; the orchestrator's producer encode does not
use this snapshot path.

## Hero verifications (the required checks)
- **s7 integers — all correct & legible** (frames 06/07): AFTER 1 YEAR `still $5,318 owed`;
  TIME TO CLEAR `215 MONTHS · 18 YRS`; INTEREST PAID `$9,506`; punch `$9,506 INTEREST
  > $6,000 BORROWED`. Match the locked model (215 / 9,506 / 5,318).
- **s7 chevron — in-font, no fallback**: the `>` renders as the CSS `.gt` chevron
  (clean red right-pointing angle, em-sized to the h1, warn colour via currentColor).
  NO visible `~` and NO system-font `>`/`~` glyph anywhere. The absent-glyph fix from
  [[fin-build-en-1]] (Fix 1) is confirmed in pixels: s7 setup reads `around 22% APR`
  (not `~22%`), s7r2 reads `18 YRS` (not `~18 YRS`). The one surviving `~` is inside an
  HTML comment (unrendered) — not present in any frame.
- **s1 month-1 split — present & legible** (frame 00): YOU PAY `$170` → INTEREST `$110`
  (red-highlighted row) → OFF THE DEBT `$60`. Exact.
- **s7 minor**: the TIME-TO-CLEAR cell wraps to two lines (`215 MONTHS · 18` / `YRS`,
  and `TIME TO` / `CLEAR`) inside its 820px panel — legible, no clip, no safe-area
  overflow. Cosmetic only (same wrap the build snapshot-accepted); not a gate defect.

## US-cut / imagery checks (fin-assets-en pre-vetted; re-verified at full res)
- **Currency**: every figure is `$` — $170/$110/$60, $6,000, $5,318, $9,506, +$20,
  plus $1/$2/$100 bill imagery. **Zero `₹`**, zero foreign currency symbol.
- **Backgrounds on-keyword & market-neutral**: s1/s2/s3/s6/s8 US bills, s5/s7 calculator
  + notepad, s3-cut restaurant/shopping bags, s4/s4-cut diploma+books / people with
  generic teal reusable bags (no legible brand), s9 open US-Southwest highway. No
  deity / revered-figure face, no foreign-language on-screen text, no legible brand
  logo in imagery, no wrong-market scenery, no phone-screen content. (s5 foot text
  cites Chase / Capital One / CFPB Reg Z — intentional US-market citations in copy,
  not imagery brands.)
- **Contrast**: solid dark panels (#161b25) over darkened Ken-Burns bg; matches the
  build's 18/18 WCAG AA. No low-contrast text at any sampled frame.

## Master QA — DEFERRED to invocation 2 (post-encode)
`renders/FINAL-1080p-en.mp4` does not exist yet (expected — orchestrator owns the
chunked encode between invocations). On invocation 2 I will run, against the master:
faster-whisper re-transcribe vs the `data-start` VO grid (target max drift ≤0.1s),
peak dBTP (must be < −1 dBTP), blackdetect scan, and runtime vs timing.json total
**178.582s**. None of these are measurable pre-encode.

## Next
Orchestrator runs the encode:
`PRODUCER_ENABLE_CHUNKED_ENCODE=true npm run render -- -q high --resolution 1080p --video-bitrate 12M`
in its own background, then re-invoke fin-render (invocation 2) for master QA.
