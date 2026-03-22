-- Same result as `avg_by_category_region.sql`,
-- but written using a CTE to demonstrate an alternative SQL style.

WITH grouped AS (
  SELECT
    category,
    region,
    AVG(value) AS avg_value_raw,
    COUNT(*) AS n
  FROM mock_data
  GROUP BY category, region
)
SELECT
  category,
  region,
  printf('%.2f', avg_value_raw) AS avg_value,
  n
FROM grouped
ORDER BY category, region;

