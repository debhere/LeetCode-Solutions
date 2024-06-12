

with cte_tbl as
(select t1.name as 'Name', t2.managerId,
count(t2.managerId) as NoOfReportees
from Employee t1 join Employee t2
on t1.id = t2.managerId
group by t2.managerId, t1.name)

select name from cte_tbl
where NoOfReportees >= 5