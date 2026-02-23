---
aliases: [Lebesgue Integration, Lebesgue integration, Lebesgue Integral, Lebesgue integral]
tags: [measure-theory, real-analysis]
source: [lebesgue-integration-1.jpeg, lebesgue-integration-2.jpeg, lebesgue-integration-3.jpeg, lebesgue-integration-4.jpeg, lebesgue-integration-5.jpeg]
date: 2026-02-17
---

# Lebesgue Integration

## Simple Functions

> [!abstract] Definition (Simple Function)
> A function whose range is finite is called a **simple function**.

Let $E \subset X$. The **characteristic function** (or indicator function) of $E$ is:

$$K_E(x) = \begin{cases} 1 & x \in E \\ 0 & x \notin E \end{cases}$$

Every simple function is a linear combination of characteristic functions:

$$s(x) = \sum_{i=1}^{n} c_i \, K_{E_i}(x).$$

Every function can be approximated by simple functions.

## The Lebesgue Integral

Let $E$ be a $\sigma$-ring measurable set with measure $\mu$. For a simple function $s(x) = \sum_{i=1}^{n} c_i \, K_{E_i}(x)$, define:

$$I_E(s) = \sum_{i=1}^{n} c_i \, \mu(E \cap E_i).$$

> [!abstract] Definition (Lebesgue Integral)
> The **Lebesgue integral** of a non-negative function $f$ over $E$ is:
>
> $$\int_E f \, d\mu = \sup I_E(s), \quad 0 \leq s \leq f.$$

^lebesgue-integral-def

## Positive and Negative Parts

For a general (not necessarily non-negative) function $f$, define the **positive part** and **negative part**:

$$f^+ = \max(f, 0), \qquad f^- = -\min(f, 0).$$

The above decomposition splits $f$ into positive and negative parts. Then the Lebesgue integral of $f$ is:

$$\int_E f \, d\mu = \int_E f^+ \, d\mu - \int_E f^- \, d\mu.$$

If both $\int_E f^+ \, d\mu$ and $\int_E f^- \, d\mu$ are finite, then $f \in \mathscr{L}(\mu)$ — that is, $f$ is ==**Lebesgue integrable**==.

## Intuition: Lebesgue vs. Riemann

> [!question] What distinguishes the Lebesgue integral from the Riemann integral?

The **Riemann integral** partitions the **domain** into subintervals and sums width $\times$ height — it asks "how tall is $f$ on each piece of the domain?"

The **Lebesgue integral** partitions the **range** and measures the **pre-images** — it asks "how much of the domain does $f$ spend near each value?"

> [!tip] Key Insight
> This shift is what makes the Lebesgue integral far more general: it only requires a measure on the domain, not any notion of intervals or ordering. The construction works over ==abstract measure spaces== where a Riemann-style partition wouldn't even make sense.

## Measure Zero and Almost Everywhere

Sets of measure $0$ always integrate to $0$.

Two functions $f \sim g$ if they differ only on a set of measure $0$. In this case their integrals agree:

$$\int_E f \, d\mu = \int_E g \, d\mu.$$

> [!abstract] Definition (Almost Everywhere)
> A property $P$ holds **almost everywhere** (a.e.) if $P$ holds for all $x \in E \setminus A$ where $\mu(A) = 0$. Equivalently, $P$ may fail, but only on a set of measure zero.

^almost-everywhere-def

## Monotone Convergence Theorem

> [!abstract] Theorem (Monotone Convergence)
> If $f_n(x) \to f(x)$ as $n \to \infty$ and the sequence is monotonically increasing:
>
> $$f_1 \leq f_2 \leq f_3 \leq \cdots,$$
>
> then
>
> $$\int_E f_n \, d\mu \to \int_E f \, d\mu.$$

^monotone-convergence-theorem

The usual arithmetic of addition and constant multiplication holds for the Lebesgue integral.

### Interchange of Sum and Integral

As a consequence of the Monotone Convergence Theorem, if $f(x) = \sum_{n=1}^{\infty} f_n(x)$ where each $f_n$ is non-negative and measurable, then

$$\int_E f \, d\mu = \sum_{n=1}^{\infty} \int_E f_n \, d\mu.$$

> [!tip] Punchline
> ==Pointwise convergence is enough== — no uniform convergence is required.

## See Also
- [[measurable-functions|Measurable Functions]]
- [[lebesgue-measure|Lebesgue Measure]]
- [[dominated-convergence-theorem|Dominated Convergence Theorem]]
- [[riesz-fischer-theorem|Riesz–Fischer Theorem]]
