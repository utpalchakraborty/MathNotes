---
aliases: [Parseval's Theorem, Parseval's theorem, Parseval's Identity, Parseval's identity]
tags: [real-analysis, fourier-analysis, convergence]
source: parsevals-theorem.jpeg
date: 2026-02-17
---

# Parseval's Theorem

All period $2\pi$ continuous functions can be approximated by a Fourier series of trigonometric functions. Parseval's theorem makes this precise in the $L^2$ sense.

## Statement

Let $f(x), g(x)$ be Riemann integrable with period $2\pi$, with Fourier expansions:

$$f(x) \sim \sum_{n=-\infty}^{\infty} c_n \, e^{inx}, \qquad g(x) \sim \sum_{n=-\infty}^{\infty} \gamma_n \, e^{inx}.$$

### Mean-Square Convergence

> [!abstract] Theorem (Mean-Square Convergence)
> The Fourier partial sums $S(n; x)$ converge to $f$ in the $L^2$ mean:
>
> $$\lim_{n \to \infty} \frac{1}{2\pi} \int_{-\pi}^{\pi} |f(x) - S(n; x)|^2 \, dx = 0.$$

^mean-square-convergence

> [!warning] Not Pointwise
> This is **average convergence** (convergence in norm), not pointwise convergence. The partial sums may not converge to $f(x)$ at every point, but the "total squared error" vanishes.

### Inner Product Identity

> [!abstract] Theorem (Inner Product Identity)
> $$\frac{1}{2\pi} \int_{-\pi}^{\pi} f(x) \, \overline{g(x)} \, dx = \sum_{n=-\infty}^{\infty} c_n \, \overline{\gamma_n}.$$

^inner-product-identity

The integral on the left is the inner product $\langle f, g \rangle$ in $L^2([-\pi, \pi])$. The sum on the right is the inner product $\langle (c_n), (\gamma_n) \rangle$ in $\ell^2(\mathbb{Z})$. The Fourier coefficient map ==preserves inner products== — it is an **isometry**.

### Parseval's Identity ($L^2$ Norm)

Setting $g = f$:

> [!abstract] Theorem (Parseval's Identity)
> $$\frac{1}{2\pi} \int_{-\pi}^{\pi} |f(x)|^2 \, dx = \sum_{n=-\infty}^{\infty} |c_n|^2.$$

^parsevals-identity

> [!tip] Energy Conservation
> The $L^2$ norm of $f$ equals the $\ell^2$ norm of its Fourier coefficient sequence. The =="energy" of the function in the time domain equals the "energy" in the frequency domain==.

## Significance

Parseval's theorem establishes that Fourier analysis is not just an approximation scheme but a ==**norm-preserving correspondence**== between functions and coefficient sequences. In the Riemann setting, this is already remarkable — but it has a limitation: the Riemann-integrable functions are **not complete** under the $L^2$ norm. A sequence of Riemann-integrable functions can converge in $L^2$ to something that is not Riemann integrable.

The [[riesz-fischer-theorem|Riesz–Fischer Theorem]] resolves this by upgrading to the Lebesgue setting, where $L^2$ is complete.

## See Also
- [[fourier-series|Fourier Series]]
- [[riesz-fischer-theorem|Riesz–Fischer Theorem]]
- [[lebesgue-integration|Lebesgue Integration]]
