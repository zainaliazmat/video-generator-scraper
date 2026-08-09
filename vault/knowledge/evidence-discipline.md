---
summary: The cross-cutting rules about what counts as proof in this pipeline, learned the expensive way across japanese-money-methods. Not about design or sound — about how a check can report green while the thing it names is broken, and what to do instead. Read before writing any new check, and before trusting a stage that says it passed.
updated: 2026-08-06
source: japanese-money-methods hi+en, sessions of 2026-08-04/05/06. Every rule below is written from a defect that actually shipped or that actually cost hours, named in place.
stage: ADOPTED — standing rules for every pipeline stage and every new check
---

# Evidence discipline

> **BOX — the ten rules. Each body section is the shipped defect that taught it.**
> 1. A test that cannot fail is not evidence.
> 2. Check what a finding SUPPRESSES, not just whether it is benign.
> 3. Assert against the artifact that ships, not against a side-file.
> 4. "Locked" means reviewed, not correct.
> 5. A "reuse the other cut's file" instruction is not a verification.
> 6. Verify attribute-by-attribute, never by total.
> 7. A wait-loop watching only for the output file cannot see a dead render.
> 8. A review finding that contradicts the plan's own device is a finding about
>    the review.
> 9. Judge a long master from the encode, not from `check`.
> 10. A `fixHint` is the checker's guess at cause, not an observation — bisect the
>    diff first.
>
> **Open the body when:** you are WRITING a new check, or a rule above is about to
> change what you do and you want the case that produced it. Reviewing against the
> ten lines needs nothing more.

The pipeline is mostly automated and mostly unattended, so a check that reports
green is the *only* thing standing between a defect and the upload. Across this
project several checks reported green over real defects. These are the patterns
that produced that, generalised.

## 1. A test that cannot fail is not evidence

The first SFX verifier compared the mix against the voice-only master and passed
**188 of 188** cues with "+58 dB lifts". The mix carries a continuous music bed
and the master carries none, so every window read louder whether a cue landed
there or not. It measured "has a music bed". **It would have passed a mix with
zero SFX in it.**

**The rule:** when the control and the treatment differ in more than the one
thing under test, you are not testing that thing. Build the control to differ in
*exactly* one variable — here, the same mix with the cue list emptied, so
`mixed − reference` is the SFX bus and nothing else. See [[design-chapter-sound]].

**The habit that catches it early:** before trusting a passing check, ask *what
input would make this fail?* If you cannot name one, the check is decoration.

## 2. Check what a finding SUPPRESSES, not just whether it is benign

The one entry ever added to `format.json known_benign` was wrong, and it cost
four cuts their browser checks. The reasoning — "the render looks right, so this
lint error is a static-analysis false positive" — was *true*. What it missed is
that a lint **error** makes `hyperframes check` skip the layout and contrast
passes entirely, so those four cuts shipped with WCAG and layout never actually
run.

**The rule:** "the output looks fine" does not establish that a finding is
benign. Establish what the finding *turns off*. `known_benign: []` is the correct
state.

## 3. Assert against the artifact that ships, not against a side-file

`check_assets` asserted image attribution by iterating `manifest.json`. A late
image round wrote 34 new photographs into the `-en` cut without updating the
manifest — so they were not merely unlisted, they were **unchecked**: the loop
never reached them and the licence assertion silently did not apply. The orphan
message that did fire read as bookkeeping ("absent from manifest") rather than as
"this photograph is on screen with no attribution". All 34 were in a rendered,
machine-checked master. (Repaired 2026-08-06; the check now also reads
`index.html`.)

**The rule:** anchor an assertion on the thing that carries the consequence. The
composition is what renders and what carries the licence exposure; a manifest is
a convenience that a later stage can leave behind. A side-file can go stale
without anyone noticing — the shipped artifact cannot.

**Corollary — a copy operation must carry the provenance with it.** Reusing
`hi/sNN.jpg` into the other cut as `sNN-hi.jpg` moved the pixels and left the
credit row behind. Attribution is a licence condition, not metadata.

## 4. "Locked" means reviewed, not correct

`-hi` ch3 was creator-approved and out of scope. It was reopened because
cross-checking the `-en` fix caught a factual error in it: scene s28 sat under
*"Japan was not always a nation of savers"* over a **European cobbled street**,
and had done since it was approved.

**The rule:** when a cross-cut or cross-stage comparison contradicts something
already signed off, the signed-off thing is a **suspect, not an authority**.
Approval records that someone looked; it does not record that they were right.

## 5. A "reuse the other cut's file" instruction is not a verification

The editor that flagged the wrong-country photograph offered
`reuse hi:.../hi-ch3/assets/img/s28.jpg` as the fallback. That fallback was taken
**without opening the file**. It was md5-identical to the -hi cut's own s28 — and
it is *the same European square*. The fallback was the defect.

**The rule:** a filename and a slot are not a photograph. An instruction naming a
file to reuse is a *pointer*, and the pointer has to be dereferenced by eye
before it is trusted. This is the same failure as trusting a stock provider's own
caption — see [[stock-photo-sourcing]] on the contact sheet versus the
full-resolution read.

## 6. Verify attribute-by-attribute, never by total

The failure this project keeps producing is a **correct total with every internal
value drifted**: durations that sum to exactly the right runtime while each
internal cut has moved, with the last scene back-solved to close the books. A
total is one number and it hides ninety-one errors.

**The rule:** compare each `data-start`, each `data-duration`, each framing sum
individually against the authority, plus monotonicity. Then separately assert
that each scene's inner HTML is **byte-identical** to its approved source — that
is the check that says nothing was redesigned in transit. (0 differences across
184 scenes is what made the two masters trustworthy.)

Related trap: `data-framings` is checked for its **sum**, not for existence, so a
scene can declare two framings, hold one photograph for the whole span, and pass.

## 7. A wait-loop that watches only for the output file cannot see a dead render

The first `-en` master was killed by the ffmpeg encode timeout at 06:00 and the
watcher sat idle until 08:55 — three hours on top of the 90-minute render it was
watching — because it was waiting for an mp4 that no longer had a process behind
it.

**The rule:** break on the **process exiting**, not only on the artifact
appearing. Absence of the output is ambiguous between "still working" and "dead";
the process is not. (The encode timeout itself is a separate standing fact — see
[[design-chapter-archetypes]] on `FFMPEG_ENCODE_TIMEOUT_MS`.)

## 8. A review finding that contradicts the plan's own device is a finding about the review

A CEO review asked for a kicker on a scene the storyboard lists as one of exactly
seven **SOLO** scenes, where SOLO is defined as *"focal alone — no kicker"* and
spread every 12–14 scenes as a deliberate rhythm. A second review independently
made the same ruling about another SOLO scene.

**The rule:** before applying a review blocker, check it against the plan's
declared devices. If it contradicts one, the reviewer did not know about the
device — and the honest resolution is usually to satisfy the *concern underneath*
somewhere the device allows, not to break the device. (Here the missing count
moved to the adjacent non-SOLO scene as drawn marks, rather than being written
into the SOLO scene's copy.)

## 9. Judge a long master from the encode, not from `check`

`hyperframes check` **cannot pass either full master**, and it is not a defect:
`check_runtime_failure: Navigation timeout of 10000 ms exceeded`. The page loads
in 28.7 s and registers its timeline at the correct duration; 92 archetype scenes
with ~100 images do not paint inside the tool's 10 s navigation budget, and
`--timeout` does not raise it.

**The rule:** run `check` on **chapter projects**, where it is fast and
meaningful, and judge the assembled master from the encoded file — runtime
against `timing.json`, cue presence, dissolves at the joints, no black runs. Do
not chase a green `check` on an artifact the tool cannot load, and do not treat
its failure there as a finding.

## 10. A `fixHint` is the checker's guess at cause, not an observation — bisect the diff first

Building the japanese-money-methods thumbnail (2026-08-06), a 34-character
`white-space: nowrap` row overflowed its container. `hyperframes check` reported:

```
Layout ✗ t=0s sweep_static [data-composition-id]
  "Timeline did not advance under seek; every green verdict on this run is unreliable."
  fixHint: "Confirm the composition seeks a paused GSAP/CSS timeline under data-*
            timing attributes rather than only autoplaying."
```

Both the message and the hint point squarely at the GSAP timeline. **The timeline
was fine.** Two changes were made on the strength of that hint before anything was
tested — rewriting the tween to animate a real proxy property, then hunting the
clip-visibility mechanism — and both were wrong. The snapshots at 0.5 s and 2.5 s
were provably different frames, which had already disproved "did not advance"
before either fix was attempted.

Bisecting the diff found it in one step: same CSS class + short content → passes;
different class + long content → passes; this class + long content → fails. It was
the width. Dropping 35px/4.5px to 29px/3.2px cleared it.

**The rule:** when a check fails, the first move is to bisect the change that
preceded it, not to act on the error text. Error strings are written for the most
common cause of a code path, and a checker reporting a *symptom class* will name
whichever cause its author saw first. Note this also contradicts the sibling
comment already in that file, which predicts overflow surfaces as
`text_occluded` — **it does, sometimes; it can also surface as `sweep_static`.**
One symptom, two codes, and neither names the width.

Corollary, and the reason this belongs here rather than in a code comment: the
run that reports `sweep_static` marks **every other verdict on it unreliable** —
the 20/20 contrast pass alongside it meant nothing. A misdiagnosed gate does not
just cost time, it silently voids the evidence you thought you had. Same shape as
§2 (check what a finding SUPPRESSES).

---

Related: [[design-chapter-sound]] · [[design-chapter-archetypes]] ·
[[stock-photo-sourcing]] · [[design-finance-blockframe]] ·
`tools/pipeline_check.py` (where most of these become executable)


---

## Records drained from `tools/format.json` (2026-08-09)

Provenance and resolved incidents. `format.json` is the constants file; its own
`_comment` says rationale belongs here, and 47% of it was rationale.

### `qa._vad_note`

Silero VAD reports speech onset LATE and quantised: every onset lands on a multiple of 0.032s (its 512-sample window), and the detector adds a systematic positive bias measured at +0.101s median across 92 lines (japanese-money-methods-hi, 2026-08-01). Subtract this bias before comparing against the 0.1s drift target — raw VAD max on that cut was +0.167s (a false FAIL) against a true residual of 0.068s. Re-measure the bias if the VAD model or window changes.

### `qa._dissolve_note`

Sample transitions at BOTH offsets into the overlap. The incoming .stack rises at start+0.30 of a 0.45s dissolve, so a midpoint frame (start+0.225) lands before the incoming text exists and CANNOT see a double-paint — the exact blind spot that let the missing `.scene` stacking context ship. start+0.38 is inside the only ~0.15s window where both scenes' text can be up.

### `qa._whisper_note`

Do NOT derive per-line drift from Whisper segment starts: `base` merged 92 lines into 173 segments and produced a phantom 7.675s outlier. Use Whisper for COVERAGE (gaps, dropped clips), VAD for onsets.
