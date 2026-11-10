# Accountability

BORA-EAI assigns accountability at two levels, and each has exactly one owner.

## Two kinds of accountability

| Level | Who | Accountable for |
|---|---|---|
| **Use case** | One executive, usually the business sponsor | The use case's **net position**: that its value justifies its expected loss and governance cost, and that it stays within risk appetite |
| **Scenario** | One executive per scenario, across all use cases | The **control lever** that prevents that scenario's loss, wherever it appears in the portfolio |

A customer-service chatbot, for example, has one accountable executive for the use case (the head of customer service, who sponsors it). Within it, B8 (misrepresentation liability) is controlled by the channel owner, B9 (technical compromise) by the CISO, and B13 (sovereignty) by the CRO. The use-case owner answers for the overall decision; each scenario owner answers for their lever.

## The rule for choosing a scenario owner

> The accountable executive is the one who holds the main lever that prevents the loss. Other functions are consulted.

This follows the RACI convention of a single "A". Shared accountability, where two or three executives co-own a risk, tends to produce committee paralysis while a decision is pending and finger-pointing once an incident happens.

Applying the rule sometimes gives an answer people do not expect. B8, bot misrepresentation liability, is a legal exposure, so General Counsel seems the natural owner. But General Counsel cannot control what a bot says. The channel owner decides the bot's scope, its knowledge sources, and what it is allowed to promise. So the channel owner is accountable, and General Counsel is consulted.

## Scenario owner matrix

Default titles; organizations should map them to their own structure.

| ID | Scenario | Accountable (A) | Consulted (C) | Main lever |
|---|---|---|---|---|
| B1 | Insider amplification | CISO | CHRO | Insider-risk program extended to AI and agent identities |
| B2 | Sanctioned-AI leakage | CIO (platform owner) | CISO | Permission hygiene and data labeling before and during copilot rollout |
| B3 | Shadow-AI leakage | CISO | CIO, Procurement | Detection plus a sanctioned alternative that is easier to use |
| B4 | Untrusted AI artifacts | CTO | CISO | Allow-listing, signing, and pinning of models, extensions, and agent tools |
| B5 | IP and license exposure | General Counsel | CTO, Procurement | License review, indemnity terms, and output-use policy |
| B6 | AI vendor and fourth-party concentration | CRO | CIO, Procurement | Dependency mapping, exit plans, and integration token scope |
| B7 | Vendor-enabled embedded AI | General Counsel | DPO, Procurement | Contract terms on AI features, training use, notice, and sub-processors |
| B8 | Bot misrepresentation liability | Channel owner (CX) | General Counsel | What the bot may state and promise, and its knowledge sources |
| B9 | Bot technical compromise | CISO | Channel owner | Security testing, input and output controls, tool permissions |
| B10 | Bot commercial manipulation | Channel owner (CX, Sales) | CFO | Concession limits enforced outside the model |
| B11 | Agentic execution failure | CTO | Business continuity owner | Credential scope, environment separation, spend caps, rollback |
| B12 | Agentic unauthorized commitments | CFO | General Counsel | Financial authority limits applied to agents |
| B13 | Sovereignty, jurisdiction, continuity | CRO | General Counsel, CIO | Deployment-model choice and preventive residency controls |
| B14 | Forgone and negative value | Use-case sponsor (line head) | CFO | Funding, measurement, and stop decisions |
| B15 | Governance cost and failure | CRO | CFO | Proportionate governance design and its funding |

## Responsibilities of every accountable owner

Each accountable executive, for each scenario they own:

1. Agrees the scenario statements written for their scenario in each use case.
2. Approves the frequency and magnitude ranges, or names who will.
3. Decides treatment: reduce, transfer, avoid, or accept, within risk appetite.
4. Owns the control lever and its funding.
5. Reports the scenario's portfolio position at the quarterly review.

## The program owner

Someone has to run the register, convene reviews, and translate results into ERM terms. In most organizations this is the CISO or CRO. The program owner is **not** accountable for every scenario. That distinction matters: a security team that owns every AI risk becomes the bottleneck the [fast lane](05-tiering.md#fast-lane) exists to avoid.

## Where existing roles fit

| Role | BORA-EAI responsibility |
|---|---|
| Board risk committee | Sets appetite; receives the portfolio view; approves High tier use cases above a threshold |
| AI governance committee (if one exists) | Runs the quarterly portfolio review; maintains fast-lane patterns |
| Internal audit | Tests that the register is complete and that decisions follow the method |
| DPO / privacy officer | Consulted on B2, B3, B7, B13; leads privacy impact assessments that feed Layer 3 |
| Procurement | Consulted on B3, B5, B6, B7; enforces AI terms in contracts |
| Business continuity owner | Consulted on B11; owns AI-specific recovery plans |

Next: [Tiering](05-tiering.md)
