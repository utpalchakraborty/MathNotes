---
aliases: [Differentiation in Higher Dimensions, Mixed Partials, Clairaut's Theorem, Mean Value Theorem in Higher Dimensions, Leibniz Integral Rule, Continuous Differentiability]
tags: [real-analysis, multivariable-calculus, differentiation, integration]
source:
  - sources/2026-02-16/implicit-function-theorem.jpeg
  - sources/2026-02-16/mean-value-higher-dimensions.jpeg
  - sources/2026-02-17/differentiability-and-contraction-mapping.jpeg
date: 2026-02-16
---

# Differentiation in Higher Dimensions

## Continuous Differentiability

> [!abstract] Theorem (Continuous Differentiability)
> If $f: \mathbb{R}^n \to \mathbb{R}^m$ with $f = (f_1, f_2, \ldots, f_m)$ where each $f_i$ takes $n$ arguments, then $f'$ is **continuous** (and $f$ is differentiable) if and only if all the partial derivatives
>
> $$\frac{\partial f_i}{\partial x_j}, \quad 1 \leq i \leq m, \quad 1 \leq j \leq n$$
>
> exist and are continuous.

^continuous-differentiability

## Symmetry of Mixed Partial Derivatives (Clairaut's Theorem)

> [!abstract] Theorem (Clairaut's Theorem)
> If $f: \mathbb{R}^n \to \mathbb{R}^m$, then
>
> $$\partial_{ij} f = \partial_{ji} f$$
>
> whenever both mixed partials exist and are **continuous**.

^clairauts-theorem

> [!warning] Continuity is essential
> There exist functions where the mixed partials exist but are unequal at a point because one of them is discontinuous.

## Mean Value Theorem in Higher Dimensions

> [!abstract] Theorem (Mean Value Theorem in Higher Dimensions)
> Let $E \subset \mathbb{R}^2$ and suppose $\partial_1 f$ and $\partial_{12} f$ exist on $E$. Consider a rectangle $Q \subset E$ with corners:
>
> - $A = f(a, b)$
> - $B = f(a+h,\, b+k)$
> - $C = f(a,\, b+k)$
> - $D = f(a+h,\, b)$
>
> Define the **second-order difference**:
>
> $$\Delta f = A + B - C - D = f(a,b) + f(a+h, b+k) - f(a, b+k) - f(a+h, b)$$
>
> Then there exists a point $P \in Q$ such that:
>
> $$\Delta f = hk\, \partial_{21} f(P)$$

^mvt-higher-dimensions

> [!note]- Proof sketch
> This follows from applying the one-dimensional mean value theorem twice. Write $\Delta f = g(b+k) - g(b)$ where $g(t) = f(a+h,t) - f(a,t)$, then apply MVT to $g$ and again to the resulting partial derivative expression. By Clairaut's theorem, $\partial_{21}f = \partial_{12}f$ when both are continuous, so ==the specific ordering of indices does not matter==.

## Interchange of Differentiation and Integration

> [!question] When is the following valid?
> $$\frac{d}{dt} \int_a^b \phi(x, t)\, dx = \int_a^b \frac{\partial \phi}{\partial t}(x, t)\, dx$$

> [!info]- Sufficient conditions (Leibniz integral rule)
> Sufficient conditions: $\phi$ and $\partial\phi/\partial t$ are continuous on $[a,b] \times I$ for some interval $I$ containing $t$. More generally, if $\partial\phi/\partial t$ exists and is dominated by an integrable function (independent of $t$), the interchange is valid by the Dominated Convergence Theorem.

## See Also

- [[inverse-and-implicit-function-theorems|Inverse and Implicit Function Theorems]]
- [[change-of-variables|Change of Variables]]
- [[continuous-functions|Continuous Functions]]
- [[uniform-convergence-and-cauchy-criterion|Uniform Convergence and Cauchy Criterion]]
- [[differential-forms|Differential Forms]]
- [[contraction-mapping-theorem|Contraction Mapping Theorem]]
