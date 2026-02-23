---
aliases: [Bounded Variation Sequences, Sequences of Bounded Variation]
tags: [real-analysis, sequences, convergence]
source: sources/2026-02-21/abel-summation-by-parts-2-bounded-variation.jpeg
date: 2026-02-21
---

# Bounded Variation Sequences

## Definition

> [!abstract] Definition (Bounded Variation)
> A sequence $\{a_n\}$ of complex numbers is said to have **bounded variation** if
>
> $$\sum_{n=1}^{\infty} |a_{n+1} - a_n| < \infty.$$

^bounded-variation-def

## Geometric Interpretation

> [!info]- Geometric Interpretation
> Plotting the terms $a_1, a_2, a_3, \ldots$ in the complex plane and connecting successive terms with straight line segments forms a polygonal path. The sequence has bounded variation precisely when the ==total length of this polygonal path is finite==:
>
> $$\text{total length of polygon} = \sum_{n=1}^{\infty} |a_{n+1} - a_n| < \infty.$$

## Convergence

> [!tip] Convergence
> Sequences of bounded variation ==converge==. However, the converse is not true: not every convergent sequence has bounded variation.

## See Also

- [[abel-summation-by-parts|Abel Summation by Parts]]
- [[convergent-sequences|Convergent Sequences]]
- [[cauchy-sequences|Cauchy Sequences]]
