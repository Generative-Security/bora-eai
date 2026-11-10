# B2: Sanctioned-AI leakage

| | |
|---|---|
| **Accountable** | CIO (platform owner) |
| **Consulted** | CISO |
| **Lens** | Internal (and customer-facing where the AI retrieves customer data) |
| **Loss domain** | Cybersecurity and privacy; regulatory and compliance |
| **Party** | First-party and third-party |
| **Status** | Draft v0.1 |

## Business outcome

An approved copilot or retrieval system exposes overshared or privileged data to employees who should not see it, or, through content an attacker plants, to people outside the organization.

## Applies when

- A sanctioned AI tool retrieves from shared repositories, mailboxes, chat, tickets, or document stores.
- Permissions in those sources have grown beyond job need, or sensitive content is unlabeled.
- Retrieval mixes untrusted content (inbound email, web pages, uploaded files) with privileged internal data.
- Regulated personal data is reachable (this also triggers the Medium override).

## What it looks like

- **Oversharing made visible:** a copilot answers a question by quoting a salary file, board paper, or HR investigation that sat on a site with broad access. The access problem existed before; the AI made it searchable in plain language.
- **Indirect prompt injection:** an attacker plants instructions in content the AI will later retrieve (an email, a document, a web page). When a user asks an ordinary question, the AI follows the planted instructions and sends internal data out.
- **Over-scoped connectors:** a sanctioned AI application is connected to more systems than its use case needs.

## Boundaries

- **B1** is a person or their agent deliberately extending their reach. B2 is the platform exposing data regardless of intent.
- **B3** is data leaving to unsanctioned services. B2 is exposure through a sanctioned one.
- **B9** is the customer-facing equivalent when the exploit targets a bot. Use B2 for internal assistants, B9 for customer-facing ones.

## Evidence

- **EchoLeak (CVE-2025-32711, CVSS 9.3).** Discovered by Aim Security and fixed by Microsoft in June 2025. An attacker emailed a hidden prompt; when the user later asked Microsoft 365 Copilot a business question, retrieval mixed the untrusted email with privileged data and Copilot leaked it, with no click required. Microsoft described it as "AI command injection in M365 Copilot allows an unauthorized attacker to disclose information over a network". There was no evidence of exploitation in the wild `[secondary]` ([The Hacker News](https://thehackernews.com/2025/06/zero-click-ai-vulnerability-exposes.html)).
- **IBM Cost of a Data Breach 2025:** 13% of organizations reported breaches of AI models or applications; 97% of those lacked AI access controls; 60% of AI-related incidents led to compromised data `[survey]` ([IBM](https://newsroom.ibm.com/2025-07-30-ibm-report-13-of-organizations-reported-breaches-of-ai-models-or-applications,-97-of-which-reported-lacking-proper-ai-access-controls)).
- **Adoption:** Netskope 2026 found Microsoft 365 Copilot in use at 52% of organizations it monitors `[vendor]`.
- **Gap:** we found no public, quantified loss from a real-world copilot oversharing incident. Evidence is from research disclosures and surveys.

## Business impact

| Loss form | Examples |
|---|---|
| Fines and judgments | Privacy breach notification and penalties where personal data is exposed |
| Response | Investigation, permission remediation at scale, rollout pause |
| Competitive advantage | Strategy, pricing, or deal information exposed externally |
| Productivity | Copilot rollout paused or reversed while permissions are fixed |

## Levers

| Lever | Type | Owner |
|---|---|---|
| Permission hygiene and access review on sources *before* rollout | Preventive | CIO |
| Sensitivity labeling, with AI retrieval honoring labels | Preventive | CIO with DPO |
| Limit connectors to what the use case needs | Preventive | CIO |
| Separate untrusted inbound content from privileged retrieval where the platform allows | Preventive | CIO with CISO |
| Prompt-injection testing for retrieval-based assistants | Detective | CISO |
| Staged rollout by population, starting where data is cleanest | Preventive | CIO |

## Quantification notes

- **Frequency:** internal oversharing findings during pre-rollout access reviews are the best leading indicator. External exploitation via injection is currently a lower-frequency, research-driven risk.
- **Magnitude:** breach-cost benchmarks apply where personal data leaves; IBM's 2025 US average was US$10.22 million `[survey]`. Internal-only oversharing is usually response and remediation cost.

## Example scenario statement

> There is a 15% to 35% probability in the next 12 months that the all-staff copilot surfaces regulated personal data or board-confidential material to unauthorized employees, producing a first-party loss of $100,000 to $800,000 in response and remediation, and a 2% to 5% probability that injected content causes external disclosure with a combined loss of $1 million to $8 million.

## Questions for the accountable executive

1. Did we fix access before we made it searchable?
2. Can untrusted content (inbound email, shared files from outside) influence what our copilot does with internal data?
3. Which connectors does each AI application have, and does it need all of them?

## Crosswalk

| Framework | Reference |
|---|---|
| Huwyler taxonomy | Privacy: Sensitive Data Leakage, Personal Data Leakage; Misuse: Prompt Injection |
| OWASP LLM 2025 | LLM01 Prompt Injection; LLM02 Sensitive Information Disclosure; LLM08 Vector and Embedding Weaknesses |
| OWASP Agentic 2026 | ASI01 Agent Goal Hijack; ASI06 Memory and Context Poisoning |
| MITRE ATLAS | AML.T0051 LLM Prompt Injection; AML.T0057 LLM Data Leakage |
| MIT AI Risk Repository | 2.1 Compromise of privacy; 2.2 AI system security vulnerabilities and attacks |
| NIST AI 600-1 | Data Privacy; Information Security |
| CSA AICM | DSP, IAM, AIS, MDS |

## Open questions

- Should pre-rollout permission remediation be counted as governance cost (Layer 8) or as part of the use case's own build cost?
