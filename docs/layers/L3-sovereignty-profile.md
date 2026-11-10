# Layer 3: Sovereignty profile

> **Executive question:** Where does it run and rest, who can see it, whose law applies, and can we leave?

## Purpose

"Data sovereignty" is used loosely, and many AI residency claims cover only part of it. A provider can store data in-country while processing it anywhere. A model can run in-region while a human abuse reviewer elsewhere reads flagged prompts. Layer 3 breaks sovereignty into six axes and records each one per use case, so that the [sovereignty scenario (B13)](../scenarios/B13-sovereignty-jurisdiction-continuity.md) can be assessed against facts rather than marketing.

We found no published framework that maps sovereignty risk across AI deployment models. The six-axis profile is a BORA-EAI construction, built from providers' own residency documentation and APRA's fourth-party framing.

## The six axes

| # | Axis | Question | Why it matters |
|---|---|---|---|
| 1 | **Inference location** | Where are prompts and outputs processed? | Many policies define residency as including processing. "Global" routing options process anywhere. |
| 2 | **Data at rest** | Where are prompts, outputs, logs, abuse-monitoring copies, files, and fine-tunes stored, and for how long? | Storage commitments are the most common residency claim, and often the only one. |
| 3 | **Plaintext access** | Who can read the content: provider staff, abuse reviewers, sub-processors? | Encryption at rest does not stop reviewers who see flagged content in plaintext. |
| 4 | **Key custody** | Who holds the keys to stored data? | Customer-managed keys protect data at rest, not data during inference. |
| 5 | **Legal reach** | Whose law can compel the operator to produce data? | Every frontier model provider and hyperscaler is US-headquartered. In-country hosting narrows US legal reach; it does not remove it. |
| 6 | **Continuity and portability** | Could access be suspended, the model deprecated, or the terms changed, and how hard is it to move? | Export controls, provider policy enforcement, and lock-in are business-continuity risks. |

The [sovereignty profile template](../../templates/sovereignty-profile.md) records all six.

## Deployment models, from most to least control

| Model | Sovereignty position | Main residual exposure |
|---|---|---|
| **Open-weight model self-hosted** (on-premises or on IaaS) | The organization controls location, keys, logs, and retention | The infrastructure operator's nationality; the organization's own operational burden |
| **Managed platform, region- or geography-pinned** (PaaS) | Provider processes inside a chosen geography; customer controls identity, logs, and often keys | Abuse-monitoring storage and human review; which models are actually available in-region |
| **Managed platform on "global" routing** | No residency guarantee | Processing anywhere the provider chooses |
| **Direct frontier-model API** | Depends entirely on the provider's current options | Options vary widely between providers and change often |
| **SaaS copilot or embedded AI** | Least visibility into the hosting chain | "Residency" claims often cover storage, not inference |

The full provider-by-provider detail, with dates checked, is in [Sovereignty by deployment model](../reference/sovereignty-by-deployment-model.md). Highlights as of November 2026 `[vendor documentation]`:

- On the managed platforms (Amazon Bedrock, Azure OpenAI / Microsoft Foundry, Google Vertex AI), the default or highest-throughput option is often "global" routing, which removes any residency guarantee. Preventive controls (AWS service control policies, Azure Policy, Google Cloud organization policies) are needed, not just procurement statements.
- Bedrock offers an Australian geographic inference profile that routes Sydney requests to Sydney or Melbourne.
- Anthropic's first-party API offered only US or global inference, with storage at rest in the US. Claude through Bedrock's Australian profile is the documented route to in-country inference for that model family.
- OpenAI offered Australian data residency at rest for new ChatGPT Enterprise and Edu workspaces from November 2025, and in-region API processing for approved enterprise customers.
- Microsoft revised its Microsoft 365 Copilot in-country processing plan in April 2026; local inferencing for Australia is now targeted for the end of 2026.

These facts change often. Check them at each assessment.

## Common traps

- **Defaults that quietly remove residency.** Global routing is frequently the default or the highest-capacity option.
- **Storage-only residency.** "Data at rest in Australia" with "processing anywhere" meets many storage-focused policies and fails policies that include processing.
- **Abuse monitoring.** On several platforms, flagged prompts are stored for review by provider staff. Removing this usually needs an approved exception, such as Azure's modified abuse monitoring or a zero-data-retention agreement.
- **Model-by-model availability.** A platform may offer in-region processing for some models and not others. Partner models on a hyperscaler platform may lack the in-region option the platform's own models have.
- **Keys that do not reach inference.** Customer-managed keys protect stored data. The operator still processes plaintext in memory.

## Legal reach and continuity

- **United States.** The CLOUD Act lets US authorities compel US providers to produce data they control, wherever it is stored. The Australia–US CLOUD Act Agreement (signed December 2021) prohibits the US from *targeting* Australian persons under that agreement, which narrows but does not remove exposure `[government]` ([Home Affairs](https://www.homeaffairs.gov.au/about-us/our-portfolios/national-security/lawful-access-telecommunications/australia-united-states-cloud-act-agreement)). FISA Section 702 lapsed on 12 June 2026 after short-term extensions, with collection continuing under existing court certifications `[secondary]` ([OPB/NPR](https://www.opb.org/article/2026/06/13/fisa-702-a-key-u-s-spy-tool-has-lapsed-now-what)); check its current status before relying on it either way.
- **Australia.** APRA treats AI under existing prudential standards. CPS 230 covers all contracted service providers from 1 July 2026, which brings AI vendors and their upstream dependencies into operational-risk management `[secondary]`.
- **Continuity.** The US AI Diffusion Rule, the first export control on model weights, was rescinded in May 2025 before its compliance date `[secondary]` ([Steptoe](https://www.steptoe.com/en/news-publications/international-compliance-blog/trump-administration-charts-new-path-on-ai-export-controls-with-significant-new-guidance-and-rescission-of-diffusion-rule.html)). The live continuity risks are policy volatility, unilateral provider suspension (Azure documents that "severe or recurring abuse may still lead to access limits"), and model deprecation.

See [Regulatory context](../reference/regulatory-context.md) for dates.

## Ranking access-suspension risk

From least to most exposed: self-hosted open weights (once the weights are held locally), then a multi-model managed platform (models can be swapped), then a single direct frontier API, then a SaaS copilot (no model swap possible).

## Method

1. Identify the deployment model and the exact provider options in use (region, routing tier, retention setting, abuse-monitoring status, key management).
2. Complete the six axes, citing the provider document and the date checked.
3. Compare with the organization's residency and transfer policies, and with any sector obligations (for example, APRA CPS 230 and CPS 234).
4. Record gaps and whether preventive controls enforce the intended configuration.
5. Feed the result to B13, and to B6 where a single upstream provider is shared across many use cases.

## Output

A sovereignty profile per use case, with dated evidence and any policy gaps.

Next: [Layer 4: Agency and tier](L4-agency-and-tier.md)
