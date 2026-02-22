---
aliases: [Nowhere Differentiable Function, Weierstrass Function]
tags: [real-analysis, continuity, differentiability, weierstrass]
source: sources/2026-02-16/4.jpeg
page: 4
date: 2026-02-16
---

# Nowhere Differentiable Continuous Function

> [!abstract] Theorem (Weierstrass, 1872)
> There exists a real continuous function on $\mathbb{R}$ that is ==nowhere differentiable==.

^weierstrass-nowhere-differentiable

![[images/weierstrass-function.png|Graph of the Weierstrass function — continuous everywhere, differentiable nowhere]]

## Definition

The **Weierstrass functions** are an infinite family parameterized by $a$ and $b$:

$$W_{a,b}(x) = \sum_{n=0}^{\infty} a^n \cos(b^n \pi x)$$

where $0 < a < 1$, $b$ is a positive odd integer, and $ab > 1 + \frac{3}{2}\pi$. Any choice of $a, b$ satisfying these conditions gives a continuous, nowhere-differentiable function. A common example is $a = \tfrac{1}{2}$, $b = 13$.

- Each partial sum is smooth (a finite sum of cosines), so $W$ is a [[uniform-convergence-and-cauchy-criterion|uniform limit]] of differentiable functions.
- The series converges uniformly by comparison with $\sum a^n$, so $W$ is continuous.
- Yet $W$ is differentiable at **no point** — the oscillations introduced by $b^n$ grow fast enough to prevent any tangent line from existing.

> [!info]- Construction idea
> The construction uses a uniformly convergent series of continuous functions — each term is differentiable, but the uniform limit is not differentiable at any point.

## See Also
- [[uniform-convergence-of-derivatives|Uniform Convergence of Derivatives]] — the condition that *would* preserve differentiability (which this function violates)
- [[uniform-convergence-and-cauchy-criterion|Uniform Convergence and the Cauchy Criterion]]
- [[continuous-functions|Continuity]]
