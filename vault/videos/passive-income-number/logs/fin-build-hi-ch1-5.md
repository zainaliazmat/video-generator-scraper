---
summary: fin-editor round-2 blocker closed — s4's `.band` deleted, index.html regenerated, redrafted and re-sheeted. Measured from the encode: s4's p90 luma 40.3 -> 47.9 and the phone is back in frame under the ₹ card. One line removed from index.html, nothing else changed.
updated: 2026-08-08
source: studio/videos/passive-income-number-hi-ch1 (build.mjs, renders/DRAFT-ch1.mp4)
---

# fin-build — passive-income-number · hi · ch1 · attempt 5

Input: fin-editor round-2 blocker (`vault/videos/passive-income-number/logs/editor-hi-ch1-styleE-2.md`
finding 1, mirrored in `run.json chapters.hi.1.editor_r2_blocker`). Ruling: **delete**
`<div class="band"></div>` from s4. No lighter band, no gradient, no partial width.

## 1. The half-state, resolved (attempt 4 died mid-edit)

`build.mjs` was 24 minutes newer than `index.html` and 18 newer than the draft, with no log,
so the edit was of unknown completeness. Verified before running anything:

- `node --check build.mjs` → exit 0. Parses. (The 2026-08-07 failure mode — a stray backtick
  pair inside a comment inside the html template literal — would have thrown here.)
- The edit was **complete and coherent.** The band push had been narrowed from unconditional
  to `if (s.art === "ticks")` (build.mjs:257–272), with the rule-9 rationale rewritten in place
  to name the measurement and to say explicitly that s6 keeps it.
- s4 is `art:"lottie"`, s6 is `art:"ticks"`; the only three `art` values in SCENES are
  `off` / `lottie` / `ticks`, so that guard is exactly "s6 only" and cannot silently catch a
  future scene that wanted no band.

**No source edit was needed by me.** Attempt 4 finished the edit and died before regenerating.

## 2. Regeneration — proved by byte diff, not by claim

`node build.mjs`, output diffed against the pre-run copies:

```
$ diff index.before.html index.html
181d180
<   <div class="band"></div>
```

**One line removed. Nothing else in the file changed.** `assets/audio.json` byte-identical
(the s3→s4 `_hold` and the absence of a transition cue at 12.222 both survive; the 12 cues are
unchanged). Every data-start / data-duration / data-framings, the S and D maps, the eight
`<audio>` rows, the root 42.475s, the chained `plateKen 1.00→1.08→1.30`, `#s3-bg`/`#s4-bg` on the
one file with one background-position, `rise("#s4-stmt", S.s4 + 1.10, 0.7, 40)`, s1's textile
frame, s7's five drawn rungs, the rate asserts and s8 are all untouched — the diff is the proof.

s6 still carries its band (index.html:208, was 209). Confirmed on the sheet: s6's lower half is
visibly stepped back behind the icon row.

## 3. Checks

| check | result |
|---|---|
| `npx hyperframes check` | **passed** · 0 errors, 0 warnings, 10 infos · Motion 0/0 · Contrast **10/10 WCAG AA** |
| `python3 tools/check_vo_frame.py passive-income-number --cut hi --chapter 1` | **PASS** — 8 scenes cross-checked against their VO lines |
| `python3 tools/audio/cues.py studio/videos/passive-income-number-hi-ch1` | **exit 0** |
| `ffprobe` on the draft | `nb_read_frames=1275` · `duration=42.500000` · `r_frame_rate=30/1` — unchanged, so ch2's declared 42.475s offset still holds |

The 10 infos are all `container_overflow #sN-bg inside #sN` — the Ken Burns `.bg` inset overflowing
its clipping scene, which is what a ken IS. `known_benign`; no token was touched to satisfy anything.

Files, in the order the contract asks for: `build.mjs` 13:52:29 → `index.html` 14:34:54 →
`DRAFT-ch1.mp4` 14:37:15 → `SHEET-ch1.jpg` 14:39:20. **Both outputs newer than the source.**

## 4. THE FIX, MEASURED FROM THE ENCODE

The defect was found by measurement, so it is closed by measurement. Same box the editor
sampled — the card's own field, **x627–1267, y780–1080** — read off `renders/DRAFT-ch1.mp4`
with ffmpeg → gray rawvideo → numpy.

| t | scene | min | p10 | med | p90 | max | range | std | max vertical step |
|---|---|---|---|---|---|---|---|---|---|
| 10.17 | s3 (never had a band — the control) | 8 | 13 | 35 | 43 | 59 | 51 | 12.01 | 21 |
| **14.90** | **s4, band gone** | **7** | **13** | **38** | **43** | **54** | **47** | **11.83** | **20** |
| 17.00 | s4, card up | 8 | 21 | 47 | 76 | 255 | 247 | 36.64 | 167 |
| 18.10 | s4, card up | 8 | 21 | 44 | 70 | 241 | 233 | 32.24 | 173 |

The editor's reading was **"a flat 15–27 with no phone/table edge anywhere in it."** At 14.90 the
same box now runs **7–54, median 38, std 11.8**, with a **20-level vertical step** — and it is
statistically indistinguishable from s3 at 10.17 (the same photograph, one continuous zoom, no band
ever applied), which is the correct target: s4 should look like s3 zoomed, and now it does.

Row profile through the box at 14.90 (mean per 20px band) shows the phone as a shape, not a haze:
`y760 35.1 → y840 41.2` (the lit top edge of the phone body) `→ y920 26.2` (the dark screen)
`→ y980 34.0` (the far bezel / table return). Under the band this whole span was 22–27.

**Phone edge visible — confirmed by eye at 1:1, not only by number.** At 14.90 the crop shows the
full phone lying across the lower frame: the bright specular line along its top edge running
left-to-right, the dark screen slab, the warm body/table return at bottom-left, and the second
device edge at right. At 17.00 and 17.90, with the ₹ card up, the phone's bottom-left corner and
its lit edge read clearly below and left of the card, so the banner is sitting **on a device** —
which is the whole claim 1.4 exists to make, and which index.html's own comment
("~100 of its 132px on the phone body throughout") asserts. That comment is now true on screen.

The card itself needed nothing: at 1:1 it is an opaque slate panel with a light border, the ₹ tile
legible, the amount masked — exactly as the editor said, it reads against the raw photograph.

### Tonal curve, re-measured (7 samples inside each scene body, p90)

| scene | dur | p90 before | p90 now | |
|---|---|---|---|---|
| s1 | 4.222 | 45.9 | 45.7 | |
| s2 | 4.144 | 55.0 | 55.0 | brightest |
| s3 | 3.856 | 46.0 | 47.0 | |
| **s4** | **5.763** | **40.3** | **47.9** | **+7.6 — no longer the second-darkest; now in line with its own photograph (s3 47.0) and s5 48.6** |
| s5 | 3.673 | 48.9 | 48.6 | |
| s6 | 8.167 | 37.7 | 37.7 | darkest, unchanged — its band is load-bearing and was not touched |
| s7 | 5.345 | 43.7 | 44.7 | |
| s8 | 7.304 | 49.9 | 49.6 | |

Duration-weighted p90 **45.1 → 46.3**. Opens 45.9, closes 49.6 — **arc +3.9**, still rising, and
the chapter's shape (s6 as the darkest and longest-held trough) is intact. The only scene that
moved is the one the ruling named. s4's payoff beat now lifts instead of dipping.

## 5. Not done, deliberately

- **No `snapshot` pass.** The change is a one-line deletion proved by byte diff, and the encode
  itself was sampled at 12 timestamps plus the 8-frame sheet — snapshotting the same composition a
  third time would test nothing the render did not already test. Layout is unchanged: nothing moved,
  one overlay stopped painting.
- **No icon written to `assets/icons/`** — nothing new was drawn.
- **s7's five drawn rungs left alone** (HELD at should-fix, referred to the CEO — not pre-empted).
- **run.json not touched** — the orchestrator owns `chapters.hi.1.status`.
