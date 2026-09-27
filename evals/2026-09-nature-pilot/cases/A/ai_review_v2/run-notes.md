# Run Notes — Blind review, case A (skill_v2)

- **Model:** Claude Opus 5.5 (claude-opus-5-5), run as a Claude Code subagent.
- **Run date:** 2026-09-26. The review was written as of the submission date, 2025-06-24.
- **Skill:** `skill_v2/SKILL.md`. References read: workflow.md, review-dossier-template.md, review-framework.md, review-template.md, style-profile.md. final-pruning.md was read after the draft existed, as the skill instructs. revision-review.md was not read (not applicable).
- **Target:** Nature, initial submission. No journal-specific fields or editor question were given, so standard fields were assumed.

## Materials used
- `blind/preprint_v1_text.md`, read in full.
- `blind/preprint_v1.xml`, consulted only to check Table 1 and the model equations.
- `blind/figures/F1–F20.jpg`, all viewed. The following panels were cropped and upscaled locally to read small labels, and the crops are stored in `ai_review_v2/zoom/`:
  - Fig. 4b axis
  - Fig. 5b
  - Supplementary Fig. S9a axis
  - Supplementary Fig. S10b
  - Supplementary Fig. S11c,d

## Missing materials (marked Not assessable or "not found in available material")
- **Table 1:** image only in the XML and not supplied, so its content was not reviewed.
- **eQTL / ieQTL model equations:** images only. Only the Fig. 1c schematic was available.
- **Supplementary Materials S1–S3 (data tables):** not retrievable. These affect:
  - the per-locus colocalisation details;
  - GSEA results;
  - the per-annotation n used to verify the r² bias quantitatively.
- **Full summary statistics:** not released ("upon publication").

## Sources verified via web search (all published before 2025-06-24)
- Mostafavi et al. 2023 Nat Genet
- Liu et al. 2023 Nat Genet (320 loci)
- Wallace 2020 and 2021 PLoS Genet (coloc priors; coloc–SuSiE)
- Hukku et al. 2021 AJHG
- Urbut et al. 2019 Nat Genet (mashr)
- Kim-Hellmuth et al. 2020 Science
- Yazar et al. 2022 Science
- Yao et al. 2020 Nat Genet (MESC)
- de Lange et al. 2017 Nat Genet (59,957 subjects)
- Pinnell et al. 2015 Immunity (Zmiz1 selective for Notch1 in T cells)
- Lewis et al. 2011 Immunity; Satpathy et al. 2013 Nat Immunol (Notch2 in intestinal cDC2)
- Milano et al. 2004 Toxicol Sci / van Es et al. 2005 (γ-secretase inhibition and goblet metaplasia)
- Oliver et al. 2024 Nature (gut atlas size)
- Tofacitinib JAK selectivity (secondary sources)

Negative search: no PKC-β inhibitor IBD trial was found. In the review this is phrased as a citation request.

Stated from reviewer knowledge without source verification this session:
- approved IL-23-pathway antibodies target the ligand (p19/p40), not IL23R;
- the hg38 position of MYC (not asserted in the review; the authors are asked to report the distance instead).

## Blinding exposures (none opened; recorded for transparency)
1. The search "single-cell eQTL human intestine colon ileum biopsies Crohn's disease colocalization 2024" returned post-cutoff items:
   - a Nature Genetics 2026 listing of the companion TI paper (manuscript ref. 70, Krzak et al.), whose search summary described its cohort size;
   - a bioRxiv item from December 2025;
   - a medRxiv item from January 2026, despite the -site filter.
   None were opened, and none were used in the review.
2. The search `"Zmiz1" "Notch1" Pinnell Immunity 2015 abstract ...` returned, despite `-site:nature.com`, a result titled "Cell-type-resolved genetic variation shapes inflammatory bowel disease risk | Nature" (nature.com/articles/s41586-026-10627-z). This reveals that a version of this manuscript was later published in Nature. The link was not opened, and its content was not seen. The exposure happened after S1–S3 judgments and the recommendation direction were already formed (the dossier was drafted afterwards but reflects earlier appraisal). It is still a blinding breach at the level of "publication outcome known".
3. The Yazar OneK1K search returned a medRxiv item from August 2025 (a different study; not opened). The Mostafavi search returned a Cell Genomics 2025 item of uncertain date (not opened, not used).
- No search used this paper's title or distinctive title phrases. Every search included "-site:nature.com -site:medrxiv.org".

## Skill ambiguities / friction
- **Length target.** The style profile targets 600–1,000 words (maximum 1,200 unless justified). With five independent validity-critical issues plus Nature-level Recommended and Minor sections, the final report is about 2,240 words. The skill does not say whether Recommended and Minor count toward the target.
- **S5 timing.** The dossier template's S5 section is naturally drafted together with S3/S4 in one write. The skill says final-pruning.md must not be loaded before a draft exists, and it was not. The S5 dossier fields were then updated after pruning.
- **Journal-stated requirements.** No Nature reviewer-field instructions were supplied, so "Journal-stated" provenance for Nature's criteria rests on general knowledge rather than a verified source. This is labelled in S0.
- **Classifying I4.** The skill offers a single class per issue, but I4 has both validity-critical wording elements and a venue-critical mechanistic-depth element. It was classified Venue-critical, with the wording issues noted.
- **Figure-derived assertions.** Visual reads from low-resolution JPEGs (r² positions, outlined points) drive parts of Major 3. The skill's verification list does not cover how to phrase these, so they were written with "appears"/"about".
