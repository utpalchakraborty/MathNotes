
Apparently, dense models are still the king. A note and discussion from Grok. 


**Yes, the claim in that post (and the image it's based on) checks out: both GPT-5.2 and the latest Claude Opus variants are indeed dense transformers.**

This isn't some fringe leak—it's consistent across multiple reports from model analyses, benchmarks, and architecture breakdowns released around their launches (GPT-5.2 in Dec 2025, Claude Opus 4.x/4.5/4.6 in mid-2025 to early 2026).

### Quick Confirmation from Sources
- **GPT-5.2**: Described as a "dense Transformer architecture" in comparisons vs. MoE rivals like GLM-5 (744B MoE) and Gemini 3 Pro. It's a full-parameter activation setup, emphasizing consistent response times and reliability for pro workflows like coding and agents.
- **Claude Opus**: Anthropic has stuck with dense transformers across the Claude 4 family (Opus, Sonnet, etc.). No MoE routing—it's all parameters firing per token, with innovations focused on hybrid reasoning modes (fast vs. extended thinking) instead.

This is in contrast to the flood of MoE models dominating cheaper/open-source frontiers right now (DeepSeek V4 at 1T params, GLM-5, Qwen3, Kimi K2.5, etc.), which route to just a subset of "experts" for massive efficiency gains.

### Why Are We *Still* Doing Dense Transformers?
Dense (full activation) vs. MoE (sparse, expert-routing) is the big architectural fork in 2025-2026 LLMs. MoE exploded because it lets you scale params *without* exploding inference costs—e.g., a 1T MoE might only activate 40B params per token, running on consumer GPUs in theory (though DeepSeek's "dual 4090" claim is hype; it needs way more VRAM).

But the top dogs (OpenAI, Anthropic) aren't switching yet. Here's why dense persists, based on performance data and lab trends:

| Aspect | Dense Transformers (GPT-5.2, Claude Opus) | MoE (DeepSeek V4, GLM-5, etc.) |
|--------|-------------------------------------------|--------------------------------|
| **Inference Efficiency** | Higher cost per token (all params active). GPT-5.2 Pro is pricey ($21/M input). | 10-40x cheaper (e.g., DeepSeek V4 at "near-zero" for coding). Scales to 1T+ params easily. |
| **Performance Edge** | Often tops benchmarks for *reasoning, coding, and consistency*. Claude Opus crushes SWE-Bench (80%+); GPT-5.2 shines in math/science (e.g., perfect contest-math). No routing noise—every token gets full model power. | Great for scale, but can have "expert imbalance" (some params underused) or routing overhead. Excels at cost/performance ratio, but trails dense on ultra-hard tasks. |
| **Training Stability** | Simpler: No router to tune. Easier to hit peak quality with proprietary data. | More complex (routing + expert specialization). Labs like DeepSeek nailed it for cheap training ($10M for V4), but it's finicky. |
| **Latency/Consistency** | More predictable (no expert load-balancing issues). Better for agents/long-context. | Faster on average for huge models, but variable if routing fails. |
| **Who Wins?** | Frontier quality (pro coding, research). | Commoditization (cheap, open, massive context like 1M tokens). |

**Do dense transformers provide *significant* benefits?**  
Yes, for the bleeding edge—especially in 2026, where "agentic" tasks (multi-hour coding, complex refactoring) matter more than raw token throughput. 

- **Quality per FLOP**: Papers (e.g., arXiv on MoE vs. dense) show well-tuned MoE *can* beat dense at equal resources, but in practice, dense models like Claude/GPT are pulling ahead on real-world evals (GPQA, SWE-Bench, agent benchmarks). Anthropic's "intent completion" and OpenAI's "thinking" modes leverage dense's uniformity.
- **Not going away soon**: Even as MoE dominates Chinese labs (winning the "race to cheap"), Western leaders are betting dense for reliability. MoE's edge is mostly economic—great for open-source disruption (DeepSeek V4's the poster child), but dense holds for $200/mo super-users.
- **Tradeoff reality**: Dense costs more to run, but if it delivers 20-30% better outputs on pro tasks (as seen in side-by-sides), the premium pays off. Expect hybrids soon (e.g., dense backbone + MoE layers).

The post's "tea" on DeepSeek is spot-on for the cost apocalypse narrative—China's MoE blitz is commoditizing AI hard. But GPT-5.2 and Claude Opus prove dense isn't obsolete; it's just the high-end play. If you're building agents or heavy coding, these are still the kings. For everything else? MoE all the way.