---
aliases: [Dominated Convergence Theorem, DCT, Lebesgue dominated convergence theorem]
tags: [measure-theory, real-analysis, convergence]
source: dominated-convergence-theorem.jpeg
date: 2026-02-17
---

# Dominated Convergence Theorem

The requirement of monotonicity in the [[lebesgue-integration|Monotone Convergence Theorem]] can be removed — at the cost of requiring an integrable dominating function.

## Statement

> [!abstract] Theorem (Dominated Convergence)
> If $f_n$ is measurable and $f_n \to f$ pointwise almost everywhere, and there exists $g \in \mathscr{L}^1(\mu)$ such that
>
> $$|f_n| \leq g \quad \text{for all } n,$$
>
> then
>
> $$\lim_{n \to \infty} \int_E f_n \, d\mu = \int_E f \, d\mu.$$

^dominated-convergence-theorem

## Key Points

- **Convergence**: Only ==pointwise convergence almost everywhere== is needed — not uniform convergence, not monotone convergence.
- **The dominator**: The function $g$ must be integrable ($g \in \mathscr{L}^1$). This is the price for dropping monotonicity — we need some control over the "size" of the $f_n$.

> [!tip] Why It Works
> The dominator $g$ prevents the mass of $f_n$ from "escaping to infinity." Without it, the $f_n$ could concentrate their integrals on shrinking sets, causing the limit of the integrals to differ from the integral of the limit.

## Comparison with the Monotone Convergence Theorem

| | MCT | DCT |
|---|---|---|
| **Monotonicity** | Required ($f_1 \leq f_2 \leq \cdots$) | Not required |
| **Sign** | Non-negative functions | Any sign allowed |
| **Dominator** | Not required (monotonicity controls growth) | Required ($\|f_n\| \leq g \in \mathscr{L}^1$) |
| **Convergence** | Pointwise | Pointwise a.e. |

## See Also
- [[lebesgue-integration|Lebesgue Integration]]
- [[measurable-functions|Measurable Functions]]
- [[riesz-fischer-theorem|Riesz–Fischer Theorem]]
