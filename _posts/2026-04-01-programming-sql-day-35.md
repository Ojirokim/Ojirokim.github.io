---
title: "Programming SQL Practice – Day 35"
date: 2026-04-01
categories: [코드-기술력-자료]
tags: [sql, programmers, daily-practice]
---
---

## 📅 Today’s Goal
- Solve Coding test SQL problems
- Focus on correctness and query structure
---

## Problem 177 — Nth Highest Salary
🔗 https://leetcode.com/problems/nth-highest-salary/description/
```sql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
with distsal as(
select salary,
dense_rank()over(order by salary) dr
from employee
order by salary)
select 
distinct salary
from distsal
where dr = N
  );
END
```
**Key Point**
- Use 'dense_rank' to get the rank of each salary, then filter the result based on the Nth rank.

better solution
```sql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N = N - 1;
  RETURN (
      SELECT DISTINCT salary
      FROM Employee
      ORDER BY salary DESC
      LIMIT 1 OFFSET N
  );
END
```

## Problem 178. Rank Scores
🔗 https://leetcode.com/problems/nth-highest-salary/description/
```sql
select 
score,
dense_rank()over(order by score desc) `rank`
from scores
order by score desc
```

**Key Point**
- Use 'dense_rank' to get the rank of each score with ties.