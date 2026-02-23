---
aliases: [Arctangent Series]
tags: [real-analysis, series, pi, trigonometry, power-series]
source: sources/2026-02-22/arctangent-series-and-leibniz.jpeg
date: 2026-02-22
---

# Arctangent Series

## Taylor Series for $\tan^{-1}(x)$

> [!abstract] Theorem (Arctangent Power Series)
> The Taylor series for the arctangent function is:
>
> $$\tan^{-1}(x) = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{2n+1} = x - \frac{x^3}{3} + \frac{x^5}{5} - \frac{x^7}{7} + \cdots$$
>
> This series converges for $|x| \leq 1$.

^arctangent-taylor-series

%%clarification: The series is obtained by integrating the geometric series $\frac{1}{1+t^2} = \sum_{n=0}^{\infty} (-1)^n t^{2n}$ term by term from $0$ to $x$. Convergence at the endpoints $x = \pm 1$ follows from Abel's theorem.%%

## Leibniz Formula for $\pi/4$

Setting $x = 1$ in the arctangent series and noting that $\tan^{-1}(1) = \pi/4$:

> [!abstract] Theorem (Leibniz Formula)
> $$\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \cdots = \sum_{n=0}^{\infty} \frac{(-1)^n}{2n+1}$$

^leibniz-formula

> [!warning] Slow convergence
> Although elegant, the Leibniz formula converges ==extremely slowly==. Hundreds of terms are needed for even modest accuracy. Faster formulas for $\pi$ are obtained by applying the arctangent addition formula below.

## Arctangent Addition Formula

Starting from the tangent addition formula:

$$\tan(\theta + \phi) = \frac{\tan\theta + \tan\phi}{1 - \tan\theta\tan\phi}$$

set $x = \tan\theta$ and $y = \tan\phi$, so that $\theta = \tan^{-1}x$ and $\phi = \tan^{-1}y$. Then:

> [!abstract] Theorem (Arctangent Addition Formula)
> $$\tan^{-1}x + \tan^{-1}y = \tan^{-1}\!\left(\frac{x + y}{1 - xy}\right)$$
>
> provided $xy < 1$.

^arctangent-addition-formula

%%clarification: The restriction $xy < 1$ ensures the result lies in $(-\pi/2, \pi/2)$, the principal branch of $\tan^{-1}$. When $xy \geq 1$, a correction of $\pm\pi$ is needed.%%

> [!example] Decomposition of $\pi/4$
> Setting $x = 1/2$ and $y = 1/3$:
>
> $$\frac{x + y}{1 - xy} = \frac{1/2 + 1/3}{1 - 1/6} = \frac{5/6}{5/6} = 1$$
>
> Therefore:
>
> $$\frac{\pi}{4} = \tan^{-1}1 = \tan^{-1}\frac{1}{2} + \tan^{-1}\frac{1}{3}$$
>
> ==Expanding each term via the arctangent Taylor series gives a faster-converging formula for $\pi$ than the Leibniz series==, since $1/2$ and $1/3$ produce geometric decay.

## See Also

- [[pi-formulas-from-arctangent|Pi Formulas from Arctangent]] -- Machin's formula and the Fibonacci arctangent identity
- [[power-series|Power Series]] -- general power series theory
- [[taylor-polynomials|Taylor Polynomials]] -- finite partial sums of the Taylor series
- [[exponential-logarithm-and-euler-constant|Exponential Logarithm and Euler Constant]] -- related series expansions
- [[pi-and-square-free-integers|Pi and Square-Free Integers]] -- another $\pi$ result in the vault
- [[eulers-product-formula-and-wallis|Euler's Product Formula and Wallis's Formula]] -- product representations of $\pi$
