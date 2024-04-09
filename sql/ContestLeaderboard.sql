/*
 Enter your query here.
 Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
 */
with hacker_cte as (
    select h.hacker_id,
        h.name,
        s.challenge_id,
        max(s.score) as max_score
    from hackers h
        join submissions as s on s.hacker_id = h.hacker_id
    group by s.challenge_id,
        h.hacker_id,
        h.name
)
select hacker_id,
    name,
    sum(max_score) as ms
from hacker_cte
group by hacker_id,
    name
HAVING SUM(max_score) > 0
order by ms desc,
    hacker_id asc