import numpy as np
import matplotlib.pyplot as plt
from calculus.function import f


def plot_function(bounds, recommendation, params=None, domain=(-1.0, 4.0),
                  save_path=None):
    lo, hi = domain
    xs = np.linspace(lo, hi, 600)
    ys = f(xs, params)

    fig, ax = plt.subplots(figsize=(10, 6))

    # Main curve
    ax.plot(xs, ys, color='steelblue', linewidth=2.5,
            label='f(x) = x³ − 3x² + 2')

    # Reference lines
    ax.axhline(0, color='black', linewidth=0.8, linestyle='--', alpha=0.5)
    ax.axvline(0, color='black', linewidth=0.8, linestyle='--', alpha=0.5)

    # Shade feasible region
    bounds_lo, bounds_hi = recommendation['bounds']
    ax.axvspan(bounds_lo, bounds_hi, alpha=0.07, color='green',
               label=f'Feasible region  [{bounds_lo}, {bounds_hi}]')

    # All evaluated candidates (grey dots)
    for pt, val in recommendation['all_candidates']:
        ax.plot(pt, val, 'o', color='dimgray', markersize=7, zorder=4)

    # Recommended operating point (red star)
    rec_x = recommendation['recommended_x']
    rec_y = recommendation['objective_value']
    ax.plot(rec_x, rec_y, '*', color='crimson', markersize=18, zorder=5,
            label=f'Recommended x* = {rec_x:.4f}   f(x*) = {rec_y:.4f}')

    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('f(x)', fontsize=12)
    ax.set_title('Experiment 02 — Objective Function and Recommended Operating Point',
                 fontsize=13)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
        if save_path is not None:
                fig.savefig(save_path, dpi=150)
    plt.show()
