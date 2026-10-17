# Traceable extraction from engineering drawings

**Project:** Pipeline Elevation Profile Extractor  
**Focus:** extraction of structured data, uncertainty, spatial reasoning, and review

Engineering PDFs can contain several plausible profile lines. The stored text order can differ from the visible label order. Some labels contain vector outlines instead of text. This Python desktop application extracts longitudinal-profile data. It retains evidence about the source of each point.

The application performs these steps:

1. Score vector candidates.
2. Calibrate the drawing axes.
3. Align elevation labels by position.
4. Order the sheets.
5. Merge the sheets.
6. Export profile data with QA information.

A review dialog lets the user correct points and protect important features. Windows OCR supports outlined text. Optional raster processing provides another extraction method when the other methods fail.

## Decisions that matter

- Use geometry and surrounding context to distinguish a longitudinal profile from borders, gridlines, and plan-view lines. Color alone is insufficient.
- Align labels with plotted stations. Do not use the PDF text-storage order to determine alignment.
- Identify calibration that uses OCR. Identify recovered vertices. Do not present an inferred elevation as text read directly from the drawing.
- Compare shared sheet boundaries before merging. Report gaps, overlaps, or elevation disagreement.
- Preserve boundaries, special features, protected points, and local extrema during optional simplification. Extraction requires review when confidence is low or the result is ambiguous.

## Source evidence reviewed

These filenames refer to the private implementation. This public portfolio does not include these files.

| Evidence | What it establishes |
| --- | --- |
| `extraction/profile_extractor.py`; `extraction/axis_calibration.py` | Calibration, point provenance, recovery warnings, and confidence-based review decisions |
| `tests/test_axis_and_vectors.py`; `tests/test_ocr_fallback.py` | Axis fitting, rotation handling, candidate selection, and OCR calibration cases |
| `processing/profile_merge.py`; `tests/test_merge_and_validation.py` | Sheet order, boundary comparison, gaps, and overlaps |
| `processing/simplification.py`; `tests/test_simplification.py` | Preservation of important points during simplification |

The implementation paths are relative to the `pipeline_profile_extractor` package. The test paths are relative to the project root.

## Transfer to AI evaluation

This project supports extraction tasks that assess accuracy and provenance. The tasks ask the model to distinguish directly read values, inferred values, and uncertain values. A strong answer records each source location and identifies ambiguous mappings. It does not fill missing labels with plausible but unsupported numbers. Inconsistent sheet boundaries help test whether a model checks the entire document.

## Validation boundary

The portfolio review covered the implementation and test source. It did not process private drawings again. Some integration tests require separately supplied reference PDFs. These tests explicitly skip when those files are absent. The available tests do not establish extraction accuracy across all drawing styles.

This portfolio does not distribute the implementation, reference drawings, extracted engineering data, or private identifiers.

Try the related public exercise: [extraction confidence](../evaluation/tasks/03-extraction-review.md).

[Technical terms](../docs/glossary.md) · [Return to the portfolio](../README.md)
