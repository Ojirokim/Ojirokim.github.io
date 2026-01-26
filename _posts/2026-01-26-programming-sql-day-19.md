---
title: "Programming SQL Practice – Day 19 (5 Problems)"
date: 2026-01-26
categories: [코드-기술력-자료]
tags: [sql, programmers, daily-practice]
---

## 📅 Today’s Goal
- Solve 5 SQL problems of SQL questions
- Focus on correctness and query structure
A
---

## Problem 181 — Draw The Triangle 1
🔗 https://www.hackerrank.com/challenges/draw-the-triangle-1/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
set @star := 21;
select repeat('* ', @star := @star -1)
from information_schema.tables
limit 20
```
**Key Point**
- Used set to store the value of @star
- Used repeat function to generate the triangle
- Used information_schema.tables to get the number of rows


## Problem 182 — Draw The Triangle 2
🔗 https://www.hackerrank.com/challenges/draw-the-triangle-2/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
set @star := 0;
select repeat('* ', @star := @star +1)
from information_schema.tables
limit 20
```
**Key Point**
- Used set to store the value of @star
- Used repeat function to generate the triangle
- Used information_schema.tables to get the number of rows


## Problem 183 — Draw The Triangle 2
🔗 https://www.hackerrank.com/challenges/draw-the-triangle-2/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
set @star := 0;
select repeat('* ', @star := @star +1)
from information_schema.tables
limit 20
```
**Key Point**
- Used set to store the value of @star
- Used repeat function to generate the triangle
- Used information_schema.tables to get the number of rows


## Problem 184 — Print Prime Numbers
🔗 https://www.hackerrank.com/challenges/print-prime-numbers/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
WITH RECURSIVE seq AS (
  SELECT 2 AS n
  UNION ALL
  SELECT n + 1 FROM seq WHERE n < 1000
)
SELECT GROUP_CONCAT(n ORDER BY n SEPARATOR '&') AS primes
FROM seq p
WHERE NOT EXISTS (
  SELECT 1
  FROM seq d
  WHERE d.n BETWEEN 2 AND FLOOR(SQRT(p.n))
    AND MOD(p.n, d.n) = 0
)
```
**Key Point**
- Used recursive CTE to generate numbers
- Used GROUP_CONCAT to concatenate numbers
- Used MOD to check if the number is prime