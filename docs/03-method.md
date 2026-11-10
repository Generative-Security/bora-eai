# Method

This page describes how to run BORA-EAI, first as a program and then for a single use case.

## Setting up the program

Before assessing individual use cases, an organization needs five things in place. Most can be done in a few weeks.

| Step | What | Who | Output |
|---|---|---|---|
| 1 | Name the **AI risk program owner**. In most organizations this sits with the CISO or CRO. | CEO or executive committee | A named owner with authority to run the register and convene reviews |
| 2 | Confirm the **accountable executives** for each scenario, using the default [owner matrix](04-accountability.md#scenario-owner-matrix) and adjusting titles to your organization. | Program owner, with each executive | An agreed owner matrix |
| 3 | Set **risk appetite** for AI in the terms the board already uses (see [Layer 9](layers/L9-erm-fit-and-completeness.md)). | CRO and board risk committee | Appetite statements and escalation thresholds |
| 4 | Define **fast-lane patterns**: the pre-approved combinations of tool, data class, and agency that can be registered without assessment. | Program owner, CIO, CISO, DPO | A [fast-lane pattern list](../templates/fast-lane-patterns.md) |
| 5 | Build the **first inventory**, including sanctioned tools, AI features already active in purchased software, and known shadow use. | Program owner, CIO, Procurement | A [use-case register](../templates/use-case-register.csv) |

## Running a single use case

Each use case moves through the nine layers in order. Layers 1 to 4 are fast for every use case and decide how much of layers 5 to 8 is needed.

```
Intake ─► L1 Inventory ─► L2 Ownership ─► L3 Sovereignty ─► L4 Agency & tier
                                                                 │
                    ┌──────────── Fast lane: register and stop ◄─┤
                    │                                            ▼
                    │           L5 Scenarios ─► L6 Loss ─► L7 Value ─► L8 Governance cost
                    │                                                        │
                    └────────────────────────────► L9 ERM fit & completeness ◄┘
                                                             │
                                                     Decision and review date
```

### Step by step

1. **Intake (Layer 1).** Record the use case in the register: business owner, line of business, [COSO capability type](layers/L1-use-case-inventory.md#capability-types), users, data classes, and whether it is internal or customer-facing. This selects the [lens](lenses/README.md).
2. **Consumption and ownership (Layer 2).** Assign the [consumption scope](layers/L2-consumption-and-ownership.md#consumption-scopes) (1, 2, 2e, 3, 4, or 5), map the supply chain to the CSA shared-responsibility roles, and name the one executive accountable for the use case's net position.
3. **Sovereignty profile (Layer 3).** Complete the six-axis [sovereignty profile](layers/L3-sovereignty-profile.md). For a fast-lane candidate this is a check that the pattern's approved deployment is the one actually in use.
4. **Agency and tier (Layer 4).** Assign the agentic scope and the CBRA dimensions, apply the override rules, and decide: fast lane, Low, Medium, or High.
   - **Fast lane:** register, set a review date, stop.
   - **Low:** go to step 5 but screen qualitatively only.
   - **Medium or High:** go to step 5 with quantification.
5. **Business threat scenarios (Layer 5).** Screen all fifteen scenarios. For each that applies, write a scenario statement in the FAIR-AIR form and note the accountable owner. For Medium, select the top three by likely impact; for High, take all that apply.
6. **Loss (Layer 6).** For Medium and High, estimate frequency and magnitude ranges per selected scenario, classify each loss as first-party or third-party, and note which insurance line, if any, responds.
7. **Value (Layer 7).** Estimate gross annual value as a range, and the probabilities of reaching production and delivering once there. Record the cost of delay.
8. **Governance cost (Layer 8).** Allocate the governance cost this use case drives, including assessments, controls, monitoring, and compliance work.
9. **ERM fit and completeness (Layer 9).** Combine the terms into the [net position](06-quantification.md), compare against risk appetite, run the completeness check against the MIT AI Risk Repository domains, and record the decision.

### Outputs

Every assessed use case produces:

- a row in the **use-case register**, with tier, lens, owner, decision, and review date;
- a **scenario register** entry for each applicable scenario, with its accountable owner;
- for Medium and High, the **net position** as a distribution (10th, 50th, 90th percentile), the probability it is negative, and a 1-in-20-year loss per quantified scenario;
- a **sovereignty profile**;
- a **decision**: approve, approve with conditions, redesign, defer, or stop.

The [use-case assessment template](../templates/use-case-assessment.md) covers all of these in one document.

## Decisions

BORA-EAI informs a decision; it does not make it. Typical outcomes:

| Decision | When |
|---|---|
| **Approve** | Net position is positive across most of the range, and no scenario's tail loss breaches appetite. |
| **Approve with conditions** | Positive, but one or more scenarios need controls before or soon after launch (for example, hard limits on what a bot may offer, before B10 can be accepted). |
| **Redesign** | A change in scope, agency, data access, or deployment model would move the use case to a lower tier or remove a scenario. This is often the most valuable outcome. |
| **Defer** | Value is plausible but uncertain, and a cheap pilot would narrow the range. Treat the pilot as an option with a defined exit. |
| **Stop** | Net position is negative across most of the range, or a tail loss breaches appetite and cannot be treated. |

A stop decision is recorded with its cost of delay. Not deploying is a cost, and the register should show it.

## Cadence

| Activity | Frequency |
|---|---|
| Fast-lane registrations | Continuous |
| Low tier screens | At intake, then annually |
| Medium and High assessments | At intake, at each material change, and at least annually |
| Inventory sweep for shadow AI and newly enabled vendor features | Quarterly |
| Portfolio review with accountable executives | Quarterly |
| Board reporting | At least twice a year, plus any High tier approval |
| Fast-lane pattern review | Every six months |

**Material changes** that trigger reassessment include: a new model or provider, a change in consumption scope or agentic scope, new data classes, a move from internal to customer-facing, a provider terms change affecting training or residency, and any incident in the use case's scenarios.

## Integrating with what you already run

- **ISO/IEC 42001:** BORA-EAI can serve as the AI risk assessment (clause 6.1.2) and feeds the AI system impact assessment (clause 6.1.4). See the [crosswalk](reference/framework-crosswalk.md).
- **Enterprise risk register:** each accountable executive's scenarios roll up into the categories your ERM already uses. See [Layer 9](layers/L9-erm-fit-and-completeness.md).
- **Third-party risk management:** Layer 2 and scenarios B6 and B7 feed vendor due diligence and contract reviews.
- **Technical threat modeling:** for Medium and High use cases, the security team decomposes each applicable scenario with STRIDE, MITRE ATLAS, MAESTRO, or the OWASP lists, using the crosswalk on each scenario page.

Next: [Accountability](04-accountability.md)
