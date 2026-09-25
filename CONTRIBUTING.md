# Contributing

Feedback and focused pull requests are welcome.

## Confidentiality first

Do not submit unpublished manuscripts, excerpts, figures, tables, response letters, reviewer identities, submission identifiers, or journal-confidential information. Use one of the following instead:

- a public paper or preprint with a DOI or stable URL;
- a synthetic example;
- a de-identified description of the model's behavior.

If an example cannot be shared safely, describe only the general failure mode.

## Useful feedback

Include, when possible:

- platform and version;
- model and reasoning setting;
- review mode: initial, revision, claim audit, literature audit, or draft audit;
- manuscript genre and approximate journal level;
- expected behavior and observed behavior;
- whether the problem concerns scientific judgment, workflow adherence, literature verification, prioritization, or writing;
- a minimal public or synthetic reproduction case.

High-value reports include missed critical claims, non-discriminating evidence treated as direct, unsupported controversy, excessive experimental requests, invalid fallback routes, incorrect recommendation severity, loss of dossier traceability, and failures during final pruning.

## Pull requests

Keep changes narrow and explain the observed failure they address. Avoid adding universal rules based on one manuscript. New instructions should change a consequential decision, improve traceability, or prevent a demonstrated failure.

Before opening a pull request:

1. check all relative links from `SKILL.md` and the reference files;
2. confirm that no local paths or confidential identifiers are present;
3. test at least one direct invocation and one realistic task;
4. describe any model-specific behavior rather than presenting it as universal.
