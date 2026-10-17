# 04 — Apply hard constraints before minimizing cost

**Provenance:** This is AI-assisted synthetic portfolio practice. The portfolio author wrote both candidate answers as illustrations. They are not real model outputs. Candidate A intentionally chooses a route that violates a mandatory constraint.

The [glossary](../../docs/glossary.md) defines the technical terms used in this task.

## Prompt

Select one of four synthetic route alternatives. Minimize the supplied total cost score. Two constraints are mandatory:

- **No protected-area crossing**.
- **Maximum slope <= 10%**.

Cost scores already include expense related to length. Do not replace the stated cost objective with shortest length. If feasible routes have equal costs, prefer the shorter route. If their lengths are also equal, select by alphabetical name.

| Route | Total cost score | Length (km) | Crosses protected area? | Maximum slope |
| --- | ---: | ---: | --- | ---: |
| A | 80 | 8 | Yes | 6% |
| B | 100 | 10 | No | 12% |
| C | 110 | 11 | No | 7% |
| D | 115 | 9 | No | 8% |

Explain the route exclusions. Explain the selected route. State whether the evidence proves a globally optimal route across the entire landscape. State the outcome if none of the listed routes satisfies all constraints.

## Illustrative candidate answers

**A:** “Choose A. It is cheapest at 80 and shortest at 8 km. Its slope is acceptable. Protected-area crossing is a concern, but a 20-point soft penalty makes its adjusted score 100, still better than C. This is the global best route.”

**B:** “Exclude A because the protected-area rule is mandatory. Exclude B because 12% exceeds 10%. C and D are feasible. Choose C at cost 110 rather than D at 115, despite D being shorter. The costs differ, so the rules for equal costs do not apply.

C is best among the supplied feasible alternatives only. The table cannot establish a global optimum across the entire landscape. If no listed alternative is feasible, report no feasible candidate. In that case, request revised alternatives or an explicitly authorized constraint change.”

## Rubric

| Criterion | 0 points | 1 point | 2 points |
| --- | --- | --- | --- |
| Constraint application | Selects an infeasible route or invents soft penalties | Correctly excludes only one prohibited route | Excludes A for crossing and B for slope |
| Objective and selection | Wrong route or replaces the cost objective | Selects C without comparing feasible costs | Selects C, cost 110 versus D 115; length does not override cost |
| Optimality claim | Claims global optimality without evidence | Does not overclaim but omits scope | Explicitly limits optimality to supplied feasible candidates |
| No-feasible outcome | Silently relaxes constraints or omits an outcome | Reports no feasible route without a next step | Reports infeasibility and requests new alternatives or authorized change |

**Critical gate:** A response fails the gate if it selects a route that violates a mandatory constraint. It also fails if it silently changes a mandatory constraint into a penalty.

## Worked scoring and ranking

| Candidate | Constraints | Selection | Optimality | No-feasible outcome | Total | Gate | Verdict |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| A | 0 | 0 | 0 | 0 | 0/8 | Fail | Unacceptable |
| B | 2 | 2 | 2 | 2 | 8/8 | Pass | Acceptable |

**Ranking: B > A.** A calculates its invented penalty correctly. However, the prompt does not authorize replacing a mandatory constraint with a penalty. That calculation does not support the route selection. B separately considers constraint compliance, cost, and the limits of the optimality claim.

## Reference answer and check

The feasible set is **{C, D}** and the selected route is **C**. Its cost is the minimum in that set. The exercise does not establish that the candidate list is complete. It also provides no global search. An empty feasible set must return no solution under the current specification.

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

Only the table is supplied. The coordinates, terrain, cost model, and environmental constraints are not real. The helper selects from a fixed list of candidates. It does not optimize routes across a map, assess environmental effects, or approve an engineering design.
