# Experiment 05: Practical Convergence and Divergence for Sequences and Series

## Why This Experiment Exists

This experiment translates convergence and divergence from textbook definitions into practical system behavior.

Instead of asking only whether a limit exists, it asks operational questions:

1. Will a recursive process stabilize or explode?
2. Will accumulated effects stay bounded or keep growing?
3. How does this change decisions in engineering and finance contexts?

## Suggested Practical Mini-Experiments

Before coding, these are the proposed mini-experiments this module is built around:

1. Thermal stabilization in a cooling pipeline (convergent sequence)
2. Compound debt growth under monthly interest (divergent sequence)
3. Infinite discounted cash-flow valuation (convergent geometric series)
4. Accumulated overhead from repeated retries (divergent harmonic series)
5. Alternating correction updates in control tuning (conditionally convergent series)

## What Is Implemented

This experiment implements all five mini-experiments above and provides:

1. Sequence generators and diagnostics for convergence/divergence behavior.
2. Series term generation with partial-sum tracking.
3. Static plots for each case and direct comparison charts.
4. Animated graphs exported as HTML for sequence progression and partial-sum evolution.
5. A consolidated report summarizing expected versus detected behavior.

## Run

From this experiment directory:

python main.py

Optional interactive mode (shows plot windows):

python run_interactive.py

## Output Artifacts

Generated files are saved to:

1. outputs/plots
2. outputs/reports

Expected artifacts include PNG plots and HTML animations.

## Folder Structure

experiment_05_series_sequence_convergence_applications/
|- settings.py
|- main.py
|- run_interactive.py
|- README.md
|- understanding.md
|- calculus/
|- visualization/
|- reporting/
|- outputs/

## Notes

1. The harmonic series diverges slowly, so divergence is visible in cumulative trend rather than term magnitude.
2. The alternating correction series converges conditionally, so partial sums oscillate while narrowing around the limit.
