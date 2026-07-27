// Background service worker.
//  - Trusted mouse input via chrome.debugger (Flow rejects synthetic clicks).
//  - Renames each downloaded image to the shot id via chrome.downloads.
const attached = new Set();

const attach = (tabId) =>
  new Promise((res, rej) =>
    chrome.debugger.attach({ tabId }, "1.3", () => (chrome.runtime.lastError ? rej(new Error(chrome.runtime.lastError.message)) : res()))
  );
const detach = (tabId) => new Promise((res) => chrome.debugger.detach({ tabId }, () => (chrome.runtime.lastError, res())));
const cmd = (tabId, method, params) =>
  new Promise((res, rej) =>
    chrome.debugger.sendCommand({ tabId }, method, params, (r) => (chrome.runtime.lastError ? rej(new Error(chrome.runtime.lastError.message)) : res(r)))
  );

async function ensureAttached(tabId) {
  if (attached.has(tabId)) return;
  await attach(tabId);
  attached.add(tabId);
}

// type: "click" (left) | "rightclick" | "move" (hover only)
async function mouse(tabId, type, x, y) {
  await ensureAttached(tabId);
  await cmd(tabId, "Input.dispatchMouseEvent", { type: "mouseMoved", x, y });
  if (type === "move") return;
  const button = type === "rightclick" ? "right" : "left";
  await cmd(tabId, "Input.dispatchMouseEvent", { type: "mousePressed", x, y, button, buttons: type === "rightclick" ? 2 : 1, clickCount: 1 });
  await cmd(tabId, "Input.dispatchMouseEvent", { type: "mouseReleased", x, y, button, buttons: 0, clickCount: 1 });
}

// --- download renaming: content queues an intended name just before triggering it
const pendingNames = [];
let lastTab = null;
const dlTab = {};

chrome.downloads.onDeterminingFilename.addListener((item, suggest) => {
  if (pendingNames.length) {
    const filename = pendingNames.shift();
    if (lastTab != null) dlTab[item.id] = lastTab;
    suggest({ filename, conflictAction: "uniquify" });
  } else {
    suggest();
  }
});
chrome.downloads.onChanged.addListener((d) => {
  if (d.state && d.state.current === "complete" && dlTab[d.id] != null) {
    const t = dlTab[d.id];
    delete dlTab[d.id];
    chrome.tabs.sendMessage(t, { evt: "downloaded", id: d.id }, () => chrome.runtime.lastError);
  }
});

chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
  const tabId = sender.tab && sender.tab.id;
  if (!tabId) {
    sendResponse({ ok: false, error: "no tab" });
    return;
  }
  (async () => {
    try {
      if (msg.cmd === "mouse") {
        await mouse(tabId, msg.type, msg.x, msg.y);
        sendResponse({ ok: true });
      } else if (msg.cmd === "expectDownload") {
        pendingNames.push(msg.name);
        lastTab = tabId;
        sendResponse({ ok: true });
      } else if (msg.cmd === "detach") {
        if (attached.has(tabId)) {
          attached.delete(tabId);
          await detach(tabId);
        }
        sendResponse({ ok: true });
      } else {
        sendResponse({ ok: false, error: "unknown cmd" });
      }
    } catch (e) {
      sendResponse({ ok: false, error: String((e && e.message) || e) });
    }
  })();
  return true; // async
});

chrome.tabs.onRemoved.addListener((tabId) => attached.delete(tabId));
chrome.debugger.onDetach.addListener((src) => src.tabId && attached.delete(src.tabId));
