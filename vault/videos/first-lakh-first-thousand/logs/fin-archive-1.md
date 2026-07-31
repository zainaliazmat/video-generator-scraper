# fin-archive — first-lakh-first-thousand · attempt 1

**Date:** 2026-07-31 · **Result:** ok · Close-out only. **No archive, no deletion.**

## Scope decision, stated first

Neither cut has a YouTube URL, so per the finished-video rule in `vault/CLAUDE.md` this
video is **not finished**. `tools/archive_cut.py` was **not run**; nothing under
`studio/` was touched or deleted. `studio/videos/first-lakh-first-thousand-{hi,en,thumbs}`
are all intact. Post-delivery cleanup runs after upload, on the creator's word.

This note is therefore a **milestone note, not a `## Published + archived` section** —
that section gets written by `archive_cut.py` when the URLs land.

## Inputs read

- `vault/CLAUDE.md` (read first), `vault/index.md`
- `vault/videos/first-lakh-first-thousand/run.json` (18 stages, all `done`; the three
  `owed_*` keys), `facts-staging.md`, `youtube-metadata-{hi,en}.md`
- `logs/fin-render-hi-4.md`, `logs/fin-render-en-3.md` (the QA numbers),
  `logs/fin-package-{hi,en}-1.md`, `logs/fin-build-hi-2.md`, `logs/fin-assets-en-3.md`,
  `logs/fin-voice-hi-1.md`
- Format reference: `vault/videos/credit-history/index.md`
- Prior-run `chosen:` readback: `vault/videos/{pay-yourself-first,credit-history}/youtube-metadata-{hi,en}.md`

## Writes made

1. `vault/videos/first-lakh-first-thousand/index.md` — **new file**, nothing overwritten
   (the directory held no `index.md` before this run). Carries: both cuts + runtimes +
   voices + scene counts + titles + thumbnails, hero numbers with HARD/SOFT sourcing, the
   render-log QA table, the five tier-scaling defects found and fixed, the 1:1 image
   lesson with its measured root cause, gate two's measured legibility standard, the s57
   post-dissolve sampling trap, the prior-run `chosen:` readback table, current state and
   the owed list.
2. `vault/index.md` — three catalog lines (milestone + both publish packs), frontmatter
   `updated` → 2026-07-31.
3. This log.

## Thumbnail readback (procedure step 3)

| Pack | `chosen:` | Action |
|---|---|---|
| pay-yourself-first hi / en | blank | none possible — no network here; recoverable off the live thumbnail, left owed |
| good-debt-vs-bad-debt hi / en | `v2` (creator, 2026-07-29) | already recorded in that milestone note — no edit needed |
| credit-history hi / en | blank | same as pay-yourself-first; already recorded as owed there |
| **this pair hi / en** | `v2` / `v2` (by construction) | recorded in the new milestone note |

**No prior milestone note was edited** — nothing was newly filled since credit-history's
close-out, so there was nothing to write back.

## Constraints honoured

- **Nothing written to `vault/knowledge/best-practices.md`** — this video has 0 days of
  analytics. Every transferable observation lives in the milestone note, and the ones that
  are performance claims rather than measurements are tagged
  `unvalidated — no analytics yet`.
- **Nothing written to `vault/knowledge/money-facts-2026.md`** — fact promotion is the
  orchestrator's step and was already done this run.
- No `.env` read. No `.claude/` or `tools/` write. No Bash, no git. No deletions.
