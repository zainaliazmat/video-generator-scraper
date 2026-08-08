"""who-is-counted — a grid of households. A minority lights up (salaried, the
37.8% survey), then the rest light up too (everyone, the national accounts).

For VO 2.9: «सैंतीस वाला आँकड़ा सिर्फ़ नौकरीपेशा परिवारों का है, दूसरा सबका —
बुज़ुर्ग, बेरोज़गार, दुकानदार, सब।»

The whole debunk turns on this and nothing else: the two rates disagree because
they count different populations. The shipped cut put a cherry-blossom branch
here, which says nothing at all. A subset inside a set is the one picture that
carries the argument, and it is a shape, not a photograph — so it gets drawn.

The lit share is NOT a published statistic and must never be read as one:
salaried households are simply a minority of all households. It is a proportion
that reads as "some of these, not all", nothing more. No figure is printed on
this frame for exactly that reason — the numbers live in the DOM `num` and the
`foot` citation, where they can be sourced.

That caveat used to live here and NOWHERE ELSE, which was the bug. LIT was 44 of
108 — 40.7% — sitting directly under a stmt reading "37.8% counts salaried
households only", and once the grid became legible (the band, editor ch2-1) a
viewer could count it and land on the number two lines above. A comment in a
Python file does not travel to the screen. Moved to 28 (25.9%) on the editor's
finding, 2026-08-05: far enough from 37.8% that no one can read one as the other,
and still a clear minority, which is the half of the argument this frame carries.
Moving it UP to ~60 would have worked arithmetically and broken the picture —
"everyone" has to arrive as an obvious increase.

Do not "improve" this by making it equal 37.8%. That figure is a share of
disposable INCOME saved, not a share of households; a grid of households at 37.8%
would be a fabricated statistic dressed as a real one.

  python3 assets/lottie/src/who-is-counted.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../../.claude/skills/lottie-master/scripts"))
from lottie_gen import (Lottie, ellipse, fill, group, transform, animated)  # noqa: E402

W, H, FPS, DUR = 1000, 520, 30, 135       # 4.5s

COLS, ROWS = 18, 6                        # 108 households
DOT = 26
STEP_X, STEP_Y = 52, 74
LIT = 28                                  # "some of these" — see the caveat above

TARGET = "#22c55e"                        # the salaried subset the 37.8% counts
MUTED = "#98a2b3"                         # everyone else
GRID_W = (COLS - 1) * STEP_X
GRID_H = (ROWS - 1) * STEP_Y


def fade(start, end, peak=100):
    return animated([(0, 0, "hold"), (start, 0, "easeOut"), (end, peak), (DUR, peak)])


def dot_xy(i):
    r, c = divmod(i, COLS)
    return -GRID_W / 2 + c * STEP_X, -GRID_H / 2 + r * STEP_Y


# Which cells are "salaried". Spread across the grid rather than clumped in the
# first rows: a solid block would read as a bar chart and invite measuring it.
#
# A fixed stride — the first cut's `(i * 108 // LIT) % 108` — spreads them, but
# an 18-wide grid and a stride of 2.45 beat against each other and produced
# visible diagonal stripes. That reads as a designed texture, which is exactly
# what this frame must not look like: the whole point is "some of these, no
# pattern to it". Scattered by a seeded LCG instead — deterministic, because a
# render must be reproducible and Math.random is banned anywhere near one, but
# with no structure for the eye to lock onto.
TOTAL = COLS * ROWS


def _scatter(total, k, seed=20240801):
    """k of `total` indices, deterministically shuffled. Plain LCG — the sequence
    matters only in that it is stable across renders."""
    x, keys = seed, []
    for _ in range(total):
        x = (x * 1103515245 + 12345) % (1 << 31)
        keys.append(x)
    return set(sorted(range(total), key=lambda i: keys[i])[:k])


lit = _scatter(TOTAL, LIT)

a = Lottie(width=W, height=H, fps=FPS, duration_frames=DUR, name="who-is-counted")

# Pass 2 — everyone else joins. The "other counts everyone" half of the line.
rest = []
for i in range(TOTAL):
    if i in lit:
        continue
    x, y = dot_xy(i)
    t = 74 + (i % COLS) * 1.6                 # sweeps left to right
    rest.append(group([ellipse(size=(DOT, DOT)),
                       fill(MUTED, opacity=fade(int(t), int(t) + 10, 72))],
                      tr=transform(position=(x, y))))
a.shape_layer(rest, tr=transform(position=(W / 2, H / 2)), name="everyone-else")

# Pass 1 — the salaried subset only. These are the households the 37.8% is
# calculated over, and for the first 2.5s they are the only thing lit.
sub = []
for i in sorted(lit):
    x, y = dot_xy(i)
    t = 10 + (i % COLS) * 1.4
    sub.append(group([ellipse(size=(DOT, DOT)),
                      fill(TARGET, opacity=fade(int(t), int(t) + 10, 92))],
                     tr=transform(position=(x, y))))
a.shape_layer(sub, tr=transform(position=(W / 2, H / 2)), name="salaried")

# The full set, held very faint from frame 0 so the subset reads as part of a
# whole rather than as scattered marks on an empty frame.
ghost = [group([ellipse(size=(DOT, DOT)), fill(MUTED, opacity=fade(0, 12, 12))],
               tr=transform(position=dot_xy(i)))
         for i in range(TOTAL)]
a.shape_layer(ghost, tr=transform(position=(W / 2, H / 2)), name="all-households")

out = os.path.join(os.path.dirname(__file__), "..", "who-is-counted.json")
a.save(os.path.abspath(out), minify=False)
print("wrote", os.path.abspath(out), a.op, "frames @", a.fr, "fps",
      f"| {LIT}/{COLS * ROWS} lit")
