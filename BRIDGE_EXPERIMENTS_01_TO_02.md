# Bridge Document: From Analysis to Decision-Making
## Understanding the Jump from Experiment 01 to Experiment 02

Walter Bishop Labs | Calculus Research Series  
Date: March 17, 2026

---

## Part 1: What Experiment 01 Gave Us

### The Core Achievement

Experiment 01 answered a **diagnostic question**: *What is the function doing?*

Given the cubic polynomial:
$$f(x) = x^3 - 3x^2 + 2$$

The experiment built a complete **analysis pipeline** that computed:

1. **Symbolic derivatives** — exact mathematical expressions for $f'(x)$ and $f''(x)$
2. **Critical points** — the exact locations where the function momentarily stops changing direction
3. **Visualizations** — both static and animated plots showing the function's full behavior

The output was **understanding**: a set of facts about the function's structure.

### The Pipeline Structure (Experiment 01)

```
experiment_01_function_behavior_analysis/
│
├── main.py                          ← Entry point
├── calculus/
│   ├── function.py                  ← Defines f(x)
│   ├── derivatives.py               ← Computes f'(x) and f''(x) symbolically
│   ├── analysis.py                  ← Finds critical points by solving f'(x)=0
│   └── __pycache__/
└── visualization/
    ├── static_plot.py               ← Renders the curve
    ├── animation_plot.py            ← Animates the drawing
    └── __pycache__/
```

**Key insight**: The structure is minimal because the goal is focused — extract derivatives and plot them.

---

## Part 2: The Conceptual Jump to Experiment 02

### The Question Changes

Experiment 02 answers a **prescriptive question**: *Where should x be?*

This is a **fundamentally different problem**:

| Experiment 01 | Experiment 02 |
|---|---|
| "Describe the function's mathematical features" | "What value of x minimises/maximises the objective?" |
| Output: derivatives, critical points, graphs | Output: a **decision** — a single recommended value of x with confidence |
| Frame: mathematics | Frame: decision-making under uncertainty |
| Tool: symbolic computation only | Tools: symbolic + numerical + statistical |

### Why This Is Harder

Experiment 01 computed derivatives — a purely symbolic operation. Once $f'(x)$ is known, critical points follow immediately from solving an equation.

Experiment 02 must handle **real-world complexity**:

1. **Constraints**: the feasible region is not always $(-\infty, \infty)$. Real problems have bounds: $x \in [a, b]$

2. **Uncertainty**: what if the function's parameters are slightly wrong? How much does that change the answer?

3. **Numerical reliability**: symbolic solvers sometimes fail (transcendental functions, non-polynomial objectives). Fallback numerical methods are needed.

4. **Robustness scoring**: a number like $x^* = 2.0$ is meaningless without context. A robustness score answers: *how much should I trust this recommendation?*

---

## Part 3: How the Folder Structure Evolved

### The Structural Problem

Experiment 01's structure was sufficient for **one-way analysis**: define → differentiate → solve → plot.

Experiment 02 requires **bidirectional decision flow**: find candidates → evaluate all options → select best → measure stability → report with confidence.

### Experiment 02's Expanded Structure

```
experiment_02_optimisation_and_sensitivity_analysis/
│
├── main.py                                  ← Entry point (orchestrates pipeline)
│
├── calculus/                                ← Mathematical foundations (extended)
│   ├── function.py                          ← f(x; a,b,c) now PARAMETRIC
│   ├── derivatives.py                       ← compute f'(x) and f''(x)
│   ├── classification.py                    ← NEW: classify critical points as min/max
│   └── __pycache__/
│
├── optimization/                            ← NEW: finding the best x
│   ├── symbolic_optimizer.py                ← solve f'(x)=0 symbolically
│   ├── numerical_optimizer.py               ← gradient descent + Newton's method
│   ├── constrained_optimizer.py             ← handle bounds [a,b]
│   └── __pycache__/
│
├── analysis/                                ← NEW: stress-testing the recommendation
│   ├── sensitivity.py                       ← perturb parameters, recompute optimal x*
│   ├── robustness.py                        ← compute stability score
│   └── __pycache__/
│
├── visualization/                           ← Plots (extended for decision context)
│   ├── static_plot.py                       ← plot f(x) with recommended x* marked
│   ├── sensitivity_plot.py                  ← NEW: show how x* shifts with params
│   └── __pycache__/
│
└── reporting/                               ← NEW: human-readable output
    ├── summary.py                           ← formatted recommendation table
    └── __pycache__/
```

### Why Each New Package Exists

| Package | Purpose | What Changed |
|---------|---------|--------------|
| **calculus/** (expanded) | Compute derivatives and classify points | Added `classification.py` to apply second-derivative test |
| **optimization/** (new) | Find candidates and select the best | Entirely new: symbolic solvers + numerical methods + constraints |
| **analysis/** (new) | Test stability under uncertainty | Entirely new: sensitivity + robustness assessment |
| **visualization/** (expanded) | Plot decisions, not just functions | Added `sensitivity_plot.py` to show parameter influence |
| **reporting/** (new) | Communicate results to humans | Entirely new: formatted summary tables and recommendations |

---

## Part 4: What Actually Happens in Experiment 02

### Step-by-Step Pipeline (What Happens When You Run It)

```python
# Stage 1: Compute the mathematics (Experiment 01 work)
d1, d2 = get_symbolic_derivatives()                # f'(x) = 3x² - 6x, f''(x) = 6x - 6

# Stage 2: Find candidates
candidates = find_symbolic_candidates()             # Solve f'(x) = 0 → [0, 2]
classified = classify_critical_points(candidates)   # x=0: local max, x=2: local min

# Stage 3: Select the best under constraints
recommendation = constrained_optimize([-0.5, 3.5])  # Evaluates all candidates in [−0.5, 3.5]
                                                    # Returns: x* = 2.0, f(x*) = −2.0

# Stage 4: Verify with numerical methods
gd_result = gradient_descent(x0=2.5)               # Descend to minimum: 276 iterations
newton_result = newtons_method(x0=2.5)             # Newton's quadratic method: 6 iterations

# Stage 5: Stress-test under parameter uncertainty
baseline, sensitivity = sensitivity_analysis(      # Perturb a, b, c by ±10%, ±20%
    [-0.5, 3.5], 'minimize'                        # Recompute x* for each scenario
)                                                   # Measure shifts: Δx*, Δf

# Stage 6: Compute robustness
score = compute_robustness_score(sensitivity)      # Formula: exp(−combined_shift)
                                                    # Result: 0.7163 → MODERATE robustness

# Stage 7: Report
print_summary(...)                                  # Human-readable table
plot_function(...)                                  # Visualise f(x) with x* marked
plot_sensitivity(...)                               # Show parameter influence
```

### A Concrete Example: Why This Matters

Imagine you're an engineer tuning a **chemical process** to minimize waste. Your model says:

> Optimal temperature: x* = 200°C

Without Experiment 02, you set the thermostat to 200°C and hope.

With Experiment 02, you learn:

- **Critical points**: There are two local optima at 180°C (max waste) and 200°C (min waste)
- **Constrained optimum**: Within your equipment's safe range [150°C, 250°C], best is 200°C
- **Numerical verification**: Both gradient descent and Newton's method confirm it
- **Sensitivity analysis**: 
  - The reaction order parameter `a` is critical — if it's off by 20%, x* moves to 250°C (bad)
  - The activation energy parameter `b` is also sensitive
  - The baseline offset `c` doesn't matter — it just shifts absolute waste, not the optimal point
- **Robustness score**: 0.7163 → MODERATE
  - **Decision**: Set to 200°C, but **invest in measuring parameter `a` more accurately** because that's what drives uncertainty

Without the robustness layer, you might have set 200°C blindly and missed that parameter estimation is your real bottleneck.

---

## Part 5: Practical Applications of Experiment 02

### A. Pricing Optimisation (E-Commerce)

**Objective**: Maximise profit as a function of price.

$$\text{Profit}(p) = (p - \text{cost}) \times \text{demand}(p)$$

where demand typically decays as price rises.

**Experiment 02 answers**:
- What price maximises profit?
- Is the optimum robust to uncertainty in price elasticity of demand?
- If we must stay within [p_min, p_max] due to contracts, what do we change?

**Real output**: "Set price to $47.50. If demand elasticity is ±10% off, price moves to $44–$51. Robustness: HIGH. Safe to implement."

---

### B. Process Engineering (Manufacturing)

**Objective**: Minimise energy cost while maintaining product quality.

$$\text{Cost}(T) = f(T) \quad \text{where } T \in [T_{\min}, T_{\max}]$$

and the function depends on:
- Raw material cost per unit
- Energy efficiency curve
- Equipment limitations

**Experiment 02 answers**:
- What temperature setting minimises total cost?
- How sensitive is this to feedstock variation or equipment degradation?
- If external energy prices increase by 15%, does the recommendation change?

**Real output**: "Optimal setpoint: 185°C. Cost is $2.30/unit. If energy prices rise 15%, setpoint is 188°C (cost rises to $2.47). Robustness: MODERATE — monitor feedstock composition."

---

### C. Portfolio Optimisation (Finance)

**Objective**: Maximise expected return subject to risk constraints.

$$\text{Return}(w_1, w_2, \ldots) \quad \text{subject to} \quad \text{Variance} \leq \sigma_{\max} \text{ and } \sum w_i = 1$$

**Experiment 02 answers** (extended to multivariate):
- What allocation of assets maximises return under the risk constraint?
- How sensitive is this to correlation estimates between assets?
- If we add a new constraint (max 20% in any single stock), how much return do we lose?

**Real output**: "Allocate 40% bonds, 35% large-cap, 15% international, 10% commodities. Expected return: 6.2%. If correlations are misestimated by ±0.1, return drops by max 0.3%. Robustness: HIGH."

---

### D. Medical Treatment Dosing

**Objective**: Minimise side effects while maintaining therapeutic bloodstream concentration.

$$\text{Harm}(d) = \text{toxicity}(d) + \text{underdose penalty}(d)$$

where the tradeoff depends on patient factors: age, weight, kidney function, etc.

**Experiment 02 answers**:
- What dose minimises overall harm?
- How much do individual patient factors shift the optimal dose?
- If a patient's kidney function is uncertain, how wide is the safe dosing range?

**Real output**: "Recommend 250 mg daily. For a 70 kg patient with normal kidney function, robustness is HIGH. If kidney function is impaired (creatinine >1.5), dose reduces to 150 mg and robustness drops to MODERATE — consider more frequent monitoring."

---

### E. Supply Chain Planning

**Objective**: Minimise total logistics cost (inventory + warehousing + transport) while staying in-stock.

$$\text{Cost}(q) = \text{ordering\_cost}(q) + \text{inventory\_cost}(q) + \text{shortage\_penalty}(q)$$

**Experiment 02 answers**:
- What reorder quantity `q` minimises total cost?
- How much does demand variability matter?
- If supplier lead time increases, does the optimal `q` change?

**Real output**: "Reorder 500 units per cycle. Minimises cost to $12,000/month. If demand is ±15% off forecast, optimal reorder is 425–575 units (cost varies $11,700–$12,300). Robustness: MODERATE. Recommendation: Use a 50-unit safety buffer."

---

## Part 6: Key Transitions in Thinking

### From Experiment 01 to 02

| Aspect | Exp 01 | Exp 02 |
|--------|--------|---------|
| **Primary question** | What is happening? | What should happen? |
| **Math focus** | Derivatives and analysis | Optimisation and robustness |
| **Output type** | Numbers and graphs | A decision with confidence |
| **Success criterion** | Correct computation | Actionable recommendation |
| **Scope of uncertainty** | None — exact math | Explicit via sensitivity analysis |
| **Typical user** | Mathematician, student | Engineer, manager, analyst |

### Why Constraints Matter (Conceptually New in Exp 02)

In pure mathematics, we optimise over all real numbers. In practice:
- Money can't be negative (budget constraints)
- Temperature can't exceed equipment limits
- Inventory can't be negative
- Time is finite

**The extreme value theorem** guarantees that a continuous function on a **closed and bounded** interval achieves its min and max. Those extrema occur either at critical points or boundaries.

Experiment 02 exploits this: evaluate interior critical points + all boundaries, then pick the best.

### Robustness as Insurance (Conceptually New in Exp 02)

A single number $x^* = 2.0$ is fragile. If the model is even slightly wrong, the answer might be garbage.

Robustness scoring asks: *across a grid of realistic parameter variations, how much does the optimal decision move?*

This is **not** confidence intervals or statistical significance. It is stress-testing the recommendation against model uncertainty.

A high robustness score means: "This recommendation is probably still good even if my model isn't perfect."

A low robustness score means: "I need to collect more data on these sensitive parameters before acting."

---

## Part 7: What Carries Forward to Experiment 03 and Beyond

Experiment 02 establishes three powerful ideas that extend infinitely:

1. **Constrained optimisation**: Everything in the real world has bounds. The mathematics is the same: evaluate candidates at interior critical points and constraints boundaries, select the best.

2. **Sensitivity analysis**: Uncertainty is often more important than optimal values. By varying parameters and measuring output shifts, you can identify which parameters deserve careful measurement and which are robust to uncertainty.

3. **Robustness scoring**: A single metric that quantifies how trustworthy a recommendation is. This scales to any number of parameters.

In **Experiment 03** (planned), these same ideas should extend to:
- **Multivariate objectives**: $f(x, y, z, \ldots)$ instead of just $f(x)$
- **Gradient-based optimisation**: $\nabla f$ replaces $f'(x)$
- **Hessian-based classification**: $H$ (the Hessian matrix) replaces $f''(x)$
- **Constrained optimisation methods**: Lagrange multipliers, KKT conditions, penalty methods
- **Multidimensional sensitivity**: how x*, y*, z* shift when parameters change across multiple dimensions

The code structure and pipeline will expand, but the conceptual framework is already built in Experiment 02.

---

## Summary: The Bridge in One Paragraph

**Experiment 01** built the ability to understand a function: compute its derivatives, find its critical points, visualise its shape. **Experiment 02** takes those tools and uses them to **make decisions**: extend from unconstrained analysis to constrained optimisation (handling real-world bounds), verify robustness via numerical methods, stress-test the recommendation via sensitivity analysis, and output a number with a confidence score. The folder structure expanded dramatically because decision-making requires orchestrating multiple computational layers (symbolic + numerical + statistical) with human-readable reporting. The practical impact is that you can now answer not just "what is the function doing?" but "where should I operate, and how much should I trust that answer?"

