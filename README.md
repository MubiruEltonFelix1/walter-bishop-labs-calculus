# Walter Bishop Labs: Calculus Experiments

Calculus can feel like a wall of symbols until you see it moving, reacting, and making decisions in real systems.

That is exactly why I built this repository.
I wanted to stop treating calculus as "notes for exams" and start using it like an engineering tool: something you can test, visualize, challenge, and trust.

## Why Calculus Still Matters

If you use modern technology, you are already surrounded by calculus.

- Machine learning: training models is optimization, and optimization is calculus in action.
- Robotics and control systems: derivatives describe motion, velocity, and stability.
- Computer graphics and simulation: smooth curves, gradients, and dynamic systems depend on calculus.
- Economics and operations: marginal change, cost optimization, and sensitivity analysis are calculus questions.
- Product and business decisions: "what happens if this input changes a little?" is fundamentally a derivative mindset.

So this repo is not about old math for old classrooms. It is about the mathematical engine behind modern decision systems.

## Why I Run Experiments Instead of Just Solving Equations

In class, we often see the final result first.
In real work, we care about the process and reliability of that result.

This project turns calculus into an experimental workflow:

1. Start with a function and assumptions.
2. Derive symbolic truths (exact derivatives, critical points, constraints).
3. Probe behavior numerically across ranges.
4. Visualize what the equations are really saying.
5. Check robustness when assumptions shift.
6. Convert math into decisions and interpretation.

The goal is to answer not just "what is the answer?" but also:

- Why does this answer happen?
- When does this answer fail?
- How much should I trust this operating point?

## Are These Experiments Only Academic?

No. They are academic in foundation, but practical in purpose.

What these experiments train directly:

- Turning abstract derivatives into explainable behavior.
- Comparing symbolic and numerical methods like a real analysis pipeline.
- Making optimization choices under constraints.
- Stress-testing recommendations through sensitivity and robustness checks.
- Writing results in a way a lecturer, teammate, or reviewer can audit.

This is the same mindset used in analytics, ML tuning, engineering optimization, and quantitative modeling.

## What Makes This Repository Different

Many calculus examples online are "single-shot": compute answer, move on.

This repository is deliberately different:

- It is experiment-driven, not answer-driven.
- It combines symbolic math and numerical evidence in one workflow.
- It prioritizes interpretation, not only correctness.
- It includes structured documentation and validation, not just scripts.
- It is built in a student voice, but organized for serious technical readers.

In short: this repo treats calculus as a lab, not a checklist.

## Current Scope

I currently focus on three connected experiments:

1. Function behavior analysis (single-variable foundations).
2. Optimization and sensitivity analysis (decision-focused calculus).
3. Integral calculus for modern accumulation problems (rate-to-total systems, numerical reliability, and applied interpretation).

The sequence is intentional: local change -> optimal decision points -> accumulated system impact.

## Repository Layout

Main experiment folders:

- [experiments/experiment_01_function_behavior_analysis](experiments/experiment_01_function_behavior_analysis)
  - Deep dive into one function using derivatives and visual behavior.
- [experiments/experiment_02_optimisation_and_sensitivity_analysis](experiments/experiment_02_optimisation_and_sensitivity_analysis)
  - Extends analysis into optimization, constraints, and robustness.
- [experiments/experiment_03_integral_calculus](experiments/experiment_03_integral_calculus)
  - Reframes integration as a modern applied experiment for estimating totals from sampled or modelled rate signals.

Useful root-level guides:

- [README.md](README.md)
- [experiment_structure.md](experiment_structure.md)
- [BRIDGE_EXPERIMENTS_01_TO_02.md](BRIDGE_EXPERIMENTS_01_TO_02.md)

Recommended read path:

1. [README.md](README.md)
2. [experiment_structure.md](experiment_structure.md)
3. [BRIDGE_EXPERIMENTS_01_TO_02.md](BRIDGE_EXPERIMENTS_01_TO_02.md)
4. [experiments/experiment_01_function_behavior_analysis/README.md](experiments/experiment_01_function_behavior_analysis/README.md)
5. [experiments/experiment_02_optimisation_and_sensitivity_analysis/README.md](experiments/experiment_02_optimisation_and_sensitivity_analysis/README.md)
6. [experiments/experiment_03_integral_calculus/README.md](experiments/experiment_03_integral_calculus/README.md)

## Quick Start

```bash
python -m pip install -r requirements.txt
python run_experiments.py --exp 1
```

Run Experiment 02:

```bash
python run_experiments.py --exp 2
```

Run Experiment 03 (direct experiment entry):

```bash
python experiments/experiment_03_integral_calculus/main.py
```

Run both experiments:

```bash
python run_experiments.py --exp both
```

Run validation only (no plots):

```bash
python run_experiments.py --validate
```

All commands are run from repository root.

## Technical Approach

I intentionally combine:

- Symbolic computation (SymPy): exact derivatives, exact candidate discovery, transparent algebra.
- Numerical computation (NumPy/Matplotlib): sampling, plotting, behavior verification, and visual intuition.

This hybrid method avoids two common traps:

- Pure symbolic work that is hard to intuit.
- Pure numerical work that is hard to justify mathematically.

## Learning Outcomes I Target

After running these experiments, I should be able to:

1. Interpret $f'(x)$ and $f''(x)$ computationally and geometrically.
2. Link critical points to actual curve behavior and decision implications.
3. Compare optimization methods and explain trade-offs clearly.
4. Discuss sensitivity and robustness in plain, practical language.
5. Produce reports that are mathematically sound and readable.

## Quality and Limitations

This project prioritizes conceptual clarity first, then engineering maturity.

Current limitations:

- Mostly 1D objective-function focus.
- Some assumptions may not generalize to non-smooth functions.
- Certain parameter choices are still manually tuned.
- Reporting and test depth are improving, but not exhaustive yet.

These limitations are documented so scope and confidence are explicit.

## Contributing

Contributions are welcome if they improve:

- calculus interpretation and clarity
- mathematical or code correctness
- output explainability and reproducibility

Please keep contributions educational, practical, and technically grounded.

## License

This repository uses the MIT License. See [LICENSE](LICENSE).
