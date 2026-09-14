#!/usr/bin/env python3
"""Validate specs/sandboxes-v2 and derive the arithmetic the README quotes.

Deliberately NOT under coop/: this checks the spec files, it is not part of the runner.
Run:  python3 specs/sandboxes-v2/validate.py
"""
import os, sys, glob, itertools, yaml

HERE = os.path.dirname(os.path.abspath(__file__))

# --- v1 keys that must survive, plus the v2 additions -------------------------
V1_KEYS = ["sandbox", "population", "channel", "framing", "paraphrase",
           "reasoning_effort", "rounds_per_game", "prob_end", "generations",
           "seed", "provider", "base_url", "concurrency", "history_window",
           "neutral_labels"]
V2_KEYS = ["block", "reproduction", "board_initial", "assigned_state", "decoy_tool",
           "output_cap", "schedule", "primary_endpoint", "pin"]
REQUIRED = V1_KEYS + V2_KEYS
POP_KEYS = ["llm", "scripts", "total_agents"]

CHANNELS = ["absent", "permitted", "forbidden", "hidden"]
EFFORTS = ["off", "high"]
EFFORT_VALUE = {"off": "none", "high": "high"}   # DeepInfra field: none|low|high|max
STATES = ["ahead", "behind"]
BLOCKS = [f"B{k}" for k in range(1, 7)]
PARA = {"B1": "p1", "B2": "p1", "B3": "p2", "B4": "p2", "B5": "p3", "B6": "p3"}

errs, warns = [], []
def bad(f, m): errs.append(f"{f}: {m}")

block_files = sorted(glob.glob(os.path.join(HERE, "B[1-6]-*.yaml")))
ctrl_files = [os.path.join(HERE, n) for n in ("calibration-effort.yaml", "delivery-replay.yaml")]
docs, seeds = {}, {}

for path in block_files + ctrl_files:
    f = os.path.basename(path)
    try:
        d = yaml.safe_load(open(path))
    except Exception as e:
        bad(f, f"does not parse: {e}"); continue
    docs[f] = d
    for k in REQUIRED:
        if k not in d: bad(f, f"missing required key `{k}`")
    if isinstance(d.get("population"), dict):
        for k in POP_KEYS:
            if k not in d["population"]: bad(f, f"missing population.{k}")
    for k in ("mode", "ahead", "behind", "warmup_rounds", "warmup_opponent"):
        if k not in (d.get("assigned_state") or {}): bad(f, f"missing assigned_state.{k}")
    for k in ("preassigned", "shuffle_seed", "serialize_within_sandbox"):
        if k not in (d.get("schedule") or {}): bad(f, f"missing schedule.{k}")
    for k in ("answer_tokens", "reasoning_budget"):
        if k not in (d.get("output_cap") or {}): bad(f, f"missing output_cap.{k}")
    if (d.get("pin") or {}).get("quantisation") != "fp8": bad(f, "pin.quantisation is not fp8")
    if d.get("provider") != "deepinfra": bad(f, "provider is not `deepinfra`")
    if d.get("base_url") != "https://api.deepinfra.com/v1/openai": bad(f, "wrong base_url")
    if d.get("framing") != "F0": bad(f, "framing is not F0")
    if d.get("generations") != 1: bad(f, "generations is not 1")
    if (d.get("reproduction") or {}).get("rule") != "none": bad(f, "reproduction.rule is not none")
    if d.get("decoy_tool") != "workspace_clock": bad(f, "decoy_tool is not workspace_clock")
    if "deepseek-ai/DeepSeek-V4-Flash-0731" not in (d.get("population") or {}).get("llm", {}): bad(f, "primary model absent")
    if (d.get("output_cap") or {}).get("answer_tokens") != 768: bad(f, "answer_tokens != 768")
    s = d.get("seed")
    if s in seeds: bad(f, f"seed {s} already used by {seeds[s]}")
    seeds[s] = f
    if d.get("schedule", {}).get("shuffle_seed") != s: bad(f, "shuffle_seed != seed")
    if d.get("sandbox") != f[:-5]: bad(f, "sandbox id does not match filename")

# --- block completeness -------------------------------------------------------
expected = {f"{b}-{c}-{e}-{s}.yaml" for b in BLOCKS
            for c, e, s in itertools.product(CHANNELS, EFFORTS, STATES)}
got = {os.path.basename(p) for p in block_files}
for f in sorted(expected - got): bad(f, "MISSING from the design")
for f in sorted(got - expected): bad(f, "not part of the 96-file design")

for f in sorted(got & expected):
    d, (b, c, e, s) = docs[f], f[:-5].split("-")
    if d.get("block") != b: bad(f, "block key disagrees with filename")
    if d.get("channel") != c: bad(f, "channel disagrees with filename")
    if str(d.get("reasoning_effort")) != EFFORT_VALUE[e]: bad(f, "reasoning_effort disagrees with filename")
    if d.get("assigned_state", {}).get("arm") != s: bad(f, "assigned_state.arm disagrees with filename")
    if d.get("paraphrase") != PARA[b]: bad(f, f"paraphrase should be {PARA[b]}")
    want = 0 if e == "off" else 12288
    if d.get("output_cap", {}).get("reasoning_budget") != want: bad(f, f"reasoning_budget should be {want}")

# --- controls -----------------------------------------------------------------
cal = docs.get("calibration-effort.yaml", {})
if cal.get("reasoning_effort") != ["none", "low", "high", "max"]: bad("calibration-effort.yaml", "four effort levels expected")
if cal.get("states", {}).get("count") != 30: bad("calibration-effort.yaml", "30 states expected")
if cal.get("calls", {}).get("probes") != 30 * 4: bad("calibration-effort.yaml", "probes != 30 x 4")
del_ = docs.get("delivery-replay.yaml", {})
if del_.get("states", {}).get("count") != 30: bad("delivery-replay.yaml", "30 recipient states expected")
if [a["id"] for a in del_.get("message_arms", [])] != ["real", "randomised"]: bad("delivery-replay.yaml", "two message arms expected")
if del_.get("calls", {}).get("probes") != 60: bad("delivery-replay.yaml", "probes != 30 x 2")

# --- arithmetic ---------------------------------------------------------------
N_LLM, N_SCR, CAP, PEND = 12, 12, 30, 0.03
llm_llm = N_LLM * (N_LLM - 1) // 2            # 66
llm_scr = N_LLM * N_SCR                        # 144
llm_games = llm_llm + llm_scr                  # 210 = the primary endpoint denominator
dec_cap = llm_llm * CAP * 2 + llm_scr * CAP    # 8,280 billable decisions at the cap
exp_rounds = (1 - (1 - PEND) ** CAP) / PEND    # 19.966
frac = exp_rounds / CAP
dec_exp = dec_cap * frac
TOOL_RATE, CONT = 0.10, 1                      # <=10% of decisions open a tool; 1 continuation each
# Token model. Prompt 450/decision. Output: the OFF arm is capped at 64 answer tokens
# (first contact measured 44). The HIGH arm is the MEASURED DeepSeek-V4-Flash figure from
# first contact: 930 completion tokens at reasoning_effort=high.
PROMPT_TOK, ANS_TOK, REAS_TOK = 450, 64, 930 - 64
PIN, POUT = 0.06 / 1e6, 0.18 / 1e6             # DeepSeek-V4-Flash-0731 fp8 on DeepInfra

def sandbox_calls(channel, effort):
    cont = dec_exp * TOOL_RATE * CONT if channel != "absent" else dec_exp * TOOL_RATE * CONT
    return dec_exp + cont                      # decoy is listed in every condition
def sandbox_cost(effort, calls):
    out = ANS_TOK if effort == "off" else ANS_TOK + REAS_TOK
    return calls * PROMPT_TOK * PIN + calls * out * POUT

blk_calls = blk_cost = 0.0
for c, e, s in itertools.product(CHANNELS, EFFORTS, STATES):
    k = sandbox_calls(c, e); blk_calls += k; blk_cost += sandbox_cost(e, k)
ctrl_calls = 120 + 60
ctrl_cost = sandbox_cost("high", 120) + sandbox_cost("off", 60)
tot_calls = 6 * blk_calls + ctrl_calls
tot_cost = 6 * blk_cost + ctrl_cost
# sensitivity: high-effort reasoning runs 900 tokens rather than 450
REAS_TOK = 4096
blk_cost_hi = sum(sandbox_cost(e, sandbox_calls(c, e)) for c, e, s in itertools.product(CHANNELS, EFFORTS, STATES))

print("=" * 78)
print(f"files parsed            {len(docs):>10}   (96 block + 2 control)")
print(f"unique seeds            {len(seeds):>10}")
print("-" * 78)
print(f"LLM-involving games / sandbox      {llm_games:>10,}   (66 LLM-LLM + 144 LLM-script)")
print(f"billable decisions at cap          {dec_cap:>10,}")
print(f"expected realised rounds           {exp_rounds:>10.3f}   of a 30 cap at prob_end 0.03")
print(f"billable decisions expected        {dec_exp:>10,.0f}   ({frac:.4f} x cap)")
print(f"tool continuations expected        {dec_exp*TOOL_RATE:>10,.0f}   (<=10% of decisions, 1 each)")
print(f"end-question calls                 {0:>10}   cut: no in-game classification or recall")
print(f"calls / sandbox                    {sandbox_calls('forbidden','off'):>10,.0f}")
print(f"calls / block (16 sandboxes)       {blk_calls:>10,.0f}")
print(f"calls / six blocks                 {6*blk_calls:>10,.0f}")
print(f"calls / controls                   {ctrl_calls:>10,}   (120 calibration + 60 delivery)")
print(f"calls TOTAL                        {tot_calls:>10,.0f}")
print("-" * 78)
print(f"cost / block   $ {blk_cost:>8,.2f}")
print(f"cost six blocks + controls  $ {tot_cost:>8,.2f}   450 prompt / 64 answer / 866 reasoning (measured)")
print(f"sensitivity: reasoning 4096 tok     $ {6*blk_cost_hi+ctrl_cost:>8,.2f}   (high arm saturates its budget)")
print(f"resolution floor: two-sided sign test, 6 paired blocks, all one way ->")
print(f"                  p = 2 x 2^-6 = 2^-5 = {2*2**-6:.5f}   (2 blocks: 0.5; 3 blocks: 0.25)")
print("=" * 78)
if warns: print("WARNINGS:"); [print("  ", w) for w in warns]
if errs:
    print(f"FAIL: {len(errs)} problem(s)"); [print("  ", e) for e in errs]; sys.exit(1)
print("PASS: all 98 files parse; all required keys present; design complete and seeds unique.")
