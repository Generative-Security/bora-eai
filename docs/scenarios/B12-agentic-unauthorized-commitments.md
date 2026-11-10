# B12: Agentic unauthorized commitments

| | |
|---|---|
| **Accountable** | CFO |
| **Consulted** | General Counsel |
| **Lens** | Both |
| **Loss domain** | Operational (financial); regulatory and compliance (legal) |
| **Party** | First-party and third-party |
| **Status** | Draft v0.1 · forward-looking |

## Business outcome

An AI agent makes payments, places orders, signs up for services, or enters contractual commitments on the company's behalf beyond its intent or authority, and the company is bound by them or must unwind them.

## Applies when

- Agents can initiate payments, purchase orders, or bookings.
- Agents hold payment credentials, corporate cards, or procurement access.
- Agents can accept terms of service, sign up for paid services, or negotiate with counterparties.
- Agents act on external marketplaces or with suppliers' agents.
- Financial authority limits for people have not been translated into limits for agents.

## What it looks like

- A procurement agent orders far more than intended because it misread a requirement.
- An agent accepts a supplier's terms, or a subscription, that no human approved.
- An agent pays a fraudulent invoice that a person would have questioned.
- An agent acting on a marketplace makes a commitment the company cannot easily reverse.

## Status of the evidence

This scenario is **forward-looking**. We found no verified public case, as of November 2026, of an enterprise agent making an unauthorized payment or commitment with a quantified loss. It is included because:

- payment networks and AI providers are building protocols for agents to transact, and practitioner commentary has focused on the liability gap when an agent "buys wrong" `[secondary]` ([Forkast](https://forkast.news/the-agentic-commerce-liability-gap-who-pays-when-the-agent-buys-wrong/));
- in Project Vend (2025), a Claude-based agent running an office shop was talked into discounts and giveaways and lost money `[secondary]`, the nearest documented analogue of an agent giving away value;
- the owner, loss type, and controls differ from B11: this is a financial-authority problem for the CFO, not an engineering problem for the CTO.

Illustrative scenarios published by payments firms (for example, a fictional agent buying €247,000 of virtual goods) are useful for tabletop exercises but are not evidence of frequency.

## Boundaries

- **B11** covers damage to the organization's own systems, data, and spend on metered services. B12 covers commitments to third parties.
- **B10** covers concessions extracted from the company's customer-facing AI by a counterparty. B12 covers the company's agent committing the company to others.

## Business impact

| Loss form | Examples |
|---|---|
| Productivity (financial) | Unwanted purchases, payments, or subscriptions |
| Fines and judgments | Contract disputes; obligations under accepted terms |
| Response | Unwinding transactions; chargebacks; supplier negotiations |
| Fines and judgments (regulatory) | Breach of payment, procurement, or sanctions rules |

## Levers

| Lever | Type | Owner |
|---|---|---|
| Translate financial delegation limits into agent limits, enforced by payment and procurement systems | Preventive | CFO |
| Separate agent payment credentials with per-transaction and periodic caps | Preventive | CFO with CISO |
| Human approval above thresholds, and for any new counterparty or new terms | Preventive | CFO |
| Prohibit agents from accepting legal terms without review | Directive | General Counsel |
| Reconciliation and anomaly detection on agent-initiated transactions | Detective | CFO |
| Contract terms with platforms and counterparties allocating liability for agent errors | Directive | General Counsel |

## Quantification notes

- **Frequency:** with no public base rate, use expert estimates tied to the agent's authority and volume, and revisit as incident data appears.
- **Magnitude:** bounded by enforced caps. Without caps, model a heavy tail.

## Example scenario statement

> There is a 3% to 10% probability in the next 12 months that the procurement agent places orders or accepts supplier terms beyond its intended authority, producing a first-party loss of $20,000 to $500,000 in unwanted commitments and unwinding costs.

## Questions for the accountable executive

1. Which agents can spend money or commit us to anything, and what are their limits?
2. Are those limits enforced by our payment and procurement systems, or only by the agent's instructions?
3. Would our delegation-of-authority policy, applied to an agent, allow what it can do today?

## Crosswalk

| Framework | Reference |
|---|---|
| OWASP LLM 2025 | LLM06 Excessive Agency |
| OWASP Agentic 2026 | ASI02 Tool Misuse and Exploitation; ASI03 Identity and Privilege Abuse; ASI09 Human-Agent Trust Exploitation (approvals obtained from humans) |
| AWS Agentic Scoping Matrix | Scopes 3 and 4 |
| MITRE ATLAS | AML.T0048 External Harms (financial) |
| MIT AI Risk Repository | 7.1 Misaligned goals (operational sense); 7.3 Lack of capability or robustness; 7.6 Multi-agent risks |
| NIST AI 600-1 | Human-AI Configuration |
| CSA AICM | IAM, GRC, LOG |

## Open questions

- What is the first credible public incident, and how should frequency be updated once it appears?
- How should liability be allocated between the organization, the agent provider, and payment networks?
