# Run Notes — blind review, case B, skill_v2

- Model: Claude Opus 5.5 (claude-opus-5-5), run as a Claude Code subagent
- Run date: 2026-09-26; review simulated as of submission date 2025-07-16 (Nature, initial submission)
- Skill: `skill_v2/SKILL.md`. I read `workflow.md`, `review-dossier-template.md` and `review-framework.md` before S0, `review-template.md` and `style-profile.md` before drafting, and `final-pruning.md` only after a complete draft (S5). I did not read `revision-review.md` because this was not a revision task.
- Outputs: `peer-review.md`, `review-dossier.md` and this file.

## Materials used / missing
- Used: `blind/preprint_v1_text.md` (read in full, 318 lines) and `blind/figures/F1–F8.jpg` (all inspected visually).
- Not read separately: `blind/preprint_v1.xml` (the text file is derived from it).
- Missing / not assessable:
  - Supplementary Figures 1–10, Supplementary Notes and Supplementary Tables S1–S22. This affects:
    - plate-level QC details;
    - the MR results with MHC instruments excluded (S22);
    - HLA imputation QC;
    - locus tables (S4, S9);
    - the SNOMED screen (S2);
    - covariate lists (S3).
  - The review marks these "not found in the available material" rather than absent.
- Folders not opened: `B/ai_review`, `B/reference`, `B/adjudication.md`. These were listed by a directory `ls` of `B/`, but I did not read them.

## External sources verified (all published before 2025-07-16)
- Kachuri et al., Genome Med 12:93 (2020). Checked in PMC full text: EBV VCA p18 and ZEBRA antibody HLA associations include DRB1*04:04.
- Bentham et al., Nat Genet 57:694 (2025). Checked in PMC: ImmuneLENS estimates B-cell fraction from IGH in blood WGS.
- Costello et al., BMC Genomics 19:332 (2018). Index-swap contamination rates, from the search abstract.
- Burgess et al., Wellcome Open Res 4:186 (2023). MR guidelines.
- Burgess & Labrecque, Eur J Epidemiol 33:947 (2018). Binary exposure in MR.
- Rich, Erlich & Concannon, Diabetes in America 3rd ed., Ch. 12 (NIDDK). Checked in the PDF text: MHC accounts for about half of T1D genetic risk, and DR4 haplotypes are high-risk. The publication year (2018) is uncertain.
- Fryer et al., Biologicals (2016), PMID 27461128. WHO 1st International Standard for EBV NAT. Volume and pages not verified.
- Sasa et al., Nat Genet 57:65 (2025). Checked in PMC: EBV was not analysed as a study variable, which was the novelty check.
- Orrù et al., Nat Genet 52:1036 (2020). n=3,757 Sardinians.
- Oelen et al., Nat Commun 13:3267 (2022). The 1M-scBloodNL dataset; basis for the reference-40 correction.

## Blinding exposures (recorded honestly)
1. **Competing preprint surfaced in results.** The search "genome-wide association Epstein-Barr virus DNA load blood whole-genome sequencing reads host genetics 2024" (with -site:nature.com -site:medrxiv.org and domain blocks) returned:
   - Nyeo et al., bioRxiv 2025.07.18.665549 ("Population-scale sequencing resolves correlates and determinants of latent Epstein-Barr Virus infection"), posted after the cutoff;
   - a September 2025 bioRxiv virome preprint;
   - a PMC item on EBV activity and MS host genetics.

   I did not open any of them and did not use them. The tool's automatic summary text did describe their content (for example, 45 EBV loci in the competing study).
2. **Summary text appearing to describe this paper after publication.** A later search ("Epstein-Barr virus reads detected unmapped reads UK Biobank whole genome sequencing 2023 2024 viral DNA blood population prevalence") returned a news-medical.net item dated 2026-02-19 and an ME Association item from January 2026 that mention a Nature publication. I did not open them. The search tool's automatic summary quoted this paper's cohort numbers (486,315 / 336,123; 16.2% / 21.8%) and a line saying EBV-read detection "was validated with laboratory tests". This reveals that a later version appears to include laboratory validation of viral load.
   - Mitigation: the qPCR-benchmark request (Major Comment 1) and the MHC-pleiotropy concern were identified from the manuscript and figures before this search. See the dossier S2 and S3 reasoning: the absence of quantitative validation is grounded in the text itself, where qPCR appears only as a future need in the Discussion.
   - Residual risk: exposure 2 may have raised my confidence that Major Comment 1 is "the right" comment. I stopped any further searches on this topic after it.
3. **nature.com.** I did not fetch nature.com, including its referee guidelines, to avoid exposure. I therefore set the Nature review fields and recommendation options by reviewer calibration.

## Skill ambiguities / friction
- **Journal fields.** The skill asks for journal-required fields, but Nature's referee form could not be consulted under blinding. I used the generic template (Overall, Major, Recommended, Minor, Recommendation, Confidential).
- **Word limits.** The style profile's 600–1,000 word target conflicted with three independent validity-critical issues plus a long list of verifiable minor inconsistencies. The final report is about 1,130 author-facing words (1,249 including the confidential note), which is within the allowed exceedance but required heavy compression of the minor comments.
- **Dossier timing.** The dossier template wants an S5 section, but the final-pruning reference may only be read after the draft. I pre-filled S5 provisionally and then revised it after reading `final-pruning.md`. It would help if the skill said explicitly that S5 dossier fields are completed only after pruning.
- **Choosing a remedy for data the authors may not hold.** The skill says not to infer undisclosed resources, yet the decisive test (qPCR in samples with matched GS) needs samples the authors may not have. I handled this by asking for "any samples with matched blood genome sequencing" and giving a claim-calibration fallback. Whether that fallback is venue-adequate for Nature is flagged only in the confidential note. The skill gives little guidance on when a fallback must be labelled venue-insufficient in the author-facing text.
- **Searches that surface the paper itself.** The skill has no instruction for this situation. Search-engine summaries can leak post-cutoff content even when results are not opened. Adding a rule such as "prefer PubMed/PMC queries by specific cited title" would reduce this.
