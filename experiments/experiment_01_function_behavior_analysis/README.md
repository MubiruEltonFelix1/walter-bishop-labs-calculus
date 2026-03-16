# Experiment 01 — Function Behavior Analysis

**Walter Bishop Labs | Calculus Research Series**
**Date:** March 15, 2026
**Status:** Complete

---

## Overview

Experiment 01 establishes the foundational computational framework for the Walter Bishop Labs Calculus Research Series. The objective of this experiment was to construct a fully automated pipeline that takes a single-variable polynomial function, derives its symbolic derivatives, identifies its critical points, and renders both static and animated visualizations of its behavior across a defined domain. Rather than relying on numerical approximation, the experiment was designed from the ground up to operate on exact symbolic mathematics, ensuring precision and reproducibility across all analytical outputs.

The function selected for this experiment is a cubic polynomial: f(x) = x³ − 3x² + 2. This function was chosen deliberately for its rich behavior within a compact domain. It exhibits a local maximum, a local minimum, two real roots, and an inflection point — making it an ideal subject for demonstrating derivative analysis, critical point detection, and graphical interpretation.

---

## Project Structure

The experiment is organized into two primary subsystems: the calculus engine and the visualization layer. The calculus engine, located in the `calculus/` directory, is responsible for all mathematical computation. The visualization layer, located in the `visualization/` directory, handles all graphical rendering. A single entry point, `main.py`, orchestrates the full experiment pipeline from symbolic derivation through to animated display.

    experiment_01_function_behavior_analysis/
        main.py
        calculus/
            function.py
            derivatives.py
            analysis.py
        visualization/
            static_plot.py
            animation_plot.py

---

## What Was Implemented

### Function Definition

The experimental function is defined in `calculus/function.py` using NumPy-compatible syntax. The function accepts either a scalar or an array as its argument, making it compatible with both the symbolic engine and the numerical plotting routines without any modification. This dual compatibility was an intentional design choice that eliminates the need for separate symbolic and numerical representations of the same mathematical object.

### Symbolic Differentiation

Symbolic differentiation is handled in `calculus/derivatives.py` using the SymPy library. Upon module load, the function is evaluated in symbolic form using a SymPy symbol for x, and both the first and second derivatives are computed via `sp.diff`. These expressions are stored as module-level variables, making them available for import by both the analysis module and the main pipeline. The first derivative characterizes the rate of change and slope behavior of the function, while the second derivative captures curvature and concavity information.

A bug was identified and resolved during development: the original import statement used a bare module reference (`from function import f`) which fails when the module is loaded as part of the `calculus` package. This was corrected to a relative import (`from .function import f`), ensuring proper package resolution regardless of how the module is invoked.

### Critical Point Detection

Critical point detection is implemented in `calculus/analysis.py`. The module imports the first derivative and the symbolic variable from the derivatives module, then uses `sp.solve` to find all values of x where the first derivative equals zero. These are the points at which the function transitions between increasing and decreasing behavior. For f(x) = x³ − 3x² + 2, the solver yields two critical points: x = 0 (local maximum) and x = 2 (local minimum).

### Static Visualization

The static plot, implemented in `visualization/static_plot.py`, samples the function over 400 evenly spaced points on the interval [−2, 4] using NumPy's `linspace`. It renders the function curve with labeled axes, a title, reference lines at x = 0 and y = 0, and a legend. The figure dimensions are set to 8 by 5 inches to maintain a clean, readable aspect ratio. This plot serves as the primary reference graphic for the experiment, providing an unambiguous view of the function's complete behavior across the domain of interest.

### Animated Visualization

The animated visualization, implemented in `visualization/animation_plot.py`, uses Matplotlib's `FuncAnimation` to render the function curve progressively, drawing one additional data point per frame across 200 frames with a 20-millisecond interval. This produces a smooth left-to-right drawing effect that reinforces the relationship between the input domain and the output range as the curve is traced in real time.

A structural bug was identified and resolved during development: the `FuncAnimation` constructor call and the `plt.show()` call were incorrectly indented inside the `update` callback function. Because `update` is invoked by the animation engine on each frame, placing the animation constructor inside it meant the animation object was never instantiated and the display was never triggered. Correcting the indentation to place both calls at the `animate_function` scope resolved the issue entirely.

### Experiment Entry Point

The `main.py` entry point coordinates the full experiment in sequence. It imports the derivative expressions from the calculus engine, prints the first and second derivatives to the console in symbolic form, retrieves and prints the critical points, and then calls the static and animated visualization routines in order. All outputs are clearly labeled in the console to make the experiment results self-documenting when run.

---

## Dependencies

This experiment depends on three libraries: NumPy for numerical array operations, Matplotlib for all graphical rendering, and SymPy for symbolic mathematics. All three are declared in the root `requirements.txt` file and can be installed with a single command:

    pip install -r requirements.txt

---

## Running the Experiment

The experiment must be run from the `experiment_01_function_behavior_analysis/` directory to ensure that the package imports resolve correctly:

    cd experiments/experiment_01_function_behavior_analysis
    python main.py

The console will display the first derivative, second derivative, and critical points in symbolic form. A static plot window will appear first, followed by the animated visualization upon closing the static plot.

---

## Limitations

### 1. Single-variable functions only
The entire architecture — `sp.symbols('x')`, `sp.diff(f(x), x)`, `np.linspace` over a 1D domain — is built around a single independent variable. Multi-variable functions (e.g., f(x, y)) would require a complete redesign of the calculus engine and the visualization layer.

### 2. Fixed domain and axis bounds
The plot domain `[-2, 4]` and the animation y-axis range `[-10, 10]` are hardcoded in the visualization files. Swapping in a function whose interesting behavior lies outside these bounds — or whose output scale is very different — produces a misleading or empty plot. There is no automatic domain or range detection.

### 3. `sp.solve` fails or misbehaves on non-polynomial functions
Critical point detection uses `sp.solve(first_derivative, x)`, which works reliably for polynomials. For transcendental functions (e.g., `sin(x)`, `exp(x) * cos(x)`), SymPy either returns an empty list, raises a `NotImplementedError`, or returns a `ConditionSet` representing infinitely many solutions — all of which break the `float(cp)` call in `static_plot.py` with no meaningful error message.

### 4. Non-differentiable functions break the symbolic pipeline
Derivatives are computed at module-load time in `derivatives.py`. If `f(x)` is non-differentiable (e.g., `floor(x)`, `abs(x)`), SymPy either returns a `DiracDelta` or `Piecewise` expression. These expressions cannot be reliably lambdified into NumPy, and `sp.solve` cannot solve them for critical points in the conventional sense. The `floor(x)` test in this experiment directly exposed this failure mode.

### 5. The dual-context function pattern does not scale
Functions that work naturally with both NumPy and SymPy (e.g., standard polynomial arithmetic) require no special treatment. But any function involving a non-algebraic operation (floor, abs, conditional logic) requires a manual `isinstance(x, sp.Basic)` branch to route to the correct implementation. This pattern becomes increasingly fragile and verbose for complex functions.

### 6. Module-level derivative computation gives opaque errors on import failure
Because `first_derivative` and `second_derivative` are computed as module-level expressions in `derivatives.py`, any error in `f(x)` during symbolic evaluation raises an import-time exception. The traceback points to the import chain rather than to the function definition, making it harder to diagnose the root cause.

### 7. No handling for poles and discontinuities in the visualization
Functions with vertical asymptotes (e.g., `1/x`, `tan(x)`) produce `inf` or `nan` values in the NumPy arrays. Matplotlib renders these as a spurious near-vertical line across the discontinuity. There is no masking, clipping, or detection logic in the current plotting code.

### 8. Complex-valued critical points are not filtered
`sp.solve` can return complex-valued roots for functions that have no real critical points (e.g., `x² + 1` has derivative `2x`, which is fine, but more exotic functions may yield complex solutions). The `float(cp)` call in `static_plot.py` will raise a `TypeError` on any complex result without a guard.

### 9. No second-derivative classification of critical points
The critical points are located and plotted, but the code does not programmatically evaluate `f''(x)` at each critical point to label them as local maxima, local minima, or saddle points. This classification is visually implied by the `f''(x)` line but is never stated explicitly in any output.

---

## Key Learnings from Experiment 01

### Symbolic and numerical computation are not interchangeable
The most important design lesson of this experiment was that SymPy and NumPy operate in fundamentally different paradigms. SymPy manipulates symbolic expression trees; NumPy operates on arrays of floating-point numbers. A function written naively in Python (using `**`, `+`, `-`) happens to work with both because Python operator overloading makes the same syntax dispatch to different implementations. The moment a function requires a non-algebraic operation, that silent compatibility breaks and must be handled explicitly.

### `sp.lambdify` is the bridge between the two worlds
`sp.lambdify` translates a SymPy expression into a callable NumPy function, which is why the derivative overlays in `static_plot.py` and the tangent slope in `animation_plot.py` can be computed numerically without re-implementing the derivatives in NumPy. Understanding this bridge — and its limits (it cannot handle all SymPy expressions cleanly) — is central to building hybrid symbolic-numerical pipelines.

### Module-level computation is a convenience with a cost
Computing derivatives at import time in `derivatives.py` makes them available as simple named imports (`from calculus.derivatives import first_derivative`), which simplifies the rest of the codebase. The cost is that errors surface at import time and are harder to trace, and there is no opportunity to pass parameters or swap the function without reloading the module. For a research tool intended to be swapped to different functions regularly, lazy evaluation (computing derivatives inside a function call rather than at module load) would be more robust.

### The second derivative test is best understood visually
Plotting `f(x)`, `f'(x)`, and `f''(x)` together on a single graph makes the second derivative test immediate and intuitive. The zeros of `f'` align vertically with the critical point markers. At those same x-positions, reading the sign of `f''` directly from the dotted line confirms whether the point is a maximum or minimum — no algebra required. This visual confirmation is more instructive than any printed output.

### Non-smooth functions expose the boundaries of the calculus engine
Testing `floor(x)` — a function that is piecewise constant and non-differentiable at every integer — revealed exactly which parts of the pipeline assume smoothness. The symbolic differentiator, the critical-point solver, and the tangent-line animator all implicitly assume a smooth, differentiable function. Extending the system to handle non-smooth functions would require either restricting the pipeline steps that are invoked, or replacing the symbolic solver with a numerical approach (e.g., finding sign changes in a numerically sampled derivative array).

### Animation reveals calculus as a process, not just a result
The animated draw paired with the moving tangent line communicates something that a static plot cannot: derivative is a local, instantaneous property that evolves as you move along the curve. Watching the tangent line flatten near the critical points and steepen in between makes the geometric meaning of the first derivative viscerally clear in a way that a printed symbolic expression does not.

---

## Results

The symbolic engine correctly computes the first derivative as 3x² − 6x and the second derivative as 6x − 6. The critical point solver returns x = 0 and x = 2. Evaluating the second derivative at these points confirms their nature: at x = 0 the second derivative is negative, confirming a local maximum; at x = 2 the second derivative is positive, confirming a local minimum. The static plot clearly shows this behavior, and the animation reproduces it in a frame-by-frame drawing sequence from left to right.

---

## Proposed Advancements

The following directions represent significant opportunities to expand Experiment 01 into a more comprehensive analytical instrument.

**Second Derivative Classification.** The analysis module currently identifies critical points but does not classify them. Applying the second derivative test programmatically at each critical point would automatically label each as a local maximum, local minimum, or inconclusive (saddle) case, and this classification could be annotated directly on the static plot.

**Inflection Point Detection.** Solving the second derivative for zero would yield the inflection point, the location at which the concavity of the function reverses. This is a natural and important companion result to the critical point analysis and could be added to the `analysis.py` module with minimal effort.

**Tangent Line Visualization.** Rendering the tangent line at a user-specified point, using the first derivative as the slope, would make the geometric meaning of the derivative immediately visible. This could be implemented as an interactive slider in Matplotlib's widget system, allowing the user to drag the point of tangency across the domain in real time.

**Definite Integration and Area Computation.** Adding a module that uses SymPy's `sp.integrate` to compute the definite integral over a user-defined interval, and shading the corresponding area under the curve in the static plot, would extend the experiment from pure differential calculus into integral calculus.

**Newton's Method for Root Finding.** Implementing Newton's method as a standalone module would provide a numerical comparison against SymPy's exact solver and would visually demonstrate iterative convergence on the static plot by drawing successive tangent line intersections with the x-axis.

**Derivative Overlay Plot.** Plotting f(x), f'(x), and f''(x) on a single multi-panel or overlaid figure would create a unified view of the function and its rate-of-change properties, making it easy to visually correlate features such as zero crossings of f'(x) with extrema of f(x).

**Taylor Series Approximation.** Using SymPy to expand f(x) around a chosen point as a Taylor polynomial, then plotting both the original function and its approximation, would introduce the concept of local linear and polynomial approximation and lay groundwork for later experiments on series convergence.

**Parametric and Multivariable Extension.** Generalizing the function definition to accept an arbitrary symbolic expression at runtime, rather than hardcoding the cubic polynomial, would transform Experiment 01 from a single-function demonstration into a reusable analysis harness. This would serve as the natural bridge to future experiments involving multivariable functions, partial derivatives, and gradient fields.

**LaTeX Report Export.** Using SymPy's built-in LaTeX printer to render the function, derivatives, and critical point results into a formatted PDF report would make each experiment run self-archiving and suitable for academic documentation.

---

## Notes

This experiment was the first in the Walter Bishop Labs series and serves as the structural template for all subsequent experiments. The separation of concerns between the calculus engine and the visualization layer, combined with the single-entry-point orchestration pattern in `main.py`, is a design convention that all future experiments in this repository should follow.
