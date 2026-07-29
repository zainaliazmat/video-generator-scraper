---
summary: Finance video "The Emergency Fund" — the pair (Haryanvi/₹ 2:24 + US-English/$ 2:46). **LIVE on YouTube** (hi youtu.be/vZG7fkPwpzI · en youtu.be/6dFBciWSs0o); source archived to `src/`, studio dir deleted 2026-07-29 — the thinnest archive of the five (no image prompts, no stock CREDITS). The numbers each cut uses, and the localization rebuild of the English cut on 2026-07-27. Owed — analytics after 28 days.
updated: 2026-07-29
source: the archived compositions in `src/{hi,en,thumbs}/` (originally studio/videos/emergency-fund, -en, -thumbs). Numbers from [[../knowledge/money-facts-2026]].
---

# Emergency Fund — video pair

Second finance video after the 50-30-20 pair's format. Nine scenes, photographic
backgrounds under a single grade, chip/stamp motion language, ~2.5 min.

| Cut | Project | Runtime | Voice | State |
|---|---|---|---|---|
| Haryanvi / ₹ | `src/hi/` | 2:24 | `9BHTbeEKC5ZqMmvZfLW6` (Haryanvi — pre-dates the standard-Hindi switch) | **LIVE** youtu.be/vZG7fkPwpzI |
| US-English / $ | `src/en/` | **2:46** | Brian `nPczCjzI2devNBz1zQrb` | **rebuilt 2026-07-27** (creator-approved), **LIVE** youtu.be/6dFBciWSs0o |

Thumbnails for both live in `vault/videos/emergency-fund/src/thumbs` (one HTML,
two sections, `snapshot --at` → PNG).

## The English cut was rebuilt, not re-priced (2026-07-27)

The 2026-07-23 `-en` render was a line-for-line English translation of the
Haryanvi script: rupees and lakh on screen and in the VO, a motorcycle as the
emergency, "skip two takeaways", "instant access", a Swiss franc coin and euro
coins in the b-roll. Creator direction: **the English version is a US video —
$ prices and US standards throughout.** That rule now lives in
[[../knowledge/us-english-script-style]]; it applies to every future `-en` cut.

What the US cut says now (numbers sourced in [[../knowledge/money-facts-2026]]):

- **Hook:** 4 in 10 Americans can't cover a $400 surprise in cash (Fed SHED
  2025) → car won't start / layoff email / **22% credit card**.
- **How big:** 3 months of *expenses*, first target **$1,000**.
- **Where:** high-yield savings, a different bank, **FDIC insured**,
  **1–2 days away, not instant** — no CDs, no stocks, no crypto.
- **How:** **$50/week = 2 DoorDash orders**, auto-transfer the day after payday.
  "Automatic beats heroic."
- **Math:** $3,000/mo → $9,000 target → first milestone $1,000 → **20 weeks**.
- **Thumbnail:** "ONE REPAIR FROM BROKE — fix it with **$50** a week" over a car
  in the shop.

## Build notes

- Per-**scene** VO (9 clips), not per-line — so every on-screen cue was placed
  from **faster-whisper word timestamps**, `scene_start + 0.4 + word_time`
  (technique now in [[../skills/hyperframes_production]] §5a).
- The finished render was re-transcribed to verify placement; all 9 scenes
  within 0.1 s of the composition's `data-start` table.
- Photo swaps carry a grade obligation: the replacement dollar-bill shots were
  far brighter than the other seven and needed a per-image `filter:` override.
- `gen_vo_en.sh` regenerates the whole English VO (the old `gen_vo.sh` /
  `gen_vo_haryanvi.sh` both `cd` into the **hi** project — don't reuse them for
  the `-en` cut).

**Final US master** *(render deleted on archive — it is on YouTube now)* — was
`renders/emergency-fund-en-US-FINAL-1080p.mp4`, 2:46,
1920×1080 H.264 30 fps, AAC 48 kHz stereo, 6.9 Mbps, 137 MB. Rendered
`-q high --resolution 1080p` with `PRODUCER_ENABLE_CHUNKED_ENCODE=true`
(18m 13s). QA: peak −2.5 dBTP, 0 black segments, VO placement verified by
re-transcription.

## Publish

**Metadata is written and researched: [[youtube-metadata-en]]** — title options
(recommended: *Emergency Fund 2026: How Much, Where to Keep It, How to Start*),
description with real chapter timestamps + on-screen source citations, a
490-char verified-autocomplete tag list, and publish settings. The competitor
scoreboard behind it is promoted into
[[../../knowledge/best-practices]] → Packaging.

The ₹ cut still needs its own pack — **do not reuse this one**: the Hindi
demand cluster is a different set of search strings entirely.

## Published + archived (2026-07-29)

**State: LIVE on YouTube (both cuts) · source archived · studio dir deleted.**

| Cut | Channel | URL | Thumbnail |
|---|---|---|---|
| hi | @cashguruguides | https://youtu.be/vZG7fkPwpzI | `thumbnail-hi.png` (single) |
| en | @moneymavens101 | https://youtu.be/6dFBciWSs0o | `thumbnail-en.png` (single) |

**Source: `src/{hi,en,thumbs}/`** — composition, meta/package JSON, `gen_vo*.sh`, the 45
VO lines (`assets/voice/*.txt`) and the thumbnail PNGs. `studio/videos/emergency-fund*`
is **deleted** per the finished-video rule ([[../../CLAUDE]]) — including the two masters
and the superseded rupee-era `-en` render that was owed a deletion.

⚠️ **The thinnest archive of the five.** It predates both the `.src` image-prompt
convention *and* the stock-`CREDITS.txt` convention, so neither the image prompts nor the
stock attribution survive. VO is fully reproducible (lines + voice IDs + `gen_vo*.sh`;
note the hi cut used the **Haryanvi** voice `9BHTbeEKC5ZqMmvZfLW6`, from before the
standard-Hindi switch) — the photography is not. Rebuild from [[youtube-metadata-en]] and
the Build notes above.

Still owed:
- **analytics after 28 days** (only then may learnings touch best-practices)

~~proof-listen of the Brian read~~ (generated blind; "two DoorDash orders" risked reading
as "two-door dash") · ~~upload both cuts~~ · ~~delete the superseded rupee-era render~~.
