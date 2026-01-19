---
title: "Programming SQL Practice – Day 14 (10 Problems)"
date: 2026-01-19
categories: [코드-기술력-자료]
tags: [sql, programmers, daily-practice]
---

## 📅 Today’s Goal
- Solve 10 SQL problems of SQL questions
- Focus on correctness and query structure
A
---

## Problem 146 — Employee Names
🔗 https://www.hackerrank.com/challenges/name-of-employees/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT NAME
FROM EMPLOYEE
ORDER BY NAME;
```
**Key Point**
- Simply order by name


## Problem 147 — Employee Salaries
🔗 https://www.hackerrank.com/challenges/salary-of-employees/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT name
from employee
where salary>2000
and months<10
order by employee_id;
```
**Key Point**
- Filter employees with salary over 2000 and months less than 10, then order by employee_id


## Problem 148 — Type of Triangle
🔗 https://www.hackerrank.com/challenges/what-type-of-triangle/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT
CASE
    WHEN a+b<=c OR a+c<=b OR b+c<=a THEN 'Not A Triangle'
    WHEN a=b AND b=c THEN 'Equilateral'
    WHEN a=b OR b=c OR c=a THEN 'Isosceles'
    ELSE 'Scalene'
END
FROM TRIANGLES
```
**Key Point**
- used a CASE statement to check the type of triangle


## Problem 149 — The PADS
🔗 https://www.hackerrank.com/challenges/the-pads/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT result
FROM (
    SELECT
        CONCAT(name, '(', LEFT(occupation, 1), ')') AS result,
        1 AS grp,
        name AS name_sort,
        NULL AS cnt_sort,
        NULL AS occ_sort
    FROM occupations
    UNION ALL
    SELECT
        CONCAT('There are a total of ', COUNT(*), ' ', LOWER(occupation), 's.') AS result,
        2 AS grp,
        NULL AS name_sort,
        COUNT(*) AS cnt_sort,
        LOWER(occupation) AS occ_sort
    FROM occupations
    GROUP BY occupation
) t
ORDER BY
    grp,
    name_sort,
    cnt_sort,
    occ_sort;

```
**Key Point**
- had to create two queries then combine them using UNION ALL
- Used Concat function to combine name and occupation


## Problem 150 — Revising Aggregations - The Count Function
🔗 https://www.hackerrank.com/challenges/revising-aggregations-the-count-function/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT count(id)
from city
where population >100000
```
**Key Point**
- Easily solved using count function


## Problem 151 — Revising Aggregations - The Sum Function
🔗 https://www.hackerrank.com/challenges/revising-aggregations-sum/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT sum(population)
from city
where district = 'California'
```
**Key Point**
- calculated sum of population in California district


## Problem 152 — Revising Aggregations - Averages
🔗 https://www.hackerrank.com/challenges/revising-aggregations-the-average-function/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT avg(population)
FROM CITY
WHERE DISTRICT = 'California'
```
**Key Point**
- calculated average of population in California district


## Problem 153 — Average Population
🔗 https://www.hackerrank.com/challenges/average-population/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT ROUND(AVG(POPULATION),0)
FROM CITY
```
**Key Point**
- Calculated average of population then rounded it to the nearest integer


## Problem 154 — Japan Population
🔗 https://www.hackerrank.com/challenges/japan-population/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT sum(population)
from city
where countrycode = 'JPN'
```
**Key Point**
- Calculated average of population then rounded it to the nearest integer


## Problem 155 — Population Density Difference
🔗 hackerrank.com/challenges/population-density-difference?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT max(population)-min(population)
from city
```
**Key Point**
- Calculated the difference between the maximum and minimum population




