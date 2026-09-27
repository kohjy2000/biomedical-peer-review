# Review Dossier (confidential; not for authors or editor)

## Status and Source Set

- Mode: Initial review (blind evaluation run)
- Current stage: S5 complete
- Completed stages: S0, S1, S2, S3, S4, S5
- Manuscript version and date: medRxiv v1 full text (JATS-derived `preprint_v1_text.md`), treated as a Nature initial submission dated 2025-07-16. Title as given in source: "Host control of latent Epstein-Barr virus infection".
- Source set reviewed: `blind/preprint_v1_text.md` (all 318 lines: abstract, introduction, results, discussion, figure legends, methods, data/code availability, references); `blind/figures/F1.jpg`–`F4.jpg` (main Figs 1–4), `F5.jpg`–`F8.jpg` (Extended Data Figs 1–4), all inspected visually.
- Sources intentionally excluded: Supplementary Figures, Notes and Tables S1–S22 (not retrievable) → dependent judgments marked Not assessable. `preprint_v1.xml` not separately read (text file is derived from it). No later version, published article, peer-review file or news item opened.
- Literature cutoff date: 2025-07-15 (publications before the 2025-07-16 submission date).
- Last verified: 2026-09-26 (run date)
- Next bounded action: none (delivered)
- Dossier confidentiality or storage note: stored locally in `B/ai_review_v2/` only.

## S0 — Review Calibration

- Journal and submission stage: Nature, initial submission.
- Article/study type: Population-scale human genetic epidemiology / discovery genetics (biobank GWAS + rare-variant burden + HLA + GRS/PheWAS + two-sample MR), using a new phenotype derived as a by-product of blood genome sequencing.
- Central question and intended contribution: What genetic and non-genetic factors govern host control of latent EBV infection? The authors propose that EBV reads in blood GS data (EBVread+) are a proxy for elevated EBV viral load, then map its determinants and its overlap with EBV-associated diseases.
- Design, data, population/model, and setting: UKB GS (n=486,315 after QC) and AoU GS (n=336,123 after QC); cross-sectional; single blood draw; European-ancestry GWAS (56,180 cases/304,103 controls), AoU European replication (n=184,948), HLA imputation (HLA*IMP:02 in UKB; HLA-TAPAS in AoU), exome RVAS (54,259/293,834), GRS in UKB disease cohorts and AoU PheWAS, 2SMR with external outcome GWAS.
- Primary claim ambition and intended scope: (i) method claim — GS-derived EBV reads are "a robust surrogate measure for increased EBV viral load"; (ii) discovery claim — MHC (54 independent HLA alleles) + 27 non-MHC loci govern latent EBV control; (iii) biology claim — CD8+ T/NK and IEI genes implicated, novel IEI candidates; (iv) disease claim — polygenic overlap with MS, RA, T1D, IBD, hypothyroidism and "potential causal effects" on RA and T1D.
- Editor question, review fields, and recommendation options: none provided. Reviewer calibration: used the commonly requested Nature referee content (key results, validity, significance, data/methodology, suggested improvements, references, clarity); recommendation options assumed Accept / Minor / Major revision / Reject (nature.com guidance not fetched to preserve blinding — see run-notes).

### Relevant Review Requirements

| Requirement or expectation | Provenance | Basis or source | Consequence for this review |
| --- | --- | --- | --- |
| A new biomarker/phenotype used as a proxy for viral load should be benchmarked against a standard quantitative measure | Field standard | Quantitative NAT (qPCR) is the reference method, standardized by the WHO 1st International Standard for EBV (Fryer et al. 2016, L7); manuscript itself names qPCR as the method needed (Discussion, limitations) | Drives I1 |
| Cross-sample contamination / index misassignment must be excluded when a trait is defined by very low read counts | Field standard | Index swapping on patterned flow cells incl. NovaSeq; ~0.13% contamination even with dual indexes (Costello et al. 2018, L3) | Drives I1 (contamination arm) |
| Cell-composition confounding must be handled for blood-derived molecular traits | Field standard / Reviewer calibration | Same design precedent (Gupta et al. 2023, ref 60) adjusts for blood composition; B-cell fraction estimable from blood WGS via IGH (Bentham et al. 2025, L2) | Drives I2 |
| MR instruments must satisfy exclusion restriction; heterogeneous, locus-driven estimates, especially from pleiotropic loci, should not be interpreted causally | Field standard | Burgess et al. 2023 MR guidelines (L4); binary-exposure interpretation (Burgess & Labrecque 2018, L5) | Drives I3 |
| GWAS summary statistics and analysis code publicly available | Reviewer calibration (consistent with Nature Portfolio data policy; not fetched) | — | Minor comment M-data |
| Nature: broad significance, conceptual advance | Reviewer calibration | — | Venue-completeness bar |

- Claim-validity bar: For the phenotype claim, orthogonal quantitative evidence that EBVread+ tracks EBV DNA load (not only EBV exposure, B-cell abundance, depth or contamination). For the genetic loci, standard GWAS QC + replication (largely met). For disease claims, association claims require control of HLA pleiotropy; causal claims require MR robust to MHC pleiotropy.
- Venue-completeness bar: a validated new population-scale phenotype for EBV persistence, with replicated loci and biologically interpretable architecture; disease links calibrated. Functional experiments not required for this study type in Nature (precedent: biobank GS by-product trait papers such as Gupta et al. 2023, cited as ref 60), but phenotype validity is essential.
- Feasibility constraints stated: UKB/AoU samples not directly accessible for wet lab; supplementary material unavailable to reviewer.
- Assumptions not made: did not assume authors have access to UKB DNA; did not assume unique dual indexing was or was not used in UKB/AoU GS.
- Calibration uncertainty: whether Nature editors regard the disease/MR component as essential to significance (confidential note).

## S1 — Structured Claim–Evidence Map

### H1 — "the detection of short-reads mapping to the EBV genome (EBV-reads), is a robust surrogate measure for increased EBV viral load"; "our study is the first to demonstrate that GS-based EBV reads can be used as proxies for elevated EBV viral load, with high specificity"
- Verb strength: "demonstrated", "established", "first" — strong methodological claim.
- Scope: blood (buffy coat) GS; UKB and AoU.

#### M1.1 — EBV reads are genuine, individual-specific EBV DNA (not contamination/artefact)
- E1.1a (Methods; Suppl Fig 1 NA): plate-level QC removed 51 plates (n=3,979); read filters (both mates on chrEBV, ≤20 soft-clip, ≥120 matched bases, dedup). Unit: individual. Endpoint: read count.
- E1.1b (Fig 1b): aggregate coverage across EBV genome "uniform" (visual: fluctuating 200–600 with dips).
- E1.1c (Fig 1d): serology cohort n=9,281: EBVread+ in 3/491 sero− (0.61%) vs 1,440/8,790 sero+ (16.38%); specificity 99.4%, sensitivity 16.4%.
- Limitation: 61.9% of positives have exactly one read; lane/run-level index misassignment not analysed (searched full text for "lane", "index", "hopping", "flow cell": only sequencing-platform description found).

#### M1.2 — EBVread+ reflects increased viral load
- E1.2a (ED Fig 1): simulation, log-normal latent load + binomial sampling, parameters "manually fitted to match the observed read count distribution". Inference: compatibility.
- E1.2b (Fig 2b): within-read-positive GWAS (1 read, n=35,703 vs ≥2 reads, n=20,477): effect-size correlation r=0.93 (non-MHC, P=6.2×10⁻⁷), r=0.94 (HLA).
- E1.2c (Fig 1e): HIV (39.7%), glucocorticoids (19.4%), other immunosuppressants (18.3%) vs 15.6% baseline.
- E1.2d (Fig 4c, ED Fig 3a): HLA_all GRS increases with read count.
- No direct quantitative comparison with qPCR/ddPCR (qPCR mentioned only as future need in limitations).

#### M1.3 — EBVread+ is not a proxy for B-cell/lymphocyte abundance or technical depth (bridge claim)
- E1.3a (Fig 1g): prevalence rises with lymphocyte % (~0.08→~0.27 across 0–60%) and GS yield (~0.12→~0.4 across ~50–300 Gb); both adjusted as covariates.
- E1.3b (ED Fig 2e): memory B-cell GWAS (Orrù 2020, n=3,757) vs EBVread+ non-MHC effects: r=0.34, P=0.112; HLA not available; TNFSF13B shared.
- Hidden assumption: lymphocyte % adequately captures B-cell (memory B-cell) DNA fraction in buffy coat.

- Logical assembly of H1: M1.1 ∧ M1.2 ∧ M1.3 → "EBVread+ = proxy for viral load". Weakest bridge: M1.3 and lack of direct M1.2 validation.

### H2 — Non-genetic determinants: HIV, immunosuppressive drugs, "current, but not former, smoking", male sex, age, winter season
- E2a (Fig 1e–g; AoU SNOMED screen, Suppl Table S2 NA). Cross-sectional, marginal standardization, bootstrap.
- "Not former": inferred because "Former smoking status was not selected by variable selection".

### H3 — Genetic architecture: MHC (116 HLA alleles → 54 independent) + 27 non-MHC loci, replicated in AoU; "specific factors associated with EBV viral load during latency"
- M3.1 GWAS discovery (Fig 2a): 56,180 cases/304,103 controls; 28 loci; SPA plateau handled by non-SPA rerun.
- M3.2 Replication (text; Suppl Tables S4/S5 NA): 98/106 matched HLA alleles nominal + consistent; 25/27 non-MHC leads P<0.05 in AoU EUR (n=184,948).
- M3.3 HLA independence: iterative allele-level conditional analysis → 54 alleles; top DRB1*04:04 (β=0.79), A*02:01 (β=−0.31), B*14:02 (β=−0.68).
- M3.4 Specificity: vs serology (Fig 2c; ED Fig 2a–d), memory B cells (ED Fig 2e), HHV-7 reads (Fig 2d: HLA r=−0.02; non-MHC r=0.37, P=0.06; 6 loci P<0.05; coloc at SLC8A1, PTPN22).
- M3.5 SNP h² = 2.04% (s.e.m. 0.44%) (scale unspecified).

### H4 — Biology: T cell/NK effector programs; IEI enrichment; novel candidate IEI genes (e.g., CD226)
- E4a (Fig 3b): 30 GOBP terms (T-cell activation); (Fig 3c) GTEx spleen, whole blood, EBV-LCL, lung, terminal ileum.
- E4b (Fig 3d–g): scDRS in 1M-scBloodNL (37,033 cells, 8 level-1 types): CD8+ T and NK significant; B cells not enriched.
- E4c MAGMA IEI enrichment (P=4.66×10⁻⁶, β=0.19); EBV-specific IEI subset β=0.35, P=0.055.
- E4d RVAS: only TNFRSF13B p.Cys104Arg significant outside MHC; 24 genes with P<0.01 in both MAGMA and RVAS; 7 pLoF-driven incl. CD226 → "strong novel candidate genes".
- E4e ERAP2 NMD haplotypes (Fig 3a), eQTLs (OneK1K).

### H5 — Disease overlap and causality
- M5.1 HLA GRS in UKB disease cohorts (Fig 4f): MS ↑HLA_MHC I (P=1.06×10⁻⁴; P=0.056 after removing A*02:01), RA ↑HLA_MHC II (persists after removing DRB1*04:04), NHL ↓HLA_all.
- M5.2 AoU PheWAS (Fig 4g, ED Fig 3d): T1D (HLA_MHC II β=0.176), IBD/UC (negative), hypothyroidism; MS, RA, NHL replicated at P<0.001.
- M5.3 2SMR (ED Fig 4, Suppl Tables S21–22 NA): RA OR_wMed 1.21 [1.09–1.35]; T1D OR_wMed 1.86 [1.64–2.10]; heterogeneity; "driven by SNPs in the MHC region"; hair colour negative control null.
- Authors' wording: abstract "suggested potential causal effects"; Discussion "For T1D, 2SMR suggested that EBV viral load might be a causal factor. The pathophysiological relevance of EBV may thus be broader than currently assumed."
- Bridge: GRS/instrument effects on disease operate through EBV load rather than directly through HLA-restricted autoimmunity.

## S2 — Claim Appraisal

### M1.1 (reads are genuine individual EBV DNA)
- Verdict: Partially supported. Relation: Indirect.
- Strongest: 3/491 sero− vs 16.4% sero+ (Fig 1d) argues against pervasive contamination; plate QC.
- Limitation: single-read positives dominate; index misassignment at ~0.1% (L3) from high-load samples (max 27,639 reads) co-sequenced on the same lane could plausibly create sporadic 1-read calls; not tested. Low sero− count (n=491) gives an imprecise false-positive estimate.
- Evidence that would change verdict: lane/run-level clustering analysis; per-individual EBV sequence-variant consistency where read depth allows; sensitivity analysis restricting to ≥2 reads.
- Verification flag: Supplementary Note 1 and Fig. 1 not assessable.

### M1.2 (reflects increased viral load)
- Verdict: Unsupported at the stated level ("robust surrogate", "demonstrated"). Relation: Non-discriminating.
- Comparison/endpoint fit: No comparison against a quantitative viral-load measure. Simulation is fitted to the observed distribution, so compatibility is guaranteed for many latent distributions; it does not test that reads index viral load. The within-positive GWAS shows a dose-response in genetic effects, which any continuous determinant of read count (including B-cell DNA fraction) would also produce. Immunosuppression/HIV associations are consistent with, but not specific to, viral load (both also change lymphocyte composition).
- Specificity against serostatus (the "high specificity" claim) concerns prior infection, not elevated load.
- Literature: Moustafa 2017 (ref 23) detected EBV in blood GS; Kanakry 2016 (ref 18) qPCR in PBMC; field reference is quantitative NAT (L7). Manuscript position: extends — first biobank-scale use, but the proxy is not benchmarked.
- Evidence that would change verdict: qPCR/ddPCR EBV DNA in samples with matched GS (any cohort), showing monotonic relation of read count/positivity with copies per µg DNA or per B cell.

### M1.3 (not B-cell abundance/technical)
- Verdict: Partially supported. Relation: Indirect.
- Limitation: EBV latency reservoir is memory B cells (ref 4). Probability of sampling an EBV genome in buffy-coat DNA = (fraction of B cells) × (infected fraction) × copies. Lymphocyte % is a coarse proxy (T cells dominate lymphocytes). The memory B GWAS used (n=3,757) is underpowered; r=0.34 (P=0.11) is not evidence of absence. Several loci are B-cell homeostasis genes (TNFSF13B/BAFF, TNFRSF13B/TACI, BCL3, IKZF3). scDRS shows no B-cell enrichment, which is modestly reassuring for the common-variant set but uses PBMC expression, not abundance.
- Available remedy in existing data: B-cell fraction from IGH recombination in the same blood WGS (ImmuneLENS; validated in blood WGS, L2).
- Consequence: loci and non-genetic factors (smoking increases memory B cells, ref 49 per authors; male sex; age) may partly reflect B-cell compartment size rather than "host control" of infection.

### Literature grounding for H1/M1.2–M1.3
- Established: EBV persists in memory B cells; qPCR is standard for load; WGS contains EBV reads (Moustafa 2017).
- Consistent prior: elevated EBV load in immunosuppression/HIV (refs 17–19).
- Controversy: none manufactured; open question is construct validity of a detection-based trait.
- Contribution: new scalable phenotype; validity contingent on benchmarking.

### H2
- Verdict: Partially supported (associations plausible, replicated for seasonality in AoU). "Current, but not former" is Unsupported at the stated level: based on non-selection by BIC stepwise selection, not on an estimated former-vs-never contrast with CI. Direction-of-causation and B-cell mediation (smoking) unresolved; authors acknowledge the latter.

### H3
- M3.1/M3.2: Supported (large n, AoU replication of 25/27 non-MHC and 98/106 HLA alleles; tables not assessable).
- M3.3 "54 independent HLA alleles": Partially supported. Allele-level stepwise conditioning in a region of extended LD with imputed alleles (HLA*IMP:02) can inflate the count of "independent" signals; amino-acid/haplotype-level modelling is the usual field approach (e.g., ref 25, Raychaudhuri 2012). Imputation accuracy not reported in main text.
- M3.4 "specific factors … not confounded": Partially supported. Serology correlations were described as "only weak", but ED Fig 2b shows p18 VCA IgG: HLA r=0.64 (P=1.55×10⁻⁵), non-MHC r=0.47 (P=0.014); ZEBRA HLA r=0.45 (P=3.68×10⁻³). DRB1*04:04 is an established HLA association for EBV VCA p18 and ZEBRA antibody levels in UKB (Kachuri 2020, L1). So HLA effects on EBVread+ partly overlap with humoral anti-EBV response determinants — biologically coherent (antigen load vs humoral response) but contradicts the framing of distinct architecture. HHV-7 non-MHC r=0.37 (P=0.06) suggests some shared non-specific component.
- M3.5 h²: Not assessable (scale).

### H4
- Enrichments: Supported as statistical enrichments. "Strong novel candidate genes" (CD226 etc.): Unsupported at the stated level — based on overlap at P<0.01 in both MAGMA and RVAS, not test-wide significant; EBV-specific IEI enrichment P=0.055. Interpretive, hypothesis-generating.
- "MHC class I and II largely equal contribution" — based on GRS R² (Fig 4b) and HLA allele counts; acceptable as descriptive.

### H5
- M5.1/M5.2: Association supported; interpretation via EBV load Unsupported/Non-discriminating. The same HLA alleles are direct disease-risk alleles: DRB1*04:04 is an RA shared-epitope allele (manuscript ref 25) and belongs to the DR4 haplotype family that confers T1D risk (L6); HLA-A*02:01 is protective for MS (ref 26); MS GRS association vanishes on removing A*02:01. HLA-GRS–disease associations are therefore expected from horizontal pleiotropy irrespective of EBV load.
- M5.3 MR: Unsupported at the stated causal level. Relation: Non-discriminating. Heterogeneity + MHC-driven estimates = exclusion-restriction violation risk (L4). Binary exposure effect is per unit log-odds liability (L5), requires reporting. Outcome of the MHC-excluded analyses not reported in main text (Supplementary Table S22 NA). ED Fig 4 includes MS as "significant using two or more estimators" while main text says no evidence for MS — needs reconciliation.
- Literature position: EBV–MS causal evidence is strong from serological cohorts (Bjornevik 2022, ref 10); this manuscript does not discriminate EBV-load-mediated vs HLA-direct mechanisms.

### Literature Source Register

| ID | Citation | Role | Exact proposition | Affected | Verified |
| --- | --- | --- | --- | --- | --- |
| L1 | Kachuri L, Francis SS, Morrison ML, et al. The landscape of host genetic factors involved in immune response to common viral infections. Genome Med 12, 93 (2020). PMC7590248 | conflicting/benchmark | In UKB serology (n=7,924), HLA class II dominates viral antibody response; DRB1*04:04 among independent alleles for EBV ZEBRA and VCA p18 IgG | M3.4, I5 | Yes (PMC full text via WebFetch) |
| L2 | Bentham R, et al. ImmuneLENS characterizes systemic immune dysregulation in aging and cancer. Nat Genet 57, 694–705 (2025). doi:10.1038/s41588-025-02086-5; PMC11906351 | precedent/method | Estimates B-cell fraction from IGH locus in blood-derived WGS; validated in 100,000 Genomes Project blood samples | M1.3, I2 | Yes (PMC) |
| L3 | Costello M, et al. Characterization and remediation of sample index swaps by non-redundant dual indexing on massively parallel sequencing platforms. BMC Genomics 19, 332 (2018). PMID 29739332 | benchmark | Index swapping on patterned flow cells incl. NovaSeq; mean contamination 0.89% (i7 only), 0.13% (dual) | M1.1, I1 | Yes (search abstract) |
| L4 | Burgess S, et al. Guidelines for performing Mendelian randomization investigations: update for summer 2023. Wellcome Open Res 4, 186 (2023). doi:10.12688/wellcomeopenres.15555.3 | consensus | Standards for instrument validity, pleiotropy-robust methods and interpretation | M5.3, I3 | Yes (search/PubMed record) |
| L5 | Burgess S, Labrecque JA. Mendelian randomization with a binary exposure variable: interpretation and presentation of causal estimates. Eur J Epidemiol 33, 947–952 (2018). doi:10.1007/s10654-018-0424-6 | consensus | Binary exposure = dichotomized liability; exclusion restriction can be violated; estimates need specific interpretation | M5.3, I3 | Yes (search abstract) |
| L6 | Rich SS, Erlich H, Concannon P. Genetics of type 1 diabetes. In: Diabetes in America, 3rd ed., Ch. 12 (NIDDK; received in final form Dec 2015; publication year 2018 — uncertain) | consensus | MHC accounts for about half of T1D genetic risk; DRB1*04-DQB1*03:02 (DR4) haplotypes confer high risk | M5.1–5.3, I3 | Yes (PDF text extracted) |
| L7 | Fryer JF, et al. A collaborative study to establish the 1st WHO International Standard for Epstein–Barr virus for nucleic acid amplification techniques. Biologicals (2016). PMID 27461128 | consensus/standard | WHO EBV NAT standard (NIBSC 09/260) established 2011 for standardizing quantitative EBV DNA assays | M1.2, I1 | Yes (search abstract; volume/pages not verified) |
| L8 | Sasa N, et al. Blood DNA virome associates with autoimmune diseases and COVID-19. Nat Genet 57, 65–79 (2025). PMC11735405 | novelty benchmark | Blood WGS virome in 6,321 Japanese; analysed eHHV-6 and anellovirus; EBV not analysed as a study variable | Novelty H1 | Yes (PMC) |
| L9 | Orrù V, et al. Complex genetic signatures in immune cells underlie autoimmunity and inform therapy. Nat Genet 52, 1036–1045 (2020) | benchmark | 731 immune traits GWAS in 3,757 Sardinians (source of memory B cell GWAS used) | M1.3, I2 | Yes (search) |
| L10 | Oelen R, et al. Single-cell RNA-sequencing of PBMCs reveals widespread, context-specific gene expression regulation upon pathogenic exposure. Nat Commun 13, 3267 (2022) | citation correction | This is the 1M-scBloodNL dataset; manuscript ref 40 (van der Wijst 2018) is a different dataset | Minor | Yes (search) |

### High-Level Roll-Up

- H1: Partially supported. Strongest: serology specificity + GRS dose-response. Weakest bridge: no quantitative validation; B-cell abundance and contamination not excluded. Defensible: "detectable EBV DNA in blood GS, a trait enriched for higher EBV DNA burden". Overclaim: "robust surrogate", "demonstrated", "first … with high specificity".
- H2: Partially supported; "not former smoking" overstated.
- H3: Loci robust and replicated (Supported); "specific to EBV load/not confounded" Partially supported; HLA allele count Partially supported.
- H4: Enrichments supported; candidate-gene language overstated.
- H5: Genetic overlap supported only as HLA-level pleiotropy; EBV-mediated or causal interpretation unsupported.

## S3 — Issue and Action Ledger

### I1 — Validity-critical
- Affects: H1, M1.1, M1.2 (and all downstream H3–H5 interpretation).
- Location: Results "Detection of EBV-reads"; Fig 1c–d; ED Fig 1; Fig 2b; Discussion para 1 ("first to demonstrate", "with high specificity").
- Problem: No orthogonal quantitative validation; simulation is fitted (non-discriminating); specificity is against serostatus; single-read calls (61.9% of positives) vulnerable to lane-level index misassignment.
- Consequence: The central phenotype may conflate viral load with exposure, contamination and composition.
- Required action: Decisive — quantitative EBV DNA (qPCR/ddPCR, WHO-standardized) in samples with matched blood GS, showing relation with read count. Contamination arm (existing data): test clustering of 1-read positives by sequencing run/lane with high-count samples; sensitivity of GWAS lead effects to restricting cases to ≥2 reads (partly present as Fig 2b).
- Role: qPCR benchmark = Decisive; lane analysis = required supporting analysis to exclude artefact; fallback = rename trait as detectable EBV DNA and remove "robust surrogate"/"first … high specificity".
- Precedent: WHO standard (L7); index swapping (L3).
- Result interpretation: monotonic positive correlation → claim stands; weak/no correlation → trait is detection/exposure-related, reframe; lane clustering present → re-define cases.
- Status: Drafted.

### I2 — Validity-critical
- Affects: H1/M1.3, H2, H3 (M3.4 "not confounded by memory B cell abundance").
- Location: Fig 1g (lymphocyte %), ED Fig 2e, Results para on memory B cells, Discussion smoking paragraph.
- Problem: Read detection depends on B-cell DNA fraction; lymphocyte % is a coarse proxy; memory B GWAS (n=3,757) underpowered; B-cell homeostasis loci present.
- Required action: estimate per-sample B-cell fraction from IGH in the same GS (e.g., ImmuneLENS, L2) and (a) show its relation to EBVread+, (b) re-estimate lead variant/HLA effects and non-genetic effects with this covariate (or as ratio of EBV reads per B-cell genome). Existing-data reanalysis.
- Fallback: explicitly state loci may act via B-cell compartment size; revise "host control" language for affected loci.
- Status: Drafted.

### I3 — Validity-critical (for disease/causal claims; headline in abstract)
- Affects: H5 (M5.1–M5.3); abstract; Discussion.
- Problem: HLA alleles are direct risk alleles for RA, T1D, MS; MR estimates heterogeneous and MHC-driven; binary exposure; MS reported inconsistently.
- Required action: report MR excluding MHC (and non-MHC GRS PheWAS) in main text; pleiotropy-robust estimators with outlier handling; interpret binary exposure per L5; remove causal language unless non-MHC instruments support it; for GRS–disease results, show whether associations persist after removing/conditioning on established disease-risk HLA alleles (not only single top allele).
- Fallback: describe as shared HLA architecture, hypothesis-generating.
- Status: Drafted.

### I4 — Recommended strengthening
- Candidate-gene claims (CD226 et al.; "novel candidates" for IEI) based on P<0.01 overlaps; ask for calibrated language or additional support (e.g., burden P after multiple testing, independent data).

### I5 — Recommended strengthening
- Serology relation understated (ED Fig 2b/c; DRB1*04:04 known for VCA/ZEBRA, L1); Fig 4d null in few sero− individuals (power). Reframe text, report power.

### I6 — Recommended strengthening
- "Current, but not former, smoking": provide explicit never/former/current estimates with CIs; discuss B-cell mediation.

### I7 — Recommended strengthening
- HLA: report imputation accuracy/INFO; amino-acid-level or haplotype conditional analysis; justify "54 independent".

### I8 — Minor (high value): data/code availability — summary statistics (UKB GWAS, HLA, RVAS) deposit; analysis code beyond read extraction.
### I9 — Minor: serology cohort n inconsistency (9,281 in Fig 1d/text; 6,531 ED Fig 3a and Fig 4c group sum; 6,065 Fig 4b/f).
### I10 — Minor: h² scale (observed vs liability), prevalence used.
### I11 — Minor: Figure legend/citation errors — Fig 2 legend "similar to those presented in c" (should be b); ED Fig 3d "in analogy to Fig. 4f" (PheWAS is Fig 4g); Fig 4a legend "(i) … (i)"; "HLA-A*2:01"; ED Fig 4 key "Weighted mean" vs "weighted mode" in Methods; ref 40 vs 1M-scBloodNL (Oelen 2022); refs 4 and 6 duplicated; UKB-cohort 490,294 (Fig 1a/Results) vs 490,293 (Methods); scDRS level-2 "26" (Methods) vs "21" (Results) cell types; snakemake "v.32.4" vs "v7.32.4"; typos ("EBVseron-egative", "performet", "Herefore").
### I12 — Minor: MS in ED Fig 4 listed as significant with ≥2 estimators vs main text "No evidence … other seven outcomes" — reconcile.
### I13 — Minor: Discussion "In RA cases, alleles at MHC class I were associated with lower …" relies on marginal (*) P<0.1 (Fig 4f) — moderate.
### I14 — Minor: AoU replication covariates lack blood counts; AoU HLA mapping 166/178 alleles with 11 class II unmapped — state impact.
### I15 — Minor: interpret scDRS absence of B-cell enrichment and GTEx EBV-LCL enrichment (LCLs are EBV-transformed B cells).

Minor classes checked: figure legibility (Fig 3b/c fonts small but legible; Fig 4e "mid AoU" bar exceeds axis — noted in I11 set? added to peer review), terminology (causal verbs — I3; "robust surrogate" — I1), counts/denominators (I9, I11), statistical reporting (I10, I12, I13), code/data (I8), prior work placement (Moustafa, Sasa, Kachuri — I5), clinical/biological context exceeding data (I3, I4).

### Recommendation State
- Central bottleneck: construct validity of EBVread+ as viral load (I1, I2).
- Scientific validity: loci robust as determinants of detectable blood EBV DNA; interpretation as viral-load control and disease causality not yet established.
- Venue-level adequacy: the calibrated contribution (first biobank-scale genetic map of detectable latent EBV DNA with cross-biobank replication) is plausibly of Nature-level interest if the phenotype is validated.
- Revisability: I2, I3 by reanalysis/claim calibration; I1 requires an external benchmark dataset (realistic but new data).
- Preliminary recommendation: Major revision.

## S4 — Draft and Verification

- peer-review.md drafted: yes. Major Comments mapped: MC1→I1, MC2→I2, MC3→I3. Recommended Revisions: I4–I7. Minor: I8–I15. Recommendation: Major revision. Confidential comment: yes.

### Verification
- Quotes and claim verbs: grep-verified — "robust surrogate measure for increased EBV viral load"; "with high specificity"; "potential causal effects of EBVread+ on RA and T1D"; "might be a causal factor"; "strong novel candidate genes for host control of latent EBV-infection"; "represent specific factors associated with EBV viral load during latency"; "largely equal".
- Numbers: 61.9% single-read; 27,639 max; 3/491 (0.61%) and 1,440/8,790 (16.38%) (Fig 1d); within-positive n 35,703/20,477; r=0.93/0.94; HHV-7 r=0.37 P=0.06; memory B r=0.3409 P=0.112 (ED Fig 2e); VCA p18 r=0.6375 P=1.55×10⁻⁵, non-MHC r=0.4719 P=0.014; ZEBRA r=0.4525 P=3.68×10⁻³; Fig 2c HLA r=0.3649 P=0.021; MS P 1.06×10⁻⁴ → 0.056; RA OR 1.21 [1.09,1.35]; T1D OR 1.86 [1.64,2.10]; h² 2.04% (0.44%); serology n 9,281 / 6,531 / 6,065 checked in text, Fig 1d, ED Fig 3 legend, Fig 4b/c/f images.
- Figure references: Fig 1g panels (lymphocyte %, yield) read from image; Fig 4f significance marks read from image; ED Fig 4 legend vs main text.
- Existing analyses checked before stating absence: qPCR (only in limitations), "lane"/"index"/"hopping"/"flow cell" (only platform description), B-cell count/fraction (only memory-B GWAS comparison), MR excluding MHC (Methods describe; results only referenced to Supplementary Table S22/Notes — "not found in the available material"), HLA imputation accuracy (not in main text; supplementary NA), summary statistics deposition (Data availability: "upon reasonable request").
- OCR/extraction artefacts: "EBVseron-egative" may be hyphenation artefact of JATS conversion — kept as possible typo but low priority; HLA-A*2:01 appears in text as such.
- Literature propositions: L1–L10 checked as listed.
- Unresolved: Supplementary-dependent items (plate QC, S22 MR-excluding-MHC results, HLA imputation QC) Not assessable.

## S5 — Final Pruning and Decision

- Requested actions classified: MC1 = new benchmark data (decisive) + existing-data lane analysis (required to exclude artefact) + fallback; MC2 = existing-data reanalysis + fallback; MC3 = reanalysis + claim calibration.
- Minimum routes retained: yes; EBV strain-variant consistency analysis moved out (supporting characterization; omitted from report).
- Recommended strengthening moved: I4–I7 to Recommended Revisions.
- Alternative-route equivalence: MC1 fallback (rename trait, drop "robust surrogate") preserves a Nature-appropriate contribution only partially — stated as acceptable fallback for the phenotype label but flagged to editor that significance then depends on the genetic map itself.
- Duplicates removed: memory-B comment consolidated into MC2 (removed from serology/specificity item); MS inconsistency kept as minor only.
- Draft 1 = 1,575 words → pruned to 1,249 words total (≈1,130 author-facing, excluding confidential note); Major Comments = 3 (three independent validity-critical issues justify >1,000 words).
- Action dispositions: MC1 qPCR/ddPCR benchmark = Minimum required (decisive); MC1 lane-clustering test = Minimum required (inseparable artefact exclusion, existing data); MC1 reframing = Claim-calibration fallback (editorial caveat in confidential note). MC2 IGH-based B-cell fraction + conditional re-estimation = Minimum required; loci re-description = fallback. MC3 MHC-excluded MR / non-MHC GRS in main text = Minimum required; conditioning on disease-risk HLA alleles = Minimum required for the GRS–disease inference; liability-scale interpretation = Minimum (clarification); causal-language removal = fallback. I4–I7 = Recommended. I8–I14 = Minor (retained). I15 (scDRS/EBV-LCL interpretation) = Removed from report (interpretive, low consequence; retained here).
- Coverage preservation decisions: external replication — no issue (AoU replication present; keep as positive statement). Novelty vs closest prior (Moustafa 2017; Sasa 2025 did not analyse EBV; Kachuri 2020 serology HLA) — Kachuri kept via Recommended 1; Moustafa/Sasa dropped (authors cite them; no novelty dispute). Cross-cohort comparability — kept (Minor 6). Data/code availability — kept (Minor 1).
- Post-compression re-check: quotes "robust surrogate measure for increased EBV viral load", "high specificity", "only weak", "driven by SNPs in the MHC region", "potential causal effects", "might be a causal factor", "Strong novel candidate genes" re-verified against source; numbers unchanged.
- Scientific judgment unchanged: yes. Earlier stage reopened: no.

### Final Decision Rationale
- Final recommendation: Major revision.
- Claim-validity basis: loci robust; phenotype interpretation and causal disease claims not yet supported.
- Venue-completeness basis: validated phenotype + calibrated disease links would meet a discovery-genetics bar for broad interest; without phenotype validation the paper's central framing ("host control", "viral load") is not secured.
- Principal remaining issues: I1, I2, I3.
- Proportionality: two of three majors resolved with existing data; one requires a modest external benchmark or explicit reframing.
- Residual uncertainty: supplementary content could already contain partial answers (e.g., MHC-excluded MR, plate/lane QC).

## Locked Decisions and Handoff
- Preserve quotes: "robust surrogate measure for increased EBV viral load"; "might be a causal factor".
- Inconsistency to flag: serology cohort n; MS MR status.
- Requests intentionally excluded: functional experiments on candidate genes; EBV strain genotyping; non-European GWAS (acknowledged by authors).
- Output paths: `B/ai_review_v2/peer-review.md`, `B/ai_review_v2/review-dossier.md`.
