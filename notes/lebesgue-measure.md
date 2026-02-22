---
aliases: [Lebesgue Measure, Lebesgue measure]
tags: [measure-theory, real-analysis]
source: [rings-and-set-functions.jpeg, set-functions-and-elementary-sets.jpeg, regularity-of-measures.jpeg, outer-measure-and-symmetric-difference.jpeg, measurable-sets-and-lebesgue-measure.jpeg]
date: 2026-02-17
---

# Lebesgue Measure

To construct the Lebesgue measure, we begin with the algebraic structure of set families and build up through set functions, regularity, and outer measure.

## Rings and $\sigma$-Rings of Sets

> [!abstract] Definition (Ring of Sets)
> $\mathcal{R}$ is a **ring** of sets if for all $A, B \in \mathcal{R}$:
>
> - $A \cup B \in \mathcal{R}$
> - $A - B \in \mathcal{R}$

^ring-of-sets-def

It follows that intersections are also in the ring:

$$A \cap B = A - (A - B) \in \mathcal{R}.$$

> [!abstract] Definition ($\sigma$-Ring)
> $\mathcal{R}$ is a **$\sigma$-ring** if, in addition, countable unions remain in $\mathcal{R}$: whenever $A_n \in \mathcal{R}$ for all $n$,
>
> $$\bigcup_{n=1}^{\infty} A_n \in \mathcal{R}.$$

^sigma-ring-def

This implies countable intersections also belong to $\mathcal{R}$:

$$\bigcap_{n=1}^{\infty} A_n \in \mathcal{R}.$$

<!-- This follows by De Morgan: ∩A_n = A_1 - ∪(A_1 - A_n), where each A_1 - A_n ∈ R and the countable union is in R by the σ-ring property. -->

## Set Functions

> [!abstract] Definition (Set Function)
> A **set function** is a map $\phi \colon \mathcal{R} \to \mathbb{R}$ assigning a real number $\phi(A)$ to each $A \in \mathcal{R}$.

$\phi$ is **additive** if whenever $A \cap B = \varnothing$:

$$\phi(A \cup B) = \phi(A) + \phi(B).$$

$\phi$ is **countably additive** (or $\sigma$-additive) if for pairwise disjoint $\{A_n\}$:

$$\phi\!\left(\bigcup_{n=1}^{\infty} A_n\right) = \sum_{n=1}^{\infty} \phi(A_n).$$

## Elementary Sets in $\mathbb{R}^p$

Let $\mathcal{E}$ denote the family of all elementary subsets of $\mathbb{R}^p$ (finite unions of intervals). $\mathcal{E}$ is a ring but ==**not** a $\sigma$-ring==.

For an interval $I = [a_1, b_1) \times \cdots \times [a_p, b_p)$ in $\mathbb{R}^p$, define:

$$m(I) = \prod_{i=1}^{p} (b_i - a_i).$$

This gives the usual length ($p = 1$), area ($p = 2$), or volume ($p = 3$).

The function $m$ is well defined on $\mathcal{E}$ and is **additive**.

## Regularity

> [!abstract] Definition (Regular Set Function)
> A set function $\phi$ on $\mathcal{E}$ is **regular** if for every $A \in \mathcal{E}$ and every $\varepsilon > 0$, there exist $F, G \in \mathcal{E}$ with $F$ closed and $G$ open such that:
>
> $$\phi(G) - \varepsilon \leq \phi(A) \leq \phi(F) + \varepsilon.$$

^regular-set-function-def

> [!tip] Key Insight
> Regularity means the measure of any elementary set can be approximated arbitrarily closely by the measures of both open and closed sets.

The function $m$ defined above is regular.

## Outer Measure

Given a measure $\mu$ on $\mathcal{E}$ that is additive, finite, and regular, we can extend it to a larger class of sets. For any set $E$ with $E \subset \bigcup_{n=1}^{\infty} A_n$ where $A_n \in \mathcal{E}$, define the **outer measure**:

> [!abstract] Definition (Outer Measure)
> $$\mu^*(E) = \inf \sum_{n=1}^{\infty} \mu(A_n),$$
>
> where the infimum is taken over all countable coverings of $E$ by sets in $\mathcal{E}$.

^outer-measure-def

For every $A \in \mathcal{E}$, the outer measure agrees with the original measure:

$$\mu^*(A) = \mu(A).$$

## Symmetric Difference and Convergence of Sets

The **symmetric difference** of two sets is:

$$S(A, B) = (A - B) \cup (B - A).$$

This induces a pseudo-metric on sets via:

$$d(A, B) = \mu^*(S(A, B)).$$

We say $A_n \to A$ if:

$$\lim_{n \to \infty} d(A_n, A) = 0.$$

## Measurable Sets and the Lebesgue Measure

> [!abstract] Definition (Measurable Sets)
> A set $A$ is **finitely $\mu$-measurable** if it can be approximated in the distance $d$ by elementary sets.
>
> A countable union of finitely $\mu$-measurable sets is **$\mu$-measurable**. The class of all $\mu$-measurable sets is denoted $\mathfrak{M}(\mu)$.

^measurable-sets-def

- $\mathfrak{M}(\mu)$ forms a **$\sigma$-ring**.
- $\mu^*$ restricted to $\mathfrak{M}(\mu)$ is a **measure** (countably additive set function).

> [!tip] Punchline
> The measure $m$ on elementary sets in $\mathbb{R}^p$, extended via this construction, is the ==**Lebesgue measure**==.

## See Also
- [[measurable-functions|Measurable Functions]]
- [[lebesgue-integration|Lebesgue Integration]]
