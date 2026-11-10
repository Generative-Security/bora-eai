# Value evidence

Supporting reference for [Layer 7](../layers/L7-value.md) and [B14](../scenarios/B14-forgone-and-negative-value.md). Evidence is labeled by strength. Several peer-reviewed figures below are cited from their canonical publications and were not re-fetched for this draft; they are marked `[not re-checked]` and should be spot-checked before formal use.

## Controlled and field evidence by function

| Function | Study | Design | Finding | Label |
|---|---|---|---|---|
| Customer support | Brynjolfsson, Li & Raymond, "Generative AI at Work" ([NBER w31161](https://www.nber.org/papers/w31161); *QJE* 2025) | Staggered rollout to 5,179 agents | Issues resolved per hour +14% on average (about +15% in the published version); novices +34%; experienced agents little gain; customer sentiment up, attrition down | `[peer-reviewed]` `[not re-checked]` |
| Consulting and analysis | Dell'Acqua et al., "Navigating the Jagged Technological Frontier" ([HBS 24-013](https://www.hbs.edu/faculty/Pages/item.aspx?num=64700)) | Field experiment, 758 BCG consultants | Inside the frontier: 12.2% more tasks, 25.1% faster, quality 40%+ higher. Outside the frontier: 19 percentage points less likely to be correct. Below-average performers gained most | `[RCT, working paper]` `[not re-checked]` |
| Product and R&D | Dell'Acqua et al., "The Cybernetic Teammate" (HBS working paper, 2025) | Field experiment, ~776 P&G professionals | Individuals with AI performed about as well as two-person teams without | `[RCT, working paper]` `[not re-checked]` |
| Writing and communications | Noy & Zhang ([*Science* 381, 2023](https://www.science.org/doi/10.1126/science.adh2586)) | Online experiment, 453 professionals | ~40% less time; ~18% higher quality; productivity gap narrowed | `[peer-reviewed]` `[not re-checked]` |
| Software engineering | Peng et al. ([arXiv 2302.06590](https://arxiv.org/abs/2302.06590)) | Lab-style, 95 developers, one greenfield task | 55.8% faster; authors partly affiliated with GitHub/Microsoft | `[RCT]` `[not re-checked]` |
| Software engineering | Cui, Demirer, Jaffe, Musolff, Peng & Salz ([SSRN 4945566](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4945566)) | Three field experiments, ~4,867 developers | +26% completed tasks; larger for junior and short-tenure developers | `[RCT, working paper]` `[not re-checked]` |
| Software engineering | Google internal trial ([arXiv 2410.12944](https://arxiv.org/abs/2410.12944)) | ~96 engineers | ~21% faster; wide confidence interval | `[RCT]` `[not re-checked]` |
| Software engineering, experts | METR, Becker et al. ([arXiv 2507.09089](https://arxiv.org/abs/2507.09089)), July 2025 | 16 experienced open-source developers, 246 real issues on mature repositories | **19% slower** with AI. Expected 24% faster beforehand; believed 20% faster afterwards. Economists forecast 39% faster, ML experts 38% | `[RCT]` |
| Software engineering, update | [METR, February 2026](https://metr.org/blog/2026-02-24-uplift-update/) | Update | Developers probably more sped up than in 2025; METR describes its own evidence on how much as very weak | `[research organization]` |
| Economy-wide | Humlum & Vestergaard, "Large Language Models, Small Labor Market Effects" ([NBER w33777](https://www.nber.org/papers/w33777)) | ~25,000 workers in 11 exposed occupations linked to Danish administrative data | ~2.8% time savings; precisely estimated null effects on earnings and hours | `[quasi-experimental]` `[not re-checked]` |
| Macroeconomy | Acemoglu, "The Simple Macroeconomics of AI" ([NBER w32487](https://www.nber.org/papers/w32487)) | Model | Total factor productivity gains of at most ~0.66% over ten years | `[peer-reviewed]` `[not re-checked]` |

**Where rigorous evidence is missing:** HR, finance and FP&A, legal, manufacturing and operations, and supply chain. Estimates for those functions rest on consulting models and surveys.

**Recurring moderators:** worker experience (novices gain most; experts on familiar work may lose time) and task position relative to the model's capability (outside it, accuracy falls). BORA-EAI records both as use-case attributes.

## Potential value

| Source | Finding | Label |
|---|---|---|
| McKinsey, *The economic potential of generative AI* (June 2023) | US$2.6 to 4.4 trillion a year across 63 use cases; about 75% in customer operations, marketing and sales, software engineering, and R&D. Customer operations about 30–45% of function costs; software engineering about 20–45% of function spend; R&D about 10–15% | `[consulting]` `[not re-checked]` |

## Realized value and failure rates

| Source | Finding | Label |
|---|---|---|
| S&P Global Market Intelligence 2025 (n > 1,000) | 42% of companies abandoned most AI initiatives (17% in 2024); average organization scrapped 46% of proofs of concept before production | `[survey]` ([CIO Dive](https://www.ciodive.com/news/ai-project-failure-rates/742590/)) |
| Gartner, June 2026 | At least 50% of GenAI projects will overrun budgets through 2028; production can cost orders of magnitude more than a pilot | `[analyst]` ([THE Journal](https://thejournal.com/articles/2026/06/22/report-half-of-gen-ai-projects-could-exceed-budget-by-2028.aspx)) |
| Gartner, July 2024 | At least 30% of GenAI projects abandoned after proof of concept by end of 2025 (poor data quality, inadequate risk controls, escalating costs, unclear value) | `[analyst]` |
| Gartner, June 2025 | Over 40% of agentic AI projects cancelled by end of 2027 (costs, unclear value, inadequate risk controls) | `[analyst]` |
| Gartner, June 2025 | By 2027, half of organizations that expected to significantly reduce customer-service workforce will abandon those plans | `[analyst]` |
| MIT NANDA, *The GenAI Divide* (August 2025) | ~95% of GenAI pilots without measurable P&L return; ~5% of custom tools reached production; vendor-partnered builds ~twice as likely to succeed | `[survey]`; methodology not verified; widely criticized as overhyped |
| McKinsey, *State of AI 2025* | ~88% use AI in at least one function; ~39% report any enterprise EBIT impact; ~6% high performers | `[survey]` `[not re-checked]` |
| BCG, *The Widening AI Value Gap* (2025) | ~5% "future-built" firms; 60% report no material value | `[consulting]` ([Computer Weekly](https://www.computerweekly.com/news/366631942/Companies-reap-the-rewards-of-being-AI-first)) |
| BCG, Applied AI Index 2026 (September 2026, 1,330 executives) | 7.5% "future-built": 2.4x revenue growth, 2.8x EBITDA growth, 2.3x shareholder return vs laggards; nearly half of companies (future-built plus scaling) generating value; only 5% have the full set of controls | `[consulting]` ([TechIntelPro](https://techintelpro.com/news/ai/agentic-ai/ai-is-starting-to-pay-off-50-of-companies-now-generate-value-bcg)) |
| Commonwealth Bank of Australia, August 2025 | Reversed replacement of 45 service roles with a chatbot | `[secondary]` |

**Potential versus realized:** potential value and realized value differ by roughly an order of magnitude. BORA-EAI shows both, and uses realized base rates for P(production) and P(value | production).

## Methods for valuing the upside

| Method | Use in BORA-EAI | Source |
|---|---|---|
| Two-sided risk | Justifies value in the risk register | ISO 31000:2018; ISO/IEC 42001 clause 6.1; NIST AI RMF MAP 3.1 and 3.2 |
| Cost of delay and WSJF | Cost of delay per quarter | Reinertsen, *Principles of Product Development Flow* (2009); [SAFe](https://framework.scaledagile.com/wsjf) |
| Real options | Pilots as staged options | Benaroch & Kauffman, *Information Systems Research* 10(1), 1999 |
| Positive risk responses | Exploit, enhance, share, accept | PMI PMBOK |
| Benefit-side FAIR | Not published; BORA-EAI constructs one by analogy | n/a |

## Gaps

- No rigorous trials for HR, finance, legal, or supply chain.
- Durability of gains (skill atrophy, quality drift) is largely unstudied.
- No study measures firm-level P&L impact causally.
- No rigorously identified estimate of competitive erosion from late adoption.
- No published empirical validation of AI use-case prioritization matrices.
