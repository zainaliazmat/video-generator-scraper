---
summary: Handover for resuming the passive-income-number run. Rewritten 2026-08-09 after a second session-limit stop. Session file — delete once folded into the milestone note.
updated: 2026-08-09
source: this run's run.json, stage logs and chapter reviews.
---

Resume with:

```
/finance-video --resume passive-income-number
```

**`vault/videos/passive-income-number/run.json` is authoritative and it is large.** Read, in
this order: `rulings_binding_on_both_cuts` (two entries — they govern every remaining
chapter), `chapters` (never `stages`, see below), `owed`, `incidents`,
`tool_fixes_this_session`, `method_learned`.

⚠ **Read chapter progress ONLY from `chapters`.** The per-cut entries in `stages` are
written by `pipeline_check mark --chapter N` and record ONE CHAPTER passing, not a cut.

## Where it stands

**Locked: hi ch1, en ch1, en ch2.** Three of thirteen.

| | hi (7 chapters) | en (6 chapters) |
|---|---|---|
| locked | ch1 | ch1, ch2 |
| in flight | ch2 — re-draft + re-measure | ch3 — verify/replace s27, s31 |
| assets done | ch3 | — |
| not started | ch4–7 | ch4–6 |

Phase 1, and script/audit/voice/storyboard for both cuts, were already done and verified.

## The two things in flight, both recovering from a session-limit stop

Neither killed agent wrote a log, and both left an artifact newer than the thing
describing it. Details in `run.json.incidents.session_limit_2026-08-08_1849`.

1. **hi ch2 — the s16 re-frame is IN PLACE and good; its measurement is GONE.** A
   792×445.5 serial-safe window bounding the *ken sweep union* (not one frame), as a
   `background-size`/`background-position` on the `.bg`, so the file is untouched and its
   md5/manifest/CREDITS all stand. The slot's own note says the re-measurement lives in
   `fin-build-hi-ch2-5.md` — **that log does not exist.** The margin must be re-measured:
   s16 led s12 by +1.053 median but only **+0.494 photograph-only**, and a 2.42× window on
   a different region changes that completely.
2. **en ch3 — s27 and s31 were replaced, unverified, and the composition predates them.**
   Both `.src` notes describe **white-dominant subjects**, which the locked grade cannot
   carry. Treat as suspect, not as done.

## The rulings that govern everything remaining

Both were settled at ch1/ch2 gates and both cost several rework rounds to reach.

- **Ground temperature is assigned by argumentative weight, not mood** — the darkest
  longest-held frame must be the chapter's most substantive beat. **The lever is always
  the photograph**, never the ground, scrim or grade (no per-scene override exists).
- **The payoff frame must satisfy all four:** sound-off pass · top quartile on **median**
  (`ceil(N/4)` floored at 3) · #1 or #2 on **p10** · non-negative median step in. The old
  "most legible = #1 of N" was retired as the wrong instrument — it made compliance depend
  on how good the other frames were, and flipped on a 1.4-point error.
- **p90 is retired for ranking legibility.** It gets the *sign* of joints wrong. Median
  ranks; report `p90 − p50` beside it. **Near-zero spread is not a credit.**
- **The sound-off gate runs first, binary:** with the type covered, can a viewer name a
  concrete object? A frame failing it is ineligible to lead regardless of its numbers.
  Reason of record: *every purely numerical measure tried on this run eventually crowned
  an empty frame* — a blank notebook page, a pale-sky field, a closed notebook cover.
- **The staircase is the ladder's metaphor, never its inventory** (hi ch1 CEO, §8 upheld).
- Tank through-line: **hi** = the Indian stepped water tank now at hi ch2 s11; **en** =
  aged brass lever tap + industrial pipework, with s46/s47/s57 needing *the lever visible
  at a different angle plus flow*. Do not import one cut's constant into the other.

## The single most expensive lesson

**The frame is not the file, and a prediction is not a measurement.** Source-side and
predicted numbers were wrong about the composed result **five times**, by 7–8 points, in
both directions — and once a declared 1.4-point lead became an 8.0-point measured deficit.
Predictions and contact sheets *shortlist*; only the encode settles. Flag any margin under
~3 points as unsafe.

## Pipeline work landed this session (all committed)

`76195ff` `9570170` `e539320` `f6c3b4d` `bb2f92c` `d1437d1` `199b0a6` `6e3b40f`

- **`tools/check_vo_frame.py`** (new) — the in-page rate assert scans on-screen tokens, so
  it could not see a VO line *speaking* money over a bare frame. Caught two real hi ch2
  violations the frame assert passed clean.
- **`tools/tts/clauses.py`** (new) — cascade offsets measured from the voice instead of a
  fixed `+1.10`. en ch3 is the first chapter built on it.
- **`tools/audio/cues.py`** ×4 — read `dur` where it meant `stagger`; hardcoded the music
  bed; `cue_min_gap_seconds` had **no reader anywhere in the tree**; could not read
  speech-anchored cascades.
- **`tools/pipeline_check.py`** — refuses to mark a stage on a log older than that stage's
  artifact. Two false positives of my own along the way, both caught against real logs.
- **`chapter-design.css`** ×2, **`motion.js`** ×1 — `.scene.centred` resets that missed
  `arch-b` children; `fade()` animating to a hardcoded opacity 1.
- **`vault/knowledge/stock-photo-sourcing.md`** — prop-money serials (check whether TWO
  notes share one, not whether one is valid) and derived crops orphaned by a re-fetch.

One claim was **corrected rather than patched**: the comma-descender fix targets
`.arch-b .mega`, and style E's rungs are `.huge`. Zero `.mega` elements exist in these
chapters. Clearance is real but incidental — fin-render measures it per chapter.

## Still owed

- `owed.cue_rung_5_does_two_jobs` — a cue-model change, deliberately not made mid-run.
- `owed.overlay_count_in_the_assembled_master` — ~162 heavy overlays in the single
  assembled render. A decision before the full render, not before chapter review.
- `owed.real_study_packet` — `study.py --ids JiuVKaO2a6c Jn3N9OzSY1c` once yt-dlp cookies
  exist. The current study's visual half is recorded MISSING, not faked.
- `vidiq_packaging_pass` — 13 credits against a ~35-credit close-out pass, resetting
  2026-08-29. Ration it, defer the title lock, or run one market only.
- hi ch1's s3 is a European tea service, accepted. **s80's callback must be re-read
  against it before ch7 is briefed** — two European tea services book-ending an INR cut is
  a different and worse problem than one in the middle.
