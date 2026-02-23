---
aliases: [Metric Spaces, Metric Space, Distance Function]
tags: [real-analysis, topology]
source: [metric-spaces-definition.jpeg, convexity-limit-points-compactness.jpeg]
date: 2025-07-06
---

# Metric Spaces

## Definition

> [!abstract] Definition (Metric Space)
> A **metric space** is a set $X$ equipped with a distance function $d \colon X \times X \to \mathbb{R}$ satisfying, for all $p, q, r \in X$:
>
> 1. $d(p, q) > 0$ if $p \neq q$; $\quad d(p, p) = 0$.
> 2. $d(p, q) = d(q, p)$ (symmetry).
> 3. $d(p, q) \leq d(p, r) + d(r, q)$ (==triangle inequality==).

^metric-space-definition

The triangle inequality can be derived from the [[cauchy-schwarz-inequality|Cauchy–Schwarz inequality]] in Euclidean spaces.

## Convexity

> [!abstract] Definition (Convex Set)
> A subset $S$ of a vector space is **convex** if for all $x, y \in S$ and $\lambda \in [0, 1]$,
>
> $$\lambda x + (1 - \lambda) y \in S,$$
>
> meaning the line segment connecting $x$ and $y$ lies entirely within $S$.

^convexity-definition

> [!example] Convex sets
> - Balls are convex.
> - Cells (closed rectangles) are convex.

## Algebraic Structure Hierarchy

> [!info]- Algebraic structure hierarchy
> In terms of structure, the chain of algebraic objects is:
>
> $$\text{Groups} \to \text{Rings} \to \text{Fields}.$$
>
> Each step adds more operations and axioms. See [[field-axioms|Field Axioms]] for the definition of a field.

## See Also
- [[cauchy-schwarz-inequality|Cauchy–Schwarz Inequality]]
- [[field-axioms|Field Axioms]]
- [[compactness|Compactness]] — topological properties of metric spaces
- [[convergent-sequences|Convergent Sequences]] — convergence in metric spaces
