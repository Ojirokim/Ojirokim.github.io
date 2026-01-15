---
title: "Programming SQL Practice – Day 12 (5 Problems)"
date: 2026-01-15
categories: [코드-기술력-자료]
tags: [sql, programmers, daily-practice]
---

## 📅 Today’s Goal
- Solve 5 SQL problems of SQL questions
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
SELECT *
FROM CITY
WHERE POPULATION >100000
AND COUNTRYCODE = 'USA';
```
**Key Point**
- Easy question where I need to give two conditions.





