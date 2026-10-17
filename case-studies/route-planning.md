# Route planning with explicit constraints

**Project:** Network LCP Pipeline Generator  
**Focus:** algorithm review, constrained reasoning, scenario comparison, and reproducibility

The geometrically shortest pipeline route can be unsuitable when terrain, crossings, and exclusion areas matter. This QGIS plugin combines a prepared cost raster or a terrain-derived cost workflow with saved constraints to generate candidate routes for engineering review.

The workflow keeps cost settings and constraints alongside route outputs. It can produce alternative scenarios, raw and smoothed geometries, elevation profiles, crossing/violation audit layers, and CSV inputs for a later hydraulic-evaluation step.

## Decisions that matter

- Route on a defined cost surface. Raw elevation and raw slope are not interchangeable with traversal cost.
- Treat NoData as unreachable and reject negative raster costs. Reject endpoints outside the raster or on blocked cells.
- Allow diagonal movement only when both adjoining orthogonal cells are traversable. This prevents a route from cutting through the corner between blocked cells.
- Weight a step by cell cost and physical step distance. Horizontal, vertical, and diagonal moves need consistent geometry.
- Keep cost-setting assumptions visible when comparing scenarios. A lower score under one set of weights does not establish universal engineering superiority.

## Source evidence reviewed

These are filenames in the private implementation, not files included in this public portfolio.

| Evidence | What it establishes |
| --- | --- |
| `core/path_worker.py`; `tests/test_path_worker.py` | Grid validation, distance-weighted route search, orthogonal movement, and blocked-corner behavior |
| `core/cost_settings.py`; `tests/test_cost_settings.py` | Cost-setting validation, invalid buffers, and forbidden-area policy checks |
| `core/route_audit.py`; `core/route_dashboard.py` | Crossing/violation review and scenario comparison components |
| `core/constraint_package.py`; `docs/Verification.md` | Persistent package design and the distinction between processing checks and interactive checks |

## Transfer to AI evaluation

A compact grid can expose a flawed AI-generated pathfinding answer immediately. Evaluation can test whether a proposed route crosses a blocked corner, whether its cost matches the stated formula, and whether the explanation distinguishes a hard constraint from a soft penalty. Scenario tasks also reveal whether a model states its assumptions before recommending a route.

## Validation boundary

This case study was checked against implementation, regression-test source, and verification notes; QGIS processing and interactive drawing were not rerun for this portfolio. The existing notes leave an interactive constraint-editor check outstanding. Candidate routes are screening outputs and require hydraulic, constructability, and engineering review. The implementation incorporates GPL-3.0 upstream work with preserved attribution; this is a description of an integration project, not a claim that all underlying algorithms are original. Code, project coordinates, terrain datasets, and generated routes are not distributed here.

Try the related public exercise: [constrained routing](../evaluation/tasks/04-constrained-routing.md).

[Return to the portfolio](../README.md)
