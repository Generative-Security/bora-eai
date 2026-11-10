# Introduction

## The problem

When security teams talk about AI risk, they usually mean one kind of failure: a control fails and something is breached, leaked, or manipulated. That kind of failure has a well-documented price. IBM's 2025 Cost of a Data Breach study put the average breach at US$4.44 million globally and a record US$10.22 million in the United States `[survey]` ([IBM](https://newsroom.ibm.com/2025-07-30-ibm-report-13-of-organizations-reported-breaches-of-ai-models-or-applications,-97-of-which-reported-lacking-proper-ai-access-controls)).

A failed AI investment is just as real, but it rarely shows up as an incident:

- In S&P Global's 2025 survey of more than 1,000 respondents, 42% of companies had abandoned most of their AI initiatives, up from 17% a year earlier. The average organization scrapped 46% of its proofs of concept before production `[survey]` ([CIO Dive](https://www.ciodive.com/news/ai-project-failure-rates/742590/)).
- Gartner expects at least 50% of GenAI projects to overrun their budgets through 2028, citing poor architectural choices and lack of operational know-how, and notes that a production-ready system can cost orders of magnitude more than a pilot `[analyst]` ([THE Journal](https://thejournal.com/articles/2026/06/22/report-half-of-gen-ai-projects-could-exceed-budget-by-2028.aspx)).
- Projects that go live can miss too. In Australia, Commonwealth Bank reversed its decision to replace 45 customer-service roles with an AI chatbot after call volumes rose `[secondary]` ([The Register](https://www.theregister.com/2025/08/22/commonwealth_ban_chatbot_fail_rehiring/)).

And not using AI has a cost. BCG's 2026 survey of 1,330 executives found its "future-built" companies, 7.5% of those surveyed, delivering 2.4 times the revenue growth and 2.8 times the EBITDA growth of laggards `[consulting]` ([BCG via TechIntelPro](https://techintelpro.com/news/ai/agentic-ai/ai-is-starting-to-pay-off-50-of-companies-now-generate-value-bcg)). That is a correlation from a consultancy survey, not proof that AI caused it, but a board will hear it whenever someone suggests slowing down.

All of these are realized risk to the enterprise, with material business impact. Most AI risk and threat models only see the first kind.

## Five pictures, five owners, five currencies

Enterprise AI risk is a puzzle with several distinct pictures inside it. Each picture is complete on its own, but only when they line up does the whole thing look right.

| Picture | Owner | Currency | What the owner wants to know |
|---|---|---|---|
| Law and regulation | General Counsel, HR | Settlements and fines | Which use cases create liability, and under which law? |
| Finance | CFO | Budget variance | What will this really cost, and what will it return? |
| Operations | COO, revenue owners | Revenue lost, efficiency gained | What happens to the process if this fails or is pulled? |
| Security | CISO | Incident and breach cost | What can this expose, and to whom? |
| Strategy | CEO, board | Growth gained or lost | What do we lose if we move too slowly? |

Some examples of what each owner sees:

- **Law and regulation.** The EU AI Act sets fines of up to €15 million or 3% of worldwide turnover for most operator obligations, and up to €35 million or 7% for prohibited practices `[government]` ([AI Act Article 99](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-99)). Air Canada's tribunal loss in *Moffatt* was only CA$812, but it established that a company owns what its chatbot tells customers `[legal ruling]` ([McCarthy Tétrault](https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot)).
- **Operations.** In Verizon's 2026 Breach Impact Study, built from about 70,000 US cyber-insurance claims, business interruption had the highest median loss of any category, around US$90,000 per claim, and made up 44% of known retail losses `[survey]` ([SecurityInfoWatch](https://www.securityinfowatch.com/cybersecurity/news/55388513/verizon-business-study-finds-median-breach-costs-have-nearly-doubled-since-2019)).
- **Security.** In IBM's 2025 study, 13% of organizations reported a breach of an AI model or application, and 97% of those lacked AI access controls. One in five reported a breach caused by shadow AI, and organizations with high levels of shadow AI paid an average of US$670,000 more per breach `[survey]` ([IBM](https://newsroom.ibm.com/2025-07-30-ibm-report-13-of-organizations-reported-breaches-of-ai-models-or-applications,-97-of-which-reported-lacking-proper-ai-access-controls)).

Each discipline already has a way to frame AI risk. As far as we could find, nothing shows how they fit together at the enterprise level, use case by use case, with benefits weighed against losses. The [landscape review](reference/landscape.md) documents what we looked at.

## What BORA-EAI is

BORA-EAI is a method for deciding, per AI use case:

- what the use case could do to the business, in terms each owner recognizes;
- what it could do for the business, as a range, including the chance it never delivers;
- what it costs to govern;
- which single executive is accountable for each consequence;
- whether the net position fits the organization's risk appetite.

It produces a register of use cases, a net position for each as a distribution, and a portfolio view a board can read.

## What BORA-EAI is not

- **Not a replacement for technical threat modeling.** STRIDE, MITRE ATLAS, MAESTRO, and the OWASP lists still do the system-level work underneath. Every BORA-EAI scenario cross-references them so the security team can decompose it.
- **Not a control catalog.** The CSA AI Controls Matrix, ISO/IEC 42001 Annex A, and similar catalogs say what to implement. BORA-EAI says which use cases need which depth of control, and why, in business terms.
- **Not a management system.** ISO/IEC 42001 is. BORA-EAI is designed to sit inside one, as the risk and impact assessment method (see [ERM fit](layers/L9-erm-fit-and-completeness.md)).
- **Not a source of precise numbers.** Where data is thin, the honest output is a wide range. The model is built to show uncertainty, not hide it.

## Who it is for

- **Executives and boards** read the scenario names, the accountability assignments, and the portfolio view.
- **CISOs and risk leads** run the program: maintain the register, run reviews, and translate results into the enterprise risk standards other owners already use.
- **Risk analysts** do the quantification for Medium and High tier use cases.
- **Auditors and regulators** can trace each assessment back to published frameworks through the crosswalk.

## The security team's role

Most pictures in the puzzle belong to someone else. Security is still essential in lining them up. Security teams have the experience to maintain a register of AI use cases with a named owner for each, run a regular review, and translate results into the enterprise risk standards the other owners already use, such as ISO/IEC 23894 and ISO/IEC 42001. That is a bigger role than owning the technical controls, and a different one from owning every risk.

Next: [Principles](02-principles.md)
