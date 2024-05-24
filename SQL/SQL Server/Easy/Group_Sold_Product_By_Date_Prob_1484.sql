select sell_date, count(product) num_sold, STRING_AGG(product, ',') as products
from (select distinct * from Activities) T
group by sell_date