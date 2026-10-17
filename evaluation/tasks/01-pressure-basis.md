# 01 — Preserve pressure basis during conversion

**Provenance:** This is AI-assisted synthetic portfolio practice. The portfolio author wrote both candidate answers as illustrations. They are not real model outputs. Candidate B intentionally gives an incorrect answer.

The [glossary](../../docs/glossary.md) defines the technical terms used in this task.

## Prompt

A synthetic input table contains two cases:

- Case G: `5.00000 bar gauge`.
- Case A: `5.00000 bar absolute`.

The next calculation accepts Pa absolute.

1. Use atmospheric pressure **101,325 Pa exactly for this exercise**.
2. Use `1 bar = 100,000 Pa`.
3. Convert both values.
4. Explain the difference.
5. State what should happen if a future row has no pressure-basis label.
6. Do not infer a basis from the magnitude.

## Illustrative candidate answers

**A:** “G is 500,000 + 101,325 = 601,325 Pa absolute, or 6.01325 bar absolute. A is already absolute, so it is 500,000 Pa absolute. Only the gauge row receives the atmospheric offset. Preserve the original value, unit, and basis alongside the converted value. A missing basis blocks conversion until its source or an authorized input definition resolves it.”

**B:** “Both rows are 500,000 Pa absolute because 1 bar equals 100,000 Pa. Gauge and absolute are two ways of displaying the same pressure. No extra adjustment is necessary. If the label is absent, assume absolute to keep the pipeline running.”

## Rubric

| Criterion | 0 points | 1 point | 2 points |
| --- | --- | --- | --- |
| Gauge conversion | Wrong value or no atmospheric offset | Correct method with a minor arithmetic error | 601,325 Pa absolute using the supplied atmosphere |
| Absolute conversion | Adds atmosphere or gives another wrong result | Identifies no offset but omits value/unit | 500,000 Pa absolute with no offset |
| Basis reasoning | Conflates the bases | States they differ without explaining how | Explains that atmosphere is added only to gauge pressure |
| Unknown-basis handling | Assumes or silently substitutes a basis | Flags uncertainty but gives no next step | Defers conversion and resolves the source definition |

**Critical gate:** A response fails the gate if a numerical conversion treats gauge pressure as absolute pressure. It also fails if it instructs the reader to invent a missing basis. Minor arithmetic errors still reduce the score. They may make a response unacceptable under the 7/8 threshold.

## Worked scoring and ranking

| Candidate | Gauge | Absolute | Reasoning | Unknown basis | Total | Gate | Verdict |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| A | 2 | 2 | 2 | 2 | 8/8 | Pass | Acceptable |
| B | 0 | 2 | 0 | 0 | 2/8 | Fail | Unacceptable |

**Ranking: A > B.** B correctly converts the absolute row's units, which earns credit. Its gauge result is low by 101,325 Pa. Its policy for missing labels silently introduces incorrect input data. Clear prose cannot compensate for those failures.

## Reference answer and check

The formula is `P_abs = P_gauge + P_atm` after both pressures use the same unit. G is **601,325 Pa absolute**. A is **500,000 Pa absolute**. Keep the pressure basis with each value. Obtain a source definition for unlabeled rows before calculating.

```python
from evaluation.reference import pressure_to_absolute_pa

assert pressure_to_absolute_pa(5, "bar", "gauge", 101325) == 601325
assert pressure_to_absolute_pa(5, "bar", "absolute", 101325) == 500000
```

## Evidence and limits

These values follow directly from the supplied conversion constant and atmospheric pressure. Actual atmospheric pressure may differ by location and time. This exercise does not prescribe 101,325 Pa for every real input. The helper tests conversion and invalid inputs. It does not test instrument calibration or simulator behavior.
