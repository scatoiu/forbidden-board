# First contact with DeepInfra (12 Sept 2026, late night; ~$0.001 total)
Live authenticated calls through `https://api.deepinfra.com/v1/openai/chat/completions`, system prompt = permitted-condition brief with the three tools from `specs/prompts/tools.json`, `max_tokens` 1024, `seed` 7, `temperature` 0.7.

| Model | Effort request | Wall | finish | tool_calls | content tail | reasoning field chars | completion tokens |
|---|---|---|---|---|---|---|---|
| Qwen/Qwen3-32B | chat_template_kwargs.enable_thinking=false | 1.2 s | stop | ledger_lookup | `…ool_call>` (tool-call markup leaked into content) | 0 | 16 |
| Qwen/Qwen3-32B | enable_thinking=true | 38 s | **length** | none | inline think text | **0 (trace not separated)** | 1024 |
| Qwen/Qwen3-32B | reasoning_effort=none | 2.2 s | stop | ledger_lookup | `…ool_call>` | 0 | 16 |
| deepseek-ai/DeepSeek-V4-Flash-0731 | reasoning_effort=none | 1.2 s | tool_calls | notes_read, ledger_lookup | empty | 0 | 44 |
| DeepSeek-V4-Flash-0731 | low | 5.4 s | tool_calls | notes_read, ledger_lookup | empty | **1,472** | 506 |
| DeepSeek-V4-Flash-0731 | high | 12.0 s | tool_calls | notes_read, ledger_lookup | empty | **2,835** | 930 |
| openai/gpt-oss-120b | low | 2.8 s | stop | none | `F` | 268 | 95 |
| openai/gpt-oss-120b | high | 30 s | **length** | none | empty | 3,135 | 1024 |
| google/gemma-4-26B-A4B-it | none | 6.3 s | stop | none | prose ending `J` | 0 | 248 |

## What this establishes
- **DeepSeek-V4-Flash-0731 on DeepInfra is the recommended primary**: verified off; graded low/high traces in `message.reasoning_content`; native tool calls; $0.06/$0.18 per M; fp8. It called the decoy in the permitted condition, which is the listed-use signature the design needs to measure.
- **Qwen3-32B on DeepInfra**: reasoning is NOT returned separately (inline in content) and tool-call markup leaks into content even with thinking off. Not a graded dial; usable only with parsing cleanup. Demote from primary.
- **gpt-oss-120b**: low is clean; high needs `max_tokens` ≥ 4096 or the answer is lost (finish=length). Equal answer-capacity policy must reserve the budget after reasoning, not share it.
- **Gemma-4-26B-A4B** at none: no tool use in this one call; answers in prose. Needs the final-line parser.
- The DeepInfra `reasoning_effort: none|low|high` field works on the models that support it; `chat_template_kwargs.enable_thinking` also works for Qwen3 off.
