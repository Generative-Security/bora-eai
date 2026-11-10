# B8: Bot misrepresentation liability

| | |
|---|---|
| **Accountable** | Channel owner (customer experience) |
| **Consulted** | General Counsel |
| **Lens** | Customer-facing |
| **Loss domain** | Regulatory and compliance (legal); reputational and market |
| **Party** | Mostly third-party |
| **Status** | Draft v0.1 |

## Business outcome

A customer-facing AI states a policy, price, eligibility rule, or piece of advice that is false, and the company is held to it, sanctioned for it, or publicly embarrassed by it.

## Applies when

- The AI answers questions about policies, prices, eligibility, products, or rights.
- Its knowledge sources are incomplete, outdated, or inconsistent.
- It gives advice in a regulated area (financial, health, legal, insurance).
- Any customer-facing representation triggers the override to at least Medium tier.

## What it looks like

- A support bot invents a refund or bereavement policy.
- A sales assistant states a price, discount, or product capability that is wrong.
- A bot gives regulated advice it is not permitted to give.
- A product's marketing overstates what its AI can do (a variant regulators have pursued).

Nothing needs to be hacked. The AI simply gets it wrong, often fluently and with confidence.

## Boundaries

- **B9** requires an attacker exploiting the AI. B8 needs no attacker.
- **B10** is a user deliberately persuading the AI to concede something. In B8 the customer asks in good faith and the AI is wrong. Where a user engineers a false statement in order to rely on it, record B10.
- **B14** covers the value lost when AI outputs degrade outcomes generally. B8 covers the liability for specific statements.

## Evidence

- **Moffatt v Air Canada, 2024 BCCRT 149 (February 2024).** Air Canada's chatbot told a customer he could buy a full-fare ticket and claim a bereavement reduction afterwards; no such policy existed. The tribunal rejected Air Canada's argument that the chatbot was "a separate legal entity that is responsible for its own actions", calling it "a remarkable submission", and held that "it makes no difference whether the information comes from a static page or a chatbot". Air Canada was ordered to pay CA$812.02 for negligent misrepresentation `[legal ruling]` ([McCarthy Tétrault](https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot)).
- **Cursor (April 2025).** The company's AI support bot invented a one-device subscription policy after a session bug logged users out; a co-founder publicly called it "an incorrect response from a front-line AI support bot" `[secondary]`.
- **FTC Operation AI Comply (September 2024).** Action against DoNotPay's "robot lawyer" claims; DoNotPay agreed to pay US$193,000 `[government, via secondary]` ([Morrison Foerster](https://www.mofo.com/resources/insights/241008-ftc-first-ai-related-enforcement-actions)).
- **Insurance market.** Lloyd's-market cover for losses from AI chatbot errors launched in 2025, backed by Armilla `[secondary]`.
- **Australia.** Australian Consumer Law's misleading-conduct provisions apply in principle. We found no ACCC action specific to chatbots as of November 2026.

## Business impact

| Loss form | Examples |
|---|---|
| Fines and judgments | Tribunal awards; consumer-law penalties; regulatory action on deceptive AI claims |
| Response | Legal review; corrections to affected customers |
| Reputation | Viral coverage; loss of customer trust |
| Productivity | Bot pulled offline while fixed |

Direct awards are often small. The precedent and the publicity are the larger cost.

## Levers

| Lever | Type | Owner |
|---|---|---|
| Define in writing what the AI may and may not state, and in which topics it must hand off to a human | Directive | Channel owner |
| Ground policy, price, and eligibility answers in a single maintained source of truth | Preventive | Channel owner |
| Route high-stakes topics (refunds, legal rights, regulated advice) to deterministic answers or humans | Preventive | Channel owner |
| Pre-release and ongoing evaluation for groundedness and accuracy | Detective | Channel owner with CTO |
| Clear AI disclosure (required in the EU from 2 August 2026) | Directive | General Counsel |
| Process to honor or correct promptly when the AI is wrong | Corrective | Channel owner |
| Review of marketing claims about AI capability | Directive | General Counsel |

Disclaimers alone are not a control. In *Moffatt*, the tribunal held Air Canada responsible for the bot's statement even though the correct policy was available elsewhere on its site.

## Quantification notes

- **Frequency:** use evaluation results (rate of incorrect answers on policy topics) multiplied by volume of such conversations, then by the share that lead to a claim or complaint.
- **Magnitude:** per-claim amounts are usually small; model the tail on regulatory action and reputational events.

## Example scenario statement

> There is a 30% to 60% probability in the next 12 months that our service assistant misstates a refund or eligibility policy to customers who rely on it, producing a third-party loss of $20,000 to $400,000 in honored claims, complaints handling, and legal costs, with a 2% to 5% probability of regulatory action.

## Questions for the accountable executive

1. What is our bot allowed to tell customers, and is that written down?
2. Where do its answers on policies and prices come from, and who keeps that source current?
3. When it is wrong, do we honor, correct, or argue, and who decides?

## Crosswalk

| Framework | Reference |
|---|---|
| Huwyler taxonomy | Unreliable Outputs: Factual Hallucination, Source Fabrication |
| OWASP LLM 2025 | LLM09 Misinformation |
| MIT AI Risk Repository | 3.1 False or misleading information; 5.1 Overreliance and unsafe use |
| NIST AI 600-1 | Confabulation; Information Integrity |
| Geneva Association | Regulatory and compliance; reputational and market (E&O is the closest insurance line) |
| CSA AICM | AIS, GRC, MDS |

## Open questions

- Will courts treat a chatbot's statement as a binding offer, rather than a misrepresentation? We found no ruling on that question.
