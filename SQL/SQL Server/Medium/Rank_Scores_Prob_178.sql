
--Ranking scores

select score, DENSE_RANK() OVER(Order by score desc) rank from scores