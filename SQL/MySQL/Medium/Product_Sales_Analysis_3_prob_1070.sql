with sales_min_year as
(select product_id, min(year) min_year from sales
group by product_id
)


select t1.product_id, year as first_year, quantity, price 
	from sales t1 join product t2
	on t1.product_id = t2.product_id
where year = (select min_year from sales_min_year where product_id = t1.product_id)