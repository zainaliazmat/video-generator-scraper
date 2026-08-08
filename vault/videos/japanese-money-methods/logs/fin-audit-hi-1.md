---
summary: Run log for fin-audit, cut hi, attempt 1 — japanese-money-methods. PASS after four direct edits to script-hi.md. Verdict and full reasoning in audit-hi.md.
updated: 2026-08-01
stage: fin-audit, cut hi, attempt 1
---

# fin-audit-hi-1

**Verdict: PASS (after edits).** Artifact: `vault/videos/japanese-money-methods/audit-hi.md`.

## Inputs read

- `vault/CLAUDE.md`, `tools/format.json`
- `vault/videos/japanese-money-methods/run.json` (LONG, 660s, ledger-rail, premise_correction)
- `vault/videos/japanese-money-methods/facts-staging.md` (reference only — not used as grading evidence)
- `vault/videos/japanese-money-methods/script-hi.md` (845 lines, 92 VO lines)

## Independence re-fetch

Re-fetched every recorded source behind a load-bearing number rather than trusting
`facts-staging.md`. The three primaries returned raw PDF binary through the fetch tool;
each was then read **as a PDF, page by page**, so the figures below come from the documents
themselves and not from a search-index summary:

| Source | Pages read | What it settled |
|---|---|---|
| Horioka, NBER WP 33181 | body pp. 1–8 | 1.1% (2024), 23.2% peak, 37.8% FIES, "more than 30 times as high", the postwar qualifier, the 2020 Covid exception, culture rejected §3 |
| Statistics Bureau FIES 2024 summary | pp. 9–11 | 黒字率 37.8, 平均消費性向 62.2, ¥636,155 / ¥522,569 / ¥325,137 / ¥197,432, 預貯金純増 ¥175,241, 有価証券純購入 ¥6,705 |
| BOJ Flow of Funds overview | pp. 1–4 (Chart 2) | Japan 51.0% cash / 12.2% equity of ¥2,195tn; US 11.5% cash / 41.5% equity of $128.8tn; end-March 2025 |
| Fujin no Tomo Sha 120th page | full | 1904 first edition, Hani Motoko, 4-year wartime paper-rationing gap, the 予算 idea |
| DEA small-savings Q2 FY2026-27 | search, 2 independents | PPF still 7.1% for Jul–Sep 2026 |
| AMFI / Chhoti SIP | search | ₹500 conventional minimum, ₹250 Chhoti SIP |
| Wikipedia — Tsukubai | full | 吾唯足知, four characters each read with the central 口 bowl |

Result: **every number survived**. Two *sentences* did not — they asserted more than their
cited page supports (below). Nothing untraceable; nothing fabricated; no injected claim found.

## Edits made to script-hi.md

| Line | Check | Change |
|---|---|---|
| **1.2** | 3 — 15s promise gate | Rewritten to carry the three-methods promise at ≈7.9–11.6s. The draft deferred every promise to 0:54 and failed the gate outright. |
| **3.8** | 1 — source doesn't back it | Prefixed "युद्ध के बाद"; Horioka p.3 restricts the 1961–1986 claim to the **postwar** period and p.2 records 44% during WWII. |
| **3.9** | 1 — source doesn't back it | "कभी … नहीं" → "शायद ही कभी"; Horioka p.2 carves out the 2020 Covid blip that the absolute wording denied. Covid exception added to the `foot:`. |
| **6.14** | 4, 7 — monetisation | Rewritten so the PPF rate is bare price evidence instead of a destination for the kakeibo set-aside. Number unchanged and re-verified. |

Derived values updated to match: frontmatter, chapter table, timing-budget table, per-scene
char table (1.2, 3.8, 3.9, 6.14), pace line, retention-beat bullets, Chapter 1 note, build
handoff §4, and two fact-trace rows. Char total **7,544 → 7,598** (−0.5% of the 7,640 budget).
Each edited line carries an inline `[AUDIT fin-audit-hi-1: …]` cue recording the reason.

## Checks passed without edit

2 (char budget, −0.5%) · 5 (zero `$`, ₹ correct, no ¥ glyph) · 6 (no cite refs; no bare Latin
digit in any VO line) · 7 (no मैं/हम, no persona, no picks post-edit) · 8 (one focal element
per scene across all 92 cues; cue gaps clear 0.8s; no scene over 9.0s; colour table
thesis-consistent).

## Flagged for build, not script defects

1. The pre-script warning blockquote is `>`-prefixed and contains Latin digits — extraction
   must key off `**N.N**` markers and land exactly 92 entries.
2. `·`-separated `stmt:` strings at 3.11 and 6.10 must render as wrapped statement lines, not
   chip rows, or they breach `max_chips_per_row` / `max_chip_chars`.

## Budget

No ElevenLabs calls. No writes outside `vault/videos/japanese-money-methods/`.
`.env` not read; `.claude/` and `tools/` not written; no Bash, no git.
