# Experiment Structure — Walter Bishop Labs

This document explains how experiments in this repository are designed, what each part of the folder structure does, and what conventions every experiment follows. Read this before contributing, before running a new experiment, or before building one from scratch.

---

## The Philosophy

Each experiment is a self-contained investigation. It takes a mathematical concept, expresses it computationally with exact symbolic tools, evaluates it numerically at scale, renders its behavior visually, and then explains what the output means. The goal is never just to produce a correct number — it is to expose why the behavior happens.

Every experiment moves through the same four stages:

```
Define  →  Analyze  →  Visualize  →  Understand
```

The code implements the first three. The `understanding.md` document inside each experiment closes the loop on the fourth.

---

## Top-Level Repository Layout

```
walter-bishop-labs-calculus/
│
├── README.md                    ← Project overview and research direction
├── experiment_structure.md      ← This document — how experiments are built (you are here)
├── requirements.txt             ← All Python dependencies for the full lab
│
└── experiments/
    ├── experiment_01_.../       ← First complete experiment
    ├── experiment_02_.../       ← Second experiment (and so on)
    └── ...
```

Experiments are numbered sequentially and named descriptively. The number reflects the order in which concepts build on each other. Later experiments depend on intuition established in earlier ones.

---

## Inside a Single Experiment

Every experiment follows this internal structure:

```
experiment_NN_descriptive_name/
│
├── main.py                      ← Single entry point — runs the full experiment
├── README.md                    ← What was built, why, and how to run it
├── understanding.md             ← What the output means (post-experiment explanation)
│
├── calculus/                    ← All mathematical computation lives here
│   ├── function.py              ← The experimental function definition
│   ├── derivatives.py           ← Symbolic differentiation via SymPy
│   ├── analysis.py              ← Critical points, classification, and derived insights
│   └── __init__.py              ← (if needed for package resolution)
│
├── visualization/               ← All graphical rendering lives here
│   ├── static_plot.py           ← Fixed plot showing the full picture
│   ├── animation_plot.py        ← Animated or dynamic view of the same data
│   └── __init__.py              ← (if needed for package resolution)
│
└── (additional modules as needed per experiment)
    ├── optimization/            ← e.g. Experiment 02 adds this layer
    ├── analysis/
    └── reporting/
```

Experiments may add subdirectories beyond `calculus/` and `visualization/` as their scope grows. The base structure above is the minimum required for every experiment.

---

## What Each File Does

### `main.py`
The single entry point. It imports from all other modules and orchestrates the full experiment pipeline in order: define → analyze → print results → visualize. It should not contain mathematical logic itself — that belongs in `calculus/`. Running this file should execute the complete experiment from start to finish.

```bash
cd experiments/experiment_NN_name
python main.py
```

### `README.md`
Written before or during implementation. It records:
- What the experiment is designed to investigate
- What was implemented and how each module works
- What dependencies are required
- How to run the experiment
- Known limitations and edge cases encountered

The README is a technical record of intent and implementation. It is not an explanation of mathematical meaning — that is the job of `understanding.md`.

### `understanding.md`
Written after the experiment is complete and the output has been observed. It records:
- What the libraries used actually do and why they were chosen
- What every element of every graph shows and how to read it
- The deep meaning of each mathematical object computed
- Intuitions and principles extracted from the results
- Specific takeaways that carry forward into the next experiment

This document is aimed at someone who has run the experiment and seen the output but wants to genuinely understand what they saw. It builds the mental model that the code alone cannot provide.

### `calculus/function.py`
Defines the experimental function `f(x)`. The function must be written to accept both a SymPy symbol (for symbolic operations) and a NumPy array (for numerical plotting) without branching — this is achieved by writing it using only operations that both libraries support (standard arithmetic, power operators). If the function requires non-algebraic operations (floor, abs, conditional logic), an `isinstance(x, sp.Basic)` branch is required.

### `calculus/derivatives.py`
Computes symbolic derivatives using SymPy at module load time. The first and second derivatives are stored as module-level variables and exported. This module is the source of truth for all exact mathematical expressions used in the experiment.

### `calculus/analysis.py`
Applies the derivatives to extract analytical conclusions: critical points via `sp.solve`, classification via second derivative evaluation, inflection points, and any other structural analysis relevant to the experiment. This module converts symbolic expressions into interpretable mathematical facts.

### `visualization/static_plot.py`
Renders a fixed, complete view of the experiment's mathematical objects. Bridges the symbolic world and the numerical world using `sp.lambdify` to convert SymPy expressions to NumPy-callable functions. The static plot is the primary reference graphic for the experiment.

### `visualization/animation_plot.py`
Renders a dynamic or progressive view of the same material. Animations are used to show processes rather than snapshots — tracing a curve, following a tangent line, stepping through gradient descent, propagating a solution through time. The animation should reinforce something that the static plot cannot convey alone.

---

## The Two-Library Convention

All experiments use the same two-library architecture for mathematical computation:

| Library | Role | When it is used |
|---|---|---|
| **SymPy** | Symbolic — exact algebra and calculus | Differentiation, solving equations, exact values |
| **NumPy** | Numerical — array computation at scale | Generating x-values, evaluating for plotting |

The bridge between them is always `sp.lambdify(symbol, expression, 'numpy')`, which converts a SymPy expression into a function that NumPy arrays can be passed to directly.

**SymPy provides the truth. NumPy renders it.**

Neither library alone is sufficient for an experiment in this lab.

---

## The Three-Document Lifecycle

Every experiment produces three documents that together form a complete record:

| Document | Written when | Purpose |
|---|---|---|
| `README.md` | During or immediately after implementation | Technical record of what was built |
| `understanding.md` | After running and observing the output | Mathematical and conceptual interpretation |
| Code itself | During implementation | The executable, reproducible implementation |

A finished experiment has all three. An experiment without `understanding.md` is incomplete regardless of whether the code runs correctly.

---

## Experiment Numbering and Dependency

Experiments are ordered so that each one builds on the conceptual foundation of the ones before it:

```
Experiment 01 — establishes what a function is doing (behavior analysis)
Experiment 02 — establishes what to do with that information (optimization)
Experiment 03 — generalizes the domain (multivariable, integration)
...
```

If an experiment references a concept or uses a module from a previous experiment, this dependency is noted in the README. Contributors should read the understanding documents of dependency experiments before working on a later one.

---

## How to Run Any Experiment

1. Install dependencies from the root of the repository:

```bash
pip install -r requirements.txt
```

2. Navigate into the specific experiment directory:

```bash
cd experiments/experiment_NN_name
```

3. Run the entry point:

```bash
python main.py
```

Experiments must be run from inside their own directory. Relative imports in the `calculus/` and `visualization/` packages depend on this.

---

## How to Contribute a New Experiment

1. Create a new directory under `experiments/` following the naming convention: `experiment_NN_descriptive_name/`
2. Build the structure described above — at minimum `main.py`, `README.md`, `calculus/`, and `visualization/`
3. Define the experimental function in `calculus/function.py` using the dual-compatible pattern
4. Implement symbolic analysis in `calculus/derivatives.py` and `calculus/analysis.py`
5. Implement a static plot and, where meaningful, an animated plot in `visualization/`
6. Write `main.py` to orchestrate all modules in sequence
7. Write `README.md` to record what was implemented and why
8. Run the experiment, observe the output, and write `understanding.md` to close the loop

Do not submit an experiment without `understanding.md`. The purpose of this lab is not to produce running code — it is to produce understanding.

---

## Naming Conventions

| Item | Convention | Example |
|---|---|---|
| Experiment directory | `experiment_NN_snake_case_name` | `experiment_01_function_behavior_analysis` |
| Python modules | `snake_case.py` | `static_plot.py`, `sensitivity.py` |
| Subdirectories | `snake_case/` | `calculus/`, `visualization/`, `optimization/` |
| The function | Always named `f` in `function.py` | `def f(x):` |
| Symbolic variable | Always `x = sp.symbols('x')` in `derivatives.py` | — |
| Derivative variables | `first_derivative`, `second_derivative` | — |

Consistency in naming makes it possible to drop into any experiment and orient immediately.
