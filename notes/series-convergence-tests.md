---
aliases: [Series Convergence Tests, Condensation Test, Cauchy Condensation Test, Ratio Test, Root Test]
tags: [real-analysis, series, convergence-tests]
source:
  - sources/2026-02-19/cauchy-sequences-and-condensation-test.jpeg
  - sources/2026-02-19/condensation-test-applications.jpeg
  - sources/2026-02-19/root-and-ratio-tests.jpeg
  - sources/2026-02-21/root-test-ratio-test.jpeg
date: 2026-02-19
---

# Series Convergence Tests

## Cauchy Condensation Test

> [!abstract] Theorem (Cauchy Condensation Test)
> Let $a_1 \geq a_2 \geq a_3 \geq \cdots \geq 0$ with $\lim_{n \to \infty} a_n = 0$. Then
>
> $$\sum_{n=1}^{\infty} a_n \quad \text{converges if and only if} \quad \sum_{k=0}^{\infty} 2^k \, a_{2^k} = a_1 + 2a_2 + 4a_4 + 8a_8 + \cdots \quad \text{converges.}$$

^cauchy-condensation-test

The idea is to group terms in blocks of size $2^k$ and compare. Because the sequence is decreasing, each block is controlled by its first term.

### Applications

> [!example] Logarithmic series
> Using the condensation test:
>
> $$\sum_{n=2}^{\infty} \frac{1}{n (\log n)^p} \quad \begin{cases} \text{converges} & \text{if } p > 1, \\ \text{diverges} & \text{if } p \leq 1. \end{cases}$$
>
> Pushing further with iterated logarithms:
>
> $$\sum_{n=3}^{\infty} \frac{1}{n \log n \cdot \log \log n} \quad \text{diverges,}$$
>
> $$\sum_{n=3}^{\infty} \frac{1}{n \log n \cdot (\log \log n)^2} \quad \text{converges.}$$

> [!tip] No sharp boundary
> The terms in these two series differ very little, yet one converges and the other diverges. By iterating further, one can construct pairs of convergent and divergent series that are arbitrarily close — ==there is no sharp boundary between convergence and divergence==.

## Ratio Test (d'Alembert)

### Basic Form

> [!abstract] Theorem (Ratio Test — Basic Form)
> Let $\sum a_n$ be a series with nonzero terms. If the limit
>
> $$L = \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right|$$
>
> exists, then:
> - $L < 1 \implies$ the series converges absolutely,
> - $L > 1 \implies$ the series diverges,
> - $L = 1 \implies$ **inconclusive**.

^ratio-test

### Limsup Form

> [!abstract] Theorem (Ratio Test — Limsup Form)
> More generally, $\sum a_n$ converges absolutely if
>
> $$\limsup_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| < 1.$$

^ratio-test-limsup

This is stronger than the basic form because it applies even when the ratio $|a_{n+1}/a_n|$ does not converge — the [[limsup-and-liminf|limsup]] always exists.

## Root Test (Cauchy)

### Basic Form

> [!abstract] Theorem (Root Test — Basic Form)
> If the limit
>
> $$d = \lim_{n \to \infty} \sqrt[n]{|a_n|}$$
>
> exists, the same trichotomy holds:
> - $d < 1 \implies$ convergence,
> - $d > 1 \implies$ divergence,
> - $d = 1 \implies$ **inconclusive**.

^root-test

### Limsup Form

> [!abstract] Theorem (Root Test — Limsup Form)
> More generally, $\sum a_n$ converges absolutely if
>
> $$\limsup_{n \to \infty} |a_n|^{1/n} < 1.$$

^root-test-limsup

This is better than the basic Cauchy root test because $|a_n|^{1/n}$ may not converge as a sequence — the plain limit may fail to exist — but the [[limsup-and-liminf|limsup]] always exists.

## Limitations

> [!warning] Inconclusive at $L = 1$
> Both the ratio test and root test are ==inconclusive when the limit equals $1$==. For example:
>
> - $\sum \frac{1}{n^2}$ converges, but both tests give $L = d = 1$.
> - $\sum \frac{1}{n}$ diverges, but both tests give $L = d = 1$.

When the ratio and root tests fail, more refined tests like the condensation test or comparison tests are needed.

## See Also
- [[limsup-and-liminf|Limsup and Liminf]] — the limsup used in the stronger forms of the root and ratio tests
- [[abels-test-for-convergence|Abel's Test for Convergence]]
- [[dirichlets-convergence-test|Dirichlet's Convergence Test]]
- [[cauchy-sequences|Cauchy Sequences]] — the Cauchy criterion for series
- [[absolute-convergence|Absolute Convergence]]
- [[power-series|Power Series]] — where the ratio and root tests determine the radius of convergence
