---
aliases: [Gamma Function, Beta Function, Gamma and Beta Functions]
tags: [real-analysis, special-functions, integration]
source:
  - sources/2026-02-16/gamma-function.jpeg
  - sources/2026-02-16/beta-function.jpeg
date: 2026-02-16
---

# Gamma and Beta Functions

## The Gamma Function

> [!abstract] Definition (Gamma Function)
> For $0 < x < \infty$:
>
> $$\Gamma(x) = \int_0^{\infty} t^{x-1} e^{-t}\, dt$$

^gamma-function-definition

### Properties

1. **Functional equation:** $\Gamma(x+1) = x\,\Gamma(x)$
2. **Factorial:** $\Gamma(n+1) = n!$ for $n = 1, 2, 3, \ldots$
3. **Log-convexity:** $\log \Gamma(x)$ is convex
4. **Normalization:** $\Gamma(1) = 1$

### Uniqueness (Bohr-Mollerup Theorem)

> [!abstract] Theorem (Bohr-Mollerup)
> The above properties define $\Gamma(x)$ **uniquely**. That is, $\Gamma$ is the only function on $(0, \infty)$ satisfying the functional equation $f(x+1) = xf(x)$, the normalization $f(1) = 1$, and log-convexity.

^bohr-mollerup-theorem

### Why Log-Convexity Is Necessary

> [!question] What happens without log-convexity?
> Without log-convexity, the functional equation and normalization alone admit an **infinite-dimensional** family of solutions.

If $f(x+1) = xf(x)$ and $f(1) = 1$, set $g(x) = f(x)/\Gamma(x)$. Then:

$$g(x+1) = \frac{f(x+1)}{\Gamma(x+1)} = \frac{xf(x)}{x\Gamma(x)} = g(x)$$

So $g$ is **periodic with period 1** and $g(1) = 1$. Conversely, for any positive periodic function $g$ with $g(x+1) = g(x)$ and $g(1) = 1$, the product $f(x) = g(x)\,\Gamma(x)$ satisfies the functional equation and normalization. The full solution set is therefore:

$$\big\{g(x)\,\Gamma(x) : g > 0,\; g(x+1) = g(x),\; g(1) = 1\big\}$$

> [!example] Non-uniqueness example
> $g(x) = e^{\sin(2\pi k x)}$ for any integer $k$ gives a valid solution.

> [!tip] Key insight
> ==Log-convexity collapses this family to a point.== If $\log f = \log g + \log \Gamma$ is convex, then since $\log \Gamma$ is already convex, $\log g$ is a periodic function whose sum with a convex function remains convex. But a periodic function on $(0, \infty)$ is bounded, and a bounded convex function on an unbounded interval must be constant. Hence $g \equiv 1$, recovering $f = \Gamma$.

This is the content of Bohr-Mollerup: ==log-convexity is the minimal regularity condition that pins down $\Gamma$ among infinitely many candidates==.

### Gauss Product Formula

$$\Gamma(x) = \lim_{n \to \infty} \frac{n!\; n^x}{x(x+1)(x+2)\cdots(x+n)}$$

> [!info]- Validity
> This limit representation is valid for all $x > 0$ (and more generally for all complex $x$ not a non-positive integer). It provides an alternative definition of the Gamma function that makes analytic continuation straightforward.

## The Beta Function

> [!abstract] Definition (Beta Function)
> For $x, y > 0$:
>
> $$B(x, y) = \int_0^1 t^{x-1}(1-t)^{y-1}\, dt$$

^beta-function-definition

### Relation to the Gamma Function

> [!abstract] Theorem (Beta-Gamma Relation)
> $$B(x, y) = \frac{\Gamma(x)\,\Gamma(y)}{\Gamma(x+y)}$$

^beta-gamma-relation

## Special Value

$$\Gamma\!\left(\frac{1}{2}\right) = \sqrt{\pi}$$

> [!note]- Proof sketch
> This follows from the Beta function relation: $B(1/2, 1/2) = \Gamma(1/2)^2/\Gamma(1) = \Gamma(1/2)^2$. Computing $B(1/2, 1/2) = \int_0^1 t^{-1/2}(1-t)^{-1/2}\, dt = \pi$ (via the substitution $t = \sin^2\theta$), we get $\Gamma(1/2)^2 = \pi$, hence $\Gamma(1/2) = \sqrt{\pi}$.

## See Also

- [[exponential-logarithm-and-euler-constant|Exponential Logarithm and Euler Constant]]
- [[fourier-series|Fourier Series]]
- [[power-series|Power Series]]
