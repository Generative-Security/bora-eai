# B7: Vendor-enabled embedded AI

| | |
|---|---|
| **Accountable** | General Counsel |
| **Consulted** | DPO, Procurement |
| **Lens** | Internal |
| **Loss domain** | Regulatory and compliance; IP |
| **Party** | First-party and third-party |
| **Status** | Draft v0.1 |

## Business outcome

A vendor of software the organization already uses switches on AI features, changes its terms to permit training on customer content, or adds a model provider as a sub-processor, putting the organization into processing it never approved.

## Applies when

- Consumption Scope 2e: AI arrives inside software bought for another purpose.
- Contracts predate the vendor's AI features, or allow unilateral changes to terms.
- AI features are on by default, or can be enabled by individual users or admins without central review.
- The organization is a controller of personal data processed by the vendor.

## What it looks like

- A meeting, collaboration, or file-transfer service updates its terms in a way that permits AI training on customer content.
- A SaaS platform adds a summarization or assistant feature that sends content to a third-party model provider.
- A vendor adds a model provider to its sub-processor list with notice buried in a release note.

## Boundaries

- **B6** is about a vendor being compromised or failing. B7 is about a vendor doing what it chose to do.
- **B5** covers the IP consequences if customer content is used for training. B7 covers the contractual and data-protection exposure of the change itself.
- **B3** covers employees choosing unsanctioned tools. In B7 the tool was sanctioned; its AI was not.

## Evidence

The recurring pattern is a terms change, public backlash, and clarification or reversal:

- **Zoom (2023):** terms changes rolled out in March 2023 were flagged in August 2023 as allowing use of customer content for AI training without opt-out. On 7 August 2023, Zoom updated its terms to state it would not use audio, video, or chat customer content to train its AI models without consent `[secondary]` ([Engadget](https://www.engadget.com/zoom-reverses-policy-that-allowed-it-to-train-ai-on-customer-data-212230598.html)).
- **Adobe (June 2024):** clarified new terms of service after concerns about AI training `[secondary]`.
- **WeTransfer (July 2025):** removed an AI clause from its terms after user backlash `[secondary]` ([The Next Web](https://thenextweb.com/news/how-wetransfer-reignited-fears-about-training-ai-on-user-data)).
- **Scale:** Netskope tracked more than 1,600 GenAI applications in 2026, up from 317, including AI embedded in broader SaaS `[vendor]`.

In each case, customers learned of the change from press coverage rather than contractual notice, and the reversal was driven by backlash rather than regulation. We found no regulator action specifically about a SaaS vendor turning on AI for business customers, and no quantified business loss for this scenario.

## Business impact

| Loss form | Examples |
|---|---|
| Fines and judgments | Processing personal data without a lawful basis or approved sub-processor |
| Competitive advantage | Proprietary content used to train a vendor's model |
| Response | Legal review, contract renegotiation, client notifications |
| Reputation | Clients learning their confidential material was processed by a new AI provider |

Professional services firms face added exposure: client confidentiality and privilege obligations may be breached by an AI feature the firm never chose.

## Levers

| Lever | Type | Owner |
|---|---|---|
| Contract terms: no training on customer content without consent; advance notice of AI features and sub-processor changes; right to disable | Preventive | General Counsel with Procurement |
| Tenant-level control of AI features, off by default until reviewed | Preventive | CIO |
| Monitor vendor terms, release notes, and sub-processor lists | Detective | Procurement |
| Privacy impact assessment when an AI feature is enabled | Directive | DPO |
| SaaS security posture monitoring for AI feature enablement | Detective | CISO |
| Include AI-enabled vendor features in the quarterly inventory sweep | Detective | Program owner |

## Quantification notes

- **Frequency:** high and rising; most large SaaS portfolios will see several AI feature launches a year. The loss frequency is lower and poorly measured.
- **Magnitude:** mostly regulatory and contractual. Scale by the sensitivity of data in the affected application and by client confidentiality obligations.

## Example scenario statement

> There is a 20% to 50% probability in the next 12 months that a vendor in our SaaS portfolio enables an AI feature that sends client documents to an unapproved model provider, producing a loss of $50,000 to $750,000 in legal, remediation, and client-relationship costs.

## Questions for the accountable executive

1. Do our contracts let vendors add AI features, or train on our content, without our consent?
2. Who in the organization can switch on a vendor's AI feature today?
3. How would we find out that a vendor added a new model provider as a sub-processor?

## Crosswalk

| Framework | Reference |
|---|---|
| Huwyler taxonomy | No clean fit (gap); nearest is Supply Chain: Insecure Data Feeds/APIs |
| AWS GenAI Scoping Matrix | Scope 2, extended by BORA-EAI as Scope 2e |
| MIT AI Risk Repository | 2.1 Compromise of privacy; 6.5 Governance failure |
| NIST AI 600-1 | Data Privacy; Intellectual Property; Value Chain and Component Integration |
| CSA AICM | STA, DSP, GRC |
| ISO/IEC 42001 | Annex A supplier controls |

## Open questions

- Is there a sector (for example, legal or health) where regulators have acted on vendor-enabled AI that we have missed?
