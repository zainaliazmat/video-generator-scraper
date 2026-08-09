# Eval rubric

Two tiers. **Tier A is asserted** by [run.py](run.py) and needs no eyes. **Tier B needs a
human or a vision model** and is scored on this sheet. A refactor may not trade Tier B for
Tier A: cheaper output that scores worse on relevance is a failed refactor, not a win.

---

## Tier A — asserted (10 checks, `python3 evals/run.py`)

Each check exists because the defect it catches actually shipped. Severity is the
project's own: **blocker** = wrong, misleading or unlicensed; **should-fix** = weak but
not false.

| Check | Sev | Catches | Source |
|---|---|---|---|
| `currency_purity` | blocker | ₹ in a `-en` cut, $ in a `-hi` cut | `fin-script.md:51-54` |
| `no_network_fetch` | blocker | a CDN reference that renders a static video with green checks | `fin-build.md:34-35` |
| `photo_every_scene` | blocker | a photo-free scene | creator rule 2026-07-28, `fin-storyboard.md:125` |
| `image_credits` | blocker | an image rendered with no attribution row (CC BY is a licence condition) | `fin-assets.md:242-248` |
| `no_repeated_image` | blocker | one photo behind two non-adjacent points | `fin-editor.md:68-70` |
| `vo_text_hygiene` | blocker | bare Latin digits / cite refs in TTS input | `fin-audit.md:51` |
| `timing_coherence` | blocker | a chapter re-timed so the total is right and the cuts drift | `pipeline_check.py:702`, `chapter_project.py:20-24` |
| `track_alternation` | should-fix | `overlapping_clips_same_track` | `fin-build.md:194-198` |
| `watermark` | should-fix | a cut with no channel mark | `fin-build.md:127-132` |
| `captions` | should-fix | cues over 84 chars or out of order | `fin-package.md:159` |

**A check that cannot find its inputs returns NA, never PASS** — `fin-assets.md:260-263`:
"a checker that cannot see the work is worse than no checker, because it reports green."

### Deliberately excluded from Tier A

`no_repeated_image` allows reuse across **adjacent** scenes: that is the documented HOLD
device (`fin-build.md:103-104`, one continuous `plateKen`), and flagging it would be
"a finding about the review" (`fin-editor.md:180-184`). A first draft of the checker did
flag them, and was wrong.

---

## Tier B — judged (score each 0–3)

Scored per chapter, from the contact sheet plus the encoded draft. **0 = blocker present,
1 = weak, 2 = fine, 3 = the standard we want.** Record the score and one sentence of why.

| # | Dimension | 0 | 3 |
|---|---|---|---|
| B1 | **Image says the line** (sound-off) | image contradicts or is absent from the line | every frame states its point with sound off and text stripped |
| B2 | **Figure honesty** | a number on screen is not in `facts-staging.md`, or a decorative proportion reads as a statistic | every figure traceable, every derived figure carries its assumption in frame |
| B3 | **Drawn art is additive** | art redraws what the photo shows | art asserts a proportion / comparison / measurement the photo cannot |
| B4 | **Script quality** | needs knowledge the video has not given; a number with no comparison | teaches in order, every number has a referent |
| B5 | **Retention** | a nameable timestamp where a viewer leaves | opens a loop, ends on a reason to continue |
| B6 | **Not a template** | would be at home in any generic finance video | unmistakably this channel |

**Gate: B1 and B2 must be ≥2.** They are correctness, not taste. B3–B6 may be 1 with a
note; two dimensions at 1 is a REWORK.

---

## Tier C — process metrics (from `tools/run_metrics.py` + `run.json`)

| Metric | Where | Baseline (`passive-income-number`) |
|---|---|---|
| billed tokens per locked chapter | `run_metrics.py --slug <slug>` | **17,616,560** |
| agent invocations per locked chapter | same | **31.0** |
| first-attempt chapter lock rate | `run.json.chapters[*].round == 1` | 0 of 4 (rounds 2, 2, 3, 3) |
| human interventions | `runs/<id>/interventions.md` (Phase 6) | **23** (13 `owed.*` + 6 tool fixes + 4 rulings) |
| Tier A blocker failures | `evals/run.py` | see [results/](results/) |

---

## How to use this on a refactor

1. `python3 evals/run.py --json evals/results/<label>.json` before and after.
2. Tier A blocker failures must not increase. Any new failure blocks the merge.
3. Tier B scored on the same chapters before and after; B1/B2 must not drop.
4. Tier C tokens must fall, or the change must be justified by a Tier A/B gain.

A change that improves Tier C while worsening Tier B is reverted. That rule is the whole
reason this file exists.
