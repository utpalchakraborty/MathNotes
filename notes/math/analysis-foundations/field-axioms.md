---
aliases: [Field Axioms, Fields, Ordered Fields]
tags: [real-analysis, foundations, algebra]
source: field-definition.jpeg, field-axiom-consequences.jpeg, existence-of-reals.jpeg
date: 2025-07-04
---

# Field Axioms

## Definition

> [!abstract] Definition (Field)
> A **field** is a set $F$ equipped with two operations $+$ (addition) and $\cdot$ (multiplication) satisfying:
>
> 1. $(F, +)$ is a commutative group with identity $0$.
> 2. $(F \setminus \{0\},\; \cdot\,)$ is a commutative group with identity $1$.
> 3. $0 \neq 1$.
> 4. Multiplication distributes over addition: $x \cdot (y + z) = x \cdot y + x \cdot z$.

^field-definition

## Consequences of the Field Axioms

From the axioms above, one can rigorously prove the following.

### Additive Properties

- **Cancellation law:** $x + y = x + z \implies y = z$.

> [!note]- Proof
> $$y = 0 + y = (-x + x) + y = -x + (x + y) = -x + (x + z) = (-x + x) + z = 0 + z = z. \qquad \square$$

- $x + y = x \implies y = 0$.
- $x + y = 0 \implies y = -x$.
- $-(-x) = x$.

### Multiplicative Properties

Similarly:

- $x \neq 0$ and $xy = xz \implies y = z$.
- $x \neq 0$ and $xy = x \implies y = 1$.
- $x \neq 0$ and $xy = 1 \implies y = 1/x$.
- $x \neq 0 \implies 1/(1/x) = x$.

### Mixed Properties

- $0 \cdot x = 0$ for all $x$.
- $x \neq 0$ and $y \neq 0 \implies xy \neq 0$.
- $(-x)y = -(xy) = x(-y)$.
- $(-x)(-y) = xy$.

## Existence of $\mathbb{R}$

> [!abstract] Theorem (Existence of $\mathbb{R}$)
> There exists a field $\mathbb{R}$ with the **least upper bound property** (every nonempty subset bounded above has a supremum) that contains $\mathbb{Q}$ as a subfield.

^existence-of-reals

> [!info]- Construction Methods
> This can be proven by explicit construction via:
>
> 1. **Dedekind cuts**, or
> 2. **Cauchy sequences**.

## See Also
- [[supremum-and-infimum|Supremum and Infimum]]
