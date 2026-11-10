# B3: Shadow-AI leakage

| | |
|---|---|
| **Accountable** | CISO |
| **Consulted** | CIO, Procurement |
| **Lens** | Internal |
| **Loss domain** | Cybersecurity and privacy; regulatory and compliance; IP |
| **Party** | First-party and third-party |
| **Status** | Draft v0.1 |

## Business outcome

Employees send company data to AI services the organization has not approved, so it reaches providers with no contract, no data processing agreement, no agreed retention or training terms, and no duty to notify the organization of a breach.

## Applies when

- Employees can reach consumer AI services from work devices or with work data.
- Sanctioned alternatives are missing, slower, or less capable than consumer tools.
- Data-loss tooling does not inspect AI destinations or browser extensions.
- Approval processes for new AI tools take longer than employees will wait.

## What it looks like

- Pasting source code, contracts, customer records, or financials into a consumer chatbot under a personal account.
- Using a free transcription, translation, or summarization service on confidential meetings or documents.
- Browser extensions that read page content and send it to an AI service.

## Boundaries

- **B2** is exposure through a sanctioned tool. B3 is exposure through an unsanctioned one.
- **B4** covers what employees install that executes code (models, MCP servers, agent skills). B3 covers where data goes. An unsanctioned extension that both reads data and executes code can be both.
- **B1** is about scale of access. A single negligent paste is usually best recorded as B3.

## Evidence

- **IBM Cost of a Data Breach 2025:** one in five organizations reported a breach due to shadow AI. Organizations with high shadow-AI use averaged US$670,000 more in breach costs. Shadow-AI incidents compromised personal data in 65% of cases and IP in 40%. Only 37% of organizations had policies to manage AI or detect shadow AI `[survey]` ([IBM](https://newsroom.ibm.com/2025-07-30-ibm-report-13-of-organizations-reported-breaches-of-ai-models-or-applications,-97-of-which-reported-lacking-proper-ai-access-controls)).
- **Netskope Cloud and Threat Report 2026:** GenAI data-policy violations doubled year on year to about 223 per organization per month (about 2,100 in the top quartile). Source code was 42% of violations, regulated data 32%, IP 16%. The share of AI users on personal accounts fell from 78% to 47% as managed accounts rose from 25% to 62% `[vendor]` ([Netskope](https://threatlabs.netskope.com/reports/2026/cloud-and-threat-report-2026)).
- **Verizon 2026 Data Breach Investigations Report,** as summarized: 67% of employees accessed AI from non-corporate accounts on corporate devices; 15% ran unauthorized AI browser extensions that collect browsing context `[secondary; primary report not checked]`.
- **Gartner (reported November 2025):** 69% of 302 cybersecurity leaders surveyed suspected or had evidence of prohibited public GenAI use; Gartner predicts more than 40% of enterprises will have shadow-AI security or compliance incidents by 2030 `[analyst, via secondary]`.

Netskope and Verizon measure different populations (share of AI users versus share of employees), so their personal-account figures are not directly comparable.

## Business impact

| Loss form | Examples |
|---|---|
| Fines and judgments | Personal data disclosed to an unapproved overseas processor; cross-border transfer breaches |
| Competitive advantage | Source code and IP in a provider's logs or training data |
| Response | Investigation with no audit trail; legal review of provider terms |
| Reputation | Disclosure that customer data went to a consumer AI service |

The distinctive cost of shadow AI is **loss of visibility**: no contract, no logs, and no forensic trail when something goes wrong.

## Levers

| Lever | Type | Owner |
|---|---|---|
| Sanctioned alternatives that are as easy and capable as consumer tools | Preventive | CIO (consulted) |
| Fast lane so approved use is faster than shadow use | Preventive | Program owner |
| Discovery: network, SaaS, browser, and endpoint telemetry for AI destinations | Detective | CISO |
| Data-loss controls on AI destinations, prioritizing source code and regulated data | Preventive | CISO |
| Blocking high-risk services and extensions, paired with an alternative | Preventive | CISO |
| Procurement path for new AI tools with standard AI terms | Preventive | Procurement |

Blocking without an alternative tends to push use further underground. Netskope's data suggests that offering managed accounts moves use onto them.

## Quantification notes

- **Frequency:** high. Use internal data-loss telemetry as the base. Treat the probability of at least one shadow-AI exposure of sensitive data in a year as close to certain for most large organizations; the question is magnitude.
- **Magnitude:** IBM's US$670,000 shadow-AI premium is a useful anchor for breach scenarios. For IP exposure, estimate the value of the affected code or material.

## Example scenario statement

> There is a 60% to 90% probability in the next 12 months that staff send regulated customer data to an unsanctioned AI service, producing a combined first- and third-party loss of $50,000 to $1.5 million in response, regulatory, and notification costs.

## Questions for the accountable executive

1. Do we know which AI services our people use, and with what data?
2. Is the approved path faster and better than the unapproved one?
3. If customer data went to a consumer AI service last month, could we prove what was sent?

## Crosswalk

| Framework | Reference |
|---|---|
| Huwyler taxonomy | Misuse: Shadow AI Usage; Privacy: Personal Data Leakage, Sensitive Data Leakage |
| FAIR-AIR vectors | Shadow GenAI |
| OWASP LLM 2025 | LLM02 Sensitive Information Disclosure |
| MIT AI Risk Repository | 2.1 Compromise of privacy; 6.5 Governance failure |
| NIST AI 600-1 | Data Privacy; Information Security; Intellectual Property |
| CSA AICM | DSP, UEM, STA, GRC |

## Open questions

- How should the value employees get from shadow use be credited in B14, when the organization decides whether to sanction a tool?
