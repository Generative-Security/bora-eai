# Layer 6: Loss

> **Executive question:** What would it cost, who pays, and how bad is a bad year?

## Purpose

Layer 6 puts ranges on the loss side of each quantified scenario: how often a loss event happens, how much it costs when it does, whether the organization or a third party bears it, and whether insurance responds. It applies to Medium and High tier use cases.

## Loss domains: the executive view

To describe *what kind* of loss, BORA-EAI uses the seven GenAI risk domains from the Geneva Association, the insurance industry's think tank, in *Gen AI Risks for Businesses* `[industry-body]` ([Geneva Association](https://www.genevaassociation.org/sites/default/files/2026-06/gen_ai_businesses_report_2506.pdf)). Each loss is also tagged first-party (the organization's own loss) or third-party (liability to others), because that decides who pays and which insurance might respond.

| Domain | Typical first-party loss | Typical third-party loss | Insurance lines that may respond |
|---|---|---|---|
| Operational | Business interruption, rework, wrong decisions | Downstream customers' losses, SLA claims | Cyber (business interruption), E&O |
| Cybersecurity and privacy | Response, recovery, regulatory fines | Privacy claims, notification costs | Cyber |
| Ethical and bias | Remediation | Discrimination claims | Employment practices, E&O |
| Regulatory and compliance (including IP) | Fines, compliance remediation | Infringement claims | Cyber (partly), media, IP |
| Reputational and market | Lost customers, lower valuation | n/a | Rarely insured |
| Workforce | Skills erosion, displacement costs | Employment claims | Employment practices |
| ESG | Disclosure and remediation | Claims from affected parties | D&O |

The Geneva Association report also maps these domains to insurance lines and identifies gaps, including in business interruption and product recall. Note that it is unclear whether the cited file is an October 2025 report or a June 2026 reissue; check before citing a date.

Chatbot-error losses are now an underwritten category in their own right: in 2025, Lloyd's-market insurers launched cover, backed by Armilla, for losses caused by AI chatbot errors `[secondary]` ([Armilla](https://www.armilla.ai/resources/insurers-launch-cover-for-losses-caused-by-ai-chatbot-errors)).

## Loss forms: the analyst view

To *build* a magnitude estimate, BORA-EAI uses the six forms of loss from the Open FAIR standard, which FAIR-AIR inherits `[standard]`:

| Loss form | What it covers | AI examples |
|---|---|---|
| Productivity | Lost output while the business cannot operate normally | Bot pulled offline; agent-caused outage |
| Response | Incident handling: investigation, legal, notification, communications | Token rotation after a vendor breach; forensic review of prompt logs |
| Replacement | Replacing or restoring assets | Restoring a deleted database; rebuilding a compromised pipeline |
| Fines and judgments | Regulatory penalties, settlements, legal awards | Privacy fines; tribunal awards; FTC orders |
| Competitive advantage | Lost IP, trade secrets, market position | Source code in a consumer AI service; strategy documents leaked |
| Reputation | Lost customers, revenue, market value attributable to reputational harm | Viral bot failure; named as a victim in a supply-chain breach |

Most AI losses combine several forms. A customer-facing bot failure might combine productivity (bot offline), response (legal and communications), fines and judgments (honored concessions, tribunal awards), and reputation.

## Frequency

Frequency is where AI loss data is weakest. Starting points, in order of preference:

1. **The organization's own incidents and near misses**, including policy violations caught by data-loss-prevention tools.
2. **Telemetry-based industry data.** For example, Netskope's 2026 report found the average organization logs about 223 GenAI data-policy violations a month, with source code the largest category `[vendor]`. Violations are not losses, but they show exposure.
3. **Survey-based base rates.** IBM 2025: 13% of organizations reported an AI model or application breach; one in five reported a breach involving shadow AI `[survey]`.
4. **The [incident library](../reference/incident-library.md)**, for which scenarios have produced public losses at all.
5. **Calibrated expert estimates**, recorded with their reasoning.

State frequency as the probability of at least one loss event in the next 12 months, or an annual rate.

## Magnitude

Build magnitude ranges from the loss forms. Useful anchors:

- IBM 2025: global average breach cost US$4.44 million; US average US$10.22 million; high shadow-AI use added about US$670,000 `[survey]`.
- Verizon 2026 Breach Impact Study, from about 70,000 US cyber-insurance claims (2019 to October 2025): median business-interruption loss about US$90,000 per claim, the highest of any category; the top 2.5% of paid claims exceeded US$5 million `[survey]` ([SecurityInfoWatch](https://www.securityinfowatch.com/cybersecurity/news/55388513/verizon-business-study-finds-median-breach-costs-have-nearly-doubled-since-2019)).
- Regulatory maxima: EU AI Act up to €15 million or 3% of worldwide turnover for most operator obligations, €35 million or 7% for prohibited practices `[government]`.
- Small-dollar, large-precedent cases: *Moffatt v Air Canada* (CA$812) shows that the direct award can be trivial while the precedent and coverage are not.

Losses from AI incidents are often heavy-tailed: most events are small, a few are very large. Fit magnitude with a lognormal or similar distribution rather than a symmetric one.

## Tail loss

Report a **1-in-20-year loss** (the 95th percentile of annual loss) for each quantified scenario alongside its expected annual loss. Risk appetite statements are usually written about bad years, not average ones. See [Quantification](../06-quantification.md#what-the-board-sees).

## Insurability

For each quantified scenario, record whether the loss is:

- **insured** under a current policy (name the line);
- **insurable** but not currently covered;
- **uninsurable** in practice (for example, most reputational loss).

This tells the CFO how much of the exposure is retained.

## Losses that resist numbers

Reputation, customer trust, and some sovereignty exposures are hard to price. Record them qualitatively with a severity rating rather than forcing a figure. Air Canada's loss was small in dollars; the precedent was the real cost.

## Output

Per quantified scenario: frequency range, magnitude range, expected annual loss, 1-in-20-year loss, party, Geneva domain, dominant loss forms, and insurability. These feed the loss term of the [net position](../06-quantification.md).

Next: [Layer 7: Value](L7-value.md)
