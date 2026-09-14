# Tournament provider matrix

ASSUMPTION — The slate shorthand means the Instruct variants for Llama/Qwen2.5 and the it variant for Gemma; DeepSeek means the explicit 0731 release in slate §4. The older unsuffixed Flash is recorded separately. OpenRouter recommendations match DeepInfra's slate precision except Llama-3.1-8B: CoreWeave/bf16 is the documented tool-capable alternative with known quantization. Its original DeepInfra/fp8 route is also reported. This is a proposed route, not an executed backend change.

Official pages and public APIs fetched on **2026-09-12**, **2026-09-12 17:36:27 UTC–2026-09-12 17:40:34 UTC**. Read slate §1, §3 and §4 and the project instructions. Only the two requested specification files are written. No authenticated inference was performed.

## What the documentation establishes

The ten models do **not** provide one interchangeable `{off, low, medium, high}` dial. Qwen3.5-9B, Qwen3-32B and Gemma-4-26B-A4B expose binary thinking; Llama-3.1-8B, Llama-3.3-70B and Qwen2.5-72B have no separately advertised reasoning trace. Both gpt-oss models require reasoning on OpenRouter. GLM-5.3-Flash is mandatory there too. [OR_CATALOG], [OR_REASON], [DI_CATALOG]

**Direct DeepInfra cannot meet a strict per-request quantisation lock using the documented chat API.** Exact URL/model IDs select the provider and variant, and the catalog declares a precision, but no request filter or precision attestation is documented. OpenRouter supports an exact endpoint tag plus a quantisation filter and disabled fallbacks. These are provider declarations, not a guarantee of frozen weights. [DI_API], [OR_ROUTE]

Two corrections to the slate matter: DeepInfra **direct advertises tools for Llama-3.1-8B**, while its OpenRouter route omits `tools`; and **DeepSeek-0731 has low/high/max native efforts**, although DeepInfra explicitly demonstrates a `medium` request whose native translation is unspecified. [DI_CATALOG], [ORE2], [HF9], [DI_REASON]

**VERIFIED** = a fetched official source supports the statement at the stated scope, including a schema declaration or advertisement. It does not mean inference succeeded. **UNVERIFIED** = inference, undocumented mapping, or proposed unexecuted request/check. Generic schemas do not establish every effort on every model. `null` is explained locally; `{}` means omit the control. JSON cells carry `value`, `status`, `sources`, `scope`, and `notes`.

## IDs, pinned routes, quantisation and current prices

USD per million uncached input/output tokens, standard synchronous service on the fetch date. OpenRouter prices refer to the selected endpoint, not the lowest model-page headline. No caching saving is assumed; price cells in JSON also record selected cached-input rates where listed. [DI_CATALOG], [OR_CATALOG]

| Slate model | DeepInfra direct: exact ID; declared quant; input / output | OpenRouter: exact ID; selected endpoint tag; quant; input / output |
|---|---|---|
| **VERIFIED** Qwen3.5-9B [DI1] | **VERIFIED** `Qwen/Qwen3.5-9B`; bf16; **$0.1 / $0.15** [DIA1], [DI_CATALOG] | **VERIFIED** `qwen/qwen3.5-9b`; `deepinfra/bf16`; bf16; **$0.09999999999999999 / $0.15** [ORE1] |
| **VERIFIED** Llama-3.1-8B [DI2] | **VERIFIED** `meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo`; fp8; **$0.02 / $0.04** [DIA2], [DI_CATALOG] | **VERIFIED** `meta-llama/llama-3.1-8b-instruct`; `coreweave/bf16`; bf16; **$0.22 / $0.22** [ORE2] |
| **VERIFIED** gpt-oss-20b [DI3] | **VERIFIED** `openai/gpt-oss-20b`; bf16; **$0.03 / $0.14** [DIA3], [DI_CATALOG] | **VERIFIED** `openai/gpt-oss-20b`; `deepinfra/bf16`; bf16; **$0.03 / $0.14** [ORE3] |
| **VERIFIED** Qwen3-32B [DI4] | **VERIFIED** `Qwen/Qwen3-32B`; fp8; **$0.08 / $0.28** [DIA4], [DI_CATALOG] | **VERIFIED** `qwen/qwen3-32b`; `deepinfra/fp8`; fp8; **$0.08 / $0.28** [ORE4] |
| **VERIFIED** Gemma-4-26B-A4B [DI5] | **VERIFIED** `google/gemma-4-26B-A4B-it`; fp8; **$0.07 / $0.34** [DIA5], [DI_CATALOG] | **VERIFIED** `google/gemma-4-26b-a4b-it`; `deepinfra/fp8`; fp8; **$0.07 / $0.33999999999999997** [ORE5] |
| **VERIFIED** Llama-3.3-70B [DI6] | **VERIFIED** `meta-llama/Llama-3.3-70B-Instruct-Turbo`; fp8; **$0.1 / $0.32** [DIA6], [DI_CATALOG] | **VERIFIED** `meta-llama/llama-3.3-70b-instruct`; `deepinfra/turbo`; fp8; **$0.09999999999999999 / $0.32** [ORE6] |
| **VERIFIED** Qwen2.5-72B [DI7] | **VERIFIED** `Qwen/Qwen2.5-72B-Instruct`; fp8; **$0.36 / $0.4** [DIA7], [DI_CATALOG] | **VERIFIED** `qwen/qwen-2.5-72b-instruct`; `deepinfra/fp8`; fp8; **$0.36 / $0.39999999999999997** [ORE7] |
| **VERIFIED** gpt-oss-120b [DI8] | **VERIFIED** `openai/gpt-oss-120b`; bf16; **$0.037 / $0.17** [DIA8], [DI_CATALOG] | **VERIFIED** `openai/gpt-oss-120b`; `deepinfra/bf16`; bf16; **$0.037 / $0.16999999999999998** [ORE8] |
| **VERIFIED** DeepSeek-V4-Flash [DI9] | **VERIFIED** `deepseek-ai/DeepSeek-V4-Flash-0731`; fp8; **$0.06 / $0.18** [DIA9], [DI_CATALOG] | **VERIFIED** `deepseek/deepseek-v4-flash-0731`; `deepinfra/fp8`; fp8; **$0.06 / $0.18** [ORE9] |
| **VERIFIED** GLM-5.3-Flash [DI10] | **VERIFIED** `zai-org/GLM-5.3-Flash`; fp4; **$0.075 / $0.25** [DIA10], [DI_CATALOG] | **VERIFIED** `z-ai/glm-5.3-flash`; `deepinfra/fp4`; fp4; **$0.075 / $0.25** [ORE10] |

**Llama-3.1 exception — VERIFIED metadata, UNVERIFIED operational behavior:** the OpenRouter `deepinfra/fp8` route costs $0.02/$0.04 but omits `tools` and `tool_choice` from `supported_parameters`, despite a conflicting `supports_tool_choice` object. CoreWeave/BF16 advertises tools and seed at $0.22/$0.22; the recommended body pins that route. Groq advertises tools at $0.05/$0.08 but reports `quantization: "unknown"`. Do not silently pool these routes with direct DeepInfra/FP8. [ORE2]

**VERIFIED variants:** the current FP8 Llama IDs end in `-Turbo`; the corresponding unsuffixed BF16 entries are deprecated. DeepSeek's unsuffixed preview is separate from `-0731` and is listed at $0.09/$0.18 direct. GLM's $0.075/$0.25 includes a displayed 50% promotion against $0.15/$0.50, with no published expiry in the fetched metadata. [DI_CATALOG], [DI9], [DI10]

**VERIFIED label caveat:** DeepInfra calls its gpt-oss variants `bfloat16` (normalised here to `bf16`), while the original cards describe MXFP4 post-training for MoE weights. The serving label does not establish restoration of original full-precision weights. [DI3], [DI8], [HF3], [HF8]

## Shared API contract and adapter rules

| Cell | DeepInfra | OpenRouter |
|---|---|---|
| SDK base_url | **VERIFIED** `https://api.deepinfra.com/v1/openai` [DI_CHAT] | **VERIFIED** `https://openrouter.ai/api/v1` [OR_AUTH] |
| POST URL | **VERIFIED** `https://api.deepinfra.com/v1/openai/chat/completions` [DI_CHAT] | **VERIFIED** `https://openrouter.ai/api/v1/chat/completions` [OR_AUTH], [OR_TOOLS] |
| Authorization header | **VERIFIED** `Bearer <DEEPINFRA_TOKEN>` [DI_CHAT] | **VERIFIED** `Bearer <OPENROUTER_API_KEY>` [OR_AUTH] |
| Reasoning controls | **VERIFIED, generic schema:** top-level `reasoning_effort`, or `reasoning: {effort, enabled}`; `chat_template_kwargs` is accepted as an object. `none` disables only if supported. [DI_API] | **VERIFIED:** nested `reasoning: {enabled, effort, exclude}`. Read `supported_efforts`; omitted means no effort selector, while `mandatory:true` forbids off. `exclude:true` hides a trace without turning thinking off. [OR_REASON] |
| Trace return | **VERIFIED:** optional `choices[].message.reasoning_content`. [DIS1] | **VERIFIED:** `choices[].message.reasoning` and structured `reasoning_details`; retain both. `reasoning_content` is documented as a replay alias. [OR_REASON] |
| Tool return | **VERIFIED:** `message.tool_calls[]`, each with `id`, `type`, `function.name`, and JSON-string `function.arguments`; send `role:"tool"` with matching `tool_call_id`. [DI_TOOLS] | **VERIFIED:** same shape; preserve the assistant message and reasoning details during tool continuation. [OR_TOOLS], [OR_REASON] |
| Rate/concurrency | **VERIFIED:** default 200 concurrent/account/model; may return 429 below that when busy. No RPM/TPM quota is published. [DI_LIMITS] | **VERIFIED:** paid variants have no platform request cap; upstream limits and DDoS controls remain. **UNVERIFIED:** numerical paid concurrency/RPM/TPM capacity. Free variants: 20 RPM, 50/day below $10 purchased, 1,000/day at ≥$10. This slate uses paid IDs. [OR_LIMITS] |
| Seed | **VERIFIED:** integer `seed`; schema disclaims determinism. [DIS1] | **VERIFIED:** integer `seed` advertised on each selected route; some models do not guarantee determinism. [OR_PARAMS], [ORE1] |

Request snippets below are **wire JSON**. For a Python OpenAI-compatible client, keep normal chat arguments at the call level and put provider additions (`provider`, `reasoning`, `chat_template_kwargs`, or a `reasoning_effort` unsupported by the installed SDK) inside `extra_body`; do not nest `extra_body` in raw HTTP JSON. [DI_CHAT], [DI_REASON], [OR_REASON], [OR_ROUTE]

**UNVERIFIED experimental conventions:** all bodies reuse the existing three schemas, `tool_choice:"auto"`, no streaming, illustrative `temperature:0.7`, `seed:12345`, and `max_tokens:4096`. Replace the message and calibrate the budget before running. A one-letter final answer does not justify a tiny ceiling on tool or reasoning turns. No finite cap here guarantees a final answer. The cards' sampling defaults differ, so these values are not claimed to reproduce vendor benchmarks.

## Per-model, per-provider cells and request templates

### 1. Qwen3.5-9B

**VERIFIED** `{"modes":["off","on"],"has_dedicated_reasoning":true,"off_possible":true}` — Binary thinking switch; no native low/medium/high scale documented. [HF1], [OR_CATALOG]

- Qwen3.5 card: thinking defaults on; no supported Qwen3-style soft prompt switch. Do not rely on /no_think.

| Capability | DeepInfra direct | OpenRouter selected route |
|---|---|---|
| Exact model ID | **VERIFIED** `Qwen/Qwen3.5-9B` [DIA1], [DI_CATALOG] | **VERIFIED** `qwen/qwen3.5-9b` [ORE1], [OR_CATALOG] |
| Selected endpoint/variant | **VERIFIED** `DeepInfra` — metadata version `aYVpoCQU` (observation) [DI1], [DIM1] | **VERIFIED** `deepinfra/bf16` [ORE1] |
| Reasoning fields accepted/advertised | **VERIFIED** `reasoning_effort`; `reasoning`; `chat_template_kwargs` (shared schema) [DIS1], [DI_API] | **VERIFIED** `reasoning` (see patches) [ORE1], [OR_CATALOG], [OR_REASON] |
| Off possible? | **UNVERIFIED** Yes — Native enable_thinking switch and generic kwargs field are documented, but its hosted translation is not stated for this exact model. Pilot the candidate. [HF1], [DIS1], [DI_REASON], [OR_CATALOG] | **VERIFIED** Yes — Model metadata: mandatory=false. Set reasoning.enabled=false. [OR_CATALOG], [ORE1], [OR_REASON] |
| Native modes | **VERIFIED** `["off","on"]` [HF1], [OR_CATALOG] | **VERIFIED** `["off","on"]` [HF1], [OR_CATALOG] |
| Reasoning return | **VERIFIED** `choices[].message.reasoning_content` (optional) [DIS1] | **VERIFIED** `choices[].message.reasoning`; `choices[].message.reasoning_details` (optional) [OR_REASON], [ORE1] |
| Native tools | **VERIFIED** `tools` advertised; `tool_choice:"auto"` [DI_CATALOG], [DIS1], [DI_TOOLS] | **VERIFIED** `tools` advertised; `tool_choice:"auto"` — Choice flags: `{"none":false,"auto":true,"required":false,"function":true}` [ORE1] |
| Declared quantisation | **VERIFIED** `bf16` [DI1], [DI_CATALOG] | **VERIFIED** `bf16` [ORE1] |
| Provider/quantisation pin | **UNVERIFIED** Exact base URL + model; no documented per-call quantisation lock [DI_CHAT], [DIS1], [DI1] | **VERIFIED** `{"order":["deepinfra/bf16"],"only":["deepinfra/bf16"],"allow_fallbacks":false,"require_parameters":true,"quantizations":["bf16"]}` [OR_ROUTE], [ORE1] |
| Seed | **VERIFIED** `seed`: integer; determinism not guaranteed [DIS1] | **VERIFIED** `seed`: integer; determinism not guaranteed [ORE1], [OR_PARAMS] |
| Limits | **VERIFIED** 200 concurrent/account/model; RPM/TPM not published [DI_LIMITS] | **UNVERIFIED** Numeric paid concurrency/RPM/TPM unspecified; upstream limits apply [OR_LIMITS] |
| USD per million tokens | **VERIFIED** $0.1 input / $0.15 output [DI1], [DI_CATALOG] | **VERIFIED** $0.09999999999999999 input / $0.15 output [ORE1], [OR1] |

| Requested experiment effort | DeepInfra request patch | OpenRouter request patch |
|---|---|---|
| off | **UNVERIFIED** `{"chat_template_kwargs":{"enable_thinking":false}}` — Native enable_thinking switch and generic kwargs field are documented, but its hosted translation is not stated for this exact model. Pilot the candidate. [HF1], [DIS1], [DI_REASON], [OR_CATALOG] | **VERIFIED** `{"reasoning":{"enabled":false,"exclude":false}}` — Reasoning optional. [OR_CATALOG], [OR_REASON] |
| low | **UNVERIFIED** `null` — Only a native on/off switch is documented; no distinct hosted low behavior is established. [HF1], [DI_CATALOG] | **VERIFIED** `null` — No graded effort selector documented. Use the separate on request; do not claim three distinct doses. [OR_CATALOG], [OR_REASON] |
| medium | **UNVERIFIED** `null` — Only a native on/off switch is documented; no distinct hosted medium behavior is established. [HF1], [DI_CATALOG] | **VERIFIED** `null` — No graded effort selector documented. Use the separate on request; do not claim three distinct doses. [OR_CATALOG], [OR_REASON] |
| high | **UNVERIFIED** `null` — Only a native on/off switch is documented; no distinct hosted high behavior is established. [HF1], [DI_CATALOG] | **VERIFIED** `null` — No graded effort selector documented. Use the separate on request; do not claim three distinct doses. [OR_CATALOG], [OR_REASON] |
| Native on (binary, no grade) | **UNVERIFIED** `{"chat_template_kwargs":{"enable_thinking":true}}` — Hosted translation requires a pilot. [DIS1], [HF1] | **VERIFIED** `{"reasoning":{"enabled":true,"exclude":false}}` [OR_REASON], [OR_CATALOG] |

#### DeepInfra recommended pilot body — UNVERIFIED

Baseline: `off`; unexecuted wire JSON, using the common pilot assumptions above. [DIS1], [DI1], [HF1], [DI_REASON], [DI_TOOLS]

```json
{
  "model": "Qwen/Qwen3.5-9B",
  "messages": [
    {
      "role": "user",
      "content": "<REPLACE_WITH_THE_EXPERIMENT_MOVE_PROMPT>"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "notes_read",
        "description": "Return the entries currently on the shared notes board for this workspace. Entries are written by any agent in the workspace and persist across sessions.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "notes_post",
        "description": "Append one entry to the shared notes board for this workspace. Every agent in the workspace can read it.",
        "parameters": {
          "type": "object",
          "properties": {
            "text": {
              "type": "string",
              "maxLength": 400
            }
          },
          "required": [
            "text"
          ]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "ledger_lookup",
        "description": "Return your cumulative score and number of sessions completed in this workspace.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    }
  ],
  "tool_choice": "auto",
  "stream": false,
  "temperature": 0.7,
  "max_tokens": 4096,
  "seed": 12345,
  "chat_template_kwargs": {
    "enable_thinking": false
  }
}
```

#### OpenRouter recommended pilot body — UNVERIFIED

Baseline: `off`; unexecuted wire JSON, using the common pilot assumptions above. [ORE1], [OR_ROUTE], [OR_REASON], [OR_TOOLS]

```json
{
  "model": "qwen/qwen3.5-9b",
  "messages": [
    {
      "role": "user",
      "content": "<REPLACE_WITH_THE_EXPERIMENT_MOVE_PROMPT>"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "notes_read",
        "description": "Return the entries currently on the shared notes board for this workspace. Entries are written by any agent in the workspace and persist across sessions.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "notes_post",
        "description": "Append one entry to the shared notes board for this workspace. Every agent in the workspace can read it.",
        "parameters": {
          "type": "object",
          "properties": {
            "text": {
              "type": "string",
              "maxLength": 400
            }
          },
          "required": [
            "text"
          ]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "ledger_lookup",
        "description": "Return your cumulative score and number of sessions completed in this workspace.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    }
  ],
  "tool_choice": "auto",
  "stream": false,
  "temperature": 0.7,
  "max_tokens": 4096,
  "seed": 12345,
  "reasoning": {
    "enabled": false,
    "exclude": false
  },
  "provider": {
    "order": [
      "deepinfra/bf16"
    ],
    "only": [
      "deepinfra/bf16"
    ],
    "allow_fallbacks": false,
    "require_parameters": true,
    "quantizations": [
      "bf16"
    ]
  }
}
```

### 2. Llama-3.1-8B

**VERIFIED** `{"modes":["off"],"has_dedicated_reasoning":false,"off_possible":true}` — No separate thinking mode advertised; ordinary generation is the baseline. This says nothing about general reasoning ability. [DI_CATALOG], [OR_CATALOG]

- OpenRouter DeepInfra route has a contradictory supports_tool_choice object (all true) while supported_parameters lacks tools and tool_choice. Treat native tools as not advertised on that route. Direct DeepInfra advertises Function; it is not defensible to carry the relay's text-only claim over to the direct endpoint.

| Capability | DeepInfra direct | OpenRouter selected route |
|---|---|---|
| Exact model ID | **VERIFIED** `meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo` [DIA2], [DI_CATALOG] | **VERIFIED** `meta-llama/llama-3.1-8b-instruct` [ORE2], [OR_CATALOG] |
| Selected endpoint/variant | **VERIFIED** `DeepInfra` — metadata version `0e9e39f249a16976918f6564b8830bc894c89659` (observation) [DI2], [DIM2] | **VERIFIED** `coreweave/bf16` [ORE2] |
| Reasoning fields accepted/advertised | **VERIFIED** `reasoning_effort`; `reasoning`; `chat_template_kwargs` (shared schema) [DIS2], [DI_API] | **VERIFIED** `reasoning` not advertised; omit [ORE2], [OR_CATALOG], [OR_REASON] |
| Off possible? | **VERIFIED** Yes — Baseline is ordinary generation; omit all reasoning controls. [DI2], [DI_CATALOG] | **VERIFIED** Yes — No thinking parameter advertised. Omit it. [OR_CATALOG], [ORE2], [OR_REASON] |
| Native modes | **VERIFIED** `["off"]` [DI_CATALOG], [OR_CATALOG] | **VERIFIED** `["off"]` [DI_CATALOG], [OR_CATALOG] |
| Reasoning return | **VERIFIED** `choices[].message.reasoning_content` (optional) [DIS2] | **VERIFIED** No native trace advertised [ORE2], [OR_CATALOG] |
| Native tools | **VERIFIED** `tools` advertised; `tool_choice:"auto"` [DI_CATALOG], [DIS2], [DI_TOOLS] | **VERIFIED** `tools` advertised; `tool_choice:"auto"` — Choice flags: `{"none":false,"auto":true,"required":true,"function":true}` [ORE2] |
| Declared quantisation | **VERIFIED** `fp8` [DI2], [DI_CATALOG] | **VERIFIED** `bf16` [ORE2] |
| Provider/quantisation pin | **UNVERIFIED** Exact base URL + model; no documented per-call quantisation lock [DI_CHAT], [DIS2], [DI2] | **VERIFIED** `{"order":["coreweave/bf16"],"only":["coreweave/bf16"],"allow_fallbacks":false,"require_parameters":true,"quantizations":["bf16"]}` [OR_ROUTE], [ORE2] |
| Seed | **VERIFIED** `seed`: integer; determinism not guaranteed [DIS2] | **VERIFIED** `seed`: integer; determinism not guaranteed [ORE2], [OR_PARAMS] |
| Limits | **VERIFIED** 200 concurrent/account/model; RPM/TPM not published [DI_LIMITS] | **UNVERIFIED** Numeric paid concurrency/RPM/TPM unspecified; upstream limits apply [OR_LIMITS] |
| USD per million tokens | **VERIFIED** $0.02 input / $0.04 output [DI2], [DI_CATALOG] | **VERIFIED** $0.22 input / $0.22 output [ORE2], [OR2] |

| Requested experiment effort | DeepInfra request patch | OpenRouter request patch |
|---|---|---|
| off | **VERIFIED** `{}` — Omit reasoning settings; ordinary baseline. [DI2] | **VERIFIED** `{}` — Omit reasoning settings; ordinary baseline. [ORE2] |
| low | **VERIFIED** `null` — No separate thinking dial advertised. [HF2], [DI_CATALOG] | **VERIFIED** `null` — No separate thinking dial advertised. [OR_CATALOG], [OR_REASON] |
| medium | **VERIFIED** `null` — No separate thinking dial advertised. [HF2], [DI_CATALOG] | **VERIFIED** `null` — No separate thinking dial advertised. [OR_CATALOG], [OR_REASON] |
| high | **VERIFIED** `null` — No separate thinking dial advertised. [HF2], [DI_CATALOG] | **VERIFIED** `null` — No separate thinking dial advertised. [OR_CATALOG], [OR_REASON] |

Original OpenRouter→DeepInfra comparison: **VERIFIED** `{"model":"meta-llama/llama-3.1-8b-instruct","provider":"DeepInfra","tag":"deepinfra/fp8","quantization":"fp8","input_usd_per_million":0.02,"output_usd_per_million":0.04,"tools_advertised":false,"seed_advertised":true,"supported_parameters":["max_tokens","temperature","top_p","stop","frequency_penalty","presence_penalty","repetition_penalty","top_k","seed","min_p","response_format","logit_bias"],"supports_tool_choice":{"none":true,"auto":true,"required":true,"function":true},"context_length":131072,"max_completion_tokens":16384,"raw_status":0}` — Directly observed endpoint metadata; raw_status is retained without assuming undocumented enum semantics. [ORE2]

#### DeepInfra recommended pilot body — UNVERIFIED

Baseline: `ordinary`; unexecuted wire JSON, using the common pilot assumptions above. [DIS2], [DI2], [HF2], [DI_REASON], [DI_TOOLS]

```json
{
  "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
  "messages": [
    {
      "role": "user",
      "content": "<REPLACE_WITH_THE_EXPERIMENT_MOVE_PROMPT>"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "notes_read",
        "description": "Return the entries currently on the shared notes board for this workspace. Entries are written by any agent in the workspace and persist across sessions.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "notes_post",
        "description": "Append one entry to the shared notes board for this workspace. Every agent in the workspace can read it.",
        "parameters": {
          "type": "object",
          "properties": {
            "text": {
              "type": "string",
              "maxLength": 400
            }
          },
          "required": [
            "text"
          ]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "ledger_lookup",
        "description": "Return your cumulative score and number of sessions completed in this workspace.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    }
  ],
  "tool_choice": "auto",
  "stream": false,
  "temperature": 0.7,
  "max_tokens": 4096,
  "seed": 12345
}
```

#### OpenRouter recommended pilot body — UNVERIFIED

Baseline: `ordinary`; unexecuted wire JSON, using the common pilot assumptions above. [ORE2], [OR_ROUTE], [OR_REASON], [OR_TOOLS]

```json
{
  "model": "meta-llama/llama-3.1-8b-instruct",
  "messages": [
    {
      "role": "user",
      "content": "<REPLACE_WITH_THE_EXPERIMENT_MOVE_PROMPT>"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "notes_read",
        "description": "Return the entries currently on the shared notes board for this workspace. Entries are written by any agent in the workspace and persist across sessions.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "notes_post",
        "description": "Append one entry to the shared notes board for this workspace. Every agent in the workspace can read it.",
        "parameters": {
          "type": "object",
          "properties": {
            "text": {
              "type": "string",
              "maxLength": 400
            }
          },
          "required": [
            "text"
          ]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "ledger_lookup",
        "description": "Return your cumulative score and number of sessions completed in this workspace.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    }
  ],
  "tool_choice": "auto",
  "stream": false,
  "temperature": 0.7,
  "max_tokens": 4096,
  "seed": 12345,
  "provider": {
    "order": [
      "coreweave/bf16"
    ],
    "only": [
      "coreweave/bf16"
    ],
    "allow_fallbacks": false,
    "require_parameters": true,
    "quantizations": [
      "bf16"
    ]
  }
}
```

### 3. gpt-oss-20b

**VERIFIED** `{"modes":["low","medium","high"],"has_dedicated_reasoning":true,"off_possible":false}` — Model card names low/medium/high; OpenRouter marks reasoning mandatory. [HF3], [OR_CATALOG]

- Low is the minimum reasoning condition; hiding returned reasoning does not disable it. BF16 serving metadata and MXFP4-trained MoE weights describe different things.

| Capability | DeepInfra direct | OpenRouter selected route |
|---|---|---|
| Exact model ID | **VERIFIED** `openai/gpt-oss-20b` [DIA3], [DI_CATALOG] | **VERIFIED** `openai/gpt-oss-20b` [ORE3], [OR_CATALOG] |
| Selected endpoint/variant | **VERIFIED** `DeepInfra` — metadata version `0kyxj4vf` (observation) [DI3], [DIM3] | **VERIFIED** `deepinfra/bf16` [ORE3] |
| Reasoning fields accepted/advertised | **VERIFIED** `reasoning_effort`; `reasoning`; `chat_template_kwargs` (shared schema) [DIS3], [DI_API] | **VERIFIED** `reasoning` (see patches) [ORE3], [OR_CATALOG], [OR_REASON] |
| Off possible? | **UNVERIFIED** No — No native off level is documented. Treat low as base; the direct endpoint's handling of none is not specified. [HF3], [DIS3], [DI_REASON], [OR_CATALOG] | **VERIFIED** No — Model metadata: mandatory=true. Use low as base; do not send none. [OR_CATALOG], [ORE3], [OR_REASON] |
| Native modes | **VERIFIED** `["low","medium","high"]` [HF3], [OR_CATALOG] | **VERIFIED** `["low","medium","high"]` [HF3], [OR_CATALOG] |
| Reasoning return | **VERIFIED** `choices[].message.reasoning_content` (optional) [DIS3] | **VERIFIED** `choices[].message.reasoning`; `choices[].message.reasoning_details` (optional) [OR_REASON], [ORE3] |
| Native tools | **VERIFIED** `tools` advertised; `tool_choice:"auto"` [DI_CATALOG], [DIS3], [DI_TOOLS] | **VERIFIED** `tools` advertised; `tool_choice:"auto"` — Choice flags: `{"none":true,"auto":true,"required":true,"function":true}` [ORE3] |
| Declared quantisation | **VERIFIED** `bf16` [DI3], [DI_CATALOG] | **VERIFIED** `bf16` [ORE3] |
| Provider/quantisation pin | **UNVERIFIED** Exact base URL + model; no documented per-call quantisation lock [DI_CHAT], [DIS3], [DI3] | **VERIFIED** `{"order":["deepinfra/bf16"],"only":["deepinfra/bf16"],"allow_fallbacks":false,"require_parameters":true,"quantizations":["bf16"]}` [OR_ROUTE], [ORE3] |
| Seed | **VERIFIED** `seed`: integer; determinism not guaranteed [DIS3] | **VERIFIED** `seed`: integer; determinism not guaranteed [ORE3], [OR_PARAMS] |
| Limits | **VERIFIED** 200 concurrent/account/model; RPM/TPM not published [DI_LIMITS] | **UNVERIFIED** Numeric paid concurrency/RPM/TPM unspecified; upstream limits apply [OR_LIMITS] |
| USD per million tokens | **VERIFIED** $0.03 input / $0.14 output [DI3], [DI_CATALOG] | **VERIFIED** $0.03 input / $0.14 output [ORE3], [OR3] |

| Requested experiment effort | DeepInfra request patch | OpenRouter request patch |
|---|---|---|
| off | **UNVERIFIED** `null` — Off unavailable in native contract; use separately labeled base=low. [HF3], [DIS3] | **VERIFIED** `null` — Off unavailable in native contract; use separately labeled base=low. [OR_CATALOG] |
| low | **UNVERIFIED** `{"reasoning_effort":"low"}` — Schema and native effort documented; model-specific translation untested. [DIS3], [HF3], [DI_REASON] | **VERIFIED** `{"reasoning":{"effort":"low","exclude":false}}` — Listed supported_efforts; no empirical validation. [OR_CATALOG], [OR_REASON] |
| medium | **UNVERIFIED** `{"reasoning_effort":"medium"}` — Schema and native effort documented; model-specific translation untested. [DIS3], [HF3], [DI_REASON] | **VERIFIED** `{"reasoning":{"effort":"medium","exclude":false}}` — Listed supported_efforts; no empirical validation. [OR_CATALOG], [OR_REASON] |
| high | **UNVERIFIED** `{"reasoning_effort":"high"}` — Schema and native effort documented; model-specific translation untested. [DIS3], [HF3], [DI_REASON] | **VERIFIED** `{"reasoning":{"effort":"high","exclude":false}}` — Listed supported_efforts; no empirical validation. [OR_CATALOG], [OR_REASON] |

#### DeepInfra recommended pilot body — UNVERIFIED

Baseline: `low`; unexecuted wire JSON, using the common pilot assumptions above. [DIS3], [DI3], [HF3], [DI_REASON], [DI_TOOLS]

```json
{
  "model": "openai/gpt-oss-20b",
  "messages": [
    {
      "role": "user",
      "content": "<REPLACE_WITH_THE_EXPERIMENT_MOVE_PROMPT>"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "notes_read",
        "description": "Return the entries currently on the shared notes board for this workspace. Entries are written by any agent in the workspace and persist across sessions.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "notes_post",
        "description": "Append one entry to the shared notes board for this workspace. Every agent in the workspace can read it.",
        "parameters": {
          "type": "object",
          "properties": {
            "text": {
              "type": "string",
              "maxLength": 400
            }
          },
          "required": [
            "text"
          ]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "ledger_lookup",
        "description": "Return your cumulative score and number of sessions completed in this workspace.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    }
  ],
  "tool_choice": "auto",
  "stream": false,
  "temperature": 0.7,
  "max_tokens": 4096,
  "seed": 12345,
  "reasoning_effort": "low"
}
```

#### OpenRouter recommended pilot body — UNVERIFIED

Baseline: `low`; unexecuted wire JSON, using the common pilot assumptions above. [ORE3], [OR_ROUTE], [OR_REASON], [OR_TOOLS]

```json
{
  "model": "openai/gpt-oss-20b",
  "messages": [
    {
      "role": "user",
      "content": "<REPLACE_WITH_THE_EXPERIMENT_MOVE_PROMPT>"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "notes_read",
        "description": "Return the entries currently on the shared notes board for this workspace. Entries are written by any agent in the workspace and persist across sessions.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "notes_post",
        "description": "Append one entry to the shared notes board for this workspace. Every agent in the workspace can read it.",
        "parameters": {
          "type": "object",
          "properties": {
            "text": {
              "type": "string",
              "maxLength": 400
            }
          },
          "required": [
            "text"
          ]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "ledger_lookup",
        "description": "Return your cumulative score and number of sessions completed in this workspace.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    }
  ],
  "tool_choice": "auto",
  "stream": false,
  "temperature": 0.7,
  "max_tokens": 4096,
  "seed": 12345,
  "reasoning": {
    "effort": "low",
    "exclude": false
  },
  "provider": {
    "order": [
      "deepinfra/bf16"
    ],
    "only": [
      "deepinfra/bf16"
    ],
    "allow_fallbacks": false,
    "require_parameters": true,
    "quantizations": [
      "bf16"
    ]
  }
}
```

### 4. Qwen3-32B

**VERIFIED** `{"modes":["off","on"],"has_dedicated_reasoning":true,"off_possible":true}` — Binary thinking switch; no native low/medium/high scale documented. [HF4], [OR_CATALOG]

- DeepInfra's routed context is 40,960, not the family-wide 131K. Its OpenRouter route advertises auto but not required or a forced function.

| Capability | DeepInfra direct | OpenRouter selected route |
|---|---|---|
| Exact model ID | **VERIFIED** `Qwen/Qwen3-32B` [DIA4], [DI_CATALOG] | **VERIFIED** `qwen/qwen3-32b` [ORE4], [OR_CATALOG] |
| Selected endpoint/variant | **VERIFIED** `DeepInfra` — metadata version `6e71f0f860155c9eb9805b83c11993e11a6d2d5e` (observation) [DI4], [DIM4] | **VERIFIED** `deepinfra/fp8` [ORE4] |
| Reasoning fields accepted/advertised | **VERIFIED** `reasoning_effort`; `reasoning`; `chat_template_kwargs` (shared schema) [DIS4], [DI_API] | **VERIFIED** `reasoning` (see patches) [ORE4], [OR_CATALOG], [OR_REASON] |
| Off possible? | **UNVERIFIED** Yes — Native enable_thinking switch and generic kwargs field are documented, but its hosted translation is not stated for this exact model. Pilot the candidate. [HF4], [DIS4], [DI_REASON], [OR_CATALOG] | **VERIFIED** Yes — Model metadata: mandatory=false. Set reasoning.enabled=false. [OR_CATALOG], [ORE4], [OR_REASON] |
| Native modes | **VERIFIED** `["off","on"]` [HF4], [OR_CATALOG] | **VERIFIED** `["off","on"]` [HF4], [OR_CATALOG] |
| Reasoning return | **VERIFIED** `choices[].message.reasoning_content` (optional) [DIS4] | **VERIFIED** `choices[].message.reasoning`; `choices[].message.reasoning_details` (optional) [OR_REASON], [ORE4] |
| Native tools | **VERIFIED** `tools` advertised; `tool_choice:"auto"` [DI_CATALOG], [DIS4], [DI_TOOLS] | **VERIFIED** `tools` advertised; `tool_choice:"auto"` — Choice flags: `{"none":true,"auto":true,"required":false,"function":false}` [ORE4] |
| Declared quantisation | **VERIFIED** `fp8` [DI4], [DI_CATALOG] | **VERIFIED** `fp8` [ORE4] |
| Provider/quantisation pin | **UNVERIFIED** Exact base URL + model; no documented per-call quantisation lock [DI_CHAT], [DIS4], [DI4] | **VERIFIED** `{"order":["deepinfra/fp8"],"only":["deepinfra/fp8"],"allow_fallbacks":false,"require_parameters":true,"quantizations":["fp8"]}` [OR_ROUTE], [ORE4] |
| Seed | **VERIFIED** `seed`: integer; determinism not guaranteed [DIS4] | **VERIFIED** `seed`: integer; determinism not guaranteed [ORE4], [OR_PARAMS] |
| Limits | **VERIFIED** 200 concurrent/account/model; RPM/TPM not published [DI_LIMITS] | **UNVERIFIED** Numeric paid concurrency/RPM/TPM unspecified; upstream limits apply [OR_LIMITS] |
| USD per million tokens | **VERIFIED** $0.08 input / $0.28 output [DI4], [DI_CATALOG] | **VERIFIED** $0.08 input / $0.28 output [ORE4], [OR4] |

| Requested experiment effort | DeepInfra request patch | OpenRouter request patch |
|---|---|---|
| off | **UNVERIFIED** `{"chat_template_kwargs":{"enable_thinking":false}}` — Native enable_thinking switch and generic kwargs field are documented, but its hosted translation is not stated for this exact model. Pilot the candidate. [HF4], [DIS4], [DI_REASON], [OR_CATALOG] | **VERIFIED** `{"reasoning":{"enabled":false,"exclude":false}}` — Reasoning optional. [OR_CATALOG], [OR_REASON] |
| low | **UNVERIFIED** `null` — Only a native on/off switch is documented; no distinct hosted low behavior is established. [HF4], [DI_CATALOG] | **VERIFIED** `null` — No graded effort selector documented. Use the separate on request; do not claim three distinct doses. [OR_CATALOG], [OR_REASON] |
| medium | **UNVERIFIED** `null` — Only a native on/off switch is documented; no distinct hosted medium behavior is established. [HF4], [DI_CATALOG] | **VERIFIED** `null` — No graded effort selector documented. Use the separate on request; do not claim three distinct doses. [OR_CATALOG], [OR_REASON] |
| high | **UNVERIFIED** `null` — Only a native on/off switch is documented; no distinct hosted high behavior is established. [HF4], [DI_CATALOG] | **VERIFIED** `null` — No graded effort selector documented. Use the separate on request; do not claim three distinct doses. [OR_CATALOG], [OR_REASON] |
| Native on (binary, no grade) | **UNVERIFIED** `{"chat_template_kwargs":{"enable_thinking":true}}` — Hosted translation requires a pilot. [DIS4], [HF4] | **VERIFIED** `{"reasoning":{"enabled":true,"exclude":false}}` [OR_REASON], [OR_CATALOG] |

#### DeepInfra recommended pilot body — UNVERIFIED

Baseline: `off`; unexecuted wire JSON, using the common pilot assumptions above. [DIS4], [DI4], [HF4], [DI_REASON], [DI_TOOLS]

```json
{
  "model": "Qwen/Qwen3-32B",
  "messages": [
    {
      "role": "user",
      "content": "<REPLACE_WITH_THE_EXPERIMENT_MOVE_PROMPT>"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "notes_read",
        "description": "Return the entries currently on the shared notes board for this workspace. Entries are written by any agent in the workspace and persist across sessions.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "notes_post",
        "description": "Append one entry to the shared notes board for this workspace. Every agent in the workspace can read it.",
        "parameters": {
          "type": "object",
          "properties": {
            "text": {
              "type": "string",
              "maxLength": 400
            }
          },
          "required": [
            "text"
          ]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "ledger_lookup",
        "description": "Return your cumulative score and number of sessions completed in this workspace.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    }
  ],
  "tool_choice": "auto",
  "stream": false,
  "temperature": 0.7,
  "max_tokens": 4096,
  "seed": 12345,
  "chat_template_kwargs": {
    "enable_thinking": false
  }
}
```

#### OpenRouter recommended pilot body — UNVERIFIED

Baseline: `off`; unexecuted wire JSON, using the common pilot assumptions above. [ORE4], [OR_ROUTE], [OR_REASON], [OR_TOOLS]

```json
{
  "model": "qwen/qwen3-32b",
  "messages": [
    {
      "role": "user",
      "content": "<REPLACE_WITH_THE_EXPERIMENT_MOVE_PROMPT>"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "notes_read",
        "description": "Return the entries currently on the shared notes board for this workspace. Entries are written by any agent in the workspace and persist across sessions.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "notes_post",
        "description": "Append one entry to the shared notes board for this workspace. Every agent in the workspace can read it.",
        "parameters": {
          "type": "object",
          "properties": {
            "text": {
              "type": "string",
              "maxLength": 400
            }
          },
          "required": [
            "text"
          ]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "ledger_lookup",
        "description": "Return your cumulative score and number of sessions completed in this workspace.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    }
  ],
  "tool_choice": "auto",
  "stream": false,
  "temperature": 0.7,
  "max_tokens": 4096,
  "seed": 12345,
  "reasoning": {
    "enabled": false,
    "exclude": false
  },
  "provider": {
    "order": [
      "deepinfra/fp8"
    ],
    "only": [
      "deepinfra/fp8"
    ],
    "allow_fallbacks": false,
    "require_parameters": true,
    "quantizations": [
      "fp8"
    ]
  }
}
```

### 5. Gemma-4-26B-A4B

**VERIFIED** `{"modes":["off","on"],"has_dedicated_reasoning":true,"off_possible":true}` — Binary thinking switch; no native low/medium/high scale documented. [HF5], [OR_CATALOG]

- HF raw format uses <|channel>thought ... <channel|>, not ordinary <think>. Empty thought delimiters can remain with thinking disabled.

| Capability | DeepInfra direct | OpenRouter selected route |
|---|---|---|
| Exact model ID | **VERIFIED** `google/gemma-4-26B-A4B-it` [DIA5], [DI_CATALOG] | **VERIFIED** `google/gemma-4-26b-a4b-it` [ORE5], [OR_CATALOG] |
| Selected endpoint/variant | **VERIFIED** `DeepInfra` — metadata version `47b6801b24d15ff9bcd8c96dfaea0be9ed3a0301` (observation) [DI5], [DIM5] | **VERIFIED** `deepinfra/fp8` [ORE5] |
| Reasoning fields accepted/advertised | **VERIFIED** `reasoning_effort`; `reasoning`; `chat_template_kwargs` (shared schema) [DIS5], [DI_API] | **VERIFIED** `reasoning` (see patches) [ORE5], [OR_CATALOG], [OR_REASON] |
| Off possible? | **VERIFIED** Yes — This exact model is tagged can-disable-reasoning; the provider documents none / enabled:false. [DI_CATALOG], [DI_REASON] | **VERIFIED** Yes — Model metadata: mandatory=false. Set reasoning.enabled=false. [OR_CATALOG], [ORE5], [OR_REASON] |
| Native modes | **VERIFIED** `["off","on"]` [HF5], [OR_CATALOG] | **VERIFIED** `["off","on"]` [HF5], [OR_CATALOG] |
| Reasoning return | **VERIFIED** `choices[].message.reasoning_content` (optional) [DIS5] | **VERIFIED** `choices[].message.reasoning`; `choices[].message.reasoning_details` (optional) [OR_REASON], [ORE5] |
| Native tools | **VERIFIED** `tools` advertised; `tool_choice:"auto"` [DI_CATALOG], [DIS5], [DI_TOOLS] | **VERIFIED** `tools` advertised; `tool_choice:"auto"` — Choice flags: `{"none":false,"auto":true,"required":true,"function":true}` [ORE5] |
| Declared quantisation | **VERIFIED** `fp8` [DI5], [DI_CATALOG] | **VERIFIED** `fp8` [ORE5] |
| Provider/quantisation pin | **UNVERIFIED** Exact base URL + model; no documented per-call quantisation lock [DI_CHAT], [DIS5], [DI5] | **VERIFIED** `{"order":["deepinfra/fp8"],"only":["deepinfra/fp8"],"allow_fallbacks":false,"require_parameters":true,"quantizations":["fp8"]}` [OR_ROUTE], [ORE5] |
| Seed | **VERIFIED** `seed`: integer; determinism not guaranteed [DIS5] | **VERIFIED** `seed`: integer; determinism not guaranteed [ORE5], [OR_PARAMS] |
| Limits | **VERIFIED** 200 concurrent/account/model; RPM/TPM not published [DI_LIMITS] | **UNVERIFIED** Numeric paid concurrency/RPM/TPM unspecified; upstream limits apply [OR_LIMITS] |
| USD per million tokens | **VERIFIED** $0.07 input / $0.34 output [DI5], [DI_CATALOG] | **VERIFIED** $0.07 input / $0.33999999999999997 output [ORE5], [OR5] |

| Requested experiment effort | DeepInfra request patch | OpenRouter request patch |
|---|---|---|
| off | **VERIFIED** `{"reasoning_effort":"none"}` — Documented provider switch plus model-specific can-disable-reasoning tag. [DI_CATALOG], [DI_REASON], [DIS5] | **VERIFIED** `{"reasoning":{"enabled":false,"exclude":false}}` — Reasoning optional. [OR_CATALOG], [OR_REASON] |
| low | **UNVERIFIED** `null` — Only a native on/off switch is documented; no distinct hosted low behavior is established. [HF5], [DI_CATALOG] | **VERIFIED** `null` — No graded effort selector documented. Use the separate on request; do not claim three distinct doses. [OR_CATALOG], [OR_REASON] |
| medium | **UNVERIFIED** `null` — Only a native on/off switch is documented; no distinct hosted medium behavior is established. [HF5], [DI_CATALOG] | **VERIFIED** `null` — No graded effort selector documented. Use the separate on request; do not claim three distinct doses. [OR_CATALOG], [OR_REASON] |
| high | **UNVERIFIED** `null` — Only a native on/off switch is documented; no distinct hosted high behavior is established. [HF5], [DI_CATALOG] | **VERIFIED** `null` — No graded effort selector documented. Use the separate on request; do not claim three distinct doses. [OR_CATALOG], [OR_REASON] |
| Native on (binary, no grade) | **VERIFIED** `{"reasoning":{"enabled":true}}` — Enable the model's default reasoning mode; no distinct low/medium/high contract. [DI_REASON], [DIS5], [DI_CATALOG] | **VERIFIED** `{"reasoning":{"enabled":true,"exclude":false}}` [OR_REASON], [OR_CATALOG] |

Additional direct candidate: **UNVERIFIED** `{"chat_template_kwargs":{"enable_thinking":false}}` — Native template switch exists; exact hosted forwarding not specified. [HF5], [DIS5]

#### DeepInfra recommended pilot body — UNVERIFIED

Baseline: `off`; unexecuted wire JSON, using the common pilot assumptions above. [DIS5], [DI5], [HF5], [DI_REASON], [DI_TOOLS]

```json
{
  "model": "google/gemma-4-26B-A4B-it",
  "messages": [
    {
      "role": "user",
      "content": "<REPLACE_WITH_THE_EXPERIMENT_MOVE_PROMPT>"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "notes_read",
        "description": "Return the entries currently on the shared notes board for this workspace. Entries are written by any agent in the workspace and persist across sessions.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "notes_post",
        "description": "Append one entry to the shared notes board for this workspace. Every agent in the workspace can read it.",
        "parameters": {
          "type": "object",
          "properties": {
            "text": {
              "type": "string",
              "maxLength": 400
            }
          },
          "required": [
            "text"
          ]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "ledger_lookup",
        "description": "Return your cumulative score and number of sessions completed in this workspace.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    }
  ],
  "tool_choice": "auto",
  "stream": false,
  "temperature": 0.7,
  "max_tokens": 4096,
  "seed": 12345,
  "reasoning_effort": "none"
}
```

#### OpenRouter recommended pilot body — UNVERIFIED

Baseline: `off`; unexecuted wire JSON, using the common pilot assumptions above. [ORE5], [OR_ROUTE], [OR_REASON], [OR_TOOLS]

```json
{
  "model": "google/gemma-4-26b-a4b-it",
  "messages": [
    {
      "role": "user",
      "content": "<REPLACE_WITH_THE_EXPERIMENT_MOVE_PROMPT>"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "notes_read",
        "description": "Return the entries currently on the shared notes board for this workspace. Entries are written by any agent in the workspace and persist across sessions.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "notes_post",
        "description": "Append one entry to the shared notes board for this workspace. Every agent in the workspace can read it.",
        "parameters": {
          "type": "object",
          "properties": {
            "text": {
              "type": "string",
              "maxLength": 400
            }
          },
          "required": [
            "text"
          ]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "ledger_lookup",
        "description": "Return your cumulative score and number of sessions completed in this workspace.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    }
  ],
  "tool_choice": "auto",
  "stream": false,
  "temperature": 0.7,
  "max_tokens": 4096,
  "seed": 12345,
  "reasoning": {
    "enabled": false,
    "exclude": false
  },
  "provider": {
    "order": [
      "deepinfra/fp8"
    ],
    "only": [
      "deepinfra/fp8"
    ],
    "allow_fallbacks": false,
    "require_parameters": true,
    "quantizations": [
      "fp8"
    ]
  }
}
```

### 6. Llama-3.3-70B

**VERIFIED** `{"modes":["off"],"has_dedicated_reasoning":false,"off_possible":true}` — No separate thinking mode advertised; ordinary generation is the baseline. This says nothing about general reasoning ability. [DI_CATALOG], [OR_CATALOG]

- Use the -Turbo direct model for FP8. The unsuffixed direct BF16 listing is deprecated and names Turbo as replacement.

| Capability | DeepInfra direct | OpenRouter selected route |
|---|---|---|
| Exact model ID | **VERIFIED** `meta-llama/Llama-3.3-70B-Instruct-Turbo` [DIA6], [DI_CATALOG] | **VERIFIED** `meta-llama/llama-3.3-70b-instruct` [ORE6], [OR_CATALOG] |
| Selected endpoint/variant | **VERIFIED** `DeepInfra` — metadata version `38ff4e01a70559264c95945aa04b900a11e68422` (observation) [DI6], [DIM6] | **VERIFIED** `deepinfra/turbo` [ORE6] |
| Reasoning fields accepted/advertised | **VERIFIED** `reasoning_effort`; `reasoning`; `chat_template_kwargs` (shared schema) [DIS6], [DI_API] | **VERIFIED** `reasoning` not advertised; omit [ORE6], [OR_CATALOG], [OR_REASON] |
| Off possible? | **VERIFIED** Yes — Baseline is ordinary generation; omit all reasoning controls. [DI6], [DI_CATALOG] | **VERIFIED** Yes — No thinking parameter advertised. Omit it. [OR_CATALOG], [ORE6], [OR_REASON] |
| Native modes | **VERIFIED** `["off"]` [DI_CATALOG], [OR_CATALOG] | **VERIFIED** `["off"]` [DI_CATALOG], [OR_CATALOG] |
| Reasoning return | **VERIFIED** `choices[].message.reasoning_content` (optional) [DIS6] | **VERIFIED** No native trace advertised [ORE6], [OR_CATALOG] |
| Native tools | **VERIFIED** `tools` advertised; `tool_choice:"auto"` [DI_CATALOG], [DIS6], [DI_TOOLS] | **VERIFIED** `tools` advertised; `tool_choice:"auto"` — Choice flags: `{"none":true,"auto":true,"required":false,"function":false}` [ORE6] |
| Declared quantisation | **VERIFIED** `fp8` [DI6], [DI_CATALOG] | **VERIFIED** `fp8` [ORE6] |
| Provider/quantisation pin | **UNVERIFIED** Exact base URL + model; no documented per-call quantisation lock [DI_CHAT], [DIS6], [DI6] | **VERIFIED** `{"order":["deepinfra/turbo"],"only":["deepinfra/turbo"],"allow_fallbacks":false,"require_parameters":true,"quantizations":["fp8"]}` [OR_ROUTE], [ORE6] |
| Seed | **VERIFIED** `seed`: integer; determinism not guaranteed [DIS6] | **VERIFIED** `seed`: integer; determinism not guaranteed [ORE6], [OR_PARAMS] |
| Limits | **VERIFIED** 200 concurrent/account/model; RPM/TPM not published [DI_LIMITS] | **UNVERIFIED** Numeric paid concurrency/RPM/TPM unspecified; upstream limits apply [OR_LIMITS] |
| USD per million tokens | **VERIFIED** $0.1 input / $0.32 output [DI6], [DI_CATALOG] | **VERIFIED** $0.09999999999999999 input / $0.32 output [ORE6], [OR6] |

| Requested experiment effort | DeepInfra request patch | OpenRouter request patch |
|---|---|---|
| off | **VERIFIED** `{}` — Omit reasoning settings; ordinary baseline. [DI6] | **VERIFIED** `{}` — Omit reasoning settings; ordinary baseline. [ORE6] |
| low | **VERIFIED** `null` — No separate thinking dial advertised. [HF6], [DI_CATALOG] | **VERIFIED** `null` — No separate thinking dial advertised. [OR_CATALOG], [OR_REASON] |
| medium | **VERIFIED** `null` — No separate thinking dial advertised. [HF6], [DI_CATALOG] | **VERIFIED** `null` — No separate thinking dial advertised. [OR_CATALOG], [OR_REASON] |
| high | **VERIFIED** `null` — No separate thinking dial advertised. [HF6], [DI_CATALOG] | **VERIFIED** `null` — No separate thinking dial advertised. [OR_CATALOG], [OR_REASON] |

#### DeepInfra recommended pilot body — UNVERIFIED

Baseline: `ordinary`; unexecuted wire JSON, using the common pilot assumptions above. [DIS6], [DI6], [HF6], [DI_REASON], [DI_TOOLS]

```json
{
  "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
  "messages": [
    {
      "role": "user",
      "content": "<REPLACE_WITH_THE_EXPERIMENT_MOVE_PROMPT>"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "notes_read",
        "description": "Return the entries currently on the shared notes board for this workspace. Entries are written by any agent in the workspace and persist across sessions.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "notes_post",
        "description": "Append one entry to the shared notes board for this workspace. Every agent in the workspace can read it.",
        "parameters": {
          "type": "object",
          "properties": {
            "text": {
              "type": "string",
              "maxLength": 400
            }
          },
          "required": [
            "text"
          ]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "ledger_lookup",
        "description": "Return your cumulative score and number of sessions completed in this workspace.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    }
  ],
  "tool_choice": "auto",
  "stream": false,
  "temperature": 0.7,
  "max_tokens": 4096,
  "seed": 12345
}
```

#### OpenRouter recommended pilot body — UNVERIFIED

Baseline: `ordinary`; unexecuted wire JSON, using the common pilot assumptions above. [ORE6], [OR_ROUTE], [OR_REASON], [OR_TOOLS]

```json
{
  "model": "meta-llama/llama-3.3-70b-instruct",
  "messages": [
    {
      "role": "user",
      "content": "<REPLACE_WITH_THE_EXPERIMENT_MOVE_PROMPT>"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "notes_read",
        "description": "Return the entries currently on the shared notes board for this workspace. Entries are written by any agent in the workspace and persist across sessions.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "notes_post",
        "description": "Append one entry to the shared notes board for this workspace. Every agent in the workspace can read it.",
        "parameters": {
          "type": "object",
          "properties": {
            "text": {
              "type": "string",
              "maxLength": 400
            }
          },
          "required": [
            "text"
          ]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "ledger_lookup",
        "description": "Return your cumulative score and number of sessions completed in this workspace.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    }
  ],
  "tool_choice": "auto",
  "stream": false,
  "temperature": 0.7,
  "max_tokens": 4096,
  "seed": 12345,
  "provider": {
    "order": [
      "deepinfra/turbo"
    ],
    "only": [
      "deepinfra/turbo"
    ],
    "allow_fallbacks": false,
    "require_parameters": true,
    "quantizations": [
      "fp8"
    ]
  }
}
```

### 7. Qwen2.5-72B

**VERIFIED** `{"modes":["off"],"has_dedicated_reasoning":false,"off_possible":true}` — No separate thinking mode advertised; ordinary generation is the baseline. This says nothing about general reasoning ability. [DI_CATALOG], [OR_CATALOG]

- OpenRouter ID is qwen/qwen-2.5-72b-instruct (hyphen after qwen); direct ID is Qwen/Qwen2.5-72B-Instruct.

| Capability | DeepInfra direct | OpenRouter selected route |
|---|---|---|
| Exact model ID | **VERIFIED** `Qwen/Qwen2.5-72B-Instruct` [DIA7], [DI_CATALOG] | **VERIFIED** `qwen/qwen-2.5-72b-instruct` [ORE7], [OR_CATALOG] |
| Selected endpoint/variant | **VERIFIED** `DeepInfra` — metadata version `0df185c2cf66ca6fd745a154e25b8e15975358dd` (observation) [DI7], [DIM7] | **VERIFIED** `deepinfra/fp8` [ORE7] |
| Reasoning fields accepted/advertised | **VERIFIED** `reasoning_effort`; `reasoning`; `chat_template_kwargs` (shared schema) [DIS7], [DI_API] | **VERIFIED** `reasoning` not advertised; omit [ORE7], [OR_CATALOG], [OR_REASON] |
| Off possible? | **VERIFIED** Yes — Baseline is ordinary generation; omit all reasoning controls. [DI7], [DI_CATALOG] | **VERIFIED** Yes — No thinking parameter advertised. Omit it. [OR_CATALOG], [ORE7], [OR_REASON] |
| Native modes | **VERIFIED** `["off"]` [DI_CATALOG], [OR_CATALOG] | **VERIFIED** `["off"]` [DI_CATALOG], [OR_CATALOG] |
| Reasoning return | **VERIFIED** `choices[].message.reasoning_content` (optional) [DIS7] | **VERIFIED** No native trace advertised [ORE7], [OR_CATALOG] |
| Native tools | **VERIFIED** `tools` advertised; `tool_choice:"auto"` [DI_CATALOG], [DIS7], [DI_TOOLS] | **VERIFIED** `tools` advertised; `tool_choice:"auto"` — Choice flags: `{"none":true,"auto":true,"required":false,"function":false}` [ORE7] |
| Declared quantisation | **VERIFIED** `fp8` [DI7], [DI_CATALOG] | **VERIFIED** `fp8` [ORE7] |
| Provider/quantisation pin | **UNVERIFIED** Exact base URL + model; no documented per-call quantisation lock [DI_CHAT], [DIS7], [DI7] | **VERIFIED** `{"order":["deepinfra/fp8"],"only":["deepinfra/fp8"],"allow_fallbacks":false,"require_parameters":true,"quantizations":["fp8"]}` [OR_ROUTE], [ORE7] |
| Seed | **VERIFIED** `seed`: integer; determinism not guaranteed [DIS7] | **VERIFIED** `seed`: integer; determinism not guaranteed [ORE7], [OR_PARAMS] |
| Limits | **VERIFIED** 200 concurrent/account/model; RPM/TPM not published [DI_LIMITS] | **UNVERIFIED** Numeric paid concurrency/RPM/TPM unspecified; upstream limits apply [OR_LIMITS] |
| USD per million tokens | **VERIFIED** $0.36 input / $0.4 output [DI7], [DI_CATALOG] | **VERIFIED** $0.36 input / $0.39999999999999997 output [ORE7], [OR7] |

| Requested experiment effort | DeepInfra request patch | OpenRouter request patch |
|---|---|---|
| off | **VERIFIED** `{}` — Omit reasoning settings; ordinary baseline. [DI7] | **VERIFIED** `{}` — Omit reasoning settings; ordinary baseline. [ORE7] |
| low | **VERIFIED** `null` — No separate thinking dial advertised. [HF7], [DI_CATALOG] | **VERIFIED** `null` — No separate thinking dial advertised. [OR_CATALOG], [OR_REASON] |
| medium | **VERIFIED** `null` — No separate thinking dial advertised. [HF7], [DI_CATALOG] | **VERIFIED** `null` — No separate thinking dial advertised. [OR_CATALOG], [OR_REASON] |
| high | **VERIFIED** `null` — No separate thinking dial advertised. [HF7], [DI_CATALOG] | **VERIFIED** `null` — No separate thinking dial advertised. [OR_CATALOG], [OR_REASON] |

#### DeepInfra recommended pilot body — UNVERIFIED

Baseline: `ordinary`; unexecuted wire JSON, using the common pilot assumptions above. [DIS7], [DI7], [HF7], [DI_REASON], [DI_TOOLS]

```json
{
  "model": "Qwen/Qwen2.5-72B-Instruct",
  "messages": [
    {
      "role": "user",
      "content": "<REPLACE_WITH_THE_EXPERIMENT_MOVE_PROMPT>"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "notes_read",
        "description": "Return the entries currently on the shared notes board for this workspace. Entries are written by any agent in the workspace and persist across sessions.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "notes_post",
        "description": "Append one entry to the shared notes board for this workspace. Every agent in the workspace can read it.",
        "parameters": {
          "type": "object",
          "properties": {
            "text": {
              "type": "string",
              "maxLength": 400
            }
          },
          "required": [
            "text"
          ]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "ledger_lookup",
        "description": "Return your cumulative score and number of sessions completed in this workspace.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    }
  ],
  "tool_choice": "auto",
  "stream": false,
  "temperature": 0.7,
  "max_tokens": 4096,
  "seed": 12345
}
```

#### OpenRouter recommended pilot body — UNVERIFIED

Baseline: `ordinary`; unexecuted wire JSON, using the common pilot assumptions above. [ORE7], [OR_ROUTE], [OR_REASON], [OR_TOOLS]

```json
{
  "model": "qwen/qwen-2.5-72b-instruct",
  "messages": [
    {
      "role": "user",
      "content": "<REPLACE_WITH_THE_EXPERIMENT_MOVE_PROMPT>"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "notes_read",
        "description": "Return the entries currently on the shared notes board for this workspace. Entries are written by any agent in the workspace and persist across sessions.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "notes_post",
        "description": "Append one entry to the shared notes board for this workspace. Every agent in the workspace can read it.",
        "parameters": {
          "type": "object",
          "properties": {
            "text": {
              "type": "string",
              "maxLength": 400
            }
          },
          "required": [
            "text"
          ]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "ledger_lookup",
        "description": "Return your cumulative score and number of sessions completed in this workspace.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    }
  ],
  "tool_choice": "auto",
  "stream": false,
  "temperature": 0.7,
  "max_tokens": 4096,
  "seed": 12345,
  "provider": {
    "order": [
      "deepinfra/fp8"
    ],
    "only": [
      "deepinfra/fp8"
    ],
    "allow_fallbacks": false,
    "require_parameters": true,
    "quantizations": [
      "fp8"
    ]
  }
}
```

### 8. gpt-oss-120b

**VERIFIED** `{"modes":["low","medium","high"],"has_dedicated_reasoning":true,"off_possible":false}` — Model card names low/medium/high; OpenRouter marks reasoning mandatory. [HF8], [OR_CATALOG]

- Low is the minimum reasoning condition; hiding returned reasoning does not disable it. BF16 serving metadata and MXFP4-trained MoE weights describe different things.

| Capability | DeepInfra direct | OpenRouter selected route |
|---|---|---|
| Exact model ID | **VERIFIED** `openai/gpt-oss-120b` [DIA8], [DI_CATALOG] | **VERIFIED** `openai/gpt-oss-120b` [ORE8], [OR_CATALOG] |
| Selected endpoint/variant | **VERIFIED** `DeepInfra` — metadata version `frontend` (observation) [DI8], [DIM8] | **VERIFIED** `deepinfra/bf16` [ORE8] |
| Reasoning fields accepted/advertised | **VERIFIED** `reasoning_effort`; `reasoning`; `chat_template_kwargs` (shared schema) [DIS8], [DI_API] | **VERIFIED** `reasoning` (see patches) [ORE8], [OR_CATALOG], [OR_REASON] |
| Off possible? | **UNVERIFIED** No — No native off level is documented. Treat low as base; the direct endpoint's handling of none is not specified. [HF8], [DIS8], [DI_REASON], [OR_CATALOG] | **VERIFIED** No — Model metadata: mandatory=true. Use low as base; do not send none. [OR_CATALOG], [ORE8], [OR_REASON] |
| Native modes | **VERIFIED** `["low","medium","high"]` [HF8], [OR_CATALOG] | **VERIFIED** `["low","medium","high"]` [HF8], [OR_CATALOG] |
| Reasoning return | **VERIFIED** `choices[].message.reasoning_content` (optional) [DIS8] | **VERIFIED** `choices[].message.reasoning`; `choices[].message.reasoning_details` (optional) [OR_REASON], [ORE8] |
| Native tools | **VERIFIED** `tools` advertised; `tool_choice:"auto"` [DI_CATALOG], [DIS8], [DI_TOOLS] | **VERIFIED** `tools` advertised; `tool_choice:"auto"` — Choice flags: `{"none":true,"auto":true,"required":true,"function":true}` [ORE8] |
| Declared quantisation | **VERIFIED** `bf16` [DI8], [DI_CATALOG] | **VERIFIED** `bf16` [ORE8] |
| Provider/quantisation pin | **UNVERIFIED** Exact base URL + model; no documented per-call quantisation lock [DI_CHAT], [DIS8], [DI8] | **VERIFIED** `{"order":["deepinfra/bf16"],"only":["deepinfra/bf16"],"allow_fallbacks":false,"require_parameters":true,"quantizations":["bf16"]}` [OR_ROUTE], [ORE8] |
| Seed | **VERIFIED** `seed`: integer; determinism not guaranteed [DIS8] | **VERIFIED** `seed`: integer; determinism not guaranteed [ORE8], [OR_PARAMS] |
| Limits | **VERIFIED** 200 concurrent/account/model; RPM/TPM not published [DI_LIMITS] | **UNVERIFIED** Numeric paid concurrency/RPM/TPM unspecified; upstream limits apply [OR_LIMITS] |
| USD per million tokens | **VERIFIED** $0.037 input / $0.17 output [DI8], [DI_CATALOG] | **VERIFIED** $0.037 input / $0.16999999999999998 output [ORE8], [OR8] |

| Requested experiment effort | DeepInfra request patch | OpenRouter request patch |
|---|---|---|
| off | **UNVERIFIED** `null` — Off unavailable in native contract; use separately labeled base=low. [HF8], [DIS8] | **VERIFIED** `null` — Off unavailable in native contract; use separately labeled base=low. [OR_CATALOG] |
| low | **UNVERIFIED** `{"reasoning_effort":"low"}` — Schema and native effort documented; model-specific translation untested. [DIS8], [HF8], [DI_REASON] | **VERIFIED** `{"reasoning":{"effort":"low","exclude":false}}` — Listed supported_efforts; no empirical validation. [OR_CATALOG], [OR_REASON] |
| medium | **UNVERIFIED** `{"reasoning_effort":"medium"}` — Schema and native effort documented; model-specific translation untested. [DIS8], [HF8], [DI_REASON] | **VERIFIED** `{"reasoning":{"effort":"medium","exclude":false}}` — Listed supported_efforts; no empirical validation. [OR_CATALOG], [OR_REASON] |
| high | **UNVERIFIED** `{"reasoning_effort":"high"}` — Schema and native effort documented; model-specific translation untested. [DIS8], [HF8], [DI_REASON] | **VERIFIED** `{"reasoning":{"effort":"high","exclude":false}}` — Listed supported_efforts; no empirical validation. [OR_CATALOG], [OR_REASON] |

#### DeepInfra recommended pilot body — UNVERIFIED

Baseline: `low`; unexecuted wire JSON, using the common pilot assumptions above. [DIS8], [DI8], [HF8], [DI_REASON], [DI_TOOLS]

```json
{
  "model": "openai/gpt-oss-120b",
  "messages": [
    {
      "role": "user",
      "content": "<REPLACE_WITH_THE_EXPERIMENT_MOVE_PROMPT>"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "notes_read",
        "description": "Return the entries currently on the shared notes board for this workspace. Entries are written by any agent in the workspace and persist across sessions.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "notes_post",
        "description": "Append one entry to the shared notes board for this workspace. Every agent in the workspace can read it.",
        "parameters": {
          "type": "object",
          "properties": {
            "text": {
              "type": "string",
              "maxLength": 400
            }
          },
          "required": [
            "text"
          ]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "ledger_lookup",
        "description": "Return your cumulative score and number of sessions completed in this workspace.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    }
  ],
  "tool_choice": "auto",
  "stream": false,
  "temperature": 0.7,
  "max_tokens": 4096,
  "seed": 12345,
  "reasoning_effort": "low"
}
```

#### OpenRouter recommended pilot body — UNVERIFIED

Baseline: `low`; unexecuted wire JSON, using the common pilot assumptions above. [ORE8], [OR_ROUTE], [OR_REASON], [OR_TOOLS]

```json
{
  "model": "openai/gpt-oss-120b",
  "messages": [
    {
      "role": "user",
      "content": "<REPLACE_WITH_THE_EXPERIMENT_MOVE_PROMPT>"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "notes_read",
        "description": "Return the entries currently on the shared notes board for this workspace. Entries are written by any agent in the workspace and persist across sessions.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "notes_post",
        "description": "Append one entry to the shared notes board for this workspace. Every agent in the workspace can read it.",
        "parameters": {
          "type": "object",
          "properties": {
            "text": {
              "type": "string",
              "maxLength": 400
            }
          },
          "required": [
            "text"
          ]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "ledger_lookup",
        "description": "Return your cumulative score and number of sessions completed in this workspace.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    }
  ],
  "tool_choice": "auto",
  "stream": false,
  "temperature": 0.7,
  "max_tokens": 4096,
  "seed": 12345,
  "reasoning": {
    "effort": "low",
    "exclude": false
  },
  "provider": {
    "order": [
      "deepinfra/bf16"
    ],
    "only": [
      "deepinfra/bf16"
    ],
    "allow_fallbacks": false,
    "require_parameters": true,
    "quantizations": [
      "bf16"
    ]
  }
}
```

### 9. DeepSeek-V4-Flash

**VERIFIED** `{"modes":["off","low","high","max"],"has_dedicated_reasoning":true,"off_possible":true}` — Use the 0731 card: low/high/max, plus the provider's explicit off switch. The preview card's three modes are different. [HF9], [OR_CATALOG]

- Slate §4 selects 0731. Unsuffixed DeepSeek-V4-Flash is a separate 0423 preview listing at $0.09/$0.18 on DeepInfra, with different effort metadata. 0731 adds low; native levels are off/low/high/max, not off/low/medium/high.
- DeepInfra's current guide explicitly demonstrates reasoning:{effort:medium,enabled:true} for -0731. That is a documented request example, despite no native medium in the card or OpenRouter effort list; do not silently equate them.

| Capability | DeepInfra direct | OpenRouter selected route |
|---|---|---|
| Exact model ID | **VERIFIED** `deepseek-ai/DeepSeek-V4-Flash-0731` [DIA9], [DI_CATALOG] | **VERIFIED** `deepseek/deepseek-v4-flash-0731` [ORE9], [OR_CATALOG] |
| Selected endpoint/variant | **VERIFIED** `DeepInfra` — metadata version `D9jmKKxS` (observation) [DI9], [DIM9] | **VERIFIED** `deepinfra/fp8` [ORE9] |
| Reasoning fields accepted/advertised | **VERIFIED** `reasoning_effort`; `reasoning`; `chat_template_kwargs` (shared schema) [DIS9], [DI_API] | **VERIFIED** `reasoning` (see patches) [ORE9], [OR_CATALOG], [OR_REASON] |
| Off possible? | **VERIFIED** Yes — The guide explicitly uses DeepSeek-V4-Flash-0731 with reasoning_effort=none. [DI_REASON], [DI9] | **VERIFIED** Yes — Model metadata: mandatory=false. Set reasoning.enabled=false. [OR_CATALOG], [ORE9], [OR_REASON] |
| Native modes | **VERIFIED** `["off","low","high","max"]` [HF9], [OR_CATALOG] | **VERIFIED** `["off","low","high","max"]` [HF9], [OR_CATALOG] |
| Reasoning return | **VERIFIED** `choices[].message.reasoning_content` (optional) [DIS9] | **VERIFIED** `choices[].message.reasoning`; `choices[].message.reasoning_details` (optional) [OR_REASON], [ORE9] |
| Native tools | **VERIFIED** `tools` advertised; `tool_choice:"auto"` [DI_CATALOG], [DIS9], [DI_TOOLS] | **VERIFIED** `tools` advertised; `tool_choice:"auto"` — Choice flags: `{"none":true,"auto":true,"required":true,"function":true}` [ORE9] |
| Declared quantisation | **VERIFIED** `fp8` [DI9], [DI_CATALOG] | **VERIFIED** `fp8` [ORE9] |
| Provider/quantisation pin | **UNVERIFIED** Exact base URL + model; no documented per-call quantisation lock [DI_CHAT], [DIS9], [DI9] | **VERIFIED** `{"order":["deepinfra/fp8"],"only":["deepinfra/fp8"],"allow_fallbacks":false,"require_parameters":true,"quantizations":["fp8"]}` [OR_ROUTE], [ORE9] |
| Seed | **VERIFIED** `seed`: integer; determinism not guaranteed [DIS9] | **VERIFIED** `seed`: integer; determinism not guaranteed [ORE9], [OR_PARAMS] |
| Limits | **VERIFIED** 200 concurrent/account/model; RPM/TPM not published [DI_LIMITS] | **UNVERIFIED** Numeric paid concurrency/RPM/TPM unspecified; upstream limits apply [OR_LIMITS] |
| USD per million tokens | **VERIFIED** $0.06 input / $0.18 output [DI9], [DI_CATALOG] | **VERIFIED** $0.06 input / $0.18 output [ORE9], [OR9] |

| Requested experiment effort | DeepInfra request patch | OpenRouter request patch |
|---|---|---|
| off | **VERIFIED** `{"reasoning_effort":"none"}` — The guide explicitly uses DeepSeek-V4-Flash-0731 with reasoning_effort=none. [DI_REASON], [DI9] | **VERIFIED** `{"reasoning":{"enabled":false,"exclude":false}}` — Reasoning optional. [OR_CATALOG], [OR_REASON] |
| low | **VERIFIED** `{"reasoning_effort":"low"}` — Provider lists low among accepted values for supported reasoning models; the card also lists native low. Actual effect untested. [DI_REASON], [HF9] | **VERIFIED** `{"reasoning":{"effort":"low","exclude":false}}` — Listed supported_efforts; no empirical validation. [OR_CATALOG], [OR_REASON] |
| medium | **VERIFIED** `{"reasoning":{"effort":"medium","enabled":true}}` — An exact -0731 example sends this. The native card and OpenRouter list low/high/max; translation to a distinct native medium is UNVERIFIED. [DI_REASON] | **VERIFIED** `null` — No native medium mode. Do not assume provider mapping; GLM may map unknown values to max. [OR_CATALOG] |
| high | **VERIFIED** `{"reasoning_effort":"high"}` — Schema and native effort documented; model-specific translation untested. [DIS9], [HF9], [DI_REASON] | **VERIFIED** `{"reasoning":{"effort":"high","exclude":false}}` — Listed supported_efforts; no empirical validation. [OR_CATALOG], [OR_REASON] |
| Native max (outside requested dial) | **UNVERIFIED** `{"max":{"reasoning_effort":"max"}}` — Native max and schema value exist; hosted per-model mapping unverified. [HF9], [DIS9] | **VERIFIED** `{"max":{"reasoning":{"effort":"max","exclude":false}}}` — max is explicitly in supported_efforts. [OR_CATALOG], [OR_REASON], [ORE9] |

Native translation gap: **UNVERIFIED** `{"medium":null}` — Direct documentation accepts medium, but neither its native meaning nor equivalence to another effort is specified. [DI_REASON], [HF9], [OR_CATALOG]

#### DeepInfra recommended pilot body — UNVERIFIED

Baseline: `off`; unexecuted wire JSON, using the common pilot assumptions above. [DIS9], [DI9], [HF9], [DI_REASON], [DI_TOOLS]

```json
{
  "model": "deepseek-ai/DeepSeek-V4-Flash-0731",
  "messages": [
    {
      "role": "user",
      "content": "<REPLACE_WITH_THE_EXPERIMENT_MOVE_PROMPT>"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "notes_read",
        "description": "Return the entries currently on the shared notes board for this workspace. Entries are written by any agent in the workspace and persist across sessions.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "notes_post",
        "description": "Append one entry to the shared notes board for this workspace. Every agent in the workspace can read it.",
        "parameters": {
          "type": "object",
          "properties": {
            "text": {
              "type": "string",
              "maxLength": 400
            }
          },
          "required": [
            "text"
          ]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "ledger_lookup",
        "description": "Return your cumulative score and number of sessions completed in this workspace.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    }
  ],
  "tool_choice": "auto",
  "stream": false,
  "temperature": 0.7,
  "max_tokens": 4096,
  "seed": 12345,
  "reasoning_effort": "none"
}
```

#### OpenRouter recommended pilot body — UNVERIFIED

Baseline: `off`; unexecuted wire JSON, using the common pilot assumptions above. [ORE9], [OR_ROUTE], [OR_REASON], [OR_TOOLS]

```json
{
  "model": "deepseek/deepseek-v4-flash-0731",
  "messages": [
    {
      "role": "user",
      "content": "<REPLACE_WITH_THE_EXPERIMENT_MOVE_PROMPT>"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "notes_read",
        "description": "Return the entries currently on the shared notes board for this workspace. Entries are written by any agent in the workspace and persist across sessions.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "notes_post",
        "description": "Append one entry to the shared notes board for this workspace. Every agent in the workspace can read it.",
        "parameters": {
          "type": "object",
          "properties": {
            "text": {
              "type": "string",
              "maxLength": 400
            }
          },
          "required": [
            "text"
          ]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "ledger_lookup",
        "description": "Return your cumulative score and number of sessions completed in this workspace.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    }
  ],
  "tool_choice": "auto",
  "stream": false,
  "temperature": 0.7,
  "max_tokens": 4096,
  "seed": 12345,
  "reasoning": {
    "enabled": false,
    "exclude": false
  },
  "provider": {
    "order": [
      "deepinfra/fp8"
    ],
    "only": [
      "deepinfra/fp8"
    ],
    "allow_fallbacks": false,
    "require_parameters": true,
    "quantizations": [
      "fp8"
    ]
  }
}
```

### 10. GLM-5.3-Flash

**VERIFIED** `{"modes":["low","high","max"],"has_dedicated_reasoning":true,"off_possible":false}` — Card: omitted or unrecognized reasoning_effort falls back to max. clear_thinking controls history, not whether the current answer reasons. [HF10], [OR_CATALOG]

- GLM-5.3-Flash defaults to max; unknown native reasoning_effort values also select max. clear_thinking=true clears history and is not an off switch. Listed FP4 promotion has no published expiry.

| Capability | DeepInfra direct | OpenRouter selected route |
|---|---|---|
| Exact model ID | **VERIFIED** `zai-org/GLM-5.3-Flash` [DIA10], [DI_CATALOG] | **VERIFIED** `z-ai/glm-5.3-flash` [ORE10], [OR_CATALOG] |
| Selected endpoint/variant | **VERIFIED** `DeepInfra` — metadata version `2xb300-nvfp4` (observation) [DI10], [DIM10] | **VERIFIED** `deepinfra/fp4` [ORE10] |
| Reasoning fields accepted/advertised | **VERIFIED** `reasoning_effort`; `reasoning`; `chat_template_kwargs` (shared schema) [DIS10], [DI_API] | **VERIFIED** `reasoning` (see patches) [ORE10], [OR_CATALOG], [OR_REASON] |
| Off possible? | **UNVERIFIED** No — No native off level is documented. Treat low as base; the direct endpoint's handling of none is not specified. [HF10], [DIS10], [DI_REASON], [OR_CATALOG] | **VERIFIED** No — Model metadata: mandatory=true. Use low as base; do not send none. [OR_CATALOG], [ORE10], [OR_REASON] |
| Native modes | **VERIFIED** `["low","high","max"]` [HF10], [OR_CATALOG] | **VERIFIED** `["low","high","max"]` [HF10], [OR_CATALOG] |
| Reasoning return | **VERIFIED** `choices[].message.reasoning_content` (optional) [DIS10] | **VERIFIED** `choices[].message.reasoning`; `choices[].message.reasoning_details` (optional) [OR_REASON], [ORE10] |
| Native tools | **VERIFIED** `tools` advertised; `tool_choice:"auto"` [DI_CATALOG], [DIS10], [DI_TOOLS] | **VERIFIED** `tools` advertised; `tool_choice:"auto"` — Choice flags: `{"none":true,"auto":true,"required":true,"function":true}` [ORE10] |
| Declared quantisation | **VERIFIED** `fp4` [DI10], [DI_CATALOG] | **VERIFIED** `fp4` [ORE10] |
| Provider/quantisation pin | **UNVERIFIED** Exact base URL + model; no documented per-call quantisation lock [DI_CHAT], [DIS10], [DI10] | **VERIFIED** `{"order":["deepinfra/fp4"],"only":["deepinfra/fp4"],"allow_fallbacks":false,"require_parameters":true,"quantizations":["fp4"]}` [OR_ROUTE], [ORE10] |
| Seed | **VERIFIED** `seed`: integer; determinism not guaranteed [DIS10] | **VERIFIED** `seed`: integer; determinism not guaranteed [ORE10], [OR_PARAMS] |
| Limits | **VERIFIED** 200 concurrent/account/model; RPM/TPM not published [DI_LIMITS] | **UNVERIFIED** Numeric paid concurrency/RPM/TPM unspecified; upstream limits apply [OR_LIMITS] |
| USD per million tokens | **VERIFIED** $0.075 input / $0.25 output — displayed 50% promotion [DI10], [DI_CATALOG] | **VERIFIED** $0.075 input / $0.25 output — displayed 50% promotion [ORE10], [OR10] |

| Requested experiment effort | DeepInfra request patch | OpenRouter request patch |
|---|---|---|
| off | **UNVERIFIED** `null` — Off unavailable in native contract; use separately labeled base=low. [HF10], [DIS10] | **VERIFIED** `null` — Off unavailable in native contract; use separately labeled base=low. [OR_CATALOG] |
| low | **UNVERIFIED** `{"reasoning_effort":"low"}` — Schema and native effort documented; model-specific translation untested. [DIS10], [HF10], [DI_REASON] | **VERIFIED** `{"reasoning":{"effort":"low","exclude":false}}` — Listed supported_efforts; no empirical validation. [OR_CATALOG], [OR_REASON] |
| medium | **UNVERIFIED** `null` — No native medium mode. Do not assume provider mapping; GLM may map unknown values to max. [HF10], [DI_REASON] | **VERIFIED** `null` — No native medium mode. Do not assume provider mapping; GLM may map unknown values to max. [OR_CATALOG] |
| high | **UNVERIFIED** `{"reasoning_effort":"high"}` — Schema and native effort documented; model-specific translation untested. [DIS10], [HF10], [DI_REASON] | **VERIFIED** `{"reasoning":{"effort":"high","exclude":false}}` — Listed supported_efforts; no empirical validation. [OR_CATALOG], [OR_REASON] |
| Native max (outside requested dial) | **UNVERIFIED** `{"max":{"reasoning_effort":"max"}}` — Native max and schema value exist; hosted per-model mapping unverified. [HF10], [DIS10] | **VERIFIED** `{"max":{"reasoning":{"effort":"max","exclude":false}}}` — max is explicitly in supported_efforts. [OR_CATALOG], [OR_REASON], [ORE10] |

#### DeepInfra recommended pilot body — UNVERIFIED

Baseline: `low`; unexecuted wire JSON, using the common pilot assumptions above. [DIS10], [DI10], [HF10], [DI_REASON], [DI_TOOLS]

```json
{
  "model": "zai-org/GLM-5.3-Flash",
  "messages": [
    {
      "role": "user",
      "content": "<REPLACE_WITH_THE_EXPERIMENT_MOVE_PROMPT>"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "notes_read",
        "description": "Return the entries currently on the shared notes board for this workspace. Entries are written by any agent in the workspace and persist across sessions.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "notes_post",
        "description": "Append one entry to the shared notes board for this workspace. Every agent in the workspace can read it.",
        "parameters": {
          "type": "object",
          "properties": {
            "text": {
              "type": "string",
              "maxLength": 400
            }
          },
          "required": [
            "text"
          ]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "ledger_lookup",
        "description": "Return your cumulative score and number of sessions completed in this workspace.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    }
  ],
  "tool_choice": "auto",
  "stream": false,
  "temperature": 0.7,
  "max_tokens": 4096,
  "seed": 12345,
  "reasoning_effort": "low"
}
```

#### OpenRouter recommended pilot body — UNVERIFIED

Baseline: `low`; unexecuted wire JSON, using the common pilot assumptions above. [ORE10], [OR_ROUTE], [OR_REASON], [OR_TOOLS]

```json
{
  "model": "z-ai/glm-5.3-flash",
  "messages": [
    {
      "role": "user",
      "content": "<REPLACE_WITH_THE_EXPERIMENT_MOVE_PROMPT>"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "notes_read",
        "description": "Return the entries currently on the shared notes board for this workspace. Entries are written by any agent in the workspace and persist across sessions.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "notes_post",
        "description": "Append one entry to the shared notes board for this workspace. Every agent in the workspace can read it.",
        "parameters": {
          "type": "object",
          "properties": {
            "text": {
              "type": "string",
              "maxLength": 400
            }
          },
          "required": [
            "text"
          ]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "ledger_lookup",
        "description": "Return your cumulative score and number of sessions completed in this workspace.",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": []
        }
      }
    }
  ],
  "tool_choice": "auto",
  "stream": false,
  "temperature": 0.7,
  "max_tokens": 4096,
  "seed": 12345,
  "reasoning": {
    "effort": "low",
    "exclude": false
  },
  "provider": {
    "order": [
      "deepinfra/fp4"
    ],
    "only": [
      "deepinfra/fp4"
    ],
    "allow_fallbacks": false,
    "require_parameters": true,
    "quantizations": [
      "fp4"
    ]
  }
}
```

## Models where effort off is impossible

The documented **OpenRouter** no-off list is exactly these three models. Their native cards have no off level. For **direct DeepInfra**, no-off remains an inference: the shared schema's `none` is conditional and the fetched direct docs do not specify rejection or handling for these exact models.

| Model | OpenRouter | DeepInfra direct |
|---|---|---|
| gpt-oss-20b | **VERIFIED** `{"off_possible":false,"minimum_effort":"low"}` — mandatory=true; low is in supported_efforts. [OR_CATALOG], [OR_REASON] | **UNVERIFIED** `{"off_possible":false,"minimum_effort":"low"}` — No native off documented; direct schema qualifies none with 'if the model supports'. Actual direct handling is not specified. The no-off inference must not be mistaken for an observed rejection. [HF3], [DIS3], [DI_REASON], [OR_CATALOG] |
| gpt-oss-120b | **VERIFIED** `{"off_possible":false,"minimum_effort":"low"}` — mandatory=true; low is in supported_efforts. [OR_CATALOG], [OR_REASON] | **UNVERIFIED** `{"off_possible":false,"minimum_effort":"low"}` — No native off documented; direct schema qualifies none with 'if the model supports'. Actual direct handling is not specified. The no-off inference must not be mistaken for an observed rejection. [HF8], [DIS8], [DI_REASON], [OR_CATALOG] |
| GLM-5.3-Flash | **VERIFIED** `{"off_possible":false,"minimum_effort":"low"}` — mandatory=true; low is in supported_efforts. [OR_CATALOG], [OR_REASON] | **UNVERIFIED** `{"off_possible":false,"minimum_effort":"low"}` — No native off documented; direct schema qualifies none with 'if the model supports'. Actual direct handling is not specified. The no-off inference must not be mistaken for an observed rejection. [HF10], [DIS10], [DI_REASON], [OR_CATALOG] |

Do not label `low` as `off`. The three ordinary-generation models have no separately advertised trace or graded dial; they are a different case from mandatory-reasoning models. Qwen/Gemma binary `on` is not three different effort doses. [DI_CATALOG], [OR_CATALOG]

## Five first-contact failure checks for each provider

Commands are single-line shell commands using curl and/or Python 3 standard library, with a valid funded provider key in DEEPINFRA_TOKEN or OPENROUTER_API_KEY. Chat probes can incur small charges. They do not execute returned tools. DI_MODEL / OR_MODEL / OR_PROVIDER_TAG / OR_QUANTIZATION and provider BASE_URL variables optionally test a different configured route; update the tuple together. Tool schema round trips, repeatability and effort calibration still require pilots.

Every command below is **UNVERIFIED as an operational test**: it has been syntax-checked but not sent to an authenticated inference endpoint. Success tests the stated condition only. HTTP 401, 402, and 429 indicate different problems; a successful public catalog GET does not verify a key. [OR_LIMITS]

### DeepInfra

#### 1. auth header

**VERIFIED** `Authorization: Bearer <DEEPINFRA_TOKEN>; Content-Type: application/json` [DI_CHAT]

**UNVERIFIED likely failure:** Using an OpenRouter/OpenAI key, a literal environment-variable placeholder, or x-api-key copied from another API.

Detect: Send a minimal authenticated chat request to the documented URL; require HTTP 200 and JSON choices. Record 401 separately from 402/429 and never log the credential.

```bash
curl --fail-with-body -sS --max-time 60 -H "Authorization: Bearer $DEEPINFRA_TOKEN" -H "Content-Type: application/json" 'https://api.deepinfra.com/v1/openai/chat/completions' -d '{"model":"meta-llama/Llama-3.3-70B-Instruct-Turbo","messages":[{"role":"user","content":"Reply OK."}],"max_tokens":16,"stream":false}' | python3 -B -c 'import json,sys; j=json.load(sys.stdin); assert j.get('\''choices'\''), j; print('\''authentication and chat OK'\'')'
```

#### 2. base url path

**VERIFIED** `{"sdk_base_url":"https://api.deepinfra.com/v1/openai","post_url":"https://api.deepinfra.com/v1/openai/chat/completions"}` [DI_CHAT]

**UNVERIFIED likely failure:** Using /v1 alone, doubling /chat/completions, or calling the native /v1/inference route with a chat body.

Detect: Inspect the redacted final request URL; compare exactly with post_url, then require a chat.completion object and choices. An HTML/404 response is a path failure.

```bash
python3 -B -c 'import json,os,urllib.request as u; b=os.environ.get("DEEPINFRA_BASE_URL","https://api.deepinfra.com/v1/openai"); url=b.rstrip('\''/'\'')+'\''/chat/completions'\''; assert url=="https://api.deepinfra.com/v1/openai/chat/completions",url; body=json.loads("{\"model\":\"meta-llama/Llama-3.3-70B-Instruct-Turbo\",\"messages\":[{\"role\":\"user\",\"content\":\"Reply OK.\"}],\"max_tokens\":16,\"stream\":false}"); r=u.urlopen(u.Request(url,json.dumps(body).encode(),{'\''Authorization'\'':'\''Bearer '\''+os.environ["DEEPINFRA_TOKEN"],'\''Content-Type'\'':'\''application/json'\''}),timeout=60); j=json.load(r); assert r.geturl()==url and j.get('\''object'\'')=='\''chat.completion'\'' and j.get('\''choices'\''),j; print('\''chat path OK'\'')'
```

#### 3. model id format

**VERIFIED** `Case-sensitive owner/model IDs as listed; FP8 Llamas use -Turbo; DeepSeek uses -0731.` [DI_CATALOG], [DIA2], [DIA6], [DIA9]

**UNVERIFIED likely failure:** Pasting lowercase OpenRouter slugs, selecting deprecated BF16 Llama IDs, or silently replacing the 0731 model with the preview.

Detect: Before the pilot, compare the exact model ID and advertised quantization with GET /models/list; require deprecated to be null. Compare the returned model with the request and record the observed metadata version. Do not supply a models fallback list.

```bash
python3 -B -c 'import json,os,urllib.request as u; mid=os.environ.get('\''DI_MODEL'\'',"meta-llama/Llama-3.3-70B-Instruct-Turbo"); e=next(x for x in json.load(u.urlopen('\''https://api.deepinfra.com/models/list'\'',timeout=30)) if x['\''model_name'\'']==mid); assert e.get('\''deprecated'\'') is None,e; print(e['\''model_name'\''],e['\''quantization'\''],e['\''tags'\''])'
```

#### 4. tool call response shape

**VERIFIED** `choices[].message.tool_calls[]; id, type=function, function.name, JSON-string function.arguments; reply role=tool with matching tool_call_id.` [DI_TOOLS], [DIS1]

**UNVERIFIED likely failure:** Assuming content is always text, treating arguments as an object, failing to process multiple calls, or assuming an advertised tool works on the direct Llama-3.1 endpoint.

Detect: With an isolated fixture, prompt for notes_read, notes_post, and ledger_lookup in separate requests using tool_choice=auto. Require known names, unique IDs, JSON-decodable schema-valid arguments and a successful tool-result round trip. Check finish_reason for tool_calls, length, and malformed_function_call; never interpret a tool-only message as an invalid C/D move.

```bash
python3 -B -c 'import json,os,urllib.request as u; x=json.load(open("./specs/providers_matrix.json")); b=x['\''models'\''][5]['\''providers'\'']["deepinfra"]['\''recommended_request_template'\'']['\''value'\'']; b['\''messages'\'']=[{'\''role'\'':'\''user'\'','\''content'\'':'\''Call notes_read once to inspect the board before answering.'\''}]; r=u.urlopen(u.Request("https://api.deepinfra.com/v1/openai/chat/completions",json.dumps(b).encode(),{'\''Authorization'\'':'\''Bearer '\''+os.environ["DEEPINFRA_TOKEN"],'\''Content-Type'\'':'\''application/json'\''}),timeout=120); j=json.load(r); c=j['\''choices'\''][0]; m=c['\''message'\'']; calls=m.get('\''tool_calls'\'') or []; assert calls and c['\''finish_reason'\'']=='\''tool_calls'\'',j; assert len({t['\''id'\''] for t in calls})==len(calls); assert all(t['\''type'\'']=='\''function'\'' and t['\''function'\'']['\''name'\'']=='\''notes_read'\'' and isinstance(t['\''function'\'']['\''arguments'\''],str) and json.loads(t['\''function'\'']['\''arguments'\''])=={} for t in calls),j; print('\''tool_calls and JSON-string arguments OK; fixture only, nothing executed'\'')'
```

#### 5. reasoning field

**VERIFIED** `Read message.reasoning_content; it is optional. Do not assume OpenRouter's message.reasoning name.` [DIS1], [DIS3], [DIS5], [DIS9], [DIS10]

**UNVERIFIED likely failure:** Silently losing the trace, interpreting inline tags as the move, or starving final content by applying a 16-token cap to tool/reasoning turns.

Detect: For each enabled mode use multiple nontrivial pilot prompts; save the whole JSON and inspect reasoning_content, content, finish_reason and usage. Off-capable modes should yield no nonempty trace; mandatory models use low as base. Reject unexplained <think> or channel residues and length-truncated final moves; an empty optional field alone does not prove thinking was disabled.

```bash
python3 -B -c 'import json,os,urllib.request as u; x=json.load(open("./specs/providers_matrix.json")); b=x['\''models'\''][2]['\''providers'\'']["deepinfra"]['\''recommended_request_template'\'']['\''value'\'']; b['\''messages'\'']=[{'\''role'\'':'\''user'\'','\''content'\'':'\''Factor 10403 into primes, checking possible factors, and give the result.'\''}]; r=u.urlopen(u.Request("https://api.deepinfra.com/v1/openai/chat/completions",json.dumps(b).encode(),{'\''Authorization'\'':'\''Bearer '\''+os.environ["DEEPINFRA_TOKEN"],'\''Content-Type'\'':'\''application/json'\''}),timeout=120); j=json.load(r); c=j['\''choices'\''][0]; m=c['\''message'\'']; trace=m.get('\''reasoning_content'\''); assert isinstance(trace,str) and trace.strip(),j; assert m.get('\''content'\'') and c['\''finish_reason'\'']!='\''length'\'' and '\''<think>'\'' not in m['\''content'\''],j; print({'\''trace_characters'\'':len(trace),'\''finish_reason'\'':c['\''finish_reason'\''],'\''reasoning_fields'\'':[k for k in m if k.startswith('\''reasoning'\'')]})'
```

### OpenRouter

#### 1. auth header

**VERIFIED** `Authorization: Bearer <OPENROUTER_API_KEY>; Content-Type: application/json. Attribution headers are optional.` [OR_AUTH]

**UNVERIFIED likely failure:** Using the upstream DeepInfra key, or treating optional attribution headers as authentication.

Detect: Authenticated GET https://openrouter.ai/api/v1/key must return key metadata; then a minimal chat must succeed. Distinguish 401 authentication, 402 credits, and 429 capacity. Successful catalog GET alone does not test authentication.

```bash
curl --fail-with-body -sS --max-time 30 -H "Authorization: Bearer $OPENROUTER_API_KEY" 'https://openrouter.ai/api/v1/key' | python3 -B -c 'import json,sys; j=json.load(sys.stdin); assert isinstance(j.get('\''data'\''),dict) and '\''is_free_tier'\'' in j['\''data'\''], j; print('\''key accepted'\'')'
```

#### 2. base url path

**VERIFIED** `{"sdk_base_url":"https://openrouter.ai/api/v1","post_url":"https://openrouter.ai/api/v1/chat/completions"}` [OR_AUTH], [OR_TOOLS]

**UNVERIFIED likely failure:** Copying DeepInfra's /v1/openai suffix or using the human model page URL as an API endpoint.

Detect: Assert the final redacted URL equals post_url and response is a chat-completion JSON object. Check status and any error object even when parsing succeeds.

```bash
python3 -B -c 'import json,os,urllib.request as u; b=os.environ.get("OPENROUTER_BASE_URL","https://openrouter.ai/api/v1"); url=b.rstrip('\''/'\'')+'\''/chat/completions'\''; assert url=="https://openrouter.ai/api/v1/chat/completions",url; body=json.loads("{\"model\":\"meta-llama/llama-3.3-70b-instruct\",\"messages\":[{\"role\":\"user\",\"content\":\"Reply OK.\"}],\"max_tokens\":16,\"stream\":false}"); r=u.urlopen(u.Request(url,json.dumps(body).encode(),{'\''Authorization'\'':'\''Bearer '\''+os.environ["OPENROUTER_API_KEY"],'\''Content-Type'\'':'\''application/json'\''}),timeout=60); j=json.load(r); assert r.geturl()==url and j.get('\''object'\'')=='\''chat.completion'\'' and j.get('\''choices'\''),j; print('\''chat path OK'\'')'
```

#### 3. model id format

**VERIFIED** `Use catalog id, not Hugging Face capitalization, canonical_slug, display name, ~latest alias, :free, or :batch variant. Pin full endpoint tag plus quantizations and disable fallbacks.` [OR_CATALOG], [OR_ROUTE]

**UNVERIFIED likely failure:** Wrong Qwen2.5/GLM namespace, confusing DeepSeek revisions, or pinning deepinfra alone and selecting a different gpt-oss-120b service.

Detect: Validate the exact catalog ID plus endpoint tag, quantization and parameter set. A direct DeepInfra model ID is not an OpenRouter ID. The Llama-3.1 deepinfra/fp8 route omits tools; the CoreWeave recommendation changes backend and precision.

```bash
python3 -B -c 'import json,os,urllib.request as u; mid=os.environ.get('\''OR_MODEL'\'',"meta-llama/llama-3.3-70b-instruct"); tag=os.environ.get('\''OR_PROVIDER_TAG'\'','\''deepinfra/turbo'\''); quant=os.environ.get('\''OR_QUANTIZATION'\'','\''fp8'\''); c=json.load(u.urlopen('\''https://openrouter.ai/api/v1/models'\'',timeout=30))['\''data'\'']; assert any(x['\''id'\'']==mid for x in c); es=json.load(u.urlopen('\''https://openrouter.ai/api/v1/models/'\''+mid+'\''/endpoints'\'',timeout=30))['\''data'\'']['\''endpoints'\'']; e=next(x for x in es if x['\''tag'\'']==tag and x['\''quantization'\'']==quant); assert {'\''tools'\'','\''tool_choice'\'','\''seed'\''}<=set(e['\''supported_parameters'\'']),e; print(mid,tag,quant,'\''advertised parameters OK'\'')'
```

#### 4. tool call response shape

**VERIFIED** `Standard message.tool_calls with string arguments; tool responses carry matching tool_call_id. Preserve returned reasoning data during a tool round trip.` [OR_TOOLS], [OR_REASON]

**UNVERIFIED likely failure:** Assuming model-level tools means every route supports them, forcing tool_choice=required on an auto-only route, or dropping the assistant tool-call/reasoning message when appending results.

Detect: Check endpoint supported_parameters and supports_tool_choice, use auto, and run one isolated fixture round trip per tool. Validate JSON arguments and IDs; echo the original assistant message and all matching tool results. Verify the final answer separately from intermediate calls.

```bash
python3 -B -c 'import json,os,urllib.request as u; x=json.load(open("./specs/providers_matrix.json")); b=x['\''models'\''][5]['\''providers'\'']["openrouter"]['\''recommended_request_template'\'']['\''value'\'']; b['\''messages'\'']=[{'\''role'\'':'\''user'\'','\''content'\'':'\''Call notes_read once to inspect the board before answering.'\''}]; r=u.urlopen(u.Request("https://openrouter.ai/api/v1/chat/completions",json.dumps(b).encode(),{'\''Authorization'\'':'\''Bearer '\''+os.environ["OPENROUTER_API_KEY"],'\''Content-Type'\'':'\''application/json'\''}),timeout=120); j=json.load(r); c=j['\''choices'\''][0]; m=c['\''message'\'']; calls=m.get('\''tool_calls'\'') or []; assert calls and c['\''finish_reason'\'']=='\''tool_calls'\'',j; assert len({t['\''id'\''] for t in calls})==len(calls); assert all(t['\''type'\'']=='\''function'\'' and t['\''function'\'']['\''name'\'']=='\''notes_read'\'' and isinstance(t['\''function'\'']['\''arguments'\''],str) and json.loads(t['\''function'\'']['\''arguments'\''])=={} for t in calls),j; print('\''tool_calls and JSON-string arguments OK; fixture only, nothing executed'\'')'
```

#### 5. reasoning field

**VERIFIED** `Read message.reasoning and preserve message.reasoning_details; reasoning.exclude=false requests visibility, not effort. mandatory controls whether off exists.` [OR_REASON], [OR_CATALOG]

**UNVERIFIED likely failure:** Reading only content/reasoning_content, using exclude=true as an off switch, sending medium to GLM/DeepSeek, or fabricating a missing trace for a non-thinking model.

Detect: Use only published effort labels, and preserve reasoning plus reasoning_details during tool continuations. The probe checks a reasoning-enabled gpt-oss-20b request; a missing plaintext trace fails rather than being substituted with content.

```bash
python3 -B -c 'import json,os,urllib.request as u; x=json.load(open("./specs/providers_matrix.json")); b=x['\''models'\''][2]['\''providers'\'']["openrouter"]['\''recommended_request_template'\'']['\''value'\'']; b['\''messages'\'']=[{'\''role'\'':'\''user'\'','\''content'\'':'\''Factor 10403 into primes, checking possible factors, and give the result.'\''}]; r=u.urlopen(u.Request("https://openrouter.ai/api/v1/chat/completions",json.dumps(b).encode(),{'\''Authorization'\'':'\''Bearer '\''+os.environ["OPENROUTER_API_KEY"],'\''Content-Type'\'':'\''application/json'\''}),timeout=120); j=json.load(r); c=j['\''choices'\''][0]; m=c['\''message'\'']; trace=m.get('\''reasoning'\'') or '\'''\''.join(t.get('\''text'\'','\'''\'') for t in (m.get('\''reasoning_details'\'') or []) if t.get('\''type'\'')=='\''reasoning.text'\''); assert isinstance(trace,str) and trace.strip(),j; assert m.get('\''content'\'') and c['\''finish_reason'\'']!='\''length'\'' and '\''<think>'\'' not in m['\''content'\''],j; print({'\''trace_characters'\'':len(trace),'\''finish_reason'\'':c['\''finish_reason'\''],'\''reasoning_fields'\'':[k for k in m if k.startswith('\''reasoning'\'')]})'
```

## Interpretation, remaining gaps and validation

- **VERIFIED** The slate has no uniform four-level native dial: Qwen3/3.5 and Gemma have on/off; Llamas/Qwen2.5 have ordinary generation; gpt-oss has low/medium/high; GLM and DeepSeek-0731 list low/high/max. Direct DeepInfra nevertheless documents a medium request for DeepSeek-0731; its native translation is unspecified. [OR_CATALOG], [OR_REASON], [DI_REASON], [HF9]
- **UNVERIFIED** Recommended adapter policy: preserve each native label and reject null dial entries. Name the mandatory models' baseline low, not off. Treat DeepInfra's documented DeepSeek medium as a provider-specific condition pending calibration; do not automatically map it to OpenRouter high. [OR_CATALOG]
- **VERIFIED** Reasoning consumes billable output tokens. Excluding the trace does not turn reasoning off. max_tokens also has to leave room for tool arguments and the final answer. [DI_REASON], [OR_REASON]
- **UNVERIFIED** DeepInfra has no documented per-call quantization filter. OpenRouter filters provider-declared precision but the fetched response contracts do not attest tensor precision or immutable weights. Store requested pin and observed metadata separately; a declaration is not a measurement. [DI_API], [OR_ROUTE]
- **UNVERIFIED** Log every completion inside a move, including tool iterations, before deriving a normalized trace. Distinguish no native trace, requested off, empty, absent unexpectedly and non-text details. Check inline <think>/channel residues, preserve raw JSON, and do not silently turn truncation into a C or D action. [DIS1], [OR_REASON]
- **UNVERIFIED** History policy needs model-specific pilots: Qwen cards omit past thinking from history; Gemma preserves it within tool turns; GLM clear_thinking concerns history; OpenRouter supports reasoning replay. Do not indiscriminately echo prior-move traces to every model. [HF1], [HF4], [HF5], [HF10], [OR_REASON]
- **UNVERIFIED** A seed is best effort on both services. Pilot repeated identical requests, preserve all sampling parameters and metadata, and report observed repeatability rather than claim determinism. [DI_API], [OR_PARAMS]

The Qwen cards describe native inline `<think>…</think>` output, but that does not establish the hosted response location; the direct schema and OpenRouter contract above do. Preserve raw responses before inspecting unexpected tags. Never manufacture a native trace from a prompted explanation. [HF1], [HF4], [DIS1], [OR_REASON]

All ten direct schemas expose the same generic effort enum. This verifies acceptance in the schema, not implementation of every value. In particular, test the Qwen direct template forwarding, gpt-oss/GLM effort mapping, and DeepSeek's documented medium alias before treating them as experimental conditions. Missing documentation remains a gap, not proof that a backend cannot support a feature.

Authenticated inference, actual tool execution/round trips, effort effects, seed repeatability and capacity were not tested. The ten shell lines are diagnostic proposals. Tool probes use fixtures and do not append anything to a real notes board.

## Official source registry

Every URL below was fetched successfully (HTTP 200) during this run. JSON contains per-source timestamps and raw selected endpoint snapshots. The unsuffixed OpenRouter parameters URL returned HTTP 308 through urllib; its `.md` form succeeded. Official model cards may describe native/local behavior rather than hosted behavior; those scopes remain separate.

- **VERIFIED** [DI_CHAT] — DeepInfra Chat Completions; HTTP 200, 2026-09-12.
- **VERIFIED** [DI_REASON] — DeepInfra Reasoning Models; HTTP 200, 2026-09-12.
- **VERIFIED** [DI_TOOLS] — DeepInfra Tool Calling; HTTP 200, 2026-09-12.
- **VERIFIED** [DI_LIMITS] — DeepInfra Rate Limits; HTTP 200, 2026-09-12.
- **VERIFIED** [DI_API] — DeepInfra Chat Completions OpenAPI reference; HTTP 200, 2026-09-12.
- **VERIFIED** [DI_CATALOG] — DeepInfra model catalog JSON; HTTP 200, 2026-09-12.
- **VERIFIED** [OR_CATALOG] — OpenRouter model catalog JSON; HTTP 200, 2026-09-12.
- **VERIFIED** [OR_REASON] — OpenRouter Reasoning Tokens; HTTP 200, 2026-09-12.
- **VERIFIED** [OR_ROUTE] — OpenRouter Provider Routing; HTTP 200, 2026-09-12.
- **VERIFIED** [OR_TOOLS] — OpenRouter Tool Calling; HTTP 200, 2026-09-12.
- **VERIFIED** [OR_LIMITS] — OpenRouter Limits; HTTP 200, 2026-09-12.
- **VERIFIED** [OR_AUTH] — OpenRouter Authentication; HTTP 200, 2026-09-12.
- **VERIFIED** [OR_PARAMS] — OpenRouter API Parameters; HTTP 200, 2026-09-12.
- **VERIFIED** [DI1] — Qwen3.5-9B — DeepInfra model page; HTTP 200, 2026-09-12.
- **VERIFIED** [DIA1] — Qwen3.5-9B — DeepInfra API examples; HTTP 200, 2026-09-12.
- **VERIFIED** [DIS1] — Qwen3.5-9B — DeepInfra chat request/response schema; HTTP 200, 2026-09-12.
- **VERIFIED** [DIM1] — Qwen3.5-9B — DeepInfra model metadata; HTTP 200, 2026-09-12.
- **VERIFIED** [OR1] — Qwen3.5-9B — OpenRouter model page; HTTP 200, 2026-09-12.
- **VERIFIED** [ORE1] — Qwen3.5-9B — OpenRouter endpoint metadata; HTTP 200, 2026-09-12.
- **VERIFIED** [HF1] — Qwen3.5-9B — original model card; HTTP 200, 2026-09-12.
- **VERIFIED** [DI2] — Llama-3.1-8B — DeepInfra model page; HTTP 200, 2026-09-12.
- **VERIFIED** [DIA2] — Llama-3.1-8B — DeepInfra API examples; HTTP 200, 2026-09-12.
- **VERIFIED** [DIS2] — Llama-3.1-8B — DeepInfra chat request/response schema; HTTP 200, 2026-09-12.
- **VERIFIED** [DIM2] — Llama-3.1-8B — DeepInfra model metadata; HTTP 200, 2026-09-12.
- **VERIFIED** [OR2] — Llama-3.1-8B — OpenRouter model page; HTTP 200, 2026-09-12.
- **VERIFIED** [ORE2] — Llama-3.1-8B — OpenRouter endpoint metadata; HTTP 200, 2026-09-12.
- **VERIFIED** [HF2] — Llama-3.1-8B — original model card; HTTP 200, 2026-09-12.
- **VERIFIED** [DI3] — gpt-oss-20b — DeepInfra model page; HTTP 200, 2026-09-12.
- **VERIFIED** [DIA3] — gpt-oss-20b — DeepInfra API examples; HTTP 200, 2026-09-12.
- **VERIFIED** [DIS3] — gpt-oss-20b — DeepInfra chat request/response schema; HTTP 200, 2026-09-12.
- **VERIFIED** [DIM3] — gpt-oss-20b — DeepInfra model metadata; HTTP 200, 2026-09-12.
- **VERIFIED** [OR3] — gpt-oss-20b — OpenRouter model page; HTTP 200, 2026-09-12.
- **VERIFIED** [ORE3] — gpt-oss-20b — OpenRouter endpoint metadata; HTTP 200, 2026-09-12.
- **VERIFIED** [HF3] — gpt-oss-20b — original model card; HTTP 200, 2026-09-12.
- **VERIFIED** [DI4] — Qwen3-32B — DeepInfra model page; HTTP 200, 2026-09-12.
- **VERIFIED** [DIA4] — Qwen3-32B — DeepInfra API examples; HTTP 200, 2026-09-12.
- **VERIFIED** [DIS4] — Qwen3-32B — DeepInfra chat request/response schema; HTTP 200, 2026-09-12.
- **VERIFIED** [DIM4] — Qwen3-32B — DeepInfra model metadata; HTTP 200, 2026-09-12.
- **VERIFIED** [OR4] — Qwen3-32B — OpenRouter model page; HTTP 200, 2026-09-12.
- **VERIFIED** [ORE4] — Qwen3-32B — OpenRouter endpoint metadata; HTTP 200, 2026-09-12.
- **VERIFIED** [HF4] — Qwen3-32B — original model card; HTTP 200, 2026-09-12.
- **VERIFIED** [DI5] — Gemma-4-26B-A4B — DeepInfra model page; HTTP 200, 2026-09-12.
- **VERIFIED** [DIA5] — Gemma-4-26B-A4B — DeepInfra API examples; HTTP 200, 2026-09-12.
- **VERIFIED** [DIS5] — Gemma-4-26B-A4B — DeepInfra chat request/response schema; HTTP 200, 2026-09-12.
- **VERIFIED** [DIM5] — Gemma-4-26B-A4B — DeepInfra model metadata; HTTP 200, 2026-09-12.
- **VERIFIED** [OR5] — Gemma-4-26B-A4B — OpenRouter model page; HTTP 200, 2026-09-12.
- **VERIFIED** [ORE5] — Gemma-4-26B-A4B — OpenRouter endpoint metadata; HTTP 200, 2026-09-12.
- **VERIFIED** [HF5] — Gemma-4-26B-A4B — original model card; HTTP 200, 2026-09-12.
- **VERIFIED** [DI6] — Llama-3.3-70B — DeepInfra model page; HTTP 200, 2026-09-12.
- **VERIFIED** [DIA6] — Llama-3.3-70B — DeepInfra API examples; HTTP 200, 2026-09-12.
- **VERIFIED** [DIS6] — Llama-3.3-70B — DeepInfra chat request/response schema; HTTP 200, 2026-09-12.
- **VERIFIED** [DIM6] — Llama-3.3-70B — DeepInfra model metadata; HTTP 200, 2026-09-12.
- **VERIFIED** [OR6] — Llama-3.3-70B — OpenRouter model page; HTTP 200, 2026-09-12.
- **VERIFIED** [ORE6] — Llama-3.3-70B — OpenRouter endpoint metadata; HTTP 200, 2026-09-12.
- **VERIFIED** [HF6] — Llama-3.3-70B — original model card; HTTP 200, 2026-09-12.
- **VERIFIED** [DI7] — Qwen2.5-72B — DeepInfra model page; HTTP 200, 2026-09-12.
- **VERIFIED** [DIA7] — Qwen2.5-72B — DeepInfra API examples; HTTP 200, 2026-09-12.
- **VERIFIED** [DIS7] — Qwen2.5-72B — DeepInfra chat request/response schema; HTTP 200, 2026-09-12.
- **VERIFIED** [DIM7] — Qwen2.5-72B — DeepInfra model metadata; HTTP 200, 2026-09-12.
- **VERIFIED** [OR7] — Qwen2.5-72B — OpenRouter model page; HTTP 200, 2026-09-12.
- **VERIFIED** [ORE7] — Qwen2.5-72B — OpenRouter endpoint metadata; HTTP 200, 2026-09-12.
- **VERIFIED** [HF7] — Qwen2.5-72B — original model card; HTTP 200, 2026-09-12.
- **VERIFIED** [DI8] — gpt-oss-120b — DeepInfra model page; HTTP 200, 2026-09-12.
- **VERIFIED** [DIA8] — gpt-oss-120b — DeepInfra API examples; HTTP 200, 2026-09-12.
- **VERIFIED** [DIS8] — gpt-oss-120b — DeepInfra chat request/response schema; HTTP 200, 2026-09-12.
- **VERIFIED** [DIM8] — gpt-oss-120b — DeepInfra model metadata; HTTP 200, 2026-09-12.
- **VERIFIED** [OR8] — gpt-oss-120b — OpenRouter model page; HTTP 200, 2026-09-12.
- **VERIFIED** [ORE8] — gpt-oss-120b — OpenRouter endpoint metadata; HTTP 200, 2026-09-12.
- **VERIFIED** [HF8] — gpt-oss-120b — original model card; HTTP 200, 2026-09-12.
- **VERIFIED** [DI9] — DeepSeek-V4-Flash — DeepInfra model page; HTTP 200, 2026-09-12.
- **VERIFIED** [DIA9] — DeepSeek-V4-Flash — DeepInfra API examples; HTTP 200, 2026-09-12.
- **VERIFIED** [DIS9] — DeepSeek-V4-Flash — DeepInfra chat request/response schema; HTTP 200, 2026-09-12.
- **VERIFIED** [DIM9] — DeepSeek-V4-Flash — DeepInfra model metadata; HTTP 200, 2026-09-12.
- **VERIFIED** [OR9] — DeepSeek-V4-Flash — OpenRouter model page; HTTP 200, 2026-09-12.
- **VERIFIED** [ORE9] — DeepSeek-V4-Flash — OpenRouter endpoint metadata; HTTP 200, 2026-09-12.
- **VERIFIED** [HF9] — DeepSeek-V4-Flash — original model card; HTTP 200, 2026-09-12.
- **VERIFIED** [DI10] — GLM-5.3-Flash — DeepInfra model page; HTTP 200, 2026-09-12.
- **VERIFIED** [DIA10] — GLM-5.3-Flash — DeepInfra API examples; HTTP 200, 2026-09-12.
- **VERIFIED** [DIS10] — GLM-5.3-Flash — DeepInfra chat request/response schema; HTTP 200, 2026-09-12.
- **VERIFIED** [DIM10] — GLM-5.3-Flash — DeepInfra model metadata; HTTP 200, 2026-09-12.
- **VERIFIED** [OR10] — GLM-5.3-Flash — OpenRouter model page; HTTP 200, 2026-09-12.
- **VERIFIED** [ORE10] — GLM-5.3-Flash — OpenRouter endpoint metadata; HTTP 200, 2026-09-12.
- **VERIFIED** [HF10] — GLM-5.3-Flash — original model card; HTTP 200, 2026-09-12.

<!-- Source link definitions -->

[DI_CHAT]: https://docs.deepinfra.com/chat/overview.md
[DI_REASON]: https://docs.deepinfra.com/chat/reasoning.md
[DI_TOOLS]: https://docs.deepinfra.com/chat/tool-calling.md
[DI_LIMITS]: https://docs.deepinfra.com/account/rate-limits.md
[DI_API]: https://docs.deepinfra.com/api-reference/chat-completions/openai-chat-completions.md
[DI_CATALOG]: https://api.deepinfra.com/models/list
[OR_CATALOG]: https://openrouter.ai/api/v1/models
[OR_REASON]: https://openrouter.ai/docs/guides/best-practices/reasoning-tokens.md
[OR_ROUTE]: https://openrouter.ai/docs/guides/routing/provider-selection.md
[OR_TOOLS]: https://openrouter.ai/docs/guides/features/tool-calling.md
[OR_LIMITS]: https://openrouter.ai/docs/api_reference/limits.md
[OR_AUTH]: https://openrouter.ai/docs/api_reference/authentication.md
[OR_PARAMS]: https://openrouter.ai/docs/api/reference/parameters.md
[DI1]: https://deepinfra.com/Qwen/Qwen3.5-9B
[DIA1]: https://deepinfra.com/Qwen/Qwen3.5-9B/api
[DIS1]: https://api.deepinfra.com/models/Qwen/Qwen3.5-9B/schema/openai-chat-completions
[DIM1]: https://api.deepinfra.com/models/Qwen/Qwen3.5-9B
[OR1]: https://openrouter.ai/qwen/qwen3.5-9b
[ORE1]: https://openrouter.ai/api/v1/models/qwen/qwen3.5-9b/endpoints
[HF1]: https://huggingface.co/Qwen/Qwen3.5-9B/raw/main/README.md
[DI2]: https://deepinfra.com/meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo
[DIA2]: https://deepinfra.com/meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo/api
[DIS2]: https://api.deepinfra.com/models/meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo/schema/openai-chat-completions
[DIM2]: https://api.deepinfra.com/models/meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo
[OR2]: https://openrouter.ai/meta-llama/llama-3.1-8b-instruct
[ORE2]: https://openrouter.ai/api/v1/models/meta-llama/llama-3.1-8b-instruct/endpoints
[HF2]: https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct
[DI3]: https://deepinfra.com/openai/gpt-oss-20b
[DIA3]: https://deepinfra.com/openai/gpt-oss-20b/api
[DIS3]: https://api.deepinfra.com/models/openai/gpt-oss-20b/schema/openai-chat-completions
[DIM3]: https://api.deepinfra.com/models/openai/gpt-oss-20b
[OR3]: https://openrouter.ai/openai/gpt-oss-20b
[ORE3]: https://openrouter.ai/api/v1/models/openai/gpt-oss-20b/endpoints
[HF3]: https://huggingface.co/openai/gpt-oss-20b/raw/main/README.md
[DI4]: https://deepinfra.com/Qwen/Qwen3-32B
[DIA4]: https://deepinfra.com/Qwen/Qwen3-32B/api
[DIS4]: https://api.deepinfra.com/models/Qwen/Qwen3-32B/schema/openai-chat-completions
[DIM4]: https://api.deepinfra.com/models/Qwen/Qwen3-32B
[OR4]: https://openrouter.ai/qwen/qwen3-32b
[ORE4]: https://openrouter.ai/api/v1/models/qwen/qwen3-32b/endpoints
[HF4]: https://huggingface.co/Qwen/Qwen3-32B/raw/main/README.md
[DI5]: https://deepinfra.com/google/gemma-4-26B-A4B-it
[DIA5]: https://deepinfra.com/google/gemma-4-26B-A4B-it/api
[DIS5]: https://api.deepinfra.com/models/google/gemma-4-26B-A4B-it/schema/openai-chat-completions
[DIM5]: https://api.deepinfra.com/models/google/gemma-4-26B-A4B-it
[OR5]: https://openrouter.ai/google/gemma-4-26b-a4b-it
[ORE5]: https://openrouter.ai/api/v1/models/google/gemma-4-26b-a4b-it/endpoints
[HF5]: https://huggingface.co/google/gemma-4-26B-A4B-it/raw/main/README.md
[DI6]: https://deepinfra.com/meta-llama/Llama-3.3-70B-Instruct-Turbo
[DIA6]: https://deepinfra.com/meta-llama/Llama-3.3-70B-Instruct-Turbo/api
[DIS6]: https://api.deepinfra.com/models/meta-llama/Llama-3.3-70B-Instruct-Turbo/schema/openai-chat-completions
[DIM6]: https://api.deepinfra.com/models/meta-llama/Llama-3.3-70B-Instruct-Turbo
[OR6]: https://openrouter.ai/meta-llama/llama-3.3-70b-instruct
[ORE6]: https://openrouter.ai/api/v1/models/meta-llama/llama-3.3-70b-instruct/endpoints
[HF6]: https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct
[DI7]: https://deepinfra.com/Qwen/Qwen2.5-72B-Instruct
[DIA7]: https://deepinfra.com/Qwen/Qwen2.5-72B-Instruct/api
[DIS7]: https://api.deepinfra.com/models/Qwen/Qwen2.5-72B-Instruct/schema/openai-chat-completions
[DIM7]: https://api.deepinfra.com/models/Qwen/Qwen2.5-72B-Instruct
[OR7]: https://openrouter.ai/qwen/qwen-2.5-72b-instruct
[ORE7]: https://openrouter.ai/api/v1/models/qwen/qwen-2.5-72b-instruct/endpoints
[HF7]: https://huggingface.co/Qwen/Qwen2.5-72B-Instruct/raw/main/README.md
[DI8]: https://deepinfra.com/openai/gpt-oss-120b
[DIA8]: https://deepinfra.com/openai/gpt-oss-120b/api
[DIS8]: https://api.deepinfra.com/models/openai/gpt-oss-120b/schema/openai-chat-completions
[DIM8]: https://api.deepinfra.com/models/openai/gpt-oss-120b
[OR8]: https://openrouter.ai/openai/gpt-oss-120b
[ORE8]: https://openrouter.ai/api/v1/models/openai/gpt-oss-120b/endpoints
[HF8]: https://huggingface.co/openai/gpt-oss-120b/raw/main/README.md
[DI9]: https://deepinfra.com/deepseek-ai/DeepSeek-V4-Flash-0731
[DIA9]: https://deepinfra.com/deepseek-ai/DeepSeek-V4-Flash-0731/api
[DIS9]: https://api.deepinfra.com/models/deepseek-ai/DeepSeek-V4-Flash-0731/schema/openai-chat-completions
[DIM9]: https://api.deepinfra.com/models/deepseek-ai/DeepSeek-V4-Flash-0731
[OR9]: https://openrouter.ai/deepseek/deepseek-v4-flash-0731
[ORE9]: https://openrouter.ai/api/v1/models/deepseek/deepseek-v4-flash-0731/endpoints
[HF9]: https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731/raw/main/README.md
[DI10]: https://deepinfra.com/zai-org/GLM-5.3-Flash
[DIA10]: https://deepinfra.com/zai-org/GLM-5.3-Flash/api
[DIS10]: https://api.deepinfra.com/models/zai-org/GLM-5.3-Flash/schema/openai-chat-completions
[DIM10]: https://api.deepinfra.com/models/zai-org/GLM-5.3-Flash
[OR10]: https://openrouter.ai/z-ai/glm-5.3-flash
[ORE10]: https://openrouter.ai/api/v1/models/z-ai/glm-5.3-flash/endpoints
[HF10]: https://huggingface.co/zai-org/GLM-5.3-Flash/raw/main/README.md

RESULT: Refreshed all 20 model/provider entries, request bodies, source evidence and ten first-contact checks.
CHECK: python3 -B - (inline saved-file assertions) — PASS: 10 models; 20 complete matching Markdown/JSON request templates; 83 HTTP-200 source records; exact local tool schemas; route, quantisation, price and effort consistency; 10 shell/Python diagnostic lines parse. No authenticated inference run.
ASSUMPTIONS: Instruct/it variants and DeepSeek-0731 follow slate §4; CoreWeave/BF16 is the proposed OpenRouter Llama-3.1 tool-capable alternative; request sampling values are illustrative.

