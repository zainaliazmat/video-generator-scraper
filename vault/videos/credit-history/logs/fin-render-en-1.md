---
summary: Gate ② frame check for credit-history en — 17 real frames inspected (9 per-scene last-cue + 8 targeted risk). PASS, no build fix required. fin-build's #s5mark invariant verified on real frames; s4's German weekday names are gone; the standing FICO/APR ban holds on the densest s7 frames. One log correction: #s5ctr does NOT cover the s5 QUALITY seal — the grade and the bottom-edge crop do.
updated: 2026-07-29
source: snapshots/gate2a · gate2b · gate2c · gate2z1-z4 in studio/videos/credit-history-en/ · index.html timeline (cue times) · assets/voice/timing.json · logs/fin-build-en-1.md
---

# fin-render — credit-history · en · attempt 1 · INVOCATION 1 (frame check)

**Result: PASS.** No finding rises to `fin-build must fix`. Encode is cleared to run.
The QA pass (transcript drift, peak dBTP, blackdetect, runtime) is invocation 2 and
appends to this file after the orchestrator's render.

## What was captured

Frame times are each scene's **last cue**, taken far enough past the cue that the
easing has landed (so the frame shows the scene at maximum element count):

| Scene | last cue | frame @ | file |
|---|---|---|---|
| s1 | `breathe #s1stamp` +14.90 → 14.90 | **15.60** | `gate2a/frame-00-at-15.6s.png` |
| s2 | `breathe #s2sub` +9.20 → 25.307 | **25.90** | `gate2a/frame-01-at-25.9s.png` |
| s3 | `pulse #s3g1` +20.40 → 47.233 | **47.80** | `gate2a/frame-02-at-47.8s.png` |
| s4 | `breathe #s4q` +16.60 → 64.895 | **65.40** | `gate2a/frame-03-at-65.4s.png` |
| s5 | `breathe #s5fix2` +16.90 → 82.895 | **83.40** | `gate2a/frame-04-at-83.4s.png` |
| s6 | `breathe #s6u2` +18.80 → 103.593 | **104.10** | `gate2a/frame-05-at-104.1s.png` |
| s7 | `breathe #s7q` +27.30 → 132.196 | **132.60** | `gate2a/frame-06-at-132.6s.png` |
| s8 | `pulse #s8f` +18.40 → 151.446 | **152.00** | `gate2a/frame-07-at-152s.png` |
| s9 | `breathe #s9cta` +18.30 → 171.92 | **172.50** | `gate2a/frame-08-at-172.5s.png` |

Plus **8 targeted risk frames** — `gate2b`: 57.00 (s4 mid), 70.60 / 72.90 / 76.00 /
81.00 (the s5 mark-vs-fill sequence), 95.79 (s6 cut-in peak), 128.40 (s7 max density),
147.60 (s8 cut-in peak); `gate2c`: 66.40 (s5 open, seal most in-frame), 129.20 (s7 APR
bands + Experian attribution co-present). Four `--zoom` crops at 3-4x device scale:
`gate2z1` (s5 seal @76s), `gate2z2` (s5 track left end @76s + @81s), `gate2z3` (s5 seal
@66.4/69/72.9), `gate2z4` (s6 muted sub over the note stack @100.5/104.1).

First `gate2a` run warned `Runtime did not become render-ready within 5000ms`. **Re-run
at `--timeout 25000`** — clean, and every frame reported here is from the clean run.
A gate-two decision must not be taken off a possibly-stale frame.

## 1 · `#s5mark` stays lit past the fill — VERIFIED (fin-build's specific ask)

Traced on four real frames, not on the timeline source:

| t | s5 offset | What the frame shows |
|---|---|---|
| 70.60 | +4.60 | Red mark slammed at **year zero**, left edge of the empty dark track. Fill sweep just starting, no amber yet. |
| 76.00 | +10.00 | Fill amber through ~year 4. **Mark still lit, rendered ON TOP of the amber.** Counter reads `YEAR 3 OF 7`. |
| 81.00 | +15.00 | Fill amber to **YEAR 7**. Mark still lit on top — zoomed 3x (`gate2z2/frame-01`), unmistakable red block inside its dark bezel against solid amber. |
| 83.40 | +17.40 | Mark **cleared** (exit +15.50), fill full, `YEAR 7 OF 7`. |

The z-order holds in practice: `#s5fill` (no z-index, DOM-earlier) under `#s5mark`
(`z-index: 2`). The invariant fin-build wrote — *slams at year zero, sits above the
fill, clears only as the fill crosses YEAR 7* — is true on rendered pixels.

## 2 · s4 German weekday names — GONE

Checked at **57.00** and at **65.40**. 65.40 is the worst case by construction: s4's
`ken` is `zoomIn=false`, so scale runs 1.16 → 1.00 and the **end** of the scene shows
the most image. Both frames show ruled cells and the hour-column numerals (9 / 10 / 11
/ 12 / 13) and **no word in any language**. `background-size: 175%;
background-position: 100% 100%` does what the build log claimed.

## 3 · s5 `QUALITY` seal — ships, but the build log's reason is wrong

**Correction for the record.** `fin-build-en-1.md` states *"the `.counter`'s opaque
panel bed covers the area anyway."* On real frames it does not:

- `#s5ctr`'s panel occupies roughly **y 445–580**.
- The seal renders at roughly **(1162, 995)** at ken scale 1.0, drifting to
  **(1182, 1034)** by +10.0s and to ~y 1068 by scene end as `ken` zooms in.
- That is a **~420px gap**. The counter never overlaps the seal at any point in s5.

What actually carries it is the grade plus the crop: at `grayscale(.32)
brightness(.62) contrast(1.05)` under the red scrim, sitting at the very bottom edge
and partly cut off, the seal reads at 1:1 as a **dark disc with no readable text**.
The word only resolves at **4x device-scale zoom** (`gate2z3/frame-00-at-66.4s.png`,
where "…LITY" arcs into view). It is a **generic** seal — no company name, no brand
mark — so it does not trip the brand-mark check either.

**Verdict: ship.** But the mitigation on file should read *"illegible under the grade at
the bottom edge"*, not *"covered by the counter"* — the false reason would let a future
cut move the counter and think the seal was still handled.

## 4 · STANDING BAN (FICO band number next to Experian APRs) — HELD

Checked on the two frames where s7 carries the most numbers at once:

- **128.40** — `TOP CREDIT TIER  ABOUT 6% → $418/mo` · `SUBPRIME  ABOUT 19% → $590/mo` ·
  `EXTRA EVERY MONTH  $172` · `EXTRA INTEREST  $12,400`.
- **129.20** — all of the above **plus** `#s7f` `Experian tier averages — illustrative
  band, not a quoted rate · payments are model output`. This is the tightest test: the
  attribution and the APRs are deliberately co-present here (+23.60 fade-in vs +24.90
  band exit, a ~1.3s overlap), and it is the single densest numeric frame in the cut.

Both bands are named **in words only**. No `670`, no `781`, no numeral from the
300–850 scale anywhere on s7. `#s3g1`'s `670+` renders at **47.80** — **81s** before
s7's first band appears at 113.99. Never co-present.

## 5 · s7 subject — the hi-cut defect does NOT repeat

The hi cut failed gate two on a car remote fob sitting under a **home-loan** punch.
Here the frame at **132.60** shows a car key — a fob head with two remote buttons and a
**metal flip blade extended at bottom-right** — under `SAME CAR. DIFFERENT NUMBER.`,
with the setup rows reading `$25,000 used car · 72 months`. **The subject matches the
line.** fin-assets' report is accurate: the blade is genuinely there, though the fob
body is what dominates the frame. No mismatch to fix.

## 6 · Standing frame checks, all 17 frames

| Check | Result |
|---|---|
| **Safe area** | Every `.stack` inside the 192–1728 title-safe box. Widest elements measured: s3's `300`/`850` mega pair spans ~258→1680; s7's `#s7f` foot spans ~285→1635. Both clear. |
| **Contrast** | Every text/photo pairing readable. Weakest is s6's `#s6u` — the green `SMALL` over the olive note band; zoomed 3x at 100.50 (`gate2z4/frame-00`) it reads cleanly, the green is far brighter and more saturated than the bed. Not a defect. |
| **Brand marks** | None legible. s3's gauge dials carry an illegible maker mark and °C scale numerals — decorative texture, reads as instrumentation, not as a brand. s8's pen and s6's pen carry no mark. |
| **Currency** | `$` throughout — `$25,000`, `$418/mo`, `$590/mo`, `$172`, `$12,400`. **No `₹` anywhere**, no Indian imagery. US market clean. |
| **Phone screens** | None in any scene. |
| **Ghosted cut-ins** | s6 @95.79 (0.45) — clock face reads as a due-date cut-in, its red second hand is a dull dark hairline entering from the right, does not read as `--warn`. s8 @147.60 (0.55) — red pen and pen marks read, the lantern still beds the type. Both fixes hold. |

## Observation — not a fail, not mine to fix

s9's chip **`READ BEFORE YOU ARE`** reads as a dangling fragment standing alone on
screen at 172.50. It is the **approved upstream copy** — `storyboard-en.md` line 441
and `script-en.md` line 284 — anchored to the VO one beat earlier: *"The lender reads
your report before it reads you."* The wordplay is carried by the narration. Recording
it so a future cut can decide deliberately rather than inherit it by accident; it is a
script/storyboard call, not a build defect, and it does not gate the encode.

## Sign-off — invocation 1

- [x] One frame per scene at that scene's last cue, captured render-ready and **looked at**
- [x] 8 targeted risk frames + 4 zoom crops for the three named caveats
- [x] `#s5mark` lit past the fill — verified on 4 real frames, incl. a 3x zoom
- [x] s4 German weekday names absent at the widest ken point
- [x] s5 `QUALITY` seal illegible at 1:1 — **coverage claim corrected**, outcome unchanged
- [x] STANDING BAN held on the two densest s7 frames
- [x] s7 subject matches its line — hi-cut defect does not repeat
- [x] Safe area / contrast / brand marks / currency / phone screens clean on all 17
- [ ] Encode — **orchestrator's**, not run here
- [ ] QA the master (drift · peak dBTP · blackdetect · runtime) — invocation 2
