# Write your MySQL query statement below
SELECT 
    round((count(a1.player_id)/(SELECT count(DISTINCT player_id) FROM Activity)), 2) AS fraction
FROM 
    Activity a1 
WHERE
    (a1.player_id, DATE_SUB(a1.event_date, INTERVAL 1 DAY))
IN
    (
        SELECT
            a2.player_id, min(a2.event_date)
        FROM
            Activity a2
        GROUP BY
            a2.player_id
    )
