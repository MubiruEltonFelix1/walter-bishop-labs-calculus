import sympy as sp
from calculus.derivatives import get_symbolic_derivatives, x


def find_symbolic_candidates(params=None):
    """
    Solve f'(x) = 0 symbolically and return all real-valued solutions.
    Returns an empty list if SymPy cannot solve the expression.
    """
    d1, _ = get_symbolic_derivatives(params)
    try:
        raw = sp.solve(d1, x)
    except Exception:
        return []
    return [cp for cp in raw if cp.is_real]
