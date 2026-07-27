// Prompt Runner — sends prompts one-by-one, waits for each image, downloads it in 2K, repeats.
// Isolated world (needs chrome.runtime). Verified on Google Flow:
//   insert  = InputEvent("beforeinput",{inputType:"insertText",data})   (Slate registers it)
//   submit  = trusted click via chrome.debugger (Flow rejects synthetic clicks)
//   download= right-click latest image -> hover "Download" -> click "2K" (trusted, via debugger),
//             then chrome.downloads renames the file to pompeii-<shotId>.jpg
(() => {
  if (window.__promptRunnerLoaded) return;
  window.__promptRunnerLoaded = true;

  const LS = "promptRunner.v1";
  const saved = JSON.parse(localStorage.getItem(LS) || "{}");

  const panel = document.createElement("div");
  panel.id = "pr-panel";
  panel.innerHTML = `
    <div class="pr-head" id="pr-drag"><span>▶ Prompt Runner</span><span class="pr-toggle" title="collapse">–</span></div>
    <div class="pr-body">
      <textarea id="pr-prompts" placeholder="Paste prompts here — separate each one with a line containing only ---"></textarea>
      <div class="pr-wait">
        <label>Wait between prompts</label>
        <div class="pr-wait-in"><input id="pr-min" type="number" value="4" min="0"><span>to</span><input id="pr-max" type="number" value="8" min="0"><span>sec</span></div>
      </div>
      <label class="pr-check"><input type="checkbox" id="pr-dl" checked> Auto-download each image in 2K</label>
      <div class="pr-progress"><div id="pr-bar"></div></div>
      <div class="pr-row"><button id="pr-start">▶ Start</button><button id="pr-stop" disabled>■ Stop</button></div>
      <details><summary>advanced</summary>
        <input id="pr-prefix" placeholder="filename prefix (pompeii-)">
        <input id="pr-inputSel" placeholder="input CSS selector (blank = auto)">
        <input id="pr-sendSel" placeholder="send-button CSS selector (blank = auto)">
      </details>
      <div id="pr-status">idle</div>
    </div>`;
  document.documentElement.appendChild(panel);

  const style = document.createElement("style");
  style.textContent = `
    #pr-panel{position:fixed;top:16px;right:16px;width:300px;z-index:2147483647;
      font:13px/1.45 system-ui,-apple-system,sans-serif;color:#e8eaed;background:#1c1f26;
      border:1px solid #363b45;border-radius:12px;box-shadow:0 12px 40px rgba(0,0,0,.55);overflow:hidden}
    #pr-panel .pr-head{background:linear-gradient(#232833,#1a1d24);padding:9px 12px;font-weight:600;
      cursor:grab;display:flex;justify-content:space-between;align-items:center;user-select:none;border-bottom:1px solid #2c313b}
    #pr-panel .pr-head:active{cursor:grabbing}
    #pr-panel .pr-toggle{cursor:pointer;padding:0 6px;border-radius:6px;color:#9aa4b2}
    #pr-panel .pr-toggle:hover{background:#2c313b;color:#fff}
    #pr-panel.pr-collapsed .pr-body{display:none}
    #pr-panel .pr-body{padding:12px;display:flex;flex-direction:column;gap:10px}
    #pr-panel textarea{width:100%;height:150px;resize:vertical;background:#12151b;color:#e8eaed;
      border:1px solid #363b45;border-radius:8px;padding:9px;box-sizing:border-box;font:12px/1.5 ui-monospace,monospace}
    #pr-panel textarea:focus,#pr-panel input:focus{outline:none;border-color:#3b82f6}
    #pr-panel .pr-wait{display:flex;flex-direction:column;gap:5px}
    #pr-panel .pr-wait label{color:#9aa4b2;font-size:12px}
    #pr-panel .pr-wait-in{display:flex;align-items:center;gap:7px;color:#c7cdd6}
    #pr-panel .pr-wait-in input{width:56px;background:#12151b;color:#e8eaed;border:1px solid #363b45;
      border-radius:7px;padding:6px 8px;box-sizing:border-box;font-size:13px;text-align:center}
    #pr-panel .pr-check{display:flex;align-items:center;gap:7px;color:#c7cdd6;font-size:12px;cursor:pointer}
    #pr-panel .pr-check input{width:15px;height:15px;accent-color:#22c55e}
    #pr-panel .pr-progress{height:6px;background:#12151b;border-radius:99px;overflow:hidden}
    #pr-panel #pr-bar{height:100%;width:0;background:linear-gradient(90deg,#3b82f6,#22c55e);border-radius:99px;transition:width .3s ease}
    #pr-panel .pr-row{display:flex;gap:8px}
    #pr-panel .pr-row button{flex:1;padding:9px;border:0;border-radius:8px;font-weight:700;font-size:13px;cursor:pointer;transition:filter .15s}
    #pr-panel .pr-row button:hover:not(:disabled){filter:brightness(1.12)}
    #pr-panel #pr-start{background:#22c55e;color:#08210f}
    #pr-panel #pr-stop{background:#ef4444;color:#fff}
    #pr-panel button:disabled{background:#2c313b!important;color:#6b7280!important;cursor:default}
    #pr-panel details{color:#9aa4b2;font-size:12px}
    #pr-panel details input{width:100%;background:#12151b;color:#e8eaed;border:1px solid #363b45;border-radius:7px;padding:6px;box-sizing:border-box;margin-top:6px}
    #pr-panel #pr-status{font-size:12px;color:#9aa4b2;min-height:16px;word-break:break-word}
    #pr-panel *{box-sizing:border-box}`;
  document.documentElement.appendChild(style);

  const $ = (s) => panel.querySelector(s);
  ["prompts", "min", "max", "prefix", "inputSel", "sendSel"].forEach((k) => { if (saved[k] != null) $("#pr-" + k).value = saved[k]; });
  if (saved.dl != null) $("#pr-dl").checked = saved.dl;
  if (saved.left != null) { panel.style.left = saved.left + "px"; panel.style.top = saved.top + "px"; panel.style.right = "auto"; }

  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const visible = (el) => el && el.getClientRects().length > 0 && el.offsetParent !== null;
  const status = (t) => ($("#pr-status").textContent = t);
  const btnEnabled = (b) => b && !b.disabled && b.getAttribute("aria-disabled") !== "true";
  const setBar = (frac) => ($("#pr-bar").style.width = Math.round(frac * 100) + "%");
  const center = (el) => { const r = el.getBoundingClientRect(); return { x: Math.round(r.left + r.width / 2), y: Math.round(r.top + r.height / 2) }; };
  async function pollFor(fn, tries = 40, gap = 100) { for (let i = 0; i < tries; i++) { const v = fn(); if (v) return v; await sleep(gap); } return null; }

  const contextOk = () => { try { return !!chrome.runtime && !!chrome.runtime.id; } catch (e) { return false; } };
  const sendBg = (msg) =>
    new Promise((res) => {
      if (!contextOk()) return res({ ok: false, error: "refresh this tab (F5) — extension was updated" });
      try { chrome.runtime.sendMessage(msg, (r) => res(chrome.runtime.lastError ? { ok: false, error: chrome.runtime.lastError.message } : r)); }
      catch (e) { res({ ok: false, error: /invalidated/i.test(String(e)) ? "refresh this tab (F5) — extension was updated" : String(e) }); }
    });

  // ---- composer / send button / busy ---------------------------------------
  function findInput() {
    const sel = $("#pr-inputSel").value.trim();
    if (sel) return document.querySelector(sel);
    return (
      document.querySelector('div[data-slate-editor="true"][role="textbox"]') ||
      document.querySelector('[data-slate-editor="true"]') ||
      document.querySelector('[role="textbox"][contenteditable="true"]') ||
      [...document.querySelectorAll('div[contenteditable="true"], textarea')].filter(visible).pop() || null
    );
  }
  const SEND_GLYPHS = ["arrow_forward", "send", "arrow_upward", "play_arrow"];
  function findSend() {
    const sel = $("#pr-sendSel").value.trim();
    if (sel) return document.querySelector(sel);
    const byGlyph = [...document.querySelectorAll("button")].find((b) => {
      const i = b.querySelector('i.google-symbols, i.material-symbols-outlined, i[class*="symbols"]');
      return i && SEND_GLYPHS.includes(i.textContent.trim());
    });
    if (byGlyph) return byGlyph;
    return [...document.querySelectorAll("button,[role=button]")].find((b) => {
      const t = ((b.getAttribute("aria-label") || "") + " " + b.textContent).toLowerCase();
      return /\b(send|run|generate|submit)\b/.test(t);
    }) || null;
  }
  const isBusy = () =>
    [...document.querySelectorAll("button")].some((b) => {
      const i = b.querySelector('i.google-symbols, i.material-symbols-outlined, i[class*="symbols"]');
      return i && i.textContent.trim() === "stop";
    });

  // ---- Slate insert --------------------------------------------------------
  function placeCaretEnd(el) {
    el.focus();
    const leaves = el.querySelectorAll('[data-slate-node="text"]');
    const target = leaves[leaves.length - 1] || el.querySelector("[data-slate-node]") || el;
    const sel = window.getSelection();
    const r = document.createRange();
    r.selectNodeContents(target);
    r.collapse(false);
    sel.removeAllRanges();
    sel.addRange(r);
  }
  function editorText(el) {
    const ph = el.querySelector("[data-slate-placeholder]");
    return el.textContent.replace(/[﻿​]/g, "").replace(ph ? ph.textContent : "", "").trim();
  }
  const composerEmpty = (el) =>
    ["textarea", "input"].includes(el.tagName.toLowerCase()) ? el.value.trim() === "" : editorText(el) === "";
  async function clearEditor(el) {
    for (let i = 0; i < 200 && editorText(el) !== ""; i++) {
      placeCaretEnd(el);
      el.dispatchEvent(new InputEvent("beforeinput", { inputType: "deleteContentBackward", bubbles: true, cancelable: true }));
      await sleep(8);
    }
  }
  async function setText(el, text) {
    el.focus();
    const tag = el.tagName.toLowerCase();
    if (tag === "textarea" || tag === "input") {
      const setter = Object.getOwnPropertyDescriptor(tag === "textarea" ? HTMLTextAreaElement.prototype : HTMLInputElement.prototype, "value").set;
      setter.call(el, ""); el.dispatchEvent(new Event("input", { bubbles: true }));
      setter.call(el, text); el.dispatchEvent(new Event("input", { bubbles: true }));
      return;
    }
    await clearEditor(el);
    for (let a = 0; a < 2; a++) {
      placeCaretEnd(el);
      el.dispatchEvent(new InputEvent("beforeinput", { inputType: "insertText", data: text, bubbles: true, cancelable: true }));
      await sleep(80);
      if (editorText(el) !== "") break;
    }
  }
  async function submit() {
    let btn = null;
    for (let i = 0; i < 40; i++) { btn = findSend(); if (btnEnabled(btn)) break; await sleep(200); }
    if (!btnEnabled(btn)) return "⚠ Send didn't enable";
    const c = center(btn);
    const r = await sendBg({ cmd: "mouse", type: "click", x: c.x, y: c.y });
    return r && r.ok ? "trusted click" : "⚠ click failed: " + ((r && r.error) || "no background");
  }

  // ---- download the latest image in 2K -------------------------------------
  function latestImage() {
    const imgs = document.querySelectorAll('img[alt="Generated image"]');
    return imgs[0] || null; // grid is newest-first
  }
  function waitForDownload(timeout = 25000) {
    return new Promise((res) => {
      let done = false;
      const h = (msg) => { if (!done && msg && msg.evt === "downloaded") { done = true; chrome.runtime.onMessage.removeListener(h); res(true); } };
      chrome.runtime.onMessage.addListener(h);
      setTimeout(() => { if (!done) { done = true; chrome.runtime.onMessage.removeListener(h); res(false); } }, timeout);
    });
  }
  async function downloadLatest2K(shotId) {
    const img = latestImage();
    if (!img) return "no image";
    img.scrollIntoView({ block: "center" });
    await sleep(350);
    const prefix = $("#pr-prefix").value.trim() || "pompeii-";
    await sendBg({ cmd: "expectDownload", name: `${prefix}${shotId}.jpg` });
    const dl = waitForDownload();
    // 1) right-click the image
    const ic = center(img);
    await sendBg({ cmd: "mouse", type: "rightclick", x: ic.x, y: ic.y });
    // 2) find the "Download" submenu trigger
    const find2K = () => [...document.querySelectorAll('[role="menuitem"]')].find((m) => /2\s*k/i.test(m.textContent) && !/upgrade|original|1\s*k|4\s*k/i.test(m.textContent));
    const dItem = await pollFor(() =>
      [...document.querySelectorAll('[role="menuitem"]')].find((m) => m.getAttribute("aria-haspopup") === "menu" || /download/i.test(m.textContent))
    );
    if (!dItem) return "no Download item";
    const dc = center(dItem);
    // reveal the submenu: hover first; if hover-intent doesn't open it, CLICK the trigger.
    await sendBg({ cmd: "mouse", type: "move", x: dc.x, y: dc.y });
    let twoK = await pollFor(find2K, 15, 100);
    if (!twoK) {
      await sendBg({ cmd: "mouse", type: "click", x: dc.x, y: dc.y });
      twoK = await pollFor(find2K, 25, 120);
    }
    if (!twoK) return "no 2K item";
    // 3) let the submenu settle (it animates in → coords drift), re-read, hover, click
    await sleep(400);
    const kc = center(find2K() || twoK);
    await sendBg({ cmd: "mouse", type: "move", x: kc.x, y: kc.y });
    await sleep(120);
    await sendBg({ cmd: "mouse", type: "click", x: kc.x, y: kc.y });
    // 4) wait for the file to land
    const ok = await dl;
    return ok ? "saved" : "download timeout";
  }

  const parsePrompts = (raw) => raw.split(/\n\s*-{3,}\s*\n/).map((s) => s.trim()).filter(Boolean);
  const shotIdOf = (p) => { const m = p.match(/\b(?:shot|scene)\s+([0-9]+[a-z]?)/i); return m ? m[1].toUpperCase() : null; };

  let running = false;

  async function waitIdle() {
    let s = 0;
    while (running && isBusy() && s < 300) { status(`⏳ waiting for queue free… (${++s}s)`); await sleep(1000); }
  }
  async function waitGenDone() {
    for (let i = 0; i < 6 && running && !isBusy(); i++) await sleep(1000); // let generation start
    await waitIdle(); // then wait until it finishes
  }

  async function run() {
    if (!contextOk()) return status("⚠ Extension was updated — press F5 to refresh this tab, then Start.");
    const prompts = parsePrompts($("#pr-prompts").value);
    if (!prompts.length) return status("no prompts — separate each with --- on its own line");
    const min = +$("#pr-min").value || 0;
    const max = Math.max(+$("#pr-max").value || 0, min);
    const autoDl = $("#pr-dl").checked;
    running = true;
    $("#pr-start").disabled = true; $("#pr-stop").disabled = false;
    setBar(0);
    let ok = 0, fail = 0, stopped = "";
    for (let i = 0; i < prompts.length && running; i++) {
      await waitIdle();
      if (!running) break;
      const input = findInput();
      if (!input) { stopped = `⚠ chat box not found — open a chat / set a selector. Stopped at #${i + 1}`; break; }
      await setText(input, prompts[i]);
      const insertedOk = !composerEmpty(input);
      const how = running ? await submit() : "stopped";
      await sleep(1000);
      const landed = insertedOk && composerEmpty(input) && !how.startsWith("⚠");
      landed ? ok++ : fail++;
      setBar((i + 1) / prompts.length);
      if (i === 0 && !landed) {
        stopped = `⚠ #1 didn't send. insert=${insertedOk} · submit="${how}" · boxCleared=${composerEmpty(input)}`;
        break;
      }
      const shot = shotIdOf(prompts[i]);
      if (autoDl && shot && running) {
        await waitGenDone();
        if (running) {
          status(`⬇ downloading ${shot}…`);
          const dres = await downloadLatest2K(shot);
          status(`${dres === "saved" ? "✓ saved" : "⚠ " + dres} ${shot}`);
          await sleep(800);
        }
      }
      const wait = Math.round(min + Math.random() * (max - min));
      for (let s = wait; s > 0 && running; s--) { status(`✓${ok} ✗${fail} — ${i + 1}/${prompts.length} done, next in ${s}s`); await sleep(1000); }
    }
    running = false;
    $("#pr-start").disabled = false; $("#pr-stop").disabled = true;
    sendBg({ cmd: "detach" });
    status(stopped || `done — ${ok} sent${fail ? `, ${fail} failed` : ""}`);
  }

  const save = () =>
    localStorage.setItem(LS, JSON.stringify({
      prompts: $("#pr-prompts").value, min: $("#pr-min").value, max: $("#pr-max").value,
      dl: $("#pr-dl").checked, prefix: $("#pr-prefix").value,
      inputSel: $("#pr-inputSel").value, sendSel: $("#pr-sendSel").value, left: saved.left, top: saved.top,
    }));

  function checkReady() {
    if (running) return;
    const inp = findInput();
    if (!inp) return status("open a chat page, then paste prompts");
    status(findSend() ? "ready ✓ — paste prompts and Start" : "found box, waiting for send button…");
  }

  (() => {
    const head = $("#pr-drag");
    let down = false, sx, sy, ox, oy;
    head.addEventListener("mousedown", (e) => { if (e.target.classList.contains("pr-toggle")) return; down = true; sx = e.clientX; sy = e.clientY; const r = panel.getBoundingClientRect(); ox = r.left; oy = r.top; e.preventDefault(); });
    window.addEventListener("mousemove", (e) => { if (!down) return; saved.left = Math.max(0, Math.min(innerWidth - 60, ox + e.clientX - sx)); saved.top = Math.max(0, Math.min(innerHeight - 30, oy + e.clientY - sy)); panel.style.left = saved.left + "px"; panel.style.top = saved.top + "px"; panel.style.right = "auto"; });
    window.addEventListener("mouseup", () => { if (down) { down = false; save(); } });
  })();

  $(".pr-toggle").addEventListener("click", (e) => { e.stopPropagation(); panel.classList.toggle("pr-collapsed"); });
  $("#pr-start").addEventListener("click", () => (save(), run()));
  $("#pr-stop").addEventListener("click", () => ((running = false), sendBg({ cmd: "detach" }), status("stopping…")));
  $("#pr-prompts").addEventListener("focus", checkReady);
  panel.addEventListener("input", save);
  setTimeout(checkReady, 800);

  // self-check: parsePrompts("a\n---\nb").length===2 ; shotIdOf("SHOT 05B — x")==="05B"
})();
