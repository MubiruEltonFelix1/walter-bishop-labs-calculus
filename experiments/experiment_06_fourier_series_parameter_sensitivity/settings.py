"""Configuration settings for Experiment 06: Fourier series parameter sensitivity."""

from __future__ import annotations

import numpy as np


FUNCTIONS = [
    "square",
    "sawtooth",
    "triangle",
]

FOCUS_FUNCTION = "square"

AMPLITUDE_LEVELS = [0.5, 1.0, 1.75]
HARMONIC_COUNTS = [1, 3, 5, 10, 20, 40]

SAMPLING = {
    "coefficient_samples": 24000,
    "plot_points": 5000,
    "domain_min": -np.pi,
    "domain_max": np.pi,
}

VISUALIZATION = {
    "plot_style": "seaborn-v0_8",
    "figure_dpi": 150,
    "figure_size": (12, 7),
    "animation_fps": 20,
}

REPORTING = {
    "summary_filename": "summary_report.txt",
}
