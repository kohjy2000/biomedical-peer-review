# Open Discovery

Use this entry point for a full initial review or for a materially new claim branch that has not previously been reviewed. Its purpose is to preserve the reviewer's ability to notice unexpected scientific problems before a claim map, literature synthesis, checklist, or reporting format narrows attention.

Until the gate below is complete:

- do not read the other skill references;
- do not search external literature;
- do not construct H/M/E identifiers or a formal claim map;
- do not assign Major/Minor status, choose a recommendation, design remedies, or compress the concern list.

## D0. Open read

Read the available manuscript, figures, tables, legends, methods, and supplementary material as an independent reviewer. Capture any potentially consequential concern, surprising or unexplained observation, internal tension, ambiguous interpretation, plausible competing explanation, or mismatch between what is shown and what is claimed.

Do not force a taxonomy or require a fixed question for every item. Record a candidate only when something may matter scientifically or editorially. Use a compact entry:

```markdown
### D1 — [short neutral label]
- Source location:
- Observation or claim:
- Open concern or question:
- Why it may matter:
```

Do not decide whether the concern is correct at this stage. A provisional or uncertain candidate is allowed.

## D1. Source-coverage sweep

After the open read, revisit the title, Abstract, each Results section, every main figure and table, the claim-bearing Methods, and available supplementary items. This is a traversal check, not a scientific checklist. Record only whether the item was reviewed and any new candidate IDs:

| Source item | Reviewed | New D# candidates |
| --- | --- | --- |
| | Yes / Not assessable | |

Do not write a justification for a reviewed item that produced no candidate.

## Preserve the discovery state

Save the entries and coverage table as `discovery-notes.md`. The D# register is append-only: later stages may validate, weaken, reject, or leave a candidate unresolved, but must not erase it. Literature review and structured appraisal may add new C# candidates; they do not close the candidate set.

## Gate

Proceed only when the available source set has been openly read, the coverage sweep is complete or an unavailable item is marked Not assessable, and `discovery-notes.md` has been saved. Then read `workflow.md`, `review-dossier-template.md`, and `review-framework.md`, import the discovery record into the dossier without rewriting it, and continue at S0.
