# 03 — Design system, visual style, and the sameness mechanism

Scope: layout, colour, type, frame structure, and the architecture-repetition mechanism.
Not covered here (other agents own them): script wording, motion timing, sound, image
sourcing, thumbnails.

Every claim is tagged `FACT` (verifiable from a file, a spec, a rendered artifact, or a
published policy) or `UNVALIDATED` (a belief about audience response — no analytics exist).

Corpus read: 10 shipped cuts under `vault/videos/*/src/{hi,en}/index.html`, plus
`tools/format.json`, `tools/pipeline_check.py`, `tools/scaffold/`,
`.claude/commands/finance-video.md`, `.claude/agents/fin-{build,script,audit,storyboard}.md`,
`vault/knowledge/design-finance-blockframe.md`, `design-techtooltester.md`, `channels.md`,
`vault/skills/hyperframes_production.md`, `vault/videos/credit-history/index.md`,
and the `run.json` of the three runs that have one.

---

## 1 · The documented system vs what shipped

### 1.1 The headline: there is no design *system*. There is a design *lineage*.

`FACT` — `.claude/agents/fin-build.md` step 1 instructs: *"For the composition itself, read
the newest archived `vault/videos/<slug>/src/{hi,en}/index.html` as the reference
implementation."* `tools/scaffold/` contains only `package.json`, `package-lock.json`,
`assets/fonts/NotoSansFinance-var.woff2`, `assets/js/gsap.min.js`, `assets/img/grain.png`.
**There is no shared stylesheet anywhere in the repo.** Every video's CSS is a hand-copy of
the previous video's CSS, with the `hi` cut copying from the previous `hi` and the `en` cut
from the previous `en`.

Three consequences, all measured:

**(a) Fixes propagate forward only, and only if the next builder notices.** In the
good-debt pair, the `en` cut discovered that `>` is missing from the font subset and
invented a `.gt` CSS chevron for it (`src/en/index.html:149-155`). The `hi` cut, built in
the same run from the same storyboard, typed `&gt;` literally into its 76px hero punch line
(`src/hi/index.html:293`). That cut is live at youtu.be/f-doI5d0NRk. Nothing back-fills.

**(b) The two channels' CSS have been diverging for five videos.** Defined-class
vocabularies, `good-debt-vs-bad-debt`:

| | `hi` only | `en` only | shared |
|---|---|---|---|
| classes | `.card .col .collabel .v-keep .v-cancel .v-down .billrow.total .mega .counter .head2 .glow .chip.target .stamp.fund` | `.claim .colcard .colhead .colsub .setup .gt .inkc` | `.chip .stamp .bill .billrow .cta .arrow .arr .tri .decision .foot .huge .kicker .sub .tag` |

`FACT` — `.decision` means two different components in the same run. In `hi` it is a flex
row of `LABEL → verdict-pill` (`src/hi/index.html:111-116`). In `en` it is a plain 40px
`max-width:1400px` paragraph (`src/en/index.html:122`). Same token name, two components,
one video.

**(c) Dead CSS accumulates.** `good-debt-vs-bad-debt/src/hi/index.html` defines and never
uses `.mega .counter .head2 .glow .chip.target .billrow.total .v-down`. `pay-yourself-first`
(both cuts) carries dead `.mega` and `.collabel`. `50-30-20-rule/src/hi` carries dead
`.arrow .glow .mega .needsc .segnum .segpct`.

`FACT` — `.mega` (290px, the top of the documented type ladder) is **defined in 8 of 10
shipped cuts and used in 4**, and has not been used since `needs-vs-wants`. The ladder's
top rung is now decoration.

### 1.2 Which documented rules are enforced by code — the complete list

`tools/pipeline_check.py::check_build` (lines 258–285) is the only code that ever looks at
a composition. It enforces exactly four things:

1. No `src`/`href` pointing at `http(s)://` — the determinism rule. **Enforced.**
2. Root `data-composition-id="main"` carries a `data-duration`. **Enforced.**
3. `len(<section> with data-start+data-duration) == len(timing.json["lines"])`. **Enforced.**
4. Root `data-duration` agrees with the last scene end and with `timing.json total`, ±0.5s. **Enforced.**

`check_voice` additionally enforces the §6 timing contract arithmetic
(`scene_duration = 0.4 + clip + 1.0`, contiguous cumulative `scene_start`) — that is real
and it is good.

**Everything else in the design doc and in `format.json`'s `layout` block is enforced by
nobody.** The following are written down and never checked by any script:

| Rule | Home | Enforced by |
|---|---|---|
| `type_ladder_px` (16 values) | format.json `layout` | nothing |
| `one_focal_per_scene` | format.json | fin-audit prose (#8), on the *script*, not the HTML |
| `cue_min_gap_seconds` 0.8 | format.json | fin-audit prose |
| `cascade` max 5 @ 0.6–0.7s | format.json | fin-audit prose |
| `first_cue_by_seconds` 0.5 | format.json | nothing |
| `max_simultaneous_elements` 6 | format.json | fin-storyboard prose |
| `max_chips_per_row` 3 | format.json | fin-audit prose |
| `max_chip_chars` 22 | format.json | fin-audit prose |
| `photo_free_scene_ratio` 0.0 | format.json | nothing |
| `keyword_images` | format.json | nothing |
| the grade `grayscale(.32) brightness(.62) contrast(1.05)` | design doc §1 | nothing |
| "one grade override per video max" | design doc §1 | nothing |
| grain 0.05 overlay | design doc §1 | nothing |
| the 4-layer scrim | design doc §1 | nothing |
| tint alpha 0.10–0.13 | design doc §2 | nothing |
| the colour tokens | format.json `colors` | nothing |
| `tabular-nums` on numerals | design doc §3 | nothing |
| the text-shadow | design doc §3 | nothing |
| `.row` has `flex-wrap: wrap` | design doc §4 | nothing |
| `tiers.<tier>.architecture` | format.json | **nothing — see §3** |
| `tiers.short.lines: 9` | format.json | nothing |

`format.json`'s `colors` block is read by **no code and no agent prompt** — the eight hex
values are re-typed by hand into every `:root` block. Same for `layout.type_ladder_px`,
which `fin-build.md` step 4 tells the agent to obey by reading, not by importing.

A rule nobody enforces is not a rule. By that standard the enforced design system is:
*a composition with N sections matching N VO lines, no network fetches, and correct timing
arithmetic.* Nothing about how it looks.

### 1.3 Measured divergences between doc and artifact

`FACT`, all verified by grep across the 10 cuts:

- **Scene padding drifts and nobody noticed**: `100px 140px` (50-30-20, both cuts),
  `120px 160px` (emergency-fund, both cuts), `110px 150px` (the other six). The doc says
  `110px 150px`.
- **`.bill` width**: doc §4 says 780px. Every shipped cut uses 820px.
- **`.foot` letter-spacing**: `1px` in good-debt-en, `2px` in good-debt-hi. Same run.
- **`.row { flex-wrap: wrap }`**: present in good-debt-hi, absent in good-debt-en. The doc
  §4 warns specifically about the wrap behaviour and it exists on only one of the two cuts.
- **Grade overrides**: the doc permits at most one per video. Four exist across the corpus —
  `emergency-fund/en` has **two** (`brightness(0.40)` on s5, `brightness(0.42)` on s6),
  `50-30-20/en` has `brightness(1.45)` on s8 (a 2.3× lift — that scene is not in the grade
  at all), `good-debt/hi` has `brightness(0.85)` on s8 (legitimate, documented in-file).
- **The colour tokens are not universal**: `50-30-20-rule` (both cuts) ships
  `--needs #38bdf8 / --wants #f59e0b / --save #22c55e` instead of `--fund/--target`, and
  introduces a **ninth colour** (`#38bdf8` sky blue) that appears in no other video and in
  no doc.
- **The scrim's `--tint` ladder shipped un-updated**: s2 carries a bare `<div class="scrim">`
  with no tint in both good-debt cuts, a leftover from when s2 was the photo-free rest beat.
  The doc's §2 table still lists s2/s7 as photo-free with a note that the practice was
  retired 2026-07-28.
- **The `.huge` nominal 112px is used once in ten cuts** (good-debt-en s1, and there it is
  *redundantly re-declared inline*). Every other `.huge` is inline-overridden to 96/88/76.
  All are on the ladder, so this is compliant — but "a fixed size ladder" describes
  intent, not practice. In practice `.huge` means "whatever fits".

### 1.4 A live, shipped rendering defect the system should have prevented

`FACT` — the vendored subset `tools/scaffold/assets/fonts/NotoSansFinance-var.woff2`
contains **97 codepoints**. Verified with fontTools:

```
ABSENT  U+003E  >     ABSENT  U+2192  →     ABSENT  U+25B6  ▶
PRESENT U+20B9  ₹     PRESENT U+0024  $     PRESENT U+00B7  ·
```

Scanning every shipped cut's text nodes against that cmap:

| Cut | Missing glyphs typed as literal characters |
|---|---|
| 50-30-20 hi | `→` `≈` `×` `▶` |
| 50-30-20 en | `→` `×` `▶` |
| emergency-fund hi | `→`×3 `×` `▶` |
| emergency-fund en | `→`×4 `×` `▶` |
| needs-vs-wants hi/en | *(clean)* |
| pay-yourself-first hi | *(clean)* |
| **pay-yourself-first en** | **`¢`** |
| **good-debt hi** | **`>` (76px hero) · `~` (40px `.sub`)** |
| good-debt en | *(clean)* |

The first four cuts are not a regression — they predate the self-hosted font (see below),
so their glyphs resolved from a system face. **The last two are.** They were built after
the subset landed, and every one of those characters renders from `system-ui` fallback:
different face, different metrics, and — critically — a fallback that will not be at
weight 900. `good-debt/hi` s7 is the video's single biggest punch line
(`₹88,614 INTEREST > ₹50,000 BORROWED`) and its `>` is a different typeface from the
numerals beside it. That cut is live.

The defect rate among subset-era cuts is **2 of 6, both in the two most recent videos** —
increasing, not decreasing, exactly as a copy-paste lineage predicts.

Neither `npm run check` nor `pipeline_check.py` looks at this.

### 1.5 The archive is not re-renderable at parity

`FACT` — 4 of 10 shipped cuts (`50-30-20-rule` and `emergency-fund`, both cuts each) have
**no `@font-face` at all**. Their `--font` is
`"Arial Black", "Helvetica Neue", "Segoe UI", system-ui, sans-serif` — they rendered in
whatever the render box happened to have installed. The design doc §3 and §8 both state
"no system-font dependency, no network fetch". That statement became true at
`needs-vs-wants` and is retroactively false for the first two videos.

Not an active defect (those two are live and archived), but it means those two videos
cannot be re-rendered at parity from their archived source, which is the whole premise of
the finished-video rule in `vault/CLAUDE.md`. Worth one line in their milestone notes.

---

## 2 · Is the look actually good?

Short answer: **the materials are good and the composition is not.** The grade, the
palette, the weight-900 type and the no-music restraint are a genuinely strong, restrained
register — better than most of the category. The frame composition is the single most
generic decision available and it is applied to 100% of frames in 100% of videos.

### 2.1 What is genuinely good

`FACT` (verifiable design properties, not taste):

- **The grade is the right idea and it works.** `grayscale(0.32)` is a smart number — enough
  desaturation to unify nine unrelated stock photos, not so much that a ₹500 note stops
  reading as money. This is the single best decision in the system and the doc is right to
  call it load-bearing.
- **One face, real weight axis, self-hosted, 32 KB, carrying ₹.** The fontTools verification
  that killed Archivo Black (no U+20B9) is exactly the right kind of engineering. Most
  channels in this category ship a Google-Fonts `<link>` and a faux-bold.
- **No music and no SFX** is a real differentiator, not a shortcut. Nearly every faceless
  finance channel runs a lo-fi bed. Silence + a competent read is more authoritative.
  `UNVALIDATED` that it retains better; `FACT` that it is uncommon.
- **`tabular-nums` on money figures.** Almost nobody does this. It is why the counters don't
  shimmy.
- **The figures are computed in-composition, not typed.** `good-debt/en:396-421` runs the
  amortization model in the page and formats with `Intl.NumberFormat("en-US")`. The screen
  cannot disagree with the maths. This is better than professional broadcast practice.

### 2.2 What is competent-but-generic

`FACT`, measured across all 10 cuts:

```
place-items: center                      10 / 10 cuts
text-align: center                       10 / 10 cuts
one vertical flex column (.stack)        10 / 10 cuts
full-bleed photo + scrim behind it       10 / 10 cuts, ~all scenes
sections per cut                          9 / 9 / 9 / 9 / 9 / 9 / 9 / 9 / 9 / 9
```

**Every frame of every video on both channels is a centre-aligned vertical column of text
over a darkened full-bleed photograph.** That is 108 scenes with one composition.

This is the default. It is what you get from `display:grid; place-items:center` — the
lowest-effort layout in CSS, and also the lowest-information one:

- Centred ragged-both-edges text has no reading anchor. The eye re-finds the left edge on
  every line. For a 40px `.sub` with two lines, that is a measurable cost.
- Type over photography always needs a scrim, a text-shadow, or both. This system uses
  **four scrim layers plus a two-part text-shadow on every text class** — six treatments
  stacked to make text legible on a surface that was never going to be a good ground for
  it. That is a lot of machinery spent recovering from one layout decision.
- Because the type must survive an unpredictable photo, it is locked to `--ink` near-white
  at weight 800–900 in almost every role. `--muted` is the only other text colour that ever
  appears in body roles. So the type system has, functionally, **two** states.
- Elements enter and leave the middle of the frame. Nothing is ever *placed*; things
  materialise where the last thing was. The `exit`-then-`pop` handoff (used in s1, s3, s5,
  s6, s7, s8 of good-debt) is the same gesture six times per video.

The scrim itself deserves a specific note. Layers 2–4 are:
`rgba(13,16,23,0.46)` + `rgba(13,16,23,0.14→0.58)` + a `0.40 → 0.10 → 0.52` vertical.
Compounded on top of `brightness(0.62)`, the centre of frame is sitting at roughly 20–25%
of the source photo's luminance. **The photograph is doing almost no work.** It is
expensive texture — a Pixabay round-trip, a retry ladder that cost 4–6 rounds per cut on
the last run, an md5 ledger, a licence file — to produce something a `radial-gradient`
would produce for free. The doc admits this ("they are texture, not information") without
following the admission to its conclusion.

`UNVALIDATED` — that any of this costs watch time. No analytics exist.
`FACT` — the frames are compositionally identical across 108 scenes; that is not a taste
claim, it is a grep result.

### 2.3 Against the 2026 field

Web research on the category returned mostly SEO content-marketing pages, so treat the
"what strong channels do" reading as directional. Two things came back that are solid:

`FACT` — **YouTube renamed its "repetitious content" policy to "inauthentic content"
effective 2025-07-15**, explicitly targeting content built with *"heavy templating or mass
reuse"* and *"generic or unoriginal templates that give the impression of mass production
without adding the creator's original insights."* Enforcement ranges from limited ad
earnings to channel termination, and reviewers assess **channel-level** patterns — themes,
top videos, metadata, overall content patterns. Sources:
[Social Media Today](https://www.socialmediatoday.com/news/youtube-clarifies-monetization-update-inauthentic-repeated-content/752892/) ·
[YouTube Help — channel monetization policies](https://support.google.com/youtube/answer/1311392?hl=en) ·
[Yahoo Finance](https://finance.yahoo.com/news/youtube-clarifies-changes-monetization-rules-194232823.html)

`vault/knowledge/channels.md` already flags this exposure and notes **Gate 2 has not been
run on either channel**. What is new here is that the sameness is now measurable in the
artifacts: 12 cuts, 9 scenes each, one composition, one runtime band, same six topics in
the same order on both channels. That is precisely the fact pattern the policy describes.

`UNVALIDATED` — whether these two specific channels would be actioned. Nobody can know
that without an enforcement event. But the risk is **not** an aesthetic opinion, and it is
the strongest available argument for the mechanism fix in §3, independent of retention.

`FACT` (directional, from category coverage) — the recommendation the category's own guides
converge on is *"vary formats and visual styles while maintaining a consistent brand
identity"*. Sources:
[virvid.ai — faceless retention 2026](https://virvid.ai/blog/faceless-youtube-algorithm-retention-2026) ·
[overseeros — faceless finance channels 2026](https://www.overseeros.com/blog/successful-faceless-finance-youtube-channels)
That is exactly the locked-vs-variable line drawn in §5, arrived at independently.

### 2.4 The verdict

The emperor is wearing good cloth, cut into one shirt, ten times.

Nothing in the token set needs replacing. The palette is right, the grade is right, the
face is right, the restraint is right. **The problem is that the only compositional idea in
the system is "centre it", and no amount of new components fixes that** — which is
demonstrably true, because five videos of bespoke components (`.meter/.bar/.leg` ·
`.coin/.block` · `.gap/.gaprow` · `.strikeable/.strikeline` · `.claim/.colcard`) produced
zero compositional variety. The variance budget has been spent, video after video, on the
layer that doesn't move the needle.

---

## 3 · THE CENTRAL PROBLEM — the mechanism fix

### 3.1 The diagnosis is right, and worse than recorded

`vault/videos/credit-history/index.md` is correct: *"the control is in the wrong place, not
unheard… `tier` is chosen in run.json BEFORE fin-script while the pack that warns is read
at upload AFTER the artifact exists."*

`FACT` — there is a **fourth** warning the note doesn't mention, and it is the decisive one.
`vault/videos/good-debt-vs-bad-debt/run.json` `owed[3]` reads verbatim:

```
"next finance cut MUST change architecture — 5th consecutive blockframe-9 on both
 channels (Gate-2 sameness crossed)"
```

That warning was **machine-readable, structured, and sitting in the pipeline's own state
file**. `credit-history/run.json` was then created three lines below it with
`"tier": "short"`. Grepping `tools/*.py` and `.claude/commands/` for readers of `owed`
returns nothing.

So the conclusion is sharper than "write the warning somewhere the pipeline reads": it was
already there. **Any fix that consists of recording something is dead on arrival. The fix
must be a refusal.**

`FACT` — the choice propagates like this, and nothing on the path compares it to history:

```
.claude/commands/finance-video.md §2.2  "Ask ONE question — the tier — with the default
                                         pre-filled: SHORT (default, target 2:45)"
        ↓  (default accepted, 6/6 runs)
run.json  {"tier": "short", "target_seconds": 165}
        ↓
format.json  tiers.short.architecture = "blockframe-9", lines = 9
        ↓
fin-script.md §"Format by tier"  "the proven 9-segment blockframe: hook · roadmap ·
                                  concept · rule · audit · action · the math ·
                                  do-this-today · recap+CTA"
        ↓
pipeline_check.check_build:280   asserts len(scenes) == len(timing.lines)   ← welds it shut
```

`FACT` — `tiers.<tier>.architecture` is read by **no code**. `pipeline_check.py` touches
`tiers` in exactly one place: `doctor()` line 351, for `disk_gb_per_pair`. The architecture
string is consumed only by `fin-script.md` as prose.

### 3.2 Where the gate must go — file, stage, check

**File: `tools/pipeline_check.py`, function `doctor(tier)` (line 327).**
**Stage: preflight, before intake.**

`doctor` is the correct home for four reasons, all structural:

1. It is invoked as **preflight step 1** in `.claude/commands/finance-video.md` §1 —
   `python3 tools/pipeline_check.py doctor --tier <tier>` — *before* the tier confirm
   block, *before* `run.json` exists, *before* any artifact and any spend.
2. The orchestrator already treats a `doctor` failure as terminal: *"Run in order; any
   failure stops the run with the failing command echoed."* **The enforcement plumbing
   already exists.** Only the predicate is missing.
3. `doctor` already takes `--tier` — the parameter that carries the architecture decision is
   already in its signature.
4. Its stated purpose, in its own docstring, is *"X-11: fail in five seconds with the fix
   command, not at minute 95."* A repeated architecture is exactly that class of failure.

Everywhere else is too late by construction:
`fin-script` — the tier is already fixed and the run is created.
`check_build` — the composition exists; ~90 minutes and ~18 ElevenLabs calls are spent.
`check_package` / the publish pack — where three warnings already died.

### 3.3 The change, concretely

**(a) `tools/format.json` — make architecture first-class and decoupled from tier.**

Today "vary the architecture" is only expressible as "change tier", and the nearest other
tier (`medium`) is 8:30 with a different build system (`per-line-chapters`, reference
`studio/videos/firaun-ka-anjaam/build.py`) and 3× the disk. If the only escape from the
gate is a 3× more expensive video, someone will use the override every time and we are
back to prose. So:

```json
"max_same_architecture": 2,
"architectures": {
  "blockframe-9":  { "tier": "short", "sections_per_line": 1, "frame": "centered-stack" },
  "ledger-rail":   { "tier": "short", "sections_per_line": 1, "frame": "left-rail" },
  "statement-card":{ "tier": "short", "sections_per_line": 1, "frame": "pinned-card" },
  "split-register":{ "tier": "short", "sections_per_line": 1, "frame": "62-38-split" },
  "per-line-chapters": { "tier": "medium", "sections_per_line": 1, "frame": "chapter" }
}
```
and `tiers.short.architecture` becomes `tiers.short.default_architecture`.
`run.json` gains a top-level `"architecture"` string, written at intake.

**(b) `tools/pipeline_check.py` — the predicate. ~15 lines, stdlib only.**

```python
def recent_architectures(n):
    """The last n runs' architecture, newest run.json first."""
    fmt = load_format()
    out = []
    for p in sorted(glob.glob(os.path.join(ROOT, "vault", "videos", "*", "run.json")),
                    key=os.path.getmtime, reverse=True):
        r = json.load(open(p, encoding="utf-8"))
        arch = r.get("architecture") or fmt["tiers"].get(
            r.get("tier", ""), {}).get("default_architecture")
        if arch:
            out.append((os.path.basename(os.path.dirname(p)), arch))
    return out[:n]
```

and inside `doctor()`, after the disk check:

```python
    n = fmt["max_same_architecture"]
    prev = recent_architectures(n)
    if len(prev) == n and all(a == arch for _, a in prev):
        problems.append(
            f"architecture '{arch}' ran the last {n} times "
            f"({', '.join(s for s, _ in prev)}) — pick a different architecture "
            f"(see format.json 'architectures'), or record "
            f"\"architecture_override\": \"<reason>\" in run.json")
```

`doctor` needs the chosen architecture, so add `--architecture` alongside the existing
`--tier` (defaulting to the tier's `default_architecture`), and change
`.claude/commands/finance-video.md` §1 to
`python3 tools/pipeline_check.py doctor --tier <tier> --architecture <arch>`.

**(c) The escape hatch, deliberately awkward.** `run.json` may carry
`"architecture_override": "<reason string>"`. The gate honours it, prints it, and it lands
in the milestone note. A repeat becomes a recorded decision instead of a default — which is
exactly what `credit-history/index.md` asks for ("make the next run's `tier` a deliberate
decision recorded in `run.json`").

**(d) The intake default must stop pre-filling the last answer.** `.claude/commands/
finance-video.md` §2.2 currently reads *"SHORT (default, target 2:45)"*. Change it to ask
for architecture explicitly and print the last two runs' architecture in the confirm block.
A default that has been accepted six times is not a default, it is a decision nobody makes.

**(e) One selftest assert**, in `_selftest()` alongside the existing currency-purity and
stale-script asserts — write two fake `run.json`s with the same architecture, assert
`doctor` reports it. This is the check that fails if the logic breaks.

**Total cost: ~25 lines across two files plus one prompt edit.** No new dependency, no new
tool, no new stage. The reason this hasn't been done is not cost.

### 3.4 The downstream lock that must be respected

`FACT` — `check_build` line 280–282 asserts `len(scenes) == len(timing.json["lines"])`, and
`check_voice` (lines 183–190) asserts `scene_duration == 0.4 + clip + 1.0` with strictly
contiguous cumulative starts. **Together these weld "one `<section>` per VO line, scenes
back-to-back" into the pipeline.**

Any alternative architecture that changes the scene:line ratio must also change both
functions, `fin-storyboard`, and `fin-build`. That is a genuinely expensive change.

**Therefore: all three alternatives below keep 1 `<section>` = 1 VO line, and vary what
happens inside the section.** This is not a compromise — the sameness is compositional, not
structural, so the cheap axis is also the effective one. `sections_per_line` is in the
`architectures` map above so the constraint is explicit when someone eventually wants to
break it.

---

## 4 · Three alternative visual architectures

All three reuse, unchanged: `--bg #0d1017`, `--panel`, `--ink`, `--muted`, `--fund`,
`--warn`, `--target`, `--pop`; FinanceSans at weights 800/900; the type ladder;
`grain.png` at 0.05 overlay; `grayscale(0.32) contrast(1.05)`; the 9-line VO; the timing
contract; the `ken` background move; all nine motion helpers.

They differ only in **where things sit in the frame** — which is the only axis that has
never varied.

---

### A · `ledger-rail` — break the centre

**The frame.** `.scene` becomes `display:grid; grid-template-columns: 300px 1fr;` with
`align-content:center`. The left 300px is a persistent rail: the scene index (`01`–`09`) in
`--muted` at 96px weight 200 — the *thin* end of the variable axis, which the system has
never used — above a vertical `--muted` hairline and the beat label (`HOOK`, `THE RULE`,
`THE MATH`) at 26px, tracked 4px. **The rail persists across the whole video**; only its
number and label change per scene. The content column is `text-align:left`, ragged right,
max-width 1200px.

**The photograph.** Stops being full-bleed. It occupies a right-hand panel from x=1180 to
x=1920, full height, with a hard vertical edge — no feather. The left 1180px is flat
`--bg`. Ken Burns survives inside the panel (it is just a smaller box). Because type now
sits on solid `#0d1017`, **the four-layer scrim and the two-part text-shadow both delete
entirely** — the panel gets one simple `linear-gradient(90deg, #0d1017, transparent 30%)`
so its left edge dissolves into the field.

**Why it reads different.** Left-aligned type has a reading anchor; the persistent rail
gives the video a spine and makes progress legible (viewers can see they're at 04 of 09);
the photo becomes a deliberate compositional element instead of wallpaper. And it looks
like an editorial page, not a slide.

**What it costs.** ~40 lines of CSS replacing ~30. Zero change to timing, scene count,
`pipeline_check`, `fin-storyboard`'s cue table, or the motion helpers. Element positions
change, so the max-density snapshot pass must re-run (it already runs every build).
Dense scenes get *more* room, not less, because the rail is narrower than the old
`150px + centred slack`. **~1 build cycle. The cheapest of the three.**

**Honest risk.** The rail is a strong device and will itself become a signature within two
videos — which is fine if it is one of a rotating set, and a new prison if it becomes the
next default.

---

### B · `statement-card` — the type never floats

**The frame.** The photograph goes back to full-bleed and gets *stronger*: drop the grade to
`brightness(0.50)`, push grain to 0.07, and **delete the scrim entirely** — the photo is
allowed to be a photograph. All type lives inside exactly **one** `--panel` card
(`background: rgba(22,27,37,0.94)`), pinned bottom-left at 120px margins, max-width 1250px,
with a 6px left edge in the scene's role colour (`--warn` / `--fund` / `--target` / `--pop`).
Radius 4px, not 18 — a document edge, not a pill.

**The rule that makes it work.** *One card on screen, always, and the card never moves.*
A new beat swaps the card's **contents** (crossfade the inner stack), so the frame has a
fixed anchor for 3 minutes while everything inside it changes. This deletes the system's
most-repeated gesture — `exit` the centre, `pop` a new thing into the centre — which
currently fires 6× per video.

**Why it reads different.** It is the opposite thesis to the current system: there, the
photo is suppressed so type can float anywhere; here, the photo is celebrated and type is
disciplined into one place. At thumbnail scale and in the first 3 seconds it is
unmistakably not the same video. It also gets the most out of the image budget the pipeline
already pays for (34–41 Pixabay fetches per cut on the last run).

**What it costs.** ~50 lines of CSS. The per-scene cue *times* transfer 1:1 from the
storyboard — only the selectors change (`#s5r1` → `.card .row1`). Two real costs:
(i) chip rows must become vertical lists or shorten, since the card is 1250px not 1620px;
(ii) the densest beats (s4 classifier, s5 mechanism, s7 math) need one element cut or a
second card-content phase — which the `one_focal_per_scene` rule already asks for and which
`fin-audit` already lints on the script. **~1.5 build cycles**, most of it on those three
beats.

**Honest risk.** A card over a bright photo is where `npm run check`'s contrast sampler is
most likely to produce false positives (the doc §9 already documents this for `.stamp`).
Budget one `known_benign` entry and hold the line on not lightening tokens.

---

### C · `split-register` — two honest surfaces

**The frame.** A hard horizontal split at 62/38. Top 62% (0–670px): the photograph under the
grade, and **nothing else on it, ever**. A 2px `--muted` hairline at y=670. Bottom 38%
(670–1080px): flat `--bg`, all type, left-aligned from x=150, tracking the same 300px-rail
idea as A but horizontal — beat label + scene index sit right-aligned at x=1770 on the same
baseline as the hairline.

**The one licensed violation:** the scene's single focal element (the `.huge` / the hero
number) may break the hairline and sit half in the photo — the only element in the system
permitted to cross a boundary, which is exactly what makes it read as focal without needing
a size change.

**Why it reads different.** It solves the type-over-photo problem by refusing to have one.
Both surfaces get to be good: the photo is finally viewable (no scrim, so the Pixabay spend
buys something), and the type is finally on a clean ground (no text-shadow, no scrim, so it
can drop to weight 700 and gain some tonal range instead of screaming at 900 all the time).
It is also the most "financial-broadcast" of the three without borrowing anyone's brand.

**What it costs.** ~35 lines of CSS and it **deletes** the four-layer scrim and every
text-shadow — a net reduction. No timing change, no scene-count change, no pipeline change.
**~1 build cycle**, tied with A for cheapest in code.

**Honest risk, and it's the real one.** 410px of type area is tight. `s4`'s two-column
classifier (2 cards × 3 tags), `s5`'s three mechanism rows + focal, and `s7`'s three bill
rows + setup + footnote **will not fit** in one phase. Those three beats must split into two
card-content phases each — which changes the storyboard, not just the CSS. So C is the
cheapest CSS and the most expensive storyboard. If the goal is one cheap experiment,
run A or B first; if the goal is the best-looking system, C is it.

---

### The free fourth option (not mine to own, but it costs zero design work)

Drop `s2` (roadmap) and `s9`'s recap chips. Both are pure bookends carrying no information —
s2 announces what s3–s8 will say, s9 repeats it. That is 7 scenes, ~30–35 seconds shorter,
and it moves the runtime **out of the 2:46–2:59 band that five of six videos sit in**. The
vault already proposes this (`credit-history/index.md`, "the same short tier with the
roadmap and recap bookends dropped"). It is a script/`fin-script` change with **zero** CSS
cost, and it composes with any of A/B/C. If only one thing ships, ship this and A together.

---

## 5 · Locked forever vs varied per video

Right now the line is drawn in exactly the wrong place: **the materials drift and the
composition is frozen.** Padding drifts (100/110/120), the grade gets overridden four times,
one video introduces a ninth colour and a system-font stack — while 108 of 108 scenes use
the same layout. Invert it.

### THE BRAND — never varies, enforced by a shared stylesheet

| Locked | Why |
|---|---|
| `--bg #0d1017`, `--ink #f5f3ec`, `--muted #98a2b3`, `--panel #161b25` | The ground. Recognisable in a 3-second scroll-past. |
| FinanceSans (Noto subset), weight axis 100–900 | One face, forever. No second family, no fallback stack in a shipped cut. |
| `grayscale(0.32) contrast(1.05)` | The desaturation *is* the signature — the one thing that makes nine stock photos one film. |
| Grain `0.05`, `mix-blend-mode: overlay` | Cheap, consistent, invisible until it's missing. |
| No music, no SFX | A real differentiator in this category. Keep it. |
| `--fund` green = the kept/safe thing · `--warn` red = the loss | See §7 — I would narrow the doc here. |
| The `--pop` CTA block closing every video | Plus the wordmark, §6. |
| `tabular-nums` on every money figure | Non-negotiable, currently unenforced. |
| Brightness matched **per image**, not per system | See §7. |

### THE VARIABLE — should change per video, and currently doesn't

| Variable | Current state |
|---|---|
| **Frame composition** (centered / rail / card / split) | **Frozen at "centered", 108/108 scenes. This is the one that must vary.** |
| Scene count and beat order | Frozen at 9, and at one beat order, 12/12 cuts |
| Runtime | Frozen — 5 of 6 inside a 13-second band |
| Which accent leads the video | Effectively frozen — red leads nearly every hook |
| How much frame the photo occupies | Frozen at 100% |
| Scrim / no scrim, shadow / no shadow | Frozen at "always both" |
| The tint ladder | Copy-pasted, including a stale un-tinted s2 |
| The component set | Varies — but **per cut**, by accident, which is the worst case. It should vary **per video**, identically across the pair. |

**The rule I would write into the doc, replacing "everything is locked":**

> Materials are brand; composition is variable. A viewer must recognise the channel from a
> single frame's colour, grade and type — and must not be able to predict its layout from
> the last video. The architecture named in `run.json` may not match either of the previous
> two runs.

`UNVALIDATED` — that this improves retention or CTR. No analytics.
`FACT` — it is the pattern the category's own guidance and YouTube's inauthentic-content
policy both point at, and it is enforceable today at zero content risk.

---

## 6 · The missing brand mark

`FACT` — `vault/knowledge/channels.md` D/E lists neither a logo nor a wordmark for
@cashguruguides or @moneymavens101. `design-finance-blockframe.md` §4 records the
consequence: *"No logo outro. Neither finance channel has a brand mark yet — the video
closes on the `.cta` block. Build the wordmarks before reinstating the standing logo rule."*
Meanwhile TechToolTester has a **standing rule** that every video ends on logo + SUBSCRIBE,
with assets in `studio/library/brand/` (`design-techtooltester.md` §Outro,
`hyperframes_production.md` §4).

So the finance channels close on an orange block reading `▶ SUBSCRIBE` — and on four of the
ten shipped cuts that `▶` is a system-font fallback glyph (§1.4).

### The minimum worth building — three things, all typographic

**1 · A wordmark, not a logo.** The channel name set in FinanceSans at weight 900, tracked
+6px, in `--ink` on `--bg`. `CASHGURU` / `GUIDES` stacked on two lines with the second in
`--pop`; `MONEY` / `MAVENS` the same. No icon, no glyph, no illustration — an icon is the
expensive part and it buys nothing a wordmark doesn't at 1920×1080.
**Cost: ~30 minutes. Zero new assets.** The font is already vendored; Noto is OFL, so
commercial use and modification are clear. Two `<div>`s.

**2 · A corner bug on every scene.** The wordmark at 22px, `--muted`, `opacity: 0.45`,
bottom-right at 60px margins, present in all nine scenes. This is what makes nine unrelated
photographs read as one channel, and what makes a scraped/re-uploaded clip traceable.
**Cost: 4 lines of CSS in the shared stylesheet — once, for every future video.**

**3 · An end card inside s9.** Do **not** add a tenth `<section>` — that breaks
`check_build`'s `scenes == lines` assertion (§3.4). Put it inside s9 as an overlay that
`pop`s in at `S.s9 + duration − 3.0`: wordmark at 120px above the existing `--pop`
subscribe pill, everything else `exit`ed. **Cost: ~10 lines of CSS + 3 timeline calls.**

**4 · The channel avatar + banner, free.** Export the wordmark from the same HTML with
headless Chrome — the repo already does exactly this for thumbnails
(`vault/videos/*/src/thumbs/index.html` are HTML→PNG projects). Avatar = the first two
letters in `--pop` on `--bg`, 800×800. Banner = the wordmark on `--bg` with one graded
photo bled off the right edge, 2560×1440.
**Cost: one 60-line HTML file per channel, reusing the thumbs recipe.**

### Total honest cost

**1–2 hours, producing: one CSS block in `tools/scaffold/assets/css/blockframe.css`, two
wordmark HTML files, four exported PNGs.** No designer, no Canva, no new dependency, no new
font licence, no ongoing cost per video (the bug and end card come free with the shared
stylesheet).

What is explicitly **not** worth building: an icon/symbol mark, a mascot, a second typeface,
a colour outside the existing eight, an animated logo sting. Every one of those is a
multi-hour decision that a wordmark makes unnecessary at this stage, and a sting would break
the no-SFX rule that is currently a differentiator.

`UNVALIDATED` — that a brand mark measurably affects subscriptions or recall.
`FACT` — it is the cheapest unbuilt item in the entire system, it is already documented as
owed in two places, and both alternatives (a) and (b) in §4 need a place to put it anyway.

---

## 7 · Contradictions with what the vault currently documents

Listed most to least consequential. Each is something a build agent reading the vault today
would get wrong.

**1 · "A single grade" is documented as load-bearing; it is not enforced and it has been
broken four times.** `design-finance-blockframe.md` §1: *"A per-scene `filter:` override is
permitted only for a near-black texture… and **never more than once per video**."*
`emergency-fund/en` has two (`brightness(0.40)` s5, `brightness(0.42)` s6);
`50-30-20/en` has a `brightness(1.45)` — a 2.3× lift that removes that scene from the grade
entirely. Nothing checks it.
Worse, the doc's own model is wrong: `hyperframes_production.md` §6 (2026-07-27) records
the correct rule — *"A swapped stock photo breaks the grade… Match brightness **per image**
(inline `filter:` override)"* — which is the opposite of "one override per video". **A
single global brightness cannot be right across nine photographs with different exposure.**
The grade should lock `grayscale` and `contrast` (the signature) and treat `brightness` as a
per-image calibration with a target measured luminance. The two notes currently contradict
each other and the artifacts follow neither.

**2 · "The design system" implies a shared implementation. There isn't one.**
`design-finance-blockframe.md` §4 lists components (`.track2/.fill2/.ticks`, `.statstrip`,
`.billrow.total`, `.decision` as a verdict row) that **do not exist** in the most recent
`en` cut, which invented `.claim/.colcard/.colhead/.colsub/.setup/.gt` instead. §4 documents
`needs-vs-wants`, which is three videos stale. The doc should either be re-scoped to
*tokens + rules only* (deleting §4's component inventory) or — the lazy correct fix — the
components should move into `tools/scaffold/assets/css/blockframe.css`, which is a
git-tracked directory that already exists and already ships the font, gsap and grain. One
file makes the doc true, kills the dead-CSS drift, back-fills the glyph shims to both
channels, and makes `--fund`/`--target` universal.

**3 · "`.mega` 290px is the top of the ladder."** It is unused since `needs-vs-wants` and
dead-declared in three later cuts. `.huge`'s nominal 112px is used exactly once in ten cuts.
The real ladder in practice is 96/88/76/54/50/46/44/40/32/30/28/26. Either use the top rungs
or delete them — a ladder whose top two rungs are decorative teaches a build agent the wrong
thing about the system's range.

**4 · "No system-font dependency" (§3, §8) is retroactively false for four shipped cuts.**
`50-30-20-rule` and `emergency-fund` (both cuts each) have no `@font-face` and run
`"Arial Black", "Helvetica Neue", "Segoe UI", system-ui`. They are archived under the
finished-video rule as *reproducible*; they are not reproducible at parity. One line in each
milestone note fixes the record.

**5 · "Semantics are per-video, derived from the thesis — not a channel rule" (§2).**
I would narrow this. Colour is one of the four or five things a viewer can recognise a
channel by, and the doc already documents the failure mode: `needs-vs-wants` inverted the
scheme so red meant only "the leak", and the doc has to spend a paragraph warning the next
video not to copy the inversion. Green = the kept/safe thing and red = the loss should be
**channel-locked**; `--target` amber remains the free per-video variable for "the thing
under examination". This costs one line of expressiveness and buys a colour language that
means the same thing across 12 videos.

**6 · The vault's sameness diagnosis is complete but stops one step short.**
`credit-history/index.md` names three written warnings. There were **four** — the fourth was
structured JSON inside `good-debt-vs-bad-debt/run.json`'s `owed` array, read by no code.
That strengthens the note's own conclusion: the fix cannot be a better recording location.
It must be a refusal at preflight (§3.2).

**7 · `format.json` is described as "the single machine-readable home for finance-pipeline
constants". Most of it is read by no machine.** The `colors` block (8 values) and
`layout.type_ladder_px` (16 values) are re-typed by hand into every composition;
`tiers.<tier>.architecture` is read by nothing; nine of the twelve `layout` constants are
read only as prose by two agent prompts. The `_comment` field's claim is aspirational. A
shared stylesheet generated from — or simply co-located with — these values would make it
true; until then the file's authority is overstated and drift is invisible.

---

## 8 · The five highest-leverage changes

Ordered by leverage per unit cost. Every one is a small, single-file diff.

**1 · `[FACT]` Gate the architecture at preflight — `pipeline_check.py::doctor()`.**
*Why:* four warnings failed because every one of them recorded rather than refused; `doctor`
already runs before intake, already takes `--tier`, and the orchestrator already treats its
failure as terminal, so only the predicate is missing.
*Cost:* ~25 lines across `tools/pipeline_check.py` + `tools/format.json` (`architectures`
map, `max_same_architecture: 2`), one line in `.claude/commands/finance-video.md` §1, one
selftest assert.
*Owner file:* `tools/pipeline_check.py`.

**2 · `[FACT]` Move the design system into `tools/scaffold/assets/css/blockframe.css`.**
*Why:* there is no shared stylesheet, so `fin-build` copies the previous cut's CSS — which
is why the `hi` and `en` channels have been diverging for five videos, why `.decision` means
two different components in one run, why dead CSS accumulates, and why the `en` cut's `.gt`
fix never reached the `hi` cut that shipped a fallback `>` in its 76px hero. The scaffold
directory is git-tracked, already ships the font/gsap/grain, and `fin-build.md` step 1
already copies from it.
*Cost:* one new file (~250 lines, extracted from the current best cut), a two-line edit to
`fin-build.md` step 1, `<link>` in place of a 150-line `<style>`. One build cycle to prove.
*Owner file:* `tools/scaffold/assets/css/blockframe.css` (new).

**3 · `[FACT]` Ship one alternative frame architecture — `ledger-rail` (§4A) or
`split-register` (§4C).**
*Why:* 108 of 108 shipped scenes are a centred column over a graded photo; five videos of
bespoke components produced zero compositional variety, so the variance budget is being
spent on the layer that doesn't move. Both alternatives reuse every token, keep 1 section =
1 VO line, need no `pipeline_check` change, and `split-register` **deletes** the four-layer
scrim and every text-shadow.
*Cost:* ~35–40 lines of CSS, ~1 build cycle. `split-register` additionally costs a
storyboard rework on the three dense beats (s4/s5/s7).
*Owner file:* `tools/scaffold/assets/css/blockframe.css` + `vault/knowledge/design-finance-blockframe.md`.

**4 · `[FACT]` Add a font-subset glyph check to `check_build`.**
*Why:* the vendored subset is 97 codepoints and `>` `→` `▶` `×` `≈` `~` `¢` are all absent.
Six of ten shipped cuts type at least one of them literally; **both post-subset regressions
are in the two most recent videos**, including the 76px hero line of a live @cashguruguides
upload. Neither `npm run check` nor `pipeline_check` looks at it.
*Cost:* commit `tools/scaffold/assets/fonts/subset.txt` (the cmap, dumped once) + ~8 lines
in `check_build` scanning text nodes against it. Stdlib only, no fontTools dependency at
check time. Allow-list, not blocklist — correct when the font changes.
*Owner file:* `tools/pipeline_check.py`.

**5 · `[FACT]` Build the two wordmarks (§6).**
*Why:* it is the cheapest unbuilt item in the system, it is already recorded as owed in
`design-finance-blockframe.md` §4 and `channels.md` D/E, TechToolTester has had a standing
logo-outro rule since 2026-07-07, and both alternative architectures need somewhere to put a
mark anyway. The videos currently close on a bare orange block whose `▶` is a fallback glyph
on four cuts.
*Cost:* ~1–2 hours total. One CSS block (corner bug + end card, free forever once in the
shared stylesheet), two wordmark HTML files, four PNGs exported with the existing
`src/thumbs/` headless-Chrome recipe. No icon, no second typeface, no new licence.
*Owner file:* `tools/scaffold/assets/css/blockframe.css` + two new files under
`studio/library/brand/` (the directory TechToolTester already uses).

---

### Runner-up, worth one line

`[UNVALIDATED]` Drop the roadmap (s2) and recap (s9) bookends → 7 scenes, ~30s shorter, and
the runtime leaves the 2:46–2:59 band that five of six videos occupy. **Zero design cost**
— it's a `fin-script` change — and it composes with any of the three architectures. The
vault already proposes it. If exactly one thing ships this week, ship this plus #1.

---

## Appendix — verification commands

```bash
# every frame in every cut is a centred column (10/10):
grep -c 'place-items: center' vault/videos/*/src/{hi,en}/index.html

# glyphs missing from the 97-codepoint subset, per cut:
venv/bin/python -c "from fontTools.ttLib import TTFont; f=TTFont('tools/scaffold/assets/fonts/NotoSansFinance-var.woff2'); cm=set(); [cm.update(t.cmap.keys()) for t in f['cmap'].tables]; print(len(cm), [hex(c) for c in (0x3E,0x2192,0x25B6) if c not in cm])"

# the fourth warning, in machine-readable form, read by nobody:
python3 -c "import json;print(json.load(open('vault/videos/good-debt-vs-bad-debt/run.json'))['owed'][3])"
grep -rn "owed" tools/*.py .claude/commands/   # → no readers

# the only code that ever inspects a composition:
sed -n '258,285p' tools/pipeline_check.py

# the scene:line weld that constrains any new architecture:
sed -n '280,282p' tools/pipeline_check.py
```
