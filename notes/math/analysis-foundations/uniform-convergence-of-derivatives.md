---
aliases: [Uniform Convergence of Derivatives, Differentiation Under Uniform Limits]
tags: [real-analysis, uniform-convergence, differentiation, limit-interchange]
date: 2026-02-22
---

# Uniform Convergence of Derivatives

> [!abstract] Theorem
> Suppose $\{f_n\}$ is a sequence of differentiable functions on $[a,b]$ such that:
> 1. $\{f_n(x_0)\}$ converges for some $x_0 \in [a,b]$, and
> 2. $\{f_n'\}$ converges **uniformly** on $[a,b]$.
>
> Then $\{f_n\}$ converges uniformly to a differentiable function $f$, and
>
> $$f'(x) = \lim_{n \to \infty} f_n'(x)$$

^derivative-interchange

## Why This Is Non-Trivial

Uniform convergence of functions preserves **continuity** but not **differentiability**. The [[nowhere-differentiable-function|Weierstrass function]] is a dramatic example: it is a uniform limit of smooth (differentiable) partial sums, yet it is nowhere differentiable.

The key issue is that differentiation involves interchanging two limits:

$$\left(\lim_{n \to \infty} f_n\right)' = \lim_{n \to \infty} f_n'$$

The left side requires a difference quotient limit, so we are really asking whether

$$\lim_{h \to 0} \lim_{n \to \infty} \frac{f_n(x+h) - f_n(x)}{h} = \lim_{n \to \infty} \lim_{h \to 0} \frac{f_n(x+h) - f_n(x)}{h}$$

and interchanging two limits requires justification.

## Proof Idea

The proof routes through **integration**, which commutes with uniform limits easily:

1. By the Fundamental Theorem of Calculus, write
$$f_n(x) - f_n(x_0) = \int_{x_0}^{x} f_n'(t) \, dt$$

2. Since $f_n' \to g$ uniformly, the [[uniform-convergence-and-cauchy-criterion#^limit-integral-exchange|limit–integral exchange]] gives
$$f(x) - f(x_0) = \int_{x_0}^{x} g(t) \, dt$$

3. Since $g$ is continuous (uniform limit of continuous functions), the Fundamental Theorem of Calculus gives $f'(x) = g(x) = \lim f_n'(x)$.

> [!tip] The logical chain
> **Continuity** (preserved by uniform limits) $\to$ **Integration** (commutes with uniform limits) $\to$ **Differentiation** (follows via FTC).
>
> Differentiation is the hardest operation to pass through a limit, and the proof reduces it to the easier cases.

## The Role of the Anchor Point

The hypothesis that $f_n(x_0)$ converges at a single point is essential. Without it, $f_n$ could differ by divergent constants — the derivatives would still converge uniformly, but $f_n$ themselves would not converge anywhere. The anchor point $x_0$ pins down the constants of integration.

## See Also
- [[nowhere-differentiable-function|Weierstrass Function]] — shows what goes wrong without uniform convergence of derivatives
- [[uniform-convergence-and-cauchy-criterion|Uniform Convergence and Cauchy Criterion]] — the parent framework
- [[power-series|Power Series]] — term-by-term differentiation justified by this theorem
