# Walter Bishop Labs: Calculus Experiments

I built this repository to help me understand calculus the way I wish it was taught in class: not just formulas to memorize, but ideas I can test, visualize, and play with in code.

Instead of treating calculus as "finished math on paper", I use Python to ask practical questions like:
- Where is this function increasing or decreasing?
- Why does a turning point happen at this exact x-value?
- How does changing parameters affect the best decision?

## Why I Built This

In lectures, abstract concepts like derivatives, curvature, optimization, and sensitivity can feel disconnected. I designed these experiments to close that gap:
- I start with the math from class
- I encode it in code
- I visualize the behavior
- I interpret the result in plain language

My goal is to make calculus feel intuitive, not mysterious.

## Current Scope

Right now I focus on two connected experiments:

1. Function behavior analysis (single-variable)
2. Optimization and sensitivity analysis (turning calculus into decisions)

These are early-stage student lab experiments, not a polished research framework.

## Repository Layout

The project is organized under [experiments](experiments):

- [experiments/experiment_01_function_behavior_analysis](experiments/experiment_01_function_behavior_analysis)
  - I analyze one function deeply using symbolic derivatives and visualizations.
- [experiments/experiment_02_optimisation_and_sensitivity_analysis](experiments/experiment_02_optimisation_and_sensitivity_analysis)
  - I extend the same ideas to optimization, constraints, and robustness checks.

## Quick Start

```bash
pip install -r requirements.txt
cd experiments/experiment_01_function_behavior_analysis
python main.py
```

## How I Work in Each Experiment

My usual workflow is:

1. Define a function
2. Compute derivatives symbolically (with SymPy)
3. Find candidate points (like critical points)
4. Sample numerically for plotting
5. Interpret the results from both math and visuals

This keeps the project close to classroom calculus while still being practical.

## What Makes This Different (For Me)

Many examples online stop at "here is the correct answer".
I care more about "why this answer makes sense".

So I always try to connect:
- symbolic result
- geometric meaning
- practical decision

## Near-Term Next Steps

I plan to keep improving these experiments by adding:
- automatic classification of critical points
- inflection point detection
- better tangent-line intuition tools
- clearer sensitivity visuals
- more reusable experiment templates

## Contributing

If you want to contribute, I welcome changes that improve:
- conceptual clarity
- correctness of the math/code
- interpretability of outputs

Please keep the style educational and practical.

## License

There is currently no license file in the repository root.
If this project goes public for broader collaboration, I should add one.
