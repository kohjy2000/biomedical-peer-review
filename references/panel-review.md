# Panel Review

Use this mode only when the user explicitly requests a panel review. It is experimental and has not been benchmarked against single-reviewer mode; do not select it on your own. It simulates how an editor assembles complementary referees, so that biological interpretation, method, and significance are each examined by a reviewer whose priorities differ.

## P0. Assign the panel (editor role)

After S0 and S1 are complete, define three reviewer roles from the manuscript itself:

| Role | Expertise | Derived from |
|---|---|---|
| **R1 — Domain** | the biological field of the headline claim (cell type, tissue, pathway, disease biology) | the object of H1 and the main biological literature cluster cited |
| **R2 — Method** | the principal data type and analysis that carry the evidence (e.g., statistical genetics, mass-spectrometry proteomics, single-cell or spatial omics, flow and functional assays, clinical epidemiology) | the measurement and analysis behind the consequential E units |
| **R3 — Significance** | clinical, translational, or population relevance when the manuscript claims it; otherwise a second domain perspective adjacent to R1 | the implication and generalization claims in the Abstract and Discussion |

For each role, record in the dossier: a one-line expertise profile, what this reviewer usually prioritizes, the lens files it will load (see `lenses/`), and why this role fits the manuscript. Define roles by expertise only; never name or imitate a real person.

## P1. Shared material

All reviewers receive the manuscript, S0 calibration, and the neutral S1 claim–evidence map. These are descriptive and do not contain judgments. Nothing from S2 onward is shared.

## P2. Independent reviews

Each reviewer runs S2–S5 independently, in a separate session or sub-agent that cannot see the other reviewers' appraisal, ledger, or report. Each reviewer:

- appraises every headline claim from its own expertise, loading its lens files during S2;
- performs the S2 literature work that its role requires (for R1, how comparable studies in the field established mechanism and physiological relevance; for R2, field standards and known limitations of the method; for R3, what the result would change for patients, populations, or the field);
- applies the normal S3 ledger, S4 verification, and S5 pruning rules to its own report;
- writes `peer-review-R1.md`, `peer-review-R2.md`, or `peer-review-R3.md` and its own dossier section.

Do not harmonize wording or remove overlaps between reviewers; independent agreement is informative.

## P3. Editor synthesis

A separate editor step reads the three reports and dossier sections and writes `editor-summary.md`:

- consensus issues (raised by two or more reviewers) and single-reviewer issues that are validity-critical;
- conflicts between reviewers, with the evidence each relies on, and which way the editor leans and why;
- the decisive required actions, combined into one list without duplicates;
- a recommendation derived from the remedy profile across all reports (see review-framework.md, section 7).

The editor does not edit the reviewers' reports. When the user asks for a single report, the editor summary plus the three reports are the deliverable; do not merge them into one voice.

## Deliverables

- `peer-review-R1.md`, `peer-review-R2.md`, `peer-review-R3.md`
- `editor-summary.md`
- `review-dossier.md` with shared S0/S1, the P0 panel assignment, and one S2–S5 section per reviewer
