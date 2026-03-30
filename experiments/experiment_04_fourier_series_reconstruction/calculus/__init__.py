"""
Fourier computation module for Experiment 04.
"""

from __future__ import annotations

import numpy as np


class FourierSeriesEngine:
    """Compute Fourier coefficients, reconstructions, and error metrics."""

    def __init__(self):
        self.period = 2 * np.pi

    def square_wave(self, x: np.ndarray) -> np.ndarray:
        return np.where(np.sin(x) >= 0.0, 1.0, -1.0)

    def sawtooth_wave(self, x: np.ndarray) -> np.ndarray:
        wrapped = ((x + np.pi) % (2 * np.pi)) - np.pi
        return wrapped / np.pi

    def triangle_wave(self, x: np.ndarray) -> np.ndarray:
        saw = self.sawtooth_wave(x)
        return 1.0 - 2.0 * np.abs(saw)

    def get_function(self, function_name: str):
        if function_name == "square":
            return self.square_wave
        if function_name == "sawtooth":
            return self.sawtooth_wave
        if function_name == "triangle":
            return self.triangle_wave
        raise ValueError(f"Unsupported function_name: {function_name}")

    def compute_coefficients(self, function_name: str, n_terms: int, n_samples: int = 20000) -> dict:
        f = self.get_function(function_name)
        x = np.linspace(-np.pi, np.pi, n_samples, endpoint=False)
        y = f(x)

        a0 = (1 / np.pi) * np.trapezoid(y, x)
        an = np.zeros(n_terms)
        bn = np.zeros(n_terms)

        for n in range(1, n_terms + 1):
            cos_nx = np.cos(n * x)
            sin_nx = np.sin(n * x)
            an[n - 1] = (1 / np.pi) * np.trapezoid(y * cos_nx, x)
            bn[n - 1] = (1 / np.pi) * np.trapezoid(y * sin_nx, x)

        return {
            "success": True,
            "function": function_name,
            "a0": float(a0),
            "an": an,
            "bn": bn,
            "n_terms": n_terms,
        }

    def reconstruct(self, x: np.ndarray, a0: float, an: np.ndarray, bn: np.ndarray) -> np.ndarray:
        y = np.full_like(x, a0 / 2.0, dtype=float)
        for n in range(1, len(an) + 1):
            y += an[n - 1] * np.cos(n * x) + bn[n - 1] * np.sin(n * x)
        return y

    def reconstruction_metrics(self, y_true: np.ndarray, y_hat: np.ndarray) -> dict:
        abs_error = np.abs(y_true - y_hat)
        mse = float(np.mean((y_true - y_hat) ** 2))
        max_error = float(np.max(abs_error))
        return {
            "mse": mse,
            "max_error": max_error,
        }

    def harmonic_magnitudes(self, an: np.ndarray, bn: np.ndarray) -> np.ndarray:
        return np.sqrt(an ** 2 + bn ** 2)
