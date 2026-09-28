# Final Pruning

Use this reference only after S4 has produced a complete, source-verified author-facing draft. This pass edits prioritization and presentation; it does not repeat the scientific appraisal.

## Inputs

- the append-only candidate register and S3 issue ledger, including classification, consequence, evidence-request role, and fallback;
- the verified S4 draft;
- the journal's required fields;
- the voice and length guidance in [style-profile.md](style-profile.md).

For a new session, read the saved review dossier and draft first. Re-open the manuscript only when pruning could change a factual statement, scientific judgment, evidence bar, or recommendation premise.

## Action audit

Inventory every requested author action in the draft and assign one disposition internally:

- **Minimum required:** needed for the stated claim to be valid or for the present claim package to meet the venue bar;
- **Recommended:** materially strengthens the work but is not necessary for validity or venue fit;
- **Claim-calibration fallback:** narrows the claim and limitations enough to resolve the issue while preserving a defensible, venue-appropriate contribution;
- **Remove:** duplicated, non-discriminating, merely interesting, or unsupported by the ledger.

A minimum evidentiary route may contain multiple inseparable components. Do not preserve extra analyses merely to make a comment appear comprehensive. When supporting characterization is needed only to interpret a chosen decisive test, state that dependency rather than presenting it as an independent requirement.

## Coverage preservation

Before pruning, compare the draft with both the candidate register and the S3 issue ledger. Every Validated or Weakened candidate must have an S3 disposition, and every Validity-critical or Venue-critical I# must appear in the draft or carry a recorded drop reason in the dossier.

Give explicit keep, move, or drop decisions, with a one-line reason, for any ledger issue in these commonly decisive classes. The first three are judged in S2 (workflow.md, High-level roll-up); a drop that contradicts the S2 judgment must say why the S2 judgment was wrong:

- external replication or independent validation of the headline result;
- novelty or added value relative to the closest prior datasets, resources, or studies;
- comparability across cohorts, batches, platforms, or sites, including covariate harmonization;
- data, code, or summary-statistic availability needed to verify the central claims.

Do not drop an issue in these classes to meet a length or comment-count preference; merge it only with a comment that shares the same underlying scientific defect, consequence, and remedy.

Pruning may merge duplicate Minor Comments and remove low-value ones (typography, stylistic preference), but it must not remove a high-value Minor Comment from the Minor sweep (see workflow.md, S3) unless it is duplicated elsewhere in the report. Write each Minor Comment as one line: location, problem, requested correction.

## Prune the draft

For each Major Comment:

1. retain one central claim-level defect and its consequence;
2. retain the minimum evidentiary route that resolves that consequence;
3. include a claim-calibration fallback only when it remains scientifically and editorially defensible;
4. move Recommended actions to a separate section when the journal permits; otherwise label them clearly as non-essential or omit them;
5. remove duplicated requests from other comments.

Treat two routes as alternatives only when both resolve the same inference. Evidence of presence, association, plausibility, or additional characterization does not substitute for a causal, functional, predictive, or generalization test when that is the unresolved inference.

Then compress the surrounding prose:

- keep only the manuscript-specific fact and literature proposition needed to justify the judgment;
- remove repeated background already stated in the Overall Assessment or another comment;
- preserve one or two discriminating examples when they materially clarify an adequate response;
- keep the report no longer than needed after all independent critical issues are preserved; there is no target number of Major Comments.

After compression, re-check every quotation, claim verb, count, and scope statement that was shortened or merged against the source; compression must not broaden, narrow, or reattribute what the manuscript says.

Prune only the reviewer-facing report. Preserve the dossier's claim map, field knowledge, resolved issues, and verification record, then update its final action dispositions and recommendation rationale.

## Return rule

If this pass reveals an untraced scientific issue, an invalid alternative, or a changed recommendation premise, return to the earliest affected stage, update the ledger, and redraft. Do not resolve a scientific disagreement by wording alone.

## Delivery gate

Deliver only when:

- every Validity-critical or Venue-critical ledger issue appears in the report or has a recorded drop reason;
- every high-value Minor sweep finding appears as a Minor Comment or is recorded as duplicated;
- every author action has a disposition;
- every Major Comment contains a central defect, consequence, and minimum required route;
- Recommended strengthening is separated or omitted;
- every stated alternative resolves the same inference as the direct route;
- duplicated requests and non-essential background are removed;
- the final recommendation still follows from the surviving issues and their remedy profile (see review-framework.md, section 7);
- the dossier's final action dispositions and recommendation rationale are updated;
- the final report is concise relative to the surviving issues and does not omit an independent critical issue for presentation reasons.
