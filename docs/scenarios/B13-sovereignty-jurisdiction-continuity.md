# B13: Sovereignty, jurisdiction, continuity

| | |
|---|---|
| **Accountable** | CRO |
| **Consulted** | General Counsel, CIO |
| **Lens** | Both |
| **Loss domain** | Regulatory and compliance; operational |
| **Party** | First-party and third-party |
| **Status** | Draft v0.1 |

## Business outcome

Data used by an AI use case is processed or stored outside the jurisdictions the organization's obligations permit, is compelled by a foreign authority, or the organization loses access to the AI it depends on through suspension, deprecation, policy, or law.

## Applies when

- Inference or storage happens outside the organization's permitted jurisdictions, or on "global" routing.
- Regulated personal data, government data, or data under sector rules (for example, APRA-regulated entities) is involved.
- The provider or any of its upstream providers is subject to foreign compelled-access law.
- A business process depends on a single provider or model with no fallback.
- Provider abuse-monitoring stores or human review apply to the use case.

## What it looks like

- A managed AI platform is configured on global routing for capacity, sending prompts outside the country.
- A SaaS assistant advertises in-country storage, but inference runs elsewhere.
- Flagged prompts are retained for review by provider staff in another jurisdiction.
- A provider suspends an account under its usage policy, or deprecates the model a process is built on.
- A change in export controls or foreign law affects access to a model or region.

The six axes of the [sovereignty profile](../layers/L3-sovereignty-profile.md) (inference location, data at rest, plaintext access, key custody, legal reach, continuity and portability) are the inputs to this scenario.

## Boundaries

- **B6** covers a vendor's compromise or failure cascading through integrations. B13 covers jurisdiction, legal reach, and loss of access. A single-provider dependency raises both.
- **B7** covers a vendor's AI changes in software already owned. Where such a change also adds an overseas sub-processor, record the sovereignty consequence here.

## Evidence

Provider facts as of November 2026 `[vendor documentation; see the reference page for sources and dates]`:

- **Global routing removes residency.** Amazon Bedrock's global cross-region inference "can route to any supported AWS commercial Region worldwide". Azure OpenAI's Global deployments process data "in any geography where the model is deployed". Google's Vertex global endpoints "don't provide regional isolation or data residency guarantees".
- **In-country options differ by provider and model.** Bedrock offers an Australian geographic profile (Sydney and Melbourne). Anthropic's first-party API offered only US or global inference, with storage at rest in the US. OpenAI offered Australian storage at rest for new ChatGPT Enterprise and Edu workspaces from November 2025. Microsoft moved its Microsoft 365 Copilot in-country inferencing target for Australia to the end of 2026.
- **Abuse monitoring is a plaintext-access path.** Azure stores flagged content for review by authorized Microsoft staff unless the customer is approved for modified abuse monitoring.
- **Legal reach.** Every frontier model provider and hyperscaler is US-headquartered. The Australia–US CLOUD Act Agreement prohibits the US from targeting Australian persons under that agreement, which narrows but does not remove exposure `[government]`. FISA Section 702 lapsed on 12 June 2026 with collection continuing under existing certifications `[secondary]`; its status after mid-2026 should be checked before use.
- **Regulation.** APRA treats AI under existing standards; CPS 230 applies to all service providers from 1 July 2026 `[secondary]`. Australian privacy policies must disclose automated decisions from 10 December 2026 `[secondary]`.
- **Continuity.** The US AI Diffusion Rule, which would have controlled model-weight exports, was rescinded in May 2025 `[secondary]`. Azure documents that "severe or recurring abuse may still lead to access limits". Gartner predicts that by 2028, 65% of governments will introduce technological sovereignty requirements `[analyst, via secondary]`.
- **Gap:** we found no public quantified loss from an AI sovereignty breach.

## Business impact

| Loss form | Examples |
|---|---|
| Fines and judgments | Unlawful cross-border transfer; breach of sector data rules |
| Response | Regulator engagement; re-architecture to in-country deployment |
| Productivity | Process stopped by suspension or deprecation |
| Replacement | Migrating to another provider or model |
| Reputation | Customers or government clients losing confidence in data handling |

## Levers

| Lever | Type | Owner |
|---|---|---|
| Choose the deployment model and region deliberately per use case | Preventive | CRO with CIO |
| Enforce region and routing with preventive controls (AWS service control policies, Azure Policy, Google Cloud organization policies), not only procurement statements | Preventive | CIO |
| Apply for zero-data-retention or modified abuse monitoring where data warrants it | Preventive | CIO with DPO |
| Customer-managed keys for stored data | Preventive | CIO |
| Exit plan and tested fallback model for critical processes | Corrective | CRO |
| Track provider terms and residency options at each review | Detective | Procurement |
| Legal assessment of foreign compelled-access exposure for sensitive data | Directive | General Counsel |

## Quantification notes

- **Frequency:** configuration drift (global routing switched on) is common and detectable; regulatory enforcement is rarer. Estimate both.
- **Magnitude:** regulatory exposure scales with data sensitivity and jurisdiction. Continuity losses use business-interruption benchmarks plus migration cost.
- Some sovereignty exposure is better recorded qualitatively (for example, government-client confidence).

## Example scenario statement

> There is a 10% to 25% probability in the next 12 months that the claims-triage assistant processes regulated personal data outside Australia through global routing, producing a loss of $100,000 to $1.5 million in regulatory, re-architecture, and client-remediation costs.

## Questions for the accountable executive

1. For each AI use case touching sensitive data, where is it actually processed, and is that enforced or just configured?
2. Who outside the organization can read our prompts, including provider reviewers?
3. If our main AI provider suspended us tomorrow, what would stop?

## Crosswalk

| Framework | Reference |
|---|---|
| Huwyler taxonomy | No fit (gap) |
| AWS GenAI Scoping Matrix | All scopes (residency differs by scope) |
| CSA AICM | DSP, CEK, IPY, BCR, STA |
| MIT AI Risk Repository | 2.1 Compromise of privacy; 6.1 Power centralization |
| NIST AI 600-1 | Data Privacy; Value Chain and Component Integration |
| APRA | CPS 230; CPS 234 |
| Australian Privacy Act | Cross-border disclosure; automated-decision disclosure (from 10 December 2026) |

## Open questions

- Is there an industry framework (CSA, ENISA, EU Cloud Sovereignty Framework, ASD) that maps sovereignty by AI deployment model that we missed?
