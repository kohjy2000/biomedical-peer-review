# Run Notes

## Run metadata

- Model: Claude Opus 5.5 (`claude-opus-5-5`), run as a Claude Code subagent.
- Run date: 2026-09-26.
- Simulated review date / literature cutoff: 2025-07-16 (initial submission to Nature). All literature cited in the review and dossier was published before this date.
- Skill followed: `prcase/skill/SKILL.md`, initial-review mode. Read in this order: `SKILL.md` → `references/workflow.md` → `references/review-dossier-template.md` → `references/review-framework.md` → (at S4) `references/review-template.md` + `references/style-profile.md` → (at S5) `references/final-pruning.md`. `references/revision-review.md` was not read (not applicable to an initial review).
- Stages executed: S0 → S1 → S2 → S3 → S4 → S5, single session, no handoff.
- Outputs: `peer-review.md` (author/editor-facing, English), `review-dossier.md` (confidential working record), this file.

## Manuscript material used

- `blind/preprint_v1_text.md` — full text including Methods, figure legends and reference list.
- `blind/figures/F1.jpg`–`F4.jpg` (main Figures 1–4) and `F5.jpg`–`F8.jpg` (Extended Data Figures 1–4). All eight images were inspected visually.
- One derived artefact: a 3× magnified crop of F7 (Extended Data Fig. 3) panel c, written to `/tmp/f7c.png`, used only to read the ancestry-group sample-size labels. No manuscript content was modified.
- `blind/preprint_v1.xml` was not needed; the Markdown conversion was complete enough for verification.

## Missing materials (judgments marked Not assessable)

Supplementary Information was not retrievable, as stated in the task. The following were therefore not assessable and are flagged as such in the dossier:

- Supplementary Figures 1–10 — in particular Supplementary Fig. 1 (library-prep plate QC, which underpins the exclusion of 51 plates) and Supplementary Fig. 2 (AoU read distribution and the claimed independent replication of the seasonality effect).
- Supplementary Notes 1–3 — including the read-extraction commands and the 2SMR supporting text.
- Supplementary Tables S1–S22 — notably S3 (covariate list), S4/S9/S13 (loci, annotation, fine-mapping), S16–S17 (rare-variant results and the MAGMA∩RVAS overlap), S20 (PheWAS) and S21–S22 (2SMR and its MHC-exclusion sensitivity analysis).
- The supplementary xlsx.

Consequence for the review: Major Comment 2 asks the authors to report the non-MHC MR analysis **in the main text**, phrased so that it remains correct if the analysis already exists in Supplementary Table S22. The same conditional framing was used in the confidential editor comment. Several Minor Comments (e.g. the three different serology-cohort sizes) could in principle be resolved by Supplementary material and are phrased as requests to reconcile, not as assertions of error.

## Literature sources verified (via web search, pre-2025-07-16 only)

| Source | What was verified | Use |
| --- | --- | --- |
| Costello et al., BMC Genomics 19:332 (2018), doi:10.1186/s12864-018-4703-0 | Title, journal, year, DOI; index swapping on patterned Illumina flow cells (HiSeqX/4000/NovaSeq) | Major 1 |
| Burgess & Labrecque, Eur J Epidemiol 33:947 (2018), doi:10.1007/s10654-018-0424-6 | Title, journal, year; binary-exposure MR interpretation caveat | Major 2 |
| Raychaudhuri et al., Nat Genet 44:291 (2012) — manuscript ref 25 | Shared-epitope HLA-DRB1 alleles as dominant seropositive-RA risk; DR4–DQ8 background and T1D | Major 2 |
| Moutsianas et al., Nat Genet 47:1107 (2015) — manuscript ref 26 | HLA class II and MS risk; HLA-A*02:01 protective | Major 2 |
| Orrù et al., Nat Genet 52:1036 (2020) — manuscript ref 30 | 731 immune traits in n = 3,757 Sardinians | Major 3 |
| Hammer et al., Am J Hum Genet 97:738 (2015), PMC4667104 | Anti-EBNA-1 IgG determined by HLA-DRβ1 positions 11 and 26 | Recommended Revision 2 |
| Moustafa et al., PLoS Pathog 13:e1006292 (2017) — manuscript ref 23 | EBV detected in ~14% of 8,000 blood WGS datasets | Novelty positioning |
| Sasa et al., Nat Genet 57:65 (2025) — manuscript ref 43 | WGS-derived blood virome (eHHV-6, anellovirus) in 6,321 Japanese genomes | Novelty positioning |
| Bjornevik et al., Science 375:296 (2022) — manuscript ref 10 | EBV as a near-prerequisite for MS | Internal-consistency argument (MR null for MS) |

General MR practice regarding routine exclusion of the MHC region was confirmed as a widely applied convention rather than a single-source rule, and is presented in the review as standard practice anchored to the manuscript's own methodological references (Burgess & Thompson 2017; Verbanck et al. 2018), not as a citable mandate.

## Internal verification performed

Arithmetic and cross-reference checks recomputed from the text and figure images: 78,771/486,315 = 16.20%; 48,771/313,387 = 15.56%; 1,440/8,790 = 16.38%; 488/491 = 99.39%; 35,703 + 20,477 = 56,180; 56,180 + 304,103 = 360,283 = 360,764 − 481. One genuine discrepancy found: 47,234 + 257,899 = 305,133 against a stated cohort of n = 305,123. The 27 non-MHC locus labels in Fig. 2a were counted against the text. Extended Data Fig. 3c labels were magnified to confirm eur AoU n = 184,949 (main text: 184,948).

Spacing and hyphenation oddities in the converted text ("EBVread-controls", "EBVseron-egative", "sero-positive") were treated as probable JATS/OCR conversion artefacts and are raised only as a consolidated copy-editing line, not as substantive errors.

## Blinding risk encountered

Two web searches returned results that directly implicate the post-submission record for this manuscript. Neither was opened.

1. A search for prior GWAS of EBV DNA load returned a result titled "Host control of persistent Epstein–Barr virus infection | Nature" (nature.com/articles/s41586-026-10274-4), which is almost certainly the published journal version of this manuscript, and a medRxiv link to this preprint itself. The search-result snippet volunteered a summary of that literature, including a sentence describing "a cross-ancestry GWAS of EBV DNA positivity in 617,186 individuals ... 39 independent susceptibility risk loci" and MR supporting an effect on Hodgkin's lymphoma. That snippet text does not match this v1 manuscript (which reports 28 loci in 822k individuals and a null MR for Hodgkin lymphoma) and appears to be drawn from the later published version and/or an independent concurrent paper. **No content from that snippet was used**: no comment, verdict, issue or recommendation in this review derives from it, and none of the numbers or conclusions attributed there appear in the review or the dossier. Readers of this evaluation should nevertheless treat the review as carrying a non-zero contamination risk from having seen that snippet in the search result stream.
2. A second search returned an independent preprint on the same phenotype (a UK Biobank + All of Us EBV-from-WGS study, bioRxiv, posted 2025-07-18), i.e. two days after the assigned submission date. It was not opened and is not cited or referenced in the review, because it postdates the review date and because it is plausibly the "companion paper" excluded by the task rules. Its existence is recorded here only because a real referee in July 2025 would not have had it, and its absence from the review is deliberate rather than an oversight.

Searches were run with `medrxiv.org` and `biorxiv.org` blocked after the first two queries specifically to reduce the chance of surfacing further versions of this preprint.

## Skill ambiguities and friction

- **Dossier size versus the style profile.** `style-profile.md` caps the author-facing report at roughly 600–1,000 words (up to 1,200 for multiple independent critical issues), while the dossier template requests a full per-claim appraisal with literature grounding for every consequential mid-level claim. For a manuscript with this many analytical layers (phenotype derivation, epidemiology, GWAS, RVAS, enrichment, GRS, PheWAS, MR) the dossier necessarily runs many times the length of the review. The skill does not bound dossier length; I recorded literature grounding in full only for the three claim branches that drive Major Comments, and compressed the rest into the claim map and roll-up.
- **Major Comment count.** `style-profile.md` states that a strong initial review "normally has 3–5 Major Comments" but also forbids merging independent critical issues to hit that range. Five independent issues survived S3 triage here (two validity-critical concerning the two headline claims, one validity-critical concerning locus specificity, one venue-critical on statistical support for gene nomination, one venue-critical on data availability). I merged the GRS-overlap and MR issues into a single Major Comment because they share one consequence (HLA pleiotropy) and adjacent remedies, which kept the count at the top of the stated range. The final reviewer-facing body is 1,392 words (1,661 including the Recommendation and the Confidential Comment to Editor), i.e. above the 1,200-word guidance. The style profile permits this when independent critical issues cannot be merged without losing their remedies, which applies here, but the overrun is recorded rather than concealed: a stricter reading of the profile would have required dropping one venue-critical comment or several Minor Comments.
- **"Do not load `final-pruning.md` during S0–S3"** is unambiguous, but the S3 gate already asks for consolidation decisions that anticipate pruning ("consolidate issues only when they share the same scientific consequence"). I performed consolidation at S3 per the gate and left request triage and prose compression to S5, as the workflow directs. Noting this because the boundary between the two consolidation steps is the one place the workflow could be misread.
- **Journal review fields.** No Nature-specific referee form was supplied, so the default field set from `review-template.md` was used, with a Recommendation section and a Confidential Comment to Editor. Nature's actual referee form differs in layout; if the evaluation expects Nature's own fields, that is a mismatch introduced by the absence of the form, not by the skill.
- **Nothing in the skill failed.** All referenced files existed and were readable; no stage could not be completed except where the missing Supplementary Information forced explicit Not assessable flags, which is the behaviour the skill's stop conditions prescribe.
