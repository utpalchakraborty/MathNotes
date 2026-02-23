---
aliases: [Countability, Countable Sets, Countable and Uncountable Sets]
tags: [real-analysis, foundations, set-theory]
source: cauchy-schwarz-and-countability.jpeg
date: 2025-07-06
---

# Countability

## Countable Sets

> [!abstract] Definition (Countable)
> A set is **countable** if it can be put in one-to-one correspondence with a subset of $\mathbb{N}$.

^countable-definition

### Key Facts

- Every infinite subset of a countable set is countable.
- No uncountable set can be a subset of a countable set.
- ==Countable sets are the smallest infinite sets== — there is no infinite cardinality smaller than $|\mathbb{N}|$.
- A countable union of countable sets is countable, because we can enumerate them (e.g., via a diagonal argument). <!-- clarification: the scan says "infinite union"; in standard usage this means countable union, which requires the axiom of countable choice -->

> [!warning] Closure under unions
> The countable union result requires the ==axiom of countable choice==. Without it, the enumeration argument does not go through.

## Examples

> [!example] Countable sets
> - $\mathbb{Q}$ is countable.
> - The algebraic numbers are countable.

## See Also
- [[field-axioms|Field Axioms]] — $\mathbb{Q}$ as a field
- [[supremum-and-infimum|Supremum and Infimum]] — the continuum hypothesis and cardinality of $\mathbb{R}$
- [[compactness|Compactness]] — the Cantor set is uncountable yet has measure zero
