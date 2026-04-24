import subprocess
import sys
from pathlib import Path


def test_experiment_05_convergence_pipeline_smoke():
    repo_root = Path(__file__).resolve().parents[1]
    exp_dir = repo_root / 'experiments' / 'experiment_05_series_sequence_convergence_applications'

    code = """
import numpy as np
from calculus import ConvergenceEngine

engine = ConvergenceEngine()

temp = engine.temperature_relaxation_sequence(initial=95.0, ambient=22.0, alpha=0.82, steps=80)
assert abs(temp[-1] - 22.0) < 0.2

growth = engine.compound_growth_sequence(initial=1200.0, growth_factor=1.08, steps=25)
assert growth[-1] > 7000.0

ratio = 1.0 / 1.06
geo_terms = engine.geometric_series_terms(payment=1200.0, ratio=ratio, terms=220)
geo_partial = engine.partial_sums(geo_terms)
expected_geo = 1200.0 / (1.0 - ratio)
assert abs(geo_partial[-1] - expected_geo) < 10.0

harm_terms = engine.harmonic_series_terms(base_cost=100.0, terms=3000)
harm_partial = engine.partial_sums(harm_terms)
assert harm_partial[-1] > 800.0

alt_terms = engine.alternating_harmonic_terms(scale=100.0, terms=3000)
alt_partial = engine.partial_sums(alt_terms)
assert abs(alt_partial[-1] - 100.0 * np.log(2.0)) < 0.15

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
