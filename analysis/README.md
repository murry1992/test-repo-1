## Mock dataset + avg aggregation (pandas vs SQL)

This folder contains a small deterministic dataset and two ways to compute the same aggregation:

1. `pandas_analysis.py` (uses `pandas`)
2. `sqlite_analysis.py` (loads the same CSV into SQLite and runs a SQL query)

Both outputs are formatted the same way (including rounding to 2 decimals), and `run_and_compare.py` asserts they match.

### Quick start

From the repo root:

```bash
pip3 install -r analysis/requirements.txt
python3 analysis/run_and_compare.py
```

If the assertion passes, you'll see the aggregated table printed once and a success message.

