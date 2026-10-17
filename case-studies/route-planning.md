# Route planning with explicit constraints

**Project:** Network LCP Pipeline Generator  
**Focus:** algorithm review, constrained reasoning, scenario comparison, and reproducibility

The geometrically shortest pipeline route can be unsuitable when terrain, crossings, and exclusion areas matter. This QGIS plugin uses a prepared cost raster or a workflow that derives costs from terrain. It applies saved constraints to generate candidate routes for engineering review.

The workflow stores cost settings and constraints with the route outputs. It can produce these outputs:

- Alternative scenarios.
- Raw and smoothed geometries.
- Elevation profiles.
- Layers for checking crossings and violations.
- CSV inputs for later hydraulic evaluation.

## Decisions that matter

- Route on a defined cost surface. Raw elevation and raw slope are not interchangeable with traversal cost.
- Treat NoData as unreachable. Reject negative raster costs. Reject endpoints outside the raster or on blocked cells.
- Allow diagonal movement only when both adjoining orthogonal cells are traversable. This prevents a route from cutting through the corner between blocked cells.
- Weight a step by cell cost and physical step distance. Horizontal, vertical, and diagonal moves need consistent geometry.
- Keep assumptions about cost settings visible when comparing scenarios. A lower score under one set of weights does not prove that a route is better for every engineering objective.

## Source evidence reviewed

These filenames refer to the private implementation. This public portfolio does not include these files.

| Evidence | What it establishes |
| --- | --- |
| `core/path_worker.py`; `tests/test_path_worker.py` | Grid validation, distance-weighted route search, orthogonal movement, and blocked-corner behavior |
| `core/cost_settings.py`; `tests/test_cost_settings.py` | Cost-setting validation, invalid buffers, and forbidden-area policy checks |
| `core/route_audit.py`; `core/route_dashboard.py` | Crossing/violation review and scenario comparison components |
| `core/constraint_package.py`; `docs/Verification.md` | Persistent package design and the distinction between processing checks and interactive checks |

## Transfer to AI evaluation

A compact grid can expose errors in an AI-generated pathfinding answer. An evaluation can check these points:

- Does the proposed route cross a blocked corner?
- Does the route cost match the stated formula?
- Does the explanation distinguish a hard constraint from a soft penalty?

Scenario tasks also show whether a model states its assumptions before recommending a route.

## Validation boundary

The portfolio review checked this case study against the implementation, regression-test source, and verification notes. It did not repeat QGIS processing or interactive drawing. The existing notes record an incomplete check of the interactive constraint editor. Candidate routes support screening. They require hydraulic, constructability, and engineering review.

The implementation includes GPL-3.0 upstream work and preserves its attribution. This case study describes an integration project. It does not claim that all underlying algorithms are original. This portfolio does not distribute code, project coordinates, terrain datasets, or generated routes.

Try the related public exercise: [constrained routing](../evaluation/tasks/04-constrained-routing.md).

[Technical terms](../docs/glossary.md) · [Return to the portfolio](../README.md)
