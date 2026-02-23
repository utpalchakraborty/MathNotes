---
aliases: [Contraction Mapping Theorem, Banach Fixed Point Theorem, Fixed Point Theorem]
tags: [real-analysis, metric-spaces, fixed-point-theory]
source: sources/2026-02-17/differentiability-and-contraction-mapping.jpeg
date: 2026-02-17
---

# Contraction Mapping Theorem

## Statement

> [!abstract] Theorem (Contraction Mapping / Banach Fixed Point)
> If $X$ is a **complete metric space** and $\phi: X \to X$ is a **contraction** on $X$, then there exists ==one and only one== $x \in X$ such that
>
> $$\phi(x) = x$$

^contraction-mapping-theorem

<!-- clarification: A map φ is a contraction if there exists a constant c with 0 ≤ c < 1 such that d(φ(x), φ(y)) ≤ c · d(x, y) for all x, y ∈ X. The unique point x satisfying φ(x) = x is called the fixed point of φ. The proof is constructive: start with any x₀ ∈ X, define xₙ₊₁ = φ(xₙ), and show {xₙ} is Cauchy (using the contraction bound and geometric series). Completeness of X guarantees convergence to the fixed point. -->

## See Also

- [[continuous-functions|Continuous Functions]]
- [[inverse-and-implicit-function-theorems|Inverse and Implicit Function Theorems]]
- [[differentiation-in-higher-dimensions|Differentiation in Higher Dimensions]]
