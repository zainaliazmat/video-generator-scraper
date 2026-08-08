---
summary: The shipped sound layer for chapter-based finance cuts — the creator-approved mix levels and why raising the voice gain cannot make the voice louder, the cue-density decision that fixed "scene changes read as silent", and the verification doctrine that a cue is only proven by the encoded file. Code homes are tools/audio/{kit,cues,mix,verify_cues}.py and their docstrings; this note is the rationale and the decisions, and does not restate the cue-to-helper mapping.
updated: 2026-08-06
source: designed and shipped across japanese-money-methods hi+en (2026-08-04/05/06). Levels A/B'd with the creator on -en ch1 and approved. Every number below was measured off encoded files, not off a mix log.
stage: ADOPTED — the standing sound system for MEDIUM/LONG chapter cuts
---

# Sound for chapter cuts

> **Code homes, which win over this prose:** `tools/audio/kit.json` (the seven
> sounds and their bound motion helpers), `tools/audio/cues.py` (the generator
> and the full rule list, in its docstring), `tools/audio/mix.py` (gains and the
> duck), `tools/audio/verify_cues.py` (the proof). This note owns the
> **decisions** and the **evidence**. It deliberately does not copy the
> cue-to-helper table — that lives in `cues.py` where it is executed.
> Related: [[design-chapter-archetypes]] · [[design-finance-blockframe]] ·
> [[finance-audit-2026-07-29/07-sound]] (the 2026-07-29 research that preceded this).

## The problem this solved

The first shipped full-cut lists carried **one `transition` in ten minutes** —
about one cue per 26 seconds. That is why scene changes read as silent. The fix
was never new sounds; the kit was already designed and is still seven sounds.
The fix was **density**: the shipped cuts now run about one cue per 3.4 seconds
(187 cues on -hi, 188 on -en).

**Density hand-authored across sixteen chapters is sixteen chances to bind a
sound to a motion that is not in the file.** So it is generated. `cues.py`
derives every cue from a motion call that actually exists, at that call's own
time, via `kit.json`'s helper column.

**Why the generator was trusted:** it reproduces the creator-approved `-en` ch1
list *exactly* — 22 of 22 cues, same times, same names — and that list was
hand-authored and signed off before the generator existed. A generator that
matches a human-approved reference on a real chapter is worth more than one that
looks reasonable on all sixteen.

## The levels — creator-approved after an A/B, now the defaults

```
BED_GAIN   = 0.128   (was 0.16 — 20% down)
VOICE_GAIN = 1.2
SFX_GAIN   = 1.2     (rides WITH the voice, deliberately)
```

Three things about this are not obvious and cost a round to work out:

1. **`VOICE_GAIN` cannot make the narration absolutely louder.** `loudnorm.py`
   pins the programme to −14 LUFS and the voice dominates that measurement, so
   raising it makes the voice stand *prouder over the bed* and nothing more.
   Measured: voice **+0.01 dB** absolute, bed **−3.51 dB**. If someone asks for
   "louder narration", what they can actually be given is a quieter bed.
2. **`SFX_GAIN` tracks the voice on purpose.** Leaving it at 1.0 while the voice
   rose would have pushed the whole kit ~1.6 dB quieter *against* the narration —
   the one thing the creator asked not to change. Measured after the change:
   −0.08 dB median across all 22 cues, i.e. unchanged relative to speech.
3. **The duck's control tap stays at the raw voice level.** `threshold=0.03` is
   calibrated against it, so gaining the control input would change how hard the
   bed ducks as a side effect of a level change that was supposed to be about
   level only.

**Roughly half the cues are inaudible in isolation, and that is the design.** At
these levels about 10 of 22 read "flat" on an envelope test: they land under
speech, where a −22 dBFS sound is felt rather than heard. The creator was offered
a +6 dB variant that scored 22/22 on the test and **chose these levels instead.**
Do not "fix" the flat half.

## Verification — the doctrine, not just the tool

**Verify sound from the encoded file, never from the mix log.** `mix.py` prints
what it *placed*. It cannot know whether ffmpeg's `adelay` landed the file,
whether a cue fell past the runtime, or whether `amix` ate it. The only evidence
that a sound is in the video is the video.

### The mistake worth not repeating: a test that cannot fail is not evidence

The first cue check compared the **mix** against the **voice-only master** and
passed 188/188 with "+58 dB lifts". The mix carries a continuous music bed and
the master carries none, so *every* window in the mix reads louder than the same
window in the master — whether a cue landed there or not. It was measuring "has a
music bed". **It would have passed a mix with zero SFX in it.**

The fix is the technique now in `verify_cues.py`: build a **reference mix with
the cue list emptied** — same bed, same gains, same duck — and subtract.
`mixed − reference` IS the SFX bus, so "quiet" and "absent" stop being
confusable. Generalised: *when a control and a treatment differ in more than the
one thing you are testing, you are not testing that thing.*

Read the output this way: a cue flat where the **reference is loud** is masked by
speech and is fine. A cue flat where the **reference is quiet** is missing —
nothing was covering it.

## Traps

- **A chapter project's `assets/` may be a SYMLINK to the shipped cut's
  `assets/`.** `-hi` ch1 and ch2 were, which is why their `audio.json` was
  byte-identical to the full cut's — it *was* the full cut's, one file behind
  three paths. Writing a chapter cue list there silently overwrites the full-cut
  list. `cues.py` now refuses to write through a symlinked `assets/` at all.
  **Check whether a project's `assets/` is a link before writing anything into
  it.**
- **`loudnorm.py` only rewrote `FINAL-` → `PUBLISH-`.** Feeding it `MIXED-` —
  which is what its own documented pipeline order does — made destination equal
  source and it refused to overwrite the master in place. A correct guard firing
  on correct usage. It now accepts both prefixes.
- **Never put a `transition` on a HOLD.** A hold is the same object with one
  continuous zoom across two lines (the storyboards name theirs explicitly). A
  whoosh there announces a change that is not happening. This is also the single
  rule that makes the generator match ch1 rather than over-firing.
- **A scene that swaps its photograph mid-line takes no fallback `reveal`** — the
  swap already carries its own `transition` cue.

## Where the numbers landed

| | -hi | -en |
|---|---|---|
| SFX cues placed | 187 | 188 |
| present in the encode | **187 / 187** | **188 / 188** |
| also lifting the programme | 54 % | 52 % |
| `PUBLISH` loudness | −14.08 LUFS · −1.63 dBTP | −14.20 LUFS · −1.69 dBTP |

The ~half that lift matches the prediction from the levels almost exactly, which
is the result that says the design is behaving as designed rather than by luck.
