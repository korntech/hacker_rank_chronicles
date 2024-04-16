WITH some_data AS (
    SELECT task_id,
        start_date,
        end_date,
        next_start_date,
        SUM(
            CASE
                WHEN datediff(day, previous_start_date, start_date) > 1 THEN 1
                ELSE 0
            END
        ) OVER (
            ORDER BY start_date
        ) AS group_id
    FROM (
            SELECT task_id,
                start_date,
                end_date,
                LAG(start_date) OVER (
                    ORDER BY start_date
                ) AS previous_start_date,
                LEAD(start_date) OVER (
                    ORDER BY start_date
                ) AS next_start_date
            FROM projects
        ) AS subquery
),
outer_cte AS (
    SELECT MIN(start_date) AS s_date,
        MAX(end_date) AS e_date,
        COUNT(*) AS duration
    FROM some_data
    GROUP BY group_id
)
SELECT s_date,
    e_date
FROM outer_cte
order by duration asc,
    s_date;