# Thermodynamic reporting with traceable inputs

**Project:** Multiflash HMB Creator  
**Focus:** numerical reasoning, data provenance, unit conversion, and missing-data handling

A thermodynamic report can look credible while silently using the wrong pressure basis, changing a phase name, or filling an unavailable property with zero. This project makes those decisions visible when converting pressure/temperature cases into heat and material balance reports.

The Python application reads independent cases or mapped simulation-export endpoints, calls an installed Multiflash engine in a separate worker process, and produces Excel and HTML reports. Each independent case uses the original overall feed. Source cells, original units, normalized inputs, explicit overrides, and input hashes support later review.

## Decisions that matter

- Compare the source pressure and temperature with the calculated state in the source units. Gauge pressure uses an explicit atmospheric reference; pressure differences do not receive an atmospheric offset.
- Preserve exact returned phase identities such as `LIQUID1` and `LIQUID2`. An unreturned phase and a returned phase with an unavailable property are different states.
- Keep unavailable properties blank with a reason. A missing viscosity is not a zero viscosity.
- Separate reporting choices from calculation evidence: display-unit changes do not alter the raw SI result archive.
- Treat worker failure or timeout as failure, retaining diagnostics without producing a misleading completed report.

## Source evidence reviewed

These are filenames in the private implementation, not files included in this public portfolio.

| Evidence | What it establishes |
| --- | --- |
| `flash_conditions.py`; `test_condition_phase_layout.py` | Source/flash state comparison, gauge conversion, real mismatch detection, and missing-state handling |
| `phase_view.py`; `test_phases_diagnostics.py` | Phase identity, phase visibility, and unavailable-property behavior |
| `excel_bridge.py`; `test_excel_bridge.py` | Rejection of incomplete rows, duplicate case names, unsupported units, and formulas without cached values; worker-failure handling |
| `reporting.py`; `test_reporting.py` | Report content, provenance, and source/template preservation checks |

## Transfer to AI evaluation

A useful evaluation task asks a model to review a plausible report and find a gauge/absolute-pressure mismatch, an invented phase label, or an unjustified zero. A strong answer identifies the exact evidence, explains the physical consequence, and requests missing information when needed. This project supplies concrete failure modes for designing those prompts and grading rubrics.

## Validation boundary

This case study was checked against implementation and test source; the native engine was not rerun for this portfolio. The adapter accepts a specifically validated engine binary, so broad version compatibility is not claimed. A software test or sample-fluid run does not establish that a fluid matches a separate hydraulic model. Engineering results require review. The implementation, vendor software, models, and result files remain private and are not distributed here.

Try the related public exercises: [pressure references](../evaluation/tasks/01-pressure-basis.md) and [missing versus zero](../evaluation/tasks/02-phase-completeness.md).

[Return to the portfolio](../README.md)
