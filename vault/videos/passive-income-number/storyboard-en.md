---
summary: Storyboard for «How Much You Need Invested To Live Off Dividends» en cut — MEDIUM tier, 81 scenes (one VO line = one clip = one scene), blockframe-9 + the chapter archetype layer. REBUILT from scratch for the style-E restyle and the re-measured 527.873s audio. Declares the colour semantics, the archetype row (arch / ground / art / centred) on all 81 scenes, the DOM with the standing `sN-rate` element that carries the rate into all fourteen corpus frames, three cue ladders on measured timing.json offsets, 2 shoves + 3 matched-frame holds, one music bed with a derived cue list, 7 drawn proportions / 1 Lottie / 0 icons, the corpus measure-ladder, both peaks, and 84 image slots. Resolves the 2.2 10.596s single-photograph breach with a derived tighter crop under one continuous zoom.
updated: 2026-08-08
source: script-en.md (fin-script en attempt 2, STYLE E, + the two fin-audit-en-2 in-place edits at 4.8 and 1.2) + studio/videos/passive-income-number-en/assets/voice/timing.json (measured, 527.873s, 81 lines) + run.json constraints/style_decision + storyboard-hi.md (skeleton + element IDs, §13) + knowledge/design-finance-blockframe.md + knowledge/design-chapter-archetypes.md + knowledge/design-chapter-sound.md + knowledge/stock-photo-sourcing.md + tools/format.json + tools/audio/kit.json + tools/audio/cues.py
stage: fin-storyboard, cut en, attempt 2 — FULL REBUILD (attempt 1 was written against the retired 78-line style-A script and is superseded in its entirety)
---

# STORYBOARD — «The Passive-Income Number» · **en** cut

**Project:** `studio/videos/passive-income-number-en/` · **Script:** `script-en.md`
**Design:** [[../../knowledge/design-finance-blockframe]] — the **dark** system, unmodified,
extended by [[../../knowledge/design-chapter-archetypes]]. Do **not** use
`design-techtooltester` (bright, non-finance).
**Channel:** @moneymavens101 $ · **Tier:** MEDIUM, per-line chapters (6 chapters, 81 lines)
**Architecture:** **`blockframe-9`** (`run.json.architecture` = `format.json architecture_lock`).
`body_class` is `""` — no `.rail`, no `.swiss-band`, no panel. Centred stack over a full-bleed
graded photograph, every scene, with the archetype layer deciding where the drawn layer lives.
**Runtime:** **527.873s (8:47.9)** — `timing.json` is the only home for every duration.
**VO:** Brian `nPczCjzI2devNBz1zQrb` · **Scenes:** 81 · **Image slots:** 84 (81 bg + 3 cut-ins),
**84 files**, 78 fetched + 6 derived crops (§10).

> **Four things this file is accountable for, from the run's own §3c checklist.**
> 1. Every scene carries `arch` / `ground` / `art` — §7, three real columns, no blanks.
> 2. Every scene carries `has-photo` and a real `.bg` — §10, `photo_free_scene_ratio` = 0.
> 3. **No rail, no chapter title, no scene counter, no slide number** — §3.
> 4. Every duration is `timing.json` verbatim — §7 / §12. Nothing here re-times a scene.
>
> **And the rule this video is built around:** every corpus figure shares a frame with its
> withdrawal rate or yield, as a real `#sN-rate` element — §4, fourteen frames, asserted.

---

## 1. Colour semantics for THIS video (derived from the thesis — mandatory)

The thesis: *the passive-income number is a division, not a forecast — a yearly bill over an
assumed rate. The rate is the whole argument: change it from four percent to about one and the
same $5,000 a month costs roughly four times as much.*

Roles are fixed; meanings are per-video. **This table is derived from the script's own
`colour:` cues, line by line. The cue is authoritative; this is the index.**

| Token | This video means | Because |
|---|---|---|
| `--fund` green `#22c55e` | **a division that closed at a rate the video has sourced** — the method itself (2.10), every rung that lands (2.13, 2.14, 2.15, 3.4, 3.8, 4.2, 4.3, 5.15), the assembled ladder (6.6, 6.7, 6.8) and what the number buys back (6.12) | green marks **arithmetic that came out**, never "safe", never "recommended". The persona rule forbids a pick, so green cannot mean approval |
| `--warn` red `#ef4444` | **what an assumption costs when it fails or when it changes** — the question that opens the loop (1.7), the papers' own limits (3.5, 3.10–3.15), the yield trap and 1932 (4.5–4.13), the dividends-only price (5.5, 5.6, 5.7, 5.9, 5.16, 6.9) and the rate not being settled (6.1, 6.4, 6.5) | red is **the price of an assumption**, not a verdict on a strategy. $5,555,556 is red because it is a *price*, not because dividends are wrong — 5.8 says both numbers are true |
| `--target` amber `#f59e0b` | **a published figure or rate under examination** — 4.0% and its two papers (2.1–2.9), every BLS numerator (2.11, 3.2, 3.6, 3.7, 5.14), the worked $5,000 convention (4.1), about 1% / 1.04 / 1.082 / about 3% and the middle price (5.1, 5.3, 5.4, 5.8, 5.10, 5.11, 5.12), 3.9% and 4.7% (6.2, 6.3) | amber is the thing being **weighed**. Every price-evidence beat is amber precisely because the persona rule forbids a pick — an amber number is being measured, not offered |
| `--pop` orange `#ff5c39` | the call to action | fixed — **exactly once**, s81 (6.13), as the `.cta` block's fill. Zero mid-roll CTA |

**The inversion trap — four prior systems, none of them applies here.** `needs-vs-wants` ran
amber = "wants"; `first-lakh-first-thousand` ran red = "the stretch nobody helps you with";
`japanese-money-methods` ran red = falsity-and-drain, green = the viewer's own hand; **this
run's own hi cut** runs green = the division closing, red = depletion-and-importation, amber =
a rate being weighed. **Here green is a division that closed, red is what an assumption costs,
amber is a published figure under examination.**

**Thesis check** (the audit's): green never lands on a figure whose rate is not in frame ·
green never lands on a BLS bill (a numerator is not an answer) · amber never lands on
$5,555,556 (it is a price, not a candidate) · red never lands on the 4.0% working rate itself.

**Role counts across 81 scenes:** amber 22 · red 26 · green 13 · orange 1 · **no role at all
19**. Nineteen colourless frames is correct and deliberate — colour is a signifier here, not
decoration.

**Role colour classes.** Text takes `.fundc` / `.warnc` / `.targetc` / `.popc` — the
**colour-only** forms in `assets/blockframe.css`. Never the bare `.fund` / `.warn` /
`.target` modifiers on text: those are the chip/stamp/billrow border-and-fill forms, and a
role token with no colour class **paints `--ink` white and passes every check silently.** The
`.cta` block on s81 is structurally immune (it sets its own `background: var(--pop)`); every
other coloured element in this cut is a text node and must carry its class explicitly.

### 1a. Per-scene `--tint` — derived from the role, never chosen

One rule, 81 applications, so it cannot drift. Not a column.

| scene's role | `--tint` | alpha |
|---|---|---|
| `--fund` | green | `.10` (green reads hotter) |
| `--warn` | red | `.12` |
| `--target` | amber | `.12` |
| `--pop` (s81 only) | orange | `.13` |
| **no role (19 scenes)** | **none** — `--tint` unset, scrim layer 1 renders `transparent` | — |

Design doc §2 caps tint at 0.10–0.13; above ~0.15 it stops reading as light and becomes a
colour wash.

---

## 2. Audio — one bed, a derived cue list

**Music bed: `bed-tension`.** This video's argument is **a cost**: a number priced out of an
assumption, and a warning that the popular route costs roughly four times. It is not a habit
or a fix, so `bed-resolve` would argue against it. Chapter 6 resolves; chapters 3, 4 and 5 are
the video. The bed is chosen for the video, not for a chapter.

> **Bed length is not a decision and is not flagged here.** `tools/audio/mix.py` feeds the
> ~248s bed in `laps` times with a 3s `acrossfade` at each joint and trims to the master's
> duration. There is no dip at 248s or 496s. Both storyboards on `japanese-money-methods`
> escalated this as an open decision on 2026-08-01; it never was one. **This cut is 527.873s —
> do not raise it.**

### The cue list is DERIVED per chapter, not hand-typed

`tools/audio/cues.py studio/videos/passive-income-number-en-ch<N> --write` emits one cue per
**real motion call**, at that call's own time, bound through `kit.json`'s helper column. This
supersedes the ≤10-cue figure in the storyboard contract, which is a **SHORT-cut** number:
creator decision **2026-08-06** retired the hand-authored ceiling for chapter cuts, because a
24-cue list over ten minutes carries exactly one `transition` and every scene change then reads
as silent — *which was the defect the creator actually reported*. Expect ~135 cues over 8:48
(one per ~3.9s), in line with the shipped 3.4s density. Discipline lives in what each cue is
**bound to**, not in how few there are.

**What this storyboard owns, because the generator cannot derive it.** `cues.py` reads these
from `studio/videos/passive-income-number-en/assets/cues-tables.json` — **fin-build writes that
file verbatim from this block.** An absent table means *no special cases*, never someone else's.

```json
{
  "holds":   [["s3","s4"], ["s41","s42"], ["s75","s76"]],
  "buzz":    {"s4": 1.85},
  "counted": ["s64", "s75"],
  "dry":     ["s1","s2","s3","s4","s5","s6","s8",
              "s12","s14","s16","s19","s20","s25","s26","s29","s30","s36",
              "s40","s42","s50","s56","s62","s63","s65","s66","s67","s68",
              "s70","s71","s74","s75","s76","s78","s79"]
}
```

| input | value here | why |
|---|---|---|
| `holds` | s3→s4 · s41→s42 · s75→s76 | the three matched-frame continuous zooms (§6). A whoosh there announces a change that is not happening |
| `buzz` | `s4` at **+1.85** | the kit's only diegetic sound, legal **only** because the frame shows the phone making the noise and the Lottie banner lights on that offset (§8). Nowhere else in the cut. **`dry` does not kill it** — `cues.py` silences derived cues only, and an explicitly declared buzz survives |
| `counted` | s64 · s75 | the two cascades where the **count is the point** ("three routes, three rates"; the three rungs recapped). **s26 (4 items) and s76 (2 items) are deliberately NOT counted** — the generator's counted branch is hardcoded to `n = 3` and would emit three clicks for a four- and a two-item row |
| `cta` | s81 only | the single `--pop` element of the video |
| `stamp` | five scenes | s7, s17, s38, s52, s73 — their `stmt` enters with **`pop`** (`back.out(1.7)`) instead of `rise`. That IS the verdict slam; it needs no `.stamp` pill and no new copy, and it is what makes the sound legal |

**Declared DRY beats — silence is the choice, not an omission** (all still take their joint
`transition`):

- **The whole cold open, s1–s6 and s8.** The what-if is paid in recognition, not punctuation;
  s7's stamp is the only sound in chapter 1 besides s4's buzz. Punctuating a coffee mug makes
  it a joke.
- **s12, s14, s16 — the papers' evidence run.** A `hero` on `95%` makes a survival statistic
  sound like a prize. The chapter's power is provenance and it is paid at s17.
- **Every BLS numerator and every ÷12 (s19, s20, s25, s26, s29, s30, s66).** These are
  measurements, not landings.
- **Rungs two, three and five (s27, s31, s67).** Only the FIRST rung and the two peaks ring.
  If every rung gets a `hero`, the ladder has no shape — which is what the measure bar (§9)
  fixes visually instead.
- **s40 ($5,000 A MONTH) and s42 (the restatement).** s40 is a chosen convention, not a result;
  hitting a restatement makes it sound like new evidence, and s42 is already carried by the
  continuous zoom out of PEAK 1.
- **s50, `13.84%`.** A `hero` on a June-1932 yield sells a warning as a prize — the one thing
  the chapter exists to refuse.
- **s62/s63, the middle route.** The video refuses to recommend between routes; a bass hit on
  `ABOUT 3%` recommends one, whatever the foot says.
- **s68, `$7,271,759`.** The largest number in the video, dry on purpose: after the reward beat
  at s59 the cut must stop escalating, or the answer it just paid out gets outbid.
- **s74–s76, the recap assembling, and s78–s79.** Nothing sounds between s77's `hero` and
  s81's `cta`, so the callback lands in a cleared room.

**Mixed in post, never in the composition.** `assets/audio.json` → `tools/audio/mix.py`
(sidechain duck) → `tools/loudnorm.py` to −14 LUFS. The composition stays voice-only: one
`<audio>` row per line, track index 10. No music or SFX `<audio>` rows in `index.html`.
**Verify from the encoded file, never from the mix log** (`tools/audio/verify_cues.py`).

---

## 3. The frame — DOM, and the standing `sN-rate` element

`<div id="root" class="cut-en">`. **No body class.** `cut-en` is load-bearing: it is the whole
@moneymavens101 watermark, painted on `#root::after` above every scene, and `check build` fails
without it. Stage 1920 × 1080, `.scene` padding `110px 150px` ⇒ content box **1620 × 860**,
centred, `isolation: isolate` (without it the outgoing scene's type paints over the incoming
one for the whole 0.45s dissolve, at all 80 boundaries).

**NO RAIL. NO CHAPTER TITLE. NO SCENE COUNTER. NO SLIDE NUMBER.** `format.json
chapter_design.rail` is `false`; the top rail was built and removed at creator request
2026-08-05 and is not to be reintroduced. **The viewer must never be shown that this video is
chapter-based.** Chapters exist for production (build → `fin-editor` → `fin-ceo`, one at a
time) and for the YouTube chapter list — nowhere on screen.

```html
<section class="scene clip arch-b has-photo centred art-off" id="s21"
         data-track-index="1" data-start="130.730" data-duration="6.527"
         data-framings="6.077" style="--tint:rgba(34,197,94,.10)">
  <div class="field" id="s21-field" style="--f1:#12351f"><div class="rules"></div></div>
  <div class="bg"    id="s21-bg" style="background-image:url(assets/img/s21.jpg)"></div>
  <div class="scrim" id="s21-scrim"></div>       <!-- --tint only when the scene has a role -->
  <div class="stack" id="s21-stack">
    <p class="kicker"     id="s21-kick">RUNG ONE</p>
    <p class="sub fundc"  id="s21-rate">AT A 4.0% WITHDRAWAL RATE</p>
    <p class="huge fundc" id="s21-num">$254,225</p>
    <p class="foot"       id="s21-foot">$10,169 divided by 0.04 · ILLUSTRATIVE ARITHMETIC</p>
  </div>
  <p   class="measure-lab under" id="s21-mlab">THE LADDER</p>
  <div class="measure under"     id="s21-meas"><div class="measure-fill fund" id="s21-mf"></div></div>
  <div class="grain"></div>
</section>
```

**ID scheme: `s<n>-<part>`, n = 1…81 in script order** — `field`, `bg`, `bg2`, `scrim`,
`stack`, `kick`, `stmt` **or** `num`, **`rate`**, `sub`, `foot`, `meas`, `mlab`, `mf`, `band`,
`plate`, `art`, `stage`, `cta`. Ported from `storyboard-hi.md` §3 so a fix travels between cuts
(§13, D1). **Five part names are load-bearing for the SOUND generator** and may not be renamed:
`-cta`, `-stmt`, `-num`, `-mf`, `-band` (`tools/audio/cues.py` matches on them literally).

**Copy is NOT restated here.** `head:` / `stmt:` / `num:` / `foot:` strings live in each line's
`[arch …]` cue block in `script-en.md` and have exactly one home. This storyboard owns the DOM,
the archetype row, the cues, the transitions, the audio, the drawn art and the images.

**Three exceptions, all from the 97-codepoint font subset** (build handoff §9):

| scene | script cue says | render instead | why |
|---|---|---|---|
| s40 (4.1) | `num: $5,000 / MONTH` | **`$5,000 A MONTH`** | `/` is not in the subset; the handoff already replaced the solidus with `DIVIDED BY` elsewhere in the same file |
| s76 (6.8) | `stmt: $5,000/mo $1,500,000 · $6,545/mo $1,963,375` | **two `.sub` lines:** `$5,000 a month · $1,500,000` and `$6,545 a month · $1,963,375` | same reason, plus one line carrying four figures is not a focal |
| s34 (3.11) · s37 (3.14) | typographic `“ ”` around the two verbatim quotations | **verify against a dumped `subset.txt`; fall back to straight `"`** | the subset was verified for `> → ▶ × ≈ ~`, never for curly quotes. A missing glyph renders as tofu and no check catches it |

**Build guard: no `/` and no `?` in any on-screen string in this cut.** `·` is the separator.
Verify every string against a dumped `subset.txt` before render.

### The three type registers

| Script field | Class here | Size | Colour |
|---|---|---|---|
| `head:` | **`.kicker`** `#sN-kick` | 30 / 800, tracked 4, uppercase | `--muted` |
| `stmt:` | **`.huge`** `#sN-stmt` | **112 / 88 / 76** by the rule below | `--ink`, or the scene's role class |
| `num:` | **`.huge`** `#sN-num` 112 (**`.mega` 300 on s55 only**) | tabular-nums, `Intl.NumberFormat("en-US")` | the scene's role class |
| the rate qualifier | **`.sub`** `#sN-rate` | **40** | the scene's role class |
| a non-rate qualifier | **`.sub`** `#sN-sub` | **40** | `--muted` |
| `foot:` | **`.foot`** `#sN-foot` | 26 / 700 | `--muted` |

**Focal size rule — deterministic, keyed on the copy, so it cannot drift when a string
changes.** FinanceSans at weight 900 averages ≈0.58 em advance; usable width 1620px.

| `stmt:` length | `.huge` inline size | lines |
|---|---|---|
| ≤ 24 chars | **112px** | 1 |
| 25–48 chars | **88px** | 2 |
| 49–89 chars | **76px** | 3 |

**Never below 76.** The longest `stmt:` in the cut is 3.14's 87-char quotation → 76px × 3 lines
= 222px in an 860px box, with room for kicker, rate and foot. Every `num:` fits one line at
112px (`$5,555,556` = 10 glyphs × 0.58 × 112 ≈ 650px). **`ABOUT 1%` at `.arch-b .mega` 300px =
8 glyphs × 0.58 × 300 ≈ 1,392px**, inside the 1500px stack — which is exactly why the `.mega`
is the RATE and not the corpus (§9c): `$5,555,556` at 300px would run ~1,740px and clip.

**Chips exist on five scenes only** — s2, s6, s26, s45, s64 (§5, ladder C). Every other
qualifier is a `.sub` line, because **a chip crushes a figure-plus-its-rate**. All chips are
≤22 chars and rows are declared explicitly (`.row` has `flex-wrap: wrap`, so four long chips
silently orphan 3+1 and no checker flags it).

**Element budget.** Per scene: photograph (1) + kicker + focal + one or two of rate/sub/foot =
**4–5 countable**, against the ceiling of 6. The six measure-bar frames run kicker + num + rate
+ foot + `mlab` + `meas` = **exactly 6**. `.field`, `.scrim` and `.grain` are grade layers, not
scene elements; `sN-bg2` is a cross-fade of the photograph layer, not a fifth element.
**Never `stmt` and `num` together** — where the script's cue block carries both (3.7), the
`stmt:` becomes the qualifier (`#s30-sub`, 40px) and the `num:` is the focal.

---

## 4. `#sN-rate` — the rate is a DOM element, not a footnote

`run.json.constraints.withdrawal_rate_on_screen`: *"Every corpus figure must carry its assumed
withdrawal/return rate ON SCREEN in the same frame as the number. A number without its
assumption visible is a fabricated promise."* Extended 2026-08-07 by
`derived_income_carries_assumption` to **derived income** figures.

fin-audit verified all fourteen VO lines re-speak their rate. **This storyboard's job is to
make the frame structurally incapable of losing it**, so the rate is not a 26px `--muted` foot
a density pass can drop — it is a **first-class `.sub` at 40px in the scene's role colour, and
it arrives at +1.10, BEFORE the corpus lands.** The assumption is on screen first and the
number arrives into it. That ordering is the constraint's strongest reading and it costs
nothing. (Mechanism ported verbatim from `storyboard-hi.md` §4, where the same two failure
frames were caught.)

Two forms, exactly as in the hi cut:

- **Its own qualifier line** → `#sN-rate` is a `.sub`, cue 2 at **+1.10 fixed** (`rise`).
- **Fused into one sentence** (the workings, the pairs, the recap) → `#sN-rate` is an inline
  `<span>` **inside the focal**, wrapping the rate token, carrying the role colour and taking a
  `pulse` at **+1.90 fixed**. No copy is reordered, nothing is printed twice, and there is a
  node to assert.

| # | scene | line | corpus / derived figure on screen | `#sN-rate` form | rate token |
|---|---|---|---|---|---|
| 1 | **s21** | 2.13 | `$254,225` | `.sub` — `AT A 4.0% WITHDRAWAL RATE` fundc | `4.0%` |
| 2 | **s22** | 2.14 | `$254,225 at 4.0% · the grocery bill stops costing hours` | span in the focal | `4.0%` |
| 3 | **s27** | 3.4 | `$332,950` | `.sub` — `AT A 4.0% WITHDRAWAL RATE` fundc | `4.0%` |
| 4 | **s31** | 3.8 | `$656,650` | `.sub` — `AT A 4.0% WITHDRAWAL RATE` fundc | `4.0%` |
| 5 | **s41** | 4.2 | `$1,500,000` | `.sub` — `AT A 4.0% WITHDRAWAL RATE` fundc | `4.0%` |
| 6 | **s42** | 4.3 | `$1,500,000 AT 4.0% = $5,000 a month` — **corpus AND derived income** | span in the focal | `4.0%` |
| 7 | **s59** | 5.7 | `$5,555,556` | `.sub` — `AT A 1.08% DIVIDEND YIELD` warnc | `1.08%` |
| 8 | **s60** | 5.8 | `$1,500,000 AT 4.0% · $5,555,556 AT 1.08%` | **two spans** — `s60-rate`, `s60-rate2` | both |
| 9 | **s63** | 5.11 | `$1,929,260` | `.sub` — `AT A 3.11% YIELD` targetc | `3.11%` |
| 10 | **s67** | 5.15 | `$1,963,375` | `.sub` — `AT A 4.0% WITHDRAWAL RATE` fundc | `4.0%` |
| 11 | **s68** | 5.16 | `$7,271,759` | `.sub` — `AT A 1.08% DIVIDEND YIELD` warnc | `1.08%` |
| 12 | **s75** | 6.7 | `Food · $254,225` / `Car · $332,950` / `Housing · $656,650` | `.sub` — `EACH AT A 4.0% WITHDRAWAL RATE` fundc | `4.0%` |
| 13 | **s76** | 6.8 | `$5,000 a month · $1,500,000` / `$6,545 a month · $1,963,375` | `.sub` — `BOTH AT A 4.0% WITHDRAWAL RATE` fundc | `4.0%` |
| 14 | **s77** | 6.9 | `$5,555,556` | `.sub` — `AT A 1.08% DIVIDEND YIELD` warnc | `1.08%` |

**The build assert (mechanised, from handoff §10).** Any scene whose rendered text contains a
corpus token — `$254,225` `$332,950` `$656,650` `$1,500,000` `$1,929,260` `$1,963,375`
`$5,555,556` `$7,271,759` — **must contain an element with id `sN-rate` whose text contains a
rate token** (`4.0%`, `1.08%`, `3.11%`). Fourteen scenes qualify and all fourteen are above.

**What the assert must NOT fire on, so it stays honest:**

- **A BLS bill divided by twelve** (s20 `$847`, s26 `$1,110`, s30 `$2,189`, s66→s67 `$6,545`)
  is arithmetic on a published statistic, not income derived from a corpus. Its foot already
  says *"arithmetic, not a separate statistic"*.
- **s40 `$5,000 A MONTH`** is a chosen INPUT, not a result. It is covered by the extension's
  *explicit marker* branch: its foot states, on screen, that the figure was chosen below the
  BLS average so it cannot be read as a promise.

**Nine frames carry a rate as their FOCAL** (s16 `95%`, s30 `33.4%`, s36 `30 YEARS`, s50
`13.84%`, s55 `ABOUT 1%`, s56 `1.04% · 1.082%`, s62 `ABOUT 3%`, s70 `3.9%`, s71 `4.7%`) and
carry **no separate `#sN-rate`** — printing a rate under itself reads as a defect.

---

## 5. The cue ladders — three variants

Offsets are **relative to `scene_start`** (§7 column `start`, verbatim from `timing.json`), so
every absolute cue time is `scene_start + offset` and is derived, never hand-typed.
`audio_start = scene_start + 0.25` (MEDIUM `lead_in_seconds`).

| variant | scenes | cue 1 | cue 2 | cue 3 | cue 4 |
|---|---|---|---|---|---|
| **A — statement** (default) | 47 | `sN-kick` **+0.30** fixed `rise` y24 | `sN-stmt` **+1.10** fixed `rise` y40 — **`pop` on the five verdict scenes** (§2) | `sN-rate` span **+1.90** fixed `pulse`, *or* `sN-sub`/`sN-foot` **+1.90** fixed `fade` | `sN-foot` **+2.70** fixed `fade` (only when cue 3 was the rate/sub) |
| **B — figure** | 29 | `sN-kick` **+0.30** fixed `rise` | `sN-rate`/`sN-sub`, else `sN-foot`, **+1.10** fixed `rise` | `sN-num` **anchored, floor +1.90**, `countUp` + `pop`; on the six ladder frames `sN-mf` `span` fires on the **same cue** | `sN-foot` = **num + 0.80** fixed `fade` (only if the foot did not take cue 2) |
| **C — cascade** | 5 (s2, s6, s26, s45, s64) | `sN-kick` **+0.30** fixed `rise` | *the chips ARE the statement* — **+1.10 / +1.70 / +2.30 (/+2.90)**, `popEach`, **fixed 0.6s** | — | `sN-foot` = last chip + 0.80 fixed `fade` |
| **D — close** | 1 (s81) | `s81-cta` **+0.40** fixed `pop` | `s81-foot` **+1.20** fixed `fade` | — | — |
| — | all 81 | `sN-bg` **+0.00 → scene end** anchored `ken` 1.0 ↔ 1.16 | | | |
| — | 3 scenes | `sN-bg2` anchored `fade` — a 0.40s cross-dissolve of the photograph layer (§6) | | | |

**Two declared per-scene exceptions:**

1. **s55 (5.3), the `.mega`.** `ABOUT 1%` is anchored at ≈+3.07 on a 4.562s scene, so the foot
   cannot follow it. Order: `s55-kick` +0.30 · `s55-foot` +1.10 · `s55-num` anchored +3.07.
   Gaps 0.80 / 1.97 ✓.
2. **s81 (6.13) has no kicker** (`head: —`). The `.cta` block therefore takes +0.40 so something
   authored is on screen inside `first_cue_by_seconds` 0.5, not only the photograph.

**s39 (3.16) carries a kicker and no statement at all** (`stmt: —`) — one element, at +0.30. It
is the emptiest frame in the cut and that is the beat: the chapter ends on a held breath before
the shove into the hero.

**Every gap is ≥0.8s.** A: 0.30→1.10→1.90→2.70 = 0.80 throughout ✓ · B: 0.30→1.10 = 0.80 and
the floor puts the num at ≥1.90 ⇒ ≥0.80, foot at num+0.80 ✓ · C: a **declared cascade**,
`layout.cascade` gap 0.6s, ≤5 items ✓ · D: 0.40→1.20 = 0.80 ✓.
`first_cue_by_seconds` 0.5: the photograph is up at +0.00 and the first authored element at
+0.30 (+0.40 on s81) ✓.

**Anchored vs fixed.** The kicker, the stmt, the rate/sub, the foot, every cascade item and the
CTA are **fixed** — constant regardless of clip length. The `ken` push, every `num` arrival,
every `bg2` swap, the s4 Lottie and every drawn-art beat are **anchored**: they land on a word
and scale with the clip. **Surplus time from a longer clip goes into the hold after the
assembly — never into a cascade.** Concretely: variant A finishes at +2.70 at the latest, so
s67 (8.506s, the longest scene) holds a finished frame for ~5s with only the ken push running.
**Nothing in this cut needs a slow reveal, which is the answer to the 6.7 slack flag** (§7).

**Anchored cue resolution.** `f` is a **fallback**: `f` = the character position of the figure's
first spoken word ÷ the line's character count, floored at +1.90, and fin-build resolves each
against **faster-whisper word timings**, using the fraction only if the word fails to align
(handoff §11). Character-offset interpolation is a stopgap, never the authority.

| scene | anchor word | `f` | offset |
|---|---|---|---|
| s16 (2.8) | "ninety-five" | 0.54 | +3.25 |
| s21 (2.13) | "two hundred" | 0.45 | +2.62 |
| s27 (3.4) | "three hundred" | 0.60 | +3.73 |
| s31 (3.8) | "six hundred" | 0.53 | +3.32 |
| **s41 (4.2)** | "one and a half million" | 0.71 | **+5.18** |
| s55 (5.3) | "about one percent" | 0.75 | +3.07 |
| **s59 (5.7)** | "five point six million" | 0.74 | **+5.12** |
| s61 (5.9) | "roughly four times" | 0.72 | +4.86 |
| **s77 (6.9)** | "five point six million" | 0.82 | +6.08 |
| s4 (1.4) | "buzzes" (Lottie + `buzz`) | 0.26 | +1.85 |
| s10 (2.2) | "draw" (the framing swap) | 0.62 | +6.324 |

**Track index alternates 1 / 2 by scene parity** (odd → 1, even → 2), because `hyperframes
check` rejects two overlapping clips on one track and every non-final scene overlaps its
successor by 0.45s. No column needed; it is `1 if n % 2 else 2`.

**`ken` direction is a rule, not a column:** s1 starts `i` (push in) and the direction **flips
at every boundary except the three holds**, where the partner continues its predecessor's move
with chained `plateKen` endpoints (§6). **s75→s76 is the one hold that runs OUT** — a pull-back
is what makes the ladder get bigger.

**`data-duration` = `timing.json` `scene_duration` + 0.45** on s1–s80; **s81 carries its
`scene_duration` bare**. Root duration is unaffected: **527.873s**.

---

## 6. The 2.2 breach, and the three holds

### 6a. s10 (2.2) — 10.596s on one photograph, resolved inside the scene

`timing.json` measures 2.2 at **10.596s**, the cut's **only** `max_scene_seconds` 9.0 breach
(next longest: s67 8.506 · s76 8.323 · s8 8.271 · s11 8.167 — all clear). The line is
creator-approved verbatim and it plants the tank, so it is not cut. It is solved the way the hi
cut solved its 14.034s breach, and the mechanism is proven on this run's own render (hi s13→s14
joint measured `scdet` 0.073 against 0.184/0.214 at the real photo boundaries either side):

| | framing 1 | framing 2 |
|---|---|---|
| file | `s10.jpg` — the whole tank, the tap low on its side | **`s10b.jpg` — a second, TIGHTER crop of the SAME source frame**, on the tap |
| element | `#s10-bg` | `#s10-bg2`, 0.40s cross-dissolve |
| ken | `i`, **1.00 → 1.06** (`plateKen`, explicit endpoints) | `i`, **1.06 → 1.16**, continuing the same push |
| `data-framings` | **6.324** | **4.272** (sums to 10.596 ✓) |
| swap at | — | **+6.324**, anchored on *"draw"* (`f` 0.62) |
| longest single framing | **6.324s** ✓ | **4.272s** ✓ |

**Never a self-dissolve back to the same file** (creator rule, firaun 2026-07-23): the same
image across two framings is ONE continuous zoom, and cross-fading a file onto itself flickers.
`s10b.jpg` is a *different file cropped from the same source*, which is what makes the swap read
as a push rather than a flash. `cues.py` fires a `transition` on the swap — correct here,
because a change genuinely happens.

### 6b. The three matched-frame holds

| pair | lines | one continuous zoom over | second file | ken |
|---|---|---|---|---|
| **s3 → s4** | 1.3 → 1.4 | the kitchen counter, 12.310s total | `s4.jpg` = **derived tighter crop of `s3.jpg`'s source**, on the phone beside the mug | `i` 1.00→1.08, then 1.08→1.16 |
| **s41 → s42** | 4.2 → 4.3 | the vault door, 14.218s total | `s42.jpg` = **derived tighter crop of `s41.jpg`'s source**, on the dial | `i` 1.00→1.08, then 1.08→1.16 |
| **s75 → s76** | 6.7 → 6.8 | the crate line, 15.419s total | inverted — **`s76.jpg` is the SOURCE** (five crates) and `s75.jpg` is the tight crop on the smaller three | **`o`** 1.16→1.08, then 1.08→1.00 |

Each single framing stays under 9.0s (6.965 · 7.749 · 8.323 max). Each pair: no `transition`
SFX at the joint (§2 `holds`), one ground hex shared across both scenes (§11), and the second
scene's `plateKen` picks up exactly where the first ended. **A derived crop, never the same file
pointed at twice.**

### 6c. Two more second framings, both derived crops

| scene | dur | `data-framings` | swap at | anchored to | second file |
|---|---|---|---|---|---|
| s56 (5.4) | 7.513 | `4.100, 3.413` | **+4.100** | *"another reads"* | `s56b.jpg` — tighter on the second table |
| s67 (5.15) | 8.506 | `4.800, 3.706` | **+4.800** | *"at four percent"* | `s67b.jpg` — tighter on the lit window |

Both clear their scene's last fixed text cue by ≥1.4s. **Emit `data-framings` on all 81
sections** — on the 76 single-framing scenes it is one value equal to `scene_duration`. That
costs nothing and removes any question about whether an absent attribute means "one framing" or
"not declared". Framings always sum to `scene_duration` (= `data-duration` − 0.45).

---

## 7. Scenes — the archetype row

One row per VO line. `start` / `dur` = `scene_start` / `scene_duration`, **verbatim from
`timing.json`, the only home**; `d-dur` = `dur + 0.45` (s81 bare). Every fixed cue is
`start + offset` from §5.

`arch`: **A** plate · **B** figure · **C** ledger · **D** band. `ground`: the scene's `--f1`
(§11). `art`: `off` · `fwd` (= `art-forward`) · a named layer. `ctr`: `centred` — **the rule is
deterministic: a scene is `centred` unless something real occupies the archetype's other side**
(a drawn layer, the Lottie stage, or a declared cascade owning the band). `fin-build` then drops
that scene's plate, `crule`, `vrule` and `brule`; a split with nothing opposite is a hole.
`trans`: `dis` = 0.45s dissolve · **`SHOVE`** · `hold` = matched-frame continuous zoom (§6).
`sfx`: the CONTENT cue this scene is expected to emit (§2) — `—` means DRY, joint only.
**Every scene carries `has-photo` and a real `.bg`. There are no exceptions and none may be added.**

| # | line | start | dur | d-dur | trans | arch | ground | art | ctr | focal · var · role | `#sN-rate` | sfx | bg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1.1 | 0.000 | 3.543 | 3.993 | dis | A | `#161f2b` | off | Y | stmt · A · — | — | — | `s1.jpg` |
| 2 | 1.2 | 3.543 | 5.711 | 6.161 | dis | D | `#1a1e24` | off | **N** | 3 chips · C · — | — | — | `s2.jpg` |
| 3 | 1.3 | 9.254 | 5.345 | 5.795 | **hold** | A | `#241d15` | off | Y | stmt · A · — | — | — | `s3.jpg` |
| 4 | 1.4 | 14.599 | 6.965 | 7.415 | dis | D | `#241d15` | **lottie `phone-notify-credit`** | **N** | stmt · A · — | — | **buzz** | `s4.jpg` ⟵ crop of s3 |
| 5 | 1.5 | 21.564 | 3.987 | 4.437 | dis | A | `#1c2027` | off | Y | stmt · A · — | — | — | `s5.jpg` |
| 6 | 1.6 | 25.551 | 5.711 | 6.161 | dis | D | `#291f13` | off | **N** | 3 chips · C · — | — | — | `s6.jpg` |
| 7 | 1.7 | 31.262 | 6.887 | 7.337 | dis | A | `#301519` | off | Y | stmt · A · **warn** | — | **stamp** | `s7.jpg` |
| 8 | 1.8 | 38.149 | 8.271 | 8.721 | dis | A | `#1f1e1c` | off | Y | stmt · A · — | — | — | `s8.jpg` |
| 9 | 2.1 | 46.420 | 5.162 | 5.612 | dis | A | `#2a2113` | off | Y | stmt · A · target | — | reveal | `s9.jpg` |
| 10 | 2.2 | 51.582 | 10.596 | 11.046 | dis | D | `#2e2411` | off | Y | stmt · A · target | — | reveal + swap | `s10.jpg` + `s10b.jpg` |
| 11 | 2.3 | 62.178 | 8.167 | 8.617 | dis | A | `#2a2113` | off | Y | stmt · A · target | — | reveal | `s11.jpg` |
| 12 | 2.4 | 70.344 | 3.856 | 4.306 | dis | C | `#1a1e24` | off | Y | stmt · A · — | — | — | `s12.jpg` |
| 13 | 2.5 | 74.201 | 6.887 | 7.337 | dis | C | `#2a2113` | off | Y | stmt · A · target | — | reveal | `s13.jpg` |
| 14 | 2.6 | 81.087 | 7.069 | 7.519 | dis | C | `#191f28` | off | Y | stmt · A · — | — | — | `s14.jpg` |
| 15 | 2.7 | 88.157 | 7.069 | 7.519 | dis | C | `#2e2411` | off | Y | stmt · A · target | — | reveal | `s15.jpg` |
| 16 | 2.8 | 95.226 | 6.364 | 6.814 | dis | B | `#372a0c` | **fwd `survival-grid`** | **N** | num `95%` · B · target | — | — | `s16.jpg` |
| 17 | 2.9 | 101.590 | 7.487 | 7.937 | dis | A | `#2a2113` | off | Y | stmt · A · target | — | **stamp** | `s17.jpg` |
| 18 | 2.10 | 109.078 | 7.618 | 8.068 | dis | D | `#0f2a1a` | **fwd `division-block`** | **N** | stmt · A · fund | — | reveal | `s18.jpg` |
| 19 | 2.11 | 116.696 | 6.547 | 6.997 | dis | B | `#2a2113` | off | Y | num `$10,169` · B · target | — | — | `s19.jpg` |
| 20 | 2.12 | 123.242 | 7.487 | 7.937 | dis | B | `#1f1e1c` | off | Y | num `$847` · B · — | — | — | `s20.jpg` |
| 21 | 2.13 | 130.730 | 6.077 | 6.527 | dis | B | `#12351f` | off | Y | num `$254,225` · B · fund | **`.sub`** | **hero** | `s21.jpg` |
| 22 | 2.14 | 136.807 | 7.383 | 7.833 | dis | B | `#12351f` | off | Y | stmt · A · fund | **span** | reveal | `s22.jpg` |
| 23 | 2.15 | 144.189 | 7.749 | 8.199 | dis | A | `#0f2a1a` | off | Y | stmt · A · fund | — | reveal | `s23.jpg` |
| 24 | 3.1 | 151.938 | 2.890 | 3.340 | dis | A | `#1c2027` | off | Y | stmt · A · — | — | reveal | `s24.jpg` |
| 25 | 3.2 | 154.828 | 6.129 | 6.579 | dis | B | `#2a2113` | off | Y | num `$13,318` · B · target | — | — | `s25.jpg` |
| 26 | 3.3 | 160.957 | 7.905 | 8.355 | dis | D | `#1f1e1c` | off | **N** | 4 chips (2+2) · C · — | — | — | `s26.jpg` |
| 27 | 3.4 | 168.862 | 6.599 | 7.049 | dis | B | `#12351f` | off | Y | num `$332,950` · B · fund | **`.sub`** | — | `s27.jpg` |
| 28 | 3.5 | 175.461 | 6.364 | 6.814 | dis | A | `#301519` | off | Y | stmt · A · warn | — | reveal | `s28.jpg` |
| 29 | 3.6 | 181.825 | 6.416 | 6.866 | dis | B | `#2a2113` | off | Y | num `$26,266` · B · target | — | — | `s29.jpg` |
| 30 | 3.7 | 188.242 | 6.651 | 7.101 | dis | B | `#2e2411` | **fwd `housing-share`** | **N** | num `33.4%` · B · target | — | — | `s30.jpg` |
| 31 | 3.8 | 194.893 | 6.599 | 7.049 | dis | B | `#12351f` | off | Y | num `$656,650` · B · fund | **`.sub`** | — | `s31.jpg` |
| 32 | 3.9 | 201.492 | 6.599 | 7.049 | dis | A | `#241d15` | off | Y | stmt · A · — | — | reveal | `s32.jpg` |
| 33 | 3.10 | 208.091 | 3.569 | 4.019 | dis | C | `#301519` | off | Y | stmt · A · warn | — | reveal | `s33.jpg` |
| 34 | 3.11 | 211.660 | 6.965 | 7.415 | dis | C | `#38151a` | off | Y | stmt · A · warn | — | reveal | `s34.jpg` |
| 35 | 3.12 | 218.625 | 6.599 | 7.049 | dis | D | `#38151a` | off | Y | stmt · A · warn | — | reveal | `s35.jpg` |
| 36 | 3.13 | 225.224 | 6.312 | 6.762 | dis | C | `#301519` | off | Y | num `30 YEARS` · B · warn | — | — | `s36.jpg` |
| 37 | 3.14 | 231.536 | 7.148 | 7.598 | dis | C | `#38151a` | off | Y | stmt · A · warn | — | reveal | `s37.jpg` |
| 38 | 3.15 | 238.684 | 6.312 | 6.762 | dis | A | `#301519` | off | Y | stmt · A · warn | — | **stamp** | `s38.jpg` |
| 39 | 3.16 | 244.996 | 3.543 | 3.993 | **SHOVE** | A | `#101720` | off | Y | kicker only · A · — | — | — | `s39.jpg` |
| 40 | 4.1 | 248.539 | 7.304 | 7.754 | dis | B | `#2a2113` | off | Y | num `$5,000 A MONTH` · B · target | *marker* | — | `s40.jpg` |
| 41 | 4.2 | 255.843 | 7.749 | 8.199 | **hold** | B | `#0f3a20` | off | Y | num `$1,500,000` · B · fund | **`.sub`** | **hero** | `s41.jpg` |
| 42 | 4.3 | 263.592 | 6.469 | 6.919 | dis | B | `#0f3a20` | off | Y | stmt · A · fund | **span** | — | `s42.jpg` ⟵ crop of s41 |
| 43 | 4.4 | 270.060 | 7.200 | 7.650 | dis | D | `#1c2027` | off | Y | stmt · A · — | — | reveal | `s43.jpg` |
| 44 | 4.5 | 277.260 | 5.711 | 6.161 | dis | A | `#2b1418` | off | Y | stmt · A · warn | — | reveal | `s44.jpg` |
| 45 | 4.6 | 282.971 | 6.834 | 7.284 | dis | C | `#301519` | off | **N** | 3 chips · C · warn | — | chip | `s45.jpg` |
| 46 | 4.7 | 289.806 | 4.744 | 5.194 | dis | D | `#38151a` | off | Y | stmt · A · warn | — | reveal | `s46.jpg` |
| 47 | 4.8 | 294.550 | 6.233 | 6.683 | dis | A | `#301519` | off | Y | stmt · A · warn | — | reveal | `s47.jpg` |
| 48 | 4.9 | 300.784 | 5.946 | 6.396 | dis | D | `#2b1418` | off | Y | stmt · A · warn | — | reveal | `s48.jpg` |
| 49 | 4.10 | 306.730 | 7.383 | 7.833 | dis | D | `#301519` | **fwd `yield-fraction`** | **N** | stmt · A · warn | — | **tick** | `s49.jpg` |
| 50 | 4.11 | 314.113 | 7.801 | 8.251 | dis | B | `#38151a` | off | Y | num `13.84%` · B · warn | — | — | `s50.jpg` |
| 51 | 4.12 | 321.913 | 7.435 | 7.885 | dis | C | `#301519` | off | Y | stmt · A · warn | — | reveal | `s51.jpg` |
| 52 | 4.13 | 329.349 | 6.469 | 6.919 | dis | D | `#38151a` | off | Y | stmt · A · warn | — | **stamp** | `s52.jpg` |
| 53 | 5.1 | 335.817 | 7.435 | 7.885 | dis | A | `#2a2113` | off | Y | stmt · A · target | — | reveal | `s53.jpg` |
| 54 | 5.2 | 343.252 | 5.711 | 6.161 | dis | A | `#1c2027` | off | Y | stmt · A · — | — | reveal | `s54.jpg` |
| 55 | 5.3 | 348.963 | 4.562 | 5.012 | dis | B | `#2e2411` | off | Y | **`.mega` `ABOUT 1%`** · B · target | — | **hero** | `s55.jpg` |
| 56 | 5.4 | 353.525 | 7.513 | 7.963 | dis | C | `#2a2113` | off | Y | 2 chips · C · target | — | swap | `s56.jpg` + `s56b.jpg` |
| 57 | 5.5 | 361.038 | 7.670 | 8.120 | dis | D | `#131f2c` ⚠ | off | Y | stmt · A · warn | — | reveal | `s57.jpg` |
| 58 | 5.6 | 368.709 | 5.215 | 5.665 | **SHOVE** | D | `#0e1c2e` ⚠ | off | Y | stmt · A · warn | — | reveal | `s58.jpg` |
| 59 | 5.7 | 373.923 | 7.383 | 7.833 | dis | B | **`#0c1a2c`** ⚠ | off | Y | num `$5,555,556` · B · warn | **`.sub`** | **hero** | `s59.jpg` |
| 60 | 5.8 | 381.306 | 7.513 | 7.963 | dis | B | `#2a2113` | off | Y | stmt · A · target | **2 spans** | reveal | `s60.jpg` |
| 61 | 5.9 | 388.820 | 7.200 | 7.650 | dis | B | **`#3b1219`** | off | Y | num `ROUGHLY 4 TIMES` · B · warn | — | **hero** | `s61.jpg` |
| 62 | 5.10 | 396.020 | 6.495 | 6.945 | dis | B | `#2a2113` | off | Y | num `ABOUT 3%` · B · target | — | — | `s62.jpg` |
| 63 | 5.11 | 402.514 | 6.364 | 6.814 | dis | B | `#2e2411` | off | Y | num `$1,929,260` · B · target | **`.sub`** | — | `s63.jpg` |
| 64 | 5.12 | 408.878 | 6.913 | 7.363 | dis | D | `#2a2113` | off | **N** | 3 chips · C · target | — | chip ×3 | `s64.jpg` |
| 65 | 5.13 | 415.791 | 3.909 | 4.359 | dis | A | `#1c2027` | off | Y | stmt · A · — | — | — | `s65.jpg` |
| 66 | 5.14 | 419.700 | 6.599 | 7.049 | dis | C | `#2a2113` | off | Y | num `$78,535` · B · target | — | — | `s66.jpg` |
| 67 | 5.15 | 426.299 | 8.506 | 8.956 | dis | B | `#12351f` | off | Y | num `$1,963,375` · B · fund | **`.sub`** | swap | `s67.jpg` + `s67b.jpg` |
| 68 | 5.16 | 434.805 | 7.096 | 7.546 | dis | B | `#38151a` | off | Y | num `$7,271,759` · B · warn | **`.sub`** | — | `s68.jpg` |
| 69 | 6.1 | 441.900 | 6.469 | 6.919 | dis | A | `#301519` | off | Y | stmt · A · warn | — | reveal | `s69.jpg` |
| 70 | 6.2 | 448.369 | 6.469 | 6.919 | dis | C | `#2a2113` | off | Y | num `3.9%` · B · target | — | — | `s70.jpg` |
| 71 | 6.3 | 454.838 | 7.148 | 7.598 | dis | C | `#2e2411` | off | Y | num `4.7%` · B · target | — | — | `s71.jpg` |
| 72 | 6.4 | 461.985 | 6.312 | 6.762 | dis | C | `#301519` | off | Y | stmt · A · warn | — | reveal | `s72.jpg` |
| 73 | 6.5 | 468.297 | 6.181 | 6.631 | dis | D | `#38151a` | off | Y | stmt · A · warn | — | **stamp** | `s73.jpg` |
| 74 | 6.6 | 474.478 | 3.987 | 4.437 | dis | A | `#0f2a1a` | off | Y | stmt · A · fund | — | — | `s74.jpg` |
| 75 | 6.7 | 478.465 | 7.096 | 7.546 | **hold** | D | `#12351f` | **fwd `ladder-bars-1-3`** | **N** | 3 `.sub` lines · C · fund | **`.sub`** | — | `s75.jpg` ⟵ crop of s76 |
| 76 | 6.8 | 485.561 | 8.323 | 8.773 | dis | D | `#12351f` | **fwd `ladder-bars-4-5`** | **N** | 2 `.sub` lines · C · fund | **`.sub`** | — | `s76.jpg` |
| 77 | 6.9 | 493.884 | 7.905 | 8.355 | dis | B ⚠`p-a` | `#38151a` | **fwd `ladder-overrun`** | **N** | num `$5,555,556` · B · warn | **`.sub`** | **hero** | `s77.jpg` |
| 78 | 6.10 | 501.789 | 5.946 | 6.396 | dis | D | `#1c2027` | off | Y | stmt · A · — | — | — | `s78.jpg` |
| 79 | 6.11 | 507.736 | 6.913 | 7.363 | dis | A | **`#2d2214`** | off | Y | stmt · A · — | — | — | `s79.jpg` |
| 80 | 6.12 | 514.648 | 5.659 | 6.109 | dis | A | `#12351f` | off | Y | stmt · A · fund | — | reveal | `s80.jpg` |
| 81 | 6.13 | 520.307 | 7.566 | **7.566** | — | A | `#33200f` | off | Y | `.cta` · D · **pop** | — | **cta** | `s81.jpg` |

### The archetype sequence, read as a rhythm

```
ch1  A D A D A D A A
ch2  A D A C C C C B A D B B B B A
ch3  A B D B A B B B A C C D C C A A
ch4  B B B D A C D A D D B C D
ch5  A A B C D D B B B B B D A C B B
ch6  A C C C D A D D B D A A A
```

Totals **A 25 · B 29 · C 15 · D 12**. B-heavy, because most beats in this video *are* a figure
— that is the argument, not a lack of variety.

**Six deliberate holds, each because the scenes are one argument:**

- **ch2 `C C C C` (s12–s15)** — "it is two papers" → Bengen → what he tested → Trinity. Four
  artefacts, one evidentiary case; the *artefact* changes underneath (two stapled papers → an
  open journal → a printed table → a bound volume). Varying the layout here would break the
  only through-line the chapter has.
- **ch2 `B B B B` (s19–s22)** — $10,169 → $847 → $254,225 → what it replaces. One number walked
  down to one corpus. This is the chapter's spine and the shape every later rung repeats.
- **ch3 `B B B` (s29–s31)** — housing yearly → its share and its month → its corpus. One rung.
- **ch3 `C C` (s33–s34)** and **`C C` (s36–s37)** — the papers' own fine print, split by the
  `D` at s35 because 3.12 is the CONSEQUENCE ("every rung here is a before-tax number"), not a
  document.
- **ch4 `B B B` (s40–s42)** — the worked figure → the division → both halves together. The hero
  chain, and s41→s42 is one continuous shot (§6b).
- **ch5 `B B B B B` (s59–s63)** — the answer, the pair, the gap, the middle route, the middle
  price. Five figures, ONE argument: what each route costs for the identical paycheck. The
  mechanism changes under it every time (an empty warehouse → two envelopes → four crates
  against one → a factsheet → a storage door), and `D` at s64 closes the run by naming it.

**Every rung is `B B`** — the corpus named, then its arithmetic worked: s19/s21, s25/s27,
s29/s31, s40/s41, s66/s67. That regularity is the ladder made visible.

**⚠ s77 overrides its plate to `p-a`** (full-frame). `.p-b` maps viewBox x 1:1 to screen x on
an 860px plate, so anything past vx = 800 does not exist on the encode — and the overrun bar is
2,603px by construction (§9c). japanese-money-methods ch2 lost the entire point of a frame to
exactly this, with every check passing.

---

## 8. Vector art — 7 drawn proportions, 1 Lottie, 0 icons, 0 emoji

Rule 8 is the test: **if you cannot say what the art asserts that the picture cannot, it is
`off`.** It is `off` on **73 of 81 scenes**. Density against the archetype note's calibration
("three or four drawn layers in a twelve-to-fourteen scene chapter is the top of the range, not
the target"): ch1 **1 (the Lottie)** · ch2 **2** · ch3 **1** · ch4 **1** · ch5 **0** · ch6 **3**.

All seven drawn layers are `art-forward` (52%) because the point of each is a **PROPORTION** and
the mechanism still wins; the photograph is there to satisfy `image_per_scene`. All are authored
**in the plate's own coordinate space**, never in 1920×1080.

| scene | line | plate · viewBox | motif | what it ASSERTS that the photograph cannot | arithmetic (truth_bar) |
|---|---|---|---|---|---|
| **s16** | 2.8 | `p-b` · `0 0 800 610` | **`survival-grid`** — a 10×10 grid, 95 cells solid `--target`, 5 left as ghost rects at ~.2 | **the SHARE**: 95 periods in 100. A photograph of a printed page states that a study exists; it cannot state 95 of 100 | exactly 95 solid of 100, equal cells. Trinity Table 3, 4.0% inflation-adjusted, 30-year payout |
| **s18** | 2.10 | `p-d` · `0 0 1920 656` | **`division-block`** — a small solid bill block, a heavy 12px divisor rule beneath it, resolving right into a corpus block **25× wider** | **the SHAPE of the arithmetic the whole video runs.** The photo shows a hand writing; only the drawing shows that ÷4% *is* ×25 | corpus block width = 25.00 × the bill block (1 ÷ 0.04). State it in the generator comment at the point of edit |
| **s30** | 3.7 | `p-b` · `0 0 800 610` | **`housing-share`** — one full-width solid bar = total household spending, its left **33.4%** filled `--target`, the remainder a ghost rect at ~.2 | **the share of a budget.** A dusk roofline says "housing"; it cannot say "a third of everything they spent" | filled = 0.334 of the bar exactly. BLS CE 2024 |
| **s49** | 4.10 | `p-d` · `0 0 1920 656` | **`yield-fraction`** — set as a FRACTION: a numerator block that never changes, a heavy 12px rule, a denominator block that halves; the quotient bar sits **below and separate**, doubling | **payout constant, price falling, yield doubling.** The photo (a peeled price sticker) says "the price changed"; only the drawing says the payout did not | denominator × 0.5 ⇒ quotient × 2.0 exactly. **Deliberately a fraction, not three parallel bars** — the hi cut's funnel read as a rising growth curve, and parallel bars would read as a chart |
| **s75** | 6.7 | `p-d` · `0 0 1920 656` | **`ladder-bars-1-3`** — bars 1, 2, 3 at the §9a scale (119 / 156 / 308 px of 920), each riding its own `.sub` line's cue | **three corpus figures to ONE scale.** The photo shows three crates; it cannot show 119 : 156 : 308 | the §9a scale, unchanged: 920px = $1,963,375 |
| **s76** | 6.8 | `p-d` · `0 0 1920 656` | **`ladder-bars-4-5`** — bars 1–3 held, 4 and 5 added (703 / 920 px) | the ladder **completing**, continuous with s75 across the hold | same scale, same track |
| **s77** | 6.9 | **`p-a`** · `0 0 1920 1080` | **`ladder-overrun`** — the completed five-bar ladder ghosted at ~.2, one new bar at **scaleX 2.8296** running off the right edge of the frame | **that this number is off the scale of everything just watched.** No photograph can leave the frame | $5,555,556 ÷ $1,963,375 = 2.8296 ⇒ 2,603px from x=500; 1,420px visible, the rest off-canvas **by design**. The only element in the cut permitted to leave the frame, and leaving is the assertion |

**Construction rules all seven obey** (they cost two draft rounds on japanese-money-methods and
one shipped invisible funnel on this run's hi cut):

- **Solid fills and heavy strokes only.** `.has-photo .art` is 30% and `.art-forward` 52%; a
  2–3px stroke at 0.4 alpha is simply not on screen. Ghost tracks are **filled rects at ~.2**,
  never outlines. Nothing thinner than 9px. *(The hi cut shipped `s16`'s funnel at fill-opacity
  `.18`, under `art_opacity.over_photo` 0.3 — the chapter's one drawn mechanism was invisible.)*
- **The per-scene `opacity` on the `<svg>` is a no-op** — `.has-photo .art` and
  `.has-photo.art-forward .art` both carry `!important`. The only levers that reach the screen
  are the weight and alpha of the elements inside.
- `stroke-width="N"` as an SVG **attribute is a no-op** — write inline `style="stroke-width:N"`.
- Any group that scrolls needs a `clipPath` or it rides out of its band into the type.
- **Never darken the photograph** to make art readable (rule 9; creator rejected it 2026-08-04,
  *"it fails to black and white"*). s18, s49, s75, s76 and s77 each get a **`.band`** behind
  their mechanism (`#sN-band`, bottom 54%). **`.art-lift` on s16 and s30**, whose plates sit on
  the brighter part of their still.
- **Assemble by about +3.3**, or the contact sheet's +2.6s sample reads as a half-built frame.
  **Declared exception: s75 and s76 are enumerations** — their bars ride a 0.6s cascade and
  finish at ~+4.0. **Judge those two from the mp4, not the sheet.**

### One Lottie — `phone-notify-credit` on s4 (1.4)

Library reuse, **no fetch**: `assets/lottie/phone-notify-credit.json` (in-house, already used on
`japanese-money-methods-hi-ch1 s1` and this run's hi ch1). **No tint** — `index.json` records it
as authored in the system's own palette, and tinting would push it into a role colour 1.4 has
not earned.

- **Why it is additive, not depictive.** The photograph is a phone **face-down** — the design
  system bans a phone-screen photo as a background and this has shipped undetected three times.
  The drawn banner is the only honest way to state that money **arrived**; the picture is
  structurally forbidden from saying it.
- **The amount is MASKED but the currency is NOT.** The card reads `$ • • • •`. Naming a figure
  at 0:15 would break the open loop the whole cold open is built on (the number is withheld
  until 4.2), but the hi cut's ch1 review found the opposite failure: a banner with no currency
  glyph at all says *"a notification arrived"*, not *"money arrived"* — on the one beat a
  45-second cold open exists to deliver. Masked digits, visible `$`.
- **Stage in PIXELS.** `.p-d` band, `left/top/width/height` declared in px with
  `.stage svg { width:100% !important; height:100% !important }`. A stage without pixel
  dimensions renders the artwork at native size pinned top-left and every check passes.
- Cue: `playLottie` **anchored +1.85** on *"buzzes"*; `s4-stmt` `rise` at **+2.75** (the words
  are the consequence, so they follow the banner). `buzz` SFX at the same +1.85 — the kit's only
  diegetic sound, legal here precisely because the frame shows the object making the noise.

**One Lottie, not four.** The cap is `max_per_chapter: 4` — a threshold at which you must
justify the next one, never a target. `lottie-web` redraws the whole illustration every frame
(two heavy ones took a 20s 1080p render from 1m27 to 3m56), and a deck of them stops looking
like a film.

### What was considered and refused

| candidate (script handoff §12) | verdict |
|---|---|
| **2.2 / 4.7 / 5.5 — the tank at three tap positions** | **`off`, all three.** A drawn tank over a photographed tank is the "ghost envelope over a photograph of an envelope" failure by name. The tank is carried **photographically** across four frames (§10) and the tap position alone says the beat |
| **4.7 — a 12% tap drawn beside a 4% tap** | **REFUSED on the script's own ⚠.** Drawing the two apertures side by side says a yield and a withdrawal rate are the same kind of thing — the exact conflation the study caught twin B making and that this chapter exists to avoid |
| **4.8 — how long a tank lasts at each rate** | **REFUSED.** A balance falling to zero over time asserts a **depletion schedule we have no source for**, and a drawn projection is the shape `no_return_promise` forbids. Same call the hi cut made |
| **5.5 — one dial moving 4.0 → 1.08** | the photograph *is* a hand on a dial (5.6) and a thin stream (5.5) — depictive. `off` |
| **5.9 — four crates against one** | the photograph is four crates against one. `off` |
| **5.12 — three lanes at three rates** | the photograph is three converging lanes. `off` |
| **4.11 — the yield series since 1871** | **REFUSED.** Drawing the series asserts every point of a curve we have one figure from. The archival page plus the `foot:` citation is the honest treatment, and `truth_bar` forbids fabricating a source document |

**No icons.** `assets/icons/` holds `checkbox-tick`, `padlock-closed`, `pen-nib-line`,
`reorder-rules`, `growth-arrow`, and none asserts anything this cut's photographs do not already
say: a padlock over a vault door, an arrow over a ladder, a tick over a conclusion page are all
the rule-8 depictive failure. **No drawn layer of any kind sits on s41, s55 or s59** — the three
frames carrying the video's big numbers already have their one focal element.

**Zero emoji, deliberately.** They are an OS font sitting outside the grade and would land as a
sticker on a dark documentary frame. The ⚠ and ⟵ marks in this file are storyboard notation,
never composition text.

---

## 9. The two peaks, and the ladder that climbs under them

### 9a. The measure bar means CORPUS, at ONE scale, on six frames

fin-script put housing at rung 3 because BLS housing is $2,189/month, below the $5,000/month
hero — a descending ladder kills the format's only escalation. So the **monthly** figures do not
ascend, but the **corpus** figures do, monotonically, and that is what the video is about. The
climb is therefore drawn, in one component, at one scale:

```
track  .measure.under = 920px wide, left calc(50% - 460px), top 910px, height 7px
scale  920px = $1,963,375   (rung five, the whole household at 4.0%)   1px = $2,134.10
```

| scene | line | corpus | scaleX | px | `#sN-mlab` |
|---|---|---|---|---|---|
| s21 | 2.13 | $254,225 | **0.1295** | 119.1 | `THE LADDER` |
| s27 | 3.4 | $332,950 | **0.1696** | 156.0 | `THE LADDER` |
| s31 | 3.8 | $656,650 | **0.3345** | 307.7 | `THE LADDER` |
| s41 | 4.2 | $1,500,000 | **0.7640** | 702.9 | `THE LADDER` |
| s42 | 4.3 | $1,500,000 | **held, no re-animation** | 702.9 | `THE LADDER` |
| s67 | 5.15 | $1,963,375 | **1.0000** | 920.0 | `THE LADDER` |

119 → 156 → 308 → 703 → 920. Every one of those frames is already a rate frame, so the bar never
appears without `AT 4.0%` beside it. `.centred` does **not** hide `.measure` / `.measure-lab`
(they are centred by their own `left: calc(50% - 460px)`), which is the whole reason the device
survives on a photo-led cut.

⚠ **Gotcha 7 — a drawn proportion's numerator and denominator are a PAIR.** The 920px track and
every fill above are ONE arithmetic; never move one without the other, and **never re-use this
component at a different scale.** The bar appears on these six frames and nowhere else.
$5,555,556 does not fit — 2,603px against a 920px track — and its absence on s59 is deliberate.
The overrun is drawn once, at s77, where a completed ladder exists to overrun.

⚠ The label reads `THE LADDER`, never `RUNG 3 OF 5`. **A rung count is a counter, and counters
are what the no-rail rule removed.**

### 9b. PEAK 1 — $1,500,000 at 4.0% (s41–s42, 48.5–51.2%)

Its power is **continuity**: the top of a climb, in the same frame family as rungs one to three,
four times bigger. Its device is the one thing no other frame gets — **the formula completes
across a single unbroken shot.**

- **s41 (4.2)** — `arch B`, ground `#0f3a20` (the hottest green in the video), `$1,500,000` at
  `.huge` 112 landing at **+5.18** on *"one and a half million"*, the rate on screen since
  +1.10, the bar filling to 702.9px on the same cue, `hero`.
- **s42 (4.3)** — the *same photograph*, tighter on the vault dial, **one continuous zoom**
  (`plateKen` 1.00→1.08 then 1.08→1.16), same ground, bar held, focal
  `$1,500,000 AT 4.0% = $5,000 a month` with the rate as an inline span. **Dry.**

Both halves of the formula land on one continuing image: `withdrawal_rate_on_screen` made into a
camera move rather than a caption.

### 9c. PEAK 2 — $5,555,556 at 1.08% (s59, 70.8%) — the title's own answer, not a footnote

The reward beat for the promise in the title, and it gets **four things peak 1 does not**:

1. **A shove into it** (s58 → s59) — 5.6 literally cues a cut: *"watch what happens to the
   number."* One of only two shoves in the cut.
2. **The three coldest grounds in the video** (`#131f2c` → `#0e1c2e` → **`#0c1a2c`**) — *the drop
   is a temperature event before it is a number.*
3. **The calmest, emptiest photograph in the cut** — a bare warehouse floor, one pallet, wide.
   One enormous figure alone in an empty room.
4. **No measure bar, deliberately** — it is off the ladder's scale, and the frame says so by
   carrying nothing but the number, its yield and its arithmetic.

And the cut's **only `.mega`** sits four scenes earlier at **s55 (5.3) `ABOUT 1%`**, 300px. That
is what makes peak 2 land: *in a video arguing that the rate is the whole answer, the RATE is
the one enormous number on screen, and the corpus it produces follows it.* `.mega` appears
**exactly once in the video** (`one_focal_per_scene`; never `.huge` and `.mega` together).

The recap pays peak 2 a **second** time at **s77 (6.9)** with the `ladder-overrun` — a completed
five-bar ladder the viewer has now watched assemble, and one new bar leaving the frame. Peak 1
is paid back in the same breath at s76 and is *inside* the ladder; peak 2 is the only thing that
does not fit in it.

---

## 10. Imagery — 84 slots, 84 files, zero photo-free scenes

**`image_per_scene` is a hard creator rule** (2026-07-28, `photo_free_scene_ratio` = 0). All 81
scenes carry `has-photo` and a real full-bleed `.bg` under the locked grade
`grayscale(.32) brightness(.62) contrast(1.05)`. **No per-scene grade override anywhere in this
cut** — the chapter archetype layer closes that escape hatch, so the photograph is the only
variable there is.

- **81 bg slots** + **3 in-scene second framings** (`s10b`, `s56b`, `s67b`) = **84 slots**.
- **78 fetched files.** `assets/img/manifest.json` is the single home for every query.
- **6 derived crops, no fetch and no manifest key** — `fin-assets` crops them from a source it
  already holds, at full resolution, and records the crop rect in `.src`:

| derived file | cropped from | what the crop lands on |
|---|---|---|
| `s4.jpg` | `s3.jpg`'s source | the phone lying face-down beside the mug |
| `s10b.jpg` | `s10.jpg`'s source | the tap, low on the tank's side |
| `s42.jpg` | `s41.jpg`'s source | the vault dial |
| `s56b.jpg` | `s56.jpg`'s source | the second of the two printed tables |
| `s67b.jpg` | `s67.jpg`'s source | the lit window of the house |
| **`s75.jpg`** | **`s76.jpg`'s source** | the smaller three of the five crates *(inverted — the wide frame is the fetched one)* |

### The grade decides the photograph — write the LIGHT, not the object

Enforced: `pipeline_check check assets --chapter <N>` fails any promoted image with source
**`YHIGH < 110`**, and warmth has its own predictor (**mean R−B ≥ ~+40** on the raw). Every query
in `manifest.json` therefore names the lighting. Three rules from this run's own hi ch1, where
three of seven backgrounds failed for one reason:

1. **Never buy high-key stock.** A white-dominant subject cannot survive `brightness(.62)`; it
   lands as a flat charcoal slab. Ask for the subject **lit against a dark ground**.
2. **Replacing one white photo with another white photo re-breaks it.** When a frame reads grey,
   the fix is a differently-lit original, not a re-crop.
3. **When a slot fails twice on brightness, change the MATERIAL, not the adjective.** Enamel,
   glass, glazed ceramic, brass, polished metal and wet stone have a specular ceiling; matte
   paper, kraft, cardboard and unfinished wood do not. **This is why 1.5's "blank index card" is
   specified as a blank white ENAMEL tag, and 3.8's "paper envelope" as BRASS on dark slate** —
   the hi cut solved its s4 exactly this way (enamel plaque, YHIGH 203, after kraft measured
   dead twice).

### Eight overrides against the script's own `img:` cues

| scene | script cue | this storyboard | why |
|---|---|---|---|
| s3 / s4 (1.3, 1.4) | "the phone now face-up beside the mug, notification glow" | phone **face-down**, its edge and the wood lit by the glow; the notification is the Lottie | **Never a phone-screen photo as a background.** Shipped undetected three times |
| s7 (1.7) | "a laptop showing a blurred search results page" | laptop **from behind**, screen not visible, hands on the keys, one lamp | same rule; a search page is also someone's brand |
| s45 (4.6) | "a phone held up showing a blurred short-video feed" | hand holding a phone with the **screen turned away**, only the glow on the fingers | same rule, and this is the most tempting violation in the cut because the frame is *about* a feed |
| s55 (5.3) | "a market data screen photographed at a shallow angle" | a **printed** index chart pinned to a bare office wall | same rule for a monitor — and this is the `.mega` frame, which needs the calmest background in the chapter |
| s5 (1.5) | "a single blank index card… hard side light" | a blank white **enamel** tag on dark oak | matte card measures dead under the grade (material rule above) |
| s31 (3.8) | "a single house key on a plain paper envelope" | a **brass** house key on dark slate | same; and brass gives the specular ceiling the gate needs |
| s30 (3.7) | "a printed pie-slice diagram on a statistical release page" | a house roofline silhouetted against a warm dusk sky | the cue is **depictive** (the drawn share bar states 33.4%, §8) **and** a generic pie chart cited to BLS is the fabricated-source-document failure |
| s69 (6.1) | "a single chair in an empty room" | a **brass plumb bob** hanging still against a dark workshop wall | s80 (6.12) is already an empty chair by a window; two chair frames read as one image reused, which the sound-off rule forbids |

### The returning objects — a visual rhyme, never a reused file

The sound-off rule is **per line**: same object family, new photograph, and the difference must
be legible with the sound off.

| object | frames | what differs, and what must stay the same |
|---|---|---|
| **the tank** | s10 (2.2) · s46 (4.7) · s47 (4.8) · s57 (5.5) | **tap position alone says the beat**: low flow → wide open, water running out → level low, still open → barely cracked, a thin stream into a tin cup. The **brass tap on a plain steel body under workshop light** is the recognisable constant. ⚠ **Source all four from one set if at all possible.** Fallback, declared: buy the wide tank at Pexels `large2x` and source the other three as tap/stream macros in the same material family — the tap is what carries the rhyme, not the tank's silhouette |
| **the ladder** | s8 (1.8) · s23 (2.15) · s74 (6.6) | the lowest rungs with the top out of frame → a macro of ONE rung, polished by use → the whole ladder, full height. Three photographs, three different statements |
| **the crates** | s61 (5.9) · s75/s76 (6.7, 6.8) · s77 (6.9) | four against one → a line of five increasing → one far larger, alone. The recap deliberately rhymes with the gap beat |
| **the morning** | s1 / s3–s4 → **s79** (6.11) | s79 is the same nightstand and phone in **late-afternoon light, the day over** — a distinct fetch, a callback, not a reuse |

### Standing rejections, restated so a re-fetch cannot lose them

- **No faces.** Hands and objects only — s18, s33, s45, s53, s58 are the only frames with a hand
  and every one is specified hands-only. It is a licence issue as much as a design one.
- **s51 (4.12) is the one exception and it is archival**: a 1930s American breadline, wide,
  **faces indistinct**. Source from **Wikimedia Commons / Library of Congress**, not Pixabay.
  s50 (4.11) is likewise a US archival newspaper page — a Depression photo from another market
  is the same defect class as the euro coin that shipped in the first `-en` cut.
- **Every frame is American.** Sweep every photo for non-US currency, signage, plugs, licence
  plates and vehicles before the build gate. Currency must be **genuine current US notes**,
  never prop money, never the other cut's currency. **No `₹` anywhere, in any frame.**
- **Nothing legible that is a fabricated source.** s12, s13, s14, s15, s34, s37, s62, s66, s70
  are photographed with **no legible title, figure or agency name**; every citation lives in the
  `foot:`, never in the photograph.
- **No readable brand marks** anywhere — s19's cart, s25's pump display and s62's factsheet are
  all specified brand-free and out of focus on the figures.
- **The densest scenes get the calmest backgrounds.** The seven `art-forward` frames (s16, s18,
  s30, s49, s75, s76, s77) and the five chip cascades (s2, s6, s26, s45, s64) are all routed to
  near-flat, low-key subjects. Density is managed by choosing a quieter image, **never** by
  dropping one.
- **The contact sheet cannot be trusted** — read every promoted file at full resolution, and
  **md5 the asset ledger: no image may repeat across videos or channels.**

### Resolution routing

`blockframe-9` is full-bleed at `inset:-8%` ⇒ ~**1.63×** on the long edge, and the Pixabay key
tops out at 1280px. Route to **Pexels `large2x` (1880px)**: **s41** (PEAK 1, and `s42` is
cropped from it), **s55** (the `.mega`), **s59** (PEAK 2), **s76** (the source of the s75 crop),
**s77** (the overrun), **s10** (the source of the s10b crop), **s3** (the source of the s4 crop),
**s67** (the source of the s67b crop) and **s81** (the CTA — the last frame anyone looks at).
**Every derived crop's source must be Pexels**, because a crop of a 1280px file is drawn at ~2×.
Pixabay is fine everywhere else: under the grade plus 5% grain it reads as soft focus.

Write `.src` prompts and `CREDITS.txt` for every file — the archive rule depends on it.

### Concrete things the VO names that deliberately get NO cut-in

So the audit does not rediscover them: 1.2's alarm, call and debt reminder (all three are type;
the clock is the bg) · 1.6's groceries, gas and rent (all three are *in* the s6 bg, which is why
the chips can be type) · 3.3's four slips (same, in the s26 bg) · 3.5's landlord-or-bank (the
second half of the line; a cut-in at f ≈ 0.8 would leave a 1.2s second framing, under the floor)
· 4.11's "June nineteen thirty-two" (a tighter crop would make archival text legible, which is
the fabricated-document risk) · 6.11's alarm, call and buzz (the callback is one held image on
purpose, and cutting back to ch1's frames would be the reuse failure).

---

## 11. The ground temperature arc

`.field` carries a per-scene `--f1` two-stop ground at 38% (`.has-photo .field`). **Role scenes
deepen into their role colour; scenes with no role move only on the neutral warm↔cool axis**, so
no frame asserts a colour it has not earned. Values are in §7. **Push it harder than looks
right** — at document scale the arc reads almost flat and in the encode it is exactly right.

The ladder used:

```
warm     #2d2214 (warmest)  #291f13  #241d15  #1f1e1c        pop-warm  #33200f
neutral  #1c2027  #1a1e24  #191f28  #101720 (cool-dark)
cool     #161f2b  #131f2c  #0e1c2e  #0c1a2c (coldest)
fund     #0f2a1a → #12351f → #0f3a20 (deepest, once)
target   #2a2113 → #2e2411 → #372a0c (deepest, once)
warn     #2b1418 → #301519 → #38151a → #3b1219 (hottest, once)
```

**Two rules that are not columns:**

1. **A hold pair shares ONE ground** (s3/s4, s41/s42, s75/s76). A temperature step in the middle
   of a continuous zoom is visible and reads as a cut that is not happening.
2. **The deepest value of each role is spent exactly once** — `#0f3a20` on s41 (PEAK 1),
   `#3b1219` on s61 (the gap), `#372a0c` on s16 (the finding), `#0c1a2c` on s59 (PEAK 2).

Read as a curve, not a stripe:

**ch1** cool first light → warming through the deposit (`#241d15`, held across the buzz) →
sobering to neutral at the index card → warmest at the three bills → **the first red at 1.7**,
the question that opens the loop → neutral-warm as the method is named. **ch2** amber staged
evidence, cooling on the neutral paper frames (s12, s14) → **`#372a0c` at s16, the deepest amber
in the video, where the finding lands** → green from the method (s18) through the first corpus
(s21/s22) and easing at the chapter close. **ch3** rungs alternate amber numerator → green
corpus, warm domestic at "say it slowly", then the fine print runs red for six scenes and the
chapter **ends empty and cold at s39 `#101720`**, one word on screen, straight into the shove.

**ch4 carries the hottest green.** s41/s42 `#0f3a20` — the only use of it, and it is the hero.
Then straight into red: `#2b1418` as the warning opens, `#38151a` at the wide-open tap, pulling
back to `#301519` where the papers answer it, calmest red on the definitional 4.9, and
`#38151a` again at 1932 and at the chapter's closing verdict.

**ch5 carries both extremes and the one declared exception.**

> ⚠ **s57, s58 and s59 are `--warn` scenes running deep COOL grounds** (`#131f2c` → `#0e1c2e` →
> `#0c1a2c`). This is the only place in the cut where the ground contradicts the role, and it is
> **declared so a later pass cannot "fix" it**: cold is neutral, so it asserts nothing, and this
> is the video's drop — the rate changes and the number quadruples. *The drop is a temperature
> event before it is a number.* Precedent: japanese-money-methods ch2 s16, the coldest frame in
> that cut, on an amber-role scene.

After the drop the chapter snaps back to amber at s60 and **hits `#3b1219` at s61 — the hottest
frame in the video**, where the same paycheck is priced at roughly four times. Then amber routes,
green at rung five, and a last red on the whole month bought from dividends alone.

**ch6 climbs home.** Red at "not a settled number" → amber for the three answers → `#38151a` at
the thesis said out loud → green warming rung by rung as the ladder assembles (`#0f2a1a` →
`#12351f`, held across the hold) → the last hot red at the dividends-only price → neutral for
"every one of those is a division" → **s79 `#2d2214`, the warmest frame in the video**, the
morning returning → green for the hours bought back → `#33200f`, the only pop-leaning ground, on
the CTA.

**No ground cross-fade is implemented.** We cross-dissolve whole sections for 0.45s, which
blends both grounds already; adding the Claude Design animatic's ground melt double-fades.

---

## 12. Transitions and timing

`dissolve` (0.45s) is the default on every boundary. **Two** boundaries are `shove`, and they
are the only two real turns in the argument:

- **s39 → s40 (3.16 → 4.1)** at **248.539s (47.1%)** — out of the papers' fine print and into
  the number the viewer came for. 3.16 is one sentence that exists to cue a cut, and the frame
  before it is deliberately empty and cold.
- **s58 → s59 (5.6 → 5.7)** at **373.923s (70.8%)** — *"watch what happens to the number"* is a
  cut, spoken. This is the reward beat; a dissolve would smuggle the title's own answer in as a
  continuation instead of announcing it.

**Three matched-frame holds** (§6b) — mechanically dissolves; what makes them holds is that each
pair is one photograph under one continuous zoom, with no `transition` SFX at the joint.

```
scene_duration = 0.25 (VO lead-in) + clip_duration + 0.55 (tail)   ← MEDIUM override
data-duration  = scene_duration + 0.45   (s1–s80; s81 bare)
audio_start    = scene_start + 0.25
root duration  = 527.873
```

`0.25 / 0.55` are `format.json tiers.medium`, **not** the `scene.*` 0.4 / 1.0 SHORT defaults.
Generated from `timing.json` — **never hand-edited.** The same numbers live in four places (the
`<section>`, the JS `S` map, the `<audio>` row, root `data-duration`); updating three of four
passes every check and ships a video whose animations fire against the old timeline. Per-scene
figures are the `start` / `dur` / `d-dur` columns of §7 and are not restated — one home per fact.

**Chapter membership** (from the VO line id, `vo-<chapter>-<line>` — never a second map):
**ch1 s1–s8 · ch2 s9–s23 · ch3 s24–s39 · ch4 s40–s52 · ch5 s53–s68 · ch6 s69–s81.**

> **The failure mode to watch for at build.** Durations that sum to exactly 527.873 while every
> internal cut has drifted is what a re-timing produces. `tools/chapter_project.py` asserts
> **GAPS, not totals**, and `tools/cut_assemble.py` verifies every scene's `data-start`,
> `data-duration`, `data-track-index` and framings **individually**. Neither may be weakened.
> **A layout pass may not touch a duration. This file re-times nothing.**

---

## 13. `-en` divergence list

`storyboard-hi.md` **was read** (attempt 1's was not — it was being written in parallel). What
is ported, and what deliberately is not:

**PORTED, on purpose** — this is what makes a fix travel between cuts:

| ported | from |
|---|---|
| the element-ID scheme `s<n>-<part>` and every part name | hi §3 |
| the `#sN-rate` mechanism (two forms, +1.10 before the number) **and its build assert** | hi §4 |
| the three cue variants and the anchored/fixed split | hi §5 |
| the deterministic focal size rule (112 / 88 / 76) | hi §3 |
| the derived-crop continuous zoom as the answer to a `max_scene_seconds` breach | hi §6 |
| the archetype / ground / art discipline, and "one role colour per scene" | hi §7, §10 |
| the derived cue list and the `cues-tables.json` contract | hi §2 |

**DIVERGENT, with a reason each:**

| # | diverges how | why |
|---|---|---|
| **D0** | **The chapter map cannot align.** hi runs `1.1 … 7.8` — 78 lines, 7 chapters. This cut runs `1.1 … 6.13` — **81 lines, 6 chapters**. Indices diverge from **s8** onward and never re-converge | A US rewrite with a different argument shape has a different chapter count. Deriving this map from the hi row would mis-cut four chapters — the japanese-money-methods lesson verbatim |
| **D1** | **New part names: `-meas`, `-mlab`, `-mf`, `-band`, `-plate`** | the corpus measure-ladder (§9a) does not exist in the hi cut. **Back-port candidate** if the hi restyle adopts a climb device; its five rungs would need their own scale |
| **D2** | US institutions and vehicles only — BLS, S&P 500, Bengen, Trinity, Morningstar, Pfau. No ₹, lakh, crore, SIP, SWP, PPF, POMIS, SCSS, post office, Indian passbook: not in a string, not in a photograph | `market_rewrite_not_translation` + script guardrail #1 |
| **D3** | **"Dividends" is BANNED in the hi cut and is this cut's title, its whole chapter 5 and its reward beat. s53–s64 and s77 have no hi analogue at all** | `hi_currency_framing` vs the en packaging promise. The hi cut answers "financial freedom"; this one answers "live off dividends" |
| **D4** | **Not one anchored fraction is ported.** Every `f` in §5 is a Brian word position at ~17.31 c/s | Amrut delivers at ~13.03 c/s and the figures land in different clause positions. Porting a fraction would put a number on screen before or after its own word |
| **D5** | The corpus token list and the whole of §4 | hi asserts on ₹ tokens across 20 scenes at 3.0% / 7.4%; this cut asserts on 8 `$` tokens across 14 scenes at 4.0% / 3.11% / 1.08%. **No frame may imply a conversion** |
| **D6** | The cut's one `.mega` is **`ABOUT 1%`** (s55), a US index yield | the hi cut cannot carry an index dividend yield at all (D3), so its one enormous number is necessarily something else |
| **D7** | Shoves at **s39→s40** and **s58→s59** | both are turns in *this* argument. hi's are s37→s38 and s54→s55 — a seven-chapter cut has its hinges elsewhere by construction |
| **D8** | **Three holds here, one in hi** (s3/s4, s41/s42, s75/s76 vs hi's s13/s14) | the style-E en script declares three continuous-zoom pairs in its own per-line cues; the hi cut's single hold exists to solve a breach. Same mechanism, different count |
| **D9** | **The tank is a four-frame photographic spine** (s10, s46, s47, s57) | style E makes the tank load-bearing in both scripts, but `storyboard-hi.md` is the **style-A** storyboard and has no tank at all. **When the hi cut is re-storyboarded, this is the first thing to port back** |
| **D10** | **7 drawn layers, 1 Lottie, 0 icons** vs hi's 5 drawn, 1 Lottie, 2 icon scenes, 1 `.stamp` | the arguments differ. This cut has **no `.stamp` component**: five lines are verdicts, and five rotated pills would be a tic — the verdicts are `pop` entries on the `stmt`, which is what makes the `stamp` SFX legal without new copy |
| **D11** | **Eight photo overrides** against the script's own `img:` cues (§10) | four are the never-a-screen rule, two the grade/material rule, one a depictive cue, one a duplicate-subject clash. The hi cut must apply the same rules against **its own** cues; this list is not copyable |
| **D12** | Music bed **`bed-tension`** | chosen for *this* cut's argument (a cost). The hi cut's is `bed-resolve` because its thesis is a habit. The bed is per video, not per channel |
| **D13** | 1930s **US** archival frames (s50, s51) from Commons / LoC | the hi cut has no archival beat; and a Depression photo from another market is the euro-coin defect class |

---

## 14. Open items

1. **None that block a build.** The 2.2 breach is *resolved* here (§6a), not deferred: a real
   derived crop plus one continuous zoom, with both framings declared and summing to 10.596.
2. **Bed length is NOT an open item** (§2). Recorded because both storyboards on
   japanese-money-methods raised it as a decision on 2026-08-01 and it never was one.
3. **The SFX count is derived, not budgeted** (§2). If a reviewer expects ≤10 cues, that is the
   SHORT-cut figure; the creator retired it for chapter cuts on 2026-08-06.
4. **s75 / s76 need one photograph containing five crates of increasing size**, wide enough to
   crop tight on the smaller three. If stock cannot supply it, the fallback is
   `wooden crates of different sizes in a line on a concrete warehouse floor` and the pair
   becomes tight-to-wide on whatever count the file has — **the drawn bars carry the count
   regardless**, which is why the art is `fwd` on both.
5. **The four tank frames are the one sourcing risk in the cut** (§10). Brief the fallback with
   the fetch, not after it: the hi cut's ch1 lost three rounds to a window it could not buy, and
   the lesson recorded in `run.json.chapters._carry_forward_from_ch1_assets` is that a later
   brief must **adjust rather than assume**.
6. **Curly quotes are unverified against the 97-codepoint subset** (§3). Dump `subset.txt` at
   build; if `“ ”` are absent, s34 and s37 fall back to straight quotes. A missing glyph renders
   as tofu and no check catches it.

## Sign-off

- [x] Colour semantics table filled and consistent with every `colour:` cue in the script
- [x] `arch` / `ground` / `art` assigned on all 81 scenes (§7) — no blanks
- [x] `has-photo` + a real `.bg` on all 81 scenes; `photo_free_scene_ratio` = 0
- [x] No rail, no chapter title, no scene counter, no slide number anywhere on screen
- [x] Every `start` / `dur` verbatim from `timing.json`; nothing re-timed
- [x] All fourteen corpus frames carry `#sN-rate` in the same frame (§4), asserted at build
- [x] The 2.2 10.596s single-photograph breach resolved with a derived crop + one continuous zoom
- [x] Two shoves, both on real turns; three holds, none carrying a `transition` SFX
- [ ] No image hash reused from any prior video on either channel — **fin-assets to verify**
- [ ] Creator approved (Gate ②) — date: __
