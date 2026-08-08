---
summary: What the claude-design MCP actually is, verified verb by verb — a design-system file store with a preview URL and two guidance prompts. No motion, no frame, no renderer. It cannot make a cut. What it CAN do is worth one thing to this pipeline, and this note says what and where.
updated: 2026-08-05
source: full 22-verb schema enumeration + a live end-to-end trial on japanese-money-methods ch2 (project a908654d, two draft renders), 2026-08-05
stage: evaluation complete — negative on the headline question, positive on one narrow use
---

# The claude-design MCP — what it is, and the one thing it is good for

Registered user-scope at `https://api.anthropic.com/v1/design/mcp`. The creator
asked for an honest evaluation against real video work: *"I want to find out what
the claude-design MCP can actually do for video work: structure, architecture,
layout, and animation… Report findings honestly, including 'it can't do this'."*
Test case: chapter 2 of japanese-money-methods, the vector cut from
[[design-vector-only-chapter]].

**The short version: it is a file store for HTML with a preview link. It has no
inference endpoint. There is nothing on the other side to ask.** Everything that
looks like design intelligence is two prompt files that the *calling* model reads
and executes locally. Do not reach for it to make, restructure or animate a cut.

## 1. What it actually does — all 22 verbs

Enumerated from the schemas, not inferred from behaviour. Every verb is gated
behind one consent grant (`/design consent`, interactive only — it cannot be
approved in a non-interactive permission mode, and until it is, *all 22 fail*,
including the read-only ones).

| Group | Verbs |
|---|---|
| Projects | `list_projects` `create_project` `get_project` |
| Files | `list_files` `read_file` `write_files` `copy_files` `delete_files` `finalize_plan` `create_support_js` |
| Preview | `render_preview` |
| Design context | `get_claude_design_prompt` `read_design_skill` `list_design_systems` |
| Collaboration | `list_comments` `ack_comments` `get_conversation` `put_conversation` `add_member` `remove_member` `update_member_role` `update_sharing` |

Output format is **files**. `write_files` takes `{path, data}` — arbitrary bytes —
and returns `{written, url, etags}`. The native format is `.dc.html`: a React-ish
component runtime (`<x-dc>` template + a `DCLogic` class + a server-written
`support.js`) that makes a page click-editable in the claude.ai editor. It has a
real optimistic-concurrency story (etags threaded as `if_match`, structured
conflict results) and a real consent boundary (`finalize_plan` returns a signed,
path-scoped or project-scoped token). That machinery is well built. It is
storage machinery.

**`render_preview` is a naming trap.** It renders nothing and returns no pixels —
just two URLs: a short-lived `serve_url` for your own headless browser, and a
durable `claude.ai/design` link for the user. Only the second may ever be shown
to a user; the first carries a project-scoped token.

## 2. Motion? Layout? Renderable? — the three answers, with evidence

**Motion: no.** There is no timeline, keyframe, easing, duration, sequence or
time concept in any of the 22 schemas. Not one verb accepts a time value. What
motion guidance exists lives in the prose of `get_claude_design_prompt` and
`read_design_skill`, and it is *UI* motion: "prioritize CSS-only solutions",
"one well-orchestrated page load with staggered reveals", "avoid infinite
decorative loops on slide content". That is hover states and slide entrances. It
is not choreography against a paused timeline, and it knows nothing about
seek-safety, which is the one property this repo's renderer actually requires.

**Layout for a fixed 1920x1080 frame: not as a verb, but yes in its guidance.**
No verb has a canvas, dimensions or a frame. But the deck section of the base
prompt is genuinely about fixed artboards: commit a type scale as CSS custom
properties *before* writing any slide, never below 24px at 1920x1080, reserve
structural bottom padding. That advice is sound and it transfers.

**Renderable: no — through the MCP.** ⚠️ **But the app can, and this is the one
place the schema-only reading was misleading.** See §3a: `claude.ai/design` ships
a starter animation engine whose stage owns
`data-om-exportable-video-with-duration-secs` and a `data-om-seek-to-time-frame`
listener — a frame-seeking **video exporter**, plus a host timeline UI whose trim
and speed gestures write back into the source JSON. None of that is reachable
from any of the 22 verbs, because it is host/UI machinery rather than API. So:
*the MCP cannot render; the product can.* An agent driving only the MCP will
never find this. Ours didn't, until the creator used the app directly.

**Three of its rules directly contradict this channel's work**, which is the
clearest proof it is not aimed at this domain: *"NEVER write out an SVG yourself
that's more complicated than a square, circle, diamond"*, *"For imagery, never
hand-draw SVGs; use subtly-striped SVG placeholders"*, *"Avoid drawing imagery
using SVG; use placeholders and ask for real materials."* The entire vector
chapter **is** hand-drawn SVG imagery. Followed literally, claude-design would
have replaced all eleven scenes with grey placeholder boxes.

## 3. The trial — where the architecture beat the hand-built cut, and where it didn't

Since it is a design-system host, it was used as one: the blockframe system and
the eleven scenes went into a project, the two skills were pulled, and the
restructure was written up as a spec (`Chapter 2 Architecture.dc.html`) and then
implemented as `index-claudedesign.html` and rendered twice.
**Say this plainly whenever this work is cited: the architecture is the calling
model's, produced under claude-design's guidance prompts and stored in its
project. The MCP generated none of it.**

Three moves came out of applying its guidance to the flat-cut problem:

1. **Four archetypes, not one.** `.stack` stops being the default. A/plate,
   B/figure (number off-centre, rule at the left margin, mechanism in a bottom
   band), C/ledger (hard vertical split, artefact full-height right), D/band
   (type under a full-width rule, mechanism owning the bottom two-thirds).
   Sequence `C D B C B B B C D D A`, holding B across s15-s17 because those three
   frames are one argument.
2. **The ground carries the argument's temperature.** `.field` gets a per-scene
   `--f1` two-stop ground; role scenes deepen into their role colour, no-role
   scenes move only on the neutral warm/cool axis so nothing asserts a colour it
   has not earned. s16 is the coldest frame in the chapter — the drop to about 1%
   is a temperature event before it is a number.
3. **Presence without a figure.** Faceless and vector-only, so presence arrives
   as *the trace* (s18's tick and s21's underline, hand-weighted, off-axis, drawn
   at speed) and *the threshold* (s11's noren).

**Beat the hand-built v3, by scene:**
- **s13 s15 s16 s17** — the four number scenes. B/figure with the left rule reads
  far more editorial than four identical centred columns, and it frees the whole
  bottom band for the mechanism. This is the clearest win.
- **s11 s14 s18** — C/ledger. s14's document and s18's form now run full height
  and are cropped by the frame edge, which is the difference between a real
  artefact and an icon of one.
- **Every scene, on temperature.** v3's eleven grounds are near-black and
  interchangeable; these are not. This is the defect the whole exercise existed
  to fix, and it is fixed.
- **s19** — the declared framing swap is finally real (see §4 below).

**Did not beat it:**
- **s12 (a feed) and s18 (a form)** are still the weakest frames. Architecture
  reduced the penalty; it did not remove it. [[design-vector-only-chapter]]'s
  rule stands unchanged: **numbers, proportions and mechanisms are better drawn;
  places, people and thresholds are worse drawn.**
- **s11 cost two full renders** and only worked after being *moved out* of the
  archetype the spec assigned it. That is the honest shape of the finding: the
  document was confidently wrong about the one scene the note had already
  flagged as hardest, and only the encode caught it.

## 3a. The chapter-1 animatic — the app writing code, and what to steal from it

**Creator, 2026-08-05.** Pasted the chapter-1 prompt section of `script-hi` into
the claude.ai/design chat. The app's agent wrote a working 57-second animated
previz: `Chapter 1 Animatic.dc.html` + `chapter1-animatic.jsx` (25 KB, hand-written)
+ `animations-v2.jsx` (61 KB, a Claude Design **starter** library pulled in by
`copy_starter_component`, not authored for this job).

**Provenance, so this is not mis-cited later.** Its header comment reads
*"Inherits the ch2 architecture: four archetypes (A plate / B figure / C ledger /
D band), a per-scene two-stop ground carrying the temperature arc, the
+0.30/+1.10/+1.90 cue ladder…"*. The agent read `Chapter 2 Architecture.dc.html`
out of the same project and applied it to a different chapter. That is a real
result — **the design system propagated across chapters without being restated** —
but it is inheritance, not independent invention of the same scheme.

### How it is built

A **scene table** drives everything: `window.OM_SCENES` is a JSON string, one row
per cut, carrying `dur`, `arch` (A/B/C/D), `head`, `stmt`, `vo[]`, an `img`
*brief*, `role`, ground `g` + previous ground `gp`, ken `k0`/`k1`, and continuity
fields `cont`/`ph`/`ps`/`pv`. A `LAYOUT` map turns `arch` into a plate rect, a
transform origin, and a type component. Motion is **pure functions of time** —
`MOTION.enter(t, at, d)` returns `{opacity, transform}` — with no timeline object
and no state. That is the same seek-safe contract HyperFrames enforces, reached
independently, and it is why porting between the two is mechanical rather than
conceptual.

### The five ideas worth taking (ranked)

1. **The Plate.** Art lives in an explicit rect with `overflow:hidden` and *its
   own* ken transform and origin, per archetype — not a full-bleed `.field`.
   This **structurally eliminates** the entire bug class of rule 6 in
   [[design-vector-only-chapter]]: art cannot be clipped by a window you forgot
   to compute, because the archetype declares the window. Strongest single idea.
2. **The scene table.** One JSON row per cut instead of a hand-written
   `<section>`. Retiming, reordering and archetype changes become data edits.
   `timing.json` already exists and is generated — this is its natural extension.
3. **Ground cross-fade.** `mix(gp, g, easeInOutSine(t/0.55))` interpolates the
   ground from the previous scene's colour over the first half-second. The
   restructured ch2 hard-switches at the cut; this is better and nearly free.
4. **Continuity as data** (`cont`/`ph`/`ps`/`pv`). One image across two lines
   continues the zoom *and* cross-fades the outgoing type — the firaun rule
   ([[../index]] memory: same image across lines = ONE continuous zoom) expressed
   as table fields rather than hand-wiring.
5. **The rail** — chapter title, `1.3 / 1.10` counter, ticks, role-coloured
   progress fill. Handsome and genuinely orienting on an 11-minute multi-chapter
   video. **A creative decision, not an automatic yes:** a progress rail can read
   as courseware, and these are faceless finance videos, not a lecture. Creator's call.

Free extra: a 45° `repeating-linear-gradient` hatch at 5% on the plate reads as
material and costs one line.

### 3b. The chapter-2 animatic — the same eleven scenes, both ways

The creator then had the app build **chapter 2** — the same eleven scenes as
`index-claudedesign.html`. A clean A/B, and it settles the provenance question.

**It is our system re-rendered, not a second opinion.** Its archetype sequence is
`C D B C B B B C D D A` — *identical* to the restructured cut, including
`s11 -> C`, which appears nowhere in the architecture spec (that spec says A) and
only in `OUTCOME.md`, written after two renders. Its grounds match ours scene for
scene, including the cold floor at 2.6 (`#0d1826` against our `#0e1c2e`). It read
both files. So it is not converging evidence for the design — it *is* the design.

**Where its execution beats ours, and these are worth porting:** the B/figure
number is far larger and hangs its footnote directly beneath, so the figure truly
owns the frame (ours is timid at 180px with a vertical rule); 2.7's two
to-scale bars sit directly under the text instead of in a separate Lottie stage;
2.8's column of checkboxes with one heavy tick beats our single large box; and
the ground **cross-fades** from the previous scene rather than hard-switching —
`2.1`'s `gp` is chapter *one*'s last ground, so the temperature carries across
the chapter boundary.

**⚠️ The trap — its timing is wrong in a way that looks right.** Its scene
durations sum to exactly **73.479s**, our locked total. Every internal cut is
still wrong: per-scene it runs `7 / 5.2 / 6.2 / 4.8 / 6.4 / 7.2 / 6.8 / 5.8 /
8 / 7.2 / 8.879` against our VO-locked `8.036 / 5.58 / 6.233 / 5.215 / 5.842 /
6.73 / 6.233 / 5.894 / 9.185 / 6.678 / 7.853`. Scene starts drift up to **1.86s**
against a 0.1s tolerance. The tell is the last scene: 8.879 versus our 7.853 —
it knew the total from the spec and **back-solved the final cut to close the
books**. A sum that matches is not a timing contract. Never take cut points from
an animatic; take them from `timing.json`, which is generated from the voice.

### What it is NOT

**It is an animatic, and that is the point.** Every scene's `img` is a *brief*
("a phone face-up on a kitchen counter at night, no face") shown on screen as an
amber `IMG 1.1` chip, and the Hindi VO is burned in as subtitles behind a `VO`
tag — both toggleable via `showVo` / `showBriefs` in the editor's Tweaks panel.
The motifs are deliberately diagrammatic stand-ins for photographs that do not
exist yet. There is no audio, and it loads three families from the Google Fonts
CDN, which is a render-time network fetch and forbidden here.

So it does not compete with a finished cut. **It fills a hole this pipeline
actually has:** we currently go storyboard -> source or generate every image ->
build -> render -> discover the staging was wrong. An animatic sits between
storyboard and assets and lets staging, pacing, temperature and type be approved
*before* anything is paid for. That is the most valuable thing in this file.

## 4. Three real bugs the trial found — all of which the shipped vector cut has

These are the most valuable output of the exercise and **none of them came from
claude-design** — they came from rendering and looking at a contact sheet. They
are drawing rules, so they live with the other drawing rules, as rules 5–7 of
[[design-vector-only-chapter]]: the `stroke-width` attribute is a no-op against
the CSS rule; the `ken` window is smaller than the viewBox; a scrolling group
needs a `clipPath`.

The one worth repeating here, because it is what an evaluation is for: the
`ken`-window bug means the edge-to-edge baseline that the previous trial added to
s19 **specifically so its declared `data-framings` swap would survive the contact
sheet** was drawn outside the visible area and has never been on screen. That
swap has been cosmetic since it was written. A design-system host cannot find
that. Only an encode can.

## 5. Where it fits in /finance-video — nowhere in the render path

**No `fin-*` agent should call this MCP as part of a run.** Every stage that
matters is blocked by the same three facts: no motion, no frame, no renderer.
`fin-build` writes the composition, `fin-render` encodes it, `fin-editor` and
`fin-ceo` read contact sheets — none of that is reachable through a file store.
Adding it to the pipeline would add a consent gate, network round-trips and a
second home for the design system, in exchange for nothing the run consumes.
That last point matters most: the design system already has exactly two homes,
`tools/scaffold/assets/blockframe.css` and [[design-finance-blockframe]], and
the two-home rule in `vault/CLAUDE.md` forbids a third.

**The two genuine uses, both outside the run:**

1. **A review surface.** It hosts a real URL, renders on a canvas, and takes
   pin-anchored comments that come back through `list_comments` with a
   `queued_for_claude` flag. This repo has nothing like it — contact sheets are
   JPEGs in a gitignored folder. If the creator wants to comment *on a specific
   element* of a proposed style rather than replying in chat, this is the tool.
2. **Previz / animatic, driven by the app rather than the MCP** (§3a). Paste a
   chapter's script section into the claude.ai/design chat and it writes a
   working animated previz in one shot. As a **thinking and approval tool before
   assets exist**, that is fast and genuinely good.

**HyperFrames vs Claude Design, for anything that ships: HyperFrames, and it is
not close.** Claude Design's exporter cannot mix eleven voice rows, cannot run
`loudnorm`, produces nothing `pipeline_check` or `check_build` can assert
against, cannot concat frame-exact with the neighbouring chapters, and pulls
fonts over the network at render time. The entire finance pipeline — timing
contract, QA, contact sheets, `archive_cut` — is HyperFrames-shaped. The correct
split is **Claude Design to decide, HyperFrames to deliver**, and the five ideas
in §3a should be ported into `tools/scaffold/` so the deciding and the delivering
speak the same language.

Its two skills are worth reading once and stealing from, and they are the reason
the archetype system exists: *"create a system up front — a layout per element
class, with intentional variety and rhythm"*, *"dominant colours with sharp
accents outperform timid, evenly-distributed palettes"*, *"asymmetry, overlap,
grid-breaking elements"*. Applied to eleven identical centred slides, those three
lines are the whole diagnosis. They are also free, static, and now quoted here —
so the note you are reading has already extracted most of the value the server
had to give.

## 5a. The port — both chapters rebuilt in HyperFrames (2026-08-05)

Creator: *"draft new videos the chapter one and the chapter two using same
designs, layout, animations using hyperframe."* Done. The archetype layer now has
ONE home — `tools/scaffold/assets/chapter-design.css`, copied into each chapter —
rather than a divergent copy per cut, which is the failure mode
[[finance-audit-2026-07-29/index]] traced to `fin-build` scaffolding by copying
the previous video. Two helpers were added to the shared `motion.js`: `span`
(scaleX between two fractions — the rail fill and the measure bar) and `plateKen`
(a push with EXPLICIT endpoints, so a zoom can continue across a cut).

- `studio/videos/japanese-money-methods-hi-ch1/index-claudedesign.html` —
  ten cuts, 55.909s. Sequence `A A C C D D B C D A`. `renders/CD-ch1.mp4` +
  `renders/SHEET-CD1.jpg`.
- `studio/videos/japanese-money-methods-hi-ch2/index-claudedesign.html` —
  eleven cuts, 73.479s, now carrying the rail and the bigger figure.
  `renders/CD-ch2.mp4` + `renders/SHEET-CD.jpg`.

**What the port taught, beyond what was visible in the animatic:**

1. **A plate is a LIFTED PANEL, not a clipped window.** Ported as a bare
   `overflow:hidden` rect first and chapter 1 rendered dead flat — every motif
   invisible, because dark art on the raw ground has nothing to read against.
   The animatic's plate carries its own base gradient and that is load-bearing,
   not decoration. Now `rgba(30,38,54,.50) -> rgba(13,16,23,.15)`: alpha, so the
   scene's ground temperature still shows through and the lift costs no colour.
2. **`breathe(dur)` rounds UP as often as down.** Asking for 4.5s yields 6.0s
   (`round(4.5/3) = 2` pairs), which ran chapter 1's timeline 0.758s past its
   root duration and left the lamp mid-swell on the chapter's last frame. Its own
   docstring only warns about rounding down ("ask for 4s and you get 3s"). Ask
   for a whole multiple of 3.
3. **The declared-framings rule finally has a clean proof.** Chapter 1's `s5`
   declares three framings and one item lands in each (envelope -> plates ->
   delivery bag); `s3` declares two and the second brings the power bill whose
   amount grows past the dashed box marking last time. Both read as different
   pictures at contact-sheet scale — which is the bar rule 4 of
   [[design-vector-only-chapter]] sets and which the shipped vector cut never met.
4. **Chapter 2 was deliberately NOT converted to plates.** Its eleven motifs are
   authored in full-frame coordinates and were tuned across two renders against
   the `ken` window; a coordinate remap of all of them is real regression risk
   for no visible gain. It takes the rail, the bigger figure and the hatch, and
   keeps the legacy field. Recorded in its header as owed, not forgotten.

**What was NOT taken, and why it matters most:** the animatic's timing. Both
chapters' `data-start` / `data-duration` / `data-framings` are verbatim from the
shipped `index.html`, which is generated from `timing.json`, which is measured
from the voice. See §3b for how convincingly wrong the animatic's version was.

## 6. What it cost

- **15 MCP round-trips** — 3 refused pre-consent, 12 successful (`create_project`,
  `finalize_plan`, `create_support_js`, 2x `write_files`, `render_preview`,
  `list_projects`, `list_design_systems`, 2x `read_design_skill`,
  `get_claude_design_prompt`, `get_project`).
- **~9,000 tokens** of input to read the base prompt plus both skills. That is
  the real price, and it is one-time — the durable content is quoted above.
- **Wall clock attributable to the MCP: a few minutes.** The expensive part was
  the work it does not do: two draft renders at 3m52 and 3m55, plus a headless
  frame harness.
- **Returned:** two prompt files, a hosted document, a preview URL.

**Verdict, in two halves — and the second half is a correction of the first.**

*The MCP* is a design-system file store: no motion, no frame, no renderer, no
inference endpoint. `render_preview` sounds like the render verb and is not.
Nothing in the 22 verbs will ever make a cut, and no `fin-*` agent should call it.

*The product* is more than its API. Driven from the app's own chat it wrote a
57-second animated previz with a scene table, four archetype layouts, a
temperature arc and pure-function-of-time motion — and its starter engine
documents a real frame-seeking video exporter. **A schema-only evaluation cannot
see any of that, and this note's first pass confidently said "no renderer" on
exactly that evidence.** The lesson generalises past this tool: enumerating an
API tells you what an agent can drive, not what a product can do.

What has not changed is where the value landed. The chapter got better because of
two draft renders and a contact sheet. The animatic is worth having because it
gets in front of the creator *before* assets are paid for — not because it
renders video better than the renderer we already have.

## Files

- `studio/videos/japanese-money-methods-hi-ch2/index-claudedesign.html` — the
  restructured cut. Scene ids, every `data-start`/`data-duration`/
  `data-framings`, the track 1/2 alternation, the eleven voice rows and every
  string are **verbatim from `index.html`** (asserted, not assumed), so it
  concatenates frame-exact and is directly comparable to both other cuts.
- `renders/CD-ch2.mp4` (17.7 MB, 73.5s) + `renders/SHEET-CD.jpg`.
- Claude Design project `a908654d-91f6-4ba9-b6e1-50043bf2e40c` —
  `Chapter 2 Architecture.dc.html` (the spec) and `OUTCOME.md` (where the spec
  was wrong). Nothing there is load-bearing; the repo is the source of truth.
- `index.html` is untouched and is still the shipped chapter.
