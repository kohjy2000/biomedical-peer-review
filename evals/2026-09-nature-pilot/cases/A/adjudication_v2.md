# Case A adjudication (v2 skill): AI review vs round-1 referees

Sources: `ai_review_v2/peer-review.md` (report only), `reference/human_points.md`, the preprint text, XML and figures, and the published text (`../../pub.txt`). The rules match `adjudication.md`. M = Matched, P = Partial, X = Missed.

## 1. Coverage

**Major (n = 15)**
- **M (5):** R1-3, R3-1, R3-7, R3-8, R5-1 (formal enrichment test now requested).
- **P (8):**
  - R1-1: dosage readout; the mRNA≠protein point is missing.
  - R1-2: power and batch; no sparsity or allele-of-origin point.
  - R3-2 (X→P): novelty narrowed to the quantitative comparison; the prior bulk finding of TSS-distal eQTLs is not cited.
  - R3-3: Yazar named; no gut-vs-blood count requested.
  - R3-4 (M→P): the "OTG-only benchmark" critique stayed in the dossier; the report only asks for the OTG version.
  - R3-6: asks which statistic entered coloc, not whether it is valid.
  - R3-9 (weak): opposite MAML2 directions are read as incoherent mechanism, not as LD sign flips.
  - R3-11 (M→P): IL23R error and speculative side effects raised; the eQTL-direction check is missing.
- **X (2):** R3-10 (OTG evidence mix); R5-2 (replication dropped, §5).

**Major recall = (5 + 4)/15 = 0.60.** On referee "major" labels (n = 17: 4 M, 11 P, 2 X): 0.56.

**Minor (n = 35)**
- **M (6):**
  - R1-9: "annotation with the largest estimated effect".
  - R1-11, R1-13, R3-13, R5-9.
  - R5-5: multiple testing across 252 annotations.
- **P (6):** R1-5, R1-6, R3-5, R3-20, R5-3, R5-4.
- **X (23):**
  - R1-4, 7, 8, 10, 12, 14–17.
  - R3-12, 14–19, 21, 22.
  - R5-6–8, 10, 11.

**Minor recall = (6 + 3)/35 = 0.26.**

## 2. AI-only issues (44)

**Valid (37).** "Pub" gives the status in the published version.
- **Carried from v1:**
  - Power/test-count null; bootstrap t-tests.
  - S7 compares only colocalising genes.
  - Max-r² bias toward small n.
  - Nominated annotation ≠ colocalising annotation (MAML2, ZMIZ1, PSEN2).
  - MYC direction; RNF14 sparsity.
  - Liu vs de Lange; sub-genome-wide MAML2/PSEN2.
  - GSI toxicity.
  - Six count mismatches; Fig. 4b; Fig. 5b.
  - RPS14; "protective role".
- **New, Majors 2–5:**
  - Negative-control traits.
  - Disease–site coupling (blood CD only, rectum non-IBD).
  - Atypical B cells are the top single cell type (10 loci), undiscussed.
  - MAML2 direction differs between VSM and DCs.
  - ZMIZ1 as a T-cell Notch1 cofactor (Pinnell). Pub rewrote ZMIZ1 and cites Pinnell.
  - Notch2 in cDC2; mo-DC composition.
  - ieQTL cell-state composition and permutation calibration.
- **New, Recommended and Minor:**
  - PRKCB IBD-trial claim uncited (pub dropped it at first mention).
  - Fig. 6 contains ribosomal and troponin targets (RPL4, RPS9, TNNI2, TNNT3).
  - Summary statistics for reviewers.
  - Legend errors ("villu", "detectermined", "wicoxon", Timshel 2022 vs 2020).
  - GSEA method and "coefficient" undefined.
  - CellTypist rescue counts.
  - "Healthy" → "non-IBD".
  - MAML binds NICD–RBPJ (pub removed the sentence).
  - OTG version.

| Debatable (6) | Justification |
|---|---|
| RASGRP1 listed as "mixed direction" | True fact, but the dossier had judged it *compatible* (RASGRP1 restricts growth). Compression flipped the reading. |
| Chemistry/genotyping-batch covariates | Genotypes jointly called across batches; expression PCs are selected per annotation. |
| Evolutionary model | Already hedged. Pub: unchanged. |
| JAK2/tofacitinib | As in v1. Pub keeps JAK2. |
| Cite "4.9 million" | Summary-paragraph claim. Pub: unchanged. |
| Qualify "largest atlas" | 2.2M cells exceeds the reviewer's own comparator (Oliver, about 1.1M). |

| Incorrect (1) | Justification |
|---|---|
| Minor 8: "please add … the eQTL model equations" | Present in the Methods ("an expanded model was used:"; XML disp-formula 1–2). Only the images were unavailable. |

## 3. Factual accuracy audit

**Verified:**
- Cohort and annotations: 397 donors, about 2.2M cells, 217/30/4 and 252/384.
- Statistics: "p<2.2e-16 for all comparisons" is verbatim; bootstrap t-tests are confirmed in the Methods; OR 2.68/1.57/0.75; eight MAML2 eQTLs.
- ieQTL and eGene counts: 1,051, 5 variables and 44 (4.2%); 1,945 cross-site eGenes.
- Figure reads:
  - Fig. 3e (atypical B = 10).
  - ZMIZ1 rectal cDC2 at about 23%.
  - MAML2 cDC1 cross-site top r², with about 5 homozygous donors.
  - Fig. 4b axis label.
  - PSEN2 outlined colonocyte points increase.
  - MYC S10b.
  - Fig. 6 targets.
- Text: all quotes; the drug-level Methods filter; arithmetic; typos.

**Literature:** all real and apt:
- Mostafavi 2023; Liu 2023; de Lange 2017.
- Kim-Hellmuth 2020 (>50% more colocalisations).
- Yazar 2022.
- Wallace 2020 and 2021.
- Urbut 2019.
- Pinnell 2015 (no role in intestinal homeostasis or myeloid suppression).
- Lewis 2011.
- Satpathy 2013 (Nat Immunol 14:937).

**Errors: 1** (the equations).

**Not counted:**
- RASGRP1 framing.
- Fig. 2f CI overlap: clear for FANTOM, marginal for ENCODE.

**The four v1 errors do not recur:**
- "Protective role": no location given.
- Fig. 3e is read correctly.
- PRKCB: no claim that "approved for oncology" is wrong, and the filter is paraphrased correctly.
- No claim that the PPH4 threshold is given only for ieQTLs.

## 4. Calibration

**Recommendation:**
- **AI:** Major Revision.
- **Outcome:** three rounds, then Nature, with text softening plus replication, GO and Cuomo analyses. No experiments.
- **Match:** Yes.

**Over-weighting:** the confidential note still makes Nature suitability depend on the resolution null plus either functional support or editorial acceptance. Neither the null nor functional support was provided, and the paper was accepted. Venue risk remains overstated.

**Under-weighting:** replication (it became Fig. 2e) and presentation.

**Blinding:** exposure to the published title was again disclosed; the page was not opened.

## 5. Skill-change checks

**(i) Coverage guard.**
- I1–I5 all appear as Majors 1–5.
- S5 records explicit decisions:
  - Novelty: kept, but thinned (R3-4 M→P).
  - Comparability and data access: kept.
  - **Replication: dropped.** Reason given: the within-data null "resolves validity".
- The drop is procedurally compliant but substantively wrong, since all three referees asked for replication.
- The dossier says replication is "noted implicitly in the confidential comment". It is not there.
- Replication never became an S3 ledger issue, so the guard could act only at S5.

**(ii) Remedy profile.**
- Yes: Majors 1–3 and 5 need reanalysis, and Major 4 needs functional evidence or recalibration, so the recommendation is Major Revision.
- Partial on "what the field accepts": the Nature criterion was not verified (run-notes).

**(iii) "Absent" assertions.**
- Search locations are logged. 1 of about 8 absence claims is wrong: the equations. The run-notes knew they were images, but the report says "please add" rather than "not found in the available material".
- Correct absence claims: ieQTL significance (also R5-5), GSEA Methods, Fig. 3b CI, coloc–SuSiE, negative controls.

**(iv) Minor recall: 0.21 → 0.26.**
- Gains: R1-9, R5-5 and R1-5. Loss: R1-17.
- The checklist was logged but shallow:
  - None of the referees' 8 legibility points were caught, including the overlapping Fig. 6 labels.
  - Code was recorded as "on GitHub" without testing the link (R3-22 and R5-11 missed).
  - "Regulate" and "colocalised" were missed.

## 6. Delta v1 → v2

| Metric | v1 | v2 | Δ |
|---|---|---|---|
| Major recall (n = 15) | 0.63 | 0.60 | −0.03 |
| Minor recall (n = 35) | 0.21 | 0.26 | +0.04 |
| AI-only V / D / I | 22 / 4 / 2 | 37 / 6 / 1 | +15 / +2 / −1 |
| Factual errors | 4 | 1 | −3 |
| Report length (words) | 1,747 | 2,236 | +489 (+28%) |
| Recommendation | Major rev. ✓ | Major rev. ✓ | = (now remedy-derived) |

**Metrics (v2):** Major recall 0.60; Minor recall 0.26; AI-only 37 Valid / 6 Debatable / 1 Incorrect; factual errors 1; recommendation match: Yes.
