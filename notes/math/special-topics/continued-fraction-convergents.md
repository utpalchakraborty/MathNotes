---
aliases: [Continued Fraction Convergents, Wallis-Euler Recurrence, Convergents of Continued Fractions]
tags: [real-analysis, number-theory, sequences]
source: sources/2026-02-23/wallis-euler-recurrence.jpeg, sources/2026-02-23/continued-fraction-convergents.jpeg, sources/2026-02-23/continued-fraction-convergence.jpeg
date: 2026-02-23
---

# Continued Fraction Convergents

When we have [[infinite-continued-fractions|continued fractions]] with both positive and negative terms, the partial sums may oscillate and can even be undefined (of course, because of denominators becoming $0$).

## Wallis-Euler Recurrence Relations

Consider a generalized continued fraction with partial numerators $b_n$ and partial denominators $a_n$, where $a_n, b_n > 0$ for $n \geq 1$.

> [!definition] Wallis-Euler Recurrence
> Define the ==numerator and denominator sequences== $(p_n)$ and $(q_n)$ by the recurrences:
>
> $$
> p_n = a_n \, p_{n-1} + b_n \, p_{n-2}, \qquad p_{-1} = 1, \quad p_0 = a_0,
> $$
>
> $$
> q_n = a_n \, q_{n-1} + b_n \, q_{n-2}, \qquad q_{-1} = 0, \quad q_0 = 1.
> $$

In particular:

$$
p_1 = a_1 \, p_0 + b_1 \, p_{-1} = a_1 a_0 + b_1,
$$

$$
q_1 = a_1.
$$

The $n$-th **convergent** is then

$$
C_n = \frac{p_n}{q_n},
$$

which equals the continued fraction truncated %%clarification: "sum till $n$ terms" in the original%% at the $n$-th level.

## Convergents as Rational Approximations

> [!theorem] Convergents Equal Truncated Continued Fractions
> If
>
> $$
> C_n = a_0 + \cfrac{b_1}{a_1 + \cfrac{b_2}{a_3 + \cdots + a_n}},
> $$
>
> then $C_n = \dfrac{p_n}{q_n}$, where $p_n$ and $q_n$ satisfy the Wallis-Euler recurrence above.

## Relatively Prime Integers and Diophantine Equations

> [!tip] Application to Diophantine Equations
> If $a \in \mathbb{N}$ and $b \in \mathbb{N}$ are ==relatively prime==, then the linear Diophantine equation
>
> $$
> ax - by = c
> $$
>
> has infinitely many integer solutions.

## Irrationality via Continued Fractions

You can prove a number is irrational by showing its continued fraction representation has infinitely many terms. %%clarification: a rational number always has a finite simple continued fraction, so an infinite simple CF must represent an irrational number%%

## Monotonicity of Convergents

> [!theorem] Even and Odd Convergent Monotonicity
> Let
>
> $$
> a_0 + \cfrac{b_1}{a_1 + \cfrac{b_2}{a_2 + \cdots}}
> $$
>
> be a continued fraction with $a_n, b_n > 0$. Let $j$ be even and $k$ be odd. Then:
>
> $$
> C_0 < C_2 < C_4 < \cdots < C_j < \cdots < C_k < \cdots < C_3 < C_1.
> $$

This means the ==odd convergents approach the limit from above== and the ==even convergents approach from below==. Since both subsequences are monotone and bounded, the limit exists.

Hence the continued fraction converges if and only if

$$
\lim_{n \to \infty} C_{2n+1} = \lim_{n \to \infty} C_{2n},
$$

i.e., the limits of the odd and even convergents agree.

Moreover,

$$
C_{2n} - C_{2n-1} = \frac{-b_1 b_2 \cdots b_{2n}}{q_{2n} \, q_{2n-1}} \to 0 \quad \text{as } n \to \infty.
$$

## Convergence Criterion

> [!theorem] Convergence of Generalized Continued Fractions
> The above monotonicity holds and the continued fraction converges if
>
> $$
> \sum_{n=1}^{\infty} \frac{a_n \, a_{n+1}}{b_n} = \infty.
> $$

> [!tip] Simple Continued Fractions Always Converge
> ==Infinite simple continued fractions== (where all $b_n = 1$) ==always converge==, since the convergence condition reduces to $\sum a_n a_{n+1} = \infty$, which holds whenever $a_n \geq 1$.

## Concept Map

```mermaid
graph TD
    CF["Generalized Continued<br/>Fraction"]
    WE["Wallis-Euler<br/>Recurrence"]
    PN["Numerators p_n"]
    QN["Denominators q_n"]
    CN["Convergents<br/>C_n = p_n / q_n"]
    EVEN["Even Convergents<br/>C_0 < C_2 < C_4 < ···"]
    ODD["Odd Convergents<br/>··· < C_3 < C_1"]
    MONO["Monotonicity +<br/>Boundedness"]
    CONV["Convergence<br/>∑ a_n·a_(n+1)/b_n = ∞"]
    SIMPLE["Simple CF<br/>(all b_n = 1)"]
    IRR["Irrationality<br/>Criterion"]

    CF -->|"defines"| WE
    WE -->|"generates"| PN
    WE -->|"generates"| QN
    PN --> CN
    QN --> CN
    CN -->|"split into"| EVEN
    CN -->|"split into"| ODD
    EVEN --> MONO
    ODD --> MONO
    MONO -->|"converges if"| CONV
    CONV -->|"special case"| SIMPLE
    SIMPLE -->|"infinite ⇒"| IRR
```

## See Also

- [[infinite-continued-fractions|Infinite Continued Fractions]]
- [[euler-continued-fraction-formula|Euler's Continued Fraction Formula]]
- [[convergent-sequences|Convergent Sequences]]
