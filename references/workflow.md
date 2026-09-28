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
- dependencies among claims, including bridge claims and unstated prerequisites the chain relies on (for example, a condition the proposed mechanism requires);
- S2a search targets: the field and keywords for the background layer; the measured phenotypes and readouts, and what each represents biologically; the entities (cells, molecules, loci, pathogens, interventions), variables (such as age, sex, time point, species, and tissue), and design arms in the consequential claims; and the manuscript sentences whose cited references carry a claim.

### Gate

Proceed when every important high-level claim is connected to all necessary mid-level claims and primary evidence locations, including bridge claims, and each consequential evidence unit states what was actually compared and measured. Do not assign verdicts during neutral mapping.

## S2. Appraise

Build the field knowledge first (S2a), then appraise each claim against the manuscript and that knowledge (S2b). Use [review-framework.md](review-framework.md) for scientific judgment.

### S2a. Field knowledge

Before appraising any claim, search the literature in two layers, background first. Organize by topic, not by paper.

**Background (field and keywords).** For the manuscript's field and the S1 entities and variables, look for:

- operational definitions and the nearest alternative states;
- the field's current framework: major mechanisms and models, the other half of each axis (ligand or receptor, upstream or downstream), competing mechanisms, and live debates;
- the normal baseline: composition, frequency range, kinetics, known differences by host variables such as age, sex, time, species, or tissue, and the known roles of the cells or molecules involved (effector or regulatory; cause or consequence);
- field-standard methods, and what the experimental system or reagents can and cannot produce;
- conservation across species, species-specific differences, and model organisms or homologous systems in which the claim could be tested.

Prefer reviews, consensus statements, and landmark studies. Keep this layer within the manuscript's field and key entities.

**Specific (claims).** Using the background vocabulary, search for each consequential H/M claim:

- prior reports of the same or a closely related finding;
- studies that support or contradict the claim;
- directly relevant experimental precedent for the same inference, and external data that could replicate it;
- whether the manuscript's key cited references support the sentences that cite them.

Record one row per proposition in the field knowledge table: layer (background or specific), topic, proposition, context of validity, expected direction or size, related H/M claim (or entity, for background rows), discriminating readout, and source ID. Keep a row only when it defines a term, states an expected pattern, or bears on a claim. Record facts only; verdicts belong to S2b.

Register every source in the table with its full citation or stable identifier, source role, and verification status. Do not retain an undigested search-result list.

When sub-agents are available, run S2a in a sub-agent that receives S0, S1, and the search targets and returns only the table and the source register; keep all verdicts in the main review. Otherwise run S2a in the same session with the same output.

### S2b. Claim appraisal

Appraise each consequential M#.# in the inference-chain order of the study type ([review-framework.md](review-framework.md), section 5), or in S1 order when the type has no chain.

**1. Verdict**

- evidence verdict: Supported / Partially supported / Unsupported at the stated level / Not assessable;
- claim–evidence relation: Direct / Indirect / Non-discriminating / Contradictory.

**2. Measurement**

- whether the evidence's comparison matches the causal, temporal, population, or mechanistic distinction made by the claim;
- whether the measured readout captures the property the claim names in this population, age, tissue, and species; when a conventional proxy is used (for example, BMI for adiposity, a transcript for function, read counts for load), whether the convention holds here;
- whether the choice of marker, target, or analysis is justified.

**3. Weight of evidence**

- strongest evidence and material limitation;
- whether the effect is large enough to matter functionally;
- internal counter-evidence: the manuscript's own readouts that point the other way;
- limits of generalization.

**4. Against field knowledge** (cite table rows)

- whether the central labels meet their operational definition and are distinguished from the nearest alternative state;
- expected versus observed: where they diverge, name the alternative explanation (see the five prompts in review-framework.md, section 2) and one request that would discriminate it;
- prior evidence that supports or conflicts with the claim, including genuine controversy or competing models;
- whether the manuscript confirms, extends, contradicts, refines, reconciles, or discriminates.

**5. Inference chain** (for each step; cite table rows)

- whether the experimental system or reagent can, in principle, produce the claimed result: walk through the protocol step by step and note where it could fail;
- whether the specific acting agent is identified: which component of a composite stimulus or exposure acts, and what directly binds or mediates the next step;
- the field-standard evidence the claim lacks and, when a new experiment may be needed, directly relevant experimental precedent and its main limitation.

Before raising a point that depends on literature not yet in the table, run a targeted search and add the rows.

Roll these judgments up to each H#, identifying the strongest evidence, weakest bridge, defensible conclusion, and remaining overclaim.

For each H#, also record an explicit judgment, with its basis, on:

- external replication or independent validation: is it present, and is it needed for the claim at this venue?
- novelty or added value relative to the closest prior datasets, resources, or studies;
- whether the link to the disease or phenotype named in the claim is shown or only assumed;
- comparability across cohorts, batches, platforms, or sites, when the claim pools or contrasts them;
- observations the authors' model does not explain: results in the manuscript, including secondary ones, and established observations in the field knowledge table that the model leaves unexplained or contradicts, each with the alternative that would explain it.

These judgments are made here, not at pruning. S5 may compress or merge them but must not reverse them without recording why.

### Gate

Proceed when every headline claim and every mid-level claim necessary to assemble it has a traceable verdict or an explicit Not assessable flag, and every divergence between expected and observed, and every observation the model leaves unexplained, has an alternative explanation or a recorded reason for setting it aside. Do not treat literature agreement as validation, manufacture controversy, or treat evidence as direct when its comparison varies a correlated state, selection process, time point, or population rather than the attribute named in the claim. Do not claim that a model is distinguished when the data remain compatible with alternatives. Do not carry a specific new experiment into S3 unless its discriminating value is supported by field knowledge or directly relevant literature; otherwise record only the evidence type needed.

## S3. Synthesize

Convert the appraisal into an issue ledger. Assign I# to every retained issue.

### Required output for each I#

- classification: Validity-critical / Venue-critical / Recommended strengthening / Minor;
- affected H#, M#.#, and E#.#a where applicable;
- origin: the step that produced it (S2b manuscript evidence, S2b field knowledge, H-level judgment, or Minor sweep);
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

#### Minor sweep

Target **high-value minor issues**: problems that do not change the main judgment but affect whether a reader can verify, reproduce, or correctly interpret a result. These classes are high value:

- consistency of counts, denominators, thresholds, and version or cohort sizes across Abstract, Results, Methods, legends, and tables;
- statistical reporting: test used, n per group, independence of observations, multiple-testing correction, effect sizes with uncertainty;
- data, code, and summary-statistic availability, including whether stated links or accessions exist;
- terminology and claim-verb precision, including the title and Abstract (causal or regulatory verbs, disease-state or infection-state terms, cell-type and population names);
- cohort and sample description needed for interpretation: ancestry, sequencing depth, batch or site, sex, covariate definitions, inclusion and exclusion;
- Methods detail needed to reproduce a reported analysis;
- statements of clinical or biological context, or placement relative to the closest prior work, that exceed or misstate the evidence;
- figure elements that prevent reading a key result (illegible labels, missing axes, undefined symbols on a panel that supports a claim).

Typography, stylistic preferences, and cosmetic figure edits on panels that do not support a claim are low value; include them only when trivial to state.

Apply the classes to each main figure, main table, and Methods section that supports a headline or consequential mid-level claim. Record only findings, as a list in the dossier: location, class, problem. Do not record "none found" entries. If a class could not be checked for a supporting item (for example, missing supplementary files), state that once with the reason.

Separately, read the title, the Abstract, and every Results subheading line by line for terminology and claim-verb precision, including whether key concept terms meet the field's definition (S2a background), and record each finding with its exact wording.


Promote a finding to a Minor Comment when it is high value; promote it further only when its consequence warrants it.

### Gate

Proceed when every proposed Major Comment maps to an H/M/E identifier or exact manuscript location and has a stated consequence and action. A Major Comment must be validity-critical or venue-critical. Separate the minimum evidence needed to resolve the inference from supporting characterization; do not present the latter as an additional required experiment unless it is necessary to interpret the decisive evidence. A named experiment must test the affected claim rather than merely add characterization. An alternative route is acceptable only when it resolves the scientific issue and preserves a contribution appropriate for the current journal.

Before drafting, consolidate issues only when they share the same scientific consequence and corrective action. Preserve independent critical issues and the evidence-request roles recorded in the ledger; final request triage and prose compression occur in S5.

## S4. Draft and verify

Use [review-template.md](review-template.md) for report structure and [style-profile.md](style-profile.md) for voice. Convert the issue ledger into `peer-review.md`; do not expose internal identifiers unless they improve clarity. Preserve the claim map, field knowledge, and full issue traceability in `review-dossier.md`.

Order Major Comments by the central bottleneck, logical dependency, and consequence rather than manuscript order. Each should contain one central problem, its consequence, the minimum required action, and, only when useful, an alternative evidentiary route or claim-calibration fallback.

Before delivery, re-open the source material and verify:

- every quoted phrase and claim verb;
- sample sizes, denominators, percentages, and statistical statements;
- figure, table, panel, section, and page references;
- consistency among Abstract, Results, Methods, legends, tables, and any response letter;
- whether a requested analysis or experiment already exists. Before stating that any item, analysis, covariate, figure, table, or threshold is absent, missing, or not reported, search the full text, Methods, legends, tables, figure panels, and any supplementary index, and record in the dossier where you looked. If supplementary material is unavailable, write "not found in the available material" rather than "absent";
- whether each figure-based statement reads the panel at the grouping level, axis, and comparison the figure actually shows;
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
- **Literature or novelty audit:** establish the relevant H/M proposition, complete S2a for it, and return the field knowledge table and source register.
- **Review drafting:** begin at S4 only when a reliable S3 issue ledger exists in the dossier, then complete S5 before delivery; otherwise return to the earliest missing stage.
- **Revision review:** use [revision-review.md](revision-review.md), then re-enter S1–S3 only for new or materially changed claim branches.
- **Draft audit:** inspect the draft against S3 traceability and the S4 verification gate, apply S5, and return the updated issue and verification sections with the revised report.
