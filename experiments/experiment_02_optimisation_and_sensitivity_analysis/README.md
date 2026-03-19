# Experiment 02 - Optimisation and Sensitivity Analysis

Walter Bishop Labs  
Date: March 16, 2026  
Status: Design Complete, Implementation Pending

---

## Why I Made This Experiment

Experiment 01 helped me answer: "What is this function doing?"

In Experiment 02, I want to answer: "What should I do with that information?"

So this experiment is about decision-making with calculus:
- find good candidate points
- choose the best feasible point
- check how stable that decision is if assumptions change

---

## My Main Goal

I want one run of this experiment to return a practical recommendation, not just equations.

Target outputs:
- recommended operating point $x^*$
- objective value at $x^*$
- classification (local min/local max/inconclusive)
- sensitivity of $x^*$ to parameter changes
- method comparison (symbolic vs numerical)

---

## How It Connects to Experiment 01

Experiment 01 gave me:
- derivative analysis
- critical point detection
- visual intuition

Experiment 02 builds on that by adding:
- optimization logic
- constraints
- sensitivity analysis
- robustness scoring

In short:
- Experiment 01 explains behavior
- Experiment 02 supports decisions

---

## Planned Structure

```text
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
```

---

## Functional Targets

### 1. Symbolic Candidate Discovery
- Solve $f'(x)=0$ where possible
- Keep only real candidates
- Include interval boundaries if constraints exist

### 2. Candidate Classification
- Evaluate $f''(x)$ at each candidate
- Label as local minimum, local maximum, or inconclusive

### 3. Numerical Optimisation
- Implement gradient descent baseline
- Implement Newton method baseline
- Track convergence behavior

### 4. Constrained Optimisation
- Support bounds $x \in [a,b]$
- Compare interior and boundary points
- Pick best point for minimize or maximize mode

### 5. Sensitivity Analysis
- Perturb parameters by percentages
- Recompute $x^*$ for each scenario
- Measure shifts in $x^*$ and objective value

### 6. Robustness Score
- Compute one score that summarizes stability
- High score means the recommendation is reliable

### 7. Reporting
- Print a short recommendation table
- Show method comparison
- Show at least one sensitivity plot

---

## Scope Limits (For Now)

- no multivariable optimization yet
- no global stochastic optimizers yet
- no web/API interface yet

I want to keep this focused and understandable first.

---

## Practical Use Cases I Care About

- pricing decisions
- process setpoint tuning
- bounded cost minimization problems

Same calculus idea, different domains.

---

## Definition of Done (My Checklist)

Implementation is done when:

1. `main.py` runs end-to-end from this folder
2. At least one objective is solved symbolically and numerically
3. Bound-constrained optimization is demonstrated
4. Sensitivity runs on a configurable perturbation grid
5. Summary output includes recommendation + robustness
6. Plots render correctly

---

## My Build Plan

### Phase 1 - Math Base
- function and derivative modules
- candidate detection and classification

### Phase 2 - Optimizers
- symbolic optimizer
- gradient descent + Newton method
- constrained wrapper

### Phase 3 - Reliability Layer
- sensitivity scenarios
- robustness computation

### Phase 4 - Communication Layer
- annotated objective plot
- sensitivity plot
- clear summary report

---

## Expected Output Style

When this runs, I want the console output to read like a decision story:

1. objective definition
2. candidates and classification
3. numerical convergence summary
4. final recommendation
5. sensitivity and robustness summary

That way, a lecturer can follow both the math and the practical conclusion.
