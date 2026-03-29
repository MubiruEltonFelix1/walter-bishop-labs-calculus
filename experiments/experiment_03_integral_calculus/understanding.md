# Understanding Integral Calculus

## The Big Picture: From Derivatives to Integrals

In earlier experiments, we studied derivatives—tools for understanding instantaneous change. Now we reverse the process.

**Derivatives** break things down: they show how fast something changes at any given moment.
**Integrals** build things up: they accumulate all those tiny changes to find the total.

**Analogy**: If derivatives are like analyzing a video frame-by-frame to see pixel shifts, integrals are like reconstructing the entire movie from those shifts—connecting individual frames back into the whole picture.

In physical terms:
- **Derivative**: Given velocity (rate of change), find acceleration (how velocity changes)
- **Integral**: Given velocity (rate of change), find distance travelled (total change)

So integrals are key for calculating totals: area under curves, distance, volume, and accumulated quantities.

---

## 1. Indefinite Integrals & Antiderivatives

An **antiderivative** of $f(x)$ is a function $F(x)$ such that $F'(x) = f(x)$.

The **indefinite integral** represents the family of all antiderivatives:
$$\int f(x) \, dx = F(x) + C$$

where $C$ is the constant of integration (it captures the fact that all antiderivatives differ by a constant).

### Basic Antiderivative Rules

| Function | Antiderivative |
|----------|----------------|
| $x^n$ $(n \neq -1)$ | $\frac{x^{n+1}}{n+1} + C$ |
| $\frac{1}{x}$ | $\ln \|x\| + C$ |
| $e^x$ | $e^x + C$ |
| $a^x$ | $\frac{a^x}{\ln a} + C$ |
| $\sin x$ | $-\cos x + C$ |
| $\cos x$ | $\sin x + C$ |
| $\sec^2 x$ | $\tan x + C$ |
| $\csc^2 x$ | $-\cot x + C$ |

---

## 2. Techniques of Integration

Finding antiderivatives isn't always straightforward. We need strategies.

### 2.1 Substitution (u-substitution)

**When**: The integrand is a composition of functions (reverse of chain rule).

**Method**: Let $u = g(x)$, then $du = g'(x) dx$:
$$\int f(g(x)) g'(x) \, dx = \int f(u) \, du$$

**Example**:
$$\int 2x \cos(x^2) \, dx$$

Let $u = x^2 \Rightarrow du = 2x \, dx$

$$\int \cos(u) \, du = \sin(u) + C = \sin(x^2) + C$$

### 2.2 Integration by Parts

**When**: Product of two functions (reverse of product rule).

**Formula**:
$$\int u \, dv = uv - \int v \, du$$

**LIATE Rule** for choosing $u$ (pick whichever comes first):
- **L**ogarithmic ($\ln x$, $\log x$)
- **I**nverse trig ($\arcsin x$, $\arctan x$)
- **A**lgebraic ($x$, $x^2$)
- **T**rigonometric ($\sin x$, $\cos x$)
- **E**xponential ($e^x$, $a^x$)

**Example**:
$$\int x e^x \, dx$$

Let $u = x \Rightarrow du = dx$ and $dv = e^x dx \Rightarrow v = e^x$

$$\int x e^x \, dx = xe^x - \int e^x \, dx = xe^x - e^x + C$$

### 2.3 Trigonometric Integrals

**Strategies**:
- **Odd powers**: Isolate one factor and use identities.
- **Even powers**: Use half-angle identities:
  $$\sin^2 x = \frac{1 - \cos(2x)}{2}, \quad \cos^2 x = \frac{1 + \cos(2x)}{2}$$

### 2.4 Trigonometric Substitution

Used when the integrand contains radicals like $\sqrt{a^2 - x^2}$, $\sqrt{a^2 + x^2}$, or $\sqrt{x^2 - a^2}$.

| Expression | Substitution |
|-----------|--------------|
| $\sqrt{a^2 - x^2}$ | $x = a \sin \theta$ |
| $\sqrt{a^2 + x^2}$ | $x = a \tan \theta$ |
| $\sqrt{x^2 - a^2}$ | $x = a \sec \theta$ |

### 2.5 Partial Fractions

**When**: Integrand is a rational function $\frac{P(x)}{Q(x)}$.

**Steps**:
1. Factor the denominator
2. Set up the decomposition
3. Solve for coefficients
4. Integrate each term

---

## 3. Definite Integrals

While an indefinite integral $\int f(x) \, dx$ gives a family of antiderivatives, a definite integral $\int_a^b f(x) \, dx$ gives a **number**—the net accumulated value from $a$ to $b$.

**Graphically**: The net area under the curve $y = f(x)$ between $x = a$ and $x = b$ (areas above the x-axis are positive; areas below are negative).

### Definition via Riemann Sums

Divide $[a, b]$ into $n$ subintervals of width $\Delta x = \frac{b-a}{n}$:

$$\int_a^b f(x) \, dx = \lim_{n \to \infty} \sum_{i=1}^n f(x_i^*) \Delta x$$

where $x_i^*$ are sample points in each subinterval.

### Properties of Definite Integrals

- **Linearity**: $\int_a^b [cf(x) + g(x)] \, dx = c\int_a^b f(x) \, dx + \int_a^b g(x) \, dx$
- **Additivity**: $\int_a^c f(x) \, dx + \int_c^b f(x) \, dx = \int_a^b f(x) \, dx$
- **Reversal**: $\int_a^b f(x) \, dx = -\int_b^a f(x) \, dx$
- **Zero interval**: $\int_a^a f(x) \, dx = 0$

---

## 4. The Fundamental Theorem of Calculus (FTC)

This theorem connects derivatives and integrals—they're inverse operations.

### Part 1: Derivative of an Integral

If $F(x) = \int_a^x f(t) \, dt$, then $F'(x) = f(x)$ (provided $f$ is continuous).

### Part 2: Evaluating Definite Integrals

If $F$ is an antiderivative of $f$, then:
$$\int_a^b f(x) \, dx = F(b) - F(a) = [F(x)]_a^b$$

This is the practical workhorse: to evaluate a definite integral, find an antiderivative and evaluate at the bounds.

**Example**:
$$\int_1^4 (3x^2 + 2x) \, dx$$

$F(x) = x^3 + x^2$, so:
$$[x^3 + x^2]_1^4 = (64 + 16) - (1 + 1) = 78$$

---

## 5. Applications of Integration

Integration isn't just abstract—it solves real-world problems.

### 5.1 Area Between Two Curves

If $f(x) \geq g(x)$ on $[a, b]$, the area between them is:
$$A = \int_a^b [f(x) - g(x)] \, dx$$

### 5.2 Volume of Solids of Revolution

Rotating a region around an axis creates a solid. Use disk/washer method:

**Disk Method** (no hole):
$$V = \pi \int_a^b [f(x)]^2 \, dx$$

**Washer Method** (with hole):
$$V = \pi \int_a^b \left([R(x)]^2 - [r(x)]^2\right) dx$$

### 5.3 Work Done by a Variable Force

If force varies with position, total work is:
$$W = \int_a^b F(x) \, dx$$

For springs (Hooke's Law with $F(x) = kx$):
$$W = \int_a^b kx \, dx$$

### 5.4 Average Value of a Function

The average output of $f(x)$ over $[a, b]$ is:
$$f_{\text{avg}} = \frac{1}{b - a} \int_a^b f(x) \, dx$$

---

## 6. Numerical Integration

Sometimes we can't find an antiderivative in closed form or the function is only known at discrete points. We approximate the integral using rectangles, trapezoids, or parabolas.

### Riemann Sums

Simple but often inaccurate:
- **Left Sum**: $L_n = \sum_{i=0}^{n-1} f(x_i) \Delta x$
- **Right Sum**: $R_n = \sum_{i=1}^n f(x_i) \Delta x$

### Trapezoidal Rule

Approximates with trapezoids. More accurate than Riemann sums:
$$\int_a^b f(x) \, dx \approx \frac{\Delta x}{2} [f(x_0) + 2f(x_1) + 2f(x_2) + \cdots + 2f(x_{n-1}) + f(x_n)]$$

### Simpson's Rule

Approximates with parabolas. Very accurate for smooth functions (requires even $n$):
$$\int_a^b f(x) \, dx \approx \frac{\Delta x}{3} [f(x_0) + 4f(x_1) + 2f(x_2) + 4f(x_3) + \cdots + 4f(x_{n-1}) + f(x_n)]$$

**Comparison**: Simpson's Rule converges faster than the trapezoidal rule for well-behaved, smooth functions.

---

## Key Insights

1. **Integration is the reverse of differentiation**—they're inverse operations connected by the FTC.
2. **Many techniques exist** because different forms require different strategies.
3. **Applications are everywhere**: calculating areas, volumes, work, and accumulated quantities.
4. **Numerical methods** fill the gap when symbolic integration is impossible or impractical.
5. **The FTC is the bridge**: it transforms finding antiderivatives into evaluating definite integrals quickly.
