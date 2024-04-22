
--We define query quality as:

--The average of the ratio between query rating and its position.

--We also define poor query percentage as:

--The percentage of all queries with rating less than 3.

--Write a solution to find each query_name, the quality and poor_query_percentage.

--Both quality and poor_query_percentage should be rounded to 2 decimal places.

--Return the result table in any order.

--The result format is in the following example.


select query_name, ROUND(AVG((rating+0.00)/position), 2) as quality, ROUND(SUM(case when rating < 3 then 1.00 else 0.00 end ) * 100/ COUNT(query_name), 2) as poor_query_percentage
from queries
where query_name is not NULL
group by  query_name


select query_name, cast(sum(Rating_Postion_ratio)/count(*) as decimal(6,2)) as quality,
cast((cast(sum(poor_query_count) as decimal(6,2))/count(*))*100 as decimal(6,2)) as poor_query_percentage
from (select query_name, rating, position,
cast(cast(rating as decimal(8,4))/position as decimal(8,4)) as Rating_Postion_ratio,
case when rating < 3 then 1 else 0 end as poor_query_count
from Queries) T
where query_name is not null
group by query_name