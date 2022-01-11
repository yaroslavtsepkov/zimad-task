with ActiveUsers(event_date,active_users)
as (
  SELECT 
  date(event_time) as event_date
  ,COUNT(user_id) as active_users
  from events
  WHERE event_name == 'launch'
  GROUP by date(event_time)
  ),
IncomePerDay(event_date,sum_values)
as (
  SELECT
  date(event_time) as event_date
  ,SUM(event_value) as sum_values
  from events
  where event_name == 'purchase'
  GROUP by DATE(event_time)
  )
SELECT 
IncomePerDay.event_date
,IncomePerDay.sum_values / ActiveUsers.active_users as 'ARPDAU'
from IncomePerDay
inner join ActiveUsers
on IncomePerDay.event_date = ActiveUsers.event_date


