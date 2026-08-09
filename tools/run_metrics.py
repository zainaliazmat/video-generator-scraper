#!/usr/bin/env python3
"""Per-agent token + wall-clock accounting for finance-video runs.

    python3 tools/run_metrics.py                          # every session, summary table
    python3 tools/run_metrics.py --slug passive-income-number
    python3 tools/run_metrics.py --session <uuid> --json runs/<id>/metrics.json
    python3 tools/run_metrics.py --selftest

WHERE THE NUMBERS COME FROM
---------------------------
Claude Code writes one JSONL transcript per session to
`~/.claude/projects/<cwd-slug>/<session-uuid>.jsonl`. Two records matter:

  1. An `Agent` tool_use block carries `input.subagent_type` — which fin-* stage ran.
  2. Its matching tool_result's sibling `toolUseResult` object carries the stage's
     own `totalTokens`, `totalDurationMs` and `totalToolUseCount`.

That second record is the only place a subagent's cost is written down; nothing in
the repo has it (audit/00-discovery.md §6 item 8 said so, and was wrong about the
transcripts). Main-loop (orchestrator) cost comes from `message.usage` on assistant
records, which is a different shape and is counted separately.

COVERAGE IS NOT 100% AND THE TOOL SAYS SO
-----------------------------------------
An agent dispatched with `run_in_background` returns a bare string instead of the
metrics object, so its cost is unrecoverable. Every report prints `covered/total`.
A summary that silently averaged only the covered calls would understate a run by
exactly the stages that ran longest in the background — so the uncovered count is
printed, never hidden.
"""

import argparse
import collections
import json
import os
import re
import sys

SLUG_RE = re.compile(r"(?:vault|studio)/videos/([a-z0-9]+(?:-[a-z0-9]+)+?)(?:-(?:hi|en)(?:-ch\d+)?)?[/\s'\"`]")

PROJECT_SLUG = "-home-zain-ali-Documents-YoutubeScraper"
SESSIONS_DIR = os.path.expanduser(f"~/.claude/projects/{PROJECT_SLUG}")

# usage keys that represent real billed input; cache_read is billed at a discount but
# is still tokens moved, so it is reported separately rather than folded in.
MAIN_LOOP_KEYS = ("input_tokens", "cache_creation_input_tokens", "output_tokens")


def _blocks(rec):
    msg = rec.get("message")
    if isinstance(msg, dict) and isinstance(msg.get("content"), list):
        return [b for b in msg["content"] if isinstance(b, dict)]
    return []


def _billed(usage):
    """Billed input+output for one API turn. cache_read is returned separately —
    it is discounted, and folding it in would triple every number."""
    if not isinstance(usage, dict):
        return 0, 0
    return (sum(usage.get(k) or 0 for k in MAIN_LOOP_KEYS),
            usage.get("cache_read_input_tokens") or 0)


def parse_subagent_dir(session_dir):
    """`<session>/subagents/agent-*.{meta.json,jsonl}` -> one row per subagent.

    This is the authoritative source: every turn the child made, with its usage.
    The parent transcript's `toolUseResult.totalTokens` is only a fallback for
    older sessions that predate these files.
    """
    sub = os.path.join(session_dir, "subagents")
    if not os.path.isdir(sub):
        return {}

    rows = {}
    for name in sorted(os.listdir(sub)):
        if not name.endswith(".meta.json"):
            continue
        stem = name[: -len(".meta.json")]
        try:
            with open(os.path.join(sub, name), encoding="utf-8") as fh:
                meta = json.load(fh)
        except (OSError, json.JSONDecodeError):
            continue

        billed = cache_read = turns = tool_calls = 0
        stamps = []
        jsonl = os.path.join(sub, stem + ".jsonl")
        if os.path.exists(jsonl):
            with open(jsonl, encoding="utf-8", errors="replace") as fh:
                for line in fh:
                    if not line.strip():
                        continue
                    try:
                        rec = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if rec.get("timestamp"):
                        stamps.append(rec["timestamp"])
                    msg = rec.get("message")
                    if rec.get("type") == "assistant" and isinstance(msg, dict):
                        b, c = _billed(msg.get("usage"))
                        if b or c:
                            turns += 1
                            billed += b
                            cache_read += c
                    for blk in _blocks(rec):
                        if blk.get("type") == "tool_use":
                            tool_calls += 1

        rows[meta.get("toolUseId") or stem] = {
            "agent": meta.get("agentType"),
            "description": meta.get("description"),
            "tokens": billed or None,
            "cache_read": cache_read,
            "turns": turns,
            "tool_calls": tool_calls,
            "duration_s": _span_seconds(stamps),
            "source": "subagent-transcript",
        }
    return rows


def _span_seconds(stamps):
    if len(stamps) < 2:
        return 0.0
    try:
        import datetime as _dt
        pts = [_dt.datetime.fromisoformat(s.replace("Z", "+00:00")) for s in stamps]
        return round((max(pts) - min(pts)).total_seconds(), 1)
    except (ValueError, TypeError):
        return 0.0


def parse_session(path):
    """One transcript -> {agents: [...], main_loop: {...}, slugs: set}."""
    pending, agents, slugs = {}, [], set()
    main = collections.Counter()
    main_turns = 0
    sub_rows = parse_subagent_dir(path[:-len(".jsonl")])
    claimed = set()

    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            if not line.strip():
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue

            for b in _blocks(rec):
                if b.get("type") == "tool_use" and b.get("name") == "Agent":
                    inp = b.get("input") or {}
                    pending[b.get("id")] = {
                        "agent": inp.get("subagent_type"),
                        "description": inp.get("description"),
                        "background": bool(inp.get("run_in_background")),
                        "at": rec.get("timestamp"),
                    }
                    # the dispatch prompt always names the run's vault dir; match that
                    # rather than guessing at kebab-case tokens (which caught CSS ids).
                    slugs.update(SLUG_RE.findall(str(inp.get("prompt", ""))))

                elif b.get("type") == "tool_result" and b.get("tool_use_id") in pending:
                    tuid = b["tool_use_id"]
                    meta = pending.pop(tuid)
                    if tuid in sub_rows:                       # authoritative
                        meta.update(sub_rows[tuid])
                        claimed.add(tuid)
                    else:                                       # older sessions only
                        res = rec.get("toolUseResult")
                        if isinstance(res, dict):
                            meta["tokens"] = res.get("totalTokens")
                            meta["duration_s"] = round((res.get("totalDurationMs") or 0) / 1000, 1)
                            meta["tool_calls"] = res.get("totalToolUseCount")
                            meta["source"] = "tool-result"
                        else:
                            meta["tokens"] = None
                            meta["source"] = None
                    agents.append(meta)

            msg = rec.get("message")
            if rec.get("type") == "assistant" and isinstance(msg, dict):
                usage = msg.get("usage")
                if isinstance(usage, dict):
                    main_turns += 1
                    for k in MAIN_LOOP_KEYS:
                        main[k] += usage.get(k) or 0
                    main["cache_read_input_tokens"] += usage.get("cache_read_input_tokens") or 0

    # An Agent call still pending at EOF never returned a matched result — but the
    # child may still have run and spent. Prefer its transcript over calling it 0.
    for tuid, meta in pending.items():
        if tuid in sub_rows:
            meta.update(sub_rows[tuid])
            claimed.add(tuid)
        else:
            meta["tokens"] = None
            meta["source"] = None
        agents.append(meta)

    # Subagent transcripts with no dispatch record in this transcript at all
    # (background work whose parent block we never saw). Real spend; count it.
    for tuid, row in sub_rows.items():
        if tuid not in claimed:
            orphan = dict(row)
            orphan["description"] = (orphan.get("description") or "") + " [orphan]"
            agents.append(orphan)

    return {
        "session": os.path.basename(path)[:-6],
        "agents": agents,
        "main_loop": dict(main),
        "main_loop_turns": main_turns,
        "slugs": sorted(slugs),
    }


def collect(sessions_dir, slug=None, session=None):
    paths = sorted(
        (os.path.join(sessions_dir, f) for f in os.listdir(sessions_dir) if f.endswith(".jsonl")),
        key=os.path.getmtime,
    )
    if session:
        paths = [p for p in paths if os.path.basename(p).startswith(session)]
    out = []
    for p in paths:
        if slug:
            # cheap prefilter: skip transcripts that never mention the slug
            with open(p, encoding="utf-8", errors="replace") as fh:
                if slug not in fh.read(50_000_000):
                    continue
        parsed = parse_session(p)
        if parsed["agents"] or parsed["main_loop_turns"]:
            out.append(parsed)
    return out


def summarize(sessions):
    by_agent = collections.defaultdict(lambda: {"n": 0, "covered": 0, "tokens": 0,
                                                "cache_read": 0, "duration_s": 0.0,
                                                "tool_calls": 0})
    main = collections.Counter()
    main_turns = 0
    for s in sessions:
        for a in s["agents"]:
            row = by_agent[a["agent"] or "<unknown>"]
            row["n"] += 1
            if a.get("tokens"):
                row["covered"] += 1
                row["tokens"] += a["tokens"]
                row["cache_read"] += a.get("cache_read") or 0
                row["duration_s"] += a.get("duration_s") or 0
                row["tool_calls"] += a.get("tool_calls") or 0
        for k, v in s["main_loop"].items():
            main[k] += v
        main_turns += s["main_loop_turns"]
    return {
        "sessions": len(sessions),
        "by_agent": dict(by_agent),
        "main_loop": dict(main),
        "main_loop_turns": main_turns,
    }


def print_report(summary, sessions):
    ba = summary["by_agent"]
    total_n = sum(r["n"] for r in ba.values())
    total_cov = sum(r["covered"] for r in ba.values())
    total_tok = sum(r["tokens"] for r in ba.values())

    print(f"sessions: {summary['sessions']}   agent invocations: {total_n}"
          f"   with token data: {total_cov} ({total_cov * 100 // max(total_n, 1)}%)")
    if total_cov < total_n:
        print(f"  ⚠ {total_n - total_cov} invocation(s) returned no metrics object "
              f"(background dispatch or unfinished) — their cost is NOT in the totals below.")
    print()
    print(f"{'agent':18}{'calls':>7}{'covered':>9}{'tokens':>12}{'mean':>10}{'share':>8}{'mins':>8}{'tools':>8}")
    print("-" * 88)
    for name, r in sorted(ba.items(), key=lambda kv: -kv[1]["tokens"]):
        mean = r["tokens"] // r["covered"] if r["covered"] else 0
        share = r["tokens"] * 100 / total_tok if total_tok else 0
        print(f"{name:18}{r['n']:7d}{r['covered']:9d}{r['tokens']:12d}{mean:10d}"
              f"{share:7.1f}%{r['duration_s'] / 60:8.0f}{r['tool_calls']:8d}")
    print("-" * 88)
    print(f"{'SUBAGENT TOTAL':18}{total_n:7d}{total_cov:9d}{total_tok:12d}")

    ml = summary["main_loop"]
    ml_billed = sum(ml.get(k, 0) for k in MAIN_LOOP_KEYS)
    print(f"{'ORCHESTRATOR':18}{summary['main_loop_turns']:7d}{'':9}{ml_billed:12d}"
          f"   (+{ml.get('cache_read_input_tokens', 0)} cache-read)")
    print(f"{'RUN TOTAL':18}{'':16}{total_tok + ml_billed:12d}")

    slugs = sorted({s for sess in sessions for s in sess["slugs"]})
    if slugs:
        print("\nslugs seen in dispatch prompts:", ", ".join(slugs[:12]))

    # Per-session coverage. An aggregate over mixed sessions is not a baseline; a
    # single session with high coverage is. This table is how you find one.
    fin = [s for s in sessions if any(str(a["agent"]).startswith("fin-") for a in s["agents"])]
    if len(fin) > 1:
        print(f"\n{'session':14}{'fin calls':>11}{'covered':>9}{'tokens':>12}  slugs")
        print("-" * 78)
        for s in sorted(fin, key=lambda x: -sum((a.get("tokens") or 0) for a in x["agents"])):
            calls = [a for a in s["agents"] if str(a["agent"]).startswith("fin-")]
            cov = [a for a in calls if a.get("tokens")]
            print(f"{s['session'][:12]:14}{len(calls):11d}{len(cov):9d}"
                  f"{sum(a['tokens'] for a in cov):12d}  {','.join(s['slugs'][:2]) or '-'}")


def selftest():
    """Parser check against a synthetic transcript covering both result shapes."""
    import tempfile

    recs = [
        {"type": "assistant", "message": {"content": [
            {"type": "tool_use", "name": "Agent", "id": "t1",
             "input": {"subagent_type": "fin-build",
                       "prompt": "slug my-video-slug cut hi; log to "
                                 "vault/videos/my-video-slug/logs/x.md and build "
                                 "studio/videos/my-video-slug-hi-ch2/index.html"}}],
            "usage": {"input_tokens": 10, "output_tokens": 5,
                      "cache_creation_input_tokens": 100, "cache_read_input_tokens": 900}}},
        {"type": "user", "toolUseResult": {"totalTokens": 12345, "totalDurationMs": 60000,
                                           "totalToolUseCount": 7},
         "message": {"content": [{"type": "tool_result", "tool_use_id": "t1"}]}},
        # background dispatch: result is a bare string, so no metrics
        {"type": "assistant", "message": {"content": [
            {"type": "tool_use", "name": "Agent", "id": "t2",
             "input": {"subagent_type": "fin-render", "run_in_background": True, "prompt": ""}}]}},
        {"type": "user", "toolUseResult": "done",
         "message": {"content": [{"type": "tool_result", "tool_use_id": "t2"}]}},
    ]
    tmp = tempfile.mkdtemp()
    path = os.path.join(tmp, "sess.jsonl")
    with open(path, "w", encoding="utf-8") as fh:
        for r in recs:
            fh.write(json.dumps(r) + "\n")

    # --- legacy shape: no subagents/ dir, metrics come from toolUseResult ---
    p = parse_session(path)
    assert len(p["agents"]) == 2, p["agents"]
    built = [a for a in p["agents"] if a["agent"] == "fin-build"][0]
    assert built["tokens"] == 12345 and built["source"] == "tool-result", built
    assert built["duration_s"] == 60.0, built
    rendered = [a for a in p["agents"] if a["agent"] == "fin-render"][0]
    assert rendered["tokens"] is None, rendered          # background => uncovered, not zero
    assert "my-video-slug" in p["slugs"], p["slugs"]
    assert p["main_loop"]["output_tokens"] == 5, p["main_loop"]

    s = summarize([p])
    assert s["by_agent"]["fin-build"]["covered"] == 1
    assert s["by_agent"]["fin-render"]["covered"] == 0   # counted as a call, not as 0 tokens
    assert s["by_agent"]["fin-render"]["n"] == 1

    # --- current shape: subagents/ dir wins, and covers the background call too ---
    sub = os.path.join(tmp, "sess", "subagents")
    os.makedirs(sub)
    for stem, tuid, kind, turns in (("agent-aaa", "t1", "fin-build", 2),
                                    ("agent-bbb", "t2", "fin-render", 1),
                                    ("agent-ccc", "t9", "fin-assets", 1)):
        with open(os.path.join(sub, stem + ".meta.json"), "w", encoding="utf-8") as fh:
            json.dump({"agentType": kind, "description": kind, "toolUseId": tuid}, fh)
        with open(os.path.join(sub, stem + ".jsonl"), "w", encoding="utf-8") as fh:
            for i in range(turns):
                fh.write(json.dumps({
                    "type": "assistant", "timestamp": f"2026-08-09T00:0{i}:00.000Z",
                    "message": {"usage": {"input_tokens": 1000, "output_tokens": 500,
                                          "cache_creation_input_tokens": 0,
                                          "cache_read_input_tokens": 7000},
                                "content": [{"type": "tool_use", "name": "Read", "id": f"r{i}"}]}}) + "\n")

    p2 = parse_session(path)
    b2 = [a for a in p2["agents"] if a["agent"] == "fin-build"][0]
    assert b2["source"] == "subagent-transcript", b2      # transcript beats toolUseResult
    assert b2["tokens"] == 3000, b2                       # 2 turns x 1500 billed
    assert b2["cache_read"] == 14000, b2                  # reported, never folded in
    r2 = [a for a in p2["agents"] if a["agent"] == "fin-render"][0]
    assert r2["tokens"] == 1500, r2                       # background call now covered
    orphan = [a for a in p2["agents"] if a["agent"] == "fin-assets"][0]
    assert orphan["tokens"] == 1500 and "[orphan]" in orphan["description"], orphan
    assert len(p2["agents"]) == 3, p2["agents"]

    import shutil
    shutil.rmtree(tmp)
    print("selftest ok")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--slug", help="only sessions whose transcript mentions this slug")
    ap.add_argument("--session", help="one session uuid (prefix ok)")
    ap.add_argument("--sessions-dir", default=SESSIONS_DIR)
    ap.add_argument("--json", help="also write the full structure here")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        return selftest()

    if not os.path.isdir(args.sessions_dir):
        sys.exit(f"ERROR: no session dir at {args.sessions_dir}")

    sessions = collect(args.sessions_dir, args.slug, args.session)
    if not sessions:
        sys.exit("no sessions matched")

    summary = summarize(sessions)
    print_report(summary, sessions)

    if args.json:
        os.makedirs(os.path.dirname(args.json) or ".", exist_ok=True)
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump({"summary": summary, "sessions": sessions}, fh, indent=2)
        print(f"\nwrote {args.json}")


if __name__ == "__main__":
    main()
