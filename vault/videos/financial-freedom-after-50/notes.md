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

## Chapter loop — chapters 1 and 2 locked (2026-08-15)

Both locked at **round 2 of 3**. Stopped here at creator request; chapter 3 not started.

- **ch1** — 11 scenes / 68.672 s / 2061 f. Round 1 REWORK, 4 P1: a payoff frame that named
  "five steps" over an uncountable fanned stack, two staircases back to back (s9/s10), an
  `arch-d art-off` pair without `centred` leaving a `.brule` over an empty 656 px band, and a
  closer crushed to unreadable dark wood.
- **ch2** — 17 scenes / 108.667 s / 3260 f. Round 1 REWORK, 4 P1: the chapter's only figure
  frame painted its source line **1.4 s before the figure**, a B&W puddle where the bucket
  metaphor should have continued, a *snowman* where the line demanded motion, and the SHOVE
  closer crushed by the grade over a well-lit source.

### Durable rulings, for chapter 3 onward

1. **A frame that names a count must show the count.** ch1's storyboard assumed a photograph
   carried "five steps"; it did not, and no drawn layer was budgeted to say so. The fix that
   worked was not the card chain the reviewer asked for — it was wooden numerals `1 2 3 4 5`,
   countable at 1.5× on a phone. **The reviewer logged its own ask as the wrong ask**, so a
   later pass does not restore it.
2. **Sound-off is per LINE and per ADJACENCY.** Both chapters lost a blocker to two adjacent
   frames saying the same thing (two staircases; a "dark passage to light" repeat). Only the
   *promoted* sheet read caught the second — the candidate read did not.
3. **A citation may never precede its figure.** Non-negotiable for this audience: a source
   stamp over a hole where the number should be is a claim of verification with nothing
   verified. Cue order is `pop(num)` then `fade(foot)`, ~1 s apart.
4. **Crushed closers are a grade defect, not a fetch defect.** Both chapters' final scenes came
   back near-black over correct, well-lit sources. The lever is per-image brightness (exposed
   by the grade) plus a wider ken — not a re-pick, and never a per-scene `filter:`.
5. **A monochrome source cannot be graded.** `grayscale(.32)` has nothing to take from a B&W
   jpg, so a "dim run" is fixed at the source image, not in the stack. Check candidates at 1:1
   for colour before promoting.
6. **`storyboard-en.md` §6's `ctr: N` rows are not reliable** — `.arch-d .stack` is
   `align-self:start`, so the chip row never occupies the lower band §6 assumes. Judge each
   scene against the rendered band. Both locked chapters ship `centred`.
7. **`data-framings` is COMMA-separated.** §3's DOM example writes it space-separated;
   `check_build` splits on `,` only and `float()` crashes on the space form.
8. **`per-line-chapters` has no `body_class` entry** in `tools/format/fin-build.json` (only the
   three short-tier entries exist). Both chapters applied the empty default — `class="cut-en"`,
   no `swiss-band`, no `rail`. Chapter 3 must match or the two disagree.
9. **Restate `window.__timelines = window.__timelines || {};`** in every chapter project or the
   layout and contrast passes die on `missing_timeline_registry`.

### Known-good, do not touch
ch2's s23 photo swap and its s18 icon (`assets/icons/step-arrow-down.svg`, written back to the
shared kit) were named the best-built things in the chapter.

### Owed, none of it blocking
- **`ken()` has no horizontal lever.** `assets/js/motion.js:133-137` hard-codes
  `xPercent: -2.5 → +2.5` and `plateKen()` is scale-only, so a review note asking to pan a
  `.bg` horizontally is unimplementable as written. Use `background-position` or inline
  brightness instead — both exist.
- **CC BY-SA attribution has no route to the description.** ch2's s22 (Rocky Mountain NP snow
  roller, @commons, CC BY-SA 4.0) carries its credit row in `assets-ch2/final/CREDITS.txt`, but
  nothing in `tools/format/*.json` requires credits to reach the video description. Attribution
  is a licence *condition*, not a courtesy. Close it as a `fin-package` default, not a note on
  this cut.
- **`composition_heavy_overlay_count_high`** (34 overlays in ch2, ~52 expected in ch3) is not a
  render failure — every layer paints, `blackdetect` is clean over the full chapter. It costs
  only on scenes whose source is already low-key. Fix those scenes; never thin the stack globally.
- **Two flat runs survive as should-fixes**, neither blocking: ch1 00:23–00:31 (an 8.271 s dark
  chess hold after the chapter's loudest frame) and ch2's s19–s21 (16 s of three pale paper
  close-ups, which the already-authorised s21 roll-down arrow closes on its own).
- **`blockframe.css` ~184–192: the stray paragraph after `known_benign. */` is live CSS** and
  eats the `.stamp.warn` rule — red-on-red for every cut that ships a red verdict stamp. One
  `/*` fixes it; `hyperframes check` cannot see it.
