select bid.client_number, sum(event_value.outcome = 'win') as win,
sum(event_value.outcome <> 'win') as lose
from test_sql_x_one.bid inner join test_sql_x_one.event_value
on test_sql_x_one.bid.play_id = test_sql_x_one.event_value.play_id and bid.coefficient = event_value.value
group by client_number
