# ProcessFA Tools

## Check engineering answers from AI

This portfolio covers Python automation, numerical checks, and quality assurance (QA) for engineering work.

It contains four software case studies and five evaluation exercises that you can run. The examples show how to check technical answers, keep evidence, and identify missing information.

**Areas of work:** engineering AI evaluation, Python code review, technical task design, scoring rules, and data quality.

[Read the evaluation exercises](evaluation/README.md) · [Check the validation evidence](docs/validation.md) · [Read the data and authorship notes](docs/data-and-authorship.md) · [Find a technical term](docs/glossary.md)

### Start here

1. Read the [pressure-reference exercise](evaluation/tasks/01-pressure-basis.md).
2. Read the [reference code](evaluation/reference.py).
3. Run the tests from the repository folder:

```sh
python -m unittest discover -s tests -v
```

Each exercise contains a prompt, two example answers, scoring rules, scores, a reason for the ranking, and a reference answer.

Use Python 3.10 or newer. The exercises use the Python standard library and synthetic data. They do not need a simulation license, an API key, or an external service.

### Selected engineering projects

| Case study | Problem | Skills used to check the result |
| --- | --- | --- |
| [Multiflash HMB reports](case-studies/multiflash-hmb.md) | Create thermodynamic reports with evidence for each input | Check pressure references, units, phase names, and missing data |
| [PIPESIM batch workflows](case-studies/pipesim-batch.md) | Run saved cases and keep data that helps explain failures | Check repeatability, software compatibility, causes of failure, and conclusions |
| [Route planning with constraints](case-studies/route-planning.md) | Compare routes that must meet specified limits | Check whether routes meet limits, compare costs, and identify assumptions |
| [Data extraction from drawings](case-studies/document-extraction.md) | Convert profile drawings into data that a reviewer can check | Check extracted values, calibration, uncertainty, and the need for human review |

The case studies describe code and tests from private engineering projects. They explain the design and its limits. This repository does not contain the original applications or engineering datasets. You can run the public evaluation exercises below.

### Evaluation work samples

| Exercise | What the reviewer must check |
| --- | --- |
| [01 · Pressure reference](evaluation/tasks/01-pressure-basis.md) | The same number can describe different pressures when one value is gauge and the other is absolute. |
| [02 · Missing versus zero](evaluation/tasks/02-phase-completeness.md) | An answer must not replace a missing phase value with zero. |
| [03 · Extraction confidence](evaluation/tasks/03-extraction-review.md) | An extracted number can look correct but still need review because the evidence is weak. |
| [04 · Route constraints](evaluation/tasks/04-constrained-routing.md) | A route is unacceptable if it breaks a mandatory rule, even when its cost is low. |
| [05 · Differences in results](evaluation/tasks/05-mismatch-diagnosis.md) | A difference in results does not justify an arbitrary correction factor. |

AI helped create these practice samples. The candidate answers are examples written for this portfolio. They are not recorded outputs from an AI model. The scores apply to these examples and do not measure model performance.

### How I check technical answers

1. Identify the task, units, constraints, and evidence needed for a correct answer.
2. Check the result against a reference calculation or a stated acceptance rule.
3. Check missing inputs, invalid values, conflicting assumptions, and failed dependencies.
4. Record which criteria pass or fail.
5. Explain why each failure matters.
6. Identify conclusions that lack evidence.
7. State which evidence would resolve the uncertainty.

### Check the work

[![Portfolio checks](https://github.com/ProcessFA-Tools/ai-evaluation-portfolio/actions/workflows/verify.yml/badge.svg)](https://github.com/ProcessFA-Tools/ai-evaluation-portfolio/actions/workflows/verify.yml)

- [Read the reference code](evaluation/reference.py).
- [Read the automated tests](tests/test_reference.py).
- [Check the validation scope and limits](docs/validation.md).
- [Read the data and authorship notes](docs/data-and-authorship.md).

For a technical question about a sample, [open a public issue](https://github.com/ProcessFA-Tools/ai-evaluation-portfolio/issues). Use a synthetic example. Do not include private data.
