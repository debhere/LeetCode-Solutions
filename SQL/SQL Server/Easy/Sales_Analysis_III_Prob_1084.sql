
--Write a solution to report the products that were only sold in the first quarter of 2019. That is, between 2019-01-01 and 2019-03-31 inclusive.

--Return the result table in any order.

--Sales Analysis III

select distinct S.product_id, P.product_name, S.sale_date from Sales S join Product P
on S.product_id = P.product_id
where sale_date between '20190101' and '20190331'
and S.product_id not in (Select S.product_id from Sales S where sale_date > '20190331' 
or sale_date < '20190101')

SELECT p.product_id, p.product_name
FROM Product AS p
JOIN Sales AS s
ON p.product_id = s.product_id
GROUP BY p.product_id, p.product_name
HAVING MIN(s.sale_date) >= '2019-01-01' AND MAX(s.sale_date) <= '2019-03-31'