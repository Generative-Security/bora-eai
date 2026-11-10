# Lenses

Internal and customer-facing AI fail in different ways, are owned by different executives, and are worth different things. Applying one lens to both mis-rates one of them. Layer 1 selects the lens for each use case, and the lens shapes how layers 5 to 7 are applied.

| | [Internal lens](internal.md) | [Customer-facing lens](customer-facing.md) |
|---|---|---|
| **Typical use cases** | Coding assistants, copilots over company data, internal agents, document processing | Customer-service chatbots, sales assistants, AI in a product, agents acting for customers |
| **Main questions** | What can it see? What can it do under whose identity? Is the productivity gain real for the people using it? | What may it say or offer? Who is liable when it is wrong? What revenue does it protect or put at risk? |
| **Scenarios in focus** | B1, B2, B3, B4, B7, B11 | B8, B9, B10, B12 |
| **Scenarios in both** | B5, B6, B13, B14, B15 | B5, B6, B13, B14, B15 |
| **Value is mostly** | Labor productivity and cycle time | Revenue, retention, cost to serve |
| **Loss is mostly** | First-party: data exposure, IP, operational disruption | Third-party and reputational: liability, consumer law, public failure |
| **Typical owners** | CISO, CIO, CTO | Channel owner, General Counsel, CFO |
| **Override rule** | Regulated personal data | Customer-facing representations or concessions |

## Choosing the lens

- If any output reaches a customer as the company's statement, or any action is taken on a customer's behalf, use the **customer-facing** lens, even if employees also use the tool.
- If a use case is internal today but planned for customer exposure, assess it under the customer-facing lens before that change, as a material change.
- Agents that act on external systems (suppliers, marketplaces, payment rails) carry customer-facing style exposure in [B12](../scenarios/B12-agentic-unauthorized-commitments.md). Screen B12 under both lenses.

## Why not one lens

A single lens tends to fail in one of two directions:

- A **security-only** lens rates a customer-service bot by its technical attack surface and misses that it can be talked into a refund it should never grant, or can state a policy that does not exist. Neither needs a vulnerability. See [B8](../scenarios/B08-bot-misrepresentation-liability.md) and [B10](../scenarios/B10-bot-commercial-manipulation.md).
- A **liability-only** lens rates an internal copilot as low risk because no customer sees it, and misses that it can surface every overshared document in the company to any employee, or to an outside attacker through injected content. See [B2](../scenarios/B02-sanctioned-ai-leakage.md).

BORA-EAI looks harder at any use case that touches regulated personal data or speaks for the company to its customers, however little else it can do. That is our judgment, encoded as the two [override rules](../05-tiering.md#override-rules).
