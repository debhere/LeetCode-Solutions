--Write a solution to find the daily active user count for a period of 30 days ending 2019-07-27 inclusively. A user was active on someday if they made at least one activity on that day.

--Return the result table in any order.

-- User activity in past 30 days

select activity_date as day, count(distinct user_id) as active_users from Activity
group by activity_date
having activity_date between DATEADD(DAY,-29,'20190727') and '20190727'