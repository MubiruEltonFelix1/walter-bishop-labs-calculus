# Contributing Guide

Thank you for contributing to Walter Bishop Labs: Calculus Experiments.

This repository is intentionally focused on two experiments:

1. Experiment 01: Function behavior analysis
2. Experiment 02: Optimisation and sensitivity analysis

The current priority is to improve correctness, clarity, reproducibility, and reporting quality inside this existing scope.

## 1. What Contributions Are Welcome

High-value contributions include:

1. Math correctness fixes in symbolic analysis and optimization logic
2. Better error handling and input validation
3. Test hardening and better failure messages
4. Plot readability improvements that increase interpretability
5. Clearer educational documentation and explanations
6. Reproducibility and deterministic behavior improvements

## 2. What Is Out of Scope (For This Branch)

Please avoid opening PRs that:

1. Add Experiment 03 or new experiment families
2. Rename stable runtime packages that are already imported (for example, `optimization/`)
3. Introduce unrelated framework migrations
4. Add large generated artifacts unless explicitly needed as teaching evidence

## 3. Repository Orientation

Recommended reading order before making changes:

1. `README.md`
2. `experiment_structure.md`
3. `BRIDGE_EXPERIMENTS_01_TO_02.md`
4. `docs/documentation_standards.md`
5. Experiment-level README for the area you are changing

Key folders:

1. `experiments/experiment_01_function_behavior_analysis/`
2. `experiments/experiment_02_optimisation_and_sensitivity_analysis/`
3. `tests/`
4. `docs/`

## 4. Development Setup

### Prerequisites

1. Python 3.10+ recommended
2. pip
3. A local desktop environment if you want to render plots interactively

### Install dependencies

From repository root:

```bash
python -m pip install -r requirements.txt
```

## 5. Running the Project

Use root commands when possible.

Run Experiment 01:

```bash
python run_experiments.py --exp 1
```

Run Experiment 02:

```bash
python run_experiments.py --exp 2
```

Run both:

```bash
python run_experiments.py --exp both
```

Run core validation only (non-plot checks):

```bash
python run_experiments.py --validate
```

If you run an experiment directly, run it from inside that experiment directory so local imports resolve as expected.

## 6. Testing and Validation Expectations

Before opening a pull request, run both validation and tests.

Validation:

```bash
python validate_experiments.py
```

Pytest smoke tests:

```bash
pytest -q
```

A contribution is considered review-ready when:

1. Validation passes
2. Smoke tests pass
3. Changed behavior is covered by at least one relevant test update
4. Any intentional behavior change is documented

## 7. Coding and Design Conventions

### General Python style

1. Follow PEP 8 and keep functions focused
2. Prefer clear names over short names
3. Keep module responsibilities narrow
4. Avoid introducing hidden side effects

### Existing architecture expectations

1. Keep calculus logic in `calculus/`
2. Keep optimization methods in `optimization/`
3. Keep sensitivity and robustness logic in `analysis/`
4. Keep rendering logic in `visualization/`
5. Keep reporting logic in `reporting/`

### Determinism and reproducibility

1. Respect experiment settings files and default run seed values
2. Do not introduce randomness without controlled seed handling
3. Keep dependency versions pinned unless there is a clear reason to update

### Output artifact policy

1. Generated outputs belong under `outputs/plots/` and `outputs/reports/`
2. Do not commit generated outputs by default
3. Commit generated outputs only when explicitly required for teaching evidence

## 8. Documentation Conventions

Documentation is part of the deliverable.

If behavior changes, update docs in the same PR.

At minimum, review and update relevant sections of:

1. Experiment-level `README.md`
2. Experiment-level `understanding.md` when interpretation changes
3. `docs/documentation_standards.md` if standards evolve

Each experiment README should continue to include:

1. Objective and scope
2. Run instructions
3. Quick verification checks
4. Expected output snapshot
5. Troubleshooting notes

Terminology note:

1. Prefer the narrative term "optimisation" in documentation text
2. Keep runtime package names unchanged when tied to imports

## 9. Branch and Commit Guidance

### Branch naming

Use descriptive branch names such as:

1. `fix/exp02-constrained-boundary-case`
2. `docs/readme-verification-clarity`
3. `test/exp01-critical-point-regression`

### Commit message style

Use focused commits with imperative messages, for example:

1. `Fix constrained optimizer boundary selection`
2. `Add smoke test for symbolic candidate filtering`
3. `Clarify experiment 02 troubleshooting notes`

## 10. Pull Request Checklist

Before requesting review, confirm all items:

1. I stayed within the two-experiment scope
2. I ran validation and pytest locally
3. I updated or added tests for behavior changes
4. I updated relevant documentation in the same PR
5. I did not commit unnecessary generated artifacts
6. I preserved naming and folder conventions
7. I kept changes focused and minimal

## 11. PR Description Template

Use this structure in your PR body:

```md
## Summary
- What changed
- Why it changed

## Scope
- Experiment(s) affected
- Modules affected

## Validation
- Commands run
- Key outputs or pass/fail summary

## Behavior Changes
- User-visible or result-visible changes

## Documentation
- Files updated

## Risks / Follow-ups
- Known limitations or next improvements
```

## 12. Review Priorities

Reviewers should prioritize:

1. Mathematical correctness over style preferences
2. Reproducibility over convenience shortcuts
3. Interpretability of outputs over visual polish alone
4. Clear educational value and traceability from math to result

## 13. Reporting Bugs or Proposing Improvements

When opening an issue, include:

1. A short problem summary
2. Steps to reproduce
3. Expected result
4. Actual result
5. Relevant environment details
6. Minimal code snippet or traceback if available

For optimization or sensitivity issues, include bounds, direction, and perturbation settings used.

## 14. Security and Safety Notes

1. Do not commit secrets or machine-specific credentials
2. Keep paths and examples portable
3. Prefer repository-root commands in docs to reduce environment-specific failures

## 15. Thank You

Contributions that improve conceptual clarity and mathematical reliability are especially valuable in this project.

If you are unsure whether a change fits scope, open an issue first and describe the intended outcome before implementing.
