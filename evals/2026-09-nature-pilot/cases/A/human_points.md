# Case A — Human peer-review ledger (round 1)

Source: `prf_s41586-026-10627-z.txt` (Nature Peer Review File, CC BY 4.0). Manuscript: cell type-resolved sc-eQTL map (IBDverse) and IBD risk.

## Header
- Substantive referees in round 1: **3** (Referee #1, #3, #5). Referees #2 and #4 are one-line co-review notes (excluded).
- Round structure in file: Version 0 (round 1), Version 1 (round 2), Version 2 (round 3; Referee #3 only).
- Editor decision: **not stated** in the PRF (no editor letter included).
- Counts (our category): **15 Major / 35 Minor** (50 points). By referee: R1 3/14, R3 10/12, R5 2/9. R1 opening-summary concerns are itemised separately from its 13 numbered comments, and numbered comment 4 is split in two (R1-7, R1-8).

Severity column = referee's own label ("major"/"minor"), or "none" if the referee did not label it. Category = our call (Major = would change validity or venue decision if unaddressed; Minor = presentation/clarification).

## Round-1 points

| ID | Ref. signal | Our cat. | Topic | Paraphrase | Author outcome | Note |
|---|---|---|---|---|---|---|
| R1-1 | major | Major | mechanism/functional validation; clinical interpretation | Biological weight of small per-cell-type eQTL effects is unclear, especially as mRNA levels poorly predict protein level/activity. | rebutted | Argued genetic support for drug targets and pathway convergence justify small effects; no new data. |
| R1-2 | major | Major | statistics | scRNA sparsity limits robustness; pseudobulk use questions the "single-cell" framing; allele of origin unknown; statistical handling of technical vs biological factors needs elaboration. | rebutted | Justified pseudobulk (literature, QC filters); declined allele-specific analysis; pointed to new GTEx/Yazar replication note. |
| R1-3 | none (opening) | Major | mechanism/functional validation; novelty | No experimental validation, single methodology, and candidate-gene links rest on existing literature rather than new biology. | text changed/claim softened | Added Discussion sentence that perturbation is needed to establish causality; no experiments. |
| R1-4 | none | Minor | novelty/literature | Lists related genetics+single-cell work (non-IBD) and a bulk IBD eQTL study; notes this work is more than incremental. | not addressed | Largely positive remark; authors only thanked. |
| R1-5 | none | Minor | presentation (over-interpretation) | Results text hard to follow; some molecular-genetic assertions (e.g., line 168 conclusion on ieQTLs) not supported by data. | text changed/claim softened | Sentence rewritten; manuscript edited for clarity after internal review. |
| R1-6 | none | Minor | presentation | Link statistical eQTL/GWAS associations to molecular concepts more clearly (e.g., enhancer-alignment statement, line 148). | text changed/claim softened | Statement reworded with explicit reference to prior enhancer enrichment work. |
| R1-7 | none | Minor | mechanism/functional validation | Chromatin structure/accessibility and TF-binding at identified loci not examined. | rebutted | Declared beyond scope of effector-gene nomination. |
| R1-8 | none | Minor | presentation | "Colocalized" used ambiguously (physical vs statistical sense). | text changed/claim softened | Formal definition of colocalisation added at first use. |
| R1-9 | none | Minor | causal inference (terminology) | "Effector cell type/gene" labels are vague given association-only data. | text changed/claim softened | Operational definition added. |
| R1-10 | none | Minor | causal inference (terminology) | Saying eQTLs "regulate" expression is not justified from association data alone. | text changed/claim softened | Reworded to "associated with"; kept germline-direction argument. |
| R1-11 | none | Minor | cohort/confounding | Recruitment and sample provenance unclear; UC mentioned but not recruited; were ileal/rectal biopsies from different people and handled in analysis; phenotype metadata thin. | text changed/claim softened | Clarified no UC patients, same-donor sampling, one pseudo-sample per person; metadata to EGA. |
| R1-12 | none | Minor | cohort/confounding | Twice as many cells targeted for IBD vs controls; how was depth handled; report cells and genes/cell pre/post QC by group. | new analysis/data added | New Supp Fig comparing CD vs healthy cell number and depth (depth not different). |
| R1-13 | none | Minor | presentation | Typo in reads-per-cell figure (line 525). | text changed/claim softened | Corrected. |
| R1-14 | none | Minor | presentation | Redundant repetition of MS4A1 (line 607). | text changed/claim softened | Corrected. |
| R1-15 | none | Minor | novelty/literature | Refs 25–26 (metallothionein, non-intestinal tissues) do not support the enterocyte metal-ion-binding protective claim. | text changed/claim softened | Named leading-edge MT genes; added tissue-specific references incl. intestine. |
| R1-16 | none | Minor | presentation (over-interpretation) | "Inter-individual differences" claimed without analysing variability across individuals. | text changed/claim softened | Sentence replaced (same edit as R1-5). |
| R1-17 | none | Minor | presentation | Lines 193–203 report findings with no accompanying figure or data. | text changed/claim softened | Added pointer to Supplementary Material S2; no new figure. |
| R3-1 | none (opening) | Major | causal inference | Counting overlapping/colocalising loci across any gut cell type is insufficient to claim causal roles in pathogenesis. | text changed/claim softened | Discussion sentences added framing results as hypotheses needing experiments. |
| R3-2 | major | Major | novelty/literature | Distal-from-TSS pattern for cell-type-specific eQTLs already reported with bulk data; acknowledge and state what is truly new. | text changed/claim softened | Prior work cited; novelty reframed as hierarchical resolution and GWAS-coloc enrichment. |
| R3-3 | major | Major | novelty/literature; replication | How many IBD genes from gut immune cells were missed by blood sc-eQTL studies (Yazar, Perez)? | new analysis/data added | Comparison to Cuomo et al. 2025 PBMC sc-eQTL added to text (novel genes/loci counted). |
| R3-4 | major | Major | novelty/literature | How many colocalised target genes are new vs prior bulk/sc studies, and what design features drove extra discovery? | new analysis/data added | New Fig 3c (CD-sample fraction vs effector discovery) and expression-level analysis; novelty counts vs Open Targets. |
| R3-5 | major | Minor | cohort/confounding; replication | Test disease-vs-control effect-size heterogeneity in terminal ileum (cf. Nishiyama 2024); highlight value of both sample sets. | rebutted | Declared beyond scope; cited existing ieQTL/disease-fraction evidence; offered to do later if required. |
| R3-6 | major | Major | statistics | Clarify ieQTL model (I vs GT:I term) and whether colocalising the GT:I signal with GWAS is a valid shared-causal-variant test. | text changed/claim softened | Methods clarified (GT:I used, prior set); supporting simulation shown in rebuttal only. Pressed again in round 2. |
| R3-7 | major | Major | causal inference; mechanism/functional validation | Colocalisation in any cell type is weak causal evidence (LD, multiplicity across many cell types); KO/variant editing needed for selected loci. | text changed/claim softened | Limitation/experimental-need sentences added; no experiments. |
| R3-8 | major | Major | statistics | Single-causal-variant assumption may fail; use SuSiE-based fine-mapping/coloc to strengthen colocalisations. | rebutted | Declined (uneven power across cell types); limitation sentence added to Discussion. |
| R3-9 | major | Major | statistics; causal inference | FUBP1 opposite-direction effects across cell types could be LD-induced sign flips; was the same causal variant fine-mapped in all cell types? | rebutted | LD-clumping and conditional analysis in rebuttal only; manuscript unchanged. Pressed again in round 2. |
| R3-10 | major | Major | replication; novelty/literature | Open Targets benchmark mixes eQTL, pQTL and in-silico evidence; compare against each source separately. | rebutted | Stated benchmark used molecular-QTL colocs only; Methods wording clarified. Pressed again in round 2. |
| R3-11 | major | Major | clinical interpretation | Drug target/repurposing and side-effect arguments are conjectural; eQTL direction for ITGA4/JAK2/IL23R not checked; diarrhoea side-effect reasoning single-gene. | new analysis/data added | Direction-of-effect plots added (Supp Fig S12); IL23R removed as erroneous; side-effect reasoning defended. |
| R3-12 | minor | Minor | presentation | Fig 2a: unclear how resolutions yield 384 annotations. | text changed/claim softened | Legend expanded. |
| R3-13 | minor | Minor | presentation | Fig 3a vs text: Open Targets locus count mismatch (137 vs 138). | text changed/claim softened | Corrected. |
| R3-14 | minor | Minor | presentation | Fig 3e cited out of order. | text changed/claim softened | Citation added so panels are sequential. |
| R3-15 | minor | Minor | presentation | Fig 4b colours hard to read; colour regional plots by LD (also Fig 5a–c). | text changed/claim softened | Plots redrawn coloured by in-sample LD. |
| R3-16 | minor | Minor | presentation | Fig 6 x-axis labels overlap. | text changed/claim softened | Spacing/text enlarged. |
| R3-17 | minor | Minor | presentation | Fig S7: define "maximum specificity of expression" in legend. | text changed/claim softened | Legend defined. |
| R3-18 | minor | Minor | presentation | Fig S13 uninformative and illegible. | text changed/claim softened | Figure removed. |
| R3-19 | minor | Minor | presentation (methods) | State whether sex in ieQTL models is self-reported or genetically inferred. | text changed/claim softened | Methods: verified by genotype and XIST/Y expression. |
| R3-20 | minor | Minor | statistics | ieQTL–eQTL overlap at a relaxed LD threshold (r2>0.1); are these lead variants? | new analysis/data added | Multi-threshold overlap added as Supp Fig (max ~14% overlap). |
| R3-21 | minor | Minor | presentation | Effector-cell-type analysis: lead eQTL or lead GWAS variant? | text changed/claim softened | Clarified lead eQTL variant (text and Methods). |
| R3-22 | code | Minor | data/code availability | Colocalisation script inaccessible; QTL-mapping repo generic, not study-specific. | new analysis/data added | Config files added; colocalisation repo made public. |
| R5-1 | major | Major | statistics | Notch/Wnt pathway emphasis lacks enrichment testing against a null; is 2/13 cDC genes more than chance? | new analysis/data added | Targeted GO over-representation tests added (both nominally significant). |
| R5-2 | major | Major | replication | Validate eQTLs against external datasets (GTEx for "all cells", Yazar for blood) to rule out dataset-specific artefacts. | new analysis/data added | pi1 replication vs GTEx and Yazar added (Supp Note, Fig 2e). |
| R5-3 | major | Minor | novelty/literature | Discuss relation to other sc-eQTL GWAS-overlap work (e.g., Yazar) and prior evidence for Notch/Wnt in IBD genetics. | new analysis/data added | Counts vs Open Targets/Cuomo for Notch/Wnt genes; Discussion expanded with monogenic IBD literature. |
| R5-4 | major | Minor | clinical interpretation (ieQTL) | Interaction-eQTL interpretation imprecise; e.g., RNF14 "inflamed enterocytes" claim although inflammation is scored at tissue level. | text changed/claim softened | Inflammation score described as sample-level; RNF14 wording adjusted. |
| R5-5 | major | Minor | statistics | Significance threshold and multiple-testing correction for eQTL discovery not stated in main text or Methods. | text changed/claim softened | Detailed multiple-testing Methods section added; FDR stated in main text. |
| R5-6 | minor | Minor | presentation | Small text and pale colours across figures (Fig 4b, 5, 6). | text changed/claim softened | Figures enlarged/rotated/redrawn. |
| R5-7 | minor | Minor | presentation | Fig 2e values lack units. | text changed/claim softened | Units added. |
| R5-8 | minor | Minor | presentation | Fig 3a numbers outside pie unexplained. | text changed/claim softened | Legend clarified. |
| R5-9 | minor | Minor | presentation | Fig 3b odds-ratio axis not explained. | text changed/claim softened | Axis and legend rewritten. |
| R5-10 | minor | Minor | presentation | Redundant "quality control and QC" (Methods line 600). | text changed/claim softened | Corrected. |
| R5-11 | minor | Minor | data/code availability | Colocalisation code link broken. | new analysis/data added | Repository made public at new URL. |


## Consensus issues (raised by 2+ referees)
1. **Causality not established / need experimental validation** — R1-1, R1-3; R3-1, R3-7 (and R3-11 for drug claims). Outcome: limitation text only; no experiments. R1 still flagged this in round 2.
2. **Robustness/replication and novelty vs existing eQTL resources (GTEx, Yazar/Cuomo, Open Targets)** — R1-2; R3-3, R3-4, R3-10; R5-2, R5-3. Outcome: substantial new comparison analyses.
3. **Statistical-method transparency (thresholds, ieQTL model, framework)** — R1-2; R3-6, R3-20; R5-5.
4. **Interaction-eQTL interpretation overstated/unclear** — R1-5, R1-16; R3-6; R5-4.
5. **Terminology of effector cell type / lead variant used** — R1-9; R3-21 (authors fixed with one shared edit).
6. **Colocalisation code unavailable** — R3-22; R5-11.
7. **Figure legibility** — R3-12..R3-18; R5-6..R5-9.

## Later-round points that were NEW (not raised in round 1)
Round 2 (Version 1):
- R3 (minor, presentation): remove boxes around some panels (e.g., Fig 4a–b, 5a–c); move overlapping pie-chart text in Fig 3a; reposition "0.75x" label in Fig 3b; reduce overlapping axis labels in Fig 4b and Supp Fig 15; add "lead variant = diamond" to Fig 5 legend; use more distinct colours for "novel" vs "in OTG"; drop y-axis label in Fig 6.
- R3 (code): eQTL-mapping repo lacks README; pseudobulking/eQTL scripts not findable.
- R3 (specific new asks attached to earlier comments): report what fraction of Cuomo et al. colocalisations this study misses and what drove study-only discoveries (ext. of R3-3); show real GT:I colocalisations have cell states with significant main genotype effect and high GWAS PIP (ext. of R3-6); explain the 33 Open Targets loci not replicated and 26 loci with different effector genes, and whether 257 novel genes lie only at the 74 new loci (ext. of R3-10).

Round 3 (Version 2):
- R3 (code): pi1 replication repository not yet public.

Not new (re-raised): R1 round 2 repeats the mechanism/experimental-validation concern (R1-1/R1-3); R3 round 2 re-presses fine-mapping for FUBP1 sign flips (R3-9).
