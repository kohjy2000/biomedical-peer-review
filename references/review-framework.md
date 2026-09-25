# Biomedical Peer Review Framework

Use this reference for the scientific judgments made in stages S0–S3 of the workflow. It defines the claim structure, evidence and logic appraisal, literature positioning, evidence-bar calibration, and issue tiering. The workflow controls order; this file controls judgment.

## 1. Hierarchical claim–evidence architecture

Use stable identifiers throughout the review:

- **H1, H2... — High-level claims:** headline conclusions or principal contributions.
- **M1.1, M1.2... — Mid-level claims:** experimental, analytical, mechanistic, or interpretive propositions required to support a high-level claim.
- **E1.1a, E1.1b... — Evidence units:** specific observations, experiments, cohort comparisons, analyses, figures, or tables supporting a mid-level claim.

Use as many claims as the argument requires. Do not force a fixed count.

### Neutral claim map

```markdown
H1 — [High-level claim in the authors' wording]
- Verb strength and claim level:
- Intended scope:
- Claimed novelty:

  M1.1 — [Mid-level claim]
  - Role in H1:
  - E1.1a — [Figure/Table/Result and observation shown]
    - Actual contrast or estimand:
    - Unit, time point, and endpoint:
    - Authors' intended inference:
  - E1.1b — [Figure/Table/Result and observation shown]
  - Evidence type: observational / associative / predictive / perturbational / validation
  - Direct or indirect support:
  - Internal counter-evidence or limitation:

  M1.2 — [Repeat as needed]

- Logical assembly:
- Missing bridge or hidden assumption:
```

Preserve the authors' wording and verb strength during extraction. Keep the authors' claim separate from the reviewer's description of what the evidence establishes. Build the map before assigning verdicts.

## 2. Evidence robustness

Assess each mid-level claim before rolling the judgment up to its high-level claim.

### Relevance and directness

- What exposure, perturbation, group, state, time point, or model actually differs in the comparison, and what endpoint is measured?
- Does that comparison isolate the attribute named in the claim, or could it primarily reflect a correlated state, selection process, history, or population difference?
- Does the evidence directly test the proposition, or is it merely compatible with it?
- Is the endpoint a valid measure of the claimed biological, clinical, or methodological property?
- Does the result demonstrate function, or only expression, phenotype, correlation, or potential?

Record the relation of each consequential evidence unit to its mid-level claim:

- **Direct:** the comparison and endpoint test the distinction made by the claim.
- **Indirect:** the result supports a required premise but does not itself test the full proposition.
- **Non-discriminating:** the result is compatible with the claim but also with a live alternative because the decisive attribute was not isolated.
- **Contradictory:** the result materially conflicts with the claim as stated.

### Design and provenance

- Are the comparison groups, controls, sampling frame, and experimental units appropriate?
- Are confounders, batch effects, leakage, selection effects, and data provenance addressed?
- Are validation data independent of model construction or hypothesis generation?

### Analysis and uncertainty

- Are the statistical or computational analyses appropriate to the design and unit of inference?
- Are effect sizes, uncertainty, biological replication, and multiple testing handled adequately?
- Do sensitivity, stability, or robustness analyses support the result where material?

### Validation and triangulation

- Is the result reproduced across relevant cohorts, models, donors, experiments, or analytical choices?
- Does an orthogonal method test the same proposition rather than a neighboring one?
- Is the breadth of validation proportionate to the stated scope and journal context?

### Alternatives and scope

- What credible alternative explanations remain?
- Does the claim stay within the sampled tissue, population, model, time frame, and assay resolution?
- Are negative results, internal exceptions, or heterogeneous subgroups obscured by an aggregate conclusion?

Use one internal verdict for each mid-level claim:

- **Supported**
- **Partially supported**
- **Unsupported at the stated level**
- **Not assessable**

For each high-level claim, confirm that every necessary mid-level claim and bridge has been appraised, then identify the strongest evidence unit, the weakest mid-level claim or bridge, the exact defensible conclusion, and the smallest correction or additional evidence that would change the verdict. Do not average away a critical weak link because the paper contains many figures.

## 3. Logical coherence

Test individual inferential steps and the full chain:

> observation → interpretation → mechanism → generalization or implication

Flag when the manuscript converts:

- marker expression or transcriptional state into demonstrated function;
- association into causation;
- cross-sectional similarity into developmental trajectory;
- pathway requirement into the identity or source of an upstream signal;
- additive effects into synergy without an interaction test;
- selected examples into general performance;
- computational association into therapeutic or clinical utility;
- one possible mechanism into the exclusive mechanism without excluding alternatives or mixtures.

Also check for missing bridge claims, necessary conditions treated as sufficient, conflicting definitions, circular construction and validation, high-level conclusions dependent on one unsupported mid-level claim, and conclusions compatible with several competing models.

## 4. Literature positioning, field standards, and experimental precedent

Anchor literature assessment to a specific H or M claim rather than collecting background references.

Assess four distinct questions:

1. **Novelty:** What is established, and what does the manuscript genuinely add?
2. **Consistency and controversy:** Does the claim agree with prior evidence, and which competing model or unresolved dispute is relevant?
3. **Field evidence standard:** What evidence package is normally needed for this exact level of claim in this field and study context?
4. **Experimental precedent:** How have prior studies directly tested or discriminated the same causal or mechanistic inference, and what limitations of those designs are known?

```markdown
Claim ID:
- Exact proposition:
- Established knowledge:
- Current consensus or governing standard:
- Prior evidence consistent with the claim:
- Prior evidence inconsistent with the claim:
- Genuine controversy or competing models:
- Possible source of disagreement:
  - species / tissue / cell state / disease stage / cohort
  - experimental model / assay / endpoint / definition / analytical method
- Position of the manuscript:
  - confirms / extends / contradicts / refines / reconciles / discriminates
- Does the evidence distinguish competing models or remain compatible with several?
- Field-standard evidence package for this claim:
- Directly relevant experimental precedent and its limitation:
- Genuine contribution:
```

Use, as needed:

1. foundational work establishing the concept, method, or competing models;
2. consensus papers, guidelines, or benchmarks defining the current interpretation or evidence standard;
3. directly relevant primary studies supporting, contradicting, qualifying, or experimentally testing the claim;
4. recent updates when the field or standard is moving.

These are search layers, not paper-count quotas. Do not manufacture a controversy where none exists.

Interpret literature carefully:

- Agreement with prior work is not automatic validation of the present study.
- Disagreement is not automatically a flaw; a well-supported conflict may be the main contribution.
- Compatibility with one model does not distinguish it from another model making the same prediction.
- Apparent conflict may reflect context dependence rather than universal contradiction.
- A manuscript claiming to resolve a controversy must test the competing explanations.

Classify contribution as confirmation, context extension, integration or resource contribution, framework refinement, reconciliation, evidence favoring one side of a controversy, direct discrimination among models, or a new mechanism, method, predictive capability, or clinical application.

Prefer primary studies for specific propositions and authoritative guidelines or benchmarks for standards. Verify title, authorship, year, journal, DOI or PMID, and the exact proposition supported. Distinguish Must-cite work from Recommended context and Optional background.

If a proposed Major Comment depends on a diagnostic criterion, assay standard, or other field norm rather than on the manuscript's internal logic alone, anchor that norm to an authoritative guideline, consensus, benchmark, or directly relevant primary study. If the standard cannot be verified, qualify the judgment and avoid presenting it as settled.

## 5. Evidence-bar and journal calibration

### Claim-validity bar

The minimum evidence needed for the exact claim to be scientifically defensible. This depends on claim level, study design, unit of inference, and intended scope.

### Venue-completeness bar

The breadth, mechanistic depth, triangulation, generalizability, and significance needed for the manuscript to constitute a sufficient contribution for the current journal.

Journal level does not change whether a narrow claim is valid. It may change whether the complete evidence package is adequate for publication there. Treat journal level as a calibration factor, not permission to create an experimental wish list.

Calibrate using the study type, claim ambition, intended scope, field-standard controls, rarity of material, journal scope, and the paper's own framing of novelty and significance. Do not infer that the authors possess undisclosed samples, data, or resources.

### Genre calibration

- **Descriptive or atlas:** prioritize annotation rationale, quantitative support, donor/sample structure, batch and sampling limitations, methods transparency, appropriate reference comparisons, and moderation of functional language.
- **Mechanistic:** central causal claims generally require appropriate perturbation, controls, biological replication, and consideration of credible alternatives. Complementary perturbations, orthogonal assays, ex vivo systems, in vivo models, or human relevance may be needed for validity, discrimination, generalization, or venue completeness.
- **Clinical cohort:** require clear cohort definition, outcome ascertainment, confounder handling, appropriate models, uncertainty, and validation proportionate to the intended associative, predictive, utility, or treatment claim.
- **Case report or rare material:** prioritize accurate description, diagnostic or biological support, key outcome data, transparent limitations, and cautious generalization. Rarity modifies feasible requests but not the scope justified by the evidence.
- **Methods or computational:** examine assumptions, baselines, parameter sensitivity, uncertainty, validation independence, leakage, circularity, reproducibility, and comparative claims. Separate computational transformation from biological interpretation or clinical utility.
- **Review article:** assess completeness, balance, evidence hierarchy, accuracy, and treatment of controversy. For systematic reviews or meta-analyses, also assess protocol, search reproducibility, selection, risk of bias, synthesis, and reporting standards.

## 6. Issue tiering and proportionate action

Assign stable issue identifiers:

- **I1, I2... — Validity-critical:** the central claim does not stand at its stated level without correction or new evidence.
- **I1, I2... — Venue-critical:** a narrower claim may stand, but the paper lacks the depth, triangulation, generalizability, or contribution expected for the current journal.
- **Recommended strengthening:** useful but not necessary for validity or venue fit.
- **Minor/publication quality:** clarity, consistency, reporting, reproducibility detail, or presentation without a material effect on the main judgment.

Every substantive request should state what it is intended to establish: direct support, causal inference, exclusion of an alternative, robustness, cross-model reproducibility, in vivo or ex vivo relevance, human relevance, mechanistic completeness, generalization, or venue-level contribution.

Choose the proportionate action:

1. clarification or correction;
2. existing-data reanalysis;
3. robustness, sensitivity, or uncertainty analysis;
4. orthogonal validation or additional evidence;
5. a new experiment or sample set;
6. explicit limitation and narrower claim.

Do not make new experiments an automatic last resort or an automatic requirement. Request them when necessary for claim validity or venue-level completeness. Offer an alternative route only when it resolves the scientific problem and leaves a contribution appropriate for the current journal.

### Domain-grounded experimental requests

Before naming a specific experiment, determine:

- the exact inference it is intended to establish or falsify;
- the field standard or directly relevant precedent supporting the design;
- why it discriminates the live alternatives better than additional characterization;
- the main biological, technical, or interpretive confounder;
- how positive, negative, and null results would change the affected claim;
- whether existing data, reanalysis, or a narrower claim could resolve the issue with less burden.

When useful, formulate three internal routes:

- **Decisive test:** the most direct field-grounded way to resolve the inference;
- **Valid alternative:** a different feasible design that resolves the same inference with acceptable limitations;
- **Supporting characterization:** optional or secondary evidence that aids interpretation but does not itself resolve the inference;
- **Claim-calibration fallback:** the analysis, limitation, or wording change required if new evidence is unavailable.

The decisive test, valid alternative, and claim-calibration fallback are alternative response paths, not a cumulative experiment list. Supporting characterization should not be presented as an additional requirement unless it is needed to interpret the chosen inference-resolving route. Include only the routes that help the authors act on the issue. If domain knowledge or literature does not support a specific design, state the required evidence class or inference without inventing assay, protocol, marker, model, or parameter details.

## 7. Recommendation logic

- **Accept:** no substantive scientific or venue-level issue remains and the journal provides this option.
- **Minor Revision:** central conclusions and venue-level contribution are supported; only limited analysis, clarification, references, figures, or wording remain.
- **Major Revision:** important validity or venue-completeness gaps are consequential but realistically revisable, and a satisfactory revision could meet the journal's criteria.
- **Reject:** the central claim is fundamentally unsupported, the needed correction is not realistically achievable within revision, or a defensible narrower contribution would not meet the journal's scope or threshold. Recommend transfer only when that option exists.

Do not disguise a venue-fit judgment as a data-validity flaw. State author-actionable scientific gaps to the authors and keep strategic journal-fit reasoning in the recommendation or confidential editor comment when appropriate.
