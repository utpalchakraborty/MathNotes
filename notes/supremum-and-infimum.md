---
aliases: [Supremum and Infimum, Least Upper Bound, Greatest Lower Bound]
tags: [real-analysis, foundations]
source: supremum-and-infimum.jpeg, density-and-continuum-hypothesis.jpeg
date: 2025-07-04
---

# Supremum and Infimum

## Motivation

> [!question] Why do we need the reals?
> The whole point of analysis — integration, differentiation, limits, etc. — cannot be done unless we first define the numbers we work with.

We start with the rationals $\mathbb{Q}$. But they have gaps: for example, $\sqrt{2}$ is not a rational number. To fill these gaps, we need the concept of a ==least upper bound==.

## Upper Bounds and Supremum

> [!abstract] Definition (Upper Bound)
> Let $S$ be a subset of an ordered set. An element $\alpha$ is an **upper bound** of $S$ if $x \leq \alpha$ for every $x \in S$.

^upper-bound-definition

> [!abstract] Definition (Supremum)
> The **supremum** (least upper bound) of $S$, written $\alpha = \sup S$, is the element satisfying:
>
> 1. $x \leq \alpha$ for all $x \in S$ (i.e., $\alpha$ is an upper bound of $S$), and
> 2. If $\gamma < \alpha$, then $\gamma$ is not an upper bound of $S$ (i.e., $\alpha$ is the *least* such bound).

^supremum-definition

## Infimum

> [!abstract] Definition (Infimum)
> The **infimum** (greatest lower bound) $\beta = \inf S$ is defined dually:
>
> 1. $x \geq \beta$ for all $x \in S$ (i.e., $\beta$ is a lower bound of $S$), and
> 2. If $\gamma > \beta$, then $\gamma$ is not a lower bound of $S$.

^infimum-definition

## Density of $\mathbb{Q}$ and $\mathbb{R} \setminus \mathbb{Q}$

Between any two numbers $a < b$ (where $a$ and $b$ can be either rational or irrational), one can find:

- A rational number $c$ with $a < c < b$, and
- An irrational number $d$ with $a < d < b$.

> [!tip] Key insight
> Both the rationals and the irrationals are ==dense== in $\mathbb{R}$.

## Cardinality and the Continuum Hypothesis

The chain of number systems is:

$$\mathbb{N} \subset \cdots \subset \mathbb{R}.$$

Is there a set whose cardinality is strictly between $|\mathbb{N}|$ and $|\mathbb{R}|$? This is the **Continuum Hypothesis**, which is ==independent of ZFC== — it can be neither proved nor disproved from the standard axioms of set theory.

## See Also
- [[field-axioms|Field Axioms]]
