# B9: Bot technical compromise

| | |
|---|---|
| **Accountable** | CISO |
| **Consulted** | Channel owner |
| **Lens** | Customer-facing |
| **Loss domain** | Cybersecurity and privacy; operational |
| **Party** | First-party and third-party |
| **Status** | Draft v0.1 |

## Business outcome

An attacker exploits a customer-facing AI to leak customer or company data, misuse the tools and systems it is connected to, run up costs, or take it out of service.

## Applies when

- The AI retrieves customer, account, or internal data to answer questions.
- It can call tools or APIs (look up orders, change bookings, issue credits, send messages).
- It processes content from outside (customer uploads, web pages, emails).
- It is exposed to the public internet at scale.

## What it looks like

- **Prompt injection** that makes the bot reveal other customers' data, internal documents, or its system instructions.
- **Tool misuse:** the attacker steers the bot into calling a connected tool in a harmful way.
- **Cost and availability attacks:** floods of expensive queries that run up inference spend or degrade service.
- **Jailbreaks** that make the bot produce content that damages the brand.

## Boundaries

- **B8** needs no attacker; the AI is simply wrong. B9 needs an attacker exploiting a weakness.
- **B10** is persuasion within what the bot is permitted to do. B9 makes the bot do something it should not be able to do. As a test: if the bot did only what its permissions and design allow, but was talked into it, it is B10. If it breached its intended boundaries, it is B9.
- **B2** is the internal equivalent. Use B9 for customer-facing AI.

## Evidence

- **Prompt injection is the top-ranked risk** in the OWASP Top 10 for LLM Applications 2025 (LLM01), and agent goal hijack is the top-ranked agentic risk (ASI01) `[industry-body]`.
- **EchoLeak (2025)** demonstrated zero-click data exfiltration from a retrieval-based assistant through planted content. It concerned an internal assistant, but the mechanism applies to any AI that mixes untrusted input with privileged data `[secondary]` (see [B2](B02-sanctioned-ai-leakage.md)).
- **IBM 2025:** 31% of AI-related security incidents led to operational disruption `[survey]`.
- **Verizon 2026 Breach Impact Study:** business interruption had the highest median loss of any category, about US$90,000 per insurance claim `[survey]`.
- **Gap:** we found few public, quantified cases of a customer-facing bot being technically compromised to leak customer data. Most public bot failures were B8 or B10.

## Business impact

| Loss form | Examples |
|---|---|
| Fines and judgments | Customer data exposed through the bot |
| Response | Incident response, notification, forensic review of conversations |
| Productivity | Bot offline; customer traffic diverted to human agents |
| Replacement | Rebuilding guardrails and integrations |
| Reputation | Public demonstration of the exploit |

## Levers

| Lever | Type | Owner |
|---|---|---|
| Least-privilege tool and data access for the bot; per-customer data scoping enforced outside the model | Preventive | CISO with channel owner |
| Input and output filtering; separation of untrusted content from instructions | Preventive | CISO |
| Red teaming before launch and after material changes | Detective | CISO |
| Rate limits and spend caps on inference | Preventive | CTO |
| Monitoring of conversations and tool calls for abuse patterns | Detective | CISO |
| Kill switch and human fallback for the channel | Corrective | Channel owner |

## Quantification notes

- **Frequency:** start from red-team findings and the bot's exposure (public, authenticated, volume). Injection attempts against public bots should be assumed; successful exploitation depends on what the bot can reach.
- **Magnitude:** scales with the data and tools the bot can reach. A bot with no access to customer records has a small data-breach magnitude but still carries interruption and reputational loss.

## Example scenario statement

> There is a 5% to 20% probability in the next 12 months that an attacker uses prompt injection to make our account-service bot disclose other customers' order data, producing a combined loss of $250,000 to $3 million in response, notification, regulatory, and interruption costs.

## Questions for the accountable executive

1. What is the worst thing our bot can reach or do if an attacker fully controls the conversation?
2. Are customer-data boundaries enforced by the system it calls, or by instructions in its prompt?
3. Has it been red-teamed since its last material change?

## Crosswalk

| Framework | Reference |
|---|---|
| Huwyler taxonomy | Misuse: Prompt Injection, LLM Jailbreaking; Adversarial: Model DoS, Query Flooding |
| OWASP LLM 2025 | LLM01 Prompt Injection; LLM02 Sensitive Information Disclosure; LLM05 Improper Output Handling; LLM06 Excessive Agency; LLM07 System Prompt Leakage; LLM10 Unbounded Consumption |
| OWASP Agentic 2026 | ASI01 Agent Goal Hijack; ASI02 Tool Misuse and Exploitation |
| MITRE ATLAS | AML.T0051 LLM Prompt Injection; AML.T0054 LLM Jailbreak; AML.T0057 LLM Data Leakage; AML.T0029 Denial of AI Service; AML.T0034 Cost Harvesting |
| MIT AI Risk Repository | 2.2 AI system security vulnerabilities and attacks; 2.1 Compromise of privacy |
| NIST AI 600-1 | Information Security; Data Privacy |
| CSA AICM | AIS, MDS, IAM, LOG, TVM |
