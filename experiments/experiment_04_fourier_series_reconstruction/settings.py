"""
Configuration settings for Experiment 04: Fourier Series Reconstruction.
"""

# Periodic signal definitions explored in this experiment.
FUNCTIONS = [
    "square",
    "sawtooth",
    "triangle",
]

# Harmonic counts used for partial-sum reconstruction.
HARMONIC_COUNTS = [1, 3, 5, 10, 20, 40]

# Sampling controls.
SAMPLING = {
    "coefficient_samples": 20000,
    "plot_points": 4000,
    "domain_min": -3.141592653589793,
    "domain_max": 3.141592653589793,
}

# Visualization controls.
VISUALIZATION = {
    "plot_style": "seaborn-v0_8",
    "figure_dpi": 150,
    "figure_size": (12, 7),
    "show_grid": True,
}

# Output/report controls.
REPORTING = {
    "save_plots": True,
    "summary_filename": "summary_report.txt",
}
