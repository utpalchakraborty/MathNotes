---
aliases: [Inverse Function Theorem, Implicit Function Theorem, Inverse and Implicit Function Theorems]
tags: [real-analysis, multivariable-calculus, differentiation, topology]
source:
  - sources/2026-02-16/inverse-function-theorem.jpeg
  - sources/2026-02-16/implicit-function-theorem.jpeg
date: 2026-02-16
---

# Inverse and Implicit Function Theorems

## The Basic Idea

> [!tip] Guiding principle
> ==Continuously differentiable transformations are locally equal to their derivatives.==

A $C^1$ mapping $f$ behaves, near any point, like the linear map $f'$. This single principle underlies both the Inverse and Implicit Function Theorems.

## Inverse Function Theorem

> [!abstract] Theorem (Inverse Function Theorem)
> A continuously differentiable mapping $f$ is **invertible in a neighborhood** of a point if $f'$ is invertible at that point.

^inverse-function-theorem

> [!info]- Precise statement
> If $f: \mathbb{R}^n \to \mathbb{R}^n$ is $C^1$ and the Jacobian matrix $f'(a)$ is invertible (i.e., $\det f'(a) \neq 0$), then there exist open sets $U \ni a$ and $V \ni f(a)$ such that $f: U \to V$ is a bijection with $C^1$ inverse.

**Intuition:** Use $f'$ to invert the change — a change in the range corresponds to a change in the domain via the inverse of the derivative.

## Implicit Function Theorem

> [!abstract] Theorem (Implicit Function Theorem)
> If $f(x, y) = 0$, then $f$ can be **solved locally for $x$ in terms of $y$** at a point provided $\frac{\partial f}{\partial x} \neq 0$.

^implicit-function-theorem

### General Case

For $f: \mathbb{R}^n \to \mathbb{R}^m$ with $m < n$, the equation $f = 0$ represents $m$ implicit equations:

$$f_1(x_1, x_2, \ldots, x_n) = 0$$
$$f_2(x_1, x_2, \ldots, x_n) = 0$$
$$\vdots$$
$$f_m(x_1, x_2, \ldots, x_n) = 0$$

These $m$ equations in $n$ unknowns generically determine an ==$(n - m)$-dimensional solution set==.

> [!info]- Precise condition
> The precise condition is that the $m \times m$ submatrix of the Jacobian corresponding to the variables being solved for has nonzero determinant. Then locally the solution set is the graph of a $C^1$ function of the remaining $n - m$ variables.

## See Also

- [[continuous-functions|Continuous Functions]]
- [[differentiation-in-higher-dimensions|Differentiation in Higher Dimensions]]
- [[change-of-variables|Change of Variables]]
