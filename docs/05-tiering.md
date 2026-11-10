# Tiering

Tiering decides how much analysis a use case gets. It never produces a loss figure.

| Tier | What the use case gets | Typical effort |
|---|---|---|
| **Fast lane** | Registered in the inventory against a pre-approved pattern. Not assessed. | Minutes |
| **Low** | Qualitative screen against all fifteen scenarios and a sovereignty check. No numbers. | Hours |
| **Medium** | Ranges for the top three scenarios and for value; net position as a distribution. | Days |
| **High** | Full range-based quantification of every applicable scenario, red teaming, insurance-coverage review, and board reporting. | Weeks |

The effort column is our expectation, not a measurement. Measuring it is part of the [validation plan](validation/validation-plan.md).

## Fast lane

The approved path has to be faster than shadow AI, or the governance process itself drives the shadow-AI scenario (B3). The fast lane exists for that reason.

A use case qualifies for the fast lane only if it matches a **pre-approved pattern** and meets every one of these conditions:

- It uses a tool or platform already approved under enterprise terms (consumption Scope 2 with a contract, or the organization's own approved Scope 3 platform).
- Its data stays within the pattern's approved data classes, with no regulated personal data and no secrets.
- It takes no autonomous actions (agentic Scope 1 or 2: it answers, drafts, or recommends, and a person decides).
- Its users are internal, and its output is not shown to customers as the company's statement.
- It is not used to make or materially support decisions about individuals (hiring, credit, eligibility, discipline).
- It does not trigger either override rule below.

The fast lane is not "no governance". The use case is still recorded with an owner, a pattern ID, and a review date, and the quarterly inventory sweep checks that fast-lane use cases still match their pattern.

Patterns are set by the program owner with the CIO, CISO, and DPO, and reviewed every six months. See the [fast-lane pattern template](../templates/fast-lane-patterns.md) for examples.

## Assigning Low, Medium, or High

BORA-EAI uses the four dimensions of the Cloud Security Alliance's Capabilities-Based Risk Assessment (CBRA) `[industry-body]` ([CSA](https://cloudsecurityalliance.org/blog/2025/10/27/calibrating-ai-controls-to-real-risk-the-upcoming-capabilities-based-risk-assessment-cbra-for-ai-systems)):

- **Criticality:** what breaks (revenue, safety, compliance) if the use case is unavailable, wrong, or hostile.
- **Autonomy:** how far it can perceive, decide, and act without human approval.
- **Permissions:** what it can read, write, execute, or delegate.
- **Impact radius:** the maximum plausible harm from one adverse event, given its autonomy and permissions.

CBRA combines them as Criticality × Autonomy × Permissions × Impact radius. CSA's own examples run from 1 for a content helper to 48 for an agent that can rotate production access policies.

### Provisional anchor scales

CSA's whitepaper defines its own anchor scales and tier thresholds. We could not retrieve them for this draft, so the scales and thresholds below are **provisional BORA-EAI defaults**, written to be consistent with CSA's published examples. Where you have the CBRA paper, use its scales instead.

| Score | Criticality | Autonomy (AWS agentic scope) | Permissions | Impact radius |
|---|---|---|---|---|
| 1 | Convenience; no process depends on it | No agency: human-initiated, read-only | Reads public data or the user's own content | One user |
| 2 | Supports a process; a workaround exists | Prescribed: prepares actions, a human approves each one | Reads internal business data | A team or department |
| 3 | A process depends on it; revenue or compliance is affected if it fails | Supervised: acts within defined bounds without per-action approval | Reads confidential or regulated data, or writes to business systems | The whole organization, or many customers |
| 4 | Safety, legal standing, or material revenue depends on it | Full: self-initiating, continuous, minimal oversight | Writes to or deletes from production, executes code, moves money, or delegates to other agents | External parties at scale, or systemic |

| Product of the four scores | Tier |
|---|---|
| 1 to 8 | Low |
| 9 to 35 | Medium |
| 36 and above | High |

Multiplying ordinal scales does not produce numbers with real meaning, which is why the product is used only to choose a tier and never as a risk figure. Treat a score near a boundary as a judgment call, and record the reasoning.

## Override rules

CBRA is capability-centric. A use case that can do very little can still create serious exposure. Two overrides correct for that:

1. **Regulated personal data.** Any use case with read access to regulated personal data is at least **Medium**. A read-only assistant over customer records scores low on autonomy but high on sanctioned-AI leakage (B2) exposure.
2. **Customer-facing representations or concessions.** Any use case that speaks for the company to customers, or can grant them anything, is at least **Medium**. This is where misrepresentation liability (B8) and commercial manipulation (B10) live, however simple the bot.

A use case caught by either override can never use the fast lane.

ISO/IEC 42005:2025 asks organizations to establish "thresholds for sensitive uses, restricted uses and impact scales" `[standard]` ([ANSI preview](https://webstore.ansi.org/preview-pages/ISO/preview_ISO+IEC+42005-2025.pdf)). These overrides are one way to meet that requirement. Organizations may add their own, for example:

- use cases in an EU AI Act Annex III high-risk category (such as employment or credit decisions) go to High;
- use cases that make or support automated decisions about individuals, which must be disclosed in Australian privacy policies from 10 December 2026, go to at least Medium.

These thresholds are our judgment and open to challenge.

## Tier and controls

The tier also selects a control baseline. CBRA maps its Low, Medium, and High tiers to graduated sets of CSA AI Controls Matrix controls: foundational hygiene at Low, added validation, monitoring, and transparency at Medium, and close to all relevant controls in depth at High `[industry-body]`. BORA-EAI adopts that mapping. The scenario pages list the business-level levers; the AICM supplies the detailed controls.

Next: [Quantification](06-quantification.md)
