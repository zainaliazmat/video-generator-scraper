---
summary: Storyboard for «वो नंबर, जो हर महीने पैसे देता है» hi cut — MEDIUM tier, 78 scenes (one VO line = one clip = one scene), blockframe-9 + the chapter archetype layer. Declares the colour semantics, the archetype row (arch / ground / art / centred) for every scene, the scene DOM with the standing `sN-rate` element that carries the withdrawal rate into every corpus frame, three cue variants on measured `timing.json` offsets, 2 shoves + 1 matched-frame hold, one music bed with a derived cue list, 1 Lottie / 1 icon / 1 stamp / 5 drawn proportions, and 80 image slots. Resolves the 2.6/2.7 14.034s single-photograph breach with a tighter crop and one continuous zoom.
updated: 2026-08-07
source: script-hi.md (fin-script hi attempt 1 + the five fin-audit-hi-1 in-place edits) + studio/videos/passive-income-number-hi/assets/voice/timing.json (measured, 488.222s, 78 lines) + run.json.constraints + knowledge/design-finance-blockframe.md + knowledge/design-chapter-archetypes.md + tools/format.json + tools/audio/kit.json
stage: fin-storyboard, cut hi, attempt 1
---

# STORYBOARD — «वो नंबर, जो हर महीने पैसे देता है» · **hi** cut

**Project:** `studio/videos/passive-income-number-hi/` · **Script:** `script-hi.md`
**Design:** [[../../knowledge/design-finance-blockframe]] — the **dark** system, unmodified,
extended by [[../../knowledge/design-chapter-archetypes]]. Do **not** use
`design-techtooltester` (bright, non-finance).
**Channel:** @cashguruguides ₹ · **Tier:** MEDIUM, per-line chapters (7 chapters, 78 lines)
**Architecture:** **`blockframe-9`** (`run.json.architecture`, = `format.json architecture_lock`).
`body_class` is `""` — no `.rail`, no `.swiss-band`, no panel. Centred stack over a full-bleed
graded photograph, every scene, with the archetype layer deciding where the drawn layer lives.
**Runtime:** **488.222s (8:08.2)** — `timing.json` is the only home for every duration.
**VO:** Harsh `HTUuC7OeeEt6OL5fViVe` · **Scenes:** 78 · **Image slots:** 80 (78 bg + 2 cut-ins),
**80 files**, 79 distinct photographs (`s14.jpg` is a crop of `s13.jpg`'s source — §6).

> **Four things this file is accountable for, from the run's own §3c checklist.**
> 1. Every scene carries `arch` / `ground` / `art` — §7, three real columns, no blanks.
> 2. Every scene carries `has-photo` and a real `.bg` — §9, `photo_free_scene_ratio` = 0.
> 3. **No rail, no chapter title, no scene counter, no slide number** — §3.
> 4. Every duration is `timing.json` verbatim — §7 / §11. Nothing here re-times a scene.

---

## 1. Colour semantics for THIS video (derived from the thesis — mandatory)

The thesis: *a monthly income from a corpus is one division — corpus × rate ÷ 12 — and the
only honest way to say any figure is to say its rate in the same breath. India's published
rate is 3.0%, not the imported American 4%.*

Roles are fixed; meanings are per-video. **This table is the script's post-audit legend
(`script-hi.md` §"Role colour semantics", rebuilt by fin-audit D5 from the per-scene cues).
The cue is authoritative; this is the index.**

| Token | This video means | Because |
|---|---|---|
| `--fund` green `#22c55e` | **the corpus doing its stated job at its stated rate** — the rungs that land: 2.9, 2.11, 3.2, 4.2, 6.2, 6.4, 6.7, 6.10, 7.6 | green marks **arithmetic that closed**, never "safe", never "recommended". The persona rule forbids a pick, so green cannot mean approval — it means the division came out |
| `--warn` red `#ef4444` | **the thing that eats the corpus, or the number that shrinks the target** — a too-high withdrawal rate (5.2, 5.4, 5.5, 5.6), the imported rule and what it excluded (5.12, 5.14, 6.12, 6.13), the failure edge (5.16), the honesty beat (4.6), the internet's inflation of it (3.8) | this video's obstacle is **depletion plus importation**. Red carries both the drain and the borrowed number. **Red never lands on India's 3.0%** |
| `--target` amber `#f59e0b` | **a rate under examination** — 2.6, 2.7, 3.5, 4.7, 4.9, 5.8, 5.10, 5.15, 5.17, 6.6, 6.15, 6.16 | amber is the thing being **weighed**, never the thing being recommended. Every published-rate beat (POMIS 7.4%, PPF 7.1%) is amber precisely because it is price evidence, not a pick. **Amber never lands on the imported 4%** |
| `--pop` orange `#ff5c39` | the call to action | fixed — **exactly once**, s78 (7.8), as the `.cta` block's fill |

**The inversion trap — three prior systems, none of them applies here.** `needs-vs-wants` ran
amber = "wants"; `first-lakh-first-thousand` ran red = "the stretch nobody helps you with";
`japanese-money-methods` ran red = "falsity and drain" and green = "the viewer's own hand".
**Here green is the division closing, red is depletion-and-importation, amber is a rate being
weighed.** Any element that renders 3.0% in red, or the imported 4% in amber, argues against
the script.

**Thesis check** (fin-audit's, carried forward): green never lands on a figure that lacks its
rate · red never lands on India's 3.0% · amber never lands on the imported 4%.

**One role colour visible per scene, ever.** On **34 of 78** scenes no role colour appears at
all (`--muted` kicker + `--ink` focal + `--muted` foot) and that is correct: colour is a
signifier here, not decoration.

**Role colour classes.** Text takes `.fundc` / `.warnc` / `.targetc` / `.popc` — the
**colour-only** forms in `assets/blockframe.css`. Never the bare `.fund` / `.warn` / `.target`
modifiers on text: those are the chip/stamp/billrow border-and-fill forms, and reaching for a
class that does not exist paints white and fails silently.

**Per-scene `--tint`** (scrim layer 1): a scene's role colour at **0.12** alpha — **0.10** for
`--fund` (green reads hotter). **A scene with no role colour carries no tint.** Rule, not a
column.

---

## 2. Audio — one bed, a derived cue list

**Music bed: `bed-resolve`.** The argument is **a habit / a fix**, not a trap or a cost.
Chapter 5 runs in a trap register for 100 seconds and it is the video's most dramatic beat, but
the thesis those seventeen lines serve is constructive: the video closes on *"इस पूरे वीडियो
में कोई भी रक़म अपनी दर के बिना नहीं बोली गई, और यही सबसे ज़रूरी आदत है"* — the habit is the
payoff. The bed is chosen for the video, not for a chapter.

> **Bed length is not a decision and is not flagged here.** `tools/audio/mix.py` feeds the
> ~248 s bed in `laps` times with a 3 s `acrossfade` at each joint and trims to the master's
> duration. There is no dip at 248 s or 496 s. Both storyboards on `japanese-money-methods`
> escalated this as an open decision on 2026-08-01; it never was one, and that escalation is
> retired. **This cut is 488.222 s — do not raise it.**

### The cue list is DERIVED per chapter, not hand-typed

`tools/audio/cues.py studio/videos/passive-income-number-hi-ch<N> --write` emits one cue per
**real motion call**, at that call's own time. This supersedes the ≤10-cues figure in the
storyboard contract, which is a **SHORT-cut** number: creator decision **2026-08-06** retired
the hand-authored ceiling for chapter cuts, because a 24-cue list over ten minutes carries
exactly ONE `transition` and every scene change then reads as silent — *which was the defect
the creator actually reported*. Density is the fix; the discipline lives in what each cue is
**bound to** (`kit.json`'s helper column), not in how few there are.

What this storyboard owns, because the generator cannot derive it:

| Input | Value here | Why |
|---|---|---|
| `HOLDS` | `{("s13","s14")}` | the one matched-frame continuous zoom (§6). A whoosh there announces a change that is not happening |
| `BUZZ` | `("hi","s3"): 0.90` | the kit's only diegetic sound. Legal **only** because s3's frame shows the phone's notification arriving (§8). Nowhere else |
| `COUNTED` | `{}` | **there is no cascade in this cut.** No `chips:` cue exists in the script and none is introduced here, so `layout.cascade` is unused and `cue_min_gap_seconds` holds with no exception |
| `cta` | s78 only | the single `--pop` element of the video |
| `stamp` | s43 only | the one `.stamp` component (§8) |

**Two declared overrides to the generator's priority order:**

1. **s49 (5.12) takes `reveal`, not `hero`.** `4%` is the number this video exists to correct.
   A bass impact glamorises the villain's entrance; the beat's power is provenance, and that
   is paid over the next three scenes.
2. **s24 (3.5) takes no content cue.** `3.0%` there is a *restatement* ("the rate held").
   Hitting a repeat makes a restatement sound like new evidence.

**Declared DRY beats — silence is the choice, not an omission:**

- **s45 (5.8) `7.4%` and s69/s70 (6.15/6.16) `7.1%` / `~12%`.** These are the three rates the
  video refuses to recommend. A `hero` hit *would* recommend one, whatever the foot says. The
  loudest silences in the cut, and they are on purpose.
- **s41–s42 (5.4/5.5), the corpus dying.** The two deepest-red frames run dry: the argument is
  a consequence, and punctuating a consequence turns it into a punchline.
- **Chapter 1 except s3's `buzz`.** The cold open is paid in recognition. Scene joints still
  carry their `transition`; nothing else fires until 2.1.
- **s63 (6.9), the PLFS figure.** The one sourced external statistic. A hit on a citation is
  the sound of a claim being sold.

**Mixed in post, never in the composition.** `assets/audio.json` → `tools/audio/mix.py`
(sidechain duck) → `tools/loudnorm.py` to −14 LUFS. The composition stays voice-only: one
`<audio>` row per line, track index 10.

---

## 3. The frame — DOM, and the standing `sN-rate` element

`<div id="root" class="cut-hi">`. **No body class.** Stage 1920 × 1080, `.scene` padding
`110px 150px` ⇒ content box **1620 × 860**, centred.

**NO RAIL. NO CHAPTER TITLE. NO SCENE COUNTER. NO SLIDE NUMBER.** `format.json
chapter_design.rail` is `false`; the top rail was built and removed at creator request
2026-08-05 and is not to be reintroduced. **The viewer must never be shown that this video is
chapter-based.** Chapters exist for production (build → `fin-editor` → `fin-ceo`, one at a
time) and for the YouTube chapter list — nowhere on screen.

```html
<section class="scene clip arch-b has-photo centred art-off" id="s15"
         data-track-index="1" data-start="80.163" data-duration="6.683"
         data-framings="6.233">
  <div class="field" id="s15-field" style="--f1:#231d17"></div>
  <div class="bg"    id="s15-bg" style="background-image:url(assets/img/s15.jpg)"></div>
  <div class="scrim" id="s15-scrim"></div>          <!-- --tint only when the scene has a role -->
  <div class="stack" id="s15-stack">
    <p class="kicker" id="s15-kick">RUNG ONE</p>
    <p class="sub"    id="s15-rate">at a 3.0% withdrawal rate</p>
    <p class="mega"   id="s15-num" style="font-size:240px">₹10,00,000</p>
    <p class="foot"   id="s15-foot">ILLUSTRATIVE · corpus × 3.0% ÷ 12 — arithmetic, not a forecast</p>
  </div>
  <div class="grain"></div>
</section>
```

**ID scheme: `s<n>-<part>`, n = 1…78 in script order** — `field`, `bg`, `bg2`, `scrim`,
`stack`, `kick`, `stmt` **or** `num`, **`rate`** (§4), `sub`, `foot`, `icon`, `art`, `stage`,
`cta`. This is the skeleton the `-en` cut ports (§12). Line-id ↔ index mapping is the `#`/`line`
columns of §7.

**Copy is NOT restated here.** `bar:`, `stmt:`/`num:` and `foot:` strings live in each line's
cue block in `script-hi.md` and have exactly one home. This storyboard owns the DOM, the
archetype row, the cues, the transitions, the audio, the drawn art and the images.

### The three type registers

| Script field | Class here | Size | Colour |
|---|---|---|---|
| `bar:` | **`.kicker`** | 30 / 800, tracked 4, uppercase | `--muted` |
| `stmt:` | **`.huge`** | **112 / 88 / 76**, by the rule below | `--ink`, or the scene's role class |
| `num:` | **`.mega`** | **240** inline (a ladder value; the 290 default overruns at 12 glyphs — `₹1,00,00,000`) | the scene's role class |
| the rate qualifier | **`.sub` `#sN-rate`** | **40** | the scene's role class, else `--muted` |
| a non-rate qualifier | **`.sub` `#sN-sub`** | **40** | `--muted` |
| `foot:` | **`.foot`** | 26 / 700 | `--muted` |

**Focal size rule — deterministic, keyed on the copy, so it cannot drift when a string
changes.** FinanceSans at weight 900 averages ≈0.58 em advance; usable width 1620 px.

| `stmt:` length | `.huge` inline size | lines |
|---|---|---|
| ≤ 24 chars | **112px** | 1 |
| 25–48 chars | **88px** | 2 |
| 49–89 chars | **76px** | 3 |

**Never below 76.** The longest `stmt:` in the cut is 7.5's 71-char sentence; 76 px × 3 lines =
222 px in an 860 px box, with room for kicker, rate and foot. Every `num:` fits one line at 240
px tabular, `₹1,00,00,000` included (12 glyphs × 0.58 × 240 = 1,670 px — **over 1620**, so the
five-glyph-group crore renders at **200 px**, the next ladder step down that clears; declared
here so the build does not discover it in a snapshot).

**No `.chip` anywhere in this cut, declared.** Every qualifier is a `.sub`, so
`max_chips_per_row` and `max_chip_chars` are satisfied vacuously and the `.row` `flex-wrap`
orphan trap cannot fire.

**Element budget.** Per scene: the photograph (1) + kicker + focal + **one or two** of
rate/sub/foot = **4–5 countable**, against the ceiling of 6 ✓. `.field`, `.scrim` and `.grain`
are grade layers, not scene elements; `sN-bg2` is a cross-fade of the photograph layer, not a
fifth element. **Never `stmt` and `num` together** — where the script's cue block carries both,
the `stmt:` string is the qualifier (`sN-rate` / `sN-sub`, 40 px) and the `num:` is the focal.
The five art-forward scenes reach 5 with the drawn layer and carry no icon.

---

## 4. `#sN-rate` — the rate is a DOM element, not a habit

`run.json.constraints.withdrawal_rate_on_screen`: *"Every corpus figure must carry its assumed
withdrawal/return rate ON SCREEN in the same frame as the number. A number without its
assumption visible is a fabricated promise."* fin-audit found this broken on **two** frames
(5.9 `₹9,00,000`, 7.6 `₹1,00,00,000`) and both were **outside the rung ladder** — a ceiling
frame and an emotional callback. That is where it breaks, because that is where nobody checks.

So the rate stops being a property of a string and becomes **a named element with an id, a
cue and a colour class**:

- **Where the script gives the rate its own qualifier line** (`stmt: at a 3.0% withdrawal
  rate`, on the five rung frames) → `#sN-rate` is that `.sub`, **and it arrives at +1.10,
  BEFORE the corpus lands at +1.90**. The assumption is on screen first and the number arrives
  into it. That ordering is the constraint's strongest possible reading and it costs nothing.
- **Where the corpus and its rate are fused in one sentence** (the workings, the ceiling frame,
  the callback) → `#sN-rate` is an inline `<span>` **inside the focal**, wrapping the rate
  token, carrying the role colour and taking a `pulse` at **+1.90 fixed**. No copy is
  reordered, nothing is printed twice, and there is a node to assert.

**The build assert (`script-hi.md` Build handoff §5, mechanised):** every scene whose rendered
text contains a corpus token — `₹10,00,000` `₹20,00,000` `₹40,00,000` `₹50,00,000`
`₹75,00,000` `₹1,00,00,000` `₹9,00,000` — **must contain an element with id `sN-rate`**, and
that element's text must contain a rate token (`3.0%`, `4%`, `7.4%`). Twenty scenes qualify:

| scene | line | corpus | `#sN-rate` form | rate token |
|---|---|---|---|---|
| s15 | 2.8 | ₹10,00,000 | `.sub` line | `3.0%` |
| s16 | 2.9 | ₹10,00,000 | span in the working | `3.0%` |
| s20 | 3.1 | ₹20,00,000 | `.sub` line | `3.0%` |
| s21 | 3.2 | ₹20,00,000 | span in the working | `3.0%` |
| s25 | 3.6 | ₹10,00,000 → ₹20,00,000 | span on *both at 3.0%* | `3.0%` |
| s29 | 4.1 | ₹40,00,000 | `.sub` line | `3.0%` |
| s30 | 4.2 | ₹40,00,000 | span in the working | `3.0%` |
| s37 | 4.9 | ₹10,00,000 · ₹20,00,000 · ₹40,00,000 | span on *all at 3.0%* | `3.0%` |
| **s46** | **5.9** | **₹9,00,000** | **span on *at 7.4%*** | **`7.4%`** ★ audit D1 |
| s47 | 5.10 | ₹9,00,000 | span in the working | `7.4%` |
| s55 | 6.1 | ₹50,00,000 | `.sub` line | `3.0%` |
| s56 | 6.2 | ₹50,00,000 | span in the working | `3.0%` |
| s60 | 6.6 | ₹1,00,00,000 | `.sub` line | `3.0%` |
| s61 | 6.7 | ₹1,00,00,000 | `.sub` line (the working) | `3.0%` |
| s64 | 6.10 | ₹1,00,00,000 *(foot)* | span on the stmt's *at 3.0%* | `3.0%` |
| s66 | 6.12 | ₹75,00,000 | `.sub` line | `4%` |
| s67 | 6.13 | ₹75,00,000 · ₹1,00,00,000 | **two spans** — `s67-rate` `4%`, `s67-rate2` `3.0%` | both |
| s73 | 7.3 | ₹1,00,00,000 | span in the working | `3.0%` |
| **s76** | **7.6** | **₹1,00,00,000** | **span on *both at 3.0%*** | **`3.0%`** ★ audit D2 |
| s52 | 5.15 | *(no corpus)* | focal is the band itself | `3.0–3.5%` |

★ = the two frames fin-audit caught shipping bare. Both now carry a cued, coloured, asserted
node. **If a later edit shortens either focal, the assert fires — it can no longer fall out
silently, which is exactly how it fell out the first time.**

The rate also appears as the **focal** on nine frames where the number under discussion *is* a
rate (s13 `3.0%`, s24 `3.0%`, s43 `12%`, s45 `7.4%`, s49 `4%`, s53 `3.75%`, s54 `~5%`) or lives
in the kicker (s69 `ASSUMED 7.1% GROWTH`, s70 `ASSUMED ~12% GROWTH`). Those carry no separate
`#sN-rate`; duplicating a rate under itself reads as a defect.

---

## 5. The cue ladder — three variants

Offsets are **relative to `scene_start`** (§7 column `start`, verbatim from `timing.json`), so
every absolute cue time is `scene_start + offset` and is derived, never hand-typed.
`audio_start = scene_start + 0.25` (MEDIUM `lead_in_seconds`).

| variant | scenes | cue 1 | cue 2 | cue 3 | cue 4 |
|---|---|---|---|---|---|
| **A — statement** (default) | 55 | `sN-kick` **+0.30** fixed `rise` 14px | `sN-stmt` **+1.10** fixed `rise` 18px | `sN-rate` span **+1.90** fixed `pulse` — *or* `sN-foot`/`sN-icon` **+1.90** fixed `fade`/`draw` | `sN-foot` **+2.70** fixed `fade` (only when cue 3 was the rate pulse) |
| **B — figure** | 22 | `sN-kick` **+0.30** fixed `rise` | `sN-rate`/`sN-sub`, else `sN-foot`, **+1.10** fixed `rise` | `sN-num` **anchored, floor +1.90**, `countUp` + `pop` | `sN-foot` = **num + 0.80** fixed `fade` (only if the foot did not take cue 2) |
| **D — close** | 1 (s78) | `s78-cta` **+1.10** fixed `pop` | — | — | — |
| — | all 78 | `sN-bg` **+0.00 → scene end** anchored `ken` 1.0 ↔ 1.16 | | | |
| — | 3 scenes | `sN-bg2` anchored `bgSwap` — 0.40 s cross-dissolve of the photograph layer (§6) | | | |

**One declared exception, s43 (5.6).** Its `bar:` is `—` (no kicker) and «बारह परसेंट» is the
**first word** of the line, so a +1.90 floor would put the number 1.65 s behind its own word on
a 4.562 s scene. s43 runs: `s43-num` **anchored +0.60** · `s43-stmt` as the **`.stamp.warn`**
**anchored +3.05** on «चेतावनी» (`stamp` SFX). Gap 2.45 ✓. This is the only anchored cue in the
cut that lands before +1.10, and the only scene with two anchored cues.

**Every gap is ≥0.8 s.** A: 0.30→1.10→1.90→2.70 = 0.80 throughout ✓ · B: 0.30→1.10 = 0.80, and
the floor puts the num at ≥1.90 ⇒ ≥0.80 ✓, foot at num+0.80 ✓ · D: single cue ✓ ·
`first_cue_by_seconds` 0.5: every scene's first content cue is at +0.30 (+0.60 on s43), and
the photograph is up at +0.00 ✓.

**Anchored vs fixed.** The kicker, the stmt, the rate/sub, the foot, the icon and the CTA are
**fixed** — constant regardless of clip length. The `ken` push, every `num` arrival, the s43
stamp and every `bgSwap` are **anchored**: they land on a word and scale with the clip.
**Surplus time from a longer clip goes into the hold after the assembly — never into a
cascade.** Concretely: variant A always finishes at **+2.70** at the latest, so s67 (6.13, the
longest scene at 8.767 s) holds a finished frame for 6.07 s with only the ken push running.
**That is the answer to the "6.13 is tight against the 9.0 ceiling" flag: nothing on that
scene needs a slow reveal, because nothing on any scene does.**

**Anchored cue resolution.** The fractions in §7 are `audio_start + f × clip_duration` with the
target Hindi word named. **`f` is a fallback**: fin-build resolves each against faster-whisper
word timings and uses the fraction only if the word fails to align. Character-offset
interpolation drifts worst on Hindi.

**Track index alternates 1 / 2 by scene parity** (odd → 1, even → 2), because `hyperframes
check` rejects two overlapping clips on one track and every non-final scene overlaps its
successor by 0.45 s. No column needed; it is `1 if n % 2 else 2`.

**`ken` direction is a rule, not a column:** s1 starts `i` (push in) and the direction **flips
at every boundary except s13 → s14**, where s14 continues its partner's push (§6). That yields
`i, o, i, o, …` with one deliberate repeat, and never two *independent* pushes in a row.

**`data-duration` = `timing.json` `scene_duration` + 0.45** on s1–s77; **s78 carries its
`scene_duration` bare**. Root duration is unaffected: **488.222 s**.

---

## 6. The 2.6 / 2.7 hold — 14.034 s on one photograph, resolved

`timing.json` measures **2.6 at 5.998 s and 2.7 at 8.036 s**, and the script has 2.7 hold 2.6's
image. That is **14.034 s on one photograph** against `scene.max_scene_seconds` 9.0 — a real
breach, and `check_build` will catch it. `script-hi.md` Build handoff §7 prescribes the fix and
this storyboard executes it:

| | s13 (2.6) | s14 (2.7) |
|---|---|---|
| file | `s13.jpg` — the pencilled figure on ruled paper, full sheet | **`s14.jpg` — a second, TIGHTER crop of the same source frame** |
| ken | `i`, **1.00 → 1.09** (`plateKen` with explicit endpoints) | `i`, **1.09 → 1.16**, continuing the same direction |
| longest single framing | **5.998 s** ✓ | **8.036 s** ✓ |
| joint | — | `hold` — a 0.45 s dissolve mechanically (`data-duration` unchanged), invisible because the crop changes under it |
| SFX | — | **no `transition` cue** (`HOLDS` in §2): a whoosh announces a change that is not happening |

**Never a self-dissolve back to the same file** — creator rule, firaun 2026-07-23: the same
image across two lines is **ONE continuous zoom**, and cross-fading a file onto itself
flickers. `s14.jpg` is a *different file cropped from the same source*, which is what makes the
dissolve read as a push rather than a flash.

**No other scene breaches.** The longest single scene in the cut is s67 (6.13) at **8.767 s**,
under 9.0 by 0.233 s; s51 (5.14) is 8.506 s and s65 (6.11) is 8.454 s. Six scenes sit in the
8.0–8.8 s band and every one holds a **finished** frame (assembly complete by +2.70, §5), so
the margin is spent on a hold, which is the correct place for it.

**Two real cut-ins**, both because the photograph cannot hold everything the VO names at once:

| scene | line | `data-framings` | swap at | anchored to | second file |
|---|---|---|---|---|---|
| s11 | 2.4 | `3.300,4.266` | **+3.30** | «एस डब्ल्यू पी में» (the second clause) | `s11b.jpg` — the same steel box, a note being drawn **out** |
| s32 | 4.4 | `2.550,5.016` | **+2.55** | «दूध» | `s32b.jpg` — milk and vegetables, which the sacks-and-oil frame cannot show |

Both swaps clear their scene's last text cue (+1.10) by 2.20 s and 1.45 s ✓.

**Emit `data-framings` on all 78 sections.** On the 76 single-framing scenes it is one value
equal to `scene_duration`; that costs nothing and removes any question of whether an absent
attribute means "one framing" or "not declared". Framings always sum to `scene_duration`
(= `data-duration` − 0.45).

---

## 7. Scenes — the archetype row

One row per VO line. `start` / `dur` = `scene_start` / `scene_duration`, **verbatim from
`timing.json`, the only home**; `d-dur` = `dur + 0.45` (s78 bare). Every fixed cue is
`start + offset` from §5.

`arch`: **A** plate · **B** figure · **C** ledger · **D** band.
`ground`: the scene's `--f1` (§10). `art`: `off` · `fwd` (= `art-forward`) · a named layer.
`ctr`: `centred` — the archetype's other side is empty, so `fin-build` drops the plate,
`crule`, `vrule` and `brule`. **`Y` on 70 of 78 scenes, and that is correct on a photo-led cut.**
`trans`: `dis` = 0.45 s dissolve · **`SHOVE`** · `hold` = matched-frame continuous zoom (§6).
`focal`: which of `stmt` / `num` carries the frame, its cue variant, and its single role colour
(`—` = no role colour and no `--tint`).
**Every scene carries `has-photo` and a real `.bg`. There are no exceptions and none may be added.**

| # | line | start | dur | d-dur | trans | arch | ground | art | ctr | focal · var · role | `#sN-rate` | bg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1.1 | 0.000 | 3.961 | 4.411 | dis | A | `#241d15` | off | Y | stmt · A · — | — | `s1.jpg` |
| 2 | 1.2 | 3.961 | 5.816 | 6.266 | dis | A | `#221c17` | off | Y | stmt · A · — | — | `s2.jpg` |
| 3 | 1.3 | 9.776 | 2.550 | 3.000 | dis | D | `#161f2b` | **lottie `phone-notify-credit`** | N | stmt · A · — | — | `s3.jpg` |
| 4 | 1.4 | 12.327 | 4.797 | 5.247 | dis | A | `#1f1b16` | off | Y | stmt · A · — | — | `s4.jpg` |
| 5 | 1.5 | 17.123 | 6.181 | 6.631 | dis | D | `#221c17` | **ticks ★** | N | stmt · A · — | — | `s5.jpg` |
| 6 | 1.6 | 23.304 | 5.842 | 6.292 | dis | A | `#1f1e1c` | off | Y | stmt · A · — | — | `s6.jpg` |
| 7 | 1.7 | 29.146 | 6.599 | 7.049 | dis | B | `#1c2027` | off | Y | stmt · A · — | — | `s7.jpg` |
| 8 | 2.1 | 35.745 | 4.980 | 5.430 | dis | A | `#1c2027` | off | Y | stmt · A · — | — | `s8.jpg` |
| 9 | 2.2 | 40.725 | 6.547 | 6.997 | dis | C | `#191f28` | off | Y | stmt · A · — | — | `s9.jpg` |
| 10 | 2.3 | 47.272 | 6.495 | 6.945 | dis | D | `#161f2b` | off | Y | stmt · A · — | — | `s10.jpg` |
| 11 | 2.4 | 53.767 | 7.566 | 8.016 | dis | D | `#1a1f26` | off | Y | stmt · A · — | — | `s11.jpg` + `s11b.jpg` |
| 12 | 2.5 | 61.332 | 4.797 | 5.247 | dis | A | `#1c2027` | off | Y | stmt · A · — | — | `s12.jpg` |
| 13 | 2.6 | 66.129 | 5.998 | 6.448 | **hold** | B | `#2a2113` | off | Y | **num `3.0%`** · B · target | *(focal)* | `s13.jpg` |
| 14 | 2.7 | 72.127 | 8.036 | 8.486 | dis | B | `#2e2411` | off | Y | stmt · A · target | span `3.0%` | **`s14.jpg`** *(crop of s13's source)* |
| 15 | 2.8 | 80.163 | 6.233 | 6.683 | dis | B | `#231d17` | off | Y | **num `₹10,00,000`** · B · — | `.sub` line | `s15.jpg` |
| 16 | 2.9 | 86.397 | 6.416 | 6.866 | dis | B | `#17291f` | **fwd** + `art-lift` | N | stmt · A · **fund** | span `3.0%` | `s16.jpg` |
| 17 | 2.10 | 92.813 | 5.476 | 5.926 | dis | C | `#1c2027` | off | Y | stmt · A · — | — | `s17.jpg` |
| 18 | 2.11 | 98.289 | 6.678 | 7.128 | dis | C | `#1b3024` | off | Y | stmt · A · **fund** | — | `s18.jpg` |
| 19 | 2.12 | 104.967 | 8.349 | 8.799 | dis | A | `#241d15` | off | Y | stmt · A · — | — | `s19.jpg` |
| 20 | 3.1 | 113.316 | 6.312 | 6.762 | dis | B | `#1c2027` | off | Y | **num `₹20,00,000`** · B · — | `.sub` line | `s20.jpg` |
| 21 | 3.2 | 119.628 | 6.887 | 7.337 | dis | B | `#1b3024` | off | Y | stmt · A · **fund** | span `3.0%` | `s21.jpg` |
| 22 | 3.3 | 126.514 | 5.633 | 6.083 | dis | C | `#221c17` | off | Y | stmt · A · — | — | `s22.jpg` |
| 23 | 3.4 | 132.147 | 5.110 | 5.560 | dis | A | `#241d15` | off | Y | stmt · A · — | — | `s23.jpg` |
| 24 | 3.5 | 137.257 | 4.091 | 4.541 | dis | B | `#2a2113` | off | Y | **num `3.0%`** · B · target | *(focal)* | `s24.jpg` |
| 25 | 3.6 | 141.349 | 8.323 | 8.773 | dis | B | `#1f1e1c` | **fwd** | N | stmt · A · — | span `3.0%` | `s25.jpg` |
| 26 | 3.7 | 149.672 | 6.651 | 7.101 | dis | D | `#1c2027` | off | Y | stmt · A · — | — | `s26.jpg` |
| 27 | 3.8 | 156.323 | 6.051 | 6.501 | dis | C | `#38151a` | off | Y | stmt · A · **warn** | — | `s27.jpg` |
| 28 | 3.9 | 162.374 | 5.528 | 5.978 | dis | A | `#1a1e24` | off | Y | stmt · A · — | — | `s28.jpg` |
| 29 | 4.1 | 167.902 | 5.763 | 6.213 | dis | B | `#1c2027` | off | Y | **num `₹40,00,000`** · B · — | `.sub` line | `s29.jpg` |
| 30 | 4.2 | 173.665 | 7.304 | 7.754 | dis | B | `#1b3024` | off | Y | stmt · A · **fund** | span `3.0%` | `s30.jpg` |
| 31 | 4.3 | 180.970 | 4.327 | 4.777 | dis | C | `#221c17` | off | Y | stmt · A · — | — | `s31.jpg` |
| 32 | 4.4 | 185.296 | 7.566 | 8.016 | dis | C | `#241d15` | off | Y | stmt · A · — | — | `s32.jpg` + `s32b.jpg` |
| 33 | 4.5 | 192.862 | 6.965 | 7.415 | dis | A | `#1c2027` | off | Y | stmt · A · — | — | `s33.jpg` |
| 34 | 4.6 | 199.827 | 7.096 | 7.546 | dis | D | `#38151a` | off | Y | stmt · A · **warn** | — | `s34.jpg` |
| 35 | 4.7 | 206.922 | 7.383 | 7.833 | dis | D | `#2e2411` | off | Y | stmt · A · target | — | `s35.jpg` |
| 36 | 4.8 | 214.305 | 4.875 | 5.325 | dis | C | `#1a1e24` | off | Y | stmt · A · — | — | `s36.jpg` |
| 37 | 4.9 | 219.180 | 6.782 | 7.232 | **SHOVE** | B | `#2a2113` | **fwd** | N | stmt · A · target | span `3.0%` | `s37.jpg` |
| 38 | 5.1 | 225.962 | 4.640 | 5.090 | dis | A | `#1c2027` | off | Y | stmt · A · — | — | `s38.jpg` |
| 39 | 5.2 | 230.602 | 6.678 | 7.128 | dis | B | `#301519` | off | Y | stmt · A · **warn** | — | `s39.jpg` |
| 40 | 5.3 | 237.280 | 5.894 | 6.344 | dis | A | `#251a1c` | off | Y | stmt · A · — | — | `s40.jpg` |
| 41 | 5.4 | 243.174 | 5.110 | 5.560 | dis | D | `#38151a` | off | Y | stmt · A · **warn** | — | `s41.jpg` |
| 42 | 5.5 | 248.284 | 4.980 | 5.430 | dis | D | **`#3b1219`** | off | Y | stmt · A · **warn** | — | `s42.jpg` |
| 43 | 5.6 | 253.264 | 4.562 | 5.012 | dis | B | `#38151a` | off | Y | **num `12%`** + **`.stamp.warn`** · **exception §5** · **warn** | — | `s43.jpg` |
| 44 | 5.7 | 257.825 | 6.834 | 7.284 | dis | C | `#1a1e24` | off | Y | stmt · A · — | — | `s44.jpg` |
| 45 | 5.8 | 264.660 | 6.913 | 7.363 | dis | B | `#2a2113` | off | Y | **num `7.4% p.a.`** · B · target | *(focal)* | `s45.jpg` |
| 46 | 5.9 | 271.572 | 6.364 | 6.814 | dis | C | `#161f2b` | off | Y | stmt · A · — | **span `7.4%` ★** | `s46.jpg` |
| 47 | 5.10 | 277.936 | 8.323 | 8.773 | dis | B | `#2e2411` | **fwd** + `art-lift` | N | stmt · A · target | span `7.4%` | `s47.jpg` |
| 48 | 5.11 | 286.260 | 6.730 | 7.180 | dis | A | `#1c2027` | off | Y | stmt · A · — | — | `s48.jpg` |
| 49 | 5.12 | 292.989 | 5.476 | 5.926 | dis | B | `#301519` | off | Y | **num `4%`** · B · **warn** | *(focal)* | `s49.jpg` |
| 50 | 5.13 | 298.465 | 6.129 | 6.579 | dis | C | **`#0e1c2e`** | off | Y | stmt · A · — | — | `s50.jpg` |
| 51 | 5.14 | 304.594 | 8.506 | 8.956 | dis | C | `#38151a` | off | Y | stmt · A · **warn** | — | `s51.jpg` |
| 52 | 5.15 | 313.100 | 5.894 | 6.344 | dis | C | `#2e2411` | off | Y | stmt · A · target | *(focal)* | `s52.jpg` |
| 53 | 5.16 | 318.994 | 6.233 | 6.683 | dis | B | `#38151a` | off | Y | **num `3.75%`** · B · **warn** | *(focal)* | `s53.jpg` |
| 54 | 5.17 | 325.228 | 5.998 | 6.448 | **SHOVE** | B | `#2a2113` | off | Y | **num `~5%`** · B · target | *(focal)* | `s54.jpg` |
| 55 | 6.1 | 331.226 | 5.215 | 5.665 | dis | B | `#1c2027` | off | Y | **num `₹50,00,000`** · B · — | `.sub` line | `s55.jpg` |
| 56 | 6.2 | 336.441 | 7.096 | 7.546 | dis | B | `#1b3024` | off | Y | stmt · A · **fund** | span `3.0%` | `s56.jpg` |
| 57 | 6.3 | 343.536 | 6.416 | 6.866 | dis | C | `#221c17` | off | Y | stmt · A · — | — | `s57.jpg` |
| 58 | 6.4 | 349.953 | 5.215 | 5.665 | dis | D | `#17291f` | off | Y | stmt · A · **fund** | — | `s58.jpg` |
| 59 | 6.5 | 355.167 | 4.327 | 4.777 | dis | A | `#1f1e1c` | off | Y | stmt · A · — | — | `s59.jpg` |
| 60 | 6.6 | 359.494 | 4.875 | 5.325 | dis | B | `#2e2411` | off | Y | **num `₹1,00,00,000`** · B · target | `.sub` line | `s60.jpg` |
| 61 | 6.7 | 364.369 | 7.383 | 7.833 | dis | B | **`#1d3a28`** | off | Y | **num `₹25,000 / month`** · B · **fund** | `.sub` line | `s61.jpg` |
| 62 | 6.8 | 371.752 | 4.640 | 5.090 | dis | A | `#1c2027` | off | Y | stmt · A · — | — | `s62.jpg` |
| 63 | 6.9 | 376.392 | 7.513 | 7.963 | dis | C | `#161f2b` | off | Y | **num `₹24,217`** · B · — | *(n/a — not a corpus)* | `s63.jpg` |
| 64 | 6.10 | 383.905 | 6.887 | 7.337 | dis | B | `#1b3024` | **fwd** | N | stmt · A · **fund** | span `3.0%` | `s64.jpg` |
| 65 | 6.11 | 390.792 | 8.454 | 8.904 | dis | B | `#1f1e1c` | off | Y | stmt · A · — | — | `s65.jpg` |
| 66 | 6.12 | 399.246 | 7.331 | 7.781 | dis | B | `#301519` | off | Y | **num `₹75,00,000`** · B · **warn** | `.sub` line `4%` | `s66.jpg` |
| 67 | 6.13 | 406.576 | **8.767** | 9.217 | dis | B | `#38151a` | off | Y | stmt · A · **warn** | **two spans** `4%` + `3.0%` | `s67.jpg` |
| 68 | 6.14 | 415.344 | 6.965 | 7.415 | dis | A | `#1c2027` | **icon** (§8) | Y | stmt · A · — | — | `s68.jpg` |
| 69 | 6.15 | 422.309 | 7.435 | 7.885 | dis | B | `#2a2113` | off | Y | **num `≈ ₹19,000 / month`** · B · target | *(kicker)* | `s69.jpg` |
| 70 | 6.16 | 429.744 | 8.167 | 8.617 | dis | B | `#2e2411` | off | Y | **num `≈ ₹10,000 / month`** · B · target | *(kicker)* | `s70.jpg` |
| 71 | 7.1 | 437.910 | 5.528 | 5.978 | dis | A | `#1f1b16` | off | Y | stmt · A · — | — | `s71.jpg` |
| 72 | 7.2 | 443.438 | 4.457 | 4.907 | dis | D | `#1a1f26` | off | Y | stmt · A · — | — | `s72.jpg` |
| 73 | 7.3 | 447.896 | 6.651 | 7.101 | dis | B | `#1c2027` | off | Y | stmt · A · — | span `3.0%` | `s73.jpg` |
| 74 | 7.4 | 454.547 | 7.096 | 7.546 | dis | A | `#221c17` | off | Y | stmt · A · — | — | `s74.jpg` |
| 75 | 7.5 | 461.642 | 7.331 | 7.781 | dis | D | `#1f1e1c` | off | Y | stmt · A · — | — | `s75.jpg` |
| 76 | 7.6 | 468.973 | 6.834 | 7.284 | dis | B | `#1b3024` | off | Y | stmt · A · **fund** | **span `3.0%` ★** | `s76.jpg` |
| 77 | 7.7 | 475.807 | 7.017 | 7.467 | dis | A | `#241d15` | off | Y | stmt · A · — | — | `s77.jpg` |
| 78 | 7.8 | 482.824 | 5.398 | *(bare)* | *(last)* | A | `#33200f` | off | Y | **`.cta`** · D · **pop** | — | `s78.jpg` |

**Row checks.** 78 scenes ✓ · last scene ends 482.824 + 5.398 = **488.222** = root
`data-duration` = `timing.json.total` ✓ · every `start`/`dur` byte-for-byte from `timing.json`,
nothing re-timed ✓ · **2 SHOVE** (s37→s38, s54→s55) ✓ · **1 hold pair** (s13→s14) ✓ · 22 `num`
scenes, none carrying a `stmt` as a second focal ✓ · `--pop` exactly once (s78) ✓ · 20 corpus
frames, 20 `#sN-rate` elements (§4) ✓ · 3 scenes with a second photograph file ✓ · 70 `centred`,
8 with something real on the other side ✓ · **`has-photo` + a real `.bg` on all 78** ✓ · ken
never repeats a direction except across the declared hold ✓ · no scene carries both a foot and
an icon ✓.

**★ Amendment, 2026-08-07 — s5 `art: off → ticks`, `ctr: Y → N`.** Ruled by fin-editor at ch1
round 2 (`logs/editor-hi-ch1-2.md`, correcting its own round-1 position) on fin-assets attempt
5's evidence (`logs/fin-assets-hi-ch1-5.md`). 1.5 names **three** subjects and a **verb** —
बिजली का बिल, राशन, किराया … चुपचाप भरता रहता है — and no photograph of that exists to be
found: 12 candidates across two queries for this file's own "three household bills fanned on a
table" spec cleared nothing (9 under the R−B +40 warmth gate, 5 carrying US dollars on a ₹ cut,
and the only two that passed both gates a red `PAST DUE` shoot that says the opposite of the
line). Neither stock pool indexes a bill as an object, only as an emotion. So the count and the
verb are drawn — three `.icon` marks (bulb · sack · house) each taking a tick in sequence — and
`s5.jpg` stays, the chapter's warmest raw. `ctr` follows `art`: `centred` exists because
`art-off` empties the archetype's other side, and D has its mechanism back. `art: off` on this
row was the file's default (74 of 78), not a declared device, so this is an amendment and not a
device being broken. **1.5 is now ch1's one drawn-art beat besides the Lottie** — a COUNT and a
PROCESS, which is `vector_art.reach_for_it_when` on the merits. Rule 8 holds: the ration mark is
a sack, not a jar, precisely so nothing drawn re-draws the photograph's own object.

### The archetype sequence, read as a rhythm

```
ch1  A A D A D A B
ch2  A C D D A B B B B C C A
ch3  B B C A B B D C A
ch4  B B C C A D D C B
ch5  A B A D D B C B C B A B C C C B B
ch6  B B C D A B B A C B B B B A B B
ch7  A D B A D B A A
```
Totals **A 20 · B 31 · C 15 · D 12**. B-heavy, because almost every beat in this video is a
figure — that is the argument, not a lack of variety.

**Four deliberate holds, each because the scenes are one argument:**

- **ch2 `B B B B` (s13–s16)** — the rate is declared, defended, applied to a corpus, divided.
  Four scenes, one chain of reasoning; the *mechanism* under it changes (a pencilled figure → a
  tighter crop of it → a cash box → a drawn proportion). Varying the layout here would break
  the only through-line the chapter has.
- **ch4 `D D` (s34–s35)** — the water mechanism: where the money comes from, and why the rate
  is therefore kept small. One physical argument across two lines.
- **ch5 `C C C` (s50–s52)** — three documents, one argument: the American paper, what it
  excluded, the Indian paper. The script names this hold explicitly and the archetype doc
  endorses exactly this shape.
- **ch6 `B B B B` (s64–s67)** — the crore meets the salary → that is what the number is → what
  the imported rule would have set instead → what importing it costs. The climax is one
  sentence spread over four scenes.

**Every rung is `B B`** — the corpus named, then its division worked. That regularity is the
ladder made visible: s15/s16, s20/s21, s29/s30, s55/s56, s60/s61.

---

## 8. Vector art — 5 drawn proportions, 1 Lottie, 2 icon scenes, 1 stamp

**The drawn layer appears on five scenes and only ever inside the `.p-b` plate.** Rule 8 is the
test: if you cannot say what the art asserts that the picture cannot, it is `off`. It is `off`
on **72 of 78** scenes, which is the correct density (`design-chapter-archetypes`: "three or
four drawn layers in a twelve-to-fourteen scene chapter is the top of the range, not the
target"). All five are `art-forward` because the point of each is a **PROPORTION** and the
mechanism still wins; the photograph is there to satisfy `image_per_scene`.

| scene | line | motif | what it ASSERTS that the photo cannot | arithmetic (truth_bar) |
|---|---|---|---|---|
| **s16** | 2.9 | `three-percent-sliver` — one solid bar = the corpus, a 3.0% sliver cut from its right end in `--fund`, that sliver split into 12 equal ticks below | **how small 3% is**, and that the monthly figure is that sliver ÷ 12. The photo (a division on a ledger page) states the sum; it cannot state the proportion | sliver = exactly 3.0% of the bar's width; 12 ticks, equal |
| **s25** | 3.6 | `corpus-doubles-rate-holds` — two solid bars, the second exactly 2× the first, with an identical 3.0% band marked on each | **only one side of the equation moved.** The photo (two brass weights) says "different"; it cannot say "exactly twice, at the same rate" | widths 1 : 2 exactly (₹10,00,000 → ₹20,00,000); the band is the same fraction of each bar |
| **s37** | 4.9 | `three-rungs-one-rate` — three solid step bars under one continuous 3.0% rule crossing all three at the same height | **the ladder's geometry and the constant rate.** The photo (three worn steps) shows three; it cannot show 1:2:4 or the rate | widths 1 : 2 : 4 exactly (₹10L / ₹20L / ₹40L) |
| **s47** | 5.10 | `the-ceiling` — a bar rising and stopping hard against a heavy cap line, ₹5,550 at the cap, nothing past it | **that it is a CAP, not a rate.** The photo (a concrete ceiling from below) is a metaphor; the drawing is the measurement | ₹9,00,000 × 7.4% ÷ 12 = **₹5,550** exactly (facts B.2; the secondaries' ₹5,500 is a bad rounding — PART E) |
| **s64** | 6.10 | `they-meet` — two solid bars at true relative width, ₹25,000 and ₹24,217 | **near-equal but NOT equal, and by how much.** The photo (a level two-pan balance) asserts "equal", which is 3.2% too strong | second bar = 24,217 / 25,000 = **96.87%** of the first. State this in the generator comment at the point of edit |

**Build rules for all five** (from `design-chapter-archetypes` §"what a drawn layer has to look
like to survive the encode"): solid fills and strokes ≥9 px, never outline scaffolding · ghost
tracks as filled rects at ~.2, never outlines · `stroke-width` inline, never as an SVG
attribute · **`.p-b` maps viewBox x 1:1 to screen x, so nothing past vx = 800 exists on the
encode** · assemble by **+3.30** so the contact sheet's +2.6 s sample is not a half-built frame
· `.has-photo .art` opacity is `!important`, so a per-scene inline opacity on the `<svg>` is a
no-op — the only levers are the weight and alpha of the elements inside.

**`art-lift` on s16 and s47.** Both sit on a bright still (ruled paper; a bare bulb on pale
concrete) where `.has-photo`'s aperture leaves ink art light-on-light. `art-lift` gives those
two plates their panel back — it darkens **behind** the art only and cannot touch the
photograph outside the plate rect. **The whole-frame darkening lever stays forbidden** (rule 9;
creator rejected it 2026-08-04, *"it fails to black and white"*).

### One Lottie — `phone-notify-credit` on s3 (1.3)

Library reuse, **no fetch**: `assets/lottie/phone-notify-credit.json` (in-house, 2.5 s,
820×300, already used on `japanese-money-methods-hi-ch1 s1`). **No tint** — `index.json` records
it as authored in the system's own palette (`--panel`/`--edge`/`--ink`/`--muted`), and tinting
would push it into a role colour 1.3 has not earned.

- **Why it is additive, not depictive.** The photograph is a phone **face-down** — the design
  system bans a phone-screen photo as a background (it has shipped undetected three times), and
  the script's own cue says the notification must be *"NOT legible"*. The drawn banner is the
  only honest way to state that money **arrived**; the picture is structurally forbidden from
  saying it.
- **The amount is MASKED** (`₹ • • • • •`). Naming a figure at 0:10 would break the open loop
  the whole cold open is built on — the number is withheld until 6.7 — and any rupee figure on
  screen drags the rate constraint with it. Nothing to state, nothing to qualify.
- Stage: `.p-d` band, declared in **pixels** (`left/top/width/height`) with
  `.stage svg { width:100% !important; height:100% !important }` — a stage without pixel
  dimensions renders the art at native size pinned top-left and every check passes.
- Cue: `playLottie` at **+0.30**, simultaneous with the stmt (one arrival, two elements) on a
  2.550 s scene. `buzz` SFX at **+0.90**, when the banner lights — the kit's only diegetic sound
  and legal here precisely because the frame shows the object making the noise.

**One Lottie, not four.** `calendar-20th-circled` was considered for 2.3 ("a fixed amount on a
fixed date") and **rejected on rule 8**: the photograph is already a date circled in ballpoint
on a wall calendar, so a drawn circled calendar over it is the "ghost envelope over a
photograph of an envelope" failure the doc names. The cap is `max_per_chapter: 4` — a threshold
at which you must justify the next one, never a target.

### Icons — s5 (1.5) and s68 (6.14)

**s5 · three marks, ticked in sequence** (amendment 2026-08-07 — see §7's ★ note for why the
photograph could not do this). Three `<svg class="icon">` glyphs in archetype D's band, in the
VO's own order — **bulb · sack · house** (बिजली का बिल · राशन · किराया) — each over its own
`checkbox-tick` box. The row arrives whole at cue slot 3 (**+1.90**), stating the **count**; the
three ticks then `draw()` at **+2.30 / +2.95 / +3.60**, 0.65 s apart, stating the **verb**
(«चुपचाप भरता रहता है»). All three are struck by **+4.05**, so the finished checklist holds
2.13 s and the sheet's +2.6 s sample catches it mid-tick, which is honest. Role: **none** (1.5
carries no `colour:` cue) — plain `.icon` on `--ink`, so nothing asserts a role colour the scene
has not earned. `.band` darkens **behind** the marks; the photograph is never darkened (rule 9).
Glyphs are library files — `light-bulb.svg`, `grain-sack.svg`, `house-door.svg` (drawn for this
scene and written back to `assets/icons/`) and the existing `checkbox-tick.svg`. `icon_first`, so
no Lottie was spent: ch1 still has 3 of its 4 slots free.

**s68 · one icon**

Inline `<svg class="icon">` stroke-drawn by `draw()` at cue slot 3 (+1.90). **Shape: two
opposed arrows through one circle — one leaving it, one entering it.** Role: **none** (6.14
carries no `colour:` cue), so plain `.icon` on `--ink`.

It asserts the **distinction** that the scene exists to make — *withdrawal rate = what you take
out; growth rate = what the corpus is assumed to earn* — which a photograph of a
standing-instruction slip cannot draw. This is the guard neither format twin has, and it sits
one scene before the only two growth figures in the cut.

**No icon sits on a `num` scene** — that scene already has its focal element and
`one_focal_per_scene` caps it at one. **Nothing at all sits on s61**, the video's one big number.

### One `.stamp` — s43 (5.6)

`.stamp.warn`: solid `--warn` fill, `#0d1017` text, `rotate(-4deg)`, `back.out(1.7)`, anchored
at **+3.05** on «चेतावनी». Copy is 5.6's own `stmt:` — *"Not an opportunity. A warning."* — 29
characters, which fits one line inside the pill at 44 px with its padding. This is the video's
most dramatic moment and the only place a verdict slams, so it is the only place the `stamp`
sound has a helper.

> Expect a **contrast finding** on `.stamp`. Design doc §9: the rotated construct reports a
> false failure on a bright fill. **Do not fix it by lightening the text.** `#0d1017` on
> `#ef4444` is genuinely high-contrast; this is the checker misreading the rotation, not a
> defect, and it is not a `known_benign` entry.

### Emoji: none, deliberately

The tonal break they buy would land as a sticker on a dark documentary grade, and they are an
OS font sitting outside the grade. The ★ and ⚠ marks in this file are **storyboard notation**,
never composition text. Stated so the audit reads it as a decision.

### What was considered and refused

- **A depletion bar under 5.4/5.5** ("a high withdrawal rate consumes the capital"). Drawing a
  balance falling to zero over time asserts a **depletion schedule we have no source for**, and
  a drawn projection is exactly the shape `no_return_promise` forbids. The photographs (a torn
  grain sack, a dry outlet pipe) carry the argument without inventing a measurement.
- **A two-bar comparison under 6.15/6.16** (₹19,000 at 7.1% vs ₹10,000 at ~12%). Drawn side by
  side, two *assumed* growth rates read as a recommendation between them. Both figures are
  labelled ILLUSTRATIVE and both stay as type. Same call as the DRY beat in §2.
- **A risk curve under 5.16** (3.75%). The Raju & Saraogi paper is 403'd to us; drawing its
  curve would fabricate a measurement on a frame cited to a real paper.
- **A drawn stats-table row under 6.9** (PLFS). `vector_art.lottie.truth_bar`: never fabricate
  a source document — no invented agency names, seals or legible figures on a frame cited to a
  real table. The folded pay slip plus the `foot:` citation is the honest treatment.

---

## 9. Imagery — 80 slots, 80 files, zero photo-free scenes

**`image_per_scene` is a hard creator rule** (2026-07-28, `photo_free_scene_ratio` = 0). Every
one of the 78 scenes carries `has-photo` and a real full-bleed `.bg` under the locked grade
`grayscale(.32) brightness(.62) contrast(1.05)`. **No per-scene grade override anywhere in this
cut.** `assets/img/manifest.json` is the single home for every query; the table in §7 names the
file.

- **78 bg slots** → **78 bg files**, of which `s14.jpg` is a **crop of `s13.jpg`'s source
  frame**, not a separate photograph (§6). 77 distinct bg photographs.
- **2 cut-in files**: `s11b.jpg` (the note drawn back OUT of the box, +3.30) and `s32b.jpg`
  (milk and vegetables, +2.55) — each anchored to its own word.
- **Total files: 80. Total slots: 80. Distinct photographs: 79.**

**Densest scenes get the calmest backgrounds.** The five art-forward frames carry a drawn layer
on top of type, so all five were routed to near-flat textures: ruled ledger paper (s16), a
shop-balance surface (s25), worn stone (s37), plain concrete lit by one bulb (s47), a plain
table under the balance pans (s64). Density is managed by choosing a quieter image, **never** by
dropping one.

**The four returning objects** (script §7: *new photographs of the same subject, not the same
file re-used* — the sound-off rule is per line):

| scene | line | returns to | how it differs |
|---|---|---|---|
| s71 | 7.1 | s1's bedside clock | same table, later daylight |
| s72 | 7.2 | s3's phone | face-down, the glow gone, daylight |
| s76 | 7.6 | s19's single brick | **three** bricks now, side by side |
| s77 | 7.7 | s2's window | full daylight, the chai glass empty |

Each is its own file and its own fetch. Give fin-assets the visual rhyme (same object family,
same surface, later light) so the callback reads — but **never re-use a file**, which is the
"one image across several points" failure the sound-off rule names.

**Standing rejections that still bite** (`knowledge/stock-photo-sourcing.md`), restated so a
re-fetch cannot lose them:

- **Never a phone-screen photo as a background.** s3 and s72 are both specified face-down; the
  notification is a Lottie (§8). This has shipped undetected three times.
- **No faces.** Hands and objects only — s11, s11b and s75 are the only frames with a hand and
  all three are specified hands-only. Licence issue as much as a design one.
- **₹ frames must be the current stone-grey ₹500 series** — s15, s20, s29 (the cash boxes and
  the trunk). A demonetised pre-2016 note is the wrong era and has shipped before.
- **Nothing legible that is foreign** (script handoff §8): s50's journal, s51's methodology page
  and s52's Indian paper are photographed with **no legible title or numerals**. The citation
  lives in the `foot:`, never in the photograph, and **no frame may put a rupee figure and a
  foreign figure in one composition.**
- **Never fabricate a source document** (handoff §9): s52 is a stapled document with a blank top
  sheet — no invented seal, agency name or legible figure on a frame cited to a real paper.
- **No image hash reused across any project on either channel.** Key the ledger by md5 and
  refuse a hash already used anywhere; Pixabay's top hit is deterministic and different queries
  collapse to it.

**Resolution.** Route the beats where softness would show most to Pexels `large2x` (1880 px):
**s61** (the hero, ₹25,000 held 7.383 s under a 240 px number), **s60**, **s43** (the stamp),
**s50** (the coldest frame), **s16 / s25 / s37 / s47 / s64** (the five drawn-art frames, where a
soft plate under solid art reads as a defect) and **s78** (the CTA — the last frame anyone
looks at). Pixabay's 1280 px ceiling is fine everywhere else: under the grade plus 5% grain it
reads as soft focus.

---

## 10. The ground temperature arc

`.field` carries a per-scene `--f1` two-stop ground. **Role scenes deepen into their role
colour; scenes with no role move only on the neutral warm↔cool axis**, so no frame asserts a
colour it has not earned. Values are in §7. **Push it harder than looks right** — at document
scale the arc reads almost flat and in the encode it is exactly right.

The ladder used:

```
warm     #241d15  #231d17  #221c17  #1f1e1c  #1f1b16      pop-warm  #33200f
neutral  #1c2027  #1a1e24  #1a1f26  #191f28
cool     #161f2b  #131f2c  #0e1c2e (coldest)
fund     #17291f → #1b3024 → #1d3a28 (deepest)
target   #2a2113 → #2e2411 → #372a0c
warn     #301519 → #38151a → #3b1219 (deepest)
```

Read as a curve, not a stripe:

**ch1** warm first light → **one cool frame at s3** (the screen glow at night) → warm through
the bills → sobers to neutral at 1.7, the first frame that is about arithmetic. **ch2** neutral
mechanism → **amber at s13/s14** as the rate is declared and defended → warm at the cash box →
green as the sum lands (s16 `#17291f`, deepening to s18 `#1b3024`) → **warmest at s19**, the
first brick. **ch3** green rung → warm domestic (the May bill is literally the hot month) →
amber at the rate → **a red spike at s27** where the internet inflates it → cools to a settled
`#1a1e24` for *"slow is the trustworthy part"*. **ch4** green rung → **warmest at s32** (a full
kitchen) → neutral for *"say it plainly"* → **red at s34**, the honesty beat → amber for why the
rate is small.

**ch5 carries both extremes.**
- **s42 (5.5) `#3b1219` — the hottest frame in the video.** Capital gone, monthly income gone.
- **s50 (5.13) `#0e1c2e` — the coldest frame in the video.** A bound 1994 American journal on a
  library table: the furthest any frame gets from the viewer's own kitchen, and the exact beat
  where the video says *this number is not ours*. **The drop is a temperature event before it is
  an argument** — 5.14 then snaps back to red and 5.15 comes home to amber.
- s40 (5.3) sits between two reds at `#251a1c`, a red-leaning **neutral**: it moves on the warm
  axis without asserting a role it does not have.

**ch6 climbs.** Neutral rung → green → warm rent → green → amber as the crore is named →
**s61 `#1d3a28`, the hottest green in the video and the only use of it: the hero.** Then cool at
the sourced pay slip, green where they meet, and **red through s66/s67** as the imported rule
costs a quarter of the target. s68 is deliberately **neutral** — the frame that separates
withdrawal from growth may not be painted as either.

**ch7 returns to ch1's temperature one step warmer**: `#1f1b16` on the clock, cool-neutral on
the dead phone, neutral for the division, warm for the habit, green for where it started, and
**s77 `#241d15`** — full daylight, the exact warmth of s1. The CTA closes on `#33200f`, the only
pop-leaning ground.

**No ground cross-fade is implemented.** We cross-dissolve whole sections for 0.45 s, which
blends both grounds already; adding the Claude Design animatic's ground melt double-fades.

---

## 11. Transitions and timing

`dissolve` (0.45 s) is the default on every boundary. **Two** boundaries are `shove`, and they
are the only two turns in the argument:

- **s37 → s38 (4.9 → 5.1)** — the ladder ends and the correction begins. Everything before is
  *the division works*; everything after is *here is the trap, and here is where the number you
  have been told came from*. This is the video's hinge and it lands at **45.1%** of runtime.
- **s54 → s55 (5.17 → 6.1)** — out of the correction and into the climb. The chapter that spent
  100 seconds proving India's rate is 3.0% hands over to the chapter that spends the rate. A
  dissolve here would smuggle the payoff in as a continuation instead of announcing it.

**One matched-frame hold**, s13 → s14 (§6) — mechanically a dissolve; what makes it a hold is
that both scenes are one photograph under one continuous zoom.

```
scene_duration = 0.25 (VO lead-in) + clip_duration + 0.55 (tail)   ← MEDIUM override
data-duration  = scene_duration + 0.45   (s1–s77; s78 bare)
audio_start    = scene_start + 0.25
root duration  = 488.222
```

`0.25 / 0.55` are `format.json tiers.medium`, **not** the `scene.*` 0.4 / 1.0 SHORT defaults.
Generated from `timing.json` — **never hand-edited.** The same numbers live in four places (the
`<section>`, the JS `S` map, the `<audio>` row, root `data-duration`); updating three of four
passes every check and ships a video whose animations fire against the old timeline. Per-scene
figures are the `start` / `dur` / `d-dur` columns of §7 and are not restated — one home per fact.

> **The failure mode to watch for at build.** Durations that sum to exactly 488.222 while every
> internal cut has drifted is what a re-timing produces. `tools/chapter_project.py` asserts
> **GAPS, not totals**, and `tools/cut_assemble.py` verifies every scene's `data-start`,
> `data-duration`, `data-track-index` and framings **individually**. Neither may be weakened.

---

## 12. The skeleton the `-en` cut ports

The `-en` storyboard ports **the element IDs** (`sN-field`, `sN-bg`, `sN-bg2`, `sN-scrim`,
`sN-stack`, `sN-kick`, `sN-stmt`/`sN-num`, **`sN-rate`**, `sN-sub`, `sN-foot`, `sN-icon`,
`sN-art`, `sN-cta`), **the three cue variants** (§5), **the focal size rule** (§3), **the
`#sN-rate` mechanism and its build assert** (§4), **the transition classes**, and **the
archetype/ground/art discipline** (§7, §10) — so a fix in one cut travels to the other.

What it must **not** port:

- **The `#` ↔ line mapping.** `script-en.md` is a US rewrite, not a translation; if its line
  count differs from 78 the mapping is rebuilt, not renumbered. (`japanese-money-methods` -en ran
  two extra lines in one chapter and its promise break sat one scene later — deriving the map by
  hand from the -hi row would have mis-cut two chapters.)
- **The anchored cue fractions.** Every one is a Hindi word position. English delivery measures
  ~17.4 c/s against Hindi's 13.03 and the figures land in different clause positions.
- **The corpus figures, the rate and the whole of §4's token list.** The -en cut is a US market
  rewrite with US vehicles and US numbers; PART C of `facts-staging.md` is its block and PART B
  is ours. **₹1 crore is not any foreign figure**, and no frame may imply a conversion.
- **The photographs.** No image may repeat across videos **or channels**, and the -hi cut's
  kirana counter, POMIS grille and ₹500 series are India-specific by construction.

A `-en` storyboard with **zero** divergences is a translation wearing a layout costume, and the
audit will flag it. It must emit an explicit divergence list with a reason per scene.

---

## 13. Open items

1. **None that block a build.** The `max_scene_seconds` breach at 2.6/2.7 is *resolved* here
   (§6), not deferred: a real second file plus a continuous zoom, with both framings declared.
   No orchestrator decision and no `known_benign` entry is owed.
2. **Bed length is NOT an open item** (§2). Recorded because both storyboards on
   `japanese-money-methods` raised it as a decision on 2026-08-01 and it never was one.
3. **The SFX count is derived, not budgeted** (§2). If a reviewer expects ≤10 cues, that is the
   SHORT-cut figure; the creator retired it for chapter cuts on 2026-08-06 and
   `tools/audio/cues.py` is the implementation.

## Sign-off

- [x] Colour semantics table filled and consistent with the script's post-audit cues
- [x] `arch` / `ground` / `art` assigned on all 78 scenes (§7)
- [x] `has-photo` + a real `.bg` on all 78 scenes; `photo_free_scene_ratio` = 0
- [x] No rail, no chapter title, no scene counter, no slide number anywhere on screen
- [x] Every `start` / `dur` verbatim from `timing.json`; nothing re-timed
- [x] Every corpus frame carries `#sN-rate` in the same frame (§4) — 20 of 20
- [x] 2.6/2.7 single-photograph breach resolved with a tighter crop + one continuous zoom
- [ ] No image hash reused from any prior video on either channel — **fin-assets to verify**
- [ ] Creator approved (Gate ②) — date: __
