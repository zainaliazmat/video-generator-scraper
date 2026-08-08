"""stats-table-row — a printed statistics table drawing itself, one row lifting
out of it.

For VO 2.3 / 2.5 — the Kakei Chosa table the 37.8% is actually read off.

Four stock searches for a statistics table returned camera lenses, reading
glasses, wine glasses, dominoes and strawberries; the shipped cut's pick is an
out-of-focus book. A table is ruled lines and blocks of figures, which is a thing
to draw, not a thing to photograph — and drawing it means the row the voice names
is the row that lights up, which no stock photograph can promise.

Deliberately abstract: bars stand in for digits, no glyphs. Inventing legible
Japanese figures on a frame cited to Table I-2-2 would be fabricating a source
document. The real numbers are set in the DOM `num` and `foot`, where the
citation sits with them.

Used twice in chapter 2 — s13 (the claim) and s15 (the survey it comes from),
which the storyboard already calls "the same table, wider".

  python3 assets/lottie/src/stats-table-row.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../../.claude/skills/lottie-master/scripts"))
from lottie_gen import (Lottie, rect, fill, group, transform, animated)  # noqa: E402

W, H, FPS, DUR = 1040, 560, 30, 120       # 4.0s

ROWS, COLS = 7, 5
ROW_H, ROW_GAP = 54, 12
COL_W, COL_GAP = 150, 28
HERO = 3                                  # the row the line is about (0-based)

INK = "#f5f3ec"
MUTED = "#98a2b3"
RULE = "#2a3241"
TARGET = "#22c55e"

TABLE_W = COLS * COL_W + (COLS - 1) * COL_GAP
TABLE_H = ROWS * ROW_H + (ROWS - 1) * ROW_GAP
X0 = -TABLE_W / 2 + COL_W / 2
Y0 = -TABLE_H / 2 + ROW_H / 2


def fade(start, end, peak=100):
    return animated([(0, 0, "hold"), (start, 0, "easeOut"), (end, peak), (DUR, peak)])


def row_y(r):
    return Y0 + r * (ROW_H + ROW_GAP)


a = Lottie(width=W, height=H, fps=FPS, duration_frames=DUR, name="stats-table-row")

# The highlight plate behind the hero row, plus a target-coloured spine on its
# left edge. Arrives after the table has finished setting, so the eye reads
# "a table" and only then "that row".
a.shape_layer(
    [group([rect(size=(10, ROW_H + 14), roundness=5),
            fill(TARGET, opacity=fade(66, 74, 100))],
           tr=transform(position=(X0 - COL_W / 2 - 24, row_y(HERO)))),
     group([rect(size=(TABLE_W + 48, ROW_H + 14), roundness=8),
            fill(TARGET, opacity=fade(62, 72, 13))],
           tr=transform(position=(0, row_y(HERO))))],
    tr=transform(position=(W / 2, H / 2)), name="hero-row")

# The figures — a bar per cell, widths varied so the columns read as numbers of
# different lengths rather than a grid of identical blocks. The hero row's cells
# are ink; every other row is muted.
cells = []
for r in range(ROWS):
    for c in range(COLS):
        w = COL_W - 30 - ((r * 7 + c * 13) % 4) * 16     # deterministic variation
        hero = r == HERO
        t = 14 + r * 5 + c * 2
        cells.append(group([rect(size=(w, 12), roundness=6),
                            fill(INK if hero else MUTED,
                                 opacity=fade(int(t), int(t) + 8, 78 if hero else 34))],
                           tr=transform(position=(X0 + c * (COL_W + COL_GAP)
                                                  + (w - COL_W) / 2 + 8, row_y(r)))))
a.shape_layer(cells, tr=transform(position=(W / 2, H / 2)), name="figures")

# Horizontal rules between rows, and a heavier one under the header.
rules = [group([rect(size=(TABLE_W + 24, 2)), fill(RULE, opacity=fade(6 + r * 3, 14 + r * 3, 72))],
               tr=transform(position=(0, row_y(r) + ROW_H / 2 + ROW_GAP / 2)))
         for r in range(ROWS - 1)]
rules.append(group([rect(size=(TABLE_W + 24, 4)), fill(RULE, opacity=fade(4, 12, 100))],
                   tr=transform(position=(0, row_y(0) - ROW_H / 2 - ROW_GAP / 2))))
a.shape_layer(rules, tr=transform(position=(W / 2, H / 2)), name="rules")

out = os.path.join(os.path.dirname(__file__), "..", "stats-table-row.json")
a.save(os.path.abspath(out), minify=False)
print("wrote", os.path.abspath(out), a.op, "frames @", a.fr, "fps",
      f"| {ROWS}x{COLS}, hero row {HERO}")
