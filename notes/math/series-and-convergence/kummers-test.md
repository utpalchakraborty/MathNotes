---
aliases: [Kummer's Test]
tags: [real-analysis, series, convergence, convergence-tests]
source:
  - sources/2026-02-21/root-ratio-kummers-test.jpeg
  - sources/2026-02-21/kummers-intuition-convergence-classes.jpeg
date: 2026-02-21
---

# Kummer's Test

## Statement

> [!abstract] Theorem (Kummer's Test)
> Let $\{a_n\}$ be a sequence of positive terms. The series $\sum a_n$ **converges** if there exists a sequence $\{b_n\}$ of positive numbers such that:
>
> $$\liminf_{n \to \infty} \left( b_n \cdot \frac{a_n}{a_{n+1}} - b_{n+1} \right) > 0$$

^kummers-test

## Intuition

Kummer's test can be thought of as a way to ==amplify the difference between successive terms== and check whether they are going to zero fast enough. The auxiliary sequence $\{b_n\}$ acts as a magnifying lens: by choosing $b_n$ cleverly, one can detect convergence that cruder tests miss.

## Special Cases

With $b_n = 1$ for all $n$, the Kummer condition becomes:

$$\liminf_{n \to \infty} \left( \frac{a_n}{a_{n+1}} - 1 \right) > 0$$

which is precisely the **ratio test**. In this sense, ==the ratio test is the simplest instance of Kummer's test==.

> [!tip] Unifying Framework
> **Most classical convergence tests are Kummer's test with a clever choice of $b_n$**. Different auxiliary sequences recover different tests (e.g., Raabe's test, Bertrand's test), making Kummer's test ==a unifying framework for comparison-based convergence criteria==.

## See Also

- [[series-convergence-tests|Series Convergence Tests]] -- root test, ratio test, and other classical tests
- [[convergence-test-classification|Convergence Test Classification]] -- taxonomy of convergence tests
- [[dirichlets-convergence-test|Dirichlet's Convergence Test]]
- [[abels-test-for-convergence|Abel's Test for Convergence]]
- [[limsup-and-liminf|Limsup and Liminf]]
