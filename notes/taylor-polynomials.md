---
aliases: [Taylor Polynomials, Taylor Polynomial, Taylor Expansion]
tags: [real-analysis, differentiation, approximation]
source: sources/2026-02-19/compact-continuity-lhopital-taylor.jpeg
date: 2026-02-19
---

# Taylor Polynomials

## Definition

> [!abstract] Definition (Taylor Polynomial)
> If $f$ has $n$ derivatives at $a$, the **Taylor polynomial of degree $n$** centered at $a$ is
>
> $$P(t) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!} (t - a)^k.$$

^taylor-polynomial-definition

This is the ==unique polynomial of degree $\leq n$ that matches $f$ and its first $n$ derivatives at $a$==.

## Relation to Power Series

The Taylor polynomial is the $n$-th partial sum of the Taylor series. When the full Taylor series converges to $f$, i.e.,

$$f(x) = \sum_{k=0}^{\infty} \frac{f^{(k)}(a)}{k!} (x - a)^k,$$

we say $f$ is **analytic** at $a$. ==Not every smooth function is analytic== — see [[power-series|Power Series]].

## See Also
- [[power-series|Power Series]] — the infinite version; convergence and uniqueness
- [[lhopitals-rule|L'Hôpital's Rule]] — another tool using derivatives for limits
- [[differentiation-in-higher-dimensions|Differentiation in Higher Dimensions]]
