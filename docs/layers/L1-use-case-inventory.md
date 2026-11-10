# Layer 1: Use-case inventory

> **Executive question:** What is AI doing for us, and where?

## Purpose

You cannot govern AI use you cannot see. Layer 1 builds and maintains a register with one row per AI use case, each with a named business owner. It also selects the [lens](../lenses/README.md) (internal or customer-facing) that the rest of the assessment uses.

## What counts as a use case

A use case is a specific use of AI by a specific population for a specific purpose. Split a candidate into separate use cases when any of these differ:

- the users (employees, a subset of employees, customers, partners, agents);
- the data classes it touches;
- what it may do (answer, recommend, act);
- the accountable business owner.

"Microsoft 365 Copilot" is a product, not a use case. "Copilot for the finance team over the finance SharePoint" and "Copilot for all staff over all of SharePoint" are two use cases with very different exposure.

Include all of these sources:

| Source | How it is found | Typical scenarios |
|---|---|---|
| Sanctioned tools and platforms | Procurement, IT service catalog | B2, B6, B13 |
| AI built in-house | Architecture review, cloud billing (model and inference API usage) | B4, B9, B11 |
| Customer-facing AI | Digital channel owners | B8, B9, B10 |
| AI features in software already owned | Vendor release notes, tenant admin consoles, SaaS security posture tools | B7 |
| Shadow use | Network and SaaS discovery, browser and endpoint telemetry, expense claims | B3, B4 |
| Agents and automations | Identity systems (agent and service accounts), automation platforms | B1, B11, B12 |

## What to record

| Field | Notes |
|---|---|
| Use-case ID and name | Short, business-recognizable name |
| Business owner | The one executive accountable for net position (confirmed in Layer 2) |
| Line of business | IT, software engineering, customer service, sales and marketing, HR, finance, legal, product and R&D, operations and manufacturing, supply chain, or other |
| Capability type | See below |
| Lens | Internal or customer-facing |
| Users | Population and approximate count |
| Data classes | Public, internal, confidential, regulated personal data, secrets, source code |
| Decisions about individuals | Yes or no: hiring, credit, eligibility, discipline, pricing |
| Product or platform | Tool, provider, model if known |
| Status | Proposed, pilot, production, retired, or discovered (shadow) |
| Tier and review date | From Layer 4 |

The [use-case register template](../../templates/use-case-register.csv) has these columns.

## Capability types

To describe what the AI does in a process, BORA-EAI uses the eight GenAI capability types in COSO's March 2026 guidance, *Achieving Effective Internal Control Over Generative AI* `[industry-body]` ([IIA summary](https://internalauditor.theiia.org/en/articles/2026/march/coso-issues-genai-guidance/)):

| Capability type | What the AI does | Example |
|---|---|---|
| Ingestion | Takes in and structures content | Extracting fields from invoices |
| Transformation | Rewrites, summarizes, translates | Summarizing case notes |
| Posting | Writes results into a system of record | Creating journal entries |
| Orchestration | Coordinates steps or tools | An agent running a workflow |
| Judgment | Recommends or decides | Triage, scoring, approval suggestions |
| Monitoring | Watches for conditions | Anomaly flags on transactions |
| Regulatory intelligence | Interprets rules and obligations | Mapping a new regulation to policies |
| Human-AI interaction | Converses with people | Assistants and chatbots |

Crossing capability type with line of business gives the inventory's main axes. It shows, for example, that posting and orchestration in finance carry different risks from transformation in marketing.

## Method

1. Build the first inventory from all six sources above. Expect shadow use and vendor-enabled features to be a large share.
2. For each row, name the business owner. A use case without an owner is a finding, not a gap to fill later.
3. Select the lens.
4. Hand off to Layer 2.
5. Sweep for new use cases quarterly, and whenever a major vendor announces AI features.

The Australian Government's AI policy for agencies (v2.0, effective 15 December 2025) requires an accountable officer for each use case and an internal use-case register `[government]` ([DTA](https://www.dta.gov.au/media-releases/ai-policy-overhauled-new-impact-assessment-tool-and-procurement-guidance)). BORA-EAI register follows the same pattern for enterprises.

## Output

One register row per use case, with a named owner and a lens.

## Pitfalls

- **Inventorying products instead of use cases.** One product can host many use cases with different risk.
- **Missing vendor-enabled AI.** Customers often learn about embedded AI features from press coverage rather than contractual notice. See [B7](../scenarios/B07-vendor-enabled-embedded-ai.md).
- **Treating shadow use only as a violation.** Shadow use is also evidence of demand and of value the organization is not capturing. Record it as a use case, then decide.
- **No owner.** If nobody will own it, that is a decision in itself.

Next: [Layer 2: Consumption and ownership](L2-consumption-and-ownership.md)
