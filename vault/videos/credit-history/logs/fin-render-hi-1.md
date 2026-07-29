---
summary: Gate ② frame check for credit-history hi — FAIL. 8 of 9 last-cue frames clean; s7's full-bleed cut-in (`s7-cut.jpg`) is a car key remote fob and it replaces the blueprint under the payoff line "SAME HOUSE. DIFFERENT NUMBER." for the last 4.2s of the scene. No encode run.
updated: 2026-07-29
source: own snapshots studio/videos/credit-history-hi/snapshots/qa{,2,3}/ at the 9 last-cue times derived from index.html's JS S-map · assets/img/*.src · logs/fin-build-hi-1.md
---

# fin-render — credit-history · hi · attempt 1 · INVOCATION 1 (frame check only)

**Result: `STATUS: fail`. One terminal-quality defect on scene 7. Encode not started**
(the orchestrator owns the encode; it was never invoked).

## Frame times — derived independently, not taken from fin-build

Each scene's last *entering* cue, at the instant that cue's tween **completes** (`breathe`
/ `pulse` loops after that point add nothing new). Computed off the `S` map + cue list in
`index.html`, not copied from the build log:

| Scene | `S` | last entering cue | frame captured |
|---|---|---|---|
| s1 | 0 | `pop #s1stamp` +15.50 (·0.6) → 16.10; breathe +16.80 | **16.80** |
| s2 | 18.562 | `rise #s2sub` +9.50 (·0.7) → 28.762 | **28.80** |
| s3 | 31.561 | `fade #s3f` +19.40 (·0.5) → 51.461 | **51.46** |
| s4 | 53.153 | `fade #s4f` +18.60 (·0.5) → 72.253 | **72.25** |
| s5 | 74.041 | `pop #s5q` +17.60 (·0.7) → 92.341; pulse 92.941 | **92.95** |
| s6 | 94.98 | `pop #s6u2` +17.20 (·0.5) → 112.68 | **112.68** |
| s7 | 115.607 | `pop #s7q` +22.50 (·0.7) → 138.807; pulse 139.007 | **139.05** |
| s8 | 141.431 | `rise #s8f` +14.80 (·0.7) → 156.931 | **156.95** |
| s9 | 160.281 | `pop #s9cta` +12.80 (·0.6) → 173.681; pulse 175.381 | **175.40** |

My first s2 shot at 28.06 was the *start* of `#s2sub`'s rise, so `#s2sub` was at opacity 0 —
re-shot at 28.80. **A last-cue frame must be the cue's completion, not its trigger**; the
0.7s `rise` default makes the difference between 6 and 7 elements on screen.
Plus one diagnostic frame at **137.10** (s7 before the cut-in fades in).

## The defect — s7 cut-in is a car key, under a home-loan payoff

`assets/img/s7-cut.jpg.src` reads **`house key`**. The delivered file is a **car key remote
fob** (flip-key blade + black plastic remote body, on a keyring on a bamboo mat). Opened the
source JPG directly to confirm — it is unambiguous.

It is not a small inset. `#s7cut` carries `class="bg"`:

```html
<div data-layout-allow-overflow class="bg" id="s7cut" style="background-image: url(assets/img/s7-cut.jpg); opacity: 0"></div>
```

so it is **full-bleed and it replaces the blueprint entirely**:

- `fade("#s7cut", S.s7 + 21.60, 0.5)` → on screen **137.21s**, fully opaque **137.71s**
- scene ends **141.431s** → **4.22s on screen**
- `pop("#s7q", S.s7 + 22.50)` → **"SAME HOUSE. DIFFERENT NUMBER." and the car keys share the
  frame for ~3.3s**, the fob the largest and sharpest object, directly above the words

This is the payoff of the video's biggest number (₹30,00,000 · 240 months · ₹3.3–4.5 lakh
extra interest — a **home** loan). The frame tells the viewer "car" while the type says
"HOUSE."

fin-build already saw the object and treated the symptom: the log records
`background-position: 22% center` applied "to keep the car fob out of 'SAME HOUSE'". The
crop moved the fob off the type; it did not stop it being a car key. **Cropping is not a fix
for the wrong subject.**

### The fix, and why it is the small one

Snapshot at **137.10** (below the cut-in's fade-in) shows `#s7 .bg` = `s7.jpg` = a
**blueprint** — the correct image for "SAME HOUSE", already in the project, already graded,
and *darker* behind the punch than the key photo is. Deleting the overlay is a better frame,
not a compromised one:

- remove the `#s7cut` div, its `fade(...)` and its `ken(...)` — three lines in `build.mjs`
- **no new asset, no asset round-trip, no re-source**
- precedent inside this same cut: `#s3cut` / `#s4cut` / `#s6cut` were all dropped at the
  asset stage and their scenes kept their `.bg`. `photo_free_scene_ratio` stays 0 — s7 still
  carries a full-bleed image, so the always-images rule holds.
- `#s7cut { background-position: 22% center; }` (line 49) goes with it

Re-sourcing an actual house key is the alternative and is strictly more work for the same
frame count.

## The other eight frames — pass

| Frame | Verdict |
|---|---|
| s1 · 16.80 | Amber "YOUR CREDIT REPORT", 3 rows, red stamp. Both `#s1cutA`/`#s1cutB` correctly gone (the double-exit fix holds). Archive-shelf bg. Clean. |
| s2 · 28.80 | Kicker + 4 chips + sub, all six present. Bg (old letters, twine) is the brightest plate in the video; see contrast table. |
| s3 · 51.46 | `300 —— 900` mega. Numerals span x≈260–1665, inside the 192/1728 title-safe box. Ledger bg. Clean. |
| s4 · 72.25 | 4 ranked rows, no percentage weights, `#s4f` names CIBIL. Clean. |
| s5 · 92.95 | 36-cell grid, 1 red cell, counter on its `--bg` panel bed (the structural contrast fix reads correctly), "ONE MISS = 36 MONTHS" x≈305–1620, in safe. Foot wraps to 2 lines with "history" alone on line 2 — cosmetic, not a gate finding. |
| s6 · 112.68 | Two lines over the pocket-watch plate. Darkest text plate in the cut; measured below. Passes. |
| s7 · 139.05 | **FAIL — see above.** Type/layout/number (`₹3.3 to 4.5 lakh`) are all correct; the image is not. |
| s8 · 156.95 | "DO THIS TODAY" + 2 numbered actions + foot. The `.swap` grid cell holds — no hole. The `brightness(.80)` pull works: green 40px now sits clearly over the document. |
| s9 · 175.40 | 4 recap chips + orange SUBSCRIBE. Clean. |

- **Brand marks: none** in any of the 9 frames.
- **Phone screens: none.**
- **Currency: ₹ throughout, lakh-grouped** (`₹30,00,000`, `₹1,390 to ₹1,860`, `₹3.3 to 4.5
  lakh`). No `$`, no US framing anywhere — correct for the India cut.
- **Safe area: 9/9.** Widest elements measured: s3 mega 260→1665, s5 verdict 305→1620,
  s7 punch 480→1450. Title-safe box is 192→1728.

## Contrast — measured, not eyeballed

Backdrop sampled straight off my own PNGs (`ffmpeg crop → scale=1:1:flags=area`), contrast
computed against the token colour by the WCAG 2.x relative-luminance formula. **The sampled
band includes the glyph pixels**, so for light-on-dark text the true backdrop is darker and
the real ratio is *higher* than the figure shown — read these as lower bounds.

| Element | Colour | Size/weight | Backdrop RGB | Ratio | AA-large (3:1) |
|---|---|---|---|---|---|
| `#s2sub` | `--muted` #98a2b3 | 40px/800 | 82,84,87 | **≈2.95** | lower bound — passes once glyphs are excluded |
| `#s4f` | `--muted` | 26px/700 | 69,77,84 | **≈3.33** | pass |
| `#s6u` | `--muted` | 40px/800 | 54,83,72 | **≈3.07** | pass |
| `#s6u2` "not the minimum" | `--muted` | 40px/800 | 72,82,87 | **≈3.11** | pass |
| `#s7f` | `--muted` | 26px/700 | 59,58,65 | **≈4.36** | pass |
| `#s7q` | `--warn` #ef4444 | 88px/900 | 70,65,66 (clean patch, no glyphs) | **≈2.66** | **below** |

`#s7q` is the one real number below the line, and it is a *clean* patch — not a lower bound.
I am **not** gating on it:

- it is legible with wide separation at 1:1 (cropped and inspected, not judged off a
  downscale — the downscaled view badly misreads that plate as bright);
- the shared `text-shadow: 0 2px 22px rgba(0,0,0,.7), 0 1px 4px rgba(0,0,0,.55)` on `.huge`
  is real contrast the formula cannot see;
- `hyperframes check` scored 22/22 AA with its own backdrop sampler;
- and the frame is being rebuilt anyway. **When s7 loses the key overlay the blueprint plate
  behind the punch is darker still, so this number improves for free.** Worth re-measuring on
  attempt 2 rather than tuning now — and `--warn` must not be lightened (fin-build's
  reasoning on `#s5ctr` was right and applies here).

## Not run this invocation

Render, transcription drift, peak dBTP, blackdetect, runtime-vs-`timing.json` — all of it is
invocation 2, and none of it can start until the encode exists. Target runtime is
**177.642s**; `renders/` does not exist yet.

## Sign-off

- [x] 9/9 last-cue frames captured at independently derived times and looked at
- [x] Safe area 9/9 · brand marks 0 · phone screens 0 · currency correct (₹, lakh-grouped)
- [x] Contrast measured on all 6 muted/warn-over-photo elements, numbers recorded
- [ ] **s7 cut-in — car key under a home-loan payoff. One build retry available.**
- [ ] Encode (orchestrator's, after the rebuild)
