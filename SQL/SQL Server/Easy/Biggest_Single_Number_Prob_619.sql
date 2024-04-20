

--A single number is a number that appeared only once in the MyNumbers table.

--Find the largest single number. If there is no single number, report null.

--The result format is in the following example.

-- Biggest Single Number

select top(1) case when count(*) = 1 then MAX(num) else NULL end as num from MyNumbers
group by num
order by num desc