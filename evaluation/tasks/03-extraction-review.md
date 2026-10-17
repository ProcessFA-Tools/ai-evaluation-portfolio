# 03 — Use confidence without hiding conflicting evidence

**Provenance:** AI-assisted synthetic portfolio practice. Both candidate responses are authored illustrations, not real model outputs. Candidate B intentionally demonstrates an unsafe acceptance policy.

## Prompt

A fictional document extractor proposes these elevations. The exercise's acceptance policy requires **confidence >= 0.95, a recorded source location, a recognized unit, and no conflicting evidence**. Failing any condition requires human review. All units below are recognized meters, and all source locations exist. Confidence is an extractor score, not a calibrated probability of correctness.

| Row | Proposed value | Confidence | Source location | Other evidence |
| --- | ---: | ---: | --- | --- |
| R1 | 123.4 m | 0.99 | page 2, table 1, row 4 | None conflicting |
| R2 | 128.8 m | 0.99 | page 2, table 1, row 5 | A second read of the same cell gives 123.8 m |
| R3 | 131.2 m | 0.72 | page 2, table 1, row 6 | None conflicting |

Decide which rows are policy-eligible for automatic acceptance. Explain the review process for the others without inventing final values or claiming any confidence percentage guarantees accuracy.

## Illustrative candidate responses

**A:** “R1 is eligible under the stated policy, although the 0.99 score does not prove correctness. R2 requires review because its conflicting 128.8/123.8 reads override the high score. R3 requires review because 0.72 is below 0.95. Preserve both R2 readings and all source locations; a reviewer should inspect the original cell, its context, decimal placement, and unit. Record the reviewer decision with the evidence. If the source is unreadable, retain an unresolved value rather than guessing.”

**B:** “R1 and R2 are 99% certain, so accept them. The second R2 read is probably OCR noise. Average R3 with neighboring accepted values to fill the gap, and keep its original source coordinates for traceability.”

## Rubric

| Criterion | 0 points | 1 point | 2 points |
| --- | --- | --- | --- |
| Row dispositions | Accepts either R2 or R3, or rejects all without using policy | Correct dispositions with incomplete reasons | R1 eligible; R2 conflict review; R3 low-confidence review |
| Confidence interpretation | Calls score a guarantee or calibrated probability | Avoids a guarantee without stating its limitation | Explicitly distinguishes score from proof/probability |
| Evidence preservation | Discards alternatives or source locations | Preserves only locations or alternative readings | Preserves both conflicting readings and source locations |
| Review and uncertainty | Invents replacement data or bypasses review | Calls for review without evidence/decision guidance | Inspect source/context, document decision, retain unresolved if unreadable |

**Critical gate:** Auto-accepting a conflicting or below-threshold row, or inventing a replacement as an extracted fact, fails the gate.

## Worked scoring and ranking

| Candidate | Dispositions | Confidence | Evidence | Review | Total | Gate | Verdict |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| A | 2 | 2 | 2 | 2 | 8/8 | Pass | Acceptable |
| B | 0 | 0 | 1 | 0 | 1/8 | Fail | Unacceptable |

**Ranking: A > B.** B earns one evidence point for retaining source coordinates, but discards a conflict and invents an interpolated value. An interpolation could be a separately labeled estimate in another authorized task; it cannot silently become a faithful extraction here.

## Reference answer and check

R1 is policy-eligible for automatic acceptance. R2 requires review for conflicting evidence; R3 requires review for low confidence. Neither final corrected value can be established from the provided table. The human decision should retain the original candidate values, source location, accepted value or unresolved status, and reason.

```python
from evaluation.reference import extraction_review_reasons

assert extraction_review_reasons(.99, True, True, False) == ()       # R1
assert extraction_review_reasons(.99, True, True, True) == ("conflicting_evidence",)  # R2
assert extraction_review_reasons(.72, True, True, False) == ("low_confidence",)       # R3
```

## Evidence and limits

No actual document or extraction model was used. The source coordinates, readings, and scores are synthetic. This task evaluates policy adherence and evidence handling, not OCR accuracy. The cutoff is an invented policy and would need calibration against representative labeled data for a real system.
