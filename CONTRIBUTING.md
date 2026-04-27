# Contributing Guide

Thank you for contributing to Walter Bishop Labs: Calculus Experiments.

This project is a calculus lab built around six experiments, with the strongest focus on correctness, clarity, reproducibility, and interpretation. If you are changing code or documentation, the goal is to keep the math trustworthy and the explanations easy to follow.

## What I’m Looking For

High-value contributions usually fall into one of these areas:

- Math correctness fixes in symbolic analysis, integration, optimization, or Fourier logic
- Better error handling, validation, and failure messages
- Test hardening and regression coverage
- Plot or animation improvements that make behavior easier to read
- Clearer educational documentation and explanations
- Reproducibility improvements, especially around settings and deterministic output

## What Is Out of Scope

Please avoid PRs that introduce unrelated framework migrations, rename stable runtime packages that other modules already import, or add large generated artifacts unless they are specifically needed as teaching evidence.

New experiment families are also out of scope unless we agree on that direction first. Small extensions within the existing six experiments are fine when they fit the current structure.

## Before You Edit

A good starting path is:

1. Read [README.md](README.md)
2. Check [experiment_structure.md](experiment_structure.md)
3. Review [docs/documentation_standards.md](docs/documentation_standards.md)
4. Open the experiment-level README for the area you are changing
5. Skim any related test files before making behavior changes

The main areas of the repo are:

- [experiments/experiment_01_function_behavior_analysis/](experiments/experiment_01_function_behavior_analysis/)
- [experiments/experiment_02_optimisation_and_sensitivity_analysis/](experiments/experiment_02_optimisation_and_sensitivity_analysis/)
- [experiments/experiment_03_integral_calculus/](experiments/experiment_03_integral_calculus/)
- [experiments/experiment_04_fourier_series_reconstruction/](experiments/experiment_04_fourier_series_reconstruction/)
- [experiments/experiment_05_series_sequence_convergence_applications/](experiments/experiment_05_series_sequence_convergence_applications/)
- [experiments/experiment_06_fourier_series_parameter_sensitivity/](experiments/experiment_06_fourier_series_parameter_sensitivity/)
- [tests/](tests/)
- [docs/](docs/)

## Development Setup

Use Python 3.10+ if possible. If you want to render plots interactively, a local desktop environment is the easiest setup.

Install dependencies from the repository root:

```bash
python -m pip install -r requirements.txt
```

## Running And Validating

Use repository-root commands when possible.

Run an experiment bundle via the root script:

```bash
# Run Experiment 01
python run_experiments.py --exp 1

# Run Experiment 02
python run_experiments.py --exp 2

# Run both (01 and 02)
python run_experiments.py --exp both

# Run all experiments (01 to 06)
python run_experiments.py --exp all

# Run validation only (no plots)
python run_experiments.py --validate
```

Run any experiment via direct entry from its own folder:

```bash
python experiments/experiment_03_integral_calculus/main.py
python experiments/experiment_04_fourier_series_reconstruction/main.py
python experiments/experiment_05_series_sequence_convergence_applications/main.py
python experiments/experiment_06_fourier_series_parameter_sensitivity/main.py
```

Before opening a PR, run the validation script and smoke tests:

```bash
python validate_experiments.py
pytest -q
```

## Coding And Design Conventions

Keep Python code small, readable, and focused. Prefer clear names over clever ones, avoid hidden side effects, and respect the existing folder responsibilities: calculus logic in `calculus/`, optimization in `optimization/`, analysis in `analysis/`, visualization in `visualization/`, and reporting in `reporting/`.

For reproducibility, respect each experiment’s settings file, avoid unseeded randomness, and keep dependency versions stable unless there is a clear reason to change them. Generated outputs belong under `outputs/plots/` and `outputs/reports/`; do not commit them by default.

## Documentation Expectations

Documentation is part of the deliverable. If behavior changes, update the relevant docs in the same PR.

At minimum, review and update the experiment-level `README.md`, `understanding.md` when interpretation changes, and `docs/documentation_standards.md` if the documentation pattern itself changes.

Each experiment README should still answer five things quickly: what the experiment does, how to run it, how to verify it, what output to expect, and what to do when something fails.

Use the narrative term “optimisation” in documentation text, but keep runtime package names unchanged when other imports depend on them.

## Branches, Commits, And PRs

Use descriptive branch names like `fix/exp04-harmonic-plot-labels`, `docs/readme-clarity-update`, or `test/exp01-regression-case`.

Keep commits focused and imperative, for example: `Fix constrained optimizer boundary selection` or `Add smoke test for symbolic candidate filtering`.

Before requesting review, confirm that the change stayed focused, validation and tests pass, behavior changes are covered by a relevant test update, docs were updated where needed, and no unnecessary generated artifacts were added.

A strong PR description should include a short summary, the scope, validation run, behavior changes, documentation updates, and any follow-up risks.

## Review Priorities

Reviewers should prioritize mathematical correctness first, then reproducibility, then interpretability of outputs, and finally visual polish. Clear educational value and traceability from math to result matter more than cosmetic changes.

## Reporting Issues

When opening an issue, include a short summary, steps to reproduce, expected result, actual result, relevant environment details, and a minimal code snippet or traceback if available. For optimization or sensitivity issues, include bounds, direction, and perturbation settings.

## Safety Notes

Do not commit secrets or machine-specific credentials. Keep paths and examples portable. Prefer repository-root commands in docs to reduce environment-specific failures.

## Thank You

Contributions that improve conceptual clarity and mathematical reliability are especially valuable here.
