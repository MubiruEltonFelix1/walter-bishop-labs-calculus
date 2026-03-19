# Experiment 01 - Function Behavior Analysis

Walter Bishop Labs  
Date: March 15, 2026  
Status: Complete

---

## What I Wanted to Learn

For this first experiment, I wanted to make derivative ideas from class more visual and practical.

I used the function:

$$f(x) = x^3 - 3x^2 + 2$$

I picked this function because it is simple enough to follow but still interesting: it has turning points, roots, and an inflection point.

---

## What I Built

I built a small pipeline that does four things:

1. Defines the function in code
2. Computes $f'(x)$ and $f''(x)$ symbolically
3. Finds critical points by solving $f'(x)=0$
4. Visualizes the function using static and animated plots

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

---

## How I Implemented It

### 1. Function Definition

In `calculus/function.py`, I defined the function so it can work with both scalar values and arrays.
That helps me use the same function for symbolic analysis and plotting.

### 2. Symbolic Derivatives

In `calculus/derivatives.py`, I use SymPy to compute:
- first derivative $f'(x)$
- second derivative $f''(x)$

These let me study slope and curvature directly.

### 3. Critical Points

In `calculus/analysis.py`, I solve $f'(x)=0$.
For this function, I get:
- $x=0$
- $x=2$

### 4. Visualizations

- `visualization/static_plot.py` draws a clean static graph.
- `visualization/animation_plot.py` draws the curve gradually so I can watch behavior build from left to right.

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

---

## Main Results

For the chosen function:

- $f'(x)=3x^2-6x$
- $f''(x)=6x-6$
- critical points: $x=0$ and $x=2$

Using the second derivative test:
- at $x=0$, $f''(0)<0$ so it is a local maximum
- at $x=2$, $f''(2)>0$ so it is a local minimum

---

## What I Learned

1. Symbolic math and numerical plotting are different worlds, and I need a good bridge between them.
2. Visualizing $f(x)$ with derivative information makes class concepts click much faster.
3. Animation helps me understand derivative as a local process, not just a formula.

---

## Current Limitations

This is still a student experiment, so there are limits:

- only 1D single-variable functions
- fixed plotting bounds in some places
- symbolic solver may fail for harder/non-smooth functions
- no automatic classification labels on plots yet

---

## Next Improvements I Plan

- automatic max/min/inconclusive labels
- inflection point detection
- better handling of non-smooth or discontinuous functions
- more interactive tangent-line exploration

---

## Notes

I treat this experiment as the foundation for the rest of the project.
The structure here (math module + visualization module + single entry script) is the pattern I want to keep as I add more experiments.
