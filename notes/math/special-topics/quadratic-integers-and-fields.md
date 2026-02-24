---
aliases: [Quadratic Integers and Fields, Quadratic Integer Ring, Quadratic Field Extension]
tags: [number-theory, algebra]
source: sources/2026-02-24/quadratic-integers-and-continued-fractions-1.jpeg
date: 2026-02-24
---

# Quadratic Integers and Fields

## The Ring $\mathbb{Z}[\sqrt{d}]$

> [!definition] Ring of Quadratic Integers
> For a squarefree integer $d$, define
>
> $$
> \mathbb{Z}[\sqrt{d}] = \{ a + b\sqrt{d} \mid a, b \in \mathbb{Z} \}.
> $$

$\mathbb{Z}[\sqrt{d}]$ is a ==commutative ring== under the usual addition and multiplication inherited from $\mathbb{R}$ (or $\mathbb{C}$ if $d < 0$).

## The Field $\mathbb{Q}[\sqrt{d}]$

> [!definition] Quadratic Field Extension
> $$
> \mathbb{Q}[\sqrt{d}] = \{ p + q\sqrt{d} \mid p, q \in \mathbb{Q} \}.
> $$

$\mathbb{Q}[\sqrt{d}]$ is a ==field== — every nonzero element has a multiplicative inverse, obtained using the conjugate.

## Conjugation

> [!definition] Quadratic Conjugate
> For $\xi = a + b\sqrt{d}$, the **conjugate** is
>
> $$
> \hat{\xi} = a - b\sqrt{d}.
> $$

> [!tip] Conjugation Preserves Algebraic Properties
> Conjugation is a ring homomorphism — it preserves addition and multiplication:
>
> $$
> \widehat{\xi + \eta} = \hat{\xi} + \hat{\eta}, \qquad \widehat{\xi \cdot \eta} = \hat{\xi} \cdot \hat{\eta}.
> $$

## See Also

- [[periodic-continued-fractions|Periodic Continued Fractions]] — continued fraction expansion of $\sqrt{d}$
- [[algebraic-completeness|Algebraic Completeness]]
- [[infinite-continued-fractions|Infinite Continued Fractions]]
