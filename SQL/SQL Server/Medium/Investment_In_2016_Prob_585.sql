select round(sum(tiv_2016)*1.00,2) tiv_2016 from 
(select distinct *, count(lat) Over(Partition by lat, lon) loc,
count(tiv_2015) Over(Partition by tiv_2015) as count_tiv_2015
from Insurance)T
where loc = 1
and count_tiv_2015 > 1