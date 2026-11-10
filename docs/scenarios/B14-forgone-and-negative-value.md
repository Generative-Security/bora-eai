# B14: Forgone and negative value

| | |
|---|---|
| **Accountable** | Use-case sponsor (line-of-business head) |
| **Consulted** | CFO |
| **Lens** | Both |
| **Loss domain** | Strategic; reputational and market; workforce |
| **Party** | First-party |
| **Status** | Draft v0.1 · carried by the value term, not the loss sum |

## Business outcome

The business loses value because it waits while competitors capture it, because a deployed use case never delivers, or because AI makes outcomes worse, through over-reliance, use outside the model's capability, or slower work by experts.

## How B14 enters the net position

B14 is **not** added to the expected-loss sum. It is carried by the value term in the [net position](../06-quantification.md), which can be negative, and by the cost of delay. Treating it as a scenario keeps it visible in the register and gives it an accountable owner.

## Three forms

### 1. Forgone value (cost of waiting)

The organization defers or declines a use case, and the value it would have delivered, net of risk and governance cost, is lost. Competitors that adopt may also erode share or margin.

BCG's 2026 survey of 1,330 executives found its "future-built" companies, 7.5% of those surveyed, delivering 2.4 times the revenue growth and 2.8 times the EBITDA growth of laggards `[consulting]` ([BCG via TechIntelPro](https://techintelpro.com/news/ai/agentic-ai/ai-is-starting-to-pay-off-50-of-companies-now-generate-value-bcg)). This is a correlation, and BCG's own figures move fast: a year earlier, it reported about 5% of companies achieving substantial value `[consulting]`.

### 2. Value that never arrives

The use case is funded but never reaches production, or reaches it and does not deliver:

- S&P Global 2025: 42% of companies abandoned most AI initiatives; the average organization scrapped 46% of proofs of concept before production `[survey]`.
- Gartner: at least 50% of GenAI projects will overrun budgets through 2028; a production system can cost orders of magnitude more than a pilot `[analyst]`.
- Gartner predicts that by 2027, half of organizations that expected to significantly reduce their customer-service workforce will abandon those plans `[analyst]`. Commonwealth Bank reversed its decision to replace 45 customer-service roles with a chatbot after call volumes rose `[secondary]`.
- MIT NANDA (2025) reported about 95% of GenAI pilots without measurable P&L return `[survey, methodology not verified; widely criticized as overhyped]`.

### 3. Negative value

The use case is live and makes outcomes worse:

- **Experts slowed down.** METR's 2025 trial found experienced open-source developers took 19% longer with AI on their own mature codebases, while believing they were 20% faster `[RCT]` ([arXiv](https://arxiv.org/abs/2507.09089)). METR's February 2026 update says developers are probably more sped up now, but describes its own evidence on how much as very weak.
- **Outside the frontier.** In the BCG field experiment, consultants using AI on a task outside its capability were 19 percentage points less likely to reach the correct answer `[RCT, working paper]`.
- **Over-reliance.** Errors accepted because the output looked authoritative.
- **Skills erosion.** Gartner lists skills erosion among five GenAI blind spots `[analyst, via secondary]`.

## Applies when

Always. Every use case carries B14. The question is which form dominates.

## Boundaries

- **B8** is liability for specific false statements to customers. B14 is the general degradation of outcomes.
- **B15** covers governance that destroys value. Where a project fails because of absent controls, record B15; where it fails because the value was never there, record B14.

## Levers

| Lever | Type | Owner |
|---|---|---|
| Measure uplift with throughput, quality, and cycle-time metrics, never self-report alone | Directive | Use-case sponsor |
| Target users and tasks where evidence supports gains (novices, well-scoped tasks inside the frontier) | Preventive | Use-case sponsor |
| Structure pilots as options with a defined decision point and exit | Directive | Use-case sponsor with CFO |
| Require human review where errors are costly and hard to detect | Preventive | Use-case sponsor |
| Record cost of delay for deferred and stopped use cases | Directive | CFO |
| Revisit stopped use cases when evidence or capability changes | Detective | Program owner |

## Quantification notes

See [Layer 7: Value](../layers/L7-value.md) and [Value evidence](../reference/value-evidence.md). Key inputs: P(production), P(value | production), and an uplift distribution that allows negative values for experts and outside-frontier tasks.

## Example scenario statement

> If we defer the claims-summarization assistant by two quarters, we forgo a risk-adjusted $90,000 to $350,000 in handling-time savings, with competitive erosion unquantified. If we deploy it to senior assessors on complex claims, there is a 30% to 50% probability that their handling time does not improve or worsens.

## Questions for the accountable executive

1. How will we know, with measurement rather than surveys, whether this is working?
2. Who is using it, and on which tasks? Is the evidence for gains strong for those people and tasks?
3. What does waiting a quarter cost us?

## Crosswalk

| Framework | Reference |
|---|---|
| ISO 31000 | Risk as positive or negative effect on objectives |
| NIST AI RMF | MAP 3.1 (benefits); MAP 3.2 (costs, including non-monetary costs of errors) |
| ISO/IEC 42001 | Clause 6.1: risks and opportunities |
| ISO/IEC 42005 | Annex C harms and benefits taxonomy |
| Huwyler taxonomy | Unreliable Outputs |
| MIT AI Risk Repository | 5.1 Overreliance and unsafe use; 6.4 Competitive dynamics; 7.3 Lack of capability or robustness |
| NIST AI 600-1 | Human-AI Configuration; Confabulation |

## Open questions

- Is there any rigorously identified estimate of competitive erosion from late AI adoption? We found none.
- How should shadow AI's informal value (B3) be credited when deciding whether to sanction a tool?
