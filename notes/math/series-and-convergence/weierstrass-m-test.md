---
aliases: [Weierstrass M-Test]
tags: [real-analysis, series, uniform-convergence, absolute-convergence]
source: sources/2026-02-16/7.jpeg
page: 7
date: 2026-02-16
---

# Weierstrass M-Test

## Statement

> [!abstract] Theorem (Weierstrass M-Test)
> Let $\{f_n\}_{n=0}^{\infty}$ be a sequence of functions. If there exist non-negative constants $M_n$ such that
>
> $$|f_n(x)| \leq M_n \quad \text{for all } x,$$
>
> and $\sum_{n=0}^{\infty} M_n$ converges, then ==$\sum_{n=0}^{\infty} f_n$ converges **absolutely** and **uniformly**==.

^weierstrass-m-test

<!-- clarification: The original notes use a_n rather than f_n(x), but the standard formulation emphasizes that the terms are functions and the bound uses absolute value. -->

## Intuition

> [!tip] Dominating envelope
> The convergent series of constants $\sum M_n$ acts as a ==dominating "envelope"== — if each function term is bounded by $M_n$ regardless of $x$, then the rate of convergence of the original series is controlled uniformly across all $x$.

$$\sum M_n \text{ converges} \implies \sum f_n \text{ converges absolutely and uniformly.}$$

## Connection to the Dominated Convergence Theorem

The M-test and the [[Dominated Convergence Theorem]] share the same principle: ==**domination controls convergence**==. The M-test dominates each term by a constant $M_n$ (independent of $x$), while DCT dominates a sequence by an integrable function $g(x)$ (which may depend on $x$).

The M-test is the more restrictive condition, but it implies DCT's hypotheses directly: if $\sum f_n$ converges by the M-test, the partial sums $S_N(x) = \sum_{n=0}^{N} f_n(x)$ are dominated by the constant $g = \sum M_n < \infty$. DCT then gives

$$\int \sum_{n=0}^{\infty} f_n = \sum_{n=0}^{\infty} \int f_n.$$

That is, the M-test provides uniform convergence, which in turn justifies ==interchanging summation and integration== via DCT.

## See Also
- [[uniform-convergence-and-cauchy-criterion|Uniform Convergence and Cauchy Criterion]]
- [[stone-weierstrass-theorem|Stone-Weierstrass Theorem]]
- [[Dominated Convergence Theorem]]
- [[series-convergence-tests|Series]]
