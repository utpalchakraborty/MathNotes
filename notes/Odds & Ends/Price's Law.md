---
aliases: [Price's Law]
tags: [organizational-theory, power-law]
source: sources/2026-02-22/prices-law-and-persian-deliberation.jpeg
date: 2026-02-22
---

# Price's Law

> [!abstract] Statement
> In an organization, the square root of the total number of people does 50% of the work.

Named after ==Derek J. de Solla Price==, who originally observed this pattern in scientific publishing: the square root of all contributors to a field produce half of all publications. The principle has since been generalized to describe productivity distributions in organizations more broadly.

## Example

In a company of 100 employees, roughly 10 people ($\sqrt{100}$) account for half the total output. As organizations grow, this becomes increasingly stark — in a company of 10,000, just 100 people carry half the load.

## Claude's Deliberation

> [!info] Attribution
> The following reflections are from Claude (AI), not the note author.

---

### The Kernel of Truth

There is something real here, but Price's Law as commonly stated is a blunt instrument swung at a nuanced phenomenon.

The underlying observation — that productivity in creative and intellectual work is ==wildly unequal== — is one of the most replicated findings in organizational research. Lotka's Law (1926) preceded Price and found the same thing in scientific authorship. Pareto distributions show up in open-source commits, sales performance, patent filings, bug fixes, and musical output. The general shape — a small minority producing a disproportionate share — is not in serious dispute.

What *is* disputable is the specific claim that $\sqrt{N}$ is the magic number and 50% is the magic share. That's suspiciously clean. And it breaks down at the edges in instructive ways.

### Where the Math Gets Uncomfortable

The square root formulation has a structural problem: it implies that organizations become *catastrophically* more dependent on a shrinking fraction of people as they grow.

| $N$ (people) | $\sqrt{N}$ (productive core) | % of workforce |
|---|---|---|
| 10 | ~3 | 32% |
| 100 | 10 | 10% |
| 10,000 | 100 | 1% |
| 1,000,000 | 1,000 | 0.1% |

> [!warning] Extraordinary Claims
> At 10 people, the law says roughly a third carry half the load — barely noteworthy. At a million people, it says ==one-tenth of one percent== does half the work. That's an extraordinary claim, and it should require extraordinary evidence.

The empirical reality is probably somewhere between the boring null hypothesis (output is roughly proportional to headcount, with variance) and Price's extreme claim. The true distribution likely follows something Pareto-like, but the exponent varies enormously by domain, incentive structure, and how you measure "output."

### The Measurement Problem

> [!question] What counts as work?
> Price's Law inherits a deep question it never answers.

In scientific publishing, you can count papers. But counting papers is already a proxy — it confuses quantity with contribution. One foundational paper can matter more than a thousand incremental ones. If you weight by citation impact, the distribution gets even *more* skewed than Price predicted, not less. If you weight by actual scientific importance (whatever that means), it may skew differently still.

In a company, "does 50% of the work" is almost meaningless without defining the unit. Revenue generated? Lines of code? Decisions made? Problems prevented? The person who quietly keeps the database from falling over on weekends may not show up in any productivity metric, but remove them and the whole system collapses. Price's Law ==measures the visible and credits the measurable==, which systematically undervalues maintenance, coordination, and institutional knowledge.

### Why People Love It Anyway

Price's Law has the same appeal as most power-law claims — ==it flatters the audience==. If you're hearing about it, you probably identify with the productive $\sqrt{N}$, not the remaining majority. It validates the felt experience of high performers ("I *knew* I was carrying this team") and gives managers an intellectual framework for what they already wanted to believe: that most of their workforce is dead weight.

> [!danger] Where It Becomes Dangerous
> It's one step from "a small minority does most of the work" to "therefore, we should only invest in that minority" or "therefore, the rest can be cut." But this ignores the ecology of an organization. The productive minority often depends on infrastructure, support, and institutional stability provided by the broader group. You cannot extract the $\sqrt{N}$ into their own company and expect the same output — they were productive *in context*, not in isolation.

### The Real Insight, Carefully Stated

> [!tip] A More Honest Formulation
> In any domain where output depends on skill, motivation, and accumulated advantage, the distribution of individual contributions will be ==heavy-tailed==. A relatively small group will account for a disproportionately large share of measurable output. This skew increases with the size of the group and the degree to which the domain rewards compounding effort.

That's less catchy than "$\sqrt{N}$ does 50% of the work." But it's closer to what the data actually supports, and it doesn't pretend to know the exponent.

### Just Another Power Law

Zoom out, and Price's Law stops looking like a discovery about organizations and starts looking like a specific parameterization of a universal pattern. The same heavy-tailed distribution appears everywhere:

- **City populations** — Zipf's Law
- **Word frequencies** — Zipf again
- **Wealth distribution** — Pareto
- **Earthquake magnitudes** — Gutenberg-Richter
- **Website traffic**
- **Species abundance** — ecological distributions
- **Network connectivity** — Barabási

> [!note] The Mechanism
> Power laws emerge naturally from any process with **preferential attachment** or **multiplicative advantage**. The scientist who publishes early gets citations, which get them grants, which get them students, which get them more publications. The productive employee gets the interesting projects, which build skills, which make them more productive. ==Success compounds.==

So Price didn't really discover something specific about organizations. He observed a general statistical regularity — that multiplicative dynamics produce heavy tails — and gave it a domain-specific name. The "law" has roughly the same explanatory depth as saying "things that compound end up unevenly distributed." True, but not surprising once you see the mechanism.

The interesting question was never *whether* the distribution is heavy-tailed — it almost always is — but what the **exponent** is in a given context and what **structural factors** make it steeper or flatter. That's where actual actionable insight lives, and Price's Law says nothing about it.

### The Uncomfortable Flip Side

> [!warning] Fragility Warning
> There's a version of Price's Law that nobody talks about because it's inconvenient: if a small minority produces most of the output, then *the system is fragile*. The departure of a handful of people could collapse half the productive capacity of the organization. Rather than celebrating the concentration, a thoughtful manager should be ==alarmed== by it. Price's Law, if true, is not a fun fact about human performance — it's a ==risk assessment==.

---

## See Also
- [[galls-law|Gall's Law]]
