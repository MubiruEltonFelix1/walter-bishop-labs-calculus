# Understanding Experiment 05

## Big Picture

Convergence and divergence are not only abstract properties.
They indicate whether repeated updates and accumulations are operationally stable.

A convergent sequence often means a recursive system settles to a predictable regime.
A divergent sequence often means growth is unchecked under the current update rule.

For series, the partial sum trend matters more than individual term size.
Terms can become small while the total still grows without bound (harmonic behavior).

## Case Interpretation

1. Temperature stabilization sequence
The update rule blends current temperature with ambient temperature. Because the carry-over factor stays below 1 in magnitude, the sequence approaches a stable fixed point.

2. Compound debt growth sequence
Each step multiplies the current balance by a factor greater than 1. Repetition creates exponential growth, so the sequence diverges.

3. Discounted cash-flow geometric series
Each future cash flow is discounted by a constant ratio below 1. The partial sums approach a finite present value.

4. Maintenance backlog harmonic series
Each added overhead term shrinks, but not fast enough for bounded accumulation. Partial sums continue to grow, confirming divergence.

5. Alternating correction series
Alternating sign and shrinking magnitude can produce conditional convergence. Partial sums oscillate around a finite target and tighten over time.

## Why Animations Help

Static plots show the current shape.
Animations show the path taken to get there.

In this experiment, animation makes two ideas immediate:

1. Recursive trajectories can settle or explode over the same step horizon.
2. Partial sums can stabilize, oscillate toward a limit, or drift upward indefinitely.

## Practical Transfer

These patterns appear in many domains:

1. Feedback loops in control systems
2. Debt and investment growth models
3. Discounted valuation and financial planning
4. Reliability overhead and retry strategies
5. Iterative optimization and correction routines
