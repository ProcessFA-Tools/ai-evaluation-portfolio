# 03 — Use confidence without hiding conflicting evidence

**Provenance:** This is AI-assisted synthetic portfolio practice. The portfolio author wrote both candidate answers as illustrations. They are not real model outputs. Candidate B intentionally uses an unsafe acceptance policy.

The [glossary](../../docs/glossary.md) defines the technical terms used in this task.

## Prompt

A fictional document extractor proposes these elevations. The exercise's acceptance policy requires all four conditions:

- **Confidence >= 0.95**.
- **A recorded source location**.
- **A recognized unit**.
- **No conflicting evidence**.

Failure to meet any condition requires human review. All units below are recognized meters, and all source locations exist. Confidence is an extractor score. It is not a calibrated probability of correctness.

| Row | Proposed value | Confidence | Source location | Other evidence |
| --- | ---: | ---: | --- | --- |
| R1 | 123.4 m | 0.99 | page 2, table 1, row 4 | None conflicting |
| R2 | 128.8 m | 0.99 | page 2, table 1, row 5 | A second read of the same cell gives 123.8 m |
| R3 | 131.2 m | 0.72 | page 2, table 1, row 6 | None conflicting |

Decide which rows the policy permits for automatic acceptance. Explain the review process for the other rows. Do not invent final values. Do not claim that any confidence percentage guarantees accuracy.

## Illustrative candidate answers

**A:** “R1 is eligible under the stated policy, although the 0.99 score does not prove correctness. R2 requires review because its conflicting 128.8/123.8 readings override the high score. R3 requires review because 0.72 is below 0.95.

Preserve both R2 readings and all source locations. A reviewer should inspect the original cell, its context, decimal placement, and unit. Record the reviewer decision with the evidence. If the source is unreadable, keep the value unresolved. Do not guess the value.”

**B:** “R1 and R2 are 99% certain, so accept them. The second R2 reading is probably OCR noise. Average R3 with neighboring accepted values to fill the gap. Keep its original source coordinates for traceability.”

## Rubric

| Criterion | 0 points | 1 point | 2 points |
| --- | --- | --- | --- |
| Row dispositions | Accepts either R2 or R3, or rejects all without using policy | Correct dispositions with incomplete reasons | R1 eligible; R2 conflict review; R3 low-confidence review |
| Confidence interpretation | Calls score a guarantee or calibrated probability | Avoids a guarantee without stating its limitation | Explicitly distinguishes score from proof/probability |
| Evidence preservation | Discards alternatives or source locations | Preserves only locations or alternative readings | Preserves both conflicting readings and source locations |
| Review and uncertainty | Invents replacement data or bypasses review | Calls for review without evidence/decision guidance | Inspect source/context, document decision, retain unresolved if unreadable |

**Critical gate:** A response fails the gate if it automatically accepts a conflicting row or a row below the confidence threshold. It also fails if it presents an invented replacement as an extracted fact.

## Worked scoring and ranking

| Candidate | Dispositions | Confidence | Evidence | Review | Total | Gate | Verdict |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| A | 2 | 2 | 2 | 2 | 8/8 | Pass | Acceptable |
| B | 0 | 0 | 1 | 0 | 1/8 | Fail | Unacceptable |

**Ranking: A > B.** B earns one evidence point for keeping source coordinates. However, it discards a conflict and invents an interpolated value. Another authorized task could permit interpolation as a separately labeled estimate. This task does not permit silently presenting an estimate as an accurately extracted value.

## Reference answer and check

The policy permits automatic acceptance of R1. R2 requires review for conflicting evidence. R3 requires review for low confidence. The supplied table cannot establish either final corrected value.

The reviewer must keep these details with the decision:

- The original candidate values.
- The source location.
- The accepted value or unresolved status.
- The reason for the decision.

```python
from evaluation.reference import extraction_review_reasons

assert extraction_review_reasons(.99, True, True, False) == ()       # R1
assert extraction_review_reasons(.99, True, True, True) == ("conflicting_evidence",)  # R2
assert extraction_review_reasons(.72, True, True, False) == ("low_confidence",)       # R3
```

## Evidence and limits

This exercise uses no actual document or extraction model. The source coordinates, readings, and scores are synthetic. This task evaluates compliance with the policy and handling of evidence. It does not evaluate OCR accuracy. The confidence threshold is an invented policy. A real system would require calibration against representative labeled data.
