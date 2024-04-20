--Write a solution to report the product_name, year, and price for each sale_id in the Sales table.

--Return the resulting table in any order.

--The result format is in the following example.

--Product analysis -1

select P.product_name, S.year, S.price from Sales S left join Product P
on S.product_id = P.product_id