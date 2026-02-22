---
aliases: [Algebraic Completeness, Algebraically Closed Field, Fundamental Theorem of Algebra]
tags: [real-analysis, algebra, complex-numbers]
source:
  - sources/2026-02-16/trig-euler-formula.jpeg
  - sources/2026-02-21/pi-definition-fta-inverse-trig.jpeg
date: 2026-02-16
---

# Algebraic Completeness

> [!abstract] Theorem (Fundamental Theorem of Algebra)
> The complex field $\mathbb{C}$ is **algebraically complete** (algebraically closed).
>
> That is, if $P(z) = \sum_{k=0}^{n} a_k z^k$ is a polynomial with $n \geq 1$ and $a_n \neq 0$, then $P(z) = 0$ for some $z \in \mathbb{C}$.

^fundamental-theorem-of-algebra

<!-- clarification: The standard term in modern algebra is "algebraically closed." The notes use "algebraically complete," which is equivalent. -->

**Corollary.** A polynomial of degree $n$ with coefficients in $\mathbb{C}$ has ==exactly $n$ roots (counted with multiplicity)==. This follows by induction: the Fundamental Theorem guarantees at least one root $z_0$, so we factor out $(z - z_0)$ to obtain a polynomial of degree $n - 1$, and repeat.

> [!tip] $\mathbb{C}$ is the smallest algebraically closed field containing $\mathbb{R}$.

There are proper subfields of $\mathbb{C}$ that are also algebraically closed. The most notable example is the field of **algebraic numbers** ($\overline{\mathbb{Q}}$):

$$\overline{\mathbb{Q}} = \{z \in \mathbb{C} : z \text{ is a root of some polynomial with rational coefficients}\}$$

This field:
- Is algebraically closed
- Is a proper subset of $\mathbb{C}$ (it's countable, while $\mathbb{C}$ is uncountable)
- Contains all rational numbers and all roots of polynomials with rational coefficients

But for $\mathbb{R}$ specifically $\mathbb{C}$ **is** the smallest algebraically closed field containing $\mathbb{R}$. This is because:

- $\mathbb{R}$ is not algebraically closed (e.g., $x^2 + 1 = 0$ has no real roots)
- To make it algebraically closed, you need to adjoin $i$ (a root of $x^2 + 1 = 0$)
- The result is exactly $\mathbb{C}$

So the statement would be more precisely: ==**$\mathbb{C}$ is the algebraic closure of $\mathbb{R}$.**==

## Non-Examples

> [!warning] Not algebraically complete
> The integers $\mathbb{Z}$, rationals $\mathbb{Q}$, and reals $\mathbb{R}$ are **not** algebraically complete.

<!-- clarification: For example, the polynomial x² + 1 = 0 has no solution in ℝ (or ℤ or ℚ), but it has solutions ±i in ℂ. -->

## Inverse Trigonometric Functions

Since $\sin$ and $\cos$ are continuous and strictly monotone on appropriate intervals (e.g., $\sin$ on $[-\pi/2, \pi/2]$ and $\cos$ on $[0, \pi]$), they have well-defined inverses $\arcsin$ and $\arccos$ on those restricted domains.

## See Also

- [[exponential-logarithm-and-euler-constant|Exponential Logarithm and Euler Constant]]
- [[power-series|Power Series]]
