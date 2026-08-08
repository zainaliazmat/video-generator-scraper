---
summary: fin-storyboard, japanese-money-methods hi, attempt 3 — full rewrite of storyboard-hi.md for blockframe-9 after the creator rejected the rendered ledger-rail frame. Beat structure, SFX placement and image assignments ported; every rail-derived property re-derived. 92 scenes, 97 image slots, 94 files, unchanged manifest.
updated: 2026-08-01
stage: fin-storyboard · cut hi · attempt 3
---

# fin-storyboard-hi-3

## What changed and why

`run.json` `architecture` moved to `blockframe-9` (creator 2026-08-01, after seeing a rendered
ledger-rail frame of this cut). The prior storyboard was read **only** for beat structure, SFX
cue placement and image assignments — the run brief certified those as sound and they are ported
verbatim. Everything that was a property of the rail was deleted and re-derived.

### Deleted with the rail
`idx` / `hair` / `beat` furniture and their IDs · the 300px rail and 730px photo panel · the
RAIL OFF ↔ rail-on split (7 scenes) · the scrim and text-shadow deletions on 85 scenes · the
damped `1.0↔1.06` panel ken · the `panelOpen` / `panelSwap` / `railIn` helpers · the declared
5-item assembly cascade · the two-type-sizes-per-scene constraint · the `num: 112px` correction
(a rail-column-width fix that does not apply at 1620px).

### Re-derived for blockframe-9
- **Type treatment.** The script's cue blocks were written for the rail's `head:` at 54px/800
  `--ink`. That does not port: a 54px ink headline above a 76–112px ink focal is two focal
  elements once type sits on a photograph. `head:` → **`.kicker`** 30px muted (which is also
  what makes kicker-first true), `stmt:` → **`.huge`**, `num:` → **`.mega` 240px**, `foot:` →
  `.foot` 26px. Three registers, not two.
- **Focal size is a rule, not 92 hand-typed values** — ≤24 chars → 112px, 25–48 → 88px, 49–89 →
  76px, never below 76. Keyed on the copy, so it cannot drift when a string changes, and the
  audit can check it. Basis: ≈0.58em advance at weight 900 against a 1620px content box.
- **Cue ladder collapsed to four variants** (A statement / B figure / C verdict / D close) with
  **every gap ≥0.8s and no cascade at all**. The rail needed a declared sub-0.8s cascade to
  assemble its furniture; with the furniture gone the exception is unnecessary and is retired.
- **Variant B inverts foot and focal** (foot at +1.10, the number anchored after). Under the old
  ladder s16's 95-character citation had a 0.94s read chasing an anchored number. Now the big
  number is the last thing to arrive on every figure scene.
- **`--tint` is back** (scrim layer 1 exists again): role colour at 0.12 alpha, 0.10 for green,
  none on the 41 scenes with no role colour. Stated as a rule rather than a 92-row column.
- **`ken` and `data-track-index` are also rules now** (`i` then flip except across the three
  holds; `1 if n odd else 2`), which removed two full columns from the scene table.
- **Holds are `dissolve`, not a third transition class.** The 0.45s overlap and
  `data-duration = scene_duration + 0.45` are unchanged, so `check_build` needs no exception;
  what makes a hold a hold is a shared file plus a continued ken plus a tighter crop. Two
  `shove`s (s33→s34, s72→s73), as before.
- **`.warnc` / `.fundc` / `.targetc` / `.popc`** used throughout for text; the bare
  `.warn`/`.fund`/`.target` modifiers are reserved for chip/stamp/billrow fills. This is the
  root fix for the two logged silent-white failures (s24 here, s91 in the en cut).

## Re-derived timing

`timing.json` is freshly measured: 92 lines, **659.135s** (was 659.709). VO 7.4 is 0.574s
shorter, so scenes 1–76 keep their starts verbatim and **77–92 all shift −0.575s**. Every
`start` / `dur` / `d-dur` in §7 is taken from the file, not carried over.

Consequences:
- **Only SFX cues #23 (s90) and #24 (s91) moved** — 636.430 → **635.855**, 645.120 → **644.545**.
  Gap between them 8.690s. Everything at or before s76 is untouched and still lands on its word.
- **The `max_scene_seconds` breach set is unchanged**: s19 (9.185), s25 (9.002), s32 (9.760).
  All three sit before line 7.5, so the shift cannot reach them, and `s19b`/`s25b`/`s32b` are
  still the right files under the new numbering. Re-checked, not assumed.
- Root `data-duration` = 659.135 (`timing.json.total`). The scene table sums to 659.134; the
  0.001 is rounding in the source and the total is the one home.

## `data-framings`

Declared as a summing set on the four swap scenes and as a single value on the other 88, so an
absent attribute never has to be interpreted:

```
s19 5.200,3.985   s25 5.200,3.802   s32 5.000,4.760   s36 3.100,2.500,2.540
```

Each framing ≤9.0 and each set sums to that scene's own duration. **s25's swap moved +5.400 →
+5.200** so it clears its anchored `51.0%` arrival (+6.153) by 0.953s instead of 0.753s — the
only cue-time change I made that was not forced by the re-measure.

## Audio

`bed-resolve`, 24 cues, ported. **Bed length is not flagged** — `mix.py` feeds the bed in `laps`
with a 3s `acrossfade` and trims to the master. Both prior storyboards on this slug escalated
that as a decision; §2 and §12 now say in the artifact itself that it is not one, so the next
reader does not re-raise it.

One substantive audio change: **s33 (3.12) now carries a real `.stamp` component**, so the
`stamp` sound finally has the helper the kit binds it to. Its copy is 44 chars and fits the pill
on one line. The other four `stamp` cues (s31, s43, s65, s90) run 58–70 chars and keep a `.huge`
focal — squeezing them into a rotated pill is the shrink-to-fit failure the design doc names,
and one stamp per video is the component's own rule. Expect the known false contrast finding on
`.stamp`; it is not a defect and is not a `known_benign` entry.

## Decisions taken at this stage, with reasons

1. **No chips anywhere.** The two `·`-separated enumerations that look like chip rows both fail
   the constraints: 3.11 as five chips is 7 simultaneous elements (cap 6); 6.10's fourth item is
   28 chars (cap 22) and shortening it is a copy edit belonging to the script. Both render as one
   `.huge` 76 statement.
2. **s91 closes on the `.cta` block, not a `.mega SUBSCRIBE`.** `.cta` is the system's closing
   component, carries `--pop` as a fill with `#0d1017` text, and is what the `cta` sound is bound
   to. `.popc` therefore goes unused in this cut — noted so its absence does not read as the old
   missing-class bug.
3. **Icon and foot never coexist.** Verified against every cue block in `script-hi.md`: 26 scenes
   carry a `foot:`, 6 carry an icon, intersection empty. Element budget is 4 countable per scene.
4. **0 Lotties.** 2.7× render cost on a 659s cut, and nothing in this argument is a person, a
   device or a scene a photograph does not carry better. **0 emoji**, deliberately — the 🇮🇳 and
   ⚠ marks in the storyboard are notation in that file, never composition text.
5. **The seven RAIL OFF beats lose their device and are not given a replacement.** The
   anti-sameness budget now sits where the vault says it sits: 2 shoves, 24 SFX cues, the tint
   ladder, alternating ken, ten 240px `.mega` scenes and a focal size that moves 112/88/76 with
   the copy.

## Imagery

**Nothing re-sourced, manifest not rewritten.** `assets/img/manifest.json` verified: 94 entries
(89 bg + 5 swap/cut-in), matching the 94 files on disk and the 97 slots (3 bg slots re-use a
hold partner's file). The run directive was explicit that the promoted set passes the gate.

**⚠ s76 / the retired square.** The manifest query for `s76.jpg` still reads *"macro of a stone
water basin with a square opening@pexels"*. That string is the historical fetch record for an
already-promoted file, not a claim the frame makes, so I left it byte-unchanged rather than
desynchronise it from the `.src` sidecar. The storyboard says so explicitly in §9 and pins the
on-screen copy (kicker `THE DESIGN`, stmt *"All four share one part — the emptiness at the
centre."*) as promising no square. Called out here so fin-audit does not read the stale query as
a live contradiction with the re-voiced line.

**Resolution flag (the one thing the brief asked me to escalate).** 77/94 files are 1280px; the
17 `@pexels` slots already cover every `hero` cue, both shove-adjacent frames and all three hold
sources. Two beats are carried by a 1280px file where softness would show most:

| scene | beat | file |
|---|---|---|
| s53 | the `62.2%` **hero** at 369.090, 7.566s under a 240px number | calculator with paper tape |
| s91 | the **CTA close** at 644.545, 8.741s, the only `--pop` element in the cut | closed notebook, capped pen |

Both are close, low-detail table-top objects — the framing that upscales best. **Recommendation:
ship both.** Creator call either way.

## Artifacts

- `vault/videos/japanese-money-methods/storyboard-hi.md` — rewritten in full
- `studio/videos/japanese-money-methods-hi/assets/img/manifest.json` — verified, unchanged (94 entries)

## Counts

92 scenes · 97 image slots (92 bg + 5 cut-in/second-framing) · 94 files · 24 SFX cues on
`bed-resolve` · 2 shoves · 3 holds · 4 `bgSwap` scenes · 1 stamp · 6 icons · 0 Lotties · 0 emoji.
