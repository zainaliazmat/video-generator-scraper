---
summary: Targeted fix — ported the en cut's `blankBar` predicate into the hi build so a bar copy that is empty or a bare dash suppresses the .swissbar element and its cue; only scene s85 (9.9) changed, runtime unchanged at 514.789s.
updated: 2026-07-31
source: studio/videos/first-lakh-first-thousand-hi (build.mjs, index.html, snapshots/qa/fix2)
---

# fin-build — first-lakh-first-thousand · hi · attempt 2

Scope: **one fix, nothing else.** Instruction was explicit that this triggers a
full re-encode + re-mix + re-loudnorm + re-QA of an otherwise finished cut, so
no other change of any kind was made to the composition.

## The defect

`build.mjs` scene table carried `bar: "—"` on row 85 (line 9.9, scene_start
504.647s, own duration 3.961s) — the storyboard's "this scene has no title"
marker, rendered literally. Result: a full-width black title bar holding one
short white dash and nothing else, on the second-to-last scene, adjacent to the
CTA. Reads as a title that failed to load. Flagged at the end of `fin-build-en-3`
and confirmed by the parent from the already-encoded hi master.

## The fix (ported verbatim from the en build, not special-cased)

`studio/videos/first-lakh-first-thousand-hi/build.mjs`:

```js
const blankBar = (s) => !String(s ?? "").replace(/[—–-]/gu, "").trim();
```

with the same inline self-check the en cut carries (`—`, `""`, `-`, `null` ⇒
true; `NEXT`, `THE ORDER`, `0.5 vs 6.5` ⇒ false) — it runs on every `node
build.mjs`, so the build fails loudly if the predicate is ever broken. Three call
sites, all general:

1. `const barPx = noBar ? 0 : ladderFit(...)` — no ladder fit for absent copy.
2. `barHtml = noBar ? "" : <div class="swissbar">…` — the element is not emitted
   at all, so there is no empty container and no leftover strip.
3. `if (!noBar) c.push(rise("#…-bar", …))` — the cue is dropped with it. A GSAP
   cue on a missing selector is a silent no-op, which is exactly how this class
   of thing hides.

No future cut of this composition can reproduce the frame: any bar copy that is
blank or dash-only suppresses itself, whatever row it sits on.

## Verification

`node build.mjs` → `86 scenes, 514.789s, 22 sfx cues`. Diff against the previous
`index.html` is **exactly two deleted lines** — the s85 `.swissbar` div and the
s85 `rise` cue. Nothing else in the file moved: no `data-start`,
no `data-duration`, no `S` map entry, no `<audio>` row (86, unchanged), no root
`data-duration` (514.789, unchanged). Timing is untouched, so the QA'd VO
alignment (86/86 lines, +0.0214s uniform drift) still holds.

**Snapshots.** Fresh per-batch dir `snapshots/qa/fix2` (batch `fix1` was
discarded — it printed "Runtime did not become render-ready within 5000ms", so it
was re-run at `--timeout 25000`; `hyperframes snapshot` wipes its `-o` dir, hence
a second dir rather than a re-use). **2 frames captured, 2 frames actually
eyeballed**, both scene s85 only — 505.200s (rule mid-fill) and 507.600s (last
cue, `rise("#s85-focal")` at 507.170 + 0.40 settled). Deliberately small: the en
encode is running on this box.

A/B against the pre-fix frame at the same time (`snapshots/frame-06-at-507.62s.png`,
old build):

| | before | after |
|---|---|---|
| y≈55–170 | pure-black full-width bar + one short white dash at x≈100 | plain page ground, continuous with the rest of the frame |
| photo band y≈170–785 | unchanged | unchanged, same pixels |
| swissrule, CTA chip, foot | unchanged | unchanged, same y |

One continuous field, no leftover black strip, no stray dash, no empty
container — the same reading verified on en's s91. Layout below the bar did not
move, as predicted: swiss-band row 2 is a fixed 120px and the aperture is
absolutely positioned.

**Checks.** `npm run check`: 1 error, 89 warnings. The single error is
`invalid_parent_traversal_in_asset_path` (`../fonts/`, `../img/` from
`blockframe.css`), which is the one entry in `tools/format.json` `known_benign`
— unchanged by this fix, present before it, and not a defect. No token was
edited to satisfy any checker. Warnings are the usual
`timeline_track_too_dense` / composition-size family (43 timed elements per
track, by design at 86 scenes).

`pipeline_check check build --slug first-lakh-first-thousand --cut hi` → **PASS
build-hi**.

## Other defects: reported, not touched

None found in this pass. The bar-suppression path was the only thing inspected;
per instruction, nothing speculative was changed.

## For the system (between runs, not now)

The predicate now lives in two cut-local `build.mjs` copies. It belongs in
`tools/scaffold/` alongside the `known_benign` `blockframe.css` re-pathing —
both are deliberate scaffold edits for the gap between runs, not mid-run
improvisation.
