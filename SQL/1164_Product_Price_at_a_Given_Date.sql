# Write your MySQL query statement below
SELECT
    p1.product_id, 10 AS price
FROM
    Products p1
WHERE
    p1.product_id NOT IN (SELECT product_id FROM Products WHERE change_date <= '2019-08-16')
UNION
SELECT
    p2.product_id, p2.new_price as price
FROM
    Products p2
WHERE
    (p2.product_id, p2.change_date) IN
    (SELECT product_id, max(change_date) FROM Products WHERE change_date <= '2019-08-16' GROUP BY product_id)
