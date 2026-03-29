"""
Calculus module for Experiment 03: Integral Calculus

Provides symbolic and numerical function definitions and utilities.
"""

from sympy import symbols, sin, cos, exp, ln, sqrt, tan, sec
from sympy import diff as symbolic_diff
from sympy import integrate as symbolic_integrate

x = symbols('x')

def create_function(expression_str):
    """
    Create a SymPy function from string expression.
    
    Args:
        expression_str: String representation of function, e.g., "x**2 + sin(x)"
    
    Returns:
        tuple: (sympy_expr, lambda_func)
    """
    import sympy as sp
    expr = sp.sympify(expression_str)
    lambda_func = sp.lambdify(x, expr, 'numpy')
    return expr, lambda_func

__all__ = ['x', 'create_function']
