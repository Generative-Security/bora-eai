# Quantification

This page applies to **Medium** and **High** tier use cases. Fast-lane and Low tier use cases do not run these numbers.

## The net position

For each use case *u*:

```
Net annual position(u) = P(production) × P(value | production) × Gross annual value
                         − Σ Expected annual loss(B1 … B13 | u)
                         − Allocated governance cost(u)
```

| Term | Meaning | Layer |
|---|---|---|
| P(production) | Probability the use case reaches production at all | [Layer 7](layers/L7-value.md) |
| P(value \| production) | Probability it delivers the expected value once in production | [Layer 7](layers/L7-value.md) |
| Gross annual value | Value if it works: affected labor cost or revenue × uplift | [Layer 7](layers/L7-value.md) |
| Expected annual loss | Frequency × magnitude for each applicable scenario, B1 to B13 | [Layer 6](layers/L6-loss.md) |
| Allocated governance cost | The governance cost this use case drives | [Layer 8](layers/L8-governance-cost.md) |

**B14 and B15 are not in the loss sum.** Forgone and negative value (B14) is carried by the value term, which can be negative. Governance cost and failure (B15) is carried by the governance term, and by its effect on P(production). Adding them to the loss sum would count them twice.

A companion figure, the **cost of delay**, tells the board what waiting costs:

```
Cost of delay(u) per quarter ≈ [P(production) × P(value | production) × Gross annual value] ÷ 4
                               + competitive erosion
```

Competitive erosion has no rigorously identified estimate in the literature. Show it as a scenario range, not a point.

## Ranges, not points

Multiplying two subjective probabilities by an uncalibrated loss estimate and presenting one dollar figure gives a board false precision. So every input is a **calibrated three-point estimate**: low, most likely, and high.

- **Low** and **high** are set so that the estimator is about 90% confident the true value lies between them.
- **Most likely** is the single value the estimator thinks most probable.
- Each estimate is fitted as a beta-PERT distribution (or a lognormal for heavy-tailed losses) and combined by Monte Carlo simulation, typically 10,000 or more trials.

This is how FAIR analyses already work `[standard]` ([FAIR Institute](https://www.fairinstitute.org/blog/fair-artificial-intelligence-ai-cyber-risk-playbook)). BORA-EAI applies the same discipline to the value and governance terms, not only to loss.

Calibration matters more than precision. Estimators should be trained (calibration exercises are standard in FAIR practice), should record where each range came from, and should prefer base rates and internal data over intuition.

## What the board sees

For each Medium or High use case:

| Output | Why |
|---|---|
| **10th, 50th, and 90th percentile** net annual position | Shows the range of plausible outcomes, not a single number |
| **Probability the net position is below zero** | The single most decision-relevant number: how likely is this to destroy value? |
| **1-in-20-year loss** for each quantified scenario (the 95th percentile of annual loss) | Expected annual loss averages away the rare, large events that risk appetite is written for |
| **Cost of delay per quarter** | What waiting costs, so that "not yet" is a visible choice |

Where loss or uplift data is thin, a wide range is the honest output. Present it as wide; do not narrow it to look decisive.

## Starting base rates

Organizations should replace these with their own pipeline and incident data as soon as they have it. Until then, published base rates give a defensible starting point.

| Input | Starting range | Basis |
|---|---|---|
| P(production) for a new custom build | 0.45 to 0.65 | S&P Global 2025: average organization scrapped 46% of proofs of concept before production `[survey]` |
| P(production) for a vendor-partnered build | Higher than custom | MIT NANDA 2025 reported vendor-partnered builds about twice as likely to succeed `[survey, methodology not verified]` |
| P(value \| production) | 0.05 to 0.40 | Between MIT NANDA's ~5% of pilots with measurable P&L return and McKinsey's ~39% of firms reporting any EBIT impact `[survey; both not cleanly conditional]` |
| Uplift, customer support | +5% to +34% | Brynjolfsson, Li & Raymond: ~14% average, ~34% for novices, little for experts `[peer-reviewed]` |
| Uplift, experienced developers on familiar code | −19% to +26% | METR 2025 (−19%) and Cui et al. field trials (+26% tasks) `[RCT]` |
| Uplift, writing tasks | +20% to +40% time saved | Noy & Zhang, *Science* 2023 `[peer-reviewed]` |

These base rates are not cleanly conditional on each other. Treat them as weak priors. See [Value evidence](reference/value-evidence.md) for the full set, including null results.

## Estimating loss per scenario

Each applicable scenario gets:

- **Frequency:** the probability of at least one loss event in the next 12 months, or an annual event rate. Sources: internal incidents, industry incident data, the [incident library](reference/incident-library.md), and expert estimates.
- **Magnitude:** a range for the loss per event, built from the [FAIR loss forms](layers/L6-loss.md#loss-forms-the-analyst-view) (productivity, response, replacement, fines and judgments, competitive advantage, reputation).
- **Party:** first-party (the organization's own loss) or third-party (liability to others), which determines which insurance line might respond.

Write each scenario as a statement in the FAIR-AIR form before estimating it:

> There is an X% probability in the next 12 months that [threat or failure] in [use case] causes [business outcome], producing a [first- or third-party] loss of $A to $B.

## A minimal simulation

The worked example uses a simulation like this. It is shown for transparency, not as a tool.

```python
import numpy as np
rng = np.random.default_rng(7)
N = 100_000

def pert(low, mode, high, size, lamb=4):
    a = 1 + lamb * (mode - low) / (high - low)
    b = 1 + lamb * (high - mode) / (high - low)
    return low + rng.beta(a, b, size) * (high - low)

p_prod  = pert(0.50, 0.65, 0.80, N)
p_value = pert(0.20, 0.45, 0.70, N)
gross   = pert(400_000, 900_000, 1_600_000, N)
value   = p_prod * p_value * gross

# One scenario: annual probability of an event, and loss per event (lognormal tail)
p_event = pert(0.05, 0.15, 0.35, N)
event   = rng.random(N) < p_event
loss    = np.where(event, rng.lognormal(np.log(60_000), 1.0, N), 0.0)

governance = pert(40_000, 70_000, 120_000, N)
net = value - loss - governance

print(np.percentile(net, [10, 50, 90]), (net < 0).mean(), np.percentile(loss, 95))
```

## The portfolio view

Across use cases, the board sees one chart: the **median net position** plotted against **residual risk** (for example, the largest 1-in-20-year scenario loss), one point per use case, with the 10th to 90th percentile range shown as an error bar.

This replaces the qualitative value-versus-feasibility 2×2 matrices commonly used in AI portfolio planning, none of which we found to have published empirical validation. Three artifacts sit behind it: the scenario register, the responsibility and insurability map from Layers 2 and 6, and the sovereignty profile from Layer 3.

## Common mistakes

- **Using vendor or pilot-survey uplift as the value input.** In METR's 2025 trial, developers believed AI had cut their time by 20% when it had increased it by 19%. Self-reported productivity is not a measurement.
- **Treating the CBRA score as a risk number.** It selects a tier, nothing more.
- **Adding B14 or B15 to the loss sum.** They are already in the value and governance terms.
- **Narrowing a range to look decisive.** The width of the range is information.
- **Quantifying a Low tier use case.** The effort is not justified, and the false precision is harmful.
- **Forgetting the tail.** Two use cases with the same expected loss can have very different 1-in-20-year losses.

Next: [Layers](layers/README.md)
