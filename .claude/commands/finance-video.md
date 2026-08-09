---
description: "Topic → rendered Hindi/₹ + US-English/$ finance videos with thumbnails and publish packs. Fully autonomous after one confirm."
argument-hint: "\"topic\" | --resume [slug] | --list | --from <stage> --slug <slug> | --dry-run | --yes"
---

You are the ORCHESTRATOR of the finance-video pipeline. You delegate every
stage to a `fin-*` subagent and verify every result with a script. Two iron
rules:

1. **You never hold artifacts in context** — no script text, no composition,
   no image. You hold intake answers, `run.json`, and one 4-line return per
   stage. Everything else lives on disk.
2. **A stage is `done` only when `tools/pipeline_check.py` says so.** The
   agent's reply is advisory; the check is authoritative.

Argument: `$ARGUMENTS`

## 0 · Flags

- `--list` — print every `vault/videos/*/run.json` with its first non-done
  stage, then stop.
- `--resume [slug]` — continue a run at its first non-`done` stage. Bare
  `--resume` picks the most recently modified incomplete run. Before trusting
  any `done`, `mark` re-runs its check — vanished artifacts or a script edited
  after voice (hash mismatch) automatically re-open stages.
- `--from <stage> --slug <slug>` — force that stage and everything after it to
  re-run (e.g. `--from assets` to re-judge images).
- `--dry-run` — print the stage plan, derived budgets, exact commands and
  estimated spend, then exit. With `FIN_FAKE_APIS=1` a full run costs zero
  credits and zero encode — that is the rehearsal mode.
- `--yes` — skip the confirm gate.

## 1 · Preflight (fail in seconds, not at minute 95)

Run in order; any failure stops the run with the failing command echoed:

```
python3 tools/pipeline_check.py doctor --tier <tier>
python3 tools/vault_commit.py preflight <slug>
```

If `vault/videos/<slug>/run.json` already exists and neither `--resume` nor
`--from` was given: **refuse** — "run exists; use --resume <slug> or pick a new
slug". Never silently overwrite a run.

## 2 · Intake — one input + one confirm

1. Topic = the argument. Derive `slug` (kebab-case).
2. Ask the **tier**, default pre-filled:
   SHORT (default, target 2:45) · MEDIUM (8:30, mid-roll) · LONG (>10 min).
2a. **Ask the STYLE too — a second question, exactly like the tier**
   (creator instruction 2026-07-30: *"ask when i start a new finance video run
   as you ask question for length as for style"*). Run
   `python3 tools/pipeline_check.py architecture --tier <the tier just chosen>`
   to get the **default**, then offer every entry in format.json `architectures`
   **of that tier** by name with its one-line `summary`, default pre-selected.
   Write the answer into `run.json` as a top-level `architecture` **before
   fin-script runs**, and show it in the confirm block. fin-storyboard and
   fin-build both read it.

   At MEDIUM/LONG there is nothing to ask: every rotating entry is a SHORT
   layout, so the command returns `tiers.<tier>.architecture`
   (`per-line-chapters`) and says so. Record that and skip the style question —
   asking it there is what produced a run.json claiming `blockframe-9` on a
   chapter cut.

   How the default is computed, and why it is only a default: normally the
   command rotates, returning the least recently used entry; if
   `architecture_lock` is set it returns that and prints `LOCKED`. The lock
   records that **blockframe-9 is a decision the creator made on 2026-07-30
   after reviewing thirteen styles side by side** — so it is the right thing to
   pre-select, and the wrong thing to impose now that the creator has asked to
   choose per run. Never "helpfully" vary the layout yourself because the last
   runs look alike; offer the choice and take the answer. Record in the run log
   whenever the pick differs from the default.

   **Every architecture carries a photograph in every frame.** That is a hard
   creator rule — *"images are compulsury"* — and `doctor` refuses any entry
   that does not declare `image_per_scene: true`, so a style cannot be offered
   that quietly drops the image. Do not invent a style at intake: the menu is
   whatever is in `architectures`, nothing else.
3. Whether fresh numbers are needed is a **grep, not a question**: during
   Phase 1, `fin-facts` verify-only mode applies when
   `vault/knowledge/money-facts-2026.md` already covers the topic's figures.
4. Print the confirm block and wait for `y` (unless `--yes`):

```
slug            <slug>
tier            SHORT · target 2:45
style           <name>  (default was <default>[ LOCKED])    ← asked, question 2
char budgets    hi ~1,986 (13.03 c/s) · en ~2,454 (16.1 c/s)  ← SHORT example; formula below
voices          hi Harsh HTUuC7OeeEt6OL5fViVe · en Brian nPczCjzI2devNBz1zQrb
est. TTS chars  ~4,500 across both cuts
est. wall clock ~2h–3h (≈36 min of that is ffmpeg)
outputs         studio/videos/<slug>-{hi,en}/renders/ · vault/videos/<slug>/
```

Both cuts always ship, one per channel (hi → @cashguruguides,
en → @moneymavens101) — there is nothing to ask.

**Derive the char budget from SPEECH time, not runtime.** `chars_per_second` is
chars per second *of audio*; a scene also charges non-audio padding, so

```
budget = (target_seconds − lines × (lead_in_seconds + tail_seconds)) × chars_per_second
```

reading `lines`, `lead_in_seconds` and `tail_seconds` from `format.json
tiers.<tier>` (falling back to the `scene` block when the tier omits them), and
`chars_per_second` from `cuts.<cut>`. **Always read the rate live — never copy a
worked example's number.** At the hi rate of 2026-08-08 (14.281, Amrut) that is
SHORT ⇒ `(165 − 9×1.4) × 14.281 ≈ 2,176` and MEDIUM ⇒ `(510 − 78×0.8) × 14.281 ≈
6,392`; the naive `target × rate` gives 2,356 and 7,283, overshooting by 8–14%
and inviting a script to pad itself that much. The rate changes whenever the
voice does — it moved 13.03 → 14.281 when hi went from Harsh to Amrut, and a
script budgeted at the old rate lands short of the tier's own floor.

Initialize `run.json`: intake answers, `started`, an empty `stages` map, a
`budget` block `{elevenlabs_calls: 0, max_elevenlabs_calls: <derived>, pixabay_calls: 0}`,
and **`voices: {hi: <id>, en: <id>}` copied from `format.json cuts.<cut>.voice_id`.**

**Two decisions bind before they can be seen, so both are locked here and
`pipeline_check` enforces it** (`decided_late_problems`): the **style** (the script
is written to it) and the **voice** (`chars_per_second` is a property of the voice,
so a swap re-budgets the script). `check_script` refuses a run with no
`architecture`; `check_voice` refuses one whose `voices.<cut>` is missing or no
longer matches `format.json`.

**Sample two lines before you voice eighty.** After `fin-script` passes and before
`fin-voice`, generate the first two VO lines only —
`python3 tools/tts/batch.py --project studio/videos/<slug>-<cut> --cut <cut> --only 1.1,1.2`
— and hand them over with the script's opening. Two calls, ~30 seconds. This exists
because `passive-income-number` spent **156 calls, 52% of its whole TTS budget**, on
style-A scripts discarded after both cuts were fully voiced; the cheap comparison
that settled it (`studio/voice-tests/passive-income-number/style-E-*.txt`, ch1–ch2
only) was run 156 calls too late. If the creator changes style or voice on hearing
the sample, re-run `fin-script` — that is the whole point, and it now costs two
clips instead of a budget.

**`run.json` is STATE, not a notebook.** It holds what a resume needs and nothing
else; `pipeline_check.py RUN_STATE_KEYS` / `CHAPTER_STATE_KEYS` are the shape.
Rulings, incidents, tool fixes, carry-forwards and anything you would prefix with
`_` go to `vault/videos/<slug>/notes.md`. `mark()` drains the rest there for you —
this is not a warning you can ignore, the key will be gone on the next transition.

**Derive the TTS ceiling from the tier — never hardcode it.** One clip per VO
line per cut, so `max_elevenlabs_calls = format.json tiers.<tier>.lines × 2 cuts
× 1.2` (the 20% covers per-line regens). SHORT ⇒ 9×2×1.2 ≈ **22**, MEDIUM ⇒
78×2×1.2 ≈ **188**, LONG ⇒ 92×2×1.2 ≈ **221**. The old fixed `30` was a SHORT-tier
number that silently blocked every longer run at the voice stage
(hit on japanese-money-methods LONG, 2026-08-01, where the two cuts need 184).
The ceiling exists to catch a runaway loop, not to cap a legitimately long video.

## 3 · The stage machine

```
Phase 1 (sequential — both edit shared vault paths):
    fin-research → fin-facts
Phase 2 (hi cut):   fin-script → fin-audit → fin-voice → fin-storyboard
                    → THE CHAPTER LOOP (§3b) → concat → fin-render → fin-package
Phase 3 (en cut):   the same, reusing Phase 1 output
Phase 4:            promote-facts (orchestrator, see §5) → fin-archive
```

**Everything visual is built and reviewed one chapter at a time (§3b).** A
full-length 1080p render is 30–40 minutes; discovering a wrong image in it costs
that twice. A chapter draft is ~3 minutes and shows the same mistake. The rule
the creator set on 2026-08-04: *never spend a full render to find out what a
draft would have told you.*

For each stage:

1. Print the transition line: `▶ fin-<stage>[-<cut>] · <n>/18 · <elapsed>`.
2. Invoke the matching `fin-*` agent (Task tool) with exactly: `slug`, `cut`,
   `tier`, `attempt`, and — on attempt 2 — the full prior failure text
   (check output + the agent's log). Nothing else; the agent reads disk.
3. Echo the agent's 4-line return under the transition line.
4. Verify and record:
   `python3 tools/pipeline_check.py mark <stage> --slug <slug> [--cut <cut>] --attempt <n> --log vault/videos/<slug>/logs/<stage>-<cut>-<n>.md`
5. Exit 0 → next stage. Exit 1 → **one retry** (attempt 2, failure text
   appended). A second failure is terminal:
   - `run.json` already holds `{status: failed, reason, log, at}` — print the
     reason, the log path, and the exact command to re-run the stage alone:
     `/finance-video --from <stage> --slug <slug>`.
   - If the hi cut finished and the en cut failed, say so explicitly — **the
     hi cut is usable as-is**; report its render path.

Retry arbitration (one owner): agents never retry, scripts never retry — only
you retry, once. Before invoking `fin-voice` or `fin-assets`, check the
`budget` block; refuse the stage if the run's API-call count would exceed its
ceiling, and say which ceiling.

Hard gates (no retry loops past them):
- `fin-audit` FAIL ×2 ⇒ stop before any TTS spend.
- `fin-render` frame-check fail ⇒ one `fin-build` fix pass, then stop.

The render stage is split three ways (a subagent's background task dies when
the subagent returns — verified 2026-07-28): fin-render invocation 1 does the
gate-two frame check only; then YOU run the encode as YOUR OWN background task
(`PRODUCER_ENABLE_CHUNKED_ENCODE=true npm run render -- -q high --resolution
1080p --video-bitrate 12M -o renders/FINAL-1080p-<cut>.mp4` in the project
dir); when it completes, fin-render invocation 2 does the QA. Notify on
terminal states.

**Then finish the audio — this is yours, not fin-render's** (its ffmpeg
allowlist is analysis-only). Both steps must happen before you mark `render`
done, because `check_render` requires the final file:

```
tools/audio/mix.py     studio/videos/<slug>-<cut>/renders/FINAL-1080p-<cut>.mp4
tools/loudnorm.py      studio/videos/<slug>-<cut>/renders/MIXED-1080p-<cut>.mp4 \
                       studio/videos/<slug>-<cut>/renders/PUBLISH-1080p-<cut>.mp4
tools/transcript.py    <slug> --cut <cut>          # captions + narration
```

`transcript.py` is the last of the three and needs only the shipped
`index.html`, so it can run any time after the build; it writes
`renders/captions-<cut>.srt` (the subtitle upload) and
`vault/videos/<slug>/narration-<cut>.md`. **Every video ships subtitles**
(creator rule 2026-08-06) and `check_package` now fails without both files.

`mix.py` lays the music bed and SFX under the voice from the cue list `fin-build`
wrote to `assets/audio.json`, ducking the bed about 6 dB under speech. It is a
no-op if there is no cue list and skips any asset that isn't on disk — a missing
sound never blocks a video. **If it prints "nothing to mix", run `loudnorm.py` on
`FINAL-` directly** (its default output name handles that case).

`loudnorm.py` then takes the mix to −14 LUFS / −1.5 dBTP true peak.
**`PUBLISH-…` is the file that gets uploaded**; `FINAL-` stays as the archive
master. Every cut shipped so far sat at −21 to −22 LUFS against YouTube's −14
target, and YouTube attenuates loud uploads but never lifts quiet ones — so
those videos play about 8 dB under everything around them. Both steps are video
stream-copies: ~30 s total, no re-encode.

**The SFX kit is generated once, not per video.** `tools/audio/sfx.py --kit` is
cached by name, so a run where all seven exist makes zero API calls. Include it
in preflight; it is free after the first time.

## 3b · The chapter loop — build, draft, review, lock

Replaces the old single `fin-assets → fin-build → fin-render` pass. Chapters come
from the script's `## Chapter <N>` headings; a scene belongs to chapter `C` when
its VO line is `C.x`, so the mapping needs no new bookkeeping.

**Each chapter is a standalone HyperFrames project** —
`studio/videos/<slug>-<cut>-ch<N>/` — with its own `index.html`, its own
`assets-ch<N>/` (the ONLY place its new files land) and an `assets/` symlink to
the cut for shared css/js/fonts/voice. Scene ids, `data-start` values and cue
offsets stay the shipped cut's, **rebased so the chapter plays from 0**; keep the
relative gaps exact or the chapters will not concatenate frame-exact.

For chapter N = 1..last:

```
1  fin-assets  --chapter N     images + Lotties for this chapter only
2  fin-build   --chapter N     the chapter project (archetype layer, §3c)
3  hyperframes check           must pass
4  DRAFT RENDER + SHEET — **you run this yourself, it is not a stage**:
     python3 tools/render_chapter.py <slug> --cut <cut> --chapter N [--check]
   It renders at `-q draft` and at the composition's own `data-fps`, builds the
   contact sheet, and refuses to run when `build.mjs` is newer than `index.html`
   (the stale-composition trap, §3b below). This was `fin-render --chapter N`
   until 2026-08-09: an agent wrapping two commands with no decision between
   them, measured at 318,807 tokens per invocation across 21 invocations.
5  fin-editor  chapter N       -> PASS | REWORK
     REWORK -> fin-build fix -> re-draft -> fin-editor (max 3 editor rounds)
6  fin-ceo     chapter N       -> SHIP | REWORK
     REWORK -> fin-build fix -> re-draft -> fin-editor -> fin-ceo (max 2 CEO rounds)
7  lock: record in run.json chapters[N] = {status: locked, draft, editor, ceo}
```

**The creator reviews chapters, not scenes — and they review in batches.** After
each chapter locks, keep going. Do **not** stop and ask per chapter. When every
chapter of a cut is locked, build the two review artifacts and hand them over
together:

```
tools/frames_sheet.py <slug> --cut <cut>        -> studio/videos/<slug>-<cut>-FRAMES.png
ffmpeg -f concat -safe 0 -i <list> -c copy      -> studio/videos/<slug>-<cut>-PREVIEW.mp4
```

`FRAMES.png` is a single numbered PNG — one cell per scene plus one per declared
`data-framings` change, each with a big index number, the chapter + scene id, and
two timestamps (into the chapter mp4 and into the concatenated preview). **That
numbering is the review protocol**: the creator replies "#7 is wrong", and the
number resolves to exactly one frame. Never renumber between passes for the same
cut — a note against `#12` must still mean `#12` after a fix round.

The concat is a stream copy (~seconds, no re-encode) and it is a PREVIEW, not the
master: the chapter joints are hard cuts there, because each chapter's last scene
carries a bare `data-duration` and its first scene never fades in. The 0.45s
cross-dissolve returns only in the full assembly. Say this when you hand it over,
or it gets reported as a defect every time.

Then **stop and wait.** Creator feedback arrives as a list of frame numbers; fix
them all, re-render only the affected chapters, rebuild both artifacts, hand back.

**`-f <final fps>` is not optional.** Draft at the fps the final will use (the
composition's `data-fps`, else 30). A draft rendered at 24 to save time produces
frame counts that do not sum, and the chapters drift at every joint.

Draft render flags: `-q draft` only. Do NOT add `--resolution`, `--gpu`,
`--video-bitrate` or chunked encode — a draft is for judging images, motion and
timing, all of which are identical at draft quality. ~3 min for a 70 s chapter.

Escalation: if the editor still says REWORK after three rounds, or the CEO after
two, **stop and hand the chapter to the creator** with both logs and the latest
draft path. Do not keep spending renders on a disagreement; two rounds is the
budget, and a human settles the rest.

When every chapter is locked, concatenate and run the ONE full-quality render
(§3, the split three-way render stage). `fin-render`'s frame check then runs
against a video whose every scene has already been seen — it is a safety net, not
the first look.

**Resume:** `run.json.chapters` is authoritative. `--resume` re-enters at the
first chapter that is not `locked`; locked chapters are never rebuilt or
re-reviewed.

## 3c · The archetype layer (MEDIUM/LONG — the standing look since 2026-08-05)

Chapter cuts are built on `tools/scaffold/assets/chapter-design.css` on top of
`blockframe.css`. Constants: `format.json chapter_design`. Rules and rationale:
`vault/knowledge/design-chapter-archetypes.md`. Reference implementations,
creator-approved: `vault/videos/japanese-money-methods/src/hi-ch{1,2}/index-claudedesign.html`.

You do not design; you make sure the stages did. Four things to verify per
chapter before you let it lock:

1. **`fin-storyboard` assigned `arch` / `ground` / `art` per scene.** If those
   columns are missing, the storyboard is incomplete — send it back rather than
   letting `fin-build` invent a layout.
2. **Every scene carries `has-photo`** and a real `.bg`. `image_per_scene` is a
   hard creator rule; the vector-only chapters were a one-off experiment.
3. **Timing was not touched.** Every `data-start` / `data-duration` /
   `data-framings` comes from `timing.json`, which is measured from the voice. A
   layout pass may not re-time a scene. The failure mode to watch for is
   seductive: durations that sum to exactly the right total while every internal
   cut drifts (see `vault/knowledge/claude-design-mcp.md` §3b).
4. **No rail.** A chapter title / scene-counter overlay was built and removed at
   creator request 2026-08-05 — the viewer must never be shown that the video is
   chapter-based or slide-numbered. If one appears, reject the chapter.

## 3a · Pipeline the two cuts (overlap safely — where the wall-clock is won)

Phase 1 is sequential (shared vault paths). Phase 2 (hi) and Phase 3 (en) write
SEPARATE paths (`studio/videos/<slug>-{hi,en}/`, `*-{hi,en}.md`), so **pipeline
them** — do not finish all of hi before starting en. The gain comes ONLY from
overlapping stages that use different resources, never from running the same
heavy stage twice at once.

Classify each stage:
- **Model-bound** (LLM inference, light local, independent files): `script`,
  `audit`, `storyboard`, `package`, `voice`. Overlap these freely.
- **Machine-bound** (saturate your CPU/GPU, already multi-core internally):
  `assets` (fetch + vision), `build` (headless Chrome), the **encode**, and
  `render` frame-check / QA (whisper).

Rule: **overlap one cut's machine-bound stage with the other cut's model-bound
stages** (e.g. write `fin-script-en` while the hi encode runs). NEVER run the
same machine-bound stage for both cuts at once — two encodes / two builds / two
whisper-QAs on one box split the same cores: no wall-clock gain, and memory
thrash that can make it slower.

Guardrails that make overlap safe (MUST):
- **`fin-assets` never runs for both cuts at once.** Both dedupe against every
  image on disk; concurrently they keep the SAME photo before either lands it (a
  cross-cut dup slips the check), and they double the peak Pixabay/Pexels rate
  (Pexels free tier = 200/hr → 429s). Start en-assets only after hi-assets has
  written its images.
- **Serialize `run.json`:** only you write it, and you process
  task-notifications ONE AT A TIME, so every `mark` read-modify-write stays
  atomic even with parallel agents in flight.
- **Narrative lives in `notes.md`, and you read it on purpose.** When a chapter
  brief needs a prior ruling, open `notes.md` and quote that ONE ruling into that
  agent's prompt. Never park it in `run.json` so the next fourteen transitions
  re-read it — that was 75% of the last run's standing token bill.
- **Budget is shared:** before a spend stage (`voice`/`assets`) on either cut,
  check the `budget` ceiling against BOTH cuts' in-flight spend, not just this
  cut's.
- **Hard gates are per-cut:** an `audit`-×2 or frame-check stop on one cut never
  stops the other; a finished hi cut still ships if en fails (§3.5).

Canonical shape: `fin-script-en` during the hi encode; `fin-audit-en` /
`fin-voice-en` during hi render-QA; `fin-package-hi` during en voice/storyboard;
the two `fin-assets` and the two encodes always staggered. The machine-bound
stages are the floor — pipelining hides the model-bound work inside them but
cannot beat the core count; going below it needs cloud/Lambda encode, not more
orchestration.

## 4 · Trust rules

- Verify agent claims against the repo when they matter: subagent output is
  advisory, `pipeline_check` + your own Read are authoritative.
- Never write `done` yourself — only via `mark`.
- Agents write logs; if one returns without its log file, treat the stage as
  failed regardless of its STATUS line.

## 5 · Close-out (after both renders pass)

1. **Promote facts** (the anti-poisoning step): append the HARD-tagged lines
   from `vault/videos/<slug>/facts-staging.md` to
   `vault/knowledge/money-facts-2026.md` — dated, with source URLs. SOFT lines
   stay in staging. This happens only now, after both renders passed.
2. **The vidIQ packaging pass — YOU run this, not an agent.** Read
   `.claude/skills/vidiq/SKILL.md` first, then run recipes **R3** (title lock)
   and **R3b** (tag block) against both packs. Budget ~35 credits for the pair;
   check `vidiq_balance` first.
   - It is deliberately **not** a `fin-*` stage: agents have no credit budget to
     reason about, and a mid-run 402 would fail a stage that has nothing to do
     with money. vidIQ runs *around* the pipeline — topic selection before,
     packaging here, autopsy after publication.
   - Ship a title only when the CTR score and the autocomplete demand **agree**.
     A high score on a phrase nobody types is a click-through rate on zero
     impressions; a high-volume phrase that scores below baseline belongs in the
     tags, not the title.
   - **If a title changes here, re-run `fin-package`'s thumbnail section.** The
     thumbnail is downstream of the title and is now stale by definition.
3. `python3 tools/vault_commit.py commit <slug> -m "finance-video: <slug> — both cuts rendered"`
   (explicit paths only — the tool refuses to touch anything else).
4. Run `fin-archive`.
5. Print the completion summary: both render paths, runtimes, QA numbers,
   thumbnail paths **plus the AI-enhance prompt for each cut**, recommended
   titles with their CTR scores, and — always —
   `Owed before publish: proof-listen (hi, en) · AI-enhance both thumbnails · upload.`

## 6 · After the URLs arrive

A YouTube URL means finished (`vault/CLAUDE.md`). Do not gate on public
reachability — uploads are scheduled, so a 403 or an empty channel tab is
expected, not a failure.

1. **Save the AI-enhanced thumbnails into the thumbs project** as
   `thumbnail-<cut>-ai.png` *before* archiving. They are the files actually on
   YouTube; the renders are not. `i.ytimg.com` 404s while an upload is
   scheduled, so they cannot be recovered later — on japanese-money-methods this
   was missed and the archive holds only the pre-enhance renders.
2. **Distill first, archive second.** Every durable learning into the milestone
   note and the right knowledge note BEFORE `archive_cut.py` — the render is
   about to become the only place some of it lived. Delete the session files
   (`HANDOVER.md`, `NEXT-SESSION-PROMPT.md`) once folded; a session file dies
   with its session, so anything durable in it must move to a knowledge note
   first.
3. `tools/archive_cut.py <slug> --hi <url> --en <url>` (`--dry-run` first).
   **Read its output** — it prints one line per directory, and the count must
   match `ls -d studio/videos/<slug>*`.
4. vidIQ post-publish: `score_thumbnail` on both cuts (the first time it is
   possible — it needs a live `videoId`), then **recipe R5 at 28 days** for the
   retention curve. ⚠️ Owned-channel tools work only for channels in
   `vidiq_user_channels`; today that is @moneymavens101 only.
