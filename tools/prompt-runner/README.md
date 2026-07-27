# Prompt Runner (personal Chrome extension)

Pastes a list of prompts one-by-one into a chat box (Gemini / AI Studio / Google Flow),
sending each and waiting between them. No API key. Keeps everything in **one chat**, so Nano
Banana's character consistency is preserved across a whole storyboard section.

**How it submits:** Flow's send button ignores JavaScript-dispatched clicks (they aren't
"trusted"), so this uses `chrome.debugger` to perform a real trusted click. That's why Chrome
shows a **"Prompt Runner started debugging this browser"** banner while a batch runs — that banner
is the mechanism; leave it up. It clears when the batch finishes or you hit Stop.

**Before running:** close DevTools on the chat tab — Chrome only allows one debugger at a time, so
an open DevTools blocks the trusted click.

## Auto-download (2K)
With **"Auto-download each image in 2K"** ticked, after each image finishes the runner right-clicks
it → **Download → 2K (Upscaled)** and saves the file to your Downloads folder, renamed to
`pompeii-<shotId>.jpg` (the shot id is read from the `SHOT 05B …` label in the prompt). The loop is
**send → wait for image → download 2K → next prompt**.

- Keep the **project grid view open** — it right-clicks the newest `img[alt="Generated image"]`.
- Change the name prefix under **advanced** (default `pompeii-`). Blocks without a `SHOT` label
  (e.g. the SETUP message) are never downloaded.
- Needs the `downloads` permission (reload the extension after updating).

**After ANY extension reload, always F5 the chat tab** — otherwise the page keeps the old content
script and you get "Extension context invalidated".

## Install (one time)
1. Open `chrome://extensions`
2. Turn on **Developer mode** (top-right)
3. Click **Load unpacked** → select this folder (`tools/prompt-runner`)

## Use
1. Open the chat page and start a fresh chat. Paste the section **SETUP block** yourself first,
   wait for "ready" (this locks the style/characters).
2. A **Prompt Runner** panel appears bottom-right. Paste that section's shot prompts into it,
   **one prompt per block, separated by a line containing only `---`**:
   ```
   First prompt text
   can be multiple lines
   ---
   Second prompt text
   ---
   Third prompt text
   ```
3. Set the wait (default 15–20s). Click **🔍 Test** first — it flashes the detected input (green)
   and send button (orange) and reports them. If both are found, click **Start**. **Stop** halts
   after the current prompt.

## After editing this extension
Reload it: `chrome://extensions` → the card's **↻ reload** icon → then **refresh the chat tab**.

## If the panel can't find the chat box
Hit **🔍 Test** to see what it detected. Auto-detect targets the Slate editor
(`[data-slate-editor]`) + a button whose icon glyph is `arrow_forward`/`send`/etc. If it grabs the
wrong element, right-click the real input → Inspect, copy a stable CSS selector, and paste it into
**advanced → input selector** (and the send button's selector if needed).

## Notes
- **Raise the wait** if an image takes longer than ~15s to generate — otherwise the next prompt
  may fire before the box is ready. (Fixed delay by design; simplest thing that works.)
- Personal use only. Respect the product's terms and daily limits — this just saves manual pasting,
  it doesn't bypass any quota.
- Prompts + settings are remembered in the page's localStorage.
