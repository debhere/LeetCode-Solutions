select top 1 customer_number from Orders
group by customer_number
order by COUNT(order_number) DESC