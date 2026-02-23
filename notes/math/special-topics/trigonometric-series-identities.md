---
aliases: [Trigonometric Series Identities]
tags: [real-analysis, series, trigonometry, fourier-series, logarithm]
source:
  - sources/2026-02-22/trigonometric-log-series.jpeg
date: 2026-02-22
---

# Trigonometric Series Identities

## Expanding $-\log(1 - e^{ix})$

Setting $z = -e^{ix}$ in the [[generalized-binomial-series|logarithmic series]] $\log(1+z) = \sum \frac{(-1)^{n-1}}{n}z^n$ gives:

$$\sum_{n=1}^{\infty} \frac{e^{inx}}{n} = -\log(1 - e^{ix})$$

Separating real and imaginary parts via [[exponential-logarithm-and-euler-constant|Euler's formula]] $e^{inx} = \cos(nx) + i\sin(nx)$:

$$\sum_{n=1}^{\infty} \frac{\cos nx}{n} + i\sum_{n=1}^{\infty} \frac{\sin nx}{n} = -\log(1 - e^{ix})$$

## Cosine Series

> [!theorem] Cosine Series
> For $0 < x < 2\pi$:
>
> $$\sum_{n=1}^{\infty} \frac{\cos nx}{n} = -\log\!\left(2\sin\frac{x}{2}\right)$$

This is the ==real part== of $-\log(1 - e^{ix})$.

%%clarification: To see this, write $1 - e^{ix} = -e^{ix/2}(e^{ix/2} - e^{-ix/2}) = -e^{ix/2} \cdot 2i\sin(x/2)$. Taking $-\log$ of the modulus gives $-\log|2\sin(x/2)|$, which equals $-\log(2\sin(x/2))$ for $0 < x < 2\pi$ where $\sin(x/2) > 0$.%%

## Sine Series

> [!theorem] Sine Series
> For $0 < x < 2\pi$:
>
> $$\sum_{n=1}^{\infty} \frac{\sin nx}{n} = \frac{\pi - x}{2}$$

This is the ==imaginary part== of $-\log(1 - e^{ix})$.

%%clarification: From $1 - e^{ix} = -e^{ix/2}\cdot 2i\sin(x/2)$, the argument of $-(1 - e^{ix})$ contributes $-(\pi/2 + x/2)$ shifted by $\pi$, yielding $(\pi - x)/2$ as the imaginary part.%%

## Connection to Fourier Series

Both identities can also be derived as [[fourier-series|Fourier series]] expansions:

- The sine series $\sum \frac{\sin nx}{n} = \frac{\pi - x}{2}$ is the Fourier sine series of the sawtooth function on $(0, 2\pi)$.
- The cosine series $\sum \frac{\cos nx}{n} = -\log(2\sin\frac{x}{2})$ is the Fourier cosine series of $-\log(2\sin\frac{x}{2})$ on $(0, 2\pi)$.

%%clarification: The Fourier approach computes the coefficients directly by integration and does not require the logarithmic series or complex exponential manipulation.%%

## See Also

- [[generalized-binomial-series|Generalized Binomial Series]]
- [[exponential-logarithm-and-euler-constant|Exponential, Logarithm, and Euler's Constant]]
- [[fourier-series|Fourier Series]]
- [[power-series|Power Series]]
