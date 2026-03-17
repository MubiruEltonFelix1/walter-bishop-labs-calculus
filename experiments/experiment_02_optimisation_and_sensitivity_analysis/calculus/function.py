import numpy as np
import sympy as sp

# Default parameters for the objective function:
#   f(x; a, b, c) = a*x^3 + b*x^2 + c
#
# With a=1, b=-3, c=2 this gives f(x) = x^3 - 3x^2 + 2,
# extending the same function studied in Experiment 01.
# Critical points remain at x=0 (local max) and x=2 (local min).
# The parametric form enables sensitivity analysis by perturbing a, b, and c.

DEFAULT_PARAMS = {
    'a': 1,
    'b': -3,
    'c': 2,
}


def f(x, params=None):
    if params is None:
        params = DEFAULT_PARAMS
    a = params['a']
    b = params['b']
    c = params['c']
    return a * x**3 + b * x**2 + c
