---
aliases: [Abel Summation by Parts]
tags: [real-analysis, series, summation]
source:
  - sources/2026-02-21/abel-summation-by-parts-1.jpeg
  - sources/2026-02-21/abel-summation-by-parts-2-bounded-variation.jpeg
date: 2026-02-21
---

# Abel Summation by Parts

> **Aside:** $\zeta(2k)$ can also be specified using [[bernoulli-and-euler-numbers|Bernoulli numbers]].

## Motivation: Integration by Parts

> [!question] Motivating analogy
> Recall the continuous integration by parts formula:
>
> $$\int_a^b f'(x)\,g(x)\,dx + \int_a^b f(x)\,g'(x)\,dx = f(b)\,g(b) - f(a)\,g(a).$$
>
> Abel's summation by parts is ==the discrete (series) analogue of this identity==.

## Series Version (Abel's Summation Formula)

> [!abstract] Theorem (Abel's Summation Formula)
> Given sequences $\{a_k\}$ and $\{b_k\}$, the discrete analogue reads:
>
> $$\sum_{k=m}^{n}(a_{k+1} - a_k)\,b_{k+1} + \sum_{k=m}^{n} a_k\,(b_{k+1} - b_k) = a_{n+1}\,b_{n+1} - a_m\,b_m.$$

^abel-summation-formula

> [!note]- Telescoping Derivation
> Expanding the left-hand side term by term, each summand contributes:
>
> $$(a_{k+1} - a_k)\,b_{k+1} + a_k\,(b_{k+1} - b_k) = a_{k+1}\,b_{k+1} - a_k\,b_{k+1} + a_k\,b_{k+1} - a_k\,b_k = a_{k+1}\,b_{k+1} - a_k\,b_k.$$
>
> Summing from $k = m$ to $k = n$, this telescopes:
>
> $$\sum_{k=m}^{n}\bigl(a_{k+1}\,b_{k+1} - a_k\,b_k\bigr) = a_{n+1}\,b_{n+1} - a_m\,b_m.$$

## Example: Summing the First $n$ Integers

> [!example] Summing the first $n$ integers
> Put $a_k = k$ and $b_k = k - 1$. Then $a_{k+1} - a_k = 1$ and $b_{k+1} - b_k = 1$, so the formula gives:
>
> $$\sum_{k=1}^{n} b_{k+1} + \sum_{k=1}^{n} a_k = a_{n+1}\,b_{n+1} - a_1\,b_1.$$
>
> Since $a_1\,b_1 = 1 \cdot 0 = 0$, $a_{n+1} = n+1$, and $b_{n+1} = n$, we obtain:
>
> $$\sum_{k=1}^{n} k + \sum_{k=1}^{n} k = n(n+1),$$
>
> and therefore
>
> $$\sum_{i=1}^{n} i = \frac{n(n+1)}{2}.$$

We can also sum the squares and the cubes using similar substitutions in the Abel summation formula.

## See Also

- [[series-convergence-tests|Series Convergence Tests]]
- [[power-series|Power Series]]
- [[riemann-stieltjes-integral|Riemann-Stieltjes Integral]]
- [[tannerys-theorem|Tannery's Theorem]]
