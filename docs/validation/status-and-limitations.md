# Status and limitations

**Status: working draft v0.1, not yet validated.** Read this page before using BORA-EAI for real decisions.

## What is borrowed and what is new

| Component | Status | Basis |
|---|---|---|
| Use case as the unit of analysis, crossed with line of business and COSO capability type | Borrowed parts, new combination | COSO GenAI guidance; Australian DTA register pattern |
| Consumption Scopes 1 to 5 | Borrowed | AWS Generative AI Security Scoping Matrix |
| **Scope 2e, vendor-enabled embedded AI** | **New** | Derived from the Zoom, Adobe, and WeTransfer pattern |
| Five supply-chain roles | Borrowed | CSA AICM shared-responsibility model |
| **Six-axis sovereignty profile** | **New** | Built from provider documentation and APRA framing; no published equivalent found |
| Agentic Scopes 1 to 4 | Borrowed | AWS Agentic AI Security Scoping Matrix |
| CBRA dimensions and tier-to-control mapping | Borrowed | CSA CBRA |
| **Provisional CBRA anchor scales and tier thresholds** | **New, provisional** | CSA's own scales were not available; ours are consistent with its published examples |
| **Override rules and fast lane** | **New** | Address CBRA's capability bias and intake friction |
| **Fifteen-scenario business library and one-owner rule** | **New** | Technical anchors borrowed from Huwyler, OWASP, MITRE ATLAS, MIT |
| **Three-way chatbot split (B8, B9, B10)** | **New** | No major framework separates commercial manipulation |
| Loss domains and first/third-party split | Borrowed | Geneva Association |
| Loss forms and quantification method | Borrowed | Open FAIR; FAIR-AIR |
| **Range-based net position with value and governance terms** | **New application of borrowed methods** | FAIR's calibrated estimates and Monte Carlo, applied to value and governance as well as loss; ISO 31000; NIST MAP 3.1 and 3.2; cost of delay |
| **Governance cost as a model term** | **New** | No framework we found includes it |
| Completeness check | Borrowed | MIT AI Risk Repository |
| ERM integration | Borrowed | ISO/IEC 23894; ISO/IEC 42001 clause 6.1; ISO/IEC 42005 |

None of the new components has been tested in practice.

## Known limitations

### Evidence

- **Loss frequency data for AI is thin.** Most scenarios rely on surveys, vendor telemetry, and a small set of public incidents, which over-represent viral customer-facing failures.
- **Several scenarios have little or no public loss data:** B5, B7, B12 (forward-looking), B13, and B15.
- **Value evidence is strong for a few functions only:** customer support, writing, software engineering, and consulting-style analysis. HR, finance, legal, manufacturing, and supply chain rely on consulting estimates.
- **Several figures were not re-checked** against primary sources for this draft. They are labeled `[not re-checked]` or `[secondary]`. See the [verification log](../reference/evidence-labels.md#verification-log-for-this-draft).

### Method

- **Provisional tiering.** The CBRA anchor scales and thresholds are ours, not CSA's. Multiplying ordinal scales is mathematically weak; we use the product only to select a tier.
- **Base rates are not cleanly conditional.** P(production) and P(value | production) starting ranges come from different surveys with different definitions.
- **Portfolio effects.** BORA-EAI assesses use cases one at a time. Concentration across use cases (many on one provider) is recognized in B6 and B13 but not yet modeled at portfolio level.
- **Correlated losses.** The net-position simulation treats scenarios as independent by default. In reality, one event (for example, a provider outage) can trigger several scenarios at once.
- **Governance as value enabler.** The assumption that governance spend raises P(production) is plausible and untested.
- **Qualitative losses.** Reputation and some sovereignty exposures are recorded qualitatively and do not enter the net position.

### Scope

- **The landscape review was not exhaustive.** We did not reach primary frameworks from several large consultancies and insurers, or run a systematic academic search. A complete model may exist that we did not find.
- **Jurisdiction.** Regulatory content focuses on Australia, the EU, and the US.
- **Bias and drift** have no dedicated business threat scenario. See [Open questions](open-questions.md).
- **BORA-EAI is not legal advice.**

## What would change our mind

- An existing, published business-outcome model that passes the [landscape test](../reference/landscape.md#the-test).
- Incident-coding results showing scenarios overlap badly or leave large gaps.
- Executives consistently rejecting the accountability assignments.
- Assessments taking so long at Medium tier that the method is impractical.

See the [validation plan](validation-plan.md).
