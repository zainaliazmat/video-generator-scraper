<script>
  import { onMount } from 'svelte'
  import { state } from '../lib/store.js'
  import { predict } from '../lib/api.js'
  import ToolHeader from './ToolHeader.svelte'

  const reRunFull = () => state.update(s => ({ ...s, view: 'input', mode: 'full' }))

  async function run() {
    if ($state.aiState === 'loading') return
    state.update(s => ({ ...s, aiState: 'loading', ai: null }))
    try {
      const out = await predict($state.jobId)
      if (out && out.ok) state.update(s => ({ ...s, aiState: 'done', ai: out }))
      else state.update(s => ({ ...s, aiState: 'error', ai: out || { reason: 'error', detail: 'Unknown error' } }))
    } catch (e) {
      state.update(s => ({ ...s, aiState: 'error', ai: { reason: 'error', detail: e.message } }))
    }
  }

  const REASONS = {
    cli_missing: { title: 'AI prediction needs the Claude CLI', body: 'Install it and log in with your Claude subscription, then retry:' },
    not_logged_in: { title: 'Claude isn’t logged in', body: 'Log in with your Claude subscription, then retry:' },
    parse_failed: { title: 'Couldn’t read a prediction from this data', body: 'The model didn’t return a usable result. Try again.' },
    error: { title: 'Couldn’t generate a prediction', body: 'Something went wrong talking to Claude. Try again.' },
  }
  $: reason = $state.ai && REASONS[$state.ai.reason] || REASONS.error
  $: needsCli = $state.ai && ($state.ai.reason === 'cli_missing' || $state.ai.reason === 'not_logged_in')

  onMount(() => { if (!$state.fast && $state.aiState === 'idle') run() })
</script>

<div style="max-width:960px;margin:0 auto;padding:30px 24px 60px">
  <ToolHeader />

  {#if $state.fast}
    <div style="background:#fff;border:1px solid #E7EBEF;border-radius:18px;box-shadow:0 1px 2px rgba(18,19,22,.05),0 8px 22px rgba(18,19,22,.06);padding:40px;text-align:center">
      <div style="font-weight:600;font-size:1.05rem;color:#1B1D21">AI prediction needs Full-mode data</div>
      <p style="margin:8px 0 0;font-size:.9rem;color:#8A93A0;max-width:48ch;margin-left:auto;margin-right:auto;line-height:1.55">The prediction reads breakout patterns (views ÷ subscribers). Fast mode skips subscriber counts, so there's nothing to analyse yet.</p>
      <button on:click={reRunFull} style="margin-top:18px;background:#121316;color:#fff;border:none;border-radius:999px;padding:10px 18px;font-weight:600;font-size:.85rem;cursor:pointer">Re-run in Full mode</button>
    </div>

  {:else if $state.aiState === 'loading' || $state.aiState === 'idle'}
    <div style="background:#fff;border:1px solid #E7EBEF;border-radius:18px;box-shadow:0 1px 2px rgba(18,19,22,.05),0 8px 22px rgba(18,19,22,.06);padding:50px;text-align:center">
      <span style="display:inline-block;width:34px;height:34px;border-radius:50%;border:3px solid #E7EBEF;border-top-color:#121316;animation:spin .8s linear infinite"></span>
      <div style="margin-top:18px;font-weight:600;color:#1B1D21">Analysing {$state.rows.length} videos across {$state.keywords.length} keywords…</div>
      <div style="margin-top:4px;font-size:.86rem;color:#8A93A0">Reading breakout patterns, title formats and theme gaps to predict your next video</div>
    </div>

  {:else if $state.aiState === 'error'}
    <div style="background:#fff;border:1px solid #F3D3D3;border-radius:18px;box-shadow:0 1px 2px rgba(18,19,22,.05),0 8px 22px rgba(18,19,22,.06);padding:34px">
      <div style="font-weight:700;font-size:1.05rem;color:#B23B3B">{reason.title}</div>
      <p style="margin:8px 0 0;font-size:.9rem;color:#5C6470;line-height:1.55">{reason.body}</p>
      {#if needsCli}
        <pre style="margin:12px 0 0;background:#F7F8FA;border:1px solid #E7EBEF;border-radius:10px;padding:12px 14px;font-size:.8rem;color:#1B1D21;white-space:pre-wrap">npm install -g @anthropic-ai/claude-code
claude        # then /login</pre>
      {/if}
      <button on:click={run} style="margin-top:16px;background:#121316;color:#fff;border:none;border-radius:999px;padding:10px 17px;font-weight:600;font-size:.85rem;cursor:pointer">Retry</button>
    </div>

  {:else if $state.ai}
    {@const ai = $state.ai}
    <div style="animation:fadeup .4s ease">
      <div style="background:#121316;border-radius:22px;padding:30px 32px;color:#fff;position:relative;overflow:hidden">
        <div style="display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap">
          <div style="font-size:.68rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#9ED4F8">Predicted next video</div>
          <span style="display:inline-flex;align-items:center;gap:6px;background:rgba(255,255,255,.12);color:#fff;border-radius:999px;padding:6px 13px;font-weight:700;font-size:.8rem">est. breakout ×<b style="color:#9ED4F8">{ai.est}</b></span>
        </div>
        <h2 style="margin:14px 0 0;font-weight:600;font-size:1.72rem;letter-spacing:-.02em;line-height:1.18;color:#fff;max-width:24ch">{ai.topic}</h2>
        <p style="margin:14px 0 0;color:#C7CDD4;font-size:.96rem;line-height:1.6;max-width:64ch">{ai.rationale}</p>
        {#if ai.angle}
        <div style="display:inline-flex;align-items:flex-start;gap:9px;margin-top:18px;background:rgba(207,234,255,.12);border:1px solid rgba(158,212,248,.3);border-radius:12px;padding:12px 15px;max-width:64ch">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#9ED4F8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex:none;margin-top:1px"><path d="M12 3l1.8 4.7L18.5 9l-4.7 1.8L12 15.5l-1.8-4.7L5.5 9l4.7-1.3L12 3z"/></svg>
          <span style="font-size:.88rem;color:#E7EBEF;line-height:1.5">{ai.angle}</span>
        </div>
        {/if}
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:18px">
        <div style="background:#fff;border:1px solid #E7EBEF;border-radius:18px;box-shadow:0 1px 2px rgba(18,19,22,.05),0 8px 22px rgba(18,19,22,.06);padding:22px 24px">
          <h3 style="font-weight:600;font-size:1.04rem;color:#1B1D21;margin:0 0 14px">Why this will work</h3>
          <div style="display:flex;flex-direction:column;gap:13px">
            {#each ai.evidence as e}
              <div style="display:flex;gap:11px"><span style="flex:none;width:23px;height:23px;border-radius:50%;background:#DFF6EA;color:#1E7A4D;display:flex;align-items:center;justify-content:center;margin-top:1px"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg></span><span style="font-size:.87rem;color:#5C6470;line-height:1.5">{e}</span></div>
            {/each}
          </div>
        </div>
        <div style="background:#fff;border:1px solid #E7EBEF;border-radius:18px;box-shadow:0 1px 2px rgba(18,19,22,.05),0 8px 22px rgba(18,19,22,.06);padding:22px 24px">
          <h3 style="font-weight:600;font-size:1.04rem;color:#1B1D21;margin:0 0 14px">More ideas to test</h3>
          <div style="display:flex;flex-direction:column;gap:10px">
            {#each ai.ideas as idea}
              <div style="display:flex;align-items:center;gap:12px;background:#FBFCFE;border:1px solid #E7EBEF;border-radius:12px;padding:11px 13px"><span style="flex:1;font-weight:600;font-size:.86rem;color:#1B1D21;line-height:1.35">{idea.title}</span>{#if idea.est}<span style="flex:none;display:inline-flex;align-items:center;background:#121316;color:#fff;font-weight:700;font-size:.74rem;padding:4px 9px;border-radius:999px">×<b style="color:#9ED4F8">{idea.est}</b></span>{/if}</div>
            {/each}
          </div>
        </div>
      </div>
      <div style="display:flex;align-items:center;justify-content:space-between;gap:14px;margin-top:18px;flex-wrap:wrap">
        <span style="font-size:.8rem;color:#8A93A0">Generated by Signal AI from this snapshot · estimates are directional, not guarantees</span>
        <button on:click={run} style="display:inline-flex;align-items:center;gap:8px;background:#fff;border:1.5px solid #E7EBEF;border-radius:999px;padding:9px 16px;font-weight:600;font-size:.85rem;color:#1B1D21;cursor:pointer"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a9 9 0 1 1-3-6.7L21 8M21 4v4h-4"/></svg>Regenerate</button>
      </div>
    </div>
  {/if}
</div>
