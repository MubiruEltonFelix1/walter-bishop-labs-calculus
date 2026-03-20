# Changes Made on 2026-03-20

This document records the implementation pass that hardened the repository while keeping scope fixed to Experiment 01 and Experiment 02.

## 1. Repository Hygiene

- Added `.gitignore` with rules for Python cache files, virtual environments, test caches, IDE noise, and generated output artifacts.
- Added MIT `LICENSE` file at repository root.

## 2. Scope and Consistency Documentation

- Updated root `README.md` to:
  - confirm frozen two-experiment scope,
  - add a recommended reading sequence,
  - replace expansion-oriented roadmap items with hardening-oriented items,
  - reflect that a license now exists.
- Updated `experiment_structure.md` to:
  - note current frozen scope,
  - remove forward-looking Experiment 03 progression text,
  - replace "new experiment contribution" guidance with "current scope contribution" guidance.
- Added `docs/documentation_standards.md` to centralize naming, output, reporting, and reproducibility conventions.

## 3. Experiment 01 Improvements

- Added `experiments/experiment_01_function_behavior_analysis/settings.py`.
- Updated plotting modules to consume settings constants:
  - `visualization/static_plot.py`
  - `visualization/animation_plot.py`
- Updated `main.py` to set and print deterministic run seed.
- Added output folder convention scaffolding:
  - `outputs/plots/.gitkeep`
  - `outputs/reports/.gitkeep`
- Updated Experiment 01 README with:
  - quick verification checks,
  - expected output snapshot,
  - troubleshooting section,
  - wording aligned to hardening-first scope.

## 4. Experiment 02 Improvements

- Added `experiments/experiment_02_optimisation_and_sensitivity_analysis/settings.py`.
- Updated `main.py` to use settings constants for:
  - bounds,
  - direction,
  - perturbation grid,
  - numerical seed point,
  - plot domain,
  - deterministic run seed.
- Added automatic artifact export in Experiment 02 run:
  - objective plot to `outputs/plots/objective_plot.png`
  - sensitivity plot to `outputs/plots/sensitivity_plot.png`
  - recommendation report to `outputs/reports/summary_report.txt`
- Updated visualization functions to support optional `save_path`:
  - `visualization/static_plot.py`
  - `visualization/sensitivity_plot.py`
- Refactored reporting module:
  - `reporting/summary.py` now returns report text from `print_summary(...)`
  - added `save_summary_report(...)` for file output
- Updated sensitivity module to source perturbation grid from settings.
- Added output folder convention scaffolding:
  - `outputs/plots/.gitkeep`
  - `outputs/reports/.gitkeep`
- Updated Experiment 02 README to:
  - move status from pending to implemented,
  - switch from planned to implemented language,
  - add run instructions,
  - add quick verification checks,
  - add expected output snapshot,
  - add troubleshooting section.

## 5. Reproducibility and Test Coverage

- Pinned dependency versions in `requirements.txt`.
- Added minimal smoke tests:
  - `tests/test_experiment_01_smoke.py`
  - `tests/test_experiment_02_smoke.py`
- Added `validate_experiments.py` for quick non-plot core validation.

## 6. Notes

- No new experiments were added.
- Existing experiment architecture was preserved.
- Changes focused on maintainability, reproducibility, documentation quality, and confidence checks.
