// Write ALL timing into index.html from assets/voice/timing.json — the one source.
// The four copies (<section> attrs, JS S/D maps, <audio> rows, root data-duration)
// are rewritten in place; re-runnable. Never hand-edit those numbers.
//
// Scene duration is derived as next_start - start (last: total - start) so scenes
// are exactly contiguous — timing.json's per-scene rounded scene_duration values
// can overlap the next start by 0.001s, which the checker rejects.
import { readFileSync, writeFileSync } from "node:fs";

const t = JSON.parse(readFileSync("assets/voice/timing.json", "utf8"));
let h = readFileSync("index.html", "utf8");
const r3 = (x) => Number(x.toFixed(3));
const S = {}, D = {};

t.lines.forEach((l, i) => {
  const n = i + 1;
  const start = l.scene_start;
  const end = i + 1 < t.lines.length ? t.lines[i + 1].scene_start : t.total;
  const dur = r3(end - start);
  S["s" + n] = start;
  D["s" + n] = dur;
  const sec = new RegExp(`(<section id="s${n}"[^>]*data-start=")[^"]*(" data-duration=")[^"]*(")`);
  const aud = new RegExp(`(<audio id="vo${n}"[^>]*data-start=")[^"]*(" data-duration=")[^"]*(")`);
  if (!sec.test(h) || !aud.test(h)) throw new Error(`scene/audio ${n} not found`);
  h = h.replace(sec, `$1${start}$2${dur}$3`).replace(aud, `$1${l.audio_start}$2${l.duration}$3`);
});

h = h
  .replace(/(data-composition-id="main"[^>]*data-duration=")[^"]*(")/, `$1${t.total}$2`)
  .replace(/var S = \{[^;]*\};/, `var S = ${JSON.stringify(S)};`)
  .replace(/var D = \{[^;]*\};/, `var D = ${JSON.stringify(D)};`);

writeFileSync("index.html", h);
console.log("timing written: total", t.total, "· scenes", t.lines.length);
