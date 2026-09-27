# Case study: blind AI peer review vs. real Nature referee reports (pilot, n = 3)

Skill: [biomedical-peer-review](https://github.com/kohjy2000/biomedical-peer-review) @ `fccb466` · Reviewer model: Claude Opus (high effort) · Date: 2026-09-26 · Status: pilot, not yet externally audited

## Question

Given only the manuscript as submitted, how much of what expert referees raised does the skill recover, what does it find that referees did not, and how often is it wrong?

## Design

- **Papers.** Three 2026 Nature papers with a published Peer Review File, CC BY licence, and a preprint posted within 0–5 days of the journal's "Received" date (so the preprint approximates the submitted manuscript):
  - **A** single-cell eQTL and IBD risk (human genetics; medRxiv v1, CC BY)
  - **B** host genetic control of persistent EBV in biobank genomes (infection immunology / population genetics; medRxiv v1, CC BY-NC-ND)
  - **C** intratumoural anti-CTLA-4 plus IV anti-PD-1, phase 1b (tumour immunology, clinical trial; Research Square v1)
- **Blind review.** One agent per paper followed the skill (S0–S5) on the preprint v1 only (text + figure images), reviewing "as of" the submission date for Nature. Reviews, later versions and the published article were off-limits.
- **Reference ledger.** A separate agent extracted every round-1 referee point from the Peer Review File, with our Major/Minor category and the authors' response outcome.
- **Adjudication.** A third agent per paper compared the AI report with the ledger, classified AI-only issues (Valid / Debatable / Incorrect, using the manuscript and whether the published paper changed), audited every number, quote, figure reference and citation in the AI report, and assessed recommendation calibration.
- **Fixed rules.** Round-1 points only; primary metric uses our Major/Minor category (referee labels also recorded); a point answered only in the rebuttal letter still counts as substantive. Recall = (Matched + 0.5 × Partial) / total.

## Results

| | A | B | C | Pooled |
|---|---|---|---|---|
| Round-1 referees (substantive) | 3 | 4 | 3 | 10 |
| Referee Major points recalled | 0.63 (of 15) | 0.62 (of 13) | 1.00 (of 2) | **0.65 (of 30)** |
| Referee Minor points recalled | 0.21 (of 35) | 0.19 (of 26) | 0.38 (of 32) | **0.26 (of 93)** |
| AI-only issues: Valid / Debatable / Incorrect | 22 / 4 / 2 | 12 / 4 / 1 | 14 / 3 / 1 | **48 / 11 / 4** |
| Factual errors in the AI report | 4 | 3 | 1 | **8** |
| Cited references that do not exist or misstate the source | 0 | 0 | 0 | **0** |
| Recommendation vs. outcome | Major rev. ✓ | Major rev. ✓ | Reject for Nature ✗ (accepted) | 2 / 3 |

AI-only "Valid" issues later changed in the published paper included locus-count and cohort-size mismatches (A, B), rewritten narratives that over-reached (A), deposition of summary statistics (B), and several internal percentage/threshold inconsistencies in the trial report (C) that no referee named.

## What the skill did well

1. **Recovered most validity-level concerns.** It found the issue all four B referees raised (whether single-read positives are real and whether read counts measure viral load) and matched a referee's MHC-instrument critique of the Mendelian randomisation exactly; in C it recovered both Major referee points.
2. **Internal-consistency auditing.** Arithmetic, denominators and cross-section contradictions were its most distinctive contribution; several were silently fixed before publication.
3. **Design-level critiques referees did not raise.** For example, in A the resolution comparison confounds annotation size with statistical power, and the max-variance cell-type assignment favours cell types with few donors.
4. **No fabricated citations.** Every cited source existed and said what was claimed.

## Failure modes

1. **Loss at the compression step.** Issues present in the dossier were dropped or distorted when the reviewer-facing report was written — external replication against GTEx/Yazar in A (raised by all three referees), and an over-generalised quotation in B.
2. **Severity over-weighting.** In each paper the AI treated one issue as decisive for the venue that editors did not: power confounding (A), MR (B), and, in C, a reject-for-venue recommendation although the AI's own remedy set (recalibration and reporting fixes on existing data) implied major revision.
3. **Minor/presentation requests largely missed** (recall 0.26): figure legibility, terminology, code links, literature placement, clinical context.
4. **Misreadings** (8 factual errors in total): a figure panel read at the wrong level (A), a requested covariate that was already in the model (B), items declared "missing" that were present (C), and one drug-approval claim (A).

## Suggested changes to the skill

- **S5 guard:** before pruning, list every dossier issue that concerns replication/external validation, novelty against prior resources, cross-cohort comparability, or data/code availability, and require an explicit keep/drop reason.
- **Recommendation from remedies:** classify each Major comment as fixable by reanalysis, by wording, or only by new data, and derive the recommendation from that profile.
- **"Absent" check:** before asserting that an analysis, item or covariate is missing, search the full text, Methods and legends and record where it was checked.
- **Referee-common checklist** for Minor comments (figure legibility, terminology precision, code/data links, literature placement).

## Iteration: skill v2 (four changes applied, re-run on A and B)

The four suggested changes were implemented on a local branch and the blind reviews of A and B were re-run with the same inputs, blinding rules (plus publisher domains excluded from search) and adjudication rules. Paper C could not be re-run: the reviewer run was stopped by a platform safety filter three times while processing the clinical-trial manuscript, so C is excluded from this comparison.

| | A v1 → v2 | B v1 → v2 |
|---|---|---|
| Referee Major recall | 0.63 → 0.60 | 0.62 → 0.58 |
| Referee Minor recall | 0.21 → 0.26 | 0.19 → 0.12 |
| AI-only Valid / Debatable / Incorrect | 22/4/2 → 37/6/1 | 12/4/1 → 20/3/0 |
| Factual errors in report | 4 → 1 | 3 → 0 |
| Report length (words) | 1,747 → 2,236 | 1,661 → 1,249 |
| Recommendation | Major rev. → Major rev. (now derived from remedy profile) | Major rev. → Major rev. (MR no longer treated as venue-decisive) |

What changed:

- **Accuracy improved in both papers** (7 → 1 factual errors in total; incorrect AI-only issues 3 → 1). No v1 error recurred; the v1 misreading in B (requesting a covariate already in the model) was replaced by a new, valid B-cell-fraction confounding issue that no referee raised.
- **Silent drops became explicit decisions.** The pruning guard produced auditable keep/drop records. In A, novelty against prior single-cell resources now appears as a Major comment, but external replication was deliberately dropped with a stated reason — a documented disagreement with all three referees rather than an accidental loss.
- **Recommendations are now justified by the remedy profile**, and in B the decisive requirement (qPCR benchmarking) matches what the authors actually delivered.
- **Recall did not improve** and stayed within what single-run variation could explain. In B the latent-versus-lytic infection issue (two referees; led to a title change) was not identified in v2 at all, which points to run-to-run variance rather than pruning.
- **The Minor checklist was applied shallowly:** figure-legibility points, code-link checks and wording issues were still largely missed, and classes such as requested biological extensions or interaction analyses are not on the list.
- **Residual compression drift:** one example of an effect-direction statement contradicted the reviewer's own dossier, which the new post-compression re-check did not catch.

Next changes suggested by v2: track replication/external validation as an explicit S2 appraisal item rather than only at pruning; apply the Minor checklist per figure; extend the post-compression re-check to direction and consistency statements; and run each paper at least three times to separate skill effects from run-to-run variance.

## Limitations

- **Training-data exposure.** The reviewer model's knowledge cutoff (June 2026) is later than all three publication dates (Feb–Jun 2026), so memorisation of the published papers or reviews cannot be excluded. The many departures from the actual revision path argue against wholesale leakage, but a replication on papers published after the cutoff is required.
- **Search exposure.** In A and B, search-result snippets surfaced the published title or a revised figure (pages not opened); in C the preprint PDF carried a banner naming the version of record. Adjudicators rated influence low to low–moderate.
- **Same-family adjudication.** The ledger, the Valid/Incorrect calls and the audit were produced by the same model family; an expert audit of a sample of calls is pending.
- **Incomplete inputs.** Supplementary files for A and B could not be retrieved; affected judgments were marked Not assessable.
- **Single runs.** Each review was run once per skill version, so v1–v2 differences below about ±0.05 in recall are within plausible run-to-run variation.
- **Platform filter.** The clinical-trial manuscript (C) repeatedly triggered a safety filter during the v2 re-run and during one adjudication attempt.
- **Small n and selection.** Three papers, all accepted at Nature; a referee ledger reflects only what referees chose to write.
- **Recall is not the only goal.** Referees also miss things; the Valid AI-only issues are evidence of complementary value, not proof of superiority.

## Next steps

1. Replicate on 3–5 papers published after the model cutoff (with Peer Review Files), with publisher domains excluded from search by default.
2. Expert audit of a random sample of AI-only issues and adjudication calls.
3. Implement the four skill changes above and re-run the same three papers to measure the effect on the compression loss and calibration.
