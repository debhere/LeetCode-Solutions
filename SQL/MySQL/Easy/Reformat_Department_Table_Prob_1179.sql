select id,
MAX((case when month='Jan' then revenue else null end)) as Jan_Revenue,
MAX((case when month='Feb' then revenue else null end)) as Feb_Revenue,
MAX((case when month='Mar' then revenue else null end)) as Mar_Revenue,
MAX((case when month='Apr' then revenue else null end)) as Apr_Revenue,
MAX((case when month='May' then revenue else null end)) as May_Revenue,
MAX((case when month='Jun' then revenue else null end)) as Jun_Revenue,
MAX((case when month='Jul' then revenue else null end)) as Jul_Revenue,
MAX((case when month='Aug' then revenue else null end)) as Aug_Revenue,
MAX((case when month='Sep' then revenue else null end)) as Sep_Revenue,
MAX((case when month='Oct' then revenue else null end)) as Oct_Revenue,
MAX((case when month='Nov' then revenue else null end)) as Nov_Revenue,
MAX((case when month='Dec' then revenue else null end)) as Dec_Revenue
from Department
group by id
order by id