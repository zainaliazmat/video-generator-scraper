---
summary: fin-render gate-two FRAME CHECK, en cut, attempt 1 — FAIL. All 92 scene frames captured at native 1920x1080 and inspected at 1:1. Three blocking findings: s21 legible Polish "SUMA PLN" on a dollar cut, s57 the same banknote serial E 34112707 E twice in one frame (prop money), s91 a plainly legible "Kaweco AL Sport Germany" brand mark in the CTA. The escalated s59 minor is CLEARED on measurement — 2.09 px per character, static panel, does not resolve at 1080p. No encode was run.
updated: 2026-07-31
source: studio/videos/first-lakh-first-thousand-en/snapshots/qa3/{b1..b8,z11,z21,z59min,z11_*,s21max,meas} (92 frames + 9 zoom/measurement captures)
stage: fin-render, cut en, attempt 1 — invocation 1 of 2 (frame check only)
---

# fin-render — «The First $10,000 Is The Hardest» en, attempt 1 — GATE TWO: FAIL

**No encode was run.** Per the orchestrator scope this invocation is the frame check only.
`renders/` does not exist and must not be created until fin-build lands a fix.

89 of 92 frames pass. Three scenes block, all image swaps — no composition change is needed.

## Method

- Snapshot times were **not** taken on trust. Every `rise`/`fill`/`fade`/`shove`/`dissolve`
  cue was re-parsed out of the inline script per scene (excluding `ken`) and each scene's last
  cue end computed. All 92 values in `snapshots-at.txt` fall inside their own scene AND land
  within 1.2 s of that last cue. **0 mismatches.** Reused as-is.
  Composition runtime from `timing.json`: **505.561 s**, 92 scenes.
- Captured all 92 into `snapshots/qa3/b1…b8`, **8 separate `-o` dirs, none reused** (the CLI
  wipes its `-o` dir on every run). Every frame is native **1920x1080 rgb24** — snapshots come
  out at delivery resolution, so 1:1 inspection is exact, not a proxy.
- `Navigation timeout of 10000 ms exceeded` fired as expected; the retry loop absorbed it.
  Attempts per batch: b1-b4, b7, b8 = 1; b5 = 2; b6 = 3; z11_52.35 = 3; z21 = 1; z11_565 = 6.
  Every dir on disk is the run that succeeded.
- **Every one of the 92 was read at full resolution.** No contact sheet was used as evidence.
- Automated pre-pass before the eyes: per-8x8-block flat-black scan (block mean <= 20 AND
  block std <= 1.5) with a largest-rectangle DP over all 92 frames, to make sure no dead region
  could hide behind a tired reviewer. Results interpreted below.

## Blocking findings

### 1. s21 — legible `SUMA PLN` (Polish zloty) on a dollar cut

| | |
|---|---|
| Window | **108.630 – 114.791 s** (6.161 s) |
| On screen | bar `SAME INPUT` · focal **`$800 a month · nothing else changes`** |
| File | `assets/img/s21.jpg` |
| What it is | a Polish fiscal receipt (`PARAGON`-style) among receipts and a calculator |

At 3x the receipt reads **`SUMA PLN`** ("TOTAL PLN") plus Polish body text. The scene has a
zoom-in ken (`ken("#s21-img", 108.630, 5.711, true)` → scale 1.0 → 1.16), so it is largest at
the ken maximum, ~114.3 s. **Measured there, directly on the native 1080p frame** (not scaled
back from the 3x crop):

```
"SUMA PLN" ink bbox on the delivered frame : 63 x 34 px
per-character width                        : 7.9 px
ink/paper contrast                          : 38/255
```

At true 1:1 (crop shown unmagnified) the line reads. This is the same defect class that took
the hi cut's s1 and s79 (`ZŁOTYCH`, `1 ZŁOTY`) — a foreign currency total sitting under a
caption that names the amount in dollars. **It is 3.8x more legible than the sterling item
being cleared below**, which is the whole reason that one ships and this one does not.

### 2. s57 — the same banknote serial twice in one frame (prop money)

| | |
|---|---|
| Window | **305.894 – 313.178 s** (7.284 s) |
| On screen | bar `20% OF $4,000` · focal **`$800`** |
| File | `assets/img/s57.jpg` |

Two separate notes in frame carry the identical serial **`E 34112707 E`** (Richmond district E,
`SERIES 2003`, John W. Snow) — the composite was built by repeating one scanned bill. Verified
by cropping both instances from the native frame: the left note shows `…12707E`, the right note
shows the full `34112707E`. The serial run measures **254 px** diagonally on the delivered frame,
~28 px per character, high-contrast green on pale paper — legible without pausing.

This is exactly the tell the brief named (`LB45440078L` on the hi cut), and it lands on a hero
money frame carrying the video's core input figure.

### 3. s91 — `Kaweco AL Sport Germany` brand mark in the CTA frame

| | |
|---|---|
| Window | **496.307 – 500.248 s** (3.941 s) |
| On screen | bar `—` · focal **`SUBSCRIBE`** |
| File | `assets/img/s91.jpg` |

A fountain pen laid on a leather notebook, engraved **`Kaweco AL Sport`** + `Germany`, white on
black, in focus, dead centre-right of the band.

```
brand-mark region on the delivered frame : 270 x 90 px
luma range (contrast)                    : 157/255
```

Plainly legible at 1:1. A named commercial brand held on screen for the full call-to-action is
the one place in the cut where an unintended product endorsement is most costly.

## The escalated item — DECIDED: s59's minor SHIPS

**The standard applied: legibility at 1080p delivery resolution, measured, not estimated.**

`#s59-min` is `assets/img/s11.jpg`, placed by `.v-ap-min` at 630x600 px, showing the source
(1780x1300) at 0.462x. Its lower-left carries a GBP/EUR revenue chart with a
`£20,000,000 / £15,000,000 / £10,000,000 / £5,000,000` axis and an *MTD revenue by currency*
column listing `GBP USD EUR BRL AUD SGD CZK CNH CAD ZAR`.

Measured on the axis labels:

```
"£15,000,000"  ink bbox 69 x 26 px at 3x  ->  23.0 x  8.7 px at 1080p  ->  2.09 px / character
"£10,000,000"  ink bbox 69 x 22 px at 3x  ->  23.0 x  7.3 px at 1080p  ->  2.09 px / character
£ glyph itself                            ->  approx 2 x 4 px at 1080p
ink/paper contrast                        ->  61/255
```

**`#s59-min` carries no ken.** The composition emits only `ken("#s59-img", 319.197, 5.345, false)`
— there is no tween on the minor at all, so the panel is static for the whole 5.795 s scene and
**2.09 px/character is its maximum, not a sample.** Confirmed visually two ways on the delivered
pixels: at true 1:1 the chart is grey mush, and at 8x nearest-neighbour magnification (every
encoded pixel shown as an 8x8 block, no interpolation inventing detail) there is no glyph
structure — no `£`, no digits, no column labels. **It does not resolve at 1080p. It ships.**

### The near miss that is worth writing down

`assets/img/s11.jpg` is used **twice**: as this illegible 630 px minor, and as the **full-bleed
background of s11** (52.251 – 58.099 s), where the 1920x676 band shows the same source at
**1.079x — 2.3x larger than in the minor**. Had the sterling axis fallen inside that band it
would have rendered at roughly 4.8 px/character, which is a different conversation.

It does not. Checked the s11 band at 3x at scene start (52.35 s), at the last-cue frame (53.8 s)
and late (56.5 s, 57.95 s): the band is a vertical crop through the banknotes and the upper
reports and **never reaches the charts at any point in its ken**. s11 is clean — every note in it
is US (`I 04332426 A`, `MD 67703056 B`, `ME 69440730 B`, `MB 73054568 A`, all distinct).

**Lesson for the next cut:** in a mosaic, `#sN-min` can be a *different scene's* image file.
A per-file audit ("where else does this asset appear, and at what scale?") catches what a
per-scene audit misses. One file here was simultaneously a pass and a near-fail.

## The six replaced slots — all confirmed clean at 1:1 delivery resolution

| slot | window | verdict at 1080p |
|---|---|---|
| **s1** | 0.000 – 5.240 s | worn US singles, `AMERICA`, green Treasury seal, distinct serials. **Clean** |
| **s2** | 5.240 – 10.590 s | fan of $100s, `FEDERAL RESERVE SYSTEM`, `Treasurer of the United States`. No crypto prop anywhere. **Clean** |
| **s36** | ~193 – 199 s | `UNITED STATES OF AMERICA`, `FEDERAL RESERVE NOTE`, `ONE DOLLAR`, Washington, `WASHINGTON, D.C.`, serial `B57053322`; second note's serial differs. **The attempt-1 CANADA / 5 CENTS blocker is closed — the BEA 2.7 % statistic now sits on US currency.** |
| **s59** major | 319.197 – 324.992 s | banded US roll, no denomination and no foreign marking legible. **Clean** (minor ruled above) |
| **s84** | ~455 – 461 s | plain blue pen on a form; no `Credit Card/Debit Card Authorization`, no brand, no product. **Clean** |
| **s88** | 480.67 s cue | rice / buckwheat / oats jars, currency-neutral. **Clean** |

Layout on all six is correct: `.stack` inside the safe area, bar + rule + focal + foot present,
one focal per scene, nothing overflowing.

## Flat-black scan — no frame loses a region to a rendering failure

The strict scan (block mean <= 20 AND block std <= 1.5) returns a recurring **592 x 1288 px rect
at YAVG 15.90, std 0.42** on 17 frames (s4, s12, s20, s24, s30, s33, s37, s41, s45, s50, s55,
s61, s65, s72, s77, s81, s84) and 160 x 1920 bands on 9 more. **Looked at, all of them are the
blockframe design's own dark text panel and its top/bottom rules** — they carry the bar, focal
and foot type. Design, not damage.

Two frames with genuinely large dark areas, both checked by eye and both photographic:

```
s48   584 x 872 px flat-black   — lit wicker basket present in frame; black studio backdrop
s90   760 x 1080 right region   YAVG 3.65  std 24.70  (97.0% of pixels <= 16)
      s90 image-band portion    YAVG 5.76  std 31.16  — smoke and flame present; black-bg photo
```

Neither is the hi cut's s17 failure mode (an un-toned region where an image should have been,
767 x 1080 at YAVG 16.03). In both of these the subject is lit and rendered inside the region;
the blackness is the photograph's own background. **Not blocking.** s90 is aesthetically thin —
the right third is nearly empty — and is worth a swap if a rebuild happens anyway.

## Non-blocking observations (recorded, no action required)

- **s13, s38-min** — bilingual / trilingual wall calendars (`November / Novembre`,
  `September / Septembre / Settembre`). Legible, non-currency; a Canada / Swiss tell only to a
  viewer looking for one.
- **s14** — European number formatting (`0,06`, `−76,45`, `1 145 869` with space separators) on a
  stock table captioned with the S&P 500 / "the US market". Legible, but carries **no currency
  symbol**, so it is outside the reject classes. Softest of the market tells; flagging it because
  a future sweep will find it again.
- **s26 `MOBA TIME`, s79 `STAIGER`** — clock-dial maker names, legible, benign set dressing.
- **s86 `Panasonic` (x3) + `10A 250V`** — a named brand and a non-US mains voltage, but both are
  embossed white-on-white plastic: contrast **72/255** and **103/255**, std 6.8 / 9.8. They do not
  resolve at 1:1. Non-blocking under the stated standard; a market tell if the shot is ever redone.
- **s29** Turkish book text, **s62** an English-translated Ukrainian tax certificate (upside down,
  largely sub-legible). Foreign-language documents, no currency.
- **s54** Converse star patch, **s71** Irish/UK doors (`APARTMENT No. 1`), **s92** European
  guardrail — locale / brand set dressing, all sub-threshold.
- **s24** apothecary drawers (`Acriflavine`, `Pills Asafoetida`) under `$90,000 → $100,000` —
  keyword drift, as fin-build flagged. Reads as generic archive texture.
- **s51, s82** — near-empty texture backgrounds (wood grain, dark plaster). Weak, not defective.
- **s91's title bar renders as a lone em-dash.** The composition sets `s91-bar` to literally `—`,
  so a full-width black bar carries one short white dash. It is intentional in the build, but on
  screen it reads as a title that failed to load. Cosmetic; worth a decision since s91 is being
  reworked anyway.

## Verdict

**FAIL.** Three image swaps: **s21** (Polish `SUMA PLN` under a dollar caption), **s57**
(repeated serial `E 34112707 E`), **s91** (`Kaweco AL Sport Germany` in the CTA).
The escalated **s59 minor is cleared and ships** at a measured 2.09 px/character on a static panel.

This is fin-build's one retry for the en cut. A second bad frame set is terminal.
