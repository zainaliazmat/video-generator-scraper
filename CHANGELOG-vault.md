# CHANGELOG — vault + pipeline shrink

Why this file exists: the vault went from 235,694 to 1,106,180 words in eleven days
(4.7×), and every stage of `/finance-video` reads part of it. This log records what
moved, what it saved, and what was measured rather than asserted. One entry per
change. **Nothing in this job is deleted — everything moves.**

Baseline, measured on `passive-income-number` (98 stage invocations, 2026-08-07 →
2026-08-09): **~5.72M standing context tokens per run**, of which `run.json` was 75%,
`tools/format.json` 9%, knowledge docs 12%, `vault/CLAUDE.md` 2%.

---

## 2026-08-09 — Phase 1 items 1 + 2

### Rescued: the one-line-per-scene rule (item 1a)

`.claude/agents/fin-script.md` cited `studio/videos/firaun-ka-anjaam/build.py` as the
authority for single-sentence VO lines. The rule already had two standing homes
(`vault/workflows/voiceover-tts.md` Rule 0, `vault/skills/long_form_scripting.md` §7),
so this was a stale pointer, not an orphaned rule. Repointed at Rule 0.

Same bug class, second and third instances — **both live and broken**:
`.claude/commands/finance-video.md` and `.claude/agents/fin-build.md` both cited
`studio/videos/japanese-money-methods-hi-ch{1,2}/index-claudedesign.html` as the
creator-approved archetype reference implementations. `archive_cut.py` deleted that
directory when japanese shipped. **`fin-build` had been reading a 404 on every run
since.** Repointed at the surviving copies under
`vault/videos/japanese-money-methods/src/hi-ch{1,2}/`.

Root cause closed: `pipeline_check.py dangling_studio_refs()`, wired into `doctor`, so
preflight fails if any `.claude/**/*.md` cites a `studio/videos/<slug>` path that does
not exist. Archived source always survives under `vault/videos/<slug>/src/`, so the fix
is always a repoint.

### `run.json` is state again (item 1e)

`run.json` had become the session notebook because narrative had nowhere else to live.
Measured on the 161 KB file: **54% chapter narrative, 31% top-level notebook
(`owed`, `incidents`, `tool_fixes_*`, `rulings_binding_on_both_cuts`), 16% actual
state.** `chapters.hi.2` alone carried 73 ad-hoc keys, twelve of them state. The
orchestrator re-read all of it at every stage transition and every `mark`.

`pipeline_check.py` gains `RUN_STATE_KEYS` / `CHAPTER_STATE_KEYS` and `drain_to_notes()`,
called from `mark()`. Anything off-schema — plus **any key starting with `_`, at any
depth**, a convention `run.json` already used and that had never meant anything — moves
to `vault/videos/<slug>/notes.md`, which nothing loads on a transition.

It drains rather than asserts. An assert would fail the stage *after* the orchestrator
had already written the key, punishing the run for something already done; draining
makes the wrong state unrepresentable and self-heals the existing file on first `mark()`.
That is the "correct default" rung of `fix-defaults-not-gates`, not the gate rung.

Ordering is copy → verify → delete, the same discipline as `archive_cut.py`: `notes.md`
is appended and fsynced before `run.json` is rewritten, because a drained ruling is the
only copy of something a CEO round arrived at.

```
run.json   161,001 → 11,775 b   (93%)   ~40,250 → ~2,940 tokens
notes.md   157,996 b, 321 blocks
loss       0 strings >40 chars, verified against git HEAD
```

`style_decision.what_style_E_is` hand-trimmed 664 → 410 chars: `fin-script` needs the
style's rules, not this video's illustrations, which live in `reference_scripts`. Full
text preserved in `notes.md` before the trim.

Every key another tool depends on survives: `check_vo_frame.py`'s
`constraints.derived_income_carries_assumption`, `recent_architectures()`'s
`architecture`, all 14 `stages`. `declared` was dropped from the chapter whitelist at
creator request.

Orchestrator (`.claude/commands/finance-video.md`) updated to match: `run.json` is state,
narrative goes to `notes.md`, and a chapter brief that needs a prior ruling quotes that
ONE ruling out of `notes.md` rather than parking it where fourteen transitions re-read it.

### The summary box became load-bearing (item 1b)

35 of 36 STANDING files already carried `summary:` frontmatter, so the convention was
not the problem — nothing read the box *instead of* the body. Five files carry 397k of
the 434k words the knowledge layer costs per run; each gained a **BOX** at the top: the
decisions one line each, and an explicit `Open the body when:` trigger.

The rule that makes a lossy box safe: **a box may only be lossy about things a script
also enforces.** `check_build` already enforces all four Lottie blank-render traps and
names the fix, so the box compresses them to one line. Judgment that no script checks
is carried in full.

| file | full | box | reads/run | before | after |
|---|---|---|---|---|---|
| design-chapter-archetypes.md | 3,472 w | 441 w | 41 | 142,352 | 32,236 |
| design-icons-emoji-lottie.md | 2,176 w | 322 w | 42 | 91,392 | 13,524 |
| design-finance-blockframe.md | 4,702 w | 550 w | 23 | 108,146 | 12,650 |
| stock-photo-sourcing.md | 3,228 w | 364 w | 23 | 74,244 | 8,372 |
| evidence-discipline.md | 1,826 w | 183 w | 16 | 29,216 | 2,928 |
| **total** | | | | **445,350 w** | **69,710 w** |

**`design-chapter-archetypes.md` refused a single box and routes instead.** Its eight
build gotchas each shipped past a *passing* check, so compressing them away would make
the vault smaller and dumber. Reviewers (`fin-editor`, `fin-ceo` — 22 reads) get the box
alone, −87%; `fin-build` (19 reads) gets box + the two sections it needs, −66%.

**`stock-photo-sourcing.md`'s box carries a supersession.** A 2026-08-09 correction in
that file records that the old "flat charcoal" mechanism was wrong and drove fetches for
two days — while the superseded reasoning still reads as current above it. The box now
states that the corrected mechanism wins over anything below reasoning from darkness.
This is exactly the disease item 1d exists to stop, occurring inside one file.

Six agent prompts changed from *read X* to *read X's box; open the body when its trigger
fires* — `fin-assets`, `fin-build`, `fin-editor`, `fin-ceo`, `fin-storyboard`, `fin-script`.

### Net

```
standing context per run   ~5.72M → ~1.5M tokens   (74%)
```

Verification: `pipeline_check.py --selftest` OK (new drain self-check included),
`doctor --tier medium` PASS, 31 backend tests pass.
