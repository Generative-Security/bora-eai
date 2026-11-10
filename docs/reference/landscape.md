# Landscape: existing models and where they stop

We looked for a published, accepted model that analyzes the risk of enterprise *use* of AI at the business-outcome level, for executives, covering the full set of exposures in BORA-EAI. We did not find one. This page records what we reviewed, what each model does well, and where it stops, so that reviewers can check our work and point us to anything we missed.

Reviewed November 2026. Coverage was not exhaustive; see [Gaps in this review](#gaps-in-this-review).

## The test

A complete model would:

1. speak to executives in business-outcome terms (liability, budget, revenue, breach cost, growth);
2. take the use case, not the system, as the unit;
3. weigh benefits and the cost of governing against losses;
4. cover: insider threat using AI; data exfiltration through sanctioned and shadow AI; downloaded models and tools and the extended supply chain; AI embedded in purchased software; customer-facing chatbot liability, technical compromise, and social engineering; opportunity cost by use case and line of business; governance cost; and data sovereignty across deployment models.

## Summary

| Model | Type | What it does well | Where it stops |
|---|---|---|---|
| **NIST AI RMF 1.0** and **AI 600-1** (Generative AI Profile) | Standard (voluntary) | Shared vocabulary; four functions (Govern, Map, Measure, Manage); twelve GenAI risks with 200+ suggested actions; MAP 3.1 and 3.2 require documenting benefits and costs | A process and catalog, not a business-impact model. Risks are not tied to owners, lines of business, or prices. |
| **ISO/IEC 42001**, **23894**, **42005** | Standards (certifiable for 42001) | Auditable management system; ERM bridge (23894 mirrors ISO 31000); impact assessment on individuals and society (42005); clause 6.1 covers risks *and* opportunities | Requires a process but does not say which AI business threat scenarios to examine, who owns them, or how to price them. 42005 puts business impact outside its scope. |
| **FAIR-AIR** (FAIR Institute) | Quantification approach | Five steps; dollar-denominated loss using FAIR's frequency × magnitude and Monte Carlo; a 2026 extension for third-party AI | Loss only; no benefit or opportunity cost. Its five "vectors" mix deployment modes and threat types, and are not a threat taxonomy. |
| **CSA CBRA** and **AI Controls Matrix (AICM)** | Industry-body framework | Capability-based tiering (criticality × autonomy × permissions × impact radius); 247 controls in 18 domains; five-role shared-responsibility model | Produces a tier and a control baseline, not a loss figure. Capability-centric, so low-autonomy exposure (for example, read-only access to personal data) can be under-scored. |
| **AWS GenAI and Agentic AI Security Scoping Matrices** | Vendor framework, vendor-neutral in substance | Clear consumption scopes (who owns what) and agency scopes | Not risk-scoring; no business impact or loss; no non-security harms. |
| **Google SAIF** | Vendor framework | Six elements; element 6 asks to "contextualize AI system risks in surrounding business processes" | One element of six; the supporting risk assessment is a technical checklist. |
| **Gartner AI TRiSM** | Analyst framework | Governance and runtime controls; market map | A tooling and governance model, largely paywalled; not a business-outcome risk model. |
| **Gartner Outcome-Driven Metrics (ODMs)** and protection-level agreements | Analyst framework | Expresses security performance in business-outcome terms executives can fund against; Gartner applies ODMs to GenAI risk, including use-case risk assessments, alongside AI TRiSM | Measures how well security controls perform. Does not decide, use case by use case, whether AI is worth its risk and governance cost, or assign an owner to each consequence. The closest naming neighbor to BORA-EAI. |
| **Gartner "five GenAI blind spots"** (reported November 2025) | Analyst research | Names shadow AI, technical debt, sovereignty, skills erosion, and lock-in as executive issues | A list of themes, not a model. |
| **Forrester AEGIS** (August 2026) | Analyst framework | Six security domains and three principles (least agency, continuous assurance, explainable outcomes) for agentic AI | A CISO controls framework; not organized around business outcomes; insider threat, supply chain, embedded AI, and sovereignty not covered. |
| **OWASP AI Exchange; OWASP LLM and Agentic Top 10s** | Industry-body | Comprehensive threat and control mapping; agentic risks (ASI01 to ASI10) | System-level, the same altitude as STRIDE and MAESTRO. |
| **MITRE ATLAS** | Industry-body | Adversary tactics and techniques against AI | System-level adversary model. |
| **CSA MAESTRO** | Industry-body | Layered threat modeling for agentic AI | System-level. |
| **Cisco Integrated AI Security and Safety Framework** (arXiv, December 2025) | Vendor preprint | Lifecycle-aware taxonomy for red teaming and prioritization | System-level; no business-outcome mapping. |
| **MIT AI Risk Repository** | Peer-reviewed meta-review | 1,725 risks from 74 documents; causal and domain taxonomies; mitigation taxonomy | A catalog, not a scoring or business model. Says nothing about likelihood or severity. |
| **Huwyler, AI System Threat Vector Taxonomy** (arXiv 2511.21901, November 2025) | Preprint, single author | Nine domains, 53 sub-threats, each mapped to business loss categories (confidentiality, integrity, availability, legal, reputation); validated against 133 incidents | Not peer-reviewed; internal inconsistencies; validation tests coverage, not mutual exclusivity; thin on agentic threats; no sovereignty or embedded-AI coverage. |
| **Geneva Association, *Gen AI Risks for Businesses*** | Insurance industry think tank | Seven risk domains, each tagged first- or third-party and mapped to insurance lines and coverage gaps; the most CFO-ready structure we found | No sovereignty, embedded AI, or governance cost; no loss-scenario library. |
| **COSO, *Achieving Effective Internal Control Over Generative AI*** (March 2026) | Industry-body guidance | Eight GenAI capability types; internal-control framing for finance and audit | Control-oriented; does not cover shadow AI, vendor AI, data leakage, or cost. |
| **KPMG, *Deploying Trustworthy AI: Risk and Controls Guide*** (March 2026) | Consulting framework | Ten trust pillars, about 18 risk categories, mapped to ISO 42001, NIST, EU AI Act | Organized by trust attribute, not business outcome; third-party AI, sovereignty, and cost not treated. |
| **Deloitte Trustworthy AI** (2020) | Consulting framework | Ethics and trust dimensions | Same pattern as KPMG. |
| **MIT Sloan, *AI Proofing the Board and C-Suite*** (Pearlson, June 2025) | Academic position paper | Board audience; includes opportunity cost of not adopting; six hypothesized risk categories | A research proposal seeking funding at publication; no follow-on framework found. Most of BORA-EAI's exposures are not covered. |
| **CSA, *Shadow AI Infrastructure*** (May 2026) | Industry-body paper | Strong on insider, shadow AI, downloaded models, supply chain, exfiltration; four classification dimensions | States it was AI-assisted and not CSA-reviewed; sovereignty largely absent; impact narrative only. |
| **WEF / Oxford, leader's guide to AI cyber risk** (January 2025) | Policy guidance | Risk-versus-reward process for executives | No taxonomy; shadow AI and supply chain not addressed. |
| **Australian Government, Guidance for AI Adoption (AI6)** | Government guidance | Six essential practices: decide who is accountable; understand impacts and plan accordingly; measure and manage risks; share essential information; test and monitor; maintain human control | A governance practice standard, not a threat model. |
| **UK AI Cyber Security Code of Practice** (January 2025; later ETSI EN 304 223) | Government code | Lifecycle security baseline | Not a threat model. |

## What BORA-EAI borrows

| Need | Borrowed from |
|---|---|
| Consumption and ownership | AWS GenAI Scoping Matrix; CSA AICM shared-responsibility roles |
| Agency | AWS Agentic Scoping Matrix |
| Tiering | CSA CBRA |
| Threat anchors | Huwyler; OWASP LLM and Agentic Top 10s; MITRE ATLAS |
| Loss language | Geneva Association domains and first/third-party split; FAIR loss forms |
| Quantification | FAIR and FAIR-AIR |
| Use-case axis | COSO capability types |
| Two-sided risk | ISO 31000; NIST AI RMF MAP 3.1 and 3.2; ISO/IEC 42001 clause 6.1 |
| ERM integration | ISO/IEC 23894; ISO/IEC 42001; ISO/IEC 42005 |
| Completeness | MIT AI Risk Repository |

## The gaps BORA-EAI is built to fill

No source we found treats these as structured model dimensions:

- AI embedded in purchased software, switched on or re-termed by the vendor;
- social engineering of a chatbot's commercial logic, as distinct from hacking it;
- opportunity cost by use case and line of business, as lost revenue and forgone efficiency;
- the internal cost of governance;
- data sovereignty compared across deployment models.

The closest anything came was ISO/IEC 42001 with the NIST AI RMF. Both tell organizations to weigh opportunities and benefits against risks and costs. Neither says what the AI-specific business threat scenarios are, who owns them, or how to price them.

## Gaps in this review

The finding that no complete model exists is bounded by what we could reach:

- We did not retrieve primary frameworks from PwC, EY, McKinsey, BCG, or Accenture.
- We did not retrieve loss-scenario material from Marsh, Aon, Beazley, Coalition, Munich Re, or Swiss Re.
- We did not find executive-level enterprise-adoption risk models from CrowdStrike, Palo Alto Networks (Unit 42), Mandiant, or Anthropic.
- We did not search Singapore's guidance (CSA's guidelines on securing AI systems; IMDA's GenAI governance framework) or ISACA.
- We did not run a systematic academic database search (Google Scholar, SSRN, MIS Quarterly, JAIS).

If you know of a model that passes the test above, please [tell us](../../CONTRIBUTING.md).
