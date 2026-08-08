"""two-rates-30x — two bars from the same government, the same year: 37.8% and
about 1.1%. The second is a sliver next to the first.

For VO 2.7: «एक ही देश, एक ही साल, एक ही सरकार — और तीस गुना से भी बड़ा फ़र्क़।»

This one is a correction, not a decoration. The shipped cut illustrated a
THIRTY-TIMES gap with a photograph of a balance scale whose two pans sit level —
a picture that says "equal" under a line that says "thirty times apart". Bars are
the only honest read: the ratio is the whole point, so the frame has to be drawn
to scale or it is lying.

Heights ARE the data. 37.8 -> 340px, 1.1 -> 9.9px, one px per 0.1113pp. The
sliver is meant to look almost absent; that is what 1.1% next to 37.8% is.

Sources (facts-staging J1/J2/J3): 37.8% = Statistics Bureau, Kakei Chosa 2024
annual, Table I-2-2, salaried-worker households. ~1.1% = National Accounts (SNA)
household saving rate, calendar 2024, per Horioka, NBER WP 33181 p.7.
37.8 / 1.1 = 34.4, which is what lets the scene say "more than 30 times" (J3,
verbatim from Horioka p.7).

⚠ J1 carries a display rule: the DECIMAL 1.1 is single-sourced (Horioka quoting
the Cabinet Office), so the video must "say about one percent, show ~1%". The
frame obeys that — the DOM `num` reads ABOUT 1% and no decimal is printed
anywhere. This bar is nonetheless drawn at 1.1, not at a rounded 1.0, because a
height is not a printed figure: at 9.9px against 340px nobody reads a decimal off
it, and rounding the geometry would make the ratio less true, not more careful.
If J1 ever hardens to a different decimal, change it here — the height is data.

  python3 assets/lottie/src/two-rates-30x.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../../.claude/skills/lottie-master/scripts"))
from lottie_gen import (Lottie, rect, fill, group, transform, animated)  # noqa: E402

W, H, FPS, DUR = 1000, 560, 30, 120       # 4.0s

BASE_Y = 210                              # y of the baseline, in shape-local space
SCALE = 340 / 37.8                        # px per percentage point — the honest bit
BAR_W = 132
GAP = 300

TARGET = "#22c55e"                        # --target: the two published rates
WARN = "#ef4444"                          # --warn: the gap between them
RULE = "#2a3241"
MUTED = "#98a2b3"


def grow(h_px, start, end):
    """A bar grows from the baseline: scale y 0 -> 100 with the anchor at its foot."""
    return animated([(0, [100, 0], "hold"), (start, [100, 0], "easeOutCubic"),
                     (end, [100, 100]), (DUR, [100, 100])])


def fade(start, end, peak=100):
    return animated([(0, 0, "hold"), (start, 0, "easeOut"), (end, peak), (DUR, peak)])


def bar(x, pct, colour, start):
    """One bar, anchored at its foot so growth reads as rising from the rule."""
    h = pct * SCALE
    return group([rect(size=(BAR_W, h)), fill(colour, opacity=fade(start, start + 4, 88))],
                 tr=transform(anchor=(0, h / 2), position=(x, BASE_Y),
                              scale=grow(h, start, start + 22)))


a = Lottie(width=W, height=H, fps=FPS, duration_frames=DUR, name="two-rates-30x")

# NO measurement bracket. Two versions were built and both were cut, and the
# reason is geometric rather than aesthetic: 1.1% is 9.9px of a 340px bar, so the
# distance between the two bar tops IS the big bar, to within 3%. A bracket
# spanning that gap is therefore drawing a second outline around a bar that is
# already the most visible thing on screen — v1 (offset to the right of the small
# bar) read as a stray red line beside the chart, v2 (leaders into a centre line)
# read as a red step-outline hugging the big bar. Neither failed on placement;
# they failed because there is no gap to point at that isn't the bar itself.
#
# The comparison is carried by the two heights and by the DOM `num` ("30 TIMES")
# over them. Adding a third element to restate it is what made the frame busy.
# If a callout is ever wanted here, the thing to draw is 30 stacked copies of the
# small bar reaching the big one — that shows the ratio instead of re-outlining it.

# The two bars. 37.8 first (the claim), then ~1.1 (what the same government's
# other book says) — the beat only lands if the big one is established first.
a.shape_layer([bar(-GAP / 2, 37.8, TARGET, 8), bar(GAP / 2, 1.1, TARGET, 46)],
              tr=transform(position=(W / 2, H / 2)), name="bars")

# Baseline.
a.shape_layer([group([rect(size=(760, 3)), fill(RULE, opacity=fade(0, 8, 100))],
                     tr=transform(position=(0, BASE_Y)))],
              tr=transform(position=(W / 2, H / 2)), name="rule")

# Two faint plinths under each bar so an empty baseline still reads as two slots.
a.shape_layer([group([rect(size=(BAR_W, 8), roundness=4),
                      fill(MUTED, opacity=fade(0, 8, 18))],
                     tr=transform(position=(x, BASE_Y + 12)))
               for x in (-GAP / 2, GAP / 2)],
              tr=transform(position=(W / 2, H / 2)), name="plinths")

out = os.path.join(os.path.dirname(__file__), "..", "two-rates-30x.json")
a.save(os.path.abspath(out), minify=False)
print("wrote", os.path.abspath(out), a.op, "frames @", a.fr, "fps",
      "| 37.8 ->", round(37.8 * SCALE, 1), "px, 1.1 ->", round(1.1 * SCALE, 1), "px")
