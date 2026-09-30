---
name: biomedical-peer-review
description: Evaluate a biomedical manuscript's scientific contribution and identify the improvements that most increase its credibility and value. Use a clean initial review, independent evidence and literature preparation, and one informed reassessment with the initial review visible.
---

# Biomedical manuscript evaluation and improvement

Answer two questions: What has this study actually established, and why does it matter? Which revisions or additional analyses would most improve its credibility and value?

For a full initial review, follow [the run guide](references/run.md): prepare the supplied PDFs, run the independent contexts, research the literature, and save the review and working dossier. The bundled Codex helper handles input provenance and isolated calls; literature search and visual verification use the host's available tools. Use the configured model unless the user chooses another, and record it. If isolated execution is unavailable, disclose that limitation instead of calling an in-session draft independent.

For a bounded question or draft edit, answer that scope directly. For a revised submission, use the supplied prior review and response with [revision review](references/revision-review.md); do not pretend that review is blind. The older S0–S5 references are retained for targeted consultation, not extra default stages.

## Workflow

1. Obtain and preserve a complete initial review in a fresh context without this skill, prior reviews, or evaluation materials.
2. Independently prepare a concise map of the study's important claims, actual comparisons and measurements, and their supporting evidence. Include the scope and contribution the authors intend. Keep the initial review hidden during preparation. This is evidence organization, not a second review: do not generate a criticism ledger or audit every mapped object. Read the source figures and tables as well as text.
3. Use the map to identify and verify relevant prior work and domain knowledge. Prioritize knowledge that can change the interpretation, novelty assessment, or choice of useful improvements. Record source, date, what was actually accessible, and limitations. Literature may extend the map. Do not treat plausibility or a cited precedent as evidence that this manuscript demonstrated a result. Keep confidential manuscript identifiers and distinctive text out of external queries.
4. Reveal the initial review alongside the map, verified literature, and original manuscript evidence. In **one reassessment**, determine the defensible contribution, consequential uncertainty, and most valuable improvements, and write a complete review draft. Reuse adequate judgments; correct errors and deepen materially incomplete reasoning. Reconsider the important conclusions together so that an omitted topic is neither presumed resolved nor presumed defective. There is no separate default full audit, integration agent, or final reconciliation call.

5. Read the saved draft and apply the final-editing reference against the accepted assessment, initial review and source evidence. Save an edited report and concise editing notes, then compare the report with the selected template and consequential scientific reasons/actions. Finalize the checked report using the run guide. Generation completion alone is not delivery; this host step uses the existing conversation and tools, without an extra default model call.

## Evidence input efficiency

Avoid upscaling raster figures into oversized page screenshots for every stage. When the PDF contains complete embedded figure images, use their native pixels with the full manuscript text/captions and explicit page/image correspondence. Verify that extraction preserves all panels, labels, and displayed orientation. Keep full-page rendering for vector figures, tables, overlays, or any content that extraction would lose; retain the original PDF for checking. Reduce redundant input representation, not scientific evidence or review scope.

## Scientific judgment

**공통 적용 원칙**

- 연구 목적·논문 유형·실제 주장 수준과 분야·저널의 기준에 맞춰 판단한다. **검토할 쟁점은 연구 질문·자료·분야 지식에서 도출한다.** 아래 참고 관점은 범위를 제한하거나 항목마다 지적을 요구하는 체크리스트가 아니다.
- **중요한 판단은 실제 결과·비교에 연결하고, 그것이 해석이나 수정 방향에 어떤 차이를 만드는지 설명한다.**
- 기존 판단을 활용하되, 중요한 추론이 실제로 성립하는지 확인한다. 같은 쟁점에 대한 판단은 연결해 정리하며, 근거가 충분한 부분은 그대로 인정한다.

**① Evidence — 이 연구의 관찰 결과는 무엇을 얼마나 믿을 만하게 보여주는가?**

> 실제 실험과 분석을 살펴, 무엇을 신뢰할 수 있는지 판단한다. 그 판단을 좌우하는 조건과 불확실성은 무엇이며, 어떤 결과의 해석을 얼마나 바꾸는지 설명한다.

참고 관점: 생물학적 모델과 실험 조건의 적합성, 측정값의 의미, 비교 설계와 통계, 자료·방법의 검증 및 재현 가능성 등.

**② Claims — 이 연구가 실제로 알아낸 것은 무엇이며, 왜 중요한가?**

> 분야의 배경지식과 관련 선행연구 속에서 이번 연구가 무엇을 확인·확장·수정했는지 판단한다. 저자의 주장이 실제 발견의 범위와 확실성에 맞는지 살피고, 근거로 뒷받침되는 기여와 가치를 설명한다.

참고 관점: 기존 지식과의 차이, 새로운 맥락에서의 의미, 재현이나 반증의 가치, 주장의 적용 범위와 일반화 가능성 등.

**③ Links — 근거에서 개별 주장으로, 주장들에서 전체 결론으로 이어지는 논리는 성립하는가?**

> 각 주장이 어떤 근거로 성립하는지, 중요한 주장들이 서로 어떤 관계를 맺어 전체 결론을 이루는지 판단한다. **개별 주장이 타당해도 그것들을 연결한 결론은 성립하지 않을 수 있다.** 전체 결론이 의존하는 중요한 연결에서, 필요한 전제와 결론을 바꿀 만한 다른 설명을 살핀다.

참고 관점: 관찰에서 기능·기전으로의 추론, 한 주장이 다른 주장의 전제가 되는 관계, 서로 다른 실험 결과의 결합, 주장 사이의 모순이나 설명의 공백 등. 논문이 필요로 하지 않는 연결까지 요구하지 않는다.

**종합 판단 — 무엇을 남기고, 무엇부터 개선해야 하는가?**

세 질문의 판단을 함께 보고, 같은 재평가 단계에서 답한다.

> **믿고 남길 수 있는 발견과 가치는 무엇인가? 어떤 수정이나 추가 분석이 연구의 신뢰도와 가치를 가장 크게 높이는가?**

수정 요구는 중요성·예상 이득·실행 부담을 고려해 우선순위를 정한다. **어떤 결론을 유지하기 위해 필요한 수정인지 명확히 하고**, 필수 수정·문제를 해결할 수 있는 대안·선택적 보강을 구분한다. 주장 조정으로 해결되는 문제와, 조정해도 남는 신뢰성 문제를 구분한다.

근거지도와 문헌에서 확인한 중요한 사실이 핵심 주장을 뒷받침하는지, 제한하는지 판단한다. 불확실성이 남아도 결론을 유지할 수 있다고 판단한다면 그 근거를 설명하고, 부족하다면 필요한 검증이나 주장 조정을 제시한다.

이 내용은 내부 판단 지침이며, 최종 보고서는 기존 사용자 템플릿을 따른다.

Preserve valid substantive reasons and actions from the initial review. Change or withdraw them when source evidence warrants it. Reopen the relevant original evidence when changing a factual judgment, including the figure for a visual claim.

## Draft, edit, and present

After reassessment, write a complete draft using the selected user/journal template, or [the default template](references/review-template.md). After the draft is saved, the host applies [final editing](references/final-pruning.md) to the actual file before delivery. These writing resources must be read when working directly, or included in full in the isolated final request; a file link alone does not deliver them.

## Outputs and limits

Preserve the initial review, evidence map, source-linked literature notes, generated draft, checked final review, and a concise explanation of material changes with evidence anchors. Keep model identity, input provenance, and usage so the incremental benefit and cost can be assessed. Do not require a fixed number of new findings, case-specific omissions, or prescribed wording.

If preparation and reassessment use separate calls, carry the complete prepared packet into reassessment and disclose that the context was reconstructed. Report missing sources or images; do not turn unavailable evidence into an assertion that an experiment was not done. Do not submit or send the review externally without user authorization.
