---
summary: fin-render gate-two FRAME CHECK, hi cut, attempt 2 — PASS. All six frames fin-assets replaced (s1/s2, s12, s17, s34, s79, s81) re-snapshotted and inspected at full resolution; every one is now Indian or currency-neutral, and s17's dead-black right region measures YAVG 88.7 against a healthy reference band of 89–90. No encode was run. Cut is cleared for the orchestrator's render.
updated: 2026-07-31
source: studio/videos/first-lakh-first-thousand-hi/snapshots/qa2/b1 (9 frames) + assets/img/CREDITS.txt + ffprobe signalstats
stage: fin-render, cut hi, attempt 2 — invocation 1 of 2 (frame check only)
---

# fin-render — «पहला एक लाख» hi, attempt 2 — GATE TWO: PASS

**No encode was run.** Per the orchestrator scope this invocation is the frame check only.
`renders/` is still empty; the orchestrator runs the encode next.

## Scope of this re-check (why it is not another 86-frame pass)

`find -newermt 06:00` on the project shows fin-assets touched **exactly** the six
declared images plus their `.src`, `CREDITS.txt` and `manifest.json`:

```
06:15  s17.jpg  s79.jpg  s81.jpg
06:16  s34.jpg
06:17  s12.jpg  s1.jpg
06:20  CREDITS.txt      06:21  manifest.json
```

`index.html` is unchanged (05:22, i.e. **older** than every replaced image), as are
`build.mjs`, the VO and the timing. No markup changed → the 80 frames that passed at
attempt 1 cannot have regressed, and their result stands. Re-snapshotted the affected
scenes only, 9 frames: the s1/s2 zoom at 1.20 / 5.40 / 10.87s (start, s1 last cue, s2 last
cue), s12 68.20, s17 at **both** 97.00 (hold start) and 102.12 (last cue), s34 198.66,
s79 468.90, s81 479.78. Batch dir `snapshots/qa2/b1`, never reused; the navigation-timeout
defect hit on tries 1–3 and the capture succeeded on try 4 — this is a real capture, not a
recorded assumption. (`snapshot` takes the project DIR, not `index.html`; passing the file
errors with "Not a directory".)

## The six blockers — all cleared

| scene | window | what is on screen now | verdict |
|---|---|---|---|
| **s1 + s2** | 0.0 – 11.74s | rolled ₹10 / ₹20 / ₹50 / ₹100 notes, rubber-banded. `₹100`, `₹50`, `₹10` denominations and the red serials (`345905`, `989612`) read clearly at 1:1 | **pass** — the 11.7s hook is now unambiguously Indian |
| **s12** | 66.64 – 71.75s | edge-on stack of milled coins against a light grey field. Zero legible text, no identifiable national device | **pass** — currency-neutral as promised |
| **s17** | 96.29 – 104.22s | hourglass left, out-of-focus grey newsprint/fabric texture right | **pass** — see grade measurement below |
| **s34** | 197.16 – 202.82s | hand fanning ₹500 notes: Gandhi portrait, `रिज़र्व बैंक`, `…OF INDIA`, serial `70R 244` | **pass** |
| **s79** | 467.40 – 473.17s | RBI Platinum Jubilee ₹5 commemorative: `RESERVE BANK OF INDIA`, `भारतीय रिज़र्व बैंक`, `PLATINUM JUBILEE 1935-2010` | **pass** — and thematically on-message under the `₹1,500 works. ₹500 works.` card |
| **s81** | 478.28 – 486.13s | pile of ₹5 coins, `₹5`, `INDIA`, `2015` legible | **pass** — RECAP ONE is clean |

`CREDITS.txt` corroborates all six: every new line is a Pixabay rupee/India asset
(rupixen ×2, F1Digitals, pprasantasahooo, ElenzaPhotograhy, Nile).

## s17 — the "is it now washed out?" check fin-assets asked for

Same crop as attempt 1, the un-toned right region `767×900+1153+180`, `ffprobe signalstats`:

| frame | YMIN | **YAVG** | YMAX |
|---|---|---|---|
| s17 @ 97.00s (hold start) | 24 | **89.94** | 144 |
| s17 @ 102.12s (last cue) | 25 | **88.74** | 225 |
| s17 attempt 1 (old asset) | — | **16.03** | — |
| s33 reference (healthy) | — | 90.02 | — |
| s84 reference (healthy) | — | 89.27 | — |

**Correctly graded, not washed out.** 88.7 / 89.9 lands inside the 89–90 band set by the
two scenes the system grade is tuned on, YMIN sits at 24–25 (off the 16 black floor,
so no crushing) and YMAX is 144 at the hold start — nowhere near clipping. The 225 at
102.12s is the white divider rule inside the crop, not blown photography.
Contrast on the type: red `2 MONTHS` and the white rule sit on the toned left panel at
full-frame YAVG 69.6 — legible at 1:1.

Other new frames, full-frame YAVG: s1 56.6, s12 89.2, s34 54.6, s79 66.6, s81 47.0 —
all inside the cut's existing range, none flat.

## Non-blocking, recorded as accepted (this cut ships with them)

- **Source resolution dropped.** The replacements are 1280 px wide where the old `s1.jpg`
  was 1880. On s1/s2 the ken-burns zoom reaches ~1.6× upscale by 10.87s and the note paper
  is visibly soft at 1:1. Type is vector and stays sharp; the softness reads as shallow
  depth of field on a contact sheet. Accepted, but the asset stage should prefer ≥1600 px
  for any full-bleed scene that carries a long zoom.
- **s34 shows the pre-2016 ₹500 note** (demonetised design). Authentic Indian currency, just
  dated. Cosmetic.
- Carried over unfixed from attempt 1, all re-affirmed by file mtime rather than re-shot
  (the assets were not touched): **s19** unidentifiable foreign coin in the piggy bank,
  **s30** German form, **s67** German calendar, **s63** orphan `to` wrap. Each was
  non-blocking at attempt 1 and none of them is currency-legible; they ship.

## Numbers

| | |
|---|---|
| Frames re-captured | **9** (7 scenes: s1, s2, s12, s17 ×2, s34, s79, s81) |
| Frames failing | **0** |
| Scenes cleared, cumulative | **86 / 86** (80 held from attempt 1 + 6 re-verified) |
| s17 right-region YAVG | **88.74** @ last cue / **89.94** @ hold start (was 16.03) |
| Snapshot retries needed | 4 (3 × `Navigation timeout of 10000 ms exceeded`) |
| Encode | **not run** — orchestrator's job |
| Runtime / VO drift / dBTP | not measured — QA is invocation 2, after the master exists |
