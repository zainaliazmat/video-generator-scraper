// Shared UI helpers used across screens.

// Pill/chip button style (active = filled dark, inactive = outline).
export const chip = (active) =>
  'display:inline-flex;align-items:center;gap:6px;border-radius:999px;padding:8px 15px;font-weight:600;font-size:.82rem;cursor:pointer;' +
  (active ? 'background:#121316;color:#fff;border:1.5px solid #121316;'
          : 'background:#fff;color:#5C6470;border:1.5px solid #E7EBEF;')

// Svelte action: keep a scroll container pinned to the bottom as content streams in.
export function autoscroll(node) {
  const obs = new MutationObserver(() => { node.scrollTop = node.scrollHeight })
  obs.observe(node, { childList: true, subtree: true, characterData: true })
  return { destroy: () => obs.disconnect() }
}
