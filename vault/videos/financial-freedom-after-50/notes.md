# financial-freedom-after-50 — run notes

## Intake rulings (2026-08-15)

**Creator supplied a finished script, not a topic.** This is the first run where
`fin-script` does not author. The draft lives at `source-draft.md` and the creator's
instruction was verbatim *"yes keep my wordings"*. `fin-script` reformats to VO lines
and chapter headings only. Recorded as the `creator_wording_is_source_of_truth`
constraint so every downstream stage sees it.

**Two tier constants were deliberately overridden, both with the creator's `y`.**

1. **`target_seconds` = 746, not 600.** LONG declares `min_seconds: 600` — a floor,
   not a target (`tiers._tier_seconds_note` says so explicitly). The draft is 11,305
   speakable chars = 1.22× the 9,249-char budget the floor implies. Trimming to the
   floor meant deleting ~18% of the creator's sentences, which contradicts the
   instruction that produced this run. So the target moved to the draft's natural
   length: 11,305/17.57 + 128×0.8 ≈ 746 s ≈ 12:25.

2. **`max_elevenlabs_calls` = 154, not 110.** The protocol derives the ceiling from
   `tiers.long.lines × 1.2` = 110. That would have blocked this cut at the voice
   stage at ~86% of the way through, which is exactly the failure the protocol names
   ("the ceiling exists to catch a runaway loop, not to cap a legitimately long
   video" — hit on japanese-money-methods, 2026-08-01). Derived from the real line
   count instead: 128 × 1.2 = 154. `scene._scene_seconds_note` already states scene
   count is emergent from the script and never a constant, so `lines: 92` was never
   the authority here.

**Style question correctly skipped.** `architecture --tier long` returns
`per-line-chapters` and states the rotation and `architecture_lock` are SHORT-tier
only. Asking the style question at LONG is what produced a run.json claiming
`blockframe-9` on a chapter cut; not repeated.

## Figures to verify (creator-supplied, UNVERIFIED at intake)

Every one of these came from the creator's draft, not from `money-facts-2026.md`.
`fin-evidence` Part B must confirm or correct each against the IRS/SSA primary source,
with the publication date. Nothing here is trusted until it is in `facts-staging.md`.

- 2026 401(k)/403(b) elective deferral limit — draft says **$24,500**
- Age-50 catch-up — draft says **$8,000** (total **$32,500**)
- 2026 IRA limit — draft says **$7,500**, catch-up **$1,100** (total **$8,600**)
- SECURE 2.0 age 60–63 "super catch-up" — draft says **$11,250** (workplace total **$35,750**)
- Roth-mandated catch-up FICA wage threshold — draft says **$150,000** prior-year
- HSA age-55 catch-up — draft says **$1,000**
- SSA early-claim reduction at 62 — draft says **25–30%**
- SSA delayed retirement credit — draft says **~8%/yr**, **24–32%** total at 70
- The 4% rule — draft already frames it as a guideline, not gospel; keep that hedge

## Creator rulings at the script stage (2026-08-15)

`fin-script` reformatted the draft to 124 lines / 7 chapters / 13:24 and handed up two
items it correctly refused to decide alone. Both were put to the creator verbatim.

1. **"For the past fifteen years, I've been in the trenches…" — REPLACED.** The question
   asked was not *which rule wins* but *is the claim true*; the creator confirmed it is
   persona colour, not biography. Replaced with the drop-in that keeps the rhythm and
   drops the credential. `run.json → no_advice_framing` was rewritten to supersede its own
   intake wording, so no later stage re-reads the old "keep it" instruction. **The durable
   lesson: a creator-supplied draft can carry an untrue first-person claim, and
   `creator_wording_is_source_of_truth` does not immunise it. Ask whether it is TRUE, not
   whether it is permitted.** Line count 124 → 123.
2. **Hook-gate hoist — KEPT, creator-approved.** The payoff promise sat at ≈55 s against a
   15 s gate; hoisted verbatim to line 1.3 (11.2 s flat model, ≈12.5 s with pauses, clears
   on both). Zero words changed, position only. Now authorized rather than a deviation, so
   `fin-audit` must not re-litigate it as an unpermitted structure change.

Also applied, none of them optional: two forced factual corrections (the "guaranteed
return from the government" phrasing, and the unsourced "number one fear" superlative),
14 sentence splits at the 144-char line ceiling, 23 joins of short adjacent pairs, a
spoken disclaimer at 3.4–3.5 (23 s before the first dollar figure) and a physical CTA at
7.10–7.12 plus a subscribe ask in 7.15 — the draft had neither and both are mandatory.

## Tool fix — `tools/tts/batch.py` stamped the sample (2026-08-15)

The protocol's own "sample two lines before you voice eighty" step **deadlocked its own
follow-up call.** `batch.py` writes the `.voice` stamp only when `want is None`, so an
`--only` sample on a fresh project left two clips and no stamp; the next invocation then
hit the unstamped-clips guard and refused, and the only ways forward were a manual
`printf` or a `--force` that throws the sample away. The cheap-comparison protocol could
not be followed as written.

Fixed at the default, not the gate (creator rule 2026-07-29): the stamp is now also
written when `prev_voice is None and on_disk <= generated` — i.e. this run produced every
clip in the directory, so it can honestly vouch for all of them. The guarantee is
unchanged; a half-finished full run still leaves no stamp. Covered by a new `--selftest`
case that fails if a fresh-dir sample leaves the directory unstamped. Note for whoever
reads the selftest: a sample run exits **nonzero on purpose** (the verify pass sees 2 of
123 clips), so the exit code is not the thing under test — the stamp is.

## Open

- Chapter split: `fin-script` chose 7 (Intro+Hook, Steps 1–5, Conclusion), matching the
  draft's own sections.
- **Lane is unmeasured.** `fin-evidence` found zero US retirement comparables in the
  library — partly because the channel repositioned to 50+ the same day, so the back
  catalogue does not apply — and the single pick was a rupee-denominated India EPF video,
  quarantined. A real vidIQ lane study is OWED, filtered to the LONG comparable band
  (480–1800 s). This cut is being written against no measured lane; treat its retention
  curve as the first real datapoint.
