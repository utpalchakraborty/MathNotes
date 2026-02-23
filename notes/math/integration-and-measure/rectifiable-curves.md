---
aliases: [Rectifiable Curves, Rectifiable Curve, Arc Length]
tags: [real-analysis, curves, integration]
source: sources/2026-02-19/rectifiable-curves-and-limit-interchange.jpeg
date: 2026-02-19
---

# Rectifiable Curves

## Definition

> [!abstract] Definition (Rectifiable Curve)
> A **rectifiable curve** is a curve that can be approximated by line segments — equivalently, ==a curve with finite length==.
>
> Given a curve $\gamma \colon [a, b] \to \mathbb{R}^n$ and a partition $P = \{x_0, x_1, \ldots, x_N\}$ of $[a, b]$, the **inscribed polygon length** is
>
> $$\Lambda(P, \gamma) = \sum_{i=1}^{N} |\gamma(x_i) - \gamma(x_{i-1})|.$$

^rectifiable-curve-def

## Arc Length

> [!abstract] Definition (Arc Length)
> The **arc length** (or total variation) of $\gamma$ is
>
> $$\Lambda(\gamma) = \sup_P \Lambda(P, \gamma),$$
>
> where the supremum is taken over all partitions $P$ of $[a, b]$. The curve is rectifiable if and only if $\Lambda(\gamma) < \infty$.

^arc-length-def

## Derivative Formula

> [!abstract] Theorem (Arc Length via Integration)
> If $\gamma$ is continuously differentiable, the arc length can be computed as
>
> $$\Lambda(\gamma) = \int_a^b |\gamma'(t)| \, dt.$$

^arc-length-derivative-formula

## See Also
- [[riemann-stieltjes-integral|Riemann–Stieltjes Integral]]
- [[continuous-functions|Continuous Functions]]
