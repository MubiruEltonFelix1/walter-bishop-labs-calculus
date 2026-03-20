import numpy as np
from calculus.function import DEFAULT_PARAMS
from optimization.constrained_optimizer import constrained_optimize
from settings import PERTURBATION_GRID

# Parameters to perturb.  'c' is the constant offset — it has no effect on
# x* but does shift the objective value, which is itself a useful finding.
PERTURBABLE_PARAMS = ['a', 'b', 'c']


def sensitivity_analysis(bounds, direction='minimize',
                         perturbations=None, param_names=None):
    """
    For each parameter in param_names, perturb it by each fraction in
    perturbations and recompute the constrained optimum.

    Returns:
        baseline  — constrained_optimize result at default parameters
        records   — list of dicts, one per (param, perturbation) combination
    """
    if perturbations is None:
        perturbations = PERTURBATION_GRID
    if param_names is None:
        param_names = PERTURBABLE_PARAMS

    baseline = constrained_optimize(bounds, direction, params=None)
    baseline_x = baseline['recommended_x']
    baseline_obj = baseline['objective_value']

    records = []
    for param in param_names:
        base_val = DEFAULT_PARAMS[param]
        for pct in perturbations:
            # If the base value is exactly 0, shift by a small absolute amount
            # instead of a percentage so the perturbation is still meaningful.
            if base_val != 0:
                new_val = base_val * (1.0 + pct)
            else:
                new_val = pct * 0.1

            perturbed_params = dict(DEFAULT_PARAMS)
            perturbed_params[param] = new_val

            result = constrained_optimize(bounds, direction, params=perturbed_params)
            records.append({
                'param': param,
                'perturbation_pct': pct * 100,
                'param_value': new_val,
                'x_star': result['recommended_x'],
                'objective': result['objective_value'],
                'dx_star': result['recommended_x'] - baseline_x,
                'd_objective': result['objective_value'] - baseline_obj,
            })

    return baseline, records
