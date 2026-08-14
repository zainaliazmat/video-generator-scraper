#!/usr/bin/env python3
"""Close a finished run out into the vault: milestone note, catalog line, facts.

    python3 tools/close_out.py <slug>              # write all three
    python3 tools/close_out.py <slug> --dry-run    # print, touch nothing
    python3 tools/close_out.py --selftest

Replaces the `fin-archive` agent (audit/01-capability-matrix.md §5) and absorbs the
orchestrator's fact-promotion step (finance-video.md §5.1). `fin-archive` loaded
78,586 B of vault to do a template fill, was forbidden to write 71,616 B of what it
loaded (`fin-archive.md:39-47`), and had never once run on the current pipeline
shape.

WHAT THIS TOOL DOES **NOT** WRITE, AND WHY THAT IS THE DESIGN
-------------------------------------------------------------
The kill list called the milestone note "a template fill plus an append". Read the
notes: the reusable half of `japanese-money-methods/index.md` is the premise
correction binding the packaging twice, and no script derives that from disk. So
this tool writes exactly the half that IS derivable — runtimes, voices, measured
loudness, cue counts, scene counts, chapter rounds, spend — and leaves the
editorial half as headed TODO markers naming the question each section answers.

That split is not a shortcut, it is the point. The orchestrator already holds the
run narrative in context and `finance-video.md` §6.2 already makes it responsible
for distilling it ("distill first, archive second"). A haiku agent re-reading the
vault to paraphrase what the orchestrator already knew was the expensive part; the
measuring is the cheap part, and it is the part that was being done by hand.

Facts are promoted ADDITIVELY, under a dated heading, and never merged into the
curated tables — a script that rewrites `money-facts-2026.md` in place is one bad
regex away from corrupting the pool every script draws from. HARD rows only; SOFT
stays in staging. Re-running is safe: an already-promoted slug is skipped.
"""
import argparse
import json
import os
import re
import sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import pipeline_check as pc  # noqa: E402

MONEY_FACTS = os.path.join(ROOT, "vault", "knowledge", "money-facts-2026.md")
INDEX = os.path.join(ROOT, "vault", "index.md")
OWED = ("proof-listen · thumbnail pick · caption upload · "
        "upload · analytics after 28 days")
TODO = "<!-- TODO close_out: {} -->"
SECTIONS = [
    ("Firsts", "what this run did that no earlier run did — or `none`"),
    ("The durable lessons", "what the NEXT run must do differently, and the "
                            "evidence for it. This is the half of the note that "
                            "compounds; the tables above are just the receipts"),
    ("What broke", "every defect that cost a re-render, with its root cause"),
]


def measure_cut(slug, cut, fmt):
    """Everything about one cut that is readable off disk. Missing → None."""
    sdir, out = pc.studio_dir(slug, cut), {}
    cfg = fmt["cuts"][cut]
    out["channel"], out["voice"] = cfg["channel"], cfg.get("voice_name", cfg["voice_id"])
    pub = os.path.join(sdir, "renders", f"PUBLISH-1080p-{cut}.mp4")
    master = os.path.join(sdir, "renders", f"FINAL-1080p-{cut}.mp4")
    shipped = pub if os.path.exists(pub) else master
    out["render"] = os.path.relpath(shipped, ROOT) if os.path.exists(shipped) else None
    out["seconds"] = pc.ffprobe_duration(shipped) if out["render"] else None
    # Loudness off the file that is actually uploaded — the master is 7-8 dB quieter
    # by design and quoting it in the note has misreported every cut so far.
    out["lufs"] = out["dbtp"] = None
    if os.path.exists(pub):
        try:
            m = __import__("loudnorm").measure(pub)
            out["lufs"], out["dbtp"] = m["input_i"], m["input_tp"]
        except (SystemExit, KeyError, ValueError, ImportError):
            pass
    srt = os.path.join(sdir, "renders", f"captions-{cut}.srt")
    out["cues"] = (open(srt, encoding="utf-8").read().count(" --> ")
                   if os.path.exists(srt) else None)
    script = os.path.join(pc.vault_dir(slug), f"script-{cut}.md")
    out["lines"] = len(pc.read_vo_lines(script)) if os.path.exists(script) else None
    out["pack"] = os.path.exists(os.path.join(pc.vault_dir(slug),
                                              f"youtube-metadata-{cut}.md"))
    # run.json.chapters is keyed by CUT and then by chapter number — the two cuts
    # lock independently and one can ship while the other fails (finance-video.md
    # §3.5), so a single global count would misreport every partial run.
    chapters = (pc.load_run(slug).get("chapters") or {}).get(cut, {})
    out["locked"] = sum(1 for c in chapters.values() if c.get("status") == "locked")
    out["chapters"] = len(chapters)
    # Rounds it took to LOCK. An unlocked chapter has not spent its rounds yet, and
    # printing `?` for it reads as a lost measurement rather than unfinished work.
    out["rounds"] = ", ".join(str(c.get("round", "?"))
                              for _, c in sorted(chapters.items())
                              if c.get("status") == "locked") or "—"
    return out


def fmt_clock(seconds):
    if not seconds:
        return "—"
    m, s = divmod(seconds, 60)
    return f"**{int(m)}:{s:04.1f}**"


def milestone_note(slug, fmt):
    run = pc.load_run(slug)
    cuts = run.get("cuts") or ["en"]
    per = {c: measure_cut(slug, c, fmt) for c in cuts}
    locked = sum(per[c]["locked"] for c in cuts)
    planned = sum(per[c]["chapters"] for c in cuts)
    today = date.today().isoformat()

    head = "| | " + " | ".join(f"{c} — {per[c]['channel']}" for c in cuts) + " |\n"
    head += "|---|" + "---|" * len(cuts) + "\n"
    for label, key, render in (("runtime", "seconds", fmt_clock),
                               ("VO lines", "lines", lambda v: v or "—"),
                               ("voice", "voice", lambda v: f'ElevenLabs "{v}"'),
                               ("loudness", "lufs", lambda v: f"{v} LUFS" if v else "—"),
                               ("true peak", "dbtp", lambda v: f"{v} dBTP" if v else "—"),
                               ("captions", "cues", lambda v: f"{v} cues" if v else "—"),
                               ("chapters locked", "locked", lambda v: v),
                               ("review rounds", "rounds", lambda v: v),
                               ("publish pack", "pack", lambda v: "✅" if v else "—"),
                               ("render", "render", lambda v: f"`{v}`" if v else "**not rendered**")):
        head += f"| {label} | " + " | ".join(str(render(per[c][key])) for c in cuts) + " |\n"

    body = [
        "---",
        f"summary: Milestone note for {slug} — {run.get('tier', '?').upper()} tier, "
        f"{run.get('architecture', '?')}, {locked} of {planned or '?'} "
        f"chapters locked. " + TODO.format("one sentence on what this run is FOR"),
        f"updated: {today}",
        f"source: run.json, vault/videos/{slug}/logs/, and the measured renders. "
        f"Tables generated by tools/close_out.py — re-run it rather than hand-editing them.",
        "---",
        "",
        f"# {slug} — " + TODO.format("the shipped title"),
        "",
        f"> **Topic as briefed.** {run.get('topic', '—')}",
        "",
        head,
        f"**Tier** {run.get('tier', '?')} · **style** {run.get('architecture', '?')}",
        "",
    ]
    for title, question in SECTIONS:
        body += [f"## {title}", "", TODO.format(question), ""]
    body += [f"## Owed before publish", "", OWED, ""]
    return "\n".join(body)


def catalog_line(slug, fmt):
    run = pc.load_run(slug)
    state = "✅ RENDERED" if all(
        os.path.exists(os.path.join(pc.studio_dir(slug, c), "renders",
                                    f"PUBLISH-1080p-{c}.mp4"))
        for c in (run.get("cuts") or ["en"])) else "🔧 IN PRODUCTION"
    return (f"- [[videos/{slug}/index]] — {state} {date.today().isoformat()} — "
            f"{run.get('tier', '?')} tier, {run.get('architecture', '?')}. "
            + TODO.format("the shipped titles, the hero numbers, and the one "
                          "durable lesson — a catalog line nobody can skim is a "
                          "catalog line nobody reads"))


def promote_facts(slug, dry_run=False):
    """HARD rows from facts-staging → money-facts, additively and once."""
    staging = os.path.join(pc.vault_dir(slug), "facts-staging.md")
    if not os.path.exists(staging):
        return [f"no facts-staging.md for {slug} — nothing to promote"]
    marker = f"## Promoted from {slug}"
    pool = open(MONEY_FACTS, encoding="utf-8").read()
    if marker in pool:
        return [f"already promoted: '{marker}' is in money-facts-2026.md"]
    # A staged fact is a table ROW whose last cell carries the tag. Rows are taken
    # verbatim with the heading they sat under, because the heading is what says
    # which market the number belongs to.
    rows, heading = [], None
    for line in open(staging, encoding="utf-8").read().splitlines():
        if line.startswith("#"):
            heading = line.lstrip("# ").strip()
        elif line.startswith("|") and re.search(r"\bHARD\b", line.rsplit("|", 2)[-2:][0]):
            rows.append((heading, line))
    if not rows:
        return [f"no HARD rows found in {staging} — SOFT and COMPUTED stay in staging"]

    out = [f"\n{marker} ({date.today().isoformat()})\n",
           f"HARD rows only, lifted verbatim from `vault/videos/{slug}/facts-staging.md` "
           f"after the render passed. SOFT/COMPUTED rows stay in staging by rule "
           f"(`fin-facts.md:32-36`). Section headings are kept.\n"]
    last = None
    for heading, row in rows:
        if heading != last:
            out.append(f"\n**{heading}**\n")
            last = heading
        out.append(row)
    text = "\n".join(out) + "\n"
    if not dry_run:
        with open(MONEY_FACTS, "a", encoding="utf-8") as fh:
            fh.write(text)
    return [f"promoted {len(rows)} HARD row(s) to "
            f"{os.path.relpath(MONEY_FACTS, ROOT)}"]


def close_out(slug, dry_run=False):
    fmt = pc.load_format()
    if not os.path.isdir(pc.vault_dir(slug)):
        sys.exit(f"ERROR: no run at {pc.vault_dir(slug)}")
    note_path = os.path.join(pc.vault_dir(slug), "index.md")
    note = milestone_note(slug, fmt)
    line = catalog_line(slug, fmt)
    said = []

    if os.path.exists(note_path):
        said.append(f"KEPT {os.path.relpath(note_path, ROOT)} — it already exists; "
                    f"generated tables printed below, merge them by hand rather than "
                    f"losing the prose")
        print(note)
    elif not dry_run:
        open(note_path, "w", encoding="utf-8").write(note)
        said.append(f"wrote {os.path.relpath(note_path, ROOT)}")
    else:
        print(note)

    catalog = open(INDEX, encoding="utf-8").read()
    if f"[[videos/{slug}/index]]" in catalog:
        said.append(f"catalog already lists {slug}")
    elif not dry_run:
        # Newest first, directly under the `## Videos` heading.
        head, sep, tail = catalog.partition("## Videos\n")
        if not sep:
            sys.exit(f"ERROR: no `## Videos` section in {INDEX}")
        open(INDEX, "w", encoding="utf-8").write(head + sep + line + "\n" + tail)
        said.append(f"added the catalog line to {os.path.relpath(INDEX, ROOT)}")
    else:
        said.append(f"would add: {line}")

    said += promote_facts(slug, dry_run)
    for s in said:
        print(f"  · {s}")
    print(f"\nNext: fill every {TODO.format('…')} in "
          f"{os.path.relpath(note_path, ROOT)} and the catalog line. "
          f"Nothing derives those from disk — that is the distillation step.")
    return 0


def _selftest():
    import shutil
    import tempfile

    tmp = tempfile.mkdtemp(prefix="closeout-")
    keep_root, keep_mf, keep_ix = ROOT, MONEY_FACTS, INDEX
    try:
        globals()["MONEY_FACTS"] = os.path.join(tmp, "money-facts.md")
        globals()["INDEX"] = os.path.join(tmp, "index.md")
        pc.ROOT = tmp
        vault = os.path.join(tmp, "vault", "videos", "s")
        os.makedirs(vault)
        pc.atomic_write_json(os.path.join(vault, "run.json"),
                             {"slug": "s", "topic": "T", "tier": "medium",
                              "architecture": "per-line-chapters", "cuts": ["en"],
                              "chapters": {"en": {"1": {"status": "locked", "round": 2},
                                                  "2": {"status": "building"}}}})
        open(os.path.join(vault, "script-en.md"), "w").write("**1.1**\n> one\n")
        open(MONEY_FACTS, "w").write("# facts\n")
        open(INDEX, "w").write("# vault\n\n## Videos\n- [[videos/old/index]] — old\n")
        open(os.path.join(vault, "facts-staging.md"), "w").write(
            "# PART A\n"
            "| 401k limit | $23,500 | IRS | HARD |\n"
            "| Median salary | $59,000 | blog | SOFT |\n"
            "## US ($)\n"
            "| Savings rate | 4.6% | BEA | HARD |\n")

        assert close_out("s") == 0
        note = open(os.path.join(vault, "index.md"), encoding="utf-8").read()
        assert "TODO close_out" in note, "the editorial half must be marked, never faked"
        assert "1 of 2 chapters locked" in note, note
        assert "| chapters locked | 1 |" in note, note
        assert "| review rounds | 2 |" in note, note
        assert "not rendered" in note, "a missing render must say so, not read as fine"

        cat = open(INDEX, encoding="utf-8").read()
        assert cat.index("[[videos/s/index]]") < cat.index("[[videos/old/index]]"), \
            "the catalog is newest-first"

        pool = open(MONEY_FACTS, encoding="utf-8").read()
        assert "401k limit" in pool and "Savings rate" in pool
        assert "Median salary" not in pool, "a SOFT row was promoted"
        assert "**PART A**" in pool and "**US ($)**" in pool, \
            "rows lost the heading that says which market they belong to"

        # idempotent: a second close-out must not double-promote or duplicate
        assert close_out("s") == 0
        assert open(MONEY_FACTS, encoding="utf-8").read() == pool, "promoted twice"
        assert open(INDEX, encoding="utf-8").read() == cat, "catalog line duplicated"
        assert open(os.path.join(vault, "index.md"), encoding="utf-8").read() == note, \
            "an existing milestone note was overwritten — the prose is unrecoverable"
        print("selftest OK")
    finally:
        pc.ROOT = keep_root
        globals()["MONEY_FACTS"], globals()["INDEX"] = keep_mf, keep_ix
        shutil.rmtree(tmp, ignore_errors=True)


def main(argv=None):
    p = argparse.ArgumentParser(description="close a finished run out into the vault")
    p.add_argument("slug", nargs="?")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--selftest", action="store_true")
    a = p.parse_args(argv)
    if a.selftest:
        return _selftest()
    if not a.slug:
        p.error("need <slug>")
    return close_out(a.slug, a.dry_run)


if __name__ == "__main__":
    sys.exit(main())
