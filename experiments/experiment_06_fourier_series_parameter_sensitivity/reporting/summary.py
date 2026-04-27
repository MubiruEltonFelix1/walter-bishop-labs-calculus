"""Summary reporting for Experiment 06."""

from __future__ import annotations

from datetime import datetime


class FourierSensitivityReporter:
    """Generate a concise textual report for the Fourier sensitivity study."""

    def __init__(self):
        self.timestamp = datetime.now()

    def generate_summary(self, results_by_function: dict, amplitude_levels) -> str:
        lines = []
        lines.append("=" * 80)
        lines.append("EXPERIMENT 06: FOURIER SERIES PARAMETER SENSITIVITY - SUMMARY REPORT")
        lines.append("=" * 80)
        lines.append(f"Generated: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("\nCore idea:")
        lines.append("Fourier coefficients scale linearly with amplitude, while the reconstruction error scales with amplitude squared when the harmonic count stays fixed.")

        for function_name, function_result in results_by_function.items():
            lines.append("\n" + "=" * 80)
            lines.append(f"Function: {function_name}")
            lines.append("=" * 80)

            lines.append("Amplitude sweep summary:")
            for amplitude in amplitude_levels:
                amplitude_result = function_result["amplitude_results"][amplitude]
                coeff = amplitude_result["coefficients"]
                first_magnitude = amplitude_result["magnitudes"][0]
                best_metrics = min(amplitude_result["metrics"], key=lambda item: item["mse"])
                lines.append(
                    f"  A={amplitude:.2f} | a0={coeff['a0']:.6f} | first harmonic={first_magnitude:.6f} | best N={best_metrics['n_terms']} | MSE={best_metrics['mse']:.8f}"
                )

            reference = function_result["reference_coefficients"]
            lines.append("\nReference coefficients (A = 1.00):")
            lines.append(f"  a0: {reference['a0']:.6f}")
            lines.append("  First 10 harmonic magnitudes:")
            for idx, mag in enumerate(reference["magnitudes"][:10], start=1):
                lines.append(f"    n={idx:2d}: {mag:.6f}")

            lines.append("\nHarmonic-count sweep at A = 1.00:")
            for entry in function_result["reference_metrics"]:
                lines.append(
                    f"  N={entry['n_terms']:2d} | MSE={entry['mse']:.8f} | MaxError={entry['max_error']:.8f}"
                )

        lines.append("\n" + "=" * 80)
        lines.append("END OF REPORT")
        lines.append("=" * 80)
        return "\n".join(lines)
