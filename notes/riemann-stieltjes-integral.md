---
aliases: [Riemann-Stieltjes Integral, Riemann–Stieltjes Integral, Stieltjes Integral]
tags: [real-analysis, integration]
source:
  - sources/2026-02-19/riemann-stieltjes-integral.jpeg
  - sources/2026-02-19/continuity-implies-integrability.jpeg
  - sources/2026-02-19/compactness-and-zeta-integral.jpeg
date: 2026-02-19
---

# Riemann–Stieltjes Integral

## Definition

> [!abstract] Definition (Riemann–Stieltjes Integral)
> Let $\alpha$ be monotonically increasing on $[a, b]$. The **Riemann–Stieltjes integral** of $f$ with respect to $\alpha$ is
>
> $$\int_a^b f(x) \, d\alpha(x).$$
>
> When $\alpha(x) = x$, this reduces to the ordinary Riemann integral $\int_a^b f \, dx$.

^riemann-stieltjes-def

> [!tip] The integrator $\alpha$ need not be continuous — this is one of the strengths of the Stieltjes generalization.

## Partitions

> [!abstract] Definition (Partition)
> A **partition** of $[a, b]$ is a finite set of points $\{x_0, x_1, \ldots, x_n\}$ with $a = x_0 < x_1 < \cdots < x_n = b$, together with a choice of one sample point from each subinterval.

^partition-def

## Continuity Implies Integrability

> [!abstract] Theorem (Continuity Implies Integrability)
> If $f$ is continuous on $[a, b]$, then $f \in \mathscr{R}(\alpha)$ on $[a, b]$ (i.e., $f$ is Riemann–Stieltjes integrable with respect to $\alpha$).

^continuity-implies-integrability

The proof relies on two facts supplied by continuity and [[compactness|compactness]]:

- **Continuity** guarantees the existence of $f$ and its limits at each point.
- **Compactness** of $[a, b]$ promotes continuity to ==**uniform continuity**==, ensuring that only finitely many subintervals are needed to control the oscillation of $f$ below any given $\epsilon$.

## Integral Representation of the Zeta Function

> [!abstract] Theorem (Zeta Function Integral)
> The Riemann–Stieltjes framework gives a clean integral representation of the Riemann zeta function. For $\operatorname{Re}(s) > 1$:
>
> $$\zeta(s) = s \int_1^{\infty} \frac{\lfloor x \rfloor}{x^{s+1}} \, dx,$$
>
> where $\lfloor x \rfloor$ is the floor function.

^zeta-integral-representation

This is established by computing the difference between the partial sums $\sum_{n=1}^{N} 1/n^s$ and the integral, and showing the difference vanishes as $N \to \infty$.

## See Also
- [[continuous-functions|Continuous Functions]] — continuity implies integrability
- [[compactness|Compactness]] — key to upgrading continuity to uniform continuity
- [[lebesgue-integration|Lebesgue Integration]] — the more general integral
- [[rectifiable-curves|Rectifiable Curves]] — arc length as an integral
