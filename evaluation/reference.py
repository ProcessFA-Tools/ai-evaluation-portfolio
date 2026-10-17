"""Small reference checks for synthetic portfolio exercises, not engine models."""

from dataclasses import dataclass
import math
from typing import Mapping, Optional, Sequence, Tuple


def _finite(value: float, name: str) -> float:
    if isinstance(value, bool):
        raise ValueError(f"{name} must be a finite number, not a boolean")
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name} must be a finite number") from exc
    if not math.isfinite(number):
        raise ValueError(f"{name} must be finite")
    return number


def pressure_to_absolute_pa(
    pressure: float, unit: str, basis: str, atmospheric_pa: float
) -> float:
    """Convert Pa/kPa/bar to Pa absolute using explicitly supplied atmosphere.

    `basis` must be "gauge" or "absolute". The supplied atmosphere must be
    positive; it is added only for gauge values. This is a unit conversion,
    not a claim about the accuracy of any source measurement.
    """
    factors = {"Pa": 1.0, "kPa": 1_000.0, "bar": 100_000.0}
    if unit not in factors:
        raise ValueError("unit must be Pa, kPa, or bar")
    if basis not in {"gauge", "absolute"}:
        raise ValueError("basis must be gauge or absolute")
    value = _finite(pressure, "pressure")
    atmosphere = _finite(atmospheric_pa, "atmospheric_pa")
    if atmosphere <= 0:
        raise ValueError("atmospheric_pa must be positive")
    result = value * factors[unit]
    if basis == "gauge":
        result += atmosphere
    if not math.isfinite(result) or result < 0:
        raise ValueError("absolute pressure must be finite and nonnegative")
    return result


@dataclass(frozen=True)
class BalanceResult:
    status: str
    known_outflow: float
    missing_phases: Tuple[str, ...]
    imbalance: Optional[float]
    within_tolerance: Optional[bool]


def phase_mass_balance(
    feed: float,
    phase_flows: Mapping[str, Optional[float]],
    expected_phases: Sequence[str],
    tolerance: float = 0.01,
) -> BalanceResult:
    """Check steady-state mass balance in one shared unit (e.g. kg/s).

    Assumes no accumulation and no unlisted inlet/outlet streams. A missing
    key or None is unknown; a measured 0.0 is valid. Unknowns prevent a final
    balance verdict even if the known subtotal equals the feed.
    """
    inlet = _finite(feed, "feed")
    tol = _finite(tolerance, "tolerance")
    if inlet < 0 or tol < 0:
        raise ValueError("feed and tolerance must be nonnegative")
    names = tuple(expected_phases)
    if not names or len(names) != len(set(names)):
        raise ValueError("expected_phases must be nonempty and unique")
    if any(not isinstance(name, str) or not name for name in names):
        raise ValueError("phase names must be nonempty strings")
    if set(phase_flows) - set(names):
        raise ValueError("unlisted phase supplied; expand expected_phases explicitly")
    missing = []
    known = []
    for name in names:
        raw = phase_flows.get(name)
        if raw is None:
            missing.append(name)
            continue
        value = _finite(raw, f"flow for {name}")
        if value < 0:
            raise ValueError("phase flows must be nonnegative")
        known.append(value)
    try:
        subtotal = math.fsum(known)
    except OverflowError as exc:
        raise ValueError("known outflow must be finite") from exc
    if not math.isfinite(subtotal):
        raise ValueError("known outflow must be finite")
    if missing:
        return BalanceResult("incomplete", subtotal, tuple(missing), None, None)
    imbalance = subtotal - inlet
    # Avoid rejecting a boundary solely because of binary floating point noise.
    passes = abs(imbalance) <= tol or math.isclose(
        abs(imbalance), tol, rel_tol=1e-12, abs_tol=0.0
    )
    return BalanceResult("complete", subtotal, (), imbalance, passes)


def extraction_review_reasons(
    confidence: float,
    source_location_present: bool,
    unit_recognized: bool,
    conflicting_evidence: bool,
    threshold: float = 0.95,
) -> Tuple[str, ...]:
    """Apply this exercise's explicit review policy, not a universal threshold.

    A confidence score is not a calibrated probability of correctness. Empty
    reasons mean policy-eligible for automatic acceptance, not proven correct.
    """
    score = _finite(confidence, "confidence")
    cutoff = _finite(threshold, "threshold")
    if not 0 <= score <= 1 or not 0 <= cutoff <= 1:
        raise ValueError("confidence and threshold must lie in [0, 1]")
    flags = (source_location_present, unit_recognized, conflicting_evidence)
    if any(not isinstance(flag, bool) for flag in flags):
        raise ValueError("evidence flags must be booleans")
    reasons = []
    if score < cutoff:
        reasons.append("low_confidence")
    if not source_location_present:
        reasons.append("missing_source_location")
    if not unit_recognized:
        reasons.append("unrecognized_unit")
    if conflicting_evidence:
        reasons.append("conflicting_evidence")
    return tuple(reasons)


@dataclass(frozen=True)
class Route:
    name: str
    cost: float
    length_km: float
    crosses_protected_area: bool
    max_slope_percent: float


def select_feasible_route(
    routes: Sequence[Route], max_allowed_slope_percent: float
) -> Optional[Route]:
    """Minimize stated cost among supplied feasible alternatives only.

    Hard constraints: no protected-area crossing; maximum slope at most the
    supplied limit. Tie-break by length, then name. This does not search the
    landscape or establish that the candidate set contains a global optimum.
    """
    slope_limit = _finite(max_allowed_slope_percent, "slope limit")
    if slope_limit < 0:
        raise ValueError("slope limit must be nonnegative")
    names = set()
    feasible = []
    for route in routes:
        if not isinstance(route.name, str) or not route.name or route.name in names:
            raise ValueError("route names must be nonempty and unique")
        names.add(route.name)
        cost = _finite(route.cost, "cost")
        length = _finite(route.length_km, "length_km")
        slope = _finite(route.max_slope_percent, "max_slope_percent")
        if min(cost, length, slope) < 0:
            raise ValueError("cost, length, and slope must be nonnegative")
        if not isinstance(route.crosses_protected_area, bool):
            raise ValueError("crosses_protected_area must be boolean")
        if not route.crosses_protected_area and slope <= slope_limit:
            feasible.append((cost, length, route.name, route))
    return min(feasible, key=lambda item: item[:3])[3] if feasible else None


def relative_change_percent(reference: float, observed: float) -> Optional[float]:
    """Return signed percent change; None means a zero reference is undefined.

    This quantifies a discrepancy only. It supplies no causal diagnosis or
    authority to correct a simulator output.
    """
    baseline = _finite(reference, "reference")
    value = _finite(observed, "observed")
    if baseline == 0:
        return None
    change = (value - baseline) / abs(baseline) * 100.0
    if not math.isfinite(change):
        raise ValueError("relative change must be finite")
    return change
