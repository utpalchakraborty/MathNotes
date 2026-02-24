---
aliases: [Exponential Logarithm and Euler Constant]
tags: [real-analysis, exponential, logarithm, euler-constant, series, trigonometry, euler-formula]
source:
  - sources/2026-02-16/enadlog/e-1.jpeg
  - sources/2026-02-16/enadlog/e-2.jpeg
  - sources/2026-02-16/enadlog/e-gamma.jpeg
  - sources/2026-02-16/enadlog/log2.jpeg
  - sources/2026-02-16/enadlog/series-3.jpeg
  - sources/2026-02-16/enadlog/series-4.jpeg
  - sources/2026-02-16/trig-euler-formula.jpeg
  - sources/2026-02-21/pi-definition-fta-inverse-trig.jpeg
  - sources/2026-02-21/irrationality-of-e.jpeg
  - sources/2026-02-24/complex-exponential-derivation.jpeg
date: 2026-02-16
---

# The Exponential Function, Logarithm, and Euler's Constant

## Motivation: Irrational Powers

> [!question] Motivating Question
> Given the real numbers, we can define the standard operations: $a + b$, $a - b$, $a/b$, $a^b$, $a^{-b}$ — at least when $b$ is rational. But what does it mean to raise $a^x$ when $x$ is irrational?

To make sense of irrational (and complex) exponents, we need to construct the exponential function carefully.

## The Exponential Function

### Definition via Power Series

> [!abstract] Definition
> $$\exp(z) = E(z) = \sum_{n=0}^{\infty} \frac{z^n}{n!}$$
>
> This [[power-series|Power Series]] converges for all $z \in \mathbb{C}$ (radius of convergence $R = \infty$).

^exp-definition

### Derivation from the Differential Equation $f'(z) = f(z)$

The exponential series can be derived from scratch by seeking a [[power-series|power series]] $f(z) = \sum_{n=0}^{\infty} a_n z^n$ satisfying:

$$f'(z) = f(z), \qquad f(0) = 1$$

Differentiating term-by-term:

$$f'(z) = a_1 + 2a_2 z + 3a_3 z^2 + \cdots + n a_n z^{n-1} + \cdots$$

Matching coefficients in $f'(z) = f(z)$ gives $a_{n-1} = n a_n$, i.e., $a_n = \dfrac{a_{n-1}}{n}$. With $a_0 = f(0) = 1$, this yields ==**$a_n = \dfrac{1}{n!}$**== for all $n$, recovering the series definition above. The resulting series $\sum z^n/n!$ converges for all $z \in \mathbb{C}$ (radius of convergence $R = \infty$ by the [[power-series#^cauchy-hadamard-formula|Cauchy--Hadamard formula]], since $\limsup \sqrt[n]{1/n!} = 0$).

^exp-from-differential-equation

%%clarification: This derivation shows the exponential is the unique power series solution to f'(z) = f(z) with f(0) = 1. The approach works identically for real and complex variables — the coefficients are forced by the recurrence, and the resulting series has infinite radius of convergence.%%

How can the exponential series $e^z = \sum z^n/n!$ be derived from a differential equation?
?
Assume $f(z) = \sum a_n z^n$ satisfies $f'(z) = f(z)$ with $f(0) = 1$. Matching coefficients gives $a_{n-1} = n a_n$, so $a_n = a_{n-1}/n$. With $a_0 = 1$, this forces $a_n = 1/n!$.

### Key Properties

- $E(z_1) \cdot E(z_2) = E(z_1 + z_2)$ (the addition formula)
- $E'(z) = E(z)$ (this can also serve as the definition — see [[#^exp-from-differential-equation|derivation above]])
- $e^x$ is **continuous** and **strictly monotone** (increasing) on $\mathbb{R}$
- $\displaystyle\lim_{x \to \infty} x^n e^{-x} = 0$ for every $n$

<!-- clarification: The last property says the exponential grows faster than any polynomial. This follows from comparing with the tail of the power series for e^x. -->

### Fundamental Inequality

> [!abstract] Theorem (Fundamental Inequality)
> For all $x \in \mathbb{R}$:
>
> $$1 + x \leq e^x$$
>
> with equality if and only if $x = 0$. Equivalently, if $x \neq 0$:
>
> $$1 + x < e^x$$

^fundamental-inequality

<!-- clarification: This follows from the convexity of e^x — the tangent line at x=0 is y = 1 + x, and a convex function lies above its tangent lines. -->

## The Natural Logarithm

Since $e^x$ is continuous and strictly monotone, it has an inverse:

$$\log : (0, \infty) \to \mathbb{R}$$

(also written $\ln$).

### The Logarithm as an Integral

Writing $E$ for $\exp$ and $L$ for $\log$, from $L(E(x)) = x$ we differentiate:

$$L'(E(x)) \cdot E'(x) = 1$$

Since $E'(x) = E(x) = y$ (where $y = E(x)$), this gives $L'(y) = \frac{1}{y}$, and therefore:

> [!abstract] Definition (Logarithm as Integral)
> $$\log y = \int_1^y \frac{dt}{t}$$

^log-integral

## General Powers and Roots

Given the properties of $\exp$ and $\log$, we can define **powers and roots** $a^r$ for $a \in \mathbb{R}$, $a > 0$, and $r \in \mathbb{Q}$.

More generally, we can define:

$$a^z = \exp(z \log a), \quad z \in \mathbb{C}$$

<!-- clarification: This requires a > 0 so that log a is defined. For complex z, this gives a^z as a well-defined complex number. -->

### Irrational Powers Can Be Rational

> [!example] Existence of irrational $\alpha, \beta$ with $\alpha^\beta$ rational
> There exist irrationals $\alpha$ and $\beta$ such that $\alpha^\beta$ is rational.

> [!info]- Non-constructive proof
> Consider $\sqrt{2}^{\sqrt{2}}$. If it is rational, take $\alpha = \beta = \sqrt{2}$. If it is irrational, take $\alpha = \sqrt{2}^{\sqrt{2}}$ and $\beta = \sqrt{2}$, giving $\alpha^\beta = (\sqrt{2}^{\sqrt{2}})^{\sqrt{2}} = \sqrt{2}^2 = 2$. Either way, such $\alpha, \beta$ exist.

<!-- clarification: The classic proof is non-constructive. Consider √2^√2. If it is rational, take α = β = √2. If it is irrational, take α = √2^√2 and β = √2, giving α^β = (√2^√2)^√2 = √2^2 = 2. Either way, such α, β exist. -->

## Trigonometric Functions via the Exponential

Given the exponential and logarithm, we define the **cosine** and **sine** functions:

$$\cos(x) = \frac{e^{ix} + e^{-ix}}{2}, \qquad \sin(x) = \frac{e^{ix} - e^{-ix}}{2i}$$

From these definitions, the usual properties of $\sin$ and $\cos$ follow.

### Euler's Formula

> [!abstract] Theorem (Euler's Formula)
> $$E(ix) = \cos(x) + i\sin(x)$$

^eulers-formula

<!-- clarification: This is Euler's formula. It follows directly from the definitions above: cos(x) + i·sin(x) = (e^{ix} + e^{-ix})/2 + i·(e^{ix} - e^{-ix})/(2i) = (e^{ix} + e^{-ix})/2 + (e^{ix} - e^{-ix})/2 = e^{ix}. -->

## Bounds for $e$

> [!abstract] Theorem (Bounds for $e$)
> For all $n \geq 1$:
>
> $$\left(1 + \frac{1}{n}\right)^n < e < \left(1 + \frac{1}{n}\right)^{n+1}$$
>
> where:
> - $\left(1 + \frac{1}{n}\right)^n$ is **strictly increasing** in $n$
> - $\left(1 + \frac{1}{n}\right)^{n+1}$ is **strictly decreasing** in $n$

^bounds-for-e

<!-- clarification: Taking logs of the right inequality gives (n+1)log(1 + 1/n) > 1, i.e., log(1 + 1/n) > 1/(n+1). The left inequality gives log(1 + 1/n) < 1/n. Together: 1/(n+1) < log(1 + 1/n) < 1/n. -->

## The Euler-Mascheroni Constant

> [!abstract] Definition (Euler-Mascheroni Constant)
> The **Euler-Mascheroni constant** is:
>
> $$\gamma := \lim_{n \to \infty} \left(1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n} - \log n\right) = \lim_{n \to \infty} (H_n - \log n)$$
>
> where $H_n = \sum_{k=1}^{n} \frac{1}{k}$ is the $n$-th harmonic number.

^euler-mascheroni-constant

**Properties:**
- $\gamma$ exists.
- $0 < \gamma < 1$.
- ==It is **not known** whether $\gamma$ is rational or irrational.==

### The Defining Sequence Is Strictly Decreasing

> [!abstract] Proposition
> Let $\gamma_n = H_n - \log n$. Then $\gamma_n > \gamma_{n+1}$ for all $n$.

> [!note]- Proof
> We need $\gamma_n - \gamma_{n+1} > 0$:
>
> $$\gamma_n - \gamma_{n+1} = (H_n - \log n) - (H_{n+1} - \log(n+1)) = \log\!\left(1 + \frac{1}{n}\right) - \frac{1}{n+1}$$
>
> From the bounds for $e$, the right inequality $(1 + 1/n)^{n+1} > e$ gives:
>
> $$\log\!\left(1 + \frac{1}{n}\right) > \frac{1}{n+1}$$
>
> Hence $\gamma_n - \gamma_{n+1} > 0$, so the sequence is strictly decreasing. $\blacksquare$

## A Limit via [[tannerys-theorem|Tannery's Theorem]]

> [!abstract] Theorem
> $$\lim_{n \to \infty} \left\{ \left(\frac{n}{n}\right)^n + \left(\frac{n-1}{n}\right)^n + \left(\frac{n-2}{n}\right)^n + \cdots + \left(\frac{1}{n}\right)^n \right\} = \frac{e}{e-1}$$

^tannery-limit

> [!note]- Proof
> Write the left-hand side as:
>
> $$\text{LHS} = \lim_{n \to \infty} \sum_{k=0}^{n-1} a_k(n), \quad \text{where } a_k(n) = \left(\frac{n-k}{n}\right)^n = \left(1 - \frac{k}{n}\right)^n$$
>
> **Pointwise limit:** For each fixed $k$:
>
> $$\lim_{n \to \infty} a_k(n) = \lim_{n \to \infty} \left(1 - \frac{k}{n}\right)^n = e^{-k}$$
>
> **Domination:** By the fundamental inequality with $x = -k/n \neq 0$ (for $k \geq 1$):
>
> $$1 - \frac{k}{n} < e^{-k/n} \implies \left(1 - \frac{k}{n}\right)^n < \left(e^{-k/n}\right)^n = e^{-k}$$
>
> So $|a_k(n)| \leq e^{-k}$, and the dominating series $\sum_{k=0}^{\infty} e^{-k}$ converges.
>
> **By [[tannerys-theorem|Tannery's theorem]]:**
>
> $$\text{LHS} = \sum_{k=0}^{\infty} \lim_{n \to \infty} a_k(n) = \sum_{k=0}^{\infty} e^{-k} = \frac{1}{1 - e^{-1}} = \frac{e}{e-1} \qquad \blacksquare$$

## The Alternating Harmonic Series

> [!abstract] Theorem (Alternating Harmonic Series)
> $$\log 2 = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5} - \cdots = \sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n}$$

^alternating-harmonic-series

> [!note]- Proof
> Consider the partial sums $S_{2n} = \sum_{k=1}^{2n} \frac{(-1)^{k-1}}{k}$. Split into even and odd parts:
>
> - $A_n = 1 + \frac{1}{3} + \cdots + \frac{1}{2n-1}$ (odd-indexed terms)
> - $B_n = \frac{1}{2} + \frac{1}{4} + \cdots + \frac{1}{2n}$ (even-indexed terms)
>
> Then:
>
> $$S_{2n} = A_n - B_n$$
>
> $$H_{2n} = A_n + B_n$$
>
> Note that $B_n = \frac{1}{2}\left(1 + \frac{1}{2} + \cdots + \frac{1}{n}\right) = \frac{1}{2} H_n$. Therefore:
>
> $$S_{2n} = H_{2n} - 2B_n = H_{2n} - H_n$$
>
> As $n \to \infty$, the asymptotic expansion $H_m \sim \gamma + \log m$ gives:
>
> $$H_{2n} \sim \gamma + \log(2n) = \gamma + \log n + \log 2$$
>
> $$H_n \sim \gamma + \log n$$
>
> $$\implies S_{2n} = H_{2n} - H_n \to \log 2 \qquad \blacksquare$$

<!-- clarification: More precisely, H_m = γ + log m + o(1), so the γ and log n terms cancel exactly in the difference H_{2n} - H_n, leaving log 2. Since S_{2n} → log 2 and S_{2n+1} = S_{2n} + 1/(2n+1) → log 2 as well, the full series converges to log 2. -->

## Definition of $\pi$

> [!abstract] Definition ($\pi$)
> We define $\pi$ as the number satisfying:
>
> $$\cos\!\left(\frac{\pi}{2}\right) = 0, \qquad 3 < \pi < 4$$
>
> That is, ==$\pi/2$ is the smallest positive zero of the cosine function==, and $\pi$ lies strictly between $3$ and $4$.

^definition-of-pi

> [!info]- Almost-integer phenomena
> The expression $e^{\pi\sqrt{n}}$ is remarkably close to an integer for many values of $n$. For example:
>
> - $e^{\pi} - \pi \approx 20$
> - $e^{\pi\sqrt{163}}$ is extraordinarily close to an integer (this is related to the Heegner number $163$ and the theory of complex multiplication)

## Irrationality of $e$

> [!abstract] Theorem (Irrationality of $e$)
> The number $e$ is irrational.

^irrationality-of-e

> [!note]- Proof
> Assume for contradiction that $e = m/n$ for some positive integers $m, n$. Since $e^{-1} = n/m$, we can write:
>
> $$\frac{n}{m} = e^{-1} = \sum_{k=0}^{\infty} \frac{(-1)^k}{k!}$$
>
> Separating the first $m+1$ terms from the tail:
>
> $$\frac{n}{m} - \sum_{k=0}^{m} \frac{(-1)^k}{k!} = \sum_{k=m+1}^{\infty} \frac{(-1)^k}{k!}$$
>
> Multiply both sides by $m!$. The left-hand side becomes:
>
> $$\frac{n \cdot m!}{m} - \sum_{k=0}^{m} \frac{(-1)^k \, m!}{k!} = n \cdot (m-1)! - \sum_{k=0}^{m} \frac{(-1)^k \, m!}{k!}$$
>
> Each term $m!/k!$ for $k \leq m$ is an integer, and $n \cdot (m-1)!$ is an integer, so the entire LHS is an integer.
>
> The right-hand side becomes:
>
> $$\sum_{k=m+1}^{\infty} \frac{(-1)^k \, m!}{k!}$$
>
> For $k > m$, we have $m!/k! < 1$ (since $k! = m! \cdot (m+1)(m+2) \cdots k$ and each additional factor exceeds $1$). Therefore the RHS is an alternating series of terms with absolute value strictly less than $1$, so it is strictly between $-1$ and $1$ — in particular, it is **not** an integer.
>
> This contradicts the LHS being an integer. ==Hence $e$ is irrational.== $\blacksquare$

## See Also

- [[power-series|Power Series]]
- [[continuous-functions|Continuity]]
- [[uniform-convergence-and-cauchy-criterion|Uniform Convergence and Cauchy Criterion]]
- [[tannerys-theorem|Tannery's Theorem]]
- [[algebraic-completeness|Algebraic Completeness]]
- [[fourier-series|Fourier Series]]
- [[analytic-functions-and-cauchy-riemann|Analytic Functions and Cauchy-Riemann Equations]] — analyticity and the exponential as a holomorphic function
