
select sell_date, count(distinct product) num_sold, group_concat(distinct product order by product asc) products
from Activities
group by sell_date