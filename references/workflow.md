# Peer Review Workflow

Use this file only after the open discovery gate in [discovery.md](discovery.md) is complete. It defines the structured verification sequence; [review-framework.md](review-framework.md) defines the scientific judgment standard. For every full initial or revision review, maintain the structured dossier defined in [review-dossier-template.md](review-dossier-template.md). The dossier is both the stage ledger and the retained analytical artifact.

## Entry rules

- A full initial review enters S0 only after `discovery-notes.md` has been saved. Import its D# candidates and source-coverage table into `review-dossier.md` without rewriting or pruning them, then proceed through S5.
- A bounded task starts at the earliest stage needed for that task and records only the relevant dossier sections.
- If a reliable review dossier exists, read it first and do not repeat completed stages unless the manuscript, evidence, or journal context changed.
- Keep the identifiers H# (high-level claim), M#.# (mid-level claim), E#.#a (evidence unit), and I# (review issue) stable.
- Keep the candidate register append-only. D# identifies open-discovery candidates; C# identifies candidates added by mapping, literature, or structured appraisal. Later stages may validate, weaken, reject, or leave a candidate unresolved, but must not erase it.
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
- links from each D# candidate to the H/M/E unit or manuscript location it may affect, without deciding the candidate's validity;
- S2a search targets: the field and keywords for the background layer; the measured phenotypes and readouts, and what each represents biologically; the entities (cells, molecules, loci, pathogens, interventions), variables (such as age, sex, time point, species, and tissue), and design arms in the consequential claims; and the manuscript sentences whose cited references carry a claim.

### Gate

Proceed when every important high-level claim is connected to all necessary mid-level claims and primary evidence locations, including bridge claims, and each consequential evidence unit states what was actually compared and measured. Do not assign verdicts during neutral mapping. If mapping itself exposes a new potential concern, append a C# candidate and defer judgment to S2b.

## S2. Appraise

After open discovery and neutral mapping, build literature-grounded field context (S2a), validate the append-only candidates and visit the evidence, claim, and claim-network layers (S2b), then run a coverage audit (S2c). Use [review-framework.md](review-framework.md) for scientific judgment.

### S2a. Literature and field context

Search the literature only after D0–D1 and S1 are complete. Organize by topic, not by paper. Literature serves two purposes: test and develop existing candidates, and add genuinely new candidates that were not apparent from the manuscript alone.

**Background (field and keywords).** For the manuscript's field and the S1 entities and variables, look for:

- operational definitions and the nearest alternative states;
- the field's current framework: major mechanisms and models, the other half of each axis (ligand or receptor, upstream or downstream), competing mechanisms, and live debates;
- the normal baseline: composition, frequency range, kinetics, known differences by host variables such as age, sex, time, species, or tissue, and the known roles of the cells or molecules involved (effector or regulatory; cause or consequence);
- field-standard methods, and what the experimental system or reagents can and cannot produce;
- conservation across species, species-specific differences, and model organisms or homologous systems in which the claim could be tested.

Prefer reviews, consensus statements, and landmark studies. Keep this layer within the manuscript's field and key entities.

**Specific (candidates and claims).** Using the background vocabulary, search for every unresolved D/C candidate and each consequential H/M claim:

- prior reports of the same or a closely related finding;
- studies that support or contradict the claim;
- directly relevant experimental precedent for the same inference, and external data that could replicate it;
- whether the manuscript's key cited references support the sentences that cite them.

Record one row per proposition in the field knowledge table: layer (background or specific), topic, proposition, context of validity, expected direction or size, related candidate/H/M/edge (or entity, for background rows), the assumption it tests or alternative it distinguishes, discriminating readout, source ID, and S2b use status. Keep a row only when it defines a term, states an expected pattern, or bears on a candidate or claim. Record facts only; verdicts belong to S2b. Set the initial use status to `Pending`; S2b must later mark each relevant row `Used` or `Set aside` with a reason.

When a literature proposition creates a new potentially consequential concern, append a C# candidate immediately. Do not wait for S3 or silently absorb it into background notes.

Register every source in the table with its full citation or stable identifier, source role, and verification status. Do not retain an undigested search-result list.

S2a may be delegated when the user and environment permit it. A delegated search receives S0, S1, and the search targets and returns only the proposition table and source register; the main review retains all verdicts and literature dispositions. Otherwise run S2a in the same session with the same output.

### S2b. Candidate validation and structured appraisal

S2b has two linked tasks. First adjudicate the candidates already found. Then traverse the mapped argument to find material concerns that open discovery or literature missed. Do not turn the traversal into a prose form: clean links receive a compact status row, while detailed reasoning is retained only for candidates and material limitations.

#### Candidate validation

For every D# and C# candidate, locate the exact manuscript evidence and identify the affected H/M/E or claim-network edge. Keep this integrated challenge intact rather than distributing it across separate form fields:

> What must be true for the claim to hold, what is the strongest live biological, technical, or inferential alternative, and do the current comparison, assay, experimental model, and analysis actually distinguish them?

Use the relevant S2a propositions to test the concern. Record the affected link, exact source, integrated challenge, literature used, and one status:

- `Validated`: a consequential problem remains;
- `Weakened`: a narrower concern remains after checking;
- `Rejected`: the manuscript or verified literature resolves the concern;
- `Unresolved`: available material cannot decide it.

Record why. Rejected candidates remain in the register. A new concern discovered during validation receives a new C# identifier.

#### Pass A. Evidence adequacy (`E→M`)

Visit every mapped evidence-to-claim link. Judge, as relevant, inference alignment; measurement validity; experimental-system or model fit for the exact context of use; internal validity; statistical or computational conclusion validity; counter-evidence; and the exact proposition established and not established. Record a compact relation: `Direct / Indirect / Non-discriminating / Contradictory / Not assessable`, plus candidate IDs when a material limitation exists.

#### Pass B. Individual claim validity (`M`)

Visit every mapped M claim. Combine its Pass A results with relevant definitions, expected patterns, prior support or conflict, internal exceptions, and scope. Record `Supported / Partially supported / Unsupported at the stated level / Not assessable`, plus candidate IDs for every material hidden premise, live alternative, missing discriminating evidence, or generalization problem.

#### Pass C. Claim-network validity (`M→H` and `H↔H`)

Visit every H claim, necessary bridge, and consequential relationship among headline claims. Test whether the required M claims jointly support the conclusion, including causal direction, necessary versus sufficient evidence, acting components or mediators, contradictions, circularity, double counting, novelty, and observations the proposed model does not explain. Record the status of each edge and candidate IDs for every material weak bridge or overclaim. H-level status follows the weakest necessary claim or bridge, not an average across figures.

Any material negative or limiting judgment in Pass A, B, or C must append or link a D/C candidate at the time it is made. Do not mention a material concern in appraisal prose without registering it. Before S2c, adjudicate every candidate added during the three passes using the same integrated challenge and status rules. Before validating a candidate that depends on literature not yet in the table, run a targeted search, add the proposition and source, and record its use.

### S2c. Coverage audit

Run this only after candidate validation and the three structured passes. It detects omissions; it does not make a second scientific judgment from a generic checklist.

**Structural coverage**

- the D1 source-coverage sweep includes every available title/Abstract/Results unit, main figure and table, claim-bearing Methods section, and relevant supplement;
- every mapped `E→M` link has a Pass A relation or explicit Not assessable flag;
- every mapped M has a Pass B verdict;
- every necessary `M→H` and consequential `H↔H` link has a Pass C judgment;
- every relevant S2a proposition is `Used` or `Set aside` with a reason;
- counter-evidence, negative results, unexplained observations, and unresolved uncertainty remain visible;
- every D/C candidate remains in the append-only register with `Validated / Weakened / Rejected / Unresolved`, a reason, and traceability to the manuscript and relevant H/M/E/K IDs;
- every material limitation stated anywhere in S1 or S2 links to a candidate rather than remaining only in prose.

**Conditional modules**

Use S0 to select only the applicable reporting or risk-of-bias modules from [appraisal-modules.md](appraisal-modules.md). Reporting completeness enables appraisal but does not establish methodological validity. When a module reveals a consequential omission or bias signal, reopen the affected S2b pass and update its judgment; do not promote an unchecked item automatically.

### Gate

Proceed when S2c confirms complete structural coverage or records each remaining Not assessable item; every divergence between expected and observed and every observation the authors' explanatory model leaves unexplained has an alternative or a recorded reason for its disposition; and each relevant literature proposition and candidate has a disposition. Do not treat literature agreement as validation, manufacture controversy, or treat evidence as direct when its comparison varies a correlated state, selection process, time point, or population rather than the attribute named in the claim. Do not claim that a model is distinguished when the data remain compatible with alternatives. Do not carry a specific new experiment into S3 unless its discriminating value is supported by field knowledge or directly relevant literature; otherwise record only the evidence type needed.

## S3. Synthesize

Convert the appraisal into an issue ledger. Assign I# to every retained issue.

### Required output for each I#

- classification: Validity-critical / Venue-critical / Recommended strengthening / Minor;
- affected H#, M#.#, and E#.#a where applicable;
- origin: the D/C candidate IDs and the step that produced or validated them (D0/D1, S1, S2a, S2b candidate validation, Pass A, Pass B, Pass C, S2c conditional module, or Minor sweep);
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

Before drafting, consolidate issues only when they share the same underlying scientific defect, consequence, and corrective action. Preserve independent critical issues even when they arise from the same figure or claim. Final request triage and prose compression occur in S5; neither step may impose a target number of Major Comments.

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
