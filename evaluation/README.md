# Engineering AI evaluation practice

Five synthetic exercises show how to turn engineering requirements into explicit grading criteria, compare candidate responses, preserve uncertainty, and verify narrow calculations with code.

These are **AI-assisted practice samples drafted for this portfolio**. Every prompt, dataset, candidate response, ranking, and reference answer was authored for illustration. The candidates are **not outputs collected from real models**. There was no model experiment, hiring evaluation, or production deployment. Scores describe these authored examples only; they are not benchmark results or evidence of model performance.

No customer data, employer documents, licensed simulator outputs, or private project source code is included. The Python helpers implement only the elementary checks described here and run without commercial engineering software.

## Sample index

| Task | Evaluation skill | Main correctness risk |
| --- | --- | --- |
| [01: Pressure basis](tasks/01-pressure-basis.md) | Unit and reference-state reasoning | Treating gauge pressure as absolute |
| [02: Phase completeness](tasks/02-phase-completeness.md) | Structured-data integrity | Inventing zero for a missing phase |
| [03: Extraction review](tasks/03-extraction-review.md) | Evidence-aware annotation | Treating confidence as proof |
| [04: Constrained routing](tasks/04-constrained-routing.md) | Following hard constraints | Choosing an infeasible cheap route |
| [05: Mismatch diagnosis](tasks/05-mismatch-diagnosis.md) | Technical error analysis | Applying an unsupported correction |

Each task is self-contained: prompt, two explicitly illustrative candidate answers, criterion-level rubric, scores, ranking rationale, reference answer, and limits of the evidence. Candidate quality and order vary; the labels A and B do not represent particular systems.

## Scoring rules

Each of four criteria receives 0, 1, or 2 points, using the task's anchors. Scores range from 0 to 8. A critical correctness gate is recorded separately: a response that triggers a gate is unacceptable even if its writing earns points. A score alone must never hide a fatal engineering error.

For these exercises, an acceptable response requires **at least 7/8 and no critical gate failure**. Missing necessary information should lead to a qualified answer or a review request, not invented data. Evaluation focuses on the supplied task, not style preferences or unsupported external assumptions.

The published scores are worked examples, not independent inter-rater agreement. To practice review, hide the scored sections, grade both answers independently, then compare disagreements against the stated anchors. A credible future model evaluation would require held-out tasks, recorded model/version/settings, genuine outputs, independent grading, and a documented sampling method.

## Run the checks

From the repository root, with Python 3.9 or newer:

```console
python -m unittest discover -s tests -v
```

No packages need installing. [reference.py](reference.py) contains the small reference functions; [the tests](../tests/test_reference.py) cover task examples, incomplete data, constraint boundaries, invalid inputs, and undefined comparisons. Passing tests establishes those helper behaviors for the tested cases. It does not validate a simulator, an extraction model, a physical design, or an AI system.

## Scope and reproducibility

The arithmetic and acceptance policies are fully specified in the prompts. Pressure atmosphere, balance tolerance, confidence cutoff, routing constraints, and comparison denominator are explicit rather than silently assumed. The 0.95 confidence threshold is an invented exercise policy, not a calibrated industry rule. Routing optimizes only over the four listed alternatives. All statements about cause, correctness, and missing evidence are limited to the supplied synthetic data.
