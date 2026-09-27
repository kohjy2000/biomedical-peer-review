# Adjudication — Case C (NIVIPIT phase 1b, Nature)

Sources: `ai_review/` (report, dossier, run notes); `reference/` (ledger, Peer Review File); `adj/` (preprint, published text, rendered figure and Methods pages).

## 1. Coverage of round-1 referee points

**Major (2/2).** R2-1 and R4-1 both ask for direct IT-versus-IV comparison of the immune data. The AI's Major Comment 4 states that the arms are pooled although the biopsied lesion differs by arm, that "regardless of route" is untested for lack of an arm-by-biomarker interaction, and asks for arm-stratified analysis. Same object, same remedy. Both **Matched** (R4-1's side-note on the "DCB" acronym is not raised). **Major recall = 2/2 = 1.00.**

**Minor (32).**
- Matched (7): R1-1 (lesion-type stratification of response — the AI's central MC1 request is lesion-matched analysis by site); R2-3 (tone down mRNA-based HLA/pre-existing-immunity claim); R2-4 (fresh-sample superiority/"robust predictive biomarkers" unsupported); R2-7 ("unexpected" framing of Treg/M2 contradicted by Hamid 2011 and Spranger 2013); R2-13 (Treg definition/gating validity — surrogate without FOXP3, blood definition, panel change); R2-16 (French "Stade" in Fig. 1d); R4-11 (FcγR association is transcript-only; corroborate at protein level).
- Partial (10): R1-2 (biomarker feasibility — the AI demands validation instead of discussing clinical implementability); R1-3 (PK observation noted in the dossier but not developed); R2-5 (cross-trial versus internal-control ambiguity flagged generically, not at the named passage); R2-6 (over-extension to earlier-stage disease appears only in the dossier); R2-9 (an arithmetic error in the same dropout sentence, not the denominator asymmetry); R2-12 (asks how the mg/kg dose was split, not the flat-versus-weight rationale); R2-14 (injection volume asked; anaesthesia, minimum size, reflux not); R4-3 (enrolment dates requested as CONSORT reporting, not accrual feasibility); R4-4 (per-patient worst-grade AE table, not grade 1–2 procedural events specifically); R4-5 (benchmarked against CheckMate 511/067, not anti-LAG-3).
- Missed (15): R1-4, R1-5, R1-6, R1-7, R2-2 (TDLN and the mismatched dose-leak citation), R2-8 (length/focus), R2-10, R2-11, R2-15 (secretome quantitation), R4-2 (copy-number burden), R4-6, R4-7, R4-8, R4-9, R4-10.

**Minor recall = (7 + 0.5×10)/32 = 12/32 = 0.375.**

The pattern is systematic: the AI captured almost every point about claim strength, statistics and measurement validity, and almost none about presentation, literature placement, clinical context or courtesy edits.

## 2. AI-only issues (not in the referee ledger)

Valid (14):
1. Primary endpoint given as 22.6% (Abstract) and 24.3% (Results), threshold as 30% (Results) vs 50% (Discussion) vs Methods p0=50/p1=70 — partly fixed: the conflicting Discussion number is deleted.
2. Endpoint labelled treatment-related in Methods but immune-related in Abstract/Fig. 2a — fixed in the published abstract.
3. No sensitivity analysis for the three excluded early deaths (Results) — unchanged.
4. Injected-vs-non-injected comparison varies lesion site, selection, denominator (35 vs 40) and response construct (Abstract, Results, Discussion) — the abstract now says "confirming the relationship between intratumoural exposure … and efficacy", but "formally demonstrating the added value" survives in the Discussion.
5. Systemic endpoints all numerically favour IV, no CIs (Fig. 3e,h–j; ED Fig. 1a,b) — "not powered for formal efficacy comparisons" added twice; still no CIs.
6. Treg decrease is relative, during an effector influx, and contradicted by ED Fig. 6d,e,g,h (Results, "Selective … Depletion") — heading and claim kept; the mouse-equivalence sentence softened to depletion only where activated Tregs and FcγR-positive effectors coexist.
7. Text calls the CD45-denominator change significant at p = 0.053 (ED Fig. 6f) — unchanged.
8. Non-significant readouts called higher/confirmatory (Fig. 5d,g; Fig. 6k,m; ED Fig. 5f,g) — partly softened; the granzyme claim leaves the abstract.
9. No per-group n, no multiplicity control (Figs 5–6; Methods) — n now given throughout; multiplicity still absent but disclosed.
10. Necessity/prediction language — "robust predictive biomarkers" and the sensitivity/specificity sentence are gone; "required", "prerequisite", "predict" remain.
11. Numeric reconciliations: ORR 45% (Results) vs 50% (Abstract); 13/40 stated as 37.5%; 46 injected lesions vs ≥48 implied; grade 3 irAE 33%/62% (text) vs 30%/52.3% (Fig. 2b); OS 50 months (text) vs "not reached for the 2 arms" (Fig. 3 legend); "TOTAL (n=149)" (Fig. 5k) — the 37.5% error and the irAE mismatch are gone; the others persist.
12. Guarantee-time bias in OS by DCB, and 36+19 ≠ 61 (ED Fig. 1d) — unchanged.
13. References 50–53 uncited and unrelated — removed.
14. Abstract says "untreated" although BRAF-mutant patients could have had prior targeted therapy — unchanged.

Debatable (3): "equivalent to anti-PD1 monotherapy" as a cross-trial inference (Abstract), a descriptive historical comparison left standing; requiring absolute Treg densities per mm² by arm and lesion, when the authors state 18G cores cannot support intracellular FOXP3 work; requiring FDR control and cross-validated AUCs in a ~20-patient exploratory set.

Incorrect (1): "Methods Figure 1 and Methods Table 2 are missing from the submitted file" (Minor 5). Both are present in the preprint — an artefact of the reviewer's own page rendering, which also drove two "Not assessable" dossier entries.

## 3. Accuracy audit

Numbers: PK values (2.2/42.2; 0.9/8.4 µg ml⁻¹), deaths (21/40 vs 7/21), new lesions (22.5% vs 9.5%), PFS 13.8 months, 9/37 = 24.3%, 28/40 ≥ 23/38, 18/40 = 45%, 23/35 = 65.7%, 13/40 = 32.5%, liver metastases 18/40, and the subgroup direction in ED Fig. 1a,b all check out.

Figure p-values: every value cited (Fig. 6e 0.032/0.156; ED 6f 0.053; ED 6g 0.415/0.031; ED 6d 0.008; ED 6e 0.301/0.322; Fig. 6f 0.25; Fig. 5d 0.080/0.054; Fig. 5g 0.084; Fig. 6k 0.169; Fig. 6m 0.221; ED 5f 0.102/0.092; ED 5g 0.174; Fig. 4a 0.834; Fig. 5k n = 149) matches the rendered figures. Cross-reference claims hold: Figure 2 has no panel "i"; the Fig. 4a axis is CD8 while the text implies CD4; the PK axis reads plasma while the text reads serum.

Literature: all twelve sources verified against Europe PMC; each supports its use, including Larkin 2015 (16.3% vs 55.0%), Lebbé 2019 (34% vs 48%; ORR 45.6% vs 50.6%), Hamid 2011 (FoxP3 p = 0.014), Romano 2015 (higher CD68/CD163 in responders), Sharma 2019, Arce Vargas 2018 (CD16a-V158F) and Ray 2016 (injected 67%, abscopal 89%, irRC ORR 40%) — the last confirming the mis-citation finding.

Errors: one, the "missing" Methods items. One further imprecision: "96% lymph node or skin" is the share of 162 injections, not of the 46 injected lesions.

## 4. Calibration of the main concerns

- Lesion-level versus systemic efficacy: **(a)/(b)**. Correct, and the abstract drops "increased efficacy" and adds the not-powered caveat, but the Discussion keeps "formally demonstrating the added value" — the core over-claim was judged acceptable. Referee 4 praised the authors' caution here.
- Treg-depletion interpretation versus the authors' own panels: **(b)**, with partial softening. The internal tension is real and accurately described, but all three referees accepted the interpretation; the published version explains rather than retracts, and the heading and the p = 0.053 claim survive.
- Inconsistent percentages and thresholds: **(a)**, partly. No referee raised them; several were silently corrected (threshold, arithmetic, irAE percentages) — a genuine AI-only contribution; others persist.
- "Significantly lower" without a formal comparison: **(b)**. Correct on the record, but retained verbatim in the published abstract and tolerated as descriptive.

Overall severity: **too harsh.** Three of the four Major issues were, by the AI's own analysis, fixable by calibration and reporting on existing data; the fourth needed new tissue work only if the mechanistic claim was kept, and the authors kept it with softened wording. Major revision would have been proportionate. The venue judgment was contradicted by the outcome (accepted 27 Feb 2026; Nature 655:219–229).

## 5. Blinding integrity

Page 3 of the preprint PDF carries a Research Square banner naming the Nature version of record and its DOI; the reviewer recorded seeing it, states it did not open or search for it, and logged the exposure in the run notes and the dossier's source set. Internal evidence supports that account: nothing that exists only in the revised paper appears in the review (SCNA analysis, van Pul citation, anti-LAG-3 comparison, the IT-versus-IV Extended Data figure, the graphical summary), the AI misses exactly the presentation-level points the published version silently fixed, and every source it cites predates the stated submission date. The leak is a case-preparation defect, not a reviewer failure: the banner page should be stripped from the blind input in future runs.

## 6. Verdict

1. The AI recovered both Major referee points and about a third of the Minor ones, missing presentation, literature-placement and clinical-context requests almost entirely.
2. Its distinctive contribution was arithmetic and internal-consistency auditing — several of those discrepancies were fixed in the published paper although no referee named them.
3. Factual accuracy is high: numbers, quotations, figure p-values and all twelve cited sources check out, with one false claim of missing Methods items and one denominator slip.
4. Its four headline concerns are scientifically defensible; the published paper softens some of the wording but retains the substance, so referees and editors judged them acceptable for an early-phase mechanistic trial.
5. The recommendation was miscalibrated — reject-for-venue where major revision fitted the AI's own remedy set, against a paper that was accepted.
