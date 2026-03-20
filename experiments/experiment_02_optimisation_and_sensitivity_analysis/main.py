import sys
import os
import numpy as np

# Ensure all packages (calculus, optimization, analysis, visualization, reporting)
# resolve correctly when this file is run directly from this directory.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from calculus.derivatives import get_symbolic_derivatives
from calculus.classification import classify_critical_points
from optimization.symbolic_optimizer import find_symbolic_candidates
from optimization.numerical_optimizer import gradient_descent, newtons_method
from optimization.constrained_optimizer import constrained_optimize
from analysis.sensitivity import sensitivity_analysis
from analysis.robustness import compute_robustness_score
from visualization.static_plot import plot_function
from visualization.sensitivity_plot import plot_sensitivity
from reporting.summary import print_summary, save_summary_report
from settings import (
    RUN_SEED,
    BOUNDS,
    DIRECTION,
    PLOT_DOMAIN,
    NUMERICAL_X0,
    PERTURBATION_GRID,
)

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'outputs')
PLOTS_DIR = os.path.join(OUTPUT_DIR, 'plots')
REPORTS_DIR = os.path.join(OUTPUT_DIR, 'reports')


def run_experiment():
    np.random.seed(RUN_SEED)
    os.makedirs(PLOTS_DIR, exist_ok=True)
    os.makedirs(REPORTS_DIR, exist_ok=True)

    print('\n=== EXPERIMENT 02 — OPTIMISATION AND SENSITIVITY ANALYSIS ===')
    print('    Objective:   f(x) = x³ − 3x² + 2')
    print(f'    Domain:      [{BOUNDS[0]}, {BOUNDS[1]}]')
    print(f'    Direction:   {DIRECTION}\n')
    print(f'    Run seed:    {RUN_SEED}\n')

    # Symbolic derivatives
    d1, d2 = get_symbolic_derivatives()
    print(f"First derivative:    f'(x)  = {d1}")
    print(f"Second derivative:   f''(x) = {d2}\n")

    # Critical point discovery and classification
    candidates = find_symbolic_candidates()
    classified = classify_critical_points(candidates)

    # Constrained optimisation
    recommendation = constrained_optimize(BOUNDS, DIRECTION)

    # Numerical methods (both seeded from x0=2.5, in the basin of the minimum)
    gd_result = gradient_descent(x0=NUMERICAL_X0)
    newton_result = newtons_method(x0=NUMERICAL_X0)

    # Sensitivity analysis across parameters a, b, c
    baseline, sens_records = sensitivity_analysis(
        BOUNDS,
        DIRECTION,
        perturbations=PERTURBATION_GRID,
    )
    robustness = compute_robustness_score(sens_records, baseline)

    # Print recommendation report
    report_text = print_summary(
        classified,
        recommendation,
        gd_result,
        newton_result,
        sens_records,
        robustness,
        numerical_x0=NUMERICAL_X0,
    )
    report_path = os.path.join(REPORTS_DIR, 'summary_report.txt')
    save_summary_report(report_text, report_path)

    # Visualizations
    print('Displaying objective function plot...')
    plot_function(
        BOUNDS,
        recommendation,
        domain=PLOT_DOMAIN,
        save_path=os.path.join(PLOTS_DIR, 'objective_plot.png'),
    )

    print('Displaying sensitivity analysis plot...')
    plot_sensitivity(
        sens_records,
        save_path=os.path.join(PLOTS_DIR, 'sensitivity_plot.png'),
    )


if __name__ == '__main__':
    run_experiment()
