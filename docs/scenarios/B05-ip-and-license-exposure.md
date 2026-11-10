# B5: IP and license exposure

| | |
|---|---|
| **Accountable** | General Counsel |
| **Consulted** | CTO, Procurement |
| **Lens** | Both |
| **Loss domain** | Regulatory and compliance (IP); reputational |
| **Party** | Mostly third-party; first-party for lost IP |
| **Status** | Draft v0.1 · thinner evidence base than other scenarios |

## Business outcome

The organization faces infringement claims over AI-generated output, uses a model or dataset outside its license terms, loses control of proprietary data because it was used to train a provider's model, or finds that a customer's IP indemnity claim lands on it rather than on the AI vendor.

## Applies when

- AI output is published, shipped in products, or given to customers (code, images, text, designs).
- Open-weight models or datasets are used commercially.
- Fine-tuned or customized models are deployed (vendor indemnities often exclude them).
- AI is accessed through an intermediary or marketplace whose terms differ from the model provider's.
- Consumer-tier tools are used for work (often no indemnity at all).
- The organization's own contracts give customers IP warranties over deliverables.

## What it looks like

- **Output infringement:** generated code reproduces licensed code, or generated images resemble protected works, and a rights holder claims against the organization that published them.
- **License breach:** an open-weight model with restricted commercial terms, or a dataset with non-commercial terms, is used in a commercial product.
- **Training exposure:** proprietary content enters a provider's training data under consumer terms, or after a terms change (see B7).
- **Indemnity gap:** the organization assumed a vendor's IP indemnity covered it, but the use case falls outside the vendor's conditions.
- **Upstream litigation:** a model provider's own training-data litigation creates uncertainty about continued use or terms.

## Boundaries

- **B4** is the security side of third-party artifacts. B5 is the legal side.
- **B7** covers vendors changing terms in software already owned. Where the change concerns training on customer content, the legal consequence is B5 and the contractual exposure is B7; record the primary owner's view.
- **B3** covers data sent to unsanctioned services. When the main concern is IP in that data rather than privacy, B5 applies too.

## Evidence

This scenario has a thinner evidence base than the others. In particular, we found no ruling holding an enterprise *deployer or user* liable for infringing AI output as of November 2026.

- **Vendor IP indemnities exist, with conditions.** Microsoft's Copilot Copyright Commitment covers commercial Microsoft 365 Copilot, GitHub Copilot, Azure OpenAI, and Copilot Studio, conditional on using Microsoft's guardrails. OpenAI's Copyright Shield covers the generally available API and ChatGPT Enterprise, excluding some customized-model outputs. Google extends Cloud IP indemnification to Gemini. Coverage through cloud marketplaces depends on the intermediary's terms, and fine-tuned models are commonly excluded `[secondary: advisory firm summary; check current terms]` ([Redress Compliance](https://redresscompliance.com/ai-ip-indemnification-enterprise-copyright-protection.html)).
- **Training-side litigation against providers:**
  - *Bartz v. Anthropic*: a US$1.5 billion class settlement over books used in training received preliminary approval in September 2025 `[secondary]`.
  - *Thomson Reuters v. Ross Intelligence* (February 2025): the court rejected Ross's fair-use defense for training a (non-generative) legal AI on Westlaw content `[secondary]`.
  - *Getty Images v. Stability AI* (UK High Court): Getty's main copyright claims were largely dismissed, with limited trademark findings `[secondary]` ([UK Judiciary](https://www.judiciary.uk/judgments/getty-images-v-stability-ai/)).
  - *New York Times v. OpenAI and Microsoft*: in discovery as of early 2026 `[secondary]` ([Traverse Legal](https://www.traverselegal.com/blog/ai-copyright-litigation-where-the-key-cases-stand/)).
- **Training-terms changes** by Zoom (2023), Adobe (2024), and WeTransfer (2025) show how proprietary content can come within a vendor's training rights (see [B7](B07-vendor-enabled-embedded-ai.md)).

These cases mostly concern model developers, not deployers. For an enterprise, the main business exposures are the indemnity gap and the commercial use of models and data outside their terms.

## Business impact

| Loss form | Examples |
|---|---|
| Fines and judgments | Infringement damages and settlements; contractual indemnity payouts to customers |
| Response | Legal defense, takedown and remediation of published output |
| Replacement | Replacing a model or dataset that cannot be used commercially |
| Competitive advantage | Proprietary content absorbed into a provider's training data |

## Levers

| Lever | Type | Owner |
|---|---|---|
| License review of open-weight models and datasets before commercial use | Preventive | General Counsel with CTO |
| Map each use case to the vendor indemnity that actually applies, including intermediary terms | Directive | General Counsel with Procurement |
| Meet indemnity conditions (required guardrails and filters) | Preventive | CTO |
| Policy on using AI output in products and customer deliverables | Directive | General Counsel |
| Contract terms: no training on customer content, notice of changes | Preventive | Procurement (see B7) |
| Review the organization's own IP warranties to customers in light of AI use | Directive | General Counsel |
| Code provenance and similarity scanning for generated code | Detective | CTO |

## Quantification notes

- **Frequency:** low for most deployers today, and poorly measured. Estimate per use case based on how much output is published or shipped.
- **Magnitude:** heavy-tailed. Most exposures are remediation; a few could be large. Note the indemnity position explicitly: a covered exposure shifts magnitude to the vendor up to its cap.

## Example scenario statement

> There is a 2% to 8% probability in the next 12 months that code generated by the fine-tuned internal coding model, which falls outside the vendor's indemnity, leads to an infringement claim from a third party, producing a loss of $100,000 to $2 million in defense, settlement, and remediation.

## Questions for the accountable executive

1. For each AI use case that produces output we ship or publish, which indemnity covers us, and what conditions must we meet?
2. Are we using any open-weight models or datasets outside their license terms?
3. Have we promised customers IP warranties over work that is now partly AI-generated?

## Crosswalk

| Framework | Reference |
|---|---|
| Huwyler taxonomy | IP Threat domain |
| Geneva Association | Regulatory and compliance (including IP and copyright) |
| OWASP LLM 2025 | LLM03 Supply Chain (licensing) |
| MIT AI Risk Repository | 6.3 Devaluation of human effort (closest available; imperfect fit) |
| NIST AI 600-1 | Intellectual Property |
| CSA AICM | STA, GRC, DSP |

## Open questions

- Should B5 be split further into inbound (licenses we accept) and outbound (warranties we give)?
- What evidence exists of deployer-level infringement claims, settled privately, that would inform frequency?
