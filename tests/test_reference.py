"""Tests for the published synthetic reference checks."""

import math
import unittest

from evaluation.reference import (
    Route,
    extraction_review_reasons,
    phase_mass_balance,
    pressure_to_absolute_pa,
    relative_change_percent,
    select_feasible_route,
)


class PressureTests(unittest.TestCase):
    def test_task_gauge_example(self):
        self.assertAlmostEqual(
            pressure_to_absolute_pa(5.0, "bar", "gauge", 101325), 601325
        )

    def test_absolute_is_not_shifted(self):
        self.assertEqual(pressure_to_absolute_pa(5.0, "bar", "absolute", 101325), 500000)

    def test_equivalent_units(self):
        values = [pressure_to_absolute_pa(v, u, "gauge", 100000)
                  for v, u in [(2, "bar"), (200, "kPa"), (200000, "Pa")]]
        self.assertEqual(values, [300000] * 3)

    def test_nonstandard_atmosphere_is_used(self):
        self.assertEqual(pressure_to_absolute_pa(0, "Pa", "gauge", 90000), 90000)

    def test_vacuum_boundary_and_below(self):
        self.assertEqual(pressure_to_absolute_pa(-100000, "Pa", "gauge", 100000), 0)
        with self.assertRaises(ValueError):
            pressure_to_absolute_pa(-100001, "Pa", "gauge", 100000)

    def test_invalid_pressure_inputs(self):
        for args in [(1, "psi", "gauge", 101325), (1, "bar", "unknown", 101325),
                     (math.nan, "Pa", "absolute", 101325), (1, "Pa", "gauge", 0),
                     (True, "Pa", "gauge", 101325), (1e308, "bar", "absolute", 101325)]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                pressure_to_absolute_pa(*args)


class MassBalanceTests(unittest.TestCase):
    phases = ("GAS", "LIQUID1", "WATER", "WAX")

    def test_unknown_wax_is_not_a_zero(self):
        result = phase_mass_balance(10, {"GAS": 2, "LIQUID1": 8, "WATER": 0, "WAX": None}, self.phases)
        self.assertEqual(result.known_outflow, 10)
        self.assertEqual(result.status, "incomplete")
        self.assertEqual(result.missing_phases, ("WAX",))
        self.assertIsNone(result.imbalance)
        self.assertIsNone(result.within_tolerance)

    def test_missing_key_is_unknown(self):
        result = phase_mass_balance(10, {"GAS": 2, "LIQUID1": 8, "WATER": 0}, self.phases)
        self.assertEqual(result.missing_phases, ("WAX",))

    def test_confirmed_zero_completes_balance(self):
        result = phase_mass_balance(10, {"GAS": 2, "LIQUID1": 8, "WATER": 0, "WAX": 0}, self.phases)
        self.assertEqual(result.status, "complete")
        self.assertEqual(result.imbalance, 0)
        self.assertTrue(result.within_tolerance)

    def test_complete_but_unbalanced(self):
        result = phase_mass_balance(10, {"GAS": 2, "LIQUID1": 8.1, "WATER": 0, "WAX": 0}, self.phases)
        self.assertAlmostEqual(result.imbalance, .1)
        self.assertFalse(result.within_tolerance)

    def test_tolerance_boundary(self):
        self.assertTrue(phase_mass_balance(1, {"GAS": 1.01}, ["GAS"], .01).within_tolerance)
        self.assertFalse(phase_mass_balance(1, {"GAS": 1.011}, ["GAS"], .01).within_tolerance)

    def test_invalid_flows_or_schema(self):
        for feed, flows, names, tolerance in [
            (10, {"GAS": -1}, ["GAS"], .01), (10, {"GAS": math.nan}, ["GAS"], .01),
            (10, {"GAS": 1, "EXTRA": 2}, ["GAS"], .01), (10, {}, [], .01),
            (10, {}, ["GAS", "GAS"], .01), (-1, {}, ["GAS"], .01),
            (10, {}, ["GAS"], -1), (1, {"A": 1e308, "B": 1e308}, ["A", "B"], .01),
        ]:
            with self.subTest(flows=flows, names=names), self.assertRaises(ValueError):
                phase_mass_balance(feed, flows, names, tolerance)


class ExtractionTests(unittest.TestCase):
    def test_conflict_overrides_high_confidence(self):
        self.assertEqual(extraction_review_reasons(.99, True, True, True), ("conflicting_evidence",))

    def test_low_confidence_requires_review(self):
        self.assertEqual(extraction_review_reasons(.72, True, True, False), ("low_confidence",))

    def test_exact_threshold_is_eligible(self):
        self.assertEqual(extraction_review_reasons(.95, True, True, False), ())

    def test_all_reasons_retained(self):
        self.assertEqual(extraction_review_reasons(.7, False, False, True),
                         ("low_confidence", "missing_source_location", "unrecognized_unit", "conflicting_evidence"))

    def test_invalid_confidence_and_flags(self):
        for args in [(-.1, True, True, False), (1.1, True, True, False),
                     (math.nan, True, True, False), (.9, "yes", True, False),
                     (.9, True, True, False, 1.1)]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                extraction_review_reasons(*args)


class RoutingTests(unittest.TestCase):
    def setUp(self):
        self.routes = [Route("A", 80, 8, True, 6), Route("B", 100, 10, False, 12),
                       Route("C", 110, 11, False, 7), Route("D", 115, 9, False, 8)]

    def test_task_constraints_before_cost(self):
        self.assertEqual(select_feasible_route(self.routes, 10).name, "C")

    def test_equality_at_slope_limit_is_feasible(self):
        self.assertEqual(select_feasible_route(self.routes, 12).name, "B")

    def test_no_feasible_candidate(self):
        self.assertIsNone(select_feasible_route(self.routes, 5))
        self.assertIsNone(select_feasible_route([], 10))

    def test_ties_resolve_by_length_then_name(self):
        routes = [Route("Z", 100, 10, False, 5), Route("B", 100, 9, False, 5), Route("A", 100, 9, False, 5)]
        self.assertEqual(select_feasible_route(routes, 10).name, "A")

    def test_invalid_candidate_is_not_silently_discarded(self):
        for route in [Route("A", -1, 1, False, 1), Route("A", math.inf, 1, False, 1),
                      Route("A", 1, 1, "no", 1), Route("", 1, 1, False, 1)]:
            with self.subTest(route=route), self.assertRaises(ValueError):
                select_feasible_route([route], 10)
        with self.assertRaises(ValueError):
            select_feasible_route([self.routes[0], self.routes[0]], 10)
        with self.assertRaises(ValueError):
            select_feasible_route(self.routes, -1)


class DiscrepancyTests(unittest.TestCase):
    def test_task_discrepancies(self):
        self.assertAlmostEqual(relative_change_percent(100, 120), 20)
        self.assertAlmostEqual(relative_change_percent(40, 60), 50)
        self.assertAlmostEqual(relative_change_percent(25, 30), 20)

    def test_negative_change_is_preserved(self):
        self.assertAlmostEqual(relative_change_percent(120, 100), -100 / 6)

    def test_zero_reference_is_undefined(self):
        self.assertIsNone(relative_change_percent(0, 0))
        self.assertIsNone(relative_change_percent(0, 5))

    def test_invalid_number_rejected(self):
        for args in [(math.nan, 1), (1, math.inf), (False, 1)]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                relative_change_percent(*args)


if __name__ == "__main__":
    unittest.main()
