# JYK Biomedical Peer Review Skill

A claim-focused workflow for reviewing immunology and biomedical manuscripts with Codex, Claude Code, and other Agent Skills-compatible environments.

The skill reconstructs a manuscript as a hierarchical claim-evidence map, evaluates evidence robustness and logical connections, positions each important claim against the literature, calibrates the evidence bar to the study type and journal, and produces an actionable reviewer report. It supports initial submissions, revised manuscripts, audits of existing review drafts, and long-session handoffs.

## What it is designed to evaluate

- whether the evidence supports each claim at the stated strength and scope;
- whether high-level conclusions are assembled from supported mid-level claims;
- whether the work confirms, extends, contradicts, refines, or discriminates among prior models;
- whether relevant controversy, field standards, and experimental precedent change the judgment;
- whether requested revisions are validity-critical, venue-critical, recommended strengthening, or minor;
- whether a proposed experiment actually resolves the affected inference;
- whether the final review is concise, traceable, and proportionate.

The workflow uses six stages:

| Stage | Purpose |
| --- | --- |
| S0 | Frame the study, claim ambition, and evidence bars |
| S1 | Build the hierarchical claim-evidence map |
| S2 | Appraise evidence, logic, literature, controversy, and novelty |
| S3 | Convert findings into a classified issue ledger |
| S4 | Draft and source-verify the reviewer-facing report |
| S5 | Remove redundant or non-decisive requests without changing the judgment |

## Repository structure

```text
jyk-peer-review/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── workflow.md
    ├── review-framework.md
    ├── review-state-template.md
    ├── review-template.md
    ├── style-profile.md
    ├── revision-review.md
    └── final-pruning.md
```

`SKILL.md` is the entry point. Detailed guidance is loaded from `references/` only when needed. `agents/openai.yaml` supplies optional Codex UI metadata; it is not required by Claude Code.

## Install

### Codex

```bash
git clone https://github.com/kohjy2000/jyk-peer-review.git ~/.codex/skills/jyk-peer-review
```

Invoke explicitly with:

```text
$jyk-peer-review
```

### Claude Code

Install globally for the current user:

```bash
git clone https://github.com/kohjy2000/jyk-peer-review.git ~/.claude/skills/jyk-peer-review
```

Or install it in one project:

```bash
git submodule add https://github.com/kohjy2000/jyk-peer-review.git .claude/skills/jyk-peer-review
```

Invoke explicitly with:

```text
/jyk-peer-review
```

Both platforms can also select the skill automatically when the request matches its description.

## Example request

```text
Use the jyk-peer-review skill to perform an independent initial peer review of the attached manuscript and its directly associated supplements. Build the claim-evidence map before drafting. Verify literature claims and citations, separate validity-critical from venue-critical issues, and complete the final-pruning stage before delivering the review. Do not use prior reviews, response letters, later revisions, or the published version unless I explicitly provide them as part of the review task.
```

For a revision, provide the prior reviewer report, point-by-point response, revised manuscript, updated figures or supplements, and editor instructions when available.

## Expected output

Unless the journal requires a different format, the skill produces:

1. Overall Assessment
2. Major Comments
3. Recommended Revisions, when useful
4. Minor Comments
5. Recommendation, when requested
6. Confidential Comment to Editor, when useful

The internal claim map and issue ledger are working artifacts and are not included in the reviewer-facing report unless they improve clarity or the user requests them.

## Tool and model considerations

The skill is instruction-based and does not bundle a PDF parser, literature database, or browser. Review quality therefore depends on the model and the document, search, and citation-verification capabilities available in the host environment.

- If a source cannot be accessed or verified, the skill should mark the affected judgment as not assessable rather than infer it.
- A named experiment should be proposed only when its discriminating value is supported by domain knowledge or directly relevant literature.
- Results can differ across models even when the same workflow is used. Report the platform, model, reasoning setting, and task type when submitting feedback.

## Confidentiality

Peer-review materials may be confidential. Use this skill only in environments permitted by the journal, institution, and applicable agreements.

Do not post unpublished manuscripts, manuscript excerpts, reviewer identities, response letters, submission identifiers, or other confidential material in GitHub Issues, Discussions, pull requests, or public test cases. Use public papers, preprints, synthetic examples, or de-identified behavioral descriptions when reporting problems.

The skill never authorizes submitting a review, contacting a journal, or transmitting manuscript material. Those actions require an explicit user request and an appropriate authorized tool.

## Contributing and feedback

Real-world feedback is welcome, especially on missed claim-evidence gaps, excessive experimental demands, weak literature positioning, incorrect severity, or unnecessary review length. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and use the structured Skill Feedback issue form.

This project is not affiliated with or endorsed by OpenAI, Anthropic, or any journal.

## License

Released under the [MIT License](LICENSE).
