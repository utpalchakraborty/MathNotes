---
aliases: [Riemann Zeta Function, Zeta Function]
tags: [number-theory, series, special-functions]
source: sources/2026-02-22/zeta-function-euler-product-mobius.jpeg
date: 2026-02-22
---

# Riemann Zeta Function

The Riemann zeta function is defined for $s > 1$ by

$$
\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s}.
$$

## Integral Representation of $\zeta(3)$

The value $\zeta(3)$ %%known as Apéry's constant%% admits the double integral representation

$$
\zeta(3) = \frac{1}{2} \int_0^1 \int_0^1 \frac{-\ln(xy)}{1 - xy} \, dx \, dy.
$$

## Euler Product

The zeta function has a product representation over all primes:

$$
\zeta(s) = \prod_{p \text{ prime}} \left(1 - \frac{1}{p^s}\right)^{-1}.
$$

This is proven by sieve (**Euler's proof**): expand each factor as a geometric series

$$
\left(1 - \frac{1}{p^s}\right)^{-1} = \sum_{k=0}^{\infty} \frac{1}{p^{ks}},
$$

and by the fundamental theorem of arithmetic, the product over all primes recovers every term $1/n^s$ exactly once.

The Euler product immediately implies that ==$\zeta(s) \neq 0$ for $s > 1$==, since no factor in the product vanishes.

## Connection to the Möbius Function

Taking the reciprocal of the Euler product gives

$$
\frac{1}{\zeta(s)} = \prod_{p \text{ prime}} \left(1 - \frac{1}{p^s}\right) = \sum_{n=1}^{\infty} \frac{\mu(n)}{n^s},
$$

where $\mu$ is the [[mobius-function|Möbius function]]. This identity is fundamental to analytic number theory and is a special case of a [[dirichlet-series|Dirichlet series]].

## Concept Map

```mermaid
graph TD
    ZetaDef["ζ(s) = Σ 1/nˢ<br/><i>Definition</i>"]
    Integral["ζ(3) = ½∫∫ −ln(xy)/(1−xy)<br/><i>Integral form</i>"]
    Euler["∏(1 − 1/pˢ)⁻¹<br/><i>Euler product</i>"]
    Recip["1/ζ(s) = ∏(1 − 1/pˢ)<br/><i>Reciprocal</i>"]
    Mobius["μ(n)<br/><i>Möbius function</i>"]
    Dirichlet["Σ a(n)/nˢ<br/><i>Dirichlet series</i>"]
    Prob["1/ζ(2) = 6/π²<br/><i>Squarefree density &<br/>coprimality probability</i>"]

    ZetaDef -->|"s = 3"| Integral
    ZetaDef -->|"sieve argument"| Euler
    Euler -->|"take reciprocal"| Recip
    Recip -->|"expand product"| Mobius
    Mobius -->|"a(n) = μ(n)"| Dirichlet
    ZetaDef -->|"a(n) = 1"| Dirichlet
    Recip -->|"evaluate at s = 2"| Prob

    style ZetaDef fill:#e8f4f8,stroke:#2196F3
    style Euler fill:#e8f4f8,stroke:#2196F3
    style Mobius fill:#f3e5f5,stroke:#9C27B0
    style Dirichlet fill:#fff3e0,stroke:#FF9800
    style Prob fill:#e8f5e9,stroke:#4CAF50
```

## See Also

- [[mobius-function|Möbius Function]] — the arithmetic function appearing in $1/\zeta(s)$
- [[dirichlet-series|Dirichlet Series]] — the general framework for series of the form $\sum a(n)/n^s$
- [[zeta-function-in-probability|Zeta Function in Probability]] — probabilistic interpretations via $\zeta(2)$
