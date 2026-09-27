# Referee Report

**Manuscript:** Cell-type-resolved genetic regulatory variation shapes inflammatory bowel disease risk
**Journal:** Nature (initial submission)

## Overall Assessment

The authors map cis-eQTLs across about 2.2 million single cells from the terminal ileum, rectum and blood of roughly 400 genotyped individuals. They report that eQTLs detected only at cell-type resolution are more distal, less promoter-biased and more likely to colocalise with IBD GWAS loci. They then nominate effector genes and cell types, and from these infer reduced Notch signalling in dendritic cells and impaired Wnt-dependent epithelial renewal. The dataset is a substantial resource, and comparing resolutions within the same donors suits the question well. However, the central resolution effect has not been separated from differences in power, in the number of annotations tested, and in how precisely lead variants are placed. The cell-type assignments rely on a metric that favours small annotations. The pathway conclusions rest on single colocalisations whose directions do not agree.

## Major Comments

**1. The resolution effect may reflect power and multiple testing rather than biology.**
The resolution bins contain 4, 30 and 217 annotations (Supplementary Fig. 4), with very different numbers of donors and cells, and eQTLs are called separately in each annotation. In small annotations, lead variants are placed less precisely and false positives are more common. Either problem alone would produce every reported trend:
- greater distance to the TSS (Fig. 2e);
- a lower nearest-gene rate (Supplementary Fig. 5);
- an enhancer/promoter ratio closer to the random-SNP value of 1 (Fig. 2f; all ratios are below 1);
- more "distinct" LD clumps per eGene (Supplementary Fig. 4). At MAML2, for example, several singleton clumps lie within tens of kb of the colocalising cluster (Supplementary Fig. 8).

The Fig. 2f p-values come from t-tests on bootstrap replicates, so they reflect the number of replicates rather than real uncertainty, and the major-population and cell-type intervals overlap. The Abstract's "over two-fold" claim rests on the odds ratio in Fig. 3b, which is not defined in the Methods and has no confidence interval. It is also measured per gene, whereas the Abstract describes eQTLs. Supplementary Fig. 7 compares expression specificity only among genes that colocalise, so it does not control the enrichment itself.

Please:
- compare resolutions at matched power, by downsampling donors and cells and by matching eQTLs on significance, effect size and MAF;
- repeat the positional and annotation analyses using fine-mapped credible sets weighted by posterior inclusion probability (PIP), and report absolute enrichments with interval-based or permutation inference;
- define the estimand in Fig. 3b and estimate it with a gene-level model with confidence intervals. The model should adjust for the number of colocalisation tests per gene, expression level and specificity, gene constraint and locus features. This matters because genes near GWAS hits are known to differ systematically in constraint and regulatory complexity (Mostafavi et al., Nat Genet 2023).

If the effect weakens after matching, please restate the Abstract, the "masked in bulk analyses" statement and the evolutionary model as power-dependent observations in this dataset.

**2. The effector cell-type assignment is biased toward small annotations.**
The Methods say that choosing the annotation with the largest genotype r² "mitigates power-related biases". However, r² is considered only where nominal p < 0.05, so its minimum possible value depends on sample size: about 13% at n = 30, about 4% at n = 100 and about 1% at n = 400. Taking the maximum therefore favours annotations with few donors, such as blood annotations (CD donors only) and intestinal dendritic cells. The nominated cell types often differ from the annotations in which colocalisation was actually detected:
- **MAML2:** colocalisation occurs in four myeloid annotations (Fig. 4c), and Fig. 4b plots the Macrophages CD163++ eQTL.
- **ZMIZ1:** the regional plot uses a CD4+ memory CXCR6+ eQTL (Supplementary Fig. 9).
- **PSEN2:** colocalisation is shown in a colonocyte annotation. The monocyte and endothelial effects discussed in the text each explain less than 5% of variance, and one genotype class has a single donor (Supplementary Fig. 11c,d).
- **MYC:** please reconcile colocalisation in stem cells with the opposite-direction effects in the annotations with the highest r² (Supplementary Fig. 10b).

Please estimate per-annotation effects with standard errors, using multi-condition shrinkage (e.g., mash; Urbut et al., Nat Genet 2019) or an equivalent method. Please test heterogeneity and sign discordance formally, which also applies to the opposite-direction claims for PSEN2 and FUBP1. Please report donor and genotype-class counts, and base Fig. 3c–e on annotations that have colocalisation support. Otherwise, label the current assignments as exploratory and remove the conclusions that depend on specific cell types.

**3. The Notch and Wnt conclusions go beyond single-locus colocalisation.**
The Abstract states that the data implicate "reduced Notch signalling in intestinal immune dysfunction" and suggest "that impaired renewal contributes to barrier breakdown". Several points weaken these statements:
- The plotted UC associations at MAML2 and PSEN2 reach only about p = 10⁻⁶ (Fig. 4b; Supplementary Fig. 11c).
- A change in MAML2 mRNA is not shown to change Notch target output.
- cDC2s cannot be separated from monocyte-derived DCs in this atlas.
- The directions are inconsistent for "impaired renewal": the risk allele increases expression of MYC, a pro-proliferative Wnt target.
- In the Discussion, "disruption of Notch pathway activity ... may play a protective role" contradicts the intended model.

Notch2 is required for intestinal cDC2 development in mice (Lewis et al., Immunity 2011), which makes the hypothesis plausible but does not establish the direction of effect. Please either provide functional evidence for at least one of these axes in relevant human cells, or present both as hypotheses in the title, Abstract and Discussion. Notch- and Wnt-target programme scores stratified by genotype would help show that the directions are coherent, but would not by themselves establish mechanism.

**4. The colocalisation calls and the novelty benchmark need robustness analyses.**
coloc.abf assumes a single causal variant per trait, but eGenes carry about 2–3 independent eQTLs (Supplementary Fig. 4) and many IBD loci contain several signals. Please:
- add a sensitivity analysis that allows multiple causal variants (coloc-SuSiE; Wallace, PLoS Genet 2021) and test sensitivity to the priors;
- state the PPH4 threshold used for standard eQTLs (it is given only for ieQTLs);
- explain how a single effector gene is chosen where several genes appear highlighted in a regional plot (ITPKB at PSEN2; NDFIP1 at RNF14; OIP5/NUSAP1/RTF1 at NDUFAF1).

The "74 loci where an effector gene is nominated for the first time" are benchmarked only against colocalisations in Open Targets Genetics (OTG). Please either compare with other resources, including ABC enhancer–gene maps (Nasser et al., Nature 2021), other single-cell eQTL datasets and cell-type-resolved blood/gut IBD eQTLs (medRxiv 2024, doi:10.1101/2024.10.14.24315443), or restrict the claim to "first colocalisation reported in OTG".

**5. The drug and safety interpretations contain factual errors.**
- ITGA4, JAK2 and IL23R are described as "the direct molecular targets of vedolizumab and tofacitinib, respectively". No approved IBD therapy targets IL23R directly, and tofacitinib preferentially inhibits JAK1/JAK3-containing pairs (US prescribing information).
- PRKCB inhibitors are described as "approved for oncology", but the PKCβ-selective inhibitor enzastaurin is not approved. The statement that these inhibitors are in IBD trials also conflicts with the Methods, which excluded genes already trialled in IBD.
- The intestinal toxicity of γ-secretase inhibitors is attributed to PSEN2 in immune and vascular cells. The established intestinal effect of Notch/γ-secretase inhibition is conversion of crypt progenitors into goblet cells (van Es et al., Nature 2005). The link between metformin and NDUFAF1 is likewise speculative.

Please correct these points, indicate in Fig. 6 whether the direction of the risk-allele effect is consistent with each drug's mechanism, and present the safety links as hypotheses.

## Recommended Revisions

1. **Interaction eQTLs.** Only 4.2% are in LD with eQTLs. Please describe the FDR procedure and show robustness to shifts in cell state within annotations and to sparse genotype-by-inflammation cells (e.g., the moderate/severe group in Fig. 5d).
2. **Evolutionary model.** Please test it (e.g., gene constraint, and MAF and effect-size distributions by resolution) or label it as speculation.
3. **Cohort design.** Blood comes only from CD patients, rectum only from non-IBD individuals, and TI from both. Please state whether disease status, inflammation and medication were covariates in the main eQTL model. Please also discuss how this design affects the cross-site analyses and UC colocalisations mapped in non-UC tissue.

## Minor Comments

1. **Locus counts:**
   - 320 loci (Introduction) vs 321 (Results).
   - 180 colocalising loci vs 104 + 74 = 178 and the Fig. 3c totals (47/178 = 26.4%).
   - 138 (text) vs 137 (Fig. 3a); 104/138 = 75.4%.
2. **Other numbers:**
   - 20,389/24,761 = 82.3%.
   - The Abstract states 421 individuals, but the eQTL cohort is 397.
   - Atlasing cells: 1,852,681 (Methods) vs 1,837,436 (Supplementary Fig. 2).
   - Typos: "2,196,874 million cells" and "50,0000 reads".
3. Fig. 3e does not support the statement that DCs are "three of the four" most frequently nominated cell types.
4. Fig. 2f shows reduced promoter bias, not preferential enrichment in enhancers over promoters; please revise the wording.
5. "RPS14" appears in the Discussion but not in the Results. The PRKCB trial sentence is duplicated.
6. Please check that ref. 43 supports "LPIN3 ... regulates Wnt signalling". For MYC, note that the lead variant lies about 0.8 Mb from the TSS, and state whether nearby transcripts (e.g., LINC00824) were tested.
7. The GWAS summary statistics (de Lange 2017, European ancestry) differ from the locus definitions (Liu 2023, multi-ancestry). Please define the denominator of loci that can be tested.
8. Please give the full eQTL and interaction models, including covariates, in the Methods.
9. Summary statistics, Table 1 and Supplementary Materials S1–S3 were not available to this referee, so the locus-level results could not be checked. Please make them available for review.

## Recommendation

Major revision.

## Confidential Comment to Editor

This is a large and valuable resource, and the question it addresses is important. The main barrier is scientific validity. The headline resolution effect and the cell-type assignments have not yet been separated from artefacts of power and multiple testing. Both can be addressed by reanalysing the existing data. If the resolution effect holds after matching, the general insight could merit Nature, though the biological claims will remain hypotheses without functional support. If the effect weakens and the authors reframe rather than add experiments, the paper would be a strong resource better suited to a specialist genetics journal. The statements about drug targets are factually wrong and need correcting whatever the decision.
