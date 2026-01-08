---
title: "Programming SQL Practice – Day 7 (10 Problems)"
date: 2026-01-08
categories: [코드-기술력-자료]
tags: [sql, programmers, daily-practice]
---

## 📅 Today’s Goal
- Solve 10 SQL problems of SQL questions
- Focus on correctness and query structure
A
---

## Problem 86 — Average Time of Process per Machine
🔗 https://leetcode.com/problems/average-time-of-process-per-machine/description/
**Difficulty:** Level 6

```sql
SELECT AA.MACHINE_ID machine_id, ROUND(AVG(BB_TS-AA_TS),3) processing_time
FROM
(SELECT MACHINE_ID, PROCESS_ID, TIMESTAMP AA_TS
FROM ACTIVITY
WHERE ACTIVITY_TYPE = 'start'
) AA
JOIN
(SELECT MACHINE_ID, PROCESS_ID, TIMESTAMP BB_TS
FROM ACTIVITY
WHERE ACTIVITY_TYPE = 'END'
) BB
ON AA.process_id= BB.process_id
AND AA. machine_id= BB. machine_id
GROUP BY AA.MACHINE_ID
```
**Key Point**
- Create two tables that has each 'start' and 'end' activity of each process.
- Join two tables and calculate average time of each machine.


## Problem 87 — Employee Bonus
🔗 https://leetcode.com/problems/employee-bonus/
**Difficulty:** Level 6

```sql
SELECT NAME, BONUS
FROM EMPLOYEE E
LEFT JOIN BONUS B
ON E.EMPID=B.EMPID
WHERE BONUS IS NULL
OR BONUS<=1000
```
**Key Point**
- Left join two tables and select employees who don't have bonus.


## Problem 88 — Employee Bonus
🔗 https://leetcode.com/problems/students-and-examinations/
**Difficulty:** Level 6

```sql
select s.student_id, student_name, sb.subject_name, count(e.student_id) attended_exams
from students s
cross join subjects sb
left join examinations e
on s.student_id = e.student_id
and sb.subject_name = e.subject_name
group by s.student_id, student_name, sb.subject_name 
order by s.student_id, student_name
```
**Key Point**
- This question took me a while to solve, due to myself not knowing how to use cross join.
- I used cross join to get all combinations of students and subjects.


## Problem 89 — Managers with at Least 5 Direct Reports
🔗 https://leetcode.com/problems/managers-with-at-least-5-direct-reports/
**Difficulty:** Level 6

```sql
SELECT NAME
FROM EMPLOYEE E
LEFT JOIN
(
select managerid, count(id) CNT
from employee
group by managerid
) BB
ON E.ID= BB.managerid
WHERE CNT>=5
```
**Key Point**
- Created a second table that has the count of each manager.
- Then used left join to get employees who have at least 5 direct reports.


## Problem 90 — Confirmation Rate
🔗 https://leetcode.com/problems/confirmation-rate/
**Difficulty:** Level 6

```sql
SELECT DISTINCT USER_ID, ROUND(CNT/cnt_all,2) confirmation_rate
from
(
SELECT S.user_id, count(case when action='confirmed' then 1 end)over(parTition by user_id) CNT, COUNT(*)OVER(partition by user_id) cnt_all
FROM SIGNUPS S
LEFT JOIN CONFIRMATIONS C
ON S.USER_ID = C.USER_ID
) AA
```
**Key Point**
- First created a table that has the count of each user who confirmed their email.
- Then used window function to get confirmation rate.
- After that, I used distinct to get only unique user_id.


## Problem 91 — Not Boring Movies
🔗 https://leetcode.com/problems/not-boring-movies/
**Difficulty:** Level 6

```sql
SELECT *
FROM CINEMA
WHERE ID%2=1
AND DESCRIPTION != "boring"
order by rating desc
```
**Key Point**
- Found the odd numbered movies by using % operator.


## Problem 92 — Average Selling Price
🔗 https://leetcode.com/problems/average-selling-price/description/
**Difficulty:** Level 6

```sql
SELECT U.PRODUCT_ID, ROUND(SUM(UNITS*PRICE)/SUM(UNITS),2) average_price
FROM UNITSSOLD U
JOIN PRICES P 
ON U.PRODUCT_ID = P.PRODUCT_ID
WHERE PURCHASE_DATE BETWEEN START_DATE AND END_DATE
GROUP BY PRODUCT_ID
```
**Key Point**
- Created a table that has the sum of units sold and price of each product.
- Then calculated average price by dividing sum of units sold and price.


## Problem 93 — Project Employees I
🔗 https://leetcode.com/problems/project-employees-i/description/
**Difficulty:** Level 6

```sql
select project_id, round(avg(experience_years),2) average_years
from project p
left join employee e
on p.employee_id= e.employee_id
group by project_id
```
**Key Point**
- Created a table that has the average years of experience of each employee.
- Then calculated average year of each project by grouping by project_id.


## Problem 94 — Percentage of Users Attended a Contest
🔗 https://leetcode.com/problems/percentage-of-users-attended-a-contest/description/
**Difficulty:** Level 6

```sql
select contest_id, round(count(*)/
(select count(*)
from users)*100,2) percentage
from Register
group by contest_id
order by percentage desc, contest_id
```
**Key Point**
- Got the number of users who attended each contest and got the whole number of users by counting all rows in a subquery.
- Then calculated percentage by dividing the number of users who attended the contest and the whole number of users.


## Problem 95 — Queries Quality and Percentage
🔗 https://leetcode.com/problems/queries-quality-and-percentage/description/
**Difficulty:** Level 6

```sql
Select AA.query_name, quality, poor_query_percentage
from
(Select query_name, round(sum(rating/position)/3,2) quality
from Queries
group by query_name
) AA
join
(
select distinct query_name,
round(count(case when rating<3 then 1 end)over(partition by query_name)/count(*)over(partition by query_name)*100,2) poor_query_percentage
from queries
) BB
on AA.query_name = BB.query_name
```
**Key Point**
- Made two tables that has the average rating of each query and the percentage of poor queries.
- Then joined two tables to get the result.
- 