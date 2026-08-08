"""calendar-20th-circled — a month grid where the days burn down and the 20th
gets ringed in red.

For VO 1.7: «और बीस तारीख़ आते-आते अकाउंट ऐसा दिखता है जैसे तनख़्वाह आई ही न हो।»
("and by the 20th the account looks like the salary never arrived").

Built rather than fetched because the shot does not exist: four stock searches
returned wall calendars whose visible date is never the 20th, and the shipped
cut's own pick reads "Tuesday 8" — a picture that argues with the line. A
generated grid is the only way the frame can say the number the voice says.

The ring is --warn: s7 is a `warn` scene (storyboard §7) and the 20th is the
drain arriving, not an action the viewer takes.

One-shot, holds at the end — playLottie runs loop:false.

  python3 assets/lottie/src/calendar-20th-circled.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../../.claude/skills/lottie-master/scripts"))
from lottie_gen import (Lottie, rect, ellipse, fill, stroke, group, trim,  # noqa: E402
                        transform, animated, static)

W, H, FPS, DUR = 900, 560, 30, 105        # 3.5s — the slot s7 has from +1.90

COLS, ROWS = 7, 5
CW, CH, GAP = 76, 62, 16
GRID_W = COLS * CW + (COLS - 1) * GAP     # 616
GRID_H = ROWS * CH + (ROWS - 1) * GAP     # 374
X0 = -GRID_W / 2 + CW / 2                 # centre of the top-left cell
Y0 = -GRID_H / 2 + CH / 2

TARGET = 20                               # the day the line names
PANEL = "#161b25"
EDGE  = "#2a3241"
INK   = "#f5f3ec"
MUTED = "#98a2b3"
WARN  = "#ef4444"


def arrive(start, end, peak=100):
    return animated([(0, 0, "hold"), (start, 0, "easeOut"), (end, peak), (DUR, peak)])


def cell_xy(i):
    """Day i (1-based) -> (x, y) of its cell centre, month starting on col 0."""
    r, c = divmod(i - 1, COLS)
    return X0 + c * (CW + GAP), Y0 + r * (CH + GAP)


a = Lottie(width=W, height=H, fps=FPS, duration_frames=DUR, name="calendar-20th-circled")

# ------------------------------------------------------------------- the ring
# Drawn last so it sits on top. `trim` sweeps the stroke on like a pen stroke;
# the ellipse is deliberately bigger and a touch rotated so it reads as drawn by
# hand around the cell, not as a shape snapped to it.
tx, ty = cell_xy(TARGET)
a.shape_layer(
    [group([ellipse(size=(CW + 34, CH + 30)),
            trim(start=0,
                 end=animated([(0, 0, "hold"), (62, 0, "easeInOut"), (86, 100), (DUR, 100)])),
            stroke(WARN, width=7, opacity=arrive(62, 68, 100))],
           tr=transform(position=(tx, ty), rotation=-4))],
    tr=transform(position=(W / 2, H / 2)), name="ring")

# ------------------------------------------------------------------ the drain
# Days 1..19 dim one after another — the money leaving a day at a time. The
# stagger IS the point, so each day carries its own two-frame offset.
drain = []
for i in range(1, TARGET):
    x, y = cell_xy(i)
    t = 30 + i                                   # ~0.03s apart, 1 -> 19
    drain.append(group([rect(size=(CW, CH), roundness=12),
                        fill(PANEL, opacity=arrive(t, t + 7, 82))],
                       tr=transform(position=(x, y))))
a.shape_layer(drain, tr=transform(position=(W / 2, H / 2)), name="drain")

# ------------------------------------------------------------------- the grid
# 31 day cells. The first 19 are ink (days you had money), the rest muted.
cells = []
for i in range(1, 32):
    x, y = cell_xy(i)
    t = 4 + i * 0.4
    lit = i < TARGET
    cells.append(group([rect(size=(CW, CH), roundness=12),
                        stroke(EDGE, width=2, opacity=arrive(int(t), int(t) + 6, 70))],
                       tr=transform(position=(x, y))))
    cells.append(group([rect(size=(CW - 26, 10), roundness=5),
                        fill(INK if lit else MUTED,
                             opacity=arrive(int(t) + 2, int(t) + 8, 62 if lit else 30))],
                       tr=transform(position=(x, y))))
a.shape_layer(cells, tr=transform(position=(W / 2, H / 2)), name="grid")

# --------------------------------------------------------------- the weekdays
head = []
for c in range(COLS):
    head.append(group([rect(size=(38, 8), roundness=4),
                       fill(MUTED, opacity=arrive(2, 10, 34))],
                      tr=transform(position=(X0 + c * (CW + GAP), Y0 - CH / 2 - 34))))
a.shape_layer(head, tr=transform(position=(W / 2, H / 2)), name="weekdays")

out = os.path.join(os.path.dirname(__file__), "..", "calendar-20th-circled.json")
a.save(os.path.abspath(out), minify=False)
print("wrote", os.path.abspath(out), a.op, "frames @", a.fr, "fps")
