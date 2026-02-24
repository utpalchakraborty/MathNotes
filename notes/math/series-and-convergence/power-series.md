---
aliases: [Power Series]
tags: [real-analysis, series, power-series, convergence, differentiability]
source:
  - sources/2026-02-16/enadlog/series-1.jpeg
  - sources/2026-02-16/enadlog/series-2.jpeg
  - sources/2026-02-16/enadlog/series-4.jpeg
  - sources/2026-02-21/root-ratio-kummers-test.jpeg
  - sources/2026-02-22/composition-of-power-series.jpeg
  - sources/2026-02-22/power-series-division-bernoulli-numbers.jpeg
  - sources/2026-02-24/complex-power-series-convergence.jpeg
date: 2026-02-16
---

# Power Series

## Definition

> [!abstract] Definition (Power Series)
> A **power series** centered at $0$ is a function of the form:
>
> $$f(x) = \sum_{n=0}^{\infty} c_n x^n$$
>
> More generally, a power series centered at $a$:
>
> $$\sum_{n=0}^{\infty} c_n (x - a)^n$$

^power-series-definition

## Convergence Properties

If $f(x)$ converges with radius of convergence $R > 0$, then it converges ==**uniformly** on $[-r, r]$ for every $0 < r < R$==.

<!-- clarification: Uniform convergence holds on every compact subset strictly inside the interval of convergence (-R, R), not necessarily at the endpoints ±R themselves. -->

## Radius of Convergence

> [!abstract] Theorem (Cauchy--Hadamard Formula)
> The **Cauchy--Hadamard formula** gives the radius of convergence of a power series $\sum c_n z^n$ explicitly in terms of the coefficients:
>
> $$R = \frac{1}{\limsup_{n \to \infty} |c_n|^{1/n}}$$
>
> with the conventions $1/0 = \infty$ and $1/\infty = 0$.

^cauchy-hadamard-formula

This formula applies equally to real and complex power series $\sum a_n z^n$: the radius of convergence is $R = 1 / \limsup |a_n|^{1/n}$.

> [!info]- Root test vs. ratio test
> **Relationship between root and ratio tests:** If the root test is inconclusive for determining the radius of convergence, then the ratio test is also inconclusive. That is, ==the root test is at least as powerful as the ratio test==. This follows from the general inequality $\liminf |a_{n+1}/a_n| \leq \liminf |a_n|^{1/n} \leq \limsup |a_n|^{1/n} \leq \limsup |a_{n+1}/a_n|$.

<!-- clarification: The Cauchy–Hadamard formula uses limsup rather than lim because the limit of |c_n|^{1/n} may not exist. The limsup always exists (in the extended reals) and correctly captures the radius of convergence. -->

## Smoothness

A convergent power series is:

- **Continuous** on $(-R, R)$
- **Differentiable** on $(-R, R)$
- Has **derivatives of all orders** on $(-R, R)$

<!-- clarification: These properties follow from term-by-term differentiation of the power series, which is justified by uniform convergence on compact subsets. See the derivative convergence theorem in [[uniform-convergence-and-cauchy-criterion|Uniform Convergence and Cauchy Criterion]]. -->

## Coefficients from Derivatives

The $k$-th coefficient is determined by the $k$-th derivative at the center:

$$f^{(k)}(0) = k! \cdot c_k \quad \implies \quad c_k = \frac{f^{(k)}(0)}{k!}$$

> [!warning] Smooth does not imply analytic
> This does **not** mean that every infinitely differentiable function can be reconstructed from its derivatives at $0$. ==A function can be $C^\infty$ without equaling its Taylor series.==

<!-- clarification: The classic counterexample is f(x) = e^{-1/x²} for x ≠ 0 and f(0) = 0. This function has f^(k)(0) = 0 for all k, so its Taylor series at 0 is identically 0, yet the function itself is not zero. Such functions are smooth but not analytic. -->

## Uniqueness of Power Series

> [!abstract] Theorem (Uniqueness)
> If two power series converge on an interval $(-R, R)$:
>
> $$\sum_{n=0}^{\infty} a_n x^n = \sum_{n=0}^{\infty} b_n x^n \quad \text{for all } x \in (-R, R)$$
>
> then $a_n = b_n$ for all $n$.

^power-series-uniqueness

<!-- clarification: In fact, equality on any set with a limit point in (-R, R) suffices, since the difference would be a power series vanishing on a set with a limit point, forcing all coefficients to be zero (identity theorem). -->

## Double Series and Rearrangement

Given a double sequence $\{a_{ij}\}$ with $i = 1, 2, 3, \ldots$ and $j = 1, 2, 3, \ldots$:

If $\displaystyle\sum_{j=1}^{\infty} |a_{ij}| = b_i$ (i.e., each row converges absolutely) and $\displaystyle\sum_{i=1}^{\infty} b_i$ converges, then ==the order of summation can be interchanged==:

$$\sum_{i=1}^{\infty} \sum_{j=1}^{\infty} a_{ij} = \sum_{j=1}^{\infty} \sum_{i=1}^{\infty} a_{ij}$$

<!-- clarification: This is the discrete analogue of Fubini's theorem. The key condition is that the iterated sum converges absolutely — without this, rearranging the order of summation can change the value (cf. conditionally convergent series). -->

## Composition of Power Series

> [!abstract] Theorem (Composition of Power Series)
> If $f(z) = \sum_{n=0}^{\infty} c_n z^n$ has radius of convergence $R > 0$ and $g(z) = \sum_{n=0}^{\infty} a_n z^n$ is a power series, then $f(g(z))$ can be defined and converges for those $z$ satisfying
>
> $$\sum_{n=0}^{\infty} |a_n z^n| < R.$$
>
> Moreover, $f(g(z))$ is ==exactly the series obtained by replacing $z$ with $g(z)$ and collecting powers==.

^power-series-composition

%%clarification: The condition requires absolute convergence of g(z) within the radius of convergence of f, not just convergence. This ensures the rearrangement of terms needed to collect powers is justified.%%

## Division of Power Series

> [!abstract] Theorem (Division of Power Series)
> If $f(z) = \sum c_n z^n$ and $g(z) = \sum d_n z^n$ are power series with ==**$g(0) \neq 0$**==, then $f(z)/g(z)$ is also a power series, convergent for $z$ within the radius of convergence of both series.

^power-series-division

> [!tip] Reduction to reciprocal
> To prove division, it suffices to show that $1/g(z)$ is a power series — then $f(z)/g(z) = f(z) \cdot (1/g(z))$ is a product of power series, which is handled by the [[absolute-convergence|Cauchy product]].

## Complex Power Series

%%clarification: The theory developed above for real power series extends naturally to the complex setting, where the interval of convergence becomes a disk in the complex plane.%%

In the complex setting, a power series takes the form:

$$P(z) = a_0 + a_1 z + a_2 z^2 + \cdots = \sum_{n=0}^{\infty} a_n z^n, \qquad z \in \mathbb{C}$$

### Circle of Convergence

> [!definition] Definition (Circle of Convergence)
> Every complex power series $P(z) = \sum a_n z^n$ has a **circle of convergence** — a circle $|z| = R$ in the complex plane such that:
>
> - $|z| < R$: the series **converges absolutely**
> - $|z| > R$: the series **diverges**
> - $|z| = R$: convergence must be checked case-by-case
>
> The radius $R$ is given by the [[#^cauchy-hadamard-formula|Cauchy--Hadamard formula]]:
>
> $$\frac{1}{R} = \limsup_{n \to \infty} \sqrt[n]{|a_n|}$$

^circle-of-convergence

%%clarification: The circle of convergence is the complex analogue of the interval of convergence $(-R, R)$ for real power series. On the real line, $|x| < R$ gives an interval; in the complex plane, $|z| < R$ gives an open disk.%%

What is the complex analogue of the interval of convergence for a real power series?
?
The **circle of convergence** $|z| = R$, where $R$ is the radius of convergence. The series converges absolutely inside the open disk $|z| < R$ and diverges outside $|z| > R$.

### Analyticity

> [!theorem] Theorem (Convergent Power Series are Analytic)
> If $P(z) = \sum a_n z^n$ converges for $|z| < R$, then ==$P(z)$ is [[analytic-functions-and-cauchy-riemann|analytic]] on the open disk $|z| < R$==.

^complex-power-series-analytic

%%clarification: Analyticity in the complex sense (holomorphicity) is a much stronger property than real smoothness — a function analytic on an open set is automatically infinitely differentiable there and equals its own Taylor series. This is in stark contrast to the real case, where smooth does not imply analytic.%%

### Uniform Convergence on Compact Subdisks

> [!theorem] Theorem (Uniform Convergence on Compact Subdisks)
> If $P(z) = \sum a_n z^n$ has radius of convergence $R > 0$, then for every $0 < \rho < R$, the series ==converges **uniformly** on the closed disk $|z| \leq \rho$==.

^uniform-convergence-compact-subdisk

%%clarification: This is the complex version of the real statement that a power series converges uniformly on $[-r, r]$ for $0 < r < R$. Uniform convergence on compact subdisks is key: it justifies term-by-term differentiation and integration of complex power series, and underpins the proof that convergent power series are analytic.%%

How does the uniform convergence property of complex power series differ from the real case?
?
In the real case, a power series converges uniformly on compact subintervals $[-r, r]$ for $0 < r < R$. In the complex case, it converges uniformly on compact subdisks $|z| \leq \rho$ for $0 < \rho < R$. Both are instances of uniform convergence on compact subsets of the domain of convergence.

## See Also

- [[taylor-polynomials|Taylor Polynomials]] — finite partial sums of the Taylor series
- [[exponential-logarithm-and-euler-constant|Exponential Logarithm and Euler Constant]]
- [[uniform-convergence-and-cauchy-criterion|Uniform Convergence and Cauchy Criterion]]
- [[weierstrass-m-test|Weierstrass M-Test]]
- [[tannerys-theorem|Tannery's Theorem]]
- [[absolute-convergence|Absolute Convergence]] — rearrangement and the Cauchy product of series
- [[limsup-and-liminf|Limsup and Liminf]] — the Cauchy--Hadamard formula relies on limsup
- [[series-convergence-tests|Series Convergence Tests]] — root test, ratio test, and their relationship
- [[bernoulli-and-euler-numbers|Bernoulli and Euler Numbers]] — defined via power series division
- [[analytic-functions-and-cauchy-riemann|Analytic Functions and Cauchy-Riemann Equations]] — analyticity of convergent power series in the complex plane
