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

---

## 2026-08-09 — Phase 2a: `format.json`

After item 1, `format.json` was the largest remaining line item: 27,183 b read
whole by 13 agents, ~550k tokens/run.

### A — the prose drained (30%)

**47% of the file was `_`-prefixed prose** — the same disease and the same
convention as `run.json`, and against the file's own `_comment`, which says
*"Prose/design rationale lives in vault/knowledge/design-finance-blockframe.md —
never duplicate it here."*

No code reads any `_` key (verified: the two apparent hits were `strip_comments`
and `cut_assemble` writing its own `_comment`). 21 keys drained into 6 vault docs
by domain — rate/voice records to `workflows/voiceover-tts.md`, architecture and
style verdicts to `design-finance-blockframe.md`, VAD/dissolve/Whisper mechanics
to `evidence-discipline.md`, the Lottie cap to `design-icons-emoji-lottie.md`.

It is 30%, not 47%, because a shortened live kernel stayed wherever a note was
doing real work at read time (`art_opacity._important_note`, the `video_scene`
traps, `scene._transition_note`). Only the records went.

```
tools/format.json   27,183 → 18,957 b   0 strings >60 chars lost (leaf-set diff vs HEAD)
```

**The live citation was worse than stale.** Both worked examples in
`.claude/commands/finance-video.md` computed the char budget at `13.03` — the
**retired Harsh rate**, when live `cuts.hi.chars_per_second` is `14.281`. The
orchestrator was teaching every run a budget ~9% too small; that is the same
failure that landed the hi cut at 7:59.259, under the 8:00 mid-roll floor. Now
reads live, with dated examples and an explicit "never copy a worked example's
number."

Also: `_components` → `components` (structured config, not prose — the underscore
would have made it a drain target), and `dangling_studio_refs()` now scans
`format.json`, where `tiers.medium/long.reference` points into `studio/` and
becomes a dangler the day firaun ships.

### B — per-agent views (a further 50%)

`format.json` has two readers with opposite needs: tools call `json.load()` and
want everything at zero cost; agents `Read` it and pay per byte. So the file does
**not** split — `doctor` derives `tools/format/<agent>.json` beside it at every
preflight, which runs before the `--resume` branch, so a stale view is impossible
rather than unlikely. Views are gitignored; the source is tracked.

A `_<key>_note` rides along with the key it explains, so no view claims prose by
hand. `doctor` fails preflight if any `format.json` key is claimed by no view —
the "every key belongs to at least one robot" check.

| agent | view | % of file | inv/run |
|---|---|---|---|
| fin-build | 17,758 b | 93% | 19 |
| fin-storyboard | 16,802 b | 88% | 4 |
| fin-editor | 12,988 b | 68% | 16 |
| fin-assets | 7,686 b | 40% | 23 |
| fin-audit | 4,533 b | 24% | 5 |
| fin-script | 3,363 b | 18% | 5 |
| fin-package | 3,081 b | 16% | 0 |
| fin-render | 2,397 b | 13% | 12 |
| fin-research | 1,943 b | 10% | 2 |
| fin-voice | 1,880 b | 10% | 5 |
| fin-facts | 1,198 b | 6% | 1 |

```
format.json reads per run   2,500,836 → 871,924 b   65% off   ≈ 407k tokens
```

`fin-research` and `fin-facts` had prompts saying only "constants from
format.json." Rather than infer their diet, **both prompts now name the keys they
use and why** — research reads `tiers.<tier>` and `cuts.*.channel`, facts reads
`cuts.<cut>.currency` / `forbidden_currency` — and the slices come from those
declarations.

`fin-ceo` and `fin-archive` are deliberately absent: neither prompt reads a
constants file at all, and a view nobody opens is a file to keep in sync for
nothing.

### The benchmark chapter in the brief was the wrong one

`japanese-money-methods` **hi**-ch1 and hi-ch2 are the two hand-built vector-only
chapters — zero archetype classes, `.field` deliberately redeclared to the legacy
full-bleed. Tracing `fin-build`'s diet against hi-ch2 proves nothing about the
archetype layer because that chapter bypasses it. `en`-ch2 *is* generator-built.

Traced instead against all **14 generator-built chapters** of that video:
**10 distinctive `format.json` constants used, 0 missing from `fin-build`'s
view.** Plus: every cited view file exists and parses, `doctor` passes on all
three tiers, and the orphan-key assert fires in the selftest.

This proves the views are sufficient for work that has actually shipped. It does
not prove an agent will never reach for a key its prompt never named — only a
live run does that.

---

## 2026-08-09 — the rehearsal, and what it found

`FIN_FAKE_APIS=1`, MEDIUM tier (SHORT never enters the chapter loop, so it would
have left `chapter_design` — the largest block in `fin-build`'s view — untested),
Phase 1 + hi cut through the chapter-1 build. Eight stages, **1,084,003 subagent
tokens, 134 min, zero credits.**

Every view carries an `_if_a_constant_is_missing` key telling the agent to log
`MISSING-CONSTANT: <key> — <why>` rather than guess, because a diet that is too
narrow otherwise fails silently and leaves no trace.

### The diet held

17 `MISSING-CONSTANT` reports; **two were real diet gaps.**

- `fin-voice` needed `tiers` — its cost-guard formula references `target_seconds`
  and the per-line padding, so without it the stage cannot check its own report.
  **Added.**
- `fin-script` reached for `chapter_design.archetypes`. **Refused, and the
  boundary written into the prompt instead:** archetype assignment is
  `fin-storyboard`'s job and `fin-build` applies only what the storyboard wrote.
  A script cue says what the frame must SHOW; naming a layout is a cue the
  storyboard has to undo.

**`fin-build` reported zero** — the 93% slice, on the highest-invocation heavy
agent, with `npm run check` at 0 errors and Contrast 9/9 AA. `fin-facts`:
"your slice was sufficient, the four keys are exactly the job." `fin-storyboard`:
"sufficient for layout, cues, archetypes and audio."

### The other 14 are gaps in `format.json` itself

Keys that exist nowhere, so no slicing decision could have supplied them. This is
the backlog the instrumentation surfaced — each was reached for by a real stage
doing real work:

| key | wanted by | for |
|---|---|---|
| `assets.min_image_bytes` | fin-assets | the 10 KB gate that failed the run, "named nowhere I can see" |
| `assets.min_source_yhigh` | fin-assets | the 110 floor; prose is in the slice, the number only in a vault note |
| `assets.min_width_px` | fin-assets | 1600, plus the Pexels-1880/Pixabay-1280 split that drives pool choice |
| `layout.font_subset` | fin-storyboard | the FinanceSans subset guard — **silently renders tofu with every check passing**; 12 strings needed rewriting |
| `audio.max_sfx_cues` per tier | fin-storyboard | the ≤10 figure is a SHORT constant; literally applied to a 9:29 cut it gives one transition for 86 boundaries |
| `layout.cascade.rows` | fin-storyboard | whether a cascade counts toward max_simultaneous_elements |
| `tiers.<tier>.char_budget_formula` | fin-audit | gate one currently derives the rule it enforces |
| `scene.max_hold_seconds` | fin-audit | — |
| `hook_gate_seconds` | fin-script | placing the payoff promise; 15 s was assumed and happened to be right |
| `mid_roll_threshold_seconds` | fin-script | whether a +2% overrun matters |
| `tiers.<tier>.length_tolerance_pct` | fin-script | whether 6,443 chars passes |
| `cuts.hi.number_scale` | fin-facts | `locale: en-IN` does not say whether ₹ renders `₹1,17,000` or `₹1.2 lakh` |
| `tiers.medium.comparable_length_band_seconds` | fin-research | study.py's 240 s floor has no upper bound to match the 510 s target |
| `architecture` resolution at MEDIUM | fin-storyboard | `run.json.architecture: blockframe-9` vs `tiers.medium.architecture: per-line-chapters` — no rule for which wins |

Not fixed. They are a real backlog, but inventing fourteen constants is a
separate decision from slicing the ones that exist.

### Three bugs it found that have nothing to do with the diet

1. **The md5 cross-project dedupe had been reading zero files since 2026-08-05.**
   `fin-assets.md` globbed `studio/videos/*/assets/img/*.jpg`; chapter projects
   write to `assets-ch<N>/final/`. Measured: **0 matched where 106 exist**, and
   under zsh a non-matching glob kills the command line, so it reported "no
   collisions" having compared nothing. Covered `japanese-money-methods` and
   `passive-income-number`. This is `evidence-discipline` rule 1 — a test that
   cannot fail is not evidence. **Fixed**: a `find` sweep that walks both layouts,
   survives an empty tree, and excludes `_cand/`, `renders/` and retired takes.
   204 in-use images, zero false positives.

2. **Rehearsal mode was free by accident.** `.env` is the only channel that
   reaches a subagent's Bash call — env does not persist between calls — and
   `batch.py` computed `fake` *before* parsing `.env`. It stayed free only because
   the not-fake branch called `load_env()`, which `setdefault`-ed the flag in time
   for `synthesize()` to re-check it. Reorder or remove that call and a rehearsal
   becomes a full-price run with no visible difference. **Fixed** in `batch.py`
   and `pixabay_fetch.py`; `doctor` now prints a REHEARSAL banner and `mark()`
   stamps `fake_apis: true` on every stage it records, so a rehearsed stage can
   never be mistaken for a real one by a later resume.

3. **`sfx.py --selftest` fails at HEAD** — `kit.json` holds 8 sfx (`buzz`), the
   assert says 7, and the vault calls it "the seven-sound kit." Not fixed:
   whether `buzz` is legitimate or a mistake is not mine to decide.

`fin-assets` also reports `check_assets` has no `_`-prefix skip, so an authored
manifest's prose keys and its `HOLD - no fetch` slots report as missing images.
Not fixed.

### What the rehearsal could not test

Fake mode makes images flat colour and voice a sine tone, so `fin-assets`' visual
rejection pass — the stage's actual job — was not exercised, and `check assets`
is red on all 11 slots for the 10 KB gate. `fin-editor`, `fin-ceo`, `fin-render`
and `fin-package` never ran.

---

## 2026-08-09 — Phase 1 items 3–6

### Item 3 (1d) — supersession is now declared, and enforced

`standing_stage_problems()`, wired into `doctor`: every note under
`vault/{knowledge,skills,workflows,templates}` must declare `stage:`, and a
`SUPERSEDED BY <path>` must name a file that exists — so a rename cannot quietly
turn a supersession into a dangling claim, the same failure as
`dangling_studio_refs()` one layer up. `_archive/` is skipped by design.

**41 files backfilled.** Three were genuinely superseded and had no marker:

- `haryanvi-hindi-script-style.md` → SUPERSEDED for finance-hi (Standard Hindi,
  creator 2026-07-28); kept as reference if a Haryanvi lane returns.
- `indian-business-culture-slang.md` → SUPERSEDED with it — its vocabulary exists
  to season Haryanvi scripts.
- `design-techtooltester.md` → ADOPTED for its own channel, SUPERSEDED by
  `design-finance-blockframe.md` for all finance work (blockframe already said so;
  the marker just moved to where a reader sees it).

**Two live correctness bugs found while backfilling — both the same disease the
item exists to kill: a summary asserting a rule that was retired in the body.**

1. `urdu-script-style.md`'s frontmatter said *"Roman Urdu… ALWAYS follow this for
   every Urdu script."* The rule change to Nastaliq (creator 2026-07-18) sits at
   **line 94**. A reader trusting the summary would have written the retired
   script. Summary rewritten: the file is live for VOICE, retired for ORTHOGRAPHY.
2. `niches/india-finance-market.md` said *"Haryanvi-flavored Hindi VO"* in its
   summary and named the retired Haryanvi voice ID in Fixed decisions, while line
   32 of the same file said Standard Hindi. Corrected, and the voice ID replaced
   with a pointer to `format.json` — it had already gone stale exactly as a
   duplicated fact does.

**A third un-promoted rule rescued.** The Standard-Hindi decision (creator
2026-07-28) lived *only* in `.claude/agents/fin-script.md` — procedure, not
memory, against `vault/CLAUDE.md`'s own two-home rule. Now in
`niches/india-finance-market.md` under a Language heading. Same class as the
firaun VO-line rule and the japanese archetype references.

### Item 4 (1a) — the shelf labels were not built, deliberately

`vault/videos/` is already RECORD and already unread — verified in Phase 0 and
re-verified here. The directory structure *is* the shelf, so a `shelf:`
frontmatter field would be a second home for a fact the path already carries.
The valuable half of 1a was the audit, and it is done: three un-promoted STANDING
rules found and rescued (firaun VO lines, japanese archetype references,
Standard Hindi).

### Item 5 (1f) — the shape, not the ceiling

Logs got a required shape — **Ran · Failed · Evidence · Changed · Owed** — in the
11 agents that write freeform logs. `fin-editor` and `fin-ceo` were left alone;
their severity-scored findings table is already a stricter template.

**The 600-word ceiling was NOT implemented.** Measured: mean 1,582, median 1,352,
**86% of all 256 logs exceed 600 words.** A cap there is a blocking gate on nearly
every normal stage — the worst rung of `fix-defaults-not-gates`. And the logs are
not in the read path: no agent declares reading a prior log, and log *content*
reached context through `run.json`, which item 1 already fixed. Capping them saves
git weight and nothing else.

The decisive evidence is the rehearsal itself. Its most valuable output — the
`batch.py` ordering bug that made rehearsal mode free only by accident, and the
md5 sweep that had been reading zero files for four days — came out of long
`fin-voice` and `fin-assets` logs. A 600-word cap would have destroyed both. The
instruction now says so explicitly: *a long log that found something is worth more
than a short one that did not.*

### Item 6 (1c) — the audit appendices moved

`vault/knowledge/finance-audit-2026-07-29/` → the twelve appendices and
`transcripts/` moved to `_archive/` inside that folder; `index.md` stays in place
because three files reference it, and its 34 wikilinks were repointed. Nothing
deleted, nothing renamed.

```
in the read path   80,614 w  ->  4,873 w   (index only)
archived           75,741 w of appendices + 19,753 w of .txt + ~114k w of .vtt
```

Token saving: **zero** — no agent ever read them, which is exactly why they could
move. This was hygiene and human legibility, and it is the item whose value I
argued was lowest at Gate 1.

---

## 2026-08-09 — the tofu guard (`layout.font_subset`)

`fin-storyboard` reported `layout.font_subset` missing during the rehearsal: the
FinanceSans subset guard existed only as prose in a previous video's storyboard,
and a missing glyph "silently renders tofu with every check passing."

**The prose was not merely missing — it was inverted on six of the eight glyphs
it named.** Measured against the font's own cmap:

| glyph | the prose claimed | actually |
|---|---|---|
| `/` `?` | absent — avoid | **present** |
| `→` `▶` `×` `≈` | carried — safe | **absent — these are the tofu** |
| `₹` `·` | carried | carried ✓ |

So it cost twelve needless string rewrites on `passive-income-number` (`₹X / MONTH`
→ `₹X A MONTH`) while blessing the arrows that actually shipped as tofu.

**Fixed as a derived check, not a constant.** `uncovered_glyphs()` reads
`NotoSansFinance-var.woff2`'s real cmap and fails any build whose on-screen text
uses a glyph the face cannot draw. A `layout.font_subset` constant would have been
a second home for a fact the font already owns, and would go stale the day the
subset is regenerated — which is exactly how the prose version died.

Scoping took three passes to get honest, and each false positive is worth
recording because each was a way to cry wolf:

1. `<head>` never renders — its `<title>` carries the Devanagari cut name on every
   hi chapter, which fired the check on all of them.
2. `<style>` and `<script>` bodies are not on screen — CSS comments contain `~`.
3. **A composition that does not link FinanceSans cannot be judged by its cmap.**
   The four pre-FinanceSans cuts (`50-30-20-rule/legacy`, `emergency-fund`)
   legitimately drew arrows and Devanagari in whatever the OS supplied.

Final: **3 of 50 compositions flagged, all true positives** — `credit-history/hi`,
`credit-history/thumbs` and `good-debt-vs-bad-debt/hi` each shipped a `~` the font
cannot draw. All seven `passive-income-number` chapters in production are clean.

`fonttools` was installed only transitively via `faster-whisper`'s chain, so a
lighter resolve would have turned the guard into a silent no-op — the exact
disease it was written to cure. Now declared in `tools/requirements.txt`, and
`doctor` fails preflight if it is not importable.

---

## 2026-08-09 — Phase 2b–2e

### 2b — decide before you spend

`passive-income-number` burned **156 ElevenLabs calls, 52% of its budget**, on
style-A scripts discarded after both cuts were fully voiced. The intake question
for style already existed and was answered; nothing stopped the decision moving
afterwards.

`decided_late_problems()` now asserts the two things that bind before they can be
seen. `check_script` refuses a run with no `run.json.architecture`. `check_voice`
refuses one whose `voices.<cut>` is missing or no longer matches `format.json` —
because `chars_per_second` is a property of the VOICE, and the Harsh → Amrut swap
moved it 13.03 → 14.281 and landed the hi cut at 7:59.259, **0.741 s under the
8:00 mid-roll floor that is the whole reason MEDIUM tier exists.**

And the default that would actually have caught it: the orchestrator now voices
**two lines** after `fin-script` and hands them over before the full run. Two calls,
~30 seconds. The cheap comparison that settled the style
(`studio/voice-tests/passive-income-number/style-E-*.txt`, ch1–ch2 only) was run
156 calls too late.

### 2e — the density regression was in the apparatus, not the scenes

|  | scenes | apparatus | sections |
|---|---|---|---|
| japanese | 4.05 w/s | 9.16 w/s | 17 |
| passive | 6.26 w/s | **28.77 w/s** | **41** |
| | 1.5× | **3.1×** | 2.4× |

The scene table barely moved. What tripled is the prose around it — *"11. The
ground temperature arc"* (968 w, which is `design-chapter-archetypes`'s job), *"the
cue list is DERIVED per chapter"* (694 w, a pipeline mechanic), *"what this file
ports and where it diverges"* (886 w, meta-commentary), and the font-subset guard
that turned out to be inverted. Standing rules re-derived per video — the same
disease as the vault, one layer down.

`check_storyboard` now fails a file over **`3000 + 14 × target_seconds`** words. The
budget is affine, not a flat w/s rate, because a storyboard has fixed overhead and a
flat rate false-fires on SHORT where the overhead is the whole file. Fitted so all
six reference cuts pass (japanese en is closest at 12,153/12,240) and both
`passive-income-number` storyboards fail (17,864 and 15,346 against 10,140).

### 2d — one bucket, and the biggest one was refused

63% of 155 reviewer findings are mechanical. **Bucket 1 — composed-frame
legibility, 32%, the biggest — was not built, and the reason is disqualifying:
there is no ground truth.** `archive_cut.py` drops renders and jpgs by design, so
`japanese-money-methods` — the only cut anyone calls good — has **no surviving
frames**. The only composed frames on disk belong to `passive-income-number`, the
cut that needed eight build attempts. Calibrating the check against the regression
would teach it to accept the thing it exists to catch. Worse than a false-fire:
unfalsifiable.

It is also the metric the humans needed **three successive rulings** to define
(`ground_and_payoff_legibility` → `payoff_clause_and_metric` → `floor_stopping_rule`,
all now in `notes.md`). A script encoding one version of a definition that moved
twice mid-run would be wrong in a way nobody could see.

Built instead: **off-canvas plate art** (archetypes gotcha 8). `.p-b` is
`left:1120 width:860` on a 1920 frame, so 60px hangs off the right edge and
anything past viewBox `x=800` renders nowhere — one chapter lost the X of a
decision fork exactly this way and every check passed. Deliberately narrow: bare
geometry attributes only, and anything under a `transform` is skipped, because this
check does not do matrix maths and would rather miss a defect than invent one.

Validated in both directions: **0 false fires across the 14 creator-approved
japanese chapters and all 7 in-production passive chapters**, catches a synthetic
`vx=815`, stays silent at `vx=700` and under a transform.

Also corrected: my keyword classification put "stale comment" findings in the
mechanical bucket. Reading them, they are all *a scene comment asserting something
the frame does not show* — prose-vs-pixels, which needs eyes. The mechanical share
is smaller than 63%.

### 2c — render and archive only

`model: haiku` on `fin-render` and `fin-archive`. `fin-voice` and `fin-assets` were
left on the strong model deliberately: `fin-voice` spent 104k tokens in the
rehearsal and used them to find the `batch.py` ordering bug — that was judgement,
not button-pressing — and `fin-assets` is the highest-rework stage in the pipeline,
where a downgrade would likely cost more in retries than it saves.

---

## 2026-08-09 — contact sheets kept; two rehearsal bugs closed

### `SHEET-ch*.jpg` survives the archive

`archive_cut.py` KEEP gains `renders/SHEET-ch*.jpg`. The contact sheets are the
only **composed** frames that survive an archive, and therefore the only ground
truth a future check can be calibrated against.

This is the direct consequence of 2d: the composed-frame legibility check — 32% of
all reviewer findings, the biggest single bucket — could not be built, because
`japanese-money-methods` kept no frames and the only frames on disk belonged to the
cut that took eight build attempts. A few MB per video buys the next approved cut
as permanent ground truth. Rationale recorded in `vault/CLAUDE.md` beside the
keep/drop list, since that is the list's home.

### The SFX kit had eight sounds and an assert that said seven

`buzz` is legitimate — a fully-formed entry (`helper: playLottie`, seconds, peak,
prompt) added for the style-E phone payoff, where the phone's silence is the
promise and its single buzz is the payoff. The test was stale, not the kit.

Fixed as **shape, never cardinality**: `len(kit) >= 7` (catching a deletion) plus
the existing per-entry asserts that every sound names the motion helper it scores.
A `== 7` only ever encoded how many sounds existed the day it was written, and it
broke the first time the catalogue legitimately grew. The generation assert now
follows the kit's own size instead of a literal.

Retired the same stale count from three prose homes
(`design-chapter-sound.md`, `design-finance-blockframe.md` ×2,
`fin-storyboard.md`), which now point at `tools/audio/kit.json` and say it grows.
`fin-storyboard` also learns `buzz` exists.

### A note in a manifest was being bought as a query

The authored full-cut manifest carries `_note`, `_reuse_note`, `_grade_note`,
`_routing_note`. `pixabay_fetch.py` iterated them as image slots — **spending a
real API search on each, using the prose as the search query** — and
`check_assets` reported all four as missing images.

One helper, `load_manifest()`, used at both of `pixabay_fetch`'s load sites, plus
the same skip in `check_assets`. Same convention as `run.json` and `format.json`:
**an underscore means narrative, everywhere.** Measured on
`passive-income-number-hi-ch1`: 91 keys → 87 slots, four paid searches saved per
invocation. Self-check added so it cannot regress.
