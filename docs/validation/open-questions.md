# Open questions

Questions we have not resolved and would like reviewers to weigh in on. Each links to the page where it matters most.

## Scope of the scenario library

1. **Should bias have its own business threat scenario?** Huwyler's taxonomy and the Geneva Association both treat bias as a domain. BORA-EAI currently routes the organizational consequence (for example, discrimination claims) through the scenario where it arises, and leaves harm to individuals to ISO/IEC 42005 impact assessment. Is that enough for hiring, credit, and eligibility use cases? ([Crosswalk](../reference/framework-crosswalk.md#scenarios-to-huwylers-taxonomy))
2. **Should model drift have its own scenario?** Gradual degradation of a deployed use case is currently part of B14 (negative value).
3. **Should "agent as insider" be separated from B1?** It has different detection and arguably different ownership. ([B1](../scenarios/B01-insider-amplification.md))
4. **Should B5 split into inbound (licenses we accept) and outbound (warranties we give)?** ([B5](../scenarios/B05-ip-and-license-exposure.md))
5. **Are deepfake-enabled fraud and impersonation attacks *on* the organization in scope?** BORA-EAI covers the organization's *use* of AI. AI-enabled attacks by outsiders (for example, deepfake executive voice fraud) are a real business risk but arguably belong in the general cyber threat model. Where should the line sit?

## Ownership

6. **Is the channel owner the right accountable executive for B8?** The rule (holder of the main lever) says yes. Some reviewers may prefer General Counsel. ([B8](../scenarios/B08-bot-misrepresentation-liability.md))
7. **Who should own B2 when there is no single platform owner** (for example, several copilots across collaboration suites)?
8. **Is the CRO the right owner for B15,** or should governance-cost accountability sit with whoever funds the program?

## Method

9. **Are the provisional CBRA scales and thresholds reasonable** until CSA's own are available? ([Tiering](../05-tiering.md#provisional-anchor-scales))
10. **How should portfolio concentration be modeled** when many use cases depend on one provider? ([B6](../scenarios/B06-ai-vendor-concentration.md))
11. **How should correlated losses be simulated** across scenarios within a use case and across the portfolio?
12. **Should the 1-in-20-year loss be the default tail metric,** or should organizations set it to match their own appetite statements?
13. **How should the informal value of shadow AI be credited** when deciding whether to sanction a tool? ([B3](../scenarios/B03-shadow-ai-leakage.md), [B14](../scenarios/B14-forgone-and-negative-value.md))
14. **Can competitive erosion be estimated at all** with available evidence? ([Layer 7](../layers/L7-value.md#cost-of-delay))

## External alignment

15. **Should "social engineering of AI" be proposed to OWASP and MITRE ATLAS as a distinct category?** ([B10](../scenarios/B10-bot-commercial-manipulation.md))
16. **Is there a sovereignty-by-deployment-model framework** from CSA, ENISA, the EU, or the Australian Signals Directorate that we missed? ([Layer 3](../layers/L3-sovereignty-profile.md))
17. **Would insurers find BORA-EAI scenario library useful** for underwriting AI exposure, and what would they need added?

Please answer any of these by opening an issue or emailing questions@generativesecurity.ai.
