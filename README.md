# Walter Bishop Labs: Calculus Experiments

Walter Bishop Labs is a computational mathematics repository built to study calculus as an experimental science. Instead of treating formulas as static results, this project treats each concept as a system that can be modeled, differentiated, visualized, tested, and extended in code.

The lab currently focuses on single-variable and multivariable intuition through symbolic analysis, numerical sampling, and visual interpretation. The long-term direction is a modular experiment suite where each topic can move from theory to implementation to interpretation in a repeatable workflow.

## Research Direction

The project is designed around four principles. The first is conceptual clarity, where every experiment should expose the geometric and physical meaning behind the mathematics. The second is computational rigor, where symbolic tools are used when exactness matters and numerical tools are used when simulation and scale matter. The third is visual intelligence, where plots and animations are used to reveal structure, not only to decorate output. The fourth is extensibility, where each experiment serves as a reusable module for future topics.

## Current Scope

The present codebase explores core calculus foundations that support later work in optimization, modeling, and differential systems. Topics include continuity behavior, derivatives, partial derivatives, gradient-based reasoning, optimization intuition, and introductory differential equation patterns.

## Repository Layout

The repository is organized as a sequence of experiments under the [experiments](experiments) directory. Each experiment is intended to include a self-contained implementation with a clear entry point, mathematical logic under a calculus module, and one or more visualization modules.

The first complete implementation is available in [experiments/experiment_01_function_behavior_analysis](experiments/experiment_01_function_behavior_analysis), where symbolic derivatives, critical points, and both static and animated visualizations are integrated into a single analysis pipeline.

## Quick Start

To run the lab locally, create a Python environment, install dependencies, and execute an experiment entry point.

```bash
pip install -r requirements.txt
cd experiments/experiment_01_function_behavior_analysis
python main.py
```

## Methodology

Each experiment follows a consistent lifecycle. A target function or system is first defined as a computational object. The system is then analyzed symbolically to produce mathematically exact derivatives or transforms. Numerical sampling is introduced for plotting and simulation where dense evaluation is required. Finally, outputs are interpreted through visual and textual reporting so that conclusions are not only computed but explained.

## What Makes This Lab Different

Most educational repositories stop at producing the right numeric answer. Walter Bishop Labs is structured to expose why behavior emerges. The aim is to connect symbolic structure with visual behavior and then connect that behavior to modeling decisions. This approach supports students, researchers, and engineers who want calculus to function as an investigative tool rather than a memorization exercise.

## Near-Term Expansion

Upcoming work will expand Experiment 01 into a broader analysis instrument by adding automatic critical point classification, inflection point detection, tangent-line dynamics, integral area visualization, and approximation modules such as Taylor-series expansion. Future experiments will generalize these ideas to multivariable surfaces, vector fields, and constrained optimization systems.

## Contributing

Contributions are welcome when they improve mathematical clarity, computational correctness, or visual interpretability. Proposed changes should preserve the experiment-first structure and include enough context that the mathematical intent is evident from code and output.

## License

This project currently has no license file defined in the repository root. If public collaboration is planned, adding an explicit open-source license is recommended so usage and contribution terms are unambiguous.
