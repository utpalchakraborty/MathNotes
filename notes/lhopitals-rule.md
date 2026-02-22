---
aliases: [L'Hôpital's Rule, L'Hospital's Rule]
tags: [real-analysis, differentiation, limits]
source: sources/2026-02-19/compact-continuity-lhopital-taylor.jpeg
date: 2026-02-19
---

# L'Hôpital's Rule

## Statement

> [!abstract] Theorem (L'Hôpital's Rule)
> If $f(x) \to 0$ and $g(x) \to 0$ as $x \to a$, or if $g(x) \to \infty$ as $x \to a$, then
>
> $$\frac{f'(x)}{g'(x)} \to A \text{ as } x \to a \implies \frac{f(x)}{g(x)} \to A.$$

^lhopitals-rule

> [!info]- Full Hypotheses
> The full hypotheses also require that $f$ and $g$ are differentiable near $a$ (except possibly at $a$ itself) and that $g'(x) \neq 0$ near $a$. The limit $A$ may be finite, $+\infty$, or $-\infty$.

The rule applies to both the $0/0$ and $\infty/\infty$ indeterminate forms. The key insight is that ==the ratio of derivatives captures the relative rates of change==, which determines the limit of the ratio.

## See Also
- [[taylor-polynomials|Taylor Polynomials]] — local polynomial approximation via derivatives
- [[continuous-functions|Continuous Functions]]
- [[differentiation-in-higher-dimensions|Differentiation in Higher Dimensions]]
