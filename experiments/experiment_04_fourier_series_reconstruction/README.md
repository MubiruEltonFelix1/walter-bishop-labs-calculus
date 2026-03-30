# Experiment 04: Fourier Series Reconstruction of Periodic Functions

## Why This Experiment Exists

This experiment is the first step into Fourier series from a practical perspective.
Instead of memorizing formulas, the goal is to watch harmonics rebuild familiar periodic shapes and measure how the reconstruction quality changes as we add more terms.

The central idea is simple:

A periodic signal can be represented as a weighted sum of sine and cosine waves.

## Core Question

How quickly can a finite Fourier partial sum recover the structure of a periodic function?

We test this on three classic signals:
1. Square wave
2. Sawtooth wave
3. Triangle wave

## What This Experiment Implements

1. Numerical estimation of Fourier coefficients for each function:
- a0
- an for n = 1..N
- bn for n = 1..N

2. Partial-sum reconstruction at increasing harmonic counts.

3. Quantitative error tracking for each reconstruction:
- Mean squared error (MSE)
- Maximum absolute error

4. Plot outputs for each function:
- True signal vs partial sums
- Harmonic magnitude spectrum
- Error decay with harmonic count

## Run

From this experiment directory:

```bash
python main.py
```

Optional interactive mode:

```bash
python run_interactive.py
```

## Output Artifacts

Generated files are saved to:
1. outputs/plots
2. outputs/reports

## Folder Structure

```text
experiment_04_fourier_series_reconstruction/
├── settings.py
├── main.py
├── run_interactive.py
├── README.md
├── understanding.md
├── calculus/
├── visualization/
├── reporting/
└── outputs/
```

## Notes

Discontinuous signals (square and sawtooth) exhibit Gibbs oscillations near jump points. This is expected and is part of the learning objective.
