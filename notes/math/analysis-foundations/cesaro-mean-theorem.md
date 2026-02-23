---
aliases: [Cesàro Mean Theorem, Cauchy's AM Theorem, Cesàro Means]
tags: [real-analysis, sequences, convergence]
source: sources/2026-02-22/cesaro-means-and-alternating-series-identity.jpeg
date: 2026-02-22
---

# Cesàro Mean Theorem

The Cesàro mean theorem (also called Cauchy's arithmetic mean theorem) states that the arithmetic means of a convergent sequence share the same limit.

## Statement

> [!abstract] Theorem (Cesàro Mean Theorem)
> If $\{a_n\}$ is a sequence converging to $L$, then the sequence of arithmetic means
>
> $$m_n := \frac{1}{n}(a_1 + a_2 + \cdots + a_n)$$
>
> also converges to $L$.

^cesaro-mean-theorem

> [!warning] Converse is False
> The converse does not hold in general. The sequence $a_n = (-1)^n$ has Cesàro mean converging to $0$, but $\{a_n\}$ itself diverges.

## Proof Sketch

> [!note]- Proof
> Fix $\epsilon > 0$. Since $a_n \to L$, there exists $N$ such that $|a_n - L| < \epsilon$ for all $n > N$. Then
>
> $$|m_n - L| = \left|\frac{1}{n}\sum_{k=1}^{n}(a_k - L)\right| \leq \frac{1}{n}\sum_{k=1}^{N}|a_k - L| + \frac{1}{n}\sum_{k=N+1}^{n}|a_k - L|.$$
>
> The first sum is a fixed constant divided by $n$, which vanishes as $n \to \infty$. The second sum is bounded by $\frac{n - N}{n}\epsilon < \epsilon$. $\blacksquare$

## See Also

- [[cauchy-sequences|Cauchy Sequences]]
- [[tannerys-theorem|Tannery's Theorem]]
