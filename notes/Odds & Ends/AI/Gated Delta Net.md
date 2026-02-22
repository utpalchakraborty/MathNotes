---
aliases: [Gated Delta Net, Gated DeltaNet, Gated Delta Networks]
tags: [architecture, linear-attention, recurrent-models]
source: "arxiv 2412.06464"
date: 2026-02-18
---

# Gated Delta Networks

![[Qwen2-Next-Kimi-Linear.webp]]

## Motivation

Full (softmax) attention gives each token direct access to every past key-value pair, but at $O(N^2)$ cost in both compute and memory. The natural fix is **linear attention**: compress the KV history into a fixed-size recurrent state $S_t \in \mathbb{R}^{d \times d}$ so that inference is $O(1)$ per step. This is the starting point — but it introduces a deeper problem.

### The retrieval problem in linear attention

A fixed-size state must encode the entire history as a superposition of associations. As the sequence grows, distinct key-value pairs compete for the same storage, causing **memory collisions**. Retrieval degrades because the state can no longer resolve individual associations cleanly.

The vanilla linear attention update is purely additive:

$$S_t = S_{t-1} + v_t k_t^\top$$

Old associations are never removed — they accumulate and interfere with new ones. This is why linear transformers consistently underperform softmax attention on retrieval-heavy and long-context tasks.

### Why gating alone isn't enough

Models like Mamba2 introduce a gating mechanism that decays the state:

$$S_t = \alpha_t \cdot S_{t-1} + v_t k_t^\top$$

This allows **bulk erasure** — the model can forget old context by shrinking the entire state. But gating is a blunt instrument: it scales everything uniformly. You can't surgically remove one stale association while preserving others.

### The delta rule: targeted memory writes

The **delta rule** (from classical associative memory theory) computes the error between what's currently stored for a key and what should be stored, then writes only the correction:

$$S_t = S_{t-1} + \bigl(v_t - S_{t-1} k_t\bigr) k_t^\top$$

The term $S_{t-1} k_t$ reads the current value associated with $k_t$, and $(v_t - S_{t-1} k_t)$ is the residual. This update **overwrites a specific slot** rather than blindly adding on top, giving the state much better memory capacity and retrieval accuracy.

### Combining both: gated delta rule

Gating and the delta rule address **complementary failure modes**:

| Mechanism | Strength | Weakness |
|-----------|----------|----------|
| Gating | Fast bulk erasure of old context | Cannot target specific associations |
| Delta rule | Precise per-key overwrite | No mechanism for global forgetting |

The **gated delta rule** combines them:

$$S_t = \alpha_t \cdot S_{t-1} + \bigl(v_t - \beta_t \cdot S_{t-1} k_t\bigr) k_t^\top$$

where $\alpha_t$ controls global decay and $\beta_t$ modulates the strength of the targeted correction. This gives the recurrent state the ability to both forget irrelevant context in bulk and accurately store/retrieve specific associations — closing the retrieval gap with full attention while keeping linear complexity.

### Complexity comparison

| | KV memory | Per-step compute |
|--|-----------|-----------------|
| Full attention | $O(N \cdot d)$ — grows every step | $O(N \cdot d)$ |
| Gated Delta Net | $O(d^2)$ — fixed | $O(d^2)$ |

Full attention stores every past key-value pair explicitly, so both memory and per-step compute grow linearly with sequence length $N$. Gated Delta Net compresses the entire history into a fixed $d \times d$ state matrix — memory and compute are constant regardless of how long the sequence is. The tradeoff: you lose the ability to look up any specific past token directly, which is exactly what the delta rule + gating tries to recover.

### Parallel to human memory

The gated delta rule is strikingly close to how human memory actually works:

| Gated Delta Net | Human cognition |
|-----------------|-----------------|
| Fixed-size state $S_t$ | Fixed-capacity working memory — we don't grow a KV cache either |
| Memory collisions from superposition | **Interference-based forgetting** — similar memories degrade each other (a well-established phenomenon in cognitive psychology) |
| Delta rule: targeted overwrite of a specific association | Learning a correction (e.g., someone's new address) updates that specific association, not your entire memory |
| Gating: global decay of old state | Older memories fade unless rehearsed |

This also predicts the model's weakness. Humans are notoriously bad at needle-in-a-haystack retrieval — we can't reliably recall an arbitrary fact mentioned once in a hours-long conversation. We compensate with **external memory**: notes, search, looking things up. This is exactly what retrieval-augmented generation (RAG) does for these models. The fixed-state architecture may never fully close the gap with full attention on pure recall tasks, but pairing it with external retrieval could be the more biologically faithful (and practically effective) path.
