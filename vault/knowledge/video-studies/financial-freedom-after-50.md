---
summary: EMPTY-LANE FINDING, not a study. backend/study.py returns zero usable US retirement comparables for this topic — the library has none in the LONG band, and the single pick it did return was a rupee-denominated India EPF video that was quarantined as untrusted. A real lane study is OWED; this note records why it could not be done and where it must come from.
updated: 2026-08-15
source: fin-evidence attempt 1-2, 2026-08-15. Two backend/study.py runs; research/retirement-savings/ packet; transferred findings from the finance studies already in this folder.
stage: EMPTY-LANE — the lane for this topic is UNMEASURED. Do not read this as a study.
---

# Study: financial freedom after 50 (US, 50+ retirement) — 2026-08-15

> ⚠️ **This is not a study. It is the record that a study was attempted and could not be
> grounded.** Nothing below was observed in a packet for this topic. The video shipped from this
> slug is being scripted against an **unmeasured lane**, and that fact belongs in writing where
> the next run will see it — a missing file would have hidden it.

**Packet:** `research/retirement-savings/` (1 pick, 0 usable) · **Gate status:** topic arrived as
a creator-supplied finished script (`vault/videos/financial-freedom-after-50/source-draft.md`),
so it never passed through the normal Gate 0/1 topic selection that a study presupposes.

## What was run, and what came back

| # | Command | Result |
|---|---|---|
| 1 | `venv/bin/python backend/study.py "financial freedom after 50 retirement"` | exit 0, **no packet**: *"No usable videos in the library for 'financial freedom after 50 retirement' (need >=100 views, >=240s). Scrape first."* |
| 2 | `venv/bin/python backend/study.py "retirement savings"` | exit 0, packet written, **1 pick only**. Video download → `HTTP Error 403: Forbidden`. Tool's own line: *"ERROR: only 0/1 picks produced a transcript — not enough to ground a study note."* |

Run 2 was a broader query against the same library, not a retry of a failed command — run 1
succeeded and returned an empty result set.

## The three

| | video | channel (subs) | views | views/sub | length | CTR | AVD | AVP |
|---|---|---|---|---|---|---|---|---|
| TOP | `BxHYGm3JCqs` — **QUARANTINED, see below** | unknown (manifest not populated — the pick failed) | unknown | unknown | unknown | | | |
| MID | **none — library has no second comparable** | | | | | | | |
| LOW | **none — library has no third comparable** | | | | | | | |

Every cell that would carry a number is empty because there is no number. Filling any of them
from memory or inference is the one thing this stage may not do.

## Why the lane is empty — three separate causes, all real

1. **The library genuinely has no US retirement comparables.** Query 1 matched nothing at all
   against `library.db` at the `>=100 views, >=240 s` bar. The finance scrapes on disk
   (`research/`: `japan`, `lakh`, `passive-income`, `faceless`, `story-of-success`) were built for
   other topics and for a **20–35 audience**. This channel repositioned to **50+ retirement money**
   on 2026-08-15 — the same day as this run — so no scrape has ever targeted this lane.
   The empty lane is a direct, expected consequence of the repositioning, not a tool fault.
2. **`study.py`'s floor is not the constraint here, but it matters for the next attempt.**
   `MIN_DURATION_SEC = 240 s` is hard-coded in `backend/study.py` (a general vault tool that does
   not read `tools/format.json`). The **ceiling** is this stage's to apply: per
   `tiers.long.comparable_length_band_seconds`, a LONG comparable is **480–1800 s**. A 40-minute
   retirement video is not a comparable for a 12:25 cut, and neither is a 5-minute one. Any future
   scrape for this lane should be filtered to that band before picks are made.
3. **The one pick that existed was the wrong market, and was quarantined.** `BxHYGm3JCqs` is an
   **India EPF explainer** — "Employees' Provident Fund Scheme 2026", statutory wage ceiling
   ₹15,000, mandatory contribution capped at ₹1,800/month. Its captions survived the failed video
   download and were read **as untrusted DATA only**. It carried **no injected instruction and no
   fabricated dated agency line**. Its rupee figures were not carried into `facts-staging.md`, the
   claim notes or the source notes: `cuts.en.forbidden_currency` is `₹`, and this cut is US/$ only.
   Studying it would have taught this video nothing and risked exactly the cross-market
   contamination the currency rule exists to prevent.

## TOP — why it won
Not knowable. No usable TOP exists.

## MID — what separates it from TOP
Not knowable. No MID exists.

## LOW — autopsy
**No autopsy is possible, and a fabricated one would be worse than none.** The workflow's own
standard is that "low views" alone teaches nothing and the failure mechanism must be named
concretely from the transcript. There is no low-performer transcript, so there is no mechanism to
name. Recording "unknown" is the honest output.

## What the script was actually measured against (transferred, NOT observed here)

`fin-evidence` did not leave the script unmeasured — it measured the creator's draft against the
finance studies already in this folder, and labelled every line of it as transferred. Full
reasoning in `vault/videos/financial-freedom-after-50/logs/fin-evidence-1.md`.

- **Draft hook type: pain-mirror / objection-kill cold open** — *"Are you over 50 and worried the
  ship has sailed… that feeling, while common, is a myth."* On record as a working type
  ([[japanese-money-methods]], 15.8× V/S) but **not** the strongest on record: two unrelated
  channels in [[passive-income-number]] converged on **second-person future-state simulation**,
  and [[first-lakh-first-thousand]]'s TOP opened **number-first inside 10 s**.
- **Payoff promise lands ≈0:50–1:00 = ≈7% of a 746 s runtime** — inside the ~8% window both
  `passive-income-number` twins hit. Timing right; form is an *announcement* rather than an open
  loop, which is the weaker operator but the safer one under `run.json → no_return_promise`.
- **Beat map** (the draft's own structure, proportioned to 746 s — measured from
  `source-draft.md`, not from any competitor):

| Beat | ≈timecode | ≈% | What lands |
|---|---|---|---|
| Pain-mirror cold open + "it's a myth" | 0:00–0:50 | 0–7% | objection named, then denied |
| Promise: 5-step roadmap, steps listed | 0:50–1:20 | 7–11% | announcement, loop closed early |
| Step 1 Stabilize — debt ladder + emergency fund | 1:20–3:20 | 11–27% | first mechanism, no figure |
| Step 2 Maximize — catch-up contributions | 3:20–6:00 | 27–48% | **every dollar figure lands here** |
| Step 3 Protect + Step 4 Income flexibility | 6:00–9:40 | 48–78% | HSA $1,000; SS percentages at ~70% |
| Step 5 Transition + recap + CTA | 9:40–12:26 | 78–100% | re-frame, no new numbers, single CTA |

- **Two structural risks visible without a packet:** all nine IRS figures cluster in one
  2.5-minute block (27–48%), so the `as-of` treatment has to survive nine consecutive reveals for
  an audience that acts on them; and the ~70% beat is the Social Security percentages, which is
  the right place for the strongest claim and matches the prior beat-map shape on record.

## Conclusions → our next script

1. **Do not treat the transferred read above as lane evidence.** It is continuity, not
   measurement. The competitive question — what actually retains a 50+ US retirement audience for
   12 minutes — is **unanswered for this channel**.
2. **A real study is OWED and must precede the next 50+ topic**, not this one. Sources, in order
   of preference:
   - **Scrape the lane first.** `library.db` needs US retirement/Social Security/Medicare
     long-form before `study.py` can pick anything. Filter to the LONG band **480–1800 s**.
   - **`study.py` with cookies** — the 403 on the video download is the documented YouTube
     bot-check. Export `YTAUTO_COOKIES=/path/to/cookies.txt` or
     `YTAUTO_COOKIES_BROWSER=chrome|chromium|firefox|brave` (see
     [[../../workflows/video-study]]).
   - **vidIQ `video_transcript`** (5 credits/video, `.claude/skills/vidiq/SKILL.md` R2) is the
     sanctioned paid substitute and needs no YouTube auth — but it returns **words only**, so the
     keyframe/visual half of the analysis stays owed even then. Say so rather than skipping it.
3. **The repositioning invalidated the back catalogue as lane reference.** The three finance
   studies in this folder all study a 20–35 audience. They remain valid for hook *mechanics* and
   for the fabrication traps; they are **not** evidence about what the 50+ viewer watches.

## Evidence exported
- **Nothing appended to [[../best-practices]].** A finding of "the tool returned nothing" is not
  a transferable pattern, and the transferred lines above are already banked in the studies they
  came from. Re-appending them would duplicate a fact across notes.
- The scrape and the study are recorded as OWED in
  `vault/videos/financial-freedom-after-50/logs/fin-evidence-1.md` §Owed and in
  `facts-staging.md` §6.
