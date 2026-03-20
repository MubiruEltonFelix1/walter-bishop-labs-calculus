# Experiment 01 - Function Behavior Analysis

Walter Bishop Labs  
Date: March 15, 2026  
Status: Complete

---

## What I Wanted to Learn

For this first experiment, I wanted to make derivative ideas from class more visual and practical.
I specifically wanted to move from "I can compute the derivative" to "I can explain what the derivative means on a graph and in a decision context."

I used the function:

$$f(x) = x^3 - 3x^2 + 2$$

I picked this function because it is simple enough to follow but still interesting: it has turning points, roots, and an inflection point.

That makes it a strong teaching function for first-pass calculus intuition.

---

## What I Built

I built a small pipeline that does four things:

1. Defines the function in code
2. Computes $f'(x)$ and $f''(x)$ symbolically
3. Finds critical points by solving $f'(x)=0$
4. Visualizes the function using static and animated plots

I designed the pipeline as a reusable template, so later experiments can keep the same flow and only swap mathematical complexity.

---

## Audience and Intent

I wrote this experiment to work for two reading modes:

1. Lecturer reading mode: clear objective, clear method, clear evidence.
2. Student/advanced reader mode: enough technical depth to inspect implementation choices and limitations.

So the style is intentionally practical, but still structured and rigorous.

---

## Project Structure

```text
experiment_01_function_behavior_analysis/
    main.py
    calculus/
        function.py
        derivatives.py
        analysis.py
    visualization/
        static_plot.py
        animation_plot.py
```

- `calculus/` contains the math logic
- `visualization/` contains the plotting logic
- `main.py` runs everything in order

This separation helps keep mathematical logic independent from plotting details.

---

## How I Implemented It

### 1. Function Definition

In `calculus/function.py`, I defined the function so it can work with both scalar values and arrays.
That helps me use the same function for symbolic analysis and plotting.

This was an important design decision because duplicate function definitions often create mismatch bugs.

### 2. Symbolic Derivatives

In `calculus/derivatives.py`, I use SymPy to compute:
- first derivative $f'(x)$
- second derivative $f''(x)$

These let me study slope and curvature directly.

I use symbolic derivatives first because they preserve exactness and make the analysis traceable.

### 3. Critical Points

In `calculus/analysis.py`, I solve $f'(x)=0$.
For this function, I get:
- $x=0$
- $x=2$

These are the candidate points where local behavior can switch from increasing to decreasing (or the reverse).

### 4. Visualizations

- `visualization/static_plot.py` draws a clean static graph.
- `visualization/animation_plot.py` draws the curve gradually so I can watch behavior build from left to right.

The animation is especially useful for classroom explanation because it emphasizes calculus as a process, not just a final static result.

---

## How to Run

From this experiment folder:

```bash
cd experiments/experiment_01_function_behavior_analysis
python main.py
```

You should see:
1. derivative expressions in the console
2. critical points in the console
3. static plot window
4. animation window

If import paths fail, make sure the command is run from this experiment directory.

---

## Quick Verification Checks

After running once, I use these checks to confirm the implementation is healthy:

1. Console prints first derivative exactly as $3x^2 - 6x$.
2. Console prints second derivative exactly as $6x - 6$.
3. Critical points list contains $x=0$ and $x=2$.
4. Static plot and animation windows open without import/runtime errors.

---

## Expected Output Snapshot

Minimal console snippet I expect:

```text
Run seed: 42

First derivative:
3*x**2 - 6*x

Second derivative:
6*x - 6

Critical points:
[0, 2]
```

---

## Main Results

For the chosen function:

- $f'(x)=3x^2-6x$
- $f''(x)=6x-6$
- critical points: $x=0$ and $x=2$

Using the second derivative test:
- at $x=0$, $f''(0)<0$ so it is a local maximum
- at $x=2$, $f''(2)>0$ so it is a local minimum

These results are consistent between symbolic output and visual interpretation, which increases confidence in the implementation.

---

## Why This Matters Conceptually

This experiment reinforces three core ideas from introductory calculus:

1. Critical points come from $f'(x)=0$.
2. Local classification comes from the sign of $f''(x)$.
3. Graph behavior and derivative behavior should tell the same story.

In this project, I verify all three with both code and plots.

---

## What I Learned

1. Symbolic math and numerical plotting are different worlds, and I need a good bridge between them.
2. Visualizing $f(x)$ with derivative information makes class concepts click much faster.
3. Animation helps me understand derivative as a local process, not just a formula.
4. Good file structure matters early; it makes later experiments easier to extend and debug.

---

## Current Limitations

This is still a student experiment, so there are limits:

- only 1D single-variable functions
- fixed plotting bounds in some places
- symbolic solver may fail for harder/non-smooth functions
- no automatic classification labels on plots yet
- limited error handling for pathological function types

I list these limits explicitly to avoid overstating what the current version can do.

---

## Next Improvements I Plan

- automatic max/min/inconclusive labels
- inflection point detection
- better handling of non-smooth or discontinuous functions
- more interactive tangent-line exploration
- optional derivative overlays in one integrated figure
- cleaner validation and test checks around solver outputs

---

## Troubleshooting

1. `ModuleNotFoundError` for local packages:
Run from `experiments/experiment_01_function_behavior_analysis` before calling `python main.py`.

2. Plot window does not open in headless/remote environments:
Switch Matplotlib backend or run on a local desktop session.

3. Unexpected symbolic output formatting:
SymPy may print equivalent algebra in a different form. Verify mathematical equivalence, not only string formatting.

---

## Notes

I treat this experiment as the foundation for the rest of the project.
The structure here (math module + visualization module + single entry script) is the pattern I keep while hardening the first two experiments.

Even though the mathematics is introductory, I wrote this as serious training for translating abstract calculus into computational reasoning.
