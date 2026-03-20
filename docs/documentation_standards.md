# Documentation Standards

This file defines shared standards for the two existing experiments.

## Scope

- Repository scope is frozen to Experiment 01 and Experiment 02.
- Improvements focus on correctness, reproducibility, readability, and reporting quality.

## Naming and Terminology

- Prefer the narrative term "optimisation" in documentation text.
- Keep existing code/package names unchanged when they are already part of runtime imports (for example, the `optimization/` package).
- Use snake_case for Python modules and folders.

## Output Conventions

Each experiment keeps generated artifacts under:

- `outputs/plots/` for image files
- `outputs/reports/` for text summaries

Generated artifacts should not be committed unless explicitly needed for teaching evidence.

## Reporting Style

Every experiment-level README should include:

1. Objective and scope
2. Run instructions
3. Quick verification checks
4. Expected output snapshot
5. Troubleshooting notes

## Reproducibility

- Keep a fixed run seed (`RUN_SEED = 42`) in experiment settings, even if current logic is deterministic.
- Pin dependency versions in `requirements.txt`.
- Include smoke tests for key math outputs.
