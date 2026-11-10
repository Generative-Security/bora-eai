# Layer 7: Value

> **Executive question:** What do we gain, or forgo by waiting?

## Purpose

Layer 7 estimates what the use case is worth if it works, the probability that it works, and the cost of waiting. It puts the upside on the same page as the threats, so that declining to deploy shows up as a cost rather than a safe default.

## Why value belongs in a risk analysis

Risk standards already treat risk as two-sided. ISO 31000 defines risk as the "effect of uncertainty on objectives," where an effect can be positive or negative `[standard]`. The NIST AI RMF asks organizations to document an AI system's potential benefits (MAP 3.1) and potential costs, including non-monetary costs of errors (MAP 3.2) `[standard]` ([NIST AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf)). ISO/IEC 42001 clause 6.1 requires actions on "risks and opportunities", and ISO/IEC 23894 describes risk management's purpose as "the creation and protection of value" `[standard]`.

FAIR, by contrast, quantifies loss only. There is no published benefit-side counterpart to FAIR, so BORA-EAI builds one by analogy.

## The value terms

```
Risk-adjusted annual value = P(production) × P(value | production) × Gross annual value
Gross annual value         = Affected labor cost or revenue × Uplift
```

All terms are ranges.

### P(production)

The probability the use case reaches production at all. S&P Global's 2025 survey found the average organization scrapped 46% of AI proofs of concept before production, and 42% of companies abandoned most of their AI initiatives `[survey]` ([CIO Dive](https://www.ciodive.com/news/ai-project-failure-rates/742590/)). Gartner predicted at least 30% of GenAI projects would be abandoned after proof of concept by the end of 2025, citing poor data quality, inadequate risk controls, escalating costs, or unclear value `[analyst]`. Start from roughly 0.45 to 0.65 for a new custom build, and replace with your own pipeline data.

### P(value | production)

The probability the use case delivers the expected value once live. Published estimates range widely: MIT's NANDA project reported about 5% of GenAI pilots delivering measurable P&L return `[survey, methodology not verified]`, while McKinsey's State of AI 2025 reported about 39% of firms seeing any enterprise-level EBIT impact `[survey]`. Projects that go live can still miss: Gartner predicts that by 2027, half of organizations that expected to significantly cut their customer-service workforce will abandon those plans `[analyst]`, and Commonwealth Bank reversed a decision to replace 45 customer-service roles with a chatbot `[secondary]`.

### Uplift

The productivity or revenue change per affected unit. This is where most value estimates go wrong. The rigorous evidence shows uplift depends on **who** uses the tool and **for what**:

| Function | Finding | Evidence |
|---|---|---|
| Customer support | +14% resolutions per hour on average; +34% for novices; little for experienced agents | Brynjolfsson, Li & Raymond, 5,179 agents `[peer-reviewed]` |
| Consulting and analysis | 25% faster, higher quality on tasks inside the AI frontier; 19 percentage points *less* likely to be correct on a task outside it | Dell'Acqua et al., 758 BCG consultants `[RCT, working paper]` |
| Writing | ~40% less time, ~18% higher quality | Noy & Zhang, *Science* 2023 `[peer-reviewed]` |
| Software engineering | +26% completed tasks in large-firm field trials, mostly for junior developers | Cui et al., ~4,867 developers `[RCT, working paper]` |
| Software engineering, experts on own code | **19% slower** with AI, while believing they were 20% faster | METR 2025, 16 developers `[RCT]` |
| Economy-wide | ~2.8% time saved; no measurable earnings effect | Humlum & Vestergaard, Danish administrative data `[quasi-experimental]` |

Rigorous evidence is strong for customer support, writing, software engineering, and consulting-style analysis. It is thin or absent for HR, finance, legal, manufacturing, and supply chain, where estimates rest mostly on consulting models. See [Value evidence](../reference/value-evidence.md).

Turn the moderators into use-case attributes:

- **User expertise:** novices gain most; experts on familiar work may lose time.
- **Task position:** inside or outside the model's demonstrated capability.
- **Verifiability:** can errors be caught before they matter?

Never use self-reported productivity as the uplift input. METR's developers were confident they had been sped up when they had been slowed down.

### Potential versus realized value

McKinsey's 2023 model put generative AI's potential at US$2.6 to 4.4 trillion a year, about 75% of it in customer operations, marketing and sales, software engineering, and R&D `[consulting]`. Realized value lags this by roughly an order of magnitude. Show both: the "theoretical opportunity" and the risk-adjusted expected value. The gap between them is the case for measuring.

## Cost of delay

```
Cost of delay per quarter ≈ Risk-adjusted annual value ÷ 4 + competitive erosion
```

This is the standard cost-of-delay concept from product development (Reinertsen; used in SAFe's weighted-shortest-job-first prioritization). Competitive erosion, the share or margin lost while competitors adopt, has no rigorously identified estimate; express it as a scenario range. BCG's 2026 finding that "future-built" firms show 2.4 times the revenue growth of laggards is a correlation, not a measure of erosion `[consulting]`.

## Pilots as options

A pilot is often best treated as a real option: pay a small, known amount to narrow the value range, with a defined decision point to expand or stop. The literature on real options for IT investment (for example, Benaroch and Kauffman, *Information Systems Research*, 1999) supports this framing. Record the decision point and the evidence that will trigger each outcome.

## Value includes avoided loss

Some AI use cases reduce other risks: fraud detection, monitoring, faster incident response. Count that as value, with the same range discipline.

## Output

Ranges for P(production), P(value | production), gross annual value, risk-adjusted annual value, and cost of delay per quarter. These feed the value term of the [net position](../06-quantification.md) and scenario [B14](../scenarios/B14-forgone-and-negative-value.md).

Next: [Layer 8: Governance cost](L8-governance-cost.md)
