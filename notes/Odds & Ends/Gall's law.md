---
aliases: [Gall's Law]
tags: [systems-thinking, heuristics, design]
date: 2026-02-17
---

# Gall's Law

> A complex system that works is invariably found to have evolved from a simple system that worked. A complex system designed from scratch never works and cannot be patched up to make it work. You have to start over with a working simple system.

— **John Gall**, *Systemantics: How Systems Really Work and How They Fail* (1975)

## Origin

John Gall was a pediatrician who wrote *Systemantics* as a semi-satirical critique of large systems — bureaucratic, technological, biological. The book was later republished as *The Systems Bible* (2002). Despite its humorous tone, the observations in it have proven remarkably durable. Gall's Law is the most widely cited of them.

## What It Actually Says

The law makes two claims, and the second is the sharper one:

1. **Working complex systems evolved from working simple systems.** This is an empirical observation. Look at any complex system that functions well — the internet, biological organisms, common law, Unix — and you'll find it grew incrementally from something simple that already worked at each stage.

2. **Complex systems designed from scratch don't work.** This is the provocative half. It says you *cannot* engineer a complex system into existence top-down. You can design a simple system, get it working, and then grow it — but you cannot skip to the end state.

The word "invariably" is doing real work here. Gall isn't saying this is a tendency; he's saying he can't find counterexamples.

## Why It Holds

A few reinforcing reasons:

- **You don't understand the problem yet.** Complex systems interact with complex environments. You can't anticipate the real requirements until you have something running and encountering reality. A simple working system is a tool for *discovering* what the complex system actually needs to be.

- **Interfaces are the hard part.** The difficulty of a system lies not in its components but in how they interact. A simple system has few interfaces. Each increment adds interfaces one at a time, and each can be debugged against an already-working whole. A from-scratch complex design introduces all interfaces simultaneously — the combinatorial explosion of failure modes is unmanageable.

- **Working systems accumulate implicit knowledge.** A simple system that works encodes lessons — about edge cases, user behavior, environmental constraints — that no specification document captures. Evolution preserves this knowledge; greenfield rewrites discard it.

- **Selection pressure.** In evolved systems, each intermediate stage had to survive contact with reality. Non-viable paths were pruned early. A top-down design has no such filtering — its first contact with reality is deployment, when the cost of failure is highest.

## Examples

**The Internet.** Started as ARPANET connecting four nodes with a simple packet-switching protocol. TCP/IP, DNS, HTTP, and the web were each layered on top of something that already worked. Nobody designed "the internet" as a spec and then built it.

**Unix.** Ken Thompson wrote the first version in three weeks on a PDP-7, as a simple operating system for one user. It worked. Over decades, it evolved into the foundation of nearly all modern computing infrastructure. Contrast this with Multics, the ambitious system it was a reaction *against*, which largely failed under its own complexity.

**Biological organisms.** Every complex organism evolved from simpler ones through incremental mutation and selection. No complex organism was ever assembled from scratch. This is arguably the deepest example — evolution *is* the process Gall's Law describes.

**Common law.** Legal systems built case-by-case from precedent (common law) tend to be more robust and adaptable than comprehensive legal codes drafted from first principles. The code-based approach keeps requiring amendments and patches; the case-based approach grows organically.

**Failed counterexamples.** Large-scale top-down system designs that struggled or collapsed: the initial healthcare.gov rollout, the FBI's Virtual Case File system ($170M abandoned), and countless enterprise software rewrites.

## Subtleties and Limits

- **Gall's Law is a heuristic, not a theorem.** It has no proof. It is an empirical generalization from observing systems. Heuristics can have exceptions — but the burden of proof is on whoever claims their complex system will be the exception.

- **"Simple" doesn't mean "trivial."** The simple starting system still requires good design. Gall's Law doesn't say *any* simple system will evolve into a working complex one — it says a working complex system will be found to have come from a simple one. The simple system has to actually work and be designed in a way that admits growth.

- **It doesn't prohibit planning.** Having a vision for where the system might go is fine, even valuable. The law says you can't *build* the complex end-state directly — not that you can't think about it. The art is holding a direction while accepting that each step must stand on its own.

- **Timescale matters.** Sometimes a "from scratch" system looks like a counterexample because the team is actually iterating rapidly internally — building simple prototypes, testing, revising — before the public launch. The final product appears to have been designed whole, but the process was evolutionary. SpaceX's rocket development looks like this.

## Connections

Gall's Law rhymes with many other ideas:

- **Agile development** is essentially Gall's Law applied as methodology: build the simplest working thing, iterate.
- **Worse is Better** (Richard Gabriel, 1989): the simpler, slightly worse design beats the complex, theoretically correct one — because the simple one actually ships and evolves.
- **The Second-System Effect** (Fred Brooks, *The Mythical Man-Month*): the second system a team builds tends to be over-engineered, exactly the failure mode Gall predicts.
- **Chesterton's Fence**: don't remove something from a system until you understand why it's there — respects the implicit knowledge that evolved systems carry.
- **Evolution as algorithm**: in theoretical biology and genetic algorithms, incremental selection from working intermediates is the only known process that reliably produces complex functional systems.

## Reflection

What makes Gall's Law compelling is that it's *humble*. It says: you are not smart enough to design a complex system that works. Nobody is. Not because of a lack of intelligence, but because complex systems operate in environments that are themselves complex, and the interactions between system and environment cannot be fully anticipated. The only way to navigate that complexity is incrementally, keeping the system functional at every step, letting reality teach you what the spec couldn't.

This is, in a sense, an argument for *epistemic modesty in engineering*. The knowledge required to build a working complex system doesn't exist before the system does — it is generated by the process of building and running simpler versions. Trying to front-load that knowledge into a design document is a category error.

The law also suggests something about the nature of understanding itself. We don't understand complex systems by analyzing them top-down; we understand them by building them bottom-up. The map is drawn by walking the territory.
