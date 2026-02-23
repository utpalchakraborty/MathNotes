---
aliases: [Convergent Sequences, Convergence of Sequences, Sequences in Metric Spaces]
tags: [real-analysis, sequences]
source: cantor-set-convergent-sequences.jpeg
date: 2025-07-06
---

# Convergent Sequences

## Definition

> [!abstract] Definition (Convergent Sequence)
> A sequence $\{p_n\}$ in a [[metric-spaces|metric space]] $X$ **converges** to $p \in X$ if
>
> $$\lim_{n \to \infty} p_n = p,$$
>
> meaning for every $\epsilon > 0$ there exists $N$ such that $d(p_n, p) < \epsilon$ for all $n > N$.

^convergent-sequence-definition

> [!warning] Ambient space matters
> The convergence depends on both the sequence $\{p_n\}$ and the ==ambient space $X$==.

## Uniqueness of Limits

> [!abstract] Theorem (Uniqueness of Limits)
> If $p_n \to p_x$ and $p_n \to p_y$, then $p_x = p_y$. That is, ==limits in a metric space are unique==.

^uniqueness-of-limits

## Limit Points via Sequences

> [!abstract] Theorem (Limit Points via Sequences)
> If $E \subset X$ and $p$ is a [[compactness|limit point]] of $E$, then there exists a sequence $\{p_n\}$ in $E$ such that
>
> $$\lim_{n \to \infty} p_n = p.$$

^limit-points-via-sequences

> [!tip] Sequential characterization
> This characterizes limit points in metric spaces ==entirely in terms of convergent sequences==.

## Algebraic Limit Theorem

> [!abstract] Theorem (Algebraic Limit Theorem)
> Convergence extends naturally to $\mathbb{R}^n$ and respects algebraic operations. If
>
> $$\lim_{n \to \infty} x_n = \sigma \quad \text{and} \quad \lim_{n \to \infty} y_n = s \quad \text{in } \mathbb{R}^n,$$
>
> then
>
> $$\lim_{n \to \infty} (x_n + y_n) = \sigma + s.$$

^algebraic-limit-theorem

## See Also
- [[cauchy-sequences|Cauchy Sequences]] — the stronger condition for convergence in metric spaces
- [[metric-spaces|Metric Spaces]]
- [[compactness|Compactness]] — compact sets and limit points
- [[uniform-convergence-and-cauchy-criterion|Uniform Convergence and Cauchy Criterion]]
