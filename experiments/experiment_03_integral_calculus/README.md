# Experiment 03: Smart Mobility Energy and Load Accumulation

## Why This Experiment Exists

This experiment is where integration stops feeling like a chapter and starts feeling like infrastructure.

In real systems, we rarely care only about what happens at one instant. We care about what builds up over time. How much energy was consumed during a commute window? How much distance was covered under variable speed? How much workload accumulated in a system where demand never stays flat?

That is the heartbeat of integral calculus: turning changing rates into decision-ready totals.

The goal here is not to copy formulas from notes into code. The goal is to build confidence that integration can be used as a practical tool in modern contexts, especially where data is sampled, noisy, and operationally important.

## The Core Question

If you only observe a process in pieces, how accurately can you recover the full accumulated story?

This is the same question behind battery analytics, telemetry pipelines, fleet monitoring, and many optimization systems. In mathematical language, it is the question of definite integration. In engineering language, it is the question of trustworthy accumulation.

## Conceptual Bridge: From Local Change to Total Impact

Derivatives tell us how fast something is changing right now. Integrals tell us what those changes add up to across an interval. In this experiment, that bridge becomes tangible:

$$
	ext{Distance} = \int \text{Speed}(t)\,dt, \qquad
	ext{Energy} = \int \text{Power}(t)\,dt, \qquad
	ext{Work} = \int \text{Force}(x)\,dx
$$

The Fundamental Theorem of Calculus is not treated as theory decoration. It is treated as a translator between model expressions and measurable totals.

## What Makes This Experiment Different

This experiment is designed as an analysis workflow, not a worksheet.

You run symbolic and numerical methods side by side. You look at convergence, not only final values. You inspect the geometry of approximation, not only the printed answer. Most importantly, you interpret results as evidence for decisions, not just as mathematically correct outputs.

Instead of asking only, "What is the integral?", we ask:

1. How sensitive is this estimate to method choice?
2. How quickly does error shrink as $n$ grows?
3. When is a quick approximation good enough for operational use?
4. When does the problem demand higher numerical care?

## Experiment Narrative

The run is structured as a sequence with a clear story arc.

It begins with antiderivatives to establish model primitives. It then moves to definite integrals as accumulated totals. After that, numerical estimation methods are compared directly so you can see the trade-offs between simplicity and accuracy. Finally, applied scenarios are interpreted in practical terms: area, volume, work, average behavior, and sensor-style accumulation.

The visualizations are not decorative. They are part of the reasoning process. Seeing rectangles and trapezoids converge toward a stable value is often the fastest way to internalize what numerical integration is really doing.

## Running It

Run from the experiment folder:

```bash
python main.py
```

If you want interactive one-by-one plot windows:

```bash
python run_interactive.py
```

Outputs are saved in:

1. outputs/plots
2. outputs/reports

## How to Read the Results

Treat the report as an engineering memo.

The absolute values matter, but the relationships matter more: which methods agree, which methods diverge, and under what discretization settings the solution becomes stable enough to trust. If two methods disagree materially, that is not a failure; it is information about uncertainty.

When the experiment reaches a function without a convenient elementary antiderivative, numerical methods become the main engine. This reflects real work, where exact closed forms are often unavailable and evidence quality depends on approximation discipline.

## Why This Matters Beyond Calculus Class

This style of integration thinking appears everywhere: energy metering, mobility analytics, demand forecasting, operational load tracking, even financial accumulation models.

So the value of this experiment is not only that it teaches Chapter 4 well. It teaches how to reason when you have partial observations and need reliable totals anyway. That is a modern analytical skill.

## File Structure

```
experiment_03_integral_calculus/
├── settings.py
├── understanding.md
├── main.py
├── run_interactive.py
├── calculus/
├── integration/
├── visualization/
├── reporting/
└── outputs/
```

## Closing Motivation

If Experiment 1 helped us understand local behavior, and Experiment 2 helped us choose good operating points, Experiment 3 helps us answer the question stakeholders usually care about first: what is the total impact over time?

That is why this experiment sits naturally in the repository journey. It turns calculus from local insight into accumulated evidence.
