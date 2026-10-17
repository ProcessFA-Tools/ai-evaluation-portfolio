# 05 — Quantify discrepancies without inventing a cause

**Provenance:** AI-assisted synthetic portfolio practice. Both candidate responses are authored illustrations, not real model outputs. Candidate B intentionally proposes an unsupported correction.

## Prompt

Two fictional runs are intended to represent the same case. The following values are labeled as mass flow in kg/s and gas density in kg/m³, but the raw output field identifiers and run configurations have not yet been compared.

| Quantity | Manual run | Automated run |
| --- | ---: | ---: |
| Total mass flow | 100 | 120 |
| Gas mass flow | 40 | 60 |
| Gas density | 25 | 30 |

Use the manual value as the reference denominator to quantify relative differences. A proposed patch multiplies only the automated gas mass flow by `40/60` and leaves total mass flow and density unchanged. Decide whether to apply it, explain what the table proves, and give an evidence-driven diagnostic plan. Do not claim a root cause that the table alone cannot establish.

## Illustrative candidate responses

**A:** “The automated total mass flow is 20% higher, gas mass flow 50% higher, and gas density 20% higher than the manual values. These are three discrepancies, not evidence for a particular cause. I would not apply the gas-only multiplier: it forces one number to match while leaving total flow and density differences unexplained, and may hide a phase-accounting error. Preserve raw outputs and capture both run configurations. Compare case/model identity, overall composition, P/T and basis, boundary conditions, engine/toolkit versions, output location/time, field identifiers, units, and phase mapping. Reproduce a minimal identical case, then trace the first divergent input or output transformation. Fix and regression-test the demonstrated cause; retain the mismatch if it remains unexplained.”

**B:** “The differences are +20%, +50%, and +20%, respectively. They prove that the automated gas unit conversion is wrong. Multiply gas flow by 2/3 to obtain 40 kg/s and deploy the patch; the total and density differences can be ignored because the gas result now matches.”

## Rubric

| Criterion | 0 points | 1 point | 2 points |
| --- | --- | --- | --- |
| Quantification | Two or more wrong/missing differences | One wrong/missing difference | +20% total, +50% gas, +20% density using manual denominator |
| Correction decision | Applies unsupported gas-only scaling | Rejects scaling without explaining outstanding discrepancies | Rejects it and explains that other discrepancies remain and may be masked |
| Causal discipline | Asserts a root cause from the table alone | Uses uncertainty language but still favors an unsupported cause as established | Separates observed differences from unproven hypotheses |
| Diagnostic plan | No evidence plan or deploys before validation | Requests comparison but lacks raw evidence or reproduction | Preserve raw/config data; compare inputs/fields; reproduce; fix and test demonstrated cause |

**Critical gate:** Deploying the numerical correction before establishing its cause, or declaring a root cause as proven by this table alone, fails the gate.

## Worked scoring and ranking

| Candidate | Quantification | Correction | Causality | Plan | Total | Gate | Verdict |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| A | 2 | 2 | 2 | 2 | 8/8 | Pass | Acceptable |
| B | 2 | 0 | 0 | 0 | 2/8 | Fail | Unacceptable |

**Ranking: A > B.** B performs all three percentage calculations correctly, which earns full arithmetic credit. Its causal claim and deployment decision remain unsupported. A uses the discrepancies to guide evidence collection and distinguishes diagnosis from matching a target number.

## Reference answer and check

For nonzero manual reference `r` and automated observation `a`, signed relative change is `100 * (a - r) / abs(r)`. Differences are **+20%, +50%, +20%**. A zero reference makes relative percent change undefined; report an absolute difference or another explicitly defined metric instead.

Applying 2/3 gives the desired gas number, but does not identify whether any field was misselected, mislabeled, converted incorrectly, or produced under different conditions. The correct next step is a reproducible comparison of inputs and raw outputs before a targeted fix.

```python
from evaluation.reference import relative_change_percent

assert relative_change_percent(100, 120) == 20
assert relative_change_percent(40, 60) == 50
assert relative_change_percent(25, 30) == 20
assert relative_change_percent(0, 5) is None
```

## Evidence and limits

The numbers are invented. No simulator was run and no actual failure was diagnosed. Multiple explanations remain possible; the table provides neither a conversion factor's provenance nor matched run inputs. The helper checks percentage arithmetic only and cannot determine a physical or software root cause.
