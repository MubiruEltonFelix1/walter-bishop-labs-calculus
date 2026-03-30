"""
Reporting module for Experiment 04.
"""

from __future__ import annotations

from datetime import datetime


class FourierReporter:
    """Generate textual summary reports for reconstruction quality."""

    def __init__(self):
        self.timestamp = datetime.now()

    def generate_summary(self, results_by_function: dict) -> str:
        lines = []
        lines.append("=" * 80)
        lines.append("EXPERIMENT 04: FOURIER SERIES RECONSTRUCTION - SUMMARY REPORT")
        lines.append("=" * 80)
        lines.append(f"Generated: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")

        for function_name, function_result in results_by_function.items():
            lines.append("\n" + "=" * 80)
            lines.append(f"Function: {function_name}")
            lines.append("=" * 80)

            coeff = function_result["max_coefficients"]
            lines.append(f"a0: {coeff['a0']:.6f}")
            lines.append("First 10 harmonic magnitudes:")
            for idx, mag in enumerate(function_result["magnitudes"][:10], start=1):
                lines.append(f"  n={idx:2d}: {mag:.6f}")

            lines.append("\nReconstruction quality by harmonic count:")
            for entry in function_result["metrics"]:
                lines.append(
                    f"  N={entry['n_terms']:2d} | MSE={entry['mse']:.8f} | MaxError={entry['max_error']:.8f}"
                )

        lines.append("\n" + "=" * 80)
        lines.append("END OF REPORT")
        lines.append("=" * 80)
        return "\n".join(lines)
