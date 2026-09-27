# Review Dossier

## Status and Source Set

- Mode: Initial
- Current stage: S5 complete (delivered)
- Completed stages: S0, S1, S2, S3, S4, S5
- Manuscript version and date: medRxiv v1, doi 10.1101/2025.06.24.25330216, posted 2025-06-24. "Cell-type-resolved genetic regulatory variation shapes inflammatory bowel disease risk" (Alegbe, Harris, ... Raine, Anderson; Wellcome Sanger Institute / Cambridge).
- Source set reviewed: blind/preprint_v1_text.md (full text, Methods, legends, references); blind/preprint_v1.xml (checked for Table 1 and model equations); figures F1–F6 (main Figs 1–6) and F7–F20 (Supplementary Figs 1–14), all viewed; selected panels enlarged (Fig. 4b,c; Supp. Figs 10b, 11c,d).
- Missing / Not assessable: Table 1 (image only; not supplied); cis-eQTL and interaction model equations (images not supplied; Fig. 1c gives "Expr ~ g + PC_GT + PC_Expr"); Supplementary Materials S1–S3 (TSV tables; not retrievable); eQTL/coloc summary statistics (not released per Data Availability).
- Sources intentionally excluded: medRxiv v2, the published journal article, its peer-review file, author responses, commentary; ../reference/ and other case folders.
- Literature cutoff date: 2025-06-24
- Last verified: 2026-09-26 (review-execution date; judgment calibrated to 2025-06-24)
- Next bounded action: none (delivered)
- Dossier confidentiality or storage note: confidential reviewer working record; stored locally in ai_review/; not for transmission to authors/editors.

## S0 — Review Calibration

- Journal and submission stage: Nature, initial submission (simulated). No editor question or review form supplied; standard Nature referee report fields assumed (summary/assessment, major, minor, recommendation, confidential comments).
- Article/study type: Human genetics resource + computational/statistical genomics (single-cell cis-eQTL mapping, colocalisation) with hypothesis-generating biological interpretation. Not mechanistic (no perturbation experiments).
- Central question and intended contribution: Whether eQTLs mapped at cell-type resolution in disease-relevant tissue differ in genomic properties from coarser-resolution eQTLs and better explain IBD GWAS loci; nomination of effector genes/cell types at IBD loci; pathway-level biological insights (Notch in DCs; Wnt/epithelial renewal) and drug-target implications.
- Design, data, population/model, and setting: Cross-sectional; 421 recruited adults at Addenbrooke's (296 non-IBD, 125 CD); scRNA-seq (10x 3') of TI (243 non-IBD, 119 CD, inflamed and uninflamed), rectum (275 non-IBD only), PBMC (95 CD only); genotyping (UKB Axiom, TOPMed imputation), European ancestry only; 397 individuals in eQTL cohort; 86 cell types, 9 major populations, 'All cells'; per-site and cross-site pseudobulk (mean ln cp10k+1, >=5 cells/sample, >=30 individuals); TensorQTL; ieQTL for age/sex/smoking/CD/inflammation; coloc.abf with de Lange 2017 CD/UC/IBD summary statistics; loci per Liu 2023.
- Primary claim ambition and intended scope: General principle (cell-type-level eQTLs distal, enhancer-enriched, 2-fold more likely to colocalise) framed as a "general framework for effector gene discovery across diverse diseases"; effector gene nomination at >half of IBD loci; "mechanistic map"; pathway implications (reduced Notch signalling in DCs; impaired epithelial renewal); drug prioritisation/safety.
- Editor question, review fields, and recommendation options: not provided; using Accept / Minor / Major / Reject.

### Relevant Review Requirements

| Requirement or expectation | Provenance | Basis or source | Consequence for this review |
| --- | --- | --- | --- |
| Colocalisation claims at loci with multiple causal variants should use methods allowing multiple causal variants or conditional signals | Field standard | Wallace 2021 PLoS Genet (L3) | Coloc.abf single-variant assumption with ~2–3 independent eQTLs/eGene is a robustness gap (I4) |
| Comparisons of eQTL vs GWAS properties must account for discovery power and selection/constraint of genes | Field standard | Mostafavi et al. 2023 Nat Genet (L1) | Resolution comparison must be power- and gene-property-matched (I1) |
| Cross-condition eQTL specificity/sharing claims should account for estimation error (shrinkage / heterogeneity tests) | Field standard | Urbut et al. 2019 Nat Genet (L4) | Max-r² cell-type assignment and "discordant effect" claims need uncertainty-aware methods (I2) |
| Nature: broad significance, conclusions supported, data available to referees on request | Journal-stated (general Nature referee criteria; not re-fetched) | Nature editorial policies (general knowledge; not re-verified) | Summary statistics not available at review → reproducibility items Not assessable (I9) |
| Mechanistic/pathway claims at Nature typically require functional support or explicit hypothesis framing | Reviewer calibration | Genre calibration (framework §5) | Notch/Wnt claims to be calibrated or supported (I3) |

- Claim-validity bar: For H1, differences among resolutions must persist after controlling for number of annotations tested, statistical power (donors/cells), lead-variant precision, and gene properties; for coloc enrichment, a defined estimand with uncertainty and gene-level covariate control. For effector cell types, assignment must be robust to sample-size-dependent estimation error and coincide with where colocalisation is supported. For pathway claims, directionally coherent evidence across loci or functional evidence; otherwise "hypothesis".
- Venue-completeness bar: Nature expects a robust general insight (resolution principle demonstrated beyond artefact, ideally with replication or negative-control traits) plus either experimental support for at least one biological axis or a clearly transformative resource. A resource with calibrated claims may be adequate if the general principle is convincingly established.
- Feasibility or material constraints stated in the manuscript: cell numbers limited (57% of cell-type annotations <100 cells/donor); blood only CD; rectum only non-IBD.
- Assumptions not made: no assumption about availability of additional cohorts, cell lines, or perturbation capacity; requested replication framed as existing public data (e.g., independent sc-eQTL resources) or internal cross-site replication.
- Calibration uncertainty: Nature's exact threshold for resource-type human genetics papers without functional validation is editorial; handled in confidential comment.

## S1 — Structured Claim–Evidence Map

### H1 — "Cell-type-level eQTLs were more distal to transcription start sites, enriched in enhancers, less likely to regulate the nearest gene, and over two-fold more likely to colocalise with IBD GWAS loci than eQTLs detected at tissue-level resolution" (Abstract); "High-resolution eQTL mapping therefore uncovers regulatory effects that are masked in bulk analyses."

- Verb strength and claim level: declarative, general principle; Discussion extends to "the genetic architecture of complex diseases is shaped by regulatory effects active in restricted cellular contexts" and an evolutionary model.
- Intended scope: IBD, generalised to complex disease.
- Claimed novelty: systematic cross-resolution quantification in disease tissue.

#### M1.1 — Cell-type-level mapping reveals many distinct eQTLs not detected at coarser resolution
- E1.1a — Fig. 2d; Results: 84,376 eQTLs, 20,389 eGenes; 31% eQTLs only at cell-type level, 36.2% at major-population-not-All-cells; eGenes 77.1/17.5/5.4%. Comparison: eQTLs binned by minimum resolution detected; unit = LD-clumped lead variant (r2>0.5, 1 Mb); endpoint = count. Inference: distinct regulatory variants.
- E1.1b — Supp. Fig. 4: eQTLs per eGene 1.9 / 2.7 / 3.1; n annotations = 4 / 30 / 217; Wilcoxon p<2.2e-16.
- E1.1c — Supp. Fig. 8 (MAML2): 8 clumps, several singletons within ~10–50 kb of the colocalising cluster (r2 0.1–0.3).
- Internal limitation: number of annotations differs ~50-fold across bins; per-annotation FDR; lead-variant instability in small annotations can create "distinct" clumps.

#### M1.2 — Cell-type-level eQTLs are more distal, less nearest-gene, and relatively enhancer-enriched
- E1.2a — Fig. 2e: median TSS distance 44/108/200 kb (All/major/cell-type); % <10 kb 22.6/11.6/6.5; p<2.2e-16.
- E1.2b — Supp. Fig. 5: nearest gene is eGene 38.3/28/20.1%.
- E1.2c — Fig. 2f: enhancer/promoter relative enrichment (normalised to random SNPs) FANTOM ~0.24/0.48/0.64; ENCODE ~0.20/0.40/0.51; bootstrap CIs over LD blocks; two-sided t-tests on bootstrap distributions all p<2.2e-16. All ratios <1.
- Estimand: lead-variant annotation overlap; unit = lead SNP; no fine-mapping.
- Limitation: all three properties shift toward the random-variant expectation (distance uniform over window; ratio→1; nearest-gene frequency ↓) if lead SNPs are less precisely localised or include more false positives; the pattern is therefore non-discriminating between biology and precision/power.

#### M1.3 — Cell-type-level eGenes are more likely to be IBD effector genes
- E1.3a — Fig. 3b: OR 2.68 (cell type), 1.57 (major), 0.75 (All cells); x = proportion of eGenes; no CI or test shown; "ratio of odds between eGene detection and disease-effector gene nomination" undefined in Methods.
- E1.3b — Supp. Fig. 7: CELLEX max specificity does not differ among colocalising genes by resolution (p 0.38–0.82). Comparison is among colocalised genes only.
- Limitation: No adjustment for number of coloc tests per gene (annotations × traits), expression level, constraint, proximity/density at IBD loci; no negative-control traits.

- Logical assembly of H1: M1.1–M1.3 → general principle. Bridge: that bin differences reflect biology of restricted-context regulation rather than detection power/precision/test multiplicity. Missing bridge: power-matched and fine-mapped comparisons; gene-level confounder control.

### H2 — Effector genes nominated at >half of IBD loci, including 74 loci "where an effector gene is nominated for the first time" (Intro), and refinement of effector cell types
- M2.1 — Coloc PPH4>0.75 at 180/321 loci, 419 genes; 74 new vs OTG coloc (E2.1a Fig. 3a, Table 1 [Not assessable], Supp. Material S2 [Not assessable]). Methods: coloc.abf default priors; GWAS suggestive p<5e-5; 2 Mb windows; HLA excluded; assignment within 500 kb of known loci; PPH4>0.75 stated for ieQTL.
  - Internal inconsistencies: Fig. 3a shows 137 public-QTL loci + 74 new = 211 annotated; text 138; 104+74=178 ≠ 180; Fig. 3c denominators = 178 (47/178=26.4%).
- M2.2 — Effector cell type = annotation with maximal r² of lead coloc variant (Methods, "mitigates power-related biases"); E2.2a Fig. 3c–e: myeloid 47 loci, T/ILC 34, colonocyte 32; top cell types include blood atypical B (10), cDC2 (8).
  - Limitation: r² computed only in annotations with nominal p<0.05; minimum r² at p<0.05 ≈13% at n=30, ≈3.9% at n=100, ≈1% at n=400 → structural bias toward small annotations; no uncertainty.
- Bridge: coloc in X + max r² in Y → effector cell Y.

### H3 — "implicating reduced Notch signalling in intestinal immune dysfunction" via MAML2, ZMIZ1 (and PSEN2) in DCs
- M3.1 — MAML2 eQTL colocalises with UC (PPH4 0.98) "in cDC2s from the TI"; only gene at locus; distinct from 7 other MAML2 eQTLs (E3.1a Fig. 4b; Supp. Fig. 8).
  - Fig. 4b plots eQTL from "Macrophages CD163++"; Fig. 4c outlines four colocalising annotations (three myeloid at ~3–4.5% r², cDC2 TI ~12.7%); max r² cDC1 cross-site (~17.5%, not colocalised); vascular smooth muscle TI opposite direction (~10.5%). UC GWAS −log10P ≈6.2 (sub-genome-wide in plotted summary stats).
- M3.2 — cDC specificity not due to baseline expression (Spearman R −0.29, p 0.21; n ≈ 20 annotations).
- M3.3 — ZMIZ1 coloc with CD (PPH4 0.99), strongest in rectal cDC2 (23% r²) (Supp. Fig. 9). Supp. Fig. 9a eQTL track is a CD4+ T-cell annotation; outlined colocalising annotations are mostly T cells (2–10% r²). Authors note mo-DCs indistinguishable from cDC2.
- M3.4 — PSEN2 (Supp. Fig. 11c,d): coloc eQTL track "Colonocyte CEACAM7+ KRT20+ IFI27+"; outlined colocalising annotations colonocyte-coloured, r² ≤ ~4%; narrative cell types (venous EC increase, monocytes decrease) all <5% r²; EC venous has a single 0-allele donor. Gene track also highlights ITPKB.
- Logical assembly: coloc + direction of expression + literature on Notch → "reduced Notch signalling in DCs". Missing bridges: mRNA of co-activator → pathway activity; DC-specific effect; direction coherence (Discussion "disruption of Notch pathway activity ... may play a protective role" is internally contradictory wording).

### H4 — "Wnt regulated genes, including MYC, in epithelial stem and progenitor cells, suggesting that impaired renewal contributes to barrier breakdown"
- E4a RASGRP1 (Fig. 5a; Supp. Fig. 10a): risk allele ↑ in colonocytes; max r² in B-cell annotations too.
- E4b MYC (Fig. 5b; Supp. Fig. 10b): risk allele ↑ MYC in OLFM4+LGR5+ stem cells; lead chr8:128,528,218, ≈0.79 Mb from MYC (hg38 127,735,434); annotations with highest r² (venous EC, IgA plasma, CCL3/CCL4 macrophages) show mixed directions; the outlined colocalising annotation appears at low r² (~1%) — reading of figure partially uncertain.
- E4c LPIN3 (Supp. Mat. S3 Not assessable); ref 43 concerns LPIN3 in CRC CD8 T-cell function.
- E4d FUBP1 (Supp. Fig. 10c,d): divergent directions across myofibroblast vs T/cDC2; sparse genotype classes.
- E4e RNF14 ieQTL (Fig. 5c,d): reduced with risk allele in inflamed enterocytes; moderate/severe group few donors (~1–5 per genotype).
- Logical assembly: gene-function literature → "impaired renewal". Direction check: MYC ↑ (pro-proliferative Wnt target) is opposite to "impaired renewal"; RASGRP1 ↑ (RasGRP1 restricts epithelial growth, Depeille 2015 cited) consistent; RNF14 ↓ consistent; FUBP1 mixed. No pathway-level statistical test.

### H5 — Effector gene mapping "informs drug prioritisation and safety"
- E5a: ITGA4, JAK2, IL23R as "direct molecular targets of vedolizumab and tofacitinib"; PRKCB (UC, PPH4 0.95) with "inhibitors approved for oncology and already undergoing early-phase clinical trials for IBD"; Methods filter excluded genes already trialled in IBD; NDUFAF1–metformin GI side effects; PSEN2–γ-secretase inhibitor toxicity. Fig. 6 ChEMBL mechanism map without direction of effect.

### H6 — ieQTLs: 1,051 ieQTLs/977 ieGenes; 78.2% inflammation-modulated; 65.6% of those in enterocytes; only 4.2% in LD (r2>0.5) with eQTLs; GSEA "response to metal ion binding"; 2 loci colocalise only with ieQTLs (Supp. Fig. 6; Supp. Mat. S1 Not assessable).

## S2 — Claim Appraisal

### M1.1
- Evidence verdict: Partially supported
- Relation: Non-discriminating
- Comparison/endpoint fit: bins differ in number of annotations (4/30/217), donors, and cells; "distinct eQTL" defined by lead-SNP clumping at r2>0.5.
- Strongest evidence: large absolute number of eQTLs only detected at finer resolution in the same donors.
- Limitation: per-annotation FDR across 251 annotations; lead-variant noise in small annotations inflates clump counts (illustrated by nearby low-LD singletons at MAML2, Supp. Fig. 8).
- Competing explanation: test multiplicity + lead-variant imprecision.
- Would change verdict: per-eGene counts normalised for annotations tested; fine-mapped credible-set overlap across resolutions; replication of cell-type-only eQTLs (cross-site within data or external).
- Verification flag: none (numbers verified against text and figures).

### M1.2
- Evidence verdict: Partially supported
- Relation: Non-discriminating
- Fit: lead-SNP positional/annotation properties; all three metrics move toward random-SNP expectation under lower mapping precision or higher false-positive rate. Fig. 2f ratios all <1 (text phrasing "more enriched in enhancer annotations rather than promoters" overstates; correct statement is "less promoter-biased").
- Statistics: t-tests on 1,000 bootstrap replicates give arbitrarily small p; overlapping 95% intervals for major vs cell-type bins in Fig. 2f.
- Would change verdict: PIP-weighted enrichment on fine-mapped credible sets; stratification/matching by eQTL significance, effect size, MAF, and annotation sample size; absolute (not only ratio) enrichments.

### Literature grounding for M1.1–M1.3
- Established: eQTLs are TSS-proximal and GWAS hits are not; genes near GWAS hits are more constrained and have more complex, cell-type-varying regulatory landscapes; selection hinders discovery of trait-relevant eQTLs (Mostafavi 2023, L1). Limited overlap of immune eQTLs with autoimmune loci (Chun 2017, L5). Cell-type-specific sc-eQTLs colocalise with immune disease loci (Yazar 2022 [ref 18]; Natri 2024 [ref 23]; Soskic 2022 [ref 7]; Nathan 2022 [ref 19]). Many trait-relevant genes lack detectable eQTLs (Connally 2022, L6).
- Manuscript position: extends (to gut + blood at scale, cross-resolution design within the same donors).
- Discrimination: does not yet distinguish biological restriction from power/precision artefact.
- Field standard: fine-mapping-based enrichment, power-matched comparisons, multi-condition shrinkage (L4), multiple-causal-variant coloc (L3).
- Contribution: potentially substantial if robust; the within-donor cross-resolution design is well suited to test Mostafavi's hypothesis.
- Confidence: moderate-high.

### M1.3
- Verdict: Unsupported at the stated level (quantitatively undefined)
- Relation: Indirect
- Fit: gene-level OR vs eQTL-level abstract claim ("eQTLs ... over two-fold more likely"); no CI; reference category unclear; OR 2.68 vs 0.75 would be ~3.6-fold if the comparison is against All-cells.
- Confounders: number of coloc tests per gene; gene properties (constraint, expression level, regulatory complexity per L1); gene density at IBD loci. Supp. Fig. 7 addresses specificity only among colocalised genes, not the relevant comparison.
- Would change verdict: gene-level logistic regression with covariates; permutation null; negative-control traits.

### M2.1
- Verdict: Partially supported
- Relation: Direct for existence of colocalisations; robustness uncertain
- Limitations: coloc.abf single causal variant with multiple eQTL/GWAS signals; PPH4 threshold stated only for ieQTL; several highlighted loci rely on GWAS signals ~1e-6 in the de Lange summary statistics (MAML2, PSEN2 per Figs 4b, S11c); multiple genes appear highlighted at some loci (ITPKB/PSEN2; NDFIP1/RNF14; OIP5/NUSAP1/RTF1/NDUFAF1) – how "single gene" is decided unclear; denominators inconsistent (178 vs 180; 137 vs 138).
- Novelty benchmark limited to OTG colocalisation; ABC-based enhancer–gene maps (Nasser 2021, L7) and a 2024 cell-type-resolved blood/gut eQTL preprint reporting matching eQTL for 140 IBD loci (L8) are relevant comparators. "Nominated for the first time" overstated.
- Would change verdict: coloc-SuSiE sensitivity; prior sensitivity; benchmark vs other resources.

### M2.2
- Verdict: Unsupported at the stated level
- Relation: Non-discriminating / partly contradictory
- The r² metric is conditioned on nominal p<0.05; its floor scales ~1/n; max-r² selection favours annotations with fewest donors (blood-only CD annotations n≤95; rectal/TI DCs). Nominated cell types frequently differ from annotations where coloc was detected (MAML2, ZMIZ1, PSEN2, possibly MYC). Claim "mitigates power-related biases" is not supported: it introduces a different, sample-size-dependent bias.
- Would change: effect-size estimates with SEs and multi-condition shrinkage (mashr, L4); formal heterogeneity/interaction test between candidate annotations; downsampling to equal donors; requirement of coloc support in nominated annotation.
- Literature: Urbut 2019 (L4) for shrinkage-based specificity.

### M3.1–M3.4 (Notch)
- Verdict: Unsupported at the stated level ("implicating reduced Notch signalling"; "support the conclusion that dysregulation of MAML2 ... in cDCs contributes to UC risk")
- Relation: Indirect
- Strongest: high PPH4 at MAML2 and ZMIZ1; biological plausibility: Notch2–RBPJ signalling required for intestinal CD11b+CD103+ cDC2 differentiation in mice (Lewis 2011, L9).
- Gaps: DC attribution rests on M2.2 metric; coloc detected in macrophage and other myeloid annotations (Fig. 4b,c); ZMIZ1 coloc mainly T-cell annotations; PSEN2 coloc in colonocytes, not monocytes/endothelium; mRNA of MAML2 (one of three MAML paralogs) not shown to change Notch target output; mo-DC/cDC2 ambiguity; UC signal sub-genome-wide in plotted data; Discussion wording internally contradictory.
- Established: γ-secretase/Notch inhibition in intestine converts crypt progenitors to goblet cells (van Es 2005, L10) – the canonical GI toxicity mechanism, epithelial rather than immune/vascular.
- Manuscript position: proposes new hypothesis; does not discriminate.
- Would change: trans-effect test (Notch target module score vs genotype in relevant myeloid annotations), pathway enrichment test with matched background, and/or perturbation of the regulatory element/gene in human DCs with Notch readouts; or calibration to hypothesis.

### H4 (Wnt/renewal)
- Verdict: Unsupported at the stated level
- Relation: Indirect; partly contradictory (MYC risk allele ↑)
- Would change: direction-aware pathway test; calibrate abstract.

### H5 (drugs)
- Verdict: Partially supported (descriptive mapping) / Unsupported (safety explanations)
- Factual errors: IL23R not a direct target of an approved IBD drug (approved agents target IL-12/23 p40 or IL-23 p19 ligands — general pharmacology knowledge, not re-verified here beyond tofacitinib label); tofacitinib preferentially inhibits JAK1/JAK3-containing pairs (FDA label, L11); "PRKCB inhibitors approved for oncology" – enzastaurin, the PKCβ-selective inhibitor, not FDA-approved (L12); IBD-trial statement conflicts with Methods filter; γ-secretase GI toxicity attributed to PSEN2 immune/vascular dysregulation contrary to epithelial goblet metaplasia mechanism (L10); metformin–NDUFAF1 explanation speculative (NDUFAF1 is an assembly factor; ChEMBL mapping is complex-level). No direction-of-effect concordance in Fig. 6.

### H6 (ieQTL)
- Verdict: Partially supported
- Concerns: 95.8% not in LD with eQTLs is unusual and consistent with elevated false positives; interaction terms with inflammation (only in CD TI) may capture within-annotation composition shifts; sparse genotype × inflammation cells (Fig. 5d); FDR procedure not described.

### Literature Source Register

| Source ID | Full citation and DOI/PMID/stable URL | Role | Exact proposition supported | Affected H/M/I | Verified |
| --- | --- | --- | --- | --- | --- |
| L1 | Mostafavi H, Spence JP, Naqvi S, Pritchard JK. Systematic differences in discovery of genetic effects on gene expression and complex traits. Nat Genet 55, 1866–1875 (2023). doi:10.1038/s41588-023-01529-1 | foundational/benchmark | eQTLs cluster near TSS whereas GWAS hits do not; genes near GWAS hits are more constrained and have complex, cell-type-varying regulatory landscapes; selection hinders discovery | H1, M1.2, M1.3; I1, I8 | Yes (search abstract) |
| L2 | Yazar S et al. Single-cell eQTL mapping identifies cell type-specific genetic control of autoimmune disease. Science 376, eabf3041 (2022) (ms ref 18) | precedent | cell-type-specific sc-eQTLs colocalise with autoimmune loci | H1 novelty | Cited in ms; not re-fetched |
| L3 | Wallace C. A more accurate method for colocalisation analysis allowing for multiple causal variants. PLoS Genet 17, e1009440 (2021). doi:10.1371/journal.pgen.1009440 | field standard | coloc.abf assumes one causal variant per trait; SuSiE-coloc gives more accurate inference with multiple causal variants | M2.1; I4 | Yes |
| L4 | Urbut SM, Wang G, Carbonetto P, Stephens M. Flexible statistical methods for estimating and testing effects in genomic studies with multiple conditions. Nat Genet 51, 187–195 (2019). doi:10.1038/s41588-018-0268-8 | field standard | multivariate adaptive shrinkage improves effect estimates and quantitative assessment of effect heterogeneity across conditions (applied to eQTLs in 44 tissues) | M2.2; I2 | Yes |
| L5 | Chun S et al. Limited statistical evidence for shared genetic effects of eQTLs and autoimmune-disease-associated loci in three major immune-cell types. Nat Genet 49, 600–605 (2017). doi:10.1038/ng.3795 | consensus/context | only ~25% of autoimmune loci share a single causal effect with immune-cell eQTLs | H1 context | Yes |
| L6 | Connally NJ et al. The missing link between genetic association and regulatory function. eLife 11, e74970 (2022). doi:10.7554/eLife.74970 | context | few variant-to-gene links from expression data despite abundant eQTL data | H1 context | Yes (not cited in report) |
| L7 | Nasser J et al. Genome-wide enhancer maps link risk variants to disease genes. Nature 593, 238–243 (2021). doi:10.1038/s41586-021-03446-x | benchmark/prior nomination | ABC links GWAS signals to genes across 131 cell types; IBD variants enriched in DC enhancers | M2.1 novelty; I4 | Yes (search abstract; volume/pages from memory – verify) |
| L8 | "Integrated cell type-specific analysis of blood and gut identifies matching eQTL for 140 IBD risk loci and entrectinib as possible repurposing candidate." medRxiv 2024, doi:10.1101/2024.10.14.24315443 (Georges/Rahmouni groups; authorship not fully verified) | direct prior work | cell-type-resolved blood (sorted) and gut (scRNA-seq) cis-eQTLs match 140 IBD loci | M2.1 novelty; I4 | Partially (title, date, summary via search; full text 403) |
| L9 | Lewis KL et al. Notch2 receptor signaling controls functional differentiation of dendritic cells in the spleen and intestine. Immunity 35, 780–791 (2011). PMID 22018469 | precedent/plausibility | DC-specific Notch2 deletion reduces DC subsets; Notch2 controls intestinal DC differentiation | H3; I3 | Yes (title/PMID; pages from memory) |
| L10 | van Es JH et al. Notch/γ-secretase inhibition turns proliferative cells in intestinal crypts and adenomas into goblet cells. Nature 435, 959–963 (2005). doi:10.1038/nature03659 | foundational | GSI/RBP-J loss converts crypt progenitors into goblet cells (epithelial mechanism of GI toxicity) | H3, H5; I3, I5 | Yes |
| L11 | XELJANZ (tofacitinib) US prescribing information, Clinical Pharmacology 12.1 (Pfizer/FDA) | authoritative label | tofacitinib preferentially inhibits signalling by JAK1- and/or JAK3-containing pairs with functional selectivity over JAK2 homodimers | H5; I5 | Yes |
| L12 | Enzastaurin – investigational PKCβ inhibitor, not FDA-approved (OncLive/Healio 2020 fast-track news) | factual check | enzastaurin not approved for any indication (as of 2020 reports) | H5; I5 | Yes (secondary sources; approval status as of 2025 assumed unchanged – qualified) |
| L13 | Liu Z et al. Genetic architecture of the inflammatory bowel diseases across East Asian and European ancestries. Nat Genet 55, 796–806 (2023). doi:10.1038/s41588-023-01384-0 | locus definition | 320 IBD loci after meta-analysis | Minor (320 vs 321) | Yes |
| L14 | Ensembl GRCh38 MYC ENSG00000136997, chr8:127,735,434–127,742,951 | reference | MYC position; lead variant chr8:128,528,218 ≈0.79 Mb away | H4 minor | Yes |

### High-Level Roll-Up

#### H1
- Status: Partially supported; headline quantitative claim not yet robust.
- Strongest evidence: large within-donor cross-resolution design; consistent monotonic trends (Fig. 2d–f; Supp. Figs 4–5).
- Weakest bridge: attribution of differences to biology rather than annotation multiplicity, power and lead-variant precision; undefined OR (M1.3).
- Defensible conclusion: eQTLs detected only at finer resolution in this dataset are, on lead-variant metrics, more distal and less promoter-biased, and their genes are over-represented among coloc-nominated genes; whether this reflects cell-type-restricted regulation remains to be shown.
- Remaining overclaim: "masked in bulk analyses"; "over two-fold"; evolutionary model; generalisation to complex disease.
- Literature: extends L1/L2 in a disease tissue; novelty moderate-high if robust.

#### H2
- Status: Partially supported; cell-type assignment unsupported at stated level.
- Defensible: coloc-supported candidate genes at many loci; cell-type labels provisional.

#### H3/H4
- Status: Unsupported at the stated level; hypothesis-generating.

#### H5
- Status: descriptive map acceptable; several factual errors and speculative safety inferences.

#### H6
- Status: Partially supported; robustness uncertain.

## S3 — Issue and Action Ledger

### I1 — Validity-critical
- Affects: H1; M1.1–M1.3; E1.1a–c, E1.2a–c, E1.3a–b
- Location: Fig. 2d–f; Supp. Figs 4, 5, 7, 8; Fig. 3b; Abstract; Discussion paras 2–3; Methods (enrichment, t-tests)
- Problem: resolution bins differ in number of annotations (4/30/217), donors/cells, per-annotation FDR; lead-SNP metrics regress toward random expectation under lower precision; OR in Fig. 3b undefined, no CI, gene-level confounders uncontrolled; Supp. Fig. 7 compares only colocalised genes.
- Consequence: headline principle could be partly or wholly an artefact of detection power and testing multiplicity.
- Required action: (i) power-/multiplicity-matched comparisons (downsampling donors/cells; normalise per annotations tested; stratify by significance/effect size/MAF); (ii) fine-mapped credible sets (e.g., SuSiE) with PIP-weighted annotation and TSS analyses, report absolute enrichments, replace bootstrap t-tests with bootstrap CIs/permutation; (iii) define the OR estimand, give CIs, and fit gene-level model adjusting for number of annotations/coloc tests, expression level and specificity, constraint, and locus features; (iv) evidence that cell-type-only eQTLs replicate (cross-site within data or independent sc-eQTL data).
- Evidence-request role: (i)–(iii) Decisive (reanalysis); (iv) Valid alternative/supporting for (i).
- Precedent: L1 (power/selection), L4.
- Positive/negative: persistence after matching → H1 stands; attenuation → reframe as detection property.
- Fallback: restate H1 descriptively (dataset-specific, power-dependent) – but this would weaken Nature fit (confidential comment).
- Recommended strengthening: negative-control traits (non-immune GWAS) to test disease specificity.
- Status: Drafted (Major 1)

### I2 — Validity-critical
- Affects: H2 (M2.2), H3, H4, H5 locus narratives; Fig. 3c–e; Figs 4c, 5; Supp. Figs 9–11
- Problem: max-r² assignment among nominally significant annotations favours small-n annotations (floor ≈13% at n=30, ≈3.9% at n=100, ≈1% at n=400); nominated cell types often differ from where coloc is detected (MAML2 coloc in several myeloid annotations incl. macrophages CD163++ shown in Fig. 4b; ZMIZ1 coloc largely T cells; PSEN2 coloc in colonocytes while narrative cites monocytes/endothelium at <5% r²); opposite-direction claims (PSEN2, FUBP1, MYC) rest on sparse genotype classes without formal heterogeneity tests.
- Consequence: effector cell-type conclusions (myeloid/DC predominance; DC Notch; stromal vs immune FUBP1; endothelial PSEN2) not reliable.
- Action: effect sizes with SE across all tested annotations, multi-condition shrinkage (mashr) or equivalent; formal tests of effect heterogeneity/sign difference; sensitivity with donor-matched downsampling; restrict effector-cell nomination to annotations with coloc support or report both; report donors and genotype-class counts.
- Role: Decisive (reanalysis). Fallback: label "annotation with largest estimated effect" as exploratory and remove cell-type-specific mechanistic conclusions.
- Status: Drafted (Major 2)

### I3 — Validity-critical (for stated wording) / Venue-critical (mechanistic depth)
- Affects: H3, H4; Abstract; Figs 4–5; Discussion
- Problem: pathway conclusions from single-locus coloc + literature; direction incoherence (MYC ↑ with risk vs "impaired renewal"); MAML2 mRNA as proxy for Notch activity; sub-genome-wide GWAS signals at MAML2/PSEN2 in plotted data; internally contradictory Notch wording; GI toxicity of γ-secretase inhibition is epithelial (L10).
- Consequence: abstract-level mechanistic claims not supported.
- Action: route A (decisive) – functional evidence for at least one axis in relevant human cells (e.g., perturbation of the risk element/gene in DCs or epithelial organoids with pathway-target readouts); route B (existing data, supporting) – genotype-stratified Notch/Wnt target-program scores in the nominated annotations and a direction-aware pathway enrichment test against matched background; route C (fallback) – reframe as hypotheses in title/abstract/Discussion.
- Precedent: L9 (plausibility of Notch in intestinal cDC2), L10.
- Note: route B alone would not establish causality; it tests coherence. Route C resolves validity but reduces Nature-level mechanistic contribution (confidential).
- Status: Drafted (Major 3)

### I4 — Validity-critical (robustness of H2 counts and novelty)
- Affects: M2.1; Fig. 3a; Table 1 (Not assessable); Intro "first time"
- Problem: coloc.abf single-variant assumption despite multiple eQTLs/eGene (Supp. Fig. 4) and multi-signal loci; threshold stated only for ieQTL; no sensitivity to priors; how single effector gene chosen where several genes colocalise (gene tracks highlight ITPKB, NDFIP1, OIP5/NUSAP1/RTF1); denominator inconsistencies (178 vs 180; 137 vs 138); novelty benchmark restricted to OTG colocalisation, omitting ABC maps (L7), cell-type-resolved blood/gut eQTL (L8), and other sc-eQTL resources.
- Action: coloc-SuSiE (L3) or conditional coloc sensitivity; state thresholds; prior sensitivity; per-locus multi-gene reporting; reconcile counts; broaden benchmark or qualify "first time" to "first colocalisation in OTG".
- Role: Decisive (reanalysis) + claim calibration.
- Status: Drafted (Major 4)

### I5 — Validity-critical for section claims (drug/safety) — handled as Major 5 after S5 review; see S5
- Affects: H5; Results "Effector gene mapping informs drug prioritisation and safety"; Fig. 6; Discussion Notch duality
- Problems: IL23R/JAK2/tofacitinib/vedolizumab mapping errors; tofacitinib JAK1/3 (L11); PRKCB approval statement (L12) and conflict with Methods filter; safety explanations (metformin–NDUFAF1; PSEN2–GSI) speculative and, for GSI, contrary to epithelial mechanism (L10); Fig. 6 lacks direction-of-effect concordance; "mixed outcomes of γ-secretase inhibition in clinical trials" – no IBD trials identified; phrasing unsupported.
- Action: correct; add risk-allele direction vs drug mechanism concordance; recast safety as hypotheses.
- Role: Direct correction / claim calibration.
- Status: Drafted (Major 5)

### I6 — Recommended strengthening
- ieQTL robustness: permutation/FDR procedure; within-annotation composition covariates (e.g., cell-state proportions); minimum donors per genotype × level; explain 4.2% LD overlap; Fig. 5d sparse cells.

### I7 — Recommended strengthening
- Evolutionary model: test with gene constraint (e.g., LOEUF) and MAF/effect-size distributions by resolution (L1), or label as speculation.

### I8 — Minor/Recommended
- Cohort structure: blood only CD, rectum only non-IBD, TI mixed; disease status/medication covariates in main eQTL model; site × disease confounding in cross-site and "shared across sites" analyses; European-only; UC colocalisations mapped mostly in non-UC tissue.

### I9 — Minor
- Data/code: summary statistics and Supp. Materials not available at review → key tables Not assessable; request deposit for referees.

### I10 — Minor (consistency and reporting)
- 320 (Intro) vs 321 loci (Results; L13 = 320).
- 180 loci vs 104+74 = 178 and Fig. 3c totals (47/178 = 26.4%).
- 138 (text) vs 137 (Fig. 3a); 104/138 = 75.4% not 75.6%.
- 20,389/24,761 = 82.3% (text 82.2%).
- Abstract "421 individuals" for eQTL mapping vs 397 genotyped individuals.
- Atlasing cells 1,852,681 (Methods) vs 1,837,436 (Supp. Fig. 2 legend); "2,196,874 million cells" typo; "50,0000 reads".
- "three of the four cell types most frequently nominated" vs Fig. 3e (atypical B 10, cDC2 8; cDC1/pDC tie at 5 with several).
- Fig. 4b plots Macrophages CD163++ eQTL while text says cDC2 TI.
- "RPS14" (Discussion) absent from Results.
- "ITGA4, JAK2 and IL23R ... vedolizumab and tofacitinib, respectively".
- Duplicated PRKCB sentence.
- Fig. 2f text "more enriched in enhancer ... rather than promoters" vs ratios <1.
- PPH4 threshold for eQTL coloc not stated (only ieQTL).
- GWAS summary stats (de Lange 2017, European) vs loci from Liu 2023 (multi-ancestry) – denominators.
- LPIN3 Wnt claim reference (ref 43) appears to address CD8 T-cell function in CRC – verify.
- MYC lead variant ≈0.79 Mb from MYC TSS; discuss alternative targets in window (LINC00824 appears in track).
- Model equations missing in text version (may be conversion artefact – ask only to ensure the covariates, including disease status and sample site, are explicit).
- Pathway name "response to metal ion binding" – check GO term.
- "disruption of Notch pathway activity ... may play a protective role" wording.

### Recommendation State
- Central bottleneck: I1 (whether resolution effect survives power/multiplicity/precision controls), then I2 (cell-type attribution).
- Scientific validity: data are valuable; headline claims not yet robust; mechanistic claims hypothesis-level.
- Venue-level adequacy: Nature-level only if H1 is robustly established (and ideally generalises/negative controls) and at least one biological insight is supported beyond coloc; otherwise specialist-journal resource.
- Realistic revisability: I1, I2, I4 are reanalyses of existing data – feasible. I3 route A requires experiments; route C feasible.
- Preliminary recommendation: Major revision.

## S4 — Draft and Verification

- `peer-review.md` drafted: yes
- Major Comments mapped: M1→I1; M2→I2; M3→I3; M4→I4; M5→I5
- Recommended Revisions: I6, I7, I8 (condensed)
- Minor Comments: I9, I10
- Recommendation: Major revision
- Confidential editor comment: yes

### Verification
- Quotes and claim verbs: re-checked against text lines 43 (Abstract), 77 (Intro "first time"), 93 ("masked in bulk analyses"), 121 ("mitigates power-related biases"), 131 ("support the conclusion..."), 133 ("disruption of Notch pathway activity ... protective role"), 151 ("respectively"), 153 (PRKCB), 169 (Discussion Notch duality). Verified.
- Numbers: 84,376; 20,389/24,761; 26,192 (31%); 30,540 (36.2%); 1.9/2.7/3.1 and annotation n 4/30/217 (Supp. Fig. 4); 44/108/200 kb; 38.3/28/20.1%; ORs 2.68/1.57/0.75; 180 loci, 419 genes, 74 new; 104/138; 78 and 29 (37.2%); 47 (26.4%), 34 (19.1%), 32 (18%); ieQTL 1,051/977/764/501/941/44. Arithmetic checked. r² thresholds computed from t critical values (df 28: 2.048; df 98: 1.984; df 398: 1.966).
- Figure references: Fig. 4b right-axis label "Macrophages CD163++" (enlarged crop); Fig. 4c four outlined annotations; Supp. Fig. 11c axis label colonocyte CEACAM7+ KRT20+ IFI27+ and outlined colonocyte-coloured points, max r² ~5%; Supp. Fig. 9a eQTL axis a CD4+ T-cell annotation (label small; described in report as "a T-cell annotation"); Supp. Fig. 10b MYC — reading of which outlined point is the stem-cell annotation is uncertain; report phrased as a request to reconcile rather than an assertion.
- Literature: L1, L3, L4, L7, L9, L10, L11, L12, L13, L14 verified via search; L8 partially (title/date/summary).
- Journal/field-standard assertions: coloc multiple-variant limitation (L3); shrinkage (L4). Nature policy statements kept generic.
- Existing analyses checked: expression-specificity control exists (Supp. Fig. 7) – report acknowledges it and explains why insufficient; bootstrap CIs exist (Fig. 2f); cross-site sharing exists (Fig. 2c) but not as replication of cell-type-only eQTLs; conditional signals mapped (Methods) but coloc input not stated.
- OCR/extraction artifacts: equations missing likely due to conversion – not raised as author error; Table 1 not assessable.
- Unresolved factual questions: exact OR definition; whether coloc used conditional stats; LPIN3 ref content (flagged as "please verify").

## S5 — Final Pruning and Decision

- Draft v1 (S4): ~1,960 words. Final (S5): ~1,750 words incl. headings/markdown.
- Action audit (dispositions):
  - M1: matched-power comparison — Minimum required; fine-mapped PIP-weighted enrichment + interval/permutation inference — Minimum required; defined OR estimand with gene-level covariate model — Minimum required; replication of cell-type-only eQTLs — Recommended (removed from report to reduce length; retained here); negative-control traits — Recommended (retained in dossier only); claim restatement — Claim-calibration fallback (stated).
  - M2: per-annotation effects with SE + shrinkage/heterogeneity tests + counts + coloc-supported nomination — Minimum required (inseparable); "label exploratory, drop cell-type-specific mechanism" — Claim-calibration fallback.
  - M3: functional evidence in relevant human cells — Minimum required route A; reframe as hypotheses — Claim-calibration fallback (resolves validity; venue implication in confidential comment only); genotype-stratified target-programme scores — Supporting characterization, explicitly labelled as not sufficient alone; direction-aware pathway enrichment — Removed from report (duplicative of programme-score coherence check).
  - M4: coloc-SuSiE + prior sensitivity + threshold statement + multi-gene locus rule — Minimum required; broadened benchmark OR restricted wording — alternatives resolving the same inference (novelty claim).
  - M5: factual corrections — Minimum required; direction-of-effect concordance in Fig. 6 — Minimum required for the prioritisation claim; safety as hypotheses — Claim calibration.
  - Recommended Revisions: ieQTL FDR/robustness; evolutionary-model tests; cohort covariates — Recommended.
  - Minor: consistency/reporting — Minimum required corrections (non-major).
- Alternative-route equivalence checked: M3 route A vs route C both resolve the validity of the stated wording; route C does not deliver mechanistic depth — noted to editor. M4 benchmark vs wording restriction both resolve the "first time" claim.
- Duplicates removed: DC mis-attribution appears only in M2 (not repeated in M3 beyond mo-DC ambiguity); drug errors only in M5 (removed "respectively" item from Minor).
- M5 retained as Major (not demoted) because a Results section heading and a Discussion model depend on incorrect premises; kept compact.
- Length justification: five independent validity-critical issues with distinct remedies; no merging without losing consequence/remedy.
- Scientific judgment and recommendation unchanged by pruning: yes.
- Earlier stage reopened: S2/S4 for MYC figure reading (phrased as a reconcile request); Supp. Fig. 9a label re-checked by enlargement (CD4+ memory CXCR6+).

### Final Decision Rationale
- Final recommendation: Major revision
- Claim-validity basis: headline resolution effect and cell-type assignment currently non-discriminating against power/multiplicity artefacts; mechanistic claims hypothesis-level.
- Venue-completeness basis: Nature fit depends on robust H1 plus at least one supported biological insight, or an unusually strong resource framing.
- Principal remaining issues: I1, I2, I3.
- Proportionality: I1, I2, I4, I5 are reanalyses/corrections of existing data; I3 offers a non-experimental calibration route.
- Residual uncertainty: exact OR estimand; contents of Table 1 and Supplementary Materials; whether coloc already used conditional statistics.

## Locked Decisions and Handoff

- Exact wording to preserve: Abstract "over two-fold more likely to colocalise"; "implicating reduced Notch signalling"; "suggesting that impaired renewal contributes to barrier breakdown"; "mitigates power-related biases".
- Inconsistencies to flag: Fig. 4b macrophage vs cDC2; PSEN2 coloc cell type; 178/180; 137/138; 320/321; tofacitinib/IL23R; PRKCB Methods filter.
- Requests intentionally excluded: new cohorts; UC tissue sampling (noted as limitation only); spatial validation.
- Tone: neutral, specific, no "fatal".
- Output paths: ai_review/peer-review.md; ai_review/review-dossier.md
- Next bounded action: none.
