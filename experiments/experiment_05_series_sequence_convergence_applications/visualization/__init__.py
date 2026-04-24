"""
Visualization and animation helpers for Experiment 05.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


class ConvergenceVisualizer:
    """Create static and animated visuals for sequence and series behavior."""

    def __init__(self, style: str = "seaborn-v0_8", dpi: int = 150, figsize=(12, 7), fps: int = 20):
        try:
            plt.style.use(style)
        except Exception:
            pass
        self.dpi = dpi
        self.figsize = figsize
        self.fps = fps

    def _save_animation_html(self, anim: FuncAnimation, filename: str, title: str):
        html = anim.to_jshtml(fps=self.fps)
        payload = (
            "<html><head><meta charset='utf-8'></head><body>"
            f"<h2>{title}</h2>{html}</body></html>"
        )
        Path(filename).write_text(payload, encoding="utf-8")

    def plot_sequence_terms(self, terms, title, expected_behavior, filename, show=False):
        n = np.arange(len(terms))
        fig, ax = plt.subplots(figsize=self.figsize, dpi=self.dpi)
        ax.plot(n, terms, marker="o", linewidth=2, label="Sequence terms")
        ax.set_title(title, fontsize=13, fontweight="bold")
        ax.set_xlabel("n")
        ax.set_ylabel("a_n")
        ax.grid(True, alpha=0.3)
        ax.legend(frameon=False, title=f"Expected: {expected_behavior}")
        fig.tight_layout()
        fig.savefig(filename, dpi=self.dpi, bbox_inches="tight")
        if show:
            plt.show(block=True)
        plt.close(fig)

    def plot_series_terms_and_partial(self, series_terms, partial_sums, title, filename, show=False):
        n = np.arange(1, len(series_terms) + 1)
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=self.figsize, dpi=self.dpi, sharex=True)

        ax1.plot(n, series_terms, color="#0f766e", linewidth=2)
        ax1.set_ylabel("Term value")
        ax1.grid(True, alpha=0.3)
        ax1.set_title(title, fontsize=13, fontweight="bold")

        ax2.plot(n, partial_sums, color="#9a3412", linewidth=2)
        ax2.set_xlabel("Number of terms")
        ax2.set_ylabel("Partial sum")
        ax2.grid(True, alpha=0.3)

        fig.tight_layout()
        fig.savefig(filename, dpi=self.dpi, bbox_inches="tight")
        if show:
            plt.show(block=True)
        plt.close(fig)

    def plot_sequence_comparison(self, convergent_terms, divergent_terms, filename, show=False):
        n1 = np.arange(len(convergent_terms))
        n2 = np.arange(len(divergent_terms))

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), dpi=self.dpi)

        ax1.plot(n1, convergent_terms, marker="o", linewidth=2, color="#1d4ed8")
        ax1.set_title("Convergent sequence")
        ax1.set_xlabel("n")
        ax1.set_ylabel("a_n")
        ax1.grid(True, alpha=0.3)

        ax2.plot(n2, divergent_terms, marker="o", linewidth=2, color="#dc2626")
        ax2.set_title("Divergent sequence")
        ax2.set_xlabel("n")
        ax2.set_ylabel("a_n")
        ax2.grid(True, alpha=0.3)

        fig.tight_layout()
        fig.savefig(filename, dpi=self.dpi, bbox_inches="tight")
        if show:
            plt.show(block=True)
        plt.close(fig)

    def plot_series_comparison(self, geometric_partial, harmonic_partial, alternating_partial, filename, show=False):
        n_geo = np.arange(1, len(geometric_partial) + 1)
        n_har = np.arange(1, len(harmonic_partial) + 1)
        n_alt = np.arange(1, len(alternating_partial) + 1)

        fig, ax = plt.subplots(figsize=self.figsize, dpi=self.dpi)
        ax.plot(n_geo, geometric_partial, linewidth=2.5, label="Geometric partial sum")
        ax.plot(n_har, harmonic_partial, linewidth=2.0, label="Harmonic partial sum")
        ax.plot(n_alt, alternating_partial, linewidth=2.0, label="Alternating partial sum")
        ax.set_title("Series partial sums: convergence vs divergence", fontsize=13, fontweight="bold")
        ax.set_xlabel("Number of terms")
        ax.set_ylabel("Partial sum value")
        ax.grid(True, alpha=0.3)
        ax.legend(frameon=False)
        fig.tight_layout()
        fig.savefig(filename, dpi=self.dpi, bbox_inches="tight")
        if show:
            plt.show(block=True)
        plt.close(fig)

    def animate_sequence_progression(self, convergent_terms, divergent_terms, filename, show=False):
        n_conv = np.arange(len(convergent_terms))
        n_div = np.arange(len(divergent_terms))
        frame_count = min(len(convergent_terms), len(divergent_terms))

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), dpi=self.dpi)

        line1, = ax1.plot([], [], color="#1d4ed8", linewidth=2)
        line2, = ax2.plot([], [], color="#dc2626", linewidth=2)

        ax1.set_title("Convergent sequence progression")
        ax1.set_xlabel("n")
        ax1.set_ylabel("a_n")
        ax1.set_xlim(0, len(convergent_terms) - 1)
        ax1.set_ylim(np.min(convergent_terms) * 0.95, np.max(convergent_terms) * 1.05)
        ax1.grid(True, alpha=0.3)

        ax2.set_title("Divergent sequence progression")
        ax2.set_xlabel("n")
        ax2.set_ylabel("a_n")
        ax2.set_xlim(0, len(divergent_terms) - 1)
        ax2.set_ylim(np.min(divergent_terms) * 0.95, np.max(divergent_terms) * 1.05)
        ax2.grid(True, alpha=0.3)

        def update(frame_index):
            idx = frame_index + 1
            line1.set_data(n_conv[:idx], convergent_terms[:idx])
            line2.set_data(n_div[:idx], divergent_terms[:idx])
            return line1, line2

        anim = FuncAnimation(fig, update, frames=frame_count, interval=1000 / self.fps, blit=True)
        self._save_animation_html(anim, filename, "Sequence convergence/divergence animation")

        if show:
            plt.show(block=True)
        plt.close(fig)

    def animate_series_partial_sums(self, geometric_partial, harmonic_partial, alternating_partial, filename, show=False):
        n_geo = np.arange(1, len(geometric_partial) + 1)
        n_har = np.arange(1, len(harmonic_partial) + 1)
        n_alt = np.arange(1, len(alternating_partial) + 1)
        frame_count = min(len(geometric_partial), len(harmonic_partial), len(alternating_partial))

        fig, axes = plt.subplots(1, 3, figsize=(16, 5), dpi=self.dpi)
        titles = ["Geometric", "Harmonic", "Alternating"]
        data = [geometric_partial, harmonic_partial, alternating_partial]
        x_data = [n_geo, n_har, n_alt]
        colors = ["#1d4ed8", "#dc2626", "#0f766e"]

        lines = []
        for ax, title, y_data, x_vals, color in zip(axes, titles, data, x_data, colors):
            line, = ax.plot([], [], color=color, linewidth=2)
            lines.append(line)
            ax.set_title(f"{title} partial sums")
            ax.set_xlabel("n")
            ax.set_ylabel("S_n")
            ax.set_xlim(1, len(y_data))
            ax.set_ylim(np.min(y_data) * 0.95, np.max(y_data) * 1.05)
            ax.grid(True, alpha=0.3)

        def update(frame_index):
            idx = frame_index + 1
            for line, x_vals, y_vals in zip(lines, x_data, data):
                line.set_data(x_vals[:idx], y_vals[:idx])
            return tuple(lines)

        anim = FuncAnimation(fig, update, frames=frame_count, interval=1000 / self.fps, blit=True)
        self._save_animation_html(anim, filename, "Series partial sums animation")

        if show:
            plt.show(block=True)
        plt.close(fig)
