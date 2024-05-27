
select name, sum(amount) Balance from Users u join Transactions t
on u.account = t.account
group by name
having sum(amount) > 10000;