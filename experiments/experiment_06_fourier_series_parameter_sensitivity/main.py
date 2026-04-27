"""Experiment 06: Fourier series parameter sensitivity and amplitude scaling."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

from calculus import FourierSensitivityEngine
from visualization import FourierSensitivityVisualizer
from reporting import FourierSensitivityReporter
import settings


def setup_output_directories():
    base = Path(__file__).parent / "outputs"
    plots = base / "plots"
    reports = base / "reports"
    plots.mkdir(parents=True, exist_ok=True)
    reports.mkdir(parents=True, exist_ok=True)
    return plots, reports


def run_experiment(show_progress: bool = True, show_plots: bool = False):
    if show_progress:
        print("\n" + "=" * 80)
        print("EXPERIMENT 06: FOURIER SERIES PARAMETER SENSITIVITY")
        print("=" * 80)

    plots_dir, reports_dir = setup_output_directories()

    engine = FourierSensitivityEngine()
    visualizer = FourierSensitivityVisualizer(
        style=settings.VISUALIZATION["plot_style"],
        dpi=settings.VISUALIZATION["figure_dpi"],
        figsize=settings.VISUALIZATION["figure_size"],
        fps=settings.VISUALIZATION["animation_fps"],
    )
    reporter = FourierSensitivityReporter()

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

        base_coefficients = engine.compute_coefficients(
            function_name=function_name,
            n_terms=max(settings.HARMONIC_COUNTS),
            n_samples=settings.SAMPLING["coefficient_samples"],
            amplitude=1.0,
        )

        base_wave = engine.evaluate(x, function_name=function_name, amplitude=1.0)
        reconstructions_by_terms = {}
        reference_metrics = []

        for n_terms in settings.HARMONIC_COUNTS:
            y_hat = engine.reconstruct(
                x=x,
                a0=base_coefficients["a0"],
                an=base_coefficients["an"][:n_terms],
                bn=base_coefficients["bn"][:n_terms],
            )
            reconstructions_by_terms[n_terms] = y_hat
            metric = engine.reconstruction_metrics(base_wave, y_hat)
            metric["n_terms"] = n_terms
            reference_metrics.append(metric)

        magnitudes = engine.harmonic_magnitudes(base_coefficients["an"], base_coefficients["bn"])

        visualizer.plot_reconstruction_comparison(
            x=x,
            y_true=base_wave,
            reconstructions=reconstructions_by_terms,
            title=f"{function_name.capitalize()} wave: true signal vs partial sums",
            filename=str(plots_dir / f"{function_name}_reconstruction.png"),
            show=show_plots,
        )
        if show_progress:
            print("  Closed reconstruction plot, continuing...")

        visualizer.plot_spectrum(
            magnitudes=magnitudes,
            title=f"{function_name.capitalize()} wave harmonic spectrum",
            filename=str(plots_dir / f"{function_name}_spectrum.png"),
            show=show_plots,
        )
        if show_progress:
            print("  Closed spectrum plot, continuing...")

        visualizer.plot_error_decay(
            harmonic_counts=settings.HARMONIC_COUNTS,
            metrics_by_amplitude={1.0: reference_metrics},
            title=f"{function_name.capitalize()} reconstruction error decay",
            filename=str(plots_dir / f"{function_name}_error_decay.png"),
            show=show_plots,
        )
        if show_progress:
            print("  Closed error-decay plot, continuing...")

        amplitude_results = {}
        amplitude_waveforms = {}
        amplitude_reconstructions = {}
        amplitude_coefficient_sets = {}
        max_terms = max(settings.HARMONIC_COUNTS)

        for amplitude in settings.AMPLITUDE_LEVELS:
            coefficients = engine.compute_coefficients(
                function_name=function_name,
                n_terms=max_terms,
                n_samples=settings.SAMPLING["coefficient_samples"],
                amplitude=amplitude,
            )
            y_true = engine.evaluate(x, function_name=function_name, amplitude=amplitude)
            amplitude_waveforms[amplitude] = y_true

            amplitude_metrics = []
            amplitude_reconstruction_series = {}
            for n_terms in settings.HARMONIC_COUNTS:
                y_hat = engine.reconstruct(
                    x=x,
                    a0=coefficients["a0"],
                    an=coefficients["an"][:n_terms],
                    bn=coefficients["bn"][:n_terms],
                )
                amplitude_reconstruction_series[n_terms] = y_hat
                metric = engine.reconstruction_metrics(y_true, y_hat)
                metric["n_terms"] = n_terms
                amplitude_metrics.append(metric)

            amplitude_reconstructions[amplitude] = amplitude_reconstruction_series[max_terms]
            amplitude_coefficient_sets[amplitude] = {
                **coefficients,
                "magnitudes": engine.harmonic_magnitudes(coefficients["an"], coefficients["bn"]),
            }
            amplitude_results[amplitude] = {
                "coefficients": coefficients,
                "magnitudes": amplitude_coefficient_sets[amplitude]["magnitudes"],
                "metrics": amplitude_metrics,
                "reconstructions": amplitude_reconstruction_series,
            }

        visualizer.plot_waveform_family(
            x=x,
            waveforms_by_label={f"A = {amplitude:.2f}": waveform for amplitude, waveform in amplitude_waveforms.items()},
            title=f"{function_name.capitalize()} wave under amplitude scaling",
            filename=str(plots_dir / f"{function_name}_amplitude_family.png"),
            show=show_plots,
        )
        if show_progress:
            print("  Closed amplitude-family plot, continuing...")

        visualizer.plot_coefficient_scaling(
            amplitudes=settings.AMPLITUDE_LEVELS,
            coefficient_sets=amplitude_coefficient_sets,
            title=f"{function_name.capitalize()} coefficients scale with amplitude",
            filename=str(plots_dir / f"{function_name}_amplitude_scaling.png"),
            show=show_plots,
        )
        if show_progress:
            print("  Closed amplitude-scaling plot, continuing...")

        visualizer.plot_error_decay(
            harmonic_counts=settings.HARMONIC_COUNTS,
            metrics_by_amplitude={amp: amplitude_results[amp]["metrics"] for amp in settings.AMPLITUDE_LEVELS},
            title=f"{function_name.capitalize()} error decay across amplitude levels",
            filename=str(plots_dir / f"{function_name}_amplitude_error_decay.png"),
            show=show_plots,
        )
        if show_progress:
            print("  Closed amplitude-error plot, continuing...")

        visualizer.animate_amplitude_sweep(
            x=x,
            amplitude_levels=settings.AMPLITUDE_LEVELS,
            true_signal_by_amplitude=amplitude_waveforms,
            reconstructions_by_amplitude=amplitude_reconstructions,
            filename=str(plots_dir / f"{function_name}_amplitude_sweep_animation.html"),
            show=show_plots,
        )
        if show_progress:
            print("  Saved amplitude sweep animation.")

        visualizer.animate_harmonic_build_up(
            x=x,
            y_true=base_wave,
            reconstructions_by_terms=reconstructions_by_terms,
            filename=str(plots_dir / f"{function_name}_harmonic_build_animation.html"),
            show=show_plots,
        )
        if show_progress:
            print("  Saved harmonic build animation.")

        results_by_function[function_name] = {
            "reference_coefficients": {
                **base_coefficients,
                "magnitudes": magnitudes,
            },
            "reference_metrics": reference_metrics,
            "amplitude_results": amplitude_results,
        }

        if show_progress:
            best = min(reference_metrics, key=lambda metric: metric["mse"])
            print(f"  Best reference MSE at N={best['n_terms']}: {best['mse']:.6f}")

    summary_text = reporter.generate_summary(results_by_function, settings.AMPLITUDE_LEVELS)
    report_path = reports_dir / settings.REPORTING["summary_filename"]
    report_path.write_text(summary_text, encoding="utf-8")

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
    run_experiment(show_progress=True, show_plots=False)


if __name__ == "__main__":
    main()
