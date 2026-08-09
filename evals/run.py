#!/usr/bin/env python3
"""Regression scorecard for finance-video output.

    python3 evals/run.py                       # score every composition on disk
    python3 evals/run.py --slug japanese-money-methods
    python3 evals/run.py --json evals/results/<ts>.json
    python3 evals/run.py --selftest

WHY THIS SCORES ARTIFACTS, NOT RUNS
-----------------------------------
One run costs ~70M tokens and hours of render (audit/05-baseline.md), so a suite of
5-8 *runs* is not an eval, it is a month. But every check below is a property of the
artifacts a run leaves on disk — so the same scorer grades the seven historical runs
(the baseline) and every future one, and the two numbers are directly comparable.

Judgment items — is the photo relevant, is the script good, would a viewer stay —
are NOT in here. They cannot be asserted, they need eyes. `evals/rubric.md` defines
them and how to score them; this file deliberately does not pretend to.

EVERY CHECK TRACES TO A DEFECT THAT ACTUALLY SHIPPED
---------------------------------------------------
No check exists because it seemed sensible. Each one cites the file and line where
this project recorded the defect it catches. A check that cannot find its inputs
returns NA — never PASS. A green board with nothing behind it is the failure mode
this whole audit exists to remove (`fin-assets.md:260-263`: "a checker that cannot
see the work is worse than no checker, because it reports green").
"""

import argparse
import collections
import datetime
import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PASS, FAIL, NA = "PASS", "FAIL", "NA"

# ── regexes ───────────────────────────────────────────────────────────────────
SCENE_RE = re.compile(r'<section[^>]*class="[^"]*\bscene\b[^"]*"[^>]*>', re.I)
ATTR = lambda name: re.compile(rf'{name}="([^"]*)"', re.I)
BG_URL_RE = re.compile(r'background-image\s*:\s*url\(([^)]+)\)', re.I)
IMG_SRC_RE = re.compile(r'(?:src|background-image\s*:\s*url\()\s*["\']?([^"\')\s]+\.(?:jpg|jpeg|png|webp))', re.I)
NET_RE = re.compile(r'(?:src|href)\s*=\s*["\']https?://', re.I)
CITE_RE = re.compile(r'\(\d+:\d+\)')
DIGIT_RE = re.compile(r'\d')
TAG_RE = re.compile(r'<[^>]+>')
SRT_CUE_RE = re.compile(r'^(\d+)\s*\n(\d\d:\d\d:\d\d,\d+)\s*-->\s*(\d\d:\d\d:\d\d,\d+)\s*\n(.*?)(?=\n\n|\Z)',
                        re.S | re.M)

RUPEE, DOLLAR = "\u20b9", "$"


def _read(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read()
    except OSError:
        return None


def _result(status, detail, evidence=None):
    return {"status": status, "detail": detail, "evidence": evidence or []}


# ── checks ────────────────────────────────────────────────────────────────────
# Signature: (ctx) -> result dict.  ctx carries html, paths, cut, slug.

def check_currency_purity(ctx):
    """No rupee glyph in a -en cut, no dollar glyph in a -hi cut.

    fin-script.md:51-54 — the check greps the WHOLE file; commentary must say
    "the dollar glyph" rather than typing it. Cost one retry on
    japanese-money-methods-hi, 2026-08-01.
    """
    if ctx["cut"] not in ("hi", "en") or ctx["html"] is None:
        return _result(NA, "no cut or no composition")
    bad = DOLLAR if ctx["cut"] == "hi" else RUPEE
    text = TAG_RE.sub(" ", ctx["html"])
    hits = [ln.strip()[:90] for ln in text.splitlines() if bad in ln]
    if hits:
        return _result(FAIL, f"{len(hits)} line(s) carry the forbidden glyph {bad!r}", hits[:5])
    return _result(PASS, f"no {bad!r} in a -{ctx['cut']} cut")


def check_no_network_fetch(ctx):
    """No CDN or remote reference in the composition.

    fin-build.md:34-35 — "a slow fetch past first paint renders a fully static
    video with green checks". Also pipeline_check.py:665.
    """
    if ctx["html"] is None:
        return _result(NA, "no composition")
    hits = NET_RE.findall(ctx["html"])
    if hits:
        ex = [m.group(0) for m in list(NET_RE.finditer(ctx["html"]))[:5]]
        return _result(FAIL, f"{len(hits)} remote reference(s)", ex)
    return _result(PASS, "no remote references")


def check_photo_every_scene(ctx):
    """Every scene carries a full-bleed background photo.

    Creator rule 2026-07-28; fin-storyboard.md:125 ("no photo-free scenes",
    photo_free_scene_ratio is 0) and fin-build.md:231-234.
    """
    if ctx["html"] is None:
        return _result(NA, "no composition")
    scenes = _scene_blocks(ctx["html"])
    if not scenes:
        return _result(NA, "no scenes found")
    missing = [sid for sid, body in scenes if not BG_URL_RE.search(body)]
    if missing:
        return _result(FAIL, f"{len(missing)} of {len(scenes)} scenes have no background image",
                       missing[:8])
    return _result(PASS, f"all {len(scenes)} scenes carry a background image")


def check_watermark(ctx):
    """#root carries the cut-<cut> class that paints the channel watermark.

    fin-build.md:127-132 — "check build fails without it".
    """
    if ctx["html"] is None or ctx["cut"] not in ("hi", "en"):
        return _result(NA, "no composition or no cut")
    m = re.search(r'id="root"[^>]*class="([^"]*)"', ctx["html"], re.I) or \
        re.search(r'class="([^"]*)"[^>]*id="root"', ctx["html"], re.I)
    if not m:
        return _result(FAIL, "no #root element with a class attribute")
    if f"cut-{ctx['cut']}" not in m.group(1):
        return _result(FAIL, f'#root class is "{m.group(1)}" — missing cut-{ctx["cut"]}')
    return _result(PASS, f"#root carries cut-{ctx['cut']}")


def check_track_alternation(ctx):
    """Adjacent scenes alternate data-track-index.

    fin-build.md:194-198 — `hyperframes check` fails overlapping_clips_same_track
    otherwise; verified 8 errors with every scene on track 1.
    """
    if ctx["html"] is None:
        return _result(NA, "no composition")
    tracks = []
    for sid, _body in _scene_blocks(ctx["html"]):
        tag = ctx["_scene_tags"].get(sid, "")
        m = ATTR("data-track-index").search(tag)
        tracks.append((sid, m.group(1) if m else None))
    if len(tracks) < 2:
        return _result(NA, "fewer than two scenes")
    if any(t is None for _, t in tracks):
        miss = [s for s, t in tracks if t is None]
        return _result(FAIL, f"{len(miss)} scene(s) have no data-track-index", miss[:8])
    clashes = [f"{tracks[i][0]}+{tracks[i+1][0]}@track{tracks[i][1]}"
               for i in range(len(tracks) - 1) if tracks[i][1] == tracks[i + 1][1]]
    if clashes:
        return _result(FAIL, f"{len(clashes)} adjacent scene pair(s) share a track", clashes[:8])
    return _result(PASS, f"{len(tracks)} scenes alternate cleanly")


def check_timing_coherence(ctx):
    """Root data-duration equals the last scene's end.

    pipeline_check.py:702 — "root data-duration ≠ last scene end". The failure this
    catches is a layout pass that re-times a chapter: durations that sum to the right
    total while every internal cut drifts (chapter_project.py:20-24).
    """
    if ctx["html"] is None:
        return _result(NA, "no composition")
    root = re.search(r'id="root"[^>]*data-duration="([\d.]+)"', ctx["html"], re.I) or \
        re.search(r'data-duration="([\d.]+)"[^>]*id="root"', ctx["html"], re.I)
    if not root:
        return _result(NA, "no root data-duration")
    ends = []
    for sid, _b in _scene_blocks(ctx["html"]):
        tag = ctx["_scene_tags"].get(sid, "")
        s = ATTR("data-start").search(tag)
        d = ATTR("data-duration").search(tag)
        if s and d:
            ends.append(float(s.group(1)) + float(d.group(1)))
    if not ends:
        return _result(NA, "no timed scenes")
    root_d, last = float(root.group(1)), max(ends)
    # the last scene may carry a bare duration while earlier ones carry a transition
    # tail, so the root is allowed to be shorter — never longer.
    if root_d > last + 0.05:
        return _result(FAIL, f"root duration {root_d:.2f}s exceeds last scene end {last:.2f}s")
    if last - root_d > 1.0:
        return _result(FAIL, f"last scene ends {last:.2f}s but root duration is {root_d:.2f}s "
                             f"({last - root_d:.2f}s of content past the end)")
    return _result(PASS, f"root {root_d:.2f}s vs last scene end {last:.2f}s")


def check_no_repeated_image(ctx):
    """No image reused across NON-ADJACENT scenes.

    fin-editor.md:68-70 — "One image per point"; the defect that created the review
    role was one photograph of books behind three different points.

    Adjacent reuse is NOT a defect and must not be flagged: fin-build.md:103-104
    blesses it explicitly — "Same image across two lines ⇒ ONE continuous zoom" via
    plateKen — and fin-editor.md:180-184 warns that a finding contradicting the
    storyboard's declared device (a HOLD is one continuous zoom) "is a finding about
    the review". A first pass here flagged every HOLD in the shipped cuts, which is
    exactly that mistake.
    """
    if ctx["html"] is None:
        return _result(NA, "no composition")
    scenes = _scene_blocks(ctx["html"])
    if not scenes:
        return _result(NA, "no scenes found")
    order = {sid: i for i, (sid, _b) in enumerate(scenes)}
    seen = collections.defaultdict(list)
    for sid, body in scenes:
        for m in BG_URL_RE.finditer(body):
            seen[m.group(1).strip("'\"")].append(sid)

    dups = {}
    for img, ids in seen.items():
        idx = sorted({order[s] for s in ids})
        if len(idx) < 2:
            continue
        # a run of consecutive indices is one HOLD; a gap is a genuine repeat
        if any(b - a > 1 for a, b in zip(idx, idx[1:])):
            dups[img] = [s for s in dict.fromkeys(ids)]
    if dups:
        ev = [f"{os.path.basename(i)} -> {','.join(s)}" for i, s in list(dups.items())[:6]]
        return _result(FAIL, f"{len(dups)} image(s) reused across non-adjacent scenes", ev)
    holds = sum(1 for img, ids in seen.items() if len({order[s] for s in ids}) > 1)
    return _result(PASS, f"{len(seen)} background images, no non-adjacent reuse"
                         + (f" ({holds} adjacent HOLD(s), allowed)" if holds else ""))


def check_image_credits(ctx):
    """Every image the composition renders has an attribution row.

    fin-assets.md:242-248 — "A COPY MUST CARRY ITS CREDIT ROW… On
    japanese-money-methods 35 photographs reached a rendered, machine-checked master
    with no credit row". Most Commons files are CC BY / CC BY-SA where attribution is
    a licence condition, not a courtesy (fin-assets.md:219-222).
    """
    if ctx["html"] is None:
        return _result(NA, "no composition")
    imgs = {os.path.basename(m.group(1).strip("'\""))
            for m in IMG_SRC_RE.finditer(ctx["html"])}
    imgs = {i for i in imgs if not i.startswith(("wm-", "grain"))}
    if not imgs:
        return _result(NA, "composition renders no images")

    credits = ""
    for cand in ctx["_credit_files"]:
        credits += (_read(cand) or "")
    if not credits:
        return _result(FAIL, f"{len(imgs)} image(s) rendered, no CREDITS file found anywhere "
                             f"under the project", sorted(imgs)[:6])
    missing = sorted(i for i in imgs if i not in credits and os.path.splitext(i)[0] not in credits)
    if missing:
        return _result(FAIL, f"{len(missing)} of {len(imgs)} rendered images have no credit row",
                       missing[:8])
    return _result(PASS, f"all {len(imgs)} rendered images credited")


def check_vo_text_hygiene(ctx):
    """VO text carries no bare Latin digits and no cite refs.

    fin-audit.md:51 — "no cite refs like (28:4) and no bare Latin digits in VO text —
    both are known silent TTS failures". Scored on the .txt files that were actually
    sent to the TTS engine, not on the script prose.
    """
    if not ctx["_vo_texts"]:
        return _result(NA, "no assets/voice/*.txt on disk")
    digit_hits, cite_hits = [], []
    for path in ctx["_vo_texts"]:
        body = _read(path) or ""
        if DIGIT_RE.search(body):
            digit_hits.append(f"{os.path.basename(path)}: {body.strip()[:70]}")
        if CITE_RE.search(body):
            cite_hits.append(os.path.basename(path))
    if digit_hits or cite_hits:
        return _result(FAIL,
                       f"{len(digit_hits)} line(s) with bare digits, "
                       f"{len(cite_hits)} with cite refs, of {len(ctx['_vo_texts'])}",
                       (digit_hits + cite_hits)[:6])
    return _result(PASS, f"{len(ctx['_vo_texts'])} VO lines clean")


def check_captions(ctx):
    """Shipped .srt is well formed: cues ordered, none over 84 chars.

    fin-package.md:159 — "0 cues over 84 characters, 0 out of order, and the last cue
    inside the runtime". Creator rule 2026-08-06: every video ships subtitles.
    """
    if not ctx["_srt_files"]:
        return _result(NA, "no .srt on disk")
    long_cues, disordered, total = [], 0, 0
    for path in ctx["_srt_files"]:
        body = _read(path) or ""
        prev_end = ""
        for m in SRT_CUE_RE.finditer(body):
            total += 1
            text = " ".join(m.group(4).split())
            if len(text) > 84:
                long_cues.append(f"{os.path.basename(path)}#{m.group(1)} ({len(text)} chars)")
            if prev_end and m.group(2) < prev_end:
                disordered += 1
            prev_end = m.group(3)
    if not total:
        return _result(FAIL, "srt file(s) present but no parseable cues",
                       [os.path.basename(p) for p in ctx["_srt_files"]])
    if long_cues or disordered:
        return _result(FAIL, f"{len(long_cues)} cue(s) over 84 chars, {disordered} out of order, "
                             f"of {total}", long_cues[:6])
    return _result(PASS, f"{total} cues, all ≤84 chars and in order")


CHECKS = [
    ("currency_purity",    "blocker",    check_currency_purity),
    ("no_network_fetch",   "blocker",    check_no_network_fetch),
    ("photo_every_scene",  "blocker",    check_photo_every_scene),
    ("image_credits",      "blocker",    check_image_credits),
    ("no_repeated_image",  "blocker",    check_no_repeated_image),
    ("vo_text_hygiene",    "blocker",    check_vo_text_hygiene),
    ("timing_coherence",   "blocker",    check_timing_coherence),
    ("track_alternation",  "should-fix", check_track_alternation),
    ("watermark",          "should-fix", check_watermark),
    ("captions",           "should-fix", check_captions),
]


# ── target discovery ──────────────────────────────────────────────────────────
def _scene_blocks(html):
    """[(scene_id, inner_html)] in document order."""
    out, tags = [], {}
    starts = [m for m in SCENE_RE.finditer(html)]
    for i, m in enumerate(starts):
        tag = m.group(0)
        sid_m = ATTR("id").search(tag)
        sid = sid_m.group(1) if sid_m else f"scene{i}"
        end = starts[i + 1].start() if i + 1 < len(starts) else len(html)
        out.append((sid, html[m.end():end]))
        tags[sid] = tag
    _scene_blocks.last_tags = tags
    return out


def build_ctx(project_dir, slug):
    html_path = os.path.join(project_dir, "index.html")
    html = _read(html_path)
    name = os.path.basename(project_dir.rstrip("/"))
    cut = None
    for token in ("-hi", "-en", "/hi", "/en"):
        if token in f"/{name}" or name.startswith(token[1:]):
            cut = token[-2:]
    m = re.search(r'\b(hi|en)\b', name)
    if m:
        cut = m.group(1)

    # Attribution is scoped to the ARCHIVE UNIT, not the directory. A cut archived to
    # vault/videos/<slug>/src/ keeps one CREDITS.txt per cut, and its per-chapter
    # subdirectories render the same files. Searching only `project_dir` reported
    # every chapter archive as uncredited when the cut-level file covered them.
    unit = project_dir
    parts = project_dir.replace("\\", "/").split("/")
    if "src" in parts:
        unit = "/".join(parts[:parts.index("src") + 1])

    credit_files, vo_texts, srt_files = [], [], []
    for dirpath, dirnames, filenames in os.walk(unit):
        dirnames[:] = [d for d in dirnames if d not in ("node_modules", "_cand", "snapshots")]
        for fn in filenames:
            if fn.startswith("CREDITS"):
                credit_files.append(os.path.join(dirpath, fn))

    for dirpath, dirnames, filenames in os.walk(project_dir):
        dirnames[:] = [d for d in dirnames if d not in ("node_modules", "_cand", "snapshots")]
        for fn in filenames:
            full = os.path.join(dirpath, fn)
            if fn.endswith(".txt") and os.sep + "voice" + os.sep in full:
                vo_texts.append(full)
            elif fn.endswith(".srt"):
                srt_files.append(full)

    ctx = {"project": project_dir, "slug": slug, "cut": cut, "html": html,
           "_credit_files": sorted(credit_files), "_vo_texts": sorted(vo_texts),
           "_srt_files": sorted(srt_files)}
    if html:
        _scene_blocks(html)
        ctx["_scene_tags"] = getattr(_scene_blocks, "last_tags", {})
    else:
        ctx["_scene_tags"] = {}
    return ctx


# Cuts NOT produced by /finance-video: the history lane and the practice builds
# (vault/knowledge/unshipped-experiments.md). They are built on a different design
# system, so scoring them against finance rules measures nothing. --all includes them.
NON_FINANCE = re.compile(r'^(video-hist-|video-0|firaun-)')


def discover(root, slug=None, include_all=False):
    targets = []
    for base in (os.path.join(root, "vault", "videos"), os.path.join(root, "studio", "videos")):
        if not os.path.isdir(base):
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [d for d in dirnames if d not in ("node_modules", "renders",
                                                            "snapshots", "_cand", "assets")]
            if "index.html" in filenames:
                rel = os.path.relpath(dirpath, base)
                s = rel.split(os.sep)[0]
                s = re.sub(r'-(hi|en)(-ch\d+)?$', '', s)
                if slug and s != slug:
                    continue
                if not include_all and not slug and NON_FINANCE.match(s):
                    continue
                if os.path.basename(dirpath).endswith("thumbs"):
                    continue          # thumbnails are one static frame, not a cut
                targets.append((s, dirpath))
    return sorted(set(targets))


def score(root, slug=None, include_all=False):
    rows = []
    for s, project in discover(root, slug, include_all):
        ctx = build_ctx(project, s)
        checks = {}
        for name, severity, fn in CHECKS:
            try:
                r = fn(ctx)
            except Exception as exc:                      # a crashed check is NA, never PASS
                r = _result(NA, f"check raised {type(exc).__name__}: {exc}")
            r["severity"] = severity
            checks[name] = r
        rows.append({"slug": s, "project": os.path.relpath(project, root),
                     "cut": ctx["cut"], "checks": checks})
    return rows


def summarize(rows):
    tally = collections.Counter()
    per_check = collections.defaultdict(collections.Counter)
    for row in rows:
        for name, r in row["checks"].items():
            tally[r["status"]] += 1
            per_check[name][r["status"]] += 1
    blockers = sum(1 for row in rows for r in row["checks"].values()
                   if r["status"] == FAIL and r["severity"] == "blocker")
    return {"targets": len(rows), "totals": dict(tally),
            "blocker_failures": blockers,
            "per_check": {k: dict(v) for k, v in per_check.items()}}


def print_report(rows, summary):
    names = [n for n, _s, _f in CHECKS]
    head = "".join(f"{n[:9]:>10}" for n in names)
    print(f"{'target':46}{head}")
    print("-" * (46 + 10 * len(names)))
    glyph = {PASS: "  ok", FAIL: "FAIL", NA: "   -"}
    for row in sorted(rows, key=lambda r: r["project"]):
        cells = "".join(f"{glyph[row['checks'][n]['status']]:>10}" for n in names)
        print(f"{row['project'][:45]:46}{cells}")
    print("-" * (46 + 10 * len(names)))
    t = summary["totals"]
    print(f"{summary['targets']} targets · "
          f"{t.get(PASS, 0)} pass · {t.get(FAIL, 0)} fail · {t.get(NA, 0)} not-applicable · "
          f"**{summary['blocker_failures']} blocker failures**")

    print("\nfailures by check:")
    for name, _sev, _fn in CHECKS:
        c = summary["per_check"].get(name, {})
        if c.get(FAIL):
            print(f"  {name:20} {c[FAIL]:3d} FAIL   ({c.get(PASS,0)} pass, {c.get(NA,0)} n/a)")

    print("\ndetail on blocker failures:")
    shown = 0
    for row in sorted(rows, key=lambda r: r["project"]):
        for name, r in row["checks"].items():
            if r["status"] == FAIL and r["severity"] == "blocker":
                print(f"  {row['project']}  [{name}] {r['detail']}")
                for e in r["evidence"][:3]:
                    print(f"      · {e}")
                shown += 1
                if shown >= 40:
                    print("  … truncated")
                    return


def selftest():
    import tempfile, shutil
    tmp = tempfile.mkdtemp()
    proj = os.path.join(tmp, "vault", "videos", "demo-slug", "src", "hi")
    os.makedirs(os.path.join(proj, "assets", "voice"))

    good = '''<div id="root" class="rail cut-hi" data-duration="10.00">
    <section class="scene clip" id="s1" data-start="0" data-duration="5.2" data-track-index="1">
      <div class="bg" style="background-image:url(assets/img/s1.jpg)"></div></section>
    <section class="scene clip" id="s2" data-start="5.0" data-duration="5.0" data-track-index="2">
      <div class="bg" style="background-image:url(assets/img/s2.jpg)"></div></section></div>'''
    with open(os.path.join(proj, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(good)
    with open(os.path.join(proj, "CREDITS.txt"), "w", encoding="utf-8") as fh:
        fh.write("s1.jpg — Pixabay/anon\ns2.jpg — Pexels/anon\n")
    with open(os.path.join(proj, "assets", "voice", "1.1.txt"), "w", encoding="utf-8") as fh:
        fh.write("पच्चीस हज़ार रुपये हर महीने\n")

    rows = score(tmp)
    assert len(rows) == 1, rows
    ck = rows[0]["checks"]
    assert rows[0]["cut"] == "hi", rows[0]
    for name in ("currency_purity", "no_network_fetch", "photo_every_scene", "image_credits",
                 "no_repeated_image", "vo_text_hygiene", "timing_coherence",
                 "track_alternation", "watermark"):
        assert ck[name]["status"] == PASS, (name, ck[name])
    assert ck["captions"]["status"] == NA, ck["captions"]          # no srt => NA, not PASS

    # An adjacent HOLD (same photo across two consecutive scenes, one continuous
    # plateKen) is CORRECT per fin-build.md:103-104 and must still pass.
    hold = good.replace('url(assets/img/s2.jpg)', 'url(assets/img/s1.jpg)')
    with open(os.path.join(proj, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(hold)
    r = score(tmp)[0]["checks"]["no_repeated_image"]
    assert r["status"] == PASS and "HOLD" in r["detail"], r

    # ...but the same photo with a gap between the two scenes is the real defect.
    gapped = good.replace(
        '<section class="scene clip" id="s2" data-start="5.0" data-duration="5.0" data-track-index="2">\n      <div class="bg" style="background-image:url(assets/img/s2.jpg)"></div></section>',
        '<section class="scene clip" id="s2" data-start="5.0" data-duration="2.0" data-track-index="2">\n      <div class="bg" style="background-image:url(assets/img/s2.jpg)"></div></section>'
        '<section class="scene clip" id="s3" data-start="7.0" data-duration="3.0" data-track-index="1">\n      <div class="bg" style="background-image:url(assets/img/s1.jpg)"></div></section>')
    with open(os.path.join(proj, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(gapped)
    r = score(tmp)[0]["checks"]["no_repeated_image"]
    assert r["status"] == FAIL and "non-adjacent" in r["detail"], r

    with open(os.path.join(proj, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(good)

    # now break four things at once and confirm each is caught independently
    bad = good.replace('url(assets/img/s2.jpg)', 'url(assets/img/s1.jpg)') \
              .replace('data-track-index="2"', 'data-track-index="1"') \
              .replace('class="rail cut-hi"', 'class="rail cut-en"') \
              .replace('<div class="bg" style="background-image:url(assets/img/s1.jpg)"></div></section>\n    <section class="scene clip" id="s2"',
                       '<div class="bg" style="background-image:url(assets/img/s1.jpg)"></div><p>costs $40</p></section>\n    <section class="scene clip" id="s2"')
    with open(os.path.join(proj, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(bad)
    with open(os.path.join(proj, "assets", "voice", "1.1.txt"), "w", encoding="utf-8") as fh:
        fh.write("25000 rupees every month (28:4)\n")

    ck = score(tmp)[0]["checks"]
    # no_repeated_image is NOT asserted here: this fixture reuses s1 on the adjacent
    # s2, which is a legal HOLD. Non-adjacent reuse is covered by `gapped` above.
    assert ck["track_alternation"]["status"] == FAIL, ck["track_alternation"]
    assert ck["watermark"]["status"] == FAIL, ck["watermark"]
    assert ck["currency_purity"]["status"] == FAIL, ck["currency_purity"]
    assert ck["vo_text_hygiene"]["status"] == FAIL, ck["vo_text_hygiene"]

    # a missing CREDITS file must FAIL, never pass silently
    os.unlink(os.path.join(proj, "CREDITS.txt"))
    assert score(tmp)[0]["checks"]["image_credits"]["status"] == FAIL

    # a composition that cannot be read yields NA across the board, never PASS
    os.unlink(os.path.join(proj, "index.html"))
    assert score(tmp) == [], "a project with no index.html is not a target"

    shutil.rmtree(tmp)
    print("selftest ok")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--slug")
    ap.add_argument("--root", default=ROOT)
    ap.add_argument("--json")
    ap.add_argument("--all", action="store_true",
                    help="also score the history lane and practice builds")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        return selftest()

    rows = score(args.root, args.slug, args.all)
    if not rows:
        sys.exit("no compositions found to score")
    summary = summarize(rows)
    print_report(rows, summary)

    out = args.json
    if out is None:
        ts = datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
        out = os.path.join(args.root, "evals", "results", f"{ts}.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        json.dump({"generated": datetime.datetime.now().isoformat(timespec="seconds"),
                   "summary": summary, "targets": rows}, fh, indent=2)
    print(f"\nwrote {os.path.relpath(out, args.root)}")


if __name__ == "__main__":
    main()
