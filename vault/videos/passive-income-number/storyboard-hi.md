---
summary: Storyboard for «वो नंबर, जो हर महीने पैसे देता है» hi cut — MEDIUM tier, 81 scenes (one VO line = one clip = one scene), blockframe-9 + the chapter archetype layer. FULL REBUILD for the style-E restyle and the measured 519.331s Amrut audio; attempt 1 (style A, Harsh, 78 lines) is superseded in its entirety. Declares the colour semantics, the archetype row (arch / ground / art / centred) on all 81 scenes, the DOM with the standing `sN-rate` element on 30 frames, four cue ladders on measured timing.json offsets, 2 shoves + 5 continuous-zoom holds, four two-framing scenes resolving every max_scene_seconds breach, one music bed with a derived cue list, 2 drawn proportions / 1 icon row / 1 Lottie, and 87 image slots of which 12 are REUSED verbatim from the superseded build.
updated: 2026-08-08
source: script-hi.md (fin-script hi attempt 3, STYLE E, 81 lines, 7 chapters, 6,425 chars, fin-audit PASS) + studio/videos/passive-income-number-hi/assets/voice/timing.json (MEASURED, 519.331s, 81 lines, Amrut) + run.json constraints / chapters / carry-forwards + storyboard-en.md (the finished sibling — structural model, section 7 archetype table, the `#sN-rate` treatment) + storyboard-hi.md attempt 1 (element IDs and the ground ladder only) + studio/videos/passive-income-number-hi-ch{1,2}/ (the 20 verified photographs and the built ch1 icon row) + knowledge/design-finance-blockframe.md + knowledge/design-chapter-archetypes.md + knowledge/stock-photo-sourcing.md + tools/format.json + tools/audio/kit.json + tools/audio/cues.py
stage: fin-storyboard, cut hi, attempt 2 — FULL REBUILD
---

# STORYBOARD — «वो नंबर, जो हर महीने पैसे देता है» · **hi** cut

**Project:** `studio/videos/passive-income-number-hi/` · **Script:** `script-hi.md`
**Design:** [[../../knowledge/design-finance-blockframe]] — the **dark** system, unmodified,
extended by [[../../knowledge/design-chapter-archetypes]]. Do **not** use
`design-techtooltester` (bright, non-finance).
**Channel:** @cashguruguides ₹ · **Tier:** MEDIUM, per-line chapters (**7 chapters, 81 lines**)
**Architecture:** **`blockframe-9`** (`run.json.architecture` = `format.json architecture_lock`).
`body_class` is `""` — no `.rail`, no `.swiss-band`, no panel. Centred stack over a full-bleed
graded photograph, every scene, with the archetype layer deciding where the drawn layer lives.
**Runtime:** **519.331s (8:39.331)** — `timing.json` is the only home for every duration.
**VO:** Amrut Deshmukh `LHJy3mhZWsvhUjy0zUM1` · **Scenes:** 81 · **Image slots:** 87
(81 bg + 4 second framings + 2 cut-ins), **87 files** — 67 fetched, 8 derived crops,
**12 reused verbatim from the superseded style-A build** (§10).

> **What this file is accountable for.**
> 1. Every scene carries `arch` / `ground` / `art` — §7, three real columns, no blanks.
> 2. Every scene carries `has-photo` and a real `.bg` — §10, `photo_free_scene_ratio` = 0.
> 3. **No rail, no chapter title, no scene counter, no slide number** — §3.
> 4. Every duration is `timing.json` verbatim — §7 / §12. Nothing here re-times a scene.
> 5. **The four measured `max_scene_seconds` breaches each carry two `data-framings`** — §6.
> 6. Every corpus **and every derived-income** figure shares a frame with its rate, as a real
>    `#sN-rate` element — §4, **thirty frames**, asserted at build.

---

## 1. Colour semantics for THIS video (derived from the thesis — mandatory)

The thesis: *the monthly number is a division, not a forecast — a corpus times a chosen
withdrawal rate, over twelve. The rate is the whole argument: hold it at three percent and the
ladder is honest; import four percent and the same ₹25,000 a month costs a quarter less than it
should; pull ten or twelve and the tank empties.*

Roles are fixed; meanings are per-video. **This table is derived from the script's own
`colour:` cues, line by line. The cue is authoritative; this is the index.**

| Token | This video means | Because |
|---|---|---|
| `--fund` green `#22c55e` | **the corpus doing its stated job at the stated rate** — every monthly figure that lands (2.10, 3.3, 4.3, 6.2, 6.7), the full year paid without touching the salary (2.12), the meeting with the sourced wage (6.10), and where the ladder actually started (7.6) | green marks **a division that came out at a rate the frame is showing**. Never "safe", never "recommended" — the persona rule forbids a pick, so green cannot mean approval |
| `--warn` red `#ef4444` | **the thing that eats the corpus** — the too-high withdrawal rate (5.2, 5.4, 5.5, 5.6), the imported rule and what it excluded (5.12, 5.14, 6.12, 6.13), the failure edge (5.16), the honesty beat about whose money it is (4.7), and the internet inflating a slow fact (3.8) | red is **depletion and importation**, never a verdict on SWP itself. 4.7 is red because the money comes out of your own tank — that is a cost, not a criticism |
| `--target` amber `#f59e0b` | **a rate under examination** — the tank and its two taps (2.3, 2.4), the working number declared and defended (2.6, 2.7), the rate held across a rung (3.6, 4.10), why the outgoing tap is small (4.8), the government's published rate and its roof (5.8, 5.10), India's own research (5.15), the inflation that explains it (5.17), the hero corpus (6.5) and both assumed growth rates (6.15, 6.16) | amber is the thing being **weighed**. Every price-evidence beat is amber precisely because the persona rule forbids a pick — an amber number is being measured, not offered |
| `--pop` orange `#ff5c39` | the call to action | fixed — **exactly once**, s81 (7.8), as the `.cta` block's fill. Zero mid-roll CTA |

**The inversion trap — five prior systems, none of them applies here.** `needs-vs-wants` ran
amber = "wants" and reserved red for the leak alone; `first-lakh-first-thousand` ran red = "the
stretch nobody helps you with"; `japanese-money-methods` ran red = falsity-and-drain, green =
the viewer's own hand; **this run's own en cut** runs green = a division that closed, red = what
an assumption costs, amber = a published figure under examination. **Here green is the corpus
doing its job at the stated rate, red is depletion and importation, amber is a rate under
examination.** Do not carry any of the other four in.

**Thesis check** (the audit's, restated so it can be run): green never lands on a figure whose
rate is not in the frame · **red never lands on India's 3.0%** · **amber never lands on the
imported 4%** · red never lands on SWP as a mechanism.

**Role counts across 81 scenes:** amber 14 · red 11 · green 8 · orange 1 · **no role at all
47**. Forty-seven colourless frames is correct and deliberate — colour is a signifier here, not
decoration, and this cut's argument is carried by arithmetic that is simply true.

### 1a. Per-scene `--tint` — derived from the role, never chosen

One rule, 81 applications, so it cannot drift. Not a column.

| scene's role | `--tint` | alpha |
|---|---|---|
| `--fund` | green | `.10` (green reads hotter) |
| `--warn` | red | `.12` |
| `--target` | amber | `.12` |
| `--pop` (s81 only) | orange | `.13` |
| **no role (47 scenes)** | **none** — `--tint` unset, scrim layer 1 renders `transparent` | — |

Design doc §2 caps tint at 0.10–0.13; above ~0.15 it stops reading as light and becomes a
colour wash.

### 1b. ⚠ Two frames where the tint must be aimed, not just set

Carried from `run.json.chapters._carry_forward_to_storyboard_hi` (fin-audit-hi attempt 2). Both
frames print India's **3.0% as the COMPARATOR**, so a `--warn` colour applied to the whole
string argues against the video's own thesis.

| scene | line | string on screen | red lands on | stays `--muted` |
|---|---|---|---|---|
| **s42** | 5.2 | `10% OR 12% WITHDRAWAL INSTEAD OF 3.0%` | `#s42-rate` span wrapping **`10% OR 12%`**, `.warnc` | the `3.0%` token — plain `--muted`, no role class |
| **s70** | 6.13 | `₹75,00,000 AT 4% vs ₹1,00,00,000 AT 3.0% — a quarter smaller` | `#s70-rate` span wrapping **`4%`**, `.warnc` | `#s70-rate2` wrapping `3.0%` — `--muted`, no role class |

**Mechanically:** neither scene may take a role class on the whole `.huge`. The focal is
`--ink`; only the declared span carries `.warnc`. A build that colours the parent element and
leaves the spans bare renders red across the 3.0% and passes every check.

---

## 2. Audio — one bed, a derived cue list

**Music bed: `bed-resolve`.** This cut's argument is a **habit and a ladder** — five rungs, each
one paying a real bill, and a closing rule («हर रक़म अपनी दर के साथ»). The trap is one chapter of
seven, not the thesis. `bed-tension` would argue against the promise the title makes.
**Deliberately different from the en cut's `bed-tension`** (`storyboard-en.md` D12): the bed is
chosen per video's argument, and the two cuts do not make the same argument.

> **Bed length is not a decision and is not flagged here.** `tools/audio/mix.py` feeds the ~248s
> bed in `laps` times with a 3s `acrossfade` at each joint and trims to the master's duration.
> There is no dip at 248s or 496s. Both storyboards on `japanese-money-methods` escalated this as
> an open decision on 2026-08-01; it never was one. **This cut is 519.331s — do not raise it.**

### The cue list is DERIVED per chapter, not hand-typed

`tools/audio/cues.py studio/videos/passive-income-number-hi-ch<N> --write` emits one cue per
**real motion call**, at that call's own time, bound through `kit.json`'s helper column.

**On the ≤10-cue budget in the storyboard contract:** that is a **SHORT-cut** figure. Creator
decision **2026-08-06** retired the hand-authored ceiling for chapter cuts, because a 24-cue list
over nine minutes carries one `transition` and every scene change then reads as silent — which
was the defect the creator actually reported. Expect ~130 cues over 8:39 (one per ~4.0s).
Discipline lives in what each cue is **bound to** and in the dry list below, not in how few there
are. The ≥0.8s minimum spacing still holds and `cues.py` enforces it.

**What this storyboard owns, because the generator cannot derive it.** `cues.py` reads this from
`studio/videos/passive-income-number-hi/assets/cues-tables.json` — **fin-build writes that file
verbatim from this block.** An absent table means *no special cases*, never someone else's.

```json
{
  "holds":   [["s14","s15"], ["s17","s18"], ["s23","s24"], ["s32","s33"], ["s63","s64"]],
  "buzz":    {"s4": 3.48},
  "counted": ["s6"],
  "dry":     ["s1","s2","s3","s5","s7",
              "s10","s11","s12","s13","s17","s18","s21",
              "s23","s24","s26","s30",
              "s32","s33","s35","s36","s39",
              "s41","s43","s44","s45","s47","s48","s49","s50","s51","s52","s53","s54","s55",
              "s59","s61","s63","s65","s66","s71",
              "s74","s75","s76","s77","s78","s79","s80"]
}
```

| input | value here | why |
|---|---|---|
| `holds` | five pairs (§6b) | each is one photograph under one continuous zoom. A whoosh at the joint announces a change that is not happening |
| `buzz` | `s4` at **+3.48** | the kit's only diegetic sound, legal **only** because the frame shows the phone making the noise and the Lottie banner is already lighting (§8). Anchored on «बजता है». Nowhere else in the cut. **`dry` does not kill it** — `cues.py` silences derived cues only |
| `counted` | `s6` | the one cascade where the **count is the point** — three bills, three ticks. The generator's counted branch is hardcoded to `n = 3` and s6 has exactly three cells. **s2's three chips are deliberately NOT counted**: that cascade enumerates *absence*, and clicking it turns the cold open into a joke |
| `cta` | s81 only | the single `--pop` element of the video |
| `hero` | **s16 · s62 · s64** | the FIRST corpus (₹10,00,000), the hero corpus (₹1,00,00,000) and the payout the video is named for (₹25,000 a month). **No other rung rings.** If every rung gets a `hero` the ladder has no shape |
| `stamp` | **five scenes** — s8, s27, s46, s56, s70 | their focal enters with **`pop`** (`back.out(1.7)`) instead of `rise`. That IS the verdict slam. **Only s46 carries an actual `.stamp` pill** (§3); five rotated pills would be a tic, and the `pop` entry is what makes the sound legal without new copy |

**Declared DRY beats — silence is the choice, not an omission** (all still take their joint
`transition`):

- **The whole cold open, s1–s3, s5, s7.** The what-if is paid in recognition, not punctuation.
  s4's buzz, s6's three ticks and s8's stamp are the only sounds in chapter 1.
- **The mechanism and the tank, s10–s13.** Teaching, not landings.
- **Every ÷12 and every carried-down page — s17, s18, s23, s24, s32, s33, s59, s63.** These are
  measurements, and the continuous zoom is already the event.
- **s21, s26, s30, s36 — the domestic and pacing beats.** «यह छोटा है, यह मानिए» does not want a hit.
- **s44 and s45, the tank draining and then empty.** Silence is the point of the frame.
- **s48 and s50, the post-office rate and its roof.** A bass hit on a published sovereign rate
  recommends it, whatever the foot says.
- **s52–s55, the provenance run.** The chapter's power is provenance; it is paid at s56's stamp.
- **s65 and s66, the comparison and the PLFS figure.** A `hero` on an average wage statistic is
  grotesque. The payoff is s67.
- **s74–s80, the whole callback.** Nothing sounds between s70's stamp and s81's `cta`, so the
  return to the day lands in a cleared room.

**Mixed in post, never in the composition.** `assets/audio.json` → `tools/audio/mix.py`
(sidechain duck) → `tools/loudnorm.py` to −14 LUFS. The composition stays voice-only: one
`<audio>` row per line, track index 10. No music or SFX `<audio>` rows in `index.html`.
**Verify from the encoded file, never from the mix log** (`tools/audio/verify_cues.py`).

---

## 3. The frame — DOM, and the standing `sN-rate` element

`<div id="root" class="cut-hi">`. **No body class.** `cut-hi` is load-bearing: it is the whole
@cashguruguides watermark, painted on `#root::after` above every scene, and `check build` fails
without it. Stage 1920 × 1080, `.scene` padding `110px 150px` ⇒ content box **1620 × 860**,
centred, `isolation: isolate` (without it the outgoing scene's type paints over the incoming one
for the whole 0.45s dissolve, at all 80 boundaries).

**NO RAIL. NO CHAPTER TITLE. NO SCENE COUNTER. NO SLIDE NUMBER.** `format.json
chapter_design.rail` is `false`; the top rail was built and removed at creator request
2026-08-05. **The viewer must never be shown that this video is chapter-based, slide-numbered or
counted.** Chapters exist for production (build → `fin-editor` → `fin-ceo`, one at a time) and
for the YouTube chapter list — nowhere on screen. This also forbids a "RUNG 3 OF 5" label
anywhere: a rung count is a counter.

```html
<section class="scene clip arch-b has-photo centred art-off" id="s16"
         data-track-index="2" data-start="87.207" data-duration="5.795"
         data-framings="5.345" style="--tint:rgba(245,158,11,.12)">
  <div class="field" id="s16-field" style="--f1:#241d15"><div class="rules"></div></div>
  <div class="bg"    id="s16-bg" style="background-image:url(assets/img/s16.jpg)"></div>
  <div class="scrim" id="s16-scrim"></div>       <!-- --tint only when the scene has a role -->
  <div class="stack" id="s16-stack">
    <p class="kicker" id="s16-kick">RUNG ONE</p>
    <p class="sub"    id="s16-rate">AT A 3.0% WITHDRAWAL RATE</p>
    <p class="huge"   id="s16-num">₹10,00,000</p>
    <p class="foot"   id="s16-foot">ILLUSTRATIVE · corpus times 3.0% divided by 12 — arithmetic, not a forecast</p>
  </div>
  <div class="grain"></div>
</section>
```

**ID scheme: `s<n>-<part>`, n = 1…81 in script order** — `field`, `bg`, `bg2`, `scrim`, `stack`,
`kick`, `stmt` **or** `num`, **`rate`**, `rate2`, `sub`, `foot`, `band`, `plate`, `art`, `stage`,
`ticks`, `stamp`, `cta`. **Ported unchanged from attempt 1 §3 and from the built ch1/ch2
projects, so a fix travels between cuts and between chapters** (§13). **Five part names are
load-bearing for the SOUND generator** and may not be renamed: `-cta`, `-stmt`, `-num`, `-mf`,
`-band` (`tools/audio/cues.py` matches on them literally). **`-meas` / `-mlab` / `-mf` do not
appear in this cut** — see §13 D1.

**Copy is NOT restated here.** `bar:` / `stmt:` / `num:` / `foot:` strings live in each line's
`[arch …]` cue block in `script-hi.md` and have exactly one home. This storyboard owns the DOM,
the archetype row, the cues, the transitions, the audio, the drawn art and the images.

### 3a. Strings that must NOT go on screen

Three `foot:` entries in the script are **production annotations, not viewer copy**. Putting
them up would print the chapter structure on screen, which the no-rail rule forbids outright.
The built ch1 already dropped one; this file rules on all three.

| scene | line | the annotation | ruling |
|---|---|---|---|
| s5 | 1.5 | *"The number is withheld until Chapter 6 — this is the open loop…"* | **DROP.** Already dropped in the built ch1 |
| s61 | 6.4 | *"The open loop from Chapter 1 closes here — NO figure on this frame…"* | **DROP.** Same reason. s61 renders kicker + stmt only |
| s39 | 4.9 | *"NO RATE STATED ON PURPOSE — facts-staging B.2's LTCG row is SOFT…"* | **DROP.** It is a sourcing note. s39 renders kicker + stmt only, and carries **zero tax figures** as the script requires |

### 3b. Font-subset guard — hard, and it has bitten this project

**No `/` and no `?` in any on-screen string in this cut.** The 97-codepoint FinanceSans subset
carries `₹ · → ▶ × ≈` but **not the solidus**, and a missing glyph renders as tofu with every
check passing.

- Every `num: ₹X / MONTH` in the script renders as **`₹X A MONTH`** — s50, s59, s64, s72, s73.
- 5.2's cue already says *no question mark on screen*; the `stmt:` renders declaratively.
- `→` and `▶` are **drawn in CSS**, never typed. `⚠` and `⟵` in this file are storyboard
  notation and never composition text.
- **Dump `subset.txt` at build and check every string against it before the render.**

**The banned word.** `hi_currency_framing` forbids the English payout word and every Devanagari
transliteration in script, on-screen text, title and tags. **It appears in no string in this
file and must appear in none in `index.html`.** Grep the built composition for it before the
build gate.

### The three type registers

| Script field | Class here | Size | Colour |
|---|---|---|---|
| `bar:` | **`.kicker`** `#sN-kick` | 30 / 800, tracked 4, uppercase | `--muted` |
| `stmt:` | **`.huge`** `#sN-stmt` | **112 / 88 / 76** by the rule below | `--ink`, or the scene's role class |
| `num:` | **`.huge`** `#sN-num` 112 (**`.mega` 240 on s14 only**) | tabular-nums, `Intl.NumberFormat("en-IN")` | the scene's role class |
| the rate qualifier | **`.sub`** `#sN-rate` | **40** | the scene's role class |
| a non-rate qualifier | **`.sub`** `#sN-sub` | **40** | `--muted` |
| `foot:` | **`.foot`** `#sN-foot` | 26 / 700 | `--muted` |

**Focal size rule — deterministic, keyed on the copy, so it cannot drift when a string changes.**
FinanceSans at weight 900 averages ≈0.58 em advance; usable width 1620px.

| `stmt:` length | `.huge` inline size | lines |
|---|---|---|
| ≤ 24 chars | **112px** | 1 |
| 25–48 chars | **88px** | 2 |
| 49–89 chars | **76px** | 3 |

**Never below 76.** The longest `stmt:` in the cut is 6.13's 63-char pair at 76px × 2 lines.
`₹1,00,00,000` at `.huge` 112 = 12 glyphs × 0.58 × 112 ≈ 780px, one line ✓. **`3.0%` at `.mega`
240 = 4 glyphs × 0.58 × 240 ≈ 557px**, comfortably inside the 1500px stack.

⚠ **`Intl.NumberFormat("en-IN")` is mandatory** for every animated figure. A plain
`\B(?=(\d{3})+(?!\d))` regex prints `10,000,000` instead of `1,00,00,000` and is wrong for India.

⚠ **Comma descenders.** ch2's shipped `₹10,00,000` struck a photographed foot through with its
comma descenders. This is COMMA-triggered and therefore recurs on **every lakh and crore rung** —
s16, s22, s31, s58, s62, s69, s70, s76, s79. Fixed system-side (the `.huge` shadow/leading), not
per scene.

**Chips exist on two scenes only** — **s2** (three chips) and **s6** (three icon tick cells,
which are a cascade, not chips). Every other qualifier is a `.sub` line, because **a chip crushes
a figure-plus-its-rate**. s2's three chips are `NO ALARM` (8) · `NO OFFICE CALL` (14) ·
`NO WORK REMINDER` (16) — all ≤22 chars, one declared row of three. `.row` has `flex-wrap: wrap`,
so four long chips silently orphan 3+1 and no checker flags it.

**Element budget.** Per scene: photograph (1) + kicker + focal + one or two of rate/sub/foot =
**4–5 countable**, against the ceiling of 6. The two `art-forward` frames run kicker + stmt +
rate + foot + `art` + `band` = **exactly 6**. `.field`, `.scrim` and `.grain` are grade layers,
not scene elements; `sN-bg2` is a cross-fade of the photograph layer, not a fifth element.
**Never `stmt` and `num` together** — where the script's cue block carries both (2.8, 3.1, 4.1,
5.10, 6.1, 6.5, 6.9), the `num:` is the focal and the `stmt:` becomes `#sN-rate` or `#sN-sub` at
40px. That is exactly how the built ch2 s15 already renders.

---

## 4. `#sN-rate` — the rate is a DOM element, not a footnote

`run.json.constraints.withdrawal_rate_on_screen`: *"Every corpus figure must carry its assumed
withdrawal/return rate ON SCREEN in the same frame as the number."* Extended 2026-08-07 by
`derived_income_carries_assumption` to **derived income** figures.

This storyboard's job is to make the frame **structurally incapable of losing it**, so the rate
is not a 26px `--muted` foot a density pass can drop — it is a **first-class `.sub` at 40px in
the scene's role colour, and it arrives at +1.10, BEFORE the corpus lands.** The assumption is
on screen first and the number arrives into it. That ordering is the constraint's strongest
reading and it costs nothing.

Two forms:

- **Its own qualifier line** → `#sN-rate` is a `.sub`, cue 2 at **+1.10 fixed** (`rise`).
- **Fused into one sentence** (the workings, the pairs, the recap) → `#sN-rate` is an inline
  `<span>` **inside the focal**, wrapping the rate token, carrying the role colour and taking a
  `pulse` at **+1.90 fixed**. No copy is reordered, nothing is printed twice, and there is a node
  to assert.

| # | scene | line | corpus / derived figure in frame | form | token |
|---|---|---|---|---|---|
| 1 | s16 | 2.8 | ₹10,00,000 | `.sub` | 3.0% |
| 2 | s17 | 2.9 | ₹10,00,000 · ₹30,000 | span | 3.0% |
| 3 | s18 | 2.10 | ₹2,500 | `.sub` fundc | 3.0% |
| 4 | s19 | 2.11 | ₹2,500 (kicker) | `.sub` | 3.0% |
| 5 | s22 | 3.1 | ₹20,00,000 | `.sub` | 3.0% |
| 6 | s23 | 3.2 | ₹20,00,000 · ₹60,000 | span | 3.0% |
| 7 | s24 | 3.3 | ₹5,000 | `.sub` fundc | 3.0% |
| 8 | s25 | 3.4 | ₹5,000 (kicker) | `.sub` | 3.0% |
| 9 | s28 | 3.7 | ₹10,00,000→₹20,00,000 · ₹2,500→₹5,000 | `.sub` — `BOTH AT A 3.0% WITHDRAWAL RATE` | 3.0% |
| 10 | s31 | 4.1 | ₹40,00,000 | `.sub` | 3.0% |
| 11 | s32 | 4.2 | ₹40,00,000 · ₹1,20,000 | span | 3.0% |
| 12 | s33 | 4.3 | ₹10,000 | `.sub` fundc | 3.0% |
| 13 | s34 | 4.4 | ₹10,000 (kicker) | `.sub` | 3.0% |
| 14 | s35 | 4.5 | — (the list) | `.sub` — `AT A 3.0% WITHDRAWAL RATE · ILLUSTRATIVE` | 3.0% |
| 15 | s40 | 4.10 | ₹10,00,000 · ₹20,00,000 · ₹40,00,000 | span on `ALL AT 3.0%` | 3.0% |
| 16 | s49 | 5.9 | ₹9,00,000 | span | 7.4% |
| 17 | s50 | 5.10 | ₹5,550 A MONTH · ₹9,00,000 | span | 7.4% |
| 18 | s58 | 6.1 | ₹50,00,000 | `.sub` | 3.0% |
| 19 | s59 | 6.2 | ₹12,500 A MONTH · ₹50,00,000 · ₹1,50,000 | span | 3.0% |
| 20 | s60 | 6.3 | ₹12,500 (kicker) | `.sub` | 3.0% |
| 21 | s62 | 6.5 | ₹1,00,00,000 | `.sub` targetc | 3.0% |
| 22 | s63 | 6.6 | ₹1,00,00,000 · ₹3,00,000 | span | 3.0% |
| 23 | s64 | 6.7 | ₹25,000 A MONTH | `.sub` fundc | 3.0% |
| 24 | **s65** | **6.8** | **none on screen — the VO speaks «पच्चीस हज़ार»** | **`.sub`** — `AT A 3.0% WITHDRAWAL RATE · ILLUSTRATIVE` | **3.0%** |
| 25 | s67 | 6.10 | ₹25,000 · ₹24,217 | span | 3.0% |
| 26 | s69 | 6.12 | ₹75,00,000 · ₹25,000 A MONTH | span | 4% |
| 27 | s70 | 6.13 | ₹75,00,000 · ₹1,00,00,000 | **two spans** (`-rate` 4% warnc · `-rate2` 3.0% muted) | 4% + 3.0% |
| 28 | s72 | 6.15 | ₹19,000 A MONTH | `.sub` targetc — `AT AN ASSUMED 7.1% GROWTH RATE` | 7.1% |
| 29 | s73 | 6.16 | ₹10,000 A MONTH | `.sub` targetc — `AT AN ASSUMED 12% GROWTH RATE` | 12% |
| 30 | s76 | 7.3 | ₹1,00,00,000 | span | 3.0% |
| 31 | s79 | 7.6 | ₹1,00,00,000 · ₹2,500 | span on `BOTH AT 3.0%` | 3.0% |

*(Thirty-one rows; §7's `#sN-rate` column carries the same set.)*

### ⚠ 4a. Row 24 is the run's known blind spot, closed here

`run.json.owed.derived_income_assert_is_frame_only`: the build's rate assert **scans on-screen
tokens**, so it is structurally incapable of seeing a VO line that speaks a derived figure over a
bare frame. **hi 6.8 was exactly that** and only fin-audit caught it.

**s65 therefore carries a real `.sub` `#s65-rate`, not a `.foot`.** It is the one frame in the
cut whose rate element exists for a figure that is spoken and never printed, and it must survive
any density pass. The frame still prints **no ₹ figure** — the payoff is s66/s67 — which is why
the marker is the rate plus `ILLUSTRATIVE` rather than the number.

**The build assert (mechanised).** Any scene whose rendered text contains a corpus or derived
token — `₹9,00,000` `₹10,00,000` `₹20,00,000` `₹40,00,000` `₹50,00,000` `₹75,00,000`
`₹1,00,00,000` `₹30,000` `₹60,000` `₹1,20,000` `₹1,50,000` `₹3,00,000` `₹2,500` `₹5,000`
`₹10,000` `₹12,500` `₹19,000` `₹25,000` `₹5,550` — **must contain an element with id `sN-rate`
whose text contains a rate token** (`3.0%`, `4%`, `7.4%`, `7.1%`, `12%`). Plus the one declared
VO-only row (s65).

**What the assert must NOT fire on, so it stays honest:**

- **s66 `₹24,217`** is a published PLFS statistic, not a figure derived from a corpus. Its
  citation lives in the `foot:`. Printing a withdrawal rate beside someone's wage would be a
  category error.
- **Nine frames carry a rate as their FOCAL** — s14 `3.0%`, s27 `3.0%`, s46 `12%`, s48
  `7.4% p.a.`, s52 `4%`, s55 `3.0% TO 3.5%`, s56 `3.75%`, s57 `5%`, and s42's rate pair. They
  carry **no separate `#sN-rate`**: printing a rate under itself reads as a defect.

---

## 5. The cue ladders — four variants

Offsets are **relative to `scene_start`** (§7 column `start`, verbatim from `timing.json`), so
every absolute cue time is `scene_start + offset` and is derived, never hand-typed.
`audio_start = scene_start + 0.25` (MEDIUM `lead_in_seconds`).

| variant | scenes | cue 1 | cue 2 | cue 3 | cue 4 |
|---|---|---|---|---|---|
| **A — statement** (default) | **56** | `sN-kick` **+0.30** fixed `rise` y24 | `sN-stmt` **+1.10** fixed `rise` y40 — **`pop` on the five verdict scenes** (§2) | `sN-rate` span **+1.90** fixed `pulse`, *or* `sN-sub`/`sN-foot` **+1.90** fixed `fade` | `sN-foot` **+2.70** fixed `fade` (only when cue 3 was the rate/sub) |
| **B — figure** | **22** | `sN-kick` **+0.30** fixed `rise` | `sN-rate`/`sN-sub`, else `sN-foot`, **+1.10** fixed `rise` | `sN-num` **anchored, floor +1.90**, `countUp` + `pop` | `sN-foot` = **num + 0.80** fixed `fade` (only if the foot did not take cue 2) |
| **C — cascade** | **2** (s2, s6) | `sN-kick` **+0.30** fixed `rise` | *the items ARE the statement* — **+1.10 / +1.70 / +2.30**, `popEach`, **fixed 0.6s** | s6 only: the three tick marks trail each cell by **+0.35**, `pulse` | `sN-foot` = last item + 0.80 fixed `fade` |
| **D — close** | **1** (s81) | `s81-cta` **+0.40** fixed `pop` | `s81-foot` **+1.20** fixed `fade` | — | — |
| — | all 81 | `sN-bg` **+0.00 → scene end** anchored `ken` 1.0 ↔ 1.16 | | | |
| — | 4 scenes | `sN-bg2` anchored `fade` — a 0.40s cross-dissolve of the photograph layer at the declared framing boundary (§6a) | | | |

**Three declared per-scene exceptions:**

1. **s14 (2.6), the `.mega`.** `3.0%` is anchored at **+4.24** on a 6.416s scene (the rate is the
   last clause of the line), so the foot cannot follow it. Order: `s14-kick` +0.30 ·
   `s14-foot` +1.10 · `s14-num` anchored **+4.24**. Gaps 0.80 / 3.14 ✓.
2. **s41 (5.1) carries a kicker and no statement at all** (`stmt: —`) — one element, at +0.30. It
   is the emptiest frame in the cut and that is the beat: chapter 5 opens on a held breath.
3. **s81 (7.8) has no kicker** (`bar: —`). The `.cta` block therefore takes +0.40 so something
   authored is on screen inside `first_cue_by_seconds` 0.5, not only the photograph.

**Every gap is ≥0.8s.** A: 0.30→1.10→1.90→2.70 = 0.80 throughout ✓ · B: 0.30→1.10 = 0.80 and the
floor puts the num at ≥1.90 ⇒ ≥0.80, foot at num+0.80 ✓ · C: a **declared cascade**,
`layout.cascade` gap 0.6s, ≤5 items ✓ (s6's tick marks are the same cue's second half, not new
cues) · D: 0.40→1.20 = 0.80 ✓. `first_cue_by_seconds` 0.5: the photograph is up at +0.00 and the
first authored element at +0.30 (+0.40 on s81) ✓.

**Anchored vs fixed.** The kicker, the stmt, the rate/sub, the foot, every cascade item and the
CTA are **fixed** — constant regardless of clip length. The `ken` push, every `num` arrival, every
`bg2` framing swap, the s4 Lottie and both drawn-art beats are **anchored**: they land on a word
and scale with the clip. **Surplus time from a longer clip goes into the hold after the assembly
— never into a cascade.** Concretely: variant A finishes at +2.70 at the latest, so s21 (8.506s)
and s39 (8.402s) hold a finished frame for ~5.5s with only the ken push running. That is the
answer to the two near-cap scenes in §6c.

**Anchored cue resolution.** `f` is a **fallback**: `f` = the character position of the figure's
first spoken word ÷ the line's character count, and fin-build resolves each against
**faster-whisper word timings**, using the fraction only if the word fails to align. Character
offset interpolation is a stopgap, never the authority — and it drifts most on Hindi, where
delivery rate swings across a long clip.

| scene | line | anchor word | `f` | offset |
|---|---|---|---|---|
| s14 | 2.6 | «तीन परसेंट» | 0.71 | **+4.24** |
| s16 | 2.8 | «दस लाख» | 0.25 | +1.90 *(floored)* |
| s18 | 2.10 | «ढाई हज़ार» | 0.72 | +3.01 |
| s24 | 3.3 | «पाँच हज़ार» | 0.78 | +4.34 |
| s33 | 4.3 | «दस हज़ार» | 0.76 | +4.58 |
| s46 | 5.6 | «बारह परसेंट चेतावनी» | 0.55 | +2.00 |
| s50 | 5.10 | «पचपन सौ» | 0.80 | +6.08 |
| s62 | 6.5 | «एक करोड़» | 0.00 | +1.90 *(floored)* |
| s64 | 6.7 | «पच्चीस हज़ार» | 0.76 | **+4.12** |
| s66 | 6.9 | «चौबीस हज़ार» | 0.69 | +5.73 |
| s69 | 6.12 | «पचहत्तर लाख» | 0.83 | +5.87 |
| s4 | 1.4 | «बजता है» (Lottie **+2.75**, `buzz` **+3.48**) | 0.65 | see §8 |
| s34 | 4.4 | «घर का पूरा राशन» (framing swap) | 0.57 | **+5.020** |
| s52 | 5.12 | «इतनी बार दोहराया गया» (framing swap) | 0.55 | **+5.090** |
| s57 | 5.17 | «अगले साल वही राशन» (framing swap) | 0.60 | **+5.280** |
| s70 | 6.13 | «चार परसेंट पर पचहत्तर लाख» (framing swap) | 0.55 | **+5.210** |

⚠ **Not one anchored fraction from `storyboard-en.md` is portable.** Brian delivers at
~17.57 c/s and Amrut at ~14.281 c/s, and Hindi puts the figure in a different clause position.
Porting a fraction would put a number on screen before or after its own word.

**Track index alternates 1 / 2 by scene parity** (odd → 1, even → 2), because `hyperframes
check` rejects two overlapping clips on one track and every non-final scene overlaps its
successor by 0.45s. No column needed; it is `1 if n % 2 else 2`.

**`ken` direction is a rule, not a column:** s1 starts `i` (push in) and the direction **flips at
every boundary except the five holds**, where the partner continues its predecessor's move with
chained `plateKen` endpoints (§6b).

**`data-duration` = `timing.json` `scene_duration` + 0.45** on s1–s80; **s81 carries its
`scene_duration` bare**. Root duration is unaffected: **519.331s**.

---

## 6. The four breaches, the five holds, and the two scenes ruled NOT to need a framing

### 6a. Four measured `max_scene_seconds` breaches — two `data-framings` each

`check_build` FAILS any scene holding one photograph past **9.0s**. Four scenes measure past it.
Each is resolved inside the scene with a **derived tighter crop of its own source** under one
continuous push — the mechanism this cut has already proven on its own render (the s14→s15 joint
measured `scdet` 0.073 against 0.184/0.214 at the real photo boundaries either side).

| scene | line | dur | `data-framings` | swap at | anchored to | framing 1 file | framing 2 file |
|---|---|---|---|---|---|---|---|
| **s34** | 4.4 | 9.159 | **5.020, 4.139** | +5.020 | «घर का पूरा राशन» | `s34.jpg` — the kirana counter, wide | `s34b.jpg` — tight on the handwritten ration list |
| **s52** | 5.12 | 9.603 | **5.090, 4.513** | +5.090 | «इतनी बार दोहराया गया» | `s52.jpg` — the printed results page | `s52b.jpg` — tight on the ringed figure |
| **s57** | 5.17 | 9.185 | **5.280, 3.905** | +5.280 | «अगले साल वही राशन» | `s57.jpg` — the price slate, wide | `s57b.jpg` — tight on one re-chalked figure |
| **s70** | 6.13 | 9.812 | **5.210, 4.602** | +5.210 | «चार परसेंट पर पचहत्तर लाख» | `s70.jpg` — the tape against the plank, WIDE | `s70b.jpg` — a push to the SHORT end |

Sums are exact (5.020+4.139 = 9.159 · 5.090+4.513 = 9.603 · 5.280+3.905 = 9.185 · 5.210+4.602 =
9.812) and **no single framing exceeds 5.28s**. Every swap clears its scene's last fixed text cue
(+2.70 at the latest) by ≥2.3s. s70's pair is the script's own instruction, verbatim: *wide on
the tape against the plank, then a push to the short end.*

**Never a self-dissolve back to the same file** (creator rule, firaun 2026-07-23). Each `b` file
is a *different file cropped from the same source at full resolution*, which is what makes the
swap read as a push rather than a flash. `cues.py` fires a `transition` on each swap — correct
here, because a change genuinely happens.

⚠ **The instruction that was INVERTED and must not be carried forward.** An earlier handoff named
**2.4** as the breaching scene and ordered two framings for it. **2.4 (s12) measures 7.853s and
takes ONE framing.** The flat character model had predicted 9.01s for it and 7.9s for 6.13, and
was wrong in both directions. `timing.json` governs.

### 6b. Five matched-frame holds — the ledger spine, plus the rate hold

| pair | lines | one continuous zoom over | second file | ken |
|---|---|---|---|---|
| **s14 → s15** | 2.6 → 2.7 | the pencilled figure on ruled paper, 13.485s total | **already on disk** — the derived crop from the superseded build | `i` 1.00→1.09, then 1.09→1.16 |
| **s17 → s18** | 2.9 → 2.10 | a ruled ledger page, 9.985s total | `s18.jpg` = derived crop of `s17.jpg`'s source, framed one line lower | `o` 1.16→1.08, then 1.08→1.00 |
| **s23 → s24** | 3.2 → 3.3 | a cloth-bound account register, 12.180s | `s24.jpg` = derived crop of `s23.jpg`'s source | `i` 1.00→1.08, then 1.08→1.16 |
| **s32 → s33** | 4.2 → 4.3 | a carbon-copy receipt counterfoil, 12.676s | `s33.jpg` = derived crop of `s32.jpg`'s source | `o` 1.16→1.08, then 1.08→1.00 |
| **s63 → s64** | 6.6 → 6.7 | a stamped ledger page, the final division, 11.892s | `s64.jpg` = derived crop of `s63.jpg`'s source, on the monthly line | `i` 1.00→1.08, then 1.08→1.16 |

Each single framing stays well under 9.0s (max 7.069). Each pair: **no `transition` SFX at the
joint** (§2 `holds`), **one ground hex shared across both scenes** (§11), and the second scene's
`plateKen` picks up exactly where the first ended.

**Why four of them are one device, not a tic.** The script's own arithmetic is stepped — corpus
and rate → yearly → monthly, each on its own line — and every rung says *"the same ledger page,
carried down"*. So the recurring shape **is** the argument: at every rung the page is pushed one
line further. Four identical zooms across four rungs read as a motif; four different treatments
would read as indecision. The fifth (s14→s15) is the script's own declared hold on the working
number and is already rendered and verified on disk.

⚠ **The ground rule this forces, declared so a later pass does not "correct" it.** A hold pair
shares ONE `--f1`, and for the four ledger pairs that hex is the **`--fund` ground of the scene
that closes the pair** — the division and its monthly answer are one green event. The first half
of each pair therefore runs a fund ground while its own TEXT carries no role colour. That is
correct: "one role colour per scene" is a rule about type, and the ground has earned green
because the frame is literally the corpus's division at the stated rate.

### 6c. Two near-cap scenes ruled NOT to need a second framing

| scene | line | dur | margin | ruling |
|---|---|---|---|---|
| **s27** | 3.6 | **8.976** | 0.024s | **ONE framing.** It passes the measured gate. Its beat is a single object being pressed once; a swap would give `cues.py` a `transition` to punctuate at exactly the moment the frame is asserting that *nothing changed but the corpus*. Surplus goes into the hold after `num` + `pop` at +2.00 |
| **s65** | 6.8 | **8.924** | 0.076s | **ONE framing.** Two sheets laid edge to edge is a static comparison; pushing in on one of them argues for one side. Surplus goes into the hold after the `.sub` rate at +1.90 |

**The trip-wire, recorded rather than swallowed:** both clear by <0.1s. **If either line is ever
re-voiced, re-measure before building** — a 100 ms lengthening puts it over the cap and
`check_build` fails the chapter. Neither may be expanded by a later script pass.

**Emit `data-framings` on all 81 sections** — on the 77 single-framing scenes it is one value
equal to `scene_duration`. That costs nothing and removes any question about whether an absent
attribute means "one framing" or "not declared". Framings always sum to `scene_duration`
(= `data-duration` − 0.45; s81 = `data-duration`).

---

## 7. Scenes — the archetype row

One row per VO line. `start` / `dur` = `scene_start` / `scene_duration`, **verbatim from
`timing.json`, the only home**; `d-dur` = `dur + 0.45` (s81 bare). Every fixed cue is
`start + offset` from §5.

`arch`: **A** plate · **B** figure · **C** ledger · **D** band — **taken from the script's own
`[arch …]` cue on every line; this file changed none of them.** `ground`: the scene's `--f1`
(§11). `art`: `off` · `fwd` (= `art-forward`) · a named layer. `ctr`: `centred` — **the rule is
deterministic: a scene is `centred` unless something real occupies the archetype's other side**
(a drawn layer, the Lottie stage, or a declared cascade owning the band); `fin-build` then drops
that scene's plate, `crule`, `vrule` and `brule`, because a split with nothing opposite is a
hole. `trans`: `dis` = 0.45s dissolve · **`SHOVE`** · `hold` = matched-frame continuous zoom
(§6b). `sfx`: the CONTENT cue this scene emits (§2) — `—` means DRY, joint only.
**Every scene carries `has-photo` and a real `.bg`. There are no exceptions and none may be added.**

| # | line | start | dur | d-dur | trans | arch | ground | art | ctr | focal · var · role | `#sN-rate` | sfx | bg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1.1 | 0.000 | 4.222 | 4.672 | dis | A | `#161f2b` | off | Y | stmt · A · — | — | — | `s1.jpg` ⟵ REUSE |
| 2 | 1.2 | 4.222 | 4.144 | 4.594 | dis | D | `#1a1e24` | off | **N** | 3 chips · C · — | — | — | `s2.jpg` ⟵ REUSE |
| 3 | 1.3 | 8.366 | 3.856 | 4.306 | dis | A | `#241d15` | off | Y | stmt · A · — | — | — | `s3.jpg` ⟵ REUSE |
| 4 | 1.4 | 12.222 | 5.763 | 6.213 | dis | D | `#241d15` | **lottie `phone-notify-credit`** | **N** | stmt · A · — | — | **buzz** | `s4.jpg` |
| 5 | 1.5 | 17.985 | 3.673 | 4.123 | dis | A | `#1c2027` | off | Y | stmt · A · — | — | — | `s5.jpg` ⟵ REUSE |
| 6 | 1.6 | 21.659 | 8.167 | 8.617 | dis | D | `#291f13` | **ticks (3 icons)** | **N** | 3 icon cells · C · — | — | **chip ×3, counted** | `s6.jpg` ⟵ REUSE |
| 7 | 1.7 | 29.825 | 5.345 | 5.795 | dis | B | `#1f1e1c` | off | Y | stmt · A · — | — | — | `s7.jpg` ⟵ REUSE |
| 8 | 1.8 | 35.171 | 7.304 | 7.754 | dis | A | `#191f28` | off | Y | stmt · A (**pop**) · — | — | **stamp** | `s8.jpg` |
| 9 | 2.1 | 42.475 | 5.293 | 5.743 | dis | A | `#1c2027` | off | Y | stmt · A · — | — | reveal | `s9.jpg` ⟵ REUSE |
| 10 | 2.2 | 47.768 | 6.260 | 6.710 | dis | C | `#191f28` | off | Y | stmt · A · — | — | — | `s10.jpg` |
| 11 | 2.3 | 54.028 | 6.129 | 6.579 | dis | D | `#2a2113` | off | Y | stmt · A · **target** | — | — | `s11.jpg` |
| 12 | 2.4 | 60.157 | 7.853 | 8.303 | dis | D | `#2e2411` | off | Y | stmt · A · **target** | — | — | `s12.jpg` |
| 13 | 2.5 | 68.010 | 5.711 | 6.161 | dis | A | `#1a1e24` | off | Y | stmt · A · — | — | — | `s13.jpg` ⟵ REUSE |
| 14 | 2.6 | 73.721 | 6.416 | 6.866 | **hold** | B | `#2e2411` | off | Y | **`.mega` `3.0%`** · B (§5 exc. 1) · **target** | *(focal)* | reveal | `s14.jpg` ⟵ REUSE |
| 15 | 2.7 | 80.137 | 7.069 | 7.519 | dis | B | `#2e2411` | off | Y | stmt · A · **target** | span 3.0% | reveal | `s15.jpg` ⟵ REUSE crop |
| 16 | 2.8 | 87.207 | 5.345 | 5.795 | dis | B | `#241d15` | off | Y | **num `₹10,00,000`** · B · — | `.sub` | **hero** | `s16.jpg` ⟵ REUSE |
| 17 | 2.9 | 92.552 | 5.345 | 5.795 | **hold** | B | `#17291f` | off | Y | stmt · A · — | span 3.0% | — | `s17.jpg` |
| 18 | 2.10 | 97.897 | 4.640 | 5.090 | dis | B | `#17291f` | off | Y | **num `₹2,500`** · B · **fund** | `.sub` | — | `s18.jpg` ⟵ crop of s17 |
| 19 | 2.11 | 102.537 | 6.547 | 6.997 | dis | C | `#1f1e1c` | off | Y | stmt · A · — | `.sub` | reveal | `s19.jpg` |
| 20 | 2.12 | 109.084 | 6.416 | 6.866 | dis | C | `#1b3024` | off | Y | stmt · A · **fund** | — | reveal | `s20.jpg` |
| 21 | 2.13 | 115.500 | 8.506 | 8.956 | dis | A | `#241d15` | off | Y | stmt · A · — | — | — | `s21.jpg` |
| 22 | 3.1 | 124.007 | 5.424 | 5.874 | dis | A | `#1c2027` | off | Y | **num `₹20,00,000`** · B · — | `.sub` | — | `s22.jpg` |
| 23 | 3.2 | 129.430 | 6.129 | 6.579 | **hold** | B | `#17291f` | off | Y | stmt · A · — | span 3.0% | — | `s23.jpg` |
| 24 | 3.3 | 135.559 | 6.051 | 6.501 | dis | B | `#17291f` | off | Y | **num `₹5,000`** · B · **fund** | `.sub` | — | `s24.jpg` ⟵ crop of s23 |
| 25 | 3.4 | 141.610 | 6.782 | 7.232 | dis | C | `#1f1e1c` | off | Y | stmt · A · — | `.sub` | reveal | `s25.jpg` |
| 26 | 3.5 | 148.392 | 8.219 | 8.669 | dis | A | `#291f13` | off | Y | stmt · A · — | — | — | `s26.jpg` |
| 27 | 3.6 | 156.611 | **8.976** | 9.426 | dis | B | `#2a2113` | off | Y | **num `3.0%`** · B (**pop**) · **target** | *(focal)* | **stamp** | `s27.jpg` |
| 28 | 3.7 | 165.587 | 8.506 | 8.956 | dis | B | `#1a1e24` | **fwd `corpus-doubles`** | **N** | stmt · A · — | `.sub` | reveal | `s28.jpg` ⟵ REUSE |
| 29 | 3.8 | 174.093 | 5.398 | 5.848 | dis | C | `#2b1418` | off | Y | stmt · A · **warn** | — | reveal | `s29.jpg` |
| 30 | 3.9 | 179.491 | 5.659 | 6.109 | dis | A | `#1f1e1c` | off | Y | stmt · A · — | — | — | `s30.jpg` |
| 31 | 4.1 | 185.149 | 4.562 | 5.012 | dis | A | `#1c2027` | off | Y | **num `₹40,00,000`** · B · — | `.sub` | — | `s31.jpg` |
| 32 | 4.2 | 189.711 | 6.181 | 6.631 | **hold** | B | `#17291f` | off | Y | stmt · A · — | span 3.0% | — | `s32.jpg` |
| 33 | 4.3 | 195.892 | 6.495 | 6.945 | dis | B | `#17291f` | off | Y | **num `₹10,000`** · B · **fund** | `.sub` | — | `s33.jpg` ⟵ crop of s32 |
| 34 | 4.4 | 202.387 | **9.159** ⚠ | 9.609 | dis | C | `#291f13` | off | Y | stmt · A · — | `.sub` | reveal + **swap** | `s34.jpg` + `s34b.jpg` |
| 35 | 4.5 | 211.546 | 7.984 | 8.434 | dis | C | **`#2d2214`** | off | Y | stmt · A · — | `.sub` | — | `s35.jpg` + `s35b.jpg` *(cut-in)* |
| 36 | 4.6 | 219.530 | 5.711 | 6.161 | dis | A | `#1c2027` | off | Y | stmt · A · — | — | — | `s36.jpg` |
| 37 | 4.7 | 225.241 | 5.293 | 5.743 | dis | D | `#301519` | off | Y | stmt · A · **warn** | — | reveal | `s37.jpg` |
| 38 | 4.8 | 230.534 | 6.181 | 6.631 | dis | D | `#2a2113` | off | Y | stmt · A · **target** | — | reveal | `s38.jpg` |
| 39 | 4.9 | 236.715 | 8.402 | 8.852 | dis | C | `#191f28` | off | Y | stmt · A · — | — | — | `s39.jpg` |
| 40 | 4.10 | 245.117 | 5.528 | 5.978 | **SHOVE** | B | `#2e2411` | off | Y | stmt · A · **target** | span 3.0% | reveal | `s40.jpg` |
| 41 | 5.1 | 250.645 | 4.091 | 4.541 | dis | A | `#1a1e24` | off | Y | kicker only · A (§5 exc. 2) · — | — | — | `s41.jpg` |
| 42 | 5.2 | 254.736 | 5.816 | 6.266 | dis | B | `#301519` | off | Y | stmt · A · **warn ⚠ §1b** | **2 spans** | reveal | `s42.jpg` |
| 43 | 5.3 | 260.552 | 8.088 | 8.538 | dis | A | `#1c2027` | off | Y | stmt · A · — | — | — | `s43.jpg` |
| 44 | 5.4 | 268.640 | 6.233 | 6.683 | dis | D | `#38151a` | off | Y | stmt · A · **warn** | — | — | `s44.jpg` |
| 45 | 5.5 | 274.873 | 4.222 | 4.672 | dis | D | **`#3b1219`** | off | Y | stmt · A · **warn** | — | — | `s45.jpg` |
| 46 | 5.6 | 279.096 | 3.987 | 4.437 | dis | B | `#38151a` | off | Y | **num `12%`** + **`.stamp.warn`** · B · **warn** | *(focal)* | **stamp** | `s46.jpg` |
| 47 | 5.7 | 283.082 | 6.782 | 7.232 | dis | C | `#1a1e24` | off | Y | stmt · A · — | — | — | `s47.jpg` |
| 48 | 5.8 | 289.864 | 6.364 | 6.814 | dis | B | `#2a2113` | off | Y | **num `7.4% p.a.`** · B · **target** | *(focal)* | — | `s48.jpg` |
| 49 | 5.9 | 296.229 | 5.946 | 6.396 | dis | C | `#191f28` | off | Y | stmt · A · — | span 7.4% | — | `s49.jpg` |
| 50 | 5.10 | 302.175 | 8.088 | 8.538 | dis | B | `#2e2411` | off | Y | **num `₹5,550 A MONTH`** · B · **target** | span 7.4% | — | `s50.jpg` |
| 51 | 5.11 | 310.263 | 6.077 | 6.527 | dis | A | `#1c2027` | off | Y | stmt · A · — | — | — | `s51.jpg` |
| 52 | 5.12 | 316.340 | **9.603** ⚠ | 10.053 | dis | B | `#301519` | off | Y | **num `4%`** · B · **warn** | *(focal)* | **swap** | `s52.jpg` + `s52b.jpg` |
| 53 | 5.13 | 325.943 | 7.931 | 8.381 | dis | C | `#131f2c` | off | Y | stmt · A · — | — | — | `s53.jpg` |
| 54 | 5.14 | 333.874 | 7.931 | 8.381 | dis | C | **`#0c1a2c`** ⚠ | off | Y | stmt · A · **warn** | — | — | `s54.jpg` |
| 55 | 5.15 | 341.806 | 5.946 | 6.396 | dis | C | **`#372a0c`** | off | Y | stmt `3.0% TO 3.5%` · A · **target** | *(focal)* | — | `s55.jpg` |
| 56 | 5.16 | 347.752 | 7.017 | 7.467 | dis | B | `#38151a` | off | Y | **num `3.75%`** · B (**pop**) · **warn** | *(focal)* | **stamp** | `s56.jpg` |
| 57 | 5.17 | 354.769 | **9.185** ⚠ | 9.635 | dis | B | `#2e2411` | off | Y | **num `5%`** · B · **target** | *(focal)* | **swap** | `s57.jpg` + `s57b.jpg` |
| 58 | 6.1 | 363.954 | 4.274 | 4.724 | dis | A | `#1c2027` | off | Y | **num `₹50,00,000`** · B · — | `.sub` | — | `s58.jpg` |
| 59 | 6.2 | 368.229 | 6.469 | 6.919 | dis | B | `#1b3024` | off | Y | **num `₹12,500 A MONTH`** · B · **fund** | span 3.0% | — | `s59.jpg` |
| 60 | 6.3 | 374.697 | 8.088 | 8.538 | dis | C | `#1f1e1c` | off | Y | stmt · A · — | `.sub` | reveal | `s60.jpg` + `s60b.jpg` *(cut-in)* |
| 61 | 6.4 | 382.785 | 7.252 | 7.702 | **SHOVE** | A | `#101720` | off | Y | stmt · A · — | — | — | `s61.jpg` |
| 62 | 6.5 | 390.038 | 4.509 | 4.959 | dis | B | `#2a2113` | off | Y | **num `₹1,00,00,000`** · B · **target** | `.sub` | **hero** | `s62.jpg` |
| 63 | 6.6 | 394.547 | 5.998 | 6.448 | **hold** | B | **`#1d3a28`** | off | Y | stmt · A · — | span 3.0% | — | `s63.jpg` |
| 64 | 6.7 | 400.545 | 5.894 | 6.344 | dis | B | **`#1d3a28`** | off | Y | **num `₹25,000 A MONTH`** · B · **fund** | `.sub` | **hero** | `s64.jpg` ⟵ crop of s63 |
| 65 | 6.8 | 406.439 | **8.924** | 9.374 | dis | A | `#1a1e24` | off | Y | stmt · A · — | **`.sub` ⚠ §4a** | reveal | `s65.jpg` |
| 66 | 6.9 | 415.363 | 8.741 | 9.191 | dis | C | `#191f28` | off | Y | **num `₹24,217`** · B · — | *(n/a — not a corpus)* | — | `s66.jpg` |
| 67 | 6.10 | 424.104 | 6.834 | 7.284 | dis | B | `#1b3024` | **fwd `they-meet`** | **N** | stmt · A · **fund** | span 3.0% | reveal | `s67.jpg` |
| 68 | 6.11 | 430.939 | 7.383 | 7.833 | dis | B | `#1c2027` | off | Y | stmt · A · — | — | reveal | `s68.jpg` |
| 69 | 6.12 | 438.322 | 7.566 | 8.016 | dis | B | `#301519` | off | Y | **num `₹75,00,000`** · B · **warn** | span 4% | — | `s69.jpg` |
| 70 | 6.13 | 445.887 | **9.812** ⚠ | 10.262 | dis | B | `#38151a` | off | Y | stmt · A (**pop**) · **warn ⚠ §1b** | **2 spans** | **stamp + swap** | `s70.jpg` + `s70b.jpg` |
| 71 | 6.14 | 455.700 | 5.659 | 6.109 | dis | A | `#1a1e24` | off | Y | stmt · A · — | — | — | `s71.jpg` |
| 72 | 6.15 | 461.358 | 6.965 | 7.415 | dis | B | `#2a2113` | off | Y | **num `₹19,000 A MONTH`** · B · **target** | `.sub` | — | `s72.jpg` |
| 73 | 6.16 | 468.323 | 6.834 | 7.284 | dis | B | `#2e2411` | off | Y | **num `₹10,000 A MONTH`** · B · **target** | `.sub` | — | `s73.jpg` |
| 74 | 7.1 | 475.158 | 4.875 | 5.325 | dis | A | `#161f2b` | off | Y | stmt · A · — | — | — | `s74.jpg` |
| 75 | 7.2 | 480.033 | 4.640 | 5.090 | dis | D | `#191f28` | off | Y | stmt · A · — | — | — | `s75.jpg` |
| 76 | 7.3 | 484.673 | 5.110 | 5.560 | dis | B | `#1c2027` | off | Y | stmt · A · — | span 3.0% | — | `s76.jpg` |
| 77 | 7.4 | 489.783 | 6.547 | 6.997 | dis | A | `#1f1e1c` | off | Y | stmt · A · — | — | — | `s77.jpg` |
| 78 | 7.5 | 496.330 | 5.816 | 6.266 | dis | D | `#241d15` | off | Y | stmt · A · — | — | — | `s78.jpg` |
| 79 | 7.6 | 502.145 | 5.894 | 6.344 | dis | B | `#17291f` | off | Y | stmt · A · **fund** | span 3.0% | — | `s79.jpg` |
| 80 | 7.7 | 508.039 | 6.547 | 6.997 | dis | A | `#291f13` | off | Y | stmt · A · — | — | — | `s80.jpg` |
| 81 | 7.8 | 514.586 | 4.744 | **4.744** | — | A | `#33200f` | off | Y | **`.cta`** · D · **pop** | — | **cta** | `s81.jpg` |

**Row checks.** 81 scenes ✓ · every `start`/`dur` byte-for-byte from `timing.json`, nothing
re-timed ✓ · **2 SHOVE** (s40→s41, s61→s62) ✓ · **5 hold pairs** ✓ · **4 two-framing scenes**,
all four the measured breaches, sums exact ✓ · 22 `num` scenes, none carrying a `stmt` as a
second focal ✓ · **`.mega` exactly once** (s14) and never with `.huge` in the same scene ✓ ·
`--pop` exactly once (s81) ✓ · 31 `#sN-rate` elements (§4) ✓ · **6 scenes carry a second image
file** (s34, s35, s52, s57, s60, s70) ✓ · **75 `centred`, 6 with something real on the other
side** (s2, s4, s6, s28, s67 — and s2/s6 are cascades owning the band) ✓ · `has-photo` + a real
`.bg` on all 81 ✓ · ken never repeats a direction except across the five declared holds ✓.

*(s2, s4, s6, s28, s67 = five `ctr: N`; the row-check line above counts them.)*

### The archetype sequence, read as a rhythm

```
ch1  A D A D A D B A
ch2  A C D D A B B B B B C C A
ch3  A B B C A B B C A
ch4  A B B C C A D D C B
ch5  A B A D D B C B C B A B C C C B B
ch6  A B C A B B B A C B B B B A B B
ch7  A D B A D B A A
```

Totals **A 23 · B 32 · C 15 · D 11**. B-heavy, because almost every beat in this video *is* a
figure — that is the argument, not a lack of variety. **Every one of these is the script's own
assignment; this file changed none.**

**Five deliberate holds of one archetype, each because the scenes are one argument:**

- **ch2 `B B B B B` (s14–s18)** — the rate is declared, defended, applied to a corpus, divided,
  and divided again. Five scenes, one chain of reasoning; the *mechanism* under it changes every
  time (a pencilled figure → a tighter crop of it → current-series notes → a ledger page → the
  same page one line lower). Varying the layout here would break the only through-line the
  chapter has.
- **ch3 `B B` (s23–s24)** and **ch4 `B B` (s32–s33)** — one rung's division and its monthly
  answer. This is the shape every rung repeats, and the regularity IS the ladder made visible.
- **ch5 `C C C` (s53–s55)** — the American paper, what it excluded, India's own paper. Three
  documents, one evidentiary case; the *artefact* changes underneath (a bound journal → a
  methodology page → a stapled paper). This is the through-line the whole run exists for.
- **ch6 `B B B B` (s67–s70)** — the meeting, the guard rail, the imported target, the cost of
  importing it. Four figures, ONE argument: what the rate does to the same monthly income.
- **ch6 `B B` (s72–s73)** — two assumed growth rates, deliberately shown side by side as two
  columns of the same calculation. Varying them would suggest one is the answer.

**Every rung is `A/B → B → B`** — the corpus named, the division worked, the monthly answer:
s16/s17/s18 · s22/s23/s24 · s31/s32/s33 · s58/s59 · s62/s63/s64.

---

## 8. Vector art — 2 drawn proportions, 1 icon row, 1 Lottie, 0 emoji

Rule 8 is the test: **if you cannot say what the art asserts that the picture cannot, it is
`off`.** It is `off` on **77 of 81 scenes**. Density against the archetype note's calibration
("three or four drawn layers in a twelve-to-fourteen scene chapter is the top of the range, not
the target"): ch1 **2** · ch2 **0** · ch3 **1** · ch4 **0** · ch5 **0** · ch6 **1** · ch7 **0**.

Both drawn proportions are `art-forward` (52%) because the point of each is a **PROPORTION** and
the mechanism still wins; the photograph is there to satisfy `image_per_scene`. Both are authored
**in the plate's own coordinate space**, never in 1920×1080.

| scene | line | plate · viewBox | motif | what it ASSERTS that the photograph cannot | arithmetic (`truth_bar`) |
|---|---|---|---|---|---|
| **s28** | 3.7 | `p-b` · `0 0 800 610` | **`corpus-doubles`** — two solid blocks, the second exactly **2.00×** the first, and beneath them a second pair at the same 2.00× for the monthly figures; a single 12px rule labelled with the rate runs under both pairs | **the ratio is identical on both sides.** The photograph shows two weights of *different* mass; only the drawing shows that the corpus doubled, the income doubled, and the rate did not move | block2 = **2.000 ×** block1 (₹20,00,000 ÷ ₹10,00,000) and pair2 = **2.000 ×** pair1 (₹5,000 ÷ ₹2,500). State it in the generator comment at the point of edit |
| **s67** | 6.10 | `p-b` · `0 0 800 610` | **`they-meet`** — two solid bars side by side, the right one at **0.9687** of the left, with a ghost rect at ~.2 marking the 3.1% shortfall | **HOW equal they are.** A level two-pan balance says "equal"; only the drawing says ₹24,217 is 96.87% of ₹25,000 — and this is the cut's one sourced external comparison | ₹24,217 ÷ ₹25,000 = **0.96868**. PLFS Annual Report 2025 (men), via PIB |

**Construction rules both obey** (they cost two draft rounds on japanese-money-methods and one
shipped invisible funnel on this cut's own ch2):

- **Solid fills and heavy strokes only.** `.has-photo .art` is 30% and `.art-forward` 52%; a 2–3px
  stroke at 0.4 alpha is simply not on screen. Ghost tracks are **filled rects at ~.2**, never
  outlines. Nothing thinner than 9px. *(ch2 shipped `s16`'s funnel at fill-opacity `.18`, under
  `art_opacity.over_photo` 0.3 — the chapter's one drawn mechanism was invisible.)*
- **The per-scene `opacity` on the `<svg>` is a no-op** — `.has-photo .art` and
  `.has-photo.art-forward .art` both carry `!important`. The only levers that reach the screen are
  the weight and alpha of the elements inside.
- `stroke-width="N"` as an SVG **attribute is a no-op** — write inline `style="stroke-width:N"`.
- **`.p-b` maps viewBox x 1:1 to screen x.** The plate is `left:1120px; width:860px`, so anything
  past **vx = 800 is off-canvas** and does not exist on the encode. Both motifs are authored
  inside 800.
- **Never darken the photograph** to make art readable (rule 9; creator rejected it 2026-08-04,
  *"it fails to black and white"*). Both scenes get a **`.band`** behind their mechanism
  (`#sN-band`). **`.art-lift` on s28**, whose plate sits on the brighter part of the balance still.
- **Assemble by about +3.3**, or the contact sheet's +2.6s sample reads as a half-built frame.

### The icon row — s6 (1.6), ported verbatim from the built ch1

**Do not re-author this.** It already renders in
`studio/videos/passive-income-number-hi-ch1/index.html` (as that project's `s5`) and is
creator-reviewed: three `.v-tickcell` groups, each an inline `<svg class="icon">` — **a lit bulb
(बिजली), a tied SACK (राशन), a house with its door (किराया)** — each followed by a small
`.icon.sm` checkbox whose tick path is drawn in sequence.

- **Why it is additive.** 1.6 names three subjects **and a verb** («…चुपचाप भरते रहना»), and no
  photograph of that exists to be bought: 12 candidates across two queries cleared nothing. The
  drawing asserts a **COUNT and a PROCESS**, which is `vector_art.reach_for_it_when` on the merits.
- **Rule 8 holds by construction:** the ration mark is a **sack, not a jar**, precisely so nothing
  drawn re-draws an object the photograph already shows.
- `art: ticks`, `ctr: N` — D has its mechanism back, so the band is not empty.
- Cue: the three cells cascade at **+1.10 / +1.70 / +2.30** (`popEach`, fixed 0.6s) and each tick
  trails its cell by **+0.35** (`pulse`). `counted` in `cues-tables.json` — three clicks, and the
  count is the point.

### One Lottie — `phone-notify-credit` on s4 (1.4)

Library reuse, **no fetch**: `assets/lottie/phone-notify-credit.json` (in-house, already used on
`japanese-money-methods-hi-ch1 s1` and on this run's own ch1, where it was **proven to draw and
animate from encoded frames**, not from the file reference). **No tint** — `index.json` records it
as authored in the system's own palette, and tinting would push it into a role colour 1.4 has not
earned.

- **Why it is additive, not depictive.** The photograph is a phone with a **dark, switched-off
  screen** — the design system bans a lit phone-screen photo as a background and that has shipped
  undetected three times. The drawn banner is the only honest way to state that money **arrived**;
  the picture is structurally forbidden from saying it.
- **⚠ The card MUST carry the `₹` glyph. The amount is MASKED; the currency is NOT.** The card
  reads `₹ • • • •`. Naming a figure at 0:14 would break the open loop the whole cold open is
  built on (the number is withheld until 6.5), but ch1's own review found the opposite failure: a
  banner with no currency glyph says *"a notification arrived"*, not *"money arrived"* — on the one
  beat a 42-second cold open exists to deliver. **This was a recorded ch1 blocker; it is closed
  here and must not reopen.**
- **Stage in PIXELS.** `.p-d` band, `left/top/width/height` declared in px with
  `.stage svg { width:100% !important; height:100% !important }`. A stage without pixel dimensions
  renders the artwork at native size pinned top-left and every check passes.
- **Cues.** `s4-kick` +0.30 · `s4-stmt` `rise` **+1.10** · `playLottie` **anchored +2.75** ·
  `buzz` SFX **+3.48** on «बजता है». The banner is visibly building ~0.7s before the sound, which
  is the ordering fin-editor measured on the en cut and ruled correct: a sound must never precede
  its own picture. The card lands ~2.3s before the cut.

**One Lottie, not four.** The cap is `max_per_chapter: 4` — a threshold at which you must justify
the next one, never a target. `lottie-web` redraws the whole illustration every frame (two heavy
ones took a 20s 1080p render from 1m27 to 3m56), and a deck of them stops looking like a film.
**No two Lotties are adjacent because there is only one.**

**Neither the Lottie nor a drawn layer sits on s16, s62 or s64** — the three frames carrying the
video's big numbers already have their one focal element (`one_focal_per_scene`).

### One `.stamp` pill — s46 (5.6)

5.6's cue block carries **both** `num: 12%` and `stmt: Not an opportunity. A warning.` The `num`
is the focal; the `stmt` becomes the **`.stamp.warn`** verbatim — a solid `--warn` fill, `#0d1017`
text, `rotate(-4deg)`, `back.out` entry, 44px. No new copy, and it is the video's single verdict
pill. The other four `stamp`-SFX scenes (s8, s27, s56, s70) take a `pop` entry on their focal
instead: five rotated pills would be a tic.

⚠ **The rotated `.stamp` reports a false contrast failure** when it sits on a bright fill. Design
doc §9: **do not fix it by lightening the text.** Carry it in `known_benign` for this scene only.

### What was considered and refused

| candidate | verdict |
|---|---|
| **2.3 / 2.4 / 4.7 / 4.8 / 5.4 / 5.5 — the tank at six tap positions** | **`off`, all six.** A drawn tank over a photographed tank is the "ghost envelope over a photograph of an envelope" failure by name. The tank is carried **photographically** across six frames (§10) and the tap position alone says the beat |
| **4.8 — how long the tank lasts at 3% vs 12%** | **REFUSED.** A level falling to zero over time asserts a **depletion schedule we have no source for**, and a drawn projection is the shape `no_return_promise` forbids. Same call the en cut made |
| **5.10 — a bar hitting the ₹9,00,000 ceiling** | **REFUSED.** A bar with no declared scale asserts nothing measurable; it is a metaphor dressed as a statistic, which `truth_bar` forbids. The concrete ceiling photograph plus the `stmt` says it honestly |
| **5.17 — a withdrawal that rises with inflation** | **REFUSED.** Drawing a rising schedule asserts a multi-year projection from a one-year CPI figure. The chalked-and-re-chalked price slate plus the `foot:` citation is the honest treatment |
| **2.12 — twelve drawn stubs** · **4.10 — three drawn rungs** | **`off`.** The photograph *is* the count in both cases — depictive |
| **6.13 — a bar at 0.75 of another** | **`off`, and this is a change of mind worth recording.** The scene already carries its assertion twice: two `data-framings` (wide → a push to the short end) and a `stmt` naming both figures. A third statement of the same proportion is padding, and it would push the frame to six countable elements |

**No icons beyond s6.** `assets/icons/` holds `checkbox-tick`, `padlock-closed`, `pen-nib-line`,
`reorder-rules`, `growth-arrow`, and none asserts anything this cut's photographs do not already
say: a padlock over a locker door, an arrow over a staircase, a tick over a receipt are all the
rule-8 depictive failure.

**Zero emoji, deliberately.** They are an OS font sitting outside the grade and would land as a
sticker on a dark documentary frame. Not used, and not meant.

---

## 9. The two peaks

### 9a. PEAK 1 — ₹10,00,000 → ₹2,500 a month (s16–s18, 16.8–19.7%)

The first rung is the **retention** beat, and it is the only rung besides the hero that rings.
Its power is that the whole method completes inside 20 seconds of screen time:

- **s16 (2.8)** — `arch B`, ground `#241d15`, `₹10,00,000` at `.huge` 112 landing at **+1.90**,
  the rate on screen since +1.10, `hero`. The photograph is the **cleared current-series note
  reference** (§10) — this frame is where the demonetised-note blocker lived.
- **s17 → s18 (2.9 → 2.10)** — one ledger page under one continuous zoom, the division carried
  down to the monthly line, `₹2,500` arriving at **+3.01** on «ढाई हज़ार». Both dry: the count is
  the event, not a hit.

### 9b. PEAK 2 — ₹1,00,00,000 at 3.0% → ₹25,000 a month (s62–s64, 75.1–77.5%)

The reward beat for the promise in the title, and it gets **four things peak 1 does not**:

1. **A shove into it** (s61 → s62). 6.4 says out loud that the number held back at the start is
   this one; a dissolve would smuggle the payoff in as a continuation instead of announcing it.
2. **The emptiest, coldest frame in the video immediately before it** — s61 runs `#101720` with
   kicker + stmt and no figure at all. *The payoff is a temperature event before it is a number.*
3. **The deepest green in the video**, `#1d3a28`, spent once, across the s63→s64 hold — so the
   division and its answer are one unbroken green shot.
4. **Two `hero` cues**, on s62 (the corpus) and s64 (the monthly figure) — the only place in the
   cut where two land inside 15 seconds, because this is the one place the video is allowed to
   celebrate.

And the cut's **only `.mega`** sits at **s14 (2.6): `3.0%` at 240px**. That is what makes both
peaks land: *in a video arguing that the rate is the whole answer, the RATE is the one enormous
number on screen, and every corpus it produces is smaller than it.* `.mega` appears **exactly once
in the video** (`one_focal_per_scene`; never `.huge` and `.mega` together).

### 9c. No measure bar — a deliberate divergence from the en cut

The en cut climbs its five rungs with a `.measure` bar at one scale (`storyboard-en.md` §9a) and
flags it as a back-port candidate. **This cut declines it**, and the reason is rule 8: the hi cut
already climbs **photographically** — a cash box (s16) → two cash boxes (s22) → a steel trunk
(s31) → a bank locker (s58) → a safe door (s62), each container visibly bigger than the last.
A drawn bar over a photograph that is already escalating is the depictive failure, and it would
add a component this cut has never rendered plus five `-meas` / `-mlab` / `-mf` nodes. **The
container ladder is the climb; nothing is drawn on top of it.**

---

## 10. Imagery — 87 slots, 87 files, zero photo-free scenes

**`image_per_scene` is a hard creator rule** (2026-07-28, `photo_free_scene_ratio` = 0). All 81
scenes carry `has-photo` and a real full-bleed `.bg` under the locked grade
`grayscale(.32) brightness(.62) contrast(1.05)`. **No per-scene grade override anywhere in this
cut** — the chapter archetype layer closes that escape hatch, so the photograph is the only
variable there is.

- **81 bg slots** + **4 second framings** (`s34b`, `s52b`, `s57b`, `s70b`) + **2 cut-ins**
  (`s35b`, `s60b`) = **87 slots**.
- **67 fetched files.** `assets/img/manifest.json` is the single home for every query.
- **8 derived crops, no fetch** — `s18`, `s24`, `s33`, `s64` (the hold pairs) and `s34b`, `s52b`,
  `s57b`, `s70b` (the breach framings). `fin-assets` crops them from a source it already holds,
  at full resolution, and records the crop rect in `.src`.
- **12 files REUSED verbatim from the superseded style-A build** — §10a.

### 10a. The reuse ledger — what survives the restyle, and what does not

The superseded build fetched and verified **20 photographs** across ch1 (`assets-ch1/final/`) and
ch2 (`assets-ch2/final/`). Style E re-cut both chapters, so the mapping is **by SUBJECT, never by
scene index** — the two numberings diverge from line 1.

**REUSE — 12 files, no fetch, no re-verification:**

| new scene | line | ← old file | what it is | note |
|---|---|---|---|---|
| **s1** | 1.1 | ch1 `s3.jpg` | smartphone face down on a wooden table, dark | style E's cold open opens on the silent phone, which is what this file already is |
| **s2** | 1.2 | ch1 `s1.jpg` | vintage alarm clock on a bedside table | 1.2 needs "nothing switched on", not "face-down" — the spec relaxes to fit the file |
| **s3** | 1.3 | ch1 `s2.jpg` | steel glass of chai on a counter, india | ⚠ **this retires a standing blocker.** **style E's 1.3 names no window** — it names a counter and a steel glass, which is exactly the photograph. (Corrected 2026-08-08: this row said the file "has no window", but the shipped `s2.jpg` does have one — the no-window complaint was against an earlier round-1 candidate, and ch1 went through five asset rounds. The conclusion is unchanged and in fact stronger; only the stated reason was stale.) |
| **s5** | 1.5 | ch1 `s4.jpg` | engraved enamel plaque, YHIGH 203 | landed after kraft measured dead twice, and already **ACCEPTED on this exact NOT RICH beat** (`run.json` ch1 rulings, spoiler risk checked). Do not re-litigate; the en cut's eight-sheet search for the same beat does not apply |
| **s6** | 1.6 | ch1 `s5.jpg` | **three glass jars** (corrected 2026-08-08 — this ledger said "desk of paper documents", which is not what the file shows) | ⚠ **this closes the last open ch1 blocker.** The three named bills could not be bought (12 candidates, 2 queries), so they are **DRAWN** as three icon cells (§8). Ruling of 2026-08-07, carried forward intact — and it reads *better* on jars than on paper: three drawn tick cells over three real jars is one object per named cost |
| **s7** | 1.7 | ch1 `s6.jpg` | narrow empty stone staircase | same beat, same file |
| **s9** | 2.1 | ch2 `s8.jpg` | old iron safe strongbox, closed | script cue says "locked steel almirah with a key"; a closed strongbox is the same statement and is verified. **Override with reason** |
| **s13** | 2.5 | ch2 `s12.jpg` | steel bucket under a running tap | exact match to 2.5's cue |
| **s14** | 2.6 | ch2 `s13.jpg` | blank notebook + pencil, dark table | carries the cut's only `.mega` |
| **s15** | 2.7 | ch2 `s14.jpg` | the derived crop of s14's source | **the s14→s15 continuous zoom is already render-verified on this cut** (joint scdet 0.073 vs 0.184/0.214 either side; crop geometry 0.91755 against the specified 0.91754) |
| **s16** | 2.8 | ch2 `s11b.jpg` | hand taking **current-series** stone-grey notes (MAHATMA GANDHI microtext) from a box | ⚠ **this kills the cut's worst blocker with zero fetches.** ch2's first corpus figure sat on **demonetised pre-2016 notes**; `s11b` is the serial-checked CLEARED reference its replacement had to match, and it is now the replacement itself. **Do not re-fetch** |
| **s28** | 3.7 | **`assets-ch1/style-a/s7.jpg`** — NOT `final/s7.jpg` | vintage weighing scale with brass weights | ⚠⚠ **PATH CORRECTED 2026-08-08 — read this before fetching ch3.** The style-E rotation re-keyed ch1's filenames, so `final/s7.jpg` is now **the staircase**, and a ch3 run following the old wording literally would ship the staircase as the weighing scale with every check green (a photograph satisfies `image_per_scene` merely by loading). The scale survives only under `assets-ch1/style-a/`; the cut manifest is already repointed and carries its credit line. ALSO **VERIFY BEFORE PROMOTING:** 3.7's balance must put two clearly different weights in frame or it reads as a duplicate — moving old `s7` here does remove the duplicate the carry-forward feared, because its own beat no longer exists |

**DISCARDED — 8 files, all for a recorded reason:**

| old file | why it cannot come back |
|---|---|
| ch2 `s15.jpg` | **DEMONETISED pre-2016 ₹500 notes** under the video's first corpus figure. Named and forbidden; replaced by `s11b` above |
| ch2 `s11.jpg` | ~30 unsold clay gullaks at a pottery market under "SIP puts in, SWP takes out" — a market stall, not a mechanism |
| ch2 `s17.jpg` | a bare RJ45 lead under "the phone recharge and the home internet" — **neither subject present** |
| ch2 `s19.jpg` | a brickyard of hundreds of blocks under THE FIRST BRICK / "this is small" |
| ch2 `s18.jpg` | asserts a COUNT of twelve over uncountable bundles |
| ch2 `s16.jpg` | high-key graph paper that reads as a UI panel (ch1's failure repeated); already queued for re-source |
| ch2 `s9.jpg` | card index that grades to indistinct brown |
| ch2 `s10.jpg` | a circled calendar date — style E has no "a fixed date" beat at all, and the frame was sliced at the bottom edge |

**Net: 12 of 20 survive.** Three of the twelve took multiple fetch rounds to land, and two of them
(`s5`, `s11b`) each close a standing blocker by being reused rather than replaced.

### The grade decides the photograph — write the LIGHT, not the object

Enforced: `pipeline_check check assets --chapter <N>` fails any promoted image with source
**`YHIGH < 110`**. Every query in `manifest.json` therefore names the lighting.

> **⚠ The companion warmth rule — `mean R−B ≥ ~+40` on the raw — is RETIRED (2026-08-08).** It is
> unreachable and it cost this run's ch1 four fetch rounds. Measured on encoded frames:
> `encoded R−B = 0.0927 × source R−B − 6.43`, so only ~9% of a photograph's warmth reaches the
> screen under a fixed −6.43 from the layer stack; a source of **+73.53** renders at **+0.76**.
> Reaching +40 on screen would need a source near +500, which does not exist. **Warmth is chrome,
> not photograph** — `--bg` (`#0d1017`, R−B −10) is every scrim, the band and the far stop of
> `.field`, so raising `.field` opacity makes a chapter COLDER. **Do not reject a candidate on
> source R−B and never send a slot back twice for warmth.** No warmth requirement appears in any
> brief in this file.

1. **Never buy high-key stock.** A white-dominant subject cannot survive `brightness(.62)`; it
   lands as a flat charcoal slab. Ask for the subject **lit against a dark ground**. Three of
   ch1's seven backgrounds failed for exactly this.
2. **Replacing one white photo with another white photo re-breaks it.** When a frame reads grey,
   the fix is a differently-lit original, not a re-crop.
3. **When a slot fails twice on brightness, change the MATERIAL, not the adjective.** Enamel,
   glass, glazed ceramic, brass, polished steel and wet stone have a specular ceiling; matte
   paper, kraft, cardboard and unfinished wood do not. This cut's own `s5` is the proof (enamel
   plaque, YHIGH 203, after kraft measured dead twice), and it is why s8's stamped receipt is
   specified beside a **brass**-bodied stamp on dark wood.

### Overrides against the script's own `img:` cues

| scene | script cue | this storyboard | why |
|---|---|---|---|
| **s4** (1.4) | "the phone now face-up beside the glass, **notification glow**" | phone screen-up and **completely dark/off**; the notification is the Lottie | **Never a lit phone-screen photo as a background** — shipped undetected three times. A black-screen phone is APPROVED (fin-editor, en ch1 r1): the screen is the *darkest* object, carries nothing, and states the beat more plainly. Applied identically on s1, s4, s74, s75, which is what makes it a decision and not an exception |
| **s4** (1.4) | "ONE continuous zoom across 1.3 and 1.4" | **dissolve, not a hold** | `s3` is the reused chai-glass counter and contains no phone, so no crop of it can produce 1.4's frame. `s4` is a separate fetch on the same counter material (steel + wood, same light) so the place still reads as one place. **Declared, not accidental** |
| **s9** (2.1) | "a locked steel almirah with a small key in the lock" | the verified closed **iron strongbox** | reuse of a cleared file that makes the same statement (§10a) |
| **s52** (5.12) | "a printed search-results page on a desk" | same, with **no phone screen and no monitor in frame** | the never-a-screen rule; this is the most tempting violation in the cut because the frame is *about* what the internet shows |
| **s55** (5.15) | "a stapled research paper… beside a cup" | same, plus **no seal and no agency name legible** | `truth_bar`: never fabricate a source document. The citation lives in the `foot:` |
| **s75** (7.2) | "the same phone… (same object, new crop)" | a **separate fetch** of the same phone from the opposite side | s74 is face-down; a crop of it cannot produce a differently-oriented frame, and pointing at the same file twice is the reuse failure |
| **s80** (7.7) | "the 1.3 kitchen counter at full daylight (same object, new crop)" | a **separate fetch** — the counter and an **empty steel tumbler**, full daylight | ⚠ `run.json.chapters._carry_forward_from_ch1_assets`: *"s77's callback should rhyme with the chai GLASS, not the window."* Honoured. The rhyme is the tumbler; the file is new |

### The returning objects — a visual rhyme, never a reused file

The sound-off rule is **per line**: same object family, new photograph, and the difference must be
legible with the sound off.

| object | frames | what differs, and what must stay the same |
|---|---|---|
| **the tank** | s11 (2.3) · s12 (2.4) · s37 (4.7) · s38 (4.8) · s44 (5.4) · s45 (5.5) | **tap position alone says the beat**: the tank at rest → both taps in one frame → outlet running, level below the fill line → a quarter turn, a thin stream → wide open, level dropping past the low mark → empty and dry. The **plain steel body under workshop light** is the recognisable constant. ⚠ **Source all six from one set if at all possible.** Declared fallback: buy the wide tank at Pexels `large2x` and source the other five as tap/stream macros in the same material family — the tap carries the rhyme, not the tank's silhouette. **This is the one sourcing risk in the cut** and the en storyboard's D9 named it as the first thing to port back |
| **the container ladder** | s16 (2.8) · s22 (3.1) · s31 (4.1) · s58 (6.1) · s62 (6.5) | notes in a box → two cash boxes → a steel trunk → a bank locker → a safe door. **Each visibly bigger than the last** — this is the climb, and it replaces the en cut's drawn measure bar (§9c) |
| **the stamp** | s8 (1.8) · s27 (3.6) · s77 (7.4) | at rest on the ink pad beside one stamped receipt → mid-press, the percent mark just inked → five stamped receipts in a row. The condition planted, paid, and recapped: three states, three files |
| **the staircase** | s7 (1.7) · s21 (2.13) · s40 (4.10) · s61 (6.4) · s79 (7.6) | the lowest steps, the top out of frame → one brick at its foot → three worn treads → the top landing → three bricks side by side. Five photographs, five different statements |
| **the ledger** | s17/s18 · s23/s24 · s32/s32 · s59 · s63/s64 | **five different paper artefacts, one per rung** — a ruled ledger page, a cloth-bound register, a carbon-copy counterfoil, a spiral accounts notebook, a stamped page with a red ruled column. Within a rung, the monthly line is a derived crop of that rung's own source (§6b). **Never one page reused across five rungs** |
| **the morning** | s1 / s3 / s4 → s74 / s75 / s80 | ch7 returns to the same objects in **late-afternoon and full daylight, the day over** — distinct fetches, a callback, not a reuse |

### Standing rejections, restated so a re-fetch cannot lose them

- **No faces.** Hands and objects only — s16, s70, s78 are the only frames with a hand and every
  one is specified hands-only. It is a licence issue as much as a design one (Pixabay bars
  unflattering use of identifiable people).
- **Every frame is Indian or currency-neutral.** Sweep every photo for non-₹ currency, foreign
  signage, plugs, licence plates and vehicles before the build gate. **Currency must be
  CURRENT-SERIES Indian notes** — never demonetised pre-2016 notes, never prop money, **never a
  `$` anywhere, in any frame** (`hi_currency_framing` and `forbidden_currency`).
- **Nothing legible that is a fabricated source.** s10, s39, s48, s49, s53, s54, s55, s66, s71,
  s73 are photographed with **no legible title, figure or agency name**; every citation lives in
  the `foot:`, never in the photograph.
- **No readable brand marks** anywhere — s10's transaction form, s34's kirana counter and s60b's
  instalment receipt are all specified brand-free.
- **The densest scenes get the calmest backgrounds.** The two `art-forward` frames (s28, s67), the
  two cascades (s2, s6) and the four two-framing scenes are all routed to near-flat, low-key
  subjects. Density is managed by choosing a quieter image, **never** by dropping one.
- **The contact sheet cannot be trusted** — read every promoted file at full resolution, and
  **md5 the asset ledger: no image may repeat across videos or channels.** ⚠ The en cut of this
  same video is being sourced in parallel; a shared query can collapse to the same deterministic
  top hit. **Hash-check against `passive-income-number-en` specifically.**

### Resolution routing

`blockframe-9` is full-bleed at `inset:-8%` ⇒ ~**1.63×** on the long edge, and the Pixabay key
tops out at 1280px. Route to **Pexels `large2x` (1880px)**: every derived-crop SOURCE (**s17,
s23, s32, s34, s52, s57, s63, s70**, because a crop of a 1280px file is drawn at ~2×), plus
**s62** (the hero corpus), **s64** (its source s63, already listed) and **s81** (the CTA — the
last frame anyone looks at). Pixabay is fine everywhere else: under the grade plus 5% grain it
reads as soft focus.

Write `.src` prompts and `CREDITS.txt` for every file — the archive rule depends on it, and
**check_assets requires an attribution line per manifest key, so a REUSED file needs its old
credit line copied across too.**

### Concrete things the VO names that deliberately get NO cut-in

So the audit does not rediscover them: **1.2's** alarm, office call and work reminder (all three
are the chip row; the clock is the bg) · **1.6's** electricity, ration and rent (drawn as the
icon row — no photograph of them exists to buy) · **2.11's** recharge and internet (both
documents are *in* the s19 bg, overlapping, which is why the stmt can be type) · **3.4/3.5's**
electricity bill (bg and meter carry it across two frames) · **5.7–5.10's** post office (four
frames already walk the counter, the board, the form and the ceiling) · **6.9's** pay slip (one
held document is the beat) · **7.1–7.2's** phone (the callback is one object held on purpose;
cutting back to ch1's files would be the reuse failure).

**Two cut-ins, both because the VO names a second concrete thing the bg cannot hold:**

| scene | line | cut-in | anchored on |
|---|---|---|---|
| **s35** | 4.5 | `s35b.jpg` — milk packet and fresh vegetables | «दूध और सब्ज़ी» — the bg carries atta, dal, rice and oil; milk and vegetables are named and absent |
| **s60** | 6.3 | `s60b.jpg` — a two-wheeler instalment receipt with a scooter key | «बाइक की क़िस्त» — the bg is a rent receipt book; the EMI is the line's second half |

---

## 11. The ground temperature arc

`.field` carries a per-scene `--f1` two-stop ground at 38% (`.has-photo .field`). **Role scenes
deepen into their role colour; scenes with no role move only on the neutral warm↔cool axis**, so
no frame asserts a colour it has not earned. Values are in §7. **Push it harder than looks right**
— at document scale the arc reads almost flat and in the encode it is exactly right.

The ladder used (ported from attempt 1, which is the hi cut's own):

```
warm     #2d2214 (warmest)  #291f13  #241d15  #1f1e1c        pop-warm  #33200f
neutral  #1c2027  #1a1e24  #191f28  #101720 (cool-dark)
cool     #161f2b  #131f2c  #0e1c2e  #0c1a2c (coldest)
fund     #17291f → #1b3024 → #1d3a28 (deepest, once)
target   #2a2113 → #2e2411 → #372a0c (deepest, once)
warn     #2b1418 → #301519 → #38151a → #3b1219 (hottest, once)
```

**Three rules that are not columns:**

1. **A hold pair shares ONE ground** (s14/s15, s17/s18, s23/s24, s32/s33, s63/s64). A temperature
   step in the middle of a continuous zoom is visible and reads as a cut that is not happening.
   For the four ledger pairs that ground is the pair's closing `--fund` value — see §6b.
2. **The deepest value of each role is spent exactly once** — `#2d2214` on s35 (the whole ration
   list, the most domestic frame in the video), `#3b1219` on s45 (the tank empty), `#372a0c` on
   s55 (India's own research), `#1d3a28` on the s63/s64 hold (one shot, therefore one use).
3. **The coldest value `#0c1a2c` is spent once, on s54**, and it is a declared contradiction —
   see below.

Read as a curve, not a stripe:

**ch1** cool first light on the silent phone (`#161f2b`) → neutral as nothing switches on →
**warming through the deposit** (`#241d15`, held across s3 and s4 so the buzz sits inside one
temperature) → sobering to neutral at the plaque → **warmest in the chapter at the three bills**
(`#291f13`) → neutral-warm at the stair → cooling to `#191f28` as the condition is stated plainly.
No red anywhere in chapter 1: nothing has gone wrong yet.

**ch2** neutral opening → **amber as the tank and its two taps come under examination**
(`#2a2113` → `#2e2411`) → the working number declared and defended at `#2e2411` across the hold →
warm at the notes (`#241d15`, rung one is a domestic win, not a rate) → **green from the division
through the monthly answer** (`#17291f`, held across the pair) → `#1b3024` at the full twelve
months → back to warm at the first brick.

**ch3** neutral → green across the second rung's hold → warm and domestic through the May
argument (`#291f13`) → **amber at the rate held** (`#2a2113`, the stamp) → neutral at the balance
→ **the video's first red at 3.8** (`#2b1418`, the calmest red — the internet inflating a slow
fact, which is an irritation, not a danger) → neutral-warm resolve.

**ch4** neutral → green across the third rung's hold → warm through the kirana counter and **the
warmest frame in the video at the whole ration list** (`#2d2214`) → cooling to say it plainly →
**red at the honesty beat** (`#301519`, the money comes out of your own tank) → amber where the
answer is why the tap is small → cool paper at the tax line → amber at three rungs, one rate, and
straight into the **SHOVE**.

**ch5 carries both extremes and the one declared exception.**
Neutral at the crack → red at the wide tap → cool at STOP → `#38151a` as the capital comes out →
**`#3b1219` at 5.5, the hottest frame in the video**, where the tank is empty and the monthly
money stops → red at the warning → neutral through the post office → amber at the published rate,
its form and its roof → red at the internet's number → **then the cold event**:

> ⚠ **s53 (`#131f2c`) and s54 (`#0c1a2c`) run deep COOL grounds, and s54 is a `--warn` scene.**
> This is the only place in the cut where the ground contradicts the role, and it is **declared so
> a later pass cannot "fix" it**: cold is neutral, so it asserts nothing, and this is where the
> imported rule's floor drops out — built on another market's history, thirty years, no tax, no
> costs. *The drop is a temperature event before it is a number.* **s55 then jumps straight to
> `#372a0c`, the deepest amber in the video** — coldest frame to hottest amber, adjacent, where
> India's own research answers it. Precedent: japanese-money-methods ch2 s16.

Then `#38151a` at the failure edge and amber at the inflation that explains it.

**ch6 climbs home.** Neutral at rung four → `#1b3024` at its monthly figure → warm at the rent
receipt → **`#101720`, cool-dark and empty, at 6.4** — the held breath, the emptiest frame in the
chapter, straight into the second **SHOVE** → amber at the hero corpus (`#2a2113`: it is a rate
being applied, not a promise) → **`#1d3a28`, the deepest green in the video, across the s63→s64
hold** → neutral through the comparison and the pay slip → `#1b3024` where they meet → neutral at
the guard rail → **red for the imported rule and its cost** (`#301519` → `#38151a`) → neutral at
the definitional line → amber for both assumed growth columns.

**ch7 returns to the morning.** `#161f2b`, the same cool as s1 → neutral through the phone and the
ledger line → neutral-warm at the habit → `#241d15` at the test you can run yourself → **green at
where it started** (`#17291f`) → `#291f13`, the second-warmest frame in the video, on the counter
at full daylight → `#33200f`, the only pop-leaning ground, on the CTA.

**No ground cross-fade is implemented.** We cross-dissolve whole sections for 0.45s, which blends
both grounds already; adding the Claude Design animatic's ground melt double-fades.

---

## 12. Transitions and timing

`dissolve` (0.45s) is the default on every boundary. **Two** boundaries are `shove`, and they are
the only two real turns in the argument:

- **s40 → s41 (4.10 → 5.1)** at **250.645s (48.3%)** — out of the three-rung ladder and into the
  question that can break the whole calculation. The ladder has just been restated as one rate
  across three rungs; 5.1 says a rate can be wrong. That is a turn, not a continuation.
- **s61 → s62 (6.4 → 6.5)** at **390.038s (75.1%)** — the number held back since 1.5 arriving.
  6.4's frame carries no figure at all and 6.5 carries `₹1,00,00,000`; a dissolve would smuggle
  the payoff in as a continuation instead of announcing it.

**Five matched-frame holds** (§6b) — mechanically dissolves; what makes them holds is that each
pair is one photograph under one continuous zoom, with **no `transition` SFX at the joint**.

```
scene_duration = 0.25 (VO lead-in) + clip_duration + 0.55 (tail)   ← MEDIUM override
data-duration  = scene_duration + 0.45   (s1–s80; s81 bare)
audio_start    = scene_start + 0.25
root duration  = 519.331
```

`0.25 / 0.55` are `format.json tiers.medium`, **not** the `scene.*` 0.4 / 1.0 SHORT defaults.
Generated from `timing.json` — **never hand-edited.** The same numbers live in four places (the
`<section>`, the JS `S` map, the `<audio>` row, root `data-duration`); updating three of four
passes every check and ships a video whose animations fire against the old timeline. Per-scene
figures are the `start` / `dur` / `d-dur` columns of §7 and are not restated — one home per fact.

⚠ **`scene_start` is authoritative; never re-derive it by summing.** Eleven joints in this
`timing.json` are 1 ms off their predecessor's `start + duration` (s23, s46, s49, s55, s59, s60,
s62, s68, s70, s71, s72, s74, s79 — the file's own rounding). A build that sums forward instead of
reading `scene_start` accumulates them. The last scene ends at **519.330** against a `total` of
**519.331**; take the root duration from `total` and **do not back-solve s81** to close the
books — that is the exact failure `tools/chapter_project.py` asserts GAPS rather than totals to
catch.

**Chapter membership** (from the VO line id, `vo-<chapter>-<line>` — never a second map):
**ch1 s1–s8 · ch2 s9–s21 · ch3 s22–s30 · ch4 s31–s40 · ch5 s41–s57 · ch6 s58–s73 · ch7 s74–s81.**
Chapter starts: 0.000 · 42.475 · 124.007 · 185.149 · 250.645 · 363.954 · 475.158.

> **The failure mode to watch for at build.** Durations that sum to exactly 519.331 while every
> internal cut has drifted is what a re-timing produces. `tools/chapter_project.py` asserts
> **GAPS, not totals**, and `tools/cut_assemble.py` verifies every scene's `data-start`,
> `data-duration`, `data-track-index` and framings **individually**. Neither may be weakened.
> **A layout pass may not touch a duration. This file re-times nothing.**

---

## 13. What this file ports, and where it diverges

Attempt 1 (`storyboard-hi.md`, style A, 78 lines, Harsh) is **superseded in its entirety** and
this file overwrites it. `storyboard-en.md` is the finished sibling and the structural model.

**PORTED, on purpose** — this is what makes a fix travel between cuts and between chapters:

| ported | from |
|---|---|
| the element-ID scheme `s<n>-<part>` and every part name | attempt 1 §3, and the built ch1/ch2 projects |
| the `#sN-rate` mechanism (two forms, +1.10 before the number) **and its build assert** | attempt 1 §4 / en §4 |
| the four cue variants and the anchored/fixed split | attempt 1 §5 / en §5 |
| the deterministic focal size rule (112 / 88 / 76) | en §3 |
| the derived-crop continuous zoom as the answer to a `max_scene_seconds` breach | attempt 1 §6, **render-verified on this cut's own ch2** |
| the ground ladder hexes and the "deepest once" rule | attempt 1 §10 |
| the derived cue list and the `cues-tables.json` contract | en §2 |
| the retired warmth screen and the YHIGH ≥ 110 gate | en §10 / `knowledge/stock-photo-sourcing` |
| **the tank as a photographic spine** | **en D9, which named this as the first thing to port back. Done — six frames, §10** |
| the black-screen-phone amendment | en §10, fin-editor en ch1 r1 |
| the `s6` icon row and the `phone-notify-credit` Lottie | the built ch1, verbatim |

**DIVERGENT from `storyboard-en.md`, with a reason each:**

| # | diverges how | why |
|---|---|---|
| **D0** | **The chapter map cannot align.** en runs 81 lines / **6** chapters; hi runs 81 lines / **7**. Indices diverge from s9 onward and never re-converge | a rewrite with a different argument shape has a different chapter count. Deriving one map from the other would mis-cut four chapters — the japanese-money-methods lesson verbatim |
| **D1** | **No measure bar, and therefore no `-meas` / `-mlab` / `-mf` nodes** | the climb is carried **photographically** by the container ladder (§9c); a drawn bar over an already-escalating photograph is rule 8's depictive failure. This declines en's own back-port offer, with a reason |
| **D2** | ₹ / lakh / crore / SIP / SWP / PPF / POMIS / post office / Indian passbook only. **No `$`, no BLS, no S&P, no Bengen-as-authority, no US institution** — not in a string, not in a photograph | `market_rewrite_not_translation` + `hi_currency_framing`. **No frame may imply a conversion between the two cuts' figures** |
| **D3** | **The en cut's title word is BANNED here** and its whole chapter 5 has no hi analogue | `hi_currency_framing`. The live trap: the index's total-return measure is *defined* using that word, so 6.16 quotes only the shape, «क़रीब बारह परसेंट» |
| **D4** | **Not one anchored fraction is ported** (§5) | Amrut delivers at ~14.281 c/s against Brian's ~17.57, and Hindi puts the figure in a different clause position |
| **D5** | The corpus token list and the whole of §4 | hi asserts on ₹ tokens across **31** frames at 3.0% / 7.4% / 7.1% / 12% / 4%; en asserts on 8 `$` tokens across 14 frames at 4.0% / 3.11% / 1.08% |
| **D6** | The cut's one `.mega` is **`3.0%`** at s14 (2.6), 240px | en's is `ABOUT 1%`, a US index yield this cut cannot carry at all (D3). Both cuts put the RATE in the enormous slot, which is the shared thesis |
| **D7** | Shoves at **s40→s41** and **s61→s62** | both are turns in *this* argument. en's are s39→s40 and s58→s59; a seven-chapter cut has its hinges elsewhere by construction |
| **D8** | **Five holds here, three in en**, and four of the five are one device (the ledger spine, §6b) | the hi script's stepped arithmetic says *"the same ledger page, carried down"* at every rung. en's rungs do not |
| **D9** | **Four two-framing scenes vs en's one breach + two derived crops** | measured, not chosen: hi has four scenes past 9.0s (9.812 / 9.603 / 9.185 / 9.159) where en had one (10.596) |
| **D10** | **2 drawn proportions, 1 icon row, 1 Lottie** vs en's 7 drawn + 1 Lottie + 0 icons | this cut's argument is arithmetic that repeats, not a set of one-off proportions; and the icon row exists because a photograph of "three bills being paid quietly" cannot be bought. **This cut also has a `.stamp` component (s46) and en has none** |
| **D11** | **Seven photo overrides against the script's own `img:` cues** (§10), a different seven from en's eight | four are the never-a-screen rule, one a reuse of a cleared file, two a crop that cannot exist. **This list is not copyable in either direction** |
| **D12** | Music bed **`bed-resolve`** | chosen for *this* cut's argument (a habit and a ladder). en's is `bed-tension` because its thesis is a cost. The bed is per video, not per channel |
| **D13** | **12 reused photographs and 8 discarded ones** (§10a) | en had no superseded build to reuse from. This is the single largest saving in the run |

---

## 14. Open items

1. **None that block a build.** All four `max_scene_seconds` breaches are *resolved* here (§6a),
   not deferred: real derived crops, both framings declared, all four sums exact.
2. **The six tank frames are the one sourcing risk** (§10). Brief the fallback **with** the fetch,
   not after it: this run's ch1 lost three rounds to a window it could not buy, and the recorded
   lesson is that a later brief must **adjust rather than assume**.
3. **`s28` needs a look before promotion** — the reused balance still must show two clearly
   different weights, or it fails 3.7's own point (§10a).
4. **`s27` and `s65` clear `max_scene_seconds` by <0.1s** (§6c). Ruled: one framing each. **Neither
   line may be expanded or re-voiced without re-measuring.**
5. **Hash-check against `passive-income-number-en`** specifically, not only against shipped videos
   — the two cuts are being sourced in parallel off the same pools (§10).
6. **`pipeline_check check storyboard` was not run by this stage** — it has no Bash tool. The
   orchestrator must run it. **One thing it may legitimately fail on:** `stale_script_problems`
   compares the current `script-hi.md` hash against `run.json stages.fin-voice-hi.script_sha256`,
   and the script carries a post-voice in-place edit at 4.9 (fin-audit-hi-3 hedged *"gets less"*
   → *"may get less"*, +3 chars). If it fires, that is a **real finding about the 4.9 clip**, not
   about this storyboard — resolve it at fin-voice, not by editing this file.
7. **Bed length is NOT an open item** (§2). Recorded because both storyboards on
   japanese-money-methods raised it as a decision on 2026-08-01 and it never was one.

## Sign-off

- [x] Colour semantics table filled and consistent with every `colour:` cue in the script
- [x] `arch` / `ground` / `art` assigned on all 81 scenes (§7) — no blanks
- [x] `has-photo` + a real `.bg` on all 81 scenes; `photo_free_scene_ratio` = 0
- [x] No rail, no chapter title, no scene counter, no slide number, no rung count anywhere on screen
- [x] Every `start` / `dur` verbatim from `timing.json`; nothing re-timed
- [x] All 31 corpus / derived-income frames carry `#sN-rate` in the same frame (§4), asserted at build
- [x] The VO-only derived figure at 6.8 carries a real rate element (§4a) — the run's known blind spot
- [x] `--warn` tint aimed at the 10/12% and 4% tokens, never at the 3.0% comparator (§1b)
- [x] All four measured `max_scene_seconds` breaches carry two `data-framings`, sums exact (§6a)
- [x] Two shoves, both on real turns; five holds, none carrying a `transition` SFX
- [x] No `$`, no `/`, no `?`, and no banned payout word in any on-screen string
- [ ] No image hash reused from any prior video, either channel, **or the parallel en cut** — fin-assets to verify
- [ ] Creator approved (Gate ②) — date: __
