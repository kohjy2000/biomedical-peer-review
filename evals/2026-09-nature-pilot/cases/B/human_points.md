# Case B — Human peer-review ledger (round 1)

Source: `prf_s41586-026-10274-4.txt` (Nature Peer Review File, CC BY 4.0). Manuscript: host genetic and non-genetic control of EBV DNA detected in biobank genome sequencing (UKB discovery, All of Us replication).

## Header
- Substantive referees in round 1: **4** (Referee #1, #2, #3, #5). Referees #4 and #6 are one-line co-review notes (excluded; they also left code remarks).
- Round structure in file: the first round is labelled **"Version 1"** (no Version 0 in the PRF); round 2 = "Version 2".
- Editor decision: **not stated** in the PRF.
- Counts (our category): **13 Major / 26 Minor** (39 points). By referee: R1 2/2, R2 4/7, R3 3/6, R5 4/11.
- Authors answered two cross-referee themes in an aggregate preface: (1) are single-read (EBV-read=1) samples true positives; (2) which EBV life-cycle phase is captured. Outcomes below reflect that preface.

Severity column = referee's own label, or "none" if unlabelled. Category = our call (Major = would change validity or venue decision if unaddressed; Minor = presentation/clarification).

## Round-1 points

| ID | Ref. signal | Our cat. | Topic | Paraphrase | Author outcome | Note |
|---|---|---|---|---|---|---|
| R1-1 | none | Minor | statistics; replication | No genome-wide meta-analysis of UKB + AoU reported; was it done and did it yield extra loci? | rebutted | Not done (AoU lacks blood counts → confounding risk); sentence and Supp Note added; covariate-sensitivity GWAS run. |
| R1-2 | none | Minor | mechanism/functional validation; statistics | Test HLA × antigen-processing gene epistasis (e.g., HLA–ERAP, as in ankylosing spondylitis). | new analysis/data added | Interaction analysis: 3 Bonferroni-significant ERAP2 × class I HLA interactions (Fig 2, Supp Table). |
| R1-3 | none | Major | measurement validity; statistics | Fig 2b suggests single-read individuals may be misclassified; should they be excluded or merged with controls? Are they misalignments or true low-level positives? | new analysis/data added | Additional GWAS definitions (0 vs 1, 0 vs ≥2) plus aggregate validation evidence; single-read group defended as true positives. |
| R1-4 | none | Major | cohort/confounding | Different covariate sets in UKB vs AoU: how do they affect association results and PRS accuracy? | new analysis/data added | UKB GWAS rerun without blood counts and with basic covariates; covariate overview table; small effect at GW-significant loci. |
| R2-1 | none | Major | measurement validity; replication | EBV-read detection as a surrogate for viral load needs orthogonal validation (e.g., qPCR on PBMC/plasma/saliva in a smaller cohort); HIV-based simulation is not adequate. | new analysis/data added | qPCR in two independent cohorts (n=72 in-house; n=262 Japanese) plus paired RNA-seq (n=1,010). |
| R2-2 | none | Major | cohort/confounding; measurement validity | Contaminated-plate exclusion: threshold unclear; check whether plate EBV sequences are identical; exclusion may explain lower UKB positivity vs AoU and bias results. | new analysis/data added | Plate grouping and EBV allele-frequency analysis (outliers match lab reference strain); recomputed positivity; cohort-difference explanation added. |
| R2-3 | none | Major | measurement validity | 61.9% of positives have one read; show per-EBV-gene coverage to exclude technical bias; antibody comparison does not show read abundance. | new analysis/data added | Per-gene coverage table and single- vs multi-read coverage comparison added. |
| R2-4 | none | Major | clinical interpretation; mechanism | Without EBV gene expression, cannot tell whether reads reflect latency or lytic reactivation. | new analysis/data added | RNA-seq correlation (BART genes highest, some lytic); per-antibody serology; "latent" relabelled "persistent" incl. title. |
| R2-5 | none | Minor | cohort/confounding (sex) | Males more often EBV-read+ yet EBV autoimmunity is female-biased; look for male-specific loci possibly protective against autoimmunity. | new analysis/data added | Sex-stratified GWAS (no sex-specific effects at GW loci); future-direction sentence in Discussion. |
| R2-6 | none | Minor | clinical interpretation | Implications of no association with MS risk allele HLA-DRB1*15:01 for known EBV–MS links? | new analysis/data added | Cross-trait forest plot (Extended Data) and Discussion text proposing non-viral-load mechanisms. |
| R2-7 | minor | Minor | presentation | Figures hard to read, low quality, especially Fig 4g. | text changed/claim softened | All main figures redrawn; legends expanded. |
| R2-8 | minor | Minor | clinical interpretation | Notes MS was not significant in MR while RA/T1D were. | rebutted | Explained in letter (MR captures viral-load pathway; MHC pleiotropy caveat); no specific text change stated. |
| R2-9 | minor | Minor | novelty/literature | Avoid claiming the study is "the first". | text changed/claim softened | Claim removed. |
| R2-10 | minor | Minor | novelty/literature | T-cell/NK-cell genes controlling EBV load is already well established, not novel. | text changed/claim softened | Rephrased. |
| R2-11 | minor | Minor | presentation | Extended Data Fig 2e shows "not available". | text changed/claim softened | Panel removed; data moved to heatmap/Supp Table. |
| R3-1 | major | Major | measurement validity | Counting single-read samples as EBV+ is a low threshold; 16.2% exceeds qPCR-based 11%; show read distribution along genome and validate by qPCR. | new analysis/data added | Coverage by read-count group, qPCR validation; text added on cohort/assay differences. |
| R3-2 | none | Minor | presentation | How many AoU positives are single-read only? | text changed/claim softened | Numbers provided (≈52% overall, ≈57% EUR) and cohort table added. |
| R3-3 | none | Major | measurement validity | ≥2 vs 1-read comparison may reflect false-positive singletons rather than viral load. | new analysis/data added | Addressed via aggregate validation analyses (coverage, allele frequencies, qPCR, RNA-seq, alternate GWAS). |
| R3-4 | none | Minor | statistics | Were non-classical HLA variants within the MHC examined after conditioning on classical alleles? | rebutted | Not done (imputation not established); limitation sentences added to Methods/Discussion. |
| R3-5 | none | Major | replication; statistics | AoU HLA imputation quality metrics needed, given rare alleles and unexpected 4-field resolution. | new analysis/data added | Reduced to 2-field; UKB–AoU frequency concordance; typing of 900 AoU individuals vs imputation (r2, PPV). |
| R3-6 | none | Minor | presentation (methods) | Conditional analysis of HLA alleles not described. | text changed/claim softened | Methods paragraph added. |
| R3-7 | none | Minor | replication | Were all 54 conditionally independent HLA alleles tested in replication? | text changed/claim softened | Replication counts reported (46 of 52 available). |
| R3-8 | none | Minor | clinical interpretation; presentation | Fig 4 GRS result for MS is driven entirely by HLA-A*02:01 but not shown; RA signal persists after DRB1*04:04 removal — distinguish these. | text changed/claim softened | Symbol and legend added; results text notes attenuation without A*02:01. |
| R3-9 | code | Minor | data/code availability | A few scripts have undocumented input files or platform-specific paths. | text changed/claim softened | Script documented; README note on platform mount paths. |
| R5-1 | major | Major | clinical interpretation; measurement validity | How is latent infection distinguished from primary or lytic infection? Make the handling explicit. | new analysis/data added | Shared answer with R2-4 (RNA-seq, serology) plus terminology change to "persistent". |
| R5-2 | major | Major | measurement validity | Serology used (EA-D, ZEBRA acute-phase; VCA isotype unstated) reflects lytic/acute, not uncontrolled latency; do a sub-analysis by antibody. | new analysis/data added | Clarified all IgG; per-antibody MFI-decile analysis (strongest with VCA-p18) added as Extended Data. |
| R5-3 | major | Minor | statistics | Use reads-per-million rather than raw counts to normalise sequencing depth. | rebutted | Binary case definition unaffected by RPM; yield kept as covariate; RPM comparison shown in letter only. |
| R5-4 | major | Minor | clinical interpretation | Winter excess of EBV-read+ unclear; could reflect other seasonal infections → reactivation (i.e., lytic, not latent). | text changed/claim softened | Hypotheses added (seasonal infections, B-cell seasonality); Supp Note on SARS-CoV-2 cohort. |
| R5-5 | major | Major | measurement validity | Repeat single- vs multi-read comparison for other downstream analyses to exclude low-level contamination. | rebutted | Declined for downstream analyses; relied on five lines of validation evidence. |
| R5-6 | major | Minor | measurement validity | Seropositivity (2 of 4 antibodies) should be stratified into lytic vs past-infection markers for Fig 2c correlation. | new analysis/data added | Per-antibody correlations and genetic correlations added (Extended Data, Supp Table). |
| R5-7 | major | Minor | presentation | Discovery/replication order switches between sections (AoU first for non-genetic, UKB first for genetic); rationale? | text changed/claim softened | Study overview Supp Note; cohort prefixes added throughout. |
| R5-8 | major | Minor | presentation | Fine-mapping/credible-set jargon too technical for broad readers; Supp Table lists single variants, not sets. | text changed/claim softened | General simplification; details moved to Supp Notes. |
| R5-9 | major | Minor | mechanism/functional validation | Are the 83 inborn-error-of-immunity genes linked to poor control of other herpesviruses (CMV) or general infection susceptibility? | new analysis/data added | Literature-based review of 9 top IEI genes (new Fig 3 panel, Supp Note); no biobank infection analysis. |
| R5-10 | major | Minor | clinical interpretation | Are these IEI genes involved in EBV-related cancers? | new analysis/data added | Same review: four genes linked to EBV-driven lymphoma. |
| R5-11 | major | Minor | clinical interpretation | Rationale for selecting the EBV-associated diseases; are they mostly linked to active infection? | text changed/claim softened | Selection rationale and reference added. |
| R5-12 | major | Major | causal inference | MR effects on RA/T1D driven by MHC variants violate MR assumptions (pleiotropy); EBV–T1D evidence weak. | text changed/claim softened | MR reframed as exploratory; causality claim removed from Abstract; all estimators in Supp Tables. |
| R5-13 | major | Minor | cohort/confounding (generalizability) | Add limitation: cohorts are predominantly European, relevant to HLA, disease prevalence and EBV strain variation. | text changed/claim softened | Limitation paragraph added. |
| R5-14 | minor | Minor | presentation (methods) | Why different read-filter criteria for EBV vs HHV7? | text changed/claim softened | Explained in Supp Note. |
| R5-15 | minor | Minor | presentation (methods) | If both mates must map, how can a sample have exactly one EBV read — fragment vs read? | text changed/claim softened | Methods define "EBVread" as one read pair. |

## Consensus issues (raised by 2+ referees)
1. **Validity of the single-read EBV+ definition (misclassification/contamination) and read-count as viral load** — R1-3; R2-1, R2-3; R3-1, R3-3; R5-5 (all four referees). Outcome: qPCR in two cohorts, RNA-seq, coverage/allele-frequency analyses, alternate GWAS definitions. R1 re-flagged residual misclassification in round 2.
2. **Which EBV phase is measured (latent vs lytic) and how serology is interpreted** — R2-4; R5-1, R5-2, R5-6. Outcome: RNA-seq and per-antibody analyses; terminology changed to "persistent infection" (title changed).
3. **UKB vs AoU comparability (covariates, positivity rate, HLA imputation)** — R1-1, R1-4; R2-2; R3-2, R3-5.
4. **Interpretation of autoimmune links, MS/HLA-DRB1*15:01, GRS and MR** — R2-6, R2-8; R3-8; R5-12. Outcome: MR causality claim removed from Abstract.
5. **Readability for a broad audience / figure quality** — R2-7; R5-8.

## Later-round points that were NEW (not raised in round 1)
Round 2 (Version 2):
- R1: The new qPCR validation shows high positivity in 0-read samples, and the second cohort shows near-equal positivity for 0, 1 and 2 reads; discuss residual misclassification and its impact. (New point arising from revision data; authors added a Discussion limitation paragraph.)
- R2: Overall biomedical conclusions (higher EBV load with immunosuppression/autoimmunity) are largely expected; methodological novelty outweighs biological impact. (Broader novelty concern than round-1 R2-10; no change requested.)
- R2 (very minor): Fragment sentence near lines 369–370 (GTEx tissues). Deleted.

Not new: R3, R4, R6 had no further concerns; code remarks were satisfied.
