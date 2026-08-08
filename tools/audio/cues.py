#!/usr/bin/env python3
"""Derive a chapter's SFX cue list from its composition, one cue per real motion call.

    python3 tools/audio/cues.py studio/videos/<slug>-<cut>-ch<N> [--write]

Reads the project's root composition (index-claudedesign.html if present, else
index.html), parses `var S = {…}` and every motion call, and writes
`assets/audio.json` with CHAPTER-LOCAL times.

WHY A GENERATOR. The shipped full-cut lists carry 24 cues in ten minutes — one
`transition` in the whole video — which is why scene changes read as silent. The
fix is cue DENSITY, and density hand-authored across sixteen chapters is sixteen
chances to bind a sound to a motion that is not there. Every cue this emits is
bound to a call that exists in the file, at that call's own time.

THE RULES (vault/videos/japanese-money-methods/HANDOVER.md §4c, creator-approved
on -en ch1, whose hand-authored list this reproduces):

  transition  every scene joint (the scene's data-start) AND every in-scene
              fade() of a `.bg` — a framing swap IS a dissolve, which is
              transition's declared helper in tools/audio/kit.json.
              NEVER on a HOLD (same object, one continuous zoom across two
              lines): a whoosh there announces a change that is not happening.
  cta         pop("#sN-cta")            the closing block, once per cut
  stamp       pop("#sN-stmt")           the verdict slam
  hero        pop/rise/countUp on #sN-num   the scene's one big number
  buzz        a frame that SHOWS the object making the noise (diegetic; the
              only cue that cannot be derived, so it is declared in BUZZ below)
  tick        span("#sN-mf") / pulse()  a measure bar draining, a beat landing
  chip        pop / popEach             ONE per cascade, not one per element —
              unless the COUNT is the point (COUNTED below)
  reveal      fade("#sN-band"), else rise("#sN-stmt") at +1.10 — never the
              kicker at +0.30, which collides with its own joint transition

One CONTENT cue per scene, taken in that priority order, plus the joint and any
framing swaps. That is what gives -en ch1 its 22 cues in 57s; a chapter that
emits four in ninety seconds means the parser missed the file's shape, not that
the chapter is quiet.
"""
import argparse
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# These three are per-VIDEO facts — each storyboard's §5 — NOT tool constants.
# They shipped hardcoded to japanese-money-methods' scene ids, so every later
# video silently inherited another video's holds: on passive-income-number that
# is a suppressed s1→s2 joint and a buzz offset measured against a Lottie this
# cut does not have (found 2026-08-07). An absent table now means NO special
# cases, never someone else's — a wrong sound is worse than a missing one.
#
# Home: the CUT dir — studio/videos/<slug>-<cut>/assets/cues-tables.json — read
# by every chapter of that cut, so the fact has one home. Resolved by stripping
# -ch<N> off the project path rather than through the chapter's assets/, which
# §3b describes as a symlink to the cut but which fin-build creates as a real
# directory of copies. Shape:
#   {"holds": [["s13","s14"]], "buzz": {"s1": 0.95}, "counted": ["s2"],
#    "dry": ["s1","s2"]}
HOLDS = {"hi": set(), "en": set()}
BUZZ = {}
COUNTED = set()

# Scenes that take their JOINT but no CONTENT cue. A chapter can be deliberately
# quiet — passive-income-number's storyboard §2 declares every statement rise in
# the cold open silent, so the generator's 7 correct-in-general `reveal`s were 7
# wrong-here cues, and running --write would have overwritten the hand-correct
# 7-cue list with 13. Density is the default; silence has to be declarable.
DRY = set()


def load_tables(proj, cut):
    """Populate HOLDS/BUZZ/COUNTED from the cut's own table file."""
    cut_dir = re.sub(r"-ch\d+$", "", proj)
    path = os.path.join(cut_dir, "assets", "cues-tables.json")
    if not os.path.exists(path):
        print(f"note: no {path} — deriving with no holds, no buzz, no counted "
              f"cascades. If this cut has continuous-zoom pairs or a diegetic "
              f"buzz, write that file from storyboard-{cut}.md §5.", file=sys.stderr)
        return
    t = json.load(open(path, encoding="utf-8"))
    HOLDS[cut] = {tuple(pair) for pair in t.get("holds", [])}
    BUZZ.update({(cut, sid): off for sid, off in t.get("buzz", {}).items()})
    COUNTED.update(t.get("counted", []))
    DRY.update(t.get("dry", []))

CALL = re.compile(r'\b(pop|popEach|rise|fade|span|pulse|countUp|draw|exit|breathe|'
                  r'ken|plateKen|playLottie|dissolve|shove|fill|drift)\('
                  r'\s*("[^"]*"|[A-Za-z_$][\w$]*)\s*,\s*([^,)]+)')


def at(expr, S):
    """A motion call's time argument, absolute or `S.sN + x`, as seconds."""
    expr = expr.strip()
    try:
        return float(expr)
    except ValueError:
        pass
    m = re.match(r"S\.(s\d+)\s*(?:\+\s*([\d.]+))?$", expr)
    return S[m.group(1)] + float(m.group(2) or 0) if m and m.group(1) in S else None


def parse(path):
    html = open(path, encoding="utf-8").read()
    S = {k: float(v) for k, v in re.findall(
        r"(s\d+):\s*([\d.]+)", re.search(r"var S = \{(.*?)\};", html, re.S).group(1))}
    order = [re.search(r'id="(s\d+)"', t).group(1)
             for t in re.findall(r'<section[^>]*class="[^"]*\bscene\b[^"]*"[^>]*>', html)]
    # EVERY script block, not just the last one. `rindex("<script>")` picked up
    # whichever block happened to come last — on passive-income-number-hi-ch1 that
    # is the corpus/rate assert, which contains zero motion calls, so the generator
    # could only ever emit joint transitions and would have silently reproduced the
    # very "scene changes read as silent" defect it was written to fix (2026-08-07).
    script = "\n".join(re.findall(r"<script[^>]*>(.*?)</script>", html, re.S))
    calls = []
    for fn, sel, arg in CALL.findall(script):
        t = at(arg, S)
        if t is not None:
            calls.append((fn, sel.strip('"'), t, arg))
    return S, order, calls, script


def cues(path, cut, first_is_joint):
    S, order, calls, script = parse(path)
    out = []

    def add(t, name, why):
        out.append({"at": round(t, 3), "name": name, "_": why})

    for i, sid in enumerate(order):
        mine = [c for c in calls if c[1].startswith("#" + sid + "-")
                or c[1].startswith("#" + sid + " ") or c[1] == "#" + sid]
        prev = order[i - 1] if i else None

        # 1 · the joint
        hold = prev is not None and (prev, sid) in HOLDS[cut]
        if (i or first_is_joint) and not hold:
            add(S[sid], "transition",
                f"{sid} joint" if i else f"{sid} · chapter joint")
        elif hold:
            out.append({"_hold": f"{prev}->{sid} is a HOLD — one object, one "
                                 f"continuous zoom. No transition."})

        # 2 · every framing swap: fade() on a .bg IS a dissolve
        swaps = 0
        for fn, sel, t, _ in mine:
            if fn == "fade" and re.fullmatch(rf"#{sid}-bg\d", sel):
                add(t, "transition", f"{sid} framing swap — fade({sel})")
                swaps += 1

        # 3 · ONE content cue, first match wins
        def find(fn, pat):
            return next(((t, s) for f, s, t, _ in mine
                         if f == fn and re.fullmatch(pat, s)), None)

        pick = None
        # DRY silences DERIVED cues only. An explicitly declared BUZZ survives it:
        # `dry` says "this scene's statement rises are silent" (a taste rule about
        # motion the generator inferred), while `buzz` says "this frame SHOWS the
        # object making the noise" (a per-scene fact someone wrote down). Killing
        # the diegetic sound too took ch1 to 6 cues where fin-editor ruled 7.
        dry = sid in DRY
        if dry:
            out.append({"_dry": f"{sid} is DRY — joint (and any declared buzz) "
                                f"only, no derived content cue"})
        for fn, pat, name, note in () if dry else (
                ("pop", rf"#{sid}-cta", "cta", "the closing block"),
                ("pop", rf"#{sid}-stmt", "stamp", "the verdict slam"),
                ("pop", rf"#{sid}-num", "hero", "the scene's one big number"),
                ("rise", rf"#{sid}-num", "hero", "the scene's one big number"),
                ("countUp", rf"#{sid}-num", "hero", "the scene's one big number"),
        ):
            hit = find(fn, pat)
            if hit:
                pick = (hit[0], name, f"{sid} · {note} — {fn}({hit[1]})")
                break

        if not pick and (cut, sid) in BUZZ:
            pick = (S[sid] + BUZZ[(cut, sid)], "buzz",
                    f"{sid} · the frame SHOWS the object making this noise — "
                    f"the kit's one diegetic cue")

        if not pick and not dry:
            hit = find("span", rf"#{sid}-mf") or find("pulse", rf"#{sid}-.*")
            if hit:
                pick = (hit[0], "tick", f"{sid} · {hit[1]}")

        if not pick and not dry:
            casc = [(t, s) for f, s, t, _ in mine if f in ("pop", "popEach")]
            if casc:
                casc.sort()
                if sid in COUNTED:
                    # the COUNT is the point: one click per item, read off the
                    # helper's own stagger argument.
                    # popEach(sel, at, stagger, dur) — motion.js:48. This read arg 4
                    # (dur) until 2026-08-08 and so emitted the cascade at the wrong
                    # spacing: on hi ch1 s6 it wanted 0.45 where the build draws 0.60,
                    # and `--write` would have regressed a correct chapter. Caught by
                    # fin-render diffing the build's audio.json against this tool.
                    m = re.search(rf'popEach\(\s*"[^"]*{sid}[^"]*"\s*,[^,]+,\s*([\d.]+)',
                                  script)
                    step = float(m.group(1)) if m else 0.5
                    # ponytail: 3 clicks assumed. Every cascade shipped so far is three
                    # chips; count the selector's elements if a 4-chip cascade appears.
                    n = 3
                    for k in range(n):
                        add(casc[0][0] + k * step, "chip",
                            f"{sid} · one click per item — the COUNT is the point"
                            if k == 0 else "")
                    pick = "done"
                else:
                    for t, s in casc:      # one per cascade, never one per element
                        add(t, "chip", f"{sid} · {s} — ONE click for the cascade")
                    pick = "done"

        # The fallback reveal is what a scene gets when nothing else happened in
        # it. A scene that swapped its photograph mid-line HAS had something
        # happen and already carries a cue for it, so it takes no second one —
        # this is the -en ch1 list's own shape at s3 and s5.
        if not pick and not swaps and not dry:
            hit = find("fade", rf"#{sid}-band")
            if hit:
                pick = (hit[0], "reveal", f"{sid} · the band under the drawn layer")

        if not pick and not swaps and not dry:
            hit = find("rise", rf"#{sid}-stmt")
            if hit:
                pick = (hit[0], "reveal",
                        f"{sid} · the statement rise (+1.10, never the kicker)")

        if pick and pick != "done":
            add(pick[0], pick[1], pick[2])

    out.sort(key=lambda c: c.get("at", -1))
    return out, S, order


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()

    proj = os.path.abspath(a.project)
    cut = "hi" if "-hi" in os.path.basename(proj) else "en"
    ch = int(re.search(r"-ch(\d+)$", os.path.basename(proj)).group(1))
    src = os.path.join(proj, "index-claudedesign.html")
    if not os.path.exists(src):
        src = os.path.join(proj, "index.html")

    load_tables(proj, cut)
    sfx, S, order = cues(src, cut, first_is_joint=ch > 1)
    n = sum(1 for c in sfx if "at" in c)
    span = max(S.values()) if S else 0
    doc = {
        "_comment": f"Chapter {ch} sound pass, -{cut}. Times are CHAPTER-LOCAL. "
                    f"GENERATED by tools/audio/cues.py from "
                    f"{os.path.basename(src)} — every cue is bound to a real "
                    f"motion call in that file per tools/audio/kit.json's helper "
                    f"column. Merge into the full cut by adding this chapter's "
                    f"offset to every `at` (tools/cut_assemble.py does it).",
        "_density": f"{n} cues over {order[0]}-{order[-1]}, about one per "
                    f"{span / max(n - 1, 1):.1f}s of scene starts. The reference "
                    f"is -en ch1: 22 cues in 57.189s.",
        "music": "bed-resolve",
        "sfx": sfx,
    }
    if a.write:
        dest = os.path.join(proj, "assets", "audio.json")
        if os.path.islink(os.path.join(proj, "assets")):
            sys.exit(f"{proj}/assets is a SYMLINK to the cut — writing audio.json "
                     f"there would overwrite the cut's own list. Replace the link "
                     f"with a directory of per-entry links first.")
        with open(dest, "w", encoding="utf-8") as fh:
            json.dump(doc, fh, ensure_ascii=False, indent=1)
            fh.write("\n")
        print(f"{os.path.relpath(dest, ROOT)}: {n} cues")
    else:
        json.dump(doc, sys.stdout, ensure_ascii=False, indent=1)
        print()


if __name__ == "__main__":
    main()
