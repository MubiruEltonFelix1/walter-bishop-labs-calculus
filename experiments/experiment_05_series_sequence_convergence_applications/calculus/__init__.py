"""
Core numerical engine for convergence and divergence analysis.
"""

from __future__ import annotations

import numpy as np


class ConvergenceEngine:
    """Generate sequence and series data plus practical diagnostics."""

    def temperature_relaxation_sequence(
        self,
        initial: float,
        ambient: float,
        alpha: float,
        steps: int,
    ) -> np.ndarray:
        terms = np.zeros(steps + 1, dtype=float)
        terms[0] = initial
        for n in range(steps):
            terms[n + 1] = alpha * terms[n] + (1.0 - alpha) * ambient
        return terms

    def compound_growth_sequence(
        self,
        initial: float,
        growth_factor: float,
        steps: int,
    ) -> np.ndarray:
        indices = np.arange(steps + 1, dtype=float)
        return initial * (growth_factor ** indices)

    def geometric_series_terms(
        self,
        payment: float,
        ratio: float,
        terms: int,
    ) -> np.ndarray:
        n = np.arange(terms, dtype=float)
        return payment * (ratio ** n)

    def harmonic_series_terms(self, base_cost: float, terms: int) -> np.ndarray:
        n = np.arange(1, terms + 1, dtype=float)
        return base_cost / n

    def alternating_harmonic_terms(self, scale: float, terms: int) -> np.ndarray:
        n = np.arange(1, terms + 1, dtype=float)
        signs = np.where((n % 2) == 1, 1.0, -1.0)
        return scale * signs / n

    def partial_sums(self, series_terms: np.ndarray) -> np.ndarray:
        return np.cumsum(series_terms)

    def classify_sequence(self, sequence_terms: np.ndarray, tolerance: float = 5e-2, window: int = 6) -> str:
        if len(sequence_terms) <= window + 1:
            return "inconclusive"

        deltas = np.diff(sequence_terms)
        tail_deltas = np.abs(deltas[-window:])
        if np.max(tail_deltas) < tolerance:
            return "convergent"

        tail_abs = np.abs(sequence_terms[-window:])
        if np.all(np.diff(tail_abs) > 0) and tail_abs[-1] > 1.5 * max(1.0, np.abs(sequence_terms[0])):
            return "divergent"

        return "likely divergent"

    def classify_series(self, series_terms: np.ndarray, partial_sums: np.ndarray, window: int = 8) -> str:
        if len(series_terms) <= window + 1 or len(partial_sums) <= window + 1:
            return "inconclusive"

        tail_terms = series_terms[-window:]
        head_terms = series_terms[:window]

        # Alternating and shrinking terms strongly indicate conditional convergence.
        signs = np.sign(tail_terms)
        alternating = np.all(signs[:-1] * signs[1:] < 0)
        if alternating and np.mean(np.abs(tail_terms)) < 0.05 * np.mean(np.abs(head_terms)):
            return "convergent"

        # For non-negative terms, compare n*a_n behavior: harmonic-like tails stay large.
        if np.all(series_terms >= 0):
            n = np.arange(1, len(series_terms) + 1, dtype=float)
            scaled = n * series_terms
            head_scaled = np.mean(scaled[:window])
            tail_scaled = np.mean(scaled[-window:])
            if tail_scaled / max(1e-12, head_scaled) > 0.6:
                return "divergent"
            return "convergent"

        return "likely divergent"
