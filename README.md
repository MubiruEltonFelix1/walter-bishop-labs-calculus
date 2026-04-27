# 🧪 Walter Bishop Labs: Calculus Experiments

> *"Calculus is not a subject you learn. It is a tool you develop."*

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![SymPy](https://img.shields.io/badge/SymPy-Symbolic%20Math-8B2BE2?style=flat-square&logo=sympy&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Numerical-013243?style=flat-square&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![Experiments](https://img.shields.io/badge/Experiments-6-orange?style=flat-square)

---

Calculus can feel like a wall of symbols until you see it moving, reacting, and making decisions in real systems.

That is exactly why I built this repository.
I wanted to stop treating calculus as *"notes for exams"* and start using it like an engineering tool: something you can test, visualize, challenge, and trust.

---

## Why Calculus Still Matters

If you use modern technology, you are already surrounded by calculus.

- **Machine learning** — training models is optimization, and optimization is calculus in action.
- **Robotics and control systems** — derivatives describe motion, velocity, and stability.
- **Computer graphics and simulation** — smooth curves, gradients, and dynamic systems depend on calculus.
- **Economics and operations** — marginal change, cost optimization, and sensitivity analysis are calculus questions.
- **Product and business decisions** — *"what happens if this input changes a little?"* is fundamentally a derivative mindset.

So this repo is not about old math for old classrooms. It is about the mathematical engine behind modern decision systems.

---

## Why I Run Experiments Instead of Just Solving Equations

In class, we often see the final result first.
In real work, we care about the *process* and *reliability* of that result.

This project turns calculus into an experimental workflow:

1. Start with a function and assumptions.
2. Derive symbolic truths (exact derivatives, critical points, constraints).
3. Probe behavior numerically across ranges.
4. Visualize what the equations are really saying.
5. Check robustness when assumptions shift.
6. Convert math into decisions and interpretation.

The goal is to answer not just *"what is the answer?"* but also:

- Why does this answer happen?
- When does this answer fail?
- How much should I trust this operating point?

---

## Are These Experiments Only Academic?

No. They are academic in foundation, but practical in purpose.

What these experiments train directly:

- Turning abstract derivatives into explainable behavior.
- Comparing symbolic and numerical methods like a real analysis pipeline.
- Making optimization choices under constraints.
- Stress-testing recommendations through sensitivity and robustness checks.
- Writing results in a way a lecturer, teammate, or reviewer can audit.

This is the same mindset used in analytics, ML tuning, engineering optimization, and quantitative modeling.

---

## What Makes This Repository Different

Many calculus examples online are *"single-shot"*: compute answer, move on.

This repository is deliberately different:

| Principle | What it means |
|---|---|
| Experiment-driven | Not answer-driven — the process is the product |
| Hybrid methods | Symbolic math and numerical evidence in one workflow |
| Interpretation-first | Results explained, not just computed |
| Structured documentation | Validation and writeups, not just scripts |
| Student voice | Built accessibly, organized for serious technical readers |

In short: this repo treats calculus as a lab, not a checklist.

---

## Experiments

> The sequence is intentional: **local change → optimal decision points → accumulated system impact**

| # | Experiment | Focus |
|---|---|---|
| 01 | [Function Behavior Analysis](experiments/experiment_01_function_behavior_analysis) | Deep dive into one function using derivatives and visual behavior |
| 02 | [Optimisation and Sensitivity Analysis](experiments/experiment_02_optimisation_and_sensitivity_analysis) | Extends analysis into optimization, constraints, and robustness |
| 03 | [Integral Calculus](experiments/experiment_03_integral_calculus) | Integration as a modern applied experiment for estimating totals from sampled or modelled rate signals |
| 04 | [Fourier Series Reconstruction](experiments/experiment_04_fourier_series_reconstruction) | Reconstructs periodic signals using Fourier partial sums and tracks approximation quality |
| 05 | [Series and Sequence Convergence Applications](experiments/experiment_05_series_sequence_convergence_applications) | Practical convergence/divergence analysis with recursive systems, partial sums, and animated behavior |
| 06 | [Fourier Series Parameter Sensitivity](experiments/experiment_06_fourier_series_parameter_sensitivity) | Studies Fourier series coefficient scaling, amplitude changes, and harmonic-count sensitivity through graphs and animations |

---

## Repository Layout

```
.
├── README.md
├── experiment_structure.md
├── BRIDGE_EXPERIMENTS_01_TO_02.md
├── run_experiments.py
├── requirements.txt
└── experiments/
    ├── experiment_01_function_behavior_analysis/
    ├── experiment_02_optimisation_and_sensitivity_analysis/
    ├── experiment_03_integral_calculus/
    ├── experiment_04_fourier_series_reconstruction/
    ├── experiment_05_series_sequence_convergence_applications/
    └── experiment_06_fourier_series_parameter_sensitivity/
```

**Recommended read path:**

1. [README.md](README.md)
2. [experiment_structure.md](experiment_structure.md)
3. [BRIDGE_EXPERIMENTS_01_TO_02.md](BRIDGE_EXPERIMENTS_01_TO_02.md)
4. [Experiment 01 README](experiments/experiment_01_function_behavior_analysis/README.md)
5. [Experiment 02 README](experiments/experiment_02_optimisation_and_sensitivity_analysis/README.md)
6. [Experiment 03 README](experiments/experiment_03_integral_calculus/README.md)
7. [Experiment 04 README](experiments/experiment_04_fourier_series_reconstruction/README.md)
8. [Experiment 05 README](experiments/experiment_05_series_sequence_convergence_applications/README.md)
9. [Experiment 06 README](experiments/experiment_06_fourier_series_parameter_sensitivity/README.md)

---

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run Experiment 01
python run_experiments.py --exp 1

# Run Experiment 02
python run_experiments.py --exp 2

# Run Experiment 03 (direct entry)
python experiments/experiment_03_integral_calculus/main.py

# Run Experiment 04 (direct entry)
python experiments/experiment_04_fourier_series_reconstruction/main.py

# Run Experiment 05 (direct entry)
python experiments/experiment_05_series_sequence_convergence_applications/main.py

# Run Experiment 06 (direct entry)
python experiments/experiment_06_fourier_series_parameter_sensitivity/main.py

# Run both (01 and 02)
python run_experiments.py --exp both

# Run all experiments (01 to 06)
python run_experiments.py --exp all

# Run validation only (no plots)
python run_experiments.py --validate
```

> All commands are run from the repository root.

---

## Technical Approach

This project intentionally combines two complementary methods:

| Method | Tool | Purpose |
|---|---|---|
| Symbolic computation | SymPy | Exact derivatives, candidate discovery, transparent algebra |
| Numerical computation | NumPy / Matplotlib | Sampling, plotting, behavior verification, and visual intuition |

This hybrid approach avoids two common traps:

- **Pure symbolic work** that is hard to intuit.
- **Pure numerical work** that is hard to justify mathematically.

---

## Learning Outcomes

After running these experiments, I should be able to:

1. Interpret $f'(x)$ and $f''(x)$ computationally and geometrically.
2. Link critical points to actual curve behavior and decision implications.
3. Compare optimization methods and explain trade-offs clearly.
4. Discuss sensitivity and robustness in plain, practical language.
5. Produce reports that are mathematically sound and readable.

---

## Quality and Limitations

This project prioritizes **conceptual clarity first**, then engineering maturity.

Current limitations (explicitly documented so scope and confidence are clear):

- Mostly 1D objective-function focus.
- Some assumptions may not generalize to non-smooth functions.
- Certain parameter choices are still manually tuned.
- Reporting and test depth are improving, but not exhaustive yet.

---

## Contributing

Contributions are welcome if they improve:

- Calculus interpretation and clarity
- Mathematical or code correctness
- Output explainability and reproducibility

Please keep contributions **educational, practical, and technically grounded**.

---

## License

This repository uses the **MIT License**. See [LICENSE](LICENSE).

---

<p align="center">Built with curiosity. Verified with evidence. Explained with intention.</p>
