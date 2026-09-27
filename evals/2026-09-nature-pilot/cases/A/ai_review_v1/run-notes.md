# Run Notes — Case A (blind review)

- Model: Claude Opus 5.5 (claude-opus-5-5), Claude Code agent
- Run date: 2026-09-26 (review calibrated to submission date 2025-06-24)
- Skill: biomedical-peer-review (SKILL.md + workflow.md, review-dossier-template.md, review-framework.md, review-template.md, style-profile.md, final-pruning.md). final-pruning.md was read only after the S4 draft existed, as the skill specifies.
- Mode: Initial review, Nature, S0–S5.

## Materials used
- blind/preprint_v1_text.md (full text); blind/preprint_v1.xml (used only to check whether Table 1 and the equations were in the text).
- All 20 figure images (F1–F6 main; F7–F20 Supp. Figs 1–14). Enlarged crops were made in scratchpad/crops/ for Fig. 4b,c and Supp. Figs 9a, 10b, 11c,d.

## Missing materials (marked Not assessable)
- Table 1: an image in the XML, and not supplied.
- The cis-eQTL and interaction model equations: images, not supplied. Fig. 1c gives only a schematic formula.
- Supplementary Materials S1–S3 (TSV): not retrievable.
- eQTL/coloc summary statistics: not released at preprint.

## Literature verified (web search; all published before 2025-06-24)
- Mostafavi et al. 2023, Nat Genet, doi:10.1038/s41588-023-01529-1
- Wallace 2021, PLoS Genet, doi:10.1371/journal.pgen.1009440 (coloc-SuSiE)
- Urbut et al. 2019, Nat Genet, doi:10.1038/s41588-018-0268-8 (mash)
- Lewis et al. 2011, Immunity, PMID 22018469 (Notch2 and intestinal DCs)
- van Es et al. 2005, Nature, doi:10.1038/nature03659 (GSI causes goblet cell conversion)
- Liu et al. 2023, Nat Genet, doi:10.1038/s41588-023-01384-0 (320 loci)
- Nasser et al. 2021, Nature, doi:10.1038/s41586-021-03446-x (ABC; IBD)
- Chun et al. 2017, Nat Genet, doi:10.1038/ng.3795
- Connally et al. 2022, eLife, doi:10.7554/eLife.74970 (context only)
- XELJANZ US label, section 12.1 (tofacitinib preferentially inhibits JAK1/JAK3 pairs)
- Enzastaurin not FDA-approved (secondary news sources, 2020). I assumed it was still not approved in 2025, and the dossier qualifies this.
- Ensembl GRCh38 MYC coordinates
- medRxiv 2024 doi:10.1101/2024.10.14.24315443 (cell-type blood/gut IBD eQTL; posted Oct 2024). Only the title, date and summary were verified; the full text returned 403 and the author list was not confirmed.
- Not re-verified, relied on general knowledge: which approved IBD biologics target IL-12/23 p40 or IL-23 p19 rather than IL23R. The report states only "No approved IBD therapy targets IL23R directly".

## Blinding risks encountered (disclose)
1. The result list for a search on Nasser et al. 2021 included a nature.com link titled "Cell-type-resolved genetic variation shapes inflammatory bowel disease risk" (s41586-026-10627-z). This is evidently the published version of this manuscript, which reveals that the paper was eventually published in Nature. I did not open it.
2. A search for prior gut single-cell eQTL work ("single-cell eQTL intestinal colon ileum biopsies ... 2024") returned a search-tool summary that quoted the published version's abstract. The quoted text said cell-type eQTLs were "more than 3.5-fold more likely" to colocalise, compared with "over two-fold" in v1. I did not open that page, the medRxiv v2, the PMC copy, or ibdverse.info.
   - Impact assessment: I had already formed the Fig. 3b critique before this exposure. It covers the undefined OR, the lack of CIs, and the point that 2.68/0.75 ≈ 3.6 if All cells is the reference (noted during S1 figure reading). The leaked number could nonetheless have reinforced my emphasis on that point. The Nature-publication knowledge could bias the recommendation toward acceptance; I set the recommendation (Major revision) and the confidential comment from the S3 ledger alone.
   - Mitigation: after exposure, later searches used blocked_domains for nature.com, and I avoided query terms specific to IBD sc-eQTL.
3. I did not access ../reference/ or other case folders.

## Skill issues / ambiguities
- Journal fields: the skill assumes journal-specific fields when provided. None were provided for Nature, so I used the default template. Nature's actual referee form may use different headings; I did not verify its current fields. The skill does not say whether to reconstruct a journal's standard form when it is not supplied.
- Length target: style-profile.md sets 600–1,000 words (a hard ceiling of about 1,200 unless justified). A large multi-claim Nature paper with five independent validity-critical issues exceeded this; the final report is about 1,750 words including headings. The skill allows the exceedance but gives no upper bound or rule for demoting issues. I cut replication and negative-control requests from the report and kept them in the dossier.
- Dossier timing: the template asks for stage-boundary updates. Running in a single session, I wrote S0–S4 in one pass and then patched S5. That is acceptable, but the skill does not say how to record incremental stages when working in a single session.
- Figure-reading uncertainty: the skill has no explicit convention for judgments that rest on low-resolution figure reading, such as which outlined point is which annotation. I phrased the MYC point as a "reconcile" request and recorded the uncertainty in the dossier.
- Blinding: the skill has no guidance for search-engine summaries that leak target-paper content without a click. Adding a recommended practice (e.g., blocked domains or preprint DOI exclusion from the start) would help blind evaluations.
- "Journal-stated" provenance for Nature criteria: I did not fetch Nature's referee guidance, because blind rules allowed it but its content could post-date the cutoff. The dossier therefore labels the Nature row as general knowledge, not re-verified.
