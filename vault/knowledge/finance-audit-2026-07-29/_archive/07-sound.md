# 07 — Sound: everything audible on @cashguruguides + @moneymavens101

Scope: loudness, music, SFX, voice, silence, and how any of it survives a HyperFrames
render. Research date 2026-07-29. Repo read-only; every measurement below was taken on
the real files in this repo.

Tags: `FACT` = verified against a spec, a licence, or a number I measured here.
`UNVALIDATED` = a belief about audience response. **No analytics exist for these channels.**

---

## 1. Establishing the facts — what is actually in the audio track today

### 1.1 Zero music, zero SFX — CONFIRMED

`FACT` `vault/videos/good-debt-vs-bad-debt/src/en/index.html` contains exactly **nine**
`<audio>` elements and nothing else audible:

```html
<audio id="vo1" src="assets/voice/en1.mp3" data-start="0.4"    data-duration="17.371" data-track-index="10" data-volume="1"></audio>
…
<audio id="vo9" src="assets/voice/en9.mp3" data-start="161.621" data-duration="15.961" data-track-index="10" data-volume="1"></audio>
```

Nine sections on track 1, nine audio rows on track 10, `data-volume="1"` on all nine, no
other media element. The design doc states it plainly:
`vault/knowledge/design-finance-blockframe.md:163` — **"No SFX. The finance format is
voice + motion only."** There is no music line in that document at all — music is not
"turned off", it was never specified.

### 1.2 §5d of the production skill DOES cover music — and none of it reached finance

`FACT` `vault/skills/hyperframes_production.md` §5d ("BACKGROUND MUSIC — sourcing +
mixing", learned on Pompeii 2026-07-17) exists and says:

- Incompetech (Kevin MacLeod, CC-BY 4.0, direct mp3 URLs) works headless; **Pixabay is a
  dead end for agents** (no music API, Cloudflare-walled); YouTube Audio Library needs the
  creator's browser.
- **Never set bed volume by a flat factor** — a `volume=0.10` guess shipped an inaudible
  bed (~−55 dB) on Pompeii. Method: measure each track's loudness, gain-stage to a
  **~−33 dB bed (~15 dB under VO)**, duck ~−8 dB further under dense VO, verify by
  rendering `bed-check.wav`.
- Slot music per act, ~4 s crossfade at act boundaries; silence is a valid slot.

§5 of the same file also documents an SFX vocabulary (`boom/whoosh/whoosh2/pop/shimmer/tick`,
real Pixabay packs in `studio/library/sfx/`).

**None of it was ever applied to a finance cut.** §5d and §5 were written for the
history/TechToolTester lane. The finance design doc supersedes the TechToolTester design
doc and, in doing so, dropped the audio layer entirely rather than re-specifying it.

### 1.3 The TTS pipeline, verbatim

`FACT` `tools/tts/batch.py:49-51` is the only place voice settings are set:

```python
tts.synthesize(key, voice, line["text"], out, model,
               stability=0.5, similarity=0.75,
               style=fmt["tts"]["style"], seed=seed)
```

- `stability=0.5` and `similarity=0.75` are **hardcoded in the script**, not in
  `format.json`. This violates the vault's own rule (`vault/CLAUDE.md`: "every *fact*
  (rates, voices, caps) lives in `tools/format.json` or a vault note").
- `style` comes from `format.json` → **0.0**, the flattest value the API accepts.
- `speed` is **never passed** → defaults to 1.0.
- `seed` is a CLI flag that `fin-voice`'s allowlisted command line never supplies
  (`.claude/agents/fin-voice.md:32`), so **every generation is unseeded**. A `--force`
  re-roll produces a different read. That is a determinism hole in a pipeline whose whole
  identity is determinism.

`FACT` `tools/format.json` `tts` block: model `eleven_multilingual_v2`, style 0.0,
min_clip_bytes 10240, min_clip_seconds 1.0, duration_tolerance_pct 35,
silence_mean_volume_db −50.0.

`FACT` `tools/pipeline_check.py:141-190` (`check_voice_dir`) checks only: file size,
duration-vs-chars ±35 %, mean volume > −50 dB (a "is it silent" guard), and scene
arithmetic. **Nothing checks loudness, peak, or level consistency between the nine clips.**

---

## 2. LOUDNESS — settled, with a proven recipe

### 2.1 What happens to a −22 LUFS upload

`FACT` YouTube's playback reference is ≈ **−14 LUFS integrated**, and **YouTube applies
attenuation only — it does not apply positive gain**. A −22 LUFS upload plays back at
−22 LUFS. It does not get turned up. (Multiple independent sources agree; this also
matches what `fin-render` already wrote into
`vault/videos/credit-history/logs/fin-render-hi-2.md:304-311`.) Contrast Spotify, which
does boost quiet masters — YouTube does not.

Consequence: every video on both channels plays **7–8 dB quieter than the video before it
in the feed**. On a phone speaker at 60 % volume that is the difference between "audible
in a kitchen" and "not". This is the only defect in my scope that is a measurable spec
violation rather than a taste call.

### 2.2 The measured state (all six cuts)

`FACT` from the QA logs and my own `loudnorm` analysis pass run today on the two
`credit-history` masters:

| Cut | Integrated | True peak | LRA | Deficit vs −14 |
|---|---|---|---|---|
| credit-history hi | **−22.17 LUFS** | −4.33 dBTP | 3.30 | −8.17 LU |
| credit-history en | **−21.19 LUFS** | −3.00 dBTP | 3.60 | −7.19 LU |
| good-debt hi / en | −22.02 / −21.09 | — | — | −8.0 / −7.1 |
| pay-yourself-first hi / en | −22.24 / −21.13 | — | — | −8.2 / −7.1 |

`FACT` Root cause measured at source. Per-clip integrated loudness of the shipped
ElevenLabs mp3s:

- en1–en9: −23.4 … −25.0 LUFS (mean ≈ **−24.1**)
- h1–h9: −24.3 … −25.9 LUFS (mean ≈ **−25.2**)

ElevenLabs returns ~−24 LUFS; there is **no gain staging anywhere in the pipeline**, so
the master is whatever the API returned. The hi cut is consistently ~1 LU quieter than en
because the Harsh voice returns quieter than Brian — another reason to normalise at the
master rather than per-voice.

### 2.3 Why a flat gain cannot work (and why the fix is one filter, not a multiply)

`FACT` hi is −22.17 LUFS with a −4.33 dBTP peak → crest ≈ 17.8 dB. Lifting to −14 by gain
alone needs +8.17 dB, which would put the peak at **+3.84 dBTP** — hard clipping. Same for
en: +7.19 dB on a −3.00 dBTP peak = **+4.19 dBTP**.

So `volume=+8dB` is not an option, and `loudnorm` with `linear=true` will refuse the
linear path and fall back to dynamic. **That fallback is fine here** — LRA is 3.3–3.6 LU
(TTS speech is almost perfectly consistent), so the dynamic path has essentially no gain
riding to do and cannot pump. Single-pass pumping is a real risk on wide-dynamic music;
it is not a risk on an LRA-3.3 TTS read.

### 2.4 The correct 2026 target

`FACT`/recommended: **I = −14 LUFS, TP = −1.5 dBTP, LRA = 11** for spoken-word YouTube.

Two notes that matter:

- **Target −1.5 dBTP, not −1.0.** The AAC re-encode overshoots. I measured it: targeting
  −1.5 landed the finished file at **−1.26 dBTP**, which passes `fin-render`'s existing
  `< −1 dBTP` gate with 0.26 dB to spare. Targeting −1.0 would have landed at ≈ −0.76 and
  **failed the pipeline's own gate.** This is the single non-obvious number in the recipe.
- YouTube transcodes to AAC/Opus on their side too, so keeping ≥1 dB of true-peak headroom
  is not paranoia.

### 2.5 The proven recipe — two-pass, video stream-copied

Pass 1 (analysis, read-only, ~9 s for a 3-minute file):

```bash
ffmpeg -hide_banner -nostats -i renders/FINAL-1080p-<cut>.mp4 -vn \
  -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null - 2>&1 | tail -14
```

Real output, credit-history en:

```json
{ "input_i":"-21.19", "input_tp":"-3.00", "input_lra":"3.60",
  "input_thresh":"-31.73", "target_offset":"0.55" }
```

Pass 2 — feed those five numbers back, **copy the video stream**:

```bash
ffmpeg -y -i renders/FINAL-1080p-<cut>.mp4 \
  -map 0 -c:v copy \
  -af "loudnorm=I=-14:TP=-1.5:LRA=11:\
measured_I=-21.19:measured_TP=-3.00:measured_LRA=3.60:\
measured_thresh=-31.73:offset=0.55:linear=true" \
  -c:a aac -b:a 192k -ar 48000 \
  renders/PUBLISH-1080p-<cut>.mp4
```

`FACT` I ran exactly this on `credit-history-en`. Result:

| | Before | After |
|---|---|---|
| Integrated | −21.19 LUFS | **−14.17 LUFS** |
| True peak | −3.00 dBTP | **−1.26 dBTP** (gate is −1) |
| LRA | 3.60 | 3.70 |
| Wall clock | — | **19.8 s** |
| Container duration | 173.248 s | 173.300 s (+0.052 s AAC tail) |

19.8 seconds of CPU on a machine that already spends ~18 minutes encoding the video. The
video stream is bit-identical (`-c:v copy`), so the frame-level gate-② proof from
`fin-render` is not invalidated — only the audio track changed.

**The +0.052 s container growth is the one thing to watch.** `fin-render`'s runtime check
compares against `timing.json` (en: 173.227 s). Before: +0.021 s. After: +0.073 s. Still
inside the 0.1 s budget, but the check should be run on `PUBLISH-*.mp4` with that known
constant documented, or it will look like a regression to the next agent.

### 2.6 Do NOT normalise the mp3s instead

Tempting (then the render comes out right and there is no second pass), but wrong:
re-encoding mp3 adds encoder delay/padding, which shifts every clip duration. `timing.json`
holds **measured** durations and `pipeline_check` cross-checks them at 0.05 s tolerance
(`timing_ffprobe_tolerance_s`). Normalising the sources would either break that check or
force a regeneration of the whole timing chain. It also becomes wrong the moment music and
SFX exist, because the thing that needs to hit −14 is the **mix**, not the VO.

**Normalise once, at the master, after the render. Nowhere else.**

### 2.7 Verdict

**Confirmed: this is the cheapest high-value fix on the board.** ~20 s of CPU per cut,
one ffmpeg invocation, zero API spend, zero creative risk, no change to any composition,
and it moves the channel from 7–8 dB below the feed to exactly at it. The vault already
lists it as owed (`vault/videos/credit-history/index.md:324`); it just needs to stop being
"optional".

Owner: the **orchestrator** (`.claude/commands/finance-video.md`), immediately after the
encode step at line 112, because `fin-render` is explicitly forbidden from running
non-analysis ffmpeg (`.claude/agents/fin-render.md:20`: "`ffmpeg` (analysis filters
only)"). Either the orchestrator runs it, or `fin-render`'s allowlist gets one narrowly
scoped exception. Cheapest: orchestrator, same background slot as the encode.

---

## 3. MUSIC

### 3.1 Why this format needs a bed more than most — the dead-air measurement

`FACT` I measured the trailing silence baked into every shipped clip:

| | hi | en |
|---|---|---|
| Trailing silence inside the clip (last speech → clip end, −45 dB) | 0.26–0.41 s, mean **0.376 s** | 0.32–0.40 s, mean **0.365 s** |

That silence sits **on top of** `format.json`'s `scene.tail_seconds: 1.0`, and the next
scene then adds `scene.lead_in_seconds: 0.4` before its clip starts.

**True gap between the last word of scene N and the first word of scene N+1:**

```
0.376 (clip tail) + 1.0 (scene tail) + 0.4 (next lead-in) = ~1.78 s
```

Eight times per video, plus a 0.4 s head and a ~1.38 s tail:

| Cut | Total silence | Runtime | Share |
|---|---|---|---|
| hi | ≈ **15.98 s** | 177.6 s | **9.0 %** |
| en | ≈ **15.90 s** | 173.2 s | **9.2 %** |

`FACT` **Roughly one minute in every eleven of these videos is pure digital silence with a
Ken Burns move over it.** Not room tone — silence, because there is no bed and TTS has no
noise floor. On headphones that reads as a file that stopped.

`UNVALIDATED` (no analytics) but this is the strongest structural argument for a bed:
music does not need to be "noticed" to work here — it needs to make those nine gaps stop
sounding like a fault.

### 3.2 The spec

**How many beds: ONE.** A 3-minute blockframe-9 does not have room for act-level music
slotting (§5d's per-act model is a 20-minute-documentary pattern). One bed, one file, one
`<audio>` row.

**Character (this is a dark, serious money-facts channel):**

- Minor key, **85–95 BPM**, no vocals, **no melody line on top** — a melodic lead competes
  with speech for the same attention channel and is the fastest way to make a bed annoying.
- Wanted: low sub-pulse, muted/plucked ostinato, sparse percussive tick, a long sustained
  low string or pad. Documentary-investigation underscore. Tension held flat, not resolved.
- **Explicitly NOT:** uplifting corporate, bright piano, "inspirational" swells, lo-fi
  hip-hop, hopeful major-key resolution. The design doc's own register is "dark, dense,
  confident. Nothing decorative, nothing cute." Music has to obey the same rule the
  visuals do.

> ⚠️ Note for whoever wires this to the `media-use` skill: its BGM mood-inference table
> maps `finance / fintech / bank / payment / invest / wealth` → **"calm cinematic, soft
> strings, subtle piano, restrained percussion, 92 BPM"**. That is the wrong brand for
> this channel. **Always pass an explicit `prompt` / `query`; never let the keyword
> default fire.**

**Levels — and the method, not a guess.** §5d's warning is the correct one: never pick a
bed volume by feel. The method that makes `data-volume` meaningful and reusable:

1. **Normalise every bed to a known level at import**, once, when it lands in
   `studio/library/music/`:
   ```bash
   ffmpeg -i raw.mp3 -af loudnorm=I=-20:TP=-3:LRA=7 -c:a libmp3lame -q:a 2 bed-<name>.mp3
   ```
   Now every bed is −20 LUFS and one set of numbers works for all of them. This is what
   kills the Pompeii "flat factor → inaudible bed" failure at the root.
2. VO sits at ≈ −24 LUFS at `data-volume="1"`.
3. Targets, expressed as LU under the voice:

| State | Bed target | Under VO | Linear gain from a −20 LUFS bed | `volume` value |
|---|---|---|---|---|
| Under speech (ducked) | ≈ −42 LUFS | **18 LU** | −22 dB | **0.08** |
| In the gaps (open) | ≈ −36 LUFS | 12 LU | −16 dB | **0.16** |
| The one planned silence | −∞ | — | — | **0.0** |

So: **an 8 dB duck**, matching §5d's "~−8 dB further under dense VO". The gap level is
what the viewer actually hears the music at; the ducked level is just "not a hole".

**Where it enters and exits:**

- In at `t = 0`, fade **0 → 0.16 over 1.5 s**, so the bed is already up before the first
  word at 0.4 s. Never a hard start.
- Out over the **last 2.5 s** of the CTA, `0.16 → 0` — the video ends on the wordmark in
  silence.
- **One planned drop to 0.0** — 1.2 s before the video's single biggest number reveal,
  back up over 0.8 s after it lands. This is the one place silence beats music, and it is
  worth exactly one use per video. §5d already licenses this ("silence is a valid slot").

**Does the bed change at the turn?** Not by swapping files. A 3-minute video does not
support a crossfade without it reading as a mistake. Instead, at the turn (the pivot from
"here's the trap" to "here's what to do"), **lift the open level 0.16 → 0.22 (+3 dB) over
1.2 s and leave it there.** Same track, more air, reads as the video opening up. If a
second bed is ever wanted, the correct shape is a 2 s crossfade on the scene boundary with
both tracks pre-normalised to −20 LUFS — but start with the level move; it is free.

### 3.3 The duck envelope, generated — not hand-placed

`timing.json` already holds `audio_start` and `duration` for all nine lines. The nine duck
envelopes fall straight out of it, in the same generator that writes the `S` map:

```js
// #bgm ducks under each VO line. Numbers from timing.json; never hand-typed.
tl.set("#bgm", { volume: 0 }, 0);
tl.to("#bgm", { volume: 0.16, duration: 1.5, ease: "power1.out" }, 0);
LINES.forEach(function (L) {
  tl.to("#bgm", { volume: 0.08, duration: 0.35, ease: "power1.out"  }, L.audio_start - 0.25);
  tl.to("#bgm", { volume: 0.16, duration: 0.60, ease: "power1.inOut" }, L.audio_start + L.duration - 0.30);
});
tl.to("#bgm", { volume: 0, duration: 2.5, ease: "power1.in" }, TOTAL - 2.5);
```

The release fires at `audio_start + duration − 0.30`, i.e. right at the point the clip's
own ~0.37 s of trailing silence begins. **The bed comes up exactly as the voice stops** —
that is what converts the 1.78 s dead gap into a deliberate beat.

### 3.4 Sourcing — real 2026 prices and licence terms, for TWO monetised channels

The constraint that eliminates most options: **many music licences are per-channel**, and
several libraries **register their own catalogue with Content ID and will claim you**
unless the specific channel is safelisted. Two channels means two channel IDs to cover.

| Option | 2026 cost | Two monetised channels? | Content ID | Agent-automatable? |
|---|---|---|---|---|
| **YouTube Audio Library** | **$0** | **Yes** — the licence attaches to the track, not to a channel; there is no channel count | **None.** YouTube's own help page: *"Copyright-safe music and sound effects downloaded from the Audio Library won't be claimed by a rights holder through the Content ID system."* And: *"If you're in the YouTube Partner Program, you can monetize videos with music and sound effects from the Audio Library."* Some tracks are CC-BY and need a description credit — filter for "Attribution required" and just avoid them | **No** — needs the creator's YouTube Studio browser session (§5d already knows this). One session, ~15 min, done |
| Uppbeat **Creator** | **$8.99/mo**, or **$62.93/yr** annual (≈ $5.24/mo) | **Yes — 3 YouTube channel safelists** (Essentials = 1, Pro = 10) | Tracks **are** in Content ID. The safelist is the mechanism that stops claims — **both channel IDs must be safelisted or you will get claimed.** Uppbeat also suspends the safelist if payment lapses | Partly (download needs an account session) |
| Epidemic Sound **Personal** | ~$10–15/mo | **NO — 1 channel per platform** | Safelist by connecting channels | No |
| Epidemic Sound **Pro/Commercial** | **$30/mo** annual, **$75/mo** monthly | Yes — 3 channels per platform | Safelist | No |
| Artlist Pro | $9.99–39.99/mo | 3 channels per platform; lifetime universal licence | Universal licence | No |
| Pixabay music | $0 | Yes — no channel limit, no attribution required | **Real risk.** Pixabay's own blog: some music tracks *"might trigger Content ID claims"*, cleared **after the fact** with a downloadable Pixabay License Certificate. Reactive, not preventive | **No** — Cloudflare-walled, no music API (§5d) |
| Suno Pro | $10/mo | Yes — commercial rights granted to paid subscribers, no channel limit; output not registered in Content ID | None claimed. Note: 2026 terms moved from "you own it" to "granted commercial rights", and 100 %-AI music likely isn't copyrightable — irrelevant for a bed you never license out | Yes (API) |
| **MusicGen** (`facebook/musicgen-small`) | $0 | **NO — DO NOT USE** | — | Yes, and that is the danger |

#### ⚠️ The landmine in the default path

`FACT` The `media-use` skill's **offline BGM fallback is MusicGen**
(`~/.claude/skills/media-use/audio/references/bgm.md`: "Local generation (Lyria →
MusicGen) — the fallback when there is no credential"). `facebook/musicgen-small`'s **model
weights are released under CC-BY-NC 4.0 — non-commercial only** (the code is MIT; the
weights are not). Its output on a monetised YouTube channel is a licence violation.

The skill's own preflight is what saves you here — it says stop and ask before generating
locally — but an autonomous pipeline with no HeyGen credential and no human in the loop
will take that branch silently. **If `media-use` is ever wired into `/finance-video`, pin
`bgm.mode` explicitly and never let the auto path reach MusicGen.** (Lyria RealTime is the
other local route and Google's terms do permit commercial use of Gemini outputs — but it
needs `$GEMINI_API_KEY`, and outputs carry a SynthID watermark.)

#### Recommendation

**YouTube Audio Library. $0/month.**

Reasons, in order: it is the only option carrying a **first-party guarantee that it will
not be Content ID claimed**; it has **no channel count at all**, so both channels are
covered by construction rather than by a subscription tier; and it costs nothing at 2
pairs/week or 20.

The whole cost is one browser session. `studio/library/music/` already exists and its
README already says exactly this: *"BGM tracks (YT Audio Library, license-safe). Empty —
creator downloads."* The folder was built for this and never filled.

**What to download:** 5–6 beds in the character above, filtered to "Attribution not
required", each ≥3:30 so no looping is needed, run through the −20 LUFS normalise in §3.2.
Rotate them; at a 3-minute runtime with the bed 18 LU under the voice, six beds is more
variety than anyone will consciously register, and reusing a bed across videos is a
*feature* — it is how a channel gets a sonic signature.

**The paid fallback, if the creator refuses browser sessions:** **Uppbeat Creator at
$62.93/year (3 channel safelists)**. Both channel IDs must be entered in the safelist —
their catalogue *is* in Content ID and the safelist is the only thing standing between you
and a claim on every upload. That is ~$5.24/mo, cheapest paid option that legitimately
covers two monetised channels.

**Not Epidemic Sound Personal** — 1 channel per platform, so it does not cover this
operation at all; the version that does is $30/mo annual, 6× the Uppbeat price for the
same channel count.

---

## 4. SFX

### 4.1 Sourcing is already solved, twice, for $0

`FACT` Two licence-cleared SFX libraries are already on this machine:

1. **`~/.claude/skills/media-use/audio/assets/sfx/`** — 20 files + `manifest.json` with
   per-file duration and placement notes. `CREDITS.md` states they are Pixabay Content
   License and that it *"permits: Commercial and non-commercial use / Modification and
   remixing / **Redistribution as part of derivative works (such as videos rendered with
   HyperFrames)** … without any attribution requirement."*
2. **`studio/library/sfx/`** — the creator's own Pixabay packs, already re-cut to the
   canonical form: **48 kHz mono, peak −1 dB, fades baked in** — `boom.wav`, `whoosh.wav`,
   `whoosh2.wav`, `pop.wav`, `shimmer.wav`, `tick.wav`, with the source packs kept
   alongside for swapping.

The Pixabay Content-ID caveat in §3.4 is a **music** caveat. Short SFX are not
Content-ID-registered in practice, and a Pixabay License Certificate clears a claim if one
ever appears. Nothing to buy.

Prefer `studio/library/sfx/` where a sound exists there — it is already gain-staged and
faded, which is half the work.

### 4.2 The kit — 7 sounds, mapped to the existing motion helpers

The nine helpers in `design-finance-blockframe.md` §5 are: `rise`, `pop`, `fade`, `pulse`,
`fill`, `countUp`, `breathe`, `ken`, `drift`. Only four of them are *events*. Those four
get sound; the rest are continuous and must stay silent.

| # | Cue | File | Fires on | Helper | `data-volume` | dB | Per video |
|---|---|---|---|---|---|---|---|
| 1 | **chip in** | `pop.mp3` (0.72 s) | `.chip` entry, `back.out(1.7)` | `pop`, `popEach` | **0.10** | −20 | ≤3 |
| 2 | **stamp slam** | `impact-bass-1.mp3` (2.12 s) | `.stamp` landing — the verdict | `pop` on `.stamp` | **0.22** | −13 | ≤2 |
| 3 | **bar fill** | `whoosh-short.mp3` (0.57 s) | `.fill2` scaleX start | `fill` | **0.09** | −21 | ≤1 |
| 4 | **number lands** | `ping.mp3` (1.32 s) | end of the tween, at `at + 1.2 s` | `countUp` | **0.14** | −17 | ≤2 |
| 5 | **the turn** | `whoosh.mp3` (0.57 s) | the ONE pivot cut, nowhere else | scene boundary | **0.16** | −16 | **exactly 1** |
| 6 | **hero reveal** | `impact-bass-2.mp3` (2.59 s) | the single biggest number/`.statstrip` | `rise` on `.huge`/`.mega` | **0.20** | −14 | **exactly 1** |
| 7 | **CTA** | `whoosh-cinematic.mp3` (5.54 s) | `.cta` block, swell peaks on landing | `rise` | **0.13** | −18 | 1 |

Sizes and durations are from `manifest.json` (`~/.claude/skills/media-use/audio/assets/sfx/`);
`impact-bass-1` and `impact-bass-2` are the media-use equivalents of `studio/library/sfx/boom.wav`
— either works, use whichever is already in the project.

`data-volume` is **linear gain**, so: 0.22 = −13 dB, 0.20 = −14 dB, 0.16 = −16 dB,
0.14 = −17 dB, 0.13 = −18 dB, 0.10 = −20 dB, 0.09 = −21 dB. These sit **under the VO** and
**above the bed** — which is the correct order for a voice-led format. Note the `media-use`
skill's blanket default is `volume: 0.35` (−9 dB); that is far too hot for this format and
should be overridden per cue.

Cue #6 pairs with the planned bed-drop in §3.2 — bed to silence 1.2 s before, impact on the
reveal, bed back over 0.8 s. That combination is the video's one real moment.

**Budget: ≤10 cues per video, ~1 per scene.** Reuse `format.json`'s existing
`layout.cue_min_gap_seconds: 0.8` as the minimum spacing between two SFX. The gate is the
same one the visuals already obey.

### 4.3 Where SFX would cheapen it — say it explicitly

- **No `tick` per kinetic word.** §5 of the production skill says `tick` fires per kinetic
  word, cap ~8/scene. That is the TechToolTester bright-SaaS pattern. The finance
  blockframe has **no word-by-word kinetic type**, and a tick bed over full-bleed graded
  photography reads as cheap motion-graphics template. Do not port it.
- **No `sparkle`, `chime`, `notification`, `typing`, `glitch-*`, `error`.** All read as
  UI/SaaS/app. The design doc's rule is "Nothing decorative, nothing cute" — these are both.
- **No sound on `ken`, `drift`, `breathe`, `pulse`, `fade`.** These are continuous or
  ambient. Sounding a `breathe` (a 1.5 s yoyo that repeats all scene) is how a video ends
  up sounding like a slot machine.
- **No `riser`.** 10.03 s of build inside a 3-minute nine-scene explainer is a trailer
  move; it swamps both the bed and the voice.
- **Never two SFX in one scene** unless one is #5 or #6 (which happen once each in the
  whole video).
- **Nothing under the last 3 s** except the single CTA cue. The end card should feel
  settled, not busy.
- **Never an SFX during the planned silence** (§3.2). That would defeat the only silence
  that is doing work.

The governing principle: this format's motion is *heavy and deliberate* — a stamp, a bill,
a bar. Sound should confirm weight, not add sparkle. If a cue makes the frame feel *faster*,
it is the wrong cue.

---

## 5. THE VOICE

### 5.1 Model — keep `eleven_multilingual_v2` (and this contradicts the vault)

`FACT` ElevenLabs' current model line-up (2026): `eleven_v3` (70+ languages, inline audio
tags, GA since Feb 2026), `eleven_multilingual_v2` (29 languages, 10,000 chars),
`eleven_flash_v2_5` (~75 ms, real-time), plus voice-design and STS models.
`eleven_multilingual_v2` is **not deprecated** and ElevenLabs' own docs still describe it
as *"ideal for professional content, audiobooks & video narration"*, the pick when
"consistent, predictable neutral narration is the priority."

⚠️ **Contradiction with the vault:** `vault/workflows/voiceover-tts.md` line 120 states
**"Default model = `eleven_v3`"** with `eleven_multilingual_v2` as "the fallback if a v3
take is inconsistent". `tools/format.json` runs the finance channels on the *fallback*.

**format.json is right; the note is stale for this lane.** v3's advantages (audio tags,
emotional range) are documentary-narration advantages, and it comes with real costs the
finance format cannot absorb: **more take-to-take variability** and **no request stitching**
(`previous_text`/`next_text` return `unsupported_model`, per the vault's own testing). A
9-line factual read that must pair-match across two channels wants consistency, not drama.

**The risk is that the note gets applied.** Someone reads `voiceover-tts.md`, sees
`format.json` on the "fallback", and "fixes" it — burning ElevenLabs credits to make the
read *less* consistent. The workflow note needs a line scoping v3 to the long-form
history lane.

### 5.2 Settings — is the delivery flat? Structurally, yes

`FACT` Current: `stability 0.5` / `similarity 0.75` (hardcoded in `batch.py`) /
**`style 0.0`** / `speed 1.0` (never passed) / **no seed**, identical for all 9 lines and
both voices.

`FACT` `style: 0.0` is the **minimum** the API accepts — the flattest available read.
The vault's own won baseline, from a creator A/B test, is **stability 0.40 / similarity
0.80 / style 0.50 / speed 0.95** (`voiceover-tts.md:107`). The finance pipeline runs
*below* the floor of that tested range on style and *above* it on stability.

`UNVALIDATED` — no analytics, and I cannot hear the output. But "the flattest setting the
API offers, applied uniformly to every line" is a default, not a decision, and there is no
record of anyone testing it for this format.

Proposed starting point (both cuts), to be A/B'd on **one line**, not a batch:

| Param | Now | Proposed | Why |
|---|---|---|---|
| `stability` | 0.5 | **0.45** | slightly more variation; still steady enough for facts |
| `similarity_boost` | 0.75 | **0.80** | vault's tested range is 0.75–0.85; 1.0 over-enunciates |
| `style` | **0.0** | **0.30** | some emphasis. **Not 0.50** — that is documentary-dramatic; this is factual. Reported phonetic distortion above ~0.60 |
| `speed` | 1.0 (implicit) | **0.97** (hi) / 1.0 (en) | slightly weightier on the Hindi read |
| `seed` | **none** | **fixed int** | reproducibility — see below |

All five belong in `format.json`'s `tts` block, **not hardcoded in `batch.py`**, per
`vault/CLAUDE.md`'s one-home rule. Two of them are currently in the wrong home.

**Fix the seed regardless of the rest.** It costs nothing, changes no sound, and closes a
real determinism hole: today a `--force` re-roll of one line produces a different read from
its neighbours, in a pipeline that verifies everything else to 0.02 s.

### 5.3 Do the hero-number lines deserve different settings?

`UNVALIDATED`, and I would **not** start there. Per-line settings mean the nine clips no
longer share a voice character, which is exactly the drift the single-timeline format is
built to avoid — and `eleven_multilingual_v2` has no audio-tag escape hatch to recover it.

There is a **cheaper lever with zero API cost**: punctuation. The vault already documents
that em-dash `—` and ellipsis `...` become natural pauses that transliterate through
(`voiceover-tts.md:112`). Writing a hero number as

> `Nine thousand, five hundred and six — dollars.`

reads differently from a flat sentence, on the existing settings, for free. That belongs to
`fin-script`, and it is one style rule, not a code change.

If per-line settings are eventually wanted, the right shape is a **zone map** (the vault
already has the pattern — `voiceover-tts.md`'s six-zone table with most-specific-wins), not
nine hand-tuned rows.

### 5.4 v3 audio tags

`FACT` Available; v3 supports inline `[dramatic tone]`, `[pause]`, `[somber]` etc., and the
vault confirmed they steer correctly on Devanagari. `FACT` v3 has no request stitching and
higher take-to-take variance.

`UNVALIDATED` verdict: **not worth switching for a 9-line factual explainer.** The whole
value of tags is beat-level emotional shaping across a long narrative; there are nine
beats here and they are all "state a fact". Revisit only if the channel ever ships a
long-form finance cut on the `per-line-chapters` tier.

### 5.5 Hindi at 12.5 chars/sec — and a real error on the en side

`FACT` I measured actual delivery rate across all nine lines of both `credit-history` cuts
(chars in `<id>.txt` ÷ measured mp3 duration from `timing.json`):

| Cut | `format.json` `chars_per_second` | **Measured** | Error |
|---|---|---|---|
| hi (Harsh, Devanagari) | 12.5 | **12.62** | +1.0 % ✅ |
| en (Brian, English) | 15.0 | **16.11** | **+7.4 %** ❌ |

Per-line hi: 11.74–13.58. Per-line en: 15.05–17.53.

- **hi's 12.5 is correct.** It also lines up with the independently measured 12.0–12.2 for
  Nastaliq masters across Pompeii and Firaun. Nothing to change.
- **en's 15.0 is wrong by 7.4 %.** Brian delivers 16.11 chars/sec. Consequence: an en
  script written to the 15.0 budget comes in at ~93 % of its target runtime, and the
  `fin-voice` cost guard (1.3× budget) is 7 % slacker than intended on every en run.
  **One-number fix in `tools/format.json`: `cuts.en.chars_per_second: 15.0 → 16.1`.**

### 5.6 The silences — yes, there is audible dead air

Fully quantified in §3.1: ~**1.78 s** of true silence between every pair of spoken lines,
~**16 s** total, **9 % of the runtime**, in a video with no bed under it.

Two independent fixes, and they are better together:

1. **A bed** (§3) turns those gaps from "the file stopped" into "the video is breathing".
   This is the fix that matters.
2. **Trim the tail: `format.json` `scene.tail_seconds: 1.0 → 0.6`.** The clip already
   carries ~0.37 s of its own trailing silence, so 1.0 is effectively 1.38 s. Setting 0.6
   makes it ~0.98 s — still a beat, but a deliberate one. Saves 8 × 0.4 = **3.2 s per cut**
   of dead time in a 3-minute video.

   Watch: `tail_seconds` is read by `batch.py` (scene arithmetic) and `pipeline_check.py`
   (the `audio_start ≠ scene_start + lead` assertion), so it is genuinely a one-number
   change — but it shortens total runtime by ~3.2 s, which shifts the target-seconds
   budget. Change it once, on a fresh pair, not retroactively.

Do **not** touch `lead_in_seconds: 0.4`. It is what stops a scene's first cue from firing
before the frame is established (`layout.first_cue_by_seconds: 0.5` depends on it).

---

## 6. IMPLEMENTATION — how this survives a deterministic render

### 6.1 What the framework guarantees

`FACT` from `~/.claude/skills/hyperframes-core/references/`:

- **`<audio>` must be a DIRECT child of the host composition root.** Not inside a
  sub-composition `<template>`, not inside any wrapper `<div>`. Media in a wrapper is never
  registered, seeked, or decoded. The finance compositions are single-file with root-level
  audio already, so this is satisfied for free.
- **`data-track-index` is temporal, not visual.** Two clips on the same track must not
  overlap in time; `hyperframes lint` flags it. There is **no fixed band convention** —
  "higher tracks (e.g. 10+) for audio" is the only guidance. (The `vault/skills`
  band scheme "visuals 0–9 · overlays 10–19 · VO/music 20–29 · SFX 30+" is a **local
  convention, not a framework rule**, and the finance compositions already ignore it — VO
  sits on 10. Stay self-consistent with what is there rather than renumbering.)
- **`data-volume`** is a static linear gain, 0–1, default 1.
- **For fades and ducking, animate `volume` on the GSAP timeline** —
  `tl.to("#bgm", { volume: 0, duration: 1 })`. The doc is explicit: *"The runtime probes
  the timeline's volume keyframes and applies them identically in preview and render;
  `data-volume` is the static baseline for elements no tween touches."* **This is the whole
  ballgame** — ducking is deterministic and preview-accurate by design. No post-render mix
  pass, no sidechain, no `assemble.py`.
  - Corollary: because `data-volume` only applies to elements *no tween touches*, set
    `#bgm`'s initial value with `tl.set("#bgm", { volume: 0 }, 0)`, not with
    `data-volume`, once you are tweening it.
- **`data-media-start`** offsets into the source file — use it to start a bed 8 s in
  (past a track's own intro) without cutting the file.
- **`data-duration`** may be omitted on `<audio>` to take the media's intrinsic length —
  but **set it explicitly** here, since the timing contract wants all four copies of every
  number to agree.

`FACT` The finance compositions already register **one paused root timeline**
(`window.__timelines`, `var tl = gsap.timeline({ paused: true })`) with all nine helpers on
it and a `var S = {...}` scene-start map. The bed's duck envelopes and every SFX go on that
same timeline. No new architecture.

### 6.2 The concrete diff

**Composition (`index.html`), generated — never hand-edited:**

```html
<!-- root-level, after the VO rows -->
<audio id="bgm" src="assets/bgm/bed-<name>.mp3"
       data-start="0" data-duration="177.642" data-track-index="11"></audio>

<audio id="sfx1" src="assets/sfx/pop.mp3"
       data-start="19.4" data-duration="0.72"
       data-track-index="12" data-volume="0.10"></audio>
<!-- … up to 10 cues, round-robin tracks 12/13/14 IN TIME ORDER … -->
```

- **BGM → track 11** (one clip, never overlaps).
- **SFX → tracks 12/13/14**, round-robin. `impact-bass-2` is 2.59 s and
  `whoosh-cinematic` is 5.54 s, so overlaps are real. **Rotate in time order, not index
  order** — §1 of the production skill already logged that index rotation collides when
  stagger groups interleave.
- `data-duration` on an SFX row must be **≥** the file length or the tail is cut.

**`tools/format.json`** gains one small block (all the numbers above live in one home):

```jsonc
"audio": {
  "bed_import_lufs": -20,
  "bed_volume_open": 0.16,
  "bed_volume_duck": 0.08,
  "bed_fade_in_s": 1.5,
  "bed_fade_out_s": 2.5,
  "sfx_max_per_video": 10,
  "publish_lufs": -14,
  "publish_tp_dbtp": -1.5
}
```

### 6.3 Cost, by owner

| Change | Owner | Cost |
|---|---|---|
| **Loudness pass** | orchestrator (`.claude/commands/finance-video.md`, after the encode at L112) | **~1 hour once.** ~20 s CPU per cut thereafter. `fin-render`'s allowlist says "ffmpeg (analysis filters only)" so it cannot do this itself |
| Bed `<audio>` row + 9 duck envelopes | `fin-build` | ~30 lines in the generator, all derived from `timing.json` |
| Pick the bed + mood | `fin-storyboard` (new `music:` field) | 1 line per video |
| SFX cue selection | `fin-storyboard` — the `STORYBOARD.md` convention **already has an `SFX` field** per §2 of the production skill; finance simply leaves it empty | 1 column, ~9 rows |
| SFX `<audio>` rows | `fin-build` — already computes every helper's `at` time, which *is* the SFX `data-start` | ~20 lines |
| Bed asset prep | one-off: creator downloads 5–6 from YT Audio Library → `studio/library/music/`, normalise to −20 LUFS | ~15 min, once, ever |
| Zero-overlap + bed-check QA | `fin-render` (analysis-only ffmpeg — already allowed) | ~10 lines |
| Voice settings → `format.json`; fixed seed | `tools/tts/batch.py` + `format.json` | trivial; removes a hardcode that violates the one-home rule |
| `cuts.en.chars_per_second: 15.0 → 16.1` | `tools/format.json` | one number |
| `scene.tail_seconds: 1.0 → 0.6` | `tools/format.json` | one number, next fresh pair only |

**Order of work:** loudness first (it is independent of everything else and ships value on
the already-built `credit-history` pair today), then the bed, then SFX. The bed is what
makes the SFX sit properly — SFX over silence sound like a fault; SFX over a bed sound like
production.

### 6.4 On the `media-use` skill

Available and relevant, with two caveats already noted: (a) its **BGM offline fallback is
MusicGen, CC-BY-NC, non-commercial — a licence landmine for monetised channels**; (b) its
default SFX volume of 0.35 (−9 dB) is far too hot for this format. The genuinely useful
part is its **bundled 20-file Pixabay SFX library with an explicit commercial-use, no-
attribution `CREDITS.md`** — take the files, ignore the engine. The finance pipeline does
not need `scripts/audio.mjs`; it already has its own TTS path and a generator that knows
every cue time.

---

## 7. Contradictions with what the vault currently documents

1. **`vault/knowledge/design-finance-blockframe.md:163` — "No SFX. The finance format is
   voice + motion only."** Presented as a design decision. There is no record of it being
   *tested*; it reads as the TechToolTester audio layer being dropped when the design doc
   was forked, not as a considered choice. It also silently covers music, which it never
   mentions. Recommend restating it as "no decorative SFX; one disciplined kit + one bed".
2. **`vault/workflows/voiceover-tts.md:120` — "Default model = `eleven_v3`."** The finance
   channels run `eleven_multilingual_v2`, which that note calls the *fallback*. For this
   format the "fallback" is the correct choice (consistency > expressiveness on a 9-line
   paired read). The note needs a lane scope or someone will "fix" `format.json` and spend
   credits making the read worse.
3. **`vault/skills/hyperframes_production.md:43` — the track-band convention "VO/music
   20–29 · SFX 30+"** is presented as a hard rule ("break one and the render silently
   corrupts"). It is not a framework rule — `hyperframes-core`'s `tracks-and-clips.md` says
   plainly *"There's no fixed convention"* and that tracks are temporal, not visual. The
   finance compositions already put VO on track 10 and render fine. The real rule is only
   "no two clips overlapping on one track".
4. **`vault/skills/hyperframes_production.md:106` — the broadcast VO chain targets
   −16 LUFS.** That was for creator-recorded audio. For YouTube the target is −14 LUFS;
   −16 leaves 2 LU on the table for no benefit (and the rest of that chain — HPF, denoise,
   de-ess — is a *microphone* chain that ElevenLabs output does not need).
5. **`tools/format.json` `cuts.en.chars_per_second: 15.0` is measurably wrong** (actual
   16.11, +7.4 %). hi's 12.5 is right (12.62).
6. **`vault/videos/credit-history/index.md:112` records the loudness lift as "owed"** and
   `fin-render`'s logs call it "optional". Given YouTube applies no positive gain, it is
   not optional — it is a spec miss on every video ever shipped here.
7. **`tools/tts/batch.py` hardcodes `stability=0.5, similarity=0.75`**, which violates
   `vault/CLAUDE.md`'s explicit rule that every fact lives in `format.json` or a vault note.
   Two of the five voice parameters are in the wrong home.

---

## Sources

- YouTube loudness normalisation (no positive gain): [Critical Listening Lab](https://www.criticallisteninglab.com/en/learn/loudness/youtube) · [APU Software](https://apu.software/youtube-audio-loudness-target/) · [Audio Forge Pro](https://audioforgepro.com/blog/youtube-lufs-normalization-guide)
- YouTube Audio Library licence (monetisation + no Content ID claim): [YouTube Help — Use music and sound effects from the Audio Library](https://support.google.com/youtube/answer/3376882?hl=en)
- Uppbeat plans, safelist and channel counts: [Uppbeat pricing](https://uppbeat.io/pricing) · [Uppbeat Claim Release](https://uppbeat.io/help-center/claim-release) · [Uppbeat YouTube Claim FAQs](https://uppbeat.io/help-center/youtube-claims-faqs)
- Epidemic Sound plans and per-platform channel limits: [Epidemic Sound Pro plan help](https://support.epidemicsound.com/s/article/what-is-the-commercial-plan?language=en_US) · [How to monetize your soundtracked content](https://www.epidemicsound.com/how-it-works/how-to-monetize-your-content/)
- Artlist channel limits: [Artlist subscription plans 2026](https://www.cchound.com/artlist/artlist-subscription-plans-and-pricing/)
- Pixabay Content License + Content ID certificate: [Pixabay Content License](https://pixabay.com/service/license-summary/) · [How to clear a YouTube Content ID claim with a Pixabay License Certificate](https://pixabay.com/blog/posts/how-to-clear-a-youtube-content-id-claim-with-a-pix-190/)
- Suno commercial rights on paid plans: [Terms.Law — Suno commercial rights 2026](https://terms.law/ai-output-rights/suno/) · [Dynamoi — Suno commercial rights explained](https://dynamoi.com/learn/ai-music-distribution/suno-commercial-rights-explained)
- MusicGen weights CC-BY-NC 4.0: [facebook/musicgen-small model card](https://huggingface.co/facebook/musicgen-small)
- Lyria / Gemini output commercial use: [Terms.Law — Gemini output rights](https://terms.law/ai-output-rights/gemini/) · [Lyria RealTime docs](https://ai.google.dev/gemini-api/docs/realtime-music-generation)
- ElevenLabs model line-up 2026: [ElevenLabs — Models](https://elevenlabs.io/docs/overview/models)
- Local, measured: `studio/videos/credit-history-{hi,en}/` VO mp3s + `renders/FINAL-1080p-*.mp4`; skill files under `~/.claude/skills/{hyperframes-core,media-use}/`.
