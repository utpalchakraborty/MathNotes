---
aliases: [Tannery's Theorem, Tannery's theorem, Tannery's Theorem for Products]
tags: [real-analysis, series, convergence, limit-interchange]
source:
  - sources/2026-02-22/infinite-products-3.jpeg
date: 2026-02-16
---

# Tannery's Theorem

Tannery's theorem gives conditions under which a limit can be exchanged with a summation whose number of terms is growing. It is the ==discrete analogue of the Dominated Convergence Theorem==.

## Statement

> [!abstract] Theorem (Tannery's Theorem)
> Let $\{a_k(n)\}$ be a double sequence such that:
>
> 1. **Pointwise limit:** For each fixed $k \geq 0$, $\displaystyle\lim_{n \to \infty} a_k(n) = a_k$.
> 2. **Domination:** There exist constants $M_k \geq 0$ with $|a_k(n)| \leq M_k$ for all $n$, and $\displaystyle\sum_{k=0}^{\infty} M_k < \infty$.
>
> If $N(n) \to \infty$ as $n \to \infty$, then:
>
> $$\lim_{n \to \infty} \sum_{k=0}^{N(n)} a_k(n) = \sum_{k=0}^{\infty} a_k$$

^tannerys-theorem

## Proof Sketch

> [!note]- Proof
> Fix $\epsilon > 0$. Since $\sum M_k$ converges, choose $K$ large enough that $\sum_{k=K+1}^{\infty} M_k < \epsilon$. Then for $n$ large enough that $N(n) > K$:
>
> $$\left|\sum_{k=0}^{N(n)} a_k(n) - \sum_{k=0}^{\infty} a_k\right| \leq \underbrace{\sum_{k=0}^{K} |a_k(n) - a_k|}_{\to\, 0 \text{ (finite sum)}} + \underbrace{\sum_{k=K+1}^{N(n)} |a_k(n)|}_{\leq\, \sum_{k=K+1}^{\infty} M_k\, <\, \epsilon} + \underbrace{\sum_{k=K+1}^{\infty} |a_k|}_{\leq\, \sum_{k=K+1}^{\infty} M_k\, <\, \epsilon}$$
>
> The first sum vanishes for $n$ sufficiently large (finite number of pointwise limits), and the remaining two sums are each less than $\epsilon$. $\blacksquare$

## Key Point

> [!tip] Key Insight
> The crucial feature is that the **number of summands** $N(n)$ is allowed to grow with $n$. Without the domination condition, interchanging the limit and summation can fail. The dominating sequence $\{M_k\}$ ==controls the tails uniformly in $n$==, which is what makes the exchange valid.

## Example

> [!example] Example
> See [[exponential-logarithm-and-euler-constant#A Limit via Tannery's Theorem|Exponential Logarithm and Euler Constant]] for an application:
>
> $$\lim_{n \to \infty} \sum_{k=0}^{n-1} \left(1 - \frac{k}{n}\right)^n = \frac{e}{e-1}$$
>
> Here $a_k(n) = (1 - k/n)^n$, the pointwise limit is $e^{-k}$, and the dominating bound $M_k = e^{-k}$ comes from the inequality $1 + x \leq e^x$.

## Product Version

> [!abstract] Theorem (Tannery's Theorem for Products)
> Let $\{a_k(n)\}$ be a double sequence such that:
>
> 1. **Pointwise limit:** For each fixed $k$, $\displaystyle\lim_{n \to \infty} a_k(n)$ exists.
> 2. **Domination:** There is a convergent series $\displaystyle\sum_{k=1}^{\infty} M_k$ such that $|a_k(n)| \leq M_k$ for all $k < m_n$ and all $n$.
>
> If $m_n \to \infty$ and $n \to \infty$, then:
>
> $$\lim_{n \to \infty} \prod_{k=1}^{m_n} \big(1 + a_k(n)\big) = \prod_{k=1}^{\infty} \big(1 + \lim_{n \to \infty} a_k(n)\big).$$

^tannerys-theorem-products

> [!tip] Reduction to Sums
> If the product series is absolutely convergent, then converting into a logarithm and expanding $\log(1 + a_k(n))$ into a series gives a double summable series. This reduces the product interchange to the sum version of Tannery's theorem.

## See Also

- [[infinite-products|Infinite Products]]
- [[exponential-logarithm-and-euler-constant|Exponential Logarithm and Euler Constant]]
- [[uniform-convergence-and-cauchy-criterion|Uniform Convergence and Cauchy Criterion]]
