import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from calculus.function import f
from calculus.derivatives import first_derivative, second_derivative, x as sym_x
from calculus.analysis import find_critical_points
from settings import PLOT_DOMAIN, PLOT_POINTS

def plot_function():
    plt.style.use('dark_background')

    x_vals = np.linspace(PLOT_DOMAIN[0], PLOT_DOMAIN[1], PLOT_POINTS)

    f_prime = sp.lambdify(sym_x, first_derivative, 'numpy')
    f_double_prime = sp.lambdify(sym_x, second_derivative, 'numpy')

    y  = f(x_vals)
    y1 = f_prime(x_vals)
    y2 = f_double_prime(x_vals)

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y,  label="f(x)",    linewidth=2)
    plt.plot(x_vals, y1, label="f'(x)",   linewidth=1.5, linestyle='--')
    plt.plot(x_vals, y2, label="f''(x)",  linewidth=1.5, linestyle=':')

    # Mark critical points
    for cp in find_critical_points():
        cp_val = float(cp)
        plt.scatter([cp_val], [f(cp_val)], zorder=5, s=80,
                    label=f"Critical point x={cp_val:.2f}")

    plt.axhline(0, color='white', linewidth=0.5, alpha=0.4)
    plt.axvline(0, color='white', linewidth=0.5, alpha=0.4)

    plt.title("Walter Bishop Calculus Experiment")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()