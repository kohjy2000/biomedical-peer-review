# Review Dossier

Confidential working record. Not for transmission to authors or editors.

## Status and Source Set

- Mode: Initial (blind evaluation, Nature, initial submission)
- Current stage: S5 complete
- Completed stages: S0, S1, S2, S3, S4, S5
- Manuscript version and date: medRxiv v1 (doi 10.1101/2025.06.24.25330216), posted 24 June 2025. Treated as a Nature initial submission.
- Source set reviewed: `blind/preprint_v1_text.md` (full text: abstract, introduction, results, methods, main and supplementary legends, references); `blind/preprint_v1.xml` (checked only for Table 1 and the equations); `blind/figures/F1–F20.jpg` (main Figs 1–6, Supplementary Figs S1–S14), all opened. Panels S10b, S11c/d and 5b were cropped and enlarged to read them.
- Sources intentionally excluded: any later version, the published article, peer-review files, author responses, news coverage.
- Not available: Table 1 (an image in the XML, not supplied); the eQTL model equations (images, not supplied; Fig. 1c gives the schematic `Expr ~ g + PC_GT + PC_Expr`); Supplementary Materials S1–S3 (data tables). Judgments that depend on these are marked Not assessable.
- Literature cutoff date: 2025-06-24
- Last verified: this session
- Next bounded action: none (delivered)
- Dossier confidentiality or storage note: local scratchpad only.

## S0 — Review Calibration

- Journal and submission stage: Nature, initial submission.
- Article/study type: large population-genomics resource (single-cell eQTL atlas) plus computational inference (resolution-dependent GWAS colocalisation) plus biological and therapeutic interpretation from statistical genetics alone. There are no functional experiments.
- Central question and intended contribution: does mapping eQTLs at cell-type resolution in disease-relevant tissue close the eQTL–GWAS "annotation gap"? The paper also nominates IBD effector genes and cell types.
- Design, data, population/model, and setting: scRNA-seq (10x 3′ v3.0/3.1) of terminal ileum (243 non-IBD, 119 CD), rectum (275 non-IBD) and blood (95 CD only), 421 donors, all from Addenbrooke's Hospital, Cambridge. 397 genotyped European-ancestry donors were used for eQTL mapping (~2.2M cells). Pseudobulk mean ln(cp10k+1), inverse normal transformed, TensorQTL cis mapping (MAF > 0.05, ±1 Mb), forward conditional signals, and LD clumping at r² > 0.5. ieQTL for age, sex, smoking, CD status and inflammation (TI-SES-CD). coloc.abf with default priors against de Lange 2017 GWAS summary statistics (CD/UC/IBD). Loci were assigned to the Liu 2023 list of known loci. Novelty was benchmarked against Open Targets Genetics colocalisations. Cell-type prioritisation used the maximum r² of the lead colocalising variant.
- Primary claim ambition and intended scope: general. "a framework for effector gene discovery in complex disease" and "a mechanistic map linking genetic risk to specific genes and cell types in IBD". It includes an evolutionary interpretation and therapeutic implications.
- Editor question, review fields, and recommendation options: none provided. Standard Nature fields assumed: Overall assessment, Major, Minor, Recommendation, Confidential comment.

### Relevant Review Requirements

| Requirement or expectation | Provenance | Basis or source | Consequence for this review |
| --- | --- | --- | --- |
| Nature requires a major conceptual advance of broad interest | Journal-stated (general editorial criteria; exact wording not re-verified this session) | Nature editorial criteria | The resolution-enrichment claim (H1) and the biological insights (H4) carry the venue case. The resource alone may not. |
| Colocalisation with multiple independent signals should relax the single-causal-variant assumption, e.g. coloc-SuSiE | Field standard | Wallace 2020 PLoS Genet; Wallace 2021 PLoS Genet (L3, L4) | Sensitivity analysis requested (I2) |
| Colocalisation posterior probability is not proof of a shared causal gene, and has known limitations | Field standard | Hukku et al. 2021 AJHG (L5) | Calibrate "effector gene" language (I4, minor) |
| Cross-condition effect-size comparison should model sharing and uncertainty rather than rely on detection thresholds | Field standard | Urbut et al. 2019 Nat Genet, mashr (L6) | I1 and I3 remedy |
| Mechanistic or pathway claims in an abstract at Nature level normally need perturbational support or at least a formal enrichment test | Reviewer calibration | Genre calibration in the framework | I4 is venue-critical |
| eQTL vs GWAS systematic differences are established. Distinguishing a real resolution effect from a detection or power artefact is the needed advance | Field standard / literature | Mostafavi et al. 2023 (L1) | Central bottleneck (I1, I2) |

- Claim-validity bar: for H1, the difference between resolutions must survive controls for number of annotations/tests, per-annotation power (donors, cells), effect size, MAF and expression level, with uncertainty correctly estimated. For H3/H4, the cell-type assignment must not be driven by sampling variance, and pathway statements must be framed as hypotheses unless tested.
- Venue-completeness bar (Nature): a rigorous, artefact-controlled demonstration of the resolution principle, plus either functional support for at least one nominated mechanism or evidence that the gene/cell-type nominations are robust and transferable. A scale-only resource would be below the bar.
- Feasibility constraints: none stated. The data exist, so most requests are reanalyses.
- Assumptions not made: no assumption that the authors hold additional UC tissue, functional assays or replication cohorts.
- Calibration uncertainty: whether a calibrated version (resource + robust H1, with the biology framed as hypotheses) meets Nature's threshold is an editorial judgment. It is recorded in the confidential comment.

## S1 — Structured Claim–Evidence Map

### H1 — "Cell-type-level eQTLs were more distal to transcription start sites, enriched in enhancers, less likely to regulate the nearest gene, and over two-fold more likely to colocalise with IBD GWAS loci than eQTLs detected at tissue-level resolution." (Abstract)
- Verb strength: declarative, generalising ("genetic architecture of complex diseases is shaped by regulatory effects active in restricted cellular contexts", Discussion).
- Scope: complex disease generally. Framed as testing a hypothesis stated in the Introduction.
- Claimed novelty: systematic quantification across resolutions in disease tissue.

#### M1.1 — Cell-type resolution reveals distinct eQTLs "masked in bulk analyses"
- E1.1a Fig. 2d, S4. Contrast: eQTLs grouped by the minimum resolution of detection. 84,376 eQTLs; 26,192 (31%) cell-type-only; 30,540 (36.2%) major-population-only. eQTLs per eGene are 3.1/2.7/1.9. Unit: LD-clumped lead variant (r² > 0.5). Supp Fig S4 shows n annotations = 217 (cell type), 30 (major), 4 (All cells).
- Inferential role: descriptive. The implied inference is that these are distinct regulatory effects.
- Internal limitation: detection-based classification, with 54× more annotations at cell-type resolution. Clumping of noisy lead variants from low-power annotations can create apparently "distinct" eQTLs.

#### M1.2 — Cell-type-only eQTLs are more TSS-distal, less often regulate the nearest gene, and are enhancer-enriched
- E1.2a Fig. 2e: median distance 44/108/200 kb; % < 10 kb = 22.6/11.6/6.5. Wilcoxon-type p < 2.2e-16.
- E1.2b Fig. S5: nearest gene is the eGene 38.3/28/20.1%.
- E1.2c Fig. 2f: enhancer vs promoter relative enrichment (FANTOM, ENCODE), bootstrapped over LD blocks. p from two-sided t-tests on bootstrap distributions. Visually the CIs for major population and cell type overlap in both annotations.
- Role: association.

#### M1.3 — Cell-type-level eGenes are more likely to be IBD effector genes (OR 2.68 / 1.57 / 0.75)
- E1.3a Fig. 3b: "ratio of odds between eGene detection and disease-effector gene nomination" by the lowest resolution at which the gene is detected. No CI or p-value is shown in the figure. The Methods do not define the calculation.
- E1.3b Fig. S7: CELLEX max specificity compared across resolutions among colocalising genes only (p = 0.46/0.82/0.38).
- Role: association framed as explanation ("increases power to detect the effector genes").
- Limitation: S7 does not compare colocalising with non-colocalising genes, so it cannot rule out confounding by specificity. The number of annotations tested per gene differs by resolution.

- Bridge: M1.1 → M1.2 → M1.3, then an evolutionary model (Discussion). The model is not tested.
- Missing bridge: that detection-at-minimum-resolution indexes biological cell-type specificity rather than power and effect size.

### H2 — "We nominate effector genes at over half of known IBD loci" (Abstract). 180/321 loci, 419 genes, 74 loci with no prior OTG colocalisation.
#### M2.1 — Colocalisation at 180 loci (PPH4 > 0.75)
- E2.1a Fig. 3a, Table 1 (image not available), Supp S2 (not available). Pie chart: 137 OTG-colocalised loci, 74 IBDverse-only, 110 remaining (sum 321). Text: 138 OTG loci, 104/138 = "75.6%", and 180 loci total. Note 104 + 74 = 178. Fig. 3c bars sum to about 178.
- Method: coloc.abf default priors, 2 Mb windows, GWAS p < 5e-5 suggestive, de Lange 2017 summary statistics, assignment to Liu 2023 loci within 500 kb, HLA excluded.
#### M2.2 — ieQTL: 1,051 ieQTLs / 977 ieGenes; 764 inflammation-modulated, 501 in enterocytes; 2 loci colocalise only with ieQTLs
- E2.2a Supp S6; Fig. 5d (RNF14). The ieQTL significance criterion is not described in the Methods (searched "FDR", "significan", "multiple testing", "Bonferroni": none for ieQTL). Only 44/1,051 are in LD (r² > 0.5) with eQTLs. GSEA methods are not given.
- Fig. 5d: moderate/severe inflammation n ≈ 3/5/1 per genotype class. The y-axis is raw pseudobulk expression.

### H3 — Effector cell types: myeloid most frequent (47 loci, 26.4%), then T/ILC (34, 19.1%) and colonocytes (32, 18%). Dendritic cells are "three of the four" top myeloid types (18 loci)
- E3.1a Fig. 3c–e. Method: for each colocalisation, the annotation with maximum r² of the lead variant (linear regression of INT pseudobulk on genotype), among annotations with a nominal eQTL p < 0.05 (Supp S9–S11 legends). Stated purpose: to "mitigate power-related biases".
- Fig. 3e: Atypical B cells = 10 loci (the highest single cell type, not discussed). cDC2 = 8, cDC1 = 5, pDC = 5.
- Supp Fig. S2: blood-derived myeloid and atypical B cells come essentially only from CD donors. Colonocytes are essentially all non-IBD (rectum).

### H4 — Biology: "implicating reduced Notch signalling in intestinal immune dysfunction" (MAML2, PSEN2, ZMIZ1 "in myeloid cells"); "Wnt regulated genes, including MYC, in epithelial stem and progenitor cells, suggesting that impaired renewal contributes to barrier breakdown"; "a mechanistic map" (Abstract)
- E4.1 MAML2 (Fig. 4, S8). The text reports colocalisation with UC in TI cDC2 (PPH4 = 0.98). Fig. 4b's eQTL track axis is labelled "Macrophages CD163++". Fig. 4c: three outlined (colocalising) myeloid annotations at about 3–4% r², plus cDC2 TI at about 12%. The top r² is cDC1 cross-site (about 17%, with about 5 homozygous-risk donors). The risk allele decreases MAML2 in DCs but increases it in vascular smooth muscle (TI). There are 8 independent MAML2 eQTLs, and the colocalising one has r² ≤ 0.3 with the others. Spearman eQTL strength vs expression R = −0.29, p = 0.21. The text says "support the conclusion that dysregulation of MAML2 ... in cDCs contributes to UC risk".
- E4.2 ZMIZ1 (S9): PPH4 = 0.99 (CD). The eQTL track is labelled a T-cell annotation (CD4+ memory CXCR6+). The top-r² annotations are cDC2 cross-site, T TI and cDC2 rectum (23%, about 35 donors).
- E4.3 PSEN2 (S11c/d): PPH4 = 0.91 (UC). The eQTL track is labelled a colonocyte annotation. The outlined (colocalising) annotations are colonocyte, with the risk allele increasing PSEN2 at 1–3% r². Classical monocytes (blood) show a decrease that is not outlined. All r² are < 5%. The GWAS UC peak is about −log10 P 6 in the summary statistics used.
- E4.4 MYC (Fig. 5b, S10b): PPH4 = 0.92 (CD). The eQTL is detected in a single stem-cell annotation. Lead variant chr8:128,528,218. The plotted window (about 128.0–129.0 Mb) does not display MYC. The top-r² annotations are CCL3/CCL4 CXCL9/10 macrophages (TI, decrease), PlasmaB CD38++++ (blood, increase) and EC venous (rectum, decrease). The stem-cell point (outlined) sits at about 1% r², increase. The text states "an eQTL regulating increased MYC expression colocalised with CD risk".
- E4.5 RASGRP1 (Fig. 5a, S10a): risk allele increases expression. The top annotations include memory/atypical B cells and rectal colonocytes. The manuscript's own reference 40 (Depeille 2015) describes RasGRP1 as restricting epithelial growth.
- E4.6 RNF14 ieQTL (Fig. 5c,d), FUBP1 (S10c,d; divergent directions), LPIN3 (no figure), FERMT1 (replication).
- Logical assembly: colocalisation plus literature on gene function leads to pathway-level mechanism. No enrichment test, no perturbation, no allelic assay.

### H5 — Therapeutic: target overlap, repurposing via ChEMBL (Fig. 6), safety (NDUFAF1–metformin, PSEN2–γ-secretase inhibitors)
- The text states "ITGA4, JAK2 and IL23R, which are the direct molecular targets of vedolizumab and tofacitinib, respectively". PRKCB: "already undergoing early-phase clinical trials for IBD" (stated twice). The Methods filter Fig. 6 to drugs "not yet been trialed as IBD treatments".

## S2 — Claim Appraisal

### M1.1
- Verdict: Partially supported. Relation: Non-discriminating.
- Fit: the comparison varies the number of annotations (217 vs 30 vs 4), donors/cells per test and lead-variant precision together with resolution. "Distinct" is defined by failure to clump at r² > 0.5, which is sensitive to lead-SNP noise in low-power tests.
- Strongest evidence: large absolute numbers, and the patterns are consistent across metrics.
- Limitation: no null model with matched test number and power; no multiple-testing control across 252 annotations.
- Competing explanation: winner's-curse and lead-SNP imprecision in small annotations inflate "new" eQTLs.
- Evidence that would change the verdict: a random-grouping (pseudo-cell-type) null, or subsampling to equalise donors and annotation count; mashr-type sharing estimates.

### M1.2
- Verdict: Partially supported. Relation: Non-discriminating.
- Fit: eQTLs only detectable in fine annotations are, on average, smaller-effect and lower-power in bulk. TSS-distal and weaker eQTLs are correlated generally (L1 shows eQTL discovery concentrated near TSS). So distance and enhancer shifts may track detectability rather than cell-type restriction.
- Statistical flaw: t-tests on 1,000 bootstrap replicates produce arbitrarily small p-values (replicates are not independent observations). In Fig. 2f the cell-type vs major-population CIs overlap in both panels, yet "p<2.2e-16 for all comparisons" is stated.
- Needed: stratify or match by effect size, MAF, expression and annotation sample size; use a bootstrap CI of the difference.

### M1.3
- Verdict: Unsupported at the stated level (as a quantitative, causal "increases power" claim). Relation: Indirect.
- Limitation: OR undefined, with no uncertainty. Genes detected only at cell-type level are tested for colocalisation across many annotations. coloc.abf's single-causal-variant assumption is violated where genes have multiple independent eQTLs (e.g. MAML2 has 8). No negative-control trait. S7 compares only effector genes, so it does not test the confounder.
- Literature: Kim-Hellmuth 2020 (L7) reported >50% more colocalisations from cell-type-interaction QTLs in GTEx. Yazar 2022 (L8) reported largely cell-type-specific eQTLs in 14 blood cell types. Mostafavi 2023 (L1) established systematic eQTL–GWAS differences and a selection-based model. Yao 2020 (L9) estimated about 11% of heritability mediated by assayed bulk expression. The manuscript therefore extends and quantifies a direction already expected. Its genuine contribution is disease-tissue scale and a direct cross-resolution comparison. That contribution only holds if the comparison is artefact-controlled.
- Position: extends / confirms. It does not discriminate the selection model from a power model.
- Field-standard package: a heritability- or enrichment-based comparison controlling for LD, MAF and annotation size (e.g. S-LDSC or MESC-type), or colocalisation rates normalised per test with negative-control traits. Reviewer calibration: the specific design choice is left to the authors.

### M2.1
- Verdict: Partially supported. The nominations are plausible, but numbers are inconsistent (180 vs 178; 137 vs 138; 75.6% vs 75.4%/75.9%). Robustness to coloc priors and to multiple causal variants has not been tested (L3, L4). The GWAS used is de Lange 2017 (59,957 subjects, European; L10), while the loci come from Liu 2023 (320 loci incl. East Asian meta-analysis; L2). The intro says 320 and the results say 321. Several highlighted signals are sub-genome-wide in the GWAS used (MAML2 and PSEN2 UC peaks about −log10 P 6, read from Fig. 4b/S11c).
- "No effector gene had previously been nominated" is judged only against OTG colocalisation. Not assessable in detail without Supp S2 and Table 1.

### M2.2
- Verdict: Not assessable / Partially supported. The significance definition and multiple-testing handling are absent. Inflammation is available only in the TI of CD patients. Within-major-population composition shifts (e.g. enterocyte states in inflamed tissue) can create apparent genotype × inflammation effects. Fig. 5d rests on very few inflamed samples. The low LD overlap with eQTLs (4.2%) is compatible with either biology or false positives.

### H3 (M3.1 effector cell type)
- Verdict: Unsupported at the stated level. Relation: Non-discriminating.
- Reason: with a nominal p < 0.05 filter, the minimum qualifying r² scales as roughly 4/n, and the null expectation of r² is about 1/(n−1). Maximising r² across up to about 250 annotations therefore preferentially selects small-n annotations. That is the opposite of the stated aim of mitigating power bias. This is consistent with rare annotations dominating: atypical B cells 10, cDC1 5, pDC 5, and cDC2 rectum 23% for ZMIZ1 with about 35 donors. The colocalising annotation often differs from the top-r² annotation: MAML2 (macrophage eQTL track vs cDC narrative), ZMIZ1 (T-cell eQTL track vs cDC), PSEN2 (colonocyte colocalisation vs monocyte/endothelial narrative), MYC (stem-cell colocalisation vs top r² in macrophage/plasma/EC with opposite directions).
- Additional confound: CD-only blood and non-IBD-only rectum couple disease status with annotation (Supp S2).
- Evidence that would change the verdict: uncertainty-aware or shrunken effect estimates (L6), CIs on r², a requirement for colocalisation in the nominated annotation, and a sensitivity analysis restricted to annotations with matched n.

### H4 (M4.1 Notch in DCs; M4.2 Wnt/impaired renewal)
- Verdict: Unsupported at the stated level. Relation: Indirect (colocalisation plus literature), and partly Contradictory on direction.
- Notch: two DC loci (MAML2, ZMIZ1). PSEN2 is not myeloid-colocalised. There is no pathway enrichment test against a matched background. Pinnell 2015 (L11) shows Zmiz1 is a selective Notch1 cofactor with major roles in T cells and no major role in intestinal homeostasis or myeloid suppression. That undercuts the claim that ZMIZ1 reports DC Notch activity, and the ZMIZ1 colocalising track is a T-cell annotation. Notch2 signalling drives intestinal CD11b+ cDC2 differentiation and IL-23/Th17 support (Lewis 2011, L12; Satpathy 2013, L13). So reduced Notch in DCs has no established direction of effect on inflammation. A cis-eQTL in a "cDC2" pseudobulk could also reflect subset composition, which the authors acknowledge (mo-DC indistinguishable). The Results sentence "disruption of Notch pathway activity ... may play a protective role" contradicts the proposed direction.
- Wnt/renewal: the MYC risk allele increases MYC in the colocalising stem-cell annotation. That is directionally inconsistent with "impaired renewal" unless argued otherwise. The RASGRP1 risk allele increases a gene that restricts epithelial growth (L-manuscript ref. 40), which is compatible with the model. RNF14 decreases in inflamed enterocytes on very few samples. FUBP1 is divergent. LPIN3 has no figure, and its Wnt link cites a CRC immunology paper (manuscript ref. 43). The genes do not form a tested pathway, and the directions are mixed.
- Venue relevance: these are abstract-level claims that carry the "mechanistic" framing.

### H5
- Factual errors: tofacitinib is a JAK inhibitor with functional preference for JAK1/JAK3 over JAK2-pair signalling (L14, from the FDA label text as reported in search results). IL23R is not the direct target of approved IL-23 pathway antibodies, which target p19/p40 (field knowledge, not re-verified by a source this session; stated in the review as a request to correct the pairing, not as a detailed pharmacology claim). "Respectively" pairs three genes with two drugs. No PKC-β inhibitor IBD trial was found in a search (L15 search negative). The claim needs a citation and conflicts with the Methods filter. The NDUFAF1–metformin side-effect inference is speculative. γ-secretase inhibitor GI toxicity via intestinal Notch/goblet metaplasia is established (L16), which the authors could cite instead of eQTL-based inference.

### Literature Source Register

| ID | Citation | Role | Proposition | Affects | Verified |
| --- | --- | --- | --- | --- | --- |
| L1 | Mostafavi H, Spence JP, Naqvi S, Pritchard JK. Nat Genet 55:1866–1875 (2023). doi:10.1038/s41588-023-01529-1 | foundational/benchmark | eQTLs cluster near TSS whereas GWAS hits do not; selection hinders discovery of functionally relevant eQTLs | H1, I1, I2, I7 | Yes (search abstract) |
| L2 | Liu Z et al. Nat Genet 55:796–806 (2023). PMID 37156999 | benchmark | 320 IBD loci from EAS+EUR meta-analysis | M2.1, minor | Yes |
| L3 | Wallace C. PLoS Genet 16:e1008720 (2020). PMID 32310995 | standard | coloc prior misspecification alters posteriors; sensitivity analysis | I2 | Yes |
| L4 | Wallace C. PLoS Genet 17:e1009440 (2021) | standard | recommends coloc+SuSiE when multiple causal variants | I2 | Yes |
| L5 | Hukku A et al. AJHG 108:25–35 (2021). PMID 33308443 | standard | promise and limitations of probabilistic colocalisation | I4/minor | Yes (metadata) |
| L6 | Urbut SM, Wang G, Carbonetto P, Stephens M. Nat Genet 51:187–195 (2019) | method precedent | mash estimates effect sharing/heterogeneity across conditions | I1, I3 | Yes |
| L7 | Kim-Hellmuth S et al. Science 369:eaaz8528 (2020) | prior evidence | cell-type-interaction QTLs yield >50% more colocalisations than standard QTLs | H1 novelty | Yes |
| L8 | Yazar S et al. Science 376:eabf3041 (2022). PMID 35389779 | prior evidence | 1.27M PBMCs, 982 donors, 14 cell types, 26,597 cis-eQTLs, most cell-type-specific | H1 novelty | Yes |
| L9 | Yao DW, O'Connor LJ, Price AL, Gusev A. Nat Genet 52:626–633 (2020). PMID 32424349 | benchmark | ~11% of heritability mediated by assayed expression; MESC framework | I2 route | Yes (pages from memory; title/journal/finding verified) |
| L10 | de Lange KM et al. Nat Genet 49:256–261 (2017) | data source | 25,305 new GWAS; meta-analysis 59,957 subjects | M2.1 | Yes |
| L11 | Pinnell N et al. Immunity 43:870–883 (2015) | conflicting/qualifying | Zmiz1 selective Notch1 cofactor in T cells; no major role in intestinal homeostasis or myeloid suppression | H4, I4 | Yes (abstract content via search snippet) |
| L12 | Lewis KL et al. Immunity 35:780–791 (2011) | context | Notch2 required for intestinal CD11b+CD103+ DC; loss reduces IL-17+ CD4 T cells | H4, I4 | Yes |
| L13 | Satpathy AT et al. Nat Immunol 14:937–948 (2013). PMID 23913046 | context | Notch2-dependent intestinal cDCs are obligate IL-23 source in C. rodentium | H4, I4 | Yes |
| L14 | Tofacitinib pharmacology (label/review text via search) | fact check | functional selectivity for JAK1/JAK3-associated receptors over JAK2 pairs | H5 minor | Partially (secondary sources) |
| L15 | Search for PKC-β inhibitor IBD trials | negative search | no trial located | H5 minor | Search negative, recorded as "citation needed" |
| L16 | Milano J et al. Toxicol Sci 2004 (PMID 15319485); van Es JH et al. Nature 2005 | context | γ-secretase inhibition causes intestinal goblet-cell metaplasia via Notch | H5 minor | Milano verified via PubMed listing; van Es via secondary snippet |
| L17 | Oliver AJ et al. Nature 635:699 (2024) | context | healthy gut reference atlas of ~1.1M cells (1.6M incl. spatial) | "largest atlas" minor | Yes |

### High-Level Roll-Up

- H1: the direction is plausible and consistent with L1, L7 and L8. The weakest bridge is detection-based classification without a matched-power/test-count null. Defensible now: "eQTLs detected only in finer annotations are more TSS-distal and more often colocalise with IBD loci". Overclaim: "increases power", "masked in bulk", "over two-fold", and the evolutionary inference.
- H2: a useful resource. Counts need reconciliation, and robustness to coloc assumptions is required. The claim "nominate" is defensible. "Effector genes" and "mechanistic map" overstate.
- H3: not supported as stated, because of the r² selection bias.
- H4: hypothesis-level only, with direction inconsistencies.
- H5: contains factual errors and speculation. Correction plus moderation is needed.

## S3 — Issue and Action Ledger

### I1 — Validity-critical
- Affects: H1 / M1.1, M1.2 / E1.1a, E1.2a–c (Fig. 2d–f, S4, S5)
- Problem: detection-based resolution classes differ in number of annotations (217/30/4), power and lead-variant precision. Bootstrap t-tests are invalid. Fig. 2f CIs overlap.
- Consequence: the genomic-context differences may be artefacts of power and test count.
- Action: (a) a null in which cells are randomly partitioned into pseudo-annotations matched in size and donor count to the real cell types, re-running the pipeline (decisive). Or, as a valid alternative, downsampling/matching annotations on donors and cells together with stratification by effect size, MAF and expression. (b) Replace t-tests with bootstrap CIs of differences. (c) Report multiple-testing control across annotations.
- Purpose: exclusion of artefact; robustness.
- Role: (a) Decisive / Valid alternative; (b, c) required correction.
- Effect of results: if pseudo-annotations reproduce the shifts, H1 collapses to an artefact. If not, H1 is strengthened substantially.
- Fallback: describe the differences as detection-associated without causal or evolutionary interpretation. That would weaken the venue case.
- Status: Drafted (Major 1).

### I2 — Validity-critical
- Affects: H1 / M1.3 / Fig. 3b, S7; M2.1
- Problem: OR undefined, no uncertainty, number of colocalisation tests per gene differs by resolution, single-causal-variant coloc with multiple independent eQTLs, no negative-control traits, and S7 does not test the confounder.
- Action: define the OR with CIs. Fit a gene-level model including number of annotations tested, expression, specificity, eQTL effect size, and effector vs non-effector. Run coloc-SuSiE and prior sensitivity (L3, L4). Test resolution enrichment for non-immune control traits. Optionally, a heritability-based comparison (MESC/S-LDSC-type).
- Role: gene-level model + negative control = Decisive. coloc-SuSiE = required robustness. Heritability analysis = Valid alternative.
- Status: Drafted (Major 2).

### I3 — Validity-critical
- Affects: H3, H4 / Fig. 3c–e, 4c, S9–S11
- Problem: the max-r² rule is biased to small-n annotations. The colocalising annotation often differs from the top-r² annotation. Disease status is coupled with site.
- Action: report n and a CI for r² in every annotation. Use shrinkage (mash) or bias-corrected effects. Require colocalisation (or report its PPH4) in the nominated annotation. Show the robustness of the Fig. 3c–e distributions to these changes.
- Fallback: rename to "annotation with largest estimated effect" and remove "effector cell type" claims.
- Status: Drafted (Major 3).

### I4 — Venue-critical (with validity-critical wording elements)
- Affects: H4 (Abstract, Figs 4–5, Discussion)
- Problem: pathway-level mechanism is inferred from 2–4 colocalisations, with no enrichment test, mixed directions, a misattributed ZMIZ1 biology (L11), and no functional data. Notch2's role in cDC2 differentiation (L12, L13) makes the direction and composition interpretation uncertain.
- Action: either provide functional evidence for at least one nominated mechanism (e.g. allele-specific regulatory activity of the colocalising variant in the relevant cell type, together with evidence that altering gene dosage changes Notch target output or DC phenotype), or formally test pathway enrichment against a matched background and recast the abstract and Results as hypotheses. The authors are not prescribed a protocol.
- Role: functional = Decisive for mechanism. Enrichment + calibration = Claim-calibration fallback. That fallback may fall below Nature's threshold (confidential).
- Status: Drafted (Major 4).

### I5 — Validity-critical (for ieQTL claims)
- Affects: M2.2, RNF14, "2 loci only ieQTL", Discussion "764 ieGenes"
- Problem: no significance definition. Composition confounding within major populations. Few inflamed samples (Fig. 5d). Coloc with interaction summary statistics is not described.
- Action: specify the testing and FDR procedure. Adjust for within-population cell-state proportions. Show robustness (permutation of the interaction variable; per-genotype n). Clarify what statistic entered coloc for ieQTLs.
- Status: Drafted (Major 5).

### I6 — Recommended strengthening
- Pseudoreplication in cross-site analysis (donors contributing multiple samples). Clarify, and if necessary use per-donor aggregation or a mixed model. Also 10x chemistry and genotyping batch covariates.
### I7 — Recommended
- Evolutionary model: test with constraint metrics (as in L1) or present as speculation.
### I8 — Recommended
- Scope: no UC patients, rectum non-IBD only, blood CD only, European only. Moderate "IBD" framing and UC tissue claims.
### I9 — Recommended
- Therapeutic section corrections (H5).
### I10 — Recommended
- Data/summary-statistic access for review; Table 1 and Supp S1–S3 not available to this reviewer.
### I11–I2x — Minor (see report): count inconsistencies, figure label mismatches, typos, missing methods (GSEA), legend and axis issues, "healthy" terminology, citation needs.

Minor classes checked: figure legibility and legends (Fig. 3b no CI; S5 clipped axis; Fig. 4b label; Fig. 5b gene track); terminology (effector gene, healthy, IBD vs CD, cDC2/mo-DC); counts (320/321; 137/138; 178/180; 82.2%; 75.6%; atlas cell counts; "2,196,874 million"; "50,0000 reads"); statistical reporting (ieQTL FDR, GSEA, bootstrap t-tests, Fig. 3b CI); code/data (code on GitHub; data "upon publication"); positioning (L1, L7, L8, L17); clinical statements exceeding data (metformin, γ-secretase, PRKCB).

### Recommendation State
- Central bottleneck: whether the resolution-dependent enrichment (H1) survives controls for test number and power. Secondarily, cell-type assignment bias (H3) and mechanistic overreach (H4).
- Scientific validity: the core observation is plausible but not yet artefact-controlled.
- Venue-level adequacy: currently below the Nature bar because of I1–I4. The dataset scale and question are Nature-relevant.
- Realistic revisability: I1, I2, I3 and I5 are reanalyses of existing data. I4 needs new experiments or calibration.
- Preliminary recommendation: Major Revision.

## S4 — Draft and Verification

- `peer-review.md` drafted: yes.
- Major Comments mapped: M1 = I1; M2 = I2; M3 = I3; M4 = I4; M5 = I5.
- Recommended Revisions: I6–I10.
- Minor Comments: I11+.
- Recommendation: Major Revision.
- Confidential comment: yes.

### Verification
- Quotes and claim verbs: re-checked by grep. "mechanistic map", "implicating reduced Notch signalling", "suggesting that impaired renewal contributes to barrier breakdown", "masked in bulk analyses", "increases power to detect the effector genes", "support the conclusion that dysregulation of MAML2 expression by this specific sc-eQTL in cDCs contributes to UC risk", and "direct molecular targets of vedolizumab and tofacitinib, respectively" are all present verbatim.
- Numbers: recomputed. 20,389/24,761 = 82.3% (text 82.2%). 104/138 = 75.4% (text 75.6%). Fig. 3a gives 137 OTG loci. 74 + 104 = 178 vs 180. 47/178 = 26.4% and 34/178 = 19.1% confirm a 178 denominator in Fig. 3c. All other percentages checked match.
- Figure references: Fig. 4b eQTL axis label "Macrophages CD163++" (read at original resolution). S10b and S11d were enlarged and read. The r² positions are approximate visual reads and are phrased as such in the review. MYC hg38 position (~127.74 Mb) comes from reviewer knowledge and is not verified by a source this session. The review therefore asks the authors to report the distance, rather than asserting it.
- Existing analyses checked before claiming absence: ieQTL significance (Methods "cis-eQTL mapping" and "Colocalisation" sections, Results, Supp S6 legend). GSEA methods (Methods: none). Multiple-testing across annotations (none). coloc-SuSiE (none). Chemistry covariate (none). Negative-control traits (none). CI for Fig. 3b (figure and legend: none). Per-donor aggregation in cross-site analysis ("Pseudobulking": "samples"; ambiguous).
- OCR/extraction artifacts: "2,196,874 million", "50,0000" and "detectermined" appear in the extracted text. They are plausibly genuine typos but could be conversion artefacts, so they are phrased as "please check".
- Unresolved: Table 1 and Supp S1–S3 were not reviewed and are marked Not assessable. The ZMIZ1 and PSEN2 eQTL track labels were read from small figure text: the PSEN2 label was read after enlargement, while the ZMIZ1 label is partially legible and is phrased as "appears to be".

## S5 — Final Pruning and Decision

- Requested actions classified: each Major keeps one decisive route plus, where defensible, one alternative or fallback. Supporting characterisation (heritability analysis; constraint analysis) was moved to optional wording or Recommended.
- Duplications removed: coloc-SuSiE appears only in M2. Composition confounding appears in M5 and briefly in M4 (a different claim).
- Alternative-route equivalence: in M1, the pseudo-annotation null and the matched-downsampling analysis both test the power artefact, so they are acceptable alternatives. In M4, the calibration fallback resolves validity but may not meet the venue bar, so that point is flagged only in the confidential comment.
- Final length: about 2,240 words in total, of which Major Comments are about 1,260, Recommended about 280 and Minor about 320. This is above the 1,200 default. It is justified by five independent validity-critical issues with distinct remedies. A compression pass after the first draft (2,345 words) shortened each Major. The PSEN2 bullet was removed from Major 4 because it duplicated Major 3.
- Coverage preservation (explicit decisions):
  - External replication of headline result: dropped as a requirement. The claim-calibration route and the within-data null (I1) resolve validity. Replication is noted implicitly in the confidential comment.
  - Novelty vs closest prior resources (Kim-Hellmuth 2020; Yazar 2022; Mostafavi 2023): kept, merged into Major 2 and Recommended 3.
  - Cross-site/batch comparability (chemistry, genotyping batch, pseudoreplication, site–disease coupling): kept as Recommended 1–2 and in Major 3 (site–disease coupling).
  - Data/summary-statistic availability: kept as Recommended 5.
- Action dispositions:
  - Minimum required: I1 null/matching + bootstrap-CI correction; I2 OR definition + gene-level model + coloc–SuSiE + negative-control traits; I3 uncertainty/shrinkage + PPH4 in nominated annotation; I4 functional evidence OR enrichment + calibration; I5 FDR spec + composition adjustment + calibration.
  - Recommended: I6–I10.
  - Removed: heritability-mediation analysis (supporting characterisation only; I2 alternative not needed in report).
- Scientific judgment and recommendation unchanged by pruning.

### Final Decision Rationale
- Final recommendation: Major Revision.
- Claim-validity basis: H1 plausible but not artefact-controlled (I1, I2). H3 method biased (I3). ieQTL not specified (I5).
- Venue-completeness basis: the mechanistic claims (I4) lack functional support expected for Nature-level mechanistic framing.
- Why proportionate: four of five Majors require reanalysis of existing data only. One requires new evidence or calibration.
- Residual uncertainty: the results of the reanalyses. Also whether the calibrated paper meets Nature's threshold (editorial).

## Locked Decisions and Handoff
- Preserve quotes as listed above.
- Flag inconsistencies: 178/180; 137/138; 75.6%; 82.2%; 320/321; atlas cell counts; Fig. 4b label; RPS14.
- Requests intentionally excluded: new UC patient cohort (scope calibration suffices); replication cohort (not required given the calibration route); specific CRISPR protocols (not prescribed).
- Output paths: `.../A/ai_review_v2/peer-review.md`, `.../A/ai_review_v2/review-dossier.md`.
