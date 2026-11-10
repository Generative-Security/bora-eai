# Principles

Seven design rules shape BORA-EAI. When a part of the model is unclear, these decide it.

## 1. The use case is the unit of analysis

Executives fund, approve, constrain, and stop use cases, not models or systems. So BORA-EAI analyzes use cases.

A use case is a specific use of AI by a specific population for a specific purpose. A coding assistant for engineers, a customer-facing chatbot, and an AI feature a vendor switched on inside software you already own are three use cases, even if all three run on the same underlying model. They differ in four ways that drive both risk and value:

- **Who uses it:** employees, customers, agents acting for either.
- **What data it touches:** public, internal, confidential, regulated personal data, secrets.
- **What it may do:** answer, recommend, act within bounds, act freely.
- **Who carries the consequence:** which executive answers when it goes wrong, or when it fails to deliver.

Organizing around systems (STRIDE, MAESTRO), trust attributes (fairness, transparency, reliability), or controls (AICM, ISO 42001 Annex A) is useful underneath. None of them maps cleanly onto the decision an executive actually makes.

## 2. Both sides of the ledger

A use case can fail the business because it gets attacked, and just as easily because it never delivers. BORA-EAI puts both on the same page:

- risk-adjusted value, including the probability of reaching production and of delivering once there;
- expected loss from the business threat scenarios;
- the cost of governing the use case.

Declining to deploy is therefore a cost, not a safe default. This is not a new idea. ISO 31000 defines risk as the "effect of uncertainty on objectives," where the effect can be positive or negative, and the NIST AI RMF asks organizations to document an AI system's potential benefits (MAP 3.1) as well as its potential costs (MAP 3.2). What we could not find was that principle applied use case by use case, across all the owners.

## 3. Two lenses

Internal and customer-facing use cases fail in different ways, and applying one lens to both mis-rates one of them.

- The [internal lens](lenses/internal.md) concentrates on permissions, data exposure, and whether the productivity gain is real for the people using the tool.
- The [customer-facing lens](lenses/customer-facing.md) concentrates on what the AI may say or offer, who is liable when it gets that wrong, and what revenue it protects or puts at risk.

## 4. Depth matches stakes

Not every use case deserves a full assessment. Requiring one would make the approved path slower than shadow AI, and the model itself would drive the shadow-AI scenario (B3). So:

- a **fast lane** registers pre-approved patterns without assessment;
- **Low** tier use cases get a qualitative screen and no numbers;
- **Medium** tier use cases get ranges for their top three scenarios and for value;
- **High** tier use cases get full quantification, red teaming, insurance review, and board reporting.

Two override rules lift a use case to at least Medium however little it can do: read access to regulated personal data, and customer-facing representations or concessions. See [Tiering](05-tiering.md).

Not every exposure comes with a clean price tag. Air Canada's loss was small in dollars, and the precedent was the real cost. Reputation, customer trust, and sovereignty resist quantification. BORA-EAI records those qualitatively rather than forcing a number.

## 5. One accountable owner

Every use case has one executive accountable for its net position. Every business threat scenario has exactly one accountable control owner: the executive who holds the main lever that prevents the loss. Everyone else is consulted. Shared accountability produces committee paralysis and finger-pointing during an incident. See [Accountability](04-accountability.md).

## 6. Ranges, not points

Multiplying subjective probabilities by uncalibrated loss estimates and presenting one dollar figure gives a board false precision. Every BORA-EAI input is a calibrated three-point estimate (low, most likely, high), combined by Monte Carlo simulation, which is how FAIR analyses already work. The board sees a range, the probability that the net position is below zero, and a 1-in-20-year loss, so that rare large events are not averaged away. Where data is thin, a wide range is the honest answer. See [Quantification](06-quantification.md).

## 7. Borrow before inventing

Most of BORA-EAI is assembled from published work: AWS's scoping matrices, CSA's AI Controls Matrix and capability-based risk assessment, FAIR, the Geneva Association's loss domains, COSO's GenAI capability types, the ISO/IEC AI standards, the NIST AI RMF, Huwyler's threat taxonomy, the OWASP lists, and the MIT AI Risk Repository. We build only where we found a gap, and we label what we built so reviewers know where to push. See [Status and limitations](validation/status-and-limitations.md).

Next: [Method](03-method.md)
