---
aliases: [Pi and Square-Free Integers]
tags: [number-theory, pi, real-analysis]
source:
  - sources/2026-02-21/complex-trig-and-euler-formula.jpeg
  - sources/2026-02-21/archimedes-pi-and-sin-product.jpeg
date: 2026-02-21
---

# Pi and Square-Free Integers

## Archimedes' Algorithm for $\pi$

Draw a regular $n$-gon inscribed inside the unit circle and another $n$-gon circumscribed outside it. The perimeters (or areas) of these polygons give lower and upper bounds:

$$\text{inside}_n < \pi < \text{outside}_n$$

As $n \to \infty$, both bounds converge:

$$\text{inside}_n \approx \pi \approx \text{outside}_n$$

> [!info]- Historical note
> Archimedes used 96-gons to obtain $3 + 10/71 < \pi < 3 + 1/7$. The method requires only elementary geometry -- computing the perimeters of inscribed and circumscribed regular polygons via recursive doubling of sides.

## Square-Free Decomposition

> [!abstract] Theorem (Square-Free Decomposition)
> Every positive integer $n$ can be written as:
>
> $$n = k^2 \cdot p \cdot q \cdots r$$
>
> where $p, q, \ldots, r$ are all **square-free** (i.e., not divisible by any perfect square other than 1).

^square-free-decomposition

> [!info]- Precise formulation
> More precisely, we factor out the largest perfect square dividing $n$. The remaining factor $m = p \cdot q \cdots r$ is square-free, meaning for every prime $p$, $p^2$ does not divide $m$. This decomposition is unique: $n = k^2 \cdot m$ where $m$ is square-free.

## Probability of Being Square-Free

> [!abstract] Theorem (Square-Free Probability)
> The probability that a randomly chosen positive integer is square-free is:
>
> $$\frac{6}{\pi^2} = \frac{1}{\displaystyle\sum_{n=1}^{\infty} \frac{1}{n^2}}$$

^square-free-probability

> [!tip] Connection to the Basel problem
> This uses Euler's result that $\sum 1/n^2 = \pi^2/6$ (the Basel problem). ==The probability of being square-free equals $6/\pi^2 \approx 60.8\%$==.

> [!note]- Proof sketch
> The probability that $n$ is NOT divisible by $p^2$ for a given prime $p$ is $1 - 1/p^2$. By independence across primes, the probability of being square-free is $\prod_p (1 - 1/p^2) = 1/\zeta(2) = 6/\pi^2$.

## See Also

- [[exponential-logarithm-and-euler-constant|Exponential Logarithm and Euler Constant]]
- [[eulers-product-formula-and-wallis|Euler's Product Formula and Wallis's Formula]]
- [[series-convergence-tests|Series Convergence Tests]]
