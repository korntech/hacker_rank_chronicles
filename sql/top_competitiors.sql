--https://www.hackerrank.com/challenges/full-score/problem?isFullScreen=true
SELECT h.hacker_id,
    h.name
FROM submissions AS s
    JOIN hackers AS h ON s.hacker_id = h.hacker_id
    JOIN challenges AS c ON s.challenge_id = c.challenge_id
WHERE s.score = (
        SELECT score
        FROM difficulty
        WHERE difficulty_level = c.difficulty_level
    )
GROUP BY h.hacker_id,
    h.name
HAVING COUNT(s.submission_id) > 1
ORDER BY COUNT(s.submission_id) DESC,
    h.hacker_id ASC;