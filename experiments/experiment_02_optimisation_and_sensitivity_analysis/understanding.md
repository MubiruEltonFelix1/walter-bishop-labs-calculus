# Understanding — Experiment 02: Optimisation and Sensitivity Analysis

Walter Bishop Labs | Calculus Research Series  
Date: March 17, 2026  
Status: Complete

---

## What This Experiment Actually Did

Experiment 01 described a function — it found derivatives, located critical points, and plotted the curve.

Experiment 02 used those same tools to answer a harder question: **given this function and a feasible region, what is the best operating point, and how much should we trust that recommendation?**

The output is not a graph of the function. The output is a decision: *operate at x = 2.0, with high confidence*.

---

## The Objective Function

The function is the same cubic studied in Experiment 01:

$$f(x) = x^3 - 3x^2 + 2$$

It is now treated as an **objective function** rather than a subject of pure analysis. The difference is the frame: we are no longer asking "what does this function do?" We are asking "where should x be?"

The function is parameterised as:

$$f(x;\, a, b, c) = ax^3 + bx^2 + c$$

with defaults $a=1$, $b=-3$, $c=2$. This parameterisation makes sensitivity analysis possible: we can hold the function structure constant while varying individual parameters to measure how much the optimal decision changes.

---

## The First and Second Derivative Test

A critical point is any $x$ where $f'(x) = 0$.  On its own, that only tells us the function is momentarily flat.  It does not tell us whether that flat point is a peak, a valley, or a transitional shoulder.

The second derivative resolves this:

$$f''(x) > 0 \implies \text{the function is concave up at } x \implies \text{local minimum}$$
$$f''(x) < 0 \implies \text{the function is concave down at } x \implies \text{local maximum}$$
$$f''(x) = 0 \implies \text{inconclusive — higher-order terms needed}$$

For $f(x) = x^3 - 3x^2 + 2$:

- $f'(x) = 3x^2 - 6x$, so critical points are at $x = 0$ and $x = 2$
- $f''(x) = 6x - 6$, so $f''(0) = -6 < 0$ (local maximum) and $f''(2) = 6 > 0$ (local minimum)

The local minimum at $x = 2$ is therefore the natural candidate for a minimisation objective.

---

## Constrained Optimisation: Why Boundaries Matter

Unconstrained optimisation finds a local minimum. Real-world problems always operate within constraints: budgets, physical limits, regulatory bounds.

When we constrain $x \in [-0.5,\, 3.5]$, we must evaluate three types of points:

1. **Interior critical points** — where $f'(x) = 0$ inside the domain
2. **Boundary endpoints** — $x = -0.5$ and $x = 3.5$

The global optimum over a closed interval is whichever of these evaluates best. This is the **extreme value theorem** in direct action: a continuous function on a closed interval always achieves its minimum and maximum, and those extrema occur either at a critical point or a boundary.

For this experiment:
- $f(-0.5) \approx 2.625$, $f(3.5) \approx 8.625$, $f(0) = 2$, $f(2) = -2$

The minimum is $f(2) = -2$. Recommendation: **operate at $x = 2$**.

---

## Gradient Descent vs Newton's Method

Both numerical methods find the same point, but through fundamentally different mechanisms.

### Gradient Descent

Uses only first-order information. The update rule is:

$$x_{n+1} = x_n - \alpha \cdot f'(x_n)$$

where $\alpha$ is the learning rate. The algorithm moves in the direction that reduces $f$ most steeply. Convergence is **linear** — each iteration reduces the error by a constant factor of approximately $|1 - \alpha \cdot f''(x^*)|$.

With $\alpha = 0.01$ and $f''(2) = 6$, the convergence factor is $|1 - 0.06| = 0.94$. Each step removes 6% of the remaining error. This is reliable but slow — it takes hundreds to thousands of iterations.

### Newton's Method

Uses both first and second-order information. It finds a root of $f'(x) = 0$ by applying Newton-Raphson to $f'$:

$$x_{n+1} = x_n - \frac{f'(x_n)}{f''(x_n)}$$

This is equivalent to fitting a local quadratic approximation to $f$ at $x_n$ and jumping directly to its minimum. Convergence is **quadratic** — the error roughly squares each iteration. Newton's method reaches machine precision in 5–10 steps where gradient descent needs thousands.

The tradeoff: Newton requires $f''(x) \neq 0$ at every step. Near a flat inflection point, $f''(x) \approx 0$ causes the step to blow up. Gradient descent has no such singularity risk.

**Key intuition**: gradient descent is cautious and slow. Newton's method is aggressive and fast. In practice, neither is universally superior.

---

## Sensitivity Analysis

A sensitivity analysis asks: *if I am wrong about the parameters, how wrong is my recommendation?*

For each parameter in $\{a, b, c\}$, we perturb the default value by $-20\%$, $-10\%$, $+10\%$, $+20\%$ and recompute the optimal $x^*$ under each scenario.

For the parametric cubic $f(x;\,a,b,c) = ax^3 + bx^2 + c$, the critical points satisfy:

$$f'(x) = 3ax^2 + 2bx = x(3ax + 2b) = 0$$

So $x^* = -2b \,/\, (3a)$ is the non-zero critical point.

This formula tells us everything about sensitivity analytically:

| Parameter perturbed | Effect on $x^*$              | Intuition                               |
|---------------------|------------------------------|-----------------------------------------|
| $a$ (cubic coeff)   | $x^* = -2b/(3a)$ → scales inversely with $a$ | More curvature means the valley narrows, shifts the bottom |
| $b$ (quadratic coeff) | $x^* = -2b/(3a)$ → scales linearly with $b$ | Tilting the quadratic term slides the valley |
| $c$ (constant offset) | $x^* = -2b/(3a)$ → **no change** | A vertical shift lifts the whole curve, not the location of the valley |

The flat sensitivity curve for $c$ in the plot is not a bug. It is a meaningful result: **the optimal operating point is independent of additive constants in the objective function**. Perturbing $c$ shifts the objective *value* by exactly the same amount as the perturbation, but the *location* of the minimum does not move.

---

## Robustness Score

The robustness score is a single number that summarises how stable the recommendation is across all perturbation scenarios. It is defined as:

$$\text{score} = \exp\!\left( -\left( \frac{1}{2} \cdot \overline{\left|\Delta x^*\right| / |x^*_0|} + \frac{1}{2} \cdot \overline{\left|\Delta f\right| / |f(x^*_0)|} \right) \right)$$

where bars denote averages over all non-baseline perturbation scenarios.

Properties of this score:

- **Score = 1.0**: the recommendation does not shift at all under any perturbation. Perfect robustness.
- **Score = 0.0**: the recommendation shifts by amounts comparable to the baseline values themselves. The model is not trustworthy.
- **Score ≥ 0.8**: HIGH robustness — safe to act on the recommendation even if parameters are uncertain.
- **Score ∈ [0.5, 0.8)**: MODERATE — the recommendation is directionally correct but precise values should be treated with caution.
- **Score < 0.5**: LOW — the recommendation is sensitive enough that parameter estimation quality is the bottleneck, not the optimiser.

The exponential form is chosen deliberately. It maps the sensitivity measure (which lives on $[0, \infty)$) into the probability-like range $[0, 1]$ and decays steeply for high sensitivity — which is the correct behavior, since a recommendation that shifts by 50% of its value is far less trustworthy than the linear-score equivalent would suggest.

---

## Reading the Plots

### Static Plot (Objective Function)

- **Blue curve**: $f(x) = x^3 - 3x^2 + 2$, the objective function
- **Green shading**: the feasible region $[-0.5, 3.5]$
- **Grey dots**: every point evaluated by the constrained optimiser (interior critical points + boundaries)
- **Red star**: the recommended operating point $x^* = 2$

The star sits at the deepest point of the curve within the shaded region. The grey dots show that the optimiser evaluated all candidate points before selecting.

### Sensitivity Plot (Three Subplots)

Each subplot shows how $x^*$ moves as one parameter is perturbed.

- **Parameter $a$**: the curve slopes — perturbing $a$ moves $x^*$ by a meaningful amount. The slope of this curve is the **sensitivity coefficient** of the recommendation with respect to $a$.

- **Parameter $b$**: similar slope, roughly linear, with the same direction intuition.

- **Parameter $c$**: completely flat. The line does not move regardless of perturbation. This is the visual proof that the constant offset has no influence on the optimal location.

A flat curve means you do not need to estimate that parameter precisely. A steep curve means accurate knowledge of that parameter is critical to a trustworthy recommendation.

---

## What Carries Forward

1. **Optimisation is derivative analysis with a purpose.** Every technique in this experiment — critical point location, second-derivative classification, constrained boundary evaluation — was developed in Experiment 01. Experiment 02 shows where those tools lead.

2. **A recommendation without a robustness check is incomplete.** The optimal $x^*$ alone is a number. The sensitivity analysis transforms it into a decision: *act with confidence* or *collect more information about parameters first*.

3. **Parameters have different roles.** Some parameters control the position of the optimum. Others control only the value at the optimum. This distinction matters enormously in practice — you can afford to be uncertain about the latter but not the former.

4. **Newton's method is faster than gradient descent by any practical measure.** Both converge to the same point. Newton uses quadratic convergence; gradient descent uses linear. For smooth, well-conditioned objectives near an initial guess, Newton should always be the default unless $f''(x)$ is unavailable or near-zero.

These principles extend directly to multivariate calculus, where gradients replace derivatives, Hessians replace second derivatives, and sensitivity analysis extends to partial derivatives and the Jacobian of the optimal solution with respect to parameters.
