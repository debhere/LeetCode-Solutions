
select user_id, max(time_stamp) as last_stamp
from Logins
where time_stamp between '2020-01-01' and '2020-12-31 23:59:59'
group by user_id


--With Statement will be high on execution time

with my_table as
(select user_id, time_stamp from Logins
having year(time_stamp) = 2020)

select user_id, max(time_stamp) as last_stamp
from my_table
group by user_id;