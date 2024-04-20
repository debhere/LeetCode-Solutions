
--Write a solution to find the average selling price for each product. average_price should be rounded to 2 decimal places.

--Return the result table in any order.



select distinct P.product_id,
ISNULL(cast(SUM((P.price * U.units)*1.00) OVER(PARTITION BY P.PRODUCT_ID)/SUM(U.units) OVER(PARTITION BY P.PRODUCT_ID) as decimal(6, 2)), 0) average_price
from Prices P left join UnitsSold U
on P.product_id = U.product_id
where U.purchase_date between P.start_date and P.end_date
or U.purchase_date is null




select P.product_id, isnull(cast(sum(P.price * U.units*1.00)/sum(u.units) as decimal(4,2)), 0) average_price
from Prices P left join UnitsSold U
on P.product_id = U.product_id
and u.purchase_date between P.start_date and P.end_date
group by P.product_id