import subprocess
import sys
from pathlib import Path


def test_experiment_02_recommendation_pipeline_smoke():
    repo_root = Path(__file__).resolve().parents[1]
    exp_dir = repo_root / 'experiments' / 'experiment_02_optimisation_and_sensitivity_analysis'

    code = """
from optimization.symbolic_optimizer import find_symbolic_candidates
from optimization.constrained_optimizer import constrained_optimize
from analysis.sensitivity import sensitivity_analysis

candidates = sorted(float(v) for v in find_symbolic_candidates())
assert candidates == [0.0, 2.0]

recommendation = constrained_optimize(bounds=(-0.5, 3.5), direction='minimize')
assert abs(recommendation['recommended_x'] - 2.0) < 1e-8

_, records = sensitivity_analysis(
    bounds=(-0.5, 3.5),
    direction='minimize',
    perturbations=[-0.10, 0.0, 0.10],
)
assert len(records) == 9
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
