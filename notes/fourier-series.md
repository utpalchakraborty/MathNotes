---
aliases: [Fourier Series, Orthogonal Functions, Orthonormal Functions, Fourier Coefficients]
tags: [real-analysis, fourier-analysis, orthogonality, series]
source:
  - sources/2026-02-16/orthogonal-functions.jpeg
  - sources/2026-02-16/fourier-coefficients.jpeg
date: 2026-02-16
---

# Fourier Series

## Orthogonal Functions

> [!abstract] Definition (Orthogonal Functions)
> A sequence of functions $\{\varphi_n(x)\}$ on $[a, b]$ is **orthogonal** if
>
> $$\int_a^b \varphi_n(x)\,\overline{\varphi_m(x)}\, dx = 0 \quad \text{for } m \neq n$$

^orthogonal-functions-def

## Orthonormal Functions

> [!abstract] Definition (Orthonormal Functions)
> If additionally
>
> $$\int_a^b |\varphi_n(x)|^2\, dx = 1$$
>
> then the functions are **orthonormal**.

^orthonormal-functions-def

<!-- clarification: The handwritten notes write ∫|φ_n(x)| = 1 without the square, but the correct orthonormality condition requires |φ_n(x)|². -->

## Best Approximation Property

> [!tip] Key Property
> The Fourier series with orthonormal functions is the ==**best possible approximation**== (given that orthonormal set). That is, among all linear combinations of the orthonormal basis functions, the Fourier partial sums minimize the mean-square error.

## The Standard Orthonormal Basis

The functions

$$\frac{e^{inx}}{\sqrt{2\pi}}, \quad n \in \mathbb{Z}$$

form an orthonormal basis on $[-\pi, \pi]$.

### Verification of Orthogonality

> [!note]- Proof Sketch
> Expanding $e^{imx} \cdot \overline{e^{inx}} = e^{imx} \cdot e^{-inx}$:
>
> $$= (\cos mx + i\sin mx)(\cos nx - i\sin nx)$$
>
> Integrating over $[-\pi, \pi]$, the cosine terms give:
>
> $$\int_{-\pi}^{\pi} \cos(mx)\cos(nx)\, dx = \pi\left(\delta_{m,n} + \delta_{m,-n}\right)$$
>
> where $\delta$ is the **Kronecker delta**.
>
> <!-- clarification: The notes label δ as "dirac delta," but in this discrete-index context it is the Kronecker delta: δ_{m,n} = 1 if m = n, and 0 otherwise. -->
>
> In particular, the integral vanishes when $m \neq n$ (and $m \neq -n$), confirming orthogonality.

## Fourier Coefficients

> [!abstract] Definition (Fourier Coefficients)
> The **Fourier coefficients** of a function $f$ on $[-\pi, \pi]$ are:
>
> $$c_n = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(x)\, e^{-inx}\, dx$$

^fourier-coefficients-def

## Why Fourier Series Works

The Fourier series rests on two pillars:

1. **Orthogonality** provides the *mechanism*. Because the basis $\{e^{inx}/\sqrt{2\pi}\}$ is orthonormal, we can compute each coefficient $c_n$ by projection (the inner product formula above), and the partial sums are guaranteed to be the best approximation in the mean-square sense.

2. **[[stone-weierstrass-theorem|Stone-Weierstrass Theorem]]** provides the *completeness*. Trigonometric polynomials form a self-adjoint algebra that separates points and vanishes nowhere on the circle, so by Stone-Weierstrass they are ==**dense** in $C([-\pi, \pi])$== under the uniform norm. No continuous function escapes the reach of trig polynomials.

> [!tip] The Punchline
> Orthogonality alone without completeness would give best approximations that might still be poor. Completeness alone without orthogonality would give density but no clean way to compute coefficients. ==Together they make the full machine work.==

<!-- clarification: Stone-Weierstrass gives density in the sup norm. For the L² theory (‖f − S_n f‖₂ → 0 for every L² function), one uses that continuous functions are dense in L², so the chain is: Stone-Weierstrass → trig polys dense in C → C dense in L² → trig polys dense in L² → orthonormal system is complete in L². -->

### The Role of $L^2$ and Hilbert Space Structure

Orthogonality is defined via an inner product: $\langle f, g \rangle = \int f\,\overline{g}\, dx = 0$. For this integral to be finite, both $f$ and $g$ must be in $L^2$ (by Cauchy-Schwarz). So orthogonal functions are in $L^2$ **by definition** — orthogonality cannot exist outside an inner product space.

The deeper reason $L^2$ is the right setting is **completeness**: $L^2$ is a Hilbert space (a complete inner product space), meaning every Cauchy sequence converges to something still in $L^2$. This guarantees:

- Fourier partial sums converge (in norm) to an element of the space
- **Parseval's identity:** $\|f\|^2 = \sum |c_n|^2$ — the map $f \mapsto (c_n)$ is an isometry to $\ell^2$
- **Best approximation** via orthogonal projection

> [!info]- Why Not Other Spaces?
> One could instead work in $C([-\pi, \pi])$ with the $L^2$ norm, where orthogonality still makes sense. But this space is **not complete** under $\|\cdot\|_2$ — there are Cauchy sequences of continuous functions whose $L^2$ limit is discontinuous. So Fourier series might "want to converge" to something outside the space. $L^2$ is the completion that fixes this.
>
> Spaces like $L^1$ or $L^\infty$ are Banach spaces (complete, but no inner product), so orthogonality, projection, and the coefficient formula are all lost. Fourier analysis in $L^1$ exists but is much harder and lacks the geometric elegance.

## See Also

- [[parsevals-theorem|Parseval's Theorem]]
- [[riesz-fischer-theorem|Riesz–Fischer Theorem]]
- [[exponential-logarithm-and-euler-constant|Exponential Logarithm and Euler Constant]]
- [[power-series|Power Series]]
- [[stone-weierstrass-theorem|Stone-Weierstrass Theorem]]
- [[uniform-convergence-and-cauchy-criterion|Uniform Convergence and Cauchy Criterion]]
