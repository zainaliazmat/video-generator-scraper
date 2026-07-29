# Vault — operating manual (read me first)

This folder is the **knowledge layer** for the faceless YouTube channel project.
It is an Obsidian vault AND a plain markdown folder — Claude Code reads it
natively with Read/Grep; the human opens it in the Obsidian app. No MCP, no
plugin, no sync machinery.

## The two-home memory rule (one home per fact — never duplicate)

| Home | What it owns |
|---|---|
| `../library.db` (SQLite)  | Raw scraped video rows: views, subs, dedup, times_seen. Numbers live HERE, never in notes. |
| **this vault** (markdown) | Everything else durable: skills, niche dossiers, verified facts (dated + sourced), scrape findings, video artifacts, templates — **and all decisions/status/session notes** (what was decided / killed / pending, current status). |

This is a **Claude Code local project — the vault is the single source of truth.**
The `skills/` files are canonical. There is no external log and no other surface
to sync to: if it matters, it lives in the vault.

## Session protocol (how this vault learns over time)

1. **Start** (channel work): read `index.md` and the relevant notes for current status.
2. **Work**: cite facts from vault notes; verify anything stale (facts carry
   dates — AI-tool prices move monthly, re-verify per the skill's rules).
   Before scripting a topic, run the study loop: `workflows/video-study.md`.
3. **End**: distill what was learned into the right vault note (update, don't
   append-forever). Decisions and status update the relevant note in place —
   full analysis and evidence included; there's nowhere else for it to go.
4. **`.claude/agents/` is procedure, not memory.** Agent prompts carry *how* a
   stage works; every *fact* (rates, voices, caps) lives in `tools/format.json`
   or a vault note, read by path. When a fact changes, change it in its one
   home — never inside an agent prompt.

## The finished-video rule (a URL means done)

Standing rule (creator, 2026-07-29, extending 2026-07-10): **a video is finished
the moment its YouTube URL exists.** Handing over the URL is the signal — nothing
else is. From then on it has two homes and no third: the **video** lives on
YouTube, its **source + knowledge** live here. `studio/` holds work in progress
only, never a shipped video.

One command per finished video:

```bash
tools/archive_cut.py <slug> --hi <url> --en <url>     # --dry-run to preview
```

It copies the reproducing text into `vault/videos/<slug>/src/{hi,en,thumbs}/`,
byte-verifies every file, records the URLs in the milestone note, then deletes
`studio/videos/<slug>*`. Copy → verify → delete, in that order, because
**nothing under `studio/videos/` is tracked by any git** — a bad copy is
unrecoverable. It refuses to delete anything without a URL.

1. **Distill first, archive second.** Capture every durable learning into the
   milestone note (`videos/<slug>/index.md`) + any reusable runbook/design BEFORE
   running it. The render is about to be the only place some of this lived.
2. **Kept** (~1–5 MB per video): `index.html`, `meta.json`, `hyperframes.json`,
   `package.json`, `gen_vo_*.sh`, `gen_timing.mjs`, `*.md`, `assets/voice/*.txt`
   (the VO lines), `assets/img/*.src` (the image prompts), `CREDITS.txt` (stock
   attribution), `thumbnail*.png` (the shipped deliverable).
3. **Dropped**: renders, `*.jpg`/`*.mp3`/`*.wav`, fonts, `gsap.min.js`,
   `package-lock.json`, `node_modules/`, `snapshots/`, `grain.png` — regenerable.
4. **The trade this makes:** the archive is *reproducible*, not *free*. Prompts
   and VO lines survive; the generated images and audio do not, so a re-render
   re-pays ElevenLabs + image credits. That is the accepted price of a delivered
   video's home being YouTube.
5. **Two gotchas a re-render hits** (found archiving the first five):
   - `gen_vo_*.sh` hardcodes an absolute `cd` into the now-deleted studio dir.
     Repoint it before running.
   - **VO is always reproducible; photography often is not.** The `.src`
     image-prompt convention starts at **pay-yourself-first** — anything older
     (50-30-20-rule, needs-vs-wants, emergency-fund) archived *no* prompts, and
     emergency-fund has no stock `CREDITS.txt` either. For those, the storyboard
     note and the archived `index.html` are the only record of what a scene
     showed. Every new cut must write `.src` prompts + CREDITS so this stops
     being true.

**Note format.** Every archived video's milestone note ends with one
`## Published + archived (<date>)` section: state line, a `| Cut | Channel | URL |
Thumbnail |` table, what `src/` holds, and what is still owed. `archive_cut.py`
writes it; keep the shape when editing by hand.

Channel is implied by the cut, not by the path: `hi/` = @cashguruguides,
`en/` = @moneymavens101 ([[knowledge/channels]]).

⚠️ The history/AI-tools cuts still in `studio/videos/` are mirrored text-only in
`../compositions/` — the only git-tracked copy of their code. Do not delete that
mirror until each of those videos goes through this rule.

**The point (creator's framing):** each shipped video is a **milestone**, not a
throwaway. The next one starts FROM its runbook + design system + learnings and must
be *better* — that compounding is the real growth. First milestone:
[[videos/video-hist-01-travel/index]].

Git versions this vault — history of every note IS the audit trail of learning.

## Note conventions

- Frontmatter on every note: `summary:` (1–2 sentences — lets a session preview
  without opening), `updated:` (date), `source:` where the facts came from.
- Every factual claim carries its date and source inline. Triangulate ≥2 sources
  for money/spec claims (per the channel skill).
- Link related notes with `[[wikilinks]]`. `index.md` is the catalog — keep it
  current when adding notes.
