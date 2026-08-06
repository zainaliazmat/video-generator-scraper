---
summary: Milestone note for the "Pay Yourself First" pair (Hindi/₹ 2:58.9 · US/$ 2:57.8) — both cuts rendered + QA-passed 2026-07-28, publish packs written. **LIVE on YouTube 2026-07-28** (hi youtu.be/PKU0_TeJ9_c · en youtu.be/mlvp4xZTROg); source archived to `src/`, studio dir deleted 2026-07-29. Owed — thumbnail-pick readback off the live videos · competitor scrape for this lane · analytics after 28 days.
updated: 2026-07-29
source: run.json + fin-render/fin-package logs in logs/ (attempt 1, /finance-video pipeline)
---

# Pay Yourself First — milestone note

Run 2026-07-27→28, `/finance-video` pipeline, all 18 stages attempt-1 pass
(fin-research failed EmptyStudyPacket and was rescued — see Run events).
Budget: **18 of 30 ElevenLabs calls**, 0 Pixabay calls.

## The two cuts

| | Hindi / India (@cashguruguides) | US / English (@moneymavens101) |
|---|---|---|
| Master *(deleted on archive — now on YouTube)* | was `…-hi/renders/FINAL-1080p-hi.mp4` | was `…-en/renders/FINAL-1080p-en.mp4` |
| Archived source | `src/hi/` | `src/en/` |
| Runtime | **178.9 s (2:58.9)** · 12.89 Mb/s | **177.8 s (2:57.8)** · 12.85 Mb/s |
| Voice | ElevenLabs **Harsh** (standard Hindi) | ElevenLabs **Brian** |
| Script | [[script-hi]] (9 lines h1–h9) | [[script-en]] (9 lines en1–en9, US rewrite not translation) |
| Publish pack | [[youtube-metadata-hi]] | [[youtube-metadata-en]] |

## Hero numbers (with sources)

- **hi: ₹12,000 auto-moved on the 1st → ₹1,44,000 in a year** (creator brief;
  counter animates month by month, en-IN lakh grouping in s7). Supporting feet
  on screen: RBI Annual Report May 2026 — net household financial savings 7.0%
  of GNDI FY25 (the ₹100→₹7 scene, s5); PLFS 2025 salaried-average foot (s7).
  fin-facts staged a **plausibility flag**: ₹12,000/mo is ambitious against the
  PLFS ₹24,217 average — the script answers it with the "even 5%" ladder.
- **en: $400 every payday → $4,800 in a year** (sourced independently per the
  US-rewrite rule). Supporting feet: BofA Institute Nov 2025 ~25% of households
  paycheck-to-paycheck (s1); BLS median usual weekly earnings $1,251 Q2 2026 +
  BEA "$1.00 earned → 3¢ saved" (s5); Fed SHED foot on the $400 card (s7).
- Both markets' facts staged in [[facts-staging]] (promotion to
  money-facts-2026 is the orchestrator's step). Known conflict recorded both
  ways: 25% (BofA) vs 66% (PYMNTS) paycheck-to-paycheck.

## QA (from the fin-render logs, both PASS)

| | hi | en |
|---|---|---|
| Runtime vs timing.json | +0.005 s | +0.041 s (AAC priming) |
| VO drift (xcorr, authoritative) | **0.021 s** max, uniform | **0.021 s** max, uniform |
| True peak | **−3.27 dBTP** (< −1 limit) | **−3.91 dBTP** |
| Loudness | −22.24 LUFS, LRA 3.3 | −21.13 LUFS, LRA 3.2 |
| Frame check | 9/9 scenes pass | 9/9 + s7 mid-count pass |
| blackdetect | 2 windows = photo-free navy scenes, false positives | same, false positives |

## Thumbnails (3 variants per cut, creator picks at upload)

`vault/videos/pay-yourself-first/src/thumbs/thumbnail-{hi,en}-v{1,2,3}.png` —
v1 THE MATH (green, centered, photo-free — recommended pattern-breaker) ·
v2 THE HOOK (red, money photo, "20 tak khali / empty by the 20th") ·
v3 THE FLIP (calculator, struck spend-first / green save-first).
`chosen:` line sits in each publish pack — **still unfilled as of 2026-07-29, i.e. it
survived a real upload blank** (read back by fin-archive on the credit-history run).

**But the creator did give feedback — in a different place.** [[youtube-metadata-en]]
records a **creator title pick, 2026-07-28**: option 8, "The $5 Trick That Saves You
Thousands Without Thinking" (vidIQ 83), plus a **`thumbnail-en-v4.png`** built for it
(`vault/videos/pay-yourself-first/src/thumbs/thumbnail-en-v4.png`, on disk). So by upload
day the `chosen:` field's own option set (v1/v2/v3) could not express the answer, and
the pick that matters may well be **v4**. Feedback lands as prose in the section the
creator was already editing — design the loop around that, not around an empty field.

**Recoverable without asking again:** the chosen thumbnail is the public thumbnail —
compare the live videos (youtu.be/mlvp4xZTROg · youtu.be/PKU0_TeJ9_c) against the four
PNGs on disk and record the match here. fin-archive has no network access, so this is
owed to whoever can open the URLs. Full argument: [[../credit-history/index]].

## AI-enhance prompts (2026-08-06) — `chosen:` **v2 on both cuts**, and the v4 theory is dead

Creator screenshots of the two live tiles, 2026-08-06. Both match
`src/thumbs/thumbnail-{hi,en}-v2.png` exactly. **This was the last 🔴 blocker in the
retro-enhance backlog** ([[../../knowledge/design-thumbnail-ai-enhance]] §5c) — the
`chosen:` field that the whole dead-feedback-loop argument was built on is now answered,
and both packs are filled.

**Two recorded beliefs above are now wrong and are corrected here, not deleted:**

1. **"The pick that matters may well be v4" — no. It is v2.** The section above reasoned
   that because the creator picked title option 8 ("The $5 Trick That Saves You Thousands
   Without Thinking") and a `thumbnail-en-v4.png` was built for it, v4 was probably live.
   It is not. The live tile is v2 and the live title is **"Why Your Account Is Empty by
   the 20th (Pay Yourself First)"** — so the creator took neither the v4 tile nor the
   title it was built for. `thumbnail-en-v4.png` was never used.
2. **"Recoverable without asking again" was right about the method and wrong about the
   channel.** It proposed opening the live URLs; those 404 while an upload is scheduled.
   What actually worked, on all three videos so far, is **the creator pasting a
   screenshot** — no network, no reachability, one action.

### The en plate breaks a standing visual rule, and the enhance is the fix

`thumbnail-en-v2.png` is built on an **empty-pocket photo containing a person** — a hand,
a wrist, a sleeve and a torso. The channel's standing rule in the enhance doc is *no
people, no faces, no hands*, and this tile predates it (shipped 2026-07-28; the rule was
written 2026-08-06). **So on this video the enhance pass is not only depth-and-props — it
replaces the hero subject.** That is a bigger change than the previous three videos got
and it is deliberate: flag it, don't smuggle it.

The replacement has to say *empty* without a body. Both cuts get **a worn wallet lying
open and flat, its note compartment splayed and visibly holding nothing** — the one
object that reads "empty" instantly at browse size, and none of the props already spent.

### Two deliberate breaks from the last four tiles

Acting on the convergence flag raised in
[[../good-debt-vs-bad-debt/index]] §Result — all four enhanced tiles so far are a warm-lit
hero group on a dark scratched wooden desk at night:

- **Cool, flat, overcast daylight instead of a warm night lamp**, and **no lamp in
  frame** (per the fixture bug — light is described as off-frame, source not visible).
- **No wooden desk.** hi sits on a worn cotton bedsheet, en on a pale laminate kitchen
  counter — domestic surfaces, not a study.

This also happens to be the better read of the claim: *empty by the 20th* is flat,
deflating and ordinary. Cold daylight suits it; a moody warm lamp would flatter it.

⚠️ **The draining bar is preserved UI, not decoration.** Both tiles carry a red-outlined
bar, filled ~66 % in translucent red with 12 tick divisions. It is part of the plate and
must return untouched — it is listed in the preserve block of both prompts.

### hi — `thumbnail-hi-v2.png` → @cashguruguides

```
Enhance this 16:9 YouTube thumbnail. Rebuild ONLY the photograph behind and around the
existing type. This is a photo-retouch task, not a redesign.

ABSOLUTE RULE — PRESERVE ALL EXISTING TEXT AND UI PIXEL-FOR-PIXEL. Do not re-render,
re-letter, restyle, translate, transliterate, move, resize or re-space ANY text or its
container shapes. Every glyph must return byte-identical:
  • "AAPKA ACCOUNT" — near-black letters on a rounded red pill (#ef4444), upper left
  • "20 TAK" — cream (#f5f3ec) mega caps
  • "KHALI?" — red (#ef4444) mega caps, same size, directly below
  • "Galti aapki nahi — system ki hai" — cream, with the span "system ki hai" in red
  • THE BAR at the bottom: a red-outlined horizontal bar divided into 12 segments,
    filled about two-thirds of its width in translucent red and empty after that.
    Preserve its outline, its fill width, its tick divisions and its position exactly.
    Do not restyle it, do not extend the fill, do not add numbers or labels to it.
Keep the rupee glyph ₹ exactly as drawn wherever it appears. Add NO new text, numbers,
labels, signs, handwriting, stamps with words, logos, watermarks or captions anywhere.

REGION: rebuild only the right ~40% of the frame plus the area behind the type. The left
column must stay in deep shadow so all four text lines and the bar keep their contrast.

LIGHT: cool, flat, overcast daylight from an off-frame window on the left. The light
source is NOT visible — no lamp, no bulb, no fixture, no window in frame. Soft shadows,
low contrast, slightly desaturated. This is daytime, not night.

SCENE: one continuous photoreal scene — an ordinary Indian home, mid-morning. ONE hero
group on the right: a worn brown leather wallet lying open and flat on a rumpled cotton
bedsheet with a faint woven check, its note compartment splayed open and visibly EMPTY,
with a single small coin resting on the sheet beside it. Shallow depth of field, deep
falloff to near-black at the frame edges. Photographic, 50mm at f/2, not CGI, not a
render, not an illustration.

THE IDEA THE IMAGE MUST CARRY: nothing left, before the month is over. The wallet must
read as EMPTY at a glance — the open, slack, flattened compartment is the whole point.

TONE — ordinary, domestic, deflated, everyday. Worn leather, soft cloth, muted colour.
No drama, no disaster, no spotlight, no light rays. Equally: no wealth, no cash piles,
no gold, no luxury, no glitter.

COLOUR LOCK: NO GREEN anywhere — not a plant, not a tick, not a banknote, not a
highlight. This tile states the problem, not the solution. Cream, muted brown, cool grey
and near-black only, with red reserved for the existing type and bar.

NO SOLUTION IMAGERY: no piggy bank, no gullak, no coin jar, no savings box, no stacked
coins, no upward arrow, no tick, no growing plant. Those belong to the video's answer,
and this tile sells the problem.

CURRENCY LOCK: Indian only. No US dollars, no foreign notes or coins. Do NOT render a
banknote at all — a printed note face comes back with garbled serials and a wrong
portrait. A plain unmarked coin is fine; a note is not.

SURFACE RULE: every paper, cloth and leather surface is blank, or covered by the props,
or so far out of focus that no line of type is resolvable. No blocks of body copy, no
lettering, no filler text, no printed rows, no brand name on the wallet, no card visible
inside it.

DO NOT USE these props (already used on this channel's other videos): desk lamp,
magnifying glass, tied paper stack, calculator, dark scratched wooden desk, hourglass,
clock, calendar, red cloth-tied file, brass key, car key, key fob, manila folder.

FORBIDDEN CONTENT: NO PEOPLE, NO FACES, NO HANDS, no wrists, no arms, no clothing being
worn, no body parts of any kind — this channel is faceless, permanently, and this is the
strictest rule in the prompt. No charts, pie graphs, bar graphs, gauges, dials, meters,
receipts with legible lines, checklists, progress bars or infographics — the bar already
in the image is the ONLY bar, do not add another. No collage, no panels, no
left-to-right sequence: ONE hero group that survives at 320×180.

OUTPUT: 16:9, 1280×720 framing, photoreal, cinematic.
```

### en — `thumbnail-en-v2.png` → @moneymavens101

```
Enhance this 16:9 YouTube thumbnail. Rebuild ONLY the photograph behind and around the
existing type. This is a photo-retouch task, not a redesign.

ABSOLUTE RULE — PRESERVE ALL EXISTING TEXT AND UI PIXEL-FOR-PIXEL. Do not re-render,
re-letter, restyle, move, resize or re-space ANY text or its container shapes. Every
glyph must return byte-identical:
  • "BE HONEST" — near-black letters on a rounded red pill (#ef4444), upper left
  • "EMPTY BY" — cream (#f5f3ec) mega caps
  • "THE 20TH?" — red (#ef4444) mega caps, same size, directly below
  • "Saving what's left? Nothing's left." — cream, with "Nothing's left." in red
  • THE BAR at the bottom: a red-outlined horizontal bar divided into 12 segments,
    filled about two-thirds of its width in translucent red and empty after that.
    Preserve its outline, its fill width, its tick divisions and its position exactly.
    Do not restyle it, do not extend the fill, do not add numbers or labels to it.
Add NO new text, numbers, labels, signs, handwriting, stamps with words, logos,
watermarks or captions anywhere.

CRITICAL — REMOVE THE PERSON. The current photograph shows a hand, a wrist, a sleeve and
a torso pulling out an empty pocket. Delete all of it. The rebuilt image must contain NO
human being, NO hand, NO arm, NO worn clothing, NO body part whatsoever. Replace the
subject entirely with the object scene below.

REGION: rebuild the entire photograph. Keep the left column in deep shadow so all four
text lines and the bar keep their contrast.

LIGHT: cool, flat, overcast daylight from an off-frame window on the left. The light
source is NOT visible — no lamp, no bulb, no fixture, no window in frame. Soft shadows,
low contrast, slightly desaturated. This is daytime, not night.

SCENE: one continuous photoreal scene — an ordinary home kitchen, mid-morning. ONE hero
group on the right: a worn brown leather wallet lying open and flat on a pale laminate
counter, its note compartment splayed open and visibly EMPTY, with a single small unmarked
coin on the counter beside it. Shallow depth of field, deep falloff to near-black at the
frame edges. Photographic, 50mm at f/2, not CGI, not a render, not an illustration.

THE IDEA THE IMAGE MUST CARRY: nothing left, before the month is over. The wallet must
read as EMPTY at a glance — the open, slack, flattened compartment is the whole point.

TONE — ordinary, domestic, deflated, everyday. Worn leather, plain counter, muted colour.
No drama, no disaster, no spotlight, no light rays. Equally: no wealth, no cash piles,
no gold, no luxury, no glitter.

COLOUR LOCK: NO GREEN anywhere — not a plant, not a tick, not a banknote, not a
highlight. This tile states the problem, not the solution. Cream, muted brown, cool grey
and near-black only, with red reserved for the existing type and bar.

NO SOLUTION IMAGERY: no piggy bank, no coin jar, no savings box, no stacked coins, no
upward arrow, no tick, no growing plant. Those belong to the video's answer, and this
tile sells the problem.

CURRENCY LOCK: US only. No rupee symbol, no foreign currency. **Do NOT render banknotes
at all** — dollar bills come back with garbled serials and wrong portraits. A plain
unmarked coin is fine; a note is not.

SURFACE RULE: every paper, card and leather surface is blank, or covered by the props, or
so far out of focus that no line of type is resolvable. No blocks of body copy, no
lettering, no filler or lorem-ipsum text, no printed rows, no brand name on the wallet,
no card visible inside it.

DO NOT USE these props (already used on this channel's other videos): desk lamp,
magnifying glass, tied paper stack, calculator, dark scratched wooden desk, hourglass,
clock, calendar, manila folder, car key, key fob, credit card shown face up.

FORBIDDEN CONTENT: NO PEOPLE, NO FACES, NO HANDS, no wrists, no arms, no clothing being
worn, no body parts of any kind — this channel is faceless, permanently, and this is the
strictest rule in the prompt. No charts, pie graphs, bar graphs, gauges, dials, meters,
receipts with legible lines, checklists, progress bars or infographics — the bar already
in the image is the ONLY bar, do not add another. No collage, no panels, no
left-to-right sequence: ONE hero group that survives at 320×180.

OUTPUT: 16:9, 1280×720 framing, photoreal, cinematic.
```

**After generation — two extra checks on this pair, beyond the usual ≥40 % assert:**

1. **Confirm the person is gone from the en tile** and that no stray hand, sleeve or
   shoulder survived at the frame edge. This is the whole reason the en prompt is more
   aggressive than the other three.
2. **Confirm the draining bar came back unmodified** — right fill width, 12 ticks, no
   added labels. It is the first preserved element in this series that is neither type
   nor a solid panel, so it is the least tested part of the technique.

Save as `src/thumbs/thumbnail-{hi,en}-v2-ai.png` **in this repo** before the swap.

- **fin-research EmptyStudyPacket, rescued**: the library has never been
  scraped for this lane — run continued on vault knowledge; scrape owed (below).
- **Render-backgrounding fix**: subagent background tasks die on return, so
  the **orchestrator now owns encodes** (both fin-render logs note "encode run
  by orchestrator"). Pipeline-level fix, keep.
- **en assets R-5 dedupe** caught 3 byte-identical cross-channel images before
  they shipped in the en cut.
- **Channel sameness FLAG (both packages)**: this is the **4th consecutive
  blockframe-9 ~3-min structure on each channel** — the next upload should vary
  the architecture, or it's a 5-in-a-row template run.
  *(unvalidated — no analytics yet)*
- Thumbnail observation: v1 would be the first-ever green/centered/photo-free
  thumb on either channel; last 3 on both are red/left-text/money-photo.
  *(unvalidated — no analytics yet)*

## Published + archived (uploaded 2026-07-28 · archived 2026-07-29)

**State: LIVE on YouTube (both cuts) · source archived · studio dir deleted.**

| Cut | Channel | URL | Thumbnail |
|---|---|---|---|
| hi | @cashguruguides | https://youtu.be/PKU0_TeJ9_c | not recorded |
| en | @moneymavens101 | https://youtu.be/mlvp4xZTROg | not recorded |

**Source: `src/{hi,en,thumbs}/`** — composition, meta/package JSON, `gen_vo_*.sh`, the VO
lines (`assets/voice/*.txt`), the image prompts (`assets/img/*.src`), stock CREDITS and the
seven thumbnail PNGs. `studio/videos/pay-yourself-first*` is **deleted** per the
finished-video rule ([[../../CLAUDE]]). **Re-render is reproducible, not free** — scene
photos and VO mp3s are gone; a rebuild re-pays image gens + ElevenLabs.

Still owed:
- **thumbnail pick** — no longer "fill `chosen:` at upload" (that already failed once
  on a live upload): **recover it off the two live videos** by comparing the public
  thumbnail against the archived `src/thumbs/thumbnail-{hi,en}-v*.png` (en has four
  candidates, incl. v4) and record the answer in the Thumbnails section above
- **competitor scrape for this lane** (`pay-yourself-first` / saving-first —
  library empty, from run.json `owed`)
- **analytics after 28 days** (only then may learnings touch best-practices)

~~proof-listen (hi, en)~~ · ~~upload~~ — both cuts went live 2026-07-28.
