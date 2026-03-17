import numpy as np


def compute_robustness_score(sensitivity_records, baseline):
    """
    Compute a scalar robustness index in [0, 1].

    Method:
      For each non-baseline perturbation scenario, compute the shift in x*
      and in the objective value as fractions of the baseline values.
      Average these relative shifts across all scenarios, then map through
      an exponential decay so that:

        score → 1.0   when all shifts are near zero (stable recommendation)
        score → 0.0   when shifts are large relative to baseline values

    Formula:
        combined = 0.5 * mean(|Δx*| / |x*_baseline|)
                 + 0.5 * mean(|Δf| / |f(x*_baseline)|)
        score = exp(-combined)
    """
    non_baseline = [r for r in sensitivity_records if r['perturbation_pct'] != 0.0]
    if not non_baseline:
        return 1.0

    x_denom = abs(baseline['recommended_x']) + 1e-10
    obj_denom = abs(baseline['objective_value']) + 1e-10

    rel_dx = [abs(r['dx_star']) / x_denom for r in non_baseline]
    rel_dobj = [abs(r['d_objective']) / obj_denom for r in non_baseline]

    combined = 0.5 * np.mean(rel_dx) + 0.5 * np.mean(rel_dobj)
    score = float(np.exp(-combined))
    return round(float(np.clip(score, 0.0, 1.0)), 4)


def robustness_label(score):
    if score >= 0.80:
        return 'HIGH — recommendation is stable under parameter uncertainty'
    elif score >= 0.50:
        return 'MODERATE — recommendation shifts under some perturbations'
    else:
        return 'LOW — recommendation is highly sensitive to parameter changes'
