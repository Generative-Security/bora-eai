# Validation plan

How we intend to test BORA-EAI before calling any version validated. Contributors are welcome to run any of these tests and report results.

## 1. Read the primary texts we could not reach

Before the model cites them as fact:

- the CSA CBRA whitepaper's anchor scales and tier thresholds (to replace our provisional ones);
- the FAIR-AIR Playbook's vector definitions and any scenario library;
- ISO/IEC 42005 Annex C, ISO/IEC 23894 Annexes A and B, and ISO/IEC 42001 clause 6.1 wording;
- the AWS GenAI Scoping Matrix's discipline grid;
- the CSA AICM's full domain names;
- the Open FAIR loss-form definitions;
- Huwyler's domain-to-loss mapping (published in the author's repository);
- the APRA AI letter and CPS 230 text;
- the Verizon 2026 DBIR primary report.

## 2. Close the search gaps

To test the finding that no complete business-outcome model exists:

- primary frameworks from PwC, EY, McKinsey, BCG, and Accenture;
- loss-scenario material from Marsh, Aon, Beazley, Coalition, Munich Re, and Swiss Re;
- executive-level material from CrowdStrike, Palo Alto Networks (Unit 42), Mandiant, and Anthropic;
- Singapore's CSA and IMDA guidance, and ISACA;
- a systematic search of Google Scholar, SSRN, and information-systems journals;
- whether the MIT Sloan board project produced its planned framework.

## 3. Test the scenario library

**Incident coding for mutual exclusivity.**

- Take at least 100 incidents from the AI Incident Database and MIT's AI Incident Tracker, plus BORA-EAI [incident library](../reference/incident-library.md).
- Have at least two people code each incident independently to one primary BORA-EAI scenario (or "none").
- Measure agreement (for example, Cohen's kappa). Low agreement on a pair of scenarios means they overlap; many "none" codes mean a gap.
- Pay particular attention to the boundaries most likely to blur: B1/B3, B2/B9, B8/B10, B9/B10, B11/B12, B6/B13.

Huwyler's taxonomy was validated for coverage (did every incident fit somewhere) but not for exclusivity (did each fit only one place). This test does both.

**Back-testing the tiering.** Would BORA-EAI's tiering have flagged known incidents in advance? Apply layers 2 to 4, as they would have stood before the incident, to Salesloft Drift, PocketOS, Replit/SaaStr, Moffatt v Air Canada, and the Chevrolet bot. A model that would have put these in the fast lane or Low tier needs fixing.

## 4. Test with executives

- **Comprehension.** Give CISOs, CROs, General Counsel, CFOs, and non-executive directors the scenario names and one-line outcomes. Can they say, unprompted, what each means and why it matters?
- **Accountability.** Do the named accountable owners accept the assignment? Where they reject it, who do they say should own it, and why?
- **Decision usefulness.** Given a board summary for a real use case, do executives make a different or more confident decision than without it?

## 5. Test in practice

- Run at least one real use case at each tier through every layer.
- Measure time and effort per tier, against the expectations in [Tiering](../05-tiering.md).
- Test whether fast-lane criteria are tight enough: does anything that should have hit an override slip through?
- Test whether Low tier screens miss scenarios that a Medium assessment would catch.

## 6. Calibrate

- AI-specific loss frequencies: insurer claims data is the most promising source.
- Uplift evidence for HR, finance, legal, manufacturing, and supply chain.
- Measured AI governance team costs.
- Evidence for or against the assumption that governance spend raises P(production).
- Correlation between scenarios, for portfolio-level simulation.

## 7. Keep the moving facts current

At each minor version:

- provider residency options, routing defaults, retention, and abuse-monitoring terms;
- EU AI Act implementation dates and guidance;
- Australian privacy reform, APRA guidance, and any ACCC action on AI;
- FISA Section 702 and other foreign compelled-access law;
- vendor IP indemnity terms;
- new public incidents, especially the first credible B12 case.

## Reporting results

Open an issue with the [evidence submission template](../../.github/ISSUE_TEMPLATE/evidence-submission.md), or email questions@generativesecurity.ai. Results that show the model is wrong are the most valuable kind.
