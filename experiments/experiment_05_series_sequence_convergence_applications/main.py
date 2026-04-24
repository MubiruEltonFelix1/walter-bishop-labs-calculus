"""
Experiment 05: Practical convergence/divergence analysis for sequences and series.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

from calculus import ConvergenceEngine
from visualization import ConvergenceVisualizer
from reporting import ConvergenceReporter
import settings


def setup_output_directories():
    base = Path(__file__).parent / "outputs"
    plots = base / "plots"
    reports = base / "reports"
    plots.mkdir(parents=True, exist_ok=True)
    reports.mkdir(parents=True, exist_ok=True)
    return plots, reports


def print_suggested_experiments():
    print("\n" + "=" * 80)
    print("SUGGESTED PRACTICAL MINI-EXPERIMENTS BEFORE EXECUTION")
    print("=" * 80)
    for item in settings.SUGGESTED_EXPERIMENTS:
        print(f"{item['id']}. {item['title']}")
        print(f"   Question: {item['question']}")


def run_sequence_cases(engine: ConvergenceEngine, visualizer: ConvergenceVisualizer, plots_dir: Path, show_plots: bool):
    print("\n" + "=" * 80)
    print("1) SEQUENCE CASES: CONVERGENCE AND DIVERGENCE")
    print("=" * 80)

    results = []
    sequence_store = {}

    for case in settings.SEQUENCE_CASES:
        print(f"\nAnalyzing: {case['title']}")

        if case["key"] == "temperature_relaxation":
            terms = engine.temperature_relaxation_sequence(
                initial=case["initial"],
                ambient=case["ambient"],
                alpha=case["alpha"],
                steps=case["steps"],
            )
            reference = case["ambient"]
        elif case["key"] == "compound_debt_growth":
            terms = engine.compound_growth_sequence(
                initial=case["initial"],
                growth_factor=case["growth_factor"],
                steps=case["steps"],
            )
            reference = None
        else:
            raise ValueError(f"Unsupported sequence case: {case['key']}")

        detected = engine.classify_sequence(terms)
        print(f"  Expected: {case['expected_behavior']}")
        print(f"  Detected: {detected}")
        print(f"  a_0 = {terms[0]:.4f}, a_{len(terms)-1} = {terms[-1]:.4f}")

        image_path = plots_dir / f"{case['key']}_sequence.png"
        visualizer.plot_sequence_terms(
            terms=terms,
            title=case["title"],
            expected_behavior=case["expected_behavior"],
            filename=str(image_path),
            show=show_plots,
        )

        sequence_store[case["key"]] = terms

        results.append(
            {
                "title": case["title"],
                "application": case["application"],
                "expected_behavior": case["expected_behavior"],
                "detected_behavior": detected,
                "initial": float(terms[0]),
                "final": float(terms[-1]),
                "reference_value": None if reference is None else float(reference),
            }
        )

    visualizer.plot_sequence_comparison(
        convergent_terms=sequence_store["temperature_relaxation"],
        divergent_terms=sequence_store["compound_debt_growth"],
        filename=str(plots_dir / "sequence_comparison.png"),
        show=show_plots,
    )

    visualizer.animate_sequence_progression(
        convergent_terms=sequence_store["temperature_relaxation"],
        divergent_terms=sequence_store["compound_debt_growth"],
        filename=str(plots_dir / "sequence_progression_animation.html"),
        show=show_plots,
    )

    return results, sequence_store


def run_series_cases(engine: ConvergenceEngine, visualizer: ConvergenceVisualizer, plots_dir: Path, show_plots: bool):
    print("\n" + "=" * 80)
    print("2) SERIES CASES: CONVERGENCE AND DIVERGENCE")
    print("=" * 80)

    results = []
    series_store = {}

    for case in settings.SERIES_CASES:
        print(f"\nAnalyzing: {case['title']}")

        if case["key"] == "discounted_cashflow":
            ratio = 1.0 / (1.0 + case["discount_rate"])
            terms = engine.geometric_series_terms(
                payment=case["payment"],
                ratio=ratio,
                terms=case["terms"],
            )
            reference = case["payment"] / (1.0 - ratio)
        elif case["key"] == "maintenance_backlog":
            terms = engine.harmonic_series_terms(
                base_cost=case["base_cost"],
                terms=case["terms"],
            )
            reference = None
        elif case["key"] == "alternating_correction":
            terms = engine.alternating_harmonic_terms(
                scale=case["scale"],
                terms=case["terms"],
            )
            reference = case["scale"] * np.log(2.0)
        else:
            raise ValueError(f"Unsupported series case: {case['key']}")

        partial = engine.partial_sums(terms)
        detected = engine.classify_series(terms, partial)

        print(f"  Expected: {case['expected_behavior']}")
        print(f"  Detected: {detected}")
        print(f"  |term_last| = {abs(terms[-1]):.6f}")
        print(f"  S_N (N={len(terms)}) = {partial[-1]:.6f}")

        image_path = plots_dir / f"{case['key']}_series.png"
        visualizer.plot_series_terms_and_partial(
            series_terms=terms,
            partial_sums=partial,
            title=case["title"],
            filename=str(image_path),
            show=show_plots,
        )

        series_store[case["key"]] = {
            "terms": terms,
            "partial": partial,
        }

        results.append(
            {
                "title": case["title"],
                "application": case["application"],
                "expected_behavior": case["expected_behavior"],
                "detected_behavior": detected,
                "last_term_abs": float(abs(terms[-1])),
                "final_partial_sum": float(partial[-1]),
                "reference_value": None if reference is None else float(reference),
            }
        )

    visualizer.plot_series_comparison(
        geometric_partial=series_store["discounted_cashflow"]["partial"],
        harmonic_partial=series_store["maintenance_backlog"]["partial"],
        alternating_partial=series_store["alternating_correction"]["partial"],
        filename=str(plots_dir / "series_partial_comparison.png"),
        show=show_plots,
    )

    visualizer.animate_series_partial_sums(
        geometric_partial=series_store["discounted_cashflow"]["partial"],
        harmonic_partial=series_store["maintenance_backlog"]["partial"],
        alternating_partial=series_store["alternating_correction"]["partial"],
        filename=str(plots_dir / "series_partial_animation.html"),
        show=show_plots,
    )

    return results, series_store


def run_experiment(show_progress: bool = True, show_plots: bool = False):
    if show_progress:
        print("\n" + "=" * 80)
        print("EXPERIMENT 05: PRACTICAL CONVERGENCE AND DIVERGENCE")
        print("=" * 80)

    print_suggested_experiments()

    plots_dir, reports_dir = setup_output_directories()

    engine = ConvergenceEngine()
    visualizer = ConvergenceVisualizer(
        style=settings.VISUALIZATION["plot_style"],
        dpi=settings.VISUALIZATION["figure_dpi"],
        figsize=settings.VISUALIZATION["figure_size"],
        fps=settings.VISUALIZATION["animation_fps"],
    )
    reporter = ConvergenceReporter()

    sequence_results, sequence_store = run_sequence_cases(
        engine=engine,
        visualizer=visualizer,
        plots_dir=plots_dir,
        show_plots=show_plots,
    )

    series_results, series_store = run_series_cases(
        engine=engine,
        visualizer=visualizer,
        plots_dir=plots_dir,
        show_plots=show_plots,
    )

    summary = reporter.generate_summary(
        suggestions=settings.SUGGESTED_EXPERIMENTS,
        sequence_results=sequence_results,
        series_results=series_results,
    )
    report_path = reports_dir / settings.REPORTING["summary_filename"]
    report_path.write_text(summary, encoding="utf-8")

    if show_progress:
        print("\nOutputs generated:")
        print(f"  Plots and animations: {plots_dir}")
        print(f"  Report:               {report_path}")

    return {
        "plots_dir": str(plots_dir),
        "report_path": str(report_path),
        "sequence_results": sequence_results,
        "series_results": series_results,
        "sequence_store": sequence_store,
        "series_store": series_store,
    }


def main():
    run_experiment(show_progress=True, show_plots=False)


if __name__ == "__main__":
    main()
