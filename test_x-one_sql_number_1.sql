select g.game, count(*) as games_count
from (select concat(least(event_entity.home_team, event_entity.away_team),
 '-', greatest(event_entity.home_team, event_entity.away_team)) as game
from test_sql_x_one.event_entity) as g
group by game
order by games_count

