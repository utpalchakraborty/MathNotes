---
aliases: [Engram, Conditional Memory via Scalable Lookup]
tags: [deep-learning, architecture, deepseek, sparsity]
source: https://arxiv.org/abs/2601.07372
date: 2026-01-12
---

# Engram: Conditional Memory via Scalable Lookup

A paper from **DeepSeek** (January 2026) introducing **Engram**, a module that modernizes classical hashed n-gram embeddings into an O(1) lookup memory system for transformers. Code at [deepseek-ai/Engram](https://github.com/deepseek-ai/Engram).

## Core Insight

Language modeling involves two qualitatively different sub-tasks:

1. **Compositional reasoning** — dynamic, context-dependent logic
2. **Knowledge retrieval** — recalling static facts and patterns

Standard transformers (even MoE variants) use the same neural computation for both. Engram argues these deserve **separate sparsity axes**:

- **Conditional computation (MoE)**: activates parameters to process dynamic logic
- **Conditional memory (Engram)**: sparse lookup to retrieve static embeddings for fixed knowledge

## How Engram Works

### Hashed N-gram Embedding

1. **Token compression**: A surjective function normalizes token IDs (NFKC normalization, lowercasing), reducing effective vocabulary size by ~23%
2. **N-gram extraction**: For each position, extract suffix n-grams from the compressed token sequence
3. **Multi-head hashing**: Apply $K$ distinct hash functions, each mapping to a separate embedding table
4. **Concatenation**: The final memory vector concatenates all retrieved embeddings across n-gram orders and hash heads

The key property: addressing is **deterministic** — memory indices depend only on the input token sequence, not on runtime hidden states. This enables asynchronous retrieval.

### Architecture Placement

Engram is inserted at specific layers, not every layer. In the 27B model, it appears at **layers 2 and 15**, balancing:

- **Early intervention** — offload static pattern reconstruction from early layers
- **Sufficient depth** — contextual gating needs some representation quality

Layer 2 achieves the best single-layer performance when constrained to one injection point.

## U-Shaped Scaling Law

Under a fixed parameter/compute budget, allocating sparse capacity between MoE experts and Engram embeddings reveals a **U-shaped** relationship. Pure MoE ($\rho = 100\%$) is suboptimal. The sweet spot is reallocating roughly **20–25% of sparse parameters** to Engram ($\rho \approx 75\text{–}80\%$).

This demonstrates structural complementarity: MoE-only systems waste computation reconstructing static patterns, while Engram-only systems lack dynamic reasoning capacity.

## Mechanistic Analysis: Effective Depth

Two interpretability tools reveal what Engram actually does:

- **LogitLens**: Engram shows smaller KL divergence across layers vs. MoE baselines, with the biggest gap in early blocks — indicating faster feature composition
- **CKA (representational alignment)**: Engram's layer 5 representations align with approximately layer 12 of the MoE baseline

In other words, Engram **effectively deepens the network** by freeing early layers from static reconstruction, letting them focus on compositional reasoning instead.

## Inference Efficiency

Because addressing is deterministic (depends only on input tokens), Engram embeddings can be **offloaded to host memory** and retrieved asynchronously via PCIe while preceding transformer blocks compute. A 100B-parameter lookup table incurs only ~2.8% throughput overhead.

## Results (27B scale, iso-parameter/iso-FLOPs vs MoE baseline)

| Benchmark | Improvement |
|-----------|-------------|
| BBH (reasoning) | +5.0 |
| MMLU (knowledge) | +3.4 |
| CMMLU (knowledge) | +4.0 |
| ARC-Challenge | +3.7 |
| HumanEval (code) | +3.0 |
| MATH | +2.4 |
| Multi-Query NIAH | 84.2 → 97.0 |

Surprisingly, the largest gains are in **reasoning and code/math**, not just knowledge retrieval — suggesting the freed-up early layers contribute meaningfully to downstream reasoning.

## See Also

- [[mHC - manifold constrained hyper connections|mHC: Manifold-Constrained Hyper-Connections]]
