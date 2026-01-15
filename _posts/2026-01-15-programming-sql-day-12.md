---
title: "Programming SQL Practice – Day 12 (10 Problems)"
date: 2026-01-15
categories: [코드-기술력-자료]
tags: [sql, programmers, daily-practice]
---

## 📅 Today’s Goal
- Solve 10 SQL problems of SQL questions
- Focus on correctness and query structure
A
---

## Problem 126 — Find Users With Valid E-Mails
🔗 https://leetcode.com/problems/find-users-with-valid-e-mails/
**Difficulty:** Level 6

```sql
SELECT user_id, name, mail
from users
where REGEXP_Like(mail, '^[A-Za-z][A-Za-z0-9_.-]*@leetcode\\.com$', 'c')
```
**Key Point**
- Question requires you to know the function REGEXP
- Can use both REGEXP + LIKE or Use REGEXP_LIKE


## Problem 127 — Revising the Select Query I
🔗 https://www.hackerrank.com/challenges/revising-the-select-query/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT *
FROM CITY
WHERE POPULATION >100000
AND COUNTRYCODE = 'USA';
```
**Key Point**
- Easy question where I need to give two conditions.


## Problem 128 — Revising the Select Query II
🔗 https://www.hackerrank.com/challenges/revising-the-select-query/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT NAME
FROM CITY
WHERE POPULATION>120000
AND COUNTRYCODE= 'USA';
```
**Key Point**
- Another easy question where I need to give two conditions.


## Problem 129 — Select All
🔗 https://www.hackerrank.com/challenges/select-all-sql/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
select *
from city;
```
**Key Point**
- Selecting all with *


## Problem 130 — Select By ID
🔗 https://www.hackerrank.com/challenges/select-by-id/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
select *
from city
where ID=1661;
```
**Key Point**
- SELECT every records that has id of 1661


## Problem 131 — Japanese Cities' Attributes
🔗 https://www.hackerrank.com/challenges/japanese-cities-attributes/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
select *
from city
countrycode='JPN';
```
**Key Point**
- SELECT every records that has country code of Japan


## Problem 132 — Japanese Cities' Names
🔗 https://www.hackerrank.com/challenges/japanese-cities-name/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT name
from city
where countrycode = 'JPN';
```
**Key Point**
- Select name of every records that has country code of Japan


## Problem 133 — Weather Observation Station 1
🔗 https://www.hackerrank.com/challenges/weather-observation-station-1/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
select city, state
from station;
```
**Key Point**
- Select city and state from table


## Problem 134 — Weather Observation Station 2
🔗 https://www.hackerrank.com/challenges/weather-observation-station-2/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT CAST(ROUND(SUM(LAT_N), 2) AS DECIMAL(10,2)), CAST(ROUND(SUM(LONG_W), 2) AS DECIMAL(10,2)) 
FROM STATION;
```
**Key Point**
- Had to force the two decimal points using Cast


## Problem 135 — Weather Observation Station 3
🔗 https://www.hackerrank.com/challenges/weather-observation-station-3/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT DISTINCT CITY
FROM STATION
WHERE ID%2=0;
```
**Key Point**
- Got the even number by getting remainder and comparing it to 0










