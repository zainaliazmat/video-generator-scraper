#!/usr/bin/env python3
"""VO-vs-frame cross-check — the half of the rate constraint the build cannot see.

run.json.constraints.derived_income_carries_assumption says a derived income figure
carries its rate in frame or an explicit ILLUSTRATIVE marker. build.mjs mechanises
that as an in-page assert, but the assert scans ON-SCREEN TOKENS only, so it is
structurally incapable of catching the case that actually shipped: hi 6.8 SPOKE a
money figure over a frame that printed neither a rate nor a marker. Recorded as
`owed.derived_income_assert_is_frame_only`.

This is that cross-check. For every scene, it reads the VO line the scene is
anchored to and the text the frame renders, and fails when the VO speaks money
over a bare frame.

Scene sN is anchored to timing.json lines[N-1] — one line = one clip = one scene,
the pipeline's own invariant (script-hi.md "Engine rule"). Verified per run: the
scene ids present across a cut's chapter projects must be exactly 1..len(lines).

Money in the VO is detected on MAGNITUDE WORDS, not on a currency mark. Digits are
spelled out for the TTS engine and the currency word is often dropped once the unit
is established — hi 6.8 is literally "इस पच्चीस हज़ार को", no रुपये anywhere. A
check that required the currency mark would have missed the one line it exists for.
That over-flags a non-money "ten thousand", so --ack takes scene ids already ruled.

The RATE and MARKER patterns are lifted out of the generated index.html's own assert
rather than restated here: one home per fact, and a per-cut rate list that drifts
between the build and the checker is worse than no checker.

    tools/check_vo_frame.py <slug> --cut hi [--chapter 3] [--ack s41,s55]
"""
import argparse
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# हज़ार/हजार (thousand) · लाख (lakh) · करोड़/करोड (crore) — every way this pipeline's
# two scripts can name a money magnitude out loud, in either script.
MAGNITUDE = re.compile(
    r"ह(?:ज़|ज)ार|लाख|करोड़?|"
    r"\b(?:thousand|lakh|crore|million|billion)\b",
    re.I,
)
# A bare currency mark with digits counts too — a VO line may quote "₹25,000" as text.
CURRENCY_FIGURE = re.compile(r"[₹$]\s?[\d,]+|\b\d[\d,]*\s*(?:rupees|dollars)\b", re.I)

TAG = re.compile(r"<[^>]+>")
# script, style AND comments. The comment case is not hypothetical: these builds carry
# long prose comments that quote the constraint text verbatim, so an unstripped comment
# saying "ILLUSTRATIVE" would satisfy the very check it is explaining — the same shape
# as the Lottie guard that fired on the comment describing the trap it prevents.
DROP = re.compile(r"<(script|style)\b.*?</\1>|<!--.*?-->", re.S | re.I)
SCENE = re.compile(r'<section class="scene[^"]*"\s+id="(s\d+)"', re.I)


def js_regex(src, name):
    """Pull `var NAME = /.../;` out of the build's own assert and port it to Python."""
    m = re.search(r"var\s+%s\s*=\s*/(.+?)/([a-z]*);" % name, src)
    if not m:
        return None
    body, flags = m.group(1), m.group(2)
    # build.mjs writes the assert inside a JS template literal, so `\$` and `\\d`
    # reach the file escaped one level deeper than the regex means.
    body = body.replace("\\\\", "\\")
    return re.compile(body, re.I if "i" in flags else 0)


def frame_text(html, scene_id, next_id):
    """Text the scene renders — script/style stripped, so the assert's own source
    can never satisfy the assert."""
    start = html.find('id="%s"' % scene_id)
    end = html.find('id="%s"' % next_id) if next_id else len(html)
    chunk = html[start:end if end > start else len(html)]
    return TAG.sub(" ", DROP.sub(" ", chunk))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--cut", required=True)
    ap.add_argument("--chapter", type=int, help="one chapter; default every built chapter")
    ap.add_argument("--ack", default="", help="comma-separated scene ids already ruled clean")
    a = ap.parse_args()

    acked = {s.strip() for s in a.ack.split(",") if s.strip()}
    voice = os.path.join(ROOT, "studio/videos/%s-%s/assets/voice" % (a.slug, a.cut))
    timing = os.path.join(voice, "timing.json")
    if not os.path.exists(timing):
        sys.exit("FAIL check_vo_frame — no timing.json at %s" % timing)
    lines = json.load(open(timing))["lines"]

    pat = "studio/videos/%s-%s-ch%s" % (a.slug, a.cut, a.chapter if a.chapter else "*")
    projects = sorted(glob.glob(os.path.join(ROOT, pat)),
                      key=lambda p: int(re.search(r"ch(\d+)$", p).group(1)))
    if not projects:
        sys.exit("FAIL check_vo_frame — no chapter project matches %s" % pat)

    bad, warn, checked = [], [], 0
    for proj in projects:
        ch = re.search(r"ch(\d+)$", proj).group(1)
        page = os.path.join(proj, "index.html")
        if not os.path.exists(page):
            warn.append("ch%s has no index.html — not built" % ch)
            continue
        html = open(page, encoding="utf-8").read()
        rate = js_regex(html, "RATE")
        if not rate:
            bad.append("ch%s index.html carries no RATE assert — the build's own in-frame "
                       "guard is missing, so this check has nothing to agree with" % ch)
            continue
        # the hi build inlines /ILLUSTRATIVE/ instead of naming a MARKER var; en names it
        # and widens it with published-statistic provenance. Absent means the narrow one.
        marker = js_regex(html, "MARKER") or re.compile("ILLUSTRATIVE")
        ids = SCENE.findall(html)
        for i, sid in enumerate(ids):
            n = int(sid[1:])
            if not 1 <= n <= len(lines):
                bad.append("%s is outside the %d VO lines — the scene/line anchor is broken"
                           % (sid, len(lines)))
                continue
            side = os.path.join(voice, "%s.txt" % lines[n - 1]["id"])
            if not os.path.exists(side):
                bad.append("%s: no VO sidecar %s" % (sid, side))
                continue
            vo = open(side, encoding="utf-8").read()
            checked += 1
            if not (MAGNITUDE.search(vo) or CURRENCY_FIGURE.search(vo)):
                continue
            txt = frame_text(html, sid, ids[i + 1] if i + 1 < len(ids) else None)
            if rate.search(txt) or marker.search(txt):
                continue
            if sid in acked:
                warn.append("ch%s %s (line %s) acked" % (ch, sid, lines[n - 1]["id"]))
                continue
            bad.append("ch%s %s (line %s) SPEAKS money over a frame carrying neither a "
                       "rate nor an ILLUSTRATIVE marker: %s"
                       % (ch, sid, lines[n - 1]["id"], vo.strip()[:90]))

    for w in warn:
        print("warn: %s" % w)
    if bad:
        print("FAIL check_vo_frame — %d scene(s):" % len(bad))
        for b in bad:
            print("  %s" % b)
        sys.exit(1)
    print("PASS check_vo_frame — %s %s, %d scenes cross-checked against their VO lines"
          % (a.slug, a.cut, checked))


def selftest():
    """One runnable check: the hi 6.8 shape must fail, and the same line must pass
    once its frame carries the rate."""
    bare = '<section class="scene" id="s1"><p>WHAT IT BUYS</p></section>'
    rated = '<section class="scene" id="s1"><p>WHAT IT BUYS</p><p>3.0%</p></section>'
    src = 'var RATE = /3\\\\.0%/;\nvar MARKER = /ILLUSTRATIVE/;'
    rate = js_regex(src, "RATE")
    assert rate and rate.pattern == "3\\.0%", rate
    assert MAGNITUDE.search("अब इस पच्चीस हज़ार को एक सरकारी आँकड़े के बगल में रखिए।")
    assert MAGNITUDE.search("that is twenty five hundred thousand a month")
    assert not MAGNITUDE.search("notice this — the phone buzzes exactly once")
    assert not rate.search(TAG.sub(" ", bare))
    assert rate.search(TAG.sub(" ", rated))
    # neither the assert's own source nor a comment quoting the rule may satisfy it
    for poison in ("<script>var RATE = /3.0%/;</script>",
                   "<!-- carries 3.0%, or an ILLUSTRATIVE marker -->"):
        p = bare.replace("</section>", poison + "</section>")
        assert not rate.search(TAG.sub(" ", DROP.sub(" ", p))), poison
        assert not re.compile("ILLUSTRATIVE").search(TAG.sub(" ", DROP.sub(" ", p))), poison
    print("PASS check_vo_frame --selftest")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
    else:
        main()
