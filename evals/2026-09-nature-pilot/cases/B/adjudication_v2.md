# Case B adjudication, skill v2: AI review vs round-1 Nature referees

Same rules as v1 `adjudication.md`: round-1 points only, ledger category, rebuttal-only answers count, and recall = (Matched + 0.5×Partial)/total. As in v1, a ledger-Major point raised only at Recommended or Minor weight scores Partial at most. The published paper was not re-opened.

## 1. Coverage

**Major (13)**

| Result | Points | Basis |
|---|---|---|
| Matched (4) | R2-1, R3-1 | MC1 asks for a qPCR/ddPCR benchmark and says the fitted simulation shows only compatibility |
| | R3-3 | MC1 says the 1- vs ≥2-read comparison can't separate load from other read-count determinants |
| | R5-12 | MC3 raises MHC pleiotropy and asks for MR without MHC instruments |
| Partial (7) | R1-3 | Lane test of singletons; no exclusion proposed |
| | R1-4 | Minor 6: content matches but at Minor weight |
| | R2-2 | Criticises plate-level QC design, not the exclusion threshold |
| | R2-3 | No coverage request |
| | R3-5 | Recommended 3 imputation accuracy |
| | R5-2 | Per-antibody data used without the lytic argument |
| | R5-5 | Same contamination concern, different remedy |
| Missed (2) | R2-4, R5-1 | Latent vs lytic. "Lytic" appears nowhere in the report or dossier, so the point was never identified, not pruned |

**Major recall = 7.5/13 = 0.58.** Scoring R1-4 as Matched would give 0.62.

**Minor (26)**

- **Matched: 0.**
- **Partial (6):**
  - R2-8: MS MR status (Minor 4).
  - R2-9: removing "first … high specificity" is asked only as a fallback.
  - R3-6: Recommended 3 questions the HLA conditioning.
  - R3-7: the 12 unmapped alleles in replication (Minor 6).
  - R3-8: MC3 uses the A*02:01 and DRB1*04:04 facts.
  - R5-6: per-antibody correlations against Fig 2c.
- **Missed (20):** R1-1, R1-2, R2-5, R2-6, R2-7, R2-10, R2-11, R3-2, R3-4, R3-9, R5-3, R5-4, R5-7 to R5-11, R5-13 to R5-15.

**Minor recall = 3/26 = 0.12.** Compared with v1, R5-3 (depth) and R5-13 (ancestry, which the dossier deliberately excluded) are now Missed, and R5-6 dropped from Matched to Partial.

## 2. AI-only issues

| Item | Verdict | Justification |
|---|---|---|
| MC2: B-cell fraction confounding (ImmuneLENS, conditional re-estimation) | **Valid** | See below |
| MC1: 99.4% is specificity for serostatus, not load | Valid | Correct reading of Fig 1d |
| MC1: lane-level index misassignment | Debatable | Plausible (Methods confirm NovaSeq S4); authors later used allele frequency and qPCR; lane metadata availability uncertain |
| MC3: liability-scale interpretation | Valid | Standard caveat (Burgess & Labrecque 2018) |
| Rec 1: serology concordance understated; power of the Fig 4d null | Valid | ED Fig 2b–c r=0.64 and 0.45; Kachuri 2020 lists DRB1*04:04 for p18 and ZEBRA (verified) |
| Rec 2: former vs never smoking | Valid | Non-selection by BIC is not a null estimate |
| Rec 3: amino-acid/haplotype conditioning | Debatable | Refinement; allele-level conditioning is common |
| Rec 4: candidate-gene wording | Valid | Correct scope; IEI subset P=0.055 |
| Minor 1: summary statistics and code | Valid | "Upon reasonable request"; only extraction commands supplied |
| Minor 2: serology n values | Valid | 9,281 / 6,531 / 6,065 confirmed |
| Minor 3: h² scale | Valid (trivial) | Scale not stated |
| Minor 4: MS in ED Fig 4 vs text | Valid | ED Fig 4 legend lists MS as significant |
| Minor 5: RA class I claim at P<0.1 | Valid | "(*)" in Fig 4f |
| Minor 7: nine corrections | 9 Valid | Fig 2 c→b; ED 3d 4f→4g; "(i)…(i)"; A*2:01; weighted mean/mode; clipped Fig 4e bar; ref 40; refs 4/6 duplicate; 490,294/490,293 |
| Minor 7: 26 vs 21 cell types | Debatable | Recurred from v1; 21 may be the post-filter count |

**Tally: 20 Valid, 3 Debatable, 0 Incorrect.**

**B-cell confounding.** No referee raised it, and the PRF does not discuss B-cell abundance. The concern is grounded:

- The reservoir is memory B cells, yet the only composition covariate is lymphocyte % (UKB has no B-cell subsets).
- "Not confounded by memory B cell abundance" rests on a non-MHC-only comparison with a 3,757-person GWAS (r=0.34, P=0.112).
- The remedy is feasible in existing WGS (Bentham 2025, verified).

One part is debatable: the claim that affected loci "should not be described as determinants of EBV control". Reservoir size is arguably host control of persistence.

**The v1 blood-cell covariate misreading did not recur.** v2 acknowledges lymphocyte % as a covariate and asks for a B-cell-specific quantity that is not in the covariate set.

## 3. Factual accuracy (peer-review.md)

**Verified correct:**
- All numbers (cohort sizes, 61.9%, 99.4%, Fig 1g 0.08–0.27, ED Fig 2, MS P 1.06×10⁻⁴ → 0.056, OR 1.21/1.86, 12 unmapped alleles), plate-only QC, all quotes and all Minor 7 items.

**Literature: all verified.**
Kachuri 2020 (Genome Med 12:93), Bentham 2025 (Nat Genet 57:694), Oelen 2022 (Nat Commun 13:3267; ref 40 is van der Wijst 2018); others as in v1.

**Errors: 0.**

**Imprecisions (not counted):**
1. IKZF3 is listed among "loci". The preprint names it only as a gene-level IEI hit; the 17q12 locus is labelled GRB7.
2. "Few seronegative individuals" for the Fig 4d null: that n is not stated in the main text.

**v1 errors did not recur.** The 24-vs-7 gene-scope error, the blood-cell covariate misreading and the "lytic-cycle antigens" overgeneralisation are all gone. The last is gone because the lytic framing is absent entirely.

## 4. Calibration and recommendation

Both versions recommend **Major revision**, which matches the referees and the outcome (accepted after substantial new data).

**Improved:**
- MR is no longer a venue gate. MC3 is claim calibration with an explicit fallback ("shared HLA architecture", remove causal language), which is nearly what the authors did.
- The venue hinge is now phenotype validity, with qPCR as the decisive minimum. The authors delivered qPCR in two cohorts, which resolves v1's "too cautious" weakness.
- Statistical-rigour points were demoted to Recommended or Minor.

**Still mis-weighted:**
- Latent vs lytic is now absent (v1 had it as Recommended), although it was Major for two referees and drove the title change.
- Cross-cohort comparability appears only at Minor weight.
- B-cell confounding is a Major point that no referee raised: defensible, but an extra burden on the authors.

## 5. Skill-change checks

**(i) Dossier issues kept or dropped with reasons.** Partly met.
- I1–I3 (Validity-critical) became MC1–3.
- I15 and the strain-variant analysis were dropped with reasons.
- Two items were dropped silently: the I1 "restrict cases to ≥2 reads" sensitivity (which would have Matched R5-5) and the I3 outlier-robust estimators.
- Cross-cohort covariate comparability, the v1 miss, survived. It is logged in S5 coverage preservation (I14 → Minor 6) but was never escalated.

**(ii) Recommendation from a remedy profile.** Met. S5 labels each action Minimum / Fallback / Recommended. The proportionality line ("two of three majors resolved with existing data") yields Major revision.

**(iii) Wrong "absent/missing" assertions.** None found. Checked: qPCR (appears only as a future need), lane/index analysis, B-cell fraction, imputation accuracy, deposition and code. MHC-excluded MR is correctly described as missing from the "main text" (it is in Supplementary Table S22).

**(iv) Minor recall.** Worse (0.19 → 0.12). Heavier compression and an issue-first design left biology extensions, presentation points and epistasis uncovered. The dossier's minor-class checklist has no "biology extension / reader interpretation" class.

## 6. Delta v1 → v2

| Metric | v1 | v2 |
|---|---|---|
| Major recall | 0.62 (4/8/1) | 0.58 (4/7/2); 0.62 if R1-4 Matched |
| Minor recall | 0.19 (3/4/19) | 0.12 (0/6/20) |
| AI-only V/D/I | 12/4/1 | 20/3/0 |
| Factual errors | 3 (+3 imprecisions) | 0 (+2 imprecisions) |
| Report length (wc) | 1,661 | 1,249 |
| Recommendation | Major revision; MR venue-decisive | Major revision; remedy-derived; phenotype validity is the venue hinge |

## 7. Blinding exposure and the qPCR request

A search summary gave the cohort numbers, said detection "was validated with laboratory tests", and revealed publication in Nature.

**Against influence on identification:** v1 (without the snippet) already proposed qPCR/ddPCR; the preprint's Discussion names qPCR; R2 and R3 asked for it independently.

**For influence on its firmness:**
- v2 hardened it from one option ("either qPCR … or in-silico decomposition") to "Minimum required (decisive)", the hindsight-correct direction; the run notes concede raised confidence.
- The remedy-profile rule is a competing explanation; outputs were written within 47 s, so file times cannot confirm the claimed ordering.

**Judgement:** influence on the request is low; influence on its severity is low to moderate. Training-data contamination (knowledge cutoff June 2026) is again unmentioned.

**Metrics:** Major recall 0.58 (4 Matched / 7 Partial / 2 Missed of 13); Minor recall 0.12 (0/6/20 of 26); AI-only 20 Valid / 3 Debatable / 0 Incorrect; factual errors 0 (+2 imprecisions); recommendation match: yes.
