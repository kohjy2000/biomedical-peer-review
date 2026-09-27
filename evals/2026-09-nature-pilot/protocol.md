# Protocol

## Papers

| Case | Paper (Nature, 2026) | DOI | Received | Preprint used as "submitted manuscript" |
|---|---|---|---|---|
| A | Cell-type-resolved eQTLs and IBD risk (Alegbe et al.) | 10.1038/s41586-026-10627-z | 2025-06-24 | medRxiv 10.1101/2025.06.24.25330216 **v1** (CC BY) |
| B | Host genetic control of persistent EBV (Schmidt et al.) | 10.1038/s41586-026-10274-4 | 2025-07-16 | medRxiv 10.1101/2025.07.19.25331823 **v1** (CC BY-NC-ND) |
| C | Intratumoural anti-CTLA-4 + IV anti-PD-1, phase 1b (Tselikas et al.) | 10.1038/s41586-026-10341-w | 2025-08-17 | Research Square rs-7394486 **v1** |

Selection criteria: published Peer Review File with round-1 reports and author responses; CC BY article; preprint posted within 0–5 days of the Received date; immunology or translational human-disease topic; substantive round-1 critique.

## Inputs (not committed)

Run `./fetch_inputs.sh <workdir>` to download the preprint v1 text/figures and the Peer Review Files. Preprint text and figures, Peer Review Files and published articles are third-party material and are not stored in this repository. Supplementary files for A and B could not be retrieved automatically.

## Procedure

1. **Blind review** (per case, one agent): follow `SKILL.md` S0–S5 on the preprint v1 only, reviewing for Nature as of the Received date; literature published before that date only; no access to later versions, the published article, the Peer Review File, news, or other case folders; publisher and preprint domains excluded from web search (v2 runs) via the search tool's `blocked_domains` parameter; the `-site:` query operator was ignored by the tool and must not be relied on. Outputs: `peer-review.md`, `review-dossier.md`, `run-notes.md`.
2. **Reference ledger** (separate agent, reference folder only): every round-1 referee point with the referee's label, our Major/Minor category, topic, paraphrase, and author response outcome → `human_points.md`.
3. **Adjudication** (separate agent per case, may open the published article):
   - Coverage: each ledger point Matched / Partial / Missed; recall = (Matched + 0.5 × Partial) / total, Major and Minor separately; round-1 points only; primary metric uses our category; rebuttal-only answers still count as substantive.
   - AI-only issues: Valid / Debatable / Incorrect, with evidence from the manuscript and whether the published paper changed.
   - Accuracy audit of every number, quotation, figure reference and cited source in `peer-review.md`.
   - Recommendation and severity calibration; blinding integrity.

## Versions

- v1: skill commit `fccb466`.
- v2: `fccb466` + the four changes listed in `CHANGELOG.md` [Unreleased]. Case C could not be re-run (platform safety filter stopped the run three times).

Reviewer and adjudicator model: Claude Opus (high effort), single run per case and version.
