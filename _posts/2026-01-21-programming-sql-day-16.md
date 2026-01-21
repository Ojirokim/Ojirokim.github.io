---
title: "Programming SQL Practice – Day 16 (5 Problems)"
date: 2026-01-21
categories: [코드-기술력-자료]
tags: [sql, programmers, daily-practice]
---

## 📅 Today’s Goal
- Solve 5 SQL problems of SQL questions
- Focus on correctness and query structure
A
---

## Problem 166 — African Cities
🔗 https://www.hackerrank.com/challenges/african-cities/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT ci.name
from city ci
join country co
on ci.countrycode= co.code
where continent = 'Africa' 
```
**Key Point**
- join two tables then filter by condition


## Problem 167 — Average Population of Each Continent
🔗 https://www.hackerrank.com/challenges/average-population-of-each-continent/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT country.continent, floor(avg(city.population))
from city
join country
on CITY.CountryCode = COUNTRY.Code
group by 1
```
**Key Point**
- Joined two tables and calculated average population of each continent


## Problem 168 — Binary Tree Nodes
🔗 https://www.hackerrank.com/challenges/binary-search-tree-1/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT N,
CASE WHEN P IS NULL THEN 'Root'
when N NOT in (select p from BST WHERE P IS NOT NULL) Then 'Leaf'
else 'Inner' end
from BST
Order by N
```
**Key Point**
- Watch out for the NULL value in the P column inside the subquery


## Problem 169 — New Companies
🔗https://www.hackerrank.com/challenges/the-company/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
WITH
lm AS (
  SELECT company_code, COUNT(DISTINCT lead_manager_code) AS lead_cnt
  FROM lead_manager
  GROUP BY company_code
),
sm AS (
  SELECT company_code, COUNT(DISTINCT senior_manager_code) AS senior_cnt
  FROM senior_manager
  GROUP BY company_code
),
m AS (
  SELECT company_code, COUNT(DISTINCT manager_code) AS manager_cnt
  FROM manager
  GROUP BY company_code
),
e AS (
  SELECT company_code, COUNT(DISTINCT employee_code) AS emp_cnt
  FROM employee
  GROUP BY company_code
)
SELECT
  c.company_code,
  c.founder,
  COALESCE(lm.lead_cnt, 0),
  COALESCE(sm.senior_cnt, 0),
  COALESCE(m.manager_cnt, 0),
  COALESCE(e.emp_cnt, 0)
FROM company c
LEFT JOIN lm ON lm.company_code = c.company_code
LEFT JOIN sm ON sm.company_code = c.company_code
LEFT JOIN m  ON m.company_code  = c.company_code
LEFT JOIN e  ON e.company_code  = c.company_code
ORDER BY c.company_code;

```
**Key Point**
- Used CTE in order to avoid repetitive queries
- Coalesce function is used to avoid NULL values


## Problem 170 — Weather Observation Station 20
🔗 https://www.hackerrank.com/challenges/weather-observation-station-20/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT ROUND(AVG(LAT_N), 4)
FROM (
  SELECT
    LAT_N,
    @rownum := @rownum + 1 AS rn,
    @total := @rownum
  FROM STATION, (SELECT @rownum := 0) r
  ORDER BY LAT_N
) t
WHERE rn IN (FLOOR((@total + 1) / 2), FLOOR((@total + 2) / 2));

```
**Key Point**
- Using user-defined variables to calculate median


