# fin-storyboard · japanese-money-methods · cut hi · attempt 1

**Date:** 2026-08-01 · **Tier:** LONG · **Architecture:** `ledger-rail` (run.json)
**Inputs read:** `vault/CLAUDE.md` · `tools/format.json` · `tools/audio/kit.json` ·
`vault/knowledge/design-finance-blockframe.md` (the dark system — `design-techtooltester`
deliberately NOT read) · `vault/knowledge/finance-audit-2026-07-29/03-design.md` §4A ·
`vault/templates/storyboard-template-finance.md` · `vault/videos/japanese-money-methods/script-hi.md`
· `vault/videos/japanese-money-methods/run.json` ·
`studio/videos/japanese-money-methods-hi/assets/voice/timing.json` (measured, 659.709s, 92 lines)

**Written:**
- `vault/videos/japanese-money-methods/storyboard-hi.md`
- `studio/videos/japanese-money-methods-hi/assets/img/manifest.json` (94 slots)

---

## Counts

| | |
|---|---|
| Scenes | **92** (one VO line = one clip = one scene) |
| Runtime | **659.709s** — last scene ends 652.457 + 7.252, matches `timing.json` total |
| Image slots | **97** (92 bg + 5 cut-in) |
| Image files to fetch | **94** (3 bg slots re-use a hold partner's file: s2←s1, s66←s65, s77←s76) |
| Photo-free scenes | **0** ✓ |
| RAIL OFF | 7 — s1, s17, s33, s43, s65, s76, s90 (exactly the seven the script names) |
| Hold pairs (one continuous zoom) | 3 — s1→s2, s65→s66, s76→s77 |
| `shove` transitions | 2 — s33→s34 (debunk → methods), s72→s73 (into the fourth) |
| SFX cues | **24**, closest pair 6.5s apart |
| Music bed | `bed-resolve` |
| Icons | 6 · **Lotties 0** · **Emoji 0** |
| Mandatory-Indian act-now frames | 12, all present |

## Decisions worth carrying

**Colour.** Derived fresh from this video's thesis: `--warn` = *the thing that is draining
or false* (both the leak AND the misused figure — this video's obstacle is a lie about a
leak), `--fund` = *the viewer's own hand*, `--target` = *a figure under examination, never
one being recommended*, `--pop` = CTA once at s91. Explicitly rejected both prior semantics:
needs-vs-wants (amber = wants) and first-lakh (red = the stretch you cross alone). 27 of 92
scenes carry **no** role colour at all — colour is a signifier, not decoration.

**Two corrections to the script's `.rail` spec**, both recorded in the storyboard §3:
1. `num:` is **112px/900**, not the script's 200px. 200 is not on `layout.type_ladder_px`,
   and at 200px an 8-glyph focal (`ABOUT 1%`, `30 TIMES`, `SUBSCRIBE`) overruns the 830px
   content column. s17 (RAIL OFF, 1620px column) takes **240px**, also on the ladder.
2. The rail label is a **per-scene 1–2 word beat name**, not the script's persisting chapter
   name — at 92 scenes the chapter version leaves the rail static for up to fourteen frames
   and throws away its only variance. `sN-of` ("OF 92") dropped with it, which also avoids
   the unverified `/` glyph in the 97-codepoint subset.

**Cue ladder.** One canonical assembly, items 1–5 declared as a cascade at 0.10/0.15/0.15/
0.20s gaps (exactly `cascade.max_items` 5). Every content cue outside it keeps ≥0.8s:
head +0.60 → focal +1.40 → foot/icon +2.20. Assembly always finishes at +2.60; **surplus
from a longer clip goes to the hold, never the cascade.** The 10 `num` scenes take an
anchored arrival instead of the fixed +1.40 so the figure does not precede the voice.

**Holds.** All three hold pairs open on a RAIL OFF scene, so the rail *arrives* over the
boundary — one `railIn` helper used three times (panel left edge 1920→1180 across the 0.45s
while the inner `ken` runs on untouched). The 0.45s overlap is **kept** on hold boundaries:
`pipeline_check` asserts it on every pair with no exception, and the dissolve is invisible
because the incoming scene's ken continues the same trajectory at a tighter crop.

**Audio.** `bed-resolve` because the argument is a habit/fix, not a trap. 24 cues declared as
a ceiling (not a runtime derivation — the ≤10 figure is a SHORT constant; scaling would give
~44, which is the "every reveal has one so none means anything" failure). Deliberate dry
beats include **6.14's 7.1% PPF** — the one rate the video refuses to recommend, so a `hero`
hit would recommend it whatever the foot says — and **3.5's US column**, where a `tick`
would turn a neutral asset-mix table into the gotcha §1 of the script forbids.

**Vector art.** Zero Lotties on purpose: 2.7× render cost measured, and nothing here is a
person/device/scene a photograph doesn't carry better. Six icons, none on a `num` scene
(one focal per scene). The three checkboxes on s38–s40 are one declared set matching SFX
cues 12–14. **Emoji: none, and this is a decision, not an omission** — the ⚠ and 🇮🇳 marks
in the storyboard are notation in that file, never composition text.

**Photography.** Densest scene (s32 / 3.11, five reasons in one 44px string, longest scene
in the cut) gets the **calmest** bg — a flat weathered-plaster wall texture, with the
campaign poster as the second framing. Three phone-adjacent slots (s1, s12, s39) all
specified around the "never a phone screen as a background" rule, which has shipped
undetected three times: face-down, silhouetted, and replaced by a printed statement
respectively. s1's face-down phone is a **deliberate deviation from the script's "face-up"**
for exactly that reason, and it foreshadows 6.12.

## Blocking issues raised (not resolvable at this stage)

1. **Three scenes breach `max_scene_seconds` 9.0 by construction** — s19 (2.9, 9.185s),
   s25 (3.4, **9.002s — over by 0.002**), s32 (3.11, 9.760s). `check_build` computes
   `own = data-duration − transition_seconds` = `scene_duration` = `clip + 0.8`, so it caps
   the *clip* at 8.2s. Its own comment says it exists to bound how long **one photograph**
   sits on screen, but `len(scenes) != n` forbids splitting a line across two sections and
   the run directive forbids a re-record — so the check cannot see the fix.
   **Applied fix:** a declared `panelSwap` to a second photograph on all three, so the
   longest single framing among them is **5.4s**. Storyboard §6 has the swap times, the
   anchor words and the file names.
   **Needs an orchestrator decision** (ranked per fix-defaults-not-gates): (a) preferred —
   `check_build` measures the longest *framing* via a `data-framings` attribute, making a
   dead frame representable as what it is; (b) interim — one `known_benign` entry naming
   these three with the swap evidence. Both live under `tools/`, which this stage may not
   write. **Not acceptable:** shortening a measured clip or hand-editing a duration.
2. **`bed-resolve` is 248s against a 659.709s cut.** `mix.py` stream-loops and both beds
   fade to silence, so audible dips land at ≈248s (inside s37 / 4.4) and ≈496s (inside s70 /
   6.12). Trim + crossfade the loop point, or source a ≥665s bed and re-normalise through the
   same two-pass loudnorm to −20 LUFS. **Do not** run `sfx.py --kit --music --force`.
3. **s65 (6.7) is a photograph that does not exist in stock.** The four-group ₹ flat-lay with
   four handwritten bilingual labels *inside the frame* cannot be a text card (no Devanagari
   in the 97-codepoint subset; the script forbids a card for this beat by name). Fetch route
   is in the manifest; **if no cell shows four distinct groups, escalate to the creator for a
   made photograph.** This is the Von Restorff beat at the 69% mark.

## Note on `.src` prompts

The run brief asked for `.src` image prompts per scene. `tools/stock/pixabay_fetch.py`
already writes each slot's query to `assets/img/<slot>.src` when it promotes the pick
(line 374), sourced from `manifest.json`. So the manifest is the one home for the query and
the `.src` sidecars fin-assets produces **are** the reproducible photography record the
finished-video rule requires. Writing them by hand now would duplicate a fact and be
overwritten at fetch time.

## Handoff to fin-assets

94 files. 12 slots flagged `@pexels` (hold-pair sources, `num` heroes, full-bleed RAIL OFF)
for ≥1600px. Currency slots needing a full-resolution read: s21, s51, s56, s65, s86 —
current stone-grey ₹500 series only, and s51/s86 are two-note stacks where repeated serial
numbers (prop money) become legible. s30's chart **must peak then fall**. s81 must carry no
legible brand mark. s86 vs s51, and s88 vs s75/s76, must be visibly different framings.
