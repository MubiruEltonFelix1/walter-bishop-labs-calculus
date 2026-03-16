# Experiment 02 - Optimisation and Sensitivity Analysis

Walter Bishop Labs | Calculus Research Series  
Date: March 16, 2026  
Status: Design Complete, Implementation Pending

---

## Why This Experiment Exists

Experiment 01 answered: what is the function doing?

Experiment 02 answers: what should we do with that information?

This experiment converts derivative analysis into decision-making. It identifies optimal operating points, measures how stable those optima are under uncertainty, and compares symbolic and numerical optimisation strategies.

---

## Core Objective

Build a pipeline that takes a single-variable objective function and returns a decision-ready recommendation:

- Recommended operating point x*
- Objective value at x*
- Classification (local max, local min, flat/saddle-like behavior in 1D)
- Stability of x* under parameter perturbations
- Method comparison (symbolic solve vs numerical solvers)

---

## Key Tangible Takeaway

A practical recommendation report, not just equations and plots.

At the end of each run, the experiment should produce:

1. A best candidate operating point for the objective and constraints
2. A confidence statement on robustness under small model changes
3. A clear explanation of why the recommendation is trusted

This is directly usable in real-world contexts like pricing, process tuning, energy control, and quality optimisation.

---

## Relationship to Experiment 01

Experiment 01 delivered:

- Function behavior visualization
- First derivative and second derivative interpretation
- Critical point detection

Experiment 02 extends those results by:

- Turning critical points into actionable optimum candidates
- Validating candidates with second-derivative classification
- Adding constrained optimisation logic
- Stress-testing the recommendation using sensitivity analysis

Combined meaning:

- Experiment 01 explains behavior
- Experiment 02 supports decisions

---

## Proposed Folder Structure

This structure will be implemented tomorrow:

experiment_02_optimisation_and_sensitivity_analysis/
    main.py
    README.md
    calculus/
        function.py
        derivatives.py
        classification.py
    optimization/
        symbolic_optimizer.py
        numerical_optimizer.py
        constrained_optimizer.py
    analysis/
        sensitivity.py
        robustness.py
    visualization/
        static_plot.py
        sensitivity_plot.py
    reporting/
        summary.py

---

## Functional Requirements

### 1. Symbolic Candidate Discovery

- Compute f'(x) and solve f'(x) = 0 symbolically where possible
- Filter to real-valued candidates
- Add interval boundaries when constraints are present

### 2. Candidate Classification

- Evaluate f''(x) at each candidate
- Classify as local minimum, local maximum, or inconclusive

### 3. Numerical Optimisation

- Implement Gradient Descent baseline
- Implement Newton method baseline
- Report convergence behavior and number of iterations

### 4. Constrained Optimisation

- Support simple bounds: x in [a, b]
- Evaluate interior candidates and boundary points
- Select final recommendation by objective direction (minimise or maximise)

### 5. Sensitivity Analysis

- Perturb model parameters by configurable percentages
- Recompute optimum for each perturbation scenario
- Measure shift in x* and objective value

### 6. Robustness Scoring

- Define a scalar robustness index, for example:
  - low shift in x* and low loss degradation -> high robustness
  - high shift in x* or high loss degradation -> low robustness

### 7. Reporting

- Print a concise recommendation table
- Display method comparison metrics
- Produce at least one sensitivity visualization

---

## Non-Goals (Current Scope Limits)

- No multivariable optimisation in this experiment
- No stochastic global optimisers (genetic algorithms, simulated annealing)
- No symbolic handling for highly pathological, non-smooth objectives beyond graceful warnings
- No production API or web interface yet

---

## Known Technical Limitations to Handle Explicitly

To avoid repeating failure modes seen in Experiment 01:

1. Symbolic solver may fail for some function classes
   - Fallback path required via numerical optimisation

2. Non-differentiable objectives may produce unusable symbolic derivatives
   - Detect and return clear warnings

3. Complex critical points can appear
   - Filter non-real candidates before classification and plotting

4. Poor initial guesses can hurt numerical convergence
   - Use multiple seeds or report sensitivity to initialization

5. Domain and range settings can hide behavior
   - Add configurable plotting domain and auto-scaling helper

---

## Real-World Relevance

### A. Pricing Optimisation

- Objective: maximize profit as a function of price
- Output: recommended price and sensitivity to demand assumptions

### B. Process Engineering

- Objective: minimize waste or energy cost by tuning a process variable
- Output: recommended setpoint and robustness to parameter drift

### C. Operations Planning

- Objective: minimize time or cost under bounded resource settings
- Output: best feasible operating value and risk envelope

The same calculus machinery supports all three: derivatives identify structure, optimisation selects action, sensitivity checks reliability.

---

## Definition of Done for Implementation

Implementation is complete when all are true:

1. main.py runs end-to-end from this experiment directory
2. At least one objective is solved symbolically and numerically
3. Bound-constrained optimisation is demonstrated
4. Sensitivity analysis runs across a configurable perturbation grid
5. Console summary includes recommendation, method comparison, and robustness score
6. Plots render correctly for objective and sensitivity outputs

---

## Tomorrow Implementation Plan

### Phase 1 - Core Math

- Build function definition and derivatives modules
- Add candidate discovery and second-derivative classification

### Phase 2 - Optimisation Engines

- Add symbolic optimiser
- Add gradient descent and Newton method numerical optimiser
- Add constrained optimizer wrapper

### Phase 3 - Sensitivity and Robustness

- Implement perturbation scenarios
- Compute shift metrics and robustness index

### Phase 4 - Visual and Reporting Layer

- Objective curve with annotated optimum
- Sensitivity plot for x* shift and objective shift
- Final recommendation summary output

---

## Expected Experiment Output Format (Target)

Console output should include sections in this order:

- Objective definition
- Candidate points and classification
- Numerical method convergence summary
- Final recommended operating point
- Sensitivity and robustness summary

This output structure ensures that the mathematical reasoning is transparent from discovery to recommendation.

---

## Future Extension After Experiment 02

- Extend to multivariable objectives and gradient fields
- Add constrained multivariable optimisation (Lagrange-style and numerical)
- Add uncertainty distributions (not only fixed perturbation percentages)
- Build a reusable optimisation experiment template for future labs
