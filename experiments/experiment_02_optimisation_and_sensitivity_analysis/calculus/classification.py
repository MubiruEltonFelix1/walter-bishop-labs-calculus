import sympy as sp
from .derivatives import get_symbolic_derivatives, x


def classify_critical_points(candidates, params=None):
    """
    Given a list of symbolic critical point candidates, evaluate f''(x) at each
    and return a list of dicts with classification labels.

    Labels:
        'local minimum'  — f''(x) > 0
        'local maximum'  — f''(x) < 0
        'inconclusive'   — f''(x) = 0 (higher-order test required)
    """
    _, d2 = get_symbolic_derivatives(params)
    results = []
    for cp in candidates:
        val = float(d2.subs(x, cp))
        if val > 0:
            label = 'local minimum'
        elif val < 0:
            label = 'local maximum'
        else:
            label = 'inconclusive (higher-order test required)'
        results.append({
            'x': float(cp),
            'second_derivative': val,
            'classification': label,
        })
    return results
