# Business threat scenario catalog

Fifteen business threat scenarios describe what an AI use case can do to the business, in terms the accountable executive recognizes. Every scenario has exactly one accountable owner. Each is cross-referenced to technical threat catalogs so the security team can decompose it.

| ID | Scenario | Business outcome, in one line | Lens | Accountable (A) | Consulted (C) | Evidence base |
|---|---|---|---|---|---|---|
| [B1](B01-insider-amplification.md) | Insider amplification | An employee, or an agent acting as one, uses AI to find, gather, or remove data at machine speed | Internal | CISO | CHRO | Moderate (negligent); thin (malicious) |
| [B2](B02-sanctioned-ai-leakage.md) | Sanctioned-AI leakage | An approved copilot or retrieval system exposes data to people who should not see it, inside or outside | Internal | CIO (platform owner) | CISO | Moderate |
| [B3](B03-shadow-ai-leakage.md) | Shadow-AI leakage | Data goes to AI services with no contract, data agreement, or notification duty | Internal | CISO | CIO, Procurement | Strong |
| [B4](B04-untrusted-ai-artifacts.md) | Untrusted AI artifacts | A model, extension, MCP server, or agent skill someone installed runs malicious code or leaks data | Internal | CTO | CISO | Strong |
| [B5](B05-ip-and-license-exposure.md) | IP and license exposure | AI output infringes, a model or dataset is used outside its license, or proprietary data trains someone else's model | Both | General Counsel | CTO, Procurement | Thin for deployers |
| [B6](B06-ai-vendor-concentration.md) | AI vendor and fourth-party concentration | An AI vendor's failure or compromise cascades through integrations or a shared upstream provider | Both | CRO | CIO, Procurement | Moderate |
| [B7](B07-vendor-enabled-embedded-ai.md) | Vendor-enabled embedded AI | A vendor switches on AI, changes training terms, or adds a model sub-processor in software already owned | Internal | General Counsel | DPO, Procurement | Moderate (pattern); thin (loss) |
| [B8](B08-bot-misrepresentation-liability.md) | Bot misrepresentation liability | A customer-facing AI states false policy, prices, or advice, and the company is held to it | Customer-facing | Channel owner (CX) | General Counsel | Moderate |
| [B9](B09-bot-technical-compromise.md) | Bot technical compromise | A customer-facing AI is exploited to leak data, misuse tools, or stop working | Customer-facing | CISO | Channel owner | Moderate |
| [B10](B10-bot-commercial-manipulation.md) | Bot commercial manipulation | A user persuades a customer-facing AI to grant concessions within what it is technically allowed to do | Customer-facing | Channel owner (CX, Sales) | CFO | Moderate (pattern); thin (loss) |
| [B11](B11-agentic-execution-failure.md) | Agentic execution failure | An agent deletes, corrupts, overspends, or cascades errors through systems it has credentials for | Both | CTO | Business continuity owner | Moderate |
| [B12](B12-agentic-unauthorized-commitments.md) | Agentic unauthorized commitments | An agent pays, orders, or commits the company beyond its intent or authority | Both | CFO | General Counsel | Forward-looking |
| [B13](B13-sovereignty-jurisdiction-continuity.md) | Sovereignty, jurisdiction, continuity | Data is processed outside permitted jurisdictions, compelled by foreign law, or access is lost | Both | CRO | General Counsel, CIO | Moderate (facts); thin (loss) |
| [B14](B14-forgone-and-negative-value.md) | Forgone and negative value | Competitors capture value while we wait, or deployed AI makes outcomes worse | Both | Use-case sponsor | CFO | Strong (uplift); thin (erosion) |
| [B15](B15-governance-cost-and-failure.md) | Governance cost and failure | Control spend does not reduce exposure, or absent controls sink the project | Both | CRO | CFO | Thin |

"Evidence base" is our rough judgment of how much public evidence exists for the scenario's frequency and loss, not of how serious it is. Thin evidence is a reason to estimate carefully, not a reason to ignore a scenario.

## How the library was built

The library was built to cover ten exposures executives raised that no single existing framework covered together: insider threat using AI; data exfiltration through authorized and unauthorized AI; tools and models employees download, and the extended supply chain; AI embedded in purchased software; customer-facing chatbots' legal risk; chatbots being hacked; chatbots being socially engineered; the opportunity cost of not using AI; the internal cost of governance; and data sovereignty across deployment models. Two more areas were added because the evidence demanded them: agents acting on business processes, and IP and license exposure.

Each candidate scenario was kept separate from its neighbors only when it had a **different accountable owner, a different dominant loss type, or a different main control lever**. That rule produced three deliberate splits:

- **Sanctioned (B2) versus shadow (B3) leakage:** different owners (platform owner versus CISO) and different levers (permission hygiene versus detection plus alternatives).
- **The three-way chatbot split (B8, B9, B10):** liability, technical compromise, and commercial manipulation need different controls, and two of the three need no vulnerability at all.
- **Agentic execution failure (B11) versus unauthorized commitments (B12):** operational loss owned by engineering versus financial and contractual loss owned by finance.

Third-party AI was split the same way, into untrusted artifacts (B4, a security problem) and IP and license exposure (B5, a legal problem).

## Scenario IDs

IDs are permanent once published. A new scenario takes the next free number. A retired scenario keeps its ID and is marked retired. Never renumber a published ID. The loss sum in the [net position](../06-quantification.md) runs over B1 to B13; B14 and B15 are carried by the value and governance terms. If a new loss scenario is added later, the loss sum lists it explicitly.

## Page structure

Every scenario page has the same sections:

- **Summary table:** owner, lens, loss domain, party.
- **Business outcome:** one sentence an executive would recognize.
- **Applies when:** structural conditions from layers 2 to 4 that make the scenario relevant.
- **What it looks like:** concrete forms.
- **Boundaries:** how it differs from neighboring scenarios.
- **Evidence:** incidents and data, with [evidence labels](../reference/evidence-labels.md).
- **Business impact:** loss forms and who bears them.
- **Levers:** business-level treatments and who owns them.
- **Quantification notes:** how to estimate frequency and magnitude.
- **Example scenario statement:** in the FAIR-AIR form.
- **Questions for the accountable executive.**
- **Crosswalk:** Huwyler, OWASP, MITRE ATLAS, MIT AI Risk Repository, NIST AI 600-1, CSA AICM.
- **Open questions.**

Crosswalk identifiers follow OWASP Top 10 for LLM Applications 2025, OWASP Top 10 for Agentic Applications (December 2025 edition), MITRE ATLAS, the MIT AI Risk Repository domain taxonomy, NIST AI 600-1's twelve GenAI risks, and CSA AICM domain codes. MITRE ATLAS technique IDs should be checked against the current ATLAS release before use in formal mappings.

## Scenarios by lens and layer driver

| Driver from layers 2 to 4 | Scenarios |
|---|---|
| Consumer terms or unsanctioned | B3, B5, B13 |
| Vendor-enabled embedded AI (Scope 2e) | B7, B13 |
| Built in-house (Scopes 3 to 5) | B4, B5, B9, B11 |
| Retrieval over internal content | B2, B1 |
| Customer-facing | B8, B9, B10 |
| Agentic Scope 3 or 4 | B11, B12, B1 |
| Shared upstream provider or broad integrations | B6 |
| Every use case | B14, B15 |
