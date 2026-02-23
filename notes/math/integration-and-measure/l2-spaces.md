---
aliases: [L² Spaces, L2 Spaces, L² space, L2 space]
tags: [measure-theory, real-analysis, functional-analysis]
source: [l2-spaces-1.jpeg, l2-spaces-2.jpeg, l2-spaces-3.jpeg]
date: 2026-02-17
---

# $L^2$ Spaces

## Definition

> [!abstract] Definition ($L^2$ Space)
> $$\mathscr{L}^2(\mu) = \left\{ f : \int_X |f|^2 \, d\mu < +\infty \right\}.$$
>
> The **$L^2$ norm** is
>
> $$\|f\| = \sqrt{\int_X |f|^2 \, d\mu}.$$

^l2-space-def

## Basic Properties

**Product integrability.** If $f, g \in \mathscr{L}^2(\mu)$, then $fg \in \mathscr{L}(\mu)$ — the product is [[lebesgue-integration|Lebesgue integrable]]. This follows from the Cauchy–Schwarz inequality:

$$\int_X |fg| \, d\mu \leq \|f\| \cdot \|g\| < \infty.$$

**Metric structure.** $\mathscr{L}^2(\mu)$ is a metric space with distance

$$d(f, g) = \|f - g\| = \sqrt{\int_X |f - g|^2 \, d\mu}.$$

> [!info]- On Equivalence Classes
> Distance $= 0$ means $f = g$ almost everywhere: the functions may differ, but only on a set of [[lebesgue-measure|measure]] zero. Strictly speaking, $L^2(\mu)$ consists of equivalence classes of functions that agree a.e., making the distance a true metric rather than a pseudometric.

## Density of Continuous Functions

The continuous functions form a ==**dense subset**== of $\mathscr{L}^2[a, b]$.

This means that given any $f \in \mathscr{L}^2[a, b]$, we can find a continuous function $g$ such that the $L^2$ distance between $f$ and $g$ is as small as we like:

$$\|f - g\| = \sqrt{\int_a^b |f - g|^2 \, dx} < \epsilon$$

for any $\epsilon > 0$.

## Completeness

> [!abstract] Theorem ($L^2$ Completeness)
> $\mathscr{L}^2(\mu)$ is a **complete** space: if $\{f_n\}$ is a Cauchy sequence in $\mathscr{L}^2(\mu)$, then it converges to some $f \in \mathscr{L}^2(\mu)$.

^l2-completeness

> [!tip] Why This Matters
> Completeness is what makes $L^2$ a ==**Hilbert space**== (a complete inner product space). The inner product is
>
> $$\langle f, g \rangle = \int_X f \, \overline{g} \, d\mu.$$

This completeness is ultimately guaranteed by the [[lebesgue-integration|Lebesgue integral]] — limits of $L^2$ functions stay in $L^2$, unlike the Riemann setting where Cauchy sequences can escape the space.

## How $L^2$ Compares to Neighboring Spaces

The properties above — inner product, completeness, density of continuous functions — are not shared equally across function spaces. The following table compares $L^2$ against three related spaces on five key structural properties.

| Property | $L^2$ | $L^1$ | $L^\infty$ | $C[a,b]$ |
|----------|:-----:|:-----:|:----------:|:---------:|
| **Inner Product** | ✓ | ✗ | ✗ | ✗ |
| **Complete** | ✓ | ✓ | ✓ | ✗ |
| **$C[a,b]$ Dense** | ✓ | ✓ | ✗ | ✓ |
| **Self-Dual** | ✓ | ✗ | ✗ | ✗ |
| **Fourier Basis** | ✓ | ✗ | ✗ | ✗ |

<!-- TODO: swap to radar-beta chart when Obsidian upgrades to Mermaid v11.4+ -->

> [!info]- Reading the Comparison Table
> - **$L^2$** fills out every axis — it is the only space here that is a Hilbert space (complete + inner product), self-dual ($L^2 \cong (L^2)^*$), and supports a complete orthonormal Fourier basis.
> - **$L^1$** is complete and has dense continuous functions, but lacks a true inner product (its norm does not satisfy the parallelogram law) and is not self-dual ($(L^1)^* = L^\infty$).
> - **$L^\infty$** is complete but not separable — continuous functions are *not* dense, it is not self-dual, and it has no standard inner product.
> - **$C[a,b]$** is dense in the $L^p$ spaces but is itself **incomplete** under any $L^p$ norm — Cauchy sequences of continuous functions can converge to discontinuous limits.

> [!tip] Punchline
> This is why ==$L^2$ occupies a privileged position==: it is the unique $L^p$ space that is also a Hilbert space.

## Complete Orthonormal Sets

> [!abstract] Definition (Complete Orthonormal Set)
> Let $\{\phi_n\}$ be a **complete orthonormal set** in $\mathscr{L}^2(\mu)$. Completeness of the orthonormal set means: if
>
> $$\int_X f \, \overline{\phi_n} \, d\mu = 0 \quad \text{for all } n,$$
>
> then $\|f\| = 0$ (i.e., $f = 0$ a.e.). No nonzero function is orthogonal to every basis element.

^complete-orthonormal-set-def

## Fourier Expansion in $L^2$

If $f \in \mathscr{L}^2(\mu)$ and $\{\phi_n\}$ is a complete orthonormal set, then

$$f \sim \sum_{n=1}^{\infty} c_n \, \phi_n,$$

where $c_n = \langle f, \phi_n \rangle$ are the **Fourier coefficients** (or Fourier components) of $f$ with respect to $\{\phi_n\}$. The convergence is in the $L^2$ norm.

## Parseval's Identity and the Riesz–Fischer Theorem

For any $f \in \mathscr{L}^2(\mu)$:

$$\int_X |f|^2 \, d\mu = \sum_{n=1}^{\infty} |c_n|^2.$$

This is [[parsevals-theorem|Parseval's identity]], extended to the full $L^2$ setting by the [[riesz-fischer-theorem|Riesz–Fischer Theorem]]. It establishes a ==**1:1 correspondence**== between the coefficients $\{c_n\}$ and functions $f \in \mathscr{L}^2(\mu)$: the map $f \mapsto (c_n)$ is an isometric isomorphism $L^2(\mu) \cong \ell^2$.

> [!tip] Coordinates in a Hilbert Space
> The Fourier coefficients $c_n$ can be thought of as **coordinates in a Hilbert space** — just as a vector in $\mathbb{R}^n$ is determined by its components along an orthonormal basis, a function in $L^2$ is determined by its coefficients along a complete orthonormal system.

## See Also
- [[lebesgue-integration|Lebesgue Integration]]
- [[lebesgue-measure|Lebesgue Measure]]
- [[fourier-series|Fourier Series]]
- [[parsevals-theorem|Parseval's Theorem]]
- [[riesz-fischer-theorem|Riesz–Fischer Theorem]]
- [[dominated-convergence-theorem|Dominated Convergence Theorem]]
- [[measurable-functions|Measurable Functions]]
