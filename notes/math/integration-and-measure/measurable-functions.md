---
aliases: [Measurable Functions, Measurable functions]
tags: [measure-theory, real-analysis]
source: measurable-functions.jpeg
date: 2026-02-17
---

# Measurable Functions

Given a **measure space** $(X, \mathfrak{M}, \mu)$ --- a set $X$ equipped with a $\sigma$-ring $\mathfrak{M}$ of measurable subsets and a countably additive measure $\mu$ --- we define measurable functions on $X$.

## Definition

> [!abstract] Definition (Measurable Function)
> A function $f \colon X \to \mathbb{R}$ is **measurable** if for every $a \in \mathbb{R}$, the set
>
> $$\{x \in X \mid f(x) > a\}$$
>
> is measurable (i.e., belongs to $\mathfrak{M}$).

^measurable-function-def

> [!info]- Equivalent Formulations
> The condition $f(x) > a$ can equivalently be replaced by any of $\geq$, $<$, or $\leq$ without changing the class of measurable functions.

## Properties

- If $f$ is measurable, then $|f|$ is measurable.
- If $f_n \to f$ pointwise and each $f_n$ is measurable, then $f$ is measurable.
- In general, ==all ordinary operations of analysis== (sums, products, limits, suprema, infima, etc.) applied to measurable functions yield measurable functions.

## Composition with Continuous Functions

> [!warning] Composition Caveat
> If $f$ is measurable and $g$ is continuous, the composition $h(x) = f(g(x))$ is **not** necessarily measurable.

<!-- Note: The reverse composition g ∘ f (continuous after measurable) IS measurable, since the preimage of (a, ∞) under g is open, hence Borel, and the preimage of a Borel set under a measurable function is measurable. -->

## See Also
- [[lebesgue-measure|Lebesgue Measure]]
- [[lebesgue-integration|Lebesgue Integration]]
