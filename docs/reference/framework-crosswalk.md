# Framework crosswalk

This page maps BORA-EAI to the frameworks organizations already use, so that BORA-EAI assessments can serve existing obligations and audits. Each scenario page also carries its own scenario-level crosswalk.

Identifiers follow: NIST AI RMF 1.0 (AI 100-1) and AI 600-1; ISO/IEC 42001:2023, 23894:2023, and 42005:2025; CSA AI Controls Matrix v1.1 domain codes; OWASP Top 10 for LLM Applications 2025; OWASP Top 10 for Agentic Applications (December 2025 edition); MITRE ATLAS; the MIT AI Risk Repository domain taxonomy; and Australia's Guidance for AI Adoption (AI6). MITRE ATLAS IDs and AICM domain names should be checked against current releases before formal use.

## Layers to standards

| BORA-EAI layer | NIST AI RMF | ISO/IEC 42001 | ISO/IEC 23894 | ISO/IEC 42005 | Australia AI6 |
|---|---|---|---|---|---|
| 1 Use-case inventory | GOVERN 1.6 (inventory); MAP 1 (context) | 4.3 scope; Annex A.4 resources (inventory of AI systems) | 6.3 scope, context, criteria | 5.4 scope | 1 Decide who is accountable |
| 2 Consumption and ownership | GOVERN 2 (accountability); GOVERN 6 (third parties); MAP 4 | 5.3 roles; Annex A.10 third-party and customer relationships | 6.3 context | 5.5 responsibilities | 1 Decide who is accountable |
| 3 Sovereignty profile | MAP 4; MANAGE 3 (third-party risk) | 6.1.2; Annex A.7 data; A.10 suppliers | Annex B risk sources | 6.6 deployment environment | 3 Measure and manage risks |
| 4 Agency and tier | MAP 3.5 (human oversight); MAP 5 | 6.1.2; Annex A.9 use of AI systems | 6.4.2 identification | 5.7 thresholds for sensitive and restricted uses | 6 Maintain human control |
| 5 Business threat scenarios | MAP 5.1 (likelihood and magnitude of impacts) | 6.1.2 AI risk assessment | 6.4.2 identification | 6.8 actual and foreseeable impacts | 2 Understand impacts and plan accordingly |
| 6 Loss | MEASURE 1 to 3 | 6.1.2 (analysis of consequences to the organization) | 6.4.3 analysis | (organizational impact out of scope) | 3 Measure and manage risks |
| 7 Value | MAP 3.1 (benefits); MAP 3.2 (costs) | 6.1.1 risks and opportunities | Purpose: "creation and protection of value" | Annex C harms and benefits | 2 Understand impacts and plan accordingly |
| 8 Governance cost | GOVERN 1 (resources) | 7.1 resources | 5 framework | n/a | 1 Decide who is accountable |
| 9 ERM fit and completeness | MANAGE 1 to 4; GOVERN 1.3 (risk tolerance) | 6.1.3 treatment; 8.2, 8.3; 9 performance evaluation | 6.4.4 evaluation; 6.5 treatment; 6.6 monitoring | 5.9 to 5.12 analysis, reporting, approval, review | 5 Test and monitor; 4 Share essential information |

NIST subcategory numbers are given at the level we are confident of; check against the AI RMF Playbook for formal mappings. ISO/IEC 42005 clause numbers are taken from the standard's public preview table of contents and should be checked against the full text.

## Scenarios to frameworks

| ID | NIST AI 600-1 risk | OWASP LLM 2025 | OWASP Agentic 2026 | MITRE ATLAS (examples) | MIT subdomain | CSA AICM | Geneva domain |
|---|---|---|---|---|---|---|---|
| B1 | Data Privacy; Information Security | LLM02, LLM06 | ASI03, ASI10 | AML.T0057, AML.T0024 | 2.1, 4.3 | IAM, DSP, HRS, LOG | Cyber and privacy; IP |
| B2 | Data Privacy; Information Security | LLM01, LLM02, LLM08 | ASI01, ASI06 | AML.T0051, AML.T0057 | 2.1, 2.2 | DSP, IAM, AIS, MDS | Cyber and privacy; regulatory |
| B3 | Data Privacy; Information Security; Intellectual Property | LLM02 | n/a | n/a | 2.1, 6.5 | DSP, UEM, STA, GRC | Cyber and privacy; regulatory; IP |
| B4 | Information Security; Value Chain and Component Integration | LLM03, LLM04 | ASI04, ASI05 | AML.T0010, AML.T0011 | 2.2 | STA, TVM, UEM, MDS | Operational; cyber |
| B5 | Intellectual Property | LLM03 | n/a | n/a | 6.3 (imperfect) | STA, GRC, DSP | Regulatory (IP) |
| B6 | Value Chain and Component Integration; Information Security | LLM03 | ASI04, ASI08 | AML.T0010 | 2.2, 6.1 | STA, BCR, IAM, IPY | Operational; cyber |
| B7 | Data Privacy; Intellectual Property; Value Chain and Component Integration | n/a | n/a | n/a | 2.1, 6.5 | STA, DSP, GRC | Regulatory; IP |
| B8 | Confabulation; Information Integrity | LLM09 | n/a | n/a | 3.1, 5.1 | AIS, GRC, MDS | Regulatory (legal); reputational |
| B9 | Information Security; Data Privacy | LLM01, LLM02, LLM05, LLM06, LLM07, LLM10 | ASI01, ASI02 | AML.T0051, AML.T0054, AML.T0057, AML.T0029, AML.T0034 | 2.2, 2.1 | AIS, MDS, IAM, LOG, TVM | Cyber and privacy; operational |
| B10 | Information Integrity; Human-AI Configuration | LLM01 (closest), LLM06 | ASI01 (closest); ASI09 (reverse) | AML.T0051, AML.T0048 | 4.3, 7.3 | AIS, GRC | Operational (financial); reputational |
| B11 | Human-AI Configuration; Information Security | LLM06, LLM10 | ASI02, ASI03, ASI08, ASI10 | n/a | 7.3, 7.6, 5.2 | IAM, BCR, LOG, CCC | Operational |
| B12 | Human-AI Configuration | LLM06 | ASI02, ASI03, ASI09 | AML.T0048 | 7.1, 7.3, 7.6 | IAM, GRC, LOG | Operational (financial); regulatory |
| B13 | Data Privacy; Value Chain and Component Integration | n/a | n/a | n/a | 2.1, 6.1 | DSP, CEK, IPY, BCR, STA | Regulatory; operational |
| B14 | Human-AI Configuration; Confabulation | n/a | n/a | n/a | 5.1, 6.4, 7.3 | n/a | Strategic; reputational; workforce |
| B15 | (GOVERN function) | n/a | n/a | n/a | 6.5 | GRC, A&A | Strategic; regulatory |

## Scenarios to Huwyler's taxonomy

Huwyler's AI System Threat Vector Taxonomy (arXiv 2511.21901) has nine domains: Misuse, Poisoning, Privacy, Adversarial, Biases, Unreliable Outputs, Drift, Supply Chain, and IP Threat `[preprint]`.

| ID | Huwyler domain: sub-threats |
|---|---|
| B1 | Misuse: Shadow AI Usage; IP Threat: Data Exfiltration |
| B2 | Privacy: Sensitive Data Leakage, Personal Data Leakage; Misuse: Prompt Injection |
| B3 | Misuse: Shadow AI Usage; Privacy: Personal Data Leakage, Sensitive Data Leakage |
| B4 | Poisoning: Tainted Open-Source Models, Poisoned ML Libraries; Supply Chain: Compromised Pre-trained Model, Vulnerable ML Framework |
| B5 | IP Threat (domain) |
| B6 | Supply Chain: Insecure Data Feeds/APIs, Compromised Pre-trained Model |
| B7 | No clean fit |
| B8 | Unreliable Outputs: Factual Hallucination, Source Fabrication |
| B9 | Misuse: Prompt Injection, LLM Jailbreaking; Adversarial: Model DoS, Query Flooding |
| B10 | Imperfect fit: Misuse (Prompt Injection, LLM Jailbreaking, Bot Abuse) |
| B11 | Thin coverage; nearest are Unreliable Outputs and Adversarial: Model DoS |
| B12 | No clean fit |
| B13 | No fit |
| B14 | Unreliable Outputs; Drift |
| B15 | No fit |

Huwyler's Biases and Drift domains have no dedicated BORA-EAI scenario. Bias harms to individuals are covered by ISO/IEC 42005 impact assessment, and the organizational consequence (for example, discrimination claims) is recorded under the scenario through which it arises, most often B8 or B14. Whether bias deserves its own business threat scenario is an [open question](../validation/open-questions.md).

## Scenarios to enterprise risk categories

A default mapping for rolling scenarios into an enterprise risk register. Adjust to your organization's categories.

| ERM category | Scenarios |
|---|---|
| Strategic | B14, B15, B6 (concentration) |
| Operational | B4, B6, B9, B11, B13 (continuity) |
| Financial | B10, B12 |
| Compliance and legal | B5, B7, B8, B13 (jurisdiction) |
| Information security and privacy | B1, B2, B3, B9 |
| Reputational | B8, B10 (and secondary for most) |
| Third-party | B5, B6, B7 |

## Lenses and tiering to frameworks

| BORA-EAI element | Related framework element |
|---|---|
| Override: regulated personal data | ISO/IEC 42005 clause 5.7 thresholds for sensitive uses; privacy impact assessment |
| Override: customer-facing representations | EU AI Act Article 50 transparency; consumer law |
| Optional override: EU AI Act Annex III | EU AI Act high-risk categories (obligations from 2 December 2027 after the 2026 Digital Omnibus) |
| Tier-to-control baseline | CSA CBRA mapping to AICM |
| Fast lane | NIST AI RMF GOVERN 1.3 (processes proportionate to risk tolerance) |
