---
summary: fin-audit log, cut en, attempt 2 (style-E restyle, 81 lines). Verdict PASS with two edits to script-en.md — VO line 4.8 (tank analogy misdescribing what Bengen and Trinity tested) and scene 1.2's third chip (27 chars against a 22-char cap). Chapters 1-2 verified verbatim against the creator-approved draft; 14/14 corpus lines speak their rate; every load-bearing source re-fetched, two read as primary PDFs. One item could not be settled from text and is pre-registered for measurement: the hook gate.
updated: 2026-08-07
source: script-en.md (attempt 2) · facts-staging.md · run.json · style-E-en-teacher-curiosity.txt · tools/format.json · re-fetched source URLs
stage: fin-audit, cut en, attempt 2
---

# fin-audit log — passive-income-number, cut `en`, attempt 2

**Verdict: PASS** (with two edits). Full evidence: `vault/videos/passive-income-number/audit-en.md`.

## What was done

Audited the restyled file from scratch. Attempt 1's `audit-en.md` was replaced, not amended —
its line numbering does not survive the restyle (its 5.6 is this file's 5.7, its 2.11 is this
file's 2.13) and its chapters 1–2 no longer exist as prose. The one thing carried forward was
the instruction not to re-litigate Bengen's `pp. 171–180`; it was not re-litigated.

## Re-fetches performed at this stage (independence rule)

| Source | Result |
|---|---|
| `aaii.com/journal/199802/feature.pdf` | **Read as a 6-page PDF, primary.** Authors, title, AAII Journal Feb 1998, pp. 16–21, Table 3's 95/95 at 4% over 30 years, and both verbatim quotations (taxes/costs; early retirees) confirmed on the artefact |
| `obj.portfolioconstructionforum.edu.au/…pdf` | **Read as a 2-page PDF.** Bengen, JFP October 1994, 50/50, retirement years 1926–1966, worst case ≈30 years (1976 retiree) |
| `multpl.com/s-p-500-dividend-yield` + `/table/by-month` | 1.04% current · mean 4.21 · median 4.19 · max 13.84% June 1932 · min 1.08% July 2026 · series starts **Jan 1871** (fetched the table to confirm the one spoken date) |
| `retirementresearcher.com/…4-rule/` | Pfau, JFP Dec 2010, 50/50 stocks-bills, SAFEMAX = worst-case (so the foot's "zero tolerated failure" is right), Japan 0.26%, 19 countries |
| `keilfp.com/blogpodcast/morningstar-safe-withdrawal-rate/` | 3.9% for a 2026 retiree, 2025 Edition pub. 3 Dec 2025, 30-yr, 90%, 30–50% equity, up from 3.7% |
| `stockanalysis.com/etf/schd/dividend/` | **3.09% today vs the staged 3.11%** — a dated 2bp drift on a live TTM yield; recorded, not killed (VO says only "about three percent") |
| `fool.com/…withdraw-more/` + publisher search | Bengen 4.7% "Safemax", *A Richer Retirement*, ~400 start dates, 55/40/5 mix; **Wiley, 5 Aug 2025 confirmed** (attempt 1 had to retain this on trust) |
| BLS | bls.gov 403'd three ways (TED, news release HTML, news release PDF). The whole 2024 CE set — 78,535 / 26,266 / 13,318 / 10,169 / ~33% / ~17% / ~50% — confirmed on `randalolson.com` plus BLS's own X post via search |

Every corpus quotient re-derived by hand; all exact to the dollar.

## Edits made to `script-en.md`

1. **4.8 (VO + cue).** *"The papers tested how fast a tank drains…"* → *"The papers tested how
   long a tank lasts at each rate…"*. The shipped line attributed a no-inflow model to the two
   papers and contradicted the script's own 2.8 (*"four percent survived ninety-five percent of
   the periods"*). Cue `stmt:` moved with it. 76 → 88 chars.
2. **1.2 (cue only).** Chip `No reminder of what you owe` (27) → `No debt reminder` (16),
   `layout.max_chip_chars` is 22. The VO line, which is creator-approved verbatim, is untouched.

Derived char tables updated for the +12: 8,002 → **8,014**, +2.5% against the padding-corrected
budget of 7,822. Chapter starts after ch4 shift ≈ +0.7s and must be regenerated from measured
audio, which build handoff 3 already requires.

## Flagged to downstream, not blocking

1. **Hook gate — pre-register and MEASURE.** On the flat 17.57 c/s model the promise clause
   opens ≈10.9s and closes ≈13.0s. But chapter 1 is punctuation-dense (1.2 is three sentences
   in 75 chars) and `tts.pause_seconds` buys real silence the flat key averages away; on a
   pause-loaded reading the line closes ≈15.5s. This is exactly how `hook_gate_hi` landed at
   14.9–15.1s. 1.1–1.3 are creator-approved verbatim so no script fix exists. **fin-voice must
   ffprobe the rendered 1.3 clip and record `hook_gate_en` in run.json before ch1 locks.**
2. **Scene 2.2's two `data-framings` are binding** — 9.6s over a 9.0s ceiling, mitigated by two
   framings, not by an exemption. `check_build` fails the scene if the second framing is absent.
3. **3.3's 4-item cascade must render 2 + 2 rows** (`max_chips_per_row` 3; `.row` wraps 3+1
   silently). **3.7** must set `$2,189` at sub weight under the focal `33.4%`.
4. **`storyboard-en.md` is attempt-1/style-A and must be regenerated, not patched.**
5. **The 5.14 quintile range** (`$35,046 → $150,342`, screen-only) is the one figure no surface
   would serve this stage. Drop that sentence from the foot if the build cannot re-confirm it.

## Spend

Zero ElevenLabs calls. Both edits land before TTS, and fin-voice was re-running all 81 clips
regardless, so the corrections cost nothing.
