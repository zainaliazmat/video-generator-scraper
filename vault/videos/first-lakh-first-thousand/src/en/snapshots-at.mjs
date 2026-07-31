/* Max-density snapshot times: each scene's LAST cue, read back out of the
   emitted index.html so it cannot drift from what actually animates. */
import fs from "node:fs";
const T = JSON.parse(fs.readFileSync("assets/voice/timing.json", "utf8"));
const html = fs.readFileSync("index.html", "utf8");
const at = T.lines.map((t, i) => {
  const m = html.match(new RegExp(`rise\\("#s${i + 1}-focal", ([0-9.]+)`));
  const focal = m ? parseFloat(m[1]) : t.scene_start + 0.7;
  const x = Math.max(t.scene_start + 1.55, focal + 0.45);
  return +Math.min(x, t.scene_start + t.scene_duration - 0.15).toFixed(2);
});
fs.writeFileSync("snapshots-at.txt", at.map((v, i) => `s${i + 1} ${v}`).join("\n") + "\n");
for (let b = 0; b * 12 < at.length; b++)
  console.log("b" + (b + 1) + " " + at.slice(b * 12, b * 12 + 12).join(","));
