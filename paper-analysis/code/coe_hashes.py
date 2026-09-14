import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Chain-of-evidence: PROVENANCE input hashes vs the freeze inventory vs disk now."""
import csv, hashlib, json, os, sys

T = _REPO+""
OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)

prov = json.load(open(f"{T}/reports/final-20260913T144509Z/PROVENANCE.json"))
inv = {}
with open(f"{T}/reports/FREEZE-20260913T144509Z-inventory.tsv") as f:
    for row in csv.DictReader(f, delimiter="\t"):
        inv[row["path"]] = row


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 22), b""):
            h.update(chunk)
    return h.hexdigest()


rows, disk_cache = [], {}
for sb in prov["sandboxes"]:
    path = sb["path"] + "/moves.jsonl"
    full = os.path.join(T, path)
    pm = sb["moves"]
    i = inv.get(path)
    if full not in disk_cache:
        disk_cache[full] = (sha(full), os.path.getsize(full)) if os.path.exists(full) else (None, None)
    d_sha, d_bytes = disk_cache[full]
    rows.append(dict(
        dataset=sb["dataset"], sandbox=sb["logical_sandbox"], path=path,
        disposition=sb["disposition"],
        prov_sha=pm["sha256"], prov_bytes=pm["bytes"], prov_lines=pm["lines"],
        inv_sha=(i or {}).get("sha256", "MISSING-FROM-INVENTORY"),
        inv_bytes=(i or {}).get("bytes", ""), inv_lines=(i or {}).get("lines", ""),
        disk_sha=d_sha or "MISSING-ON-DISK", disk_bytes=d_bytes,
        prov_vs_inv="OK" if i and i["sha256"] == pm["sha256"] else "MISMATCH",
        prov_vs_disk="OK" if d_sha == pm["sha256"] else "MISMATCH",
        inv_vs_disk="OK" if i and i["sha256"] == d_sha else "MISMATCH",
    ))

# inventory entries PROVENANCE never mentions
prov_paths = {r["path"] for r in rows}
for p, i in inv.items():
    if p in prov_paths:
        continue
    full = os.path.join(T, p)
    d_sha = sha(full) if os.path.exists(full) else None
    rows.append(dict(dataset="(inventory only)", sandbox=p.split("/")[-2], path=p,
                     disposition="not-in-PROVENANCE", prov_sha="", prov_bytes="", prov_lines="",
                     inv_sha=i["sha256"], inv_bytes=i["bytes"], inv_lines=i["lines"],
                     disk_sha=d_sha or "MISSING-ON-DISK", disk_bytes=os.path.getsize(full) if os.path.exists(full) else "",
                     prov_vs_inv="n/a", prov_vs_disk="n/a",
                     inv_vs_disk="OK" if i["sha256"] == d_sha else "MISMATCH"))

fn = os.path.join(OUT, "coe_hash_check.csv")
with open(fn, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)
n = len(rows)
for col in ("prov_vs_inv", "prov_vs_disk", "inv_vs_disk"):
    bad = [r for r in rows if r[col] == "MISMATCH"]
    print(col, "MISMATCH:", len(bad), [r["path"] for r in bad][:10])
print("files checked:", n, "->", fn)
