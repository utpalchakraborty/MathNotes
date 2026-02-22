---
aliases: [Chinchilla Scaling Laws, Compute-Optimal Training, Chinchilla Paper]
tags: [deep-learning, scaling-laws]
date: 2026-02-22
---

# Chinchilla Scaling Laws

**Paper:** [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) — Hoffmann et al., DeepMind, 2022 (NeurIPS 2022)

## Core Claim

For a given compute budget, existing large language models are significantly **undertrained**. Model size and training data should be scaled **equally** — for every doubling of model size, the number of training tokens should also be doubled.

The optimal ratio is roughly **20 tokens per parameter**.

## The Scaling Law

### Compute Budget

Total training compute is approximated by:

$$C \approx 6ND$$

where $N$ is the number of parameters and $D$ is the number of training tokens. The factor of 6 accounts for both forward and backward passes across all operations.

### Parametric Loss Function

The final loss as a function of model size and data is:

$$L(N, D) = E + \frac{A}{N^\alpha} + \frac{B}{D^\beta}$$

with fitted values:

| Parameter | Value |
|-----------|-------|
| $A$ | $406.4$ |
| $\alpha$ | $0.34$ |
| $B$ | $410.7$ |
| $\beta$ | $0.28$ |
| $E$ | $1.69$ |

The first term $E$ is the irreducible loss (entropy of natural language). The second term captures how loss decreases with more parameters. The third captures how loss decreases with more data.

### Optimal Allocation

Given a fixed compute budget $C$, the optimal number of parameters and tokens both scale as the **square root** of compute:

$$N_{\text{opt}} \propto C^{0.50}, \qquad D_{\text{opt}} \propto C^{0.50}$$

This means parameters and data should grow at the **same rate** — a stark contrast to the prior Kaplan et al. scaling laws, which suggested spending most of the budget on larger models.

## Three Approaches, One Answer

The paper is notable for using three independent methods that all converge on the same conclusion:

```mermaid
graph TD
    A["<b>Approach 1</b><br/><i>Fixed model sizes</i><br/>Vary tokens for each of<br/>400+ models (70M–16B)"]
    B["<b>Approach 2</b><br/><i>IsoFLOP profiles</i><br/>Fix compute budget,<br/>vary N and D"]
    C["<b>Approach 3</b><br/><i>Parametric fit</i><br/>Fit L(N, D) = E + A/Nᵅ + B/Dᵝ<br/>directly to all runs"]
    D["<b>Conclusion</b><br/>N and D scale equally<br/>≈ 20 tokens per parameter"]

    A --> D
    B --> D
    C --> D

    style A fill:#e8d5b7,stroke:#333
    style B fill:#e8d5b7,stroke:#333
    style C fill:#e8d5b7,stroke:#333
    style D fill:#d4edda,stroke:#333
```

The agreement across three different methodologies gives strong confidence in the result.

## How Undertrained Were Existing Models?

```mermaid
graph LR
    subgraph "Pre-Chinchilla Models"
        GPT3["<b>GPT-3</b><br/>175B params<br/>300B tokens<br/>1.7 tok/param"]
        Gopher["<b>Gopher</b><br/>280B params<br/>300B tokens<br/>1.1 tok/param"]
        MT["<b>Megatron-Turing NLG</b><br/>530B params<br/>270B tokens<br/>0.5 tok/param"]
    end

    subgraph "Chinchilla-Optimal"
        Chinchilla["<b>Chinchilla</b><br/>70B params<br/>1.4T tokens<br/>20 tok/param"]
    end

    GPT3 -.- |"~12× undertrained"| Chinchilla
    Gopher -.- |"~18× undertrained"| Chinchilla
    MT -.- |"~40× undertrained"| Chinchilla

    style GPT3 fill:#f5c6c6,stroke:#333
    style Gopher fill:#f5c6c6,stroke:#333
    style MT fill:#f5c6c6,stroke:#333
    style Chinchilla fill:#d4edda,stroke:#333
```

Every major model before Chinchilla was massively undertrained relative to its size. They invested heavily in parameters while starving the model of data.

### Concrete Example

At a budget of $10^{22}$ FLOPs:

| Strategy | Parameters | Tokens |
|----------|-----------|--------|
| **Chinchilla-optimal** | $\sim 9.1\text{B}$ | $\sim 182\text{B}$ |
| **Kaplan-optimal** (prior law) | $\sim 759\text{B}$ | $\sim 22\text{B}$ |

Same compute, radically different allocation — and the Chinchilla allocation wins.

At $10^{24}$ FLOPs, the gap widens:

| Strategy | Parameters | Tokens |
|----------|-----------|--------|
| **Chinchilla-optimal** | $\sim 91\text{B}$ | $\sim 1.8\text{T}$ |
| **Kaplan-optimal** | $\sim 759\text{B}$ | $\sim 220\text{B}$ |

## The Chinchilla Model

To validate the theory, DeepMind trained **Chinchilla**: a 70B parameter model on 1.4T tokens, using the same compute budget as the 280B parameter Gopher.

Results on MMLU (Massive Multitask Language Understanding):

| Model | Parameters | MMLU Accuracy |
|-------|-----------|---------------|
| Gopher | 280B | 60.0% |
| GPT-3 | 175B | 43.9% |
| Megatron-Turing NLG | 530B | 33.3% |
| **Chinchilla** | **70B** | **67.6%** |

Chinchilla — 4× smaller than Gopher — beat it by 7.6 percentage points. It also surpassed expert forecasts for June 2023 accuracy (63.4%) and achieved >90% on four individual MMLU tasks.

## Why It Matters

```mermaid
graph TD
    C["<b>Chinchilla Insight</b><br/>Scale data equally with params"]

    I1["<b>Smaller Models</b><br/>Cheaper inference,<br/>easier deployment"]
    I2["<b>Data Bottleneck</b><br/>Training data quality<br/>becomes the constraint"]
    I3["<b>LLaMA Family</b><br/>7B–65B models trained<br/>on 1–1.4T tokens"]
    I4["<b>Beyond Chinchilla</b><br/>Overtrain small models<br/>for cheaper inference"]

    C --> I1
    C --> I2
    C --> I3
    C --> I4

    I4 -.- |"e.g. LLaMA trained<br/>past optimal for its size"| I3

    style C fill:#e8d5b7,stroke:#333
    style I1 fill:#b7d5e8,stroke:#333
    style I2 fill:#b7d5e8,stroke:#333
    style I3 fill:#b7d5e8,stroke:#333
    style I4 fill:#b7d5e8,stroke:#333
```

1. **Inference cost** — A compute-optimal model is smaller, so it's cheaper to serve. Chinchilla at 70B is far easier to deploy than Gopher at 280B, while performing better.
2. **Data becomes king** — The field shifted focus to data quality and quantity. Getting enough high-quality tokens became the bottleneck, not GPU count.
3. **Influenced LLaMA** — Meta's LLaMA models (2023) followed Chinchilla's philosophy: smaller models trained on much more data. LLaMA-7B was trained on 1T tokens (~140 tok/param), deliberately *overtraining* past Chinchilla-optimal to trade training compute for cheaper inference.
4. **"Beyond Chinchilla" strategies** — For deployment, it can make sense to train a model past its compute-optimal point. A smaller model that's overtrained costs less to serve per query, even if the training run was "wasteful" by Chinchilla standards.

## Scope: Pretraining Only

Chinchilla addresses **pretraining** exclusively — autoregressive next-token prediction on a text corpus. The paper came out in March 2022, the same month as InstructGPT, before the modern multi-stage pipeline became standard.

A frontier model's training today looks more like:

```mermaid
graph LR
    PT["<b>Pretraining</b><br/><i>Chinchilla applies here</i><br/>Next-token prediction<br/>on trillions of tokens"]
    SFT["<b>SFT</b><br/>Supervised fine-tuning<br/>on curated instruction/<br/>response pairs"]
    RL["<b>RL Post-Training</b><br/>RLHF, RLAIF, or<br/>outcome-based RL<br/>(e.g. DeepSeek-R1, o1)"]
    EVAL["<b>Deployed Model</b>"]

    PT --> SFT --> RL --> EVAL

    style PT fill:#d4edda,stroke:#333
    style SFT fill:#b7d5e8,stroke:#333
    style RL fill:#b7d5e8,stroke:#333
    style EVAL fill:#e8d5b7,stroke:#333
```

Chinchilla says nothing about:

- **SFT compute** — How much supervised fine-tuning data and how many passes over it are optimal
- **RL compute** — How to allocate FLOPs between pretraining and reinforcement learning. Models like OpenAI's o1/o3 and DeepSeek-R1 spend enormous compute on RL, which fundamentally reshapes what "compute-optimal" means
- **Inference-time compute** — Chain-of-thought, search, and verification at inference time (the "test-time compute" paradigm) didn't exist yet
- **Data mixing** — The optimal blend of code, math, web text, synthetic data, etc.

This is arguably the biggest gap in the Chinchilla framework for understanding 2025–2026 models. A lab's total compute budget now splits across pretraining, SFT, and RL — and the optimal *split* across stages is a separate (and largely unpublished) scaling question. It's entirely possible that for a fixed total budget, spending *less* on pretraining and *more* on RL yields a better model than Chinchilla-optimal pretraining alone.

## Limitations

- The law was derived for **autoregressive transformer LMs** — it may not transfer directly to other architectures or tasks.
- The fitted exponents depend on the specific training setup (optimizer, learning rate schedule, data distribution).
- At very large scales, the power-law relationship may break down or shift.
- The paper doesn't account for **inference cost** in its optimality criterion — it only optimizes for training loss per FLOP. Models deployed at scale may benefit from being smaller and overtrained.
- Recent work suggests the optimal ratio may be higher than 20 for some settings, and data quality matters as much as quantity.
- **Only covers one stage** of a multi-stage pipeline — see above.

## See Also
- [[Dense vs Moe|Dense vs MoE]] — Architectural choices in frontier models (2025–2026)
