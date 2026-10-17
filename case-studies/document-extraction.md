# Traceable extraction from engineering drawings

**Project:** Pipeline Elevation Profile Extractor  
**Focus:** structured-data extraction, uncertainty, spatial reasoning, and review workflows

Engineering PDFs often contain more than one plausible line, text stored in a different order from its visual placement, and labels that are vector outlines rather than text. This Python desktop application extracts longitudinal-profile data while retaining evidence about how each point was obtained.

The workflow scores vector candidates, calibrates drawing axes, aligns elevation labels by position, orders and merges sheets, and exports profile data with QA information. A review dialog allows point corrections and protection of important features. Windows OCR supports outlined text, while optional raster processing provides an additional fallback.

## Decisions that matter

- Use geometry and surrounding context to distinguish a longitudinal profile from borders, gridlines, and plan-view lines. Color alone is insufficient.
- Align labels with plotted stations rather than relying on PDF text-storage order.
- Identify OCR-derived calibration and recovered vertices explicitly. An inferred elevation must not appear to be directly transcribed text.
- Compare shared sheet boundaries and report gaps, overlaps, or elevation disagreement before merging.
- Preserve boundaries, special features, protected points, and local extrema during optional simplification. Low-confidence or ambiguous extraction requires review.

## Source evidence reviewed

These are filenames in the private implementation, not files included in this public portfolio.

| Evidence | What it establishes |
| --- | --- |
| `extraction/profile_extractor.py`; `extraction/axis_calibration.py` | Calibration, point provenance, recovery warnings, and confidence-based review decisions |
| `tests/test_axis_and_vectors.py`; `tests/test_ocr_fallback.py` | Axis fitting, rotation handling, candidate selection, and OCR calibration cases |
| `processing/profile_merge.py`; `tests/test_merge_and_validation.py` | Sheet order, boundary comparison, gaps, and overlaps |
| `processing/simplification.py`; `tests/test_simplification.py` | Preservation of important points during simplification |

Implementation module paths above are relative to the `pipeline_profile_extractor` package; test paths are relative to the project root.

## Transfer to AI evaluation

This project motivates extraction tasks scored on both accuracy and provenance: identify which value was read directly, which was inferred, and which remains uncertain. A strong response preserves source location, flags ambiguous mappings, and resists filling missing labels with plausible but unsupported numbers. Boundary inconsistencies make useful adversarial cases for testing whether a model checks the entire document.

## Validation boundary

The implementation and test source were reviewed; no private drawing was processed again for this portfolio. Some integration tests require separately supplied reference PDFs and explicitly skip when those files are absent. Therefore, test availability is not a claim of general extraction accuracy across drawing styles. The implementation, reference drawings, extracted engineering data, and private identifiers are not distributed here.

Try the related public exercise: [extraction confidence](../evaluation/tasks/03-extraction-review.md).

[Return to the portfolio](../README.md)
