---
aliases: [Change of Variables, Jacobian, Change of Variables Formula]
tags: [real-analysis, multivariable-calculus, integration, jacobian]
source:
  - sources/2026-02-16/change-of-variables-jacobian.jpeg
date: 2026-02-16
---

# Change of Variables

## The Change of Variables Formula

> [!abstract] Theorem (Change of Variables)
> Let $T: \mathbb{R}^k \to \mathbb{R}^k$ be a continuously differentiable mapping. Then:
>
> $$\int_{\mathbb{R}^k} f(y)\, dy = \int_{\mathbb{R}^k} f(T(x))\, \left|J_T(x)\right|\, dx$$
>
> where
>
> $$J_T(x) = \det\!\left(\frac{\partial y}{\partial x}\right)$$
>
> is the **Jacobian determinant** of $T$, and $J_T(x) \neq 0$.

^change-of-variables-formula

## Interpretation

==The Jacobian $|J_T(x)|$ adjusts the **measure** (volume element) to account for the change of variables.== Under the mapping $T$, an infinitesimal volume element $dx$ is scaled by the factor $|J_T(x)|$ to give the corresponding volume element $dy$ in the new coordinates.

> [!info]- Technical conditions
> More precisely, $T$ must be a $C^1$ diffeomorphism (or at least injective a.e. with nonvanishing Jacobian). The formula generalizes the one-dimensional substitution rule $\int f(g(x))|g'(x)|\,dx = \int f(y)\,dy$. The absolute value is needed because the Jacobian determinant can be negative (orientation-reversing), but volume is always positive.

<!-- clarification: More precisely, T must be a C¹ diffeomorphism (or at least injective a.e. with nonvanishing Jacobian). The formula generalizes the one-dimensional substitution rule ∫f(g(x))|g'(x)|dx = ∫f(y)dy. The absolute value is needed because the Jacobian determinant can be negative (orientation-reversing), but volume is always positive. -->

## See Also

- [[inverse-and-implicit-function-theorems|Inverse and Implicit Function Theorems]]
- [[differentiation-in-higher-dimensions|Differentiation in Higher Dimensions]]
- [[gamma-and-beta-functions|Gamma and Beta Functions]]
