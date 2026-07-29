---
summary: fin-archive credit-history · attempt 1 · STATUS ok. Milestone note written (both cuts, hero numbers + sources, QA from both render logs, the 10 run findings, owed list); vault/index.md catalog extended with 7 lines; prior-run `chosen:` lines read back — all six blank, but pay-yourself-first-en carries a creator title pick + a v4 thumbnail, recorded in that milestone note along with the read-it-off-the-live-video recovery mechanism. Nothing written to best-practices.md or money-facts-2026.md; nothing deleted.
updated: 2026-07-29
source: vault/CLAUDE.md · vault/videos/credit-history/{run.json,facts-staging.md,script-hi.md,script-en.md,storyboard-hi.md,storyboard-en.md,youtube-metadata-hi.md,youtube-metadata-en.md} · logs/{fin-render-hi-2,fin-render-en-2,fin-package-hi-1,fin-package-en-1,fin-assets-hi-1,fin-assets-en-1}.md · vault/videos/{pay-yourself-first,good-debt-vs-bad-debt}/{index.md,youtube-metadata-hi.md,youtube-metadata-en.md} · Glob of studio/videos/*-thumbs/*.png
---

# fin-archive — credit-history · attempt 1

**Result: `STATUS: ok`.**

## Artifacts written

| File | What |
|---|---|
| `vault/videos/credit-history/index.md` | **new** milestone note |
| `vault/index.md` | +7 catalog lines (index · 2 packs · 2 scripts · 2 storyboards), inserted at the top of `## Videos` |
| `vault/videos/pay-yourself-first/index.md` | thumbnail-loop readback: `chosen:` survived a live upload blank; creator title pick (option 8) + `thumbnail-en-v4.png` recorded; owed item rewritten from "fill the field" to "recover it off the live video" |
| `vault/videos/good-debt-vs-bad-debt/index.md` | one block: its "the NEXT cut MUST change architecture" instruction did not hold — records what happened and points at the diagnosis |
| `vault/videos/credit-history/logs/fin-archive-1.md` | this log |

## Verification done rather than assumed

- **Runtimes, drift, peaks, loudness, black scans, frame counts** taken from
  `fin-render-hi-2.md` and `fin-render-en-2.md` directly, not from run.json.
- **`fin-render-en-2.md` is invocation 2 of attempt 1, not a failed attempt** — stated in
  the milestone note so nobody later reads the en cut as a rework. The log says so itself.
- **Pixabay counts** taken from the two fin-assets logs (hi 14/20 over 4 rounds, en 11/30
  over 6) because `run.json`'s `budget.pixabay_calls: 0` is stale.
- **`chosen:` read back from all four prior packs** (pay-yourself-first hi/en, good-debt
  hi/en) by opening the files — **all four blank**, plus both of this run's = six.
  pay-yourself-first was uploaded 2026-07-28, so the field is proven not to work.
- **`thumbnail-en-v4.png` confirmed on disk** by Glob before recording it.

## Deliberately NOT done

- **No write to `vault/knowledge/best-practices.md`.** Zero of this run's learnings have
  28 days of analytics behind them. Every transferable observation is in the milestone
  note instead, and the audience-response ones carry `unvalidated — no analytics yet`.
- **No write to `vault/knowledge/money-facts-2026.md`** — fact promotion from staging is
  the orchestrator's step, and it already ran this run (incl. the CICRA "Do not claim").
- **Nothing deleted.** Renders, audio, frames and assets stay until upload, on the
  creator's word (`vault/CLAUDE.md` post-delivery cleanup).
- **No `.claude/` or `tools/` writes**, so the two code-level fixes this run earned (the
  `$-N`/`₹-N` → `US-N`/`IN-N` claim-ID rename in fin-facts, and moving the architecture
  control to `tier` in `run.json`) are recorded as **owed to the orchestrator**, not made.
- **Thumbnail-pick recovery not run** — it needs the live YouTube thumbnails and this
  stage has no network access. Mechanism + the two live URLs are recorded in the
  pay-yourself-first milestone note so it can be done in one pass by anyone who can open
  them.

## What is flagged as owed (the full list lives in the milestone note)

proof-listen (hi, en) · thumbnail pick — **and recovery of the two pay-yourself-first
picks off the live videos** · upload + record URL/date · analytics after 28 days ·
**architecture decision in the next `run.json` before scripting (the 6th blockframe-9
happened after three written warnings — the control fires too late)** · finance-lane
scrape into `library.db` (2nd rescue) · promote `loudnorm I=-14:TP=-1` to standard
(en peaks at −3.00 dBTP straight from `en1.mp3`) · rename the facts-staging claim-ID
convention · storyboard queries as 1–3 nouns · fix the `#s5ctr` mitigation text in the
en build notes (the seal is illegible from the grade + bottom-edge crop, **not** covered
by the counter).
