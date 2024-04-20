--delete from person
--where id not in (select distinct MIN(id) OVER(PARTITION by email) from
--(select id, email, count(email) OVER(PARTITION BY email) as email_count
--from person) T)

delete from person
where id not in (select MIN(ID) from person
group by email)


delete p1 from person p1, person p2
where p1.email = p2.email
and p1.id > p2.id