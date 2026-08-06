---
summary: The AI-enhance pass is now the LAST step of every thumbnail (creator rule 2026-08-06). HyperFrames renders the type and the layout; Nano Banana rebuilds the photograph and props around it. The technique that makes it safe is PLATE-ONLY — the model is told to preserve every letter pixel-for-pixel, because it garbles lettering and invents promises. Proven on japanese-money-methods, both cuts shipped.
updated: 2026-08-06
source: japanese-money-methods, two enhance rounds with the creator (2026-08-06) — one unconstrained, one plate-only
stage: adopted — permanent pipeline step, mechanics in .claude/agents/fin-package.md
---

# The thumbnail AI-enhance pass

**Standing creator rule, 2026-08-06:** *"From now on we always enhance the images
using AI. So first we build the thumbnail on our side with the text and the
image, and also you have to provide me the prompt for each thumbnail so I can
enhance that with Nano Banana / Google Flow."*

So a thumbnail is now **two artifacts**: the rendered PNG, and a paste-ready
enhance prompt shipped beside it in the publish pack. `fin-package` writes both.

## 1 · Why — what the AI pass actually buys

A HyperFrames build produces a clean, correct, **flat** tile: type over a graded
stock photograph with a scrim. It cannot produce depth, staged props, or a lit
scene. The creator's word for the pre-enhance build was **"sterile"**, and it was
accurate.

The enhance pass adds what the render cannot: cinematic depth of field, warm
practical lighting, and **culturally specific props that a stock search will
never hand you in one frame** — on this video, a maneki-neko, a bonsai in a
glazed pot and a fan of ₹500 notes on a wooden ledge, in a misty lantern-lit
post-town street. That combination does not exist as a stock photo. It does
exist as a prompt.

## 2 · The technique: PLATE-ONLY

**Ask the model to rebuild the photograph and props. Tell it not to touch the
type.** The prompt opens with an absolute rule naming every string that must
return byte-identical, and forbids new text anywhere in the image.

> Anything the viewer must **read** is HyperFrames' job.
> Anything they must **feel** is the model's.

This is not stylistic preference — it is the only way the pass is safe. See §3.

Only ask the model to render text when it is 1–3 short words, and prefer not to.

## 3 · The three failure modes, all observed on the first pass

The first enhance round was run without these constraints. All three appeared at
once, and every prompt since is written to prevent them.

**a) It garbles lettering.** `HARA HACHI BU` came back as **`LOKA HACHTFW`**;
`FUTURE SECURED` as **`FUTURE SCCHNED`**. A tile with broken words reads as
low-effort at exactly the moment you are asking for a click. Preserve the type
and this class disappears entirely — the second round returned every letter of
`MOTTAINAI · KAKEIBO · HARA HACHI BU`, `JAPAN KE 3 TARIKE` and `₹30,000 PE BHI`
intact.

**b) It invents promises the video does not make.** Unprompted, it added a
`FINANCIAL FREEDOM` card with `NO DEBT STRESS` · `EMERGENCY READY` ·
`FUTURE SECURED`. No finance cut on either channel may promise any of that —
@moneymavens101's own About says *"No jargon. No stock tips. No get-rich-quick
schemes"*, the packs are education-not-advice, and the video's actual ask is
*one page, one pen, fifteen minutes*. **The prompt must name the forbidden
promises explicitly**, because the model reaches for them on its own. A tile
promising financial freedom over a video that says "write four questions on
paper" is both a retention problem and a trust problem.

**c) It builds narrative collages that die at browse size.** The first pass
returned a left-to-right story — coin jar, bills list with red arrows, a
`BALANCE $0` receipt, a `SAVE FIRST` jar, an 80 % donut chart, a wooden divider
box, a checklist. Beautiful at 2752 px. **Roughly 60 % of the frame was mud at
320×180.** One hero group survives a browse row; a sequence does not.

## 4 · What every prompt must carry

1. **Preserve instruction** — "preserve every existing letter pixel-for-pixel;
   do not re-render, re-letter, restyle, translate, move or re-space ANY text",
   then list the exact strings and their colours. Plus: no new text, labels,
   signs, handwriting, numbers, kanji or captions anywhere.
2. **The region** — "rebuild only the right N % of the frame, behind and around
   the type", and "deep shadow on the [text] side so the column stays clean".
3. **The currency lock** — ₹ props on a `hi` cut, $ props on `en`. The render is
   held to this rule and the enhanced image inherits it. ⚠️ **US banknotes are
   the likeliest visual failure** — models render fake dollars with garbled
   serials and wrong portraits far more often than they botch rupees. Check note
   faces at 1:1; the fallback is "banknotes shown edge-on and partially fanned,
   faces not fully visible".
4. **The claim lock** — the enhanced image inherits `run.json.premise_correction`
   and Gate 2. Name the forbidden promises (§3b).
5. **Browse-size discipline** — "ONE hero group; no charts, pie graphs, receipts,
   bill lists, jars-and-arrows sequences, checklists, progress bars or
   infographics."
6. **The channel's standing visual rules** — no people, no faces, no hands
   (faceless is permanent); one continuous photoreal scene, not a collage, not
   CGI.
7. **Aspect** — "16:9, 1280×720". The model returns ~2752×1536 (1.79:1); resize
   before upload.

## 5 · After the pass

- **Re-measure on the RETURNED image, not the render.** It is a different
  picture. Downscale to 320×180 and assert the focal line still spans ≥40 % of
  frame width with a real right margin.
- Save as `thumbnail-<cut>-ai.png` beside the render and record which one is
  `chosen:`. ⚠️ On japanese-money-methods this was missed — the enhanced files
  stayed in the creator's Google Flow session, `i.ytimg.com` 404s while an upload
  is scheduled, and the archive therefore holds only the pre-enhance renders.
  **Get the file back into the repo before `archive_cut.py` runs.**
- The **prompt is the reproducing artifact** and lives in the publish pack, which
  is consistent with the archive's existing trade: prompts survive, generated
  assets do not, and a rebuild re-pays the generation.

## 5b · Second application — first-lakh-first-thousand (2026-08-06)

Run against a **published** pair, retroactively, on tiles built before this step
existed. It confirmed the technique transfers and added two rules.

**Everything transferred.** Both cuts came back with every string intact —
including the `₹` glyph, the two-colour sub-lines (white with a green span), and
the cream ink-box chip. Zero garbling, zero invented text, in one pass each. The
plate-only prompt is now proven on two videos, four tiles.

**New rule — a TONE constraint, and it is a content decision.** This video's
honest thesis is that the **first** lakh is slow (20 months) and only the tenth
is fast (7). A triumphant cash-pile would have argued with the script's own
point, so both prompts specified *"it must read as PATIENT, ORDINARY SAVING, not
wealth — small denominations, modest quantities, a domestic table. No overflowing
cash, no gold bars, no luxury, no glitter, no rays of light, no upward arrows."*
What came back was a worn brass **gullak** with four modest ascending coin stacks
and a few ₹10 notes, on a scratched wooden table in window light — exactly the
register the script argues in.

→ **Run the sound-off test on the PROMPT, not just on the returned image.** The
existing rule says a plate must not argue with its claim
(`format.json layout.image_relevance`); with a generated plate you can enforce
that *before* generation, and it is much cheaper there.

**New rule — physical stacks are allowed; charts are not.** "No charts, no
infographics" nearly excluded ascending coin stacks. It should not: a row of real
coin stacks is an *object* photographed, reads as accumulation instantly at
browse size, and carries no axis, label or number. The line to hold is
**physical props yes, data graphics no.**

**A culturally specific prop is the single biggest win available.** The gullak
does what no stock search in [[stock-photo-sourcing]] could deliver — that note
measures India-with-people stock at a ~20 % hit rate and prescribes an object-led
workaround. A named cultural object in a prompt sidesteps the whole problem.
Proven twice now: the maneki-neko on japanese-money-methods, the gullak here.

⚠️ **Unmeasured on this pair.** `12.5 MONTHS` now overlaps the jar in the -en
tile. It looks legible, but that is an eyeball on a downscaled paste — the
returned files are not on disk, so the ≥40 % assert has not been re-run. Measure
once the PNGs land.

## 5bb · Third application — credit-history (2026-08-06)

Six tiles, three videos, **zero garbled letters and zero invented promises.** The
technique is no longer provisional. This run added three things.

**The `chosen:` blocker has a cheap solution: ask for a screenshot.** See §5c route 2.

**Forbidding a prop outright beats constraining it.** §3c names US banknotes as the
likeliest failure. The en prompt did not ask for careful dollars — it said *"do NOT
render banknotes at all, cash is not part of this scene"* and gave the model a key fob
and a folder to carry the money idea instead. Nothing to garble, nothing to check at
1:1. **When a prop is both risky and inessential, delete it from the prompt rather than
qualifying it.** Same shape as the build-stage rule this very video produced — *a wrong
subject cannot be fixed by framing; delete the element.*

**⚠️ "No legible characters" is too weak an instruction for paper.** Both prompts carried
it. The hi file cover complied; the **en manila folder came back with a full page of
lorem-ipsum body copy** — no real word, but unmistakably *type* at 1:1. The model reads
the rule as "unreadable text is fine." It is harmless at browse size and both tiles
ship, but the phrasing to use from now on constrains the **surface**, not the legibility:

> *"Any paper is blank, or covered by the props, or so far out of focus that no line of
> type is resolvable. No blocks of body copy, no lines of lettering, no filler text."*

## 5c · BACKLOG — retro-enhance every published finance tile

Creator decision 2026-08-06: work back through the catalogue and write an enhance
prompt for every finance thumbnail already published, **one video at a time**.
Cross off here as each ships. All eight cuts are LIVE on both channels, so each
one is a thumbnail *swap* on an existing video — which also makes it a real CTR
test against a known baseline.

| video | tiles | enhance source | blocker |
|---|---|---|---|
| japanese-money-methods | 2 | — | ✅ **done** · enhanced PNGs not in repo |
| first-lakh-first-thousand | 2 | — | ✅ **done** · enhanced PNGs not in repo |
| emergency-fund | 2 | `src/thumbs/thumbnail-{hi,en}.png` | — |
| 50-30-20-rule | 2 | `src/thumbs/thumbnail-from-youtube-1280.png` | ⚠️ one tile only — recovered from the CDN, the build's own PNGs were never archived |
| needs-vs-wants | 2 | `src/thumbs/thumbnail-from-youtube-1280.png` | ⚠️ same |
| credit-history | 6 (v1/v2/v3 × 2) | `src/thumbs/thumbnail-{hi,en}-v2.png` | ✅ **done** 2026-08-06 (§5bb) · `chosen:` v2/v2 · enhanced PNGs not in repo, assert unrun |
| good-debt-vs-bad-debt | 6 | archive | 🔴 `chosen:` partly unfilled |
| pay-yourself-first | 7 (en has a v4) | archive | 🔴 `chosen:` unfilled on both |

**The blocker that matters:** the pre-2026-07-29 videos shipped **3–4 variants per
cut and their packs never recorded which one was uploaded.** You cannot enhance a
tile you cannot identify. Two ways out, in order:

1. **Pull the live thumbnail from the CDN** and match it against the archived
   variants. `https://i.ytimg.com/vi/<id>/maxresdefault.jpg`, falling back to
   `sddefault` then `hqdefault`. ⚠️ **Unreliable** — measured 2026-08-06:
   50-30-20-rule and needs-vs-wants returned 1280×720 (and were saved, since
   their own PNGs were never archived at all), emergency-fund only had a 640×480
   `sddefault`, and pay-yourself-first / credit-history / good-debt 404'd at every
   quality. A scheduled or restricted upload serves nothing.
2. **Ask the creator** which variant is live. Cheaper than guessing, and the
   answer should be written back into the pack's `chosen:` line — that field
   exists precisely so this question is never asked twice.

**Route 2 works, and the cheapest form of it is a screenshot.** 2026-08-06 the
creator pasted the two live credit-history tiles as browser screenshots. Both
matched an archived variant on sight — layout, every string, every colour — and
**v2/v2** went into both packs' `chosen:` lines in one pass, after six weeks of
that field surviving uploads unfilled. `i.ytimg.com` had 404'd on this exact
video. **A screenshot of the live tile beats every CDN route: it needs no public
reachability, works while an upload is scheduled, and is one action for the
creator.** Ask for the screenshot first, not the URL.

**Do not enhance a multi-variant video until its `chosen:` is filled.** Enhancing
the wrong variant produces a tile that does not match what is on YouTube.

## 6 · What this does NOT change

The render still has to be right first. The AI pass is an enhancement of a
correct tile, not a rescue of a wrong one — it cannot fix copy that names no
subject, a plate that argues with its claim, or a line that fails the ≥40 %
legibility assert. Every rule in `fin-package` §Thumbnail still applies to the
thing you hand the model.

Related: [[design-finance-blockframe]] · [[design-chapter-archetypes]] ·
[[evidence-discipline]] · [[../videos/japanese-money-methods/index]] ·
`.claude/agents/fin-package.md` §The AI-enhance handoff
