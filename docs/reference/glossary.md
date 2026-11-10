# Glossary

**Accountable owner.** The single executive answerable for a use case's net position, or for a scenario's control lever. See [Accountability](../04-accountability.md).

**Agentic scope.** How much an AI system can do without per-action human approval, from 1 (no agency) to 4 (full agency), following the AWS Agentic AI Security Scoping Matrix.

**Agent.** An AI system that takes actions (calls tools, changes systems, communicates, transacts), not only produces text.

**Beta-PERT distribution.** A probability distribution defined by a low, most likely, and high value, commonly used for expert estimates.

**CBRA.** Capabilities-Based Risk Assessment, published by the Cloud Security Alliance in November 2025. Scores AI systems on criticality, autonomy, permissions, and impact radius to assign a tier.

**Channel owner.** The executive responsible for a customer-facing channel (for example, head of customer experience or digital sales).

**Consulted.** A function whose input is sought on a scenario but which is not accountable for it.

**Consumption scope.** How the organization consumes AI, from Scope 1 (consumer app) to Scope 5 (self-trained model), following the AWS Generative AI Security Scoping Matrix, plus BORA-EAI Scope 2e (vendor-enabled embedded AI).

**Cost of delay.** The value lost per period of waiting to deploy a use case.

**Customer-facing lens.** BORA-EAI lens for use cases whose output reaches customers as the company's statement or acts on their behalf.

**Expected annual loss.** Frequency times magnitude, averaged over a year. Reported alongside the 1-in-20-year loss, never alone.

**FAIR.** Factor Analysis of Information Risk, an Open Group standard for quantifying information risk as loss event frequency times loss magnitude. **FAIR-AIR** is the FAIR Institute's approach for AI risk.

**Fast lane.** Registration without assessment for use cases that match a pre-approved pattern. See [Tiering](../05-tiering.md#fast-lane).

**First-party loss.** A loss the organization bears directly. **Third-party loss** is liability to others.

**Fourth party.** A supplier's supplier, such as the model provider behind a SaaS vendor's AI feature.

**Frontier (jagged frontier).** The uneven boundary of tasks a model can do well. Inside it, AI tends to help; outside it, accuracy can fall.

**Gross annual value.** The value a use case would deliver in a year if it reached production and worked: affected labor cost or revenue times uplift.

**Integration token.** An OAuth grant, API key, or connector credential that lets an AI application reach another system.

**Internal lens.** BORA-EAI lens for use cases used by employees whose output stays inside the organization.

**Lens.** One of two perspectives (internal or customer-facing) that shape which questions and scenarios dominate an assessment.

**Line of business.** A function or business unit (for example, IT, customer service, HR, finance, product, operations).

**MCP server.** A Model Context Protocol server, which gives an AI agent access to tools or data. A common component in agent supply chains.

**Monte Carlo simulation.** Repeated random sampling from input distributions to produce a distribution of outcomes.

**Net annual position.** Risk-adjusted value minus expected annual loss minus allocated governance cost, per use case, expressed as a distribution.

**1-in-20-year loss.** The annual loss exceeded with 5% probability: the 95th percentile of the annual loss distribution.

**Override rule.** A rule that lifts a use case to at least Medium tier regardless of its CBRA score: read access to regulated personal data, or customer-facing representations or concessions.

**P(production).** The probability a use case reaches production at all.

**P(value | production).** The probability a use case delivers its expected value once in production.

**Program owner.** The executive who runs BORA-EAI program: register, reviews, and ERM translation. Not accountable for every scenario.

**Prompt injection.** Instructions planted in input or retrieved content that cause an AI system to act against its intended behavior.

**Retrieval-augmented generation (RAG).** An AI pattern that retrieves documents and supplies them to a model to ground its answer.

**Scenario.** One of BORA-EAI's fifteen business threat scenarios: a business outcome an executive would recognize, with one accountable owner.

**Scenario statement.** A scenario written for a specific use case in the FAIR-AIR form: probability, cause, outcome, party, loss range.

**Shadow AI.** AI use without formal approval, risk assessment, or governance oversight.

**Sovereignty profile.** The six-axis record of where a use case runs and rests, who can see its data, who holds the keys, whose law reaches it, and how hard it is to leave.

**Tier.** Fast lane, Low, Medium, or High; decides how much analysis a use case receives.

**Uplift.** The change in productivity, quality, or revenue per affected unit from using AI. Can be negative.

**Use case.** A specific use of AI by a specific population for a specific purpose. BORA-EAI's unit of analysis.
