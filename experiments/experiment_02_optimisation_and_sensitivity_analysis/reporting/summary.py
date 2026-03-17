from analysis.robustness import robustness_label

_SEP = '=' * 70
_DIV = '-' * 50


def print_summary(classified, recommendation, gd_result, newton_result,
                  sensitivity_records, robustness_score):
    print('\n' + _SEP)
    print('  EXPERIMENT 02 — RECOMMENDATION REPORT')
    print(_SEP)

    # --- Critical point classification ---
    print('\n  CRITICAL POINT CLASSIFICATION')
    print('  ' + _DIV)
    for cp in classified:
        print(
            f"  x = {cp['x']:>8.4f}  |  "
            f"f''(x) = {cp['second_derivative']:>8.4f}  |  "
            f"{cp['classification']}"
        )

    # --- Constrained optimisation result ---
    print('\n  CONSTRAINED OPTIMISATION RESULT')
    print('  ' + _DIV)
    rec = recommendation
    print(f"  Feasible domain:    [{rec['bounds'][0]}, {rec['bounds'][1]}]")
    print(f"  Direction:          {rec['direction']}")
    print(f"  Recommended x*:     {rec['recommended_x']:.6f}")
    print(f"  Objective f(x*):    {rec['objective_value']:.6f}")
    print()
    print('  All candidates evaluated:')
    for pt, val in sorted(rec['all_candidates'], key=lambda t: t[0]):
        marker = '  ← selected' if abs(pt - rec['recommended_x']) < 1e-9 else ''
        print(f"    x = {pt:>8.4f}   f(x) = {val:>10.4f}{marker}")

    # --- Numerical method comparison ---
    print('\n  NUMERICAL METHOD COMPARISON  (x0 = 2.5)')
    print('  ' + _DIV)
    for result in [gd_result, newton_result]:
        status = 'converged' if result['converged'] else 'did not converge'
        print(
            f"  {result['method']:<25}  "
            f"x = {result['x']:.6f}  |  "
            f"{result['iterations']:>5} iterations  |  "
            f"{status}"
        )

    # --- Sensitivity summary ---
    print('\n  SENSITIVITY SUMMARY  (top shifts in x*)')
    print('  ' + _DIV)
    non_baseline = [r for r in sensitivity_records if r['perturbation_pct'] != 0.0]
    sorted_by_impact = sorted(non_baseline, key=lambda r: abs(r['dx_star']), reverse=True)
    for r in sorted_by_impact[:6]:
        sign = '+' if r['perturbation_pct'] > 0 else ''
        print(
            f"  param {r['param']}  {sign}{r['perturbation_pct']:.0f}%  →  "
            f"x* = {r['x_star']:>8.4f}  "
            f"(Δx* = {r['dx_star']:>+.4f},  Δf = {r['d_objective']:>+.4f})"
        )

    # --- Robustness ---
    print('\n  ROBUSTNESS ASSESSMENT')
    print('  ' + _DIV)
    print(f"  Robustness score:   {robustness_score:.4f}")
    print(f"  Assessment:         {robustness_label(robustness_score)}")

    print('\n' + _SEP)
    print('  END OF REPORT')
    print(_SEP + '\n')
