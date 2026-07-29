---
summary: credit-history en — INVOCATION 2, master QA of FINAL-1080p-en.mp4. PASS. Runtime 173.233 s video / 173.248 s container vs timing.json 173.227 (+0.006 / +0.021 s), 5197 frames exact. Max VO drift +0.0218 s — the same one-AAC-frame priming constant as hi, 0.9 ms spread over 9 clips. True peak -3.00 dBTP (2.00 dB headroom), traced to en1.mp3's own -2.99 dBFS source peak, not a render-chain limiter. Zero black frames in 5197 at three sensitivities. All 9 VO lines present, right slot, right order. Deliverable.
updated: 2026-07-29
source: own ffprobe/ffmpeg astats+ebur128+loudnorm+silencedetect+blackdetect+blackframe+psnr on renders/FINAL-1080p-en.mp4 · faster-whisper small int8 (venv) single pass, word timestamps · assets/voice/timing.json + en1-en9.mp3/.txt · index.html data-start table L390-398 · own snapshots/qa-master/ vs gate2a/gate2c
---

# fin-render — credit-history · en · INVOCATION 2 (master QA)

**Result: `STATUS: ok`. The cut is deliverable.**

**Filename note, so nobody misreads it later:** this is the QA half of the *same*
attempt whose gate-② frame check is in `fin-render-en-1.md`. The en cut did **not**
fail and get re-run — it passed gate ② first time. The `-2` follows the contract's
`fin-render-<cut>-<attempt>.md` naming with the attempt counter the orchestrator
passed in; it is not a second attempt after a failure (unlike `fin-render-hi-2.md`,
which genuinely was one).

Gate ② was cleared in invocation 1 and is **not** re-run here.

File as delivered by the orchestrator: **258,766,680 bytes** (246.8 MB), encoded in
16m 47.9s with `PRODUCER_ENABLE_CHUNKED_ENCODE=true npm run render -- -q high
--resolution 1080p --video-bitrate 12M`. The encoder emitted
`credit-history-en_2026-07-29_15-53-41.mp4`; the orchestrator renamed it to the
canonical `FINAL-1080p-en.mp4`. `renders/` holds nothing else.

## 1 · Runtime vs `timing.json` — PASS

| Measure | Value | vs 173.227 |
|---|---|---|
| `timing.json` total | **173.227 s** | — |
| Video stream duration | **173.233333 s** | **+0.006333 s** (0.19 frame) |
| Audio stream duration | 173.248000 s | +0.021000 s |
| Container duration | **173.248000 s** | **+0.021000 s** |
| Frames | **5197** @ 30/1 fps CFR (`r_frame_rate` = `avg_frame_rate` = 30/1) | — |
| Frames expected | `ceil(173.227 × 30)` = `ceil(5196.81)` = **5197 — exact** | — |

Tolerance is 1.0 s; the worst reading uses **2.1 %** of it.

The +0.021 s on the audio track is AAC frame padding: **8121 AAC frames × 1024 =
8,315,904 samples = 173.248 s @ 48 kHz**, against 173.227 × 48000 = 8,314,896 samples
of nominal content — **1008 samples of tail pad**. `astats` independently counts
8,315,904 samples. Nothing truncated at either end (see §2 tail residuals and the
digital-silence tail below).

## 2 · VO placement drift — PASS, max **+0.0218 s** (target ≤ 0.1 s)

### Method

Carried from the hi cut and re-confirmed sound here: faster-whisper word timestamps
cannot resolve 0.1 s on this audio, so **whisper is used for content only** (§5) and
**placement is measured with `silencedetect=n=-45dB` at the same threshold on the
source mp3 and on the master**, which is exact to the sample.
`drift = master_onset − (data-start + source_lead-in)`.

Source lead-ins were taken at `d=0.0005` so sub-10 ms lead-ins register — this
mattered: **en3 and en9 have zero lead-in** (their first `silencedetect` event is a
`silence_start` mid-clip, i.e. audio is above threshold from t=0), and **en4 (9.4 ms)
and en8 (3.2 ms)** would have read as zero at the `d=0.01` used on the hi cut.

Verified the source timestamps are 0-based and not offset by the mp3 container's
`start: 0.025057`: en1 reports `silence_start: 0`, not `0.025`. Had that been wrong,
every drift below would be off by −25 ms and would not land on the AAC constant.

### Onsets

| Clip | `data-start` | Source lead-in | Expected onset | Master onset | **Drift** |
|---|---|---|---|---|---|
| en1 | 0.400 | 0.104218 | 0.504218 | 0.525562 | **+0.02134** |
| en2 | 16.507 | 0.028390 | 16.535390 | 16.5567 | **+0.02131** |
| en3 | 27.233 | 0.000000 | 27.233000 | 27.2544 | **+0.02140** |
| en4 | 48.695 | 0.009433 | 48.704433 | 48.7257 | **+0.02127** |
| en5 | 66.395 | 0.053515 | 66.448515 | 66.4698 | **+0.02129** |
| en6 | 85.193 | 0.090952 | 85.283952 | 85.3053 | **+0.02135** |
| en7 | 105.296 | 0.029229 | 105.325229 | 105.347 | **+0.02177** |
| en8 | 133.446 | 0.003152 | 133.449152 | 133.47 | **+0.02085** |
| en9 | 154.020 | 0.000000 | 154.020000 | 154.041 | **+0.02100** |

**max +0.0218 s (en7) · min +0.0208 s (en8) · mean +0.02129 s · spread 0.00092 s.**

Precision caveat, stated rather than hidden: ffmpeg prints `silencedetect` times at
6 significant figures, so the en7 (`105.347`) and en8 (`133.47`) master onsets carry
±0.0005 s of display rounding. Even at the worst end of that the max is +0.0223 s —
**4.5 × inside** the 0.1 s target either way.

### What the ~21.3 ms is — same constant as hi, not a new defect

**1024 samples at 48 kHz = 21.3333 ms**, exactly one AAC-LC encoder-delay (priming)
frame. The measured mean is **21.29 ms — 0.04 ms off that value**. The mux carries
`start_pts=0` on both streams with no edit list (confirmed: audio packet 0 is
`pts=0 dts=0 duration=1024`), so the priming is never trimmed and the whole audio
track sits one AAC frame late against video, uniformly.

Evidence it is the pipeline constant and not this render: 0.9 ms of spread across
nine clips; `credit-history` hi logged **+0.0216 s** and `pay-yourself-first` logged
**0.021 s** on both cuts by an independent cross-correlation method. 21 ms of
audio-late is far inside ITU-R BT.1359 (−125 ms … +45 ms imperceptible).
**Reported, not a defect. Same in kind as hi — no flag.**

### Offsets — nothing truncated, nothing accumulating

Each clip's last transition into silence in the source, plus `data-start`, plus the
single mean offset 0.02129, against the master's matching `silence_start`:

| Clip | Predicted tail | Master tail | Residual |
|---|---|---|---|
| en1 | 14.80339 | 14.8034 | +0.00001 |
| en2 | 25.47555 | 25.4756 | +0.00005 |
| en3 | 46.91959 | 46.9197 | +0.00011 |
| en4 | 64.64789 | 64.6479 | +0.00001 |
| en5 | 83.49109 | 83.4911 | +0.00001 |
| en6 | 103.87279 | 103.873 | +0.00021 |
| en7 | 131.67809 | 131.678 | −0.00009 |
| en8 | 152.27049 | 152.271 | +0.00051 |
| en9 | 171.87049 | 171.870 | −0.00049 |

**Worst residual 0.5 ms over 172 s, using one constant offset for all nine. Zero
accumulation.** The tail residuals are the strongest proof of this — a drifting
clock would fan out; these do not.

### Tail is clean

Master audio from **172.25 s to EOF 173.248 s reads `Peak level: -inf`** — a full
second of digital silence after en9's nominal end at 172.227 s. Nothing clipped off
the end.

One thing I chased and cleared rather than assumed: en1 and en9's source
`silencedetect` runs emit a trailing `silence_end` (14.675 / 18.158) that the master
does not reproduce, which at first looked like a lost breath tail. Measured directly:
**source en9 @17.95–18.21 peaks at −52.19 dB, master at the same region −52.35 dB**
— both ~7 dB *below* the −45 dB analysis threshold. Those are EOF markers, not speech
onsets; the 0.16 dB delta is AAC round-trip noise on a signal 52 dB down. No content
lost.

## 3 · Peak level — PASS, **−3.00 dBTP** (ceiling −1 dBTP, **2.00 dB** headroom)

Three independent reads agree to two decimals:

| Reader | Value |
|---|---|
| `astats` sample peak | **−3.001530 dBFS** (Overall; ch1/ch2 RMS agree to 0.00002 dB → dual mono) |
| `ebur128` true peak | **−3.0 dBFS** |
| `loudnorm` `input_tp` (4× oversampled) | **−3.00 dBTP** |

True peak == sample peak → **no inter-sample overshoot**. RMS **−24.7503 dB**;
RMS peak −14.6694 dB; crest factor 12.23; **flat factor 0.000000** (no clipped runs);
peak count 2; abs peak count 1.

### Where the suspiciously round −3.00 comes from — traced, not assumed

It is **not** a limiter in the render chain. Source clip peaks:

| en1 | en2 | en3 | en4 | en5 | en6 | en7 | en8 | en9 |
|---|---|---|---|---|---|---|---|---|
| **−2.9907** | −5.3896 | −4.5748 | −3.6721 | −4.4880 | −4.8558 | −4.4300 | −4.9219 | −4.0947 |

**en1.mp3 already peaks at −2.9907 dBFS.** The master's −3.0015 is en1 through the
AAC round-trip (−0.011 dB). The ceiling is ElevenLabs' own output level on the
loudest clip, inherited untouched — which is the correct behaviour for a pipeline
that does no gain staging.

**Reported, not a gate:** this cut runs **1.33 dB hotter than hi** (−3.00 vs −4.33)
purely because en1 came back hotter from the TTS. 2.00 dB of headroom still passes
comfortably, but it is the thinnest margin logged in this pipeline so far. If a future
cut's TTS returns a clip nearer 0 dBFS the gate could actually bite — worth a
`loudnorm I=-14:TP=-1` pre-publish pass becoming standard rather than optional.

## 4 · Black-segment scan — PASS, **zero**

| Pass | Result |
|---|---|
| `blackdetect=d=0.05:pix_th=0.10` | **0 detections** |
| `blackframe=amount=95:threshold=32` | **0 detections** |
| `blackdetect=d=0.033:pix_th=0.15` (single-frame sensitivity) | **0 detections** |

`frame= 5197` decoded on the full video passes — **5197/5197**, the complete file, so
the zeros are a real scan and not an early exit. At 30 fps `d=0.033` catches a
one-frame flash; there is not one. Sustained **11,765 kb/s** video bitrate also rules
out any frozen or blank stretch.

## 5 · Content — all 9 lines present, right slot, right order

faster-whisper `small` int8, single pass, `language=en`, `beam_size=5`,
`word_timestamps=True`, `vad_filter=False`, `condition_on_previous_text=False`.

**31 segments · 447 words · 0 words outside the nine VO windows.**

| Clip | ASR/src words | Similarity | Nature of every difference |
|---|---|---|---|
| en1 | 52/52 | **1.000** | — |
| en2 | 28/28 | **1.000** | — |
| en3 | 46/51 | 0.887 | numerals only: "three hundred to eight hundred fifty" → `300 to 850`; "six hundred seventy" → `670` |
| en4 | 47/52 | 0.889 | numerals only: "thirty-five percent / thirty percent / sixty-five percent" → `35% / 30% / 65%` |
| en5 | 54/54 | 0.981 | numerals only: "ten" → `10` |
| en6 | 53/54 | 0.972 | orthography only: "auto-pay" → `autopay` |
| en7 | 63/72 | 0.830 | numerals only: "twenty-five-thousand-dollar" → `$25,000`; "six percent" → `6%`; "nineteen" → `19`; "a hundred seventy dollars" → `$170`; "twelve thousand four hundred dollars" → `$12,400` |
| en8 | 61/61 | **1.000** | — |
| en9 | 54/54 | **1.000** | — |

**Every sub-1.000 score is ASR numeral formatting, nothing else.** The source `.txt`
spells numbers out because that is what the TTS needs; whisper writes digits. Word
order and semantics are identical in all nine. **Zero dropped, duplicated, reordered
or swapped words.** The similarity column is diagnostic only — the side-by-side read
is the check that counts, and it is clean.

Also worth recording: the VO speaks `300`, `850` and `670`. That does **not** touch
the standing FICO-band ban, which is about the on-screen numeral appearing beside
Experian APRs — see §6.

## 6 · Master vs the composition gated in invocation 1

Not required by the contract; run because this is the last gate before publish and
the useful proof is that the *shipped bytes* are what passed, not just that the
composition was good.

Six frames pulled from the MP4 and PSNR'd (RGB average) against the invocation-1
gate-② PNGs:

| @ | 15.60 | 47.80 | 83.40 | 129.20 | 132.60 | 172.50 |
|---|---|---|---|---|---|---|
| PSNR | 34.68 | **38.89** | 36.29 | **33.84** | 35.57 | 35.27 |

A tight **33.8–38.9 dB** band with no outlier — this is 12 Mbps h.264 quantisation
plus up to 33 ms of animation phase from `-ss` landing on the nearest frame. Notably
**no frame hit an animation cliff** here, unlike the hi cut where one landed on a
`pop` boundary and read 23 dB.

Confirmed by eye **in the encoded master**:

- **@129.20 — the standing ban holds in the shipped file.** `TOP CREDIT TIER ABOUT 6%
  → $418/mo` · `SUBPRIME ABOUT 19% → $590/mo` · `EXTRA EVERY MONTH $172` ·
  `EXTRA INTEREST $12,400` · `Experian tier averages — illustrative band, not a quoted
  rate · payments are model output`. **No numeral from the 300–850 scale anywhere.**
- **@47.80 — s3** `300 —— 850`, `670+ = GENERALLY GOOD`, `FICO — score range 300 to
  850 · CFPB consumer education`. **81 s before** s7's first band. Never co-present.
- **@83.40 — s5** amber fill at `YEAR 7 OF 7`, mark cleared, `Fair Credit Reporting
  Act · 15 U.S.C. 1681c(a) · CFPB`, struck-through "clock starts when you pay it off"
  over `CLOCK STARTS AT THE MISSED PAYMENT`.
- **@15.60 — s1** `YOUR CREDIT REPORT` + 3 rows + `A MISS CAN STAY 7 YEARS` stamp.
- **@172.50 — end card** 4 chips + SUBSCRIBE intact.
- **Currency `$` throughout. No `₹`, no Indian imagery.** US market clean through
  the encode.

## 7 · Reported, not gates

1. **Integrated loudness −21.19 LUFS** (loudnorm) / **−21.2 LUFS** (ebur128); LRA
   3.60 LU (ebur128 3.5 LU, low −24.1, high −20.6); threshold −31.73. That is ~7.2 LU
   under YouTube's −14 LUFS reference, and YouTube applies **no positive gain**, so
   this ships quieter than the feed average. It is broadcast-correct (EBU R128 is −23)
   and it is **not** the gate — the gate is peak < −1 dBTP, which passes with 2.00 dB
   spare. It matches every prior cut in this pipeline (`credit-history` hi −22.17;
   `good-debt-vs-bad-debt` hi −22.02 / en −21.09; `pay-yourself-first` hi −22.24 /
   en −21.13), so it is a pipeline constant, not a regression. See §3 for why the
   optional `loudnorm I=-14:TP=-1` lift is worth promoting to standard.
2. **VO says "about a hundred seventy dollars", card reads `$172`.** Not a
   contradiction — "about" is doing exactly the work it should, and $172 is the exact
   figure. Recorded only so a future cut does not "fix" one to match the other and
   break the pairing in the other direction.
3. **Carried from invocation 1, unchanged:** s9's `READ BEFORE YOU ARE` chip is
   approved upstream copy anchored to the VO one beat earlier (confirmed present in
   the master at 172.50); the s5 `QUALITY` seal mitigation on file should read
   *"illegible under the grade at the bottom edge"*, not *"covered by the counter"*.

## Stream sheet

`h264 High L5.0 · yuv420p · tv range · bt709/bt709/bt709 · progressive · 1920×1080 ·
30 fps CFR · 11,765 kb/s` + `aac LC · 48 kHz · stereo · 178 kb/s` · overall
11,949 kb/s · 258,766,680 bytes.

## Sign-off — invocation 2

- [x] Runtime **173.233 s** video / **173.248 s** container vs 173.227 s → **+0.006 / +0.021 s**; **5197 frames exact**
- [x] Max VO drift **+0.0218 s** ≤ 0.1 s; 0.9 ms spread across 9 clips; 0.5 ms worst tail residual; no accumulation
- [x] Drift is the one-AAC-frame priming constant (21.29 ms measured vs 21.333 ms theoretical) — same in kind as hi, no flag
- [x] All 9 VO lines re-transcribed, present, correct slot and order; 0 words outside the VO windows
- [x] True peak **−3.00 dBTP** < −1 dBTP (2.00 dB headroom); no inter-sample overshoot; traced to en1.mp3's own −2.99 dBFS
- [x] Black segments **0** at three sensitivities, 5197/5197 frames scanned
- [x] Encoded master proven to be the gate-② composition (6 frames PSNR + 5 visual confirmations)
- [x] **MASTER QA: PASS — deliverable**
