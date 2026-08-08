"""one-number-travels — two equally true figures. One is picked up and copied
everywhere; the other sits exactly where it started.

For VO 2.10: «दोनों आँकड़े सच हैं। पर इंटरनेट सिर्फ़ बड़ा वाला उठाता है, क्योंकि
छोटा वाला बिकता नहीं।»

Why this is drawn and not photographed
--------------------------------------
The beat is a COMPARISON of REACH, which is not a thing a camera can point at.
The slot shipped as a stack of newspapers, and the editor killed it twice over
(editor-hi-ch2-2, blocker 1): the print in it is legibly GERMAN — "Institut für
Stadtgeschichte", "Frankfurter Schule", Frankfurt phone numbers — inside a
chapter built entirely on Japan's own two published figures, and a side-on stack
of classified listings says "old newsprint", not "one number travels".
format.json `vector_art.lottie.reach_for_it_when` is explicit that a comparison
no photograph states is a FAIL as a flat photo, not a missed opportunity.

What is drawn, and what is deliberately NOT
-------------------------------------------
Two identical tokens. Identical is the whole design: the kicker over this frame
reads BOTH ARE TRUE, so the asymmetry the art draws is REACH — one multiplies,
one does not — and never magnitude. Drawing 37.8 and 1.1 to scale is s17's job,
it already did it two scenes ago, and repeating that vocabulary here would both
restate a point already made and quietly re-assert a size comparison under a line
that is about circulation.

Nothing here is a measurement, so nothing here may look like one:

* No text. `lottie_gen` has no text primitive, which is a convenience — a printed
  37.8% on a frame this loose would be a figure without its source.
* The copy count is 22. NOT 30 and NOT 34: those are the real ratio (37.8/1.1 =
  34.4, "more than 30 times", Horioka p.7) and a countable 30 copies here would
  read as that published ratio restated by a frame that is not measuring
  anything. 22 is chosen to be unmappable onto any figure in the video.
* The copies overlap and vary in size, so the eye reads "spread" and is never
  invited to count them. That is the same defect class as the 44/108 grid in
  who-is-counted.py — a decorative proportion that reads as a statistic.

The one that stays gets a single contained pulse at the moment the other starts
multiplying: it is not inert or still loading, it is being passed over. "छोटा
वाला बिकता नहीं" — the small one doesn't sell.

  python3 assets/lottie/src/one-number-travels.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../../.claude/skills/lottie-master/scripts"))
from lottie_gen import (Lottie, rect, fill, group, transform, animated)  # noqa: E402

W, H, FPS, DUR = 1000, 520, 30, 120       # 4.0s, same as the other three

TOK_W, TOK_H, TOK_R = 92, 58, 10          # one "figure" as it circulates: a card
ORIGIN_Y = 200                            # both tokens sit on the same line, low
LEFT_X, RIGHT_X = -250, 250
RULE_Y = 240                              # the line they both start from

# The copies live in a band ABOVE the origin row and never touch it. First cut
# scattered them over the whole left half INCLUDING the origins' own y, which
# buried the red original inside its own spread — the frame then read as "a red
# blob and one stray grey chip" rather than as two tokens that started level and
# only one of which went anywhere. The gap between the two zones is what carries
# the sentence, so it is a layout constant, not slack.
SPREAD_X = (-500, -30)                    # left half only: the right token's
SPREAD_Y = (-235, 60)                     # territory stays visibly untouched

WARN = "#ef4444"                          # --warn: the number that travels
MUTED = "#98a2b3"                         # the one that doesn't
COPIES = 22                               # see the caveat above — not 30, not 34


def fade(start, end, peak=100):
    return animated([(0, 0, "hold"), (start, 0, "easeOut"), (end, peak), (DUR, peak)])


def arrive(start, end, to=100):
    """A copy lands: scales up from nothing with a little overshoot settle."""
    return animated([(0, [0, 0], "hold"), (start, [0, 0], "easeOutCubic"),
                     (end, [to * 1.08, to * 1.08], "easeOut"),
                     (end + 6, [to, to]), (DUR, [to, to])])


def _lcg(n, seed=20260805):
    """Deterministic pseudo-random stream. Math.random is banned anywhere near a
    render; the sequence matters only in that it is stable across them."""
    x, out = seed, []
    for _ in range(n):
        x = (x * 1103515245 + 12345) % (1 << 31)
        out.append(x / (1 << 31))
    return out


# Scatter the copies across the LEFT half only. Splitting the field is what makes
# the read unambiguous: same token, same starting line, one side fills and the
# other stays at one. Letting the copies drift over the right half would put the
# spread on top of the thing that is supposed to be untouched by it.
r = _lcg(COPIES * 3)
spread = []
for i in range(COPIES):
    x = SPREAD_X[0] + r[i * 3] * (SPREAD_X[1] - SPREAD_X[0])
    y = SPREAD_Y[0] + r[i * 3 + 1] * (SPREAD_Y[1] - SPREAD_Y[0])
    sc = 52 + r[i * 3 + 2] * 46            # 52-98%: varied, so counting is not invited
    t = 24 + i * 2.9                       # a rolling cascade, not a single pop
    spread.append(group([rect(size=(TOK_W, TOK_H), roundness=TOK_R),
                         fill(WARN, opacity=fade(int(t), int(t) + 7, 70))],
                        tr=transform(position=(x, y),
                                     scale=arrive(int(t), int(t) + 11, sc))))
a = Lottie(width=W, height=H, fps=FPS, duration_frames=DUR, name="one-number-travels")
a.shape_layer(spread, tr=transform(position=(W / 2, H / 2)), name="copies")

# The line both tokens start from. Without it they are two chips floating at the
# same height by coincidence; with it they are two entries on one register, which
# is what "BOTH ARE TRUE" needs the eye to accept before the asymmetry lands.
a.shape_layer([group([rect(size=(760, 3)), fill(MUTED, opacity=fade(0, 8, 26))],
                     tr=transform(position=(0, RULE_Y)))],
              tr=transform(position=(W / 2, H / 2)), name="rule")

# The two originals, drawn last so they sit above the spread they threw off.
a.shape_layer([group([rect(size=(TOK_W, TOK_H), roundness=TOK_R),
                      fill(WARN, opacity=fade(6, 16, 96))],
                     tr=transform(position=(LEFT_X, ORIGIN_Y)))],
              tr=transform(position=(W / 2, H / 2)), name="travels")

# Passed over, not inert: one contained pulse on the frame the other starts
# multiplying, and then nothing for the remaining 3.2s.
a.shape_layer([group([rect(size=(TOK_W, TOK_H), roundness=TOK_R),
                      fill(MUTED, opacity=fade(6, 16, 92))],   # 82 -> 92: editor ch2-3 note
                     tr=transform(position=(RIGHT_X, ORIGIN_Y),
                                  scale=animated([(0, [100, 100], "hold"),
                                                  (24, [100, 100], "easeOut"),
                                                  (32, [104, 104], "easeIn"),
                                                  (44, [100, 100]),
                                                  (DUR, [100, 100])])))],
              tr=transform(position=(W / 2, H / 2)), name="stays")

out = os.path.join(os.path.dirname(__file__), "..", "one-number-travels.json")
a.save(os.path.abspath(out), minify=False)
print("wrote", os.path.abspath(out), a.op, "frames @", a.fr, "fps",
      f"| {COPIES} copies left, 1 right")
