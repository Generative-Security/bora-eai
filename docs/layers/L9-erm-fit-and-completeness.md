# Layer 9: ERM fit and completeness

> **Executive question:** Does it fit risk appetite, and did we miss anything?

## Purpose

Layer 9 closes every assessment. It nets the terms into a decision, compares the result with the organization's risk appetite, translates it into the enterprise risk management (ERM) categories executives already use, and checks the assessment for blind spots.

## 1. Net and decide

For Medium and High use cases, combine layers 6 to 8 into the [net position](../06-quantification.md): the 10th, 50th, and 90th percentiles, the probability it is negative, and the 1-in-20-year loss per scenario. For Low tier, summarize the qualitative screen. Then choose a [decision](../03-method.md#decisions): approve, approve with conditions, redesign, defer, or stop.

## 2. Compare with risk appetite

Risk appetite for AI should be stated in the terms the board already uses. Examples of BORA-EAI-compatible appetite statements:

- No single AI use case may carry a 1-in-20-year loss above [amount] without board approval.
- Customer-facing AI may not make binding commitments outside limits enforced by systems of record.
- No AI use case may process regulated personal data outside [jurisdiction] without CRO approval.
- We accept a probability of negative net position up to [percentage] for pilots structured as options with a defined exit.
- Agents may not hold standing credentials that can delete production data or its backups.

A use case that breaches appetite is escalated to the owner named in the appetite statement, usually the CRO or the board risk committee.

## 3. Translate into ERM

BORA-EAI is designed to sit inside existing standards rather than beside them.

| Standard | How BORA-EAI fits |
|---|---|
| **ISO/IEC 23894:2023** (AI risk management) | Mirrors the clause structure of ISO 31000:2018. Its process (scope and criteria; identification, analysis, evaluation; treatment; monitoring; recording) maps onto BORA-EAI layers 1 to 9. Its Annex A (objectives) and Annex B (risk sources) can serve as checklists. `[standard]` |
| **ISO/IEC 42001:2023**, clause 6.1.2 (AI risk assessment) | Requires assessing effects on the **organization, individuals, and societies**, and their likelihood, with consistent, valid, and comparable results. BORA-EAI can serve as this process for the organizational side. `[standard]` |
| **ISO/IEC 42001**, clause 6.1.3 (AI risk treatment) | Treatment options and control selection against Annex A, with a statement of applicability. BORA-EAI scenario levers and tier-based AICM baselines feed this. |
| **ISO/IEC 42001**, clause 6.1.4, and **ISO/IEC 42005:2025** (AI system impact assessment) | Assess effects on **individuals, groups, and societies**. ISO/IEC 42005 puts business and financial impact outside its own scope, so BORA-EAI complements it: 42005 covers people and society, BORA-EAI covers the business. Results from 42005 feed back into 6.1.2. `[standard]` |
| **NIST AI RMF 1.0** | BORA-EAI layers map to GOVERN (accountability, Layer 2 and the owner matrix), MAP (layers 1 to 5, and MAP 3.1 and 3.2 in Layer 7), MEASURE (layers 6 to 8), and MANAGE (Layer 9 decisions). `[standard]` |
| **COSO ERM** and enterprise risk registers | Roll each scenario into the organization's risk categories (strategic, operational, financial, compliance, reputational). The [crosswalk](../reference/framework-crosswalk.md) gives a default mapping. |
| **Australia: Guidance for AI Adoption (AI6)** | The six practices (decide who is accountable; understand impacts and plan accordingly; measure and manage risks; share essential information; test and monitor; maintain human control) map to BORA-EAI layers in the crosswalk. `[government]` |

## 4. Check completeness

Most AI risk frameworks cover only a fraction of the risk landscape. The MIT AI Risk Repository, a peer-reviewed meta-review of 74 documents and 1,725 risks, found that frameworks cover on average 8 of its 24 subdomains `[peer-reviewed]` ([Slattery et al., *Patterns*, 2026](https://www.arxiv.org/pdf/2408.12622)). BORA-EAI uses the repository as a completeness check, not a scoring engine.

For each assessed use case:

1. List the MIT subdomains the applicable scenarios touch (each scenario page gives its mapping).
2. Look for empty domains that plausibly apply. Enterprise models commonly miss 5.1 (overreliance and unsafe use), 6.4 (competitive dynamics), 6.5 (governance failure), and 7.6 (multi-agent risks).
3. Record subdomains that are deliberately out of scope, with the reason. Enterprise deployers typically scope out frontier-developer domains such as 7.1 (misaligned goals), 7.2 (dangerous capabilities), and 7.5 (AI welfare and rights). Record that as a decision, not an omission.
4. Use the causal tags from Layer 5 (entity, intent, timing) to check that both human and AI causes, intentional and unintentional, are represented.

A gap that does not fit any BORA-EAI scenario is a finding for the model itself. Please [report it](../../CONTRIBUTING.md).

## Output

- A decision and review date in the use-case register.
- Register entries in ERM categories, owned by the accountable executives.
- A coverage-gap note.
- For High tier, a board summary (see the [template](../../templates/board-summary.md)).

Back to: [Layers](README.md) · Next: [Lenses](../lenses/README.md)
