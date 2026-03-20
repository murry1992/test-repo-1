from __future__ import annotations

import pathlib

from pandas_analysis import compute_avg_by_category_region as pandas_compute
from sqlite_analysis import compute_avg_by_category_region as sql_compute


def _stable_key(row: dict) -> tuple[str, str]:
    return (str(row["category"]), str(row["region"]))


def main() -> None:
    repo_root = pathlib.Path(__file__).resolve().parents[1]
    csv_path = repo_root / "analysis" / "mock_dataset.csv"
    sql_path = repo_root / "analysis" / "avg_by_category_region.sql"

    pandas_rows = pandas_compute(csv_path)
    sql_rows = sql_compute(csv_path, sql_path)

    # Sort deterministically by the grouping keys.
    pandas_rows = sorted(pandas_rows, key=_stable_key)
    sql_rows = sorted(sql_rows, key=_stable_key)

    # Ensure exact match for all fields (strings/numbers).
    assert pandas_rows == sql_rows, f"Mismatch!\nPandas: {pandas_rows}\nSQL: {sql_rows}"

    print(pandas_rows)
    print("OK: pandas vs SQL results match.")


if __name__ == "__main__":
    main()

