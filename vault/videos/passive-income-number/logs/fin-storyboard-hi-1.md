---
summary: Process log for fin-storyboard, passive-income-number cut hi attempt 1. Result ok. Records the archetype/ground/art derivation, how the rate constraint became a DOM element, how the 2.6/2.7 14.034s single-photograph breach was resolved, and the six judgement calls that could have gone the other way.
updated: 2026-08-07
source: run.json.constraints, script-hi.md (post fin-audit-hi-1), audit-hi.md, timing.json (measured), knowledge/design-finance-blockframe.md, knowledge/design-chapter-archetypes.md, tools/format.json, tools/audio/kit.json, tools/audio/cues.py, assets/lottie/index.json
stage: fin-storyboard, cut hi, attempt 1
---

# fin-storyboard-hi-1 — process log

**Result: ok.** Artifacts: `vault/videos/passive-income-number/storyboard-hi.md` and
`studio/videos/passive-income-number-hi/assets/img/manifest.json`.

## Order of work

1. `vault/CLAUDE.md` → `run.json` (constraints block, `architecture: blockframe-9`) →
   `tools/format.json` constants.
2. `script-hi.md` **as it exists now** — the five fin-audit-hi-1 in-place edits are present
   (5.9 and 7.6 VO + frames, 5.14 VO, 5.15 foot, the rebuilt role-colour legend). Read
   `audit-hi.md` for what those edits were and why, so the storyboard would not undo one.
3. `timing.json` — 78 rows, total 488.222. Every `scene_start` / `scene_duration` in §7 is
   copied from it; **no duration in this storyboard was computed, rounded or re-derived.**
   Verified end-to-end: 482.824 + 5.398 = 488.222 = `timing.json.total`.
4. `design-finance-blockframe.md` (the dark system — `design-techtooltester` deliberately not
   opened) → `design-chapter-archetypes.md` → `chapter_design` in format.json.
5. Reference read: `japanese-money-methods/storyboard-hi.md` for the cue-variant and scene-table
   shape only. Its colour semantics, SFX list and image picks are that video's and were not
   carried across.

## The three run-specific problems, and what was done

### 1. The rate constraint — made structural, not restated

`run.json.constraints.withdrawal_rate_on_screen` broke twice in the script (5.9 `₹9,00,000`,
7.6 `₹1,00,00,000`), and both breaks were **outside the rung ladder** — a ceiling frame and an
emotional callback where the corpus is being *denied*. Restating the rule in prose would not
change that.

So `#sN-rate` is a **named DOM element with an id, a cue slot and a colour class**, present on
all 20 corpus frames, in one of two forms (§4 of the storyboard):

- the script's own qualifier line as a `.sub`, arriving at **+1.10, BEFORE the corpus lands at
  +1.90** — the assumption is on screen first and the number arrives into it;
- an inline `<span>` inside the focal wrapping the rate token, taking a `pulse` at +1.90, where
  the corpus and rate are fused in one sentence.

No copy is invented, reordered or printed twice. The build assert is now checkable against a
node rather than a substring: *every scene whose text contains a corpus token contains
`#sN-rate`, and that element's text contains a rate token.* The two ★ frames are listed by name
in the table so a later edit that shortens either focal fires the assert instead of silently
dropping the assumption — which is exactly how it dropped the first time.

### 2. 2.6 + 2.7 = 14.034 s on one photograph

Executed `script-hi.md` Build handoff §7 rather than inventing a fix: `s14.jpg` is a **tighter
crop of `s13.jpg`'s source frame**, and the ken runs `1.00 → 1.09` on s13 and `1.09 → 1.16` on
s14 in the **same direction** via `plateKen`'s explicit endpoints. Longest single framing is
8.036 s, under the 9.0 ceiling. The joint is a `hold`: mechanically a 0.45 s dissolve, but
declared in `cues.py`'s `HOLDS` so it takes **no `transition` SFX** — a whoosh there announces a
change that is not happening. Never a self-dissolve back to the same file (firaun 2026-07-23).

The manifest entry for `s14.jpg` says *derive by cropping s13's source; do not fetch a second
photograph and do not reuse s13.jpg unchanged*, so fin-assets cannot resolve it as a normal slot.

### 3. 6.13 at 8.767 s against a 9.0 ceiling

Nothing on s67 needs a slow reveal because **nothing on any scene does**: every cue variant is
fixed-offset and finishes by +2.70 at the latest, so s67 holds a finished frame for 6.07 s with
only the ken push running. `art: off` there as well (see judgement call 3).

## Judgement calls worth recording

**1. The archetype sequence — the ladder gets one archetype.** fin-script assigned `arch` per
line; I kept it except on four rung-naming scenes (3.1, 4.1, 6.1, and by extension 2.8/6.6)
which it filed as `A` (chapter opens) while 2.8 was `B`. Made them all **B**, so every rung
reads `B B` — the corpus named, then its division worked. That is the ladder made visible and it
removes an inconsistency that would have read as randomness. Four holds are deliberate and named
in §7: ch2 `B B B B`, ch4 `D D`, ch5 `C C C` (the script names this one itself), ch6 `B B B B`.
The archetype doc is explicit that holding across one argument is correct; varying there breaks
the through-line.

**2. 71 of 78 scenes are `centred`.** With `art: off` on 73 scenes, B/C/D splits have nothing on
the other side and the doc says such a scene re-centres and drops its plate and rules. That is
the documented consequence on a photo-led cut, not a defect — the archetypes then vary the
*art*, not the type. Seven scenes have something real on the other side (five drawn proportions,
one Lottie, one icon), which is at the low end of the doc's range and deliberate: this cut's
recurring graphic mark is the rate element, on 20 frames, and adding decoration on top of it
would compete with the one thing the video is about.

**3. Four drawn layers were refused, and the refusals matter more than the five that shipped.**

- A **depletion bar** under 5.4/5.5 would assert a depletion schedule we have no source for —
  a drawn projection is precisely the shape `no_return_promise` forbids.
- A **two-bar comparison** under 6.15/6.16 (₹19,000 at 7.1% vs ₹10,000 at ~12%) reads as a
  recommendation between two assumed growth rates the moment it is drawn side by side.
- A **risk curve** under 5.16 would fabricate a measurement on a frame cited to a paper that is
  403'd to us.
- A **stats-table row** under 6.9 would fabricate a source document on a frame cited to PLFS —
  `vector_art.lottie.truth_bar` forbids it by name.

Each of the five that survived states an arithmetic that comes from `facts-staging.md` and is
written into the scene comment (§8 table), per gotcha 7 (numerator and denominator are a pair).

**4. One Lottie, not four.** `phone-notify-credit` on s3 is a library reuse with no fetch and no
tint (it is authored in the system's own palette; tinting would push it into a role colour 1.3
has not earned). It is additive rather than depictive for a structural reason: a phone-screen
photograph is banned by the design system and the script's own cue requires the notification to
be illegible, so **the picture is forbidden from saying the thing the scene exists to say.**
The amount is masked (`₹ • • • • •`) — a figure at 0:10 would break the open loop the whole cold
open is built on and would drag the rate constraint onto a frame that has nothing to qualify.

`calendar-20th-circled` was considered for 2.3 and **rejected on rule 8**: the photograph is
already a date circled in ballpoint on a wall calendar, so the drawn version is the "ghost
envelope over a photograph of an envelope" failure. `max_per_chapter: 4` is a threshold at which
the next one must be justified, not a target to hit.

**5. The SFX count is derived, and I am not budgeting it by hand.** The stage contract names
≤10 cues, which `kit.json` and the japanese storyboard both record as a **SHORT-cut** figure;
the creator retired the hand-authored ceiling for chapter cuts on **2026-08-06** because a
24-cue list over ten minutes carries exactly one `transition` and every scene change then reads
as silent — the defect actually reported. `tools/audio/cues.py` is the implementation, so this
storyboard supplies only what the generator cannot derive: `HOLDS`, `BUZZ`, `COUNTED` (empty —
there is no cascade in this cut), the two priority overrides (s49 takes `reveal` not `hero`; s24
takes nothing, it is a restatement) and the dry list. **Flagging this because it is the one place
this storyboard knowingly departs from the letter of the stage contract, on a dated creator
decision recorded in the vault.**

**6. Bed length was not escalated.** `mix.py` loops with `acrossfade`; there is no dip at 248 s.
Recorded because both storyboards on `japanese-money-methods` raised it as a decision on
2026-08-01 and it never was one. The cut is 488.222 s and `bed-resolve` is chosen because the
argument is a habit, not a trap — chapter 5 runs in a trap register for 100 s but the thesis it
serves is the closing habit line at 7.4.

## Ground arc — the two declared temperature events

- **s42 (5.5) `#3b1219`, the hottest frame**: capital gone, monthly income gone.
- **s50 (5.13) `#0e1c2e`, the coldest frame**: a 1994 American journal on a library table, the
  furthest any frame gets from the viewer's kitchen and the exact beat where the video says
  *this number is not ours*. The drop is a temperature event before it is an argument.
- **s61 (6.7) `#1d3a28`**, the only use of the deepest green: the hero.
- s68 (6.14) is deliberately **neutral** — the frame that separates withdrawal rate from growth
  rate may not be painted as either.
- s40 (5.3) sits between two reds on a red-leaning **neutral** (`#251a1c`): it moves on the warm
  axis without asserting a role it has not earned.

## Constraint compliance

| Constraint | How it is carried |
|---|---|
| `withdrawal_rate_on_screen` | §4 — 20 corpus frames, 20 `#sN-rate` elements, one build assert |
| `no_return_promise` | four drawn layers refused (call 3); `.sub` qualifiers never render a rate as an expectation; s68's icon draws the withdrawal/growth distinction |
| `no_unsourced_retire_early` | no age, no date, no horizon appears as an on-screen element anywhere; 6.11's refusal keeps its focal |
| `hi_currency_framing` | grepped the storyboard and the manifest for `dividend` / `डिविडेंड` / `लाभांश` / `$` — **zero hits**. No manifest query names a foreign document, price or institution |
| `market_rewrite_not_translation` | §12 lists what the -en cut ports and what it must not — the corpus figures and §4's whole token list are named as non-portable |
| no rail | §3, stated three times: no rail, no chapter title, no scene counter, no slide number |
| `image_per_scene` | §9 — 78 scenes, 78 `.bg` files, `photo_free_scene_ratio` 0, no exceptions available to add |
| timing verbatim | §7 / §11 — copied from `timing.json`, verified against `total` |

## Owed / carried

- **fin-assets** must md5-check every fetched file against the cross-project ledger (no hash
  reused on either channel) and honour the eleven Pexels routings in §9.
- `s14.jpg` is a **crop job**, not a fetch. If fin-assets resolves it as a normal slot, the
  14.034 s breach comes back and `check_build` will catch it.
- The four returning objects (s71, s72, s76, s77) are **new photographs** of the same subject.
  Re-using s1/s3/s19/s2's files would satisfy the eye and break the per-line sound-off rule.
- Nothing here unblocks `run.json.owed` (the real study packet, the vidIQ packaging pass).
