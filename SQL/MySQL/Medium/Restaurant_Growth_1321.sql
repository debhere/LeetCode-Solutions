

with cte1 as
(
	select distinct visited_on,
	sum(amount) over(partition by visited_on order by visited_on) as totamount,
	DENSE_RANK() Over(order by visited_on) as rnk
	from Customer
),
cte2 as
(
	select visited_on,
	sum(totamount) over(order by visited_on rows between 6 preceding and current row) as amount,
	round(((sum(totamount) over(order by visited_on rows between 6 preceding and current row))/7.00), 2) as average_amount,
	rnk
	from cte1
)

select visited_on, amount, average_amount from cte2
where rnk >= 7
order by visited_on
