#!/usr/bin/env python3
"""Generate a standalone chapter project from a shipped cut, on the archetype layer.

    python3 tools/chapter_project.py <slug> --cut hi --chapter 3

Reads  studio/videos/<slug>-<cut>/index.html          (the SHIPPED photographic cut)
       studio/videos/<slug>-<cut>-ch<N>/chapter.json  (the design spec, hand-authored)
Writes studio/videos/<slug>-<cut>-ch<N>/index.html   <- THE archetype chapter cut
       + assets/ symlinks, package.json, node_modules symlink, renders/

The chapter composition is `index.html` and there is no second root .html. Three
things force that and they all point the same way: `hyperframes check` only ever
looks for index.html, `tools/chapter_sheet.py` hardcodes it, and the linter's
`multiple_root_compositions` rule is an ERROR on any project with two root files
carrying data-composition-id — so ch1/ch2's index.html + index-claudedesign.html
pair cannot pass a check. In a CHAPTER project index.html is not the shipped cut;
the shipped cut lives in <slug>-<cut>/ and is never touched.

WHY THIS EXISTS
---------------
The one failure this project has seen twice is a layout pass that re-times a
chapter — durations that sum to exactly the right total while every internal cut
drifts (vault/knowledge/claude-design-mcp.md §3b). Hand-copying 92 scenes'
`data-start` / `data-duration` / `data-framings` / `data-track-index` and 92
`<audio>` rows across fourteen chapter projects is that failure waiting to
happen. So none of it is hand-copied: every timing attribute, every on-screen
string, every `.bg` and every audio row is lifted VERBATIM from the shipped
index.html and only the START is rebased, by one constant per chapter.

What the spec file owns is the DESIGN, and only the design: which archetype a
scene is, its ground temperature, whether its drawn layer survives, and any art.

THE TWO REBASES
---------------
1. `data-start` and `<audio data-start>` shift by the chapter's offset (the first
   scene's shipped start). Relative gaps are therefore exact by construction and
   the chapters concatenate frame-exact.
2. The motion script's TIME arguments shift by the same offset. Every helper in
   motion.js takes its time as argument index 1 — `ken(sel, at, ...)`,
   `rise(sel, at, ...)`, `pop(sel, at)`, `countUp(sel, at, ...)`. The -hi cut
   writes those as `S.sN + x` (S is rebased, so they need nothing); the -en cut
   writes them as absolute literals, which do get shifted. Both are handled by
   the same rule, and anything that is neither is left alone and reported.

THE ONE DURATION THAT CHANGES
-----------------------------
A chapter's last scene drops the +0.45 cross-dissolve overlap and carries its
bare `scene_duration`, exactly as s10 does in ch1 and s21 in ch2 — there is no
successor inside this project to dissolve into. The 0.45 comes back on concat.
`data-framings` is untouched: it always described scene_duration.
"""
import argparse
import json
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OVERLAP = 0.45

ARCH_PLATE = {"a": ("p-a", "0 0 1920 1080"), "b": ("p-b edge", "0 0 860 610"),
              "c": ("p-c edge", "0 0 934 1200"), "d": ("p-d", "0 0 1920 656")}
# the structural rule each archetype hangs off, and where it sits
ARCH_RULE = {"a": None, "b": ("vrule", "top:196px;height:392px"),
             "c": ("crule", "left:980px"), "d": ("brule", "top:424px")}
ROLE_GLOW = {"239,68,68": "rgba(239,68,68,.16)", "34,197,94": "rgba(34,197,94,.16)",
             "245,158,11": "rgba(245,158,11,.16)", "255,92,57": "rgba(255,92,57,.16)"}


def num(x):
    """Trim a float the way the shipped file writes them (6.501, not 6.5010)."""
    s = f"{x:.6f}".rstrip("0").rstrip(".")
    return s or "0"


def parse_cut(path):
    """[{id, n, tag, attrs, body}] in document order, plus the audio rows."""
    html = open(path, encoding="utf-8").read()
    scenes = []
    for chunk in re.split(r'(?=<section[^>]*class="[^"]*\bscene\b)', html):
        tag = re.match(r"<section[^>]*>", chunk)
        if not tag:
            continue
        tag = tag.group(0)
        sid = re.search(r'id="(s\d+)"', tag).group(1)
        attrs = dict(re.findall(r'(data-[\w-]+|style)="([^"]*)"', tag))
        body = chunk[len(tag):chunk.index("</section>")]
        scenes.append({"id": sid, "n": int(sid[1:]), "attrs": attrs, "body": body})
    audio = re.findall(r"<audio[^>]*></audio>", html)
    script = html[html.rindex("<script>") + len("<script>"):html.rindex("</script>")]
    return scenes, audio, script


def motion_lines(script, ids):
    """The per-scene motion statements, keyed by scene id, verbatim.

    Both cuts group their calls under a `/* sN · line · … */` comment; -hi keeps
    the whole scene on one line and -en spreads it over several. Splitting on the
    comment rather than on newlines handles both without a format flag."""
    out = {i: [] for i in ids}
    parts = re.split(r"/\* (s\d+) ·[^*]*\*/", script)
    for k in range(1, len(parts) - 1, 2):
        sid = parts[k]
        if sid in out:
            out[sid] = [ln.strip() for ln in parts[k + 1].strip().split("\n") if ln.strip()]
    return out


TIME_ARG = re.compile(r"\b(ken|rise|pop|popEach|fade|draw|breathe|pulse|fill|exit|"
                      r"countUp|countDown|span|plateKen|drift|dissolve|shove|playLottie)"
                      r"\(\s*([^,]+),\s*(-?\d+(?:\.\d+)?)\s*(?=[,)])")


def rebase_motion(line, offset):
    """Shift every absolute time literal in a motion call by -offset.

    Argument index 1 is the time in every motion.js helper, without exception —
    that uniformity is the whole reason this can be a regex instead of a parser.
    `S.sN + x` forms carry no literal there and are left untouched; S itself is
    rebased, so they follow automatically."""
    return TIME_ARG.sub(lambda m: f"{m.group(1)}({m.group(2)}, {num(float(m.group(3)) - offset)}",
                        line)


def extract_div(html, opener):
    """The whole `<div class="stack">…</div>`, nesting counted.

    A regex to the next `</div>` stops at the first nested one, and a regex to
    the following `.grain` assumes an element order the two cuts do not share
    (-en writes grain BEFORE stack). Counting is the only version that is right
    for both."""
    i = html.index(opener)
    depth, j = 0, i
    for m in re.finditer(r"<div\b|</div>", html[i:]):
        depth += 1 if m.group(0) == "<div" else -1
        if depth == 0:
            j = i + m.end()
            break
    return html[i:j]


def scene_html(sc, spec, drop_overlap, offset):
    """One <section>, archetype layer applied. Timing attributes are verbatim."""
    sid, a = sc["id"], sc["attrs"]
    arch = spec.get("arch", "a")
    art = spec.get("art", "off")                       # "off" | "" | "forward"
    svg = spec.get("svg")
    if svg and art == "off":
        art = ""                                       # authoring art implies it is on
    # A split with an empty other side is a hole. A is already centred.
    centred = spec.get("centred", art == "off" and arch != "a")

    cls = ["scene", "clip", f"arch-{arch}", "has-photo"]
    if art == "off":
        cls.append("art-off")
    elif art == "forward":
        cls.append("art-forward")
    if spec.get("lift"):
        cls.append("art-lift")
    if centred:
        cls.append("centred")

    dur = float(a["data-duration"]) - (OVERLAP if drop_overlap else 0)
    tag = (f'<section class="{" ".join(cls)}" id="{sid}"'
           f' data-track-index="{a["data-track-index"]}"'
           f' data-start="{num(float(a["data-start"]) - offset)}"'
           f' data-duration="{num(dur)}"')
    # A spec may DECLARE MORE framings than the shipped cut — ch1 splits s3 into
    # 3.400,2.912 because it added a real second photograph there. It may never
    # change their SUM, which is the scene's measured duration.
    fr = spec.get("framings", a.get("data-framings"))
    if fr:
        base = a.get("data-framings")
        if base and abs(sum(map(float, fr.split(","))) - sum(map(float, base.split(",")))) > 1e-6:
            sys.exit(f"{sid}: framings {fr} do not sum to the shipped {base}")
        tag += f' data-framings="{fr}"'
    if "style" in a:                                   # -en carries --tint here
        tag += f' style="{a["style"]}"'
    tag += ">"

    body = sc["body"]
    bgs = re.findall(r'<div class="bg"[^>]*></div>', body)
    scrim = re.search(r'<div class="scrim"[^>]*></div>', body)
    stack = extract_div(body, '<div class="stack"')

    glow = ""
    # The role colour is READ OFF the shipped scrim's --tint (-hi) or the shipped
    # section style (-en) rather than restated in the spec, so the glow can never
    # disagree with the scrim about what role a scene carries.
    tint = re.search(r"--tint:\s*rgba\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)",
                     a.get("style", "") + " " + (scrim.group(0) if scrim else ""))
    if tint:
        key = ",".join(tint.groups())
        if key not in ROLE_GLOW:
            sys.exit(f"{sid}: --tint rgba({key}) is not a role colour")
        glow = f' style="--gl:{ROLE_GLOW[key]}"'

    L = ["  " + b for b in bgs]
    L.append(f'  <div class="field" style="--f1:{spec["f1"]}"><div class="rules"></div>'
             f'<div class="glow"{glow}></div></div>')
    # Spec html goes between the field and the plate. A `.band` has to sit BEHIND
    # the drawn art it exists to make readable — ch2 could place it after the
    # scrim because its art lived in the field and its Lottie was at z 2, but a
    # plate is z 0, so a z-1 band after it would darken the very thing it is for.
    # (`.measure` is z 2 and lands above everything either way.)
    L.extend("  " + x for x in spec.get("html", []))
    m = spec.get("measure")
    if m:
        L.append(f'  <p class="measure-lab under" id="{sid}-ml">{m["label"]}</p>')
        L.append(f'  <div class="measure under" id="{sid}-mt">'
                 f'<div class="measure-fill {m["role"]}" id="{sid}-mf"></div></div>')
    # No plate without art. An empty one is an aperture onto nothing: `.has-photo`
    # already strips its panel lift and its hatch, so it renders as a no-op div.
    if svg and not centred:
        plate, viewbox = ARCH_PLATE[arch]
        plate = spec.get("plate", plate)
        L.append(f'  <div class="plate {plate}" id="{sid}-plate">')
        L.append(f'    <div class="plate-in" id="{sid}-pin">')
        L.append('      <div class="hatch"></div>')
        if svg:
            L.append(f'      <svg class="art" id="{sid}-art" viewBox="{spec.get("viewbox", viewbox)}"'
                     f' preserveAspectRatio="xMidYMid slice" style="opacity:{spec.get("opacity", ".68")}">')
            L.append(re.sub(r"^", "        ", svg.strip(), flags=re.M))
            L.append("      </svg>")
        L.append("    </div>")
        L.append("  </div>")
    L.append("  " + (scrim.group(0) if scrim else '<div class="scrim"></div>'))
    if not centred and ARCH_RULE[arch]:
        rule, pos = ARCH_RULE[arch]
        L.append(f'  <div class="{rule}" id="{sid}-{rule[0]}r"'
                 f' style="{spec.get("rule", pos)}"></div>')
    L.append("  " + stack.strip())
    L.append('  <div class="grain"></div>')
    return tag + "\n" + "\n".join(L) + "\n</section>"


def build(slug, cut, chapter):
    cutdir = os.path.join(ROOT, "studio/videos", f"{slug}-{cut}")
    chdir = os.path.join(ROOT, "studio/videos", f"{slug}-{cut}-ch{chapter}")
    spec = json.load(open(os.path.join(chdir, "chapter.json"), encoding="utf-8"))

    scenes, audio, script = parse_cut(os.path.join(cutdir, "index.html"))
    # Chapter membership comes from the VO line id (vo-<chapter>-<line>), which is
    # the script's own chapter numbering — no second bookkeeping to drift.
    rows = [(i, r) for i, r in enumerate(audio)
            if re.search(rf'id="vo-{chapter}-\d+"', r)]
    if not rows:
        sys.exit(f"no <audio> rows for chapter {chapter} in {cut}")
    lo, hi = rows[0][0], rows[-1][0]
    mine = scenes[lo:hi + 1]
    offset = float(mine[0]["attrs"]["data-start"])
    nxt = scenes[hi + 1]["attrs"]["data-start"] if hi + 1 < len(scenes) else None
    # The last chapter closes on the CUT's own root duration — timing.json's
    # total, the one home — not on a re-derived sum of its final scene.
    cut_root = float(re.search(r'id="root"[^>]*data-duration="([\d.]+)"',
                               open(os.path.join(cutdir, "index.html"),
                                    encoding="utf-8").read()).group(1))
    root = (float(nxt) - offset) if nxt else (cut_root - offset)

    ids = [s["id"] for s in mine]
    missing = [i for i in ids if i not in spec.get("scenes", {})]
    if missing:
        sys.exit(f"chapter.json is missing a spec for: {', '.join(missing)}")

    secs = []
    for s in mine:
        sp = spec["scenes"][s["id"]]
        if sp.get("comment"):
            secs.append("<!-- " + sp["comment"].strip() + " -->")
        secs.append(scene_html(s, sp, s is mine[-1] and nxt is not None, offset))
    secs = "\n\n".join(secs)

    mot = motion_lines(script, ids)
    body = []
    for s in mine:
        sid = s["id"]
        lines = [rebase_motion(ln, offset) for ln in mot[sid]]
        if s is mine[-1]:   # the last scene's ken must not run past the chapter root
            bare = num(float(s["attrs"]["data-duration"]) - OVERLAP)
            lines = [re.sub(rf'(ken\("#{sid}-bg", [^,]+, )[\d.]+', rf"\g<1>{bare}", ln)
                     for ln in lines]
        sp = spec["scenes"][sid]
        m = sp.get("measure")
        if m:
            lines.append(f'rise("#{sid}-ml", S.{sid} + 1.10, 0.6, 10);')
            lines.append(f'span("#{sid}-mf", S.{sid} + {m.get("at", 1.9)}, '
                         f'{m.get("dur", 1.6)}, {m["from"]}, {m["to"]});')
        lines += sp.get("motion", [])
        body.append(f"/* {sid} */ " + " ".join(lines) if len(lines) == 1
                    else f"/* {sid} */\n" + "\n".join(lines))

    S = ", ".join(f'{s["id"]}: {num(float(s["attrs"]["data-start"]) - offset)}' for s in mine)
    acts = spec.get("acts", [])
    acts_js = f', {{ acts: {json.dumps(acts)} }}' if acts else ""
    aud = [re.sub(r'data-start="([\d.]+)"',
                  lambda m: f'data-start="{num(float(m.group(1)) - offset)}"', r)
           for _, r in rows]

    # `.arch-b .mega` is 300px !important, which beats the shipped inline size. A
    # focal size is a property of the copy, so the shipped value wins — re-declared
    # here at the only specificity that can carry it.
    megas = []
    for s in mine:
        if spec["scenes"][s["id"]].get("arch") != "b":
            continue
        m = re.search(rf'id="{s["id"]}-num"[^>]*font-size:(\d+)px', s["body"])
        if m:
            megas.append(f'#{s["id"]}-num {{ font-size: {m.group(1)}px !important; }}')
    megas = "\n".join(megas)

    head_extra = "".join(f'\n<script src="assets/lottie/{l}.js"></script>' for l in spec.get("lottie", []))
    out = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{spec.get("title", slug)} — {cut} · CHAPTER {chapter} · CLAUDE-DESIGN CUT</title>

<!-- ===========================================================================
     CHAPTER {chapter}, CLAUDE-DESIGN CUT — {ids[0]}–{ids[-1]}, {num(root)}s.

{spec.get("note", "")}

     GENERATED by tools/chapter_project.py from studio/videos/{slug}-{cut}/index.html.
     Every data-start / data-duration / data-framings / data-track-index, every
     on-screen string, every .bg and every <audio> row is VERBATIM from that file;
     the only change is a −{num(offset)}s rebase so the chapter plays from 0. Edit
     chapter.json and re-run the generator — do not hand-edit the timing here.
     Last scene carries a BARE data-duration (no +0.45 overlap); the 0.45 comes
     back on concat with chapter {chapter + 1}.
     =========================================================================== -->

<link rel="stylesheet" href="assets/blockframe.css">
<link rel="stylesheet" href="assets/chapter-design.css">
<style>
#root {{ position: relative; width: 1920px; height: 1080px; overflow: hidden; background: var(--bg); }}
/* the four plate rects, one per archetype */
.p-a {{ left: 0;      top: 0;     width: 1920px; height: 1080px; }}
.p-b {{ left: 1120px; top: 150px; width: 860px;  height: 610px;  }}
.p-c {{ left: 1046px; top: -60px; width: 934px;  height: 1200px; }}
.p-d {{ left: 0;      top: 424px; width: 1920px; height: 656px;  }}
/* B forces .mega to 300px; these scenes' focal sizes are a property of the copy. */
{megas}
{spec.get("css", "")}
</style>
</head>
<body>
<div id="root" class="cut-{cut}" data-composition-id="main" data-width="1920" data-height="1080" data-start="0" data-duration="{num(root)}">

{secs}

<!-- Voice only, rebased by −{num(offset)}. Music and SFX are the post-mix step. -->
{chr(10).join(aud)}

</div>

<script src="assets/js/gsap.min.js"></script>{'<script src="assets/js/lottie.min.js"></script>' if spec.get("lottie") else ""}
<script src="assets/js/motion.js"></script>{head_extra}
<script>
var S = {{ {S} }};
var IDS = {json.dumps(ids)};

sceneTransitions(IDS, S{acts_js});

{chr(10).join(body)}

{chr(10).join(spec.get("tail", []))}
window.__timelines = window.__timelines || {{}};
register();
</script>
</body>
</html>
"""
    dest = os.path.join(chdir, "index.html")
    open(dest, "w", encoding="utf-8").write(out)
    verify(dest, mine, rows, offset, root)
    print(f"{slug}-{cut}-ch{chapter}: {len(mine)} scenes {ids[0]}–{ids[-1]}  "
          f"offset −{num(offset)}  root {num(root)}s  timing OK")


def verify(dest, mine, rows, offset, root):
    """Re-read what we just wrote and prove the rebase against the shipped cut.

    This is the guard for the one failure this project keeps hitting: a chapter
    whose durations sum to the right total while its internal cuts drift. It
    compares GAPS, not totals, because a correct total is exactly what that
    failure produces."""
    h = open(dest, encoding="utf-8").read()
    got = [dict(re.findall(r'(id|data-[\w-]+)="([^"]*)"', t))
           for t in re.findall(r"<section[^>]*>", h)]
    assert len(got) == len(mine), f"{len(got)} sections written, {len(mine)} expected"
    for g, s in zip(got, mine):
        assert g["id"] == s["id"], f"{g['id']} != {s['id']}"
        assert abs(float(g["data-start"]) - (float(s["attrs"]["data-start"]) - offset)) < 1e-9, \
            f"{s['id']} start drifted"
        assert g["data-track-index"] == s["attrs"]["data-track-index"], f"{s['id']} track"
        if "data-framings" in g:
            assert abs(sum(map(float, g["data-framings"].split(","))) -
                       sum(map(float, s["attrs"]["data-framings"].split(",")))) < 1e-6, \
                f"{s['id']} framings do not sum to the shipped scene_duration"
    # The last scene should land exactly on the chapter root. A few boundaries in
    # the shipped cut are 1ms out against their successor's start (rounding in
    # timing.json); that is the source's, not ours, so it is reported rather than
    # silently absorbed — but anything larger is a real drift and stops the build.
    last = got[-1]
    delta = float(last["data-start"]) + float(last["data-duration"]) - root
    assert abs(delta) < 0.002, \
        f"last scene ends {delta:+.4f}s off the chapter root — that is a re-time, not rounding"
    if abs(delta) > 1e-6:
        print(f"  note: last scene ends {delta:+.4f}s off root (rounding in the shipped cut)")
    au = re.findall(r'<audio[^>]*id="(vo-[\d-]+)"[^>]*data-start="([\d.]+)"', h)
    assert len(au) == len(rows), f"{len(au)} audio rows, {len(rows)} expected"
    for (aid, ast), (_, src) in zip(au, rows):
        want = float(re.search(r'data-start="([\d.]+)"', src).group(1)) - offset
        assert abs(float(ast) - want) < 1e-9, f"{aid} audio start drifted"


def scaffold(slug, cut, chapter):
    """assets/ that LINKS the shared css/js/fonts/voice/img — nothing is copied.

    A chapter project that copies the cut's assets costs ~120 MB each; fourteen of
    them do not fit on this box. Symlinks are transparent to Chrome, and the CSS's
    own relative url(fonts/…) / url(img/…) still resolve because the browser
    resolves against the URL it was given, not the link target."""
    chdir = os.path.join(ROOT, "studio/videos", f"{slug}-{cut}-ch{chapter}")
    cutrel = f"../../{slug}-{cut}/assets"
    os.makedirs(os.path.join(chdir, "assets/js"), exist_ok=True)
    os.makedirs(os.path.join(chdir, "renders"), exist_ok=True)

    def link(rel_target, at):
        p = os.path.join(chdir, at)
        if os.path.islink(p) or os.path.exists(p):
            if os.path.islink(p):
                os.unlink(p)
            else:
                return
        os.symlink(rel_target, p)

    link("../../../../tools/scaffold/assets/blockframe.css", "assets/blockframe.css")
    link("../../../../tools/scaffold/assets/chapter-design.css", "assets/chapter-design.css")
    link("../../../../../tools/scaffold/assets/js/motion.js", "assets/js/motion.js")
    for f in ("gsap.min.js", "lottie.min.js"):
        if os.path.exists(os.path.join(ROOT, "studio/videos", f"{slug}-{cut}/assets/js", f)):
            link(f"../{cutrel}/js/{f}", f"assets/js/{f}")
    for d in ("fonts", "img", "voice", "lottie"):
        if os.path.exists(os.path.join(ROOT, "studio/videos", f"{slug}-{cut}/assets", d)):
            link(f"{cutrel}/{d}", f"assets/{d}")
    link(f"../{slug}-{cut}/node_modules", "node_modules")
    if not os.path.exists(os.path.join(chdir, "package.json")):
        shutil.copy(os.path.join(ROOT, "studio/videos", f"{slug}-{cut}/package.json"),
                    os.path.join(chdir, "package.json"))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--cut", default="hi")
    ap.add_argument("--chapter", type=int, required=True)
    ap.add_argument("--scaffold", action="store_true", help="(re)make assets links first")
    a = ap.parse_args()
    if a.scaffold:
        scaffold(a.slug, a.cut, a.chapter)
    build(a.slug, a.cut, a.chapter)
