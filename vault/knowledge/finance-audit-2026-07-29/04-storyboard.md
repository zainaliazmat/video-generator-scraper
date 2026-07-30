# 04 — Storyboard, scene architecture, pacing & time

Scope: the storyboard document, scene structure, the timing contract, cue placement.
Not covered here: script wording, colour/type, imagery sourcing, sound.

Every claim is tagged **FACT** (a spec, a source line, a rendered artifact, a measured
number) or **UNVALIDATED** (a belief about audience response). No analytics exist for
any video on either channel, so nothing about viewer behaviour can be a FACT.

Primary artifacts read:
- `vault/videos/good-debt-vs-bad-debt/storyboard-en.md`, `storyboard-hi.md`
- `vault/videos/credit-history/storyboard-en.md`
- `vault/videos/good-debt-vs-bad-debt/src/en/index.html` (shipped)
- `studio/videos/credit-history-en/index.html` + `build.mjs` (built 2026-07-29, newest)
- `vault/templates/storyboard-template-finance.md`, `vault/knowledge/design-finance-blockframe.md`
- `.claude/agents/fin-storyboard.md`, `fin-build.md`, `fin-voice.md`, `fin-render.md`, `fin-audit.md`
- `tools/pipeline_check.py`, `tools/format.json`, `tools/archive_cut.py`
- all `vault/videos/*/logs/fin-{voice,storyboard,assets,build,render}-*.md`

---

## 1. Is the storyboard the single source of truth?

**FACT: no. It is a pre-build proposal, and nothing ever reconciles it with the build.**

`storyboard-en.md` for good-debt declares 16 image slots (9 bg + 7 cut-ins) and cue
rows for `#s1cut` (+3.3, exit +8.9), `#s5cut` (+14.7), `#s6cut` (+8.5, exit +13.0),
`#s8cut` (+2.0, exit +5.0). The shipped `src/en/index.html` contains only `#s3cutA`,
`#s3cutB`, `#s4cut`. Four cut-ins and eight cue rows were never built. The storyboard
was never updated; the archived "SPEC" describes a video that does not exist.

Same on the newest cut, worse: `vault/videos/credit-history/logs/fin-build-en-1.md`
records **6 cut-in cues removed** plus 5 further deliberate divergences (s3 exits moved
+15.4 → +14.0, s8 handoff moved, `×` U+00D7 absent from the font subset so `#s9d` ships
`3x RATE`).

This is not the build agent going rogue. `fin-assets` runs *after* `fin-storyboard` and
correctly drops images it cannot source cleanly (`fin-assets-en-1.md`: 66 Pixabay
fetches, 4 cut-ins dropped rather than faked — brand marks, faces, hash collisions).
The defect is that the drop never travels back into the storyboard, and no gate notices.

### FACT: nothing verifies the composition against the storyboard

`tools/pipeline_check.py:check_build()` asserts exactly five things:
1. no `src=`/`href=` pointing at `http(s)://`
2. a root `data-duration` exists
3. at least one `<section>` with timing exists
4. root duration ≈ last scene end (±0.5s) and ≈ `timing.json total` (±0.5s)
5. scene count == `timing.json` line count

It never reads the JS `S` map, never reads the `<audio>` rows, never opens the
storyboard. `fin-audit` — the only adversarial stage — runs **before** `fin-storyboard`
in the pipeline order (`vault/videos/credit-history/run.json`: script → audit → voice →
storyboard → assets → build), so it cannot ever see a storyboard. Its check #8
nonetheless says *"the storyboard's colour table must not argue against the script's
thesis"* — auditing an artifact that does not exist when it runs.

### FACT: `.claude/agents/fin-build.md` contains a false claim

Line 36: *"The four copies must agree; `pipeline_check` asserts it."* It does not.
A composition with a correct root duration and a corrupted `S` map — every animation
firing against the wrong scene start — passes `pipeline_check check build` green.
Design doc §6 names exactly this failure mode ("updating three of four passes every
check and ships a video whose animations fire against the old timeline") and then
nothing implements the check.

The real defence today is the per-project `build.mjs` generator, which derives all four
from `timing.json`. That is a convention, not a gate — and good-debt's generator was
written *"(scratchpad, not committed)"* (`fin-build-hi-1.md`) and no longer exists.

### Load-bearing fields vs decoration

**Load-bearing** — consumed downstream, changes the artifact:

| field | evidence |
|---|---|
| Timing table (clip / scene dur / scene start) | copied into all four homes; verified byte-exact below |
| Element IDs + per-scene DOM list | the build emits exactly these IDs |
| Cue offsets | **FACT: the shipped JS matches the storyboard's declared offsets to 0.01s on every cue in good-debt-en.** The storyboard *is* the timeline. |
| Image slot table + query | becomes `manifest.json`, consumed by fin-assets |
| Colour semantics table | fin-build logs frame-by-frame verification against it; credit-history's anti-drift note demonstrably stopped a red-reuse |
| `tint`, `ken` direction | emitted verbatim |
| Deliberate placeholders (hero integers) | honoured — storyboard said `$9,496`, build recomputed and shipped `$9,506` |

**Decoration** — written every time, read by nobody, never verified:

| field | why it's dead |
|---|---|
| **Cue class `A` (anchored) / `F` (fixed)** | **FACT: zero representation in any output.** Both compile to a constant `S.sN + <literal>`. No code path anywhere in the repo treats an anchored offset differently. The column exists to support a feature that was never built (§3). |
| "lands on «word»" column | no artifact consumes it; nothing checks the cue landed on the word |
| Simultaneous-element counts ("peak = 5 ✓") | hand-computed prose; no checker counts visible elements at time *t* |
| Chip char checks (≤22) | hand-counted prose; `pipeline_check` never counts a chip |
| Sign-off checklist | self-attested; good-debt-en shipped with "No image hash reused" **unticked** |
| `-en` divergence table | genuinely good reasoning, but "zero divergences is suspicious" is an honour system — nothing enforces it |

---

## 2. The timing contract — verified, then attacked

### Verification (FACT — `vault/videos/good-debt-vs-bad-debt/src/en/index.html`)

`scene_duration = 0.4 + clip + 1.0` holds on all nine: s1 `0.4 + 17.371 + 1.0 = 18.771`.
Cumulative starts hold; s9 ends `161.221 + 17.361 = 178.582` = root `data-duration`
= `timing.json total`. `audio data-start = scene_start + 0.4` on all nine;
`audio data-duration` = the measured clip. The JS `S` map equals the nine `<section>`
`data-start`s. All four homes agree.

**One deviation, documented and correct.** Three scenes' `data-duration` were
regenerated as `next_start − this_start` (s2 11.248→11.249, s3 23.082→23.081,
s8 17.100→17.099) because `timing.json` rounds `scene_start` and `scene_duration`
to 3dp *independently*, so the naive formula produces a 1ms
`overlapping_clips_same_track` error in the hyperframes checker. **Both cuts of
good-debt hit this independently, and credit-history hit it again** — it is now encoded
at `studio/videos/credit-history-en/build.mjs:17`. **FACT: neither the design doc §6 nor
the storyboard template mentions the butt-join rule**; both still state the naive
formula as the generation rule. Three builds have paid for the same rediscovery.

### Is the flat 1.0s tail dead air nine times? (FACT, measured)

Padding is **12.60s of the 178.58s runtime — 7.1%** (3.6s lead-in + 9.0s tail).
Spoken VO totals 165.98s. Identical proportion across all six cuts (6.5–7.5%).

Time after each scene's **last animation event** (good-debt EN):

| scene | dur | last cue | dead tail | largest new-info gap | between |
|---|---|---|---|---|---|
| s1 | 18.77 | 16.60 | 2.17 | **6.20** | `#s1q` → `#s1r1` |
| s2 | 11.25 | 8.40 | 2.85 | 2.60 | `#s2c` → `#s2d` |
| s3 | 23.08 | 20.80 | 2.28 | **7.20** | `#s3sub` → `#s3good` |
| s4 | 25.64 | 20.40 | **5.24** | 5.30 | `#s4good .tag` → `#s4bad` |
| s5 | 20.05 | 17.30 | 2.75 | 3.40 | `#s5k` → `#s5r1` |
| s6 | 17.36 | 13.30 | 4.06 | **6.70** | `#s6h` → `#s6f1` |
| s7 | 27.97 | 25.10 | 2.87 | **7.00** | `#s7r1` → `#s7r2` |
| s8 | 17.10 | 12.60 | 4.50 | 3.70 | `#s8rule` → `#s8sub` |
| s9 | 17.36 | 16.00 | 1.36 | 6.60 | `#s9d` → `#s9cta` |

**28.08s (15.7% of runtime) sits after the last animation event of its scene.**
The final 1.0s of every scene is both silent (VO has ended) and motionless but for ken —
**9.0s, 5.0% of the video, guaranteed dead.**

Not all of it is waste: at a scene boundary the tail is a beat before a hard cut. Two
places where it is waste:
- **s9's CTA.** `#s9cta` enters at +15.40 of a 17.361s scene → **1.96s of screen time**
  for the only ask in the video, 1.0s of it in silence. (FACT)
- **s4 / s8 / s6**, which hold 4.06–5.24s past their last cue mid-argument.

### Metronomic? (FACT)

Across **6 videos × 9 scenes = 54 scenes**, every single scene opens its first cue at
exactly **+0.40** and closes with exactly **1.0s** of tail. Zero variation. The scene
rhythm is a literal constant-period grid; only the middles differ.

### Variable pacing, deterministically — yes, cheaply

The tail is a single constant, `format.json scene.tail_seconds`. It participates in
exactly one equation. Because `scene_start` is recomputed cumulatively, changing one
tail shifts everything downstream automatically and consistently — **nothing else in the
system needs to know**. Two options:

- **(a) per-scene tail from the storyboard.** Optional `tail` per line in `timing.json`
  (default 1.0): 0.4 on momentum beats (s2 roadmap, s8 action), 1.6 where a punch needs
  air (s7, s9). `check_voice` already computes `lead + duration + tail` on line 185 —
  it would read the per-line value instead of the constant. **~20 lines** across
  `format.json`, `tools/tts/batch.py`, `build.mjs`, `pipeline_check.py`.
- **(b) derive it, no new data.** `tail = 0.4` when the next scene opens on a slam
  (stamp/pop), `1.2` when this scene ends on a focal. Deterministic, zero new fields.

Either satisfies "a code pipeline can do it deterministically". The stronger companion
rule: **no scene may end more than ~2.5s after its last cue** — mechanically checkable
from the emitted JS, and it would have flagged s4, s6 and s8 on the shipped video.

---

## 3. The cue-timing stopgap — VERDICT

### FACT: word-level cue timing was never implemented, on any cut, ever.

Direct evidence, `vault/videos/credit-history/logs/fin-build-en-1.md` (2026-07-29, the
newest cut):

> **Every anchored cue is still char-interpolated** from the storyboard; no
> faster-whisper refinement ran (whisper is not on this stage's allowlist).

**The structural reason:** `fin-build.md`'s Bash allowlist is `npm run check`,
`npm install`, `npx hyperframes snapshot`, `node …` — `venv/bin/python` is not on it, so
faster-whisper is *literally unrunnable* in the only stage that writes cue times. The
only stage that may run it is `fin-render` (`fin-render.md:21`), which runs **after** the
build and cannot change a cue.

Every storyboard since needs-vs-wants declares the intent and leaves it as an unfinished
placeholder — `storyboard-en.md:381`: *"Anchored cue offsets are char-interpolated
intent — refine with faster-whisper word timings at build."* Six cuts, six placeholders,
zero implementations.

**One cut did it — before the agent pipeline existed.** `emergency-fund-en`, rebuilt by
hand 2026-07-27: *"per-scene VO cued from faster-whisper word timestamps"*
(`vault/index.md:93`; recipe at `vault/skills/hyperframes_production.md` §5a). The
technique is proven on this machine and was then **not carried into the pipeline**.

### How much does on-the-word cueing actually matter? (quantified)

**Clip-level rate error is already solved** — storyboards are derived from measured
`timing.json`, not estimates. For scale, the raw estimate error is large: good-debt-en
en5 measured **−3.42s (−15.5%)** against the nominal rate; credit-history-en measured
**16.11 c/s vs the 15.0 in `format.json` (+7.4%)**. All of that is corrected today.

**Intra-clip drift is the open problem, and it is small.** Char interpolation assumes a
uniform character rate; the real error comes from punctuation pauses, which I measured
as **13–19% of every clip's duration** (real en VO text + measured clip lengths).
Modelling each cue with a standard ElevenLabs pause budget (sentence 0.42s, comma 0.16s,
em-dash 0.22s) over 17 anchored cues on en1/en2/en3/en5/en7:

| clip | chars / clip | pause budget | worst cue drift |
|---|---|---|---|
| en1 | 289 / 17.371s | 3.22s (19%) | **−0.36s** (`#s1q`) |
| en2 | 152 / 9.848s | 1.32s (13%) | −0.18s |
| en3 | 287 / 21.682s | 3.24s (15%) | +0.22s |
| en5 | 331 / 18.651s | 3.18s (17%) | −0.22s |
| en7 | 410 / 26.567s | 3.82s (14%) | +0.24s |

**Worst −0.36s; mean |drift| ≈ 0.19s.** The reason it's small: drift is
`p·(k − (c/C)·N)` — it cancels whenever sentence lengths are even, which these scripts
are (fin-script writes short declarative lines). The pathological case is a very short
sentence early followed by a long one — en1's *"It feels safe. It's a trap."* is exactly
that, and it produces the worst number in the set.

**Independent corroboration:** `fin-voice-en-1.md` measured en1's interest clause at
~13.2s; the storyboard char-interpolated it at **13.1** — **0.1s error on the single
most timing-critical cue in the video** (the audit's ≤15s trap-proof gate).

**Verdict: not worth building as specified.** A graphic landing 0.2–0.35s off its word
is at or under the threshold where a reveal reads as "off". It is not what is hurting
these videos; the 7-second dead patches (§4) are two orders of magnitude bigger. The
design doc's claim that drift "is worst on Hindi" is untested but plausible (wider
delivery variance, different char→phoneme mapping) — and now bounded: the error cannot
exceed the clip's pause budget, which is measurable per clip and is 13–19% on English.

### If you build it anyway — cost, and a cheaper route

- **Full version:** add `venv/bin/python` to fin-build's allowlist; one script running
  faster-whisper `word_timestamps=True` over the 9 mp3s → `assets/voice/words.json`;
  `build.mjs` resolves each cue's `lands on «phrase»` to a word start instead of a char
  fraction, falling back to char-interp on no match. **~80 lines + an allowlist edit.**
  Runtime ~30–60s per cut on `small int8` — `fin-render` already does this exact pass
  (447 words / 31 segments on credit-history-en).
- **The lazy route that removes ~all of the modelled error:** `tools/tts/batch.py`
  already has every mp3 and already shells out to ffprobe. Have it piggyback one
  `silencedetect` pass per clip and write sentence boundaries into `timing.json`. Anchor
  each cue to its nearest sentence boundary + a within-sentence char fraction — the
  entire modelled drift lives at sentence boundaries, so this removes it. **~15 lines in
  `batch.py` + a resolver in `build.mjs`. No new dependency, no model download, no
  allowlist change.**
- **The contradiction that decides it:** `fin-render-en-2.md` (credit-history, today)
  concluded in writing that *"faster-whisper word timestamps cannot resolve 0.1 s on this
  audio, so whisper is used for content only… placement is measured with
  `silencedetect=n=-45dB`, which is exact to the sample."* That finding is about clip
  **onset** measurement — a stricter problem than in-clip cue placement, so it does not
  by itself disqualify whisper for cueing. But the pipeline has already established that
  silencedetect beats whisper for timing on this audio, and **design doc §6 has not
  absorbed it.**

---

## 4. Scene count and shape

**FACT (good-debt EN):** 9 scenes / 178.58s = **19.84s mean scene**; longest 27.97s.
Across all six blockframe-9 cuts scenes run 10.5–31.1s; the longest ever shipped is
needs-vs-wants-en s7 at **31.08s**.

But "one scene" ≠ "one frame". Counting **new-information events** only (an element
actually appearing: `rise` / `pop` / `popEach` / `fade` / `fill` / `countUp`; `pulse` at
1.06–1.12× and `breathe` at 1.035× are sub-perceptual and excluded):

| cut | events | s per event | gaps > 3s | worst gap |
|---|---|---|---|---|
| good-debt EN | 65 | 2.75 | 24 | 7.20s |
| good-debt HI | 63 | 3.10 | 28 | **9.10s** (s4) |
| credit-history EN | 72 | 2.41 | 16 | 5.50s |
| needs-vs-wants EN | 78 | 2.17 | 17 | 8.40s |

**The mean cadence is already fine. The variance is the defect.** 16–28 gaps per video
exceed 3s and the worst run 6–9s. (credit-history, the newest, is measurably the best of
the four — 16 gaps, worst 5.50s — so the pipeline is already improving on this axis.)

### FACT: the "no static frame beyond ~2s" rule is satisfied by ken alone, and ken is slowest exactly where it's needed most

`ken` has a **fixed amplitude** (1.0 ↔ 1.16 = 0.16 scale) spread over the **whole scene**,
so its velocity is inversely proportional to scene length:

| | shortest scene | longest scene |
|---|---|---|
| good-debt EN | s2 11.25s → **1.42 % scale/s** | s7 27.97s → **0.57 % scale/s** |
| credit-history EN | s2 10.73s → **1.49 % scale/s** | s7 28.15s → **0.57 % scale/s** |

The longest, densest, most numerically demanding scene gets **2.5× less motion per
second** than the shortest, calmest one. That is the exact inverse of what pacing wants,
and it is why the 7.00s gap in s7 is a genuinely static-reading frame.

**Deterministic fix that doesn't touch the bleed:** `.bg { inset: -8% }` gives 16% extra
width, which supports scale up to ~1.16 exactly — so you cannot simply raise the
amplitude without showing edges. Instead, for any scene > ~20s run ken as **two opposed
half-length moves** (in, then out). Same 0.16 amplitude, **double the velocity**, no
bleed change — and the direction reversal at the midpoint is itself a perceptible beat
that lands right where the current dead patches are. ~6 lines in `build.mjs`.

### Sub-scene beats — the mechanism already exists

`fin-build-hi-1.md` ("Layout fix during the snapshot pass") describes two `.stack`
layers pinned to the same grid cell (`grid-area: 1/1`) so a scene can hold two
self-centring phases. good-debt s5/s6/s7/s8 and credit-history s3/s5 already use it.
**A "scene" is already sometimes two beats — but only where a snapshot defect forced it.**
The cheap change is to make the phase-swap *mandatory* for any scene over ~20s rather
than a bug fix discovered late.

### B-roll cut-ins as pacing devices — the format has them and keeps losing them

**FACT:** 4 of 7 storyboarded cut-ins dropped on good-debt-en; 6 of 8 on
credit-history-en. `fin-assets` is right to drop them (Pixabay's deterministic top hit
for an abstract concept returns brand marks, faces and hash collisions — "snowball" →
skiing child; "card statement" → Mastercard in a pocket). But the consequence is that
**the format's only non-typographic pacing device is the one thing it reliably fails to
source.** credit-history's build already improvised the right answer — *"its cut-in was
dropped at the asset stage; fin-assets prescribed a pulse here rather than an unrelated
photo"* — so the storyboard should stop planning cut-ins it cannot source and plan a
*typographic* second beat instead, which never fails to source.

### What comparable videos do (UNVALIDATED — weak sources)

WebSearch surfaced only SEO/content-marketing pages (virvid.ai, fluxnote.io,
framesail.com, increditors.com, humbleandbrag.com), not primary research. The
convergent heuristic across them: **change something visually every 3–5s** (some say
5–7s); educational long-form averages ~40–55% percentage-viewed; ~33% of viewers leave
in the first 30s. None of them measure a format like this one. Treat as folklore, not
evidence. What they emphatically do **not** support is "9 scenes is wrong" — they
support "no 7-second gap".

---

## 5. Where does this format lose people? (all UNVALIDATED)

No retention curve exists for any video on either channel. This maps *measurable
structural defects* onto the 9 beats; the ranking is by the size of the defect I can
measure, not by any observed drop-off.

| beat | window | measurable defect (FACT) | structural fix (UNVALIDATED that it helps) | owner |
|---|---|---|---|---|
| **s1 hook** | 0–18.8s (the 33%-leave window) | 6.20s gap between `#s1q` (+3.30) and `#s1r1` (+9.50) — one headline holds while the VO says "It feels safe. It's a trap." | move a second element into that gap using the existing phase-swap; needs no new asset | fin-storyboard |
| **s2 roadmap** | 18.8–30.0s | the only scene with **zero** >3s gaps — and the only scene that promises instead of paying | it is a table of contents. Highest-risk beat to keep at all; consider cutting it so the payoff starts at ~19s | fin-script + fin-storyboard |
| **s3 concept** | 30.0–53.1s | **7.20s** gap (`#s3sub` +4.90 → `#s3good` +12.10), under a `breathe` on an element that exits mid-breathe | phase-swap the scene | fin-storyboard |
| **s4 classifier** | 53.1–78.7s | 5.30s gap **and** 5.24s after the last cue; densest scene gets the calmest bg *and* (via the ken bug) the slowest motion | constant-velocity ken + a third phase | design doc §5 + fin-build |
| **s5 mechanism** | 78.7–98.8s | fine — 7 events, worst gap 3.40s | — | — |
| **s6 action** | 98.8–116.2s | 6.70s gap; 4.06s dead tail | tail rule (≤2.5s past last cue) | fin-storyboard |
| **s7 the math** | 116.2–144.1s | **worst stretch in the video: 7.00s with nothing new, at 127.7–134.7s, while the VO says "It's barely moved"** — the frame illustrates its own line | this is the payoff scene and should be the busiest: split into 2–3 sub-beats keyed to the three figures | fin-storyboard |
| **s8 do this today** | 144.1–161.2s | 4.50s dead tail | tail rule | fin-storyboard |
| **s9 recap + CTA** | 161.2–178.6s | **SUBSCRIBE on screen 1.96s**, 1.0s of it silent | CTA at ~+11 over the still-visible recap chips; longer tail on the last scene only | fin-storyboard + format.json |

Plus one global: **54 consecutive scenes across 6 videos with an identical +0.40 open and
1.0s close.** Whatever else is true, the format currently has no rhythmic variation at
the scene level at all.

---

## 6. The five highest-leverage changes

1. **[FACT] Make `check_build` assert the four timing homes + the storyboard's element IDs.**
   `fin-build.md` claims it already does; it does not. Today a corrupt `S` map ships
   green — the exact failure the design doc warns about. Parse the `S = {…}` literal and
   the `<audio>` rows (one regex each), compare against `timing.json`; then diff the
   storyboard's declared `#id` set against the emitted HTML and print every ID
   declared-but-not-built. That single diff would have surfaced all four dropped cut-ins
   on good-debt and all six on credit-history at build time.
   **Cost ~25 lines.** Owner: `tools/pipeline_check.py` + one-line correction to
   `.claude/agents/fin-build.md`.

2. **[FACT] Promote `build.mjs` to `tools/scaffold/build.mjs`.**
   The generator that enforces one-source-of-truth is re-invented every video:
   good-debt's was written *"(scratchpad, not committed)"* and is gone; credit-history's
   (682 lines, already carrying the butt-join rule and a hard self-check on the hero
   integers) lives in a gitignored dir. `fin-build.md` step 1 points the next build at the
   previous **`index.html`**, not at the generator — so the mechanics get re-derived from
   the output every time. Every other change below has to live in this file.
   **Cost: move + parameterise.** Owner: `tools/scaffold/` + `.claude/agents/fin-build.md` step 1.

3. **[FACT] Constant-velocity ken (two opposed half-moves on scenes > 20s).**
   Measured: the longest scene gets 0.57 %/s and the shortest 1.42 %/s, so the
   "no static frame beyond ~2s" guarantee is weakest exactly where the new-information
   gaps are longest (7.0–9.1s). Halving each long scene's ken doubles its velocity
   without exceeding the `inset: -8%` bleed, and puts a direction change in the middle of
   the dead patch. **Cost ~6 lines + one line in the design doc §5.**
   Owner: `vault/knowledge/design-finance-blockframe.md` §5 + fin-build.

4. **[FACT] Per-scene tail, and a hard "no scene ends >2.5s after its last cue" rule.**
   12.60s (7.1%) is fixed padding, 9.0s of it trailing silence; 28.08s (15.7%) sits after
   the last animation of its scene; the CTA gets 1.96s. `check_voice` already computes
   `lead + duration + tail` — make `tail` an optional per-line field (default 1.0) and add
   the last-cue rule, which is mechanically checkable from the emitted JS and would have
   flagged s4, s6 and s8 on the shipped video. **Cost ~20 lines.**
   Owner: `tools/format.json` + `tools/tts/batch.py` + `build.mjs` + `fin-storyboard`.

5. **[FACT] Retire the `A`/`F` cue-class column, and stop storyboarding cut-ins the asset
   stage can't source.** The anchored/fixed distinction has **zero** representation in any
   output — both compile to a constant literal — and exists to support the whisper feature
   that was never built. Meanwhile 4/7 and 6/8 storyboarded cut-ins were dropped, leaving
   cue rows in the archived "SPEC" for elements nobody built. Replace the planned cut-in
   with a planned *typographic* second beat, which never fails to source.
   **Cost: a template edit.** If you want the timing feature instead, take the
   silencedetect route (§3), ~15 lines — not faster-whisper.
   Owner: `vault/templates/storyboard-template-finance.md` + `.claude/agents/fin-storyboard.md` §3.

---

## 7. Contradictions with what the vault currently documents

1. **`.claude/agents/fin-build.md:36`** — *"The four copies must agree; `pipeline_check`
   asserts it."* **False.** `check_build` never reads the JS `S` map or the `<audio>` rows.
2. **`design-finance-blockframe.md` §6 + `storyboard-template-finance.md`** state
   `scene_duration = 0.4 + clip + 1.0` as the *generation* rule. The rule that actually
   ships — rediscovered independently on three builds — is
   `duration = next_scene_start − this_scene_start`; the documented formula produces a 1ms
   `overlapping_clips_same_track` failure. Undocumented in both places.
3. **`design-finance-blockframe.md` §6** prescribes faster-whisper word timings.
   **`vault/videos/credit-history/logs/fin-render-en-2.md` (2026-07-29)** concludes the
   opposite for this audio: *"faster-whisper word timestamps cannot resolve 0.1 s… placement
   is measured with silencedetect."* (Different problem — onset vs in-clip — but the doc has
   not absorbed the finding.)
4. **`.claude/agents/fin-audit.md` check #8** audits *"the storyboard's colour table"*, but
   fin-audit runs **before** fin-storyboard (`run.json` stage order). **No stage audits the
   storyboard, and no stage compares the build to the storyboard.**
5. **`design-finance-blockframe.md` §5 rule 2** — *"No scene may hold a static frame beyond
   ~2s."* Satisfied **only** by ken, whose measured velocity on the longest scenes is
   0.57 % scale/s, while new-information gaps reach **7.0–9.1s**. The rule is true by
   letter and false by intent.
6. **`vault/index.md:93`** records emergency-fund-en as cued from faster-whisper word
   timestamps — the only cut ever to do it, and it predates the agent pipeline. Every
   storyboard since declares the intent; no pipeline build has ever done it. The vault
   reads as though it is the standard.
7. **`tools/format.json cuts.en.chars_per_second: 15.0`** — measured **16.11** on
   credit-history-en and **16.64** on good-debt en1. Consistently ~7% under Brian's real
   rate. It drives the audit's ±10% budget gate and fin-voice's 1.3× cost guard, so the
   error biases scripts *short* every time. (`cuts.hi` 12.5 not separately verified here.)
