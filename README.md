# Walter Bishop Labs: Calculus Experiments

I built this repository to help me understand calculus in a way that complements what I learn in class: not only as formulas to memorize, but as ideas I can test, visualize, and apply.

Instead of treating calculus as finished math on paper, I use Python to ask practical questions such as:
- Where is this function increasing or decreasing?
- Why does a turning point happen at this exact value of $x$?
- Which operating point is best when constraints are present?
- How stable is that recommendation if assumptions change?

## Why I Built This

In lectures, abstract concepts like derivatives, curvature, optimization, and sensitivity can feel disconnected. I designed these experiments to close that gap:
- I start with the math from class
- I encode it in code
- I visualize the behavior
- I interpret the result in plain language

My goal is to make calculus feel intuitive, explainable, and useful for decision-making.

I still treat this as a student project, but I want the documentation to be organized enough that a lecturer, a teaching assistant, or an experienced reader can quickly understand the technical intent.

## Who This Is For

I wrote this repository for three groups of readers:

1. Students who want a practical bridge between lecture theory and computation.
2. Lecturers who want to assess conceptual understanding through reproducible experiments.
3. Experienced readers (including multivariable-calculus learners) who want a clean base that can be extended beyond 1D examples.

## Current Scope

Right now I focus on two connected experiments:

1. Function behavior analysis (single-variable)
2. Optimization and sensitivity analysis (turning calculus into decisions)

These are student-led lab experiments with a structured methodology, not a polished research framework yet.

## Repository Layout

The project is organized under [experiments](experiments):

- [experiments/experiment_01_function_behavior_analysis](experiments/experiment_01_function_behavior_analysis)
  - I analyze one function in depth using symbolic derivatives and visual intuition.
- [experiments/experiment_02_optimisation_and_sensitivity_analysis](experiments/experiment_02_optimisation_and_sensitivity_analysis)
  - I extend the same ideas to optimization, constraints, and robustness checks.

Supporting documents at the repository root summarize progression and learning flow across experiments.

## Quick Start

```bash
pip install -r requirements.txt
cd experiments/experiment_01_function_behavior_analysis
python main.py
```

If you want to run Experiment 02:

```bash
cd experiments/experiment_02_optimisation_and_sensitivity_analysis
python main.py
```

## How I Work in Each Experiment

My usual workflow is:

1. Define a function
2. Compute derivatives symbolically (with SymPy)
3. Find candidate points (like critical points)
4. Sample numerically for plotting
5. Interpret the results from both math and visuals
6. Convert math insight into a clear recommendation (when applicable)

This keeps the project close to classroom calculus while still being practical and auditable.

## Technical Approach

I intentionally combine two computation styles:

- Symbolic computation (SymPy): for exact derivatives, exact candidate discovery, and mathematical transparency.
- Numerical computation (NumPy/Matplotlib): for dense sampling, plotting, animation, and practical behavior checks.

This hybrid approach helps me avoid two extremes: pure symbolic work with limited visual intuition, and pure numerical work with weak algebraic traceability.

## What Makes This Different (For Me)

Many examples online stop at "here is the correct answer".
I care more about "why this answer makes sense".

So I always try to connect:
- symbolic result
- geometric meaning
- practical decision

## Learning Outcomes I Target

After running these experiments, I expect to be able to:

1. Derive and interpret $f'(x)$ and $f''(x)$ in a computational setting.
2. Link critical points to geometric behavior (max/min/concavity transitions).
3. Compare symbolic and numerical optimization strategies.
4. Explain sensitivity and robustness in plain language.
5. Communicate findings in a report format that is mathematically correct but still readable.

## Near-Term Next Steps

I plan to keep improving these experiments by adding:
- automatic classification of critical points
- inflection point detection
- better tangent-line intuition tools
- clearer sensitivity visuals
- more reusable experiment templates

I also plan to begin a multivariable extension track after the current single-variable pipeline is stable and well-tested.

## Quality and Limitations

I aim for conceptual clarity first, then engineering polish. Current limitations include:

- heavy focus on 1D objective functions
- function-class assumptions that can break for non-smooth expressions
- manual parameterization choices in some modules
- early-stage reporting and testing depth

I document these limitations intentionally so readers can evaluate scope and trust level correctly.

## Contributing

If you want to contribute, I welcome changes that improve:
- conceptual clarity
- correctness of the math/code
- interpretability of outputs

Please keep the style educational, practical, and technically grounded.

## License

There is currently no license file in the repository root.
If this project goes public for broader collaboration, I should add one.
