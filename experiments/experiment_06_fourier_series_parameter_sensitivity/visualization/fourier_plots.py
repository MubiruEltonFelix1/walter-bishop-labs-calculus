"""Plotting and animation helpers for Experiment 06."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


class FourierSensitivityVisualizer:
    """Create static and animated Fourier sensitivity figures."""

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

    def plot_waveform_family(self, x, waveforms_by_label, title, filename, show=False):
        fig, ax = plt.subplots(figsize=self.figsize, dpi=self.dpi)

        for label, waveform in waveforms_by_label.items():
            ax.plot(x, waveform, linewidth=2.0, label=label)

        ax.set_title(title, fontsize=13, fontweight="bold")
        ax.set_xlabel("x (radians)")
        ax.set_ylabel("Signal amplitude")
        ax.grid(True, alpha=0.3)
        ax.legend(frameon=False, ncol=2)
        ax.margins(x=0.01)
        fig.tight_layout()
        fig.savefig(filename, dpi=self.dpi, bbox_inches="tight")
        if show:
            plt.show(block=True)
        plt.close(fig)

    def plot_reconstruction_comparison(self, x, y_true, reconstructions, title, filename, show=False):
        fig, ax = plt.subplots(figsize=self.figsize, dpi=self.dpi)
        ax.plot(x, y_true, color="black", linewidth=2.4, label="True signal")

        for n_terms, y_hat in reconstructions.items():
            ax.plot(x, y_hat, linewidth=1.4, alpha=0.92, label=f"N = {n_terms}")

        ax.set_title(title, fontsize=13, fontweight="bold")
        ax.set_xlabel("x (radians)")
        ax.set_ylabel("Signal amplitude")
        ax.grid(True, alpha=0.3)
        ax.legend(ncol=2, frameon=False)
        ax.margins(x=0.01)
        fig.tight_layout()
        fig.savefig(filename, dpi=self.dpi, bbox_inches="tight")
        if show:
            plt.show(block=True)
        plt.close(fig)

    def plot_spectrum(self, magnitudes, title, filename, show=False):
        harmonic_indices = np.arange(1, len(magnitudes) + 1)

        fig, ax = plt.subplots(figsize=self.figsize, dpi=self.dpi)
        ax.stem(harmonic_indices, magnitudes, basefmt=" ")
        ax.set_title(title, fontsize=13, fontweight="bold")
        ax.set_xlabel("Harmonic n")
        ax.set_ylabel("Coefficient magnitude")
        ax.grid(True, alpha=0.3)
        ax.margins(x=0.01)
        fig.tight_layout()
        fig.savefig(filename, dpi=self.dpi, bbox_inches="tight")
        if show:
            plt.show(block=True)
        plt.close(fig)

    def plot_coefficient_scaling(self, amplitudes, coefficient_sets, title, filename, show=False):
        harmonic_count = len(next(iter(coefficient_sets.values()))["an"])
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=self.figsize, dpi=self.dpi, sharex=True)

        a0_values = [coefficient_sets[amp]["a0"] for amp in amplitudes]
        ax1.plot(amplitudes, a0_values, marker="o", linewidth=2.2, color="#0f766e")
        ax1.set_ylabel("a0")
        ax1.set_title(title, fontsize=13, fontweight="bold")
        ax1.grid(True, alpha=0.3)

        for harmonic_index in range(min(8, harmonic_count)):
            values = [coefficient_sets[amp]["magnitudes"][harmonic_index] for amp in amplitudes]
            ax2.plot(amplitudes, values, marker="o", linewidth=1.8, label=f"n = {harmonic_index + 1}")

        ax2.set_xlabel("Amplitude scale")
        ax2.set_ylabel("Harmonic magnitude")
        ax2.grid(True, alpha=0.3)
        ax2.legend(frameon=False, ncol=2, title="First harmonics")

        fig.tight_layout()
        fig.savefig(filename, dpi=self.dpi, bbox_inches="tight")
        if show:
            plt.show(block=True)
        plt.close(fig)

    def plot_error_decay(self, harmonic_counts, metrics_by_amplitude, title, filename, show=False):
        fig, ax = plt.subplots(figsize=self.figsize, dpi=self.dpi)

        for amplitude, metrics in metrics_by_amplitude.items():
            mse_values = [item["mse"] for item in metrics]
            ax.plot(harmonic_counts, mse_values, marker="o", linewidth=2.0, label=f"A = {amplitude}")

        ax.set_title(title, fontsize=13, fontweight="bold")
        ax.set_xlabel("Number of harmonics (N)")
        ax.set_ylabel("MSE")
        ax.grid(True, alpha=0.3)
        ax.legend(frameon=False, title="Amplitude")
        fig.tight_layout()
        fig.savefig(filename, dpi=self.dpi, bbox_inches="tight")
        if show:
            plt.show(block=True)
        plt.close(fig)

    def animate_amplitude_sweep(self, x, amplitude_levels, true_signal_by_amplitude, reconstructions_by_amplitude, filename, show=False):
        frame_count = len(amplitude_levels)
        fig, ax = plt.subplots(figsize=self.figsize, dpi=self.dpi)

        true_line, = ax.plot([], [], color="black", linewidth=2.4, label="True signal")
        recon_line, = ax.plot([], [], color="#dc2626", linewidth=2.0, label="Partial sum")
        info = ax.text(0.02, 0.94, "", transform=ax.transAxes, va="top", ha="left", fontsize=11)

        ax.set_xlim(x.min(), x.max())
        y_limits = []
        for signal in true_signal_by_amplitude.values():
            y_limits.extend([float(np.min(signal)), float(np.max(signal))])
        for signal in reconstructions_by_amplitude.values():
            y_limits.extend([float(np.min(signal)), float(np.max(signal))])
        y_min = min(y_limits)
        y_max = max(y_limits)
        if y_min == y_max:
            y_min -= 1.0
            y_max += 1.0
        ax.set_ylim(y_min * 1.1, y_max * 1.1)
        ax.set_title("Amplitude sweep: true signal vs reconstructed partial sum", fontsize=13, fontweight="bold")
        ax.set_xlabel("x (radians)")
        ax.set_ylabel("Signal amplitude")
        ax.grid(True, alpha=0.3)
        ax.legend(frameon=False)

        def update(frame_index):
            amplitude = amplitude_levels[frame_index]
            true_line.set_data(x, true_signal_by_amplitude[amplitude])
            recon_line.set_data(x, reconstructions_by_amplitude[amplitude])
            info.set_text(f"Amplitude = {amplitude:.2f}")
            return true_line, recon_line, info

        anim = FuncAnimation(fig, update, frames=frame_count, interval=1000 / self.fps, blit=True)
        self._save_animation_html(anim, filename, "Amplitude sweep")

        if show:
            plt.show(block=True)
        plt.close(fig)

    def animate_harmonic_build_up(self, x, y_true, reconstructions_by_terms, filename, show=False):
        harmonic_counts = list(reconstructions_by_terms.keys())
        frame_count = len(harmonic_counts)

        fig, ax = plt.subplots(figsize=self.figsize, dpi=self.dpi)
        true_line, = ax.plot(x, y_true, color="black", linewidth=2.4, label="True signal")
        recon_line, = ax.plot([], [], color="#2563eb", linewidth=2.0, label="Partial sum")
        info = ax.text(0.02, 0.94, "", transform=ax.transAxes, va="top", ha="left", fontsize=11)

        ax.set_xlim(x.min(), x.max())
        y_values = [float(np.min(y_true)), float(np.max(y_true))]
        for signal in reconstructions_by_terms.values():
            y_values.extend([float(np.min(signal)), float(np.max(signal))])
        y_min = min(y_values)
        y_max = max(y_values)
        if y_min == y_max:
            y_min -= 1.0
            y_max += 1.0
        ax.set_ylim(y_min * 1.1, y_max * 1.1)
        ax.set_title("Harmonic build-up: reconstruction improves as N increases", fontsize=13, fontweight="bold")
        ax.set_xlabel("x (radians)")
        ax.set_ylabel("Signal amplitude")
        ax.grid(True, alpha=0.3)
        ax.legend(frameon=False)

        def update(frame_index):
            n_terms = harmonic_counts[frame_index]
            recon_line.set_data(x, reconstructions_by_terms[n_terms])
            info.set_text(f"Harmonics = {n_terms}")
            return recon_line, info

        anim = FuncAnimation(fig, update, frames=frame_count, interval=1000 / self.fps, blit=True)
        self._save_animation_html(anim, filename, "Harmonic build-up")

        if show:
            plt.show(block=True)
        plt.close(fig)
