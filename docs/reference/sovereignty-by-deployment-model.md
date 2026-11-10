# Sovereignty by deployment model

Supporting reference for [Layer 3](../layers/L3-sovereignty-profile.md) and [B13](../scenarios/B13-sovereignty-jurisdiction-continuity.md). Provider terms change often. **Every fact on this page was checked on or about 6 November 2026** and should be re-checked at each assessment. Items we could not verify are listed at the end, not presented as fact.

All entries are `[vendor documentation]` unless labeled otherwise.

## Managed platforms (PaaS)

### Amazon Bedrock

- **Routing tiers:** in-region; geographic cross-region inference (keeps requests within a geography such as US, EU, AU, JP); global cross-region inference, which "can route to any supported AWS commercial Region worldwide". AWS says global is appropriate only "if your compliance rules allow processing in any commercial Region" ([AWS ML Blog](https://aws.amazon.com/blogs/machine-learning/securing-amazon-bedrock-cross-region-inference-geographic-and-global/)).
- **Australia:** an AU geographic profile routes requests from Sydney to Sydney or Melbourne.
- **Logging and storage:** cross-region calls are logged in the source region's CloudTrail with an `inferenceRegion` field. Cross-region inference "doesn't change where data is stored"; logs, knowledge bases, and configuration stay in the source region.
- **Abuse detection:** if a model requires storage for abuse detection, prompts and outputs are stored in the *destination* region ([Bedrock docs](https://docs.aws.amazon.com/bedrock/latest/userguide/geographic-cross-region-inference.html)).
- **Preventive control:** service control policies can deny global profiles; region-restricting policies must allow every destination region in a geographic profile.
- **Note:** the Bedrock documentation we read listed us, eu, apac, and in profile prefixes without an `au` prefix, while the AWS blog confirms an AU geography. Check the current console.

### Azure OpenAI / Microsoft Foundry

(Page last updated 19 May 2026.)

- **Deployment types:** Standard (regional, may move between regions within the geography); DataZone (anywhere in a zone such as US or EU); Global (processed "in any geography where the model is deployed"). For Global and DataZone, data at rest, including the abuse-monitoring store, stays in the customer's geography; only processing moves ([Microsoft Learn](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/data-privacy)).
- **Training:** prompts and completions are not available to OpenAI or other customers and are not used to train base models without permission.
- **Abuse monitoring:** flagged content is stored per geography; authorized Microsoft employees review it on secure workstations with just-in-time approval. For EEA deployments, reviewers are in the EEA. Customers can apply for modified abuse monitoring, which removes storage and human review; automated review continues, and "severe or recurring abuse may still lead to access limits".
- **Keys:** AES-256 at rest; customer-managed keys supported, with some preview features excepted.
- **Australia:** the page makes no Australia-specific statements.

### Google Vertex AI

(Now documented under "Gemini Enterprise Agent Platform"; page last updated 4 November 2026.)

- Data at rest stays in the selected location whatever endpoint is used. Jurisdictional multi-regions (US, EU) keep processing within the jurisdiction; the EU multi-region excludes the UK and Switzerland. Single-region endpoints keep processing in that region. Global endpoints "don't provide regional isolation or data residency guarantees" ([Google Cloud](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/data-residency)).
- **Australia:** the table for Google's own models has an `australia-southeast1` column. The tables for partner and open models have no Australia column, which implies partner models (including Claude on Vertex) lack an Australian processing guarantee.

## Direct frontier-model APIs

### Anthropic (Claude API)

- Two separate controls: `inference_geo` (per request or workspace default) supports only `"us"` and `"global"`, defaulting to global; **workspace geography**, which sets storage at rest, supports only `"us"` and cannot be changed after creation ([Claude docs](https://platform.claude.com/docs/fr/manage-claude/data-residency); the English page was not reachable, so the same document in French was read).
- US-only inference is priced at 1.1x on newer models. On Bedrock and Vertex, region is set by the platform's endpoint or profile instead.
- **Australia:** no Australian option on the first-party API as of this check. Claude through Bedrock's AU profile is the documented route to in-country inference. Anthropic has committed to lease data-center capacity in Queensland for inference, targeted for 2027 and subject to approvals `[secondary]`.

### OpenAI

- From 25 November 2025, data residency for ChatGPT Enterprise, ChatGPT Edu, and the API Platform expanded to regions including **Australia**. For ChatGPT, conversations, files, custom GPTs, and image artifacts are stored at rest in-region, for *new* workspaces created with residency. For the API, approved enterprise customers can create region-pinned projects whose requests are "handled in-region" and not stored at rest ([OpenAI](https://openai.com/index/expanding-data-residency-access-to-business-customers-worldwide)).
- Whether ChatGPT *inference* is in-region was not stated on that page. OpenAI's help article is now titled "Data residency and inference residency", but we could not read it.

## SaaS copilots

### Microsoft 365 Copilot

- November 2025 plan: in-country processing of Copilot interactions in Australia, the UK, India, and Japan by the end of 2025. Updated 3 April 2026: Microsoft is "refining our timeline and scope". Local inferencing for **Australia**, India, the UAE, the UK, and the US is now targeted for the **end of 2026**; Canada 2027; Japan 2028. EU/EFTA get regional inferencing under the EU Data Boundary. In-country data residency at rest is offered in 27 countries ([Microsoft 365 Blog](https://www.microsoft.com/en-us/microsoft-365/blog/2025/11/04/microsoft-offers-in-country-data-processing-to-15-countries-to-strengthen-sovereign-controls-for-microsoft-365-copilot/)).

## Comparison by axis

| Axis | Self-hosted open weights | Managed PaaS, pinned | Managed PaaS, global | Direct frontier API | SaaS copilot / embedded |
|---|---|---|---|---|---|
| Inference location | Customer | Chosen geography | Anywhere | Provider-dependent (often US or global) | Often undisclosed or storage-only commitment |
| Data at rest | Customer | Customer's region; abuse store may differ | Customer's region (Azure); varies | Provider-dependent (Anthropic: US) | Vendor commitment, often by country |
| Plaintext access | Customer | Provider abuse reviewers unless exempted | Same | Provider; zero-retention by agreement | Vendor and its sub-processors |
| Key custody | Customer | Customer-managed keys at rest (in-memory plaintext remains) | Same | Generally provider | Generally vendor |
| Legal reach | Infrastructure operator | US parent (CLOUD Act) | US parent | US parent | US parent, plus vendor's own |
| Continuity | Highest once weights held | Models swappable within platform | Same | Single provider | Lowest; no model swap |

## Not verified in this draft

- Exact list of Bedrock models available in the AU geographic profile; Bedrock's own data-privacy statements.
- Which Azure OpenAI models are available as Standard regional deployments in Australia East; whether Australia has a DataZone.
- Which Gemini models have processing in `australia-southeast1`.
- Default retention periods for Anthropic, OpenAI, and Gemini APIs (commonly cited as 30 days for the first two).
- Claude Enterprise and Team residency; Gemini for Workspace residency in Australia.
- Whether ChatGPT Enterprise or Claude Enterprise support customer-managed or external keys.
- Australian Hosting Certification Framework status and IRAP assessments of the main AI platforms.
- Residency of AI embedded in major SaaS platforms (for example, Salesforce, ServiceNow).

Contributions with dated primary sources are welcome.
