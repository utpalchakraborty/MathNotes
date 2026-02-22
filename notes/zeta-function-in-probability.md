---
aliases: [Zeta Function in Probability, Probabilistic Number Theory]
tags: [number-theory, series]
source: sources/2026-02-22/probabilistic-number-theory-zeta.jpeg
date: 2026-02-22
---

# Zeta Function in Probability

The [[riemann-zeta-function|Riemann zeta function]] at $s = 2$ has elegant probabilistic interpretations in number theory.

## Squarefree Numbers

> [!theorem] Squarefree Density
> The probability that a natural number is **squarefree** (not divisible by any perfect square other than $1$) is
>
> $$
> \frac{1}{\zeta(2)} = \frac{6}{\pi^2} \approx 0.6079.
> $$

## Coprimality

> [!theorem] Coprimality Probability
> The probability that two natural numbers chosen at random are **coprime** (share no common factor) is
>
> $$
> \frac{1}{\zeta(2)} = \frac{6}{\pi^2}.
> $$

## Proof Sketch via Euler Product

Both results follow from the same idea. The probability that a random number is divisible by a prime $p$ is $1/p$. For divisibility by $p^2$, the probability is $1/p^2$. Since divisibility by different primes is independent:

- A number is squarefree iff it is not divisible by $p^2$ for any prime $p$.
- Two numbers are coprime iff they do not share any prime factor $p$.

In both cases, taking the product over all primes gives

$$
\prod_{p \text{ prime}} \left(1 - \frac{1}{p^2}\right) = \frac{1}{\zeta(2)} = \frac{6}{\pi^2}.
$$

This is precisely the reciprocal of the [[riemann-zeta-function|Euler product]] for $\zeta(s)$ evaluated at $s = 2$, using the classical result $\zeta(2) = \pi^2/6$.

## See Also

- [[riemann-zeta-function|Riemann Zeta Function]] — the Euler product underlying these identities
- [[mobius-function|Möbius Function]] — $\mu(n) \neq 0$ exactly when $n$ is squarefree
