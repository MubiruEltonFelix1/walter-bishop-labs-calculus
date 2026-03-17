# Understanding — Experiment 01: Function Behavior Analysis

**Walter Bishop Labs | Calculus Research Series**
**Date:** March 15, 2026
**Status:** Complete

---

## What This Document Is

This is the post-experiment understanding document for Experiment 01. It exists to close the loop between running the code and actually knowing what you saw. If the README explains what was built, this document explains what it means — the libraries, the graphs, the mathematical lines on screen, and the intuition you should carry forward.

---

## The Function Under Study

Everything in this experiment is built around one function:

$$f(x) = x^3 - 3x^2 + 2$$

This is a cubic polynomial. It was chosen deliberately because within a compact domain it demonstrates every behavior worth studying at this stage: a local maximum, a local minimum, an inflection point, and two real roots. It is rich enough to be interesting and simple enough to be fully understood.

---

## The Two Libraries

### NumPy — The Numerical Engine

NumPy is used whenever the code needs to evaluate the function at many points simultaneously for plotting. The line `np.linspace(-2, 4, 400)` generates 400 evenly spaced x-values as an array. Passing that array directly to `f(x_vals)` evaluates the function at all 400 points at once. NumPy operates on concrete floating-point numbers — it does not know or care what the function means symbolically. It computes values at scale.

The critical connection between NumPy and SymPy happens through `sp.lambdify`. This call takes a SymPy symbolic expression — for example `3*x**2 - 6*x` — and converts it into a NumPy-compatible function that accepts arrays. Without this bridge, SymPy and NumPy cannot work together: SymPy cannot operate on arrays, and NumPy cannot differentiate.

**NumPy's role in one sentence:** density and scale — it answers *what does this function look like across many points?*

---

### SymPy — The Symbolic Engine

SymPy treats `x` as an algebraic symbol, not a number. When the code calls `sp.diff(f(x), x)`, SymPy applies the actual rules of calculus — power rule, chain rule, product rule — and returns an exact algebraic expression. For this function:

- `sp.diff(f(x), x)` → $3x^2 - 6x$
- `sp.diff(first_derivative, x)` → $6x - 6$
- `sp.solve(3x^2 - 6x, x)` → $[0, 2]$

All of these are exact. A numerical solver approximates, producing results like `x ≈ 0.0000000001` and `x ≈ 1.9999999998`. SymPy returns exactly `0` and `2`. That precision is what makes classification reliable — when you evaluate the second derivative at a critical point, you get an exact integer, not a floating-point value that might round the wrong way.

**SymPy's role in one sentence:** exactness and reasoning — it answers *what is this function structurally?*

---

## The Static Plot — Every Line Explained

The static plot renders three curves over the domain $x \in [-2, 4]$ and marks two special points on a dark background.

### Line 1 — `f(x)` (solid line): the function itself

This is $x^3 - 3x^2 + 2$ evaluated numerically across 400 points. The curve you see is the complete behavior of the function — where it rises, where it falls, where it crosses zero, and the shape of its peaks and valleys. This is the subject of the experiment. Everything else on the plot is commentary on this line.

### Line 2 — `f'(x)` (dashed line): the first derivative

This is $3x^2 - 6x$, plotted as its own curve on the same axes. Its position relative to zero tells you what the solid `f(x)` curve is doing at every x:

| Where `f'(x)` is | What `f(x)` is doing |
|---|---|
| Above the x-axis | Rising — output increasing as x increases |
| Below the x-axis | Falling — output decreasing as x increases |
| Crossing zero | At a peak or a valley — slope is exactly flat |

Reading both lines together on the static plot:

- From $x = -2$ to $x = 0$: the dashed line sits above zero → `f(x)` is rising
- At $x = 0$: the dashed line touches zero from above → `f(x)` reaches its **local maximum** at this point
- From $x = 0$ to $x = 2$: the dashed line sits below zero → `f(x)` is falling
- At $x = 2$: the dashed line touches zero from below → `f(x)` reaches its **local minimum** at this point
- From $x = 2$ to $x = 4$: the dashed line rises back above zero → `f(x)` is rising again

The zero-crossings of `f'(x)` are the critical points of `f(x)`. This is not coincidence — it is the definition of a critical point.

### Line 3 — `f''(x)` (dotted line): the second derivative

This is $6x - 6$, a straight line with slope 6 that crosses zero at $x = 1$. It is the simplest curve on the plot but it carries distinct information: it measures **curvature** — whether the `f(x)` curve is bending upward like a bowl ($\cup$) or bending downward like a hill ($\cap$).

| Where `f''(x)` is | Curvature of `f(x)` | Visual shape |
|---|---|---|
| Above zero | Concave up — bowl shape | Slope of `f(x)` is increasing |
| Below zero | Concave down — hill shape | Slope of `f(x)` is decreasing |
| Exactly zero | Inflection point | Curvature reversal |

Reading the dotted line:

- Left of $x = 1$: dotted line is negative → `f(x)` curves downward (concave down, hill-like)
- At $x = 1$: dotted line crosses zero → **inflection point** — the curve stops bending one way and begins bending the other
- Right of $x = 1$: dotted line is positive → `f(x)` curves upward (concave up, bowl-like)

### The scatter dots: critical point markers

The two orange/colored dots are placed on the `f(x)` curve at `x = 0` and `x = 2`. These are the solutions to `f'(x) = 0` — the points where the function's slope is exactly zero. One is a local maximum at `(0, 2)` and the other is a local minimum at `(2, -2)`.

---

## The Animated Plot — What It Teaches

The animation draws the `f(x)` curve progressively from $x = -2$ toward $x = 4$, one point per frame across 200 frames. At each frame, two additional elements update:

### The growing curve
You watch the function build itself from left to right. This reinforces that the function is a relationship between an input and an output, traced across a domain — not a static picture.

### The tangent line (chasing dashed red line)
At the current leading point, the animation computes:

```python
slope = float(f_prime(x_tip))
tangent.set_data(t, y_tip + slope * (t - x_tip))
```

This is point-slope form: $y = y_1 + m(x - x_1)$. The short line segment drawn is the tangent line — the local linear approximation of `f(x)` at that exact point. Its slope is the value of the first derivative at that x.

**Watch what the tangent line does as the animation runs:**
- When the curve is rising steeply: the tangent line tilts sharply upward
- As the curve approaches the peak at $x = 0$: the tangent line gradually flattens toward horizontal
- Just after the peak: the tangent line tilts downward
- As the curve approaches the minimum at $x = 2$: the tangent line flattens toward horizontal again
- After the minimum: the tangent line tilts upward again

You are watching the first derivative change in real time. The tangent line *is* the first derivative made physical.

---

## The First Derivative — Full Intuition

### What it is

The first derivative $f'(x) = 3x^2 - 6x$ is the instantaneous rate of change of `f(x)`. At any point $x = a$, the value $f'(a)$ is the exact slope of the tangent line to the curve at that point.

### The sign is what matters most

You do not need to know that $f'(1.5) = -2.25$ to know the function is falling at $x = 1.5$. You need to know it is negative. Sign analysis drives all optimization logic:

$$f'(x) > 0 \Rightarrow \text{function is increasing}$$
$$f'(x) < 0 \Rightarrow \text{function is decreasing}$$
$$f'(x) = 0 \Rightarrow \text{candidate for a maximum or minimum}$$

### Why it matters beyond this experiment

The first derivative is the engine of optimization. Every optimizer — gradient descent in machine learning, SciPy's `minimize`, Excel Solver, portfolio optimization in finance, training a neural network — is fundamentally chasing the point where the derivative equals zero, or following the direction the derivative points. Experiment 02 operationalizes this directly.

---

## The Second Derivative — Full Intuition

### What it is

The second derivative $f''(x) = 6x - 6$ is the derivative of the first derivative. It measures how fast the slope itself is changing — not how fast the function changes, but how fast the rate of change changes. Geometrically it is curvature.

### The second derivative test — classification

Once a critical point is found by solving $f'(x) = 0$, the second derivative classifies it:

$$f''(x^*) > 0 \Rightarrow \text{local minimum — you are at the bottom of a bowl}$$
$$f''(x^*) < 0 \Rightarrow \text{local maximum — you are at the top of a hill}$$
$$f''(x^*) = 0 \Rightarrow \text{inconclusive — higher-order analysis needed}$$

Applying this to the two critical points found:

- At $x = 0$: $f''(0) = 6(0) - 6 = -6 < 0$ → confirmed **local maximum**
- At $x = 2$: $f''(2) = 6(2) - 6 = +6 > 0$ → confirmed **local minimum**

This classification step is exactly what Experiment 02 implements systematically.

### The second derivative as a stability measurement

The magnitude of $f''$ at a minimum is more than a classification — it is a description of how tight the bowl is:

- A large $|f''(x^*)|$ means the bowl curves sharply. Small movements away from $x^*$ cost a lot in function value. The minimum is stable and well-defined.
- A small $|f''(x^*)|$ means the bowl is nearly flat. Small movements away from $x^*$ barely change the function value. The minimum is shallow and sensitive — easy to drift away from under perturbation.

This is the foundational intuition behind sensitivity analysis. Experiment 02 builds directly on this: how much does the optimal point shift when the function parameters change slightly?

---

## Key Takeaways to Carry Forward

**1 — The three-curve system is complete.**
`f(x)`, `f'(x)`, and `f''(x)` together give a full description of any smooth function's behavior. You can read the entire story of a function from these three curves alone: where it rises, where it falls, where it peaks, where it dips, and where its curvature flips.

**2 — Critical points are found by algebra, classified by the second derivative.**
`f'(x) = 0` finds candidates. `f''(evaluated at each candidate)` determines what kind of candidate it is. They serve different purposes and you need both.

**3 — The tangent line is the first derivative made visible.**
Gradient descent in machine learning is exactly the tangent-line-following you watched in the animation. The algorithm evaluates the slope at the current point and steps in the direction of steepest descent. You have already seen this happen.

**4 — Sign matters more than magnitude for directional reasoning.**
Whether the function is rising or falling, concave up or concave down — all of this is determinable from sign alone. Magnitude tells you how fast or how sharp. This distinction between *direction* and *rate* is a recurring pattern in all applied mathematics.

**5 — Sensitivity starts with the second derivative's magnitude.**
A narrow bowl is robust. A flat bowl is fragile. This is the bridge into Experiment 02: the second derivative at an optimal point is not just a classification label — it is the first quantitative measure of how much you can trust that optimum under real-world conditions.

**6 — SymPy finds the truth; NumPy renders it.**
Exact symbolic answers guide correct classification. Dense numerical evaluation makes behavior visible. Neither alone is sufficient. Both together — bridged by `lambdify` — form the computational workflow this lab is built on.
