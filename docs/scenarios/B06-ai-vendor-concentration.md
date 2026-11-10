# B6: AI vendor and fourth-party concentration

| | |
|---|---|
| **Accountable** | CRO (third-party risk) |
| **Consulted** | CIO, Procurement |
| **Lens** | Both |
| **Loss domain** | Operational; cybersecurity and privacy |
| **Party** | First-party and third-party |
| **Status** | Draft v0.1 |

## Business outcome

The compromise, failure, or change of an AI vendor, or of the upstream model provider many vendors share, cascades into the organization through integrations, tokens, and dependencies it does not control.

## Applies when

- AI applications hold integration tokens (OAuth grants, API keys, connectors) into systems of record such as CRM, email, or storage.
- Several use cases or vendors depend on the same upstream model provider or platform.
- A business process depends on one AI vendor with no fallback.
- Vendors use sub-processors the organization has not reviewed.
- The organization is regulated for operational resilience (for example, APRA CPS 230 in Australia).

## What it looks like

- **Token store compromise:** an attacker breaches an AI vendor and uses its stored integration tokens to reach customers' systems.
- **Shared upstream outage or change:** a frontier model provider has an outage, deprecates a model, or changes behavior, affecting many "wrapper" products at once.
- **Fourth-party surprise:** the organization learns that its vendor's AI feature runs on a model provider and region it never approved.

## Boundaries

- **B4** is about artifacts pulled in directly, usually without a contract. B6 is about contracted vendors and their chains.
- **B7** is about a vendor changing what its product does or what its terms allow. B6 is about a vendor failing or being compromised.
- **B13** covers jurisdiction and access suspension. Concentration on a single provider raises both; B6 owns the cascade, B13 the legal and continuity exposure.

## Evidence

- **Salesloft Drift (2025).** Salesloft's GitHub was compromised as early as March 2025; attackers then reached Drift's AWS environment and stole OAuth tokens for integrations. Between 8 and 18 August 2025, the stolen tokens were used to access customers' Salesforce instances with automated tooling that searched for AWS keys and Snowflake tokens. More than 700 organizations were affected; named victims include Palo Alto Networks, Zscaler, Cloudflare (which rotated 104 API tokens), Proofpoint, Tenable, Qualys, and others `[secondary]` ([TechTarget](https://www.techtarget.com/searchsecurity/news/366630934/News-brief-Salesloft-Drift-breach-update-and-timeline)). The breach arrived through an AI chat product, but the exposure was the token store, not the model.
- **APRA letter to industry on AI (30 April 2026),** as summarized: APRA flags vendor concentration and "wrappers" built on the same few platforms as fourth-party risk, and expects reviews of single-upstream-vendor dependencies and redundancy plans. CPS 230 applies to all contracted service providers from 1 July 2026 `[secondary: law-firm summary]` ([HWL Ebsworth](https://hwlebsworth.com.au/not-so-fast-apra-issues-ai-reminder-ahead-of-cps-230-deadline/)).
- **Gartner (reported November 2025)** lists ecosystem lock-in among five generative AI blind spots `[analyst, via secondary]`.
- **Gap:** we found no primary source quantifying business harm from a provider-side model change or deprecation.

## Business impact

| Loss form | Examples |
|---|---|
| Response | Token rotation at scale, incident investigation, customer notification |
| Fines and judgments | Breach of customer data reached through the vendor |
| Productivity | Processes stalled while a vendor is offline or disconnected |
| Reputation | Being named as a victim of a supply-chain breach |

## Levers

| Lever | Type | Owner |
|---|---|---|
| Map AI dependencies to the fourth party: which model, which provider, which region | Directive | CRO with CIO |
| Minimize integration token scope; review and expire grants | Preventive | CIO |
| Monitor for anomalous use of integration tokens | Detective | CISO |
| AI-specific vendor due diligence: token storage, sub-processors, incident notice | Preventive | Procurement |
| Exit and fallback plans for critical AI-dependent processes | Corrective | CRO |
| Avoid single-provider dependency for critical processes where feasible | Preventive | CIO |

## Quantification notes

- **Frequency:** per vendor, low; across a portfolio of AI vendors with integrations, material. Count vendors with tokens into systems of record.
- **Magnitude:** scales with what the tokens reach. For a vendor with access to CRM data, use breach-cost benchmarks; for a critical-process dependency, use business-interruption costs (Verizon 2026: median about US$90,000 per claim, highest of any category `[survey]`).

## Example scenario statement

> There is a 5% to 15% probability in the next 12 months that compromise of an AI sales-assistant vendor exposes our CRM data through its integration tokens, producing a combined loss of $300,000 to $4 million in response, notification, and regulatory costs.

## Questions for the accountable executive

1. Which AI vendors hold tokens into our systems of record, and what can those tokens do?
2. How many of our AI use cases depend on the same upstream model provider?
3. If our main AI vendor went offline for a week, which processes would stop?

## Crosswalk

| Framework | Reference |
|---|---|
| Huwyler taxonomy | Supply Chain: Insecure Data Feeds/APIs, Compromised Pre-trained Model |
| OWASP LLM 2025 | LLM03 Supply Chain |
| OWASP Agentic 2026 | ASI04 Agentic Supply Chain Vulnerabilities; ASI08 Cascading Failures |
| MITRE ATLAS | AML.T0010 AI Supply Chain Compromise |
| MIT AI Risk Repository | 2.2 AI system security vulnerabilities and attacks; 6.1 Power centralization (concentration) |
| NIST AI 600-1 | Value Chain and Component Integration; Information Security |
| CSA AICM | STA, BCR, IAM, IPY |
| APRA | CPS 230 (operational risk, service providers) |

## Open questions

- How should portfolio-level concentration (many use cases on one provider) be represented, given BORA-EAI assesses use cases one at a time?
