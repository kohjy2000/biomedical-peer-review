# Run a full initial review

The host assistant carries out these steps; the user supplies the manuscript and relevant supplements. The helper is a Codex CLI adapter, not a standalone literature researcher. Other hosts may implement the same three independent contexts with their own tools, but must disclose any missing isolation or evidence.

Use a private output directory outside the skill/public repository. Preserve successful stages rather than rerunning them to get preferred wording. Never include previous reviews, response letters, published versions, or scoring keys in an initial-review packet unless explicitly within the requested scope.

## 1. Prepare and inspect evidence

Use Python with `pypdf`, `pypdfium2`, and Pillow. In Codex Desktop, discover its bundled Python if these are not available. Resolve `scripts/review_run.py` relative to this skill, and locate the Codex CLI on PATH or in the desktop runtime. Do not change the user's authentication or configuration.

Run `review_run.py inspect --pdf MANUSCRIPT.pdf` (repeat `--pdf` for supplied supplements). Read the source text and inspect pages to identify the figures, tables and image-only evidence. The inventory does not detect all vector graphics. Render source pages with the host PDF tools as necessary.

Write a visual plan in the private output parent directory:

```json
{
  "coverage_note": "Describe which documents/pages were inspected, where relevant figures/tables occur, and any unavailable evidence.",
  "pages": [
    {"document": 1, "page": 8, "note": "Vector table; preserve full page."},
    {"document": 1, "page": 9, "note": "Verified complete native figure and displayed orientation.",
     "images": [{"name": "Image1.jpg", "clockwise": 90}]}
  ]
}
```

Numbers are 1-based PDF indices. An entry without `images` renders the full page. Native selections use the actual inventory names and explicit lossless clockwise rotation (0/90/180/270); select all scientific content. Use full pages when overlays, vector labels, transformations, or completeness are uncertain. Full text and captions are always extracted. For scanned PDFs, obtain and check OCR before proceeding; the helper does not perform OCR.

```text
PYTHON review_run.py prepare --pdf MANUSCRIPT.pdf --visual-plan visual-plan.json --run PRIVATE_RUN --model MODEL --effort high --journal JOURNAL --cutoff YYYY-MM-DD
```

When the user or journal supplies an output template, prepare its submission instructions as UTF-8 text, preserve the original, and pass `--template TEMPLATE.md`. Preserve the supplied fields and order; disclose any extraction from Word/PDF. Otherwise the bundled template is used. Preparation freezes the template and editing guide alongside the skill; only the final context receives them.

Choose the current date for ordinary literature review, or the requested historical cutoff; record why. `--language` defaults to English. Inspect the saved native/fallback images against the source pages and confirm text extraction before any model call. If preparation is wrong, fix the plan and use a new run directory; do not modify frozen inputs. Model/effort remain the same for all three calls unless a new run is explicitly chosen.

## 2. Independent initial review and neutral preparation

```text
PYTHON review_run.py run --run PRIVATE_RUN --stage baseline --cli CODEX_CLI
PYTHON review_run.py run --run PRIVATE_RUN --stage map --cli CODEX_CLI
```

Each command uses a fresh, ephemeral, tool-disabled context with source text/images. Baseline gets neither this skill nor map/literature/prior reviews. Map gets neither baseline nor criticism prompts. The commands print status/usage, not the initial review. Do not open `runs/baseline/response.json` or `review.md` during literature preparation.

The adapter requires a CLI supporting `--ignore-user-config`, `--ignore-rules`, `skip_host_skill_discovery`, and the feature flags in the script. It retains normal auth, uses an empty temporary working directory, disables host skills/plugins/tools, and rejects tool activity in the execution log. This is audited context separation, not a security boundary for arbitrary malicious files. Record a failure rather than silently weakening these controls.

## 3. Literature from the neutral map

Read `runs/map/map.md` and `response.json`. Search public primary literature with generic queries; do not send confidential manuscript identifiers or distinctive text. Verify the sources that can affect contribution, interpretation or useful improvements, respecting the cutoff. Do not search until a fixed source count is reached.

Write `literature-notes.md` with each source's title, stable URL/DOI, publication date, actual access (full text/abstract/excerpt/unavailable), relevant evidence, map connection, and limitations. Preserve unresolved questions without inventing a finding. Write `search-log.json` recording actual queries, access dates, URLs and access outcomes. The log has no prescribed schema beyond valid nonempty JSON.

```text
PYTHON review_run.py seal-literature --run PRIVATE_RUN --notes literature-notes.md --search-log search-log.json --preparation-note "State who prepared the literature, actual prior exposure, and whether the current initial review remained unread."
```

Sealing checks artifact provenance; it does not prove scientific completeness or blindness. Reused literature must be identified as reused and its coverage/access/cutoff checked. New evidence after sealing belongs in a new run, preserving the earlier output.

## 4. One reassessment and saved draft

```text
PYTHON review_run.py run --run PRIVATE_RUN --stage final --cli CODEX_CLI
```

This reconstructs a complete context from manuscript, visuals, map, verified notes, initial review, frozen skill, selected output template and final-editing guide. Existing frozen runs retain their original runner and inputs; use a new run for a changed package. It saves:

- `assessment.md`: contribution, central uncertainty, and highest-value author actions.
- `draft-review.md`: generated review awaiting host editing and verification.
- `review-dossier.md`: map, source notes, material changes, and limitations.
- `runs/`: preserved initial/map/final responses, requests, execution logs, model/settings, completion and usage records.
- `manifest.json`, `source/`, `provenance/`, `literature/`, `usage.json`: frozen evidence, code/skill, literature provenance and per-call usage.

## 5. Edit, check, and finalize

The current host assistant now reads the saved draft and applies the frozen final-pruning guide. Preserve `draft-review.md` unchanged. First correct factual premises and requested actions in a separate `full-review.md`, retaining the detailed reasoning. Then compress that checked version into `edited-review.md` under the selected template. The default is connected prose with a 600–1,000-word working target for the final report, not a hard cap; preserve independent consequential issues, sufficient remedies and valid alternatives. Compare the edited text with the accepted assessment, useful initial-review reasons/actions, relevant manuscript/figures and frozen output template. Check contribution and priorities, required/optional consistency, sufficient alternatives, retained scientific reasons, and factual statements changed by editing. Save `editing-notes.md` with what changed, source reasons for substantive changes, remaining limitations, draft/full/final word counts, and where consequential issues were retained, merged or removed. Compare the concise report with the checked detailed version; explain any necessary length exception. If the draft already meets these requirements, it may be retained after this real check; do not make cosmetic edits merely to manufacture a difference.

Run the local finalization command only after that work:

```text
PYTHON review_run.py finalize --draft PRIVATE_RUN/draft-review.md --full-review PRIVATE_RUN/full-review.md --review PRIVATE_RUN/edited-review.md --notes PRIVATE_RUN/editing-notes.md --template PRIVATE_RUN/provenance/review-template.md --out PRIVATE_RUN/delivery
```

The command requires and preserves the raw draft, checked detailed `full-review.md`, concise `peer-review.md`, notes and selected template with provenance hashes. Existing finalized deliveries remain untouched; use a new output directory when adding a detailed version to an older delivery. It does not call a model or judge scientific quality. The host performs that judgment before running it; a completion record alone is not evidence of a good review. Report the final deliverable and any unresolved limitation plainly. Finalization also works on an existing saved draft from another compatible host; record its actual origin in the editing notes rather than claiming a fresh review.

Keep independent-review generation at three calls. Source/template editing is an actual host task after the draft is available, not a new scientific audit or a hidden extra paid CLI call. Record this host work separately from generation usage, which does not measure its cost.

A completed command validates its saved files and exits without another call. An incomplete or failed attempt remains on disk and blocks overwrite: inspect its logs, correct the operational cause, and explicitly document any new run. Do not claim success from an exit code alone. No external submission is performed.
