---
summary: The /finance-video pipeline — one topic in, one rendered US-English/$ video (@moneymavens101) out, with a thumbnail and a researched publish pack. US-only since 2026-08-15 (the Hindi/₹ cut and @cashguruguides are retired). Eleven fin-* agents own judgment; scripts in tools/ own mechanics; pipeline_check.py is the only thing that can mark a stage done.
updated: 2026-08-15
source: docs/superpowers/specs/2026-07-27-finance-video-agent-pipeline-design.md (spec + 5 review rounds, 24/24 consensus) — this note is the human-facing operating doc
stage: ADOPTED — the human doc for /finance-video
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
studio/videos/<slug>-en/renders/PUBLISH-1080p-en.mp4   (the upload)
studio/videos/<slug>-en/renders/captions-en.srt        (the subtitles)
studio/videos/<slug>-thumbs/thumbnail-en.png           (ONE, not variants)
vault/videos/<slug>/   script, audit, storyboard, publish pack, narration-en.md,
                       run.json, logs/
```

One cut, one channel: **@moneymavens101, US/$**. It is written for the US market
from the start — $ figures, US institutions, US shocks, Brian voice — never a
translation of anything ([[knowledge/us-english-script-style]]).

## The moving parts (one home per fact)

| Piece | Home |
|---|---|
| Machine constants (voices, rates, tiers, ladder, caps) | `tools/format.json` |
| Stage postconditions + run.json writer + doctor | `tools/pipeline_check.py` |
| TTS batch → measured `timing.json` | `tools/tts/batch.py` |
| Stock images (query-keyed skip, incremental credits) | `tools/stock/pixabay_fetch.py` |
| Stock Lottie: search + contact sheet, download + re-tint | `tools/lottie/{search,tint}.py` — [[knowledge/design-icons-emoji-lottie]] |
| SFX cue lists, mix, loudness, cue proof | `tools/audio/{cues,mix,verify_cues}.py` — [[knowledge/design-chapter-sound]] |
| YouTube captions + narration file | `tools/transcript.py` (see below) |
| What counts as proof at any stage | [[knowledge/evidence-discipline]] |
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
  [[knowledge/money-facts-2026]] **after** the render passes. A bad run is one
  `git revert` of explicit paths (`tools/vault_commit.py`).
- Fetched pages, transcripts and autocomplete are treated as untrusted data in
  every agent that touches them; no agent reads `.env` or writes `.claude/`.

## Still human (owed after every run)

Proof-listen · thumbnail pick (write it into the pack's `chosen:`
line) · upload · analytics after 28 days — `fin-archive` may not write
[[knowledge/best-practices]] until those analytics exist.


## The chapter review loop (standing since 2026-08-05)

Everything visual is built and reviewed **one chapter at a time**. A full 1080p
render is 30–40 minutes; a chapter draft is ~3 and shows the same mistake.

Per chapter: `fin-assets` → `fin-build` → `hyperframes check` → draft render +
contact sheet → `fin-editor` → `fin-ceo` → lock. The pipeline does not stop
between chapters.

When every chapter of a cut is locked you get **two artifacts, together**:

| artifact | what it is |
|---|---|
| `studio/videos/<slug>-<cut>-FRAMES.png` | one numbered PNG, every reviewable frame — `tools/frames_sheet.py` |
| `studio/videos/<slug>-<cut>-PREVIEW.mp4` | all chapters concatenated, stream-copy |

**The numbering is the protocol.** Reply with frame numbers — *"#7 and #12 are
wrong"* — and each resolves to exactly one frame. Numbers are stable across fix rounds.

Two things about the preview that are expected, not defects: the chapter joints
are **hard cuts** (the cross-dissolve only returns in the full assembly), and its
duration runs a few hundredths long because it joins separately-encoded files.

The look itself — four archetypes, the plate, the ground temperature arc, the
photograph rules — is [[../knowledge/design-chapter-archetypes]].

### Closing the loop — chapters back into ONE master

The preview is never the deliverable. When the chapters are locked:

```bash
python3 tools/audio/cues.py studio/videos/<slug>-<cut>-ch<N> --write   # per chapter
python3 tools/cut_assemble.py <slug> --cut <cut>                       # prints the rest
```

`cut_assemble.py` writes `studio/videos/<slug>-<cut>-full/index.html` — all
scenes in one composition, each chapter's `+0.45s` cross-dissolve overlap
restored, so the seven joints are real dissolves — plus the merged full-cut
`audio.json`. It then prints the render → mix → loudnorm → verify → check chain
to run. **`FFMPEG_ENCODE_TIMEOUT_MS` in that printed command is load-bearing**:
the default kills a full-length encode two thirds of the way through and writes
no file.

Two checks that are worth the minutes, because neither the log nor
`hyperframes check` can tell you:

- `tools/audio/verify_cues.py <MIXED>` — builds an identical mix with the cue
  list emptied and subtracts, so every cue is proven present in the *encode*.
  About half will read "masked by speech"; that is the design, not a fault.
- `hyperframes check` **cannot pass on a full-length archetype master** — its
  navigation budget is 10s and the page needs ~29s. Lint still matters; judge
  the picture from the encode.

### Captions — standing since 2026-08-06

**Every video now ships subtitles.** Creator rule: YouTube must be able to show
the narration text on the video.

```bash
python3 tools/transcript.py <slug> --cut en
```

Writes two files:

- `studio/videos/<slug>-<cut>/renders/captions-<cut>.srt` — **the upload.**
  YouTube Studio → the video → Subtitles → Add language → *Upload file* →
  **With timing**.
- `vault/videos/<slug>/narration-<cut>.md` — the readable narration, chapter
  headed with real timestamps, plus a no-timecode transcript block at the foot
  for YouTube's auto-sync path if the .srt is ever not used.

**It is a JOIN, never a retype** — the same rule as the TTS stage. Line text
comes from `script-<cut>.md` (the `**N.M**` / `> line` blocks) and the times come
from the shipped composition's own `<audio data-start>` / `data-duration`, keyed
on the VO line id. So a cue cannot drift from its clip, and mismatched ids are a
hard error rather than a silent partial file. Run it **after** the cut is
rendered, and re-run it if a line is ever re-recorded.

Cues are split at a clause boundary when a line exceeds 84 characters, because
YouTube renders at most two ~42-character lines; the split shares the line's
duration by character count. Verify with the tool's own numbers — 0 overlong,
0 out-of-order, and a final cue that lands inside the runtime.
