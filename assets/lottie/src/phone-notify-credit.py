"""phone-notify-credit — the bank credit notification that lands on scene 1.1.

The photograph under it (s1.jpg) is already a phone face-up on a night counter,
so this is NOT a second phone: it is the banner that arrives ON that phone,
lifted out of the frame and set under the headline. Beats: buzz -> card drops in
-> screen bloom -> app mark -> title -> the amount wipes on -> a second settle.

Palette is blockframe's, and deliberately role-COLOURLESS: storyboard §7 gives
s1 `stmt · A · —` (no role colour, no --tint). Green here would read the salary
credit as "the behaviour that works", which is what --fund means in this video.
The accent enters on s2, which is the fund scene.

One-shot, not a loop: playLottie() runs loop:false and the card must HOLD after
it arrives, so frame 0 and the last frame are deliberately NOT equal.

  python3 assets/lottie/src/phone-notify-credit.py          # -> phone-notify-credit.json      (INR)
  python3 assets/lottie/src/phone-notify-credit.py --usd    # -> phone-notify-credit-usd.json  (USD)

The two cuts are two markets, so the app mark is the ONE thing that differs: a
`$` on -en, a `₹` on -hi. Everything else — geometry, timing, palette, the
masked amount — is shared, because the beat is identical. A ₹ on a US cut is
the wrong-currency defect this project has shipped before; a separate hand-made
asset would be the same defect waiting on a divergent edit.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../../.claude/skills/lottie-master/scripts"))
from lottie_gen import (Lottie, rect, ellipse, fill, stroke, group, path,  # noqa: E402
                        transform, animated, static, hex)

W, H, FPS, DUR = 820, 300, 30, 75          # 2.5s — the slot s1 has between +1.90 and +4.40
CX, CY = 410, 168                          # card centre
CARD_W, CARD_H = 640, 132

PANEL = "#161b25"   # --panel
EDGE  = "#2a3241"   # --edge
INK   = "#f5f3ec"   # --ink
MUTED = "#98a2b3"   # --muted

# ONE light curve drives the bloom, the card's rim and the app mark's glow.
# Two swells: the arrival, then the phone settling on stone.
LIGHT = [(0, 0), (5, 0, "easeOut"), (15, 100), (34, 88, "easeInOut"),
         (48, 72), (51, 72, "easeOut"), (57, 94), (67, 84, "easeInOut"), (75, 80)]


def light(peak):
    return animated([(kf[0], round(kf[1] * peak / 100, 2), *kf[2:]) for kf in LIGHT])


def arrive(start, end, peak=100):
    """Held off, then eased in, then held. The reveal every card part uses."""
    return animated([(0, 0, "hold"), (start, 0, "easeOut"), (end, peak), (DUR, peak)])


def radial(color, radius, stops, opacity=100):
    """Soft falloff = a gradient with an alpha ramp. Stacked ellipses band."""
    r, g, b = hex(color)
    flat = []
    for off, _ in stops:
        flat += [off, r, g, b]
    for off, alpha in stops:
        flat += [off, alpha]
    return {"ty": "gf", "nm": "glow", "t": 2, "r": 1,
            "o": opacity if isinstance(opacity, dict) else static(opacity),
            "s": static([0, 0]), "e": static([radius, 0]),
            "g": {"p": len(stops), "k": static(flat)}}


def rupee(size, color, position=(0, 0), opacity=100, weight=0.135):
    """The ₹ mark, as five round-capped strokes on a `size` box.

    Why this is here at all: masking the AMOUNT is the cold open's declared open
    loop, but masking the figure is not the same as removing every trace that it
    is money — without a currency mark the card said "a notification arrived" on
    the one beat the whole 35 s cold open exists to deliver (editor, ch1 att.1).
    The digits stay bars; only the currency is named.

    Traced against Noto Sans Bold's own U+20B9 rendered at 184 px and compared
    side by side at the 46 px this actually ships at. The bowl MUST be the curve
    — the first cut of this drew it as a left stem plus a horizontal floor, which
    put a THIRD full bar under the two real ones and read as ₣, not ₹. A wrong
    currency mark on a currency video is worse than no mark, so the closed curve
    is load-bearing, not a refinement. Order: two full-width bars, a left stem, a
    bowl arcing right and closing back left, a leg falling to the bottom-right.
    The doubled bar is the rupee's own signature, so it cannot read as $/€/£/¥.
    """
    s, t = size, max(2.0, size * weight)

    def stroked(shape):
        return group([shape, stroke(color, width=t, opacity=opacity, cap="round")])

    def seg(a_, b_):
        return stroked(path([[a_[0] * s, a_[1] * s], [b_[0] * s, b_[1] * s]], closed=False))

    def arc(a_, b_, out_, in_):
        """One cubic. Tangents are relative to their own vertex, as Lottie wants."""
        return stroked(path([[a_[0] * s, a_[1] * s], [b_[0] * s, b_[1] * s]],
                            in_tangents=[[0, 0], [in_[0] * s, in_[1] * s]],
                            out_tangents=[[out_[0] * s, out_[1] * s], [0, 0]],
                            closed=False))

    return group([seg((0.05, 0.10), (0.95, 0.10)),    # shirorekha — the top bar
                  seg((0.05, 0.31), (0.95, 0.31)),    # the doubled bar
                  seg((0.12, 0.10), (0.12, 0.55)),    # the bowl's left stem
                  arc((0.12, 0.10), (0.26, 0.55),     # the bowl, closing back left
                      (0.46, 0.04), (0.32, -0.22)),
                  seg((0.13, 0.54), (0.64, 0.97))],   # the leg
                 tr=transform(anchor=(s / 2, s / 2), position=position))


def dollar(size, color, position=(0, 0), opacity=100, weight=0.135):
    """The $ mark, as four round-capped strokes on a `size` box.

    Same job as rupee() and drawn to the same weight, because the -en card has
    to carry the identical density at the identical 46 px. Order: the top bowl
    (one cubic bulging up), the waist (one cubic crossing the middle), the
    bottom bowl (bulging down), then the stem straight through all three.

    Built from THREE cubics rather than a traced glyph for the reason the ₹ is:
    a stroked S drawn as two half-circles plus a straight diagonal reads as a
    Z at card size. The waist has to be a curve, and the two bowls have to
    bulge past the stem's ends, or the mark reads as a crossed-out S.
    """
    s, t = size, max(2.0, size * weight)

    def stroked(shape):
        return group([shape, stroke(color, width=t, opacity=opacity, cap="round")])

    def seg(a_, b_):
        return stroked(path([[a_[0] * s, a_[1] * s], [b_[0] * s, b_[1] * s]], closed=False))

    def arc(a_, b_, out_, in_):
        return stroked(path([[a_[0] * s, a_[1] * s], [b_[0] * s, b_[1] * s]],
                            in_tangents=[[0, 0], [in_[0] * s, in_[1] * s]],
                            out_tangents=[[out_[0] * s, out_[1] * s], [0, 0]],
                            closed=False))

    return group([arc((0.84, 0.27), (0.16, 0.30),      # top bowl, bulging up
                      (-0.22, -0.22), (0.22, -0.22)),
                  arc((0.16, 0.30), (0.84, 0.70),      # the waist
                      (0.02, 0.20), (-0.02, -0.20)),
                  arc((0.84, 0.70), (0.16, 0.73),      # bottom bowl, bulging down
                      (-0.22, 0.22), (0.22, 0.22)),
                  seg((0.50, 0.04), (0.50, 0.96))],    # the stem
                 tr=transform(anchor=(s / 2, s / 2), position=position))


USD = "--usd" in sys.argv
MARK = dollar if USD else rupee
NAME = "phone-notify-credit-usd" if USD else "phone-notify-credit"

a = Lottie(width=W, height=H, fps=FPS, duration_frames=DUR, name=NAME)

# ------------------------------------------------------------------- the bloom
# The screen waking. Wide and low so it reads as light on a surface, not a halo.
#
# The falloff is a ROUND gradient in a round ellipse, stretched by the group's
# scale. Lottie's radial gradient is circular in shape-local space, so a wide
# ellipse with a wide radius dies outside its own geometry and gets cut off by
# the SVG viewBox — a hard-edged glow. Round-then-stretch keeps alpha at 0 on
# every edge, and every extent below stays inside the 820x300 canvas.
a.shape_layer(
    [group([ellipse(size=(160, 160)),
            radial(INK, 80, [(0, 0.17), (0.44, 0.06), (1, 0)])],
           tr=transform(position=(0, 28), scale=(420, 80))),
     group([ellipse(size=(264, 264)),
            radial(INK, 132, [(0, 0.30), (0.28, 0.14), (0.64, 0.04), (1, 0)])],
           tr=transform(scale=(300, 100)))],
    tr=transform(position=(CX, CY), opacity=light(100)), name="bloom")

# -------------------------------------------------------------------- the card
# Buzz and drop live on ONE position track: eased fall, then ~2px of jitter at
# each of the two beats. Sub-pixel motion is what sells it as a physical event.
buzz = animated([
    (0, [CX, CY + 54], "hold"), (5, [CX, CY + 54], "easeOutBack"), (15, [CX, CY], "linear"),
    (16, [CX + 2.4, CY + 1.4]), (18, [CX - 2.0, CY - 1.0]), (20, [CX + 1.6, CY + 1.2]),
    (22, [CX - 1.0, CY - 0.5]), (24, [CX, CY], "linear"),
    (50, [CX, CY], "linear"),
    (51, [CX + 2.0, CY + 1.1]), (53, [CX - 1.7, CY - 0.9]), (55, [CX + 1.2, CY + 0.9]),
    (57, [CX - 0.8, CY - 0.4]), (59, [CX, CY]), (DUR, [CX, CY])])

card_in = arrive(5, 15)

# Left edges are the anchors the wipe grows from; x is relative to the card centre.
TITLE_X, TITLE_W = -204, 294
# The amount row keeps its full original span, flush-left with the title. ONE ₹ on
# the card, and it is the app mark's — a second glyph at the head of this bar was
# tried and reads as a repeat at card size, not as emphasis.
AMT_X, AMT_W = -204, 196

# First item in a shape list paints ON TOP. Written front-to-back.
a.shape_layer([
    # the timestamp, top-right — the quietest thing on the card
    group([rect(size=(68, 10), roundness=5), fill(MUTED, opacity=arrive(21, 30, 46))],
          tr=transform(position=(254, -30))),

    # the amount. Wipes left-to-right from its own left edge: anchor 0,0 sits at
    # the edge, the bar is drawn to the right of it, scaleX carries the reveal.
    group([rect(size=(AMT_W, 24), position=(AMT_W / 2, 0), roundness=8),
           fill(INK, opacity=arrive(24, 30, 92))],
          tr=transform(anchor=(0, 0), position=(AMT_X, 22),
                       scale=animated([(0, [0, 100], "hold"), (26, [0, 100], "easeOutCubic"),
                                       (44, [100, 100]), (DUR, [100, 100])]))),

    # the title line
    group([rect(size=(TITLE_W, 14), position=(TITLE_W / 2, 0), roundness=7),
           fill(MUTED, opacity=arrive(19, 28, 74))],
          tr=transform(anchor=(0, 0), position=(TITLE_X, -26),
                       scale=animated([(0, [0, 100], "hold"), (20, [0, 100], "easeOutCubic"),
                                       (34, [100, 100]), (DUR, [100, 100])]))),

    # the app mark, lit by the same curve as the bloom
    group([rect(size=(76, 76), roundness=22), stroke(INK, width=2, opacity=light(30))],
          tr=transform(position=(-262, 0))),
    # The app mark WAS a blank grey square — a bank app with no bank on it. It is
    # the card's only badge, so it is where the money lives.
    MARK(46, INK, position=(-262, 0), opacity=arrive(15, 24, 92)),
    group([rect(size=(76, 76), roundness=22), fill(EDGE, opacity=arrive(13, 22, 100))],
          tr=transform(position=(-262, 0))),

    # the card: rim first (it must sit over the fill), then the fill
    group([rect(size=(CARD_W + 4, CARD_H + 4), roundness=28),
           stroke(INK, width=2, opacity=light(26))]),
    group([rect(size=(CARD_W, CARD_H), roundness=26),
           stroke(EDGE, width=3, opacity=card_in)]),
    group([rect(size=(CARD_W, CARD_H), roundness=26),
           fill(PANEL, opacity=animated([(0, 0, "hold"), (5, 0, "easeOut"),
                                         (15, 94), (DUR, 94)]))]),
], tr=transform(position=buzz), name="notification")

out = os.path.join(os.path.dirname(__file__), "..", f"{NAME}.json")
a.save(os.path.abspath(out), minify=False)
print("wrote", os.path.abspath(out), a.op, "frames @", a.fr, "fps")
