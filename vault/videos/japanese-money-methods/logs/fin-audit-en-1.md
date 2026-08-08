---
summary: Run log for fin-audit, cut en, attempt 1 — japanese-money-methods. PASS after six direct edits to script-en.md. One staged US figure (G.19 card APR, "22.15% Q2 2026") did not survive re-fetch and was killed; the two Horioka qualifier errors WERE inherited by this cut, contrary to the handoff note. Verdict and full reasoning in audit-en.md.
updated: 2026-08-01
stage: fin-audit, cut en, attempt 1
---

# fin-audit-en-1

**Verdict: PASS (after edits).** Artifact: `vault/videos/japanese-money-methods/audit-en.md`.

## Inputs read

- `vault/CLAUDE.md`, `tools/format.json`
- `vault/videos/japanese-money-methods/run.json` (LONG, 660s, ledger-rail, premise_correction)
- `vault/videos/japanese-money-methods/facts-staging.md` (reference only — not used as grading evidence)
- `vault/videos/japanese-money-methods/audit-hi.md` + `logs/fin-audit-hi-1.md` (prior-cut precedent)
- `vault/videos/japanese-money-methods/script-en.md` (882 lines, 92 VO lines)

## Independence re-fetch

Re-fetched every recorded source behind a load-bearing number rather than trusting
`facts-staging.md`. The three primaries returned raw PDF binary through the fetch tool and
were then read **as PDFs, page by page**.

| Source | Pages read | What it settled |
|---|---|---|
| Horioka, NBER WP 33181 | abstract + body pp. 1–7 | 1.1% (2024), 23.2% postwar peak, 44% wartime, the postwar restriction on 1961–86, the 2020 Covid carve-out, 37.8% FIES, "more than 30 times as high", culture rejected §3, the five drivers |
| Statistics Bureau FIES 2024 summary | pp. 8–11 | 黒字率 37.8, 平均消費性向 62.2, ¥636,155 / ¥522,569 / ¥325,137 / ¥197,432, 預貯金純増 ¥175,241, 有価証券純購入 ¥6,705 |
| BOJ Flow of Funds overview | pp. 1–4 (Chart 2) | Japan 51.0% cash / 12.2% equity of ¥2,195tn; US 11.5% cash / 41.5% equity of $128.8tn; end-March 2025 |
| Federal Reserve G.19, current release | terms-of-credit table | rel. 8 Jul 2026, ref. month May 2026: 2026 Q1 and Q2 **n.a.**; latest = **21.52% (2025 Q4)** |
| Federal Reserve SHED 2025 | press release 13 May 2026 | 63% **of adults** would cover a $400 emergency with cash or its equivalent |
| Census P60-286 | summary | real median household income $83,730 (2024), issued Sept 2025 |
| Fujin no Tomo Sha 120th page | full | 1904 first edition, Hani Motoko, 4-year wartime paper-rationing gap, the 予算 / divide-by-twelve-savings-first idea |
| Wikipedia — Tsukubai, Mottainai | full | 吾唯足知 read with the central 口; mottainai = regret at full value unused, 13th-century attestation |

**One number did not survive: the G.19 card APR.** `facts-staging.md` U7's "22.15%, Q2 2026"
does not exist in the source — G.19 has published nothing for 2026 Q1 or Q2. This is exactly
the plausible-dated-line failure the independence rule is written for, and grading against
the staging text alone would have shipped it.

## Edits made to script-en.md

| Line | Check | Change |
|---|---|---|
| **1.2** | 3 — 15s promise gate | Rewritten to carry the three-methods promise at ≈8.7–13.2s. The draft deferred every promise to 2.1 at 0:59 and failed the gate outright. |
| **1.5** | 4 — named platform | "two DoorDash orders" → "two food delivery orders". A platform name that is not price evidence; the scene's own screen cue was already generic. |
| **3.8** | 1 — source doesn't back it | Prefixed "After the war". Horioka p.3 restricts the 1961–86 exclusivity to the postwar period; p.2 records 44% during WWII. **Inherited from the pre-correction J6 despite the handoff note.** |
| **3.9** | 1 — source doesn't back it | "peaked" → "postwar peak", "has not been above five percent" → "hardly ever been above five percent". Horioka p.2 carves out the 2020 Covid blip the absolute denied. **Also inherited.** |
| **5.7** | 4, 7 — monetisation | Rewritten so the set-aside is not routed into a product category. `HIGH-YIELD SAVINGS · FDIC INSURED · A DIFFERENT BANK` removed from screen. Mechanic (automate + separate) unchanged. |
| **6.14** | 1 — fabricated date | Screen only. `ABOUT 22%` → `OVER 20%`; foot now cites 21.52% (2025 Q4) and the 8 Jul 2026 release. VO ("over twenty percent") was already true and is unchanged. |
| **6.15** | 1 — wrong unit | "four in ten households" → "four in ten adults". SHED reports a share of adults. |

Derived values updated to match: frontmatter, chapter table, timing-budget table, two-rate
hedge table, per-scene char table (1.2, 1.5, 3.8, 3.9, 5.7, 6.15), pace line, retention-beat
bullets, the Chapter 1 and Chapter 6 notes, three fact-trace rows, the "Deliberately NOT
used" list and build handoff §4. Char total **9,581 → 9,619** (+1.9% of the 9,441 budget,
was +1.5%). Each edited line carries an inline `[… AUDIT fin-audit-en-1: …]` field in its cue
recording the reason.

## Checks passed without edit

2 (char budget, +1.9%) · 5 (zero `₹`, `$` correct, no `¥` glyph) · 6 (no cite refs; no bare
Latin digit in any of the 92 VO lines) · 7 (no first person, no persona, no picks post-edit) ·
8 (one focal element per scene across all 92 cues; cue gaps clear 0.8s; longest scene 8.8s;
colour table thesis-consistent).

## Flagged for build, not script defects

1. The pre-script warning blockquote is `>`-prefixed and contains Latin digits — extraction
   must key off `**N.N**` markers and land exactly 92 entries.
2. `·`-separated `stmt:` strings at 3.11 and 6.10 must render as wrapped statement lines, not
   chip rows, or they breach `max_chips_per_row` / `max_chip_chars`.
3. The six `AUDIT fin-audit-en-1:` cue fields are annotations — strip them from scene content.
4. Build handoff §2 still says `max_elevenlabs_calls` is 30; run.json now carries 221. Stale
   prose only.

## Owed upstream

`facts-staging.md` **U7 must not be promoted** to `money-facts-2026.md` as written — there is
no Q2 2026 G.19 print and no 22.15%. The correct carried row is 21.52% for 2025 Q4, latest as
of the 8 July 2026 release. Not edited here: `facts-staging.md` is fin-facts' artifact and
this stage writes the audit, but the orchestrator must not promote that row.

## Budget

No ElevenLabs calls. No writes outside `vault/videos/japanese-money-methods/`. `.env` not
read; `.claude/` and `tools/` not written; no Bash, no git.
