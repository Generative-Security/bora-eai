# Evidence labels and verification log

Every factual claim in BORA-EAI carries a label so readers can judge how much weight it bears.

## Labels

| Label | Meaning |
|---|---|
| `[peer-reviewed]` | Published in a peer-reviewed journal or accepted conference |
| `[preprint]` | Working paper or preprint, not yet peer-reviewed |
| `[RCT]` | Randomized controlled or field experiment (may also be a preprint or working paper) |
| `[quasi-experimental]` | Natural experiment or administrative-data study |
| `[standard]` | Published standard or framework text (ISO, NIST, Open Group) |
| `[government]` | Government publication, regulator statement, or official estimate |
| `[legal ruling]` | Court or tribunal decision |
| `[industry-body]` | Not-for-profit industry body (CSA, OWASP, COSO, Geneva Association, FAIR Institute) |
| `[analyst]` | Analyst firm research or prediction (Gartner, Forrester) |
| `[consulting]` | Consultancy research or estimate, not peer-reviewed |
| `[survey]` | Practitioner or executive survey, including vendor-sponsored surveys with disclosed methods |
| `[vendor]` | Data or claims from a seller of the relevant product or service. Applied even when the data looks sound |
| `[vendor documentation]` | A provider's own product documentation, used for facts about that product |
| `[secondary]` | Reported by a third party; the primary source was not read |
| `[unverified]` | Could not be confirmed against a primary source; treat as a lead, not a fact |
| `[not re-checked]` | Cited from a canonical primary publication but the specific figure was not re-checked for this draft |
| `[illustrative]` | Invented for an example; not evidence of anything |

## Verification log for this draft

Items checked in a dedicated verification pass in November 2026, with outcomes.

| Claim | Outcome | Source |
|---|---|---|
| Gartner: at least 50% of GenAI projects will overrun budgets through 2028 | **Confirmed** (June 2026), with causes "poor architectural choices and lack of operational know-how" and the note that production can cost orders of magnitude more than a pilot. A per-user cost comparison sometimes cited alongside it was not in the article we read | [THE Journal](https://thejournal.com/articles/2026/06/22/report-half-of-gen-ai-projects-could-exceed-budget-by-2028.aspx) |
| BCG: "future-built" firms show 2.4x revenue and 2.8x EBITDA growth vs laggards | **Confirmed** for BCG's September 2026 Applied AI Index (7.5% of 1,330 executives). Note that BCG's 2025 figures differ (about 5% future-built; 1.7x revenue growth, 2.7x ROI), so the two years should not be mixed | [TechIntelPro](https://techintelpro.com/news/ai/agentic-ai/ai-is-starting-to-pay-off-50-of-companies-now-generate-value-bcg); [Computer Weekly](https://www.computerweekly.com/news/366631942/Companies-reap-the-rewards-of-being-AI-first) |
| Verizon 2026: business interruption median about US$90,000 per claim | **Confirmed.** Source is the Verizon 2026 Breach Impact Study (with CyberAcuView), based on about 70,000 US cyber-insurance claims, January 2019 to October 2025, published July 2026. BI was the highest-median category and 44% of known retail losses. The "top 2.5% over US$5 million" figure applies to all paid claims, not to business interruption specifically | [SecurityInfoWatch](https://www.securityinfowatch.com/cybersecurity/news/55388513/verizon-business-study-finds-median-breach-costs-have-nearly-doubled-since-2019); [HIPAA Journal](https://www.hipaajournal.com/verizon-2026-breach-impact-study/) |
| CSA CBRA anchor scales and tier thresholds | **Not available.** The public artifact page and blog do not publish them. BORA-EAI uses provisional scales and thresholds, labeled as such | [CSA](https://cloudsecurityalliance.org/artifacts/capabilities-based-risk-assessment-cbra-for-ai-systems) |
| ISO/IEC 42001 clause 6.1 structure | **Confirmed** from a structured summary: 6.1.2 assesses effects on the organization, individuals, and societies; 6.1.4 on individuals, groups, and societies, feeding 6.1.2 | [Modulos](https://docs.modulos.ai/frameworks/iso-42001/clauses-4-10.html) |
| Australia's AI6 practices | **Confirmed** (six practices, replacing the Voluntary AI Safety Standard) | [Actuaries Institute](https://www.actuaries.asn.au/research-analysis/understanding-australia-s-ai6-a-framework-for-ai-governance) |
| EU AI Act timeline after the Digital Omnibus | **Confirmed**: Regulation (EU) 2026/1744 in force 27 July 2026; Annex III high-risk from 2 December 2027; Annex I from 2 August 2028; Article 50 transparency from 2 August 2026; marking grace period to 2 December 2026 | [White & Case](https://www.whitecase.com/insight-alert/eu-ai-omnibus-enters-force-amending-ai-act); [Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/) |
| FISA Section 702 status | **Partly confirmed**: lapsed 12 June 2026 after 10-day and 45-day extensions; collection continued under existing certifications. Status after mid-2026 not confirmed | [OPB/NPR](https://www.opb.org/article/2026/06/13/fisa-702-a-key-u-s-spy-tool-has-lapsed-now-what) |
| Vendor IP indemnities (for B5) | **Confirmed in outline** from an advisory-firm summary; conditions and exclusions vary and must be checked per contract | [Redress Compliance](https://redresscompliance.com/ai-ip-indemnification-enterprise-copyright-protection.html) |
| AI copyright litigation status (for B5) | **Confirmed in outline** as of March 2026 | [Traverse Legal](https://www.traverselegal.com/blog/ai-copyright-litigation-where-the-key-cases-stand/) |
| Public incident of an enterprise agent making an unauthorized payment (for B12) | **None found.** One widely shared "incident" turned out to be a fictional scenario published by a payments consultancy | [Fime](https://www.fime.com/blog/blog-15/post/when-autonomous-agents-transact-lessons-from-the-llama-incident-665) |
| arXiv 2511.21901 authorship | **Confirmed**: Hernan Huwyler (IE Business School / IE Law School), sole author | [arXiv](https://arxiv.org/abs/2511.21901v1) |

## Known open verification items

- Verizon 2026 DBIR figures cited via a secondary summary (primary report not read).
- Replit/SaaStr record counts.
- McKinsey State of AI 2025 percentages.
- Geneva Association report date (October 2025 text, June 2026 file path).
- ISO/IEC 42005 annex contents and exact clause numbers.
- AWS GenAI Scoping Matrix discipline grid.
- CSA AICM full domain names (codes confirmed; names follow CSA's Cloud Controls Matrix naming).
- Provider retention defaults and per-model regional availability (see [Sovereignty by deployment model](sovereignty-by-deployment-model.md#not-verified-in-this-draft)).
