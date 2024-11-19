with deliv_extn as
(select customer_id, order_date,
case
	when DATEDIFF(order_date, customer_pref_delivery_date) = 0 then 'immediate'
	else 'scheduled'
	end as ordtype,
FIRST_VALUE(order_date) over(partition by customer_id order by order_date) as first_order,
count(customer_id) over(partition by customer_id) as totalorders
from delivery),
tblinter as
(select customer_id, count(case when ordtype = 'immediate' then customer_id end) as immdcount
from deliv_extn
where order_date = first_order
group by customer_id
)

select round(((sum(immdcount) * 1.00 / count(*)) * 100), 2) as immediate_percentage
from tblinter