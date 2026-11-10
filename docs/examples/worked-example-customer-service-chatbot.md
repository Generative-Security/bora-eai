# Worked example: customer-service chatbot

> **Illustrative only.** The organization, figures, and estimates on this page are invented to show how the method works. They are not evidence of anything, and they are not benchmarks. Where a real benchmark informed an estimate, it is noted. All amounts are in Australian dollars.

## The use case

*Example Retail* is a fictional Australian online retailer handling about 400,000 customer-service contacts a year, at a fully loaded cost of about A$6 per contact handled by a person. It proposes an **order-help assistant** on its website and app that:

- answers questions about orders, delivery, returns, and policies;
- looks up the customer's orders and starts returns;
- issues store credit for late deliveries and minor problems.

It is built on a managed model platform, with retrieval over a policy knowledge base and tool calls into the order system.

## Layer 1: Inventory

| Field | Value |
|---|---|
| Use case | Order-help assistant |
| Accountable executive | Head of Customer Experience |
| Line of business | Customer service |
| Capability type | Human-AI interaction; posting (credits and returns written to the order system) |
| Lens | **Customer-facing** |
| Users | Customers, about 400,000 contacts a year |
| Data | Customer names, addresses, order history (regulated personal data) |
| Decisions about individuals | Store-credit decisions (low stakes) |
| Status | Proposed, after a successful pilot |

## Layer 2: Consumption and ownership

- **Scope 3** (pre-trained model with the organization's own application).
- Supply chain: cloud service provider and model provider (via the managed platform), orchestrated service (the platform's agent tooling), application (built in-house), AI customer (Example Retail).
- Integration tokens: read access to customer and order records; write access to returns and store credit.
- Contract: enterprise cloud agreement; model provider terms via the platform.
- Accountable executive confirmed: Head of Customer Experience.

## Layer 3: Sovereignty profile

| Axis | Finding |
|---|---|
| Inference location | Australian geographic profile (Sydney and Melbourne). **Gap:** nothing prevents a developer switching to global routing for capacity |
| Data at rest | Logs and knowledge base in Sydney |
| Plaintext access | Provider abuse-detection storage may apply, depending on the model |
| Key custody | Customer-managed keys for stored data |
| Legal reach | US-headquartered providers (CLOUD Act; Australia–US agreement limits targeting of Australian persons) |
| Continuity | Several models available on the platform; fallback model not yet tested |

Action: add a preventive control that blocks global routing.

## Layer 4: Agency and tier

**Agentic scope 3** (supervised): once a customer starts a conversation, the assistant looks up orders, starts returns, and issues credit without per-action approval.

Initial design: credit limits ("no more than $50, at most once per order") were written in the system prompt.

| CBRA dimension | Initial | After redesign |
|---|---|---|
| Criticality | 2 (supports service; human agents are the fallback) | 2 |
| Autonomy | 3 (issues credit without approval) | 2 (credit above $20 requires human approval, enforced by the order system) |
| Permissions | 3 (reads personal data; writes to order system) | 3 |
| Impact radius | 2 (a working manipulation script could spread to many customers) | 2 |
| **Product** | **36 → High** | **24 → Medium** |

Overrides: both apply (regulated personal data; customer-facing concessions), so the floor is Medium either way. Not eligible for the fast lane.

**Redesign decision:** move credit limits out of the prompt and into the order system (hard cap of $50 per order, one credit per order, $20 auto-approval threshold, per-customer monthly cap). This drops the use case to Medium and, as Layer 6 shows, roughly halves the chance of a negative net position.

## Layer 5: Business threat scenarios

| Scenario | Applies? | Why | Quantify? |
|---|---|---|---|
| B1 Insider amplification | No | No employee-facing retrieval | n/a |
| B2 Sanctioned-AI leakage | Partly | Internal knowledge base; covered under B9 for this customer-facing case | Screen |
| B3 Shadow-AI leakage | No | n/a | n/a |
| B4 Untrusted AI artifacts | Low | Built with approved platform components | Screen |
| B5 IP and license exposure | Low | No published output beyond conversations | Screen |
| B6 Vendor concentration | Yes | Single platform dependency | Screen |
| B7 Embedded AI | No | n/a | n/a |
| **B8 Misrepresentation liability** | **Yes** | States return and delivery policies | **Yes** |
| **B9 Technical compromise** | **Yes** | Reads customer data; calls order tools | **Yes** |
| **B10 Commercial manipulation** | **Yes** | Grants store credit | **Yes** |
| B11 Agentic execution failure | Low | Writes limited to returns and credit records | Screen |
| B12 Unauthorized commitments | Partly | Credit is covered under B10 | Screen |
| B13 Sovereignty | Yes | Personal data; routing gap | Screen (control added) |
| B14 Forgone and negative value | Always | Value term | Value term |
| B15 Governance cost and failure | Always | Governance term | Governance term |

Scenario statements for the top three (Medium tier):

- **B10:** There is a 30% to 80% (most likely 50%) probability in the next 12 months that customers persuade the assistant to grant credit outside policy, producing a first-party loss of typically A$15,000, with a heavy tail.
- **B8:** There is a 20% to 60% (most likely 40%) probability in the next 12 months that the assistant misstates a returns or delivery policy that customers rely on, producing a third-party loss of typically A$25,000 in honored claims, complaint handling, and legal review.
- **B9:** There is a 3% to 15% (most likely 8%) probability in the next 12 months that an attacker uses prompt injection or tool misuse to disclose other customers' order data, producing a loss of typically A$400,000 in response, notification, and regulatory costs, with a heavy tail.

Accountable owners: B10 and B8, Head of Customer Experience (channel owner); B9, CISO.

## Layer 6: Loss

Each scenario is simulated as: an annual probability of an event (beta-PERT over the range above), and a loss per event drawn from a lognormal distribution centered on the typical value. The B9 typical value was informed by breach-cost benchmarks, scaled down for the limited data the assistant can reach.

| Scenario | Probability of at least one event | Expected annual loss | 1-in-20-year loss | Party | Insurance |
|---|---|---|---|---|---|
| B10 (after redesign) | 52% | A$16,000 | A$71,000 | First | Not insured |
| B8 | 40% | A$23,000 | A$111,000 | Third | E&O (partial) |
| B9 | 8% | A$56,000 | A$312,000 | First and third | Cyber |
| **All three** | | **A$95,000** | **A$434,000** | | |

## Layer 7: Value

| Input | Range (low / most likely / high) | Basis |
|---|---|---|
| Gross annual value | A$350,000 / A$700,000 / A$1,100,000 | Share of 400,000 contacts fully contained, times A$6, less run cost. The customer-support uplift literature (about 14% average, more for novices) informs the human-assist share `[illustrative, informed by peer-reviewed evidence]` |
| P(production) | 0.60 / 0.75 / 0.90 | Pilot already succeeded; higher than the ~0.54 survey base rate |
| P(value \| production) | 0.30 / 0.55 / 0.80 | Containment targets are often missed; see Commonwealth Bank's 2025 reversal |

Risk-adjusted annual value: median **A$284,000** (10th to 90th percentile A$193,000 to A$402,000).

Cost of delay: about **A$71,000 per quarter** (A$48,000 to A$100,000), before any competitive erosion.

## Layer 8: Governance cost

| Item | Annualized |
|---|---|
| Share of program cost (Medium weighting) | A$20,000 |
| Pre-launch red teaming, including persuasion testing | A$35,000 |
| Monitoring and conversation review | A$25,000 |
| Privacy impact assessment and legal review | A$10,000 |
| Reassessment and evaluation runs | A$5,000 |

Range used: A$60,000 / A$90,000 / A$150,000 (mean about A$95,000).

## Layer 9: Net position and decision

Simulated with 200,000 trials (see [worked_example_simulation.py](worked_example_simulation.py)):

| | After redesign | Initial design (limits in the prompt) |
|---|---|---|
| Net annual position, 10th percentile | **−A$27,000** | −A$254,000 |
| Net annual position, median | **A$152,000** | A$120,000 |
| Net annual position, 90th percentile | **A$282,000** | A$264,000 |
| Probability net position is negative | **12%** | 23% |
| B10 1-in-20-year loss | A$71,000 | A$424,000 |

For the initial design, B10 was re-estimated with a higher event probability (50% / 70% / 90%) and a heavier, larger loss per event (typical A$40,000), reflecting limits that a working script could bypass.

**Appetite check:** Example Retail's appetite statement says no customer-facing AI may carry a single-scenario 1-in-20-year loss above A$350,000 without CRO approval, and concessions must be enforced by systems of record. The initial design breached both. After redesign, B9's tail (A$312,000) is the largest and sits inside appetite.

**Completeness check (MIT AI Risk Repository):** covered 2.1, 2.2, 3.1, 4.3, 5.1, 7.3. Considered and recorded as low for this use case: 1.1 (unfair discrimination in credit decisions, given small amounts and rule-based limits), 6.4 (competitive dynamics, noted qualitatively in cost of delay). Out of scope: 7.1, 7.2, 7.5.

**Decision: approve with conditions.**

1. Credit limits enforced in the order system before launch (B10).
2. Policy answers grounded in a single maintained source, with returns-policy questions above a value threshold routed to people (B8).
3. Red teaming for injection *and* persuasion before launch and after material changes (B9, B10).
4. Preventive control blocking global routing (B13).
5. AI disclosure in the chat interface.
6. Fallback model tested within 90 days (B6).
7. Reassess at six months with measured containment, replacing the P(value | production) estimate with real data.

## What the example shows

- The most valuable decision happened in **Layer 4**, not Layer 6: moving one limit from the prompt to the system halved the probability of a negative outcome and removed most of the B10 tail.
- **B10 and B8 need no attacker**, and a security-only review would have missed them.
- The answer is a **range**. A one-in-eight chance of losing money in the first year is a fact the accountable executive can accept or reject; a single "expected net value of A$100,000" would have hidden it.
- **Not deploying costs about A$71,000 a quarter.** That belongs in the decision too.

## Templates used

- [Use-case assessment](../../templates/use-case-assessment.md)
- [Sovereignty profile](../../templates/sovereignty-profile.md)
- [Board summary](../../templates/board-summary.md)
