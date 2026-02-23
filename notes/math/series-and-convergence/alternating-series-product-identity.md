---
aliases: [Alternating Series Product Identity]
tags: [real-analysis, series, convergence]
source: sources/2026-02-22/cesaro-means-and-alternating-series-identity.jpeg
date: 2026-02-22
---

# Alternating Series Product Identity

A Parseval-type identity relating the square of an alternating series to the sum of squares and shifted product sums.

## Statement

> [!abstract] Theorem
> Let $\{a_n\}$ be a non-increasing sequence such that $\sum_{n=0}^{\infty} a_n^2$ converges. Define:
>
> $$S := \sum_{n=0}^{\infty} (-1)^n a_n, \qquad \delta_k := \sum_{n=0}^{\infty} a_n \cdot a_{n+k} \quad (k = 1, 2, 3, \ldots)$$
>
> Then $S$ and each $\delta_k$ converge. Furthermore,
>
> $$\Delta := \sum_{k=1}^{\infty} (-1)^{k-1} \delta_k$$
>
> also converges, and
>
> $$\sum_{n=0}^{\infty} a_n^2 = S^2 + 2\Delta.$$

^alternating-product-identity

%%clarification: The convergence of S follows from the alternating series test since {a_n} is non-increasing and a_n → 0 (guaranteed by the convergence of ∑a_n²). The convergence of each δ_k follows from Cauchy-Schwarz applied to the shifted product.%%

> [!tip] Interpretation
> The identity decomposes the "energy" $\sum a_n^2$ into the square of the alternating sum plus a correction term involving the shifted autocorrelation sums $\delta_k$. This is ==reminiscent of Parseval's identity== in Fourier analysis.

## See Also

- [[dirichlets-convergence-test|Dirichlet's Convergence Test]]
- [[absolute-convergence|Absolute Convergence]]
