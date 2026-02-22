---
name: discover-connections
description: Use when the user asks to find missing connections, deep insights, or gaps in the vault, or when asked to explore a note and find what's missing between related concepts
---

# Discover Connections

Finds mathematical insights that are implicit across multiple vault notes but never stated explicitly. Reads a note, traces its wikilink neighborhood, and identifies a bridging concept or theorem that unifies the connected notes — then writes it up as a new note.

## Workflow

### 1. Pick a Seed Note

Accept a note from the user, or choose one that is a **hub** — many outgoing wikilinks to diverse topics. Good seeds have 4+ See Also links spanning different areas (e.g., a note linking to both series convergence and special functions).

### 2. Read the Neighborhood (1-2 Hops)

- Read the seed note fully
- Follow every wikilink in its See Also section and read those notes
- For the most promising connections, follow one more hop (the connected notes' See Also links)
- Goal: hold 4-8 notes in context simultaneously

### 3. Identify the Gap

Look for one of these patterns:

| Gap type | Signal | Example |
|----------|--------|---------|
| **Missing bridge** | Two notes reference the same concept from different angles but never link to each other | Infinite products + Gamma function both use convergence factors, but no note explains the Weierstrass product connecting them |
| **Unstated consequence** | A theorem in note A, applied to a definition in note B, yields a result mentioned in neither | Digamma derivatives evaluated at integers give zeta values |
| **Hidden equivalence** | Two notes prove related things by different methods, but the deeper equivalence is never stated | Euler's sine product *is* the Gamma reflection formula |
| **Missing generalization** | Several notes are special cases of a theorem not in the vault | Multiple convergence tests as corollaries of a single comparison principle |

**Quality bar:** The insight should be something a student reading the individual notes would likely miss, but that deepens understanding of both sides once seen.

### 4. Write It Up

Use the `new-math-note` skill to create the note. Additional requirements for discovered connections:

- **Tags must include `claude-generated`** — marks this as a synthesized insight, not transcribed from course material
- **Introduction should frame the gap** — explain which existing notes contain the pieces and why the connection matters
- **Cross-link densely** — the whole point is bridging existing notes, so the See Also section and inline wikilinks should be rich
- **Include a Mermaid concept map** — show visually how the new note sits at the center of the existing connections

### 5. Present the Insight

After writing the note, explain to the user:
- Which notes you read and what gap you found
- Why this insight matters (what it unifies or reveals)
- A brief summary of the mathematical content

## Vault Search Tool

```bash
uv run python scripts/vault_search.py search <query>              # full-text search
uv run python scripts/vault_search.py search --titles <query>     # search note names/aliases
uv run python scripts/vault_search.py backlinks <note>            # find notes linking to a note
uv run python scripts/vault_search.py links --check               # verify wikilinks after writing
```

## Choosing Good Seeds

If the user says "any note," prefer notes that are:
- **High-degree hubs** — many See Also links (more surface area for gaps)
- **At topic boundaries** — e.g., a note touching both series and special functions, or convergence and number theory
- **Recently created** — newer notes may not yet be fully integrated into the vault's link graph

Avoid notes that are:
- Leaf nodes with 0-1 outgoing links
- Pure definition notes with no theorems to connect
- Already heavily cross-linked with no obvious gaps

## Checklist

- [ ] Seed note chosen (hub with 4+ diverse links)
- [ ] Seed note and all See Also targets read
- [ ] At least one second-hop note read
- [ ] Gap identified (bridge, consequence, equivalence, or generalization)
- [ ] Insight is non-obvious — not just "these two things are related"
- [ ] New note created via `new-math-note` workflow
- [ ] Tags include `claude-generated`
- [ ] Mermaid diagram shows the new note's position among existing notes
- [ ] Wikilinks verified: `uv run python scripts/vault_search.py links --check`
- [ ] Insight explained to user with context
