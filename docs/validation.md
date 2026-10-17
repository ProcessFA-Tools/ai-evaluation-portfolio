# Validation record

## Public evaluation pack

The reference implementation is designed to run with Python 3.10+ and the standard library. The test suite exercises calculations and decision rules, including invalid inputs and boundary cases.

From the repository root:

```sh
python -m unittest discover -s tests -v
python tools/check_links.py
```

The [Portfolio checks workflow](https://github.com/ProcessFA-Tools/ai-evaluation-portfolio/actions/workflows/verify.yml) runs these checks on Python 3.10 and 3.12. Its status and logs are the current evidence for the public repository.

## Private project case studies

The four case studies were written after inspecting application source and associated tests. File references in those case studies identify the inspected components, not downloadable public source.

No licensed PIPESIM or Multiflash simulation was rerun as part of preparing this portfolio. No new end-to-end QGIS or source-drawing extraction result is claimed. The publicly runnable examples demonstrate specific evaluation concepts independently of those applications.

The PIPESIM case study also records a runtime documentation discrepancy: current compatibility logic and tests are stronger evidence than the older release-specific README text. A live engine-startup blocker remains distinct from the correctness of unit conversions and report logic.

## What these checks establish

The checks support the specific synthetic examples and tested input contracts. They do not establish that a numerical model is valid for a real fluid, that a selected route is feasible on real terrain, or that a recovered drawing value is accurate without source review. Those conclusions require their own inputs and validation evidence.
