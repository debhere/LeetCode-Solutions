--Write an SQL query that reports the average experience years of all the employees for each project, rounded to 2 digits.

--Return the result table in any order.

--Project Employees I


select project_id, cast(cast(sum(experience_years) as numeric(6,2))/count(project_id) as decimal(6,2)) average_years 
from (select P.project_id, E.employee_id, E.experience_years from Employee E join Project P
on E.employee_id = P.employee_id
where E.experience_years is not null) T
group by project_id