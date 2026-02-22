---
aliases: [Cauchy Sequences, Cauchy Sequence, Cauchy Criterion for Series]
tags: [real-analysis, sequences, series]
source: sources/2026-02-19/cauchy-sequences-and-condensation-test.jpeg
date: 2026-02-19
---

# Cauchy Sequences

## Definition

> [!abstract] Definition (Cauchy Sequence)
> A sequence $\{p_n\}$ in a [[metric-spaces|metric space]] $(X, d)$ is a **Cauchy sequence** if for every $\epsilon > 0$ there exists $N$ such that
>
> $$d(p_n, p_m) < \epsilon \quad \text{for all } n, m \geq N.$$

^cauchy-sequence-def

Intuitively, the ==entire tail of the sequence is getting uniformly squeezed together== — not just consecutive terms, but *all* pairs of terms past some index.

## Cauchy vs. Consecutive Convergence

> [!warning] Cauchy is strictly stronger
> The Cauchy condition is strictly stronger than requiring $d(x_n, x_{n+1}) \to 0$. A sequence can have consecutive terms getting arbitrarily close while still wandering off (e.g., partial sums of the harmonic series).

## Complete Spaces

> [!abstract] Definition (Complete Space)
> A [[metric-spaces|metric space]] is **complete** if every Cauchy sequence in the space converges to a point in the space. In complete spaces, ==Cauchy sequences always converge==.

^complete-space-def

> [!example] Examples of Complete Spaces
> $\mathbb{R}$, $\mathbb{R}^n$, any closed subset of a complete space.

## Cauchy Criterion for Series

> [!abstract] Theorem (Cauchy Criterion for Series)
> A series $\sum a_n$ satisfies the **Cauchy criterion** if for every $\epsilon > 0$ there exists $N$ such that
>
> $$\left| \sum_{k=n}^{m} a_k \right| \leq \epsilon \quad \text{for all } m \geq n \geq N.$$

^cauchy-criterion-for-series

This is simply the Cauchy condition applied to the sequence of partial sums. In $\mathbb{R}$ (which is complete), ==the Cauchy criterion is equivalent to convergence==.

## See Also
- [[convergent-sequences|Convergent Sequences]]
- [[metric-spaces|Metric Spaces]]
- [[series-convergence-tests|Series Convergence Tests]] — tests for determining whether a series converges
- [[absolute-convergence|Absolute Convergence]]
