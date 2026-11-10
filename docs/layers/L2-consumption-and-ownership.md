# Layer 2: Consumption and ownership

> **Executive question:** Who controls the application, the model and the data? Who is accountable for this use case?

## Purpose

How an organization consumes AI decides who controls what, and therefore where residual risk sits: with the organization, with a vendor under contract, or with a vendor under no contract at all. Layer 2 records that structure and names the one executive accountable for the use case's net position.

## Consumption scopes

BORA-EAI uses the five scopes of the AWS Generative AI Security Scoping Matrix `[vendor, vendor-neutral in substance]` ([AWS](https://aws.amazon.com/blogs/security/securing-generative-ai-applying-relevant-security-controls/)), plus one new scope.

| Scope | Description | Organization controls | Provider controls | Example |
|---|---|---|---|---|
| **1. Consumer app** | Public service under consumer terms | Only the data it sends | Application, model, training data, terms | An employee using a free chatbot |
| **2. Enterprise app** | Service under an enterprise agreement | Its data, plus contract terms | Application, model, training data | A licensed copilot; GenAI features in a CRM bought for them |
| **2e. Vendor-enabled embedded AI** *(new)* | AI added by a vendor to software the organization already uses, under terms written before the AI existed or changed after purchase | Its data, and whatever the existing contract happens to say | Application, model, sub-processors, and often the decision to turn the feature on | A meeting tool, file-transfer service, or ERP that adds AI features to an existing subscription |
| **3. Pre-trained model** | The organization builds an application on a foundation model | Application and its data | Model and training data | A retrieval-augmented chatbot on a managed model platform |
| **4. Fine-tuned model** | The organization fine-tunes a model on its own data | Application, fine-tuning data, fine-tuned model | Base model and its training data | A fine-tuned classifier for claims |
| **5. Self-trained model** | The organization trains from scratch | Everything | Infrastructure only | Rare outside large technology firms |

### Why Scope 2e

Scope 2 assumes the organization chose to buy AI and negotiated terms for it. Scope 2e is different: the AI arrived inside software bought for another purpose, often switched on by default, sometimes with terms changed to permit training on customer content. Zoom (2023), Adobe (2024), and WeTransfer (2025) each changed terms in ways customers read as permitting AI training on their content, then clarified or reversed after public backlash `[secondary]` (see [B7](../scenarios/B07-vendor-enabled-embedded-ai.md)). The exposure is contractual and regulatory, it is created by the vendor rather than the customer, and it reaches the customer through press coverage more often than through notice. That warrants its own scope.

## The supply chain behind each use case

Most AI use cases sit on a chain of providers. The CSA AI Controls Matrix (AICM) shared-responsibility model names five roles `[industry-body]` ([CSA research note](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/07/CSA_research_note_aicm_v1_1_update_20260730-csa-styled.pdf)):

| Role | What they provide |
|---|---|
| Cloud service provider | Infrastructure |
| Model provider | The foundation model |
| Orchestrated service provider | Platforms that combine models, tools, and data (managed AI platforms, agent frameworks) |
| Application provider | The application the user sees |
| AI customer | The organization using it |

For each use case, record who fills each role. A SaaS assistant built on a frontier model served through a hyperscaler is a three-deep chain. The Australian Prudential Regulation Authority (APRA) described this pattern in its 30 April 2026 letter to industry: many "wrapper" products depend on the same few upstream platforms, creating fourth-party risk, and APRA expects regulated entities to review single-upstream-vendor dependencies `[secondary: law-firm summary]` ([HWL Ebsworth](https://hwlebsworth.com.au/not-so-fast-apra-issues-ai-reminder-ahead-of-cps-230-deadline/)).

Also record **integration tokens**: what the AI application can reach in other systems through OAuth grants, API keys, or connectors. In the Salesloft Drift breach (August 2025), attackers stole the AI chat vendor's integration tokens and used them to reach more than 700 customers' Salesforce instances `[secondary]` ([TechTarget](https://www.techtarget.com/searchsecurity/news/366630934/News-brief-Salesloft-Drift-breach-update-and-timeline)). The tokens, not the model, were the exposure.

## Naming the accountable executive

Confirm the one executive accountable for the use case's net position, usually the business sponsor. See [Accountability](../04-accountability.md). If two executives both claim the use case, it is probably two use cases.

## Method

1. Assign the consumption scope. Where a use case spans scopes (for example, an in-house application calling a SaaS AI API), record the lowest-control scope as primary.
2. Fill the five supply-chain roles, naming providers.
3. List integration tokens and the systems they reach.
4. Record the contract status: none, consumer terms, enterprise agreement, data processing agreement, AI-specific terms (training use, retention, notice of change, sub-processors, IP indemnity).
5. Confirm the accountable executive.

## Output

A responsibility map per use case: scope, supply chain, integrations, contract status, and accountable executive.

## Scenarios this layer drives

| Scope or finding | Raises |
|---|---|
| Scope 1 | B3 (shadow-AI leakage), B5 (IP), B13 |
| Scope 2 | B2, B6, B7 |
| Scope 2e | B7 above all; B13 |
| Scope 3 to 5 | B4, B9, B11; B5 for training data |
| Deep supply chain or shared upstream provider | B6, B13 |
| Broad integration tokens | B6, B9, B11 |

## Pitfalls

- **Assuming Scope 2 is safe.** An enterprise agreement moves some risk to the vendor; it does not remove the use case's exposure.
- **Ignoring the chain.** The vendor you contract with is rarely the one running the model.
- **Overlooking tokens.** An AI application with broad OAuth grants is an access path into everything it connects to.

Next: [Layer 3: Sovereignty profile](L3-sovereignty-profile.md)
