
select distinct id, num from
(select id, count(id) Over(Partition by id) num
from (select requester_id id from RequestAccepted
UNION ALL
select accepter_id from RequestAccepted)T) T2
where num = (select MAX(num) from
(select id, count(*) Over(Partition by id order by id desc) num
from
(select requester_id id from RequestAccepted
UNION ALL
select accepter_id from RequestAccepted)T)T2)