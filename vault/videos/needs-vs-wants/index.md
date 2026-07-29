---
summary: Milestone note for «Needs vs Wants — the subscription leak» (video #3) — Hindi/₹ 2:58.7 · US/$ 2:49.6, both rendered 2026-07-27. LIVE on YouTube (hi youtu.be/I9cxxhcdfg0 · en youtu.be/4DimmIqnxSM); source archived to `src/`, studio dir deleted 2026-07-29. Owed — analytics after 28 days. Introduced the wants=amber / red-is-only-the-leak colour rule.
updated: 2026-07-29
source: the archived compositions in `src/` (runtimes read from `data-duration`, voices from `gen_vo_*.sh`) + [[script-hi]] · [[script-en]] · [[storyboard-hi]] · [[storyboard-en]] + the two publish packs
---

# Needs vs Wants — the subscription leak (milestone note)

Video #3 of the finance pair. The thesis: the money is not lost to one big
purchase — it leaks out of small recurring ones nobody ever re-decides.

## The two cuts

| Cut | Runtime | Voice | Title |
|---|---|---|---|
| hi | **2:58.7** (178.7 s, 9 VO lines) | Harsh `HTUuC7OeeEt6OL5fViVe` — standard Hindi, **not** Haryanvi; on-screen text stays English | Har Saal ₹24,564 Chup-Chaap Gayab — Aapke Subscriptions Ka Sach |
| en | **2:49.6** (169.6 s, 9 VO lines) | Brian `nPczCjzI2devNBz1zQrb` — a US rewrite, never a translation | You Think You Spend $86 a Month on Subscriptions. It's $219. |

Same skeleton and the same element IDs across both cuts so fixes port; s1/s5/s7
deliberately diverge — 42% stat strip · iPhone-PayPal audit · the $86→$219→$133
gap table ([[storyboard-en]]).

> Correction (2026-07-29, read off the archived `gen_vo_hi.sh`): the Hindi voice was
> **Harsh**, the same ID 50-30-20-rule used. [[script-hi]]'s frontmatter still says
> "Vikram S" — that is stale; the shipped audio is Harsh.

## Hero numbers

- **hi** — an itemised **₹2,047/mo** stack → **₹24,564/yr** → **25 days** of a
  ₹30,000 in-hand salary.
- **en** — claimed-vs-real **$86 → $219/mo**, a **$133/mo** gap → **$1,596/yr** →
  **12 days** of a $4,000 take-home.

Sourced from [[../../knowledge/subscription-economics-2026]].

## What this build contributed to the system

- **Colour semantics, still in force:** wants = **amber**, never red. **Red is
  reserved for the leak itself.** The `.bill` / `.decision` CSS was introduced here.
- **Render rule born here:** `-q high --video-bitrate 12M` — the upload master came
  out at 12.3 Mbps. Recorded in [[storyboard-hi]].
- 11 Pixabay photo slots; the design system was inherited from emergency-fund.

## Packaging findings (read before judging the analytics)

- **hi** — the browse-not-search finding, and why `auto debit kaise band kare` (a
  376k lane) is a **trap**: it's all PhonePe click-path tutorials, i.e. the wrong
  intent entirely.
- **en** — the lane is unclaimed but **demand-limited**: every competitor is sub-10k
  and Ramsey's own EveryDollar entry got 1,517. **Low views here are the expected
  default, not evidence of a bad video.**

## Published + archived (2026-07-29)

**State: LIVE on YouTube (both cuts) · source archived · studio dir deleted.**

| Cut | Channel | URL | Thumbnail |
|---|---|---|---|
| hi | @cashguruguides | https://youtu.be/I9cxxhcdfg0 | `src/hi/thumbnail-hi.png` (single) |
| en | @moneymavens101 | https://youtu.be/4DimmIqnxSM | `src/en/thumbnail-en.png` (single) |

**Source: `src/{hi,en,thumbs}/`** — composition, meta/package JSON, `gen_vo_*.sh`, the
18 VO lines (`assets/voice/*.txt`), stock CREDITS and the thumbnail PNGs.
`studio/videos/needs-vs-wants*` is **deleted** per the finished-video rule
([[../../CLAUDE]]).

⚠️ **Predates the `.src` image-prompt convention — no `assets/img/*.src` in this
archive.** The VO is fully reproducible (lines + voice ID + `gen_vo_*.sh`); the 11
Pixabay photo slots are **not** — re-sourcing them means working from
[[storyboard-hi]] / [[storyboard-en]] and the stock CREDITS, not from a prompt file.

Still owed:
- **analytics after 28 days** (only then may anything here touch
  [[../../knowledge/best-practices]])

Related: [[script-hi]] · [[script-en]] · [[storyboard-hi]] · [[storyboard-en]] ·
[[youtube-metadata-hi]] · [[youtube-metadata-en]] · [[../emergency-fund/index]] ·
[[../../knowledge/channels]]
