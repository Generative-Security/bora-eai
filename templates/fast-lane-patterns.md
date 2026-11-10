# Fast-lane patterns

> BORA-EAI v0.1 template. A fast-lane pattern is a pre-approved combination of tool, data, users, and agency. A use case that matches a pattern is registered, not assessed. See [Tiering](../docs/05-tiering.md#fast-lane).

## Conditions every pattern must meet

- Tool or platform approved under enterprise terms (Scope 2 with a contract, or the organization's approved Scope 3 platform).
- Approved data classes only; no regulated personal data; no secrets.
- Agentic scope 1 or 2 (no autonomous actions).
- Internal users; no output shown to customers as the company's statement.
- Not used to make or materially support decisions about individuals.
- Does not trigger either override rule.

## Pattern register

| ID | Pattern | Approved tool or platform | Approved data classes | Users | Agency | Exclusions | Owner | Approved | Review by |
|---|---|---|---|---|---|---|---|---|---|
| FL-01 *(example)* | Meeting and document summaries | Licensed enterprise copilot | Internal, confidential (no regulated personal data) | All staff | Scope 1 | HR, legal privilege, and board materials | CIO | | |
| FL-02 *(example)* | Drafting and editing internal communications | Licensed enterprise chat assistant | Public, internal | All staff | Scope 1 | Customer-facing publication without review | CIO | | |
| FL-03 *(example)* | Code completion in approved repositories | Approved coding assistant under enterprise terms | Source code in approved repositories; no secrets | Engineering | Scope 2 (suggestions only) | Agent mode; repositories containing customer data; secrets | CTO | | |
| FL-04 *(example)* | Analysis of public information | Approved assistant with web access | Public | All staff | Scope 1 | Uploading internal files | CIO | | |

## Registering a fast-lane use case

Record in the [use-case register](use-case-register.csv): use-case name, accountable executive, pattern ID, users, and review date. The quarterly inventory sweep checks that registered use cases still match their pattern.

## Reviewing patterns

Every six months, the program owner, CIO, CISO, and DPO review:

- incidents or near misses involving fast-lane use cases;
- whether patterns have drifted (for example, a tool gaining agent features);
- shadow-AI discovery that suggests a new pattern is needed;
- time from request to registration.
