"""Recompute the headline numbers from the released compact tables and compare them
with the frozen report. Prints PASS or FAIL. Needs: pip install -e . (pandas, pyarrow).

Raw per-move logs (about 6 GB) are not in this repository; paper-analysis/code/extract.py
rebuilds the compact tables from them and is included for completeness."""
import runpy, sys, pathlib
root = pathlib.Path(__file__).resolve().parent
out = root / "paper-analysis" / "00-extraction-check.md"
runpy.run_path(str(root / "paper-analysis" / "code" / "check_extraction.py"), run_name="__main__")
text = out.read_text() if out.exists() else ""
ok = "PASS" in text and "NO" not in text.split("## Registered-family")[0]
print(text[-1500:])
print("\nRESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
