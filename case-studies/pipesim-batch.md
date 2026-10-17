# Reproducible batch simulation and failure diagnosis

**Project:** PIPESIM Profile Batch Runner  
**Focus:** software QA, result interpretation, reproducibility, and evidence-based debugging

Batch automation needs to preserve the meaning of the original simulation while making failures easy to investigate. This Python application runs saved network cases through the PIPESIM Toolkit, extracts physical-flowline profiles, and writes reports with explicit units and diagnostics.

Each case runs from an isolated model copy. The application records runtime identity, requested study, available input snapshots, raw results, and case status. A failed case produces failure diagnostics and does not prevent other scheduled cases from completing.

## Decisions that matter

- Check the Toolkit and engine release years before opening a model. Record the actual loaded versions instead of inferring them from an installation-folder name.
- Preserve native point order, repeated positions, and flowing-phase quantities. Stock-tank properties are not substitutes for unavailable in-situ properties.
- Convert liquid and total mass rates to a common basis before calculating liquid mass percent. Missing inputs, invalid denominators, and out-of-range ratios remain unavailable with warnings.
- Retain an unmapped branch as an explicitly labelled branch. Sparse equipment labels do not justify inventing pipeline identities.
- Compare the same model, study, boundaries, runtime, and returned units when investigating disagreement with a GUI run. A discrepancy does not justify an arbitrary correction factor.

## Source evidence reviewed

These are filenames in the private implementation, not files included in this public portfolio.

| Evidence | What it establishes |
| --- | --- |
| `profile_batch/toolkit_runtime.py`; `tests/test_toolkit_runtime.py` | Runtime identity checks, rejection of mismatched releases, and acceptance of matching releases in mocked tests |
| `toolkit_worker.py`; `profile_batch/runner.py` | Saved-condition requests, input snapshots, isolated copies, raw diagnostics, and batch scheduling |
| `profile_batch/reporting.py`; `tests/test_profiles.py` | Unit handling, sparse equipment mapping, missing results, point alignment, and failed-run reporting |
| `tests/test_toolkit_discovery.py` | Detection errors, timeouts, and candidate selection |

## Transfer to AI evaluation

This is a basis for debugging tasks where a model must distinguish an extraction bug from a different underlying simulation. Good answers state which evidence is missing, propose a controlled comparison, and preserve the original values until a cause is demonstrated. It also supports code-review tasks about failure propagation and misleading success states.

## Validation boundary

The implementation and test source were reviewed; no live PIPESIM simulation was rerun for this portfolio. The recorded live attempt was blocked while the local simulation server opened a model, so a completed live comparison is not claimed. The older README describes a release restriction that the current runtime code and tests no longer impose; this case study follows the code. Matching release years alone are not proof of every vendor-version combination working. The implementation, licensed software, models, and result files remain private and are not distributed here.

Try the related public exercise: [diagnosing mismatches](../evaluation/tasks/05-mismatch-diagnosis.md).

[Return to the portfolio](../README.md)
