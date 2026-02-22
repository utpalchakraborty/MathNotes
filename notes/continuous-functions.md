---
aliases: [Continuity, Continuous Functions]
tags: [real-analysis, continuity, IVT, fixed-point, monotone-functions, connectedness]
source:
  - sources/2026-02-16/8.jpeg
  - sources/2026-02-16/9.jpeg
  - sources/2026-02-16/10.jpeg
  - sources/2026-02-16/11.jpeg
  - sources/2026-02-19/riemann-series-theorem-and-continuity.jpeg
pages: [8, 9, 10, 11]
date: 2026-02-16
---

# Continuous Functions

## Intuition

> [!tip] Core Intuition
> The precision of the output can be controlled by restricting input changes to a small enough value. That is, for any desired output tolerance $\epsilon$, there exists an input tolerance $\delta$ that guarantees it.

## Definitions

There are two standard definitions of continuity:

> [!abstract] Definition (Metric, $\epsilon$-$\delta$)
> A function $f \colon X \to Y$ between [[metric-spaces|metric spaces]] is continuous at $p \in X$ if for every $\epsilon > 0$ there exists $\delta > 0$ such that
>
> $$d_X(x, p) < \delta \implies d_Y(f(x), f(p)) < \epsilon.$$

^epsilon-delta-continuity

This definition requires a metric on both the domain and codomain.

> [!abstract] Definition (Topological)
> A function $f \colon X \to Y$ between topological spaces is continuous if the preimage of every open set is open:
>
> $$V \subseteq Y \text{ open} \implies f^{-1}(V) \subseteq X \text{ open.}$$

^topological-continuity

This definition only requires a topology, not a metric. In metric spaces the two definitions coincide.

## Basic Examples

> [!example] Examples
> - **Polynomials** $f \colon \mathbb{R}^n \to \mathbb{R}^n$ are continuous.
> - **Rational functions** $P/Q \colon \mathbb{R}^n \to \mathbb{R}^n$ (with $Q \neq 0$) are continuous on their domain.

## Uniform Continuity on Compact Sets

Compact sets allow nice continuity properties. ==Continuous maps from a [[compactness|compact]] set are **uniformly continuous**== — the $\delta$ in the $\epsilon$-$\delta$ definition can be chosen independently of the point.

## Boundedness on Compact Intervals

A continuous real-valued function on a closed and bounded interval is bounded.

> [!info]- Details
> This is a consequence of the Extreme Value Theorem — the continuous image of a compact set is compact, hence closed and bounded in $\mathbb{R}$.

## Intermediate Value Theorem

> [!abstract] Theorem (Intermediate Value Theorem)
> Let $f$ be a real continuous function and $I$ an interval. Then $f(I)$ is also an interval.

^intermediate-value-theorem

==Connectedness is the key==: continuous functions preserve connectedness, and connected subsets of $\mathbb{R}$ are precisely the intervals. On a compact interval, $f(I)$ has a maximum and minimum and takes all values between them.

**General form.** $f: \mathbb{R}^n \to \mathbb{R}^m$ preserves connectedness if $f$ is continuous.

In fact it is stronger: continuous image of **path connected** is path connected.

## Fixed Point Theorems

### 1-D Fixed Point Theorem (from IVT)

> [!abstract] Theorem (1-D Fixed Point)
> If $f: \mathbb{R} \to \mathbb{R}$ is continuous and maps an interval $I$ to itself, then $f$ has a fixed point.

^1d-fixed-point-theorem

> [!note]- Proof
> Consider $g(x) = f(x) - x$. Since $f$ maps $I = [a,b]$ to itself, $g(a) = f(a) - a \geq 0$ and $g(b) = f(b) - b \leq 0$. By IVT, $g$ has a zero, so $f(x) = x$ for some $x$ in $I$.

So ==IVT $\implies$ fixed point theorem in 1-D==.

### Brouwer's Fixed Point Theorem

> [!abstract] Theorem (Brouwer's Fixed Point Theorem)
> Let $f: \mathbb{R}^n \to \mathbb{R}^n$ map $U$ to $U$. If $U$ is compact and convex, then the map has a fixed point.

^brouwer-fixed-point-theorem

> [!info]- Details
> The 1-D case above is the special case of Brouwer for $n = 1$, where the compact convex set is a closed interval.

## Monotone Functions

Let $f$ be a monotone function on $\mathbb{R}$.

- $f$ has an **uncountable** number of points of continuity and at most a **countable** number of points of discontinuity.
- If the range of $f$ is an interval, then $f$ is continuous.
- If $f$ is continuous, then $f$ has an inverse.

The relationships: continuous and one-to-one $\iff$ has an inverse, and on an interval, continuous and one-to-one $\iff$ strictly monotone.

## Thomae Function (Modified Dirichlet)

> [!abstract] Definition (Thomae Function)
> $$T(x) = \begin{cases} 1/q & \text{if } x \in \mathbb{Q} \text{ and } x = p/q \text{ in lowest terms} \\ 0 & \text{if } x \text{ is irrational} \end{cases}$$

^thomae-function

$T(x)$ is ==**continuous at all irrationals** and **discontinuous at all rationals**==.

> [!warning] Important Caveat
> The reverse cannot exist — there is no function that is continuous at all rationals and discontinuous at all irrationals.

## Volterra's Theorem

> [!abstract] Theorem (Volterra's Theorem)
> Two pointwise discontinuous functions (each having a dense set of continuity points) defined on a non-empty open interval always share a point of **continuity**.

^volterras-theorem

> [!note]- Proof Sketch
> The set of continuity points of any function is a $G_\delta$ set. If both functions have dense continuity sets, these are dense $G_\delta$ sets. By the Baire category theorem, the intersection of two dense $G_\delta$ sets in a complete metric space is dense $G_\delta$, hence non-empty. This is why the reverse of the Thomae function cannot exist — $\mathbb{Q}$ is not a $G_\delta$ set, so no function can have $\mathbb{Q}$ as its set of continuity points.

This explains why the reverse Thomae function is impossible: $\mathbb{Q}$ is not a $G_\delta$ set, so it cannot be the continuity set of any function.

## Topology of Discontinuity Sets

> [!tip] The $G_\delta$ Constraint
> The set of continuity points of **any** function $\mathbb{R} \to \mathbb{R}$ must be a $G_\delta$ set (countable intersection of open sets). ==This is a topological constraint, not a cardinality one.==

- The irrationals **are** $G_\delta$ — so they can be a continuity set. Thomae demonstrates this.
- $\mathbb{Q}$ is **not** $G_\delta$ (by the Baire Category Theorem) — so $\mathbb{Q}$ can never be a continuity set. The reverse Thomae is impossible.

The constraint is not about how many discontinuities a function has:

- Dense, countable discontinuities (like $\mathbb{Q}$)? Perfectly fine — Thomae does it.
- Uncountable discontinuities? Also fine — e.g. the characteristic function of a fat Cantor set.
- But continuous exactly on $\mathbb{Q}$? Topologically forbidden, regardless of cardinality.

Analysis cares about the **category** (meager vs. comeager, $G_\delta$ vs. $F_\sigma$) of discontinuity sets more than their size. A dense countable set and a dense uncountable set can behave very differently in the Baire category sense, even though both are "infinite" and "dense."

## See Also
- [[uniform-convergence-and-cauchy-criterion|Uniform Convergence and Cauchy Criterion]]
- [[equicontinuity|Equicontinuity]]
- [[compactness|Compact Spaces]]
- Connectedness
