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

This moves the project from descriptive calculus to decision-oriented calculus.

---

## My Main Goal

I want one run of this experiment to return a practical recommendation, not just equations.

Target outputs:
- recommended operating point $x^*$
- objective value at $x^*$
- classification (local min/local max/inconclusive)
- sensitivity of $x^*$ to parameter changes
- method comparison (symbolic vs numerical)

So the objective is not just a mathematically valid answer, but a recommendation I can defend.

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

I treat Experiment 02 as a natural continuation, not a separate project.

---

## Audience and Documentation Style

I wrote this README to serve both:

1. Lecturer-level review: structured objectives, method, outputs, and scope.
2. Experienced technical reading: enough implementation detail to evaluate design choices.

The tone stays student-first, but the structure is intentionally professional.

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

Each package has a single responsibility so the pipeline remains understandable as complexity increases.

---

## Functional Targets

### 1. Symbolic Candidate Discovery
- Solve $f'(x)=0$ where possible
- Keep only real candidates
- Include interval boundaries if constraints exist

This stage gives mathematically grounded candidates before numerical heuristics are used.

### 2. Candidate Classification
- Evaluate $f''(x)$ at each candidate
- Label as local minimum, local maximum, or inconclusive

This keeps the decision layer tied to standard calculus interpretation.

### 3. Numerical Optimisation
- Implement gradient descent baseline
- Implement Newton method baseline
- Track convergence behavior

I use this as both a fallback and a cross-check against symbolic methods.

### 4. Constrained Optimisation
- Support bounds $x \in [a,b]$
- Compare interior and boundary points
- Pick best point for minimize or maximize mode

This stage reflects realistic conditions where unconstrained optima may be infeasible.

### 5. Sensitivity Analysis
- Perturb parameters by percentages
- Recompute $x^*$ for each scenario
- Measure shifts in $x^*$ and objective value

This helps me evaluate how fragile or stable the recommendation is.

### 6. Robustness Score
- Compute one score that summarizes stability
- High score means the recommendation is reliable

I use this as a compact communication metric for non-specialist readers.

### 7. Reporting
- Print a short recommendation table
- Show method comparison
- Show at least one sensitivity plot

The report should explain not only what the recommended point is, but why it is trustworthy.

---

## Scope Limits (For Now)

- no multivariable optimization yet
- no global stochastic optimizers yet
- no web/API interface yet

I want to keep this focused and understandable first.

I also limit scope intentionally so each module remains inspectable for teaching purposes.

---

## Core Methodology

My intended decision pipeline is:

1. Define objective function and parameters.
2. Compute symbolic derivatives.
3. Generate candidate optima.
4. Classify and filter candidates.
5. Enforce constraints.
6. Compare with numerical methods.
7. Run sensitivity scenarios.
8. Compute robustness and print a recommendation summary.

This pipeline keeps mathematical validity, computational practicality, and interpretability in one flow.

---

## Practical Use Cases I Care About

- pricing decisions
- process setpoint tuning
- bounded cost minimization problems

Same calculus idea, different domains.

My main learning target is transferable reasoning: once the pipeline is clear in one domain, the same structure can be reused in others.

---

## Definition of Done (My Checklist)

Implementation is done when:

1. `main.py` runs end-to-end from this folder
2. At least one objective is solved symbolically and numerically
3. Bound-constrained optimization is demonstrated
4. Sensitivity runs on a configurable perturbation grid
5. Summary output includes recommendation + robustness
6. Plots render correctly

If any one of these fails, I consider the experiment incomplete.

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

I keep this phased plan so implementation remains manageable and review-friendly.

---

## Evaluation Criteria

I will evaluate this experiment using three criteria:

1. Mathematical correctness: symbolic and numerical results are consistent.
2. Practical reliability: recommendation remains stable under moderate perturbations.
3. Communication quality: output is clear enough for a lecturer or non-specialist stakeholder to follow.

This helps me avoid treating "it runs" as "it is done."

---

## Expected Output Style

When this runs, I want the console output to read like a decision story:

1. objective definition
2. candidates and classification
3. numerical convergence summary
4. final recommendation
5. sensitivity and robustness summary

That way, a lecturer can follow both the math and the practical conclusion.

I also want experienced readers to see clear traceability from derivative math to final decision output.
