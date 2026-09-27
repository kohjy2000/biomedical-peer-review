# Review Dossier

## Status and Source Set

- Mode: Initial
- Current stage: S5 complete
- Completed stages: S0, S1, S2, S3, S4, S5
- Manuscript version and date: medRxiv preprint v1, "Host control of latent Epstein-Barr virus infection"; reviewed as an initial submission to Nature, submission date 2025-07-16.
- Source set reviewed: `blind/preprint_v1_text.md` (full text, Methods, figure legends, reference list); `blind/figures/F1–F4.jpg` (main Figures 1–4); `blind/figures/F5–F8.jpg` (Extended Data Figures 1–4). One crop of F7 panel c was magnified to verify an axis label.
- Sources intentionally excluded: Supplementary Information (Supplementary Figures, Supplementary Notes, Supplementary Tables S1–S22, supplementary xlsx) — not provided. Any later version of this preprint, its published version, peer-review file or companion work. A concurrent independent preprint on the same phenotype posted after the submission date (see run-notes.md) was deliberately not read or used.
- Literature cutoff date: 2025-07-16 (all cited grounding literature published before this date).
- Last verified: numbers, panel references and arithmetic re-checked against the text and figure images at S4.
- Next bounded action: none; review delivered.
- Dossier confidentiality note: confidential working record. Not for transmission to authors or editors.

## S0 — Review Calibration

- Journal and submission stage: Nature, initial submission (Article).
- Article/study type: population-scale human genetics / biobank observational study with a new sequencing-derived phenotype; combines phenotype derivation, epidemiological association, GWAS (common and rare variant), functional annotation, polygenic score analysis, PheWAS and two-sample Mendelian randomization. Genre calibration: primarily **clinical cohort / computational-methods hybrid**, with no experimental perturbation component.
- Central question and intended contribution: what host factors control Epstein-Barr virus (EBV) during persistent infection? The intended contribution is (i) establishing EBV short reads recovered as a by-product of human genome sequencing (GS) as a surrogate for EBV viral load, (ii) a first well-powered GWAS of that phenotype, and (iii) linking the resulting genetic architecture to EBV-associated diseases, including possible causal effects.
- Design, data, population/model, setting: UK Biobank (UKB) GS data, n=490,294 initial, n=486,315 after QC; All of Us (AoU), n=365,931 initial, n=336,123 after QC. Discovery GWAS restricted to UKB individuals of European genetic ancestry without HIV/immunosuppressive medication (56,180 EBVread+ vs 304,103 EBVread−). Replication in the AoU European subgroup (n=184,949 per Extended Data Fig. 3c). Blood-derived DNA; PCR-free Illumina NovaSeq 6000 WGS aligned with DRAGEN to a GRCh38 graph genome containing the chrEBV contig.
- Primary claim ambition and intended scope: high. The abstract moves from read detection → "increased viral load" → host genetic control of **latent** infection → polygenic overlap with autoimmune disease → "potential causal effects" on RA and T1D → a general method for studying persistent viral infection from human GS by-products.
- Editor question, review fields, recommendation options: not provided. Default fields used (Overall Assessment, Major Comments, Recommended Revisions, Minor Comments, Recommendation, Confidential Comment to Editor).

### Relevant Review Requirements

| Requirement or expectation | Provenance | Basis or source | Consequence for this review |
| --- | --- | --- | --- |
| A new biomarker presented as a surrogate for a quantitative biological measure requires benchmarking against an orthogonal quantitative assay, or an explicit technical-error model that is not fitted to the data it explains | Field standard | General measurement-validation practice in biomarker/genomics studies; the manuscript's own simulation (Extended Data Fig. 1) is stated in the legend to have parameters "manually fitted to match the observed read count distribution" | Drives I1; determines whether "viral load" language is admissible |
| Index hopping/sample-index swapping on patterned Illumina flow cells generates low-level cross-sample read misassignment | Field standard | Costello et al., BMC Genomics 19:332 (2018), doi:10.1186/s12864-018-4703-0 | Supports requesting lane/plate-level technical bounds for a phenotype where 61.9% of "positives" carry exactly one read |
| MR requires instruments free of horizontal pleiotropy; the MHC is commonly excluded because of extensive LD and pervasive pleiotropy with immune-mediated disease | Field standard | Standard MR practice (Burgess & Thompson, Eur J Epidemiol 2017; Verbanck et al., Nat Genet 2018 — both cited by the manuscript as refs 83–84) | Drives I2; a causal claim resting on MHC instruments is not interpretable |
| HLA-DRB1*04:04 is a shared-epitope RA risk allele and sits on the DR4–DQ8 background associated with T1D | Field standard | Raychaudhuri et al., Nat Genet 44:291 (2012) (manuscript ref 25); DR4-DQ8 T1D/RA literature | Makes the RA/T1D MR and GRS results directly vulnerable to pleiotropy |
| MR estimates for a binary exposure that dichotomizes an underlying continuum are not interpretable as per-unit effects of that exposure | Field standard | Burgess & Labrecque, Eur J Epidemiol 33:947 (2018), doi:10.1007/s10654-018-0424-6 | Drives the ORwMed interpretation element of I2 |
| Nature requires that GWAS summary statistics and analysis code supporting the conclusions be available | Journal-stated (editorial policy) | Nature reporting/availability policies for genomics papers | Drives I5 (venue-critical) |
| Anti-EBNA-1 IgG is the canonical HLA class II-associated EBV humoral trait | Field standard | Hammer et al., Am J Hum Genet 97:738 (2015), PMC4667104 | Used to interpret the Extended Data Fig. 2 pattern (correlation with lytic-antigen antibodies, not EBNA-1) |
| Effect-size correlation against an external immune-cell GWAS is only informative if that GWAS is adequately powered | Field standard | Orrù et al., Nat Genet 52:1036 (2020): 731 immune traits in n=3,757 Sardinians (manuscript ref 30) | Drives I3 |

- Claim-validity bar: for the GWAS itself (EBVread+ as a binary sequencing-derived trait), association results are valid if QC, covariate control, relatedness and replication are sound — this bar appears largely met. For the "viral load" claim, an orthogonal quantitative anchor or a technical-noise model not fitted to the observed distribution is required. For the causal claims, MR instruments must survive removal of pleiotropic MHC variants.
- Venue-completeness bar: Nature requires that the biological payload — not just the resource — be established. Here that means (i) the phenotype is credibly viral load rather than a sequencing artefact composite, (ii) the disease links are distinguishable from generic HLA pleiotropy, and (iii) full data/code availability.
- Feasibility/material constraints stated in the manuscript: no access to biospecimens for qPCR is stated or implied; the authors work entirely within the UKB RAP and AoU Workbench. Requests were calibrated accordingly (in-silico routes preferred).
- Assumptions not made: no assumption that the authors can perform qPCR, obtain new samples, or access non-released AoU fields.
- Calibration uncertainty: all Supplementary material is unavailable, so several verification items (Supplementary Tables S4–S22, Supplementary Figs 1–10, Supplementary Notes) are marked Not assessable. In particular, the Methods state that MR was repeated excluding MHC SNPs, and the result may be in Supplementary Table S22 / Supplementary Notes; the main text does not report it.

## S1 — Structured Claim–Evidence Map

### H1 — "we report the identification of genetic and non-genetic factors that contribute to latent EBV infection control"; EBV reads from GS are "a robust surrogate measure for increased EBV viral load"

- Verb strength and claim level: strong ("robust surrogate measure", "demonstrated"); measurement-validation claim plus biological-interpretation claim.
- Intended scope: general adult populations of two biobanks; extended in the final paragraph to "other human pathogens".
- Claimed novelty: "our study is the first to demonstrate that GS-based EBV reads can be used as proxies for elevated EBV viral load, with high specificity".

#### M1.1 — EBV-read detection is specific for prior EBV infection

- Role in H1: establishes that reads are genuine EBV signal, not noise.
- Evidence type: validation (against serology).

##### E1.1a — Fig. 1d, serology subcohort

- Location: Fig. 1d; Results "Detection of EBV-reads".
- Actual comparison: EBVread+/− vs EBVsero+/− in n=9,281 UKB participants with serology (491 sero−, 8,790 sero+).
- Unit / time point / endpoint: individual; single baseline blood draw; specificity 99.4% (488/491), sensitivity 16.4% (1,440/8,790). Arithmetic verified.
- Authors' intended inference: read detection is a highly specific marker of EBV infection.
- Internal limitation: 3/491 seronegative individuals are EBVread+ (0.6%), consistent with a low but non-zero technical false-positive floor; 83.6% of seropositive individuals are read-negative.

#### M1.2 — EBVread+ status reflects elevated EBV viral load

- Role in H1: converts a binary detection variable into a quantitative biological trait; every downstream biological and causal interpretation depends on it.
- Evidence type: simulation.

##### E1.2a — Extended Data Fig. 1, log-normal simulation

- Location: Extended Data Fig. 1a–d; Results paragraph 2.
- Actual comparison: simulated viral loads (log-normal, shape borrowed from HIV-1 set-point viral load, ref 24) → binomial read sampling at ~4×10⁸ trials → simulated read-count distribution compared with the observed distribution (Fig. 1c).
- Endpoint: visual/parametric compatibility of simulated and observed read-count distributions.
- Authors' intended inference: because a log-normal viral load reproduces the observed zero-inflated read distribution, read count approximates viral load.
- Internal limitation: the legend states that "the success rate of the binomial distribution as well as the parameters of the log-normal distribution ... were manually fitted to match the observed read count distribution in our data". The simulation is therefore fitted to the quantity it is used to explain and is not a discriminating test.

##### E1.2b — Fig. 2b, within-positive GWAS effect-size concordance

- Location: Fig. 2b.
- Actual comparison: effect sizes from the main EBVread+ GWAS vs a GWAS of read count = 1 (n=35,703) vs ≥2 (n=20,477); Spearman r=0.93 (non-MHC), r=0.94 (HLA).
- Authors' intended inference: the phenotype is dose-like, therefore load-like.
- Internal limitation: the two analyses share cases and the same read-generation process; concordance shows internal consistency of a monotone read-count trait, not calibration to viral copies. Any technical determinant of read yield would produce the same concordance.

##### E1.2c — Fig. 1g, sequencing yield covariate

- Location: Fig. 1g (top right).
- Actual comparison: marginal prevalence of EBVread+ across GS yield (Gb).
- Endpoint: prevalence rises from ≈0.1 to ≈0.45 across the observed yield range — the largest covariate effect shown in Fig. 1e–g apart from HIV.
- Role here: internal counter-evidence for M1.2; read detection is strongly depth-dependent, as expected for a detection threshold, and is adjusted for but not decomposed.

- Logical assembly of H1: specificity (M1.1) + dose-concordance (E1.2b) + fitted simulation (E1.2a) are assembled into "surrogate for viral load".
- Missing bridge: no measurement of EBV DNA by an independent quantitative assay in any subset, and no technical-noise model estimated independently of the observed data.

### H2 — Non-genetic factors (HIV, immunosuppressive drugs, current smoking, age, sex, lymphocyte %, season) influence EBVread+

#### M2.1 — Immunosuppression raises EBVread+ prevalence

- E2.1a — Fig. 1e: no-outlier cohort (n=313,387 non-related; 48,771 EBVread+, 15.6%). Reported HIV 39.7% (s.d. 3.5%), glucocorticoids 19.4% (0.7%), other immunosuppressants 18.3% (0.5%) vs 15.6% baseline. Marginal standardization with 1,000 bootstraps. Direct and biologically expected.

#### M2.2 — Current, but not former, smoking increases EBVread+

- E2.2a — Fig. 1f: 22.1% (s.d. 0.3%) in current smokers vs 14.7% (0.1%) in current non-smokers, in the no-immune-supp cohort. Former smoking not retained by BIC-based selection.
- Internal limitation acknowledged by the authors: current smoking increases memory B-cell counts (ref 49), an alternative explanation for a B-cell-reservoir-derived read signal.

#### M2.3 — Season (winter) increases EBVread+

- E2.3a — Fig. 1g (bottom right): proportion with EBV reads vs date of assessment-centre attendance, spline-modelled; stated to replicate in AoU (Supplementary Fig. 2, Not assessable).
- Limitation: sampling date in UKB is correlated with assessment centre, sample handling and, critically, with library-preparation plate (51 plates were excluded for excess EBVread+ prevalence). Seasonality and processing batch are not orthogonal in this design.

### H3 — EBVread+ is a polygenic trait with a dominant MHC contribution and 27 replicated non-MHC loci implicating specific EBV-control biology

#### M3.1 — 28 genome-wide significant loci; extended MHC signal resolved to 54 independent HLA alleles

- E3.1a — Fig. 2a Manhattan (56,180 cases / 304,103 controls; sum 360,283 = 360,764 minus 481 individuals lacking imputed data — verified consistent). 27 non-MHC labelled loci counted in the figure, matching the text.
- E3.1b — 116 associated HLA alleles reduced to 54 independent by iterative conditional analysis; lowest P for HLA-DRB1*04:04 (beta=0.79, s.e.m.=0.02); HLA-A*02:01 (beta=−0.31) and HLA-B*14:02 (beta=−0.68) protective.
- E3.1c — AoU European replication: 98/106 matched HLA alleles nominally significant with consistent direction (77 genome-wide significant); 25/27 non-MHC lead variants at P<0.05.
- Limitation: replication thresholds are nominal; HLA alleles are imputed by different algorithms in the two cohorts (HLA*IMP:02 in UKB; HLA-TAPAS with a 1000G phase 3 panel, n=2,504, in AoU), and 12/178 alleles could not be mapped.

#### M3.2 — The associated loci are specific to EBV control rather than to lymphocyte biology or herpesviruses generally

- E3.2a — Fig. 2d, HHV-7 read-positivity comparison: HLA alleles r=−0.02 (P=0.877); non-MHC loci r=0.37 (P=0.061), six loci at P<0.05 with consistent direction, two colocalizing (SLC8A1, PTPN22; PP(H4)>0.5).
- E3.2b — Extended Data Fig. 2e, memory B-cell abundance GWAS (Orrù 2020, n=3,757): non-MHC r=0.34 (P=0.112); no MHC data available; one shared locus (13q33.3 TNFSF13B).
- Authors' inference: "These findings suggest that the genetic associations with EBVread+ represent specific factors associated with EBV viral load during latency. They do not seem to be confounded by memory B cell abundance, with the exception of the TNFSF13B locus".
- Internal counter-evidence: both comparisons are nulls with n=27 points; the HHV-7 comparison in fact trends positive; TNFRSF13B (TACI) emerges as the only non-MHC rare-variant gene, and TNFSF13B (BAFF) as a shared locus — both B-cell-survival genes.

#### M3.3 — Prioritized genes and pathways implicate antigen presentation and CD8+ T/NK effector biology

- E3.3a — Fig. 3a: ERAP2 haplotype structure; rs2927608 G tags NMD haplotypes B/C, reduced ERAP2 expression, higher EBVread+ prevalence. Coherent and mechanistically interpretable.
- E3.3b — Fig. 3b: 30 Bonferroni-significant GOBP terms, all T/lymphocyte activation-related.
- E3.3c — Fig. 3c: GTEx tissue enrichment (spleen, whole blood, EBV-transformed lymphocytes, lung, terminal ileum).
- E3.3d — Fig. 3d–g: scDRS on 1M-scBloodNL PBMCs (37,033 cells, 8 level-1 types); CD8+ T and NK significant (FDR<0.05).
- Limitation: circularity risk in E3.3c (the GTEx "EBV-transformed lymphocytes" tissue is an LCL panel); all enrichments derive from the same MAGMA gene ranking, so they are not independent lines of evidence.

#### M3.4 — Common- and rare-variant convergence nominates novel host-control genes (CD226, PTPN22, GP1BA, C6orf222, ZNF284, CHD4, HKR1)

- E3.4a — MAGMA: 63 Bonferroni-significant genes; IEI gene set (n=456) enriched, P=4.66×10⁻⁶, beta=0.19 (s.e.m. 0.04); 14-gene monogenic-EBV subset beta=0.35 (s.e.m. 0.22), P=0.055.
- E3.4b — RVAS (SKAT-O, MAF<1%, n=54,259 EBVread+/293,834 EBVread−): 29 genes with a test-wide significant mask, 28 of them within the MHC; the only non-MHC gene, TNFRSF13B, is driven entirely by p.Cys104Arg (P=0.087 when the variant is removed).
- E3.4c — Overlap of MAGMA and RVAS at P<0.01 (non-MHC): 24 genes, 7 with LoF-driven rare-variant enrichment, described as "strong novel candidate genes".
- Limitation: no formal test of excess overlap; the P<0.01 × P<0.01 intersection across ~19,000 genes has a non-trivial chance expectation, and the "further increased" effect size in E3.4a is a non-significant comparison of two overlapping estimates (0.19±0.04 vs 0.35±0.22).

### H4 — The polygenic architecture of EBVread+ overlaps EBV-associated diseases and is causally related to RA and T1D

#### M4.1 — HLA-based GRS predicts EBVread+ and transfers across ancestries

- E4.1a — Fig. 4b: HLA_all ΔR²(Nagelkerke)=0.079 ± 0.009 in the UKB serology cohort (n=6,065 in the panel label).
- E4.1b — Fig. 4e / Extended Data Fig. 3c: eur AoU ΔR²=0.072 (s.d. 0.002; n=184,949); afr 0.055; amr 0.065; eas ≈0.015; mid very large with an error bar spanning the panel (n=1,245); sas ≈0.04 (n=4,544).
- Limitation: "largest improvements ... in each of the five non-European ancestry groups" rests on n=1,245 (mid) and n=7,927 (eas) subgroups; Discussion's "largely equal contribution of MHC class I and MHC class II" is not what Fig. 4b / Extended Data Fig. 3c show (class II ΔR² ≈0.045–0.047 vs class I ≈0.031).

#### M4.2 — Disease cohorts show class-specific GRS elevation (MS: MHC I; RA: MHC II)

- E4.2a — Fig. 4f: MS n=1,637, RA n=8,093 vs serology control n=6,065. MS HLA_MHC I P=1.06×10⁻⁴, reduced to P=0.056 when HLA-A*02:01 is removed. RA HLA_MHC II association not abolished by removing HLA-DRB1*04:04. NHL shows lower HLA_all.
- Authors' inference: distinct dysregulation of EBV-specific immunity in RA, and a mechanistic hypothesis for MS.
- Internal counter-evidence: the MS result is carried by a single allele that is itself an established MS-protective allele (ref 26); the RA result is carried by class II alleles whose shared-epitope members are the dominant RA risk alleles (ref 25).

#### M4.3 — PheWAS nominates T1D, IBD and hypothyroidism as new EBV-related diseases

- E4.3a — Fig. 4g: AoU European PheWAS, 1,751 PheCodes × 4 GRS. T1D beta=0.176 (HLA_MHC II); IBD beta=−0.135 (HLA_all) and −0.112 (HLA_MHC II); hypothyroidism beta=−0.039 (HLA_MHC I) and +0.037 (SNP_wo_MHC).
- Limitation: opposite-signed and negative betas are reported without interpretation; a negative coefficient means the EBV-control-risk score is associated with *lower* disease odds, which does not fit a simple "higher EBV load → disease" model. Hypothyroidism has discordant signs across two GRS.

#### M4.4 — MR suggests causal effects of EBVread+ on RA and T1D

- E4.4a — Results/Extended Data Fig. 4: RA OR(wMed)=1.21 (95% CI 1.09–1.35); T1D OR(wMed)=1.86 (1.64–2.10); MS null; the text states "significant heterogeneity of effects was observed across SNPs, and the causal effects for these outcomes were driven by SNPs in the MHC region".
- Methods state that analyses were repeated excluding MHC SNPs for associations with evidence for causality; no result of that sensitivity analysis appears in the main text (possibly in Supplementary Table S22 / Supplementary Notes — Not assessable).
- Extended Data Fig. 4 forest plots show MHC SNPs (purple) among the largest-effect instruments for both RA and T1D.
- Bridge assumption: EBVread+ instruments affect disease only through EBV load. Given that the top instrument set is dominated by HLA alleles with established direct effects on RA (shared epitope) and T1D (DR4–DQ8), this assumption is not defensible as stated.

## S2 — Claim Appraisal

### M1.1 (read detection is specific for EBV infection)

- Evidence verdict: Supported.
- Claim–evidence relation: Direct.
- Comparison/endpoint fit: serology is an appropriate orthogonal anchor for *infection status*; specificity 99.4% is a fair readout.
- Strongest supporting evidence: Fig. 1d, with uniform EBV genome coverage (Fig. 1b) arguing against a mismapping artefact concentrated in a few regions.
- Material limitation: sensitivity 16.4% means the trait captures only the upper tail; 3 seronegative positives set a false-positive floor of ~0.6%, which is large relative to a phenotype in which 61.9% of positives have exactly one read.
- Verification flag: resolved (arithmetic recomputed from Fig. 1d counts).

### M1.2 (EBVread+ reflects elevated viral load) — central claim

- Evidence verdict: **Partially supported**; unsupported at the stated level ("robust surrogate measure for increased EBV viral load").
- Claim–evidence relation: **Non-discriminating.** The simulation (E1.2a) was fitted to the observed distribution; the within-positive concordance (E1.2b) shares the read-generation process; neither separates biological load from technical read yield.
- Comparison/endpoint fit: no EBV copy-number measurement exists anywhere in the manuscript. The endpoint is a detection indicator whose probability is jointly determined by viral copies, DNA input, sequencing depth, duplicate rate, alignment filters and cross-sample index swapping.
- Logical gap / competing explanation: a composite technical-plus-biological detection variable would reproduce every reported property — zero inflation, dose-concordance, depth dependence, plate-level excess (51 plates excluded), season/date structure.
- Scope limit: even under the authors' interpretation, the trait ranks only the top ~16% of a distribution whose lower 84% is censored.
- Evidence that would change the verdict: qPCR/ddPCR in any subset; or a technical model estimated independently (down-sampling, within-flow-cell/lane analysis of read sharing, re-sequenced duplicate concordance), showing that residual variance after technical adjustment is individual-specific and stable.
- Verification flag: the "manually fitted" wording is quoted verbatim from the Extended Data Fig. 1b legend; verified.

### Literature Grounding for M1.2

- Exact proposition: "GS-derived EBV read positivity is a robust surrogate measure of elevated EBV viral load in blood."
- Established knowledge: EBV DNA is recoverable from blood WGS by-products (Moustafa et al., PLoS Pathog 2017 — 14% of 8,000 individuals; manuscript ref 23), and virome-from-WGS analyses can support disease association (Sasa et al., Nat Genet 57:65, 2025 — manuscript ref 43, eHHV-6 and anellovirus in 6,321 Japanese genomes).
- Consensus/governing standard: EBV load in clinical and research settings is quantified by qPCR of whole blood or PBMC (manuscript ref 18, Kanakry et al., Blood 2016).
- Prior evidence consistent: read-detection prevalence (16.2%/21.8%) is of the same order as Moustafa's 14% and Kanakry's 11.03% qPCR positivity, as the authors note.
- Prior evidence inconsistent: none identified; the issue is absence of calibration, not contradiction.
- Genuine controversy: none. Possible source of disagreement would be technical (platform, depth, index swapping) rather than biological.
- Manuscript position: **extends** prior virome-from-WGS work to biobank scale; the "first to demonstrate proxy for elevated viral load" phrasing goes beyond what is shown.
- Field-standard evidence package: an orthogonal quantitative anchor in a subset, or a technical-noise decomposition; neither is present.
- Directly relevant precedent and limitation: Costello et al., BMC Genomics 19:332 (2018) documents index swapping on patterned flow cells (HiSeqX/4000/NovaSeq), the exact platform class used here; its limitation is that swap rates are library- and site-specific and must be estimated in the data at hand.
- Genuine contribution: substantial — scale (822k individuals), QC discipline, and the first well-powered genetic analysis of this trait.
- Literature-dependent judgment and confidence: high confidence that the "viral load" framing exceeds the evidence; moderate confidence that technical variance is material rather than negligible (the plate exclusions and yield effect are supportive but not decisive).

### M2.1–M2.3 (non-genetic factors)

- M2.1: **Supported**, Direct. Effect sizes are large, biologically expected, and bootstrapped.
- M2.2: **Partially supported**, Indirect. The current/former contrast is interesting but the memory-B-cell alternative is acknowledged and not excluded; smoking also affects DNA yield and lymphocyte composition.
- M2.3: **Partially supported**, Non-discriminating. Assessment date is entangled with processing batch and with the plate-level artefact that motivated excluding 51 plates. Claimed AoU replication is Not assessable (Supplementary Fig. 2).
- Verification flag: prevalence figures recomputed (48,771/313,387 = 15.56%); consistent.

### M3.1 (loci discovery and replication)

- Evidence verdict: **Supported**.
- Claim–evidence relation: Direct.
- Strongest evidence: regenie with SPA, relatedness handling, 18 selected covariates plus 20 PCs, cross-biobank replication, and an explicit re-run of the MHC without SPA to escape the P-value plateau at −log₁₀P = 306.653. This is careful work.
- Material limitation: replication declared at nominal P<0.05 across 27 loci and 106 HLA alleles; HLA imputation differs between cohorts; AoU could not include blood-count covariates.
- Scope: European ancestry only for discovery and for the reported replication.
- Verification: case/control sums reconcile with Fig. 1a minus the 481 individuals lacking imputed data.

### M3.2 (specificity of loci to EBV control)

- Evidence verdict: **Unsupported at the stated level.**
- Claim–evidence relation: Non-discriminating (both arms are underpowered nulls, and one trends against the claim).
- Comparison/endpoint fit: the HHV-7 comparison actually yields r=0.37 (P=0.061) with 6/27 loci nominally concordant and two colocalizing — evidence *for* partial sharing, presented as evidence of specificity. The memory-B-cell arm uses Orrù 2020 (n=3,757), where the standard errors of the external betas are large enough that r≈0.34 with P=0.112 is uninformative in either direction; MHC was not testable at all.
- Logical gap: absence of evidence treated as evidence of absence, twice.
- Evidence that would change the verdict: power calculation for the effect-size correlation given the external GWAS standard errors; conditioning the EBVread+ GWAS on measured lymphocyte and (where available) B-cell parameters; formal enrichment testing of the HHV-7 concordance against a matched null.

### Literature Grounding for M3.2

- Exact proposition: "the genetic associations with EBVread+ ... do not seem to be confounded by memory B cell abundance."
- Established knowledge: EBV persists in memory B cells (refs 4, 6); total blood EBV DNA is the product of infected-cell number and per-cell copy number. TNFSF13B/BAFF and TNFRSF13B/TACI are core determinants of B-cell survival (ref 31, Müller-Winkler et al., J Exp Med 2021; ref 37, Salzer & Grimbacher 2021).
- Prior evidence consistent with the authors' position: the strong MHC class I signal and CD8/NK scDRS enrichment are hard to explain by B-cell abundance alone.
- Prior evidence inconsistent: the two B-cell-axis genes that do emerge (TNFSF13B locus; TNFRSF13B p.Cys104Arg as the sole non-MHC RVAS hit) are exactly what a reservoir-size contribution would predict.
- Manuscript position: **confirms** a T-cell-centric model for the MHC signal; does not **discriminate** load-per-cell from reservoir-size for the non-MHC signal.
- Field-standard package: conditioning on directly measured cell-composition covariates, plus a powered comparison against an immune-cell-trait GWAS.

### M3.3 (pathways, tissues, cell types)

- Evidence verdict: **Supported** as hypothesis-generating; Indirect.
- Material limitation: GOBP, GTEx and scDRS all derive from one MAGMA gene ranking and are not independent corroboration. GTEx "EBV-transformed lymphocytes" is an LCL panel; its appearance among top tissues is not independent biological evidence about EBV control in vivo.
- Scope: fine-grained level-2 NKbright signal rests on a small cluster, which the authors state.

### M3.4 (novel candidate genes)

- Evidence verdict: **Partially supported.**
- Claim–evidence relation: Indirect. CD226 has a coherent biological rationale (refs 53–54), but "strong novel candidate genes for host control of latent EBV-infection" is an assertion about a P<0.01 ∩ P<0.01 intersection with no excess-overlap statistic.
- Logical gap: the IEI effect-size statement ("the effect size further increased", beta 0.35 ± 0.22, P=0.055) compares two overlapping estimates without testing the difference, and the Discussion then converts it to "with a higher effect size for IEIs that lead to a loss of EBV-control".
- Evidence that would change the verdict: a permutation or matched-null test for the size of the MAGMA∩RVAS overlap, and a formal contrast (or joint model) for the two IEI gene sets.

### M4.1 (GRS performance and transferability)

- Evidence verdict: **Supported** for European and, more weakly, African/Admixed American groups; **Partially supported** for East Asian, Middle Eastern and South Asian groups.
- Limitation: n=1,245 (mid) and n=7,927 (eas) cannot support "largest improvements ... in each of the five non-European ancestry groups" as a robust statement; the mid AoU estimate in Fig. 4e exceeds the panel's axis with a correspondingly wide interval.
- Verification: eur AoU n verified as 184,949 by magnifying Extended Data Fig. 3c; main text states 184,948.

### M4.2 / M4.3 / M4.4 (disease overlap and causality) — second central claim branch

- Evidence verdict for M4.2: **Partially supported** (the associations are real) but **Non-discriminating** for the intended interpretation (EBV-specific immune dysregulation).
- Evidence verdict for M4.3: **Partially supported**; the associations are statistically convincing at biobank scale, but the direction of several is opposite to the stated interpretation and is left unaddressed.
- Evidence verdict for M4.4: **Unsupported at the stated level.**
- Comparison/endpoint fit: the exposure GWAS is dominated by HLA; the instrument set for RA/T1D therefore consists largely of variants with direct, well-established effects on those diseases. This violates the exclusion restriction rather than merely inflating heterogeneity. The manuscript itself reports both significant instrument heterogeneity and MHC-driven effects.
- Logical gaps: (i) association of an HLA-derived score with an HLA-driven disease is expected under pure pleiotropy; (ii) a binary exposure that dichotomizes a latent continuum yields MR estimates that are not interpretable as per-unit effects (Burgess & Labrecque 2018), so ORwMed = 1.86 for T1D has no defined scale; (iii) reverse causation cannot be excluded for hypothyroidism/T1D/IBD in the PheWAS framing but is less of an issue for genetic instruments than pleiotropy.
- Evidence that would change the verdict: MR restricted to non-MHC instruments (Methods say this was run); GRS-disease analyses conditioned on the established HLA risk alleles for each disease, or restricted to non-MHC SNP scores; and an explicit statement of the direction of each PheWAS beta.

### Literature Grounding for M4.4

- Exact proposition: "Mendelian randomization analyses suggested potential causal effects of EBVread+ on RA and T1D."
- Established knowledge: HLA-DRB1 shared-epitope alleles including DRB1*04:04 are the dominant genetic risk factors for seropositive RA (ref 25, Raychaudhuri et al. 2012); the DR4–DQ8 haplotype background is the principal class II risk haplotype for T1D. HLA-A*02:01 is MS-protective (ref 26).
- Current consensus/standard: the MHC is routinely excluded from MR instrument sets because of long-range LD and pervasive pleiotropy with immune-mediated disease; MR-Egger/PRESSO adjust for average pleiotropy but not for instruments acting directly on the outcome through the same molecule.
- Prior evidence consistent with causality for EBV in disease: Bjornevik et al., Science 375:296 (2022) (ref 10) establishes EBV infection as a prerequisite for MS — yet the present MR is null for MS, i.e. the one outcome with the strongest external causal evidence.
- Prior evidence inconsistent/competing model: shared HLA pleiotropy (HLA alleles independently shape both EBV control and autoimmunity) predicts exactly the reported pattern without any causal path through viral load.
- Genuine controversy: whether EBV load is causal for autoimmunity beyond MS is genuinely open; this manuscript does not discriminate.
- Manuscript position claimed: discriminates (causal). Position supported: compatible with two models.
- Field-standard package: non-MHC instrument MR; multivariable MR conditioning on the relevant HLA risk alleles; or colocalization at non-MHC loci.
- Directly relevant precedent and limitation: MR of infection-related exposures on autoimmune outcomes routinely founders on HLA pleiotropy; the standard remedy is instrument restriction, at the cost of power (here, non-MHC SNP-based GRS explains far less of EBVread+ — Fig. 4b, SNP_wo_MHC ΔR² ≈ 0.005 — so the non-MHC MR may be weak-instrument limited, which must then be stated).

### Literature Source Register

| Source ID | Full citation | Role | Exact proposition supported | Affected H/M/I | Verified |
| --- | --- | --- | --- | --- | --- |
| L1 | Costello M. et al. Characterization and remediation of sample index swaps by non-redundant dual indexing on massively parallel sequencing platforms. BMC Genomics 19:332 (2018). doi:10.1186/s12864-018-4703-0 | Precedent / benchmark | Index swapping causes low-level cross-sample read misassignment on patterned Illumina flow cells (HiSeqX/4000/NovaSeq) | M1.2, I1 | Yes (title, journal, year, DOI verified) |
| L2 | Burgess S. & Labrecque J.A. Mendelian randomization with a binary exposure variable: interpretation and presentation of causal estimates. Eur J Epidemiol 33:947–952 (2018). doi:10.1007/s10654-018-0424-6 | Consensus / standard | MR estimates for a binary exposure that dichotomizes an underlying continuum are not interpretable as per-unit causal effects of that exposure | M4.4, I2 | Yes |
| L3 | Raychaudhuri S. et al. Five amino acids in three HLA proteins explain most of the association between MHC and seropositive rheumatoid arthritis. Nat Genet 44:291–296 (2012) (manuscript ref 25) | Foundational | HLA-DRB1 shared-epitope alleles, including DRB1*04:04, are the dominant MHC risk factors for seropositive RA | M4.2, M4.4, I2 | Yes (cited by the manuscript itself for this allele) |
| L4 | Moutsianas L. et al. Class II HLA interactions modulate genetic risk for multiple sclerosis. Nat Genet 47:1107–1113 (2015) (manuscript ref 26) | Foundational | HLA-A*02:01 reduces MS risk; DRB1*15:01 is the major MS risk allele | M4.2, I2 | Yes |
| L5 | Orrù V. et al. Complex genetic signatures in immune cells underlie autoimmunity and inform therapy. Nat Genet 52:1036–1045 (2020) (manuscript ref 30) | Benchmark | The memory-B-cell abundance GWAS used for the confounding check comprises 731 immune traits in n=3,757 Sardinians | M3.2, I3 | Yes (n and design verified) |
| L6 | Hammer C. et al. Amino acid variation in HLA class II proteins is a major determinant of humoral response to common viruses. Am J Hum Genet 97:738–743 (2015). PMC4667104 | Supporting | Anti-EBNA-1 IgG is strongly determined by HLA-DRβ1 positions 11 and 26 | Extended Data Fig. 2 interpretation; Minor 9 | Yes |
| L7 | Moustafa A. et al. The blood DNA virome in 8,000 humans. PLoS Pathog 13:e1006292 (2017) (manuscript ref 23) | Supporting | EBV DNA is detectable in ~14% of blood WGS datasets | M1.1 novelty framing | Yes (14% verified) |
| L8 | Sasa N. et al. Blood DNA virome associates with autoimmune diseases and COVID-19. Nat Genet 57:65–79 (2025) (manuscript ref 43) | Recent update | WGS-derived blood virome traits (eHHV-6, anellovirus) can be associated with autoimmune disease in 6,321 Japanese genomes | Novelty positioning for H1 | Yes |
| L9 | Bjornevik K. et al. Longitudinal analysis reveals high prevalence of EBV associated with multiple sclerosis. Science 375:296–301 (2022) (manuscript ref 10) | Foundational | EBV infection is a near-prerequisite for MS | M4.4 internal-consistency argument (MR null for MS) | Yes |

### High-Level Roll-Up

#### H1 (EBV reads as a viral-load surrogate)

- Status at the stated level: not supported as "a robust surrogate measure for increased EBV viral load"; supported as "a specific but insensitive indicator of detectable blood EBV DNA that behaves monotonically".
- Strongest evidence: Fig. 1d specificity plus uniform genome coverage (Fig. 1b).
- Weakest bridge: M1.2 — the fitted simulation.
- Defensible conclusion: GS by-product reads identify individuals with unusually high blood EBV DNA content, with a specificity near 99% against serology, and the trait behaves as an ordered variable.
- Remaining overclaim: "viral load", "latent", and "first to demonstrate ... proxies for elevated EBV viral load".
- Literature position and novelty: genuine extension of refs 23 and 43 to biobank scale; the methodological generalization to other pathogens in the final paragraph is speculative and should be conditional.

#### H2 (non-genetic factors)

- Status: largely supported; season and smoking require confound separation.
- Weakest bridge: M2.3, because sampling date and processing batch are entangled in UKB.

#### H3 (genetic architecture)

- Status at the stated level: the association results are supported and well executed; the **specificity** framing (M3.2) and the **novel-candidate-gene** framing (M3.4) are not.
- Strongest evidence: Fig. 2a/2b with cross-biobank replication; the ERAP2 haplotype analysis (Fig. 3a).
- Defensible conclusion: EBVread+ has a strongly MHC-dominated polygenic architecture with 27 replicable non-MHC loci enriched for antigen-presentation and T/NK effector genes.
- Remaining overclaim: "specific factors associated with EBV viral load during latency"; "strong novel candidate genes".

#### H4 (disease overlap and causality)

- Status at the stated level: not supported. Both the GRS-disease and MR results are compatible with shared HLA pleiotropy.
- Strongest evidence: the RA class I/class II directional dissociation (Fig. 4f), which is the one pattern that a pure pleiotropy model does not obviously predict and is worth preserving.
- Weakest bridge: M4.4.
- Defensible conclusion: the HLA determinants of EBV read positivity overlap those of MS, RA, T1D, IBD and hypothyroidism, with class-specific directional structure; this is hypothesis-generating about shared antigen-presentation biology.
- Remaining overclaim: "Mendelian randomization analyses suggested potential causal effects of EBVread+ on RA and T1D"; "EBV viral load might be a causal factor" for T1D.

## S3 — Issue and Action Ledger

### I1 — Validity-critical

- Affects: H1, M1.2, E1.2a–c; propagates to every downstream "viral load" statement including the title, abstract and Discussion.
- Location: Abstract ("The detection of EBV-reads (EBVread+) reflected increased viral load"); Results paragraph 2; Extended Data Fig. 1 and its legend; Discussion paragraph 1.
- Problem: the only evidence offered that read positivity indexes viral load is a simulation whose parameters were, per the legend, manually fitted to reproduce the observed read distribution, plus a within-phenotype effect-size concordance that shares the read-generation process. Sequencing yield is one of the strongest covariates of read detection (Fig. 1g) and 51 library-preparation plates had to be removed for excess positivity.
- Consequence: the trait may be a composite of viral DNA content and sample/run-level technical read yield; "viral load" cannot be asserted, and any biological interpretation inherits the ambiguity.
- Required action: provide an orthogonal quantitative anchor or a technical-variance decomposition estimated independently of the observed distribution.
- Purpose: establish that the measured endpoint tracks EBV copies rather than detection propensity.
- Evidence-request role: Decisive — orthogonal EBV DNA quantification (qPCR/ddPCR) in any subset, or comparison with an independently deep-sequenced subset. Valid alternative — an in-silico technical package: uniform-depth down-sampling, estimation of within-flow-cell/lane read sharing to bound index swapping (L1), and concordance of EBVread+ across any re-sequenced or duplicated samples. Claim-calibration fallback — retitle the phenotype as "detectable blood EBV DNA (EBV-read positivity)" and remove "viral load" from the title, abstract and conclusions.
- Target inference and precedent: L1 establishes the specific artefact class for this platform; the in-silico route is feasible entirely within the UKB RAP/AoU Workbench.
- Main confounder/limitation of the requested route: down-sampling reduces power and cannot bound contamination by itself, which is why the lane-sharing analysis is part of the same route.
- Effect of outcomes: a positive orthogonal correlation licenses "viral load" throughout; a null or depth-dominated result forces the fallback wording but leaves the GWAS intact.
- Status: Drafted (Major 1).

### I2 — Validity-critical

- Affects: H4, M4.2, M4.4; E4.2a, E4.4a.
- Location: Abstract (final two sentences); Results "Two-Sample Mendelian Randomization"; Results paragraph on Fig. 4f; Discussion paragraph 4; Extended Data Fig. 4.
- Problem: the exposure GWAS is MHC-dominated, so the MR instrument set and the best-performing GRS are largely HLA alleles with established direct effects on the outcome diseases (HLA-DRB1*04:04 for RA, DR4–DQ8 class II for T1D, HLA-A*02:01 for MS). The manuscript states that the RA and T1D causal effects were driven by MHC SNPs and that instrument heterogeneity was significant.
- Consequence: the exclusion restriction fails; the reported causal effects and the "polygenic overlap" interpretation are equally consistent with shared HLA pleiotropy. The binary exposure also leaves ORwMed = 1.86 without a defined scale (L2).
- Required action: report, in the main text, the MR restricted to non-MHC instruments (the Methods state this analysis was performed) and the GRS-disease associations conditioned on the established HLA risk alleles for each disease or restricted to non-MHC scores; state instrument strength for the restricted analysis.
- Evidence-request role: Decisive (existing-data reanalysis). Claim-calibration fallback: if the non-MHC analyses are null or weak-instrument limited, replace causal language throughout with shared-genetic-architecture language and state that pleiotropy cannot be excluded.
- Effect of outcomes: a surviving non-MHC effect would substantially strengthen the paper's headline; a null would still leave a valuable descriptive overlap result.
- Status: Drafted (Major 2).

### I3 — Validity-critical

- Affects: H3, M3.2; E3.2a, E3.2b.
- Location: Results, end of "Identification of common genetic variants" ("These findings suggest ... specific factors ... They do not seem to be confounded by memory B cell abundance"); Fig. 2d; Extended Data Fig. 2e.
- Problem: specificity is inferred from two non-significant comparisons across 27 points, one of which (HHV-7, r=0.37, P=0.061, six concordant loci, two colocalizing) trends toward sharing, and the other of which uses an external GWAS of n=3,757 (L5) with no MHC data.
- Consequence: the claim that the loci are EBV-specific host-control factors rather than determinants of lymphocyte/B-cell compartment size or general herpesvirus control is not established; TNFSF13B and TNFRSF13B point directly to the reservoir-size alternative.
- Required action: state the power of each comparison given the external standard errors, and provide a sensitivity GWAS conditioned on measured blood-cell parameters; reword the specificity claim to what the data support, explicitly noting the positive HHV-7 trend and the colocalizing loci.
- Evidence-request role: Decisive is not available without cell-sorted data; the requested route is existing-data reanalysis plus claim calibration.
- Status: Drafted (Major 3).

### I4 — Venue-critical

- Affects: H3, M3.4; E3.4a, E3.4c.
- Location: Results "Gene-based analyses..." final paragraph ("24 genes had complementary evidence ... representing strong novel candidate genes"); IEI enrichment sentence (beta=0.35; s.e.m.=0.22, P=0.055); Discussion ("with a higher effect size for IEIs that lead to a loss of EBV-control").
- Problem: the intersection of two gene lists at P<0.01 is presented without a chance expectation or excess-overlap test, and a non-significant gene-set result is described as an increased effect.
- Consequence: the paper's claim to nominate new IEI/host-control genes — a main biological selling point for this venue — is not statistically supported as stated.
- Required action: provide a permutation or matched-null test for the overlap, and either a formal contrast between the two IEI gene sets or explicit acknowledgement that P=0.055 does not support a difference.
- Evidence-request role: Decisive (existing-data reanalysis). Claim-calibration fallback: describe CD226 and the other six genes as candidates requiring functional follow-up.
- Status: Drafted (Major 4).

### I5 — Venue-critical

- Affects: reproducibility of all genetic claims.
- Location: Data availability and Code availability statements.
- Problem: EBVread+ and HHV-7read+ GWAS summary statistics are not stated to be deposited anywhere; code is limited to the read-extraction commands in Supplementary Note 1, with all other analyses described only by software names and versions.
- Consequence: the central resource cannot be reused or independently checked, which does not meet the availability expectations for a genomics Article at this journal.
- Required action: deposit the full summary statistics (common-variant, HLA-allele, rare-variant gene-level, and HHV-7) in a public repository such as the GWAS Catalog, and release analysis code.
- Evidence-request role: Decisive; no alternative.
- Status: Drafted (Major 5).

### I6 — Recommended strengthening

- Affects: H3, M3.1 scope; H4, M4.1.
- Problem: discovery and the reported replication are European-only, although AoU contributes n=64,927 (African) and n=60,854 (Admixed American) individuals who are used only for GRS transferability.
- Required action: a trans-ancestry meta-analysis or at least ancestry-stratified association results for the 27 non-MHC loci and the HLA alleles.
- Evidence-request role: Recommended (not required for the stated European-scoped claims).
- Status: Drafted (Recommended Revisions).

### I7 — Recommended strengthening

- Affects: M1.2/H1 interpretation and the title's "latent".
- Problem: Extended Data Fig. 2 shows effect-size correlation with antibodies against lytic-cycle antigens (p18 VCA r=0.64, P=1.55×10⁻⁵; ZEBRA r=0.45, P=3.68×10⁻³) but not against EBNA-1 (r=−0.08, P=0.623) — a pattern with a concrete interpretation (L6), given that anti-EBNA-1 is the canonical HLA class II-determined EBV antibody trait.
- Required action: interpret this pattern and justify "latent" in the title, or use a neutral term.
- Evidence-request role: Recommended / claim calibration.
- Status: Drafted (Recommended Revisions, and Minor 9 for the text–figure inconsistency).

### Minor issue set (I8–I19)

| ID | Location | Problem | Action |
| --- | --- | --- | --- |
| I8 | Methods "Identification of high-quality EBV-reads" vs Results and Fig. 1a | n=490,293 vs n=490,294 | Reconcile |
| I9 | Results, non-genetic factors | 47,234 + 257,899 = 305,133, but the cohort is given as n=305,123 | Reconcile (10-individual discrepancy) |
| I10 | Results (serology cohort n=9,281) vs Fig. 4b/4f (n=6,065) vs Extended Data Fig. 3a (n=6,531) | Three different serology-cohort sizes without a stated derivation | State the filtering steps |
| I11 | Results, AoU replication (n=184,948) vs Extended Data Fig. 3c (n=184,949) | Off-by-one | Reconcile |
| I12 | Results, scDRS (level 2 "21 cell types") vs Methods ("level 2: 26 cell types") | Inconsistent | Reconcile |
| I13 | Fig. 2a labels 5q31.1 as IRF1; Methods fine-mapping calls the same locus 5q31.1_SLC22A5; Results cite an SLC22A5 eQTL | Inconsistent locus naming | Harmonize |
| I14 | Results, fine-mapping | "credible sets of variants (CS; posterior inclusion probability (PIP) >95%)" conflates cumulative CS coverage (defined correctly in Methods) with per-variant PIP | Reword |
| I15 | Results, PheWAS | "beta = -0,039" decimal comma; negative betas for IBD and hypothyroidism, and opposite signs across HLA_MHC I and SNP_wo_MHC for hypothyroidism, are not interpreted | Fix and interpret direction |
| I16 | Results, AoU replication | Replication declared at nominal P<0.05 for 27 loci and 106 HLA alleles | Report multiplicity-adjusted replication and directional concordance |
| I17 | Discussion ("largely equal contribution of MHC class I and MHC class II") vs Fig. 4b and Extended Data Fig. 3c (class II ΔR² ≈0.045–0.047 vs class I ≈0.031) | Overstated equality | Reword |
| I18 | Methods, HLA imputation (HLA*IMP:02 in UKB vs HLA-TAPAS with a 1000G n=2,504 panel in AoU; 166/178 alleles mapped) | Cross-cohort comparability of allele calls not quantified | Report imputation accuracy/concordance |
| I19 | Methods, 2SMR | All outcome GWAS exclude UKB except the "red hair colour" negative control, which includes UKB | State whether overlap affects the negative control |
| I20 | Throughout | Typographical: "Herefore" (twice), "performet", "EBVseron-egative", "EBVread-controls", "honorario" | Copy-edit |

### Recommendation State

- Central bottleneck: the phenotype is asserted to be viral load without an independent anchor (I1), and the two headline biological outputs — disease overlap and causality — cannot be separated from HLA pleiotropy (I2).
- Scientific validity: the association analyses are valid and carefully executed; the measurement-interpretation and causal layers are not.
- Venue-level adequacy: the resource and GWAS are of Nature scale; the biological payload as currently supported is not, primarily because the causal claim is the novelty and it is currently uninterpretable.
- Realistic revisability: high for I2, I3, I4, I5 (all existing-data reanalysis or deposition); moderate for I1 (the decisive route needs biospecimens the authors do not claim to have, but the in-silico alternative is feasible).
- Preliminary recommendation: Major revision, with an explicit conditional to the editor that if the non-MHC MR is null and no orthogonal viral-load anchor can be provided, the remaining contribution is a strong but more specialist genetics resource.

## S4 — Draft and Verification

- `peer-review.md` drafted: yes.
- Major Comments mapped to issue IDs: Major 1 = I1; Major 2 = I2; Major 3 = I3; Major 4 = I4; Major 5 = I5.
- Recommended Revisions drafted: I6, I7.
- Minor Comments drafted: I8–I20 (pruned to the highest-value items at S5).
- Recommendation drafted: yes (Major revision).
- Confidential editor comment drafted: yes.

### Verification

- Quotes and claim verbs: all quoted phrases re-checked against `preprint_v1_text.md` — "robust surrogate measure for increased EBV viral load"; "manually fitted to match the observed read count distribution"; "These findings suggest that the genetic associations with EBVread+ represent specific factors associated with EBV viral load during latency"; "do not seem to be confounded by memory B cell abundance"; "representing strong novel candidate genes for host control of latent EBV-infection"; "the causal effects for these outcomes were driven by SNPs in the MHC region"; "largely equal"; "the effect size further increased". Verified verbatim.
- Numbers, denominators, sample sizes: 78,771/486,315 = 16.20% ✓; 48,771/313,387 = 15.56% ✓; 1,440/8,790 = 16.38% ✓; 488/491 = 99.39% ✓; 35,703 + 20,477 = 56,180 ✓; 56,180 + 304,103 = 360,283 = 360,764 − 481 ✓; 47,234 + 257,899 = 305,133 ≠ 305,123 ✗ (raised as Minor); 491 + 8,790 = 9,281 ✓.
- Figure, panel and section references: Fig. 1b–g, 2a–d, 3a–g, 4a–g and Extended Data Figs 1–4 inspected as images; the 27 non-MHC locus labels in Fig. 2a were counted (28 labels including the MHC) and match the text; Extended Data Fig. 3c axis labels magnified to confirm eur AoU n=184,949 and the ancestry-group sizes; Fig. 4b bar heights used for the ΔR² class I/class II comparison.
- Literature propositions and citation metadata: L1–L9 verified by search for title, journal, year and, where used, the specific numeric proposition (Moustafa 14%; Orrù n=3,757/731 traits; Hammer DRβ1 positions 11 and 26).
- Journal or field-standard assertions: the MHC-exclusion norm in MR and the binary-exposure interpretation caveat were anchored to L2 and standard practice rather than asserted; the Nature availability expectation is stated as journal policy and framed as such in the review.
- Manuscript/response consistency: not applicable (initial submission).
- Existing analyses checked: the Methods state that MR was repeated excluding MHC SNPs and that colocalization was run for HHV-7; Major 2 therefore asks for these to be *reported in the main text* rather than newly performed. A memory-B-cell comparison and an HHV-7 comparison already exist; Major 3 asks for power quantification and a cell-composition sensitivity analysis, not for a repetition of the existing comparison.
- OCR/extraction artefacts checked: the text file is a JATS conversion; spacing artefacts ("EBVread-controls", "EBVseron-egative", "sero-positive") were checked against surrounding context and are reported as copy-editing items with that caveat, not as substantive errors. Numeric discrepancies were only raised where both values appear cleanly in the converted text or in a figure image.
- Unresolved factual questions: all Supplementary Tables and Figures (S1–S22, Supplementary Figs 1–10, Supplementary Notes) are unavailable. Judgments that depend on them are marked Not assessable: the content of the non-MHC MR sensitivity analysis (Supplementary Table S22), the AoU seasonality replication (Supplementary Fig. 2), the covariate list (Supplementary Table S3), the plate-level QC (Supplementary Fig. 1), fine-mapping and colocalization detail (Supplementary Tables S4, S9, S13), and the PheWAS/2SMR tables (S20–S22).

## S5 — Final Pruning and Decision

- Requested actions classified: I1 decisive/alternative/fallback triple retained as alternatives, not as a cumulative list; I2, I3, I4, I5 minimum-required (all existing-data reanalysis or deposition); I6, I7 moved to Recommended Revisions; I8–I20 pruned to ten Minor Comments, dropping I18 and I19 into a single consolidated line and merging the typographical items.
- Minimum required routes retained: one per Major Comment.
- Recommended strengthening moved: yes, to a separate section.
- Alternative-route equivalence checked: for I1, the orthogonal-quantification route and the in-silico technical-decomposition route both resolve the same inference (is the endpoint viral DNA content or detection propensity?); the wording fallback does not resolve it and is presented explicitly as a claim-calibration option, not as an equivalent.
- Duplicated requests removed: the "MHC pleiotropy" argument appeared in both the GRS and MR comments and was consolidated into Major 2; a separate comment on ancestry restriction was demoted to Recommended Revisions because the authors scope their claims to European ancestry and state the limitation.
- Final word count and Major Comment count: 5 Major Comments, 2 Recommended Revisions, 10 Minor Comments. Author-facing body (Overall Assessment through Minor Comments) = 1,392 words; 1,661 words including the Recommendation and the Confidential Comment to Editor. This exceeds the 1,200-word guidance in `style-profile.md`, which permits the excess when independent validity- or venue-critical issues cannot be combined without losing their distinct consequences or remedies. Three validity-critical issues (I1 phenotype calibration, I2 HLA pleiotropy, I3 locus specificity) and two venue-critical issues (I4 statistical support for gene nomination, I5 data and code availability) have distinct remedies and were not merged. One merge was performed: the GRS-overlap and MR issues share the HLA-pleiotropy consequence and were consolidated into Major 2. A first draft ran to 1,828 words and was compressed by ~170 words in the reviewer-facing body without removing any requested action.
- Scientific judgment and recommendation unchanged by pruning: yes.
- Earlier stage reopened: no.

### Final Decision Rationale

- Final recommendation: **Major revision** (substantial revision required before reconsideration).
- Claim-validity basis: the association analyses (H3) are valid; the measurement claim (H1/M1.2) and the causal claim (H4/M4.4) are not supported at their stated level, but both are addressable — the causal claim by reporting an analysis the Methods say was already run, and the measurement claim by an in-silico technical decomposition or orthogonal quantification.
- Venue-completeness basis: scale, QC discipline and cross-biobank replication meet the bar; the biological payload does not until I2 is resolved, and availability (I5) must be fixed regardless.
- Principal remaining issues: I1 (phenotype interpretation), I2 (HLA pleiotropy in the causal and overlap claims).
- Why the requested actions are proportionate: four of the five Major Comments require only reanalysis of data already in hand or deposition of existing results; no new sample collection or experiment is demanded, consistent with the authors' stated constraint of working within two biobank computing platforms.
- Residual uncertainty: the Supplementary Information may already contain the non-MHC MR sensitivity analysis and parts of the technical QC; if so, Majors 2 and part of 1 reduce to relocation and reframing rather than new work. This is stated conditionally in the review and flagged to the editor.

## Locked Decisions and Handoff

- Exact wording that must be preserved in the review: the quoted phrase "manually fitted to match the observed read count distribution" (Extended Data Fig. 1b legend), because it is the load-bearing basis of Major 1.
- Inconsistencies that must be flagged: the 305,133 vs 305,123 arithmetic; the three serology-cohort sizes (9,281 / 6,531 / 6,065); the Extended Data Fig. 2 antibody correlations described in the text as only "suggestive".
- Requests intentionally excluded: new qPCR as a *required* action (no evidence the authors have biospecimen access); single-cell or sorted-cell experiments; a demand for non-European discovery GWAS as a validity condition.
- Tone and style requirement: Nature-style initial review; English; claim-focused; no internal identifiers exposed.
- Output paths: `.../prcase/B/ai_review/peer-review.md` and `.../prcase/B/ai_review/review-dossier.md`.
- Next bounded action: none; review complete.
