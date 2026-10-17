# ProcessFA Tools

## Engineering judgment for AI evaluation

Python automation, numerical verification, and technical QA for engineering workflows.

This portfolio brings together four engineering software case studies and five runnable evaluation exercises. The focus is on assessing whether a technical answer is correct, preserving evidence, and explaining when the available information is insufficient.

**Relevant work:** engineering AI evaluation · Python code review · technical task design · rubric writing · data quality and QA

[Explore the evaluation exercises](evaluation/README.md) · [Review validation evidence](docs/validation.md) · [Data and authorship](docs/data-and-authorship.md)

### Start here

For a quick review, read the [pressure-reference evaluation](evaluation/tasks/01-pressure-basis.md), inspect the [reference implementation](evaluation/reference.py), and run the tests. Each exercise includes a prompt, two illustrative answers, scored criteria, a ranking rationale, and a reference answer.

```sh
python -m unittest discover -s tests -v
```

Python 3.10 or newer is sufficient. The exercises use the standard library and synthetic data; no simulation license, API key, or external service is required.

### Selected engineering projects

| Case study | Engineering problem | Evaluation skills demonstrated |
| --- | --- | --- |
| [Multiflash HMB reporting](case-studies/multiflash-hmb.md) | Turn thermodynamic outputs into traceable reports | Pressure references, units, phase identity, missing data, evidence checks |
| [PIPESIM batch workflows](case-studies/pipesim-batch.md) | Run saved cases and retain diagnostic context | Reproducibility, compatibility checks, failure diagnosis, justified conclusions |
| [Constrained route planning](case-studies/route-planning.md) | Compare route alternatives while respecting constraints | Feasibility checks, assumptions, optimization criteria, edge cases |
| [Engineering document extraction](case-studies/document-extraction.md) | Convert profile drawings into reviewable structured data | Extraction quality, calibration, uncertainty, human review |

The case studies summarize source and test inspection of private engineering projects. They explain the design and its limits; the original applications and engineering datasets are not distributed in this repository. Publicly runnable evidence is provided by the evaluation exercises below.

### Evaluation work samples

| Exercise | What the reviewer has to notice |
| --- | --- |
| [01 · Pressure reference](evaluation/tasks/01-pressure-basis.md) | Equal-looking pressure values can describe different states when gauge and absolute references differ. |
| [02 · Missing versus zero](evaluation/tasks/02-phase-completeness.md) | An absent phase value must not be silently substituted with zero. |
| [03 · Extraction confidence](evaluation/tasks/03-extraction-review.md) | A plausible extracted number can still require review when the evidence is weak. |
| [04 · Constrained routing](evaluation/tasks/04-constrained-routing.md) | A cheap route is not acceptable if it violates a hard constraint. |
| [05 · Diagnosing mismatches](evaluation/tasks/05-mismatch-diagnosis.md) | A difference in outputs does not justify an arbitrary correction factor. |

These are AI-assisted practice samples created for this portfolio. Candidate answers are illustrative examples, not outputs attributed to an actual model. Rubric scores describe those examples and are not model benchmark results.

### How I approach technical evaluation

1. Establish the task, units, constraints, and evidence needed for a correct answer.
2. Check the result against a reference calculation or an explicit acceptance rule.
3. Examine edge cases: missing inputs, invalid values, conflicting assumptions, and failed dependencies.
4. Record which criteria passed, which failed, and why the failures matter.
5. Keep unsupported conclusions visible and identify what evidence would resolve them.

### Verify the work

[![Portfolio checks](https://github.com/ProcessFA-Tools/ai-evaluation-portfolio/actions/workflows/verify.yml/badge.svg)](https://github.com/ProcessFA-Tools/ai-evaluation-portfolio/actions/workflows/verify.yml)

- [Reference code](evaluation/reference.py) and [automated tests](tests/test_reference.py)
- [Validation scope and limitations](docs/validation.md)
- [Synthetic-data and authorship notes](docs/data-and-authorship.md)

For a public technical question about a sample, [open an issue](https://github.com/ProcessFA-Tools/ai-evaluation-portfolio/issues). Please use a synthetic example and omit private data.
