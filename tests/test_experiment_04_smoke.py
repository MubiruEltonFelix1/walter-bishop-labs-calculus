import subprocess
import sys
from pathlib import Path


def test_experiment_04_fourier_reconstruction_smoke():
    repo_root = Path(__file__).resolve().parents[1]
    exp_dir = repo_root / 'experiments' / 'experiment_04_fourier_series_reconstruction'

    code = """
import numpy as np
from calculus import FourierSeriesEngine

engine = FourierSeriesEngine()

x = np.linspace(-np.pi, np.pi, 4000, endpoint=False)
y_true = engine.square_wave(x)

coeff = engine.compute_coefficients('square', n_terms=25, n_samples=14000)
assert coeff['success']

# Square-wave sanity checks
assert abs(coeff['a0']) < 0.05
assert np.max(np.abs(coeff['an'][:10])) < 0.1
assert abs(coeff['bn'][0] - 4/np.pi) < 0.08

# Reconstruction quality should improve as N grows.
y_hat_5 = engine.reconstruct(x, coeff['a0'], coeff['an'][:5], coeff['bn'][:5])
y_hat_25 = engine.reconstruct(x, coeff['a0'], coeff['an'][:25], coeff['bn'][:25])

m5 = engine.reconstruction_metrics(y_true, y_hat_5)
m25 = engine.reconstruction_metrics(y_true, y_hat_25)
assert m25['mse'] < m5['mse']

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
