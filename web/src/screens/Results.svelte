<script>
  import { state, filteredRows, pagedRows, pageInfo, runProgress } from '../lib/store.js'
  import { cancelJob, downloadUrl } from '../lib/api.js'
  import { fmtViews, fmtSubs, fmtK, fmtDate, gradientFor } from '../lib/fmt.js'
  import ToolHeader from './ToolHeader.svelte'

  const sortDefs = [
    ['breakout', 'Best'], ['views', 'Most views'], ['likes', 'Most likes'],
    ['comments', 'Most comments'], ['newest', 'Newest'], ['longest', 'Longest'],
  ]
  const chip = (active) =>
    `display:inline-flex;align-items:center;gap:6px;border-radius:999px;padding:8px 15px;font-weight:600;font-size:.82rem;cursor:pointer;` +
    (active ? 'background:#121316;color:#fff;border:1.5px solid #121316;' : 'background:#fff;color:#5C6470;border:1.5px solid #E7EBEF;')

  $: fast = $state.fast
  const setSort = (k) => { if (!(fast && k === 'breakout')) state.update(s => ({ ...s, sort: k, page: 1 })) }
  const setPage = (p) => state.update(s => ({ ...s, page: p }))
  const reRunFull = () => state.update(s => ({ ...s, view: 'input', mode: 'full' }))

  async function cancel() {
    state.update(s => ({ ...s, cancelling: true }))
    await cancelJob($state.jobId)
  }

  // Auto-scroll the terminal log to the newest line.
  function autoscroll(node) {
    const obs = new MutationObserver(() => { node.scrollTop = node.scrollHeight })
    obs.observe(node, { childList: true, subtree: true, characterData: true })
    return { destroy: () => obs.disconnect() }
  }
</script>

<div style="max-width:960px;margin:0 auto;padding:30px 24px 60px">
  <ToolHeader />

  {#if $state.running}
    <div style="background:#fff;border:1px solid #E7EBEF;border-radius:18px;box-shadow:0 1px 2px rgba(18,19,22,.05),0 8px 22px rgba(18,19,22,.06);padding:28px 30px">
      <div style="display:flex;align-items:center;gap:13px">
        <span style="display:inline-block;width:26px;height:26px;flex:none;border-radius:50%;border:3px solid #E7EBEF;border-top-color:#121316;animation:spin .8s linear infinite"></span>
        <div style="flex:1;min-width:0">
          <div style="font-weight:600;color:#1B1D21">{$runProgress.phase}…</div>
          <div style="font-size:.84rem;color:#8A93A0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">{$state.progress.length ? $state.progress[$state.progress.length - 1] : 'Starting the scrape…'}</div>
        </div>
        <button on:click={cancel} disabled={$state.cancelling} style="flex:none;background:#fff;border:1.5px solid #E7EBEF;border-radius:999px;padding:8px 16px;font-weight:600;font-size:.84rem;color:#1B1D21;cursor:pointer">{$state.cancelling ? 'Cancelling…' : 'Cancel run'}</button>
      </div>

      <!-- progress bar -->
      <div style="margin-top:16px;height:7px;border-radius:999px;background:#EEF1F4;overflow:hidden">
        <div style="height:100%;border-radius:999px;background:#121316;width:{$runProgress.pct}%;transition:width .4s ease"></div>
      </div>

      <!-- live terminal log -->
      <div use:autoscroll style="margin-top:14px;background:#0E1116;border-radius:12px;padding:14px 16px;height:200px;overflow:auto;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.78rem;line-height:1.7;color:#C7D0DA">
        {#each $state.progress as line}
          <div><span style="color:#4B5563">$</span> <span style="color:{line.includes('FAILED') ? '#F0A0A0' : (line.includes('Cancelled') ? '#F0C674' : '#9ED4F8')}">{line}</span></div>
        {/each}
        <div style="color:#5B6675">▌</div>
      </div>
    </div>

  {:else if $state.error}
    <div style="background:#fff;border:1px solid #F3D3D3;border-radius:18px;box-shadow:0 1px 2px rgba(18,19,22,.05),0 8px 22px rgba(18,19,22,.06);padding:34px">
      <div style="font-weight:700;font-size:1.05rem;color:#B23B3B">Run didn't complete</div>
      <p style="margin:8px 0 0;font-size:.9rem;color:#5C6470;line-height:1.55">{$state.error}</p>
      <button on:click={() => state.update(s => ({ ...s, view: 'input' }))} style="margin-top:16px;background:#121316;color:#fff;border:none;border-radius:999px;padding:10px 17px;font-weight:600;font-size:.85rem;cursor:pointer">Back to setup</button>
    </div>

  {:else}
    <div style="display:flex;align-items:flex-end;justify-content:space-between;gap:16px;margin-bottom:16px">
      <p style="margin:0;color:#5C6470;font-size:.92rem"><b style="color:#1B1D21">{$state.rows.length} videos</b> from {$state.keywords.length} {$state.keywords.length === 1 ? 'keyword' : 'keywords'}{#if $state.date} · scraped {fmtDate($state.date)}{/if}</p>
      <a href={downloadUrl($state.jobId)} style="display:inline-flex;align-items:center;gap:8px;background:#121316;color:#fff;text-decoration:none;border:none;border-radius:999px;padding:10px 17px;font-weight:600;font-size:.85rem;cursor:pointer;box-shadow:0 8px 20px rgba(18,19,22,.25)"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12M7 10l5 5 5-5M5 21h14"/></svg>Download TSV</a>
    </div>

    {#if $state.failedNote}
      <div style="background:#FFF6E6;border:1px solid #F2E2BE;border-radius:12px;padding:10px 14px;margin-bottom:12px;font-size:.84rem;color:#8A6D1E">{$state.failedNote}</div>
    {/if}

    {#if fast}
      <div style="display:flex;align-items:center;justify-content:space-between;gap:12px;background:#EEF4FF;border:1px solid #D7E4FB;border-radius:12px;padding:11px 15px;margin-bottom:14px">
        <span style="font-size:.86rem;color:#33507F"><b>Breakout & AI need Full mode.</b> Fast mode skips subscriber data, so breakout can't be computed.</span>
        <button on:click={reRunFull} style="flex:none;background:#121316;color:#fff;border:none;border-radius:999px;padding:8px 14px;font-weight:600;font-size:.82rem;cursor:pointer">Re-run in Full mode</button>
      </div>
    {/if}

    <!-- filter row -->
    <div style="display:flex;gap:10px;align-items:center;margin-bottom:12px;flex-wrap:wrap">
      <div style="flex:1;min-width:200px;display:flex;align-items:center;gap:9px;background:#fff;border:1.5px solid #E7EBEF;border-radius:12px;padding:10px 14px">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#8A93A0" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4-4"/></svg>
        <input bind:value={$state.query} placeholder="Filter by title or channel…" style="border:none;outline:none;background:none;font-size:.9rem;color:#1B1D21;width:100%">
      </div>
      <div style="display:flex;align-items:center;gap:7px;background:#fff;border:1.5px solid #E7EBEF;border-radius:12px;padding:9px 13px">
        <span style="font-size:.74rem;font-weight:700;color:#8A93A0">KEYWORD</span>
        <select bind:value={$state.keyword} style="border:none;outline:none;background:none;font-size:.86rem;font-weight:600;color:#1B1D21;cursor:pointer">
          <option value="all">All</option>
          {#each $state.keywords as kw}<option value={kw}>{kw}</option>{/each}
        </select>
      </div>
      <button on:click={() => state.update(s => ({ ...s, verifiedOnly: !s.verifiedOnly }))} disabled={fast} title={fast ? 'Needs full mode' : ''} style={chip($state.verifiedOnly) + (fast ? 'opacity:.4;cursor:not-allowed;' : '')}><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>Verified only</button>
    </div>

    <!-- sort chips -->
    <div style="display:flex;align-items:center;gap:8px;margin-bottom:14px;flex-wrap:wrap">
      <span style="font-size:.74rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#8A93A0;margin-right:2px">Sort</span>
      {#each sortDefs as [k, label]}
        <button on:click={() => setSort(k)} disabled={fast && k === 'breakout'} title={fast && k === 'breakout' ? 'Needs full mode' : ''} style={chip($state.sort === k) + (fast && k === 'breakout' ? 'opacity:.4;cursor:not-allowed;' : '')}>{label}</button>
      {/each}
    </div>

    <!-- table -->
    <div style="background:#fff;border:1px solid #E7EBEF;border-radius:18px;box-shadow:0 1px 2px rgba(18,19,22,.05),0 8px 22px rgba(18,19,22,.06);overflow:hidden">
      <div style="display:grid;grid-template-columns:minmax(0,1fr) 150px 78px 84px 76px 60px;gap:12px;padding:12px 18px;border-bottom:1px solid #E7EBEF;background:#FBFCFE">
        <span style="font-size:.66rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#8A93A0">Video</span>
        <span style="font-size:.66rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#8A93A0">Channel</span>
        <span style="font-size:.66rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#8A93A0;text-align:right">Views</span>
        <span style="font-size:.66rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#8A93A0;text-align:right">Likes</span>
        <span style="font-size:.66rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#8A93A0;text-align:right">Breakout</span>
        <span style="font-size:.66rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#8A93A0;text-align:right">Len</span>
      </div>

      {#if $filteredRows.length === 0}
        <div style="padding:38px;text-align:center;color:#8A93A0;font-size:.9rem">No videos match your filters. <a on:click={() => state.update(s => ({ ...s, query: '', keyword: 'all', verifiedOnly: false }))} style="color:#1B1D21;font-weight:600;cursor:pointer;text-decoration:underline">Clear filters</a></div>
      {:else}
        {#each $pagedRows as v (v.video_id)}
          <div style="display:grid;grid-template-columns:minmax(0,1fr) 150px 78px 84px 76px 60px;gap:12px;padding:11px 18px;border-top:1px solid #F2F4F6;align-items:center">
            <div style="display:flex;align-items:center;gap:11px;min-width:0">
              <a href={v.video_url} target="_blank" rel="noopener" style="width:80px;height:46px;flex:none;border-radius:8px;position:relative;overflow:hidden;background:{v.thumbnail ? `center/cover url('${v.thumbnail}')` : gradientFor(v.video_id)};text-decoration:none"><span style="position:absolute;right:4px;bottom:4px;background:rgba(10,14,22,.8);color:#fff;font-size:.6rem;font-weight:700;padding:1px 4px;border-radius:4px">{v.duration || ''}</span></a>
              <div style="min-width:0"><a href={v.video_url} target="_blank" rel="noopener" style="font-weight:600;font-size:.86rem;color:#1B1D21;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;display:block;text-decoration:none">{v.title}</a><div style="font-size:.72rem;color:#8A93A0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">{v.keyword}</div></div>
            </div>
            <div style="font-size:.82rem;color:#1B1D21;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">{v.channel}<div style="font-size:.71rem;color:#8A93A0;font-weight:500">{v.subscribers == null ? '—' : fmtSubs(v.subscribers) + ' subs'}</div></div>
            <div style="text-align:right;font-weight:600;font-size:.84rem;color:#1B1D21">{fmtViews(v.views)}</div>
            <div style="text-align:right;font-size:.83rem;color:#5C6470">{fmtK(v.likes)}</div>
            <div style="text-align:right">{#if v.breakout == null}<span style="color:#C2C8D0">—</span>{:else}<span style="display:inline-flex;align-items:center;background:#121316;color:#fff;font-weight:700;font-size:.78rem;padding:4px 9px;border-radius:999px">×<b style="color:#9ED4F8">{v.breakout.toFixed(1)}</b></span>{/if}</div>
            <div style="text-align:right;font-size:.78rem;color:#5C6470">{v.duration || '—'}</div>
          </div>
        {/each}
      {/if}
    </div>

    <div style="display:flex;align-items:center;justify-content:space-between;margin-top:14px;font-size:.82rem;color:#8A93A0">
      <span>Showing {$pagedRows.length} of {$pageInfo.total}</span>
      {#if $pageInfo.showPager}
        <span style="display:flex;gap:6px">
          {#each Array($pageInfo.pages) as _, i}
            <span on:click={() => setPage(i + 1)} style="width:30px;height:30px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-weight:600;cursor:pointer;{$pageInfo.page === i + 1 ? 'background:#121316;color:#fff' : 'background:#fff;border:1px solid #E7EBEF;color:#1B1D21'}">{i + 1}</span>
          {/each}
        </span>
      {/if}
    </div>
  {/if}
</div>
