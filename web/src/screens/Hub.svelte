<script>
  import { state } from '../lib/store.js'
  const openTool = () => state.update(s => ({ ...s, view: 'input' }))
</script>

<div style="max-width:860px;margin:0 auto;padding:50px 24px 70px">
  <div style="font-size:.68rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#8A93A0">Toolkit</div>
  <h1 style="margin:10px 0 0;font-weight:600;font-size:2.5rem;letter-spacing:-.025em;color:#1B1D21;line-height:1.12">Research tools for YouTube creators</h1>
  <p style="margin:13px 0 0;color:#5C6470;font-size:1.04rem;max-width:54ch">A growing set of small, sharp tools. Start with content research — more are on the way.</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:36px">
    <div style="background:#fff;border:1px solid #E7EBEF;border-radius:18px;box-shadow:0 1px 2px rgba(18,19,22,.05),0 8px 22px rgba(18,19,22,.06);padding:24px;display:flex;flex-direction:column;gap:16px">
      <div style="display:flex;align-items:center;justify-content:space-between">
        <span style="width:44px;height:44px;border-radius:13px;background:#121316;display:flex;align-items:center;justify-content:center"><svg width="20" height="20" viewBox="0 0 24 24" fill="#fff"><path d="M8 5v14l11-7z"/></svg></span>
        <span style="display:inline-flex;align-items:center;gap:6px;background:#DFF6EA;color:#1E7A4D;border-radius:999px;padding:5px 11px;font-weight:700;font-size:.72rem"><span style="width:7px;height:7px;border-radius:50%;background:#34A86B"></span>Live</span>
      </div>
      <div>
        <h3 style="font-weight:600;font-size:1.12rem;color:#1B1D21;margin:0">YouTube Content Research</h3>
        <p style="margin:7px 0 0;font-size:.9rem;color:#5C6470;line-height:1.55">Scrape the top search results for any niche, sort by what's breaking out, and let AI predict your next video — then export the data as a TSV.</p>
      </div>
      <button on:click={openTool} style="align-self:flex-start;margin-top:2px;display:inline-flex;align-items:center;gap:8px;background:#121316;color:#fff;border:none;border-radius:999px;padding:11px 19px;font-weight:600;font-size:.88rem;cursor:pointer;box-shadow:0 8px 20px rgba(18,19,22,.25)">Open tool <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></button>
    </div>
    {#each [
      { t: 'Title & Thumbnail Tester', d: 'Compare title and thumbnail variants against your niche before you publish.', icon: '<rect x="3" y="4" width="18" height="13" rx="2"/><path d="M8 21h8M12 17v4"/>' },
      { t: 'Channel Audit', d: "Spot a channel's best-performing formats, lengths and posting cadence.", icon: '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>' },
      { t: 'Trend Tracker', d: 'Watch a niche evolve with automatic weekly snapshots and movement alerts.', icon: '<path d="M3 17l6-6 4 4 8-8M21 7h-5M21 7v5"/>' },
    ] as card}
      <div style="background:#FBFCFE;border:1px solid #E7EBEF;border-radius:18px;box-shadow:0 1px 2px rgba(18,19,22,.05),0 8px 22px rgba(18,19,22,.06);padding:24px;display:flex;flex-direction:column;gap:16px">
        <div style="display:flex;align-items:center;justify-content:space-between">
          <span style="width:44px;height:44px;border-radius:13px;background:#F2F4F6;display:flex;align-items:center;justify-content:center"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#8A93A0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{@html card.icon}</svg></span>
          <span style="background:#F2F4F6;color:#8A93A0;border-radius:999px;padding:5px 11px;font-weight:700;font-size:.72rem">Coming soon</span>
        </div>
        <div><h3 style="font-weight:600;font-size:1.12rem;color:#5C6470;margin:0">{card.t}</h3><p style="margin:7px 0 0;font-size:.9rem;color:#8A93A0;line-height:1.55">{card.d}</p></div>
      </div>
    {/each}
  </div>
</div>
