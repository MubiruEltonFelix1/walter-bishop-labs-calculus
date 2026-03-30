"""
Experiment 04 main script: Fourier series reconstruction of periodic functions.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

from calculus import FourierSeriesEngine
from visualization import FourierVisualizer
from reporting import FourierReporter
import settings


def setup_output_directories():
    base = Path(__file__).parent / "outputs"
    plots = base / "plots"
    reports = base / "reports"
    plots.mkdir(parents=True, exist_ok=True)
    reports.mkdir(parents=True, exist_ok=True)
    return plots, reports


def run_experiment(show_progress: bool = True):
    if show_progress:
        print("\n" + "=" * 80)
        print("EXPERIMENT 04: FOURIER SERIES RECONSTRUCTION")
        print("=" * 80)

    plots_dir, reports_dir = setup_output_directories()

    engine = FourierSeriesEngine()
    visualizer = FourierVisualizer(
        style=settings.VISUALIZATION["plot_style"],
        dpi=settings.VISUALIZATION["figure_dpi"],
        figsize=settings.VISUALIZATION["figure_size"],
    )
    reporter = FourierReporter()

    x = np.linspace(
        settings.SAMPLING["domain_min"],
        settings.SAMPLING["domain_max"],
        settings.SAMPLING["plot_points"],
        endpoint=False,
    )

    results_by_function = {}

    for function_name in settings.FUNCTIONS:
        if show_progress:
            print(f"\nAnalyzing function: {function_name}")

        f = engine.get_function(function_name)
        y_true = f(x)

        reconstructions = {}
        metrics = []

        max_n = max(settings.HARMONIC_COUNTS)
        coeff_max = engine.compute_coefficients(
            function_name=function_name,
            n_terms=max_n,
            n_samples=settings.SAMPLING["coefficient_samples"],
        )

        for n_terms in settings.HARMONIC_COUNTS:
            y_hat = engine.reconstruct(
                x=x,
                a0=coeff_max["a0"],
                an=coeff_max["an"][:n_terms],
                bn=coeff_max["bn"][:n_terms],
            )
            reconstructions[n_terms] = y_hat
            metric = engine.reconstruction_metrics(y_true, y_hat)
            metric["n_terms"] = n_terms
            metrics.append(metric)

        magnitudes = engine.harmonic_magnitudes(coeff_max["an"], coeff_max["bn"])

        visualizer.plot_reconstructions(
            x=x,
            y_true=y_true,
            reconstructions=reconstructions,
            title=f"{function_name.capitalize()} wave: true signal vs partial sums",
            filename=str(plots_dir / f"{function_name}_reconstruction.png"),
            show=show_progress,
        )
        if show_progress:
            print("  Closed reconstruction plot, continuing...")

        visualizer.plot_spectrum(
            magnitudes=magnitudes,
            title=f"{function_name.capitalize()} wave harmonic spectrum",
            filename=str(plots_dir / f"{function_name}_spectrum.png"),
            show=show_progress,
        )
        if show_progress:
            print("  Closed spectrum plot, continuing...")

        visualizer.plot_error_decay(
            harmonic_counts=settings.HARMONIC_COUNTS,
            mse_values=[m["mse"] for m in metrics],
            max_error_values=[m["max_error"] for m in metrics],
            title=f"{function_name.capitalize()} reconstruction error decay",
            filename=str(plots_dir / f"{function_name}_error_decay.png"),
            show=show_progress,
        )
        if show_progress:
            print("  Closed error-decay plot, continuing...")

        results_by_function[function_name] = {
            "max_coefficients": coeff_max,
            "metrics": metrics,
            "magnitudes": magnitudes,
        }

        if show_progress:
            best = min(metrics, key=lambda m: m["mse"])
            print(
                f"  Best MSE at N={best['n_terms']}: {best['mse']:.6f}, max error={best['max_error']:.6f}"
            )

    summary_text = reporter.generate_summary(results_by_function)
    report_path = reports_dir / settings.REPORTING["summary_filename"]
    with open(report_path, "w", encoding="utf-8") as handle:
        handle.write(summary_text)

    if show_progress:
        print("\nOutputs generated:")
        print(f"  Plots:   {plots_dir}")
        print(f"  Report:  {report_path}")

    return {
        "plots_dir": str(plots_dir),
        "report_path": str(report_path),
        "results": results_by_function,
    }


def main():
    run_experiment(show_progress=True)


if __name__ == "__main__":
    main()
