# Understanding Experiment 04

## Big Picture

Experiment 04 teaches a key modeling idea:

A complicated periodic waveform can be represented using simple building blocks.
Those blocks are harmonics, and each harmonic carries a specific amount of signal structure.

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

## Why This Matters

This is not only a calculus concept. It underpins practical workflows in:
1. Signal denoising
2. Compression
3. Feature extraction
4. Frequency-domain analysis for control and communications

Experiment 05 and Experiment 06 build directly on this foundation.
