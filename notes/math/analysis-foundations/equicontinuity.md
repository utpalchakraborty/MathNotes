---
aliases: [Equicontinuity]
tags: [real-analysis, equicontinuity, uniform-continuity, uniform-convergence]
source:
  - sources/2026-02-16/4.jpeg
  - sources/2026-02-16/5.jpeg
pages: [4, 5]
date: 2026-02-16
---

# Equicontinuity

## Definition

> [!abstract] Definition (Equicontinuity)
> Let $\mathscr{F}$ be a family of functions with $f \in \mathscr{F}$. The family $\mathscr{F}$ is **equicontinuous** if for every $\epsilon > 0$ there is a $\delta > 0$ such that
>
> $$|f(x) - f(y)| < \epsilon$$
>
> whenever $d(x, y) \leq \delta$, for all $x, y$ and all $f \in \mathscr{F}$.

^equicontinuity-definition

## Basic Consequence

==Equicontinuity $\implies$ uniform continuity== of each member function.

## $C(X)$ and Equicontinuity

Let $X$ be a metric space. Denote by $C(X)$ the set of all complex-valued continuous bounded functions on $X$.

> [!abstract] Theorem
> If $X$ is compact and $\{f_n\} \subset C(X)$ converges uniformly, then $\{f_n\}$ is equicontinuous.

^uniform-convergence-equicontinuity

> [!note]- Proof Idea
> The uniform limit $f$ is uniformly continuous on compact $X$, the tail of the sequence is uniformly close to $f$, and the finitely many remaining terms are each individually uniformly continuous on the compact space, so ==a single $\delta$ works for all $n$==.

## See Also
- [[continuous-functions|Uniform Continuity]]
- [[Arzelà-Ascoli Theorem]]
- [[compactness|Compact Spaces]]
- [[uniform-convergence-and-cauchy-criterion|Uniform Convergence and Cauchy Criterion]]
