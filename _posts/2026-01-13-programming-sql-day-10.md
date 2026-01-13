---
title: "Programming SQL Practice – Day 10 (5 Problems)"
date: 2026-01-13
categories: [코드-기술력-자료]
tags: [sql, programmers, daily-practice]
---

## 📅 Today’s Goal
- Solve 5 SQL problems of SQL questions
- Focus on correctness and query structure
A
---

## Problem 116 — Restaurant Growth
🔗 https://leetcode.com/problems/restaurant-growth/
**Difficulty:** Level 6

```sql
WITH CUST_VIS AS(
SELECT VISITED_ON, sum(AMOUNT) amount
FROM CUSTOMER
GROUP BY VISITED_ON
)
SELECT VISITED_ON,
SUM(AMOUNT)OVER(ORDER BY VISITED_ON ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AMOUNT,
ROUND(AVG(AMOUNT)OVER(ORDER BY VISITED_ON ROWS BETWEEN 6 PRECEDING AND CURRENT ROW),2)  average_amount 
FROM CUST_VIS
ORDER BY visited_on
LIMIT 1000000 OFFSET 6;
```
**Key Point**
- Very important part of this code was to understand the ways how window function works.
- You need to write ROWS BETWEEN 6 PRECEDING AND CURRENT ROW in order to get the 6 preceding dates


## Problem 117 — Friend Requests II: Who Has the Most Friends
🔗 https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/description/
**Difficulty:** Level 6

```sql
with subang as
(SELECT *
FROM
(SELECT accepter_id, COUNT(*) CNT
FROM RequestAccepted
GROUP BY ACCEPTER_ID) R
left join
(
SELECT REQUESTER_ID, COUNT(*) CNTA
FROM RequestAccepted
GROUP BY REQUESTER_ID
) AA
ON R.ACCEPTER_ID= AA.REQUESTER_ID
Union
SELECT *
FROM
(SELECT accepter_id, COUNT(*) CNT
FROM RequestAccepted
GROUP BY ACCEPTER_ID) R
right join
(
SELECT REQUESTER_ID, COUNT(*) CNTA
FROM RequestAccepted
GROUP BY REQUESTER_ID
) AA
ON R.ACCEPTER_ID= AA.REQUESTER_ID
)
SELECT IFNULL(ACCEPTER_ID,REQUESTER_ID) ID, IFNULL(CNT, 0) + IFNULL(CNTA, 0) NUM
FROM SUBANG
WHERE IFNULL(CNT, 0) + IFNULL(CNTA, 0)=
(SELECT MAX(IFNULL(CNT, 0) + IFNULL(CNTA, 0))
FROM SUBANG)
```
**Key Point**
- Very important part of this code was to understand the ways how window function works.
- You need to write ROWS BETWEEN 6 PRECEDING AND CURRENT ROW in order to get the 6 preceding dates


## Problem 118 — Investments in 2016
🔗 https://leetcode.com/problems/investments-in-2016/description/
**Difficulty:** Level 6

```sql
with counting as(
select  tiv_2016, count(tiv_2015)over(partition by tiv_2015) cnt, count(*)over(partition by lat, lon) ll
from insurance
)
select round(sum(tiv_2016),2) tiv_2016
from counting
where cnt>=2
and ll=1
```
**Key Point**
- Got a CTE having both counts for tiv_2015 and lat, lon.
- Then gave condition on the main query.


## Problem 119 — Department Top Three Salaries
🔗 https://leetcode.com/problems/department-top-three-salaries/
**Difficulty:** Level 6

```sql
with combine as(
Select e.name Employee, d.name Department, salary, dense_rank()over(partition by d.name order by salary desc) ranks
from employee e
join department d
on e.departmentid = d.id
)
select department, Employee, salary
from combine
where ranks<=3
```
**Key Point**
- Got a CTE to get dense rank of the salary.
- Then used the CTE to get the 1~3rd salary ranked employees


## Problem 120 — Fix Names in a Table
🔗 https://leetcode.com/problems/fix-names-in-a-table/description/
**Difficulty:** Level 6

```sql
with divide as(
select user_id, upper(substring(name,1,1)) first, lower(substring(name,2)) last
from users
)
select user_id, concat(first,last) name
from divide
order by user_id
```
**Key Point**
- Got a CTE to divide the character into two parts
- Then concatenated the divided character into one.






