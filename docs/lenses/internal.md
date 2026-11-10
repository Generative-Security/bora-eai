# Internal lens

**Applies to:** use cases whose users are employees or contractors, and whose output stays inside the organization. Coding assistants, copilots over company data, internal agents, document processing, analytics, and AI features in internal software.

## The three questions

### 1. What can it see?

An internal assistant sees whatever its user's identity can reach, and often more than anyone realized that identity could reach. Retrieval-augmented copilots turn existing permission problems (overshared sites, stale access, unlabeled sensitive files) into a fast discovery tool for any user.

They can also become a channel for outsiders. EchoLeak (CVE-2025-32711, CVSS 9.3, fixed in June 2025) showed that a single crafted email could cause Microsoft 365 Copilot to retrieve privileged internal data and leak it, with no click by the user `[secondary]` ([The Hacker News](https://thehackernews.com/2025/06/zero-click-ai-vulnerability-exposes.html)). IBM's 2025 study found that 97% of organizations reporting an AI breach lacked AI access controls `[survey]`. Most of this is a governance failure, not an exotic exploit.

Assess: data classes reachable, permission hygiene in the sources, sensitivity labeling, and whether retrieval mixes untrusted content (email, web, uploaded files) with privileged data.

Scenarios: [B2](../scenarios/B02-sanctioned-ai-leakage.md), [B1](../scenarios/B01-insider-amplification.md).

### 2. What can it do, and as whom?

Agents act under an identity. When that identity is a user's, the agent inherits the user's full reach at machine speed. When it is a service account with standing production rights, an agent can do anything those rights allow, regardless of what its instructions say. In both the Replit/SaaStr (2025) and PocketOS (2026) incidents, coding agents deleted production databases despite instructions not to.

Assess: agentic scope, credentials (whose, how long-lived, how broad), limits enforced outside the model, and environment separation.

Scenarios: [B11](../scenarios/B11-agentic-execution-failure.md), [B1](../scenarios/B01-insider-amplification.md), [B12](../scenarios/B12-agentic-unauthorized-commitments.md) for agents that can spend or order.

### 3. Is the productivity gain real?

This is the internal lens's value question, and the evidence says the answer depends on who uses the tool and for what. In the best-known customer-support study, novices gained about 34% while experienced agents gained little. In METR's 2025 trial, experienced developers working on their own mature codebases were 19% *slower* with AI, while believing they were 20% faster `[RCT]`. Danish administrative data across AI-exposed occupations found about 3% time savings and no measurable earnings effect `[quasi-experimental]`.

Assess: user expertise, whether tasks sit inside the model's demonstrated capability, whether errors are caught before they matter, and how value will be measured (throughput, quality, cycle time, never self-report alone).

Scenario: [B14](../scenarios/B14-forgone-and-negative-value.md).

## Where internal use cases come from

Many internal use cases are not chosen: they arrive.

- **Shadow use.** Verizon's 2026 data breach report, as summarized by a secondary source, found shadow AI was the third most common non-malicious insider action in data-loss telemetry and that 67% of employees accessed AI from non-corporate accounts on corporate devices `[secondary]`. Netskope's telemetry found source code was the largest single category of GenAI data-policy violations `[vendor]`. See [B3](../scenarios/B03-shadow-ai-leakage.md).
- **Tools employees install.** Models, browser extensions, MCP servers, and agent "skills" are executable code plus instructions an agent obeys. Over a thousand malicious agent skills were confirmed on one marketplace in early 2026 `[industry-body]`. See [B4](../scenarios/B04-untrusted-ai-artifacts.md).
- **Features vendors switch on.** See [B7](../scenarios/B07-vendor-enabled-embedded-ai.md).

Shadow use is also evidence of demand. The internal lens treats it as a use case to decide on, not only a violation to block. Netskope found that as organizations offered managed accounts, the share of AI users on personal accounts fell from 78% to 47% in a year `[vendor]`.

## Typical loss profile

Mostly first-party: data exposure and the regulatory consequences of it, loss of IP and source code, operational disruption, and incident response. Third-party exposure arises where personal data of customers or employees is involved.

## Typical value profile

Labor productivity and cycle time, measured per function. Rigorous evidence is strongest for customer support, writing, software engineering, and analysis; weakest for HR, finance, legal, and operations.

## Typical owners

CISO (B1, B3, B9 where internal), CIO as platform owner (B2), CTO (B4, B11), General Counsel (B7), and the business sponsor for value (B14).

## Quick screen for internal use cases

| Question | If yes, look at |
|---|---|
| Does it retrieve from shared repositories, mailboxes, or chat? | B2 |
| Does it act under a user's identity, or with standing credentials? | B1, B11 |
| Can it write, delete, execute, or spend? | B11, B12 |
| Is it used through personal or consumer accounts? | B3, B5, B13 |
| Did employees install the model, extension, or tool themselves? | B4 |
| Did it arrive inside software bought for something else? | B7 |
| Will experts use it on familiar work? | B14 (uplift may be negative) |
| Does regulated personal data reach it? | Override to at least Medium |
