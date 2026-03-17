import sympy as sp
from .function import f

x = sp.symbols('x')


def get_symbolic_derivatives(params=None):
    expr = f(x, params)
    d1 = sp.diff(expr, x)
    d2 = sp.diff(d1, x)
    return d1, d2
