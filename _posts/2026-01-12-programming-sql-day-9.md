---
title: "Programming SQL Practice – Day 9 (10 Problems)"
date: 2026-01-12
categories: [코드-기술력-자료]
tags: [sql, programmers, daily-practice]
---

## 📅 Today’s Goal
- Solve 10 SQL problems of SQL questions
- Focus on correctness and query structure
A
---

## Problem 106 — Monthly Transactions I
🔗 https://leetcode.com/problems/monthly-transactions-i/description/
**Difficulty:** Level 6

```sql
select e.employee_id, name, reports_count, average_age
from employees e
left join 
(
select reports_to employee_id, count(reports_to) reports_count, round(avg(age),0) average_age
from employees
group by reports_to
) aa
on e.employee_id = aa.employee_id
where reports_count is not null
order by e.employee_id
```
**Key Point**
- Created a Subquery to get the Counts and the average.
- Then combined it with the original table to get the wanted columns.


## Problem 107 — Primary Department for Each Employee
🔗 https://leetcode.com/problems/primary-department-for-each-employee/description/
**Difficulty:** Level 6

```sql
SELECT employee_id, department_id
from employee
where primary_flag = "Y"
Union
SELECT Employee_id, department_id
from employee
where primary_flag = "N"
and Employee_id not in
(select Employee_id
from employee
where primary_flag = "Y")
```
**Key Point**
- Got the employees who have primary as Y first.
- Then got the employees who have primary as N next.
- Then Unioned the table.


## Problem 108 — Triangle Judgement
🔗 https://leetcode.com/problems/triangle-judgement/description/
**Difficulty:** Level 6

```sql
Select x, y ,z, "Yes" triangle
from Triangle
where x+y>z
and (z>=x and z>=y)
or x+z>y
and (y>=x and y>=z)
or z+y>x
and (x>=z and x>=y)
Union
Select x,y,z, "No" triangle
from Triangle
Where x+y <=z
or x+z<=y
or z+y<=x
```
**Key Point**
- Divided the code into two parts where I find a triangle and not a triangle.
- Then used union to connect the tables.


## Problem 109 — Consecutive Numbers
🔗 https://leetcode.com/problems/consecutive-numbers/description/
**Difficulty:** Level 6

```sql
SELECT DISTINCT NUM ConsecutiveNums
FROM
(
SELECT ID, NUM, LEAD(NUM,1,0)OVER(ORDER BY ID) FIRST , LEAD(NUM,2)OVER(ORDER BY ID) SECOND
FROM LOGS
) AA
WHERE NUM = FIRST
AND NUM = SECOND
```
**Key Point**
- Created other colums using Lead window function
- The compared the value to get the consecutive numbers


## Problem 110 — Product Price at a Given Date
🔗 https://leetcode.com/problems/product-price-at-a-given-date/description/
**Difficulty:** Level 6

```sql
WITH WAWAWA AS(
SELECT PRODUCT_ID, new_price PRICE, CHANGE_DATE, MAX(CHANGE_DATE)OVER(PARTITION BY PRODUCT_ID) MAX
FROM PRODUCTS
WHERE CHANGE_DATE<="2019-08-16"
)
SELECT PRODUCT_ID, PRICE
FROM WAWAWA
WHERE CHANGE_DATE=MAX
UNION
SELECT DISTINCT PRODUCT_ID, 10 INITIAL_PRICE
FROM PRODUCTS
WHERE CHANGE_DATE >"2019-08-16"
AND PRODUCT_ID NOT IN 
(SELECT PRODUCT_ID
FROM WAWAWA)
```
**Key Point**
- Created a table where you have the products within the change_date.
- Also created a table where it has a product that uses initial price.
- Union both table.


## Problem 111 — Last Person to Fit in the Bus
🔗 https://leetcode.com/problems/last-person-to-fit-in-the-bus/description/
**Difficulty:** Level 6

```sql
WITH BB AS (
SELECT NAME, TOTAL_WEIGHT
FROM(
SELECT TURN, PERSON_ID ID, PERSON_NAME NAME, WEIGHT, SUM(WEIGHT)OVER(ORDER BY TURN) TOTAL_WEIGHT
FROM QUEUE
) AA
WHERE TOTAL_WEIGHT<=1000
)
SELECT NAME person_name
FROM BB
WHERE TOTAL_WEIGHT =
(SELECT MAX(TOTAL_WEIGHT)
FROM BB)
```
**Key Point**
- Created a CTE where you can find the list of people who can go in the bus.
- Then got the last person to enter.


## Problem 112 — Count Salary Categories
🔗 https://leetcode.com/problems/count-salary-categories/description/
**Difficulty:** Level 6

```sql
SELECT c.category AS category,
       COALESCE(b.accounts_count, 0) AS accounts_count
FROM (
    SELECT 'Low Salary' AS category
    UNION ALL SELECT 'Average Salary'
    UNION ALL SELECT 'High Salary'
) c
LEFT JOIN (
    SELECT
        CASE
            WHEN income < 20000 THEN 'Low Salary'
            WHEN income <= 50000 THEN 'Average Salary'
            ELSE 'High Salary'
        END AS category,
        COUNT(*) AS accounts_count
    FROM Accounts
    GROUP BY 1
) b
ON c.category = b.category;

```
**Key Point**
- Created a new table that has the category using UNION ALL
- Then left join the table that we have to get the whole category sorted.


## Problem 113 — Count Salary Categories
🔗 https://leetcode.com/problems/count-salary-categories/description/
**Difficulty:** Level 6

```sql
SELECT EMPLOYEE_ID
FROM EMPLOYEES
WHERE SALARY <30000
AND MANAGER_ID NOT IN 
(SELECT EMPLOYEE_ID
FROM EMPLOYEES)
ORDER BY employee_id
```
**Key Point**
- Found the employees that has lower salary than 30000 and does not have a manager using where clause


## Problem 114 — Exchange Seats
🔗 https://leetcode.com/problems/exchange-seats/description/
**Difficulty:** Level 6

```sql
SELECT id,
IFNULL(CASE WHEN MOVE="NOT" THEN LEAD_STU
WHEN MOVE="MOVE" THEN LAG_STU END, 
(SELECT STUDENT
FROM SEAT
order by id desc
limit 1
)) student
FROM
(
SELECT ID, STUDENT,
CASE WHEN ID%2=0 THEN "MOVE"
WHEN ID%2=1 THEN "NOT" END MOVE,
LAG(student)over(order by id) LAG_STU,
LEAD(student)over(order by id) LEAD_STU
FROM SEAT
) AA
```
**Key Point**
- Created a lag, lead table to get the front and the back value of student name.
- Then changed them by giving condition through Move column


## Problem 115 — Movie Rating
🔗 https://leetcode.com/problems/movie-rating/description/
**Difficulty:** Level 6

```sql
WITH moviee AS (
  SELECT
    u.name,
    m.user_id,
    m.movie_id,
    m.rating,
    mv.title,
    m.created_at
  FROM movierating m
  LEFT JOIN users  u  ON m.user_id  = u.user_id
  LEFT JOIN movies mv ON m.movie_id = mv.movie_id
)
SELECT distinct name AS results
FROM moviee
WHERE name = (
  SELECT name
  FROM moviee
  GROUP BY name
  ORDER BY COUNT(*) DESC, name ASC
  LIMIT 1
)
UNION ALL
SELECT(
SELECT title
FROM MOVIEE
WHERE created_at >= '2020-02-01'
AND created_at <  '2020-03-01'
GROUP BY movie_id, title
ORDER BY AVG(rating) DESC, title ASC
LIMIT 1
) AA
```
**Key Point**
- I had to create a separate result for each question asked.
- Join CTE to be used in the main query.
- Then first query is for names that have high counts
- Second query is for titles that have high counts.









