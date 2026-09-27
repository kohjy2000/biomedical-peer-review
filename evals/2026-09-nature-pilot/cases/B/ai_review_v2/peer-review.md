# Referee Report — Nature (initial submission)

Manuscript: "Host control of latent Epstein-Barr virus infection"

## Overall Assessment

The authors use EBV reads recovered from blood genome sequencing in UK Biobank (n=486,315) and All of Us (n=336,123) as a population-scale phenotype, "EBVread+". They map its non-genetic correlates, its genetic architecture (54 HLA alleles and 27 non-MHC loci, largely replicated in All of Us) and its overlap with EBV-associated diseases. The resource is original, the GWAS is large and replicated, and a genetic map of persistent EBV DNA in blood would be of broad interest. The central problem is that every interpretation depends on EBVread+ measuring viral load. This has not been validated against a quantitative measure, and it has not been separated from B-cell content or sequencing artefact. The disease and Mendelian randomization results are also interpreted beyond what HLA pleiotropy allows. These problems appear revisable.

## Major Comments

**1. EBVread+ has not been validated as a measure of viral load.**
The manuscript states that EBV-read detection "is a robust surrogate measure for increased EBV viral load", with "high specificity". None of the supporting evidence tests this directly:
- The 99.4% specificity (Fig. 1d) is specificity for seropositivity. It indicates prior infection, not load.
- The simulation (Extended Data Fig. 1) was fitted by hand to the observed count distribution. It therefore shows compatibility, not measurement.
- The 1-read versus ≥2-read GWAS (Fig. 2b) would show the same dose-response for any continuous determinant of read count.

Artefact has also not been excluded. Most EBVread+ individuals (61.9%) carry a single read. Contamination QC was done per library-preparation plate, not per sequencing lane. Index misassignment on patterned flow cells occurs at about 0.1% even with dual indexing (Costello et al., BMC Genomics 2018), so a sample with thousands of reads could seed single-read calls in lane-mates.

Please:
- benchmark read counts against quantitative EBV DNA (qPCR or ddPCR, ideally calibrated to the WHO international standard) in any samples with matched blood genome sequencing;
- test whether single-read positives cluster by lane with high-count samples.

If quantitative validation is not obtainable, please describe the trait as detectable EBV DNA and remove the "robust surrogate" and "first … with high specificity" wording.

**2. B-cell abundance may explain part of the phenotype and the loci.**
EBV persists in memory B cells, so the chance of sampling an EBV genome from buffy-coat DNA scales with the sample's B-cell fraction. EBVread+ prevalence rises steeply with lymphocyte percentage (Fig. 1g, about 0.08 to 0.27). Lymphocyte percentage, however, mostly reflects T cells. The memory B-cell comparison (Extended Data Fig. 2e; r=0.34, P=0.11; no HLA data) rests on a GWAS of 3,757 individuals and cannot exclude confounding. Several loci regulate B-cell homeostasis (TNFSF13B, TNFRSF13B, BCL3, IKZF3), and smoking changes memory B-cell numbers, as the authors note.

Please estimate the B-cell fraction from IGH rearrangement in the same WGS data (e.g., ImmuneLENS; Bentham et al., Nat. Genet. 2025). Then re-estimate the non-genetic effects, lead-variant effects and HLA-allele effects conditional on it. Loci that this adjustment explains should not be described as determinants of EBV control.

**3. The disease and causal claims do not account for HLA pleiotropy.**
The alleles that drive the GRS are established disease-risk alleles:
- HLA-DRB1*04:04, the top allele, is an RA shared-epitope allele and belongs to the high-risk DR4 group for T1D;
- HLA-A*02:01 protects against MS. Removing it abolishes the MS association (P=1.06×10⁻⁴ to 0.056).

The associations in Fig. 4f–g are therefore expected whether or not EBV load contributes. The MR estimates for RA (OR 1.21) and T1D (OR 1.86) are heterogeneous and "driven by SNPs in the MHC region". This is the pattern of an exclusion-restriction violation. Despite this, the Abstract reports "potential causal effects", and the Discussion says EBV viral load "might be a causal factor" in T1D.

Please:
- report in the main text the MR results without MHC instruments, and the non-MHC GRS/PheWAS results;
- test whether the HLA-GRS associations survive conditioning on each disease's established risk alleles;
- interpret the binary-exposure estimates on the liability scale (Burgess & Labrecque, Eur. J. Epidemiol. 2018).

Without non-MHC support, please present these results as shared HLA architecture that generates hypotheses, and remove the causal language.

## Recommended Revisions

1. **Serology.** Extended Data Fig. 2b–c shows HLA concordance with VCA p18 (r=0.64, P=1.6×10⁻⁵) and ZEBRA (r=0.45) antibody effects. DRB1*04:04 is a known HLA association for these antibodies in UK Biobank (Kachuri et al., Genome Med. 2020). Please revise the statement that serology shows "only weak" correlation, and report the power of the Fig. 4d null, which is based on few seronegative individuals.
2. **Smoking.** "Current, but not former, smoking" rests on former smoking not being selected in stepwise selection. Please give never/former/current estimates with confidence intervals.
3. **HLA signals.** Please report HLA imputation accuracy. Please also support the count of "54 independent" alleles with conditional analysis at the amino-acid or haplotype level.
4. **Candidate genes.** "Strong novel candidate genes" (e.g., CD226) rests on overlap at P<0.01 between two analyses. The EBV-specific IEI enrichment has P=0.055. Please moderate this wording.

## Minor Comments

1. **Data and code.** Please deposit the GWAS, HLA and rare-variant summary statistics publicly rather than making them available "upon reasonable request". Please also release the analysis code, not only the read-extraction commands.
2. **Serology cohort size.** Please reconcile the three sizes given: n=9,281 (Fig. 1d), n=6,531 (Extended Data Fig. 3a; Fig. 4c groups) and n=6,065 (Fig. 4b,f).
3. **Heritability.** Please state the scale of the 2.04% SNP heritability.
4. **MS in the MR results.** Extended Data Fig. 4 lists MS as significant with ≥2 estimators, but the main text reports no evidence for MS. Please reconcile.
5. **RA and MHC class I.** The Discussion claim about MHC class I in RA rests on P<0.1 (Fig. 4f). Please moderate it.
6. **All of Us comparability.** Please state the effect of the missing blood-count covariates in All of Us, and of the 12 unmapped HLA alleles (11 of them class II), on replication and GRS transfer.
7. **Corrections.**
   - Fig. 2 legend: "presented in c" should read b.
   - Extended Data Fig. 3d refers to Fig. 4f, which should be 4g.
   - Fig. 4a legend has "(i) … (i)".
   - "HLA-A*2:01" should read HLA-A*02:01.
   - The Extended Data Fig. 4 key reads "Weighted mean", whereas the Methods say weighted mode.
   - The Fig. 4e "mid" bar is clipped.
   - Reference 40 does not describe 1M-scBloodNL (Oelen et al., Nat. Commun. 2022).
   - References 4 and 6 are duplicates.
   - The cohort is n=490,294 in one place and 490,293 in another.
   - Level-2 cell types are given as 26 in one place and 21 in another.

## Recommendation

Major revision. The associations are robust. The interpretation as viral-load control, and the causal disease claims, need the validation, B-cell adjustment and pleiotropy analyses described above. These are achievable within a revision.

## Confidential Comment to Editor

This is a large, well-executed analysis of a new phenotype. My reservation concerns construct validity, not the robustness of the GWAS. Comments 2 and 3 can be answered with existing data. Comment 1 ideally needs a modest external qPCR-plus-sequencing benchmark. If the authors can only reframe the trait as "detectable EBV DNA" and must withdraw the causal disease claims, the paper becomes mainly a replicated genetic map of a novel trait. Whether that alone reaches Nature's threshold is borderline and an editorial call. I could not assess the Supplementary material, which may partly address the QC and MR-sensitivity points.
