# Use-case assessment: [use case name]

> BORA-EAI v0.1 template. Delete guidance in italics as you complete it. For Low tier, complete sections 1 to 5 and 9 only.

| | |
|---|---|
| Use-case ID | |
| Assessed by | |
| Date | |
| Tier | Fast lane / Low / Medium / High |
| Decision | Approve / Approve with conditions / Redesign / Defer / Stop |
| Next review | |

## 1. Inventory (Layer 1)

| Field | Value |
|---|---|
| Accountable executive (net position) | |
| Line of business | |
| Capability type (COSO) | *Ingestion, transformation, posting, orchestration, judgment, monitoring, regulatory intelligence, human-AI interaction* |
| Lens | Internal / Customer-facing |
| Users and approximate count | |
| Data classes | |
| Decisions about individuals? | |
| Product, platform, model | |
| Status | Proposed / pilot / production / discovered |

## 2. Consumption and ownership (Layer 2)

| Field | Value |
|---|---|
| Consumption scope | 1 / 2 / 2e / 3 / 4 / 5 |
| Cloud service provider | |
| Model provider | |
| Orchestrated service provider | |
| Application provider | |
| Integration tokens and what they reach | |
| Contract status and AI terms (training use, retention, notice, sub-processors, IP indemnity) | |

## 3. Sovereignty profile (Layer 3)

Attach or summarize the [sovereignty profile](sovereignty-profile.md). Note any policy gaps and whether preventive controls enforce the intended configuration.

## 4. Agency and tier (Layer 4)

| Field | Value |
|---|---|
| Agentic scope | 1 / 2 / 3 / 4 |
| Actions available | |
| Credentials (whose, lifetime, scope) | |
| Limits enforced outside the model | |
| Human approval points | |
| CBRA: criticality / autonomy / permissions / impact radius | _ / _ / _ / _ |
| CBRA product and provisional tier | |
| Override: regulated personal data? | |
| Override: customer-facing representations or concessions? | |
| Organizational overrides | |
| Fast-lane pattern (if any) | |
| **Tier and reasoning** | |
| Redesign options considered | *Changes to agency, permissions, data, or deployment that would lower the tier* |

## 5. Business threat scenarios (Layer 5)

| ID | Applies? | Reason | Accountable | Quantify? | Qualitative rating (Low tier) |
|---|---|---|---|---|---|
| B1 Insider amplification | | | CISO | | |
| B2 Sanctioned-AI leakage | | | CIO | | |
| B3 Shadow-AI leakage | | | CISO | | |
| B4 Untrusted AI artifacts | | | CTO | | |
| B5 IP and license exposure | | | General Counsel | | |
| B6 Vendor concentration | | | CRO | | |
| B7 Vendor-enabled embedded AI | | | General Counsel | | |
| B8 Misrepresentation liability | | | Channel owner | | |
| B9 Technical compromise | | | CISO | | |
| B10 Commercial manipulation | | | Channel owner | | |
| B11 Agentic execution failure | | | CTO | | |
| B12 Unauthorized commitments | | | CFO | | |
| B13 Sovereignty, jurisdiction, continuity | | | CRO | | |
| B14 Forgone and negative value | Always | | Use-case sponsor | Value term | |
| B15 Governance cost and failure | Always | | CRO | Governance term | |

Scenario statements (FAIR-AIR form) for each quantified scenario:

> There is a [low]% to [high]% (most likely [mode]%) probability in the next 12 months that [threat or failure] in [use case] causes [business outcome], producing a [first- or third-party] loss of typically $[amount], [with a heavy tail].

## 6. Loss (Layer 6) — Medium and High

| Scenario | Frequency (low / mode / high) | Magnitude (typical; distribution) | Expected annual loss | 1-in-20-year loss | Party | Geneva domain | Insurance line | Insurability |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

Losses recorded qualitatively (reputation, trust, sovereignty):

## 7. Value (Layer 7) — Medium and High

| Input | Low | Most likely | High | Basis |
|---|---|---|---|---|
| Gross annual value | | | | |
| P(production) | | | | |
| P(value \| production) | | | | |

| Output | Value |
|---|---|
| Risk-adjusted annual value (P10 / P50 / P90) | |
| Cost of delay per quarter | |
| User expertise and task position notes | |
| How value will be measured | |

## 8. Governance cost (Layer 8) — Medium and High

| Item | One-off | Annual |
|---|---|---|
| Program allocation | | |
| Assessment | | |
| Assurance (red teaming, testing) | | |
| Controls and monitoring | | |
| Compliance | | |
| **Range (low / mode / high)** | | |

## 9. ERM fit and completeness (Layer 9)

| Output | Value |
|---|---|
| Net annual position (P10 / P50 / P90) | |
| Probability net position is negative | |
| Largest 1-in-20-year scenario loss | |
| Appetite statements tested, and result | |
| ERM categories and register entries | |
| MIT subdomains covered | |
| MIT subdomains considered and rated low | |
| MIT subdomains out of scope (with reason) | |
| Gaps that fit no BORA-EAI scenario | |

**Decision:**

**Conditions (each with an owner and date):**

1.
2.
3.

**Sign-off:** accountable executive, and scenario owners for each quantified scenario.
