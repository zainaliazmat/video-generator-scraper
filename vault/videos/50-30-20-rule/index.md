---
summary: Milestone note for the «50-30-20 Rule» pair — Hindi/₹ 3:13.5 · US/$ 3:43.3, built 2026-07-27. LIVE on YouTube (hi youtu.be/FstXhGwOCjo · en youtu.be/-qrvQMrETn0); source archived to `src/`, studio dir deleted 2026-07-29. Both cuts argue a MODIFIED split, not the textbook one. Owed — analytics after 28 days.
updated: 2026-07-29
source: the archived compositions in `src/` (runtimes read from `data-duration`, voices from `gen_vo_*.sh`) + [[youtube-metadata-hi]] · [[youtube-metadata-en]] + [[../../knowledge/channels]]
---

# 50-30-20 Rule (milestone note)

The budgeting-rule pair. Both cuts take the same position: the textbook
50-30-20 split **does not survive 2026 costs**, so each ships a modified
version rather than repeating the rule.

## The two cuts

| Cut | Runtime | Voice | Title |
|---|---|---|---|
| hi | **3:13.5** (193.45 s, 9 VO lines) | Harsh `HTUuC7OeeEt6OL5fViVe` — standard Hindi, informative/educational | ₹30,000 Salary Kaise Manage Kare \| 50-30-20 Rule Ka India Version |
| en | **3:43.3** (223.25 s, 9 VO lines) | Brian `nPczCjzI2devNBz1zQrb` — same voice as emergency-fund-en, for channel continuity | The 50/30/20 Budget Rule Doesn't Survive 2026 Rent (Here's the Fix) |

Both run **long for the format** (the finance norm is ~2:50–3:00); the en cut at
3:43 is the longest finance cut shipped so far.

`src/legacy/` is a **third, superseded cut** — the pre-hi/en single-version draft
(`meta.json` dated 2026-07-21, 2:15.9). It predates the two-channel split and was
never published. Kept because it is the only record of the pre-pivot structure.

## Packaging findings

- **hi — the Warikoo warning.** His 65-20-15 video did **507k views on our exact
  thesis**. Ours is **65-15-20** — we protect *savings*, he protects *wants*. That
  one-position difference is the whole differentiation; do not blur it.
- **en — the bare "50/30/20" keyword is AI-slop-saturated.** The live US lane is
  the **payday routine** (Nick Invests, 350k). Title off the routine, not the rule.

## Published + archived (2026-07-29)

**State: LIVE on YouTube (both cuts) · source archived · studio dir deleted.**

| Cut | Channel | URL | Thumbnail |
|---|---|---|---|
| hi | @cashguruguides | https://youtu.be/FstXhGwOCjo | `src/hi/thumbnail-hi.png` (single) |
| en | @moneymavens101 | https://youtu.be/-qrvQMrETn0 | `src/en/thumbnail-en.png` (single) |

**Source: `src/{hi,en,legacy,thumbs}/`** — composition, meta/package JSON,
`gen_vo_*.sh`, the VO lines (`assets/voice/*.txt`), stock CREDITS and the thumbnail
PNGs. `studio/videos/50-30-20-rule*` and `studio/videos/50-30-20-thumbs` (the odd
name predating the `<slug>-thumbs` convention) are **deleted** per the finished-video
rule ([[../../CLAUDE]]). **Re-render is reproducible, not free** — the scene photos
and VO mp3s are gone, so a rebuild re-pays image gens + ElevenLabs.

⚠️ **Predates the `.src` image-prompt convention** — no `assets/img/*.src` in this
archive (the convention starts at pay-yourself-first). VO is fully reproducible (27
lines + voice IDs + `gen_vo_*.sh`); the scene photos are not, and **no storyboard note
was ever written for this pair**, so the publish packs' chapter list and the archived
`index.html` are the only record of what each scene showed.

Still owed:
- **analytics after 28 days** (only then may anything here touch
  [[../../knowledge/best-practices]])

Related: [[youtube-metadata-hi]] · [[youtube-metadata-en]] ·
[[../needs-vs-wants/index]] · [[../emergency-fund/index]] · [[../../knowledge/channels]]
