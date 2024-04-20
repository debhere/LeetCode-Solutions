select E.name as Employee from employee E, (select id, salary from Employee
where id in (select managerId from Employee)) T
where E.managerId = T.id
and E.salary>T.salary

--self join

select E.name as Employee from Employee E join Employee M
on E.managerId = M.id
where E.salary > M.salary