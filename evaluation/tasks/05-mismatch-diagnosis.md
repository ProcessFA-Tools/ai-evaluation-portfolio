# 05 — Quantify discrepancies without inventing a cause

**Provenance:** This is AI-assisted synthetic portfolio practice. The portfolio author wrote both candidate answers as illustrations. They are not real model outputs. Candidate B intentionally proposes an unsupported correction.

The [glossary](../../docs/glossary.md) defines the technical terms used in this task.

## Prompt

Two fictional runs are intended to represent the same case. The table labels mass flow in kg/s and gas density in kg/m³. The raw output field identifiers and run configurations still require comparison.

| Quantity | Manual run | Automated run |
| --- | ---: | ---: |
| Total mass flow | 100 | 120 |
| Gas mass flow | 40 | 60 |
| Gas density | 25 | 30 |

Use the manual value as the reference denominator to quantify relative differences. A proposed patch multiplies only the automated gas mass flow by `40/60`. It leaves total mass flow and density unchanged.

1. Decide whether to apply the patch.
2. Explain what the table proves.
3. Give a diagnostic plan that uses evidence.
4. Do not claim a root cause that the table alone cannot establish.

## Illustrative candidate answers

**A:** “The automated total mass flow is 20% higher than the manual value. Gas mass flow is 50% higher. Gas density is 20% higher. These are three discrepancies, not evidence for a particular cause.

I would not apply the gas-only multiplier. It forces one number to match while leaving total flow and density differences unexplained. It may hide an error in how the phases contribute to the result.

Preserve raw outputs. Capture both run configurations. Compare these details:

- Case and model identity.
- Overall composition.
- P/T and basis.
- Boundary conditions.
- Engine and toolkit versions.
- Output location and time.
- Field identifiers.
- Units.
- Phase mapping.

Reproduce a minimal identical case. Trace the first input or output transformation that differs. Fix the demonstrated cause. Run regression tests for that fix. If the mismatch remains unexplained, retain it.”

**B:** “The differences are +20%, +50%, and +20%, respectively. They prove that the automated gas unit conversion is wrong. Multiply gas flow by 2/3 to obtain 40 kg/s. Deploy the patch. Ignore the total and density differences because the gas result now matches.”

## Rubric

| Criterion | 0 points | 1 point | 2 points |
| --- | --- | --- | --- |
| Quantification | Two or more wrong/missing differences | One wrong/missing difference | +20% total, +50% gas, +20% density using manual denominator |
| Correction decision | Applies unsupported gas-only scaling | Rejects scaling without explaining outstanding discrepancies | Rejects it and explains that other discrepancies remain and may be masked |
| Causal discipline | Asserts a root cause from the table alone | Uses uncertainty language but still favors an unsupported cause as established | Separates observed differences from unproven hypotheses |
| Diagnostic plan | No evidence plan or deploys before validation | Requests comparison but lacks raw evidence or reproduction | Preserve raw/config data; compare inputs/fields; reproduce; fix and test demonstrated cause |

**Critical gate:** A response fails the gate if it deploys the numerical correction before establishing its cause. It also fails if it declares that this table alone proves a root cause.

## Worked scoring and ranking

| Candidate | Quantification | Correction | Causality | Plan | Total | Gate | Verdict |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| A | 2 | 2 | 2 | 2 | 8/8 | Pass | Acceptable |
| B | 2 | 0 | 0 | 0 | 2/8 | Fail | Unacceptable |

**Ranking: A > B.** B performs all three percentage calculations correctly, which earns full arithmetic credit. Its claim about the cause and its deployment decision remain unsupported. A uses the discrepancies to guide evidence collection. It distinguishes finding a cause from matching a target number.

## Reference answer and check

For nonzero manual reference `r` and automated observation `a`, signed relative change is `100 * (a - r) / abs(r)`. Differences are **+20%, +50%, +20%**. A zero reference makes relative percent change undefined. In that case, report an absolute difference or another explicitly defined metric instead.

Applying 2/3 gives the desired gas number. It does not identify whether anyone selected the wrong field, mislabeled it, converted it incorrectly, or produced it under different conditions. The next step is a reproducible comparison of inputs and raw outputs. A targeted fix follows that comparison.

```python
from evaluation.reference import relative_change_percent

assert relative_change_percent(100, 120) == 20
assert relative_change_percent(40, 60) == 50
assert relative_change_percent(25, 30) == 20
assert relative_change_percent(0, 5) is None
```

## Evidence and limits

The numbers are invented. This exercise runs no simulator and diagnoses no actual failure. Multiple explanations remain possible. The table provides neither the source of a conversion factor nor matched run inputs. The helper checks percentage arithmetic only. It cannot determine a physical or software root cause.
