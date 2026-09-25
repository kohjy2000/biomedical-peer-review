# Review State Template

Use this compact ledger to preserve progress, evidence locations, and decisions across long reviews, context compaction, or session handoff. It is an internal working record, not part of the author-facing report.

For a short task, maintain the equivalent state in the session. For work spanning multiple turns, keep one local state file when local file creation is authorized. Store it locally, include only the manuscript text needed to identify claims, and do not transmit it externally.

Update the ledger at stage boundaries rather than continuously. Keep identifiers stable unless the manuscript changes materially.

```markdown
# Review State

- Mode: Initial / R1 / R2 / Claim audit / Literature audit / Draft audit
- Current stage: S0 / S1 / S2 / S3 / S4 / S5
- Completed stages:
- Source set reviewed:
- Last verified:
- Next bounded action:

## S0 — Frame

- Journal and submission stage:
- Central question and intended contribution:
- Article/study type:
- Design, data, population/model, and setting:
- Primary claim ambition and intended scope:
- Claim-validity bar:
- Venue-completeness bar:
- Editor question or journal fields, if provided:

## S1 — Claim Map

H1 — [High-level claim]
- M1.1 — [Mid-level claim]
  - E1.1a — [Figure/Table/Result; actual contrast or estimand → endpoint]
  - E1.1b — [Figure/Table/Result; actual contrast or estimand → endpoint]
- M1.2 — [Mid-level claim]
  - E1.2a — [Figure/Table/Result]

H2 — [Repeat as needed]

## S2 — Appraisal

M1.1
- Evidence verdict: Supported / Partially supported / Unsupported / Not assessable
- Claim–evidence relation: Direct / Indirect / Non-discriminating / Contradictory
- Comparison-to-claim fit:
- Logic:
- Literature position:
- Controversy or competing model:
- Scope/generalization:
- Verification flag:

[Repeat for consequential mid-level claims]

High-level roll-up:
- H1 status:
- Strongest evidence:
- Weakest bridge:
- Defensible claim:
- Remaining overclaim:

## S3 — Issue Ledger

I1 — [Validity-critical / Venue-critical / Recommended / Minor]
- Affects: H# / M# / E#
- Evidence location:
- Problem:
- Scientific or editorial consequence:
- Required action:
- Purpose of evidence request, if any:
- Evidence-request role: Decisive / Valid alternative / Supporting characterization / Claim-calibration fallback
- Status: Open / Drafted / Resolved / Verification pending

[Repeat as needed]

Recommendation state:
- Scientific validity:
- Venue-level adequacy:
- Realistic revisability:
- Preliminary recommendation and rationale:

## S4 — Draft and Verification

- Overall Assessment drafted:
- Major Comments mapped to issue IDs:
- Recommended Revisions drafted, if used:
- Minor Comments drafted:
- Recommendation drafted:
- Confidential editor comment drafted, if used:

Verification:
- Quotes and claim verbs:
- Numbers and sample sizes:
- Figure/table references:
- Literature propositions and citations:
- Manuscript/response consistency:
- Existing analyses checked:
- Unresolved factual questions:

## S5 — Final Pruning

- Requested actions classified:
- Minimum required routes retained:
- Recommended strengthening moved or omitted:
- Alternative-route equivalence checked:
- Duplicated requests removed:
- Final word count and Major Comment count:
- Scientific judgment and recommendation unchanged:
- Earlier stage reopened, if required:

## Locked Decisions

- Exact wording or quotation:
- Inconsistency that must be flagged:
- Requests intentionally excluded:
- Tone/style requirement:

## Next

- [One bounded action]
```

On resume, read this ledger first, confirm that the cited source material is still available, and continue from the earliest incomplete stage. Do not rerun completed stages unless the source changed or the recorded state is unreliable.
