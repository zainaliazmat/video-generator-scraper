---
summary: Finance video "The Emergency Fund" — the pair (Haryanvi/₹ + US-English/$). State, the numbers each cut uses, and the localization rebuild of the English cut on 2026-07-27.
updated: 2026-07-27
source: studio/videos/emergency-fund (hi) + emergency-fund-en (en) + emergency-fund-thumbs. Numbers from [[../knowledge/money-facts-2026]].
---

# Emergency Fund — video pair

Second finance video after the 50-30-20 pair's format. Nine scenes, photographic
backgrounds under a single grade, chip/stamp motion language, ~2.5 min.

| Cut | Project | Runtime | Voice | State |
|---|---|---|---|---|
| Haryanvi / ₹ | `studio/videos/emergency-fund` | 2:24 | Prayan `9BHT…` | rendered 2026-07-23, upload pending |
| US-English / $ | `studio/videos/emergency-fund-en` | **2:46** | Brian `nPczC…` | **rebuilt 2026-07-27**, final 1080p rendered + creator-approved, publish pack written — **ready to upload** |

Thumbnails for both live in `studio/videos/emergency-fund-thumbs` (one HTML,
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

**Final US master:** `renders/emergency-fund-en-US-FINAL-1080p.mp4` — 2:46,
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

## Owed

- Proof-listen of the Brian read (generated blind; "two DoorDash orders" may
  read as "two-door dash").
- Upload both cuts; record URLs + publish dates here, then run the post-delivery
  cleanup in [[../CLAUDE]] (delete renders/audio, keep text + thumbnails).
- The superseded rupee-era `-en` render is still in `renders/` — delete on the
  creator's word.

## Published + archived (2026-07-29)

- **en** (@moneymavens101): https://youtu.be/6dFBciWSs0o
- **hi** (@cashguruguides): https://youtu.be/vZG7fkPwpzI

Finished per the finished-video rule (`vault/CLAUDE.md`): source archived to `src/`, `studio/videos/emergency-fund*` deleted.
