"""Quick validation script for core experiment checks."""

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent


VALIDATIONS = [
    {
        'name': 'Experiment 01 core checks',
        'cwd': ROOT / 'experiments' / 'experiment_01_function_behavior_analysis',
        'code': """
import sympy as sp
from calculus.derivatives import get_derivatives
from calculus.analysis import find_critical_points

x = sp.symbols('x')
d1, d2 = get_derivatives()
assert sp.simplify(d1 - (3*x**2 - 6*x)) == 0
assert sp.simplify(d2 - (6*x - 6)) == 0
assert sorted(float(v) for v in find_critical_points()) == [0.0, 2.0]
print('pass')
""",
    },
    {
        'name': 'Experiment 02 core checks',
        'cwd': ROOT / 'experiments' / 'experiment_02_optimisation_and_sensitivity_analysis',
        'code': """
from optimization.symbolic_optimizer import find_symbolic_candidates
from optimization.constrained_optimizer import constrained_optimize

assert sorted(float(v) for v in find_symbolic_candidates()) == [0.0, 2.0]
result = constrained_optimize(bounds=(-0.5, 3.5), direction='minimize')
assert abs(result['recommended_x'] - 2.0) < 1e-8
print('pass')
""",
    },
    {
        'name': 'Experiment 04 core checks',
        'cwd': ROOT / 'experiments' / 'experiment_04_fourier_series_reconstruction',
        'code': """
import numpy as np
from calculus import FourierSeriesEngine

engine = FourierSeriesEngine()
coeff = engine.compute_coefficients('square', n_terms=15, n_samples=12000)

# For a square wave, cosine terms should stay close to zero.
assert abs(coeff['a0']) < 0.05
assert np.max(np.abs(coeff['an'][:8])) < 0.1

# First sine harmonic should be close to 4/pi.
expected_b1 = 4 / np.pi
assert abs(coeff['bn'][0] - expected_b1) < 0.08

print('pass')
""",
    },
    {
        'name': 'Experiment 05 core checks',
        'cwd': ROOT / 'experiments' / 'experiment_05_series_sequence_convergence_applications',
        'code': """
import numpy as np
from calculus import ConvergenceEngine

engine = ConvergenceEngine()

temp = engine.temperature_relaxation_sequence(initial=95.0, ambient=22.0, alpha=0.82, steps=80)
assert abs(temp[-1] - 22.0) < 0.2

growth = engine.compound_growth_sequence(initial=1200.0, growth_factor=1.08, steps=25)
assert growth[-1] > 7000.0

ratio = 1.0 / 1.06
geo_terms = engine.geometric_series_terms(payment=1200.0, ratio=ratio, terms=200)
geo_partial = engine.partial_sums(geo_terms)
expected_geo = 1200.0 / (1.0 - ratio)
assert abs(geo_partial[-1] - expected_geo) < 20.0

harm_terms = engine.harmonic_series_terms(base_cost=100.0, terms=2000)
harm_partial = engine.partial_sums(harm_terms)
assert harm_partial[-1] > 700.0

alt_terms = engine.alternating_harmonic_terms(scale=100.0, terms=2000)
alt_partial = engine.partial_sums(alt_terms)
assert abs(alt_partial[-1] - 100.0 * np.log(2.0)) < 0.2

print('pass')
""",
    },
]


def run_validation(item):
    result = subprocess.run(
        [sys.executable, '-c', item['code']],
        cwd=item['cwd'],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.returncode == 0, result


def main():
    all_ok = True
    for item in VALIDATIONS:
        ok, result = run_validation(item)
        if ok:
            print(f"[PASS] {item['name']}")
        else:
            all_ok = False
            print(f"[FAIL] {item['name']}")
            print(result.stderr.strip())

    if all_ok:
        print('\nValidation complete: all checks passed.')
        return 0

    print('\nValidation complete: at least one check failed.')
    return 1


if __name__ == '__main__':
    raise SystemExit(main())
