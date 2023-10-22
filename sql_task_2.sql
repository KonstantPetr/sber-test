-- case

CREATE TABLE employee (
  id SERIAL PRIMARY KEY,
  name VARCHAR
);

CREATE TABLE sales (
  id SERIAL PRIMARY KEY,
  employee_id INTEGER,
  price INTEGER,
  FOREIGN KEY (employee_id) REFERENCES employee (id)
);

INSERT INTO employee (name) VALUES
('Petya'),
('Vasya'),
('Ksenia'),
('Yogg-Saron');

INSERT INTO sales (employee_id, price) VALUES
(1, 150),
(1, 80),
(1, 48),
(2, 100),
(2, 200),
(3, 55),
(3, 5),
(3, 79),
(3, 98),
(4, 50),
(4, 60),
(4, 70),
(4, 80),
(4, 90),
(4, 99);


-- query

WITH total_sales AS (
    SELECT
        employee_id,
        COUNT(*) AS sales_c,
        SUM(price) AS sales_s,
        RANK() OVER (ORDER BY COUNT(*) DESC) AS sales_rank_c,
        RANK() OVER (ORDER BY SUM(price) DESC) AS sales_rank_s
    FROM
        sales
    GROUP BY
        employee_id
)

SELECT
    e.id,
    e.name,
    ts.sales_c,
    ts.sales_rank_c,
    ts.sales_s,
    ts.sales_rank_s
FROM
    employee AS e
JOIN
    total_sales ts ON e.id = ts.employee_id
ORDER BY
    ts.sales_rank_c,
    ts.sales_rank_s;
