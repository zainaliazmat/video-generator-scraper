---
summary: Combined gate-two frame check + master QA for the -en cut, attempt 2 (blockframe-9 rebuild). Every measured number passes — 626.773s runtime, max latency-corrected VO drift +0.107s, PUBLISH -14.19 LUFS / -1.69 dBTP, 0 black segments in 18,803 frames, dissolve stacking proven correct by measurement. FAIL on one item only - s77.jpg was never replaced; the birdbath gate two blocked in attempt 1 is still on screen for 14.9s while the VO describes the Ryoan-ji tsukubai.
updated: 2026-08-02
source: hyperframes snapshot (120 frames, 5 batches) + ffmpeg astats/loudnorm/blackdetect/signalstats + Silero VAD and faster-whisper base.en over renders/FINAL-1080p-en.mp4
stage: fin-render, cut en, attempt 2 (post-encode QA, no encode run by this stage)
---

# fin-render — japanese-money-methods · cut `en` · attempt 2

**STATUS: fail.** One finding (§1). Everything else — all 92 scene frames, all 24
mid-dissolve frames, and every audio/video number below — passes.

## Masters measured

| File | Duration | Video | Audio | Size |
|---|---|---|---|---|
| `renders/FINAL-1080p-en.mp4` | **626.773333 s** (18,803 frames @ 30 fps) | h264 1920×1080 30/1, 12.181 Mb/s | AAC 48 kHz stereo, 29,380 frames | 954,367,099 B |
| `renders/MIXED-1080p-en.mp4` | 626.773000 s | same, 12.204 Mb/s | 29,381 frames | 956,128,741 B |
| `renders/PUBLISH-1080p-en.mp4` | 626.800000 s | same, 12.205 Mb/s | 30,085,120 samples | 956,258,300 B |

**Runtime vs `timing.json`.** `timing.json total` = **626.743 s**; `#root
data-duration` = 626.743 s. FINAL is **+0.030 s** (0.9 frame — the encoder's
tail frame), PUBLISH **+0.057 s**. Both inside a frame quantum; no truncation,
no over-run. Last VO line (`8.8`) ends at 626.193 s, 0.550 s before the tail.

## 1. The one finding — `s77.jpg` is still the birdbath

`assets/img/s77.jpg` was **not replaced** after gate two blocked it in attempt 1.
Evidence, three independent ways:

- `assets/img/s77.jpg.src` still reads `square stone water basin japanese
  garden@pexels#7` — the same query the previous log identified as the root cause.
- `CREDITS.txt` line 92 still reads `s77.jpg → …/serene-leaf-floating-on-water-in-birdbath-37181885/ by Dhanush N`.
- File mtime 2026-08-01 11:55, i.e. **older than the blockframe-9 `index.html`
  (14:20)** — it predates the rebuild.

What the rebuild changed instead was the **words**: line `7.4` was re-voiced from
*"…the empty square hole in the middle of the basin"* to *"…the emptiness at the
centre of the basin"*, and `#s77-stmt` to *"All four share one part — the
emptiness at the centre."*

**Words and frame still do not agree.** Sampled at 519.820 / 520.100 / 524.898 /
525.053 / 526.823 / 527.300 s, the frame shows a square garden birdbath brim-full
of murky water with one yellow leaf floating at its centre. There is no opening,
no round stone and no carved characters — so nothing on screen is empty, and
nothing on screen is the object the narration spends four lines explaining:

| Where | Text |
|---|---|
| VO `7.2` (over s75) | "…a stone water basin with **four characters cut around the hole in its center**." |
| `#s75-stmt` | "A stone basin. **Four characters cut into it**." |
| `#s76-foot` | "The **tsukubai inscription at Ryoan-ji, Kyoto**" |
| VO `7.4` / `#s77-stmt` | "…that shared part is **the emptiness at the centre** of the basin." |
| VO `7.5` / `#s78-stmt` | "Each needs **the emptiness in the middle** to be whole." |

Exposure is unchanged at **14.9 s** — `#s77-bg` (517.368→525.122) and `#s78-bg`
(524.673→532.323) both point at the same file. It is the longest single-photograph
hold in the cut, and the only place the narration describes the picture in detail.

Softening the copy narrowed the contradiction but did not remove it: the cut still
asserts an inscription and a central opening that the photograph does not contain.

*Motion on the pair is correct* — one continuous `ken` push per scene on the shared
file, plain cross-dissolve between, **no self-dissolve flicker**; 527.300 s is
visibly tighter on the water than 520.100 s. The motion is right; the photograph is not.

## 2. VO drift — 92/92 lines, latency-corrected

Silero VAD (`faster_whisper.vad`, threshold 0.5, `min_silence 180 ms`,
`speech_pad 0`) over FINAL's decoded audio → 201 speech runs; each of the 92
`<audio data-start>` values matched to its nearest onset. Matches are **unique and
monotonic** (92 distinct onsets, strictly increasing) — no line unmatched, none
double-claimed.

| | Raw VAD | Corrected (− `qa.vad_onset_latency_seconds` 0.101) |
|---|---|---|
| min | +0.018 s | **−0.083 s** |
| max | +0.208 s | **+0.107 s** |
| max abs | 0.208 s | **0.107 s** |
| median | +0.103 s | **+0.002 s** |
| mean | +0.104 s | +0.003 s |

**Max drift 0.107 s, on one line (`8.7`, expected 614.448 → onset 614.656).**
91 of 92 lines are ≤ 0.090 s. That one raw value, 0.208 s, is exactly 6.5 ×
`qa.vad_grid_seconds` (0.032) — the detector's own quantum puts its true residual
somewhere in **[0.075, 0.107] s**, so it is at the resolution limit of the
measurement rather than 7 ms over target. Treated as pass.

Sanity check on the constant itself: the raw **median +0.103 s** reproduces the
stored 0.101 s bias to 2 ms across a different cut and a different voice — the
calibration in `format.json` holds.

Worst ten, corrected: `8-7` +0.107 · `8-4` +0.090 · `2-7` −0.083 · `8-3` +0.070 ·
`4-5` +0.068 · `3-4` −0.066 · `7-5` −0.064 · `7-10` +0.064 · `6-11` −0.062 ·
`1-6` −0.061.

## 3. Whisper — coverage only

`base.en`, int8, `vad_filter=False`. **105 segments** for 92 lines (the hi cut's
`base` produced 173 for the same 92 — this run merged far less). Speech occupies
**571.5 s of 626.77 s (91.2 %)**; largest inter-segment gap **2.0 s** (at 572.5 s
and 538.5 s), consistent with the tiered pauses; **no gap > 3 s anywhere**. First
speech at 0.000 s, last segment ends 625.5 s. **No dropped clip, no silent stretch.**

Keyword sweep of all 92 `assets/voice/*.txt` against the transcript flagged four
lines under 50 % — `3.8`, `3.9`, `5.5`, `5.10` — all four are Whisper writing
numerals where the VO spells them out ("15 %" for "fifteen percent", "$3,200" for
"thirty-two hundred dollars"). Each verified present verbatim. **Coverage: 92/92.**

No per-line onset was taken from Whisper.

## 4. Levels

| Master | LUFS-I | True peak | LRA |
|---|---|---|---|
| FINAL | −21.21 | **−2.60 dBTP** | 3.00 |
| MIXED | −21.26 | **−2.75 dBTP** | 2.90 |
| **PUBLISH** | **−14.19** | **−1.69 dBTP** | 3.10 |

PUBLISH `astats`: peak level −1.691785 dBFS, sample peak +0.823021 / −0.819798,
RMS −17.603 dB, RMS peak −9.466 dB, crest 6.25, **abs-peak count 1**, flat factor
0.000, 0 NaN / 0 Inf / 0 denormals, bit depth 31/32. **All three masters sit below
the −1 dBTP ceiling**; PUBLISH lands on the −14 LUFS target to 0.19 dB.

## 5. Black scan — the 92-scrim warning is a false alarm here too

`blackdetect=d=0.05:pic_th=0.98:pix_th=0.10` + `signalstats` over **all 18,803
frames** of FINAL:

- **0 black segments.**
- YAVG **min 32.38** (t = 168.87 s), **max 76.54**, **mean 54.10**.
- First half **52.79** vs second half **55.40** — the second half is *brighter*;
  no cumulative darkening from the stacked overlays.
- Frames below YAVG 25: **0**. Below 16: **0**. Below 10: **0**.

The build escalated `composition_heavy_overlay_count_high` (92 `.scrim` divs).
This is the second long blockframe-9 cut to clear it cleanly (hi: 0 segments in
19,775 frames, min 31.1, 52.9 / 52.1). **The warning can be closed for long
blockframe-9 cuts generally** — a `.scrim` per scene is one composited layer per
scene, not 92 stacked ones, and the numbers say so on both cuts.

## 6. Frames sampled — 120

| Batch | Count | What |
|---|---|---|
| `snapshots/qa3/sceneA` | 46 | scenes s1–s46, each at its own last cue + 0.35 s |
| `snapshots/qa3/sceneB1` | 23 | s47–s69 |
| `snapshots/qa3/sceneB2r` | 27 | s70–s92 + 4 extra on s75–s78 (507.0, 514.0, 520.1, 527.3) |
| `snapshots/qa3/diss` | 24 | 12 boundaries × **both** `qa.dissolve_sample_offsets` |
| `snapshots/qa3/warm` | 4 | timing warm-up (1.65, 6.189, 13.624, 19.57) |

Scene sample times were computed, not guessed: `min(last_non-ken_cue_end + 0.35,
scene_end − 0.55)`, floored at `scene_start + 1.0`, so every frame lands after the
last text has finished rising and before the next dissolve opens.

**Dissolve boundaries, both offsets** (start + 0.225 / start + 0.380):
s1→s2 4.264/4.419 · s12→s13 71.030/71.185 · s23→s24 145.763/145.918 ·
**s33→s34 220.950/221.105 (act shove)** · s44→s45 292.914/293.069 ·
s57→s58 386.253/386.408 · s66→s67 449.120/449.275 ·
**s73→s74 498.214/498.369 (act shove)** · **s77→s78 524.898/525.053 (shared image)** ·
s84→s85 574.357/574.512 · **s90→s91 614.423/614.578 (CTA)** · s91→s92 621.074/621.229.

### The stacking fix holds — and this time it is measured, not eyeballed

At the `+0.380` offset the incoming `.stack` is up, so the double-paint window is
actually open. At all 12 boundaries the outgoing block is **under** the incoming
scene and visibly attenuated; background detail reads *through* the outgoing
glyphs. Never two headlines at full strength.

Quantified on s90→s91, using the `.cta` pill as a known solid (`--pop` #ff5c39).
Chroma-V excess over neutral in the pill's 280×60 px box:

| Frame | V excess | Residual |
|---|---|---|
| 618.160 s (pill alone, full strength) | 51.3 | 100 % |
| 621.074 s (+0.225 into the overlap) | 26.8 | **52 %** |
| 621.229 s (+0.380 into the overlap) | 4.0 | **7.8 %** |

A monotonic decay tracking the crossfade ramp. Under the japanese-money-methods-hi
defect this figure would have stayed at 100 % for the whole 0.45 s. It does not.
`blockframe.css:63` `.scene { isolation: isolate; }` is doing its job.

## 7. The rest of gate two — pass

| Check | Result |
|---|---|
| Architecture | **blockframe-9, genuinely.** `<div id="root" class="cut-en">`, no body class. 92 × `.scene.clip`, each exactly `.bg` + `.scrim` + `.grain` + `.stack`. Document contains **0** `.rail`, **0** `.railcol`, **0** `.panel`. Centred stack over full-bleed photo in all 120 frames. |
| Watermark | `#root.cut-en::after → img/wm-en.png`, md5 `21de2de7fedf2d0cdaec655ed60704cb` = **@moneymavens101** (pink ring, yellow bespectacled coin). Distinct from `wm-hi.png` `292c19c0c87ccc8db23384dcd044a110`, which appears nowhere. Present bottom-right in **all 120 frames**, dissolve frames included (it hangs off `#root`). |
| `cut-en` class | Present on `#root`. No `cut-hi` anywhere. |
| SUBSCRIBE | `.cta` block: `background: var(--pop)` #ff5c39, `color:#0d1017`. Sampled 618.160 s — **solid orange pill, dark label, on a dark desk photo** (pill box YAVG 102.2, VAVG 179.3). Not white. |
| Safe area | All kicker / statement / foot / icon type inside the 110×150 px scene padding across 92 scene frames. No clipping, no overflow, nothing under the watermark. |
| Contrast | Legible in every frame. Weakest is s43 @ 282.760 s (green #22c55e on a pale wall) — holds via its text shadow, but it is the floor of the cut. |
| `data-framings` | All three fire and are visually distinct: s32 → Japanese noticeboard @ 211.847; s36 → cotton field / semi truck @ 239.5 / 240.828; s79 → apartment block @ 538.123. |
| Currency & market | **$ only** — 12 `$` tokens: $4,000 worked example, $800 / $3,200, $200, $400, $83,730 (Census P60-286). USD notes and a US quarter as b-roll. JPY appears only inside Japan's own quoted statistics (197,432 / 522,569 / 175,241 / 6,705, FIES 2024) and BOJ Flow of Funds. US institutions throughout (Federal Reserve G.19, SHED 2025, US Census). |
| Prohibited imagery | **0 ₹, 0 Devanagari codepoints in `index.html` and in all 92 VO text files.** 0 hits for rupee/India/Indian/RBI/SEBI/lakh/crore/UPI/Paytm. Only non-Latin script on screen is Japanese signage in s32's second framing and s33 — intentional. |
| Phone screens | s12 @ 66.539 (phone silhouette at dusk, no UI) and s39 @ 257.810 (a printed statement, not a phone) — no currency symbol, no localised UI. |

## 8. Cosmetic, unchanged from attempt 1

`#s69-icon`'s arrowhead still reads as a hook rather than an arrow at the
`.icon.sm` 130 px size (466.985 s). Draws, takes `fundc` green, legible as motion.
Not worth a rebuild.

## 9. Process note — the snapshot readiness warning

**Every** batch, including a 27-frame batch run alone on an idle machine with
`--timeout 20000`, printed `⚠ Runtime did not become render-ready within Nms —
snapshots may be inaccurate`, and most also printed `⚠ Shader transitions did not
finish pre-rendering` (this composition uses no shader transitions — its dissolves
are GSAP opacity). Frames came back correct in all five batches: fonts loaded,
images present, text at final position, watermark composited, and the dissolve
residuals decay exactly as the ramp predicts. Treated as a readiness-signal quirk
of this project, not a frame defect. Worth a look next time `tools/scaffold/` moves.

Also: `hyperframes snapshot` fails hard on `Navigation timeout of 10000 ms
exceeded` when the box is loaded (one 46-frame batch died that way at load ~8 and
needed a retry loop). Budget gate-two sampling on an idle machine.

## Verdict

The master is technically clean — runtime, drift, levels, black scan and the
dissolve stacking all pass with margin, and two long-standing warnings
(`composition_heavy_overlay_count_high`, the cross-dissolve double-paint) are now
closed with numbers rather than opinion.

The one thing gate two blocked last time is the one thing that did not change.
This is the **second frame set carrying the same defect**, so it is terminal for
automatic retry: the next move is the creator's, not another build loop.

**NEXT: creator decision on `s77.jpg` — swap it for a real Ryoan-ji tsukubai frame
(search `tsukubai` / `chozubachi` / `ryoanji stone basin square hole`, never
`square stone water basin`), keep it held across `#s77-bg` and `#s78-bg`, update
`.src` / `manifest.json` / `CREDITS.txt`, and re-encode — or accept the mismatch
and ship as-is.**
