
select product_id, 
FIRST_VALUE(new_price) over(partition by product_id order by change_date desc) as price
from productss
where change_date <= '20190816'
UNION
select product_id, 10
from productss
group by product_id
having MIN(change_date) > '20190816'