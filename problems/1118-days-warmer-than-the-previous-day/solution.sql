-- your query
with cte as (
SELECT
recorded_on,
temperature,
lag(temperature) OVER (ORDER BY recorded_on) as prev_day_temp
FROM weather)

select
recorded_on
from cte
WHERE temperature > prev_day_temp
order by recorded_on