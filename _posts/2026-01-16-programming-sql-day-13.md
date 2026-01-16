---
title: "Programming SQL Practice – Day 13 (10 Problems)"
date: 2026-01-16
categories: [코드-기술력-자료]
tags: [sql, programmers, daily-practice]
---

## 📅 Today’s Goal
- Solve 10 SQL problems of SQL questions
- Focus on correctness and query structure
A
---

## Problem 136 — Weather Observation Station 4
🔗 https://www.hackerrank.com/challenges/weather-observation-station-4/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
select count(city)-count(distinct city)
from station;
```
**Key Point**
- Calculated the difference between disntinct and all.


## Problem 137 - Weather Observation Station 5
🔗 https://www.hackerrank.com/challenges/weather-observation-station-5/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT CITY, LENGTH(CITY)
FROM(
select CITY, LENGTH(CITY), RANK()OVER(ORDER BY LEnGTH(CITY),CITY) RN,
RANK()OVER(ORDER BY LEnGTH(CITY) DESC,CITY) RRN
FROM STATION
) AA   
WHERE RN=1
or RRN=1;
```
**Key Point**
- Had to create a window function to get the longest length and the shortest length
- Then select them in the outer query


## Problem 138 - Weather Observation Station 6
🔗 https://www.hackerrank.com/challenges/weather-observation-station-6/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT distinct CITY
FROM STATION
WHERE CITY LIKE 'a%'
or CITY LIKE 'e%'
or CITY LIKE 'i%'
or CITY LIKE 'o%'
or CITY LIKE 'u%';
```
**Key Point**
- used like to select the ones that starts with a vowel.
- Can also use REGEXP to select the vowels as well
```sql
SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '^[aeiou]';
```


## Problem 139 - Weather Observation Station 7
🔗 https://www.hackerrank.com/challenges/weather-observation-station-7/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT distinct CITY
FROM STATION
WHERE CITY LIKE '%a'
or CITY LIKE '%e'
or CITY LIKE '%i'
or CITY LIKE '%o'
or CITY LIKE '%u';
```
**Key Point**
- used like to select the ones that ends with a vowel.
- Can also use REGEXP to select the vowels as well
```sql
SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '[aeiou]$';
```


## Problem 140 - Weather Observation Station 8
🔗 https://www.hackerrank.com/challenges/weather-observation-station-8/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT CITY
FROM STATION
WHERE (CITY LIKE '%a'
or CITY LIKE '%e'
or CITY LIKE '%i'
or CITY LIKE '%o'
or CITY LIKE '%u')
AND 
(CITY LIKE 'a%'
or CITY LIKE 'e%'
or CITY LIKE 'i%'
or CITY LIKE 'o%'
or CITY LIKE 'u%');
```
**Key Point**
- used like to select the ones that ends with a vowel.
- Can also use REGEXP to select the vowels as well
```sql
SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '^[aeiou].*[aeiou]$';
```


## Problem 141 - Weather Observation Station 9
🔗 https://www.hackerrank.com/challenges/weather-observation-station-9/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT distinct CITY
FROM STATION
WHERE CITY not LIKE 'a%'
and CITY not LIKE 'e%'
and CITY not LIKE 'i%'
and CITY not LIKE 'o%'
and CITY not LIKE 'u%';
```
**Key Point**
- used like to select the ones that do not start with a vowel.
- Can also use REGEXP to select the vowels as well
```sql
SELECT DISTINCT CITY
FROM STATION
WHERE CITY NOT REGEXP '^[aeiou]';
```


## Problem 142 - Weather Observation Station 10
🔗 https://www.hackerrank.com/challenges/weather-observation-station-10/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT distinct CITY
FROM STATION
WHERE CITY not LIKE '%a'
and CITY not LIKE '%e'
and CITY not LIKE '%i'
and CITY not LIKE '%o'
and CITY not LIKE '%u';
```
**Key Point**
- used like to select the ones that do not end with a vowel.
- Can also use REGEXP to select the vowels as well
```sql
SELECT DISTINCT CITY
FROM STATION
WHERE CITY not REGEXP '[aeiou]$';
```


## Problem 143 - Weather Observation Station 11
🔗 https://www.hackerrank.com/challenges/weather-observation-station-11/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT distinct CITY
FROM STATION
WHERE (CITY not LIKE '%a'
and CITY not LIKE '%e'
and CITY not LIKE '%i'
and CITY not LIKE '%o'
and CITY not LIKE '%u')
or 
(CITY not LIKE 'a%'
and CITY not LIKE 'e%'
and CITY not LIKE 'i%'
and CITY not LIKE 'o%'
and CITY not LIKE 'u%');
```
**Key Point**
- used like to select the ones that do not start or end with a vowel.
- Can also use REGEXP to select the vowels as well
```sql
SELECT DISTINCT CITY
FROM STATION
WHERE not CITY REGEXP '^[aeiou].*[aeiou]$';
```


## Problem 144 - Weather Observation Station 12
🔗 https://www.hackerrank.com/challenges/weather-observation-station-12/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT DISTINCT CITY
FROM STATION
WHERE not CITY REGEXP '^[aeiou]|[aeiou]$';
```
**Key Point**
- used REGEXP to select the ones that both do not start and end with a vowel.


## Problem 145 - Higher Than 75 Marks
🔗 https://www.hackerrank.com/challenges/more-than-75-marks/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT NAME
FROM STUDENTS
WHERE MARKS>75
ORDER BY SUBSTRING(NAME,-3), ID
```
**Key Point**
- ORDER THE NAME BY the last 3 character of the name using substring.


