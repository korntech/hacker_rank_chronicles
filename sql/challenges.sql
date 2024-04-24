WITH cte AS (
    SELECT h.hacker_id,
        h.name,
        COUNT(c.challenge_id) AS challenge_count
    FROM hackers h
        JOIN challenges c ON c.hacker_id = h.hacker_id
    GROUP BY h.hacker_id,
        h.name
),
max_count AS (
    SELECT MAX(challenge_count) AS max_challenge_count
    FROM cte
),
without_duplicates AS (
    SELECT a.*
    FROM cte a
    WHERE NOT EXISTS (
            SELECT 1
            FROM cte b
            WHERE a.challenge_count = b.challenge_count
                AND b.hacker_id != a.hacker_id
                AND a.challenge_count < (
                    SELECT max_challenge_count
                    FROM max_count
                )
        )
)
SELECT hacker_id,
    name,
    challenge_count
FROM without_duplicates
order by challenge_count desc,
    hacker_id