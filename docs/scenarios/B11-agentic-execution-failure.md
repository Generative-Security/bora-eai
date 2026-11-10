# B11: Agentic execution failure

| | |
|---|---|
| **Accountable** | CTO |
| **Consulted** | Business continuity owner |
| **Lens** | Both |
| **Loss domain** | Operational (business interruption) |
| **Party** | First-party and third-party (downstream customers, SLAs) |
| **Status** | Draft v0.1 |

## Business outcome

An AI agent deletes, modifies, or corrupts systems or data, runs up uncontrolled spend, or triggers cascading errors across integrations, using credentials it was given, causing outages, data loss, or financial waste.

## Applies when

- Agentic Scope 3 or 4: the agent acts within bounds, or freely, without per-action approval.
- The agent holds credentials that can write to or delete from production, or reach backups.
- Agents call other agents or chain through several integrations.
- Agents consume metered services (inference, cloud resources, paid APIs) without caps.
- Limits are expressed in the prompt rather than enforced by the systems the agent uses.

## What it looks like

- A coding agent deletes a production database while "fixing" an unrelated problem.
- An agent loops, calling a paid API or model thousands of times.
- An agent's error propagates through connected systems before anyone notices.
- An agent silently rewrites or transforms data it was not meant to touch.
- Multi-agent workflows amplify one agent's mistake, or drift from their intended state over time.

These failure modes share an owner, a loss type, and a control set: credential scope, environment separation, spend caps, and rollback. BORA-EAI treats them as one business threat scenario.

## Boundaries

- **B12** covers agents committing the company to third parties (payments, orders, contracts). B11 covers damage to the organization's own systems, data, and spend.
- **B1** covers agents extending a human's reach to data. B11 covers agents causing operational damage.
- **B9** requires an attacker. B11 can happen with no attacker at all, and usually does.

## Evidence

- **Replit and SaaStr (July 2025).** During a declared code freeze, Replit's AI agent deleted the production database of SaaStr founder Jason Lemkin's project, and misrepresented what had happened. Coverage reported records on more than 1,200 executives and 1,190 companies lost, and about 4,000 fabricated users. Replit's CEO subsequently introduced development and production separation `[secondary; record counts not confirmed from a primary source]` ([The Stack](https://www.thestack.technology/vibe-coding-ceo-deletes-production-database/)).
- **PocketOS (April 2026).** A Cursor coding agent powered by Anthropic's Claude Opus 4.6, on a routine task, tried to resolve a "credential mismatch" by deleting the database volume and then all backups, on its own initiative, without asking for confirmation and despite a safeguard against destructive commands. PocketOS's car-rental customers lost access to customer records and bookings in an outage of more than 30 hours, and three months of reservations and sign-ups were unavailable until data was recovered two days later `[secondary]` ([Euronews](https://www.euronews.com/2026/04/28/an-ai-agent-deleted-a-companys-entire-database-in-9-seconds-then-wrote-an-apology)).
- **IBM 2025:** 31% of AI-related security incidents led to operational disruption `[survey]`.
- **OWASP Top 10 for Agentic Applications (2026 edition):** ASI02 (tool misuse, including destructive commands and costly services), ASI03 (identity and privilege abuse), ASI08 (cascading failures), ASI10 (rogue agents) `[industry-body]`.

In both deletion cases the agent held credentials that could destroy production *and* its backups, and instructions not to ("code freeze", "no destructive commands") were not enforced controls.

## Business impact

| Loss form | Examples |
|---|---|
| Productivity | Outage; staff idle; customers unable to transact |
| Replacement | Data restoration; rebuilding environments |
| Response | Investigation; customer communications |
| Fines and judgments | SLA penalties; obligations to customers' customers |
| Reputation | Public incident; loss of customer confidence |

## Levers

| Lever | Type | Owner |
|---|---|---|
| Short-lived, narrowly scoped agent credentials; no standing delete rights in production | Preventive | CTO with CISO |
| Separate agent environments from production by default | Preventive | CTO |
| Immutable backups under credentials agents cannot reach | Preventive | Business continuity owner |
| Human approval for destructive, irreversible, or bulk actions, enforced by the system, not the prompt | Preventive | CTO |
| Spend caps and rate limits on agent use of metered services | Preventive | CTO with CFO |
| Logging of agent actions and anomaly detection | Detective | CISO |
| Tested rollback and recovery for agent-touched systems | Corrective | Business continuity owner |
| Circuit breakers for multi-agent chains | Preventive | CTO |

## Quantification notes

- **Frequency:** grows with the number of agents holding write access. Count agents by credential reach rather than by product.
- **Magnitude:** business-interruption benchmarks apply. Verizon 2026 reported business interruption as the highest-median loss category in cyber-insurance claims, about US$90,000 per claim `[survey]`. Add downstream customer impact where the organization runs a platform.

## Example scenario statement

> There is a 5% to 15% probability in the next 12 months that a coding agent with production credentials deletes or corrupts a customer-facing database, producing a combined loss of $100,000 to $2.5 million in interruption, restoration, and customer remediation.

## Questions for the accountable executive

1. Which agents can delete or modify production data, and could any of them reach the backups?
2. Are our "don't do this" rules for agents enforced by systems, or written in prompts?
3. What caps stop an agent from spending without limit?

## Crosswalk

| Framework | Reference |
|---|---|
| Huwyler taxonomy | Thin coverage of agentic threats; nearest is Unreliable Outputs and Adversarial: Model DoS |
| OWASP LLM 2025 | LLM06 Excessive Agency; LLM10 Unbounded Consumption |
| OWASP Agentic 2026 | ASI02 Tool Misuse and Exploitation; ASI03 Identity and Privilege Abuse; ASI08 Cascading Failures; ASI10 Rogue Agents |
| AWS Agentic Scoping Matrix | Scopes 3 and 4 |
| MIT AI Risk Repository | 7.3 Lack of capability or robustness; 7.6 Multi-agent risks; 5.2 Loss of human agency and autonomy |
| NIST AI 600-1 | Human-AI Configuration; Information Security |
| CSA AICM | IAM, BCR, LOG, CCC |
