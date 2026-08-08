"""Overhead: a phone face-up on a dark kitchen counter, waking with a
notification. Two buzzes, light spilling across the stone, then dark again.
30fps, 180 frames, seamless loop."""
import sys
sys.path.insert(0, "/mnt/skills/user/lottie-master/scripts")
from lottie_gen import (Lottie, ellipse, rect, fill, stroke, group,
                        transform, animated, static, hex)

W, H, FPS, DUR = 640, 420, 30, 180
PX, PY = 302, 216
TILT = -14

GLOW      = "#4B79D8"
CORE      = "#89B4FF"
RIMLIGHT  = "#7CA6FF"
BANNER    = "#DDE8FF"
TEXT      = "#63769B"
ICON      = "#5B8DEF"

# One light curve drives everything: screen, spill, rim, mug. Scale it per element.
CURVE = [(0, 0), (24, 0, "easeOut"), (27, 100), (66, 94, "easeInOut"),
         (96, 34), (108, 34, "easeOut"), (111, 92), (122, 86, "easeInOut"),
         (150, 26), (170, 0), (180, 0)]
BANNER_CURVE = [(0, 0), (25, 0, "hold"), (26, 0, "easeOut"), (34, 100),
                (66, 96, "easeInOut"), (96, 54), (108, 54, "easeOut"), (112, 100),
                (122, 96, "easeInOut"), (150, 32), (168, 0), (180, 0)]

def light(curve, peak):
    return animated([(kf[0], round(kf[1] * peak / 100, 2), *kf[2:]) for kf in curve])

def radial(color, radius, stops, opacity=100):
    """Radial gradient with an alpha ramp — a real soft light falloff."""
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

a = Lottie(width=W, height=H, fps=FPS, duration_frames=DUR, name="phone-on-counter-night")

# ---------------------------------------------------------------- counter ---
a.shape_layer(
    [rect(size=(W, H)),
     {"ty": "gf", "nm": "stone", "t": 1, "r": 1, "o": static(100),
      "s": static([0, -H / 2]), "e": static([0, H / 2]),
      "g": {"p": 2, "k": static([0, 0.035, 0.047, 0.070,
                                 1, 0.082, 0.102, 0.137])}}],
    tr=transform(position=(W / 2, H / 2)), name="counter")

# Warm light from somewhere else in the house, bleeding in from off-frame.
a.shape_layer([ellipse(size=(1500, 320)), radial("#6B4A2A", 750,
              [(0, 0.22), (0.4, 0.12), (0.75, 0.03), (1, 0)])],
              tr=transform(position=(240, -78)), name="hall-light")

# Grain in the stone.
grain = [group([rect(size=(W + 60, h)), fill("#39465A", opacity=o)],
               tr=transform(position=(0, y - H / 2), rotation=-0.6))
         for y, o, h in [(58, 5, 1.5), (132, 3.5, 1), (268, 4.5, 1.5),
                         (352, 3, 1), (398, 4, 1)]]
a.shape_layer(grain, tr=transform(position=(W / 2, H / 2)), name="grain")

# Dried coffee ring, a few crumbs. Nobody wiped down after dinner.
a.shape_layer(
    [group([ellipse(size=(96, 92)), stroke("#5A4A38", width=3, opacity=10)],
           tr=transform(position=(-150, -104))),
     group([ellipse(size=(5, 4)), fill("#6B7280", opacity=14)], tr=transform(position=(196, 78))),
     group([ellipse(size=(3.5, 3.5)), fill("#6B7280", opacity=11)], tr=transform(position=(214, 96))),
     group([ellipse(size=(4, 3)), fill("#6B7280", opacity=9)], tr=transform(position=(-208, 132))),
     group([ellipse(size=(3, 3)), fill("#6B7280", opacity=12)], tr=transform(position=(24, -168)))],
    tr=transform(position=(W / 2, H / 2)), name="counter-marks")

# A mug left out, half in frame.
a.shape_layer(
    [     group([ellipse(size=(88, 88)), stroke("#000000", width=6, opacity=35)]),
     group([ellipse(size=(88, 88)), fill("#080B10")]),
     group([ellipse(size=(116, 116)), stroke("#55637A", width=2.5, opacity=55)]),
     group([ellipse(size=(116, 116)), fill("#171D28")]),
     group([ellipse(size=(36, 50)), stroke("#48566B", width=7, opacity=40)],
           tr=transform(position=(54, 2)))],
    tr=transform(position=(72, 366), rotation=-8), name="mug")

# The mug rim catches the screen light.
a.shape_layer([group([ellipse(size=(116, 116)),
                      stroke(RIMLIGHT, width=2, opacity=light(CURVE, 30))])],
              tr=transform(position=(72, 366), rotation=-8), name="mug-rimlight")

# ------------------------------------------------------------------- spill ---
# Wide pool of light on the stone, elongated along the phone's axis.
spill_scale = animated([(0, [84, 84]), (24, [84, 84], "easeOut"), (36, [112, 112]),
                        (66, [107, 107], "easeInOut"), (96, [93, 93]),
                        (108, [93, 93], "easeOut"), (115, [110, 110]),
                        (150, [98, 98], "easeInOut"), (180, [84, 84])])
a.shape_layer(
    [group([ellipse(size=(250, 340)),
            radial(CORE, 150, [(0, 0.5), (0.4, 0.19), (1, 0)])]),
     group([ellipse(size=(680, 750)),
            radial(GLOW, 360, [(0, 0.62), (0.3, 0.32), (0.66, 0.09), (1, 0)])])],
    tr=transform(position=(PX, PY + 10), scale=spill_scale, rotation=TILT,
                 opacity=light(CURVE, 100)), name="spill")

# ------------------------------------------------------------------ phone ---
buzz = animated([
    (0, [PX, PY]), (24, [PX, PY], "linear"),
    (26, [PX + 1.7, PY + 1]), (28, [PX - 1.5, PY - 0.7]), (30, [PX + 1.2, PY + 1.2]),
    (32, [PX - 0.8, PY - 0.4]), (34, [PX, PY], "linear"), (108, [PX, PY], "linear"),
    (110, [PX + 1.6, PY + 0.9]), (112, [PX - 1.4, PY - 0.7]), (114, [PX + 1, PY + 1]),
    (116, [PX - 0.6, PY - 0.3]), (118, [PX, PY]), (180, [PX, PY])])

phone = list(reversed([
    group([rect(size=(134, 268), roundness=22), fill("#05070A")]),
    group([rect(size=(134, 268), roundness=22), stroke("#2B3444", width=1.6, opacity=45)]),
    group([rect(size=(120, 252), roundness=17), fill("#0B0E14")]),                 # asleep
    group([rect(size=(120, 252), roundness=17),
           fill("#1C3055", opacity=light(CURVE, 100))]),                            # awake
    group([ellipse(size=(150, 260)),
           radial(CORE, 110, [(0, 0.20), (0.5, 0.08), (1, 0)],
                  opacity=light(CURVE, 100))]),                                     # glass bloom
    group([rect(size=(44, 6), roundness=3), fill(BANNER, opacity=light(CURVE, 22))],
          tr=transform(position=(0, -14))),                                         # date
    group([rect(size=(80, 15), roundness=7), fill(BANNER, opacity=light(CURVE, 34))],
          tr=transform(position=(0, -36))),                                         # clock
    group([                                                                          # banner
        group([rect(size=(34, 4), roundness=2), fill(TEXT, opacity=light(BANNER_CURVE, 48))],
              tr=transform(position=(3, 5))),
        group([rect(size=(46, 4), roundness=2), fill(TEXT, opacity=light(BANNER_CURVE, 72))],
              tr=transform(position=(9, -6))),
        group([rect(size=(18, 18), roundness=5), fill(ICON, opacity=light(BANNER_CURVE, 100))],
              tr=transform(position=(-38, 0))),
        group([rect(size=(108, 34), roundness=11), fill(BANNER, opacity=light(BANNER_CURVE, 92))]),
    ], tr=transform(position=animated([(0, [0, -80]), (26, [0, -80], "easeOutBack"),
                                       (36, [0, -88]), (180, [0, -88])]))),
    group([rect(size=(138, 272), roundness=24),
           stroke(RIMLIGHT, width=2.4, opacity=light(CURVE, 36))]),                 # edge leak
]))
a.shape_layer(phone, tr=transform(position=buzz, rotation=TILT), name="phone")

a.save("/home/claude/anims/phone-night.json", minify=False)
print("built")
