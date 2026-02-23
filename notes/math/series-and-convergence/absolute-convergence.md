---
aliases: [Absolute Convergence, Cauchy Product, Mertens' Theorem, Riemann Series Theorem, Riemann Rearrangement Theorem]
tags: [real-analysis, series, convergence]
source:
  - sources/2026-02-19/absolute-convergence-and-cauchy-product.jpeg
  - sources/2026-02-19/riemann-series-theorem-and-continuity.jpeg
  - sources/2026-02-22/riemanns-rearrangement-theorem.jpeg
  - sources/2026-02-22/cauchy-product-mertens-theorem.jpeg
date: 2026-02-19
---

# Absolute Convergence

## Definition

> [!abstract] Definition (Absolute Convergence)
> A series $\sum a_n$ converges **absolutely** if
>
> $$\sum |a_n| \quad \text{converges.}$$

^absolute-convergence-def

For series with all nonnegative terms, absolute convergence is the same as convergence.

## Properties

Absolute convergence is ==strictly stronger than conditional convergence== and grants several useful properties:

- **Rearrangement invariance**: The sum does not change under any rearrangement of terms.
- **Term-by-term addition**: Absolutely convergent series can be added term by term.

## Cauchy Product

> [!abstract] Definition (Cauchy Product)
> Given two series $A = \sum a_n$ and $B = \sum b_n$, their **Cauchy product** is the series $\sum c_n$ where
>
> $$c_n = \sum_{k=0}^{n} a_k \, b_{n-k}.$$

^cauchy-product-def

This is the formula one obtains by multiplying the series formally and collecting terms of the same index — analogous to multiplying polynomials or [[power-series|power series]] and grouping by powers.

> [!abstract] Theorem (Mertens' Theorem)
> If both $\sum a_n$ and $\sum b_n$ converge, and at least one of them converges absolutely, then
>
> $$\sum c_n = \left(\sum a_n\right)\left(\sum b_n\right).$$

^mertens-theorem

<!-- clarification: Without absolute convergence of at least one factor, the Cauchy product can diverge even when both factors converge. A classical counterexample uses a_n = b_n = (-1)^n / sqrt(n+1). -->

> [!warning] Absolute convergence required
> Without absolute convergence of at least one factor, the Cauchy product can diverge even when both factors converge.

> [!tip] Converse direction
> If you can show by other means that the Cauchy product $\sum c_n$ converges, then it ==automatically converges to $AB$== — you need not verify absolute convergence of either factor. This is a consequence of [[abels-test-for-convergence|Abel's Test]].

## Riemann Series Theorem

> [!abstract] Theorem (Riemann Rearrangement)
> If $\sum a_n$ converges but not absolutely (i.e., converges conditionally), then for any $\alpha, \beta$ with
>
> $$-\infty \leq \alpha \leq \beta \leq +\infty,$$
>
> there exists a rearrangement of the series whose partial sums $S_N$ satisfy
>
> $$\liminf_{N \to \infty} S_N = \alpha \quad \text{and} \quad \limsup_{N \to \infty} S_N = \beta.$$

^riemann-rearrangement-theorem

In particular:
- Taking $\alpha = \beta = S$ for any finite $S$ gives a rearrangement converging to $S$.
- Taking $\alpha = \beta = +\infty$ gives a rearrangement diverging to $+\infty$.
- Taking $\alpha \neq \beta$ gives a rearrangement whose partial sums oscillate.

> [!tip] Why absolute convergence matters
> ==Absolute convergence is exactly the condition that ensures the sum is independent of the order of summation.==

> [!info]- Why absolute convergence is immune
> If $\sum a_n$ converges absolutely, let $P_+ = \sum_{a_n > 0} a_n$ and $P_- = \sum_{a_n < 0} |a_n|$. Both are finite. Every partial sum of any rearrangement lies in the interval $[-(P_-), P_+]$, so partial sums cannot escape to a different limit.

### Intuitive Construction of Rearrangements

> [!example]- Constructing a rearrangement to any target
> Say you want the series to sum to $\alpha$. Separate the terms into positive terms $p_n$ and negative terms $q_n$.
>
> 1. Select enough positive terms to exceed $\alpha$
> 2. Start selecting negative terms to go below $\alpha$
> 3. Select positive terms to exceed $\alpha$ again
> 4. Repeat
>
> This works because conditional convergence means both $\sum p_n = +\infty$ and $\sum q_n = -\infty$ (if either were finite, the series would converge absolutely), so you ==never run out of terms to overshoot in either direction==. Meanwhile, $p_n \to 0$ and $q_n \to 0$ ensures the overshoots get smaller, so the partial sums converge to $\alpha$.

## See Also
- [[cauchy-sequences|Cauchy Sequences]] — Cauchy criterion for series
- [[series-convergence-tests|Series Convergence Tests]]
- [[power-series|Power Series]] — where the Cauchy product arises naturally
