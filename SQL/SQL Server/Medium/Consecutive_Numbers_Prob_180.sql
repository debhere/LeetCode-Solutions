
--Consecutive Numbers

select distinct num as ConsecutiveNums from 
		(select *, 
		case when num = LEAD(num) OVER(Order by (select null), id) and 
		num = Lag(num) OVER(Order by (select null), id) and 
		id = Lead(id) OVER(Order by id) - 1 and 
		id = Lag(id) OVER(Order by id) + 1
		then 1 else 0 end
as MyLead 
from Logs)T
where MyLead = 1


SELECT DISTINCT num AS ConsecutiveNums
FROM 
(
    SELECT num, 
    LAG(num) OVER (ORDER BY id) AS prev, 
    LEAD(num) OVER (ORDER BY id) AS next
    FROM Logs
) t
WHERE num = prev AND num = next
GROUP BY num;


SELECT distinct 
    i1.num as ConsecutiveNums 
FROM 
    logs i1,
    logs i2,
    logs i3
WHERE 
    i1.id=i2.id+1 AND 
    i2.id=i3.id+1 AND 
    i1.num=i2.num AND 
    i2.num=i3.num