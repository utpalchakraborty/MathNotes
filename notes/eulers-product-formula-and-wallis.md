---
aliases: [Euler's Product Formula and Wallis's Formula]
tags: [real-analysis, infinite-products, trigonometry, pi, bernoulli-numbers]
source:
  - sources/2026-02-21/archimedes-pi-and-sin-product.jpeg
  - sources/2026-02-21/euler-product-wallis-bernoulli.jpeg
date: 2026-02-21
---

# Euler's Product Formula and Wallis's Formula

## Motivation: Factoring Sine by Its Zeros

> [!question] Motivating Question
> The function $\sin x$ has zeros at $x = 0, \pm\pi, \pm 2\pi, \pm 3\pi, \ldots$ By analogy with factoring a polynomial by its roots, we might expect:
>
> $$\sin x = x(x - \pi)(x + \pi)(x - 2\pi)(x + 2\pi) \cdots$$

Pairing the factors $(x - n\pi)(x + n\pi) = x^2 - n^2\pi^2$, and normalizing so that $\frac{\sin x}{x} \to 1$ as $x \to 0$, we arrive at Euler's product formula.

## Euler's Product Formula

> [!abstract] Theorem (Euler's Product Formula)
> $$\sin x = x \prod_{k=1}^{\infty} \left(1 - \frac{x^2}{\pi^2 k^2}\right)$$

^eulers-product-formula

Equivalently, $\frac{\sin x}{x}$ has roots at $\pm\pi, \pm 2\pi, \ldots$ and satisfies $\frac{\sin x}{x}\big|_{x=0} = 1$.

> [!info]- Rigorous Justification
> A rigorous proof requires showing that the infinite product converges and equals $\sin x$. This can be done via the Weierstrass factorization theorem, or by comparing logarithmic derivatives (partial fraction decomposition of $\cot x$). The naive root-factoring argument is motivational, not a proof.

## Wallis's Product Formula

Setting $x = \frac{\pi}{2}$ in Euler's product formula:

$$\sin\frac{\pi}{2} = 1 = \frac{\pi}{2} \prod_{n=1}^{\infty} \left(1 - \frac{1}{4n^2}\right)$$

Writing each factor as:

$$1 - \frac{1}{4n^2} = \frac{4n^2 - 1}{4n^2} = \frac{(2n-1)(2n+1)}{(2n)^2}$$

we get:

> [!abstract] Theorem (Wallis's Product Formula)
> $$\frac{\pi}{2} = \prod_{n=1}^{\infty} \frac{(2n)(2n)}{(2n-1)(2n+1)} = \frac{2}{1} \cdot \frac{2}{3} \cdot \frac{4}{3} \cdot \frac{4}{5} \cdot \frac{6}{5} \cdot \frac{6}{7} \cdots$$

^wallis-product-formula

> [!info]- Historical Note
> This is Wallis's product formula for $\pi/2$, discovered by John Wallis in 1656. It provides a ==purely arithmetic expression for $\pi$== as an infinite product of rational numbers.

## Closed-Form Formula for Bernoulli Numbers

> [!abstract] Recursive Relation for Bernoulli Numbers
> There is a recursive closed-form relation for the Bernoulli numbers $\beta(2k)$:
>
> $$\left(k + \frac{1}{2}\right) \beta(2k) = \sum_{\ell=1}^{k-1} \beta(2\ell)\, \beta(2k - 2\ell)$$

^bernoulli-number-recurrence

> [!info]- Details
> Here $\beta(2k)$ denotes the Bernoulli numbers (sometimes written $B_{2k}$). This convolution-type identity allows computation of higher Bernoulli numbers from lower ones. It arises from expanding the product formula for $\sin x$ or equivalently from the generating function $x/(e^x - 1)$.

## See Also

- [[exponential-logarithm-and-euler-constant|Exponential Logarithm and Euler Constant]]
- [[hyperbolic-functions|Hyperbolic Functions]]
- [[power-series|Power Series]]
- [[gamma-and-beta-functions|Gamma and Beta Functions]]
- [[pi-and-square-free-integers|Pi and Square-Free Integers]]
