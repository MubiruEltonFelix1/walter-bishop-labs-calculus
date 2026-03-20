import matplotlib.pyplot as plt


def plot_sensitivity(sensitivity_records, param_names=None, save_path=None):
    """
    One subplot per parameter, showing how the recommended x* shifts as the
    parameter is perturbed by various percentages.

    A flat line means the parameter has no effect on x* (e.g., a constant
    offset c).  A steep line means the recommendation is highly sensitive to
    that parameter and the robustness of the recommendation is lower.
    """
    if param_names is None:
        param_names = sorted(set(r['param'] for r in sensitivity_records))

    n = len(param_names)
    fig, axes = plt.subplots(1, n, figsize=(5 * n, 5), sharey=False)
    if n == 1:
        axes = [axes]

    for ax, param in zip(axes, param_names):
        subset = [r for r in sensitivity_records if r['param'] == param]
        subset.sort(key=lambda r: r['perturbation_pct'])

        pcts = [r['perturbation_pct'] for r in subset]
        x_stars = [r['x_star'] for r in subset]

        # Baseline x* is the entry with 0% perturbation
        baseline_x = next(r['x_star'] for r in subset if r['perturbation_pct'] == 0.0)

        ax.plot(pcts, x_stars, 'o-', color='steelblue', linewidth=2, markersize=8)
        ax.axhline(baseline_x, color='crimson', linestyle='--', linewidth=1.4,
                   label=f'Baseline x* = {baseline_x:.3f}')
        ax.axvline(0, color='gray', linestyle=':', linewidth=0.9)

        ax.set_xlabel(f'Perturbation of  {param}  (%)', fontsize=11)
        ax.set_ylabel('Recommended x*', fontsize=11)
        ax.set_title(f'Sensitivity to  {param}', fontsize=12)
        ax.legend(fontsize=9)
        ax.grid(True, alpha=0.3)

    fig.suptitle(
        'Experiment 02 — Sensitivity Analysis: Shift in x* Under Parameter Perturbation',
        fontsize=13, y=1.03,
    )
    plt.tight_layout()
    if save_path is not None:
        fig.savefig(save_path, dpi=150)
    plt.show()
