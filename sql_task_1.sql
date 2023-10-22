-- query

WITH RECURSIVE DateSequence AS (
  SELECT
    CURRENT_DATE AS generated_date,
    1 AS seq
  UNION ALL
  SELECT
    generated_date + FLOOR(RANDOM()::NUMERIC * 5 + 2)::INTEGER,
    seq + 1
  FROM DateSequence
  WHERE seq < 100
)
SELECT TO_CHAR(generated_date, 'dd.mm.YYYY') AS random_date
FROM DateSequence
