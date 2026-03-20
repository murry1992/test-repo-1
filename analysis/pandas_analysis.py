from __future__ import annotations

import pathlib
from typing import Any

import pandas as pd


def compute_avg_by_category_region(csv_path: str | pathlib.Path) -> list[dict[str, Any]]:
    """
    Compute the avg(value) and count per (category, region) using pandas.

    Output is stable and comparable:
    - `avg_value` is rounded to 2 decimals and formatted as a string with 2 decimals.
    - Rows are sorted by (category, region).
    """

    df = pd.read_csv(csv_path)

    grouped = (
        df.groupby(["category", "region"], as_index=False)
        .agg(avg_value=("value", "mean"), n=("value", "size"))
        .sort_values(["category", "region"], kind="stable")
    )

    # Format to a fixed 2-decimal string so pandas and SQL match exactly.
    grouped["avg_value"] = grouped["avg_value"].map(lambda x: f"{x:.2f}")

    # Convert to a JSON-friendly structure.
    return grouped.to_dict(orient="records")


if __name__ == "__main__":
    repo_root = pathlib.Path(__file__).resolve().parents[1]
    csv_path = repo_root / "analysis" / "mock_dataset.csv"
    rows = compute_avg_by_category_region(csv_path)
    print(rows)

