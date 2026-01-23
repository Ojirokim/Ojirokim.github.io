---
title: "Programming SQL Practice – Day 17 (5 Problems)"
date: 2026-01-22
categories: [코드-기술력-자료]
tags: [sql, programmers, daily-practice]
---

## 📅 Today’s Goal
- Solve 5 SQL problems of SQL questions
- Focus on correctness and query structure
A
---

## Problem 176 — SQL Project Planning
🔗 https://www.hackerrank.com/challenges/sql-projects/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT Start_Date, End_Date
from
(
SELECT Start_date, end_Date, DATEDIFF(b.End_Date, a.Start_Date) AS date_diff
FROM (
  SELECT Start_Date, ROW_NUMBER() OVER () AS rn
  FROM Projects
  where START_DATE not IN 
(SELECT End_Date 
FROM PROJECTS)
) a
JOIN (
  SELECT end_Date, ROW_NUMBER() OVER () AS rn
  FROM Projects
  where end_DATE not IN 
(SELECT start_Date 
FROM PROJECTS)
) b
ON a.rn = b.rn
) datedifftable
order by date_diff, start_Date
```
**Key Point**
- Used DATEDIFF() function to get the difference between two dates
- Used row_number() OVER() to get the row number
- Then used them to join two tables


## Problem 177 — Placements
🔗 https://www.hackerrank.com/challenges/placements/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
select s.name
from friends f
join packages p1
on f.ID = p1.ID
join packages p2
on f.Friend_id = p2.ID
join students s
on f.id = s.id
where p1.salary < p2.salary
order by p2.salary
```
**Key Point**
- Joined three tables to get the table with the highest salary
- Used the condition to get the table with the highest salary


## Problem 178 — Symmetric Pairs
🔗 https://www.hackerrank.com/challenges/symmetric-pairs/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT f1.X, f1.Y
FROM Functions f1
JOIN Functions f2
  ON f1.X = f2.Y
 AND f1.Y = f2.X
WHERE f1.X < f1.Y
UNION
SELECT X, Y
FROM Functions
GROUP BY X, Y
HAVING X = Y AND COUNT(*) > 1
ORDER BY X, Y;

```
**Key Point**
- Used UNION to get the symmetric pairs of the table
- Used GROUP BY and HAVING to get the table with the same value


## Problem 179 — Interviews
🔗 https://www.hackerrank.com/challenges/interviews/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT
  ct.contest_id,
  ct.hacker_id,
  ct.name,
  COALESCE(SUM(ss.total_submissions), 0) AS total_submissions,
  COALESCE(SUM(ss.total_accepted_submissions), 0) AS total_accepted_submissions,
  COALESCE(SUM(vs.total_views), 0) AS total_views,
  COALESCE(SUM(vs.total_unique_views), 0) AS total_unique_views
FROM contests ct
JOIN colleges co
ON ct.contest_id = co.contest_id
JOIN challenges ch
ON ch.college_id = co.college_id
LEFT JOIN (
  SELECT
    challenge_id,
    SUM(total_submissions) AS total_submissions,
    SUM(total_accepted_submissions) AS total_accepted_submissions
  FROM submission_stats
  GROUP BY challenge_id
) ss
  ON ss.challenge_id = ch.challenge_id
LEFT JOIN (
  SELECT
    challenge_id,
    SUM(total_views) AS total_views,
    SUM(total_unique_views) AS total_unique_views
  FROM view_stats
  GROUP BY challenge_id
) vs
  ON vs.challenge_id = ch.challenge_id
GROUP BY ct.contest_id, ct.hacker_id, ct.name
HAVING
    total_submissions
  + total_accepted_submissions
  + total_views
  + total_unique_views > 0
ORDER BY ct.contest_id;
```
**Key Point**
- Had to group the tables before joining them in order to get the correct result
- Used COALESCE() to check for null values.

## Problem 180 — 15 Days of Learning SQL
🔗 https://www.hackerrank.com/challenges/15-days-of-learning-sql/problem?isFullScreen=true
**Difficulty:** Level 6


