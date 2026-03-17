import sys
import os

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
from reporting.summary import print_summary

BOUNDS = (-0.5, 3.5)
DIRECTION = 'minimize'


def run_experiment():
    print('\n=== EXPERIMENT 02 — OPTIMISATION AND SENSITIVITY ANALYSIS ===')
    print('    Objective:   f(x) = x³ − 3x² + 2')
    print(f'    Domain:      [{BOUNDS[0]}, {BOUNDS[1]}]')
    print(f'    Direction:   {DIRECTION}\n')

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
    gd_result = gradient_descent(x0=2.5)
    newton_result = newtons_method(x0=2.5)

    # Sensitivity analysis across parameters a, b, c
    baseline, sens_records = sensitivity_analysis(BOUNDS, DIRECTION)
    robustness = compute_robustness_score(sens_records, baseline)

    # Print recommendation report
    print_summary(classified, recommendation, gd_result, newton_result,
                  sens_records, robustness)

    # Visualizations
    print('Displaying objective function plot...')
    plot_function(BOUNDS, recommendation)

    print('Displaying sensitivity analysis plot...')
    plot_sensitivity(sens_records)


if __name__ == '__main__':
    run_experiment()
