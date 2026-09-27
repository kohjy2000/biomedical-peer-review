# Case A adjudication: AI review vs round-1 human referees

Sources: `ai_review/peer-review.md` (report only; dossier-only items are noted), `reference/human_points.md` plus the PRF, the preprint text and figures F1–F20, and the published Nature article (3 Jun 2026). M = Matched, P = Partial, X = Missed.

## 1. Coverage of human points

### Major (ledger; n = 15)

| ID | Ref. label | AI | Basis |
|---|---|---|---|
| R1-1 | major | P | M3: MAML2 mRNA not shown to change Notch output. The general small-effect / mRNA≠protein point is absent. |
| R1-2 | major | P | M1: same "technical vs biological" inference, attributed to power and multiplicity. No sparsity, pseudobulk or allele-of-origin point. |
| R1-3 | none | M | M3: functional evidence, or reframe as hypotheses. |
| R3-1 | none | M | M3 and the confidential note: colocalisation claims are hypotheses. |
| R3-2 | major | X | Novelty relative to prior bulk TSS-distal findings not raised. |
| R3-3 | major | P | M4: other sc-eQTL datasets, but no blood-vs-gut framing. |
| R3-4 | major | M | M4: novelty benchmarked only against OTG. |
| R3-6 | major | P | Mi8 asks for the model. Validity of GT:I colocalisation not questioned. |
| R3-7 | major | M | M1–M3: multiplicity across annotations, spurious assignments, perturbation. |
| R3-8 | major | M | M4: coloc-SuSiE. |
| R3-9 | major | P | M2: formal sign-discordance test (FUBP1, PSEN2). No LD sign-flip or fine-mapping point. |
| R3-10 | major | P | M4: OTG insufficient. The mix of evidence types within OTG is not noted. |
| R3-11 | major | M | M5: IL23R error, direction vs mechanism, safety links as hypotheses. |
| R5-1 | major | P | M3 challenges the pathways but asks for no enrichment test (that request is in the dossier only). |
| R5-2 | major | X | External replication was pruned from the report (dossier only). |

**Major recall = (6 + 0.5×7)/15 = 0.63.** Using the referees' own "major" labels (n = 17: 4 M, 11 P, 2 X): 0.56.

### Minor (ledger; n = 35)

- **M (4):** R1-11, R1-13, R3-13, R5-9.
- **P (7):**
  - R1-6: Mi4.
  - R1-17: Mi9.
  - R3-5: Rec3.
  - R3-20: Rec3 queries the 4.2% figure.
  - R5-3: M4.
  - R5-4: Rec1.
  - R5-5: FDR requested for ieQTLs only.
- **X (24):**
  - R1: 4, 5, 7, 8, 9, 10, 12, 14, 15, 16.
  - R3: 12, 14–19, 21, 22.
  - R5: 6, 7, 8, 10, 11.
  - These are mainly figure legibility, terminology ("regulate", "effector", "colocalised"), code links and references 25–26.

**Minor recall = (4 + 0.5×7)/35 = 0.21.**

**Later-round new points:** none anticipated. The only loose link is R3's round-2 questions on the 33 non-replicated OTG loci and novel genes versus loci, which touch Mi1 and M4.

## 2. AI-only issues

"Pub" gives the status in the published version.

| # | Item | Class | Justification |
|---|---|---|---|
| 1 | M1: power/multiplicity confounds the resolution effect | Valid | Follows from Supp 4 (4/30/217 annotations) and Fig 2b. "Every trend" is overstated. Pub: no matched analysis; OR redefined; Abstract now ">3.5-fold". |
| 2 | M1: Fig 2f p-values from t-tests on bootstrap replicates | Valid | Confirmed in the Methods. |
| 3 | M1: Supp 7 compares only colocalising genes | Valid | Matches the Results wording. |
| 4 | M2: max-r² gated at p < 0.05 favours small-n annotations | Valid | Minimum r² of about 13/4/1% at n = 30/100/400 is correct. Pub: unchanged. |
| 5 | M2: nominated cell type ≠ colocalising annotation (MAML2, ZMIZ1, PSEN2, MYC) | Valid | All figure attributions verified. Pub: PSEN2 narrative rewritten. |
| 6 | M3: MYC risk allele raises a pro-proliferative target, against "impaired renewal" | Valid | Fig 5b and the text. |
| 7 | M3: GWAS p about 1e-6 at MAML2 and PSEN2 | Valid | Fig 4b; Supp 11c. |
| 8 | M3: "protective role" sentence contradicts the model | Valid | Location given wrongly (§3). Pub: retained. |
| 9 | M4: PPH4 threshold "given only for ieQTLs" | Debatable | True of the Methods only. Results and Fig 3 legend give > 0.75 for all eQTLs. |
| 10 | M4: several highlighted genes per locus (ITPKB, NDFIP1, OIP5/NUSAP1/RTF1) | Valid | Verified in Supp 11a,c and Fig 5c. |
| 11 | M5: JAK2/tofacitinib called an error | Debatable | Tofacitinib preferentially inhibits JAK1/JAK3 but also inhibits JAK2 pairs. Pub keeps JAK2. |
| 12 | M5: "PRKCB inhibitors approved for oncology" wrong; conflicts with Methods | Incorrect | ChEMBL lists midostaurin (approved) as a PKC inhibitor. The Methods exclude *therapeutics* trialled in IBD, not genes. Pub: unchanged. |
| 13 | M5: GSI gut toxicity is goblet-cell conversion, not PSEN2 in immune/vascular cells | Valid | Pub deleted the immune/vascular attribution. |
| 14 | Rec1: ieQTL robustness to sparse genotype × inflammation cells | Valid | Fig 5d has 1–6 donors per moderate/severe class. |
| 15 | Rec2: evolutionary model untested | Debatable | Already hedged in the text. Pub: unchanged. |
| 16 | 320 vs 321 loci | Valid | Pub: 321. |
| 17 | 180 vs 104 + 74 = 178 | Valid | Pub: unreconciled. |
| 18 | 104/138 = 75.4% | Valid | Pub: 104/137 = 75.9%. |
| 19 | 82.3%, not 82.2% | Valid | Trivial. Pub: unchanged. |
| 20 | 421 vs 397 individuals | Debatable | 421 is the number recruited. Pub keeps 421. |
| 21 | 1,852,681 vs 1,837,436 cells | Valid | Pub: harmonised. |
| 22 | "2,196,874 million" | Valid | Typo. |
| 23 | Fig 3e does not support DCs being "three of the four" | Incorrect | Within myeloid cells the top four are cDC2 (8), classical monocytes (6), cDC1 (5) and pDC (5). Pub retains the claim. |
| 24 | RPS14 appears only in the Discussion | Valid | Pub: unchanged. |
| 25 | PRKCB sentence duplicated | Valid | Pub: fixed. |
| 26 | Ref 43 does not support "LPIN3 regulates Wnt" | Valid | Ref 43 is about CD8+ T cells in CRC. Pub: same reference. |
| 27 | MYC lead variant about 0.8 Mb from TSS; LINC00824 | Valid | 128.53 vs 127.74 Mb. |
| 28 | de Lange 2017 summary statistics vs Liu 2023 loci | Valid | Confirmed in the Methods. |

**Totals: 22 Valid, 4 Debatable, 2 Incorrect.**

## 3. Factual accuracy audit

- **Verified correct:**
  - Annotation counts, the Fig 2f ratios (all below 1), and the bootstrap t-tests.
  - The OR is undefined, has no CI and is gene-level.
  - The r² arithmetic.
  - All figure-panel attributions.
  - Cohort structure.
  - 4.2% LD overlap.
  - Arithmetic in Minor 1–2, both typos, RPS14.
  - Every quoted phrase matches the preprint verbatim.
- **Literature (Crossref and PubMed):** every citation exists and supports its use:
  - Mostafavi 2023.
  - Urbut mash (online 2018; "2019" is the print year).
  - Wallace 2021 coloc-SuSiE.
  - Lewis 2011 Notch2/cDC.
  - van Es 2005.
  - Nasser 2021 ABC.
  - medRxiv 10.1101/2024.10.14.24315443 (Perée et al., blood/gut IBD eQTL).
  - XELJANZ §12.1 (preferential JAK1/JAK3).
  - Enzastaurin: not approved, which is correct.

**Errors (4):**
1. The "protective role" sentence is placed in the Discussion. It is in the Results.
2. Fig 3e is misread (see item 23 above).
3. PRKCB:
   - "Approved for oncology" is not an error, since midostaurin is an approved PKC inhibitor.
   - The Methods filter is misparaphrased as gene-level.
4. PPH4 threshold "only for ieQTLs" (see item 9 above).

**Overgeneralisations (not counted as errors):**
- The Fig 2f CIs overlap for FANTOM only.
- For MYC, 2 of 3 top annotations are opposite in direction.
- The JAK2 framing.

## 4. Recommendation and severity calibration

- **AI:** Major revision. The confidential note allows for a specialist-journal outcome.
- **Referees:**
  - R1: valid, but needs experiments.
  - R3: major-revision stance.
  - R5: "no flaws that would preclude publication".
- **Outcome:** three rounds, then published in Nature. Changes were text softening plus added comparisons (π1 vs GTEx/Yazar, GO tests, Cuomo counts); no experiments.
- **Match:** Yes. The AI aligns with R3 and the aggregate outcome, and is harsher than R5.
- **Over-weighting:** the AI called M1 (power) and M2 (r² bias) the "main barrier". No referee raised them, they were unaddressed, and the paper was accepted. They are valid, but over-weighted relative to editorial judgement, and the venue-downgrade scenario did not happen.
- **Under-weighting:**
  - Novelty relative to bulk work (R3-2).
  - Replication (R5-2): pruned from the report, yet it became a main-figure addition.
  - Presentation and terminology.
- **Well calibrated:** the drug-target errors were rated as must-fix. IL23R was conceded and the PSEN2/GSI text revised.

## 5. Blinding integrity

The run-notes disclose two passive exposures:
- (a) A search result title revealed publication in Nature.
- (b) A search snippet quoted the published ">3.5-fold".

My assessment:
- **(b):** the "2.68/0.75 ≈ 3.6" note is in the dossier only. The report's OR critique is fully derivable from Fig 3b and the Methods, and R5-9 raised it independently. Influence: low.
- **(a):** could bias the AI toward leniency, but the AI gave Major revision with a harsh confidential note. No evidence of bias.
- **Mitigation:** blocking nature.com was appropriate.
- **Undisclosed residual risk:** the model's knowledge cutoff (June 2026) overlaps the publication date, so parametric exposure cannot be excluded. No comment mirrors author-response content.
- **`../reference/` access:** denied in the notes; not verifiable.

No specific comment appears contaminated.

## 6. Verdict

1. Strength: rigorous figure-level statistical scrutiny (r²-max bias, bootstrap p-values, OR estimand). It found real issues referees missed, several fixed in the published version.
2. Strength: good coverage of validity-critical human themes (causality, coloc-SuSiE, novelty benchmark, drug errors); Major recall 0.63. All citations are real and apt.
3. Weakness: it missed novelty relative to bulk work and pruned replication. Minor recall is 0.21 (figures, terminology, code).
4. Weakness: 4 factual slips and 2 Incorrect comments, two of them inside its own "factual errors" section.
5. Calibration: the recommendation matches the outcome, but the report over-weights power confounding as a venue-level barrier.

**Metrics:** Major recall 0.63; Minor recall 0.21; AI-only 22 Valid / 4 Debatable / 2 Incorrect; factual errors 4; recommendation match: Yes.
