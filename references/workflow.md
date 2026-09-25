# Peer Review Workflow

Use this file as the execution sequence and [review-framework.md](review-framework.md) as the scientific judgment standard. For every full initial or revision review, maintain the structured dossier defined in [review-dossier-template.md](review-dossier-template.md). The dossier is both the stage ledger and the retained analytical artifact.

## Entry rules

- A full initial review starts at S0, instantiates `review-dossier.md`, and proceeds through S5.
- A bounded task starts at the earliest stage needed for that task and records only the relevant dossier sections.
- If a reliable review dossier exists, read it first and do not repeat completed stages unless the manuscript, evidence, or journal context changed.
- Keep the identifiers H# (high-level claim), M#.# (mid-level claim), E#.#a (evidence unit), and I# (review issue) stable.
- At the end of each completed stage, update the dossier with the stage output, open verification flags, and one next bounded action.
- Do not advance past a gate merely to begin drafting. If a required input is missing, mark the affected item Not assessable and continue only with independent work.
- Record concise, auditable judgments and their supporting sources. Do not record private chain-of-thought or an unfiltered search history.

## S0. Frame

Establish the scientific and editorial context using [review-framework.md](review-framework.md).

### Required output

- central question and intended contribution;
- article or study type;
- design, data types, population, model, and setting;
- primary claim ambition and intended scope;
- journal scope and expected level of contribution;
- journal review fields and recommendation options, when provided;
- review requirements or evidence expectations relevant to the study, labeled as Journal-stated / Field standard / Reviewer calibration and linked to their basis;
- claim-validity bar;
- venue-completeness bar;
- submission stage and editor question, when provided.

### Gate

Proceed when the study type, claim ambition, and both evidence bars are explicit enough to calibrate the review, and when each consequential journal or genre expectation is either grounded or explicitly labeled as reviewer calibration. Do not infer undisclosed data, samples, resources, or experimental availability.

## S1. Map

Reconstruct the manuscript neutrally as a hierarchical claim–evidence map.

### Required output

- H# for each headline conclusion or principal contribution;
- M#.# for the claims required to support each H#;
- E#.#a for the figures, tables, cohorts, experiments, or analyses supporting each M#.#;
- for each consequential E#.#a, the actual comparison, exposure, perturbation, or estimand; the unit and relevant time point; and the measured endpoint;
- the inferential role the authors assign to that evidence, such as association, necessity, sufficiency, prediction, validation, or generalization;
- authors' wording, verb strength, intended scope, and claimed novelty;
- dependencies among claims, including bridge claims.

### Gate

Proceed when every important high-level claim is connected to all necessary mid-level claims and primary evidence locations, including bridge claims, and each consequential evidence unit states what was actually compared and measured. Do not assign verdicts during neutral mapping.

## S2. Appraise

Evaluate evidence robustness, logical coherence, literature position, controversy, novelty, field evidence standards, experimental precedent, and scope using [review-framework.md](review-framework.md).

### Required output for each consequential M#.#

- evidence verdict: Supported / Partially supported / Unsupported at the stated level / Not assessable;
- claim–evidence relation: Direct / Indirect / Non-discriminating / Contradictory;
- whether the evidence's comparison and endpoint match the causal, temporal, population, or mechanistic distinction made by the claim;
- strongest evidence and material limitation;
- logical gap or competing explanation;
- established knowledge and relevant consensus;
- consistent and conflicting prior evidence;
- genuine controversy or competing model, if present;
- whether the manuscript confirms, extends, contradicts, refines, reconciles, or discriminates;
- the field-standard evidence package for the exact claim, when it affects the judgment;
- when a new experiment may be needed, directly relevant experimental precedent, the inference it can resolve, and its main confounder or limitation;
- limits of generalization.

For every literature source that materially changes a claim verdict, evidence standard, experimental request, novelty judgment, or recommendation, record its full citation or stable identifier, source role, exact proposition supported, affected H/M claim, and verification status in the dossier. Do not retain an undigested search-result list.

Roll these judgments up to each H#, identifying the strongest evidence, weakest bridge, defensible conclusion, and remaining overclaim.

### Gate

Proceed when every headline claim and every mid-level claim necessary to assemble it has a traceable verdict or an explicit Not assessable flag. Do not treat literature agreement as validation, manufacture controversy, or treat evidence as direct when its comparison varies a correlated state, selection process, time point, or population rather than the attribute named in the claim. Do not claim that a model is distinguished when the data remain compatible with alternatives. Do not carry a specific new experiment into S3 unless its discriminating value is supported by field knowledge or directly relevant literature; otherwise record only the evidence type needed.

## S3. Synthesize

Convert the appraisal into an issue ledger. Assign I# to every retained issue.

### Required output for each I#

- classification: Validity-critical / Venue-critical / Recommended strengthening / Minor;
- affected H#, M#.#, and E#.#a where applicable;
- exact evidence or manuscript location;
- problem and scientific or editorial consequence;
- required action;
- purpose of any new evidence request;
- role of each evidence request: Decisive / Valid alternative / Supporting characterization / Claim-calibration fallback;
- for a specific new experiment: target inference, relevant precedent, main confounder, and how positive, negative, or null results would change the claim;
- when useful, a decisive test, a valid alternative, and a claim-calibration fallback, treated as alternative routes rather than a cumulative checklist;
- status: Open / Drafted / Resolved / Verification pending.

Also record the central bottleneck, scientific-validity judgment, venue-level adequacy, realistic revisability, and preliminary recommendation.

Perform a coverage sweep of methods, statistics, ethics when relevant, reproducibility, data/code access, figures, tables, terminology, and conclusions versus the data range. Promote an issue only when its consequence warrants it.

### Gate

Proceed when every proposed Major Comment maps to an H/M/E identifier or exact manuscript location and has a stated consequence and action. A Major Comment must be validity-critical or venue-critical. Separate the minimum evidence needed to resolve the inference from supporting characterization; do not present the latter as an additional required experiment unless it is necessary to interpret the decisive evidence. A named experiment must test the affected claim rather than merely add characterization. An alternative route is acceptable only when it resolves the scientific issue and preserves a contribution appropriate for the current journal.

Before drafting, consolidate issues only when they share the same scientific consequence and corrective action. Preserve independent critical issues and the evidence-request roles recorded in the ledger; final request triage and prose compression occur in S5.

## S4. Draft and verify

Use [review-template.md](review-template.md) for report structure and [style-profile.md](style-profile.md) for voice. Convert the issue ledger into `peer-review.md`; do not expose internal identifiers unless they improve clarity. Preserve the claim map, literature grounding, and full issue traceability in `review-dossier.md`.

Order Major Comments by the central bottleneck, logical dependency, and consequence rather than manuscript order. Each should contain one central problem, its consequence, the minimum required action, and, only when useful, an alternative evidentiary route or claim-calibration fallback.

Before delivery, re-open the source material and verify:

- every quoted phrase and claim verb;
- sample sizes, denominators, percentages, and statistical statements;
- figure, table, panel, section, and page references;
- consistency among Abstract, Results, Methods, legends, tables, and any response letter;
- whether a requested analysis or experiment already exists;
- whether OCR or extraction artifacts created a false discrepancy;
- the exact proposition supported by every cited paper;
- whether a diagnostic criterion, assay standard, or field-standard assertion driving a Major Comment is anchored to an authoritative source or explicitly qualified as uncertain;
- whether each named experiment has a field-grounded rationale, changes the claim under plausible outcomes, and is not presented cumulatively with equivalent alternatives;
- whether Major Comments remain validity-critical or venue-critical;
- whether required and recommended requests are clearly distinguished;
- whether speculation is conditional;
- whether confidential and author-facing comments are consistent;
- whether the recommendation follows from the surviving issues and journal criteria.

### Gate

Record verification outcomes and unresolved questions in the dossier. Proceed to S5 only when verification flags are resolved or explicitly disclosed and every Major Comment and recommendation premise is traceable to the dossier and source material. Do not deliver the draft before S5.

## S5. Final prune

After a complete, source-verified draft exists, read [final-pruning.md](final-pruning.md). Use the S3 issue ledger and S4 draft as the primary inputs. Re-open source material only when a proposed edit could change a factual statement, scientific judgment, evidence bar, or recommendation premise.

This is an editorial decision pass on `peer-review.md`, not a new appraisal. Classify every requested author action, retain the minimum evidentiary route required for each Major Comment, move non-decisive strengthening to Recommended Revisions when the journal permits or omit it, test whether proposed alternatives resolve the same inference, remove duplication, and compress the prose without changing the supported scientific judgment. Preserve the analytical detail in the dossier and update its final action dispositions and recommendation rationale.

### Gate

Deliver `peer-review.md` and `review-dossier.md` only when the checks in [final-pruning.md](final-pruning.md) pass, the author-facing structure follows the journal fields, the dossier reflects the final judgment, and any scientific issue discovered during pruning has been returned to the appropriate earlier stage rather than silently edited around.

## Bounded-task entry points

- **Claim audit:** complete S0–S2 for the claims in scope and return those dossier sections.
- **Literature or novelty audit:** establish the relevant H/M proposition, complete the literature portion of S2, and return the literature-grounding section and source register.
- **Review drafting:** begin at S4 only when a reliable S3 issue ledger exists in the dossier, then complete S5 before delivery; otherwise return to the earliest missing stage.
- **Revision review:** use [revision-review.md](revision-review.md), then re-enter S1–S3 only for new or materially changed claim branches.
- **Draft audit:** inspect the draft against S3 traceability and the S4 verification gate, apply S5, and return the updated issue and verification sections with the revised report.
