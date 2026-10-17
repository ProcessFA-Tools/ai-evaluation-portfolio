# 04 — Apply hard constraints before minimizing cost

**Provenance:** AI-assisted synthetic portfolio practice. Both responses are authored illustrations, not real model outputs. Candidate A intentionally chooses an infeasible alternative.

## Prompt

Select one of four synthetic route alternatives. Minimize the supplied total cost score. Two constraints are mandatory: **no protected-area crossing** and **maximum slope <= 10%**. Cost scores already include length-related expense; do not replace the stated objective with shortest length. If feasible routes tie in cost, prefer shorter length, then alphabetical name.

| Route | Total cost score | Length (km) | Crosses protected area? | Maximum slope |
| --- | ---: | ---: | --- | ---: |
| A | 80 | 8 | Yes | 6% |
| B | 100 | 10 | No | 12% |
| C | 110 | 11 | No | 7% |
| D | 115 | 9 | No | 8% |

Explain exclusions and the choice. State whether the evidence proves a globally optimal route across the entire landscape. State the outcome if none of the listed routes satisfies all constraints.

## Illustrative candidate responses

**A:** “Choose A: it is cheapest at 80 and shortest at 8 km. Its slope is acceptable. Protected-area crossing is a concern, but a 20-point soft penalty makes its adjusted score 100, still better than C. This is the global best route.”

**B:** “Exclude A because the protected-area rule is mandatory. Exclude B because 12% exceeds 10%. C and D are feasible; choose C at cost 110 rather than D at 115, despite D being shorter. No tie-break is needed. C is best among the supplied feasible alternatives only; the table cannot establish a landscape-wide global optimum. If no listed alternative is feasible, report no feasible candidate and request revised alternatives or an explicitly authorized constraint change.”

## Rubric

| Criterion | 0 points | 1 point | 2 points |
| --- | --- | --- | --- |
| Constraint application | Selects an infeasible route or invents soft penalties | Correctly excludes only one prohibited route | Excludes A for crossing and B for slope |
| Objective and selection | Wrong route or replaces the cost objective | Selects C without comparing feasible costs | Selects C, cost 110 versus D 115; length does not override cost |
| Optimality claim | Claims global optimality without evidence | Does not overclaim but omits scope | Explicitly limits optimality to supplied feasible candidates |
| No-feasible outcome | Silently relaxes constraints or omits an outcome | Reports no feasible route without a next step | Reports infeasibility and requests new alternatives or authorized change |

**Critical gate:** Selecting a route that violates a hard constraint, or silently converting a hard constraint to a penalty, fails the gate.

## Worked scoring and ranking

| Candidate | Constraints | Selection | Optimality | No-feasible outcome | Total | Gate | Verdict |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| A | 0 | 0 | 0 | 0 | 0/8 | Fail | Unacceptable |
| B | 2 | 2 | 2 | 2 | 8/8 | Pass | Acceptable |

**Ranking: B > A.** A's arithmetic for its invented penalty is irrelevant because the prompt does not authorize trading away a hard constraint. B distinguishes feasibility, objective value, and scope of the optimality claim.

## Reference answer and check

The feasible set is **{C, D}** and the selected route is **C**. Its cost is the minimum in that set. Neither the candidate list's completeness nor a global search is provided. An empty feasible set must return no solution under the current specification.

```python
from evaluation.reference import Route, select_feasible_route

routes = [
    Route("A", 80, 8, True, 6),
    Route("B", 100, 10, False, 12),
    Route("C", 110, 11, False, 7),
    Route("D", 115, 9, False, 8),
]
assert select_feasible_route(routes, 10).name == "C"
assert select_feasible_route(routes, 5) is None
```

## Evidence and limits

The coordinates, terrain, cost model, and environmental constraints are not real; only the table is supplied. The helper performs finite candidate selection. It is not a geospatial optimizer, environmental assessment, or engineering approval.
