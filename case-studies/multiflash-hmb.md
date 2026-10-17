# Thermodynamic reporting with traceable inputs

**Project:** Multiflash HMB Creator  
**Focus:** numerical reasoning, data provenance, unit conversion, and missing data

A thermodynamic report can look credible while it uses the wrong pressure basis. It can also change a phase name or replace an unavailable property with zero. This project makes these decisions visible when it converts pressure/temperature cases into heat and material balance reports.

The Python application reads independent cases or mapped endpoints from simulation exports. It calls an installed Multiflash engine in a separate worker process. It produces Excel and HTML reports. Each independent case uses the original overall feed. Source cells, original units, normalized inputs, explicit overrides, and input hashes support later review.

## Decisions that matter

- Compare the source pressure and temperature with the calculated state in the source units. Gauge pressure uses an explicit atmospheric reference. Pressure differences do not receive an atmospheric offset.
- Preserve exact returned phase identities such as `LIQUID1` and `LIQUID2`. An unreturned phase and a returned phase with an unavailable property are different states.
- Keep unavailable properties blank with a reason. A missing viscosity is not a zero viscosity.
- Separate reporting choices from calculation evidence. Changes to display units do not alter the archive of raw SI results.
- Treat a worker failure or timeout as failure. Retain the diagnostics. Do not produce a misleading completed report.

## Source evidence reviewed

These filenames refer to the private implementation. This public portfolio does not include these files.

| Evidence | What it establishes |
| --- | --- |
| `flash_conditions.py`; `test_condition_phase_layout.py` | Source/flash state comparison, gauge conversion, real mismatch detection, and missing-state handling |
| `phase_view.py`; `test_phases_diagnostics.py` | Phase identity, phase visibility, and unavailable-property behavior |
| `excel_bridge.py`; `test_excel_bridge.py` | Rejection of incomplete rows, duplicate case names, unsupported units, and formulas without cached values; worker-failure handling |
| `reporting.py`; `test_reporting.py` | Report content, provenance, and source/template preservation checks |

## Transfer to AI evaluation

A useful evaluation task asks a model to review a plausible report. The report can contain a gauge/absolute-pressure mismatch, an invented phase label, or an unjustified zero. A strong answer identifies the exact evidence and explains the physical consequence. It requests missing information when needed. These failures provide examples for evaluation prompts and scoring rubrics.

## Validation boundary

The portfolio review checked this case study against the implementation and test source. It did not run the native engine again. The adapter accepts a specifically validated engine binary. This case study does not claim compatibility across engine versions. A software test or sample-fluid run does not establish that a fluid matches a separate hydraulic model. Engineering results require review.

The implementation, vendor software, models, and result files remain private. This portfolio does not distribute them.

Try the related public exercises: [pressure references](../evaluation/tasks/01-pressure-basis.md) and [missing versus zero](../evaluation/tasks/02-phase-completeness.md).

[Technical terms](../docs/glossary.md) · [Return to the portfolio](../README.md)
