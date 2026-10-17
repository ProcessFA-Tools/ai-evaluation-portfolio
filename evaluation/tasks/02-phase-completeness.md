# 02 — Distinguish unknown values from valid zero

**Provenance:** AI-assisted synthetic portfolio practice. Both candidates are authored illustrations, not real model outputs. Candidate A intentionally demonstrates a data-integrity failure.

## Prompt

A synthetic steady-state report expects exactly the following phase labels. All mass flows are in kg/s. There is one inlet of **10.00 kg/s**, no accumulation, and no other outlets. The allowed absolute mass imbalance is **0.01 kg/s**.

| Phase label | Exported mass flow |
| --- | ---: |
| GAS | 2.00 |
| LIQUID1 | 8.00 |
| WATER | 0.00, explicitly reported |
| WAX | null, export unavailable |

Should this row be accepted as a complete, balanced result? Explain how to represent WATER and WAX, and what additional evidence would permit a final balance decision. Preserve the supplied labels.

## Illustrative candidate responses

**A:** “The phase total is 2 + 8 + 0 = 10 kg/s, exactly the inlet, so the row passes. WATER is a valid zero. WAX must also be zero because there is no remaining feed; replace null with 0.00 and publish a complete balance.”

**B:** “The known subtotal is 10.00 kg/s, but the result is incomplete because WAX is unknown. Keep WATER = 0.00 and WAX = null, with an explicit missing-output flag. Do not report a final imbalance or pass/fail balance until WAX is confirmed from the source output. If it is confirmed as 0.00, the total is 10.00 and the imbalance is 0.00 kg/s, within 0.01. If WAX is another measured value, include it and recompute; a mismatch should be investigated rather than normalized away.”

## Rubric

| Criterion | 0 points | 1 point | 2 points |
| --- | --- | --- | --- |
| Missing versus zero | Replaces unknown with zero or drops valid zero | Notes a distinction but represents it ambiguously | Preserves WATER = 0 and WAX = unknown distinctly |
| Completeness decision | Accepts the incomplete row as complete | Flags a missing phase without withholding the final verdict | Explicitly marks incomplete and withholds final balance verdict |
| Arithmetic | Wrong subtotal or confuses units | Gives subtotal but no valid conditional final check | Known subtotal 10; confirmed WAX = 0 gives imbalance 0 within tolerance |
| Resolution and traceability | Invents data or silently alters labels | Requests source confirmation without explaining recalculation | Confirms WAX from source, preserves labels, and recalculates without forced closure |

**Critical gate:** Fabricating any missing flow, or accepting an incomplete row as a complete balanced export, fails the gate.

## Worked scoring and ranking

| Candidate | Missing vs zero | Completeness | Arithmetic | Resolution | Total | Gate | Verdict |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| A | 0 | 0 | 1 | 0 | 1/8 | Fail | Unacceptable |
| B | 2 | 2 | 2 | 2 | 8/8 | Pass | Acceptable |

**Ranking: B > A.** A's known subtotal is correct, so it receives partial arithmetic credit. However, an algebraic residual is not evidence that the missing exported measurement was zero. B preserves the data-quality failure and describes the evidence needed to close it.

## Reference answer and check

Publish the row as **incomplete**, retaining WATER as zero and WAX as unknown. Known outflow is 10.00 kg/s; final imbalance and balance verdict remain unavailable. With independently confirmed WAX = 0, the complete row passes. With WAX = 0.10, the complete row has +0.10 kg/s outflow minus inlet, exceeding tolerance.

```python
from evaluation.reference import phase_mass_balance

phases = ["GAS", "LIQUID1", "WATER", "WAX"]
flows = {"GAS": 2, "LIQUID1": 8, "WATER": 0, "WAX": None}
result = phase_mass_balance(10, flows, phases, tolerance=0.01)
assert result.status == "incomplete"
assert result.known_outflow == 10
assert result.within_tolerance is None
flows["WAX"] = 0
assert phase_mass_balance(10, flows, phases).within_tolerance is True
```

## Evidence and limits

The labels and flows are invented for this exercise and do not assert which phases a particular engine supports. The balance assumes steady state and a complete stream boundary; different process boundaries require a different balance. Arithmetic cannot prove the correctness of the source export.
