# Reproducible batch simulation and failure diagnosis

**Project:** PIPESIM Profile Batch Runner  
**Focus:** software QA, result interpretation, reproducibility, and debugging with evidence

Batch automation must preserve the meaning of the original simulation. It must also make failures easy to investigate. This Python application runs saved network cases through the PIPESIM Toolkit. It extracts physical-flowline profiles and writes reports with explicit units and diagnostics.

Each case runs from an isolated model copy. The application records the runtime identity, requested study, available input snapshots, raw results, and case status. A failed case produces diagnostics. Other scheduled cases can still complete.

## Decisions that matter

- Check the Toolkit and engine release years before opening a model. Record the actual loaded versions. Do not infer versions from an installation-folder name.
- Preserve native point order, repeated positions, and flowing-phase quantities. Stock-tank properties are not substitutes for unavailable in-situ properties.
- Convert liquid and total mass rates to a common basis before calculating liquid mass percent. Results remain unavailable when inputs are missing, denominators are invalid, or ratios are outside the valid range. These conditions produce warnings.
- Retain an unmapped branch as an explicitly labelled branch. Sparse equipment labels do not justify inventing pipeline identities.
- Use the same model, study, boundaries, runtime, and returned units to compare results with a GUI run. A discrepancy does not justify an arbitrary correction factor.

## Source evidence reviewed

These filenames refer to the private implementation. This public portfolio does not include these files.

| Evidence | What it establishes |
| --- | --- |
| `profile_batch/toolkit_runtime.py`; `tests/test_toolkit_runtime.py` | Runtime identity checks, rejection of mismatched releases, and acceptance of matching releases in mocked tests |
| `toolkit_worker.py`; `profile_batch/runner.py` | Saved-condition requests, input snapshots, isolated copies, raw diagnostics, and batch scheduling |
| `profile_batch/reporting.py`; `tests/test_profiles.py` | Unit handling, sparse equipment mapping, missing results, point alignment, and failed-run reporting |
| `tests/test_toolkit_discovery.py` | Detection errors, timeouts, and candidate selection |

## Transfer to AI evaluation

This project supports debugging tasks that distinguish an extraction bug from a difference in the underlying simulation. A strong answer states which evidence is missing and proposes a controlled comparison. It preserves the original values until evidence establishes the cause. The project also supports code-review tasks about failure propagation and misleading success states.

## Validation boundary

The portfolio review covered the implementation and test source. It did not run a live PIPESIM simulation again. The recorded live attempt was blocked while the local simulation server opened a model. This case study does not claim a completed live comparison.

The older README describes a release restriction that the current runtime code and tests no longer impose. This case study follows the code. Matching release years alone do not prove that every combination of vendor versions works.

The implementation, licensed software, models, and result files remain private. This portfolio does not distribute them.

Try the related public exercise: [diagnosing mismatches](../evaluation/tasks/05-mismatch-diagnosis.md).

[Technical terms](../docs/glossary.md) · [Return to the portfolio](../README.md)
