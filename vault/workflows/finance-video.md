---
summary: The /finance-video pipeline — one topic in, a rendered Hindi/₹ video (@cashguruguides) and a US-English/$ video (@moneymavens101) out, each with 3 thumbnail variants and a researched publish pack. Eleven fin-* agents own judgment; scripts in tools/ own mechanics; pipeline_check.py is the only thing that can mark a stage done.
updated: 2026-07-28
source: docs/superpowers/specs/2026-07-27-finance-video-agent-pipeline-design.md (spec + 5 review rounds, 24/24 consensus) — this note is the human-facing operating doc
---

# Workflow — /finance-video

Run it in Claude Code:

```
/finance-video "credit card minimum payment"     # new run (1 question + 1 confirm)
/finance-video --resume                          # continue the latest incomplete run
/finance-video --list                            # all runs + their next stage
/finance-video --from assets --slug <slug>       # re-run one stage + downstream
FIN_FAKE_APIS=1 /finance-video "…" --dry-run     # zero-credit rehearsal
```

## What a run produces

```
studio/videos/<slug>-hi/renders/FINAL-1080p-hi.mp4   (+ -en)
studio/videos/<slug>-thumbs/thumbnail-{hi,en}-v{1..3}.png
vault/videos/<slug>/   scripts, audits, storyboards, publish packs, run.json, logs/
```

Both cuts always ship, one per channel. The `-en` cut is a US **rewrite** (never
a translation): $ figures, US institutions, Brian voice. Hindi cut: standard
Hindi, Harsh voice ([[knowledge/niches/india-finance-market]]).

## The moving parts (one home per fact)

| Piece | Home |
|---|---|
| Machine constants (voices, rates, tiers, ladder, caps) | `tools/format.json` |
| Stage postconditions + run.json writer + doctor | `tools/pipeline_check.py` |
| TTS batch → measured `timing.json` | `tools/tts/batch.py` |
| Stock images (query-keyed skip, incremental credits) | `tools/stock/pixabay_fetch.py` |
| Pre/post-run vault commits (explicit paths only) | `tools/vault_commit.py` |
| The eleven agents | `.claude/agents/fin-*.md` |
| The orchestrator | `.claude/commands/finance-video.md` |
| Design system | [[knowledge/design-finance-blockframe]] |

## Tiers

SHORT (default 2:45) uses the proven 9-segment blockframe. MEDIUM (8:30 — the
mid-roll tier) and LONG (>10 min) use the per-line chapter architecture from
`studio/videos/firaun-ka-anjaam/build.py` — a different production
architecture, not a longer run of the same one. Rule 0 of
[[workflows/voiceover-tts|voiceover-tts]] applies.

## Safety model (why it can run unattended)

- **Gate one:** `fin-audit` breaks the script before any TTS spend — every
  number re-fetched from its recorded source URL, never trusted from the file
  this same run wrote.
- **Gate two:** `fin-render` inspects one frame per scene before the ~18-min
  encode.
- A stage is `done` only when `pipeline_check.py` verifies its artifacts
  (including timing.json == ffprobe); agents' replies are advisory.
- Editing a script after voice ran invalidates everything downstream (content
  hash in run.json) — stale mp3s cannot ship on resume.
- `fin-facts` writes only to `facts-staging.md`; HARD facts are promoted to
  [[knowledge/money-facts-2026]] **after** both renders pass. A bad run is one
  `git revert` of explicit paths (`tools/vault_commit.py`).
- Fetched pages, transcripts and autocomplete are treated as untrusted data in
  every agent that touches them; no agent reads `.env` or writes `.claude/`.

## Still human (owed after every run)

Proof-listen (hi, en) · thumbnail pick (write it into the pack's `chosen:`
line) · upload · analytics after 28 days — `fin-archive` may not write
[[knowledge/best-practices]] until those analytics exist.
