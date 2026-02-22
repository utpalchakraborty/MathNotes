---
aliases: [Dirichlet Series]
tags: [number-theory, series, special-functions]
source: sources/2026-02-22/dirichlet-series.jpeg
date: 2026-02-22
---

# Dirichlet Series

> [!definition] Dirichlet Series
> A **Dirichlet series** is a series of the form
>
> $$
> S(s) = \sum_{n=1}^{\infty} \frac{a(n)}{n^s},
> $$
>
> where $a : \mathbb{N} \to \mathbb{C}$ is an arithmetic function and $s$ is a complex variable.

This theme occurs over and over in analytic number theory: different choices of the arithmetic function $a(n)$ connect to different functions of the [[riemann-zeta-function|Riemann zeta function]] $\zeta(s)$.

## Key Examples

| Arithmetic function $a(n)$ | Dirichlet series |
|:---|:---|
| $a(n) = 1$ | $\displaystyle\sum_{n=1}^{\infty} \frac{1}{n^s} = \zeta(s)$ |
| $a(n) = \mu(n)$ | $\displaystyle\sum_{n=1}^{\infty} \frac{\mu(n)}{n^s} = \frac{1}{\zeta(s)}$ |

Here $\mu$ is the [[mobius-function|Möbius function]].

The first identity is simply the definition of $\zeta(s)$. The second follows from the Euler product representation %%see the riemann-zeta-function note for the derivation%%.

## See Also

- [[riemann-zeta-function|Riemann Zeta Function]] — the Dirichlet series with $a(n) = 1$
- [[mobius-function|Möbius Function]] — generates $1/\zeta(s)$ as a Dirichlet series
- [[dirichlets-convergence-test|Dirichlet's Convergence Test]] — a convergence criterion for series (different topic, same namesake)
