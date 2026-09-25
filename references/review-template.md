# Peer Review Templates

Use [review-dossier-template.md](review-dossier-template.md) for the working claim map, literature record, and issue ledger. This file converts the completed S3 synthesis into reviewer-facing prose. Apply [style-profile.md](style-profile.md) when drafting. The dossier remains a separate confidential artifact; do not paste its internal identifiers or full analytical record into the author-facing report.

## Pre-draft synthesis check

```markdown
- Central bottleneck:
- Scientific-validity judgment:
- Venue-level adequacy:
- Validity-critical issue IDs:
- Venue-critical issue IDs:
- Recommended-strengthening issue IDs:
- Minor issue IDs:
- Preliminary recommendation and rationale:
- Required evidence separated from supporting characterization:
- Verification flags that must be resolved before delivery:
```

Do not draft a Major Comment that lacks an S3 issue record with an affected claim or exact manuscript location, consequence, and action.

## Major Comment construction

Each Major Comment should normally contain:

1. one claim-level problem;
2. its scientific or editorial consequence;
3. the minimum required action;
4. when appropriate, one claim-calibration fallback.

Draft from the S3 classifications rather than trying to make every comment comprehensive. Final action triage, alternative-route checking, duplication removal, and length control occur in S5 using [final-pruning.md](final-pruning.md).

## Author-facing initial review

```markdown
Overall Assessment

[Usually 3–5 sentences. State what the manuscript studies and its genuine contribution, then identify the central evidentiary or logical risk and the level of revision needed. Limit praise to what is specific and defensible.]

Major Comments

1. [Short claim-focused title]
[Problem.] [Consequence for validity, interpretation, or venue-level completeness.] [Minimum required action and what it is intended to establish.] [Optional claim-calibration fallback, when scientifically and editorially defensible.]

2. [Short claim-focused title]
[Problem.] [Consequence.] [Minimum required action.]

[Continue only for validity-critical or venue-critical issues.]

Recommended Revisions

[Include only when the journal format permits a separate non-required section.]

1. [Material strengthening that is not required for claim validity or venue fit.]

Minor Comments

1. [Specific location and correction.]
2. [Specific location and correction.]

Recommendation

[Include only when requested by the journal or user. Use the journal's available options and add a concise rationale.]
```

## Confidential editor comment

```markdown
Confidential Comment to Editor

[Briefly state the value of the question or dataset, the central publication blocker, whether it concerns scientific validity or venue-level completeness, whether it is realistically revisable, and the likely outcome after adequate revision. Do not hide author-actionable scientific criticism here or copy the author-facing review verbatim.]
```

## Major Comment construction options

### Direct correction

Use when clarification, reanalysis, consistency correction, or claim moderation resolves the issue:

```markdown
[Problem and manuscript location.] [Scientific consequence.] Please [specific correction or analysis].
```

### Required evidence

Use when new evidence is necessary for claim validity or venue-level completeness:

```markdown
[Unsupported claim or missing evidence.] [Why the gap affects validity or the completeness required for this journal.] Please provide [specific evidence], which is needed to establish [causality / alternative exclusion / robustness / generalization / mechanistic completeness].
```

### Alternative route

Use only when both routes resolve the scientific issue and preserve a contribution appropriate for the current journal:

```markdown
[Problem.] [Why it matters.] Please either [direct evidentiary route] or, if the narrower contribution remains appropriate for this journal, [specific analysis, limitation, and claim revision].
```

Do not offer a nominal alternative that makes the claim defensible but leaves the paper below the current journal's publication threshold.
