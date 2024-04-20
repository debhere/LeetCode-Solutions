--Write a solution to find all the pairs (actor_id, director_id) where the actor has cooperated with the director at least three times.

--Return the result table in any order.

--The result format is in the following example.

select T.actor_id, T.director_id from
(select distinct actor_id, director_id, COUNT(timestamp) OVER(PARTITION BY actor_id, director_id) Cord
from ActorDirector) T
where Cord >=3