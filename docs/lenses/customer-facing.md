# Customer-facing lens

**Applies to:** use cases whose output reaches customers as the company's statement, or that act on a customer's behalf. Customer-service chatbots, sales and booking assistants, AI features in a product, and agents that transact externally.

Any customer-facing use case that makes representations or can grant concessions is at least **Medium** tier, however simple it is. See the [override rules](../05-tiering.md#override-rules).

## The three questions

### 1. What may it say or offer?

A customer-facing AI speaks with the company's voice. Tribunals have treated it that way. In *Moffatt v Air Canada* (2024 BCCRT 149), Air Canada's chatbot told a customer he could claim a bereavement fare reduction after travel, which was not the airline's policy. The tribunal rejected Air Canada's argument that the chatbot was "a separate legal entity that is responsible for its own actions", called that "a remarkable submission", and held that "it makes no difference whether the information comes from a static page or a chatbot" `[legal ruling]` ([McCarthy Tétrault](https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot)).

Define, in writing, what the AI may state (policies, prices, eligibility, advice) and what it may grant (refunds, discounts, credits, exceptions), and where those are enforced.

Scenario: [B8](../scenarios/B08-bot-misrepresentation-liability.md).

### 2. Who is liable when it is wrong, and how does it go wrong?

Customer-facing AI fails in three distinct ways, and BORA-EAI keeps them separate because their owners and controls differ:

| | Liability (B8) | Technical compromise (B9) | Commercial manipulation (B10) |
|---|---|---|---|
| **What happens** | The AI states something false: a policy, price, or piece of advice | The AI is exploited to leak data, misuse its tools, or stop working | A user talks the AI into a concession, discount, refund, or "offer" within what it is technically allowed to do |
| **Needs a vulnerability?** | No | Yes | No |
| **Example** | Air Canada (2024); Cursor's support bot inventing a device policy (2025) | Prompt injection leading to data leakage or tool misuse | Chevrolet of Watsonville's bot "agreeing" to sell a Tahoe for US$1 (2023); Project Vend's shop agent talked into discounts and giveaways (2025) |
| **Main lever** | What the AI may state, and its knowledge sources | Security testing and input, output, and tool controls | Concession limits enforced outside the model |
| **Accountable** | Channel owner | CISO | Channel owner |

Existing security frameworks fold commercial manipulation into prompt injection or goal hijack. OWASP's agentic top 10 covers "agent goal hijack" (ASI01), and its ASI09 covers the reverse direction, agents socially engineering humans. We found no major framework that treats persuasion of a bot's business logic as its own class `[industry-body]`. BORA-EAI does, because a bot can be secure from a cyber perspective and still give away money.

Scenarios: [B8](../scenarios/B08-bot-misrepresentation-liability.md), [B9](../scenarios/B09-bot-technical-compromise.md), [B10](../scenarios/B10-bot-commercial-manipulation.md).

### 3. What revenue does it protect or put at risk?

Customer-facing AI is usually justified by cost to serve, availability, or conversion. It also puts revenue at risk when it has to be pulled. DPD disabled the AI part of its customer-service chat in January 2024 after a customer prompted it to swear and call DPD the "worst delivery firm in the world" `[secondary]`. Several car dealerships disabled their chatbots after the Chevrolet episode `[secondary]`. In the Verizon 2026 Breach Impact Study, business interruption had the highest median loss of any category, about US$90,000 per insurance claim `[survey]`.

Assess: the revenue or cost-to-serve the use case affects, what happens to that process if the AI is pulled for a week, and the fallback.

Scenarios: [B14](../scenarios/B14-forgone-and-negative-value.md) for value, [B9](../scenarios/B09-bot-technical-compromise.md) and [B10](../scenarios/B10-bot-commercial-manipulation.md) for interruption.

## Regulatory exposure

- **Disclosure.** From 2 August 2026, the EU AI Act requires that people be told when they are interacting with an AI system (Article 50); this date was not deferred by the 2026 Digital Omnibus amendments `[secondary: law-firm summaries]`.
- **Deceptive claims.** The US FTC's "Operation AI Comply" (September 2024) included action against DoNotPay's "robot lawyer" claims, settled for US$193,000 `[government, via secondary]`.
- **Consumer law.** Australian Consumer Law's misleading-conduct provisions apply to what a bot says in principle. We found no ACCC action specific to chatbots as of November 2026.
- **Automated decisions.** From 10 December 2026, Australian privacy policies must disclose automated decisions that significantly affect individuals `[secondary: law-firm summary]`.

See [Regulatory context](../reference/regulatory-context.md).

## Typical loss profile

Third-party and reputational: honored concessions, tribunal awards, consumer-law exposure, regulatory action, viral coverage, and lost revenue while the AI is offline. Direct awards are often small; the precedent and the publicity are not.

## Typical value profile

Cost to serve, availability, conversion, and retention. Customer-support uplift evidence is the strongest in the literature (about 14% average resolutions per hour, more for novices), but evidence on replacing rather than assisting human agents is mixed: Commonwealth Bank reversed a decision to replace 45 roles with a chatbot, and Gartner expects half of organizations that planned major service-workforce cuts to abandon those plans by 2027.

## Typical owners

Channel owner (B8, B10), CISO (B9), CFO (B12 and consulted on B10), General Counsel (consulted on B8, B12), and the business sponsor for value (B14).

## Quick screen for customer-facing use cases

| Question | If yes, look at |
|---|---|
| Does it state policies, prices, eligibility, or advice? | B8 |
| Can it grant refunds, discounts, credits, or exceptions? | B10 |
| Are those limits enforced in the prompt, or in a system of record? | B10 (prompt-only is a finding) |
| Does it retrieve customer or account data, or call tools? | B9, B2 |
| Can it place orders, make payments, or sign up customers? | B12 |
| Is it disclosed as AI? | Regulatory (EU AI Act Article 50) |
| What happens to revenue and service if it is offline for a week? | B14, B6 |
