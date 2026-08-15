#!/usr/bin/env python3
"""Fold the approved CHAPTER designs back into ONE full-length composition.

    python3 tools/cut_assemble.py <slug> --cut en

Writes studio/videos/<slug>-<cut>-full/index.html  <- THE MASTER composition
       studio/videos/<slug>-<cut>/assets/audio.json <- the merged cue list
       + assets/ symlinks, package.json, node_modules symlink, renders/

This is the exact inverse of tools/chapter_project.py, and it exists because
tools/chapter_preview.py is a PREVIEW, not a master: it stream-concats eight
independently-rounded encodes, so the seven chapter joints become HARD CUTS and
up to eight frames of rounding accumulate. `pipeline_check.py check_render`
wants one file whose duration matches timing.json's total to within a second,
with real 0.45s dissolves at every joint. That means ONE composition, rendered
once — which means the chapter designs have to come back together as HTML.

THE THREE UNDOS
---------------
1. `data-start`, `<audio data-start>` and every absolute motion-time literal get
   the chapter's offset ADDED back. (`S.sN + x` forms need nothing: S is rebased,
   so they follow.)
2. Each chapter's LAST scene gets its +0.45 cross-dissolve overlap back. The
   generator strips it because a chapter has no successor to dissolve into; the
   full cut does. The final scene of the last chapter keeps its bare duration.
3. Each chapter's own `sceneTransitions(...)` / `register()` / `var S` / `var D`
   / `var IDS` are dropped and replaced by ONE of each over all 92 scenes.

TWO KINDS OF CHAPTER
--------------------
* GENERATED — has a `chapter.json`. Rebuilt from the shipped index.html through
  chapter_project's own `scene_html`, at offset 0. Deterministic, so the whole
  -en cut round-trips exactly.
* HAND-BUILT — no `chapter.json`, an approved `index-claudedesign.html` instead
  (-hi ch1 and ch2). Its scene blocks are SPLICED VERBATIM. Nothing is
  regenerated or redesigned; only the two rebases above are applied, and every
  scene is checked attribute-by-attribute against the shipped cut afterwards.

  Their `<style>` blocks are SCOPED to their own scenes. -hi ch2 deliberately
  redeclares `.field` as the legacy `inset:-8%` full-bleed field and overrides
  `.arch-b/.arch-c/.arch-d .stack` — correct inside that chapter, catastrophic
  across the other 81 scenes, which are built plate-first. Unscoped, the merge
  would silently restyle six chapters that the creator has already signed off.
"""
import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chapter_project as cp                                   # noqa: E402

ROOT = cp.ROOT
OVERLAP = cp.OVERLAP

# `.p-*` and `#root` are emitted by this file; a chapter's copy of them is a
# duplicate, not an override, so it is dropped rather than scoped.
DROP_RULES = re.compile(r"^\s*(#root|\.p-[abcd])\b")


CSS_RULE = re.compile(r"([^{}]+)\{([^{}]*)\}", re.S)


def scope_css(css, cls):
    """Prefix every selector with `.cls`, so a chapter's CSS reaches only its
    own scenes. `.arch-b .stack` becomes `.cls.arch-b .stack` — the archetype
    class lives ON the section, so a descendant prefix there would match
    nothing; everything else is a descendant of the section and prefixes
    normally.

    Comments are STRIPPED FIRST, and that is load-bearing rather than tidy: the
    chapter files put a `/* C · LEDGER — type in a left column, artefact on the
    right */` immediately above the rule it describes, and splitting the
    selector list on "," while that text is still attached turns the comma
    INSIDE the prose into a selector boundary. `.arch-c .stack` then comes out
    as `.cls .arch-c .stack` — a DESCENDANT of the section rather than the
    section itself — which matches nothing and silently drops the layout the
    comment was describing. (The prose stays in the chapter project, which is
    the file a human edits; the master is generated and says so.)"""
    body_only = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    out = []
    for m in CSS_RULE.finditer(body_only):
        sels = [s.strip() for s in m.group(1).split(",") if s.strip()]
        if not sels or any(DROP_RULES.match(s) for s in sels):
            continue
        out.append(", ".join(f".{cls}{s}" if s.startswith(".arch-")
                             else f".{cls} {s}" for s in sels)
                   + " { " + " ".join(m.group(2).split()) + " }")
    # An at-rule or a nested block would be dropped silently, which is exactly
    # the failure this scoping exists to prevent. Refuse instead.
    assert sum(len(re.sub(r"\s", "", m.group(0))) for m in CSS_RULE.finditer(body_only)) \
        == len(re.sub(r"\s", "", body_only)), \
        f"scope_css did not account for all of ch{cls}'s CSS (an at-rule?)"
    return "\n".join(out)


def add_class(tag, cls):
    return re.sub(r'class="([^"]*)"', lambda m: f'class="{m.group(1)} {cls}"',
                  tag, count=1)


TAIL_NOISE = re.compile(r"^\s*(window\.__timelines\s*=|register\(\)|"
                        r"sceneTransitions\(|var\s+(S|D|IDS)\s*=)")

def generated(slug, cut, ch, scenes, script, spec):
    """Sections + motion for a chapter that has a chapter.json, at offset 0."""
    ids = [s["id"] for s in scenes]
    missing = [i for i in ids if i not in spec.get("scenes", {})]
    if missing:
        sys.exit(f"ch{ch}: chapter.json is missing a spec for {missing}")

    secs = []
    for s in scenes:
        sp = spec["scenes"][s["id"]]
        if sp.get("comment"):
            secs.append("<!-- " + sp["comment"].strip() + " -->")
        # drop_overlap=False, offset=0: in the full cut every scene keeps the
        # shipped duration it was measured with, including the +0.45.
        secs.append(add_class(cp.scene_html(s, sp, False, 0), f"ch{ch}"))

    mot = cp.motion_lines(script, ids)
    body = []
    for s in scenes:
        sid = s["id"]
        # The shipped script's own tail sits inside the LAST scene's comment
        # block, so lifting motion verbatim also lifts `register()`. Harmless in
        # a chapter project (it is the tail there too); a second registration in
        # the merged file is not.
        lines = [ln for ln in mot[sid] if not TAIL_NOISE.match(ln)]
        sp = spec["scenes"][sid]
        m = sp.get("measure")
        if m:
            lines.append(f'rise("#{sid}-ml", S.{sid} + 1.10, 0.6, 10);')
            lines.append(f'span("#{sid}-mf", S.{sid} + {m.get("at", 1.9)}, '
                         f'{m.get("dur", 1.6)}, {m["from"]}, {m["to"]});')
        lines += sp.get("motion", [])
        body.append(f"/* {sid} */ " + " ".join(lines) if len(lines) == 1
                    else f"/* {sid} */\n" + "\n".join(lines))

    megas = []
    for s in scenes:
        if spec["scenes"][s["id"]].get("arch") != "b":
            continue
        m = re.search(rf'id="{s["id"]}-num"[^>]*font-size:(\d+)px', s["body"])
        if m:
            megas.append(f'#{s["id"]}-num {{ font-size: {m.group(1)}px !important; }}')

    return {"secs": secs, "body": body, "css": spec.get("css", ""),
            "megas": megas, "lottie": spec.get("lottie", []), "D": {},
            "tail": spec.get("tail", [])}




def handbuilt(path, ch, offset, last_scene_id):
    """Sections + motion spliced VERBATIM from an approved hand-built chapter.

    Only the two rebases are applied. The design is not touched: this chapter is
    creator-approved and there is no spec to regenerate it from."""
    html = open(path, encoding="utf-8").read()
    secs = []
    for chunk in re.split(r'(?=<section[^>]*class="[^"]*\bscene\b)', html):
        tag = re.match(r"<section[^>]*>", chunk)
        if not tag:
            continue
        tag, sid = tag.group(0), re.search(r'id="(s\d+)"', chunk).group(1)
        body = chunk[:chunk.index("</section>") + len("</section>")]
        new = tag
        new = re.sub(r'data-start="([\d.]+)"',
                     lambda m: f'data-start="{cp.num(float(m.group(1)) + offset)}"', new)
        if sid == last_scene_id:      # give the cross-dissolve overlap back
            new = re.sub(r'data-duration="([\d.]+)"',
                         lambda m: f'data-duration="{cp.num(float(m.group(1)) + OVERLAP)}"',
                         new)
        secs.append(add_class(new, f"ch{ch}") + body[len(tag):])

    style = re.search(r"<style>(.*?)</style>", html, re.S)
    lottie = re.findall(r'<script src="assets/lottie/([\w-]+)\.js"></script>', html)
    D = dict(re.findall(r"(s\d+):\s*([\d.]+)",
                        (re.search(r"var D = \{(.*?)\};", html, re.S) or
                         re.match("", "")).group(1))) if "var D" in html else {}

    # EVERY attribute-less <script>, in document order — not just the last one.
    # A hand-built chapter keeps its timeline in one block, so `rindex` used to
    # be right. A build.mjs chapter emits TWO: the motion timeline first, then
    # the RATE ASSERT. Taking the last one silently dropped every ken/rise/
    # countUp/playLottie in the cut and left a master of 81 static slides that
    # merely cross-dissolved — and nothing caught it, because `hyperframes
    # check` reports "Motion 0 errors" when there is no motion to check.
    body = []
    for blk in re.findall(r"<script>(.*?)</script>", html, re.S):
        # Everything after the declarations, minus this chapter's own globals.
        start = blk.index("var IDS") if "var IDS" in blk else 0
        body += [cp.rebase_motion(ln, -offset)
                 for ln in blk[blk.index("\n", start) + 1:].split("\n")
                 if not TAIL_NOISE.match(ln)]
    while body and not body[-1].strip():
        body.pop()

    return {"secs": secs, "body": [f"/* ---- chapter {ch}, hand-built, spliced "
                                   f"verbatim (+{cp.num(offset)}s) ---- */"] + body,
            "css": scope_css(style.group(1), f"ch{ch}") if style else "",
            "megas": [], "lottie": lottie, "D": D, "tail": []}


def take_rate_assert(body):
    """Lift a chapter's RATE ASSERT out of its body. -> (body, block or None).

    Every chapter carries its own copy, so a verbatim merge writes six of them
    into one file, each scanning all 81 scenes. Identical copies are merely
    wasteful; a DIVERGENT one is not, and they do diverge — on this cut ch1's
    predates the `derived_income_carries_assumption` extension and is missing
    the BILL branch. A stale copy that throws (or fails to) on scenes it was
    never written for would surface in the 18-minute master render and nowhere
    earlier, so the master keeps exactly ONE, and the caller says which."""
    text = "\n".join(body)
    m = re.search(r"\(function \(\)\s*\{(?:(?!\}\)\(\);).)*\}\)\(\);", text, re.S)
    if not m or "RATE ASSERT" not in m.group(0):
        return body, None
    start = m.start()
    lead = list(re.finditer(r"/\*.*?\*/", text[:start], re.S))
    if lead and not text[lead[-1].end():start].strip():
        start = lead[-1].start()          # swallow the prose comment above it
    return (text[:start] + text[m.end():]).rstrip().split("\n"), m.group(0)


def from_chapters(slug, cut):
    """Cut-level facts for a cut whose CHAPTERS are the origin, not a carving.

    §3b builds chapter-first, so a run reaches assembly having never produced a
    full-length index.html — there was nothing to carve chapters out of, the
    chapters came first. (`japanese-money-methods` went the other way, which is
    why the shipped file used to be assumed.) Nothing is lost, only spread out:
    `assets/voice/timing.json` is the one home of every start and duration —
    one VO line is one clip is one scene, the pipeline's own invariant — and
    each chapter's index.html holds its sections, audio rows and styling
    rebased to zero. The chapter offset is the timing of its first line, which
    is the same constant `chapter_project.py` rebased BY, so this is its exact
    inverse rather than a re-derivation."""
    T = json.load(open(os.path.join(ROOT, "studio/videos", f"{slug}-{cut}",
                                    "assets/voice/timing.json"), encoding="utf-8"))
    lines, root = T["lines"], T["total"]

    chdirs = []
    for ch in range(1, 99):
        p = os.path.join(ROOT, "studio/videos", f"{slug}-{cut}-ch{ch}")
        if not os.path.exists(os.path.join(p, "index.html")):
            break
        chdirs.append((ch, p))
    if not chdirs:
        sys.exit(f"no {slug}-{cut}/index.html and no {slug}-{cut}-ch1/index.html "
                 "— nothing to assemble from")

    parts, scenes, audio, chapters, acts, n = [], [], [], [], [], 0
    for k, (ch, chdir) in enumerate(chdirs):
        path = os.path.join(chdir, "index.html")
        html = open(path, encoding="utf-8").read()
        secs = re.findall(r'<section[^>]*class="[^"]*\bscene\b[^"]*"[^>]*>', html)
        final = k == len(chdirs) - 1
        offset = lines[n]["scene_start"]

        for j, tag in enumerate(secs):
            a = dict(re.findall(r'(id|data-[\w-]+)="([^"]*)"', tag))
            t = lines[n + j]
            # The chapter is only trusted for its DESIGN. That it sits where the
            # voice says it does is asserted, not assumed — this is the one check
            # that would catch a chapter rebuilt against a re-cut line.
            assert abs(float(a["data-start"]) + offset - t["scene_start"]) < 2e-3, \
                (f"ch{ch} {a['id']}: starts at {float(a['data-start']) + offset} "
                 f"but timing.json line {t['id']} says {t['scene_start']}")
            # Only the CUT's final scene keeps a bare duration; every chapter's
            # own last scene gets the +0.45 cross-dissolve overlap back.
            bare = final and j == len(secs) - 1
            scenes.append({"id": a["id"], "attrs": dict(
                a, **{"data-start": cp.num(t["scene_start"]),
                      "data-duration": cp.num(t["scene_duration"]
                                              + (0 if bare else OVERLAP))})})

        for row in re.findall(r"<audio[^>]*></audio>", html):
            audio.append(re.sub(
                r'data-start="([\d.]+)"',
                lambda m: f'data-start="{cp.num(float(m.group(1)) + offset)}"',
                row, count=1))

        p = handbuilt(path, ch, offset, None if final else
                      re.search(r'id="(s\d+)"', secs[-1]).group(1))
        p["body"], p["assert"] = take_rate_assert(p["body"])
        p["ch"], p["src"], p["ids"] = ch, "index.html (chapter-first)", \
            [re.search(r'id="(s\d+)"', s).group(1) for s in secs]
        p["path"] = path
        parts.append(p)
        chapters.append((ch, [{"attrs": {"data-start": cp.num(offset)}}]))
        m = re.search(r"acts:\s*(\[[^\]]*\])", html)
        if m:
            acts += json.loads(m.group(1).replace("'", '"'))
        n += len(secs)

    if n != len(lines):
        sys.exit(f"{n} scenes across {len(chdirs)} chapters but timing.json has "
                 f"{len(lines)} lines — a chapter is missing or double-counted")

    blocks = [p.pop("assert") for p in parts]
    keep = max([b for b in blocks if b], key=len, default=None)
    if keep and len(set(b for b in blocks if b)) > 1:
        print(f"  rate assert: {len(set(b for b in blocks if b))} variants across "
              f"chapters, keeping the strictest ({len(keep)} chars)")

    head = open(os.path.join(chdirs[0][1], "index.html"), encoding="utf-8").read()
    title = re.search(r"<title>(.*?)</title>", head, re.S).group(1)
    return (parts, scenes, audio, chapters, root, acts,
            re.search(r'id="root"[^>]*class="([^"]*)"', head).group(1),
            re.split(r"\s*·\s*CHAPTER", title)[0].strip(), [keep] if keep else [])


def assemble(slug, cut):
    cutdir = os.path.join(ROOT, "studio/videos", f"{slug}-{cut}")
    outdir = os.path.join(ROOT, "studio/videos", f"{slug}-{cut}-full")
    shipped = os.path.join(cutdir, "index.html")
    if not os.path.exists(shipped):
        (parts, scenes, audio, chapters, root, acts, rootcls, title,
         extra_tail) = from_chapters(slug, cut)
        ids = [s["id"] for s in scenes]
        S = ", ".join(f'{s["id"]}: {s["attrs"]["data-start"]}' for s in scenes)
        D = {}
        for p in parts:
            D.update(p["D"])
        return emit(slug, cut, cutdir, outdir, parts, scenes, audio, chapters,
                    ids, S, D, root, acts, rootcls, title, extra_tail)
    scenes, audio, script = cp.parse_cut(shipped)
    html = open(shipped, encoding="utf-8").read()
    root = float(re.search(r'id="root"[^>]*data-duration="([\d.]+)"', html).group(1))
    acts = json.loads((re.search(r"acts:\s*(\[[^\]]*\])", html) or
                       re.match("", "")).group(1).replace("'", '"')) \
        if "acts:" in html else []
    rootcls = re.search(r'id="root"[^>]*class="([^"]*)"', html).group(1)
    title = re.search(r"<title>(.*?)</title>", html, re.S).group(1)

    by_id = {s["id"]: i for i, s in enumerate(scenes)}
    parts, chapters = [], []
    for ch in range(1, 99):
        rows = [(i, r) for i, r in enumerate(audio)
                if re.search(rf'id="vo-{ch}-\d+"', r)]
        if not rows:
            break
        lo, hi = rows[0][0], rows[-1][0]
        chapters.append((ch, scenes[lo:hi + 1]))
    if not chapters:
        sys.exit("no chapters found — the <audio> ids are not vo-<chapter>-<line>")

    for ch, mine in chapters:
        chdir = os.path.join(ROOT, "studio/videos", f"{slug}-{cut}-ch{ch}")
        specp = os.path.join(chdir, "chapter.json")
        offset = float(mine[0]["attrs"]["data-start"])
        if os.path.exists(specp):
            p = generated(slug, cut, ch, mine, script,
                          json.load(open(specp, encoding="utf-8")))
            src = "chapter.json"
        else:
            hand = os.path.join(chdir, "index-claudedesign.html")
            if not os.path.exists(hand):
                sys.exit(f"ch{ch}: neither chapter.json nor index-claudedesign.html")
            p = handbuilt(hand, ch, offset,
                          mine[-1]["id"] if ch < len(chapters) else None)
            p["path"] = hand
            src = "index-claudedesign.html (spliced verbatim)"
        p["ch"], p["src"], p["ids"] = ch, src, [s["id"] for s in mine]
        parts.append(p)

    ids = [s["id"] for s in scenes]
    S = ", ".join(f'{s["id"]}: {s["attrs"]["data-start"]}' for s in scenes)
    D = {}
    for p in parts:
        D.update(p["D"])
    return emit(slug, cut, cutdir, outdir, parts, scenes, audio, chapters,
                ids, S, D, root, acts, rootcls, title, [])


def emit(slug, cut, cutdir, outdir, parts, scenes, audio, chapters,
         ids, S, D, root, acts, rootcls, title, extra_tail):
    """Write the master, verify it and merge the cue list. Shared by both paths:
    what differs between a carved cut and a chapter-first one is where the facts
    come FROM, not what gets written."""
    lottie = [l for p in parts for l in p["lottie"]]
    css = "\n".join(x for p in parts for x in (p["megas"] + [p["css"]]) if x.strip())
    provenance = "\n".join(f"     ch{p['ch']:<2} {p['ids'][0]}-{p['ids'][-1]:<4} "
                           f"{p['src']}" for p in parts)

    out = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title} · FULL CUT · CLAUDE-DESIGN</title>

<!-- ===========================================================================
     THE MASTER — all {len(ids)} scenes, {cp.num(root)}s, one composition, one render.

     ASSEMBLED by tools/cut_assemble.py from the {len(parts)} approved chapter projects,
     each named below with what it was assembled FROM. Do not hand-edit: change
     the chapter and re-run the assembler.

{provenance}

     Every start and duration is checked attribute-by-attribute against
     studio/videos/{slug}-{cut}/assets/voice/timing.json, which is measured from the
     voice and is the one home of both.

     Every chapter's last scene has its +0.45s cross-dissolve overlap BACK — the
     chapter generator strips it because a chapter has no successor. The {len(parts) - 1}
     chapter joints are therefore real dissolves here, not the hard cuts that
     tools/chapter_preview.py produces.
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
{css}
</style>
</head>
<body>
<div id="root" class="{rootcls}" data-composition-id="main" data-width="1920" data-height="1080" data-start="0" data-duration="{cp.num(root)}">

{chr(10).join(chr(10).join(p["secs"]) + chr(10) for p in parts)}
<!-- Voice only, verbatim from the shipped cut. Music and SFX are the post-mix
     step: tools/audio/mix.py reads the merged cue list from ../{slug}-{cut}/assets/audio.json. -->
{chr(10).join(audio)}

</div>

<script src="assets/js/gsap.min.js"></script>{'<script src="assets/js/lottie.min.js"></script>' if lottie else ""}
<script src="assets/js/motion.js"></script>{''.join(f'{chr(10)}<script src="assets/lottie/{l}.js"></script>' for l in lottie)}
<script>
var S = {{ {S} }};
var D = {{ {", ".join(f"{k}: {v}" for k, v in D.items())} }};
var IDS = {json.dumps(ids)};

sceneTransitions(IDS, S{f", {{ acts: {json.dumps(acts)} }}" if acts else ""});

{(chr(10) * 2).join(chr(10).join(p["body"]) for p in parts)}

{chr(10).join(x for p in parts for x in p["tail"])}
{chr(10).join(extra_tail)}
window.__timelines = window.__timelines || {{}};
register();
</script>
</body>
</html>
"""
    os.makedirs(outdir, exist_ok=True)
    dest = os.path.join(outdir, "index.html")
    open(dest, "w", encoding="utf-8").write(out)
    paths = [p.get("path") for p in parts]
    verify(dest, scenes, audio, root,
           sources=paths if all(paths) else ())
    merge_audio(slug, cut, chapters, cutdir)
    print(f"{slug}-{cut}-full: {len(ids)} scenes {ids[0]}-{ids[-1]}  "
          f"root {cp.num(root)}s  {len(audio)} voice rows  timing OK")
    # FFMPEG_ENCODE_TIMEOUT_MS is NOT optional at this length and its absence is
    # a silent 90-minute loss: capture finishes, ffmpeg keeps going at ~0.17x,
    # and the default 41.8-minute encode timeout kills it at about frame 11000
    # of 18800 with the mp4 never written (measured on -en, 2026-08-06). The
    # pipeline's own orchestrator command carries PRODUCER_ENABLE_CHUNKED_ENCODE
    # for the same reason (a subagent's background task dies when it returns);
    # either works.
    print(f"""
  render it with (the env var is load-bearing — see the note in this file):
    cd studio/videos/{slug}-{cut}-full
    FFMPEG_ENCODE_TIMEOUT_MS=10800000 npx hyperframes render . \\
        -o ../{slug}-{cut}/renders/FINAL-1080p-{cut}.mp4 -q high -f 30
    python3 tools/audio/mix.py  studio/videos/{slug}-{cut}/renders/FINAL-1080p-{cut}.mp4
    python3 tools/loudnorm.py   studio/videos/{slug}-{cut}/renders/MIXED-1080p-{cut}.mp4
    python3 tools/audio/verify_cues.py studio/videos/{slug}-{cut}/renders/MIXED-1080p-{cut}.mp4
    python3 tools/pipeline_check.py check render --slug {slug} --cut {cut}""")
    return outdir


def verify(dest, scenes, audio, root, sources=()):
    """Every timing attribute must equal the SHIPPED cut's, exactly.

    Not "sums to the right total" — the failure this project keeps hitting
    produces a correct total with every internal cut drifted. Attribute by
    attribute against the one home, or it is not verified."""
    h = open(dest, encoding="utf-8").read()
    got = [dict(re.findall(r'(id|data-[\w-]+)="([^"]*)"', t))
           for t in re.findall(r'<section[^>]*class="[^"]*\bscene\b[^"]*"[^>]*>', h)]
    assert len(got) == len(scenes), f"{len(got)} sections, {len(scenes)} expected"
    prev = -1.0
    for g, s in zip(got, scenes):
        a = s["attrs"]
        assert g["id"] == s["id"], f"{g['id']} != {s['id']}"
        for k in ("data-start", "data-duration", "data-track-index"):
            assert abs(float(g[k]) - float(a[k])) < 1e-9 if k != "data-track-index" \
                else g[k] == a[k], f"{s['id']} {k}: {g[k]} != {a[k]}"
        assert float(g["data-start"]) > prev, f"{s['id']} start is not monotonic"
        prev = float(g["data-start"])
        if "data-framings" in g or "data-framings" in a:
            assert abs(sum(map(float, g["data-framings"].split(","))) -
                       sum(map(float, a["data-framings"].split(",")))) < 1e-6, \
                f"{s['id']} framings do not sum to the shipped scene_duration"
    last = got[-1]
    delta = float(last["data-start"]) + float(last["data-duration"]) - root
    assert abs(delta) < 0.002, f"last scene ends {delta:+.4f}s off the root"
    au = re.findall(r"<audio[^>]*></audio>", h)
    assert au == audio, f"{len(au)} voice rows written, {len(audio)} expected"
    assert h.count("register()") == 1, "more than one register() survived the merge"
    assert h.count("sceneTransitions(") == 1, "more than one sceneTransitions()"
    verify_motion(h, sources)


# Every helper in motion.js whose absence means a scene simply does not animate.
MOTION_CALLS = ("ken", "rise", "pop", "popEach", "fade", "draw", "breathe", "pulse",
                "fill", "exit", "countUp", "countDown", "span", "plateKen", "drift",
                "dissolve", "shove", "playLottie")


def verify_motion(h, sources):
    """The master must carry every motion call its chapters do.

    THIS EXISTS BECAUSE THE MERGE LOST ALL OF THEM ONCE AND NOTHING NOTICED
    (gate two, 2026-08-15). `handbuilt` took the LAST inline <script>, which in a
    build.mjs chapter is the rate assert, not the timeline — so the master
    rendered 81 static slides that cross-dissolved, for 29 minutes, and passed
    `hyperframes check`, whose Motion section reports "0 errors" when there is
    nothing to animate. Absence is invisible to every checker that asks whether
    what ran was well-formed; only a count against the source can see it."""
    if not sources:
        # A carved cut's generated chapters take their motion from the shipped
        # cut's one script, so there is no per-chapter file to count against.
        # Say so rather than printing a reassuring zero.
        print("  motion: not verified (no per-chapter source files)")
        return

    def calls(text):
        # Comments FIRST. These files document their motion in prose — "s9's
        # dissolve is against the incoming boundary", "one ken( per scene" — and
        # the merge legitimately drops some of those blocks (the declarations
        # preamble, the rate assert's header, every CSS comment). Counting them
        # compares prose against code and reports a loss that never happened.
        text = re.sub(r"/\*.*?\*/|<!--.*?-->", "", text, flags=re.S)
        return {c: len(re.findall(rf"\b{c}\s*\(", text)) for c in MOTION_CALLS}

    want = {c: 0 for c in MOTION_CALLS}
    for src in sources:
        for c, n in calls(open(src, encoding="utf-8").read()).items():
            want[c] += n
    got, short = calls(h), []
    for c in MOTION_CALLS:
        # >= not ==: `emit` adds the cut's own sceneTransitions/register tail, and
        # a chapter's own globals are dropped on purpose. Losing calls is the bug.
        if got[c] < want[c]:
            short.append(f"{c} {got[c]}/{want[c]}")
    assert not short, ("the merge DROPPED motion calls the chapters declare: "
                       + ", ".join(short) + " — the master would render as static "
                       "slides. See verify_motion().")
    print(f"  motion: {sum(got[c] for c in MOTION_CALLS)} calls carried "
          f"({sum(want.values())} declared across {len(sources)} chapters)")


def merge_audio(slug, cut, chapters, cutdir):
    """The full-cut cue list: each chapter's list with its own offset added back."""
    sfx, missing = [], []
    for ch, mine in chapters:
        p = os.path.join(ROOT, "studio/videos", f"{slug}-{cut}-ch{ch}",
                         "assets", "audio.json")
        if not os.path.exists(p):
            missing.append(ch)
            continue
        off = float(mine[0]["attrs"]["data-start"])
        for c in json.load(open(p, encoding="utf-8")).get("sfx", []):
            if "at" not in c:                       # a `_hold` annotation
                continue
            sfx.append({"at": round(c["at"] + off, 3), "name": c["name"],
                        "_": f"ch{ch} +{cp.num(off)} · {c.get('_', '')}".rstrip(" ·")})
    if missing:
        sys.exit(f"no assets/audio.json for chapters {missing} — "
                 f"run tools/audio/cues.py <project> --write first")
    sfx.sort(key=lambda c: c["at"])
    dest = os.path.join(cutdir, "assets", "audio.json")
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump({"_comment":
                   "FULL-CUT cue list — the eight chapter lists merged, each "
                   "chapter's offset added back. GENERATED by "
                   "tools/cut_assemble.py; edit a chapter's assets/audio.json "
                   "(tools/audio/cues.py) and re-run the assembler.",
                   "music": "bed-resolve", "sfx": sfx}, fh,
                  ensure_ascii=False, indent=1)
        fh.write("\n")
    print(f"  {os.path.relpath(dest, ROOT)}: {len(sfx)} cues merged")


def scaffold(slug, cut):
    """assets/ that LINKS the cut's media and the shared stylesheets.

    chapter-design.css comes from tools/scaffold, NOT from the cut's copy: the
    cut's is 20 lines behind (no `.art-lift`, no `.measure.under`) and chapters
    3-8 were rendered against the scaffold one. Safe for the hand-built pair —
    neither uses either selector, so the extra rules are inert there."""
    d = os.path.join(ROOT, "studio/videos", f"{slug}-{cut}-full")
    cutrel = f"../../{slug}-{cut}/assets"
    os.makedirs(os.path.join(d, "assets/js"), exist_ok=True)
    os.makedirs(os.path.join(d, "renders"), exist_ok=True)

    def link(target, at):
        p = os.path.join(d, at)
        if os.path.islink(p):
            os.unlink(p)
        elif os.path.exists(p):
            return
        os.symlink(target, p)

    # WHERE EACH SHARED ASSET COMES FROM, and it is not one place.
    # `fonts` and `img` (grain.png, wm-en.png) belong to the DESIGN SYSTEM and
    # are linked from tools/scaffold like the two stylesheets beside them — not
    # from the cut. The cut also has an `assets/img/`, and it is a different
    # thing wearing the same name: a manifest of the sourced photographs. Taking
    # the cut's because it merely EXISTS is what shadowed grain.png and wm-en.png
    # into 404s on the first chapter-first assembly. A chapter project links
    # these exactly this way — see the live links in any -ch<N>/assets/.
    link("../../../../tools/scaffold/assets/blockframe.css", "assets/blockframe.css")
    link("../../../../tools/scaffold/assets/chapter-design.css", "assets/chapter-design.css")
    link("../../../../../tools/scaffold/assets/js/motion.js", "assets/js/motion.js")
    for sub in ("fonts", "img"):
        link(f"../../../../tools/scaffold/assets/{sub}", f"assets/{sub}")

    # The rest are the CUT's, and a chapter-first run keeps some of them beside
    # the chapters instead — so each is resolved by looking, not assumed.
    def owner(rel):
        for cand in [f"{slug}-{cut}"] + [f"{slug}-{cut}-ch{c}" for c in range(1, 9)]:
            if os.path.exists(os.path.join(ROOT, "studio/videos", cand, "assets", rel)):
                return cand
        return None

    for f in ("gsap.min.js", "lottie.min.js"):
        home = owner(f"js/{f}")
        if home:
            link(f"../../../{home}/assets/js/{f}", f"assets/js/{f}")
    for sub in ("voice", "lottie"):
        home = owner(sub)
        if home:
            link(f"../../{home}/assets/{sub}", f"assets/{sub}")
    # The hand-built chapters keep their photographs beside themselves.
    for ch in range(1, 9):
        src = os.path.join(ROOT, "studio/videos", f"{slug}-{cut}-ch{ch}", f"assets-ch{ch}")
        if os.path.isdir(src):
            link(f"../{slug}-{cut}-ch{ch}/assets-ch{ch}", f"assets-ch{ch}")
    # The npm project comes from the cut dir when one was scaffolded, else from
    # the first chapter. A chapter-wise run never scaffolds the cut dir — the
    # chapters ARE the projects — so the cut dir is routinely a bare assets/
    # stub and the old unconditional copy died on FileNotFoundError.
    def npm_home():
        for cand in [f"{slug}-{cut}"] + [f"{slug}-{cut}-ch{c}" for c in range(1, 9)]:
            p = os.path.join(ROOT, "studio/videos", cand)
            if os.path.exists(os.path.join(p, "package.json")) and \
               os.path.isdir(os.path.join(p, "node_modules")):
                return cand
        sys.exit(f"no package.json + node_modules under studio/videos/{slug}-{cut}*"
                 " — run `npm i` in the cut or a chapter project first")

    home = npm_home()
    link(f"../{home}/node_modules", "node_modules")
    if not os.path.exists(os.path.join(d, "package.json")):
        import shutil
        shutil.copy(os.path.join(ROOT, "studio/videos", home, "package.json"),
                    os.path.join(d, "package.json"))


def _selftest():
    """The guard that would have caught the 2026-08-15 silent-motion-loss, tested
    in both directions — a guard that only ever passes is not a guard."""
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        src = os.path.join(d, "ch1.html")
        open(src, "w", encoding="utf-8").write(
            '<script src="assets/js/gsap.min.js"></script>\n'
            "<script>\nvar IDS = [\"s1\"];\n"
            'ken("#s1-bg", 0, 4, false);\ncountUp("#s1-num", 1.2, 1.0, 0, 95);\n'
            "</script>\n"
            "<script>\n/* RATE ASSERT */\n(function () { var x = 1; })();\n</script>")

        # 1. the real failure: only the LAST <script> survives, so motion is gone.
        try:
            verify_motion('<script>\n(function () { var x = 1; })();\n</script>', [src])
            raise AssertionError("verify_motion passed a master with NO motion")
        except AssertionError as e:
            assert "DROPPED motion calls" in str(e), e

        # 2. the merged-whole case must pass.
        verify_motion('<script>\nken("#s1-bg", 0, 4, false);\n'
                      'countUp("#s1-num", 1.2, 1.0, 0, 95);\n</script>', [src])

        # 3. prose describing motion must not be counted as motion — the false
        #    positive this guard actually produced on its first run.
        verify_motion("/* one ken( per scene, and a countUp( on the hero */\n"
                      '<script>\nken("#s1-bg", 0, 4, false);\n'
                      'countUp("#s1-num", 1.2, 1.0, 0, 95);\n</script>', [src])

        # 4. no sources -> says so rather than passing silently.
        verify_motion("<script></script>", [])
    print("selftest OK")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("slug", nargs="?")
    ap.add_argument("--cut", default="en", choices=("en",))
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        _selftest()
        sys.exit(0)
    if not a.slug:
        ap.error("slug is required (or pass --selftest)")
    scaffold(a.slug, a.cut)
    assemble(a.slug, a.cut)
