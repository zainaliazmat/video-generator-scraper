# fin-storyboard · cut en · attempt 1 · 2026-08-01

**Result: ok.**

## Artifacts
- `vault/videos/japanese-money-methods/storyboard-en.md` (92 scenes)
- `studio/videos/japanese-money-methods-en/assets/img/manifest.json` (93 slots)

## Inputs read
`vault/CLAUDE.md` · `tools/format.json` · `vault/knowledge/design-finance-blockframe.md`
(the dark system — `design-techtooltester` was NOT opened) ·
`vault/templates/storyboard-template-finance.md` · `vault/videos/.../script-en.md` ·
`vault/videos/.../storyboard-hi.md` (skeleton + IDs) · `run.json` · `tools/audio/kit.json` ·
`studio/videos/japanese-money-methods-en/assets/voice/timing.json` (measured, 626.586s).

## Counts
- **92 scenes**, one per VO line, ledger-rail, `.rail cut-en`, root **626.586s**.
- **96 image slots** = 92 bg + 4 cut-ins. **93 files** — s2/s66/s78 are tighter crops of
  s1/s65/s77 (the three hold pairs) and get no file of their own.
- 7 RAIL OFF (s1, s17, s33, s43, s65, s77, s90) = exactly the seven the script names.
- 11 `num` scenes · 5 icons · 0 lotties · 0 emoji · 29 American act-now frames = the script
  handoff §7 list exactly.
- Transitions: 86 dissolve, **2 shove** (s33→s34, s73→s74), 3 hold pairs.
- SFX: **24 cues**, closest pair 6.31s apart. Dry beats declared, including 32 dry seconds
  across 6.14/6.15 running into SHOVE #2.

## The four things the orchestrator directives asked for

**1. `max_scene_seconds` — zero breaches.** Longest scene is s79 (7.6) at **8.349s**; every
one of the 92 is under 9.0. The hi cut's three unclearable findings (9.185 / 9.002 / 9.760)
**do not exist in this cut** — Brian's 17.39 c/s flat against Harsh's 13.03 is the whole
reason. **No `known_benign` entry is owed for en.**

`data-framings` is emitted on exactly **three** scenes, and not to clear a gate — each names
more concrete things than one photograph holds, and each swap is anchored to its own word:

| scene | dur | swap(s) | `data-framings` | sum |
|---|---|---|---|---|
| s32 (3.11) | 8.140 | +5.66 | `5.66,2.48` | 8.140 |
| s36 (4.3) | 7.801 | +2.74, +4.77 | `2.74,2.03,3.031` | 7.801 |
| s79 (7.6) | 8.349 | +5.50 | `5.50,2.849` | 8.349 |

Every other scene has one framing and carries **no attribute** — a cosmetic `data-framings`
on a panel that never changes is exactly what the new check exists to reject. Hold pairs need
no attribute either: the crop changes at the section boundary, so the sections already
partition the framings (longest hold framing 7.435s).

**2. Music bed — `bed-resolve`, 248s, flagged.** Chosen because the argument is a habit/fix,
not a trap. Against 626.586s `mix.py`'s stream-loop dips to silence twice:

- **≈248.0s** → inside **s37 (4.4)**, tail of a `--warn` beat. Survivable.
- **≈496.0s** → inside **s73 (6.15)**, "about four in ten adults could not cover that four
  hundred dollars". **This is the worse one**: 6.15 is a declared DRY `num` scene carried
  entirely by voice and sits 2.0s before SHOVE #2, so it is the most exposed silence in the
  cut. The hi cut's second dip landed on an ordinary `stmt` beat.

Fix is yours at mix time: trim + crossfade the loop point, or source a ≥632s bed re-normalised
through the same two-pass loudnorm to −20 LUFS. **Do not run `sfx.py --kit --music --force`** —
it destroys the creator-supplied beds, which live only in gitignored `studio/`.

**3. No CJK on screen.** Every on-screen Japanese string is romaji (`MOTTAINAI`,
`HARA HACHI BU`, `KAKEIBO`, `TARU WO SHIRU`, `RYOAN-JI`). Kanji appear only inside the
s76 / s77 / s88 tsukubai photographs. The `🇺🇸` and `▣` marks are storyboard notation in the
md file and never reach the composition — said explicitly in §3 and §8 so the audit reads it
as a decision.

**4. `.src` image prompts.** Written as the manifest, deliberately not by hand.
`tools/stock/pixabay_fetch.py cmd_pick` does `open(out + ".src", "w").write(meta["query"])`
for every promoted slot, so the manifest **is** the one home for the prompt and the `.src`
sidecars land at fetch time. Hand-writing 93 sidecars would duplicate a fact across two files,
which the vault's one-home rule forbids, and they would drift the first time a query changed.

## The -en pass

Ported: element ID scheme, rail geometry, the whole §4 cue ladder including the declared
five-item assembly cascade, transition classes and their mechanics, the `hold` continuous-zoom
rule, the icon shapes, the SFX ceiling of 24, and both `.rail` spec corrections (`num` at
112px not 200px; rail label = per-scene beat name, not a persisting chapter).

**24 explicit divergences with a reason each** (§11). The structural ones:

- **D1** — the `#` ↔ line-id mapping is **rebuilt, not renumbered**. en Ch6 has 15 lines to
  hi's 14 (6.15 Fed SHED is new) and en Ch7 has 11 to hi's 12 (hi 7.11 has no counterpart).
  s1–s58 and s85–s92 keep the hi line ids; s59–s84 do not.
- **D4** — zero `max_scene_seconds` breaches (above).
- **D14 / D15** — s53 is a **new scene** (5.7 automate-and-separate, imaged as two labelled
  envelopes rather than a bank UI, because fin-audit-en-1 stripped the account category out of
  the VO and a photograph of a transfer screen would put the recommendation back through the
  picture); hi's ₹500/₹250 ENTRY TICKET scene has **no en counterpart** for the same rule.
- **D18** — s73 is a new scene, so SHOVE #2 moves to s73→s74. D19 — the third hold pair moves
  to s77→s78.
- **D20** — **5 icons, not 6.** The pen-nib icon lived on hi 7.11, a line the US rewrite does
  not contain. Not replaced: it existed to carry that sentence, and a substitute would be
  decoration chasing symmetry.
- **D13 / D21** — s36's anchor frame becomes the shirt (en 4.3 opens on it) with the field and
  a US interstate semi as swaps, and **the mill is deliberately dropped** rather than faked
  into a 0.98s framing; s79 gains a swap the hi cut did not need because it is the longest
  scene in this cut and enumerates six things.
- **D16** — s55/s56 are two adjacent `num` scenes, which the hi cut separated. Declared so the
  audit reads it as the script's line order; 5.10 is DRY so only one of the two is punctuated.
- **D5 / D8** — the four screen-adjacent slots (s1, s8, s12, s39) are each specified around the
  "never a phone/laptop screen as a background" rule; s39's printed statement is the same
  substitution the hi cut made, so that fix travels.

## Owed upward (not writable from this stage)

1. `bed-resolve` loop (above).
2. `format.json cuts.en.chars_per_second` — this cut measures **17.39 c/s flat**
   (9,619 chars / 552.986s of audio), the **third** independent measurement above 17.3 against
   a 16.1 key. Per `_chars_per_second_trap` the fix is both-or-neither: budget formula first,
   then the key.
3. **s65 flat-lay placeholder** — US coins and bills in four groups with four handwritten
   labels **inside the frame**. If no candidate cell shows four distinct groups, escalate for a
   made photograph; do not substitute a text card (script handoff §8).
