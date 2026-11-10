# B15: Governance cost and failure

| | |
|---|---|
| **Accountable** | CRO |
| **Consulted** | CFO |
| **Lens** | Both |
| **Loss domain** | Strategic; regulatory and compliance |
| **Party** | First-party |
| **Status** | Draft v0.1 · carried by the governance term, not the loss sum |

## Business outcome

The organization spends on AI governance that does not reduce exposure, or fails to put adequate controls in place, so that projects are cancelled, regulatory obligations are breached, or teams route around governance altogether.

## How B15 enters the net position

B15 is **not** added to the expected-loss sum. It is carried by the governance-cost term in the [net position](../06-quantification.md), and by its effect on P(production) in the value term. Treating it as a scenario keeps governance itself under review, with an accountable owner.

## Two failure modes

### 1. Too much, or the wrong kind

- Low-risk use cases wait weeks for approval.
- Red teaming and full assessments are applied regardless of tier.
- Governance cost exceeds the value it protects.
- Teams route around the process, which drives shadow AI (B3).

### 2. Too little

- Use cases go live without controls, and are later cancelled, rebuilt, or pulled.
- Regulatory obligations are missed (for example, EU AI Act transparency from 2 August 2026, or Australian automated-decision disclosure from 10 December 2026).
- Nobody owns the register, so the organization cannot say what AI it uses.

## Evidence

- **Controls and cancellation.** Gartner's predictions on abandoned GenAI projects (at least 30% after proof of concept by end of 2025) and cancelled agentic AI projects (over 40% by end of 2027) both name inadequate risk controls among the causes `[analyst]`.
- **The controls gap.** BCG's 2026 survey found only 5% of companies had the full set of controls in place, while 42% expect to grant AI agents autonomy by 2030 `[consulting]`.
- **Governance maturity.** IBM 2025: 63% of breached organizations lacked or were still developing an AI governance policy; of those with policies, only 34% audited for unsanctioned AI `[survey]`.
- **Governance activity.** IAPP's 2025 survey found 77% of organizations working on AI governance `[survey]`.
- **Cost.** Hard data is scarce; see [Layer 8](../layers/L8-governance-cost.md) and [Governance cost evidence](../reference/governance-cost-evidence.md).
- **Gap:** we found no study measuring whether governance spend raises the rate at which AI projects reach production or deliver value.

## Applies when

Always, at the portfolio level. For an individual use case, B15 is most relevant when:

- the use case is High tier (governance cost is material);
- it falls under a regulatory regime (EU AI Act, sector rules);
- intake or approval delays are pushing teams to alternatives.

## Boundaries

- **B14** covers value that never arrives for reasons other than governance. B15 covers value lost because of governance, too much or too little.
- **B3** is the symptom; disproportionate governance is one of its causes.

## Levers

| Lever | Type | Owner |
|---|---|---|
| Tiered governance with a fast lane, so effort matches stakes | Directive | CRO |
| Measure and report assessment time and cost per tier | Detective | Program owner |
| Fund governance as an enabler, with a link to the value it protects | Directive | CFO |
| Track regulatory deadlines that touch AI use cases | Detective | General Counsel (consulted) |
| Internal audit of register completeness and decision quality | Detective | Internal audit |
| Review fast-lane patterns every six months | Corrective | Program owner |

## Signs governance is disproportionate

- Fast-lane candidates wait more than a few days.
- Low tier use cases receive red-team engagements.
- Allocated governance cost exceeds the 90th percentile of risk-adjusted value for a use case that is not High tier.
- Shadow-AI discovery rises after a new approval process is introduced.

## Quantification notes

- The governance term is estimated in [Layer 8](../layers/L8-governance-cost.md).
- If an organization believes a control investment raises P(production), it can model that explicitly in Layer 7. This is an assumption, not a measured effect; record it as such.

## Example scenario statement

> Our current approval process adds a median of six weeks before any AI use case can go live. We estimate this pushes 20% to 40% of demand to unsanctioned tools (raising B3) and delays $0.5 million to $2 million of risk-adjusted value a year across the portfolio.

## Questions for the accountable executive

1. How long does it take to get a low-risk AI use case approved?
2. Is our governance effort concentrated on the use cases that matter most?
3. Which regulatory deadlines in the next 12 months touch our AI use cases, and who owns each?

## Crosswalk

| Framework | Reference |
|---|---|
| MIT AI Risk Repository | 6.5 Governance failure |
| NIST AI RMF | GOVERN function |
| ISO/IEC 42001 | Clauses 5 (leadership), 6.1 (risks and opportunities), 9 (performance evaluation) |
| CSA AICM | GRC, A&A |
| Gartner | AI technical debt and TCO among GenAI blind spots (as a theme) |

## Open questions

- Does governance spend measurably raise P(production) or P(value | production)? This is the key empirical question for B15.
