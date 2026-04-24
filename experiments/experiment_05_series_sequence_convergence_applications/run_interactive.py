"""Interactive launcher for Experiment 05."""

from main import run_experiment


if __name__ == "__main__":
    print("=" * 80)
    print("INTERACTIVE MODE: Experiment 05 convergence/divergence")
    print("=" * 80)
    print("Close each plot window to continue.")
    run_experiment(show_progress=True, show_plots=True)
