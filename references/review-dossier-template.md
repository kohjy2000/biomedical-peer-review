# Review Dossier Template

For a full initial review, instantiate this dossier only after `discovery-notes.md` has been saved under [discovery.md](discovery.md). Import the discovery record without alteration. Use the dossier for the remaining initial review and for every revision review. It is the retained analytical record and the session-state ledger; it is not part of the author-facing report. For a bounded claim, literature, or draft audit, complete only the sections needed for that scope.

Update it at stage boundaries rather than recording a running monologue. Preserve structured judgments, source propositions, evidence locations, and verification status; do not record private chain-of-thought or an unfiltered search log. Keep manuscript excerpts to the minimum needed to identify claims. Store the dossier locally and do not transmit it unless the user explicitly requests that action.

## Sections

- Status and source set
- D0–D1 open discovery and append-only candidate register
- S0 review calibration
- S1 structured claim–evidence map
- S2a literature and field context; S2b candidate validation and three-pass coverage; S2c coverage audit
- S3 issue and action ledger
- Revision resolution ledger
- S4 draft verification
- S5 final pruning and decision rationale
- Locked decisions and handoff

```markdown
# Review Dossier

## Status and Source Set

- Mode: Initial / R1 / R2 / Claim audit / Literature audit / Draft audit
- Current stage: D0 / D1 / S0 / S1 / S2a / S2b / S2c / S3 / S4 / S5
- Completed stages:
- Manuscript version and date:
- Source set reviewed:
- Sources intentionally excluded:
- Literature cutoff date:
- Last verified:
- Next bounded action:
- Dossier confidentiality or storage note:

## D0–D1 — Open Discovery

Import `discovery-notes.md` without rewriting, merging, prioritizing, or pruning its entries.

### Source-Coverage Sweep

| Source item | Reviewed / Not assessable | New D# candidates |
| --- | --- | --- |
| | | |

### Append-Only Candidate Register

Keep every D# row. Append C# rows discovered during S1, S2a, S2b, or S2c. Update status and traceability; never delete a row.

| Candidate | Origin | Source location | Open concern or question | Why it may matter | Affected H/M/E/K | Status | Reason | Issue ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D1 | D0 / D1 | | | | Pending mapping | Pending | Open discovery | |

Allowed status after S2b: `Validated / Weakened / Rejected / Unresolved`.

## S0 — Review Calibration

- Journal and submission stage:
- Article/study type:
- Central question and intended contribution:
- Design, data, population/model, and setting:
- Primary claim ambition and intended scope:
- Editor question, review fields, and recommendation options, if provided:

### Relevant Review Requirements

| Requirement or expectation | Provenance: Journal-stated / Field standard / Reviewer calibration | Basis or source | Consequence for this review |
| --- | --- | --- | --- |
| | | | |

- Claim-validity bar:
- Venue-completeness bar:
- Feasibility or material constraints stated in the manuscript or instructions:
- Assumptions not made about undisclosed data, samples, or resources:
- Calibration uncertainty or unresolved question:

## S1 — Structured Claim–Evidence Map

### H1 — [High-level claim in the authors' wording]

- Verb strength and claim level:
- Intended scope:
- Claimed novelty:

#### M1.1 — [Mid-level claim required for H1]

- Role in H1:
- Evidence type: observational / associative / predictive / perturbational / validation

##### E1.1a — [Figure/Table/Result and observation]

- Evidence location:
- Actual comparison, exposure, perturbation, or estimand:
- Experimental or inferential unit:
- Relevant time point:
- Measured endpoint:
- Authors' intended inference:
- Internal counter-evidence or limitation:

[Repeat E and M units as needed]

- Logical assembly of H1:
- Bridge claims or dependencies:
- Missing bridge or hidden assumption:

[Repeat H claims as needed]

## S2a — Literature and Field Context

Search targets (from S1):

| K# | Layer | Topic | Proposition | Context of validity | Expected direction/size | Related D/C/H/M/edge or entity | Assumption tested or alternative distinguished | Discriminating readout | Source ID | S2b use |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| K1 | Background / Specific | | | | | | | | L1 | Pending / Used / Set aside + reason |

### Literature Source Register

Include only sources that materially affect a claim verdict, evidence standard, experimental request, novelty judgment, or recommendation.

| Source ID | Full citation and DOI/PMID/stable URL | Role: foundational / consensus / supporting / conflicting / benchmark / precedent / recent update | Exact proposition supported | Affected D/C/H/M/I | Verified |
| --- | --- | --- | --- | --- | --- |
| L1 | | | | | Yes / No |

## S2b — Candidate Validation and Structured Appraisal

### Candidate Adjudication

Complete this only for D/C candidates, not for clean links.

#### D1 — [candidate label]

- Exact manuscript source and affected H/M/E or edge:
- Integrated challenge — required premise; strongest live alternative; whether the comparison, assay, experimental model, and analysis distinguish them:
- Relevant S2a propositions and sources:
- Evidence adequacy (`E→M`) when implicated:
- Individual-claim validity (`M`) when implicated:
- Claim-network effect (`M→H` or `H↔H`) when implicated:
- Status: Validated / Weakened / Rejected / Unresolved
- Reason and evidence that would change the judgment:
- Candidate register updated:

[Repeat for every D/C candidate]

### Pass A Coverage — Evidence Adequacy (`E→M`)

| E→M link | Visited | Relation | Exact proposition established / material limitation | D/C candidate IDs | K#/source used | Verification flag |
| --- | --- | --- | --- | --- | --- | --- |
| | Yes / Not assessable | Direct / Indirect / Non-discriminating / Contradictory / Not assessable | | | | |

### Pass B Coverage — Individual Claim Validity (`M`)

| M claim | Visited | Verdict | Defensible scope / material premise or alternative | D/C candidate IDs | K#/source used | Verification flag |
| --- | --- | --- | --- | --- | --- | --- |
| | Yes / Not assessable | Supported / Partially supported / Unsupported at stated level / Not assessable | | | | |

### Pass C Coverage — Claim-Network Validity (`M→H`, `H↔H`)

| H or edge | Visited | Necessary claims and bridge status | Defensible conclusion / material weak link | D/C candidate IDs | K#/source used | Verification flag |
| --- | --- | --- | --- | --- | --- | --- |
| | Yes / Not assessable | | | | | |

If a coverage row contains a material negative or limiting judgment, it must link an existing D/C candidate or append a new C# row before S2c.

## S2c — Coverage Audit

### Structural Coverage

| Coverage target | Complete / Not assessable / Missing | Missing item or disposition |
| --- | --- | --- |
| D1 source-coverage sweep includes every required source item | | |
| Every mapped E→M link has a Pass A relation | | |
| Every mapped M claim has a Pass B verdict | | |
| Necessary M→H and consequential H↔H links have Pass C judgments | | |
| Relevant K rows are Used or Set aside with reasons | | |
| Counter-evidence, negative results, unexplained observations, and uncertainty remain visible | | |
| Every D/C candidate has status, reason, and traceability | | |
| Every material limitation in S1–S2 links to a D/C candidate | | |

### Conditional Modules Used

| Module | Why applicable | Omission or bias signal | S2b pass reopened and result |
| --- | --- | --- | --- |
| | | | |

### Candidate Register Check

- Candidate rows deleted or overwritten: None / [explain and restore]
- Candidates added after open discovery:
- Validated or Weakened candidates not promoted to S3, with reason:
- Unresolved candidates and effect on the review:

## S3 — Issue and Action Ledger

### I1 — [Validity-critical / Venue-critical / Recommended strengthening / Minor]

- Affects: H# / M# / E#
- Origin: D/C candidate IDs and D0/D1 / S1 / S2a / S2b validation / Pass A / Pass B / Pass C / S2c conditional module / Minor sweep
- Exact evidence or manuscript location:
- Problem:
- Scientific or editorial consequence:
- Required action:
- Purpose of new evidence request, if any:
- Evidence-request role: Decisive / Valid alternative / Supporting characterization / Claim-calibration fallback
- Target inference and relevant precedent, if a specific experiment is named:
- Main confounder or limitation:
- Effect of positive, negative, or null result on the claim:
- Valid alternative route, if any:
- Claim-calibration fallback, if defensible:
- Status: Open / Drafted / Resolved / Verification pending

[Repeat as needed]

### Minor Sweep

Findings only; items that support a headline or consequential mid-level claim.

- [Location] — [class] — [problem]

Not checked: [item, class, reason], if any.

#### Terminology read (title, Abstract, Results subheadings)

- [Location] — "[exact wording]" — [problem]

### Recommendation State

- Central bottleneck:
- Scientific validity:
- Venue-level adequacy:
- Realistic revisability:
- Preliminary recommendation and rationale:

## Revision Resolution Ledger

Complete this section for R1/R2 reviews.

### Prior issue [number/title]

- Issue ID:
- Original concern and affected H/M/E:
- Author response:
- Verified manuscript change and location:
- Resolution: Fully resolved / Partially resolved / Unresolved / Not assessable
- Evidence for the resolution judgment:
- Remaining validity or venue-completeness gap:
- Remaining action, if any:

## S4 — Draft and Verification

- `peer-review.md` drafted:
- Major Comments mapped to issue IDs:
- Recommended Revisions drafted, if used:
- Minor Comments drafted:
- Recommendation drafted:
- Confidential editor comment drafted, if used:

### Verification

- Quotes and claim verbs:
- Numbers, denominators, and sample sizes:
- Figure, table, panel, section, and page references:
- Literature propositions and citation metadata:
- Journal or field-standard assertions:
- Manuscript/response consistency:
- Existing analyses or experiments checked:
- OCR or extraction artifacts checked:
- Unresolved factual questions:

## S5 — Final Pruning and Decision

- Requested actions classified:
- Minimum required routes retained:
- Recommended strengthening moved or omitted:
- Alternative-route equivalence checked:
- Duplicated requests removed:
- Final word count and Major Comment count:
- Scientific judgment and recommendation unchanged:
- Earlier stage reopened, if required:

### Final Decision Rationale

- Final recommendation:
- Claim-validity basis:
- Venue-completeness basis:
- Principal remaining issues:
- Why the requested actions are proportionate:
- Residual uncertainty:

## Locked Decisions and Handoff

- Exact wording or quotation that must be preserved:
- Inconsistency that must be flagged:
- Requests intentionally excluded:
- Tone or style requirement:
- Output paths for `peer-review.md` and `review-dossier.md`:
- Next bounded action, if unfinished:
```

On resume, read this dossier first, confirm that the cited source material remains available, and continue from the earliest incomplete stage. Do not rerun completed stages unless the source changed or the recorded state is unreliable.
