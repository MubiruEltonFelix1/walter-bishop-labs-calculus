# Settings Configuration Guide (Experiment 01 + Experiment 02)

## Why this document exists

I created this guide to make `settings.py` easy to reason about as an experiment control panel, not just a list of constants.

My goals here are to explain:

1. What each setting is.
2. How each setting flows into code behavior.
3. Why the setting exists (design intention).
4. What to adjust for specific outcomes.
5. Real-world scenarios where these adjustments are useful.
6. Why this approach is better than hardcoding values directly in logic modules.

---

## The core idea: `settings.py` is experimental methodology

In both experiments, `settings.py` defines assumptions and operating conditions.

- In Experiment 01, settings mostly control reproducibility and visualization quality/speed.
- In Experiment 02, settings define parts of the optimization problem itself (feasible bounds, objective direction, numerical start point, sensitivity sweep intensity).

This means changing settings is not cosmetic. It can change scientific conclusions.

---

## Where settings are consumed

### Experiment 01

- File: `experiments/experiment_01_function_behavior_analysis/settings.py`
- Imported in:
  - `main.py` for run seed
  - `visualization/static_plot.py` for plotting domain and resolution
  - `visualization/animation_plot.py` for animation domain, frame density, and speed

### Experiment 02

- File: `experiments/experiment_02_optimisation_and_sensitivity_analysis/settings.py`
- Imported in:
  - `main.py` for experiment-wide execution parameters
  - `analysis/sensitivity.py` for default perturbation grid fallback

---

## Design philosophy behind this structure

### 1) Single source of truth

One value is defined once and reused across the pipeline. This avoids mismatch bugs where one module assumes one domain while another module assumes a different one.

### 2) Reproducibility first

A fixed seed (`RUN_SEED = 42`) preserves run consistency and keeps outputs stable across reruns and environments, even if current logic is mostly deterministic.

### 3) Separation of concerns

Math and optimization modules focus on algorithms. Settings and scenario definitions live in one dedicated place.

### 4) Fast experimentation

I can run controlled what-if analysis by editing one file instead of modifying many modules.

### 5) Teaching and auditability

A reviewer can inspect settings first to understand assumptions before reading the full implementation.

---

## Experiment 01 settings in depth

File: `experiments/experiment_01_function_behavior_analysis/settings.py`

### `RUN_SEED = 42`

What it controls:

- Numpy random seed initialization in `main.py`.

Why it exists:

- Keeps reproducibility policy consistent across the repository.
- Future-proofs the experiment if random sampling/noise is added later.

If adjusted:

- Current visible behavior may not change much now.
- Future stochastic behavior would become run-dependent.

Typical real-world use case:

- Classroom demo where everyone should see identical result traces.

Pros vs not using a seed:

- With seed: repeatable output, easier debugging, fair comparisons.
- Without seed: hard to compare runs; accidental drift can look like algorithmic change.

---

### `PLOT_DOMAIN = (-2.0, 4.0)`

What it controls:

- Horizontal x-window for static and animated plots.

Why it exists:

- Keeps both visualizations centered on meaningful behavior (critical points and curve shape transitions).

If adjusted:

- Wider range: more context, potentially less detail around key points.
- Narrower range: more detail, less global intuition.

Real-world use case:

- Stakeholder asks for local behavior around a known operating region only.

Pros vs hardcoding in plotting functions:

- With setting: one edit updates all relevant plots.
- Hardcoded: risk of inconsistent domains between static and animation plots.

---

### `PLOT_POINTS = 400`

What it controls:

- Number of sampled x-values in static plot generation.

Why it exists:

- Balances curve smoothness with speed.

If adjusted:

- Higher (e.g., 800–1200): smoother visuals, more compute.
- Lower (e.g., 120–250): faster rendering, possible jagged curves.

Real-world use case:

- Low-power classroom machine where plotting lag needs reduction.

Pros vs fixed hidden value:

- With setting: explicit quality/performance tradeoff.
- Hardcoded: optimization requires code edits and risks accidental logic changes.

---

### `ANIMATION_POINTS = 200`

What it controls:

- Number of animation frames from start to end of domain.

Why it exists:

- Controls granularity of tangent-motion story.

If adjusted:

- More points: smoother animation and denser tangent updates.
- Fewer points: faster completion but coarser motion.

Real-world use case:

- Live lecture with strict time budget: reduce points for a shorter animation.

Pros vs no setting:

- With setting: predictable demo timing.
- Without setting: timing can vary unpredictably after code changes.

---

### `ANIMATION_INTERVAL_MS = 20`

What it controls:

- Delay between animation frames (milliseconds).

Why it exists:

- Decouples visual pacing from frame count.

If adjusted:

- Smaller (10–15): faster animation.
- Larger (30–60): slower and easier to narrate.

Real-world use case:

- Slowing the animation for conceptual walkthrough of tangent interpretation.

Pros vs hardcoded interval:

- With setting: quick pacing changes for different audiences.
- Hardcoded: every pacing change requires code surgery.

---

## Experiment 02 settings in depth

File: `experiments/experiment_02_optimisation_and_sensitivity_analysis/settings.py`

### `RUN_SEED = 42`

What it controls:

- Run-level random state initialization in `main.py`.

Why it exists:

- Consistent repository-level reproducibility policy.

If adjusted:

- Immediate effect may be limited now, but keeps future stochastic additions controlled.

Real-world use case:

- Comparing two algorithm versions where only code should differ, not random state.

Pros vs no seed:

- With seed: fair A/B comparison.
- Without seed: result variability can mask regressions.

---

### `BOUNDS = (-0.5, 3.5)`

What it controls:

- Feasible interval for constrained optimization.
- Domain assumptions used by recommendation and sensitivity stages.

Why it exists:

- Real systems always operate under constraints (safety, budget, physical limits).

If adjusted:

- Tight bounds can force boundary recommendations.
- Wide bounds can reveal interior optima.

Real-world use case:

- Process engineering: actuator/temperature/pressure cannot exceed safe limits.

Pros vs unconstrained-only approach:

- With bounds: actionable recommendations that can actually be implemented.
- Without bounds: mathematically valid but operationally impossible suggestions.

---

### `DIRECTION = 'minimize'`

What it controls:

- Whether the recommendation selects min or max objective candidate.

Why it exists:

- Same mathematics, different business goals (cost minimization vs yield maximization).

If adjusted:

- `'maximize'` flips recommendation target.

Real-world use case:

- Minimize energy cost during normal operations; maximize throughput during high-demand events.

Pros vs duplicating code for min/max:

- With direction setting: one reusable pipeline supports both goals.
- Without setting: duplicated code paths increase maintenance risk.

---

### `PLOT_DOMAIN = (-1.0, 4.0)`

What it controls:

- Display window of the objective plot, separate from feasible bounds.

Why it exists:

- Visual context and feasible context are different concerns.

If adjusted:

- Can zoom out for global shape or zoom in for decision-region detail.

Real-world use case:

- Executive presentation: zoom in around feasible range to emphasize decision relevance.

Pros vs tying plot range to bounds only:

- With separate setting: clearer communication flexibility.
- Without it: plots may hide useful context or overemphasize irrelevant zones.

---

### `NUMERICAL_X0 = 2.5`

What it controls:

- Initial point for gradient descent and Newton's method.

Why it exists:

- Numerical optimization behavior depends on initial condition.

If adjusted:

- Can change convergence speed, path, and in harder problems final local optimum.

Real-world use case:

- Warm-starting from previous cycle's operating point in online optimization.

Pros vs buried initial value:

- With setting: transparent and easy to justify in reports.
- Hardcoded: hidden assumption that can silently bias outcomes.

---

### `PERTURBATION_GRID = [-0.20, -0.10, 0.0, 0.10, 0.20]`

What it controls:

- Fractional perturbation levels for sensitivity analysis.

Why it exists:

- Robustness claims should be stress-tested under controlled parameter changes.

If adjusted:

- Wider grid (e.g., ±30%): stronger stress test, potentially less realistic.
- Narrow grid (e.g., ±5%): realistic fine-grained local sensitivity.
- More points: better resolution, more runtime and denser plots.

Real-world use case:

- Supply chain volatility testing: cost coefficient uncertainty under market swings.

Pros vs single-point analysis:

- With grid: trend-level understanding of stability and fragility.
- Without grid: false confidence from one nominal scenario.

---

## Adjustment playbook: what to change for specific goals

## Goal A: Faster runtime during development

Recommended adjustments:

- Experiment 01: reduce `PLOT_POINTS` and `ANIMATION_POINTS`; increase `ANIMATION_INTERVAL_MS` only if you also want less CPU pressure during playback.
- Experiment 02: use fewer `PERTURBATION_GRID` points.

Good starter set:

- Exp01: `PLOT_POINTS = 250`, `ANIMATION_POINTS = 120`
- Exp02: `PERTURBATION_GRID = [-0.10, 0.0, 0.10]`

Tradeoff:

- Faster iteration, less visual and sensitivity resolution.

---

## Goal B: Publication-quality visuals

Recommended adjustments:

- Increase `PLOT_POINTS` (Exp01) and keep a meaningful `PLOT_DOMAIN`.
- Keep `ANIMATION_POINTS` reasonably high if capturing demo videos.

Good starter set:

- Exp01: `PLOT_POINTS = 900`, `ANIMATION_POINTS = 280`

Tradeoff:

- Better visual smoothness at the cost of render time.

---

## Goal C: More conservative robustness claims

Recommended adjustments:

- Expand `PERTURBATION_GRID` range and/or increase grid density.

Good starter set:

- `PERTURBATION_GRID = [-0.30, -0.20, -0.10, 0.0, 0.10, 0.20, 0.30]`

Tradeoff:

- More realistic stress envelope for uncertainty; more compute and potentially noisier interpretation.

---

## Goal D: Reflect operational constraints accurately

Recommended adjustments:

- Edit `BOUNDS` first.
- Keep `PLOT_DOMAIN` broad enough to show what is feasible vs infeasible.

Good starter set:

- If physical process allows only positive control values: `BOUNDS = (0.0, 3.0)`

Tradeoff:

- Decisions become more deployable and policy-compliant.

---

## Goal E: Switch objective strategy without rewriting the pipeline

Recommended adjustments:

- Change `DIRECTION` from `'minimize'` to `'maximize'` when business objective flips.

Tradeoff:

- Massive code reuse with one setting change; lower chance of implementation drift.

---

## Real-world scenario map

### Scenario 1: Plant safety envelope tightened by regulation

Change:

- Reduce or shift `BOUNDS`.

Why:

- Feasible recommendations must obey legal/safety ranges.

Benefit vs not changing:

- With adjustment: recommendations remain implementable.
- Without adjustment: optimizer may propose non-compliant setpoints.

### Scenario 2: Analyst preparing a board presentation

Change:

- Narrow `PLOT_DOMAIN` near feasible region; increase `PLOT_POINTS` for cleaner visuals.

Why:

- Communication clarity over raw computation speed.

Benefit vs not changing:

- With adjustment: cleaner narrative and visual trust.
- Without adjustment: cluttered or coarse visuals weaken decision confidence.

### Scenario 3: Rapid model iteration in a hack sprint

Change:

- Reduce `PLOT_POINTS`, `ANIMATION_POINTS`, and perturbation grid size.

Why:

- Turnaround speed is critical early in ideation.

Benefit vs not changing:

- With adjustment: many more experiments per hour.
- Without adjustment: slow cycle time, fewer tested ideas.

### Scenario 4: Uncertainty in coefficient estimates increased

Change:

- Widen `PERTURBATION_GRID` and optionally add more grid points.

Why:

- Robustness claims must cover plausible parameter uncertainty.

Benefit vs not changing:

- With adjustment: fewer surprises in deployment.
- Without adjustment: fragile recommendations may fail under mild drift.

### Scenario 5: Objective changed from cost reduction to output maximization

Change:

- Set `DIRECTION = 'maximize'`.

Why:

- Same model, different business objective.

Benefit vs not changing:

- With adjustment: immediate policy alignment.
- Without adjustment: systematically wrong recommendations.

---

## Benefits of settings-driven design vs hardcoded design

### Settings-driven (current design)

Pros:

- Explicit assumptions.
- Faster controlled experimentation.
- Better reproducibility and auditability.
- Lower risk of cross-module inconsistency.
- Cleaner separation between methodology and implementation.

### Hardcoded constants in algorithm/plot files

Costs:

- Hidden assumptions.
- More fragile code edits for routine what-if analysis.
- Easier to introduce contradictions across modules.
- Harder to review, teach, and defend results.

---

## Practical safety checks before and after changes

Before changing settings:

1. State the reason (speed, realism, communication, robustness).
2. Choose one primary setting group first (domain, optimization, numerical, sensitivity).
3. Avoid changing too many dimensions at once if you need causal clarity.

After changing settings:

1. Re-run the corresponding experiment.
2. Confirm recommendation, report output, and plots are still coherent.
3. Run smoke tests in `tests/` to ensure key math behavior remains valid.
4. Record what changed and why (for traceability).

---

## Suggested tuning presets

### Preset: Fast Developer Loop

- Exp01: `PLOT_POINTS = 250`, `ANIMATION_POINTS = 120`, `ANIMATION_INTERVAL_MS = 25`
- Exp02: `PERTURBATION_GRID = [-0.10, 0.0, 0.10]`

### Preset: Teaching Demo

- Exp01: `ANIMATION_INTERVAL_MS = 35` (slower narration pace)
- Exp02: keep `BOUNDS` visible in plots and reports; keep moderate perturbation density

### Preset: Robustness Study

- Exp02: `PERTURBATION_GRID = [-0.30, -0.20, -0.10, 0.0, 0.10, 0.20, 0.30]`
- Optionally run both `DIRECTION = 'minimize'` and `'maximize'` for policy comparison

---

## Final takeaway

`settings.py` is where I define experiment assumptions transparently.

That gives me:

- cleaner code,
- more trustworthy comparisons,
- faster scenario testing,
- and recommendations that map better to real-world constraints.

In this repository, this design is a major reason Experiment 01 and Experiment 02 stay understandable, reproducible, and extensible.
