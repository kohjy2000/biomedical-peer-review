# Review Dossier

## Status and Source Set

- Mode: Initial
- Current stage: S5 complete (delivered)
- Completed stages: S0, S1, S2, S3, S4, S5
- Manuscript version and date: Research Square preprint v1 (65 pages), "Safety and Efficacy of Intratumoral Anti-CTLA4 with Intravenous Anti-PD1" (NIVIPIT trial, NCT02857569). The review is written as of the submission date, 2025-08-17.
- Source set reviewed: main text, Methods, references, figure legends, Figures 1–6, Extended Data Figures 1–6, Extended Data Tables 1–3, Methods Table 1 (all within preprint_v1.pdf). Text was extracted with PyMuPDF and figure pages were rendered as images and inspected visually.
- Sources intentionally excluded: any later version, the published article, peer review files and commentary. Page 3 of the PDF (Research Square cover) states that a version of record exists. I noted it and did not open, search for or use it.
- Not available: Methods Figure 1 and Methods Table 2 (these pages render as captions only), the trial protocol, the statistical analysis plan, and any separate supplementary files. Judgments that depend on them are marked Not assessable.
- Literature cutoff date: 2025-08-17 (all sources used were published 2004–2020).
- Last verified: this session.
- Next bounded action: none (delivered).
- Dossier confidentiality or storage note: this dossier is confidential to the reviewer and is stored locally only.

## S0 — Review Calibration

- Journal and submission stage: Nature, initial submission.
- Article/study type: randomized, multicentre, open-label Phase 1b clinical trial (2:1, IT vs IV ipilimumab, both arms with IV nivolumab), plus exploratory translational biomarker analyses on paired tumour biopsies and blood.
- Central question and intended contribution: (i) whether low-dose (0.3 mg/kg) intratumoral ipilimumab plus IV nivolumab reduces severe irAEs compared with standard IV ipilimumab 3 mg/kg + nivolumab without losing efficacy; (ii) which baseline and on-treatment tumour immune features are associated with durable clinical benefit (DCB); (iii) a mechanistic claim that anti-CTLA4 acts in humans by FcγR-dependent depletion of activated intratumoral Tregs.
- Design, data, population/model, and setting: 86 screened, 63 randomized, 61 analysed (IT 40, IV 21). Four French centres. First-line unresectable stage III/IV melanoma (BRAF-mutant patients could have received prior BRAF/MEK therapy). The primary endpoint is 6-month treatment-related grade 3–4 AE-free survival in the IT arm, assessed with a Fleming design (p0 = 50%, p1 = 70%, α = 10%, power 90%, 38 evaluable patients, success if ≥23/38). The IV arm is an internal control with no formal comparison planned. Median follow-up is 55.5 months. Translational data: flow cytometry of fresh biopsies (n ≈ 22 with the CD39-containing panel), secretome (n = 17), RNA-seq/deconvolution, IHC, WES, plasma cytokines and blood flow cytometry. Paired BL/W3 data are available for about 16 patients.
- Primary claim ambition and intended scope: high. The Abstract asserts that IT anti-CTLA4 is safe, has "increased efficacy", has toxicity "equivalent to anti-PD1 monotherapy", and that "persisting intratumoral regulatory–effector immune interface … is a pre-requisite" for efficacy. The Discussion asserts that anti-CTLA4 works "in humans just like in mice by depleting activated tumor-specific Tregs" and that fresh-biopsy assays are "robust predictive biomarkers".
- Editor question, review fields, and recommendation options: none were provided. I used the default structure (Overall Assessment / Major / Minor / Recommendation / Confidential comment) and standard Nature options (Accept / Minor / Major / Reject, with transfer possible).

### Relevant Review Requirements

| Requirement or expectation | Provenance | Basis or source | Consequence for this review |
| --- | --- | --- | --- |
| CONSORT-conformant reporting, flow diagram, baseline table, AE reporting, exact first/last enrolment dates and data-lock date | Journal-stated (Nature Portfolio clinical research policy; page accessed in 2026, so its wording as of 2025-08 is not independently verified) | nature.com/nature-portfolio/editorial-policies/clinical-research | Enrolment dates and data-lock date are missing, and the flow diagram excludes 2 randomized patients → minor/reporting comment |
| Prospective registration before first enrolment | Journal-stated (ICMJE, same page) | same | ClinicalTrials.gov registration is dated 19 July 2016 and EudraCT November 2015. The enrolment start is not reported, so compliance is Not assessable → ask for dates |
| Response assessment of injected vs non-injected lesions in IT trials should follow standardized lesion-level criteria (e.g., itRECIST) | Field standard | Goldmacher et al., JCO 2020 (L3) | Lesion-level comparison of injected vs non-injected lesions using ad hoc RECIST → Major comment on the efficacy claim |
| A causal/mechanistic claim about Treg depletion in humans requires absolute quantification and consideration of competing models (no depletion by IHC, Sharma 2019; FcγR genotype association, Arce Vargas 2018) | Field standard / Reviewer calibration | L4, L5, L9 | Major comment |
| Exploratory biomarker associations in small cohorts need multiplicity control, reporting of effect sizes and n, and independent validation before "predictive"/"required" language | Field standard (reviewer calibration grounded in REMARK-type practice; not anchored to a single guideline here) | Reviewer calibration | Major comment on biomarker claims |

- Claim-validity bar: the safety claim needs the pre-specified single-arm decision rule, correctly reported, with sensitivity to exclusions. Any efficacy claim needs like-for-like comparisons with uncertainty. Biomarker associations need correct denominators, arm-adjusted analysis and multiplicity control. The mechanistic claim (Treg depletion) needs a direct quantitative demonstration that discriminates depletion from dilution or phenotypic change.
- Venue-completeness bar (Nature): a conceptual advance with broad significance. For a trial, that means either a practice-relevant clinical result with credible efficacy or a mechanistic human insight that is convincingly established. A small randomized Phase 1b with descriptive efficacy and exploratory associations would have to excel on at least one of these.
- Feasibility constraints: limited biopsy material (18G cores, no FOXP3 intracellular staining possible per the authors) and small n. I did not assume that additional samples exist.
- Assumptions not made: I did not assume germline data are available for FCGR genotyping. WES with FACETS implies matched normal DNA, but the manuscript does not state this, so the request is conditional.
- Calibration uncertainty: I could not verify Nature policy wording as of 2025-08.

## S1 — Structured Claim–Evidence Map

### H1 — "intratumoral anti-CTLA4 … is safe … with a low incidence of immune-related adverse events"; primary endpoint "met"; "equivalent to anti-PD1 monotherapy" (Abstract; Discussion)

- Verb strength: "demonstrating the safety", "significantly lower incidence", "equivalent".
- Intended scope: advanced melanoma, and by extension oligometastatic and earlier-stage disease.
- Claimed novelty: first randomized comparison of IT vs IV ipilimumab with nivolumab (implicit).

#### M1.1 — The IT arm meets the pre-specified safety threshold

- E1.1a: Results p.6 and Fig. 2a. 9/37 evaluable (24.3%) had treatment-related G3–4 AEs by 6 months, and 75.7% were free of them. Three patients who died within 6 months without G3–4 toxicity were excluded. Fleming rule (Methods): acceptable if ≥23/38 are toxicity-free. Observed 28/37. If the 3 excluded patients are counted as failures, 28/40 (70%) still exceeds 23.
- Discrepancies: the Abstract reports 22.6% vs 57.1%, the Results 24.3%, and Fig. 2a 75.7%/42.9% free (implying 24.3%/57.1%). The Results call 30% the "pre-specified threshold", the Discussion calls 50% the threshold, and the Methods give p0 = 50% EFS and p1 = 70% EFS. The endpoint is labelled "treatment-related grade 3-4 AE" (Results, Statistical Methods) but "immune related" in the Objectives, Abstract and Fig. 2a.

#### M1.2 — Lower toxicity than IV ipilimumab ("significantly lower")

- E1.2a: Fig. 2a–f. G3–4 TRAE cumulative incidence is 32.5% (IT) vs 66.6% (IV) in the text. Fig. 2c shows 0.33 vs 0.64, and Fig. 2b shows grade 3 in 30% vs 52.3% and grade 4 in 2.5% vs 14.3%. The text says IT 13/40 (33%) grade 3 and IV 13 (62%) grade 3.
- The Methods state "No formal comparison between the 2 arms will be performed". No test statistic or CI is given for the "significantly lower" claim.
- Exposure confounder: in the IV arm 11/21 discontinued ipilimumab for AEs; the IT arm received nivolumab for longer.

#### M1.3 — Toxicity "equivalent to anti-PD1 monotherapy"

- E1.3a: no monotherapy arm. This is a cross-trial comparison (CheckMate 067 nivolumab G3–4 TRAE 16.3%; L1).

#### M1.4 — Systemic ipilimumab exposure is lowered

- E1.4a: Fig. 2g and p.7. n = 24 patients. Peak 2.2 vs 42.2 µg/ml, trough 0.9 vs 8.4, p < 0.0001. Nivolumab is lower in the IV arm after C2 (text cites "Fig. 2i", but the panel is the right side of Fig. 2g). The per-arm n is not given.

### H2 — "increased efficacy upon intratumoral anti-CTLA4 therapy" (Abstract); "formally demonstrating the added value of anti-CTLA4 on top of anti-PD1 therapy … with patients used as their own internal controls" (Discussion)

#### M2.1 — Injected lesions respond more than non-injected lesions

- E2.1a: p.8 and Fig. 3f,h. Injected-lesion BORR 23/35 (65.7%). Non-injected target lesions: 10/40 CR + 8/40 PR = 18/40 = 45% in the text. The Abstract and Discussion give 50%. Fig. 3h bars appear to be about 28% CR and 22% PR (≈50%), which suggests a different denominator.
- Comparison: lesion-level response of the selected injected lesion (mostly LN/skin, 96% of injections) vs patient-level RECIST sum of non-injected target lesions (which can include visceral/liver; liver metastases in 18/40 IT patients). The response criteria for single injected lesions are not defined. irRC is listed as an endpoint but not reported.
- Authors' inference: dose-dependent added value of anti-CTLA4 on top of anti-PD1.

#### M2.2 — IT arm systemic efficacy is comparable/"compares favorably"

- E2.2a: Fig. 3e,h,i,j; ED Fig. 1a,b; p.8. Non-injected ORR is 45–50% (IT) vs 62% (IV). New-lesion progression 22.5% vs 9.5%. Deaths 21/40 vs 7/21. Median OS is 50 months (IT) vs not reached in the text, but "not reached for the 2 arms" in the Fig. 3 legend. Median PFS is 13.8 months vs NR. Log-rank p ≈ 0.23 (PFS) and ≈ 0.19 (OS) per the figure. ED Fig. 1a,b shows lower BORR in the IT arm in every subgroup.
- The favourable framing depends on cross-trial comparisons with nivolumab or pembrolizumab monotherapy (CheckMate 067, KEYNOTE-006).

### H3 — Pre-existing MHC-I/II-mediated T- and B-cell immunity is "required" for DCB and "predicting" DCB "regardless of the anti-CTLA4 administration route" (Results header; Abstract)

#### M3.1 — Baseline adaptive immune features are higher in DCB

- E3.1a: Fig. 5; ED Fig. 4. Arms are pooled. DCB is defined as a RECIST response or SD beyond 6 months. Wilcoxon tests, no multiplicity correction (Methods, Statistical methods). Several readouts described as "higher"/"confirmed" have p > 0.05 in the figures: HLA-I IHC 0.080, HLA-II IHC 0.054, CD20 IHC 0.084, CD8+PD1+ RNA 0.076, CXCL13 0.12, PD-L1 IHC 0.082. Per-group n is not stated in the legends.
- Fig. 5k reports "TOTAL (n=149)", which is incompatible with the trial size.

#### M3.2 — On-treatment increases in DCB

- E3.2a: ED Fig. 5. On-treatment W3 features could reflect early response (circularity with an outcome defined at 6 months). Granzyme secretome increase in DCB: p = 0.102 / 0.092 (ED Fig. 5f), yet the Abstract states that a "tumor-secreted Granzymes increase was found only in patients with DCB". The cancer-cell decrease has p = 0.174 (ED Fig. 5g), but the text states it as a finding.

#### M3.3 — "regardless of route"

- No arm-by-biomarker interaction analysis. Biopsy site differs by arm (IT baseline = injected lesion; W3 = injected and/or non-injected; the site used in paired analyses is not stated).

### H4 — Activated Tregs and M2 macrophages at baseline associate with DCB; "unexpectedly"; "persisting intratumoral regulatory–effector immune interface … is a pre-requisite" (Abstract; Discussion)

#### M4.1 — More CD25+CD39+ CD4+ cells, Treg deconvolution and Treg genes in DCB at baseline

- E4.1a: Fig. 6a–c; ED Fig. 6b,c. Flow p = 0.003, RNA p = 0.003. FOXP3 IHC p = 0.194 (the text says "higher Foxp3 gene and protein").
- Surrogate: CD25+CD39+ without FOXP3. In ED Fig. 6a (7 external melanoma TILs), about 60–90% of CD25+CD39+ CD4 cells are FOXP3+.

#### M4.2 — More FcγR-expressing myeloid cells and M2 macrophages in DCB

- E4.2a: Fig. 6h–p. FCGR1A/3A/3B RNA p = 0.008–0.033. Macrophage deconvolution 0.071. CD68 IHC 0.169. CD163 IHC 0.221 (the text says "gene and protein"). Only RNA-level values are significant.

### H5 — Anti-CTLA4 "work[s] in humans just like in mice by depleting activated tumor-specific Tregs", which requires FcγR+ effector cells; Treg depletion "only … in responding patients" (Discussion; Results header "Selective Intratumoral Activated Tregs Depletion")

#### M5.1 — Activated Tregs decrease on treatment in DCB

- E5.1a: Fig. 6e. CD25+CD39+ as % of CD4, BL→W3 in DCB: p = 0.032. No DCB: p = 0.156 (upward).
- E5.1b: ED Fig. 6f. As % of CD45: p = 0.053 in DCB (not significant, although the text says "significant decrease … within the total CD45+ subset").
- E5.1c: ED Fig. 6g. CD4+CD25+CD39+CTLA4+ as % of CD45 (the proposed ipilimumab target): DCB p = 0.415 (no change). No DCB increases (p = 0.031).
- Internal counter-evidence: total Treg deconvolution increases in DCB (ED Fig. 6d, p = 0.008). FOXP3 IHC does not decrease (ED Fig. 6e). CD8/FOXP3 IHC ratio p = 0.25 (Fig. 6f). Circulating Tregs increase (ED Fig. 6h).
- Actual comparison: relative proportions within CD4 or CD45 at W3 vs BL, during CD8/CD4 effector influx (ED Fig. 5c,d). No absolute cell counts per mm² or per mg of tissue. Arms are pooled. The lesion biopsied at W3 may differ from the baseline lesion.

#### M5.2 — FcγR expression enables depletion

- E5.2a: correlation of FCGR RNA with DCB (Fig. 6h,i). There is no test linking FcγR level to Treg change within patients, and no FCGR3A genotype analysis.

- Logical assembly of H5: depletion → requires M5.1 to be a true loss of cells, M5.2 to be linked within patients, and the effect to be ipilimumab-specific (it would be expected to differ by dose/route, but this is untested). None of these bridges is directly tested.

### H6 — Fresh-biopsy assays (CD4+CD25+CD39+ flow, secretome granzymes) are "simple and rapid … robust predictive biomarkers" with "great sensitivity and specificity" (Discussion)

- E6.1a: group comparisons only. No ROC/AUC, thresholds, cross-validation or independent cohort. The "predictive" vs "prognostic" distinction is not addressed (there is no arm without anti-CTLA4).

## S2 — Claim Appraisal

### M1.1 (safety threshold met)

- Evidence verdict: Supported (the decision rule is met; robust to counting the 3 excluded deaths as failures, 28/40 ≥ 23).
- Relation: Direct.
- Limitation: the endpoint label (TRAE vs irAE), the threshold description (30% vs 50%) and the percentages (22.6% vs 24.3%) are inconsistent. Exclusion of early deaths from the evaluable population needs a sensitivity analysis to be reported. The 90% CI for the proportion is not reported.
- Verification flag: resolved from Methods p.38 and Results p.6.

### M1.2 (lower toxicity vs IV)

- Verdict: Partially supported (the descriptive difference is large and consistent with lower systemic exposure, M1.4). "Significantly" is unsupported because no pre-specified test exists and none is reported.
- Relation: Direct but descriptive. Confounded by differential nivolumab exposure and early IV-arm discontinuation. The irAE counts in text and figures disagree.

### M1.3 ("equivalent to anti-PD1 monotherapy")

- Verdict: Unsupported at the stated level (cross-trial; CheckMate 067 nivolumab alone had 16.3% G3–4 TRAE vs 24.3–32.5% here; L1).
- Relation: Non-discriminating.

### M1.4 (lower systemic exposure)

- Verdict: Supported (PK). Minor: the per-arm n and timing are missing, the text refers to "serum" while the figure axis says "plasma", and the figure panel reference is wrong.

### M2.1 (injected > non-injected = added value of anti-CTLA4)

- Verdict: Unsupported at the stated level.
- Relation: Non-discriminating. The comparison varies lesion site (LN/skin vs any, including liver), lesion selection (injectable, biopsied), denominator (35 vs 40) and response construct (single-lesion vs RECIST sum), not only the local ipilimumab concentration. There is no anti-PD1-alone comparator, so "added value of anti-CTLA4 on top of anti-PD1" cannot be inferred. The rates (65.7% vs 45–50%) have overlapping uncertainty and are unpaired.
- Field standard: itRECIST (L3) provides standardized separate assessment of injected and non-injected lesions and was designed for exactly this setting.
- Literature: Ray 2016 (L8) also found high local response. The manuscript quotes that study's irRC ORR as the "distant abscopal response rate" (40%, 4/10), whereas the Ray abstract reports an abscopal response in 89% and an irRC ORR of 40%. This is a citation-accuracy issue (minor).

### M2.2 (systemic efficacy of IT arm)

- Verdict: Partially supported as "activity". A "compares favorably" framing is not supported. Every internal efficacy readout (ORR, new lesions, PFS, OS, deaths, subgroup BORR) numerically favours the IV arm. The trial is not powered, so it cannot exclude a clinically important efficacy loss. This is the central safety–efficacy trade-off for the proposed clinical use.
- Literature: CheckMate 511 (L2) showed that reducing the ipilimumab dose (1 mg/kg) lowered G3–5 TRAE (34% vs 48%) with descriptively similar ORR (45.6% vs 50.6%). That is the relevant benchmark for "lower toxicity with preserved efficacy", and IT 0.3 mg/kg needs to be positioned against it.

### M3.1–M3.3 (adaptive immunity required/predictive; regardless of route)

- Verdict: Partially supported as an association (several features are nominally significant and directionally concordant with literature). "Required" is unsupported, "predicting" is unsupported, and "regardless of route" is not assessable (no interaction test, n too small).
- Relation: Indirect/associative. Arms are pooled, biopsy sites differ, there is no multiplicity control, and multiple non-significant readouts are described as confirmatory.
- Literature: consistent with established associations of CD8/PD-1/PD-L1 (Tumeh 2014, L10) and B cells/TLS (Helmink 2020, L11) with ICB benefit. The manuscript confirms these; it does not extend them.

### M4.1–M4.2 (Tregs/M2 associate with DCB; "unexpected"; "pre-requisite")

- Verdict: Partially supported as a baseline association at the RNA/flow level. "Unexpected" is contradicted by prior literature. "Pre-requisite" is unsupported.
- Competing explanation: Treg, FOXP3, CCR8, IL10, FCGR1A/3A and CD163 transcripts co-vary with overall T-cell inflammation. CD8+ T cells and IFNγ drive recruitment of Tregs and expression of PD-L1/IDO in melanoma (Spranger 2013, L7). High baseline FoxP3 was associated with clinical activity of ipilimumab (Hamid 2011, L6). Without normalization to total immune/T-cell infiltration or multivariable adjustment, these features may simply index an inflamed tumour.
- Conflicting evidence: Romano 2015 (L9) reported a higher CD68+/CD163+ ratio (relatively fewer M2) in ipilimumab responders, whereas this manuscript reports more CD163. The contrast should be discussed.
- Manuscript position: confirms (Tregs with inflamed TME), partly contradicts (M2).

### M5.1–M5.2 (Treg depletion mechanism in humans)

- Verdict: Unsupported at the stated level. Internal evidence is mixed-to-contradictory.
- Relation: Non-discriminating (a proportional decrease is compatible with depletion, with dilution by effector influx, with CD25/CD39 downregulation or phenotypic conversion, and with lesion sampling differences). The CTLA4+ subset (ED Fig. 6g) and FOXP3 IHC (ED Fig. 6e) do not decrease, and Treg deconvolution increases (ED Fig. 6d).
- Controversy (genuine): Sharma 2019 (L4): no FOXP3+ depletion after ipilimumab/tremelimumab by quantitative IHC (plus CyTOF, n = 5). Arce Vargas 2018 (L5): Fc-dependent Treg depletion in hFcγR mice, and response to ipilimumab associated with the CD16a-V158F high-affinity polymorphism in inflamed melanoma. Romano 2015 (L9): ex vivo ADCC of Tregs by CD16+ non-classical monocytes, and decreased Treg infiltration after treatment in responders. The manuscript's reconciliation (technique and timing) is plausible but not tested. It does not discriminate between the models.
- Field-standard evidence for the claim: absolute densities of FOXP3+ (or CD25+CD39+) cells in matched lesions, with spatial or multiplex IHC/IF on the same FFPE cores. Ideally, an Fc-linked readout: FCGR3A-158 genotype (precedent L5) or a within-patient correlation between FcγR/CD16+ myeloid density and Treg change. Comparison by dose/route (injected-lesion high local concentration vs IV) would further test ipilimumab dependence.
- Precedent and limitation: L5 genotype association (retrospective, modest n). L4 IHC (FOXP3 only; timing).

### H6 (robust predictive fresh-biopsy biomarkers)

- Verdict: Unsupported at the stated level (no performance metrics, no validation, and predictive vs prognostic is not separable in this design).

### Literature Source Register

| Source ID | Full citation and DOI/PMID | Role | Exact proposition supported | Affected H/M/I | Verified |
| --- | --- | --- | --- | --- | --- |
| L1 | Larkin J et al. Combined nivolumab and ipilimumab or monotherapy in untreated melanoma. N Engl J Med 2015;373:23–34. doi:10.1056/NEJMoa1504030; PMID 26027431 | benchmark | G3–4 TRAE 16.3% nivolumab, 55.0% nivolumab + ipilimumab | M1.3; I2 | Yes (Europe PMC abstract) |
| L2 | Lebbé C et al. Evaluation of two dosing regimens for nivolumab in combination with ipilimumab … CheckMate 511. J Clin Oncol 2019;37:867–875. doi:10.1200/JCO.18.01998; PMID 30811280 | benchmark | Lower ipilimumab dose (NIVO3+IPI1) reduced G3–5 TRAE (34% vs 48%, P = .006) with descriptively similar ORR (45.6% vs 50.6%) | M1.2, M2.2; I1, I2 | Yes |
| L3 | Goldmacher GV et al. Response criteria for intratumoral immunotherapy in solid tumors: itRECIST. J Clin Oncol 2020;38:2667–2676. doi:10.1200/JCO.19.02985; PMID 32552274 | consensus/standard | Standardized framework for separate response assessment of injected and non-injected lesions in IT immunotherapy trials | M2.1; I1 | Yes (metadata; abstract text not returned) |
| L4 | Sharma A et al. Anti-CTLA-4 immunotherapy does not deplete FOXP3+ regulatory T cells (Tregs) in human cancers. Clin Cancer Res 2019;25:1233–1238. doi:10.1158/1078-0432.CCR-18-0762; PMID 30054281 | conflicting | Ipilimumab/tremelimumab increased CD4/CD8 infiltration without depleting intratumoral FOXP3+ cells (quantitative IHC; CyTOF n = 5) | M5.1; I3 | Yes |
| L5 | Arce Vargas F et al. Fc effector function contributes to the activity of human anti-CTLA-4 antibodies. Cancer Cell 2018;33:649–663. doi:10.1016/j.ccell.2018.02.010; PMID 29576375 | supporting/precedent | Fc-dependent intratumoral Treg depletion in hFcγR mice; ipilimumab response associated with CD16a-V158F high-affinity polymorphism in inflamed melanoma | M5.2; I3 | Yes |
| L6 | Hamid O et al. A prospective phase II trial exploring the association between tumor microenvironment biomarkers and clinical activity of ipilimumab in advanced melanoma. J Transl Med 2011;9:204. doi:10.1186/1479-5876-9-204; PMID 22123319 | conflicting with "unexpected" | High baseline FoxP3 (p = 0.014) and IDO associated with clinical activity of ipilimumab | M4.1; I4 | Yes |
| L7 | Spranger S et al. Up-regulation of PD-L1, IDO, and Tregs in the melanoma tumor microenvironment is driven by CD8+ T cells. Sci Transl Med 2013;5:200ra116. doi:10.1126/scitranslmed.3006504; PMID 23986400 | foundational | Tregs/PD-L1/IDO are enriched in T-cell-inflamed melanomas and their recruitment depends on CD8+ T cells | M4.1–4.2; I4 | Yes |
| L8 | Ray A et al. A phase I study of intratumoral ipilimumab and interleukin-2 in patients with advanced melanoma. Oncotarget 2016;7:64390–64399. doi:10.18632/oncotarget.10453; PMID 27391442 | precedent | Injected-lesion response 67%; abscopal response 89%; irRC ORR 40% | M2.1; minor citation | Yes |
| L9 | Romano E et al. Ipilimumab-dependent cell-mediated cytotoxicity of regulatory T cells ex vivo by nonclassical monocytes in melanoma patients. PNAS 2015;112:6140–6145. doi:10.1073/pnas.1417320112; PMID 25918390 | supporting + partly conflicting | Ex vivo ADCC of Tregs by CD16+ monocytes; responders had higher CD68+/CD163+ ratios at baseline and decreased Treg infiltration after treatment | M4.2, M5.1; I3, I4 | Yes |
| L10 | Tumeh PC et al. PD-1 blockade induces responses by inhibiting adaptive immune resistance. Nature 2014;515:568–571. doi:10.1038/nature13954; PMID 25428505 | consistent/benchmark | Pre-existing CD8/PD-1/PD-L1 associated with anti-PD-1 response | M3.1; I4 | Yes |
| L11 | Helmink BA et al. B cells and tertiary lymphoid structures promote immunotherapy response. Nature 2020;577:549–555. doi:10.1038/s41586-019-1922-8; PMID 31942075 | consistent | B cells/TLS associated with ICB response | M3.1; I4 | Yes |
| L12 | Nature Portfolio. Clinical research editorial policy (web page; accessed 2026) | journal policy | Registration before first enrolment; CONSORT; enrolment dates and data-lock date in main text | S0; I7 | Partial (current page; 2025-08 version not verified) |

### High-Level Roll-Up

#### H1 (safety)

- Status: Supported for "meets pre-specified safety threshold, with lower systemic ipilimumab exposure and numerically fewer severe TRAEs than the IV control". Unsupported for "significantly lower" and "equivalent to anti-PD1 monotherapy".
- Strongest evidence: E1.1a with the Fleming rule, and PK (E1.4a).
- Weakest bridge: M1.3.
- Defensible conclusion: IT ipilimumab 0.3 mg/kg + nivolumab met its pre-specified safety endpoint in a Phase 1b trial.

#### H2 (efficacy)

- Status: Unsupported at the stated level ("increased efficacy", "formally demonstrating added value").
- Weakest bridge: M2.1 (non-discriminating comparison).
- Defensible conclusion: IT ipilimumab + nivolumab shows antitumour activity in injected and non-injected lesions. All systemic efficacy readouts are numerically lower than in the concurrent IV arm, and the trial cannot exclude a clinically relevant loss of efficacy.

#### H3/H4 (biomarkers)

- Status: associative, hypothesis-generating. The language of necessity and prediction is unsupported. "Unexpected" is inconsistent with L6/L7.

#### H5 (mechanism)

- Status: Unsupported. Internal readouts conflict.

#### H6

- Status: Unsupported.

## S3 — Issue and Action Ledger

### I1 — Validity-critical

- Affects: H2; M2.1, M2.2; E2.1a, E2.2a; Abstract; Discussion p.19 ("formally demonstrating the added value").
- Problem: the efficacy claim rests on an injected vs non-injected comparison that varies lesion type, selection, denominator and response construct, and lacks an anti-PD1-alone comparator. At the same time, the concurrent randomized control shows numerically inferior systemic efficacy in the IT arm. The Abstract reports only the favourable comparison.
- Consequence: the central clinical proposition (lower toxicity without efficacy loss; IT use in oligometastatic/earlier-stage disease) is not supported. For Nature, the efficacy question determines the significance.
- Required action: (a) Remove "increased efficacy"/"formally demonstrating" language, or re-analyse with a lesion-matched design: injected vs non-injected lesions matched on site and baseline size within patient, using a pre-defined lesion-level criterion (itRECIST where feasible), with CIs and the exact denominators. (b) Report all systemic efficacy endpoints (ORR, PFS, OS, new lesions) side by side in the Abstract with uncertainty (HR with 95% CI, even if descriptive), and position the result against CheckMate 511.
- Evidence-request role: re-analysis = Valid alternative. Claim calibration = Claim-calibration fallback (sufficient for validity). Neither restores Nature-level significance by itself.
- Effect of results: if matched lesions still show higher local response, a local dose-effect claim is reasonable (not "added value on top of anti-PD1"). If not, the claim is withdrawn.
- Status: Drafted.

### I2 — Validity-critical (claim calibration, correctable)

- Affects: H1; M1.1–M1.3; Abstract, Results p.6, Discussion p.17.
- Problem: "significantly lower" has no pre-specified comparison. "Equivalent to anti-PD1 monotherapy" rests on cross-trial comparison (CheckMate 067 nivolumab G3–4 TRAE 16.3%). The primary-endpoint figure (22.6% vs 24.3%), the threshold (30% vs 50%) and the endpoint label (TRAE vs irAE) are inconsistent. The handling of early deaths needs a sensitivity analysis.
- Action: report the primary endpoint exactly as pre-specified, with its 90% (or 95%) CI. State the Fleming rule once, consistently. Add a sensitivity analysis counting the 3 excluded deaths (and the 2 randomized-but-excluded patients) as failures. Describe the between-arm difference as descriptive. Remove "equivalent to anti-PD1 monotherapy". Provide a per-patient AE table (worst grade per patient by arm, including any grade 5) and reconcile the text with Fig. 2b/2d.
- Status: Drafted.

### I3 — Validity-critical

- Affects: H5; M5.1–5.2; Fig. 6e–g; ED Fig. 6d–h; Discussion pp.21–22; Results header p.16.
- Problem: "Selective depletion" and "work in humans just like in mice" rest on a decrease in CD25+CD39+ as a proportion of CD4 (p = 0.032) in pooled arms. Measured as a proportion of CD45 it is not significant (p = 0.053). The CTLA4+ activated subset is unchanged in DCB (p = 0.415), total Tregs increase by deconvolution, FOXP3 IHC is unchanged, and blood Tregs rise. A proportional decrease during effector influx cannot distinguish depletion from dilution, phenotypic change or sampling differences. FcγR expression is associated with DCB but not linked to Treg loss within patients. The genuine controversy (L4 vs L5/L9) is not resolved.
- Consequence: the headline mechanistic insight, which is the main Nature-level conceptual claim beyond the trial, is unsupported.
- Required action: the decisive route is absolute quantification of FOXP3+ (and, if possible, CD25+/CD39+ or CTLA4+) cells per mm² in paired FFPE sections from the same lesion type. Multiplex IHC/IF on existing cores would do this. Show the analysis stratified by arm and by injected vs non-injected lesion (ipilimumab dependence), with a within-patient test of association between FcγR+/CD16+ myeloid density and Treg change. Valid alternative for the Fc link: FCGR3A-158V/F genotyping, if germline DNA exists (precedent L5). Fallback: reframe as "a relative decrease in CD25+CD39+ CD4+ cells, compatible with but not demonstrating depletion", and remove the mouse-equivalence statement.
- Effect of results: an absolute FOXP3+ decrease restricted to DCB and to higher local ipilimumab exposure would support depletion. No absolute change would favour dilution or phenotypic change.
- Status: Drafted.

### I4 — Validity-critical (inferential framework for biomarker claims)

- Affects: H3, H4, H6; Figs 5–6; ED Figs 4–6; Abstract; Discussion.
- Problem: many markers were tested across platforms with unadjusted Wilcoxon tests, and per-group n is not reported. Arms are pooled. Biopsy site differs by arm and time point. On-treatment (W3) features may partly reflect early response (the outcome is defined at 6 months). Multiple readouts with p > 0.05 are described as higher or confirmatory (HLA-I/II IHC, CD20 IHC, CXCL13, CD68/CD163 IHC, CD25+CD39+/CD45, granzyme secretome W3 changes, cancer-cell fraction). "Required", "pre-requisite", "predicting" and "robust predictive biomarkers" are not supported without adjustment, performance metrics or validation. The Treg/M2 associations may index general inflammation (L7). "Unexpected" ignores L6.
- Action: report n per group per panel. Apply FDR control across the pre-defined marker families and distinguish pre-specified from exploratory analyses. Adjust or stratify by arm and by biopsied lesion type. For Treg/M2 features, normalize to total CD45/CD3 or IFNγ/T-cell-inflamed scores, or use multivariable models, to test independence from inflammation. Report AUC with CIs (cross-validated) before using "predictive". Revise the language to association. Cite and discuss L6, L7 and L9 (M2 direction).
- Status: Drafted.

### I5 — Venue-critical

- Affects: overall contribution.
- Problem: after calibration, the defensible contribution is a small randomized Phase 1b meeting a single-arm safety threshold, with descriptive, numerically inferior systemic efficacy, and exploratory biomarker associations that largely confirm known ICB correlates. The efficacy question needed to establish clinical significance cannot be answered by this trial.
- Consequence: below the Nature threshold for conceptual advance unless I3 is resolved convincingly. Resolving I3 would require new tissue analyses whose outcome is uncertain.
- Action: none for the authors beyond I1–I4. The journal-fit judgment goes in the recommendation and confidential comment.
- Status: Drafted (editor comment).

### Minor issues (I6–I16)

- I6: Denominators. Non-injected ORR is 18/40 = 45% in the text vs 50% in the Abstract/Discussion/Fig. 3h. IV ORR is 62% in the text vs about 65% in Fig. 3h/Discussion. Early ipilimumab discontinuation is "13/40 (37.5%)" (= 32.5%), and 25/40 receiving 4 doses implies 15 did not. Injected lesion count: 46 lesions vs 65%×40 one lesion + 27.5%×40 two lesions ≥ 48. G3 irAE is 33% vs 30% (IT) and 62% vs 52.3% (IV) between text and Fig. 2b. Median OS is 50 months in the text vs "not reached for the 2 arms" in the Fig. 3 legend. Fig. 5k n = 149.
- I7: CONSORT/reporting. First/last enrolment dates and data-lock date are missing. The analysis population excludes 2 randomized IT patients (Fig. 1c) and is not ITT. IV arm n = 21 vs 19 planned. There are no CIs for ORR. irRC was a stated endpoint but is not reported. Any grade 5 events or treatment-related deaths should be stated. Registration timing relative to first enrolment should be stated.
- I8: IT procedure details. Volume injected, how 0.3 mg/kg was split across lesions, lesion size rule (≥1 cm³), and whether the injected lesion could also be a RECIST target lesion.
- I9: "Untreated" (Abstract) vs eligibility allowing prior BRAF/MEK therapy in BRAF-mutant patients. Report how many received prior targeted therapy.
- I10: Figure cross-reference errors. "Fig. 2i" should be Fig. 2g right. Fig. 4a/ED Fig. 2a CD4/CD8 are swapped relative to the text. Serum vs plasma labelling. Fig. 1d "Stade". ED Fig. 3a DCB colour key reversed relative to other figures. Methods Figure 1 and Methods Table 2 are not rendered.
- I11: PD-1 decrease on CD8 TILs seen only in the IT arm (Fig. 4a; IV p = 0.834). Discuss whether this reflects the injected-lesion sampling rather than nivolumab target engagement.
- I12: Flow panel change after 9 patients (CD39 added). State n with CD39 data per group and whether any analyses mix panels.
- I13: ED Fig. 1d OS by DCB is subject to guarantee-time bias (DCB requires ≥6-month survival). Use a 6-month landmark or remove. Six patients are unaccounted for (36 + 19 = 55).
- I14: Reference list. Refs 50–53 (cGAMP hydrolysis, chromosomal instability, HSF2BP, BRME1) appear uncited and unrelated. Ray 2016 is mis-summarized (irRC ORR 40% presented as "abscopal response rate"; that abstract reports abscopal response in 89%).
- I15: Data availability is limited to controlled access for clinical data. State deposition of RNA-seq/WES (controlled-access repository) and analysis code.
- I16: CD25+CD39+ is used as a Treg surrogate. Quantify the FOXP3+ fraction within the gate in trial samples where possible (ED Fig. 6a uses 7 external tumours) and acknowledge activated conventional CD4 contamination.

### Recommendation State

- Central bottleneck: the two claims that would make this a Nature paper, preserved/increased efficacy with IT delivery (I1) and a human Treg-depletion mechanism (I3), are not supported. The safety result is solid but modest in scope.
- Scientific validity: the safety primary endpoint is valid. The efficacy, biomarker and mechanism claims are overstated, and some are internally contradicted.
- Venue-level adequacy: insufficient for Nature. The calibrated contribution is appropriate for a clinical/translational oncology journal.
- Realistic revisability: claim calibration is fully feasible. Resolving I3 requires new tissue analyses with an uncertain outcome. I1 cannot be resolved beyond calibration within this trial.
- Preliminary recommendation: Reject for Nature. The work could be suitable, after revision, for a more specialized clinical/translational journal (transfer at the editor's discretion).

## S4 — Draft and Verification

- `peer-review.md` drafted: yes.
- Major Comments mapped to issue IDs: MC1 → I1; MC2 → I2; MC3 → I3; MC4 → I4 (I5 in the recommendation and confidential comment).
- Recommended Revisions: I15, I16 plus the FcγR genotype as optional.
- Minor Comments: I6–I14.
- Recommendation: Reject (transfer suggested in the confidential comment).
- Confidential editor comment: yes.

### Verification

- Quotes and claim verbs: re-checked against the extracted text: "demonstrating an increased efficacy upon intratumoral anti-CTLA4 therapy" (Abstract p.3); "formally demonstrating the added value of anti-CTLA4 on top of anti-PD1 therapy" (p.19); "anti-CTLA4 antibodies work in humans just like in mice by depleting activated tumor-specific Tregs" (p.22); "is a pre-requisite for anti-CTLA- 4 + anti-PD1 efficacy" (Abstract); "equivalent to anti-PD1 monotherapy" (Abstract); "No formal comparison between the 2 arms will be performed" (Methods p.38). Verified.
- Numbers: 9/37 = 24.3%; 28/40 = 70% ≥ 23/38 rule; 18/40 = 45%; 23/35 = 65.7%; 13/40 = 32.5%; deaths 21/40 vs 7/21; new lesions 22.5% vs 9.5%; PK 2.2 vs 42.2 µg/ml. Verified.
- Figure p-values: read from the rendered figures at 110 dpi. Fig. 6e 0.032/0.156; ED 6f 0.053; ED 6g 0.415/0.031; ED 6d 0.008; ED 6e 0.301/0.322; Fig. 6f 0.25; Fig. 5d 0.080/0.054; Fig. 5g IHC 0.084; Fig. 6k IHC 0.169; Fig. 6m IHC 0.221; ED 5f 0.102/0.092/0.099; ED 5g 0.174. Legible, but the OS log-rank p (≈0.19) is small in the image and is reported as approximate.
- Fig. 3h percentages: estimated visually from bar heights; phrased as "appear".
- Literature propositions: L1, L2, L4–L11 verified against Europe PMC abstracts. L3 metadata only.
- Journal assertions: Nature policy verified on the current page only, and hedged accordingly.
- Existing analyses checked: no FDR, no HR/CI, no enrolment dates, no irRC results, no absolute Treg counts, no arm-stratified biomarker analyses (grep and visual review). Confirmed absent.
- OCR artifacts: the Greek letters in cytokine names (IFNγ, TGFβ) were lost in extraction; this was not treated as an error. Line numbers were stripped.
- Unresolved: whether germline DNA exists (the FCGR genotype request is conditional); Methods Table 2 and Methods Figure 1 content.

## S5 — Final Pruning and Decision

- Requested actions classified: MC1 fallback (calibration) required, lesion-matched re-analysis offered as an alternative. MC2 required corrections. MC3 decisive = absolute FOXP3 quantification by arm/lesion, FcγR genotype = valid alternative for the Fc link only, fallback = reframing. MC4 required reanalysis/reporting and calibration.
- Minimum required routes retained: yes.
- Recommended strengthening moved: FCGR genotype (optional), data deposition, FOXP3 fraction within the gate.
- Alternative-route equivalence checked: the reframing fallback in MC3 resolves validity but not venue fit, and this is stated to the editor.
- Duplicated requests removed: "unexpected"/literature points merged into MC4; denominator issues consolidated in Minor 1.
- Final word count and Major Comment count: 1,843 words including headings (roughly 1,750 of body prose), above the style profile's 1,200-word soft limit. Justification: four independent validity-critical issues (efficacy comparison, safety reporting, mechanism, biomarker inference) that cannot be merged without losing distinct remedies, plus a consolidated list of numeric inconsistencies that a clinical-trial report must have corrected. Counts: 4 Major, 3 Recommended, 9 Minor. A further pruning pass removed the S4 draft's duplicated background and compressed Major 3 and the confidential comment; no scientific content was dropped.
- Scientific judgment and recommendation unchanged: yes.
- Earlier stage reopened: no.

### Final Decision Rationale

- Final recommendation: Reject (for Nature). Encourage submission of a calibrated clinical report to a specialized journal.
- Claim-validity basis: the safety endpoint is valid. The efficacy superiority, Treg-depletion mechanism and predictive/necessity claims are unsupported or internally contradicted.
- Venue-completeness basis: the calibrated contribution (Phase 1b safety with descriptive efficacy and confirmatory associations) does not meet a Nature-level conceptual advance.
- Principal remaining issues: I1, I3 (not resolvable within the current data without new tissue analyses of uncertain outcome).
- Why the requested actions are proportionate: mostly re-analysis and calibration on existing data. The only new laboratory work (multiplex IHC on existing FFPE) is needed only if the mechanistic claim is retained.
- Residual uncertainty: exact Fig. 3h values; availability of germline DNA; protocol details not provided.

## Locked Decisions and Handoff

- Exact wording that must be preserved: the quotes listed under S4 verification.
- Inconsistency that must be flagged: primary endpoint 22.6% vs 24.3%; threshold 30% vs 50%; non-injected ORR 45% vs 50%; median OS legend vs text; Fig. 5k n = 149; ED 6g contradiction of depletion.
- Requests intentionally excluded: new clinical trial or anti-PD1-alone arm (not feasible and not proportionate; handled through calibration); single-cell sequencing (supporting characterization only).
- Tone: neutral, firm through evidence.
- Output paths: ai_review/peer-review.md; ai_review/review-dossier.md; ai_review/run-notes.md.
