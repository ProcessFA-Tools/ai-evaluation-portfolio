# Engineering AI evaluation practice

Five synthetic exercises show how to evaluate engineering answers. Each exercise defines grading criteria, compares candidate answers, preserves uncertainty, and checks specific calculations with code.

These are **AI-assisted practice samples written for this portfolio**. The portfolio author created every prompt, dataset, candidate answer, ranking, and reference answer for illustration. The candidates are **not outputs collected from real models**. There was no model experiment, hiring evaluation, or production deployment. Scores describe these authored examples only. They do not measure model performance or provide benchmark results.

The exercises contain no customer data, employer documents, licensed simulator outputs, or private project source code. The Python helpers perform only the basic checks described here. They run without commercial engineering software. The [glossary](../docs/glossary.md) defines technical terms used in these exercises.

## Sample index

| Task | Evaluation skill | Main correctness risk |
| --- | --- | --- |
| [01: Pressure basis](tasks/01-pressure-basis.md) | Unit and reference-state reasoning | Treating gauge pressure as absolute |
| [02: Phase completeness](tasks/02-phase-completeness.md) | Structured-data integrity | Inventing zero for a missing phase |
| [03: Extraction review](tasks/03-extraction-review.md) | Evidence-aware annotation | Treating confidence as proof |
| [04: Constrained routing](tasks/04-constrained-routing.md) | Following hard constraints | Choosing an infeasible cheap route |
| [05: Mismatch diagnosis](tasks/05-mismatch-diagnosis.md) | Technical error analysis | Applying an unsupported correction |

Each task contains all material needed for the exercise:

- A prompt and two illustrative candidate answers.
- A rubric with criteria, scores, and reasons for the ranking.
- A reference answer and limits of the evidence.

Candidate quality and order vary. The labels A and B do not represent particular systems.

## Scoring rules

Each task has four criteria. Each criterion receives 0, 1, or 2 points under the task's scoring rules. The total score ranges from 0 to 8. Each task also records a separate critical gate. A response that fails this gate is unacceptable, even if its writing earns points. A score must never hide a critical engineering error.

An acceptable response requires **at least 7/8 and no critical gate failure**. When necessary information is missing, the answer must state this limit or request a review. The answer must not invent data. Evaluation uses the supplied task. Style preferences and unsupported external assumptions do not determine the score.

The published scores are worked examples. They do not show agreement between independent reviewers.

To practice review:

1. Hide the scored sections.
2. Grade both answers independently.
3. Compare disagreements against the stated scoring rules.

A credible future model evaluation requires:

- Tasks reserved for evaluation.
- Records of the model, version, and settings.
- Actual model outputs.
- Independent grading.
- A documented method for selecting samples.

## Run the checks

Use Python 3.10 or newer. The portfolio workflow checks Python 3.10 and 3.12. Run this command from the repository root:

```console
python -m unittest discover -s tests -v
```

The helpers require no package installation. [reference.py](reference.py) contains the reference functions. [The tests](../tests/test_reference.py) cover task examples, incomplete data, constraint boundaries, invalid inputs, and undefined comparisons. Passing tests establishes helper behavior for the tested cases. It does not validate a simulator, an extraction model, a physical design, or an AI system.

## Scope and reproducibility

The prompts specify the arithmetic and acceptance policies. They define atmospheric pressure, balance tolerance, confidence threshold, routing constraints, and the comparison denominator. The 0.95 confidence threshold is an invented exercise policy. It is not a calibrated industry rule. Route selection uses only the four listed alternatives. Statements about cause, correctness, and missing evidence apply only to the supplied synthetic data.
