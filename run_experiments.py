"""Root launcher for running experiments without manual path juggling.

Usage examples:
    python run_experiments.py --exp 1
    python run_experiments.py --exp 2
    python run_experiments.py --exp 3
    python run_experiments.py --exp 4
    python run_experiments.py --exp 5
    python run_experiments.py --exp both
    python run_experiments.py --exp all
    python run_experiments.py --validate
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXP_01_DIR = ROOT / "experiments" / "experiment_01_function_behavior_analysis"
EXP_02_DIR = ROOT / "experiments" / "experiment_02_optimisation_and_sensitivity_analysis"
EXP_03_DIR = ROOT / "experiments" / "experiment_03_integral_calculus"
EXP_04_DIR = ROOT / "experiments" / "experiment_04_fourier_series_reconstruction"
EXP_05_DIR = ROOT / "experiments" / "experiment_05_series_sequence_convergence_applications"


def run_python_script(cwd: Path, script_name: str) -> int:
    result = subprocess.run(
        [sys.executable, script_name],
        cwd=cwd,
        check=False,
    )
    return result.returncode


def run_validation() -> int:
    result = subprocess.run(
        [sys.executable, "validate_experiments.py"],
        cwd=ROOT,
        check=False,
    )
    return result.returncode


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run Walter Bishop Labs experiments from repository root."
    )
    parser.add_argument(
        "--exp",
        choices=["1", "2", "3", "4", "5", "both", "all"],
        default="both",
        help="Which experiment to run (default: both, meaning 1 and 2).",
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Run core validation checks only (no plots).",
    )
    args = parser.parse_args()

    if args.validate:
        return run_validation()

    if args.exp == "1":
        return run_python_script(EXP_01_DIR, "main.py")

    if args.exp == "2":
        return run_python_script(EXP_02_DIR, "main.py")

    if args.exp == "3":
        return run_python_script(EXP_03_DIR, "main.py")

    if args.exp == "4":
        return run_python_script(EXP_04_DIR, "main.py")

    if args.exp == "5":
        return run_python_script(EXP_05_DIR, "main.py")

    if args.exp == "all":
        for exp_dir in (EXP_01_DIR, EXP_02_DIR, EXP_03_DIR, EXP_04_DIR, EXP_05_DIR):
            exit_code = run_python_script(exp_dir, "main.py")
            if exit_code != 0:
                return exit_code
        return 0

    code_1 = run_python_script(EXP_01_DIR, "main.py")
    if code_1 != 0:
        return code_1
    return run_python_script(EXP_02_DIR, "main.py")


if __name__ == "__main__":
    raise SystemExit(main())
