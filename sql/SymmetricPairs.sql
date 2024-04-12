WITH ranked_values AS (
    SELECT x AS rv_x,
        y AS rv_y,
        row_number() OVER (
            ORDER BY x
        ) AS row_num
    FROM functions
)
SELECT TOP 50 PERCENT sub.rv_x,
    sub.f_rv_x
FROM (
        SELECT rv.rv_x,
            f.rv_x AS f_rv_x,
            row_number() OVER (
                ORDER BY rv.rv_x
            ) AS ind
        FROM ranked_values rv
            JOIN ranked_values f ON rv.rv_x = f.rv_y
            AND rv.rv_y = f.rv_x
        WHERE rv.row_num != f.row_num
    ) AS sub
ORDER BY sub.ind;