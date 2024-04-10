/*
 Enter your query here.
 Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
 */
with salaries as (
    select s.id,
        s.name,
        p.salary,
        (
            select salary
            from packages
            where id = f.friend_id
        ) as friend_salary
    from students as s
        join friends as f on f.id = s.id
        join packages as p on p.id = s.id
)
select name
from salaries
where friend_salary > salary
order by friend_salary asc;