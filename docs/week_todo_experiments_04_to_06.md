# Week Task Plan: Experiments 04 to 06

Date: 2026-03-30

## Goal for This Week
Implement a connected sequence of Fourier-focused experiments:
1. Experiment 04: Fourier series reconstruction of basic periodic functions.
2. Experiment 05: Fourier-based filtering and denoising.
3. Experiment 06: Fourier coefficient compression and quality trade-offs.

## Day-by-Day Task Flow

## Day 1 (Today): Build Experiment 04
Status: In progress

Tasks:
1. Create experiment folder structure and module scaffolding.
2. Implement Fourier coefficient computation for periodic functions.
3. Implement partial-sum reconstruction for increasing harmonic counts.
4. Build static plots:
- True function vs multiple partial sums.
- Harmonic magnitude spectrum.
- Error decay vs number of harmonics.
5. Generate summary report with MSE and max-error metrics.
6. Add smoke test and wire root runner/validation script support.

Deliverable:
- Working Experiment 04 with reproducible outputs in plots and reports.

## Day 2: Stabilize and Deepen Experiment 04
Tasks:
1. Add convergence notes and interpretation examples in understanding document.
2. Add optional interactive runner for function-by-function exploration.
3. Improve plot readability and labels for lecturer-facing review.

Deliverable:
- Experiment 04 polished for presentation and hand-in.

## Day 3: Scaffold Experiment 05 (Denoising)
Tasks:
1. Define noisy signal generation pipeline.
2. Add harmonic truncation and low-pass filtering functions.
3. Add baseline metrics: MSE, SNR, coefficient-energy retention.

Deliverable:
- Core Experiment 05 computation pipeline complete.

## Day 4: Visual and Report Layer for Experiment 05
Tasks:
1. Build plots for clean/noisy/filtered time-domain comparison.
2. Build frequency-domain plots showing retained vs removed harmonics.
3. Generate summary report with recommendation for practical harmonic cutoff.

Deliverable:
- Experiment 05 complete and documented.

## Day 5: Scaffold Experiment 06 (Compression)
Tasks:
1. Implement coefficient ranking by energy contribution.
2. Implement top-K reconstruction workflow.
3. Compute compression ratio and fidelity metrics.

Deliverable:
- Experiment 06 core engine complete.

## Day 6: Visual and Analysis Layer for Experiment 06
Tasks:
1. Build quality-vs-compression curves.
2. Add reconstruction snapshots at multiple K values.
3. Write interpretation notes around decision thresholds for acceptable quality.

Deliverable:
- Experiment 06 complete and interpreted.

## Day 7: Cross-Experiment Integration and Review
Tasks:
1. Add/expand smoke tests for Experiments 04 to 06.
2. Update root README with scope progression and run commands.
3. Run full validation and prepare submission-ready summary.

Deliverable:
- Stable multi-experiment pipeline and clear documentation trail.

## Dependencies and Risk Checks
1. Numerical coefficient estimation must use sufficiently high sampling density.
2. Piecewise periodic functions may show Gibbs behavior near discontinuities; this is expected and should be explained.
3. Plot generation should save artifacts even when display is disabled.

## Success Criteria for the Week
1. All three experiments run from their main entry points without manual path fixes.
2. Each experiment outputs at least one report and multiple plots.
3. Each experiment has a smoke test validating core numerical behavior.
4. Root-level validation includes all completed experiments.
