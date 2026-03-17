# Experiment 02: Reading Guide
## How to Understand the Code Flow (Start to Finish)

This guide shows you **which file to read in which order** to understand Experiment 02 from first principles.

---

## Stage 1: The Foundation (What We're Optimising)

### 1. Start: `calculus/function.py`
**What it does**: Defines the parametric objective function.

**Key code**:
```python
def f(x, params=None):
    if params is None:
        params = DEFAULT_PARAMS
    a = params['a']
    b = params['b']
    c = params['c']
    return a * x**3 + b * x**2 + c
```

**Why start here**: This is the **one mathematical object** that everything else depends on. You need to know what you're optimising before anything else makes sense.

**Takeaway**: The function is now **parametric** — you can swap out a, b, c values. This enables sensitivity analysis later.

---

### 2. Next: `calculus/derivatives.py`
**What it does**: Computes symbolic derivatives from the function.

**Key code**:
```python
def get_symbolic_derivatives(params=None):
    expr = f(x, params)
    d1 = sp.diff(expr, x)    # f'(x) = 3ax² + 2bx
    d2 = sp.diff(d1, x)      # f''(x) = 6ax + 2b
    return d1, d2
```

**Why here**: Just like Experiment 01, derivatives are foundational. But now you're NOT just analyzing — you're **setting up for optimisation**.

**Takeaway**: $f'(x) = 0$ tells you where to look. $f''(x)$ at those points tells you whether found a minimum or maximum.

---

### 3. Then: `calculus/classification.py` (NEW in Exp 02)
**What it does**: Applies the second-derivative test to classify critical points.

**Key code**:
```python
def classify_critical_points(candidates, params=None):
    _, d2 = get_symbolic_derivatives(params)
    results = []
    for cp in candidates:
        val = float(d2.subs(x, cp))
        if val > 0:
            label = 'local minimum'
        elif val < 0:
            label = 'local maximum'
        else:
            label = 'inconclusive'
        results.append({...})
    return results
```

**Why here**: You've computed $f'(x)$ and found where it equals zero. Now classify what you found: is each critical point a peak or valley?

**Takeaway**: This bridges analysis (Exp 01) with optimisation (Exp 02). Pure math determines the structure.

---

## Stage 2: Finding the Best Operating Point

### 4. Next: `optimization/symbolic_optimizer.py`
**What it does**: Solves $f'(x) = 0$ symbolically to find all critical points.

**Key code**:
```python
def find_symbolic_candidates(params=None):
    d1, _ = get_symbolic_derivatives(params)
    try:
        raw = sp.solve(d1, x)  # Solve 3ax² + 2bx = 0
    except Exception:
        return []
    return [cp for cp in raw if cp.is_real]  # Filter non-real solutions
```

**Why here**: Before you can classify critical points (step 3), you have to **find** them. This solver discovers candidates.

**Takeaway**: Critical points are just the solutions to an equation. Real-world functions might have 0, 1, 2, or many.

---

### 5. Then: `optimization/constrained_optimizer.py` (KEY FILE)
**What it does**: Finds the **best** candidate under constraints.

**Key code**:
```python
def constrained_optimize(bounds, direction='minimize', params=None):
    # Step 1: Find interior critical points
    interior = [cp for cp in symbolic_candidates if a <= cp <= b]
    
    # Step 2: Add boundary points
    all_points = interior + [a, b]
    
    # Step 3: Evaluate f at all candidates
    evals = [(pt, f(pt, params)) for pt in all_points]
    
    # Step 4: Pick the best according to direction
    if direction == 'minimize':
        best = min(evals, key=lambda t: t[1])
    else:
        best = max(evals, key=lambda t: t[1])
    
    return {'recommended_x': best[0], 'objective_value': best[1], ...}
```

**Why here**: This is where the **decision** happens. Given candidates and constraints, select one. This is the **core of optimisation**.

**Takeaway**: The extreme value theorem guarantees the minimum of a continuous function on a closed interval lives at a critical point or boundary. Evaluate both — pick the best.

---

### 6. Optional Verification: `optimization/numerical_optimizer.py`
**What it does**: Verifies the answer using two independent numerical methods.

**Key code**:
```python
def gradient_descent(params=None, x0=2.5, learning_rate=0.01, max_iter=2000):
    # Start at x0, repeatedly move in direction of steepest descent
    x = x0
    for i in range(max_iter):
        step = -learning_rate * grad_fn(x)
        x += step
        if abs(step) < tol:
            return {'x': x, 'method': 'Gradient Descent', ...}

def newtons_method(params=None, x0=2.5, max_iter=100):
    # Start at x0, use quadratic approximation to jump to root
    x = x0
    for i in range(max_iter):
        step = -grad_fn(x) / hess_fn(x)
        x += step
        if abs(step) < tol:
            return {'x': x, 'method': "Newton's Method", ...}
```

**Why optional**: These methods independently arrive at the same answer as `constrained_optimizer`, confirming correctness.

**Takeaway**: Gradient descent is slow but stable. Newton's method is fast but requires $f''(x)$. Both convergent if you start near the answer.

---

## Stage 3: Measuring Reliability

### 7. Next: `analysis/sensitivity.py` (KEY FILE)
**What it does**: Perturbs each parameter and recomputes the optimal $x^*$ under each scenario.

**Key code**:
```python
def sensitivity_analysis(bounds, direction='minimize', perturbations=None):
    baseline = constrained_optimize(bounds, direction)  # Get x* at default params
    
    records = []
    for param in ['a', 'b', 'c']:
        base_val = DEFAULT_PARAMS[param]
        for pct in [-20%, -10%, 0%, +10%, +20%]:
            # Create new params with this param perturbed
            new_val = base_val * (1 + pct)
            perturbed_params = {..., param: new_val, ...}
            
            # Recompute optimal x* with perturbed params
            result = constrained_optimize(bounds, direction, perturbed_params)
            
            # Record how much x* and f(x*) shifted
            records.append({
                'param': param,
                'perturbation_pct': pct,
                'x_star': result['x'],
                'dx_star': result['x'] - baseline['x'],  # The shift
                'd_objective': result['f'] - baseline['f'],
            })
    
    return baseline, records
```

**Why here**: You have a recommendation ($x^* = 2.0$). But **how confident should you be** if model parameters are slightly wrong?

**Takeaway**: This doesn't compute uncertainty in the statistical sense. It asks: *across a grid of reasonable parameter values, how much does the answer change?*

---

### 8. Then: `analysis/robustness.py`
**What it does**: Aggregates sensitivity data into a single robustness score.

**Key code**:
```python
def compute_robustness_score(sensitivity_records, baseline):
    non_baseline = [r for r in records if r['perturbation_pct'] != 0.0]
    
    # Measure relative shifts in x* and objective value
    rel_dx = [abs(r['dx_star']) / abs(baseline['x']) for r in non_baseline]
    rel_dobj = [abs(r['d_objective']) / abs(baseline['f']) for r in non_baseline]
    
    # Combine into a single sensitivity measure
    combined = 0.5 * mean(rel_dx) + 0.5 * mean(rel_dobj)
    
    # Map to [0, 1] via exponential decay
    score = exp(-combined)  # 1.0 = very stable, 0.0 = very sensitive
    
    return score  # e.g., 0.7163
```

**Why here**: Sensitivity produces many data points (15 scenarios × 3 parameters = 45 data points). Robustness distills these into **one actionable number**.

**Takeaway**: High score (>0.8) means the recommendation is safe even with parameter uncertainty. Low score (<0.5) means you need better parameter estimates.

---

## Stage 4: Visualisation and Reporting

### 9. Optional: `visualization/static_plot.py`
**What it does**: Plots the objective function with the recommended $x^*$ marked prominently.

**Why optional**: Provides visual confirmation. Not strictly necessary to understand the logic, but helps intuition.

**What to look for**: The red star should sit at the deepest point within the green-shaded feasible region.

---

### 10. Optional: `visualization/sensitivity_plot.py`
**What it does**: Shows per-parameter sensitivity curves — how $x^*$ shifts as each parameter is perturbed.

**Why optional**: Useful for identifying which parameters matter. Flat curves (like parameter `c`) mean that parameter doesn't affect the optimal location.

**What to look for**: Steep curves = sensitive, flat curves = robust to that parameter.

---

### 11. Finally: `reporting/summary.py`
**What it does**: Prints a human-readable recommendation table to console.

**Why last**: Brings together all results (classification, constrained optimum, numerical verification, sensitivity, robustness) into one formatted report.

**What to look for**: This is the **deliverable** — the output that a non-technical person would read.

---

## The Dependency Graph

Here's what depends on what:

```
calculus/function.py
    ↓
calculus/derivatives.py
    ├→ calculus/classification.py
    └→ optimization/symbolic_optimizer.py
        └→ optimization/constrained_optimizer.py
            ↑
            ├← optimization/numerical_optimizer.py (parallel verification)
            ├← analysis/sensitivity.py
            │   └→ analysis/robustness.py
            │       └→ reporting/summary.py
            └→ visualization/static_plot.py
                (along with sensitivity.py)
                └→ visualization/sensitivity_plot.py (parallel)
```

**Read order by criticality:**

| Must read | Should read | Nice to read |
|-----------|------------|-------------|
| `function.py` | `numerical_optimizer.py` | `visualization/static_plot.py` |
| `derivatives.py` | `sensitivity.py` | `visualization/sensitivity_plot.py` |
| `classification.py` | `robustness.py` | |
| `symbolic_optimizer.py` | `summary.py` | |
| `constrained_optimizer.py` | | |

---

## Quick Reference: What Each File Outputs

| File | Inputs | Key Output | Type |
|------|--------|-----------|------|
| `function.py` | a, b, c (parameters) + x (evaluation point) | f(x) — the objective value | scalar |
| `derivatives.py` | params + symbolic x | f'(x), f''(x) — symbolic expressions | SymPy expressions |
| `classification.py` | critical points + params | Classification (min/max/inconclusive) | list of dicts |
| `symbolic_optimizer.py` | params | Critical point candidates | list of numbers |
| `constrained_optimizer.py` | bounds + params + direction | x*, f(x*), all candidates evaluated | dict with recommendation |
| `numerical_optimizer.py` | x0 (starting guess) + params | x*, iteration count, convergence flag | dict per method |
| `sensitivity.py` | bounds + params + grid | Records of (param, perturbation, x*, f*) | list of 45 dicts |
| `robustness.py` | sensitivity records | Single robustness score ∈ [0, 1] | float |
| `visualization/*` | recommendation + sensitivity data | Plot opened in window | matplotlib figure |
| `reporting/summary.py` | all of the above | Formatted console table | printed text |

---

## A Concrete Walk-Through

Here's what happens when you run `main.py`:

```python
# Line 1: Get f'(x) and f''(x) for f(x) = x³ - 3x² + 2
d1, d2 = get_symbolic_derivatives()
# Output: d1 = 3x² - 6x,   d2 = 6x - 6

# Line 2: Solve f'(x) = 0
candidates = find_symbolic_candidates()
# Output: [0, 2]  ← two critical points

# Line 3: Classify them
classified = classify_critical_points(candidates)
# Output: [
#   {'x': 0, 'f''(x)': -6, 'label': 'local maximum'},
#   {'x': 2, 'f''(x)': 6, 'label': 'local minimum'},
# ]

# Line 4: Find the best within bounds [-0.5, 3.5]
recommendation = constrained_optimize([-0.5, 3.5], 'minimize')
# Evaluates: f(-0.5) = 1.125, f(0) = 2, f(2) = -2, f(3.5) = 8.125
# Output: {'x*': 2.0, 'f(x*)': -2.0, 'all_candidates': [...]}

# Line 5: Verify with gradient descent and Newton
gd = gradient_descent(x0=2.5)      # Takes 276 iterations to converge to x=2
newton = newtons_method(x0=2.5)    # Takes 6 iterations to converge to x=2

# Line 6: Perturb parameters and measure shifts
baseline, sensitivity = sensitivity_analysis([-0.5, 3.5], 'minimize')
# For each param in [a, b, c], applies perturbations [-20%, ..., +20%]
# Example: when a → 0.8*a, x* shifts from 2.0 to 2.5 (Δx = +0.5)

# Line 7: Compute robustness from all sensitivity scenarios
robustness = compute_robustness_score(sensitivity, baseline)
# Output: 0.7163  ← MODERATE robustness

# Line 8: Print human-readable report
print_summary(classified, recommendation, gd, newton, sensitivity, robustness)
# Prints formatted table to console

# Line 9-10: Visualize
plot_function(...)        # Shows f(x) with x* marked by a red star
plot_sensitivity(...)     # Shows three curves: how x* shifts with a, b, c
```

---

## Key Insight: The Two Phases

**Phase 1 (Stages 1–2):** Pure mathematics → answer the question *where is x\*?*
- Uses symbolic computation (SymPy)
- Deterministic: the answer is exact
- Output: a single number, $x^* = 2.0$

**Phase 2 (Stages 3–4):** Parameter uncertainty → answer the question *how much should I trust x\*?*
- Uses numerical perturbation (replicate the decision under different parameter values)
- Measure variability: how much does x* move?
- Output: a robustness score, 0.7163

Most people stop at Phase 1. Experiment 02 extends to Phase 2, which is what makes the recommendation actionable in the real world.

