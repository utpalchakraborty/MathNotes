---
aliases: [Infinite Continued Fractions, Continued Fractions]
tags: [real-analysis, number-theory, sequences]
source: sources/2026-02-23/benoit-cloitre-sequences.jpeg, sources/2026-02-23/continued-fractions-intro.jpeg
date: 2026-02-23
---

# Infinite Continued Fractions

## Finite Continued Fractions and Rationals

Every rational number can be written as a finite continued fraction of even or odd length. If somewhere in the chain you get zero in the numerator, everything after that is $0$, so the continued fraction sequence is finite.

## Quadratic Equations and Continued Fractions

Every quadratic equation leads to a continued fraction. Given

$$
x^2 + ax - b = 0,
$$

we can write $x(x + a) = b$, so

$$
x = \frac{b}{a + x}.
$$

Substituting recursively:

$$
x = \cfrac{b}{a + \cfrac{b}{a + \cfrac{b}{a + \cdots}}}.
$$

> [!example] $\sqrt{2}$ as a Continued Fraction
> Taking $x^2 - 2 = 0$ (i.e., $a = 0$, $b = 2$), we need $x^2 = 2$. Rewriting as $x = 1 + (x - 1) = 1 + \frac{x^2 - 1}{x + 1} = 1 + \frac{1}{x + 1}$ %%clarification: derived from the identity $\sqrt{2} = 1 + (\sqrt{2} - 1)$ and rationalizing%%:
>
> $$
> \sqrt{2} = 1 + \cfrac{1}{2 + \cfrac{1}{2 + \cfrac{1}{2 + \cdots}}}.
> $$

> [!example] The Golden Ratio $\phi$
> The golden ratio satisfies $x^2 - x - 1 = 0$, giving $x = 1 + \frac{1}{x}$:
>
> $$
> \phi = 1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1 + \cdots}}}.
> $$

## Benoit Cloitre Sequences

Define two sequences $(a_n)$ and $(b_n)$ by the initial conditions and recurrences:

$$
a_1 = b_1 = 0, \qquad a_2 = b_2 = 1,
$$

$$
a_{n+2} = a_{n+1} + \frac{a_n}{n}, \qquad b_{n+2} = \frac{b_{n+1}}{n} + b_n.
$$

> [!theorem] Limits of Benoit Cloitre Sequences
> The ratios of consecutive terms converge to fundamental constants:
>
> $$
> \lim_{n \to \infty} \frac{n}{a_n} = e, \qquad \lim_{n \to \infty} \frac{n}{b_n^2} = \frac{\pi}{2}.
> $$

## See Also

- [[continued-fraction-convergents|Continued Fraction Convergents]] — Wallis-Euler recurrence, convergent monotonicity, and convergence criteria
- [[euler-continued-fraction-formula|Euler's Continued Fraction Formula]]
- [[exponential-logarithm-and-euler-constant|Exponential, Logarithm, and Euler Constant]]
- [[pi-formulas-from-arctangent|Pi Formulas from Arctangent]]
