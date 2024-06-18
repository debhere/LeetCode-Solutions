select id, case 
		when id not in (select p_id from Tree where p_id is not null) and p_id is not null
		then 'Leaf'
		when p_id is null
		then 'Root'
		Else 'Inner'
		End as type
from Tree