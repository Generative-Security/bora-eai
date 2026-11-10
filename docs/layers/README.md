# Layers

Every use case moves through nine layers. Each answers one executive question and borrows the strongest existing component for that job. Layers 1 to 4 run for every use case; they decide how much of layers 5 to 8 is needed. Layer 9 closes every assessment.

| # | Layer | Executive question | Borrows from | Output |
|---|---|---|---|---|
| 1 | [Use-case inventory](L1-use-case-inventory.md) | What is AI doing for us, and where? | COSO GenAI capability types; line of business; Australian DTA register pattern | One register row per use case, with a named owner |
| 2 | [Consumption and ownership](L2-consumption-and-ownership.md) | Who controls the application, model and data? Who is accountable? | AWS GenAI Scoping Matrix Scopes 1 to 5, plus new Scope 2e; CSA AICM shared-responsibility roles | Responsibility map, including the third- and fourth-party chain; one accountable executive |
| 3 | [Sovereignty profile](L3-sovereignty-profile.md) | Where does it run, whose law applies, can we leave? | Provider residency tiers; APRA's fourth-party framing (new six-axis profile) | Sovereignty profile per use case |
| 4 | [Agency and tier](L4-agency-and-tier.md) | How much can it do without us? Does it qualify for the fast lane? | AWS Agentic Scoping Matrix; CSA CBRA | Fast lane, Low, Medium, or High |
| 5 | [Business threat scenarios](L5-business-threat-scenarios.md) | What could go wrong, in business terms? | New fifteen-scenario library, anchored to Huwyler, OWASP, and MITRE ATLAS | Scenario statements in FAIR-AIR form |
| 6 | [Loss](L6-loss.md) | What would it cost, who pays, and how bad is a bad year? | Geneva Association loss domains; FAIR and FAIR-AIR | Annual loss distribution with tail, split by party and insurability |
| 7 | [Value](L7-value.md) | What do we gain, or forgo by waiting? | ISO 31000; NIST AI RMF MAP 3.1 and 3.2; controlled uplift studies; cost of delay | Risk-adjusted value range and cost of delay |
| 8 | [Governance cost](L8-governance-cost.md) | What does controlling it cost? | ISO/IEC 42001; EU AI Act cost estimates | Allocated governance cost range |
| 9 | [ERM fit and completeness](L9-erm-fit-and-completeness.md) | Does it fit risk appetite? What did we miss? | ISO/IEC 23894, 42001, 42005; MIT AI Risk Repository | Decision, register entries in ERM categories, coverage-gap note |

## How the layers relate to the lenses and scenarios

- Layer 1 selects the [lens](../lenses/README.md): internal or customer-facing.
- Layers 2 to 4 describe the use case's structure: who controls it, where it runs, and what it may do. Those facts make some scenarios likely and others irrelevant.
- Layer 5 picks the applicable [scenarios](../scenarios/README.md).
- Layers 6 to 8 put numbers on the scenarios, the value, and the governance cost.
- Layer 9 nets them and compares against appetite.

The evidence behind BORA-EAI points to one practical conclusion. The best-documented AI losses so far came from ownership, permission, and contract failures: 97% of organizations with an AI breach lacked AI access controls (IBM 2025), agents held credentials that could delete production and its backups (PocketOS 2026), an AI chat vendor's token store opened more than 700 customers' CRMs (Salesloft Drift 2025), and vendors rewrote training terms in their own favor (Zoom 2023, Adobe 2024, WeTransfer 2025). So the decisive layers are often 2 and 4, consumption scope and agency, not the threat taxonomy. That is where executives can act.
