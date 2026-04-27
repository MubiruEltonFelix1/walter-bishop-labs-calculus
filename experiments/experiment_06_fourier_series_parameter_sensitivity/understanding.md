# Understanding Experiment 06

## Big Picture

This experiment is really about two things at once:

1. Understanding what Fourier series are doing mathematically.
2. Seeing how the approximation responds when I change practical parameters like amplitude and harmonic count.

If Experiment 04 showed me that Fourier partial sums can rebuild periodic shapes, this experiment shows me how sensitive that reconstruction is.

## Fourier Series in Plain Terms

The formula

$$
f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left(a_n \cos(nx) + b_n \sin(nx)\right)
$$

means that a complicated periodic signal can be built from simple repeating waves.

The coefficients tell me how much of each harmonic I need.

The low harmonics describe the coarse shape.
The higher harmonics sharpen corners, ramps, and jumps.

## What the Plots Show

### 1. Reconstruction plots

These compare the true signal against partial sums with different harmonic counts.

What I should notice:

- Small N gives a rough shape only.
- Larger N gives a better global fit.
- Sharp jumps still show ringing near the discontinuity.

That ringing is the Gibbs phenomenon again. It is not a bug. It is the cost of approximating a jump with smooth sine and cosine waves.

### 2. Amplitude family plots

These show the same signal shape at different amplitude levels.

The important lesson is that amplitude does not change the structure of the Fourier series.
It mostly rescales the coefficients.

So if I double the signal amplitude, the Fourier coefficients should roughly double too.

### 3. Coefficient scaling plots

These plots make the scaling law visible.

For a signal multiplied by a constant factor A:

- the coefficient values scale by A
- the reconstruction scales by A
- the absolute error also scales by A
- the MSE scales approximately by A^2

That last point matters because it tells me that larger signals can look worse in absolute error even if the approximation quality is the same in relative terms.

### 4. Harmonic build-up animation

This animation shows the reconstruction changing as the harmonic count increases.

The point is not just to see a curve move.
It is to see how the approximation becomes more faithful in stages.

That is the practical meaning of Fourier expansion: every new harmonic adds a bit more information, but the improvement is not always uniform.

### 5. Amplitude sweep animation

This animation keeps the harmonic count fixed and changes the amplitude.

That helps me separate two ideas:

- changing the scale of the signal
- changing the number of terms in the approximation

Those are different questions, and the plots make the distinction visible.

## What I Learn From the Different Waveforms

Square wave:

- The odd harmonics are especially important.
- The jump points create the strongest ringing.

Sawtooth wave:

- The ramp structure shows up early.
- The wrap-around discontinuity keeps the maximum error noticeable.

Triangle wave:

- This is the smoothest of the three examples.
- It is usually easier to approximate with fewer harmonics.

## Derivation Insight

The derivation behind Fourier series matters because it explains why the coefficients are computed with integrals.

Each coefficient is a projection of the target function onto a basis wave.
In other words, I am measuring how much of each sine and cosine component already exists inside the signal.

That is why the method is so useful:

- it is interpretable
- it is systematic
- it works across many periodic signals

## Why This Matters

This experiment is useful because the same ideas appear in:

1. Signal processing
2. Control systems
3. Compression and denoising
4. Audio and vibration analysis
5. Numerical approximations in general

The main takeaway is simple:

Fourier series are not just a formula to memorize.
They are a way to understand periodic structure, control approximation quality, and reason about how a signal changes when I change its scale or complexity.
