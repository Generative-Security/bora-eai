# B1: Insider amplification

| | |
|---|---|
| **Accountable** | CISO |
| **Consulted** | CHRO |
| **Lens** | Internal |
| **Loss domain** | Cybersecurity and privacy; IP |
| **Party** | First-party and third-party |
| **Status** | Draft v0.1 |

## Business outcome

An employee, contractor, or an agent acting under their identity uses AI to find, gather, or remove data at a speed and scale no person could manage alone, causing data exposure, IP loss, or damaging actions.

## Applies when

- Employees have AI tools that can search or retrieve across repositories, mailboxes, chat, or code.
- Agents act under a user's identity or with delegated credentials.
- The organization's insider-risk program does not yet monitor AI tool use or agent identities.
- Data access is broad relative to job need (common in collaboration suites).

## What it looks like

- **Negligent insider:** an employee pastes source code, customer records, or strategy documents into an AI tool to get work done. This is the most common form by far.
- **Malicious insider:** a departing employee uses a copilot to locate and summarize everything valuable they can reach, then removes it.
- **Agent as insider:** an agent running under a user's identity reads, moves, or changes far more than the user ever would, at machine speed. OWASP describes an agent drifting from its intended behavior as harming the organization "in a way similar to an insider threat".

## Boundaries

- **B2 (sanctioned-AI leakage)** is about the *platform* exposing data, through oversharing or injection, regardless of the user's intent. B1 is about a *person or their agent* using AI to extend their own reach. If a copilot surfaces a file the user should not see and they never act on it, that is B2. If they use it to gather and exfiltrate, that is B1.
- **B3 (shadow AI)** covers data sent to unsanctioned services. A negligent insider pasting data into a consumer chatbot is both B1 and B3; record it as B3 when the main issue is the unsanctioned destination, and B1 when it is the scale of access.
- **B11** covers agents causing operational damage through execution failure. B1 covers agents extending a human's reach to data.

## Evidence

- **Samsung (2023).** Employees entered sensitive information, including source code, into ChatGPT in three reported incidents. Samsung restricted generative AI on company devices `[secondary]` ([TechRadar](https://www.techradar.com/news/samsung-bans-chatgpt-use-after-employee-leak)). This is the canonical negligent-insider case.
- **Verizon 2026 Data Breach Investigations Report**, as summarized: shadow AI was the third most common non-malicious insider action in data-loss telemetry, with detections up fourfold year on year; source code was the most common data type uploaded to unauthorized AI services `[secondary; primary report not checked]` ([Security Boulevard](https://securityboulevard.com/2026/05/the-ai-governance-gap-verizons-2026-dbir-shows-attackers-scaling-ai-while-employees-leak-data-through-it/)).
- **Netskope 2026:** 60% of insider-threat incidents involved personal cloud-app instances `[vendor]` ([Netskope](https://threatlabs.netskope.com/reports/2026/cloud-and-threat-report-2026)).
- **OWASP Top 10 for Agentic Applications (2026 edition):** ASI03 (identity and privilege abuse) covers agents exploiting inherited user identities; ASI10 (rogue agents) describes the insider-like failure `[industry-body]`.
- **Gap:** we found no well-documented public case (court filing or regulator action) of a *malicious* employee using an enterprise AI assistant or agent as the exfiltration channel. Evidence is overwhelmingly about negligence.

## Business impact

| Loss form | Examples |
|---|---|
| Competitive advantage | Source code, product plans, pricing, or trade secrets lost |
| Fines and judgments | Privacy breach where personal data is involved |
| Response | Investigation, legal hold, forensic review of AI logs |
| Reputation | Disclosure of a breach caused by an employee's AI use |

## Levers

| Lever | Type | Owner |
|---|---|---|
| Extend insider-risk monitoring (data-loss prevention, user behavior analytics) to AI tools and agent identities | Detective | CISO |
| Separate human and agent identities; scope agent credentials to the task | Preventive | CISO with CIO |
| Reduce standing access in collaboration suites before rolling out retrieval-based AI | Preventive | CIO (see B2) |
| Acceptable-use policy covering AI, with HR process for breaches | Directive | CHRO |
| Employment terms on IP and confidentiality that name AI tools | Directive | CHRO with General Counsel |
| Offboarding review of AI tool history for high-risk leavers | Detective | CISO with CHRO |

## Quantification notes

- **Frequency:** start from internal data-loss telemetry on AI destinations. Policy violations are not losses, but they show how often sensitive data moves. Malicious cases are rare and should carry a low frequency with a heavy-tailed magnitude.
- **Magnitude:** dominated by competitive advantage (what the leaked material is worth) and, where personal data is involved, breach costs. IBM 2025 reported that shadow-AI incidents compromised personal data in 65% of cases and IP in 40% `[survey]`.

## Example scenario statement

> There is a 10% to 30% probability in the next 12 months that an engineer using the approved coding assistant through a personal account exposes proprietary source code, producing a first-party loss of $200,000 to $2 million in competitive advantage and response costs.

## Questions for the accountable executive

1. Does our insider-risk program see AI tool use and agent activity, or only file and email movement?
2. Which agents act under employee identities, and what can those identities reach?
3. Would we know if a departing employee used a copilot to gather everything they could see?

## Crosswalk

| Framework | Reference |
|---|---|
| Huwyler taxonomy | Misuse: Shadow AI Usage; IP Threat: Data Exfiltration |
| OWASP Agentic 2026 | ASI03 Identity and Privilege Abuse; ASI10 Rogue Agents |
| OWASP LLM 2025 | LLM02 Sensitive Information Disclosure; LLM06 Excessive Agency |
| MITRE ATLAS | AML.T0057 LLM Data Leakage; AML.T0024 Exfiltration via AI Inference API |
| MIT AI Risk Repository | 2.1 Compromise of privacy; 4.3 Fraud, scams, targeted manipulation (malicious variant) |
| NIST AI 600-1 | Data Privacy; Information Security |
| CSA AICM | IAM, DSP, HRS, LOG |

## Open questions

- Should "agent as insider" eventually become its own scenario, given different detection and ownership?
- How should organizations weigh the low-frequency, high-magnitude malicious case against the high-frequency negligent case when evidence for the former is so thin?
