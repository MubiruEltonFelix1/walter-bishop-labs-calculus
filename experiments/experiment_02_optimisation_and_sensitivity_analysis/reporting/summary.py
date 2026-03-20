from analysis.robustness import robustness_label

_SEP = '=' * 70
_DIV = '-' * 50


def print_summary(classified, recommendation, gd_result, newton_result,
                  sensitivity_records, robustness_score, numerical_x0=2.5):
    lines = []

    lines.append('')
    lines.append(_SEP)
    lines.append('  EXPERIMENT 02 — RECOMMENDATION REPORT')
    lines.append(_SEP)

    # --- Critical point classification ---
    lines.append('')
    lines.append('  CRITICAL POINT CLASSIFICATION')
    lines.append('  ' + _DIV)
    for cp in classified:
        lines.append(
            f"  x = {cp['x']:>8.4f}  |  "
            f"f''(x) = {cp['second_derivative']:>8.4f}  |  "
            f"{cp['classification']}"
        )

    # --- Constrained optimisation result ---
    lines.append('')
    lines.append('  CONSTRAINED OPTIMISATION RESULT')
    lines.append('  ' + _DIV)
    rec = recommendation
    lines.append(f"  Feasible domain:    [{rec['bounds'][0]}, {rec['bounds'][1]}]")
    lines.append(f"  Direction:          {rec['direction']}")
    lines.append(f"  Recommended x*:     {rec['recommended_x']:.6f}")
    lines.append(f"  Objective f(x*):    {rec['objective_value']:.6f}")
    lines.append('')
    lines.append('  All candidates evaluated:')
    for pt, val in sorted(rec['all_candidates'], key=lambda t: t[0]):
        marker = '  ← selected' if abs(pt - rec['recommended_x']) < 1e-9 else ''
        lines.append(f"    x = {pt:>8.4f}   f(x) = {val:>10.4f}{marker}")

    # --- Numerical method comparison ---
    lines.append('')
    lines.append(f'  NUMERICAL METHOD COMPARISON  (x0 = {numerical_x0})')
    lines.append('  ' + _DIV)
    for result in [gd_result, newton_result]:
        status = 'converged' if result['converged'] else 'did not converge'
        lines.append(
            f"  {result['method']:<25}  "
            f"x = {result['x']:.6f}  |  "
            f"{result['iterations']:>5} iterations  |  "
            f"{status}"
        )

    # --- Sensitivity summary ---
    lines.append('')
    lines.append('  SENSITIVITY SUMMARY  (top shifts in x*)')
    lines.append('  ' + _DIV)
    non_baseline = [r for r in sensitivity_records if r['perturbation_pct'] != 0.0]
    sorted_by_impact = sorted(non_baseline, key=lambda r: abs(r['dx_star']), reverse=True)
    for r in sorted_by_impact[:6]:
        sign = '+' if r['perturbation_pct'] > 0 else ''
        lines.append(
            f"  param {r['param']}  {sign}{r['perturbation_pct']:.0f}%  →  "
            f"x* = {r['x_star']:>8.4f}  "
            f"(Δx* = {r['dx_star']:>+.4f},  Δf = {r['d_objective']:>+.4f})"
        )

    # --- Robustness ---
    lines.append('')
    lines.append('  ROBUSTNESS ASSESSMENT')
    lines.append('  ' + _DIV)
    lines.append(f"  Robustness score:   {robustness_score:.4f}")
    lines.append(f"  Assessment:         {robustness_label(robustness_score)}")

    lines.append('')
    lines.append(_SEP)
    lines.append('  END OF REPORT')
    lines.append(_SEP)
    lines.append('')

    report_text = '\n'.join(lines)
    print(report_text)
    return report_text


def save_summary_report(report_text, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report_text)
