---
aliases: [Hyperbolic Functions]
tags: [real-analysis, hyperbolic-functions, trigonometry, series]
source:
  - sources/2026-02-21/complex-trig-and-euler-formula.jpeg
  - sources/2026-02-21/hyperbolic-functions-and-cos-properties.jpeg
date: 2026-02-21
---

# Hyperbolic Functions

## Definition

> [!abstract] Definition
> The **hyperbolic cosine** and **hyperbolic sine** are defined for $z \in \mathbb{C}$ by:
>
> $$\cosh z = \frac{e^z + e^{-z}}{2}, \qquad \sinh z = \frac{e^z - e^{-z}}{2}$$

^hyperbolic-functions-def

## Relation to Trigonometric Functions

The hyperbolic functions are directly connected to the ordinary trigonometric functions via imaginary arguments:

$$\cosh z = \cos(iz), \qquad \sinh z = -i \sin(iz)$$

<!-- clarification: These follow from substituting iz into the definitions of cos and sin from the complex exponential: cos(iz) = (e^{i(iz)} + e^{-i(iz)})/2 = (e^{-z} + e^z)/2 = cosh z, and similarly for sinh. -->

From these relations, we can derive series expansions for $\cosh$ and $\sinh$ just as we can for $\cos$ and $\sin$.

## The Unifying Viewpoint

> [!tip] All four functions are really just $e^z$ in disguise.

| Function | In terms of $e^z$ |
|----------|-------------------|
| $\cosh z$ | $\frac{e^z + e^{-z}}{2}$ |
| $\sinh z$ | $\frac{e^z - e^{-z}}{2}$ |
| $\cos z$ | $\frac{e^{iz} + e^{-iz}}{2}$ |
| $\sin z$ | $\frac{e^{iz} - e^{-iz}}{2i}$ |

The only difference is whether the argument is real ($z$) or rotated to the imaginary axis ($iz$). ==All trigonometric and hyperbolic identities, series expansions, and differential equations are consequences of the single identity $E(z_1) \cdot E(z_2) = E(z_1 + z_2)$.==

The chain extends further. Since $e^x$ is continuous and strictly monotone, it has an inverse — the [[exponential-logarithm-and-euler-constant|logarithm]] $\log y = \int_1^y \frac{dt}{t}$. Once we have $\exp$ and $\log$, general powers follow:

$$a^z = e^{z \log a}, \qquad a > 0,\; z \in \mathbb{C}$$

In particular, rational powers $a^{p/q}$ (roots and integer powers) are special cases. ==The entire edifice — trigonometric functions, hyperbolic functions, logarithms, roots, and arbitrary powers — derives from the single power series $E(z) = \sum \frac{z^n}{n!}$.==

## Real Trigonometric Functions

In all of the above, we can take $z \in \mathbb{R}$, and the usual real formulae for $\sin$ and $\cos$ appear. Using the complex exponential definitions:

$$\cos z = \frac{e^{iz} + e^{-iz}}{2}, \qquad \sin z = \frac{e^{iz} - e^{-iz}}{2i}$$

and [[exponential-logarithm-and-euler-constant|Euler's formula]] $e^{iz} = \cos z + i \sin z$, one can prove all standard trigonometric identities and derive the power series expansions for $\sin$ and $\cos$.

## Properties of Cosine

The following properties can all be established from the series definition:

1. **Continuity**: $\cos$ is continuous on $\mathbb{R}$.
2. **$\cos 0 = 1$**.
3. **Monotonicity**: $\cos$ is monotone (decreasing) on $[0, 2]$.
4. **$\cos 2 < 0$**.

Since $\cos 0 = 1 > 0$ and $\cos 2 < 0$, by the [[continuous-functions|Intermediate Value Theorem]] there exists a number $x \in (0, 2)$ at which $\cos x = 0$.

> [!info]- Remark
> This number is $\pi/2$. This gives a ==purely analytic definition of $\pi$== without any geometric arguments — we define $\pi/2$ as the smallest positive zero of cosine.

<!-- clarification: This number is π/2. This gives a purely analytic definition of π without any geometric arguments — we define π/2 as the smallest positive zero of cosine. -->

## See Also

- [[exponential-logarithm-and-euler-constant|Exponential Logarithm and Euler Constant]]
- [[power-series|Power Series]]
- [[continuous-functions|Continuous Functions]]
- [[eulers-product-formula-and-wallis|Euler's Product Formula and Wallis's Formula]]
