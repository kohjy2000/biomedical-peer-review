# Changelog

All notable changes to this project will be documented here.

## [Unreleased]

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
