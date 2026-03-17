import numpy as np
import sympy as sp
from calculus.derivatives import get_symbolic_derivatives, x as sym_x


def _to_numpy(expr):
    return sp.lambdify(sym_x, expr, modules='numpy')


def gradient_descent(params=None, x0=2.5, learning_rate=0.01,
                     max_iter=2000, tol=1e-9):
    """
    Minimise f by following the negative gradient of f'(x) (i.e. steepest descent).

    Update rule:  x_{n+1} = x_n - lr * f'(x_n)

    With lr=0.01 and f''(x*)=6, convergence factor is |1 - 0.01*6| = 0.94
    per iteration — linear but reliable from x0=2.5 toward the minimum at x=2.
    """
    d1, _ = get_symbolic_derivatives(params)
    grad_fn = _to_numpy(d1)
    xv = float(x0)
    for i in range(max_iter):
        step = -learning_rate * grad_fn(xv)
        xv += step
        if abs(step) < tol:
            return {
                'x': xv,
                'iterations': i + 1,
                'converged': True,
                'method': 'Gradient Descent',
            }
    return {
        'x': xv,
        'iterations': max_iter,
        'converged': False,
        'method': 'Gradient Descent',
    }


def newtons_method(params=None, x0=2.5, max_iter=100, tol=1e-12):
    """
    Find a root of f'(x) = 0 using Newton–Raphson on the first derivative.

    Update rule:  x_{n+1} = x_n - f'(x_n) / f''(x_n)

    This is second-order convergence in the neighbourhood of a non-degenerate
    critical point.  Starting from x0=2.5, the method quadratically converges
    to the local minimum at x=2.
    """
    d1, d2 = get_symbolic_derivatives(params)
    grad_fn = _to_numpy(d1)
    hess_fn = _to_numpy(d2)
    xv = float(x0)
    for i in range(max_iter):
        h = hess_fn(xv)
        if abs(h) < 1e-14:
            break
        step = -grad_fn(xv) / h
        xv += step
        if abs(step) < tol:
            return {
                'x': xv,
                'iterations': i + 1,
                'converged': True,
                'method': "Newton's Method",
            }
    return {
        'x': xv,
        'iterations': max_iter,
        'converged': False,
        'method': "Newton's Method",
    }
