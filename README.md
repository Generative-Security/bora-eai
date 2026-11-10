# Business Outcome Risk Analysis for Enterprise AI (BORA-EAI)

Threats, value, and ownership for each AI use case. Driven by strategy and performance.

**Working draft v0.1 · Open for review · November 2026**

Business Outcome Risk Analysis for Enterprise AI (BORA-EAI) is an open model for analyzing the risk of how an enterprise *uses* AI, at the level where executives make decisions: whether to fund, constrain, or stop a specific use of AI, and who answers for the outcome.

Technical threat models such as STRIDE, MITRE ATLAS, and MAESTRO are good at describing how an AI system can be attacked but they stop at the system boundary. They do not tell a CFO what a failure will cost, tell General Counsel which use cases carry liability, or tell a CEO what the business loses by not deploying at all. BORA-EAI is intended to work at that executive level. It takes each AI use case and asks what could happen to the business if something goes wrong, what value it brings to the business when it goes right, what it costs to govern, and which executive carries each consequence.

> **Status: not yet validated.** BORA-EAI is a working draft published for review. Several components are new and untested. Please read [Status and limitations](docs/validation/status-and-limitations.md) before using it for real decisions, and [tell us where it breaks](#help-us-break-it).

---

## Why another model

Enterprise AI risk is a puzzle of several pictures that only look right when they line up. Each executive owns one picture and measures it in a different currency:

| Picture | Owner | Currency | Example of what goes wrong |
|---|---|---|---|
| Laws and regulations | General Counsel, HR | Settlements and fines | A chatbot's statement binds the company; a hiring tool discriminates |
| Finance | CFO | Budget variance | A production system costs far more than the pilot did |
| Operations | COO, revenue owners | Revenue lost, efficiency gained | A revenue-generating bot is pulled offline |
| Security | CISO | Incident and breach cost | A copilot leaks data it should never have been able to see |
| Strategy | CEO, board | Growth gained or lost | Competitors capture value while we wait |

Each discipline already has a way to frame AI risk. But at Generative Security we have been trying to find a published model that lines them up, use case by use case, with the benefits on the same page as the threats. The [landscape review](docs/reference/landscape.md) explains what we looked at and where each existing model stops.

## How BORA-EAI works, in one minute

1. **The use case is the unit.** A coding assistant, a customer-facing chatbot, and an AI feature a vendor switched on inside software you already own are three use cases, even if they run on the same model. They differ in who uses them, what data they touch, what they may do, and which executive carries the consequence.
2. **Both sides of the ledger.** Benefits are weighed against losses and the cost of governing. Declining to deploy is a cost, not a safe default. This follows ISO 31000 and the NIST AI RMF (MAP 3.1 and 3.2), which both treat risk as two-sided.
3. **Two lenses.** Internal use cases are mostly about permissions, data exposure, and whether the productivity gain is real. Customer-facing use cases are mostly about what the AI may say or offer, who is liable, and what revenue it protects or puts at risk.
4. **Depth matches stakes.** A fast lane registers pre-approved patterns without assessment. Everything else gets a Low, Medium, or High tier that sets how much analysis it receives.
5. **One accountable owner per scenario.** Each use case has one executive accountable for its net position. Each business threat scenario has one accountable control owner, who holds the main lever that prevents the loss.
6. **Ranges, not points.** Inputs are three-point estimates combined by Monte Carlo simulation. The board sees a range, the chance the net position is negative, and a 1-in-20-year loss.

Each use case runs through **nine layers**, each answering one executive question:

| # | Layer | Executive question |
|---|---|---|
| 1 | [Use-case inventory](docs/layers/L1-use-case-inventory.md) | What is AI doing for us, and where? |
| 2 | [Consumption and ownership](docs/layers/L2-consumption-and-ownership.md) | Who controls the application, model and data? Who is accountable? |
| 3 | [Sovereignty profile](docs/layers/L3-sovereignty-profile.md) | Where does it run, whose law applies, can we leave? |
| 4 | [Agency and tier](docs/layers/L4-agency-and-tier.md) | How much can it do without us? Does it qualify for the fast lane? |
| 5 | [Business threat scenarios](docs/layers/L5-business-threat-scenarios.md) | What could go wrong, in business terms? |
| 6 | [Loss](docs/layers/L6-loss.md) | What would it cost, who pays, and how bad is a bad year? |
| 7 | [Value](docs/layers/L7-value.md) | What do we gain, or forgo by waiting? |
| 8 | [Governance cost](docs/layers/L8-governance-cost.md) | What does controlling it cost? |
| 9 | [ERM fit and completeness](docs/layers/L9-erm-fit-and-completeness.md) | Does it fit risk appetite? What did we miss? |

Layer 5 draws on a library of **fifteen business threat scenarios**, each with one accountable owner:

| ID | Scenario | Accountable (A) | Consulted (C) |
|---|---|---|---|
| [B1](docs/scenarios/B01-insider-amplification.md) | Insider amplification | CISO | CHRO |
| [B2](docs/scenarios/B02-sanctioned-ai-leakage.md) | Sanctioned-AI leakage | CIO (platform owner) | CISO |
| [B3](docs/scenarios/B03-shadow-ai-leakage.md) | Shadow-AI leakage | CISO | CIO, Procurement |
| [B4](docs/scenarios/B04-untrusted-ai-artifacts.md) | Untrusted AI artifacts | CTO | CISO |
| [B5](docs/scenarios/B05-ip-and-license-exposure.md) | IP and license exposure | General Counsel | CTO, Procurement |
| [B6](docs/scenarios/B06-ai-vendor-concentration.md) | AI vendor and fourth-party concentration | CRO | CIO, Procurement |
| [B7](docs/scenarios/B07-vendor-enabled-embedded-ai.md) | Vendor-enabled embedded AI | General Counsel | DPO, Procurement |
| [B8](docs/scenarios/B08-bot-misrepresentation-liability.md) | Bot misrepresentation liability | Channel owner (CX) | General Counsel |
| [B9](docs/scenarios/B09-bot-technical-compromise.md) | Bot technical compromise | CISO | Channel owner |
| [B10](docs/scenarios/B10-bot-commercial-manipulation.md) | Bot commercial manipulation | Channel owner (CX, Sales) | CFO |
| [B11](docs/scenarios/B11-agentic-execution-failure.md) | Agentic execution failure | CTO | Business continuity owner |
| [B12](docs/scenarios/B12-agentic-unauthorized-commitments.md) | Agentic unauthorized commitments | CFO | General Counsel |
| [B13](docs/scenarios/B13-sovereignty-jurisdiction-continuity.md) | Sovereignty, jurisdiction, continuity | CRO | General Counsel, CIO |
| [B14](docs/scenarios/B14-forgone-and-negative-value.md) | Forgone and negative value | Use-case sponsor (line head) | CFO |
| [B15](docs/scenarios/B15-governance-cost-and-failure.md) | Governance cost and failure | CRO | CFO |

The output is a **net position per use case**, expressed as a range:

```
Net annual position = P(reaches production) × P(delivers value | production) × gross annual value
                      − expected annual loss across B1 to B13
                      − allocated governance cost
```

See [Quantification](docs/06-quantification.md) for how each term is estimated and why the answer is a distribution, not a number.

## Where to start

| If you are... | Start with |
|---|---|
| An executive or board member | [Introduction](docs/01-introduction.md), then the [scenario catalog](docs/scenarios/README.md) |
| A CISO or risk lead setting this up | [Method](docs/03-method.md), [Tiering](docs/05-tiering.md), [Accountability](docs/04-accountability.md) |
| A risk analyst running assessments | [Quantification](docs/06-quantification.md), the [layer pages](docs/layers/README.md), and the [templates](templates/) |
| Mapping to an existing program | [Framework crosswalk](docs/reference/framework-crosswalk.md) |
| Looking for a full example | [Worked example: customer-service chatbot](docs/examples/worked-example-customer-service-chatbot.md) |
| Reviewing the model | [Status and limitations](docs/validation/status-and-limitations.md), [Validation plan](docs/validation/validation-plan.md), [Open questions](docs/validation/open-questions.md) |

The full table of contents is in [docs/README.md](docs/README.md).

## Reading the evidence labels

Factual claims in the documentation carry a short label in brackets, such as `[peer-reviewed]` or `[vendor]`. The label says what kind of source stands behind the claim, so you can judge how much weight it bears. It is not a citation; the link next to it is.

| Label | Means |
|---|---|
| `[peer-reviewed]`, `[RCT]`, `[standard]`, `[legal ruling]`, `[government]` | Strongest sources: published research, standards, rulings, official statements |
| `[industry-body]`, `[analyst]`, `[consulting]`, `[survey]` | Credible but not independently tested: industry bodies, analyst firms, consultancies, surveys |
| `[vendor]` | Data from a company that sells the relevant product. Useful, but read with that in mind |
| `[secondary]` | Reported by someone else; we did not read the primary source |
| `[not re-checked]`, `[unverified]` | We could not confirm the figure for this draft. Treat it as a lead |
| `[illustrative]` | Invented for an example. Not evidence |

The full list, and a log of what we verified for this draft, is in [Evidence labels and verification log](docs/reference/evidence-labels.md).

## What is new and what inspired us

BORA-EAI is a combination of the best from existing work and a novel way of combining the pieces into a coherent outcome that empowers decision-making. You will find inspiration from AWS's generative and agentic AI scoping matrices, the CSA AI Controls Matrix and Capabilities-Based Risk Assessment, FAIR and FAIR-AIR, the Geneva Association's insurer view of GenAI risk, COSO's GenAI capability types, ISO/IEC 23894, 42001 and 42005, the NIST AI RMF, Huwyler's AI threat taxonomy, OWASP's LLM and agentic top 10 lists, and the MIT AI Risk Repository. Credit for those components belongs to their authors.

The parts we built, and which most need testing, are:

- the fifteen-scenario business library and its ownership rule;
- the three-way split of chatbot risk into liability (B8), technical compromise (B9), and commercial manipulation (B10);
- consumption Scope 2e, vendor-enabled embedded AI;
- the six-axis sovereignty profile by deployment model;
- the fast lane and the two override rules on tiering;
- netting value and governance cost against loss, per use case, as a distribution.

## Help us break it

The new parts of BORA-EAI have not been validated, so we want your help testing them.

- **Does it make sense?** Does it answer the questions you, or your executives, would actually ask?
- **Where does it fall short?** Is a scenario missing, merged, owned by the wrong executive, or worded in a way an executive would not recognize?
- **What have we missed?** Published business-level AI risk models, or loss, uplift, and sovereignty evidence we should be using.

Open an issue using one of the [issue templates](.github/ISSUE_TEMPLATE/), submit a pull request (see [CONTRIBUTING.md](CONTRIBUTING.md)), or email **questions@generativesecurity.ai**.

## License and citation

This work is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE). You may share and adapt it, including commercially, as long as you give appropriate credit to Generative Security and indicate if changes were made. Third-party frameworks, standards, and data referenced here remain the property of their owners and are cited, not relicensed.

To cite BORA-EAI, see [CITATION.cff](CITATION.cff), or use:

> Generative Security (2026). *Business Outcome Risk Analysis for Enterprise AI (BORA-EAI)*, working draft v0.1. https://github.com/Generative-Security

---

Maintained by [Generative Security](https://generativesecurity.ai). Background: [What's different about enterprise AI risk](https://blog.generativesecurity.ai/).
