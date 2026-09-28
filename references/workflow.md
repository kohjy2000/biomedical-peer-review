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

Build literature-grounded field context first (S2a), appraise evidence, claims, and the claim network in three passes (S2b), then run a coverage audit (S2c). Use [review-framework.md](review-framework.md) for scientific judgment.

### S2a. Literature and field context

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

Record one row per proposition in the field knowledge table: layer (background or specific), topic, proposition, context of validity, expected direction or size, related H/M/edge (or entity, for background rows), the assumption it tests or alternative it distinguishes, discriminating readout, source ID, and S2b use status. Keep a row only when it defines a term, states an expected pattern, or bears on a claim. Record facts only; verdicts belong to S2b. Set the initial use status to `Pending`; S2b must later mark each relevant row `Used` or `Set aside` with a reason.

Register every source in the table with its full citation or stable identifier, source role, and verification status. Do not retain an undigested search-result list.

S2a may be delegated when the user and environment permit it. A delegated search receives S0, S1, and the search targets and returns only the proposition table and source register; the main review retains all verdicts and literature dispositions. Otherwise run S2a in the same session with the same output.

### S2b. Claim appraisal

Use the three passes below in the inference-chain order of the study type ([review-framework.md](review-framework.md), section 5), or in S1 order when the type has no chain. The passes are fixed; the prompts within each pass are selected for relevance rather than filled mechanically.

#### Pass A. Evidence adequacy (`E→M`)

For every consequential evidence-to-claim link, determine:

- **inference alignment:** whether the comparison, perturbation or exposure, time point, population, estimand, and endpoint test the distinction made by the claim;
- **measurement validity:** whether the readout, marker, target, or proxy measures the claimed property in this population, age, tissue, species, and assay context;
- **experimental system or model fit:** the model's context of use, whether it preserves the biology needed for this inference, relevant distortions or missing components, and the boundary beyond which complementary evidence is required; when material, follow the protocol from intervention to readout and identify where another path could produce the result;
- **internal validity:** controls, experimental unit, independence, provenance, confounding, selection, batch or leakage, exclusions, missingness, reagent validity, randomization or blinding when relevant;
- **statistical or computational conclusion validity:** effect size and uncertainty, sample size, multiplicity, model assumptions, robustness or sensitivity, validation independence, and exploratory versus confirmatory status;
- **counter-evidence and exact support:** internal results that point the other way, the exact proposition this evidence establishes, and what it does not establish.

Record `Direct / Indirect / Non-discriminating / Contradictory / Not assessable`, the material limitation, and any field-knowledge rows used.

#### Pass B. Individual claim validity (`M`)

For every consequential M#.#:

- state the warrant and hidden premises required to move from the Pass A results to the claim;
- combine the appraised evidence with the relevant S2a propositions, including definitions, expected patterns, support, conflict, and genuine controversy;
- identify the strongest live alternative and whether the current evidence distinguishes it;
- compare expected with observed and retain internal exceptions, negative results, or heterogeneous subgroups;
- identify missing field-standard evidence and directly relevant experimental precedent when they would distinguish the live alternatives;
- state the defensible scope and limits of generalization.

Record `Supported / Partially supported / Unsupported at the stated level / Not assessable`, the evidence that would change the verdict, and the S2a rows marked `Used`. Mark relevant rows not used in the verdict `Set aside` with a reason.

#### Pass C. Claim-network validity (`M→H` and `H↔H`)

For every H# and consequential relationship among headline claims:

- confirm that every necessary M and bridge claim is present and appraised;
- test the full chain for unsupported moves such as association→causation, marker→function, mechanism→phenotype, experimental model→target population, or selected examples→general performance;
- for a composite stimulus or exposure, check whether the acting component and direct mediator required by the chain are actually identified;
- distinguish necessary from sufficient evidence and check temporal order, causal direction, contradictions, circularity, and double counting;
- identify the strongest evidence, weakest required bridge, defensible headline conclusion, remaining overclaim, and observations the authors' explanatory model does not explain;
- judge novelty, disease or phenotype linkage, external replication, and cross-cohort, batch, platform, site, or model comparability when they matter to the headline claim.

H-level status follows the weakest necessary claim or bridge, not an average across figures. These judgments are made here, not at pruning. S5 may compress or merge them but must not reverse them without recording why.

Before raising a point that depends on literature not yet in the table, run a targeted search, add the proposition and source, and record its use.

Record each consequential gap as an issue candidate with its origin and affected H/M/E/K. Do not silently discard candidates before S2c.

### S2c. Coverage audit

Run this only after the three S2b passes. It detects omissions; it does not make a second scientific judgment from a generic checklist.

**Structural coverage**

- every consequential `E→M` link has a Pass A relation or explicit Not assessable flag;
- every consequential M has a Pass B verdict;
- every necessary `M→H` and consequential `H↔H` link has a Pass C judgment;
- every relevant S2a proposition is `Used` or `Set aside` with a reason;
- counter-evidence, negative results, unexplained observations, and unresolved uncertainty remain visible;
- every issue candidate is `Retained / Set aside / Pending` with a reason, and every retained candidate is traceable to H/M/E and relevant K/source IDs.

**Conditional modules**

Use S0 to select only the applicable reporting or risk-of-bias modules from [appraisal-modules.md](appraisal-modules.md). Reporting completeness enables appraisal but does not establish methodological validity. When a module reveals a consequential omission or bias signal, reopen the affected S2b pass and update its judgment; do not promote an unchecked item automatically.

### Gate

Proceed when S2c confirms complete structural coverage or records each remaining Not assessable item; every divergence between expected and observed and every observation the authors' explanatory model leaves unexplained has an alternative or a recorded reason for setting it aside; and each relevant literature proposition and issue candidate has a disposition. Do not treat literature agreement as validation, manufacture controversy, or treat evidence as direct when its comparison varies a correlated state, selection process, time point, or population rather than the attribute named in the claim. Do not claim that a model is distinguished when the data remain compatible with alternatives. Do not carry a specific new experiment into S3 unless its discriminating value is supported by field knowledge or directly relevant literature; otherwise record only the evidence type needed.

## S3. Synthesize

Convert the appraisal into an issue ledger. Assign I# to every retained issue.

### Required output for each I#

- classification: Validity-critical / Venue-critical / Recommended strengthening / Minor;
- affected H#, M#.#, and E#.#a where applicable;
- origin: the step that produced it (S2b Pass A, Pass B, Pass C, S2c conditional module, or Minor sweep);
- exact evidence or manuscript location;
- problem and scientific or editorial consequence;
- required action;
- purpose of any new evidence request;
- role of each evidence request: Decisive / Valid alternative / Supporting characterization / Claim-calibration fallback;
- for a specific new experiment: target inference, relevant precedent, main confounder, and how positive, negative, or null results would change the claim;
- when useful, a decisive test, a valid alternative, and a claim-calibration fallback, treated as alternative routes rather than a cumulative checklist;
- status: Open / Drafted / Resolved / Verification pending.

Also record the central bottleneck, scientific-validity judgment, venue-level adequacy, realistic revisability, and preliminary recommendation.

Perform a publication-quality sweep of methods, statistics, ethics when relevant, reproducibility, data/code access, figures, tables, terminology, and conclusions versus the data range. Promote an issue only when its consequence warrants it.

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
