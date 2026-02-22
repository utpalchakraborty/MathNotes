---
aliases: [Uniform Convergence and Cauchy Criterion, Uniform Convergence and the Cauchy Criterion]
tags: [real-analysis, uniform-convergence, cauchy-criterion, limits, continuity, compactness, dini-theorem, integration, differentiation]
source: [sources/2026-02-16/1.jpeg, sources/2026-02-16/2.jpeg, sources/2026-02-16/3.jpeg]
pages: [1, 2, 3]
date: 2026-02-16
---

# Uniform Convergence and the Cauchy Criterion

> [!tip] Key Idea
> Uniform convergence is the condition that makes "naive" limit operations safe — exchanging limits, passing limits through integrals, and passing limits through derivatives. Without it, pathological results arise. On compact spaces, Dini's theorem shows that ==pointwise convergence is automatically uniform== when combined with continuity and monotonicity — so compactness + continuity + monotonicity suffices to stay in the safe regime.

## Exchanging Limits

> [!warning] Limits do not commute in general
> You cannot exchange limits arbitrarily.
>
> $$\lim_{m \to \infty} \lim_{n \to \infty} \left(\cos(m! \pi x)\right)^{2n} = \begin{cases} 1 & x \text{ rational} \\ 0 & x \text{ irrational} \end{cases}$$

## Uniform Convergence and the Cauchy Criteria

> [!abstract] Cauchy Criterion for Uniform Convergence
> $\{f_n\} \to f$ uniformly if and only if $|f_n(x) - f_m(x)| < \epsilon$ for some $N$ with $m, n \geq N$. <!-- clarification: handwriting shows N ≥ m, N ≥ n but the mathematically correct Cauchy criterion requires m, n ≥ N -->

^cauchy-criterion-uniform

Or equivalently, let

$$M_n = \sup_{x \in E} |f_n(x) - f(x)|$$

If ==$M_n \to 0$ as $n \to \infty$==, then $\{f_n\}$ also converges uniformly to $f$.

## Interchanging Limits Under Uniform Convergence

> [!abstract] Theorem (Limit Interchange)
> If $f_n \to f$ converges uniformly and each $f_n$ is continuous, then ==$f$ is continuous==.

^limit-interchange-theorem

Under uniform convergence, limits can be interchanged.

## Convergence on Compact Spaces (Dini's Theorem)

On compact spaces it is nicer.

> [!abstract] Theorem (Dini's Theorem)
> Let $K$ be compact. Suppose each $f_n$ is continuous on $K$, $f_n$ converges pointwise to a continuous function $f$, and <!-- clarification: continuity of f_n and f required by Dini's theorem but omitted in original notes -->
>
> $$f_n(x) \geq f_{n+1}(x) \quad \text{for all } x \in K \text{ and all } n$$
>
> Then ==$f_n \to f$ uniformly==.

^dinis-theorem

## Exchanging Limit and Integral

> [!abstract] Theorem (Limit–Integral Exchange)
> Under uniform convergence, the limit and integral can be exchanged:
>
> $$\int_a^b f \, d\alpha = \lim_{n \to \infty} \int_a^b f_n \, d\alpha$$

^limit-integral-exchange

## Uniform Convergence of Derivatives

> [!abstract] Theorem (Uniform Convergence of Derivatives)
> If $f'_n(x)$ converges uniformly and $\{f_n(x_0)\}$ converges at some point $x_0$, then $f_n(x) \to f(x)$ uniformly. <!-- clarification: the full theorem also concludes that f is differentiable and f'(x) = lim f'_n(x), omitted in original notes --> Moreover, $f$ is differentiable and
>
> $$f'(x) = \lim_{n \to \infty} f'_n(x)$$

^uniform-convergence-derivatives

> [!tip] Anchor point intuition
> You have the ==anchor point== and then the derivatives force the rest.

## See Also
- [[cauchy-sequences|Cauchy Sequences]]
- [[continuous-functions|Continuity]]
- [[compactness|Compact Spaces]]
- [[riemann-stieltjes-integral|Riemann–Stieltjes Integral]]
- Pointwise Convergence
- Dini's Theorem
