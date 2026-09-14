"""Small, dependency-light estimators. numpy only, so every number is auditable.

Design notes that matter for reading the output:
* Proportions here are proportions *of games*, never of rounds or of moves
  (README §3). The confirmatory replicate, though, is the sandbox, not the game
  (review-astra.md §2) - see the block section at the bottom of this file.
* Treatment (condition x effort x opponent mix) is assigned at the *sandbox*
  level, so permutation tests shuffle labels between sandboxes, not between
  games. That is the conservative choice: it respects what was randomised.
* Bootstraps resample sandboxes (clusters), not games, for the same reason,
  except where a game-level bootstrap is explicitly named.
"""
from __future__ import annotations

import numpy as np

Z95 = 1.959963984540054


def wilson_ci(k: int, n: int, z: float = Z95) -> tuple[float, float]:
    """Wilson score interval for a binomial proportion. (0,0) -> (0,1)."""
    if n <= 0:
        return (0.0, 1.0)
    p = k / n
    denom = 1.0 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = (z / denom) * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (float(max(0.0, centre - half)), float(min(1.0, centre + half)))


def cluster_bootstrap_mean_ci(values, clusters, n_boot: int = 2000, seed: int = 0,
                              alpha: float = 0.05) -> tuple[float, float]:
    """Percentile CI for the mean of `values`, resampling whole clusters."""
    values = np.asarray(values, dtype=float)
    if values.size == 0:
        return (float("nan"), float("nan"))
    clusters = np.asarray(clusters)
    uniq = np.unique(clusters)
    idx = {c: np.flatnonzero(clusters == c) for c in uniq}
    rng = np.random.default_rng(seed)
    draws = np.empty(n_boot)
    for b in range(n_boot):
        pick = rng.choice(uniq, size=uniq.size, replace=True)
        sel = np.concatenate([idx[c] for c in pick])
        draws[b] = values[sel].mean()
    return (float(np.quantile(draws, alpha / 2)), float(np.quantile(draws, 1 - alpha / 2)))


def cluster_bootstrap_diff_ci(values_a, clusters_a, values_b, clusters_b,
                              n_boot: int = 2000, seed: int = 0,
                              alpha: float = 0.05) -> tuple[float, float]:
    """Percentile CI for mean(a) - mean(b), resampling clusters within each arm."""
    va, vb = np.asarray(values_a, float), np.asarray(values_b, float)
    if va.size == 0 or vb.size == 0:
        return (float("nan"), float("nan"))
    ca, cb = np.asarray(clusters_a), np.asarray(clusters_b)
    ua, ub = np.unique(ca), np.unique(cb)
    ia = {c: np.flatnonzero(ca == c) for c in ua}
    ib = {c: np.flatnonzero(cb == c) for c in ub}
    rng = np.random.default_rng(seed)
    draws = np.empty(n_boot)
    for b in range(n_boot):
        pa = rng.choice(ua, size=ua.size, replace=True)
        pb = rng.choice(ub, size=ub.size, replace=True)
        draws[b] = va[np.concatenate([ia[c] for c in pa])].mean() - vb[np.concatenate([ib[c] for c in pb])].mean()
    return (float(np.quantile(draws, alpha / 2)), float(np.quantile(draws, 1 - alpha / 2)))


def permutation_p_grouped(values, groups, group_label, statistic, n_perm: int = 10000,
                          seed: int = 0, group_stratum=None) -> tuple[float, float, int]:
    """Two-sided permutation p for a group-level treatment.

    values          per-observation outcome (e.g. 1/0 channel use per game)
    groups          per-observation group id (the sandbox: the randomisation unit)
    group_label     dict group -> treatment label
    statistic       f(values, per_observation_labels) -> float
    group_stratum   optional dict group -> stratum; labels are shuffled only
                    within a stratum (keeps e.g. effort fixed while permuting mix)

    Returns (p, observed_statistic, n_perm_used).
    """
    values = np.asarray(values, dtype=float)
    groups = np.asarray(groups)
    uniq = list(dict.fromkeys(groups.tolist()))
    pos = {g: np.flatnonzero(groups == g) for g in uniq}
    labels_obs = np.empty(values.size, dtype=object)
    for g in uniq:
        labels_obs[pos[g]] = group_label[g]
    obs = statistic(values, labels_obs)
    if not np.isfinite(obs):
        return (float("nan"), float(obs), 0)

    strata: dict = {}
    for g in uniq:
        s = "ALL" if group_stratum is None else group_stratum[g]
        strata.setdefault(s, []).append(g)

    rng = np.random.default_rng(seed)
    count = 0
    for _ in range(n_perm):
        lab = np.empty(values.size, dtype=object)
        for s, gs in strata.items():
            perm = [group_label[g] for g in gs]
            rng.shuffle(perm)
            for g, l in zip(gs, perm):
                lab[pos[g]] = l
        t = statistic(values, lab)
        if np.isfinite(t) and abs(t) >= abs(obs) - 1e-12:
            count += 1
    p = (1.0 + count) / (n_perm + 1.0)
    return (float(p), float(obs), n_perm)


def linear_trend_statistic(scores: dict):
    """Statistic: slope of the cell means against ordered scores (per one step).

    With scores {off:0, low:1, high:2} on equally-spaced levels this is the
    ordinary least-squares slope through the three level means, i.e. the
    pre-registered ordered-trend contrast. Returns f(values, labels) -> float.
    """
    def stat(values, labels):
        levels = [l for l in scores if np.any(labels == l)]
        if len(levels) < 2:
            return float("nan")
        x = np.array([scores[l] for l in levels], dtype=float)
        y = np.array([values[labels == l].mean() for l in levels], dtype=float)
        x = x - x.mean()
        denom = float((x * x).sum())
        if denom == 0:
            return float("nan")
        return float((x * (y - y.mean())).sum() / denom)
    return stat


def mean_diff_statistic(label_a, label_b):
    """Statistic: mean(values | label_a) - mean(values | label_b)."""
    def stat(values, labels):
        a, b = values[labels == label_a], values[labels == label_b]
        if a.size == 0 or b.size == 0:
            return float("nan")
        return float(a.mean() - b.mean())
    return stat


def stratified_mean_diff_statistic(label_a, label_b, strata_of_obs):
    """Mean over strata of (mean_a - mean_b) within stratum."""
    strata_of_obs = np.asarray(strata_of_obs)
    uniq = list(dict.fromkeys(strata_of_obs.tolist()))

    def stat(values, labels):
        diffs = []
        for s in uniq:
            m = strata_of_obs == s
            a, b = values[m & (labels == label_a)], values[m & (labels == label_b)]
            if a.size and b.size:
                diffs.append(a.mean() - b.mean())
        return float(np.mean(diffs)) if diffs else float("nan")
    return stat


def pp(x: float) -> str:
    """Format a proportion as percentage points with one decimal and a sign."""
    return f"{100.0 * x:+.1f} pp" if np.isfinite(x) else "n/a"


def pct(x: float) -> str:
    return f"{100.0 * x:.1f}%" if np.isfinite(x) else "n/a"


def fmt_p(p: float, n_perm: int) -> str:
    """p never appears bare: it is always reported with its resolution."""
    if not np.isfinite(p):
        return "p n/a"
    floor = 1.0 / (n_perm + 1.0)
    if p <= floor + 1e-12:
        return f"p < {floor:.1e} (permutation floor, {n_perm} draws)"
    return f"p = {p:.4f} ({n_perm} permutation draws)"


def stratified_cluster_bootstrap_diff_ci(strata, labels, values, clusters, label_a, label_b,
                                         n_boot: int = 2000, seed: int = 0,
                                         alpha: float = 0.05) -> tuple[float, float]:
    """CI for the stratum-averaged difference mean(a) - mean(b), resampling
    clusters inside each stratum x arm. Matches the statistic used by the
    stratified permutation test, so the interval and the p value speak about the
    same quantity."""
    strata = np.asarray(strata)
    labels = np.asarray(labels)
    values = np.asarray(values, dtype=float)
    clusters = np.asarray(clusters)
    cells = {}
    for s in dict.fromkeys(strata.tolist()):
        entry = {}
        for lab in (label_a, label_b):
            m = (strata == s) & (labels == lab)
            cl = np.unique(clusters[m])
            entry[lab] = (cl, {c: np.flatnonzero(m & (clusters == c)) for c in cl})
        if len(entry[label_a][0]) and len(entry[label_b][0]):
            cells[s] = entry
    if not cells:
        return (float("nan"), float("nan"))
    rng = np.random.default_rng(seed)
    draws = np.empty(n_boot)
    for b in range(n_boot):
        diffs = []
        for s, entry in cells.items():
            arm = []
            for lab in (label_a, label_b):
                cl, idx = entry[lab]
                pick = rng.choice(cl, size=cl.size, replace=True)
                arm.append(values[np.concatenate([idx[c] for c in pick])].mean())
            diffs.append(arm[0] - arm[1])
        draws[b] = float(np.mean(diffs))
    return (float(np.quantile(draws, alpha / 2)), float(np.quantile(draws, 1 - alpha / 2)))


def cluster_bootstrap_did_ci(a1, c1, a0, c0, b1, d1, b0, d0, n_boot: int = 2000, seed: int = 0,
                             alpha: float = 0.05) -> tuple[float, float]:
    """CI for a difference in differences, (mean(a1)-mean(a0)) - (mean(b1)-mean(b0)),
    resampling clusters independently inside each of the four arms."""
    arms = []
    for v, c in ((a1, c1), (a0, c0), (b1, d1), (b0, d0)):
        v = np.asarray(v, dtype=float)
        c = np.asarray(c)
        if v.size == 0:
            return (float("nan"), float("nan"))
        u = np.unique(c)
        arms.append((v, u, {x: np.flatnonzero(c == x) for x in u}))
    rng = np.random.default_rng(seed)
    draws = np.empty(n_boot)
    for b in range(n_boot):
        m = []
        for v, u, idx in arms:
            pick = rng.choice(u, size=u.size, replace=True)
            m.append(v[np.concatenate([idx[x] for x in pick])].mean())
        draws[b] = (m[0] - m[1]) - (m[2] - m[3])
    return (float(np.quantile(draws, alpha / 2)), float(np.quantile(draws, 1 - alpha / 2)))


# --------------------------------------------------------------------------------
# Block-level (sandbox-as-replicate) inference. Added after the adversarial review
# (review-astra.md §2): games inside a sandbox share a board, agents and dyads, so
# they are not independent replicates. The randomisation unit is the sandbox and
# the confirmatory contrasts are paired differences between sandboxes inside a
# matched block.
# --------------------------------------------------------------------------------

def min_attainable_two_sided_p(k: int) -> float:
    """With k paired blocks a sign-flip test cannot go below 2^-(k-1).

    k=2 -> 0.5, k=3 -> 0.25, k=6 -> 0.03125. This is a resolution floor, not a
    power guarantee (review-astra.md §2), and every block verdict prints it.
    """
    return float(2.0 ** -(k - 1)) if k >= 1 else float("nan")


def sign_flip_test(diffs, n_perm: int = 0, seed: int = 0) -> dict:
    """Exact two-sided sign-flip (randomisation) test on paired block differences.

    Under the null that the treatment does nothing, the sign of each block's
    difference is exchangeable. With k <= 20 every one of the 2^k sign patterns
    is enumerated, so the p value is exact; above that, n_perm random patterns
    are drawn (n_perm defaults to 20000 in that case).
    """
    d = np.asarray([x for x in np.asarray(diffs, dtype=float) if np.isfinite(x)])
    k = d.size
    out = {"k": k, "mean": float(d.mean()) if k else float("nan"),
           "min_attainable_p": min_attainable_two_sided_p(k) if k else float("nan"),
           "n_positive": int((d > 0).sum()), "n_negative": int((d < 0).sum()),
           "exact": True, "diffs": d.tolist()}
    if k == 0:
        out.update({"p": float("nan"), "exact": False})
        return out
    obs = abs(d.mean())
    if k <= 20:
        total, count = 2 ** k, 0
        for mask in range(total):
            signs = np.array([1.0 if (mask >> i) & 1 else -1.0 for i in range(k)])
            if abs(float((signs * d).mean())) >= obs - 1e-12:
                count += 1
        out["p"] = count / total
    else:
        n_perm = n_perm or 20000
        rng = np.random.default_rng(seed)
        signs = rng.choice([-1.0, 1.0], size=(n_perm, k))
        count = int((np.abs((signs * d).mean(axis=1)) >= obs - 1e-12).sum())
        out["p"] = (1.0 + count) / (n_perm + 1.0)
        out["exact"] = False
        out["n_perm"] = n_perm
    return out


def block_bootstrap_ci(diffs, n_boot: int = 5000, seed: int = 0, alpha: float = 0.05) -> tuple[float, float]:
    """Percentile CI for the mean paired difference, resampling blocks.

    With a handful of blocks this interval is coarse; it is reported as a range,
    never as if it had the resolution of a game-level interval.
    """
    d = np.asarray([x for x in np.asarray(diffs, dtype=float) if np.isfinite(x)])
    if d.size == 0:
        return (float("nan"), float("nan"))
    rng = np.random.default_rng(seed)
    draws = rng.choice(d, size=(n_boot, d.size), replace=True).mean(axis=1)
    return (float(np.quantile(draws, alpha / 2)), float(np.quantile(draws, 1 - alpha / 2)))


def holm(pvalues: dict) -> dict:
    """Holm-Bonferroni adjustment within one declared confirmatory family."""
    items = [(k, v) for k, v in pvalues.items() if np.isfinite(v)]
    items.sort(key=lambda kv: kv[1])
    m = len(items)
    out, running = {}, 0.0
    for i, (k, p) in enumerate(items):
        adj = min(1.0, (m - i) * p)
        running = max(running, adj)     # enforce monotonicity
        out[k] = running
    for k, v in pvalues.items():
        out.setdefault(k, float("nan"))
    return out


def fmt_exact_p(res: dict) -> str:
    """p for a sign-flip test, always with its resolution floor stated."""
    p, k = res.get("p"), res.get("k", 0)
    if not np.isfinite(p):
        return "p n/a"
    kind = "exact sign-flip" if res.get("exact") else f"sampled sign-flip, {res.get('n_perm')} draws"
    return (f"p = {p:.4f} ({kind} over k = {k} blocks; smallest attainable two-sided p = "
            f"{res['min_attainable_p']:.5f})")
