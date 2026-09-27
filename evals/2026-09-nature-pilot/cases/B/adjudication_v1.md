# Case B adjudication: AI review vs round-1 Nature referees

Checked: AI outputs, ledger (13 Major / 26 Minor re-counted), PRF, preprint text/XML/8 figures, published article (Nature 653:444–454, 2026).

## 1. Coverage of human round-1 points

**Major (13).** Label = referee's own label.

| ID | Label | AI | Basis |
|---|---|---|---|
| R1-3 singletons misclassified (Fig 2b) | none | Partial | AI says Fig 2b can't validate load and singletons may be technical; does not propose re-defining/excluding the EBV=1 group |
| R1-4 UKB vs AoU covariate sets | none | **Missed** | Not raised |
| R2-1 orthogonal validation (qPCR); simulation inadequate | none | **Matched** | M1: same inference, same remedy (qPCR/ddPCR), same critique of the fitted simulation |
| R2-2 plate-exclusion threshold/contamination bias | none | Partial | AI uses the 51 excluded plates as evidence of technical detection; no challenge to the threshold or its bias |
| R2-3 per-gene coverage for singletons | none | Partial | AI asks for technical decomposition of singletons (index swapping), not coverage |
| R2-4 latent vs lytic (expression) | none | Partial | Recommended 2 questions "latent" through antibody pattern only; weaker |
| R3-1 single-read threshold; qPCR | major | **Matched** | M1 (61.9% single reads, qPCR request) |
| R3-3 ≥2 vs 1 comparison may reflect false positives | none | **Matched** | M1: both Fig 2b phenotypes come from the same read process, so they can't separate load from detection |
| R3-5 AoU HLA imputation quality | none | Partial | Minor 8 asks HLA*IMP:02 vs HLA-TAPAS concordance; minor weight |
| R5-1 latent vs primary/lytic handling | major | Partial | Recommended 2 only |
| R5-2 serology antigens are lytic; per-antibody analysis | major | Partial | Recommended 2 interprets the per-antibody pattern; framed as optional, not as a validity problem |
| R5-5 repeat 1 vs ≥2 downstream (contamination) | major | Partial | Same contamination concern; different remedy |
| R5-12 MR driven by MHC → pleiotropy | major | **Matched** | M2: identical inference, stronger remedies |

Major: 4 Matched, 8 Partial, 1 Missed → **recall = (4 + 4)/13 = 0.62**.

**Minor (26).**
- Matched (3): R5-3 (depth normalisation ≈ AI's depth dependence/down-sampling), R5-6 (stratify serology lytic vs latent ≈ Recommended 2), R5-13 (European-ancestry skew ≈ Recommended 1).
- Partial (4): R1-1 (UKB+AoU meta-analysis vs AI's trans-ancestry request), R3-7 (replication of the 54 alleles vs AI's multiplicity-adjusted replication), R3-8 (A*02:01/DRB1*04:04 GRS display vs AI's pleiotropy use of the same facts), R5-8 (credible-set confusion vs AI Minor 6).
- Missed (19): R1-2 (HLA×ERAP epistasis, which became a headline result), R2-5, R2-6, R2-7, R2-8, R2-9, R2-10, R2-11, R3-2, R3-4, R3-6, R3-9, R5-4, R5-7, R5-9, R5-10, R5-11, R5-14, R5-15.

Minor: **recall = (3 + 2)/26 = 0.19**.

The four-referee consensus theme (singletons / viral load) is AI Major 1; the latent-vs-lytic theme only reached Recommended. Misses are mostly presentation, novelty wording and biology extensions.

## 2. AI-only issues

| AI item | Verdict | Justification |
|---|---|---|
| M3 locus-specificity claim rests on non-significant correlations; HHV-7 trends positive | Valid | Text reports HHV-7 r = 0.37, P = 0.06, six concordant, two colocalising, yet concludes "specific"; memory-B GWAS n = 3,757, no MHC. Published version *strengthened* the claim (not adopted). |
| M3 remedy: sensitivity GWAS conditioned on blood-cell parameters | **Incorrect** | GWAS covariates already drawn from a blood-composition set; lymphocyte % selected (Results, Fig 1g; Methods). |
| M4a MAGMA∩RVAS overlap (24 genes) with no chance expectation | Valid | No overlap test; wording kept in published version. |
| M4b IEI subset "further increased" (0.35±0.22, P = 0.055) vs 0.19±0.04, not contrasted | Valid | Clear from text; published drops "further". |
| M5 summary statistics not deposited | Valid | True of preprint; published deposits GCST90809298–306 (bonus). Code half moot: referees had the repository. |
| M2 sub-point: binary exposure means the MR OR has no clean per-unit scale (Burgess & Labrecque) | Valid | Standard caveat, correctly sourced. |
| M1 sub-point: index swapping on patterned flow cells as a singleton source; down-sampling and lane-sharing bounds | Debatable | Plausible (Costello 2018); authors later addressed contamination via allele-frequency, coverage and qPCR instead. |
| m1 490,293 vs 490,294 | Valid | Published harmonises to 490,293. |
| m2 305,123 vs 47,234 + 257,899 = 305,133 | Valid | Arithmetic confirmed. |
| m3 serology n = 9,281 / 6,531 / 6,065 | Valid | 6,531 (ED 3a) vs 6,065 (Fig 4) is real; published now 6,063. |
| m4 184,948 vs 184,949 | Valid (trivial) | Confirmed in ED Fig 3c. |
| m4 21 vs 26 level-2 cell types | Debatable | 26 = dataset total; 21 may remain after filtering. |
| m5 IRF1 vs 5q31.1_SLC22A5 | Valid (trivial) | Confirmed; unchanged. |
| m6 "credible sets (PIP > 95%)" conflates cumulative coverage and per-variant PIP | Valid | Published rewrote passage. |
| m7 decimal comma; sign of IBD/hypothyroidism coefficients | Valid | Published fixes comma. |
| m9 "largely equal" class I/II contribution | Debatable | ΔR² ≈0.044 vs 0.031, but wording defensible; retained. |
| m10 red-hair negative control includes UKB | Debatable | Overlap biases toward false positive; none seen. |

Tally: **12 Valid, 4 Debatable, 1 Incorrect**; five Valid points changed in the published version. Copy-edit line correct ("EBVseron-egative" is in the source XML).

## 3. Factual accuracy audit (peer-review.md)

**Verified correct** against the preprint text or figures:
- Cohort sizes, 54 alleles, 51 plates, 61.9%, all quotations, ref 25/26 attributions, A*02:01 exclusion, ORwMed 1.86, Fig 2d/ED 2e correlations, TNFRSF13B, IEI estimates, ED 3c ancestry n's, ED 2 antibody correlations, and all Minor-comment numbers.

**Literature**: all items exist and support the stated use.
Costello 2018 (BMC Genomics 19:332), Burgess & Labrecque 2018 (EJE 33:947), Hammer 2015 (AJHG 97:738), Orrù 2020 (Nat Genet 52:1036, n = 3,757); Raychaudhuri 2012 and Moutsianas 2015 used as the manuscript cites them.

**Errors (3):**
1. **M4 misattributed scope.** The review says all 24 overlap genes are called "strong novel candidate genes". The preprint applies it only to the 7 loss-of-function-driven genes (dossier correct; error introduced in pruning).
2. **M3 misreading.** The requested blood-cell-conditioned GWAS overlooks the existing blood-composition covariates.
3. **Recommended 2 overgeneralises.** Claims correlation with "lytic-cycle antigens"; EA-D (lytic) shows none (r = 0.21, P = 0.19).

**Imprecisions (not counted):**
- Fig 1g yield range given as ≈0.10–0.45; the fitted curve runs about 0.12 to 0.40.
- Class II ΔR² given as 0.045–0.047; the figures show about 0.038–0.044.
- "27 points" for the memory-B comparison; ED 2e appears to plot fewer (uncertain).

## 4. Recommendation and severity calibration

- **Recommendation matches.** The AI recommended Major revision. All four referees were positive ("well executed", "meticulous", "novel and robust") and none asked for rejection, while all four demanded substantive work. The outcome was acceptance after two rounds with major new data: qPCR in two cohorts, RNA-seq, epistasis analysis, and a title change from "latent" to "persistent".
- **Over-weighted: MR.** The AI called the MHC-pleiotropy MR issue decisive for venue and said a null non-MHC MR would make this a specialist-journal paper. In reality only R5 raised it. The authors relabelled MR as exploratory, removed causality from the Abstract, and never put a non-MHC MR in the main text, and Nature still published.
- **Over-weighted: statistical-rigour points.** Specificity (M3), gene-overlap statistics (M4) and data deposition (M5) were Major in the AI review but absent from the human reviews. Only M5 clearly changed the paper.
- **Under-weighted: latent vs lytic.** This was Major for two referees and drove the title change, but the AI made it a Recommended revision.
- **Under-weighted: cross-cohort comparability.** R1-4 (covariates), R3-5 (HLA imputation) and R1-1 were missed or given minor weight.
- **Feasibility.** The AI avoided requiring qPCR; authors did it anyway.

## 5. Blinding integrity

- **Disclosed exposures.** The run notes honestly report two:
  1. A search result showing the published title ("Host control of **persistent** EBV infection | Nature") with a snippet (617,186 individuals; 39 loci; Hodgkin MR). Snippet numbers don't match this paper (probably the concurrent paper; uncertain).
  2. An independent bioRxiv preprint on the same phenotype, which was not opened.
- **Possible influence 1: title wording.** Recommended 2 asks to justify "latent" in the title, and the dossier suggests a neutral term. The real title changed latent → persistent. Seeing the published title could plausibly have prompted this. But the manuscript already says "persistent viral infections", and R2-4/R5-1 raise it independently. Risk: low to moderate.
- **Possible influence 2: trans-ancestry request.** Recommended 1 could echo the snippet's "cross-ancestry GWAS". Naturally motivated by ED 3c; the published paper ran no meta-analysis, so no hindsight advantage.
- **Undisclosed risk.** The model's knowledge cutoff (June 2026) is after publication (Feb 2026) and the PRF release. Training-data contamination can't be excluded, and the run notes don't mention it. Divergence from the real revision path (no epistasis request, qPCR not required, MR treated as decisive) argues against wholesale leakage.
- No numbers in the review trace to the snippet.

## 6. Verdict

1. **Strength:** it caught the central validity problem that all four referees raised (EBV reads as a viral-load proxy, with qPCR as the remedy) and matched R5's MR-pleiotropy point exactly, with sharper remedies.
2. **Strength:** its numerical cross-checking was precise and useful. Several real inconsistencies were found that the referees never flagged, and four of them were fixed in the published paper; it also correctly asked for summary-statistic deposition.
3. **Weakness:** biological interpretation is thin. Latent vs lytic got only Recommended weight, and HLA×ERAP epistasis, DRB1*15:01/MS, seasonality, IEI extensions, sex and novelty wording were all missed. Minor recall is 0.19.
4. **Weakness:** it over-weighted MR as a venue gate and was too cautious in requesting wet-lab validation, which the authors delivered anyway.
5. **Weakness:** three factual errors, including a misattributed quote introduced during pruning, plus a small but real risk that the published title leaked into one recommendation.

**Metrics:** Major recall 0.62 (4 Matched / 8 Partial / 1 Missed of 13); Minor recall 0.19 (3 / 4 / 19 of 26); AI-only 12 Valid / 4 Debatable / 1 Incorrect; factual errors 3 (plus 3 imprecisions); recommendation match: yes (Major revision vs positive-with-major-work referees; accepted after substantial revision).
