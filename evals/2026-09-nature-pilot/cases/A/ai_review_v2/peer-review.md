# Referee Report — Nature, initial submission

**Manuscript:** Cell-type-resolved genetic regulatory variation shapes inflammatory bowel disease risk

## Overall Assessment

The authors map cis-eQTLs in about 2.2 million single cells from the terminal ileum, rectum and blood of 397 genotyped donors. They then colocalise these eQTLs with IBD GWAS signals. The cohort is large and valuable. The central question, whether finer cellular resolution closes the eQTL–GWAS gap, is important and of broad interest.

The headline result is that eQTLs detected only at cell-type resolution are more TSS-distal, more enhancer-enriched and more often colocalise with IBD loci. The direction is plausible and consistent with prior work. However, the resolution classes are defined by detection, and they differ markedly in the number of annotations tested and in statistical power. The analysis does not yet separate these factors from biology.

Two further problems follow. First, the procedure used to assign "effector cell types" is biased towards small annotations. Second, the Notch and Wnt mechanistic conclusions in the Abstract rest on a handful of colocalisations whose effect directions are mixed.

Most of these issues can be addressed by reanalysing existing data. The mechanistic claims need either functional support or substantial recalibration.

## Major Comments

**1. The genomic-context differences between resolutions need a matched-power, matched-test-count null.**

eQTLs are assigned to the minimum resolution at which they are detected. The resolution classes differ in:

- number of annotations (217 cell-type vs 30 major-population vs 4 All Cells annotations; Supplementary Fig. S4);
- donors and cells per test;
- precision of the lead variant.

Because "distinct" eQTLs are defined by failure to clump at r² > 0.5, imprecise lead variants from small annotations tend to be scored as new signals. Effects detectable only in small annotations are also, on average, weaker in bulk, and eQTL discovery concentrates near the TSS (Mostafavi et al., Nat Genet 2023). The shifts in Fig. 2d–f and Supplementary Fig. S5 could therefore arise partly from power and multiplicity. Separately, the Fig. 2f p-values come from t-tests on bootstrap replicates, which are not independent observations. The cell-type and major-population intervals overlap, yet p < 2.2 × 10⁻¹⁶ is reported for all comparisons.

Please compare resolutions against a null that preserves power and test number, for example cells randomly partitioned into pseudo-annotations matched in size and donor count to the real cell types. An acceptable alternative is to match annotations on donors and cells and stratify by effect size, MAF and expression. Please also report bootstrap CIs for the between-resolution differences and state how multiple testing across the 252 annotations is controlled. If pseudo-annotations reproduce the shifts, the "masked in bulk analyses" interpretation and the evolutionary model should be withdrawn.

**2. The colocalisation enrichment by resolution (Fig. 3b) is not defined, lacks uncertainty, and is not controlled for plausible confounders.**

The "ratio of odds between eGene detection and disease-effector gene nomination" (2.68/1.57/0.75) is not defined in the Methods, and no confidence interval or test is shown. This comparison underlies the Abstract's "over two-fold more likely" and the statement that cell-type mapping "increases power to detect the effector genes".

Three problems remain:

- **More tests per gene.** Genes detected only at cell-type level are tested for colocalisation in many annotations, which multiplies the chances of exceeding PPH4 > 0.75.
- **Single-causal-variant assumption.** coloc.abf assumes one causal variant per trait, yet many eGenes carry several independent eQTLs (eight for MAML2).
- **Confounding is not tested.** Supplementary Fig. S7 compares expression specificity only among colocalising genes, so it cannot show whether specificity confounds effector versus non-effector status.

Please define the statistic and report CIs, and fit a gene-level model of colocalisation status that includes number of annotations tested, expression level, CELLEX specificity and eQTL effect size. Please also repeat the colocalisation with coloc–SuSiE plus prior sensitivity analysis (Wallace, PLoS Genet 2020, 2021), and test whether the same resolution gradient appears for traits without an expected immune or intestinal component.

This matters for positioning. Cell-type-interaction QTLs (Kim-Hellmuth et al., Science 2020) and single-cell blood eQTLs (Yazar et al., Science 2022) have already yielded colocalisations beyond bulk. The distinctive contribution here is therefore a rigorous quantitative comparison across resolutions.

**3. The "effector cell type" assignment is biased towards small annotations.**

For each locus, the chosen annotation is the one where the lead variant explains the largest r², among annotations with nominal p < 0.05. This is described as mitigating power bias, but it does the opposite. The null expectation of r² is about 1/(n−1), and the r² needed to reach p < 0.05 rises steeply as n falls. Taking the maximum across many annotations therefore favours annotations with few donors.

The data show this pattern:

- Rare annotations rank highly in Fig. 3e: atypical B cells (10 loci, the top single cell type, not discussed), cDC1 and pDC.
- ZMIZ1 reaches 23% variance explained in rectal cDC2 (Supplementary Fig. S9).
- The top MAML2 r² is in cross-site cDC1, where about five donors are risk-homozygous (Fig. 4c).

The nominated annotation also often differs from the one that colocalises:

- **MAML2:** Fig. 4b plots the eQTL in "Macrophages CD163++", but the text reports colocalisation in TI cDC2.
- **ZMIZ1:** the eQTL track appears to be a CD4+ memory T-cell annotation.
- **PSEN2:** the colocalising annotations in Supplementary Fig. S11c,d appear to be colonocytes, where the risk allele increases expression. The monocyte decrease highlighted in the text is not marked as colocalising.

Disease status is also partly coupled with annotation. Blood myeloid and atypical B cells come almost entirely from Crohn's disease (CD) donors, and colonocytes almost entirely from non-IBD donors (Supplementary Fig. S2).

Please report n and a CI for r² per annotation, and use shrinkage or multi-condition effect estimates (e.g. mashr; Urbut et al., Nat Genet 2019). Please also report the PPH4 in the nominated annotation and show whether Fig. 3c–e and the dendritic-cell emphasis survive these changes. Otherwise, please describe these results as "the annotation with the largest estimated effect", not the effector cell type.

**4. The Notch and Wnt mechanistic conclusions exceed the evidence.**

The Abstract states that the data implicate "reduced Notch signalling in intestinal immune dysfunction" and suggest "that impaired renewal contributes to barrier breakdown", and calls the result "a mechanistic map". The Results state that the data "support the conclusion" that MAML2 dysregulation in cDCs "contributes to UC risk".

Each of these rests on two to four colocalisations, with no pathway enrichment test against a matched background and no functional data. The effect directions are also mixed:

- **MYC:** the risk allele increases expression in the colocalising stem-cell annotation, which is hard to reconcile with impaired renewal. The largest effects are in macrophages, plasma cells and venous endothelium, with discordant directions (Supplementary Fig. S10b).
- **RASGRP1:** the risk allele increases expression.
- **MAML2:** the risk allele increases expression in vascular smooth muscle but decreases it in DCs.

The cited biology also needs care:

- **ZMIZ1.** Pinnell et al. (Immunity 2015) describe Zmiz1 as a selective Notch1 cofactor in T cells with no major role in intestinal homeostasis or myeloid suppression. It is therefore not a natural readout of DC Notch activity.
- **Notch2 in DCs.** Notch2 signalling drives intestinal CD11b⁺ cDC2 differentiation and their support of IL-17/IL-23 responses (Lewis et al., Immunity 2011; Satpathy et al., Nat Immunol 2013). The inflammatory consequence of reduced DC Notch activity is therefore not established.
- **Composition.** A cis-eQTL in a "cDC2" pseudobulk that includes mo-DCs could reflect subset composition.

For a Nature-level mechanistic claim, please provide functional evidence for at least one nominated mechanism. That means showing that the colocalising variant regulates the gene in the relevant cell type, and that altering gene dosage changes the proposed pathway output or phenotype. Otherwise, please test pathway enrichment formally and recast these sections as hypotheses, using "candidate effector gene".

**5. The interaction-eQTL analysis is not specified well enough to assess.**

The Methods do not state how the 1,051 ieQTLs were declared significant, or how multiple testing was handled across variants, genes, annotations and five interaction variables. Inflammation varies only within CD terminal ileum. Within a major population such as enterocytes, inflammation also shifts the mix of cell states, which can create apparent genotype × inflammation effects.

Only 44 of the ieQTLs (4.2%) are in LD with an eQTL. That is compatible with novel biology but also with false positives. The RNF14 example (Fig. 5d) rests on very few moderately or severely inflamed samples per genotype. It is also unclear which statistics entered colocalisation for ieQTLs.

Please specify the testing procedure and FDR, adjust for within-population cell-state proportions, show permutation-based calibration, and report n per genotype and inflammation class. The "764 ieGenes" and the two ieQTL-only loci cannot be interpreted until this is done.

## Recommended Revisions

1. **Pseudoreplication and covariates.** Please clarify whether donors contributing more than one tissue are represented once or several times in the "cross-site" pseudobulks. If more than once, use per-donor aggregation or a mixed model, because the 1,945 cross-site-only eGenes could otherwise be inflated. Please state whether 10x chemistry (v3.0/v3.1) and genotyping batch were modelled.
2. **Scope.** The cohort includes no UC patients. Rectal tissue is from non-IBD donors only, blood is from CD donors only, and all donors are of European ancestry. Please use "CD" where appropriate, moderate UC-specific tissue interpretations, and note that the Liu et al. (2023) locus list includes East Asian-derived signals while colocalisation used de Lange et al. (2017) summary statistics. Some highlighted signals (e.g. MAML2 and PSEN2) appear to be sub-genome-wide in those statistics.
3. **Evolutionary model.** Please either test it (for example, gene constraint by resolution class, as in Mostafavi et al.) or present it clearly as speculation.
4. **Therapeutic section.**
   - The sentence pairing ITGA4, JAK2 and IL23R with vedolizumab and tofacitinib "respectively" is incorrect. Tofacitinib acts predominantly through JAK1/JAK3-dependent signalling, and approved IL-23-pathway agents target the ligand rather than IL23R.
   - Please cite the PRKCB inhibitor trials in IBD, and reconcile this with the Methods, which restrict Fig. 6 to drugs not yet trialled in IBD.
   - The NDUFAF1–metformin and PSEN2 side-effect inferences should be framed as speculative. γ-secretase inhibitor gastrointestinal toxicity via intestinal Notch inhibition is already well documented.
   - Please filter implausible drug–target pairs from Fig. 6 (e.g. ribosomal proteins, troponins).
5. **Data access.** Full eQTL, ieQTL and colocalisation summary statistics, Table 1 and Supplementary Materials S1–S3 were not available to this reviewer. Please make the summary statistics available to reviewers.

## Minor Comments

1. **Counts need reconciling.**
   - 320 (Introduction) vs 321 (Results) known loci.
   - 137 (Fig. 3a) vs 138 (text) OTG-colocalised loci; 104/138 is 75.4%, not 75.6%.
   - 74 new + 104 previously colocalised = 178, and Fig. 3c appears to sum to about 178, vs 180 in the text.
   - 20,389/24,761 is 82.3%, not 82.2%.
   - 1,852,681 (Methods) vs 1,837,436 (Supplementary Fig. S2) atlas cells.
   - "2,196,874 million cells" and "50,0000 reads per cell" also need checking.
2. **Fig. 3b.** Please define the x-axis and add CIs.
3. **Fig. 4b.** Please plot the eQTL for the annotation named in the text.
4. **Fig. 5b.** Please show the MYC gene position and its distance to the lead variant (chr8:128,528,218).
5. **Figure legends.**
   - Fig. 5 legend: "villu"; "disease severity" vs "inflammation" in the text.
   - Supplementary Fig. S4 legend: "detectermined", "wicoxon".
   - Supplementary Fig. S5: the y-axis is clipped.
   - Supplementary Fig. S7 cites "Timshel et al., 2022", whereas the reference list gives 2020.
6. **Discussion.** The Discussion lists RPS14, which does not appear in the Results (RNF14?).
7. **Wording.** "disruption of Notch pathway activity ... may play a protective role" appears to invert the intended meaning.
8. **Missing Methods.** Please add the gene set enrichment method (including what "coefficient" denotes), the ieQTL colocalisation inputs, and the eQTL model equations.
9. **Cell rescue.** Please state how many cells that failed within-lineage QC were reintroduced by CellTypist, and whether excluding them changes eQTL results.
10. **Terminology.** Participants without IBD undergoing endoscopy are not necessarily "healthy". "Non-IBD controls" is more accurate.
11. **MAML2.** MAML proteins bind the NICD–RBPJ complex rather than RBPJ alone; please correct the description.
12. **Citations and positioning.**
    - Please cite a source for "over 4.9 million people worldwide".
    - Please qualify "largest single-cell atlas of IBD-relevant tissues" relative to existing integrated gut atlases.
    - Please state the version and access date of Open Targets Genetics used to define novelty.

## Recommendation

Major Revision. Comments 1, 2, 3 and 5 can be addressed by reanalysing existing data. Comment 4 requires either new functional evidence or substantial recalibration of the mechanistic claims.

## Confidential Comment to Editor

This is a large, carefully generated resource, and the question is of broad interest. The main risk is that the central quantitative claim (resolution-dependent enrichment) is currently confounded by the number of annotations tested and by power. This is a validity issue, not a presentation issue. It is testable with the existing data, so I recommend Major Revision rather than rejection.

Whether the paper reaches Nature's threshold after revision depends on two things. First, the resolution effect needs to survive an appropriate null. Second, either at least one nominated mechanism needs functional support, or the editors need to judge that a robust quantitative demonstration plus the resource is sufficient. If the enrichment weakens substantially under the requested controls and the biology stays at the level of colocalisation-based hypotheses, the work would be better suited to a specialist genetics journal.
