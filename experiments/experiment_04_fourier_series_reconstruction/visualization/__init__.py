"""
Visualization module for Experiment 04.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np


class FourierVisualizer:
    """Create and save core Fourier reconstruction plots."""

    def __init__(self, style: str = "seaborn-v0_8", dpi: int = 150, figsize=(12, 7)):
        try:
            plt.style.use(style)
        except Exception:
            pass
        self.dpi = dpi
        self.figsize = figsize

    def plot_reconstructions(self, x, y_true, reconstructions, title, filename, show=False):
        fig, ax = plt.subplots(figsize=self.figsize, dpi=self.dpi)
        ax.plot(x, y_true, color="black", linewidth=2.4, label="True signal")

        for n_terms, y_hat in reconstructions.items():
            ax.plot(x, y_hat, linewidth=1.4, alpha=0.9, label=f"N={n_terms}")

        ax.set_title(title, fontsize=13, fontweight="bold")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.grid(True, alpha=0.3)
        ax.legend(ncol=2)
        fig.tight_layout()
        fig.savefig(filename, dpi=self.dpi, bbox_inches="tight")
        if show:
            plt.show(block=True)
        plt.close(fig)

    def plot_spectrum(self, magnitudes, title, filename, show=False):
        indices = np.arange(1, len(magnitudes) + 1)

        fig, ax = plt.subplots(figsize=self.figsize, dpi=self.dpi)
        ax.stem(indices, magnitudes, basefmt=" ")
        ax.set_title(title, fontsize=13, fontweight="bold")
        ax.set_xlabel("Harmonic n")
        ax.set_ylabel("Magnitude sqrt(an^2 + bn^2)")
        ax.grid(True, alpha=0.3)
        fig.tight_layout()
        fig.savefig(filename, dpi=self.dpi, bbox_inches="tight")
        if show:
            plt.show(block=True)
        plt.close(fig)

    def plot_error_decay(self, harmonic_counts, mse_values, max_error_values, title, filename, show=False):
        fig, ax = plt.subplots(figsize=self.figsize, dpi=self.dpi)
        ax.plot(harmonic_counts, mse_values, marker="o", linewidth=2, label="MSE")
        ax.plot(harmonic_counts, max_error_values, marker="s", linewidth=2, label="Max abs error")
        ax.set_title(title, fontsize=13, fontweight="bold")
        ax.set_xlabel("Number of harmonics (N)")
        ax.set_ylabel("Error")
        ax.grid(True, alpha=0.3)
        ax.legend()
        fig.tight_layout()
        fig.savefig(filename, dpi=self.dpi, bbox_inches="tight")
        if show:
            plt.show(block=True)
        plt.close(fig)
