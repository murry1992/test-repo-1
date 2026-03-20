-- SQLite query for matching the pandas aggregation.
-- It computes AVG(value) and COUNT(*) per (category, region),
-- rounding AVG(value) to 2 decimals and formatting it as a string.

SELECT
  category,
  region,
  printf('%.2f', AVG(value)) AS avg_value,
  COUNT(*) AS n
FROM mock_data
GROUP BY category, region
ORDER BY category, region;

