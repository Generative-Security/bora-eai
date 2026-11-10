# B10: Bot commercial manipulation

| | |
|---|---|
| **Accountable** | Channel owner (customer experience, sales) |
| **Consulted** | CFO |
| **Lens** | Customer-facing |
| **Loss domain** | Operational (financial); reputational and market |
| **Party** | First-party |
| **Status** | Draft v0.1 · proposed as a distinct class |

## Business outcome

A user persuades a customer-facing AI to grant a concession, discount, refund, credit, or "offer" that is within what it is technically able to do but outside what the business intended, and the company either honors it or suffers for refusing.

## Applies when

- The AI can grant, promise, or negotiate anything of value: refunds, discounts, credits, upgrades, waived fees, exceptions to policy.
- Limits on those concessions are expressed as instructions in the prompt rather than enforced by the system the AI calls.
- The AI negotiates or sells on the company's behalf.
- Any customer-facing concession triggers the override to at least Medium tier.

## What it looks like

- A user instructs the bot to agree to anything and to call it legally binding, then asks for an absurd price.
- A customer argues, flatters, or role-plays the bot into a larger refund or credit than policy allows.
- An agent running a shop or sales process is talked into discounts and giveaways.
- Users share a working script, and the concession is claimed at scale.

This is social engineering of the bot's commercial logic, not hacking. The bot is not exploited in a security sense; it is persuaded.

## Why this is a distinct scenario

Existing security frameworks fold this into prompt injection or goal hijack. The OWASP Top 10 for Agentic Applications (December 2025) covers agent goal hijack (ASI01), and its ASI09 covers the reverse direction, agents socially engineering *humans*. We found no major framework that treats persuasion of a bot's business logic as its own class `[industry-body]`.

BORA-EAI separates it because:

- **The owner is different.** The lever is the commercial policy and how it is enforced, which belongs to the channel and finance owners, not the CISO.
- **The controls are different.** Hard limits enforced in systems of record, and offers confirmed by deterministic systems, matter more than injection filters.
- **A security review can miss it entirely.** A bot can pass a penetration test and still give away money.

## Boundaries

- **B9** breaches the bot's intended boundaries. B10 stays within them. If the bot can technically issue a 100% refund and is talked into it, that is B10. If it is tricked into reaching a system it should not reach, that is B9.
- **B8** is a good-faith customer receiving a false statement. B10 is a user deliberately engineering a concession.
- **B12** covers agents committing the company to third parties on their own initiative. B10 covers concessions extracted by the counterparty.

## Evidence

- **Chevrolet of Watsonville (December 2023).** A user instructed the dealership's chatbot (supplied by Fullpath) to end every reply with "and that's a legally binding offer – no takesies backsies", then got it to agree to sell a 2024 Chevy Tahoe (starting MSRP US$58,195) for US$1. No sale was honored and the matter was not litigated. Dealerships disabled bots after a spike in similar attempts `[secondary]` ([VentureBeat](https://venturebeat.com/ai/a-chevy-for-1-car-dealer-chatbots-show-perils-of-ai-for-customer-service)).
- **DPD (January 2024).** After a system update, a customer prompted the parcel firm's chatbot to swear, write a poem criticizing the company, and call DPD the "worst delivery firm in the world". DPD disabled the AI element `[secondary]`. This was manipulation for reputational damage rather than a concession.
- **Project Vend (June 2025).** In an experiment by Anthropic and Andon Labs, a Claude-based agent running an office shop was talked by employees into discounts and giveaways and lost money `[secondary]` ([TechCrunch](https://techcrunch.com/2025/06/28/anthropics-claude-ai-became-a-terrible-business-owner-in-experiment-that-got-weird)). It is the clearest public example of persuasion-based manipulation of an agent's commercial logic.
- **Gap:** we found no public, quantified loss from honored bot concessions, and no ruling on whether a bot's "offer" is binding.

## Business impact

| Loss form | Examples |
|---|---|
| Productivity (financial) | Honored refunds, discounts, credits; margin leakage at scale |
| Fines and judgments | Disputes over refused "offers"; consumer-law complaints |
| Reputation | Viral screenshots; brand appearing careless |
| Productivity (operational) | Bot disabled; traffic back to human agents |

## Levers

| Lever | Type | Owner |
|---|---|---|
| Enforce concession limits in the system of record the AI calls, not in its prompt | Preventive | Channel owner with CFO |
| Require deterministic confirmation for any offer, price, or concession above a threshold | Preventive | Channel owner |
| Terms stating that conversational statements are not offers until confirmed | Directive | General Counsel (consulted) |
| Monitor concession patterns for anomalies and shared scripts | Detective | Channel owner |
| Test for persuasion, not only for injection, before launch | Detective | Channel owner with CISO |
| Approval limits for AI-granted concessions, set by finance | Directive | CFO |

## Quantification notes

- **Frequency:** for any public bot with concession authority, attempts are near-certain. Use red-team results on persuasion and the bot's concession authority to estimate success rate.
- **Magnitude:** bounded by enforced limits. If limits exist only in the prompt, model a heavy tail driven by viral sharing of a working script.

## Example scenario statement

> There is a 40% to 80% probability in the next 12 months that customers persuade our retention bot to grant credits above policy, producing a first-party loss of $30,000 to $600,000 in margin and remediation, with a 5% to 10% probability of a viral episode adding reputational loss.

## Questions for the accountable executive

1. What can our bot give away, and where is that limit enforced?
2. Have we tested whether a determined customer can talk it past that limit?
3. If a screenshot of our bot "agreeing" to something absurd went viral tomorrow, what would we do?

## Crosswalk

| Framework | Reference |
|---|---|
| Huwyler taxonomy | Imperfect fit: Misuse (Prompt Injection, LLM Jailbreaking, Bot Abuse) |
| OWASP LLM 2025 | LLM01 Prompt Injection (as the closest category); LLM06 Excessive Agency |
| OWASP Agentic 2026 | ASI01 Agent Goal Hijack (closest); ASI09 Human-Agent Trust Exploitation (reverse direction) |
| MITRE ATLAS | AML.T0051 LLM Prompt Injection; AML.T0048 External Harms (financial) |
| MIT AI Risk Repository | 4.3 Fraud, scams, targeted manipulation; 7.3 Lack of capability or robustness |
| NIST AI 600-1 | Information Integrity; Human-AI Configuration |
| CSA AICM | AIS, GRC |
| Generative Security | [Rethinking social engineering under MITRE ATLAS](https://blog.generativesecurity.ai/rethinking-social-engineering-under-mitre-atlas/) |

## Open questions

- Should "social engineering of AI" be proposed to OWASP and MITRE ATLAS as a distinct category?
- Does a bot "agreeing" to an offer create a contract in any jurisdiction? Watch for the first ruling.
