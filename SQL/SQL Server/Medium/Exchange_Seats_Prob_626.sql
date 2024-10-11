select t1.id, case
	when t1.id % 2 = 0
	then (select student from Seat where id = t1.id - 1)
	when t1.id % 2 <> 0 and exists(select student from Seat where id = t1.id + 1)
	then (select student from Seat where id = t1.id + 1)
	else t1.student
	end as student
from Seat t1