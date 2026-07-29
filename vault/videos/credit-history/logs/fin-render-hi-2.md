---
summary: credit-history hi attempt 2, both invocations. INV 1 = gate ② frame check, PASS (s7 car-fob defect cleared, 9/9 frames). INV 2 = master QA of FINAL-1080p-hi.mp4, PASS — runtime 177.667 s video / 177.707 s container vs timing.json 177.642 (+0.025 / +0.065 s), max VO drift +0.0216 s (a constant 21.3 ms AAC priming offset, 2 ms spread across 9 clips), true peak −4.33 dBTP (3.33 dB under the −1 ceiling), zero black frames in 5330. All 9 VO lines present in the right slots. Deliverable.
updated: 2026-07-29
source: own ffprobe/ffmpeg astats+ebur128+loudnorm+silencedetect+blackdetect on renders/FINAL-1080p-hi.mp4 · faster-whisper small int8 (venv) single-pass + 9 isolated per-block passes · assets/voice/timing.json + h1-h9.mp3/.txt · index.html data-start table L346-354 · own snapshots snapshots/qa5{,z}/
---

# fin-render — credit-history · hi · attempt 2 · INVOCATION 1 (frame check only)

**Result: `STATUS: ok`. Gate ② cleared. No encode run** (the orchestrator owns it;
`renders/` still does not exist, which is correct at this point).

## Decision on `#s7q` — **(a) it passes**

Asked to choose explicitly. **(a).** Seeing the actual frame did **not** change my mind;
if anything it strengthened attempt 1's reasoning. Full argument below the numbers.

## The s7 fix — verified independently, not taken on report

| Check | Result |
|---|---|
| `s7cut` / `s7-cut` occurrences in `index.html` | **0** |
| same in `build.mjs` | **0** |
| s7 `.bg` at 139.05 | `s7.jpg` blueprint, full-bleed, `ken` running |
| vehicle object anywhere in scene | **none** — drafting lines, the "580" dimension, one pen at the top-right corner |
| root `data-duration` | **177.642** — 9 sections butt-joined, unchanged |

The payoff now reads over a blueprint under the words "SAME HOUSE." — subject and type
finally agree. **The attempt-1 defect is fully resolved.**

## Frame times — re-derived from source, not carried over

Re-read `S` (L363) and every entering cue (L421–573) after the edit. All nine last-cue
times are **unchanged**, because the only cues deleted belonged to `#s7cut`, which was
never the last entering cue (`pop #s7q` at S.s7+22.50 is, completing 138.807, pulse
139.007 → shot at **139.05**).

`16.80 · 28.80 · 51.46 · 72.25 · 92.95 · 112.68 · 139.05 · 156.95 · 175.40`

## Nothing regressed — pixel proof, not eyeballing

My fresh `qa5/` frames vs the exact PNGs I judged in attempt 1 (`qa/`, s2 from `qa2/`),
ffmpeg `psnr`, average over R/G/B:

| Scene | @ | PSNR vs attempt 1 | Read |
|---|---|---|---|
| s1 | 16.80 | **inf** | byte-identical |
| s2 | 28.80 | 99.54 dB | rasteriser noise |
| s3 | 51.46 | **inf** | byte-identical |
| s4 | 72.25 | 85.58 dB | rasteriser noise |
| s5 | 92.95 | **inf** | byte-identical |
| s6 | 112.68 | 72.21 dB | rasteriser noise |
| s7 | 139.05 | **19.22 dB** | the intended plate swap |
| s8 | 156.95 | 77.23 dB | rasteriser noise |
| s9 | 175.40 | 74.32 dB | rasteriser noise |

72 dB is an RMSE under 0.07 of one channel level. A single dropped or shifted element
would land in the 30–45 dB band, nowhere near this. **8/8 non-s7 frames are the frames I
already inspected at full resolution and passed** — re-confirmed visually on the contact
sheet (element counts all match attempt 1: s1 3 rows + stamp, s2 kicker + 4 chips + sub,
s3 mega + 2 gates + foot, s4 4 rows + foot, s5 grid + counter + foot + verdict, s6 2
lines, s8 stamp + 2 actions + foot, s9 4 chips + SUBSCRIBE).

fin-build reported 6 byte-identical / 2 noisy; I measure 3 byte-identical / 5 noisy. The
difference is immaterial — everything non-s7 is at or under the noise floor either way.

Build identity confirmed too: my `qa5` s7 vs fin-build's `qa4` s7 = **98.67 dB**, s2 =
**inf**. We are looking at the same generated `index.html`.

## `#s7q` contrast — my own measurement, own method

Windows cropped from **my** PNG, averaged with `crop → format=gbrp → scale=1:1:flags=area`
and read off `showinfo` plane means (gbrp order G,B,R). Every window is **clean plate at or
adjacent to the glyph rows** — no glyph pixels included, so these are true values, not
lower bounds. WCAG 2.x relative luminance; `--warn` #ef4444 computes to L = **0.2290**.

| Window (x,y,w,h in the 1920×1080 frame) | Backdrop RGB | L | Ratio vs #ef4444 |
|---|---|---|---|
| left of line 1 — 520,512,140,88 | 82,71,74 | 0.0679 | **2.37** (worst) |
| above line 1 — 520,486,520,22 | 80,66,70 | 0.0604 | **2.53** |
| right of line 1 — 1270,512,140,88 | 78,67,71 | 0.0609 | **2.52** |
| below line 2 — 520,684,890,22 | 70,58,63 | 0.0469 | **2.88** (best) |

**This confirms fin-build's correction and refutes my attempt-1 prediction.** My
right-of-line-1 window reproduces their worst-window 2.51 to two decimals with an
independently chosen method, so their measurement is sound: the blueprint is the
*brighter* plate, the car photo's crushed left two-thirds was accidentally doing contrast
work, and removing it cost ~0.15 of ratio. I was wrong in attempt 1 to predict a free
improvement; the correction is accepted.

For reference, the whole punch box including glyphs reads RGB **132,55,56** — red
dominates the box, which is the point.

### Why 2.37–2.88 is not a gate ② failure

1. **I looked at it at 1:1, not at a downscale.** `snapshots/qa5z/frame-00-at-139.05s.png`
   is a 3× device-scale crop of `#s7q`. The type is the most dominant object in the frame,
   cleanly separated, edges intact. The blueprint's linework is *thin and dark* — where a
   drafting line crosses a glyph it **raises** local edge contrast, it does not wash the
   type out. The plate is smooth mid-grey with no bright hotspot under any letter.
2. **Luma separation is real and is what survives encoding.** Y(#ef4444) ≈ 119,
   Y(plate 78,67,71) ≈ 71 — a **~48/255 (19%) luma delta**. The WCAG formula is harsh here
   because relative luminance weights green at 0.7152 and this red has almost none; the
   eye and the encoder both see the luma step. 4:2:0 chroma subsampling is the usual risk
   for red-on-grey, and it is not a risk at 88px/900 — the stems are far wider than the
   2×2 chroma grid, and the luma plane carries the edge at full resolution regardless.
3. **`text-shadow: 0 2px 22px rgba(0,0,0,.7), 0 1px 4px rgba(0,0,0,.55)`** on `.huge` is
   contrast the formula cannot sample. Visible in the 3× crop as a dark halo hugging every
   glyph.
4. **`hyperframes check` scores 22/22 AA** with its own backdrop sampler, on this build.
5. **Consistency.** I declined to gate this same element at **2.66** in attempt 1. 2.37–2.52
   is not a change in kind from 2.66 — the perceptual difference is invisible, and it would
   be incoherent to kill the run over 0.15 of a ratio I already ruled non-blocking.
6. Everything legal has been tried and correctly refused: `--warn` is a token and is the
   video's thesis colour; design §1 allows one per-scene `filter:` per video and s8 holds
   it; `s7.jpg` reads ~200/255 across a 9×5 tile map so no reframe helps.

**Owed, not blocking:** a darker s7 background is fin-assets' call for a future cut. It
would buy back ~0.5 of ratio on this one element. It is a polish item, not a defect, and it
does not justify a terminal gate on a legible frame.

## The rest of the gate ② checklist

- **Safe area 9/9.** s7's red elements span x 460→1459, y 329→671 against the 192→1728 /
  108→972 title-safe box. Other eight are pixel-identical to attempt 1's measured pass
  (widest: s3 mega 260→1665, s5 verdict 305→1620).
- **Brand marks: 0.** CIBIL / TransUnion CIBIL appear as set type naming the bureau, never
  as a logo or mark.
- **Phone screens: 0.**
- **Currency: ₹ throughout, lakh-grouped** — `₹30,00,000`, `₹1,390 to ₹1,860`,
  `₹3.3 to 4.5 lakh`. No `$`, no US framing. Correct for the India cut.
- **Wrong-subject imagery: 0** — this was the attempt-1 finding and it is cleared.
- Carried cosmetic note (not a finding, unchanged): s5's foot wraps with "history" alone on
  line 2.

## Not run this invocation

Encode, transcription drift, peak dBTP, blackdetect, runtime-vs-`timing.json` — all
invocation 2. Target runtime **177.642s**. `renders/FINAL-1080p-hi.mp4` does not exist yet;
if it still does not exist when I am called for QA I will fail with
`NEXT: orchestrator must run the render`.

## Sign-off

- [x] 9/9 last-cue frames re-shot at independently re-derived times and looked at
- [x] s7 fix verified at source (0 refs) and on the frame — no vehicle, blueprint carries the payoff
- [x] 8/8 other frames proven unchanged by PSNR (72 dB–inf), nothing regressed
- [x] `#s7q` re-measured on four clean windows; fin-build's correction independently confirmed
- [x] **Explicit call: (a) pass** — legible at 1:1, consistent with attempt 1's ruling
- [x] Safe area 9/9 · brand marks 0 · phone screens 0 · currency ₹ correct
- [ ] Encode (orchestrator's) → then invocation 2 QA

---

# INVOCATION 2 — master QA on `renders/FINAL-1080p-hi.mp4`

**Result: `STATUS: ok`. The cut is deliverable.** Every gate passes; two reported-only
observations at the bottom.

File as delivered by the orchestrator: **279,767,597 bytes**, encoded in 21m 38.5s with
`PRODUCER_ENABLE_CHUNKED_ENCODE=true npm run render -- -q high --resolution 1080p
--video-bitrate 12M`. The encoder emitted `credit-history-hi_2026-07-29_14-04-43.mp4`;
the orchestrator renamed it to the canonical `FINAL-1080p-hi.mp4`. `renders/` holds
nothing else.

## 1. Runtime vs `timing.json` — PASS

| Measure | Value |
|---|---|
| `timing.json` total | **177.642 s** |
| Video stream duration | **177.666667 s** (**+0.0247 s**, 0.74 frame) |
| Audio stream duration | 177.706667 s (+0.0647 s) |
| Container duration | 177.706667 s (+0.0647 s) |
| Frames | **5330** @ 30/1 fps CFR (`r_frame_rate` = `avg_frame_rate` = 30/1) |
| Frames expected | `ceil(177.642 × 30)` = `ceil(5329.26)` = **5330 — exact** |

Tolerance is 1.0 s; the worst reading uses **6.5 %** of it. The +0.065 s on the audio track
is AAC frame padding: 8330 AAC frames × 1024 = 8,529,920 samples = 177.70667 s at 48 kHz,
against 8,526,816 samples of nominal content — 3104 samples of tail pad. Nothing is
truncated at either end.

## 2. VO placement drift — PASS, max **+0.0216 s** (target ≤ 0.1 s)

### Method note — why the number below is not a whisper number

faster-whisper `small` int8 word timestamps **cannot resolve 0.1 s on this audio.** Run
per-block with `clip_timestamps=[start−0.30, end+0.30]`, six of nine blocks reported their
first word at *exactly* the window edge (−0.300 s): h1, h4, h5, h6, h7, h8. The onsets are
saturated against the clip boundary, not measured. The single-pass run was worse — it
merged h1+h2 into one 0.000→29.360 segment and truncated h2 at the model's 30 s window.

So whisper is reported below for **content**, which it is good at, and placement is measured
with `silencedetect=n=-45dB` run at the **same threshold on the source mp3 and on the
master**, which is exact to the sample. `drift = master_onset − (data-start + source_lead)`.

### Onsets

| Clip | `data-start` | Source lead-in | Expected onset | Master onset | **Drift** |
|---|---|---|---|---|---|
| h1 | 0.400 | 0.03365 | 0.43365 | 0.454979 | **+0.0213** |
| h2 | 18.962 | 0.08562 | 19.04762 | 19.0690 | **+0.0214** |
| h3 | 31.961 | 0.10045 | 32.06145 | 32.0828 | **+0.0213** |
| h4 | 53.553 | 0.06429 | 53.61729 | 53.6388 | **+0.0215** |
| h5 | 74.441 | 0.03361 | 74.47461 | 74.4959 | **+0.0213** |
| h6 | 95.380 | 0.05844 | 95.43844 | 95.4598 | **+0.0214** |
| h7 | 116.007 | 0.04041 | 116.04741 | 116.0670 | **+0.0196** |
| h8 | 141.831 | 0.04692 | 141.87792 | 141.8990 | **+0.0211** |
| h9 | 160.681 | 0.03240 | 160.71340 | 160.7350 | **+0.0216** |

**max +0.0216 s · min +0.0196 s · mean +0.0212 s · spread 0.0020 s.**

### Offsets — nothing truncated, nothing accumulating

Same method on each clip's trailing edge (source last-speech + `data-start` + 0.0213):

| Clip | Predicted tail | Master tail | Residual |
|---|---|---|---|
| h1 | 17.2231 | 17.2231 | 0.0000 |
| h2 | 30.3233 | 30.3234 | +0.0001 |
| h3 | 51.7663 | 51.7663 | 0.0000 |
| h4 | 72.6947 | 72.6947 | 0.0000 |
| h5 | 93.6010 | 93.6010 | 0.0000 |
| h6 | 114.2153 | 114.2150 | −0.0003 |
| h7 | 140.1296 | 140.1300 | +0.0004 |
| h8 | 158.9035 | 158.9040 | +0.0005 |
| h9 | 176.2745 | 176.2750 | +0.0005 |

**Worst residual 0.5 ms over 176 s. Zero accumulation.**

### What the 21.3 ms actually is

It is not render jitter. **1024 samples at 48 kHz = 21.333 ms** — exactly one AAC-LC
encoder-delay (priming) frame. The mux carries `start_pts=0` with no edit list, so the
priming is never trimmed and the whole audio track sits one AAC frame late against video,
uniformly. Evidence it is the constant and not this render: it lands within 2 ms on all
nine clips, and `pay-yourself-first` logged **0.021 s** on both its en and hi cuts by an
independent cross-correlation method. 21 ms of audio-late is far inside ITU-R BT.1359
(−125 ms … +45 ms imperceptible). Reported, not a defect.

### Content — all 9 lines present, right slot, right order

Single pass: 41 segments, 393 words, 0 words outside the nine VO windows. Then nine
isolated per-block passes, each diffed against its `h*.txt`. Every block matches its source
line; `h2` ("चार बातें — ये रिपोर्ट है क्या…") is fully present in the master and its absence
from the single-pass run was purely the 30 s window artifact described above. No dropped,
duplicated, reordered or swapped line. (A normalised-similarity score was computed and
**discarded as unusable** — stripping virama to compare Devanagari destroys conjuncts, and
`small` misspells Haryanvi-accented Hindi heavily while getting the words right. The
side-by-side read is the check that counts.)

## 3. Peak level — PASS, **−4.33 dBTP** (ceiling −1 dBTP, **3.33 dB** of headroom)

Three independent reads agree:

| Reader | Value |
|---|---|
| `astats` sample peak | **−4.327057 dBFS** (ch 1 and ch 2 identical to 6 dp → dual mono) |
| `ebur128` true peak | **−4.3 dBFS** |
| `loudnorm` `input_tp` (4× oversampled) | **−4.33 dBTP** |

True peak == sample peak → **no inter-sample overshoot**. RMS −25.2499 dB (both channels);
flat factor 0.000000; peak count 2.

## 4. Black-segment scan — PASS, **zero**

| Pass | Result |
|---|---|
| `blackdetect=d=0.05:pix_th=0.10` | **0 detections** |
| `blackframe=amount=95:threshold=32` | **0 detections** |
| `blackdetect=d=0.033:pix_th=0.15` (single-frame sensitivity) | **0 detections** |

`5330/5330` frames decoded on both passes (`frame= 5330 … Lsize=N/A time=00:02:57.63`).
At 30 fps `d=0.033` catches a one-frame flash; there is not one. Sustained 12,412 kb/s
video bitrate also rules out any frozen or blank stretch.

## 5. Master vs the composition I gated in invocation 1

Not required by the contract — run because I am the last gate before publish and wanted
end-to-end proof that the shipped bytes are the composition I passed, not just that the
composition was good.

Four frames pulled from the MP4 and PSNR'd against my `snapshots/qa5/` gate-② PNGs:
**35.46 / 23.34 / 27.56 / 34.96 dB** @ 16.80 / 92.95 / 139.05 / 175.40.

The low readings are **animation phase, not content mismatch** — established, not assumed.
A PSNR sweep around 92.95 gives 32.56 / 32.62 / 32.64 dB at 92.783–92.917 then a one-frame
cliff to 23.34 at 92.950, which is precisely the s5 last-cue boundary. Looking at the actual
frames at 92.85 and 93.10: **identical content**, with `ONE MISS = 36 MONTHS` still growing
through its pop (span ≈ 305→1620 px vs 270→1650 px). A 100 px-tall headline moving 35 px is
an enormous pixel diff and a zero-content diff.

Confirmed by eye **in the encoded master**:

- **@139.60 — the attempt-1 defect is fixed in the shipped file**, not merely in the
  composition: blueprint plate, **no vehicle anywhere**, `EXTRA INTEREST  ₹3.3 to 4.5 lakh`,
  payoff `SAME HOUSE. DIFFERENT NUMBER.` Subject and type agree; red-on-grey is clean
  through 4:2:0.
- **@92.85 / 93.10 — s5** grid of 36 cells with exactly one red, `MONTH 36 OF 36`, CIBIL
  foot, verdict. Matches the element list I recorded in invocation 1.
- **@175.40 — end card** 4 chips + SUBSCRIBE intact.
- Currency **₹**, lakh-grouped, survives the encode. No `$`, no brand logos, no phone screens.

## 6. Reported, not gates

1. **Integrated loudness −22.17 LUFS** (loudnorm) / −22.1 LUFS (ebur128); LRA 3.30 LU
   (ebur128 3.0 LU, low −24.6, high −21.6); threshold −32.84. That is ~8.2 LU under
   YouTube's −14 LUFS reference, and YouTube applies **no positive gain**, so this ships
   quieter than the feed average. It is broadcast-correct (EBU R128 is −23) and it is **not**
   the gate — the gate is peak < −1 dBTP, which passes with 3.33 dB spare. It also matches
   every prior cut in this pipeline (`good-debt-vs-bad-debt` hi −22.02 / en −21.09;
   `pay-yourself-first` hi −22.24 / en −21.13), so it is a pipeline constant, not a
   regression on this render. Optional pre-publish lift to ~−14 LUFS via `loudnorm
   I=-14:TP=-1` — the headroom allows it; a flat +8 dB gain would not.
2. **Carried from invocation 1, unchanged:** s5's foot wraps with "history" alone on line 2
   (cosmetic); a darker s7 plate would buy back ~0.5 of contrast ratio on `#s7q` — fin-assets'
   call for a future cut, not a defect here.

## Stream sheet

`h264 High L5.0 · yuv420p · tv range · bt709/bt709/bt709 · progressive · 1920×1080 SAR 1:1 ·
30 fps CFR · 12,412 kb/s` + `aac LC · 48 kHz · stereo · 178 kb/s` · overall 12,594 kb/s.

## Sign-off

- [x] Runtime 177.667 s video / 177.707 s container vs 177.642 s → +0.025 / +0.065 s, 5330 frames exact
- [x] Max VO drift **+0.0216 s** ≤ 0.1 s; 2 ms spread across 9 clips; 0.5 ms tail residual; no accumulation
- [x] All 9 VO lines re-transcribed, present, correct slot and order
- [x] True peak **−4.33 dBTP** < −1 dBTP (3.33 dB headroom); no inter-sample overshoot
- [x] Black segments **0** at three sensitivities, 5330/5330 frames scanned
- [x] Encoded master proven to be the gate-② composition (4 frames + 3 visual confirmations)
- [x] **MASTER QA: PASS — deliverable**
