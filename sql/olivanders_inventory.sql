WITH cte AS (
    SELECT w.id,
        w.power,
        wp.code,
        wp.age,
        wp.is_evil,
        w.coins_needed,
        ROW_NUMBER() OVER (
            PARTITION BY w.power,
            wp.age
            ORDER BY w.power DESC,
                w.coins_needed ASC
        ) AS PriceRank
    FROM wands_property AS wp
        JOIN wands AS w ON w.code = wp.code
    WHERE wp.is_evil = 0
)
SELECT id,
    age,
    coins_needed,
    power
FROM cte
WHERE PriceRank = 1
ORDER BY power DESC,
    age DESC;