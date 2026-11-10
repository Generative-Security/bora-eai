# Layer 8: Governance cost

> **Executive question:** What does controlling it cost?

## Purpose

Governance is not free, and a model that ignores its cost will either over-control low-value use cases or under-fund high-risk ones. Layer 8 estimates the governance cost each use case drives, so it can be netted against value and expected loss. We found no published AI risk framework that includes governance cost as a model term; Gartner names cost and technical debt as executive concerns, but as themes rather than a structured input.

## What to include

| Cost category | Examples | Fixed or per use case |
|---|---|---|
| **Program** | AI governance owner and team, committee time, policy, training, register tooling | Fixed; allocate across use cases |
| **Assessment** | BORA-EAI assessment effort, privacy and AI impact assessments, legal review | Per use case, scaled by tier |
| **Assurance** | Red teaming, security testing, model evaluation, independent validation | Per use case, mostly Medium and High |
| **Controls** | Guardrails, data-loss prevention, monitoring, logging, gateway or proxy, human review time | Mix |
| **Compliance** | Certification (for example, ISO/IEC 42001), EU AI Act conformity work, regulatory reporting | Mix |
| **Contracting** | Negotiating AI terms, indemnities, residency commitments | Per vendor |
| **Ongoing** | Monitoring, periodic reassessment, incident handling | Per use case, annual |

## Allocation

Allocate fixed program costs across use cases in proportion to tier, so that fast-lane and Low tier use cases carry a small share and High tier use cases a large one. A simple default weighting is fast lane 0.1, Low 1, Medium 4, High 12. These weights are our assumption and should be replaced with measured effort once available.

Count only the **incremental** cost a use case drives. Controls that already exist for other reasons (for example, enterprise data-loss prevention) should be allocated, not counted in full.

## Reference costs

Hard governance-cost data is scarce. What exists `[labels as shown]`:

| Item | Range | Evidence |
|---|---|---|
| ISO/IEC 42001 certification, 1 to 50 staff | £8,000 to £15,000 | `[vendor]` ISMS.online |
| ISO/IEC 42001 certification, 51 to 250 staff | £15,000 to £30,000 | `[vendor]` |
| ISO/IEC 42001 certification, 250+ staff | £30,000 to £50,000+ | `[vendor]` |
| ISO/IEC 42001 surveillance audits | £1,500 to £5,000 a year | `[vendor]` |
| EU AI Act compliance per high-risk system | about €6,000 to €7,000 (Commission) to about €29,000 a year (supporting study) | `[government]`, 2021 estimates on the draft text |
| EU AI Act quality management system setup, where none exists | about €193,000 to €330,000 | `[consulting]` CEPS 2021 |
| EU AI Act, economy-wide | €31 billion over five years | `[think tank]` ITIF 2021, disputed by CEPS |

All EU figures predate the final 2024 text and the 2026 Digital Omnibus amendments. Use them only as orders of magnitude. People cost, probably the largest line, has no reliable public benchmark; the IAPP's 2025 survey found 77% of organizations working on AI governance but we could not verify its budget figures. There is no reliable public pricing for AI red teaming. See [Governance cost evidence](../reference/governance-cost-evidence.md).

## Governance can create value

Both Gartner predictions on abandoned AI projects name inadequate risk controls as a cause `[analyst]`, and BCG's 2026 survey found only 5% of companies had the full set of controls in place for the agentic autonomy many expect to grant by 2030 `[consulting]`. Good governance plausibly raises P(production) and P(value | production), not only lowers loss. BORA-EAI lets an organization model that explicitly: if a control investment is expected to raise P(production), show it in Layer 7. This is a modeling assumption, not a measured effect, and the [validation plan](../validation/validation-plan.md) lists it as something to test.

## Proportionality

Governance cost should scale with stakes. Signs it does not:

- fast-lane candidates waiting weeks for approval;
- Low tier use cases receiving red-team engagements;
- governance cost exceeding the 90th percentile of risk-adjusted value for a use case that is not High tier;
- teams routing around the process (watch B3).

These are the symptoms of scenario [B15](../scenarios/B15-governance-cost-and-failure.md).

## Output

An allocated governance cost range per use case, split into one-off and annual. This feeds the governance term of the [net position](../06-quantification.md).

Next: [Layer 9: ERM fit and completeness](L9-erm-fit-and-completeness.md)
