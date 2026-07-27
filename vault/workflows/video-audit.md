---
summary: Reusable open-handed prompt to have Claude audit a finished video for engagement/retention — hook, script, visuals, motion, audio-sync — and return prioritized fixes + reusable rules. Deliberately non-prescriptive.
updated: 2026-07-22
source: creator request 2026-07-22 — wants an open prompt that lets Claude use its own judgment, not a fixed checklist.
---

# Workflow — video engagement audit (open-handed)

Drop the prompt below into a fresh Claude Code session **in this repo** and swap the project path for whichever video you want audited (`studio/videos/<slug>`). It hands Claude the goal + the artifacts + how to inspect them, then gets out of the way — no forced steps, so it uses its own creative-director judgment. Pairs with [[knowledge/haryanvi-hindi-script-style]] and [[knowledge/niches/india-finance-market]].

> **Why open-handed:** a rigid checklist caps the audit at what we already thought of. This prompt sets the objective (hold the viewer, make it more interesting) and lets Claude bring frameworks we didn't list.

## The prompt

```
You are auditing a finished short video from my faceless personal-finance
YouTube channel. Your one job: figure out how to make it genuinely more
interesting, more engaging, and better at holding a viewer to the end —
then tell me, plainly and specifically.

THE VIDEO
- Project: studio/videos/emergency-fund   (swap for any videos/<slug>)
- Rendered draft: newest file in that project's renders/*.mp4
- Composition (the actual visuals + timing + animation): index.html
- Narration: the Haryanvi-Hindi VO in assets/voice/ (script text in
  assets/voice/haryanvi-lines.json; durations drive the scene timing)
- Audience: young Indians, 20-28, first salaries. Delivery is Hindi in a
  Haryanvi accent (meant to be funny, blunt, attention-grabbing). Style is
  a bold "blockframe" motion-graphics look, 16:9, ~2-3 min. Educational
  only — no specific products recommended.
- Channel knowledge lives in vault/knowledge/ (haryanvi-hindi-script-style,
  indian-business-culture-slang, niches/india-finance-market). Read what's
  useful; don't feel bound by it.

HOW TO LOOK (use whatever gets you the truest picture — you decide)
You can read index.html to see exactly how every scene is built, take frame
snapshots with `npx hyperframes snapshot --at <t1,t2,...>` (writes PNGs +
a contact sheet you can view), read the narration text and its timings, and
read the script/scene structure. Inspect as deeply or broadly as you want.

WHAT I ACTUALLY WANT
Use your own best judgment and whatever frameworks you trust — retention
curves, hook theory, motion-design principles, comedic timing, information
design, whatever. I am NOT giving you a checklist on purpose. Think like a
sharp creative director who wants this specific video to perform.

Look at all of it and tell me honestly:
- Is the hook strong enough in the first 3-5 seconds? Would you keep watching?
- Where does attention sag, and why — pacing, repetition, dead air, a weak beat?
- Is the script tight, clear, and funny where it should be? Any wasted lines,
  any confusing bits, any better way to say it in Haryanvi?
- Are the visuals appealing and legible, or flat/templated? Color, type,
  motion, transitions, negative space, variety scene-to-scene?
- Does audio + visual land on the same beat (numbers appearing as spoken, etc.)?
- What's the single highest-impact change? What are the next few?

DELIVER
A candid, prioritized read — biggest wins first, each with the concrete change
and *why* it helps engagement (not vague praise). Show me before/after where it
helps. Then distill it into a short set of reusable rules I should follow on
every future video in this channel. Be opinionated. Push back on my choices if
they're weak, and propose bold alternatives, not just safe tweaks.
```

## After an audit

Fold the durable "reusable rules" it returns into the relevant vault note (script style, design, or [[knowledge/best-practices]]) so each video compounds on the last.
