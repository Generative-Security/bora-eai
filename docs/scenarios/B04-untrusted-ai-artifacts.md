# B4: Untrusted AI artifacts

| | |
|---|---|
| **Accountable** | CTO |
| **Consulted** | CISO |
| **Lens** | Internal |
| **Loss domain** | Operational; cybersecurity and privacy |
| **Party** | Mostly first-party |
| **Status** | Draft v0.1 |

## Business outcome

A model, browser extension, MCP server, agent skill, or AI library that someone in the organization installed runs malicious code, steals credentials, or quietly sends data to an attacker.

## Applies when

- Developers or data scientists can download models from public hubs and run them.
- Employees can install browser extensions, IDE extensions, MCP servers, or agent skills without review.
- AI tooling runs on developer endpoints with access to source code, secrets, and cloud credentials.
- The organization builds AI in-house (consumption Scopes 3 to 5).

## What it looks like

- A model file on a public hub executes code when loaded.
- An MCP server that impersonates a legitimate one silently copies data to an attacker.
- A previously approved MCP configuration is swapped for a malicious one (a "rug pull").
- An agent skill contains instructions that lead the agent to show the user fake installation steps that install malware.
- An AI browser extension harvests chat histories or page content.

These artifacts are executable code *plus* natural-language instructions an agent obeys, so they can slip past both code scanning (which inspects code) and data-loss tools (which inspect data).

## Boundaries

- **B3** is about where data goes. B4 is about what runs. An extension that both executes and exfiltrates can be both.
- **B5** covers the legal side of third-party models and data (licenses, IP). B4 covers the security side.
- **B6** covers compromise of a *vendor* the organization contracts with. B4 covers artifacts pulled in directly, usually without a contract.

## Evidence

- **Malicious models on Hugging Face (2024):** JFrog found models with a "silent backdoor" targeting data scientists; reporting counted more than 100 malicious models `[vendor, via secondary]` ([The Hacker News](https://thehackernews.com/2024/03/over-100-malicious-aiml-models-found-on.html)).
- **Typosquatted Postmark MCP server (first seen September 2025):** a malicious npm package impersonating the official Postmark MCP server silently copied all email traffic to an attacker `[industry-body]` ([CSA research note](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-skill-supply-chain-attacks-20260624-csa/)).
- **ClawHub agent-skill campaign (February to May 2026):** an audit found 341 malicious skills, 11.9% of those available; the "ClawHavoc" campaign reached 1,184 confirmed malicious skills. Trend Micro found skills distributing the Atomic macOS Stealer, harvesting browser credentials, keychain passwords, crypto wallets, SSH keys, and Telegram sessions. Malicious instructions in skill files led agents to show users fake prerequisite steps `[industry-body]` (CSA research note, above).
- **MCPoison (2025):** Check Point showed an approved MCP configuration in the Cursor IDE could be swapped for a malicious one, giving persistent code execution `[industry-body, via CSA]`.
- **Malicious AI assistant browser extensions (March 2026):** Microsoft disclosed extensions harvesting LLM chat histories across multiple enterprise deployments `[industry-body, via CSA]`.
- **Verizon 2026,** as summarized: 15% of users run unauthorized AI browser extensions that collect browsing context `[secondary]`.
- **Gap:** we found no quantified dollar loss from a malicious MCP server or agent skill incident.

## Business impact

| Loss form | Examples |
|---|---|
| Response | Credential rotation, endpoint rebuilds, investigation |
| Replacement | Rebuilding compromised developer environments or pipelines |
| Competitive advantage | Source code or secrets stolen from developer endpoints |
| Productivity | Engineering time lost; release delays |

The compromise often starts on one developer laptop and reaches cloud environments through the credentials stored there.

## Levers

| Lever | Type | Owner |
|---|---|---|
| Allow-list of approved models, MCP servers, skills, and extensions | Preventive | CTO |
| Signing, version pinning, and change alerts for approved artifacts | Preventive | CTO |
| Safe model formats and scanning before load | Preventive | CTO with CISO |
| Developer endpoint controls; no long-lived cloud credentials on laptops | Preventive | CISO |
| Sandboxing for agent tools and MCP servers | Preventive | CTO |
| Inventory of AI artifacts (an AI bill of materials) | Detective | CTO |

## Quantification notes

- **Frequency:** rising quickly as agent marketplaces grow. Use internal discovery of unapproved artifacts as a leading indicator.
- **Magnitude:** model on incident response and credential-compromise costs; the tail is driven by what the compromised endpoint could reach.

## Example scenario statement

> There is a 10% to 25% probability in the next 12 months that a developer installs a malicious MCP server or agent skill that steals cloud credentials, producing a first-party loss of $150,000 to $3 million in response, replacement, and IP costs.

## Questions for the accountable executive

1. Do we know which models, MCP servers, agent skills, and AI extensions are running on our developers' machines?
2. If one of them were malicious, what credentials could it reach?
3. Is there a fast way for engineers to get a new tool approved?

## Crosswalk

| Framework | Reference |
|---|---|
| Huwyler taxonomy | Poisoning: Tainted Open-Source Models, Poisoned ML Libraries; Supply Chain: Compromised Pre-trained Model, Vulnerable ML Framework |
| OWASP LLM 2025 | LLM03 Supply Chain; LLM04 Data and Model Poisoning |
| OWASP Agentic 2026 | ASI04 Agentic Supply Chain Vulnerabilities; ASI05 Unexpected Code Execution |
| MITRE ATLAS | AML.T0010 AI Supply Chain Compromise; AML.T0011 User Execution (unsafe AI artifacts) |
| MIT AI Risk Repository | 2.2 AI system security vulnerabilities and attacks |
| NIST AI 600-1 | Information Security; Value Chain and Component Integration |
| CSA AICM | STA, TVM, UEM, MDS |

## Open questions

- Should agent marketplaces (skills, MCP registries) be treated as a distinct supply-chain tier with its own due-diligence standard?
