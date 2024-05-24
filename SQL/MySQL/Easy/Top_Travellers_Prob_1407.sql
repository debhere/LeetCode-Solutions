
select U.name, ifnull(sum(R.distance), 0)
travelled_distance from Users U left join Rides R
on U.id = R.user_id
group by U.name, U.id
order by travelled_distance desc, U.name asc;