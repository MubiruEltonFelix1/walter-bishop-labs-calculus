from calculus.function import f
from optimization.symbolic_optimizer import find_symbolic_candidates


def constrained_optimize(bounds, direction='minimize', params=None):
    """
    Optimise f over the closed interval [bounds[0], bounds[1]].

    Strategy:
      1. Find interior critical points symbolically.
      2. Filter to those within the feasible region.
      3. Evaluate f at interior candidates and both boundary endpoints.
      4. Select the best point according to direction ('minimize' or 'maximize').

    Returns a dict with the recommendation and every candidate evaluated.
    """
    lo, hi = bounds
    symbolic_candidates = find_symbolic_candidates(params)
    interior = [
        float(cp) for cp in symbolic_candidates
        if lo <= float(cp) <= hi
    ]
    all_points = interior + [lo, hi]
    evals = [(pt, float(f(pt, params))) for pt in all_points]

    if direction == 'minimize':
        best = min(evals, key=lambda t: t[1])
    else:
        best = max(evals, key=lambda t: t[1])

    return {
        'recommended_x': best[0],
        'objective_value': best[1],
        'direction': direction,
        'all_candidates': evals,
        'bounds': bounds,
    }
