# Understanding Experiment 04

## Big Picture

Experiment 04 teaches a key modeling idea:

A complicated periodic waveform can be represented using simple building blocks.
Those blocks are harmonics, and each harmonic carries a specific amount of signal structure.

This experiment is also a reminder that Fourier analysis is not just about exact formulas.
It is about what a finite approximation does well, where it struggles, and how the error changes as we include more terms.

## What We Should Notice in the Plots

1. True vs partial sums:
- Low harmonic counts capture coarse structure.
- Higher counts sharpen transitions and corners.
- For discontinuities, ringing near jumps remains visible even when overall error drops.

2. Harmonic spectrum:
- The magnitude bars show which harmonics dominate each waveform.
- Smooth signals concentrate energy in fewer low-frequency terms.
- Less smooth signals distribute energy across more terms.

3. Error decay:
- MSE should generally decrease as harmonic count increases.
- Max error can remain elevated around jump points for discontinuous functions.

## Convergence Notes

The main convergence pattern is straightforward:

1. Smooth parts of the waveform are recovered first.
2. Sharp corners and jumps need more harmonics to look convincing.
3. For discontinuous functions, the overall approximation improves even though the overshoot near the jump never fully disappears.

That last point matters. The visible ringing is not a bug in the code. It is the Gibbs phenomenon, and it is one of the most important practical lessons in Fourier series.

## Interpretation Examples

Square wave:
- The low harmonics capture the general high/low shape quickly.
- The spectrum is spread across odd harmonics, which is why the reconstruction improves in steps rather than all at once.

Sawtooth wave:
- The reconstruction gets the ramp shape early, but the discontinuity at the wrap-around point keeps the max error noticeable.
- This is a good example of why max error can stay informative even when MSE drops.

Triangle wave:
- The reconstruction usually looks cleaner with fewer terms because the signal is smoother.
- Energy is concentrated more strongly in the low frequencies, so the spectrum falls off faster.

## Why This Matters

This is not only a calculus concept. It underpins practical workflows in:
1. Signal denoising
2. Compression
3. Feature extraction
4. Frequency-domain analysis for control and communications

Experiment 05 and Experiment 06 build directly on this foundation.

If I can explain why the partial sums behave differently across these three signals, then the later filtering and compression experiments become much easier to understand.
