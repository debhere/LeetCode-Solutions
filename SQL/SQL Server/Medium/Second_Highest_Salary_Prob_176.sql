
--Second highest salary

select MAX(salary) SecondHighestSalary from 
(select *, DENSE_RANK() OVER(Order by salary desc) MyRank from Employee)T
where MyRank = 2