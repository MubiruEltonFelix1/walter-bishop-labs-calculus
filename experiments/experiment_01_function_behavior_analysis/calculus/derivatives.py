import sympy as sp
from .function import f

x=sp.symbols('x')

first_derivative = sp.diff(f(x), x)
second_derivative = sp.diff(first_derivative, x)

def get_derivatives():
    return first_derivative, second_derivative