# Layer 4: Agency and tier

> **Executive question:** How much can it do without us? Does it qualify for the fast lane?

## Purpose

What an AI system is allowed to do, without a person approving each step, is the strongest single driver of how bad things can get. Layer 4 records the use case's agency, scores it, applies the override rules, and assigns the tier that decides how much of layers 5 to 8 it gets. The full rules are in [Tiering](../05-tiering.md); this page covers how to apply them.

## Agentic scope

BORA-EAI uses the four scopes of the AWS Agentic AI Security Scoping Matrix `[vendor, vendor-neutral in substance]` ([AWS](https://aws.amazon.com/ai/security/agentic-ai-scoping-matrix/)):

| Scope | Name | What it means | Where controls concentrate |
|---|---|---|---|
| 1 | No agency | Human-initiated, read-only | Identity, input validation, boundaries |
| 2 | Prescribed agency | Recommends and prepares changes; a human approves each one | Approval workflows, secure human-agent channels |
| 3 | Supervised agency | Human-initiated, then acts autonomously within predefined bounds | Continuous monitoring, behavioral validation, shut-off switches |
| 4 | Full agency | Self-initiating, continuous, minimal oversight | Behavioral monitoring, anomaly detection, automated containment |

Record the scope the use case actually operates at, not the one it was designed for. A "prescribed" agent whose approvals are rubber-stamped is closer to supervised.

## What to record

| Item | Notes |
|---|---|
| Agentic scope | 1 to 4 |
| Actions available | Read, write, delete, execute code, send external communications, spend or commit money, call other agents |
| Credentials | Whose identity the AI acts under; standing or short-lived; scope |
| Hard limits | Limits enforced outside the model (transaction caps, allow-lists, environment separation) versus instructions in the prompt |
| Human approval points | Which actions need a person, and whether the approver sees enough to judge |
| CBRA scores | Criticality, autonomy, permissions, impact radius (1 to 4 each) |
| Override triggers | Regulated personal data; customer-facing representations or concessions |
| Fast-lane pattern | Pattern ID, if it matches one |

## Prompts are not controls

In both of the best-documented destructive agent incidents, the agent was told not to do the thing it did. In July 2025, Replit's coding agent deleted SaaStr's production database during a declared code freeze `[secondary]`. In April 2026, a Cursor agent running Anthropic's Claude Opus 4.6 deleted PocketOS's production database and then its backups, without asking for confirmation and despite a safeguard against destructive commands, causing an outage of more than 30 hours for PocketOS's car-rental customers `[secondary]` ([Euronews](https://www.euronews.com/2026/04/28/an-ai-agent-deleted-a-companys-entire-database-in-9-seconds-then-wrote-an-apology)).

For tiering, count only limits enforced outside the model. An instruction in a system prompt is not a permission boundary. Assume an agent can do anything its credentials allow.

## Applying the tier

1. **Check the fast lane.** Does the use case match a pre-approved pattern and meet every [fast-lane condition](../05-tiering.md#fast-lane)? If yes, register it and stop.
2. **Score CBRA.** Use the [provisional anchor scales](../05-tiering.md#provisional-anchor-scales), or CSA's own if you have them. Multiply the four scores to get a provisional tier.
3. **Apply the overrides.** Regulated personal data or customer-facing representations lift the tier to at least Medium.
4. **Apply organizational overrides,** if any (for example, EU AI Act Annex III categories to High).
5. **Record the reasoning,** especially near a boundary.

## Redesign before you assess

Layer 4 is often where the most valuable decision is made. Small changes in agency or permissions move a use case down a tier and remove whole scenarios. CBRA's multiplicative structure makes this visible: reducing autonomy from 3 to 2, or permissions from 4 to 3, materially lowers the product. Typical redesigns:

- replace standing credentials with short-lived, narrowly scoped ones;
- separate agent environments from production, and keep backups under separate credentials the agent cannot reach;
- move concession or spending limits out of the prompt and into the system the agent calls;
- add a human approval step for destructive, external, or financial actions;
- narrow the data the use case can retrieve.

## Output

The use case's agentic scope, CBRA scores, override triggers, tier, and the reasoning. If fast lane, a pattern ID and review date.

## Scenarios this layer drives

| Finding | Raises |
|---|---|
| Agentic scope 3 or 4 | B11, B12, B1 |
| Can spend, order, or commit | B12 |
| Can write to or delete from production | B11 |
| Acts under a user's identity | B1, B2 |
| Customer-facing representations or concessions | B8, B10 (override to at least Medium) |
| Regulated personal data | B2, B3, B13 (override to at least Medium) |

Next: [Layer 5: Business threat scenarios](L5-business-threat-scenarios.md)
