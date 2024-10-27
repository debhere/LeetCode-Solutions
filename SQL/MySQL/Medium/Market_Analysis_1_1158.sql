
SELECT u.user_id AS buyer_id, u.join_date, count(o.order_id) as orders_in_2019

FROM Users u 
LEFT JOIN Orders o ON u.user_id = o.buyer_id
AND o.order_date like '2019%'
GROUP BY u.user_id, u.join_date