---
aliases: [Abel's Test for Convergence, Abel's Test]
tags: [real-analysis, series, convergence-tests]
source: sources/2026-02-21/abels-test-limsup-liminf.jpeg
date: 2026-02-21
---

# Abel's Test for Convergence

## Statement

> [!abstract] Theorem (Abel's Test)
> Let $\sum a_n$ be a convergent series, and let $\{b_n\}$ be a sequence of **[[bounded-variation-sequences|bounded variation]]**. Then $\sum a_n b_n$ converges.

^abels-test

> [!warning] No requirement that $b_n \to 0$
> $\{b_n\}$ does **not** need to converge to $0$ — only bounded variation is required.

## Comparison with Dirichlet's Test

Abel's test and [[dirichlets-convergence-test|Dirichlet's test]] are companion results that handle products $\sum a_n b_n$ under different hypotheses:

| Condition | Dirichlet's Test | Abel's Test |
|-----------|-----------------|-------------|
| $\{a_n\}$ | Partial sums $\sum a_n$ bounded | $\sum a_n$ converges |
| $\{b_n\}$ | Bounded variation, $b_n \to 0$ | Bounded variation |

> [!tip] Key distinction
> Dirichlet's test asks less of $\{a_n\}$ (only bounded partial sums) but more of $\{b_n\}$ (must tend to $0$). Abel's test asks more of $\{a_n\}$ (actual convergence) but ==less of $\{b_n\}$ (no requirement that $b_n \to 0$)==.

## See Also

- [[dirichlets-convergence-test|Dirichlet's Convergence Test]] — the companion oscillation-control test
- [[bounded-variation-sequences|Bounded Variation Sequences]]
- [[abel-summation-by-parts|Abel Summation by Parts]] — the discrete integration-by-parts identity (a different result)
- [[series-convergence-tests|Series Convergence Tests]]
