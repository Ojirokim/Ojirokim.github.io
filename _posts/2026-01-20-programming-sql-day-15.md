---
title: "Programming SQL Practice – Day 15 (10 Problems)"
date: 2026-01-20
categories: [코드-기술력-자료]
tags: [sql, programmers, daily-practice]
---

## 📅 Today’s Goal
- Solve 10 SQL problems of SQL questions
- Focus on correctness and query structure
A
---

## Problem 156 — The Blunder
🔗 https://www.hackerrank.com/challenges/the-blunder/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT CEIL(
  AVG(Salary) - AVG(CAST(REPLACE(CAST(Salary AS CHAR), '0', '') AS UNSIGNED))
)
FROM EMPLOYEES;

```
**Key Point**
- Cast the salary value into Character then removed 0.
- Then Cast it back to Number


## Problem 157 — Top Earners
🔗 https://www.hackerrank.com/challenges/earnings-of-employees/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
select 
CONCAT(EARNINGS, ' ', CNT)
FROM
(
SELECT
  (salary * months) AS earnings,
  COUNT(*) AS cnt
FROM employee
GROUP BY earnings
ORDER BY earnings DESC
limit 1
) AA
```
**Key Point**
- The question specifically asked to return values as 2 space-separated integers.
- So we need to use CONCAT function to combine them.


## Problem 158 — Weather Observation Station 13
🔗 https://www.hackerrank.com/challenges/weather-observation-station-13/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT TRUNCATE(SUM(LAT_N),4)
from station
where LAT_N >38.788
AND LAT_N<137.2345
```
**Key Point**
- Truncate the result to 4 decimal places.
- Gave condition in where line to filter out the result.


## Problem 159 — Weather Observation Station 14
🔗 https://www.hackerrank.com/challenges/weather-observation-station-14/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
select TRUNCATE(MAX(LAT_N),4)
from station
WHERE LAT_N < 137.2345
```
**Key Point**
- Truncate the result to 4 decimal places.
- Gave condition to filter out the result.


## Problem 160 — Weather Observation Station 15
🔗 https://www.hackerrank.com/challenges/weather-observation-station-15/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT ROUND(LONG_W,4)
FROM STATION
WHERE LAT_N<137.2345
order by LAT_N DESC
LIMIT 1
```
**Key Point**
- Truncate the result to 4 decimal places.
- Gave condition to filter out the result.
- Used order by and limit to get the maximum value.


## Problem 161 — Weather Observation Station 16
🔗 https://www.hackerrank.com/challenges/weather-observation-station-16/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT ROUND(LAT_N,4)
FROM STATION
WHERE LAT_N >38.778
ORDER BY LAT_N
LIMIT 1
```
**Key Point**
- Used order by and limit to get the minimum value.
- Truncate the result to 4 decimal places.


## Problem 162 — Weather Observation Station 17
🔗 https://www.hackerrank.com/challenges/weather-observation-station-17/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
select ROUND(LONG_W,4)
from STATION
WHERE LAT_N >38.778
ORDER BY LAT_N
LIMIT 1
```
**Key Point**
- Used order by and limit to get the minimum value.
- Truncate the result to 4 decimal places.


## Problem 163 — Weather Observation Station 18
🔗 https://www.hackerrank.com/challenges/weather-observation-station-18/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
WITH LOCATION AS(
SELECT MAX(LAT_N) MaxN, MAX(LONG_W) MAXW,
MIN(LAT_N) MINN, MIN(LONG_W) MINW
FROM STATION
)
SELECT ROUND(MAXN-MINN+MAXW-MINW,4)
FROM LOCATION
```
**Key Point**
- Created a CTE to store the maximum and minimum values of latitude and longitude.
- Used the CTE to calculate the difference between maximum and minimum values of latitude and longitude.
- Truncate the result to 4 decimal places.


## Problem 164 — Weather Observation Station 19
🔗 https://www.hackerrank.com/challenges/weather-observation-station-19/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
WITH LOCATION AS(
SELECT MAX(LAT_N) MaxN, MAX(LONG_W) MAXW,
MIN(LAT_N) MINN, MIN(LONG_W) MINW
FROM STATION
)
SELECT ROUND(SQRT(POWER(MAXN-MINN,2)+POWER(MAXW-MINW,2)),4)
FROM LOCATION
```
**Key Point**
- Created a CTE to store the maximum and minimum values of latitude and longitude.
- Used the CTE to calculate the euclidean distance between maximum and minimum values of latitude and longitude.
- Truncate the result to 4 decimal places.


## Problem 165 — Weather Observation Station 19
🔗 https://www.hackerrank.com/challenges/weather-observation-station-19/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
select sum(ci.population)
from city ci
join country co
on ci.countrycode = co.code
where Continent = 'Asia'
```
**Key Point**
- Joined the city table and country table based on the country code.
- Filtered the result to get the population of cities in Asia.



