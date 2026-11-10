# Layer 5: Business threat scenarios

> **Executive question:** What could go wrong, in business terms?

## Purpose

Layer 5 identifies which of BORA-EAI's fifteen business threat scenarios apply to the use case and writes each as a statement an executive would recognize. It is the bridge between the structural facts from layers 2 to 4 and the numbers in layers 6 to 8.

## The scenario library

Each scenario is written as a business outcome, has one accountable owner, and is cross-referenced to technical threat catalogs (Huwyler's AI threat taxonomy, the OWASP LLM and agentic top 10 lists, MITRE ATLAS, the MIT AI Risk Repository, and NIST AI 600-1), so the security team can decompose it into STRIDE, ATLAS, or MAESTRO work underneath.

| ID | Scenario | Lens | Accountable |
|---|---|---|---|
| [B1](../scenarios/B01-insider-amplification.md) | Insider amplification | Internal | CISO |
| [B2](../scenarios/B02-sanctioned-ai-leakage.md) | Sanctioned-AI leakage | Internal | CIO (platform owner) |
| [B3](../scenarios/B03-shadow-ai-leakage.md) | Shadow-AI leakage | Internal | CISO |
| [B4](../scenarios/B04-untrusted-ai-artifacts.md) | Untrusted AI artifacts | Internal | CTO |
| [B5](../scenarios/B05-ip-and-license-exposure.md) | IP and license exposure | Both | General Counsel |
| [B6](../scenarios/B06-ai-vendor-concentration.md) | AI vendor and fourth-party concentration | Both | CRO |
| [B7](../scenarios/B07-vendor-enabled-embedded-ai.md) | Vendor-enabled embedded AI | Internal | General Counsel |
| [B8](../scenarios/B08-bot-misrepresentation-liability.md) | Bot misrepresentation liability | Customer-facing | Channel owner (CX) |
| [B9](../scenarios/B09-bot-technical-compromise.md) | Bot technical compromise | Customer-facing | CISO |
| [B10](../scenarios/B10-bot-commercial-manipulation.md) | Bot commercial manipulation | Customer-facing | Channel owner (CX, Sales) |
| [B11](../scenarios/B11-agentic-execution-failure.md) | Agentic execution failure | Both | CTO |
| [B12](../scenarios/B12-agentic-unauthorized-commitments.md) | Agentic unauthorized commitments | Both | CFO |
| [B13](../scenarios/B13-sovereignty-jurisdiction-continuity.md) | Sovereignty, jurisdiction, continuity | Both | CRO |
| [B14](../scenarios/B14-forgone-and-negative-value.md) | Forgone and negative value | Both | Use-case sponsor |
| [B15](../scenarios/B15-governance-cost-and-failure.md) | Governance cost and failure | Both | CRO |

See the [scenario catalog](../scenarios/README.md) for how the library was built and how scenarios relate.

## Method

1. **Screen all fifteen.** For each, use the "applies when" conditions on its page and the facts from layers 2 to 4 to mark it as applicable, not applicable, or uncertain. Record the reason for "not applicable".
2. **Write scenario statements** for each applicable scenario, in the FAIR-AIR form:

   > There is an X% probability in the next 12 months that [threat or failure] in [use case] causes [business outcome], producing a [first- or third-party] loss of $A to $B.

   For a Low tier use case, leave X, A, and B blank: the statement still focuses the qualitative screen.
3. **Select for quantification.**
   - Low: none. Rate each applicable scenario High, Medium, or Low qualitatively, with a one-line reason.
   - Medium: the top three by likely impact.
   - High: all applicable scenarios.
4. **Confirm owners.** The accountable owner for each scenario agrees the statement.
5. **Add MIT causal tags.** For each scenario, record the MIT AI Risk Repository's causal attributes: entity (human or AI), intent (intentional or unintentional), and timing (pre- or post-deployment). This helps the completeness check in Layer 9.

## How layers 2 to 4 point to scenarios

| Structural fact | Scenarios to look at first |
|---|---|
| Scope 1 (consumer terms) or unsanctioned use | B3, B5, B13 |
| Scope 2e (vendor-enabled embedded AI) | B7, B13 |
| Scope 3 to 5 (built in-house) | B4, B5, B9, B11 |
| Copilot or retrieval over internal content | B2, B1 |
| Customer-facing | B8, B9, B10 |
| Agentic scope 3 or 4 | B11, B12, B1 |
| Shared upstream provider, deep supply chain, broad tokens | B6 |
| Inference or storage outside policy; single provider | B13 |
| Any use case | B14, B15 |

## When an event fits no scenario, or two

That is the most useful finding BORA-EAI can produce in its draft state. Record it and report it (see [CONTRIBUTING](../../CONTRIBUTING.md)). The [validation plan](../validation/validation-plan.md) includes a structured test of how cleanly real incidents map to one scenario each.

## Output

A list of applicable scenarios per use case, each with a statement, an accountable owner, MIT causal tags, and a quantify-or-screen decision. The [scenario register template](../../templates/scenario-register.csv) captures this.

Next: [Layer 6: Loss](L6-loss.md)
