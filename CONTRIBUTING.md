# Contributing to BORA-EAI

Thank you for helping test and improve Business Outcome Risk Analysis for Enterprise AI (BORA-EAI). It is a working draft, and outside review is the main way it will get better.

By contributing, you agree that your contribution is licensed under the same [CC BY 4.0](LICENSE) license as the rest of the repository, and that you have the right to contribute it.

## What we most want

In rough order of value:

1. **Evidence that breaks or calibrates the model.** Incidents that do not fit any scenario, or fit two equally well. Loss data, frequency data, or uplift data for a line of business. Primary sources beat summaries.
2. **Executive feedback.** If you are a CISO, CRO, General Counsel, CFO, COO, or board member: does the language match how you think about the risk? Would you accept the accountability assignments?
3. **Missed models.** Published business-level AI risk or threat models we did not find, especially from consultancies, insurers, and regulators.
4. **Corrections.** Wrong facts, broken links, stale regulatory dates, provider terms that have changed.
5. **Field reports.** You ran a real use case through BORA-EAI. How long did it take? Where did the method fail?

## How to contribute

- **Quick feedback or a question:** open an issue with the [feedback template](.github/ISSUE_TEMPLATE/feedback.md), or email questions@generativesecurity.ai.
- **A new or changed scenario:** open an issue with the [scenario proposal template](.github/ISSUE_TEMPLATE/scenario-proposal.md) before writing a pull request. Scenario changes affect IDs, ownership, and the loss sum, so we discuss them first.
- **Evidence:** use the [evidence submission template](.github/ISSUE_TEMPLATE/evidence-submission.md).
- **Corrections:** use the [correction template](.github/ISSUE_TEMPLATE/correction.md), or open a pull request directly for small fixes.

## Editorial rules

These keep the model honest and usable.

**Label your evidence.** Every factual claim carries an [evidence label](docs/reference/evidence-labels.md) such as `[peer-reviewed]`, `[survey]`, `[vendor]`, or `[unverified]`. A claim from a seller of the relevant product is labeled `[vendor]` even when the data looks good. If you could not check a figure against its primary source, say so.

**Report incidents plainly.** State what happened, to whom, and what it cost. Do not add exculpatory asides about a vendor's intent, or soften an incident by noting an apology or a fix alongside it, unless the fix is itself the point being made.

**Write for executives first.** Scenario names and descriptions should be recognizable to a non-technical executive. Technical decomposition belongs in the crosswalk sections, not the scenario statement.

**Keep IDs stable.** Once published, scenario IDs (B1 to B15) are permanent. A new scenario takes the next free number. A retired scenario keeps its ID and is marked retired. Never renumber a published ID.

**One accountable owner.** Every scenario has exactly one accountable (A) executive: the one who holds the main lever that prevents the loss. Other functions are consulted (C). Proposals that add a second accountable owner will be asked to choose.

**Borrow before inventing.** If an existing framework already does what you are proposing, cite and reuse it. Mark anything new as new, so reviewers know what needs testing.

**Date anything that moves.** Regulatory dates, provider terms, and product availability change. Give the date you checked.

**Spelling and style.** US English. Plain, direct sentences. Avoid jargon where a plain word works.

## Pull requests

- Keep each pull request to one logical change.
- Update the [CHANGELOG](CHANGELOG.md) under "Unreleased".
- If you change a scenario, layer, or owner, update every page that refers to it (the README tables, the scenario catalog, the crosswalk, and the templates).
- Run a link check if you can. Relative links should resolve within the repository.

## Versioning

BORA-EAI uses `MAJOR.MINOR` versions while in draft. Minor versions add or revise content. A major version will mark the first validated release. Scenario IDs never change between versions.

## Conduct

Participation is governed by our [Code of Conduct](CODE_OF_CONDUCT.md).
