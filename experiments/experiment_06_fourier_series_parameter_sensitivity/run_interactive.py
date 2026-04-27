"""Interactive launcher for Experiment 06."""

from main import run_experiment


if __name__ == "__main__":
    print("=" * 80)
    print("INTERACTIVE MODE: Experiment 06 Fourier series parameter sensitivity")
    print("=" * 80)
    print("Close each plot window to continue.")
    run_experiment(show_progress=True, show_plots=True)
