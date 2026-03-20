import subprocess
import sys
from pathlib import Path


def test_experiment_01_symbolic_and_critical_points():
    repo_root = Path(__file__).resolve().parents[1]
    exp_dir = repo_root / 'experiments' / 'experiment_01_function_behavior_analysis'

    code = """
import sympy as sp
from calculus.derivatives import get_derivatives
from calculus.analysis import find_critical_points

x = sp.symbols('x')
d1, d2 = get_derivatives()
assert sp.simplify(d1 - (3*x**2 - 6*x)) == 0
assert sp.simplify(d2 - (6*x - 6)) == 0

critical_points = sorted(float(v) for v in find_critical_points())
assert critical_points == [0.0, 2.0]
print('ok')
"""

    result = subprocess.run(
        [sys.executable, '-c', code],
        cwd=exp_dir,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert 'ok' in result.stdout
