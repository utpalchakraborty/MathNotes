---
aliases: [Compactness, Compact Sets, Heine-Borel Theorem, Limit Points, Closed Sets]
tags: [real-analysis, topology]
source: [convexity-limit-points-compactness.jpeg, closedness-compactness-heine-borel.jpeg, cantor-set-convergent-sequences.jpeg]
date: 2025-07-06
---

# Compactness

## Limit Points

> [!abstract] Definition (Limit Point)
> A point $p$ is a **limit point** of a set $S$ if every neighborhood of $p$ contains a point of $S$ distinct from $p$ itself. <!-- clarification: the "distinct from p" condition is implicit in the scan -->

^limit-point-definition

> [!abstract] Definition (Closed Set)
> A set $S$ is **closed** if it contains all of its limit points.

^closed-set-definition

## Compact Spaces

> [!abstract] Definition (Compact)
> A set $K$ is **compact** if every open cover of $K$ has a finite subcover.

^compact-definition

> [!tip] Intuition
> $K$ is compact if you cannot construct an open cover that requires infinitely many elements — ==every cover can always be reduced to a finite one==.

## Closedness and Compactness

Closedness and compactness go together often:

- Compact subsets of [[metric-spaces|metric spaces]] are closed.
- Closed subsets of compact sets are compact.

## $k$-Cells

> [!abstract] Definition ($k$-Cell)
> A **$k$-cell** is the set of all points $x = (x_1, x_2, \ldots, x_k)$ such that
>
> $$a_j \leq x_j \leq b_j \quad (1 \leq j \leq k),$$
>
> i.e., each coordinate $x_j$ is bounded between $a_j$ and $b_j$ inclusive.

^k-cell-definition

> [!abstract] Theorem ($k$-Cells are Compact)
> Every $k$-cell is compact.

^k-cell-compact-theorem

## Heine--Borel Theorem

> [!abstract] Theorem (Heine--Borel)
> Every ==closed and bounded== subset of $\mathbb{R}^n$ is compact.

^heine-borel-theorem

## The Cantor Set

> [!example] The Cantor Set
> The **Cantor set** is a compact set of [[lebesgue-measure|Lebesgue measure]] zero with uncountably many elements. It demonstrates that a set can be ==uncountable yet negligibly small== in terms of measure.

## See Also
- [[metric-spaces|Metric Spaces]]
- [[convergent-sequences|Convergent Sequences]] — limit points can be characterized via sequences
- [[countability|Countability]] — the Cantor set is uncountable
- [[lebesgue-measure|Lebesgue Measure]]
