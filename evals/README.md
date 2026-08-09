# evals/

Measures whether a change to the finance-video pipeline made the output better, worse, or
only cheaper.

```bash
python3 evals/run.py                       # score every finance cut on disk
python3 evals/run.py --slug japanese-money-methods
python3 evals/run.py --all                 # include the history lane + practice builds
python3 evals/run.py --selftest            # the checker checks itself
python3 tools/run_metrics.py --slug <slug> # tokens, wall time, invocations
```

| File | What |
|---|---|
| [run.py](run.py) | 10 asserted checks (Tier A) over every composition on disk |
| [rubric.md](rubric.md) | Tier A + the judged dimensions (Tier B) + process metrics (Tier C) |
| [briefs.md](briefs.md) | 6 golden briefs for full end-to-end runs |
| `results/` | one JSON per scoring pass |

## Why it scores artifacts, not runs

One run costs ~70M tokens and hours of render ([audit/05-baseline.md](../audit/05-baseline.md)).
A suite of 5–8 *runs* is not a test suite, it is a month. Every Tier A check is instead a
property of what a run leaves on disk — so the same scorer grades the seven historical runs
(the baseline) and every future one, and the numbers are directly comparable.

## The rule

Tier A blocker failures must not increase, and Tier B B1/B2 must not drop. A change that
lowers token cost while worsening either is reverted. Cheapness is not the goal; cheapness
at equal accuracy is.
