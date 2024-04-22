
--Department Highest salary

select department, Employee, salary from
(select D.name department, E.name Employee, E.salary salary, MAX(E.salary) Over(Partition by D.name) MaxSalary
from Employee E join department D
on E.departmentid = D.id)T
where salary = MaxSalary