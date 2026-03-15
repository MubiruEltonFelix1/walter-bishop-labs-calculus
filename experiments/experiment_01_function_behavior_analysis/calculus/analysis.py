import sympy as sp
from calculus.derivatives import first_derivative, x

def find_critical_points():
    critical_points=sp.solve(first_derivative, x)
    return critical_points

    