# Changelog

All notable changes to this project will be documented here.

## [Unreleased]

### Changed (v6 draft)

- Full initial reviews now begin with an open manuscript-only discovery pass and source-coverage sweep before the claim map, literature search, appraisal framework, or report format is loaded.
- Discovery candidates are preserved in an append-only register. Mapping, literature, and structured appraisal may add candidates; every material limitation must link to a candidate, and every candidate receives an explicit disposition.
- The three evidence/claim/network judgments now act as post-discovery validation and compact coverage checks. Clean links are not expanded into repetitive prose.
- Literature search occurs after discovery and can both validate existing candidates and generate new ones.
- Default word-count and Major Comment count targets were removed. Independent validated issues may not be dropped or merged for presentation length.

### Changed (v5 draft)

- S2b now uses three explicit appraisal passes: evidence adequacy for each `E→M` link, validity of each individual M claim, and validity of the `M→H`/`H↔H` claim network.
- Experimental systems and models are judged fit-for-purpose against the exact inference and context of use, including preserved biology, distortions, and generalization boundaries.
- S2a remains a two-layer literature investigation and now records the claim or edge informed, the assumption or alternative addressed, and whether each relevant proposition was used or set aside.
- S2c is a structural coverage audit rather than a second scientific checklist. Study-type reporting and risk-of-bias guidance is routed through conditional modules and can only reopen the affected S2b judgment.

### Changed (v4.2)

- The Minor sweep runs in the main review again; a separate sub-agent added cost without improving recall in replicate tests.

### Changed (v4.1)

- Claim appraisal asks separately whether the measured readout captures the claimed property in the population, age, tissue, and species studied, including whether a conventional proxy holds.
- Measured phenotypes and readouts are S1 search targets; background literature search covers cross-species conservation and model systems.
- Claim appraisal (S2b) is grouped under five headings (verdict, measurement, weight of evidence, field knowledge, inference chain) without merging questions, and asks whether the specific acting agent in each step is identified.

### Changed (v4)

- S2 is split into S2a field knowledge (background literature for the field and key entities, then literature specific to each claim; one table of propositions; facts only; run in a sub-agent when available) and S2b claim appraisal in inference-chain order against the manuscript and that table.
- Five general prompts for alternative explanations (measurement, state or time, cause, direction, context); the S2 gate requires an alternative or a recorded reason for every divergence between expected and observed.
- Headline-level judgments add the disease or phenotype link and observations the authors' model does not explain; S1 records unstated prerequisites; each issue records the step that produced it.

### Changed (v3.1)

- Panel review is experimental and runs only on explicit request.
- Replication, novelty against the closest prior work, and cross-cohort comparability are judged per headline claim in S2; pruning may not reverse them without a recorded reason.
- The Minor sweep records findings only (no "none found" cells) and adds a line-by-line terminology read of the title, Abstract, and Results subheadings.

### Changed (v3)

- Minor Comments target high-value issues (verifiability, reproducibility, correct interpretation), defined as eight classes derived from the round-1 referee points of the pilot papers.
- The minor sweep is recorded as a per-figure, per-table, per-Methods-section table in the dossier, with a specific finding or "none found" in every cell.
- Minor Comments are outside the length target; pruning may not remove high-value Minor Comments.


Changes motivated by a pilot comparison of blind skill reviews with real round-1 referee reports for three 2026 Nature papers.

### Changed

- Final pruning now requires every Validity- or Venue-critical ledger issue to appear in the report or carry a recorded drop reason, with explicit keep/move/drop decisions for replication, novelty-versus-prior-resources, cross-cohort comparability, and data/code availability issues.
- Compressed quotations, claim verbs, counts, and scope statements are re-verified against the source after pruning.
- The recommendation is derived from a remedy-profile check: Reject requires an issue that cannot realistically be resolved within revision or a calibrated claim below the journal threshold; venue-decisive severity must be justified against field norms for the study type.
- Verification requires a documented full-text search before stating that any item is absent, and a check that figure-based statements read the panel at the correct grouping level.
- The S3 coverage sweep includes a checklist of commonly raised Minor Comment classes.

## [0.2.0-beta] - 2026-09-24

### Added

- A persistent `review-dossier.md` as the second default artifact for full initial and revision reviews.
- Structured retention of journal and genre calibration, claim–evidence maps, literature grounding, issue traceability, verification, and decision rationale.
- Explicit provenance labels for journal-stated requirements, field standards, and reviewer calibration.

### Changed

- Replaced the transient review-state template with a combined review-dossier and session-state template.
- Final pruning now compresses only the reviewer-facing report while preserving the analytical dossier.
- Revision reviews update the existing dossier and retain the evidence for resolved issues.

## [0.1.1-beta] - 2026-09-24

### Changed

- Renamed the project and skill to `biomedical-peer-review`.
- Removed personal naming from the reviewer-facing title and style profile.
- Documented the tested GPT-5.6 Sol/high baseline and the provisional Claude Opus/high starting point for full scientific appraisal.

## [0.1.0-beta] - 2026-09-24

### Added

- S0-S5 workflow for initial biomedical manuscript review.
- Hierarchical high-level claim, mid-level claim, and evidence-unit mapping.
- Evidence robustness, logical coherence, literature positioning, controversy, novelty, and venue-calibration framework.
- Domain-grounded experimental request rules.
- Revision-review workflow and resolution ledger.
- Review-state template for long sessions and handoffs.
- Final-pruning pass for request triage and compression.
- Codex and Claude Code installation guidance.

### Safety and privacy

- Added explicit controls against transmitting confidential peer-review material.
- Public feedback requires public, synthetic, or de-identified examples.
