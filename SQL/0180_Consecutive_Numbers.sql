# Write your MySQL query statement below
SELECT
    DISTINCT l1.num AS ConsecutiveNums
FROM
    Logs l1,
    Logs l2,
    Logs l3
WHERE
    l3.id = l2.id + 1 AND
    l3.id = l1.id + 2 AND
    l1.num = l2.num AND
    l1.num = l3.num
