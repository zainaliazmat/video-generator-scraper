---
summary: Chapter-1 draft render + contact sheet for passive-income-number-hi. 1073 frames / 35.767s at 30fps, phone_notify_credit Lottie confirmed drawing on screen. One image defect: s4's envelope reads as a flat grey panel.
updated: 2026-08-07
source: studio/videos/passive-income-number-hi-ch1 draft render, attempt 1
---

# fin-render — passive-income-number · hi · chapter 1 · attempt 1

**Mode: chapter draft (orchestrator §3b step 4).** No gate-two frame check, no
dissolve sampling, no 1080p encode — those run once at cut level. This pass
exists so images / motion / timing get judged in minutes.

## Commands run (verbatim)

```
npx hyperframes render . -c index.html -o renders/DRAFT-ch1.mp4 -q draft -f 30
python3 tools/chapter_sheet.py studio/videos/passive-income-number-hi-ch1 \
        renders/DRAFT-ch1.mp4 -o .../renders/SHEET-ch1.jpg
```

No `--resolution`, no `--gpu`, no `--video-bitrate`, no chunked encode. `-f 30`
matches the fps the final will use (the composition declares no `data-fps`; the
CLI default is 30 and the s3 Lottie comment fixes 30 as the design fps — "75
frames at 30fps = 2.50s"). Nothing rendered at 24, so the frame counts sum.

## Measured numbers

| Quantity | Measured | Expected | Verdict |
|---|---|---|---|
| Frame count (`ffprobe -count_frames`) | **1073** | ceil(35.745 × 30) = 1073 | exact |
| Video stream duration | **35.767s** | 1073 / 30 = 35.7667 | exact |
| Container / audio duration | 35.776s | — | +0.009s AAC frame pad, benign |
| Declared root `data-duration` | 35.745s | timing.json | matches |
| Frame rate | 30/1 CFR | 30 | ok |
| Resolution | 1920×1080 | 1920×1080 | ok |
| Chapter offset | 0.000s | ch1 opens the cut | concatenates as-is |
| Last scene `data-duration` | 6.599 (bare, no +0.45) | bare by design | `cut_assemble.py` re-adds the overlap |
| Black segments (`blackdetect d=0.15 pix_th=0.10`) | **none** | none | ok |
| Draft audio max_volume | −5.1 dB | not silent | VO present (voice-only; bed/SFX are the post-mix step) |
| Draft audio mean_volume | −25.3 dB | — | informational |
| Render wall time | 1m 05.7s, 8.0 MB | — | — |

Scene starts land where `timing.json` put them; nothing was re-timed here.

## The Lottie — verified from the ENCODED frames, not from the reference

`phone_notify_credit` shipped absent once: `tools/lottie/tint.py` built the
wrapper identifier from the output basename verbatim, so the hyphenated twin in
the same directory emitted invalid JS, left `window.L_phone_notify_credit`
undefined, and rendered a blank scene with every check green. index.html now
loads the UNDERSCORED file and throws loudly on an undefined global.

Confirming the file is *referenced* proves nothing, so this was read off the
mp4. Cropped 1000×420 at (460,600) — the `.v-lstage` box — at seven times
across the play window (`playLottie(s3art, S.s3 + 0.30, 2.50)` = 10.076 →
12.576):

| t | What is on screen |
|---|---|
| 9.900 | s2 (chai) — Lottie not started. Correct. |
| 10.100 | s3 fading in, banner not yet up. Correct (starts 10.076, alpha still low). |
| 10.400 | Banner card + avatar square only. |
| 10.880 | Title bar and right-hand timestamp dash drawn in. (Bloom peak +0.80 = 10.876 — the frame the buzz cue binds to.) |
| 11.300 | Second (amount) bar begins, short. |
| 11.800 | Amount bar longer. |
| 12.250 | Amount bar at full length. |

**Visible AND animating** — the artwork builds monotonically across the window
rather than holding one frame, which is what a broken seek would look like. The
`.v-lstage` 820×300 pixel box works: the svg is centred in the D-band, not
pinned top-left at native size.

Also confirmed: the amount is masked (bars, no legible figure), the phone is
face-down, so the "no phone-screen photo" rejection and the open loop both hold.

## Contact sheet

`renders/SHEET-ch1.jpg` — 7 cells, one per scene, plus `SHEET-ch1.json` for the
orchestrator's cross-chapter PNG. s3 sampled at 12.026 (its 3.0s duration is not
> SETTLE+0.4, so `chapter_sheet.py` falls to duration × 0.75) which lands inside
the Lottie window — the sheet shows the banner, not a blank.

### Repetition check
Seven distinct photographs, no reuse: clock · chai · face-down phone · envelope ·
paper stack · stone stairs · brass scale. The "one photo behind three points"
failure is not present.

### Legibility check (full-res, not sheet-res)
- s1 / s2 / s5 / s6 / s7 — white type over scrimmed dark ground, all legible.
- s7's foot fits on ONE line: the `.scene.centred .v-footwide { max-width: 1400px }`
  one-off works, "arithmetic" is no longer orphaned. The 2-line focal at 900px
  is the intended shape.
- Channel watermark (`#root.cut-hi::after` → `img/wm-hi.png`) present bottom-right
  on all 7 frames. By design, not a defect.

## Defect found — s4

**s4 is functionally photo-free.** The prompt was
`single closed brown envelope on a bare wooden table@pexels` and the file
delivers exactly that — but the envelope is a featureless kraft rectangle that
fills ~85% of the 1733×1300 source. After `.has-photo`'s 38% tint + scrim + the
ken pass, the frame reads as **flat charcoal with a thin wood border**. No flap,
no seam, no address, no depth — nothing that says "envelope".

Checked at both ken extremes (s4's ken is `zoomIn=false`, 1.16 → 1.0, so the
widest framing is at the end): at 14.927 it is a grey slab; at 16.600, its widest,
it is still a grey slab. The crop is not the problem — the photograph is.

Two standing rules this lands on:
- `format.json _image_per_scene_note` — "images are compulsury", and
  `layout.photo_free_scene_ratio = 0`. s4 satisfies the letter (a jpg is loaded)
  and breaks the intent (the viewer sees flat colour).
- The sound-off image rule — the image alone must say the LINE. s4's line is
  "You just reached a number"; a blank panel says nothing.

Nothing to fix in build.mjs — this is an asset swap. Suggested direction: an
envelope with a visible flap / postmark / a hand holding it, or drop the envelope
metaphor entirely for something that reads a *threshold* (a bank passbook page, a
milestone marker). The reviewers own the call; `fin-assets` owns the swap.

## Minor note, not a defect

s2's copy is "Tea. The window. One buzz." — the photo carries the tea only. The
tea is the anchor and it reads, so this is not being raised as a failure, but if
fin-editor wants a stronger sound-off frame the window or the phone buzz is the
missing half.

## Not done here, by contract

Gate-two per-scene frame check, cross-dissolve sampling at
`qa.dissolve_sample_offsets` [0.225, 0.38], faster-whisper VO drift vs the
`data-start` table, VAD onsets less `qa.vad_onset_latency_seconds` (0.101), and
the −1 dBTP peak read all belong to the cut-level QA pass on
`renders/FINAL-1080p-hi.mp4`, after all seven chapters are assembled. This
chapter draft is not a master and none of those numbers would mean anything on it.
