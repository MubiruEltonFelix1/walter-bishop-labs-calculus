# Experiment 06: Fourier Series Parameter Sensitivity and Amplitude Scaling

## Why This Experiment Exists

This experiment goes one level deeper than the basic reconstruction work in Experiment 04.
Here I want to see what Fourier series are actually doing when I change the signal amplitude and the number of harmonics.

The main questions are:

1. How does a Fourier series represent a periodic function in the first place?
2. What happens to the coefficients when I scale the amplitude of the signal?
3. How much does the reconstruction improve as I toggle the harmonic count?
4. Do the same ideas hold for different kinds of periodic waves?

## Core Idea

A periodic function can be written as:

$$
f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left(a_n \cos(nx) + b_n \sin(nx)\right)
$$

In this experiment, I use that form to compare:

1. The original periodic wave.
2. Its partial Fourier sums.
3. The way coefficients move when the amplitude changes.
4. The way reconstruction quality changes when the harmonic count changes.

## What Is Implemented

1. Fourier coefficient estimation for three classic periodic signals:
- square wave
- sawtooth wave
- triangle wave

2. Reconstruction at multiple harmonic counts.

3. Amplitude-scaling studies that show how the coefficients and errors shift when the signal amplitude changes.

4. Static plots for:
- signal families under amplitude scaling
- coefficient magnitude behavior
- reconstruction comparisons
- error decay with harmonic count

5. Animated HTML outputs for:
- amplitude sweeps
- harmonic build-up sweeps

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
experiment_06_fourier_series_parameter_sensitivity/
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

Amplitude scaling is the cleanest parameter study here because Fourier coefficients respond linearly to the signal scale.
That makes the error behavior easy to interpret: if the amplitude grows, the absolute reconstruction error grows too, even when the shape of the approximation stays the same.
