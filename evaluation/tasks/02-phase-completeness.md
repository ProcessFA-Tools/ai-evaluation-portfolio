# 02 — Distinguish unknown values from valid zero

**Provenance:** This is AI-assisted synthetic portfolio practice. The portfolio author wrote both candidate answers as illustrations. They are not real model outputs. Candidate A intentionally changes missing data into an unsupported value.

The [glossary](../../docs/glossary.md) defines the technical terms used in this task.

## Prompt

A synthetic steady-state report expects exactly the following phase labels. All mass flows are in kg/s. The report has one inlet of **10.00 kg/s**. There is no accumulation and no other outlet. The allowed absolute mass imbalance is **0.01 kg/s**.

| Phase label | Exported mass flow |
| --- | ---: |
| GAS | 2.00 |
| LIQUID1 | 8.00 |
| WATER | 0.00, explicitly reported |
| WAX | null, export unavailable |

Decide whether to accept this row as a complete, balanced result. Explain how to represent WATER and WAX. State what additional evidence would permit a final balance decision. Preserve the supplied labels.

## Illustrative candidate answers

**A:** “The phase total is 2 + 8 + 0 = 10 kg/s, exactly the inlet, so the row passes. WATER is a valid zero. WAX must also be zero because there is no remaining feed. Replace null with 0.00. Publish a complete balance.”

**B:** “The known subtotal is 10.00 kg/s, but the result is incomplete because WAX is unknown. Keep WATER = 0.00 and WAX = null, with an explicit missing-output flag. Do not report a final imbalance or balance verdict until the source output confirms WAX.

If the source confirms WAX as 0.00, the total is 10.00 and the imbalance is 0.00 kg/s, within 0.01. If WAX is another measured value, include that value. Recalculate the balance. Investigate any mismatch. Do not adjust values to force a balance.”

## Rubric

| Criterion | 0 points | 1 point | 2 points |
| --- | --- | --- | --- |
| Missing versus zero | Replaces unknown with zero or drops valid zero | Notes a distinction but represents it ambiguously | Preserves WATER = 0 and WAX = unknown distinctly |
| Completeness decision | Accepts the incomplete row as complete | Flags a missing phase without withholding the final verdict | Explicitly marks incomplete and withholds final balance verdict |
| Arithmetic | Wrong subtotal or confuses units | Gives subtotal but no valid conditional final check | Known subtotal 10; confirmed WAX = 0 gives imbalance 0 within tolerance |
| Resolution and traceability | Invents data or silently alters labels | Requests source confirmation without explaining recalculation | Confirms WAX from source, preserves labels, and recalculates without forced closure |

**Critical gate:** A response fails the gate if it invents any missing flow. It also fails if it accepts an incomplete row as a complete, balanced export.

## Worked scoring and ranking

| Candidate | Missing vs zero | Completeness | Arithmetic | Resolution | Total | Gate | Verdict |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| A | 0 | 0 | 1 | 0 | 1/8 | Fail | Unacceptable |
| B | 2 | 2 | 2 | 2 | 8/8 | Pass | Acceptable |

**Ranking: B > A.** A's known subtotal is correct, so it receives partial arithmetic credit. However, a calculated remainder does not prove that the missing exported measurement was zero. B preserves the missing-data status. It describes the evidence needed to resolve that status.

## Reference answer and check

Publish the row as **incomplete**. Keep WATER as zero and WAX as unknown. Known outflow is 10.00 kg/s. The final imbalance and balance verdict remain unavailable. With independently confirmed WAX = 0, the complete row passes. With WAX = 0.10, the complete row has +0.10 kg/s outflow minus inlet, which exceeds tolerance.

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

The labels and flows are invented for this exercise. They do not specify which phases a particular engine supports. The balance assumes steady state and a boundary that includes every inlet and outlet. Different process boundaries require a different balance. Arithmetic cannot prove that the source export is correct.
