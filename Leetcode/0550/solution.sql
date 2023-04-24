SELECT ROUND( COUNT(t2.player_id) / COUNT(t1.player_id), 2 ) AS fraction
FROM (SELECT DISTINCT player_id
    , MIN(event_date) AS first_day
FROM activity
    GROUP BY player_id ) t1
    LEFT JOIN activity t2 ON t1.player_id = t2.player_id AND t1.first_day + 1 = t2.event_date