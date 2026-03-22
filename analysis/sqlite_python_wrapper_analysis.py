from __future__ import annotations

import csv
import pathlib
import sqlite3
from typing import Any


# SQL embedded directly in Python (no external .sql file).
SQL_QUERY = """
SELECT
  category,
  region,
  printf('%.2f', AVG(value)) AS avg_value,
  COUNT(*) AS n
FROM mock_data
GROUP BY category, region
ORDER BY category, region;
"""


def _load_csv_into_sqlite(conn: sqlite3.Connection, csv_path: str | pathlib.Path) -> None:
    conn.execute(
        """
        CREATE TABLE mock_data (
            category TEXT NOT NULL,
            region TEXT NOT NULL,
            value REAL NOT NULL
        )
        """
    )

    insert_sql = "INSERT INTO mock_data(category, region, value) VALUES (?, ?, ?)"

    with open(csv_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows: list[tuple[str, str, float]] = []
        for row in reader:
            rows.append((row["category"], row["region"], float(row["value"])))

    conn.executemany(insert_sql, rows)
    conn.commit()


def compute_avg_by_category_region(csv_path: str | pathlib.Path) -> list[dict[str, Any]]:
    csv_path = pathlib.Path(csv_path)

    conn = sqlite3.connect(":memory:")
    try:
        _load_csv_into_sqlite(conn, csv_path)

        conn.row_factory = sqlite3.Row
        cur = conn.execute(SQL_QUERY)
        return [dict(r) for r in cur.fetchall()]
    finally:
        conn.close()


if __name__ == "__main__":
    repo_root = pathlib.Path(__file__).resolve().parents[1]
    csv_path = repo_root / "analysis" / "mock_dataset.csv"
    rows = compute_avg_by_category_region(csv_path)
    print(rows)

