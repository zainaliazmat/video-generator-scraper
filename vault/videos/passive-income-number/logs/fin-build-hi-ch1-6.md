---
summary: CEO rework, hi ch1 attempt 6 — the single blocker only. s6's three-cell cascade is no longer a fixed +1.10/0.60 popEach; it is three pop() calls at 1.6.mp3's own measured clause onsets (+2.50/+3.95/+5.10), ticks +0.35, and the three chip cues moved with them. Cells now land 0.00s / 0.05s / 0.05s ahead of the nouns they count, and the dead tail drops 5.07s -> 2.72s. Nothing else in the chapter changed; 1275 frames / 42.500s unchanged. cues.py exits 0 but DISAGREES with the shipped list on chips 2 and 3 — the build is right and why is recorded below.
updated: 2026-08-08
source: measured RMS envelope of assets/voice/1.6.mp3 (0.05s window, -26 dB gate) + tools/tts/clauses.py --cells 3 + eight frames extracted from renders/DRAFT-ch1.mp4 + ceo-hi-ch1-1.md finding 1
stage: fin-build, cut hi, chapter 1, attempt 6
---

# fin-build · passive-income-number · hi · chapter 1 · attempt 6
STATUS: ok

## What changed — three numbers and their consequences, nothing else

All edits are in `build.mjs`; `index.html` and `assets/audio.json` are regenerated
from it, so the picture and the sound come out of one array and cannot drift apart.

| where | before | after |
|---|---|---|
| `sc[5].cellAt` (new) | — | `[2.50, 3.95, 5.10]` — the scene-relative clause onsets of 1.6.mp3 |
| markup | `<div class="v-tickcell">` | `<div class="v-tickcell" id="s6-cellN">` — a per-clause anchor needs a per-cell selector |
| motion | `popEach("#s6-ticks .v-tickcell", S.s6 + 1.10, 0.60, 0.45)` | `pop("#s6-cell1", S.s6 + 2.50, 0.45)` / `+3.95` / `+5.10` |
| ticks | `draw(..., +1.45 / +2.05 / +2.65)` | `draw(..., +2.85 / +4.30 / +5.45)` — still exactly `cell + 0.35` |
| `audio.json` chips | 22.759 / 23.359 / 23.959 | 24.159 / 25.609 / 26.759 — generated from the same `cellAt` array |

Untouched, as instructed and verified by diffing the regenerated `index.html`:
every `data-start` / `data-duration` / `data-framings`, the `S`/`D` maps, the root
42.475s, s7's five drawn rungs (no overlay, no re-fetch), the s3/s4 chained
plateKen, the deleted s4 `.band`, `rise("#s4-stmt", …)`, s1's textile, both rate
asserts, s8, and the corrected Lottie comment.

## The measurement — the fix against the voice, which is the defect

`1.6.mp3` anchored at 21.909. RMS envelope, 0.05s window, -26 dB gate relative to
clip peak. Four internal pauses at rel 1.60–2.25 / 3.30–3.75 / 4.50–4.90 /
5.70–6.15, reproducing the CEO's boundaries to within 0.05s. Independently,
`tools/tts/clauses.py passive-income-number --cut hi --line 1.6 --cells 3` returns
`+2.50 / +3.99 / +5.15`. Clause spans, absolute:

| clause | text | span |
|---|---|---|
| C1 | उस नंबर का काम एक ही है | 21.959 – 23.509 |
| C2 | आपका बिजली का बिल, | **24.159** – 25.209 |
| C3 | आपका राशन | **25.659** – 26.409 |
| C4 | और आपका किराया | **26.809** – 27.609 |
| C5 | चुपचाप भरते रहना। | 28.059 – 28.809 |

| cell | pops at | its clause onset | lead | its tick strikes | inside its clause? |
|---|---|---|---|---|---|
| bulb (बिजली) | **24.159** | 24.159 | **0.000s** | 24.509 | yes (24.159–25.209) |
| sack (राशन) | **25.609** | 25.659 | **0.050s early** | 25.959 | yes (25.659–26.409) |
| house (किराया) | **26.759** | 26.809 | **0.050s early** | 27.109 | yes (26.809–27.609) |

Before: bulb 1.400s early, sack 2.250s early, house 2.800s early. The picture now
leads each word by at most 0.05s — the 0.45s `back.out` pop is still resolving as
the noun is spoken, which is the correct order (the frame must never arrive
after the word, and it never arrives a second before it either).

**Dead tail.** Last event onset 27.109 (tick3), next event the s7 cut at 29.825 →
**2.716s**, down from 5.070s, exactly the CEO's predicted 2.72. Measured from the
last pixel to move (tick3 completes 27.559) it is 2.266s. That tail now carries C5
«चुपचाप भरते रहना» over the completed row — the settle the row was built for,
rather than a resolved frame waiting for the list to start.

**Verified from the ENCODE, not the source.** Eight frames pulled from
`renders/DRAFT-ch1.mp4`: 23.90 empty · 24.55 bulb up, box drawing · 25.50 bulb
ticked, nothing else · 26.05 sack up, its box empty · 26.65 sack ticked · 27.20
house up, its box drawing · 28.40 all three ticked · 29.70 unchanged. One item
per clause, on screen, in order.

## cues.py — it exits 0 and it is WRONG about s6, on purpose-adjacent grounds

`python3 tools/audio/cues.py studio/videos/passive-income-number-hi-ch1` → **exit 0**
(it validates the shipped list as well as its own; the new chip gaps 1.450s and
1.150s both clear the 0.8s floor — checked, not assumed). But its output differs
from the shipped list on two rows:

```
generated: … 24.159 chip · 24.659 chip · 25.159 chip …
shipped  : … 24.159 chip · 25.609 chip · 26.759 chip …
```

**The shipped list is right.** Cause: the `counted` branch recovers the cascade
spacing by regexing a `popEach(sel, at, stagger, …)` out of the script. With three
`pop()` calls there is no popEach, so it falls through to its hardcoded
`step = 0.5` and re-emits a uniform cascade from the first cell — i.e. it
reconstructs precisely the fixed-offset shape the CEO's blocker ordered removed,
0.5s apart instead of 0.6s. This is a **second, different** cues.py defect from
today's (that one was reading popEach's 4th argument instead of its 3rd, and is
fixed). The structural point: **a generator that can only express a uniform
stagger cannot express a cascade anchored to speech**, which per the CEO's closing
note is now the intended default for every remaining "what X buys" beat in both
cuts. Six chapters of hi and seven of en will each hit this.

I did not fix it — `tools/` is outside this stage's write boundary. Recorded here
and in `build.mjs`'s own audio.json comment block so nobody runs `--write` against
this chapter and silently restores the blocker. **The upgrade the tool needs**: for
a `counted` scene, collect every `pop("#sN-cell*")` / `pop("#sN-chip*")` selector
match and emit one chip at each call's OWN time, instead of deriving n clicks from
one anchor plus a step. That also makes the popEach path a special case of the
general one rather than a parallel branch.

## Checks

| check | result |
|---|---|
| `npm run check` (`hyperframes check`) | **passed** — 0 errors, 0 warnings, 10 infos (all `container_overflow #sN-bg`, the ken push, `known_benign`); Motion 0/0; Contrast **10/10 WCAG AA** |
| `check_vo_frame.py passive-income-number --cut hi --chapter 1` | **PASS** — 8 scenes cross-checked |
| `tools/audio/cues.py <proj>` | **exit 0** (disagreement on s6 chips 2–3 documented above) |
| ffprobe `renders/DRAFT-ch1.mp4` | **1275 frames · 42.500000s · 30/1** — unchanged |
| mtimes | build.mjs 15:02:12 → index.html 15:02:21 → DRAFT 15:04:46 → SHEET 15:04:57 |
| `chapter_sheet.py` | regenerated from the new draft; s6 sampled at 27.659 (`SETTLE_VECTOR` 6.0), after the row completes at 27.559, so the cell sheets fully assembled |

**No max-density snapshot pass this attempt.** Not one layout property changed —
same elements, same positions, same `.stack`, only three anchor times — and the
eight extracted encode frames above are stronger evidence for what actually
changed than a re-run of a passing safe-area sweep. Stated rather than skipped
silently.

## System notes

Nothing missing from the system this attempt. `pop`, `draw` and the `.v-ticks`
one-off (`.v-` prefixed, in the composition's own `<style>`) all already existed;
no icon was added to `assets/icons/` — s6's three glyphs are the git-tracked
`light-bulb` / `grain-sack` / `house-door` files already in the library.
