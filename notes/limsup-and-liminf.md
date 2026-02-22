---
aliases: [Limsup and Liminf, Limit Superior, Limit Inferior, Limit Supremum, Limit Infimum]
tags: [real-analysis, sequences, limits]
source:
  - sources/2026-02-21/abels-test-limsup-liminf.jpeg
  - sources/2026-02-21/root-test-ratio-test.jpeg
date: 2026-02-21
---

# Limsup and Liminf

## Definitions

> [!abstract] Definition (Limsup and Liminf)
> Given a sequence $\{a_n\}$, define:
>
> $$\limsup_{n \to \infty} a_n = \lim_{n \to \infty} \sup\{a_k \mid k \geq n\},$$
>
> $$\liminf_{n \to \infty} a_n = \lim_{n \to \infty} \inf\{a_k \mid k \geq n\}.$$

^limsup-liminf-def

The sequence $\sup\{a_k \mid k \geq n\}$ is decreasing in $n$ (as we take the supremum over a shrinking set), so its limit always exists in $\mathbb{R} \cup \{-\infty\}$. Similarly, $\inf\{a_k \mid k \geq n\}$ is increasing, so its limit always exists in $\mathbb{R} \cup \{+\infty\}$.

## Existence

> [!tip] Always exist
> For an oscillating sequence, the ordinary limit $\lim a_n$ may not exist. However, ==$\limsup a_n$ and $\liminf a_n$ **always exist**== (possibly as $\pm\infty$) for any bounded or unbounded sequence.

- If $\{a_n\}$ is **bounded**, then both $\limsup a_n$ and $\liminf a_n$ are finite real numbers.
- If $\{a_n\}$ is **unbounded above**, then $\limsup a_n = +\infty$.
- If $\{a_n\}$ is **unbounded below**, then $\liminf a_n = -\infty$.

## Characterization of Limits

> [!abstract] Theorem (Characterization of Limits)
> $\lim_{n \to \infty} a_n$ exists (as a value in $\mathbb{R} \cup \{\pm\infty\}$) if and only if
>
> $$\limsup_{n \to \infty} a_n = \liminf_{n \to \infty} a_n,$$
>
> in which case all three are equal:
>
> $$\lim_{n \to \infty} a_n = \limsup_{n \to \infty} a_n = \liminf_{n \to \infty} a_n.$$

^characterization-of-limits

> [!tip] Key takeaway
> To show a limit exists, it suffices to show the ==limsup and liminf agree==.

## See Also

- [[supremum-and-infimum|Supremum and Infimum]] — the underlying definitions of sup and inf
- [[convergent-sequences|Convergent Sequences]]
- [[series-convergence-tests|Series Convergence Tests]] — the limsup formulations of the root and ratio tests
