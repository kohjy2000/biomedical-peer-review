# Review Dossier Template

Use this dossier for every full initial or revision review. It is the retained analytical record and the session-state ledger; it is not part of the author-facing report. For a bounded claim, literature, or draft audit, complete only the sections needed for that scope.

Update it at stage boundaries rather than recording a running monologue. Preserve structured judgments, source propositions, evidence locations, and verification status; do not record private chain-of-thought or an unfiltered search log. Keep manuscript excerpts to the minimum needed to identify claims. Store the dossier locally and do not transmit it unless the user explicitly requests that action.

## Sections

- Status and source set
- S0 review calibration
- S1 structured claim–evidence map
- S2a literature and field context; S2b three-pass appraisal; S2c coverage audit
- S3 issue and action ledger
- Revision resolution ledger
- S4 draft verification
- S5 final pruning and decision rationale
- Locked decisions and handoff

```markdown
# Review Dossier

## Status and Source Set

- Mode: Initial / R1 / R2 / Claim audit / Literature audit / Draft audit
- Current stage: S0 / S1 / S2a / S2b / S2c / S3 / S4 / S5
- Completed stages:
- Manuscript version and date:
- Source set reviewed:
- Sources intentionally excluded:
- Literature cutoff date:
- Last verified:
- Next bounded action:
- Dossier confidentiality or storage note:

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

| K# | Layer | Topic | Proposition | Context of validity | Expected direction/size | Related H/M/edge or entity | Assumption tested or alternative distinguished | Discriminating readout | Source ID | S2b use |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| K1 | Background / Specific | | | | | | | | L1 | Pending / Used / Set aside + reason |

### Literature Source Register

Include only sources that materially affect a claim verdict, evidence standard, experimental request, novelty judgment, or recommendation.

| Source ID | Full citation and DOI/PMID/stable URL | Role: foundational / consensus / supporting / conflicting / benchmark / precedent / recent update | Exact proposition supported | Affected H/M/I | Verified |
| --- | --- | --- | --- | --- | --- |
| L1 | | | | | Yes / No |

## S2b — Claim Appraisal

### Pass A — Evidence Adequacy (`E→M`)

#### E1.1a → M1.1

- Inference alignment — comparison/perturbation, time, population, estimand, endpoint:
- Measurement validity — readout, marker, target, or proxy in this context:
- Experimental system/model fit — context of use, preserved biology, distortions, generalization boundary:
- Internal validity — controls, unit, independence, provenance, bias/confounding, exclusions/missingness, reagents:
- Statistical/computational validity — effect and uncertainty, n, multiplicity, assumptions, robustness, validation independence:
- Internal counter-evidence:
- Exact proposition established and not established:
- Relation: Direct / Indirect / Non-discriminating / Contradictory / Not assessable
- Material limitation:
- K#/source used:
- Verification flag:

[Repeat for consequential E→M links]

### Pass B — Individual Claim Validity (`M`)

#### M1.1

- Warrant and hidden premises:
- Integrated evidence from Pass A:
- Relevant definitions, expected patterns, support/conflict/controversy (K#):
- Strongest live alternative and whether it is distinguished:
- Internal exceptions, negative results, or heterogeneous subgroups:
- Missing field-standard evidence and relevant precedent, if discriminating (K#):
- Defensible scope and generalization limit:
- Verdict: Supported / Partially supported / Unsupported at the stated level / Not assessable
- Evidence that would change the verdict:
- K# disposition updated:
- Verification flag:

[Repeat for consequential M claims, in inference-chain order]

### Pass C — Claim-Network Validity (`M→H`, `H↔H`)

#### H1

- Necessary M claims and bridge status:
- Inferential leaps, if any:
- Acting component and direct mediator in composite stimuli or exposures, if applicable:
- Necessary vs sufficient; temporal and causal direction:
- Contradictions, circularity, or double counting:
- Strongest evidence:
- Weakest necessary claim or bridge:
- Defensible headline conclusion:
- Remaining overclaim:
- Literature position and novelty:
- Disease/phenotype link (shown or assumed):
- External replication (present? needed at this venue? basis):
- Cross-cohort/batch/platform/site/model comparability (if applicable):
- Observations the authors' explanatory model does not explain (manuscript or K#), with the alternative:
- H-level status at the stated level:

[Repeat for H claims and record consequential H↔H relationships]

## S2c — Coverage Audit

### Structural Coverage

| Coverage target | Complete / Not assessable / Missing | Missing item or disposition |
| --- | --- | --- |
| Consequential E→M links have Pass A relations | | |
| Consequential M claims have Pass B verdicts | | |
| Necessary M→H and consequential H↔H links have Pass C judgments | | |
| Relevant K rows are Used or Set aside with reasons | | |
| Counter-evidence, negative results, unexplained observations, and uncertainty remain visible | | |
| Issue candidates are Retained / Set aside / Pending with reasons and traceability | | |

### Conditional Modules Used

| Module | Why applicable | Omission or bias signal | S2b pass reopened and result |
| --- | --- | --- | --- |
| | | | |

### Issue-Candidate Disposition

| Candidate | Origin and affected H/M/E/K | Retained / Set aside / Pending | Reason |
| --- | --- | --- | --- |
| | | | |

## S3 — Issue and Action Ledger

### I1 — [Validity-critical / Venue-critical / Recommended strengthening / Minor]

- Affects: H# / M# / E#
- Origin: S2b Pass A / S2b Pass B / S2b Pass C / S2c conditional module / Minor sweep
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
