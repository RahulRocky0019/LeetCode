--Write your MySQL query statement below
select A.id as id 
from Weather A, Weather B
where datediff(A.recordDate, B.recordDate) = 1 and A.temperature > B.temperature
