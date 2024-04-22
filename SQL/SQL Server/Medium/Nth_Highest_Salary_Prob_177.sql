
--NthHighestSalary

CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
        /* Write your T-SQL query statement below. */

		select MAX(salary) SecondHighestSalary from 
		(select *, DENSE_RANK() OVER(Order by salary desc) MyRank from Employee)T
		where MyRank = @N

    );
END