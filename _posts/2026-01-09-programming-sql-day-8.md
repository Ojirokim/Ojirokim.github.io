---
title: "Programming SQL Practice – Day 8 (10 Problems)"
date: 2026-01-09
categories: [코드-기술력-자료]
tags: [sql, programmers, daily-practice]
---

## 📅 Today’s Goal
- Solve 10 SQL problems of SQL questions
- Focus on correctness and query structure
A
---

## Problem 96 — Monthly Transactions I
🔗 https://leetcode.com/problems/monthly-transactions-i/description/
**Difficulty:** Level 6

```sql
SELECT DISTINCT MONTH, COUNTRY, COUNT(*)OVER(PARTITION BY MONTH, COUNTRY) TRANS_COUNT,
COUNT(CASE WHEN STATE="approved" then 1 end)OVER(partition by MONTH, country) approved_count,
SUM(AMOUNT)OVER(PARTITION BY MONTH, COUNTRY) TRANS_TOTAL_AMOUNT,
IFNULL(SUM(CASE WHEN STATE="approved" then AMOUNT end)OVER(PARTITION BY MONTH, COUNTRY),0) APPROVED_TOTAL_AMOUNT
FROM (
SELECT DATE_FORMAT(TRANS_DATE, '%Y-%m') MONTH, COUNTRY, STATE, AMOUNT, TRANS_DATE
FROM TRANSACTIONS
) BB
```
**Key Point**
- Created a Query that returns the Transaction table with the month column added.
- Then used the PARTITION BY clause to group the data by month and country.


## Problem 97 — Immediate Food Delivery II
🔗 https://leetcode.com/problems/immediate-food-delivery-ii/description/
**Difficulty:** Level 6

```sql
SELECT ROUND(SUM(ZERO)/COUNT(*)*100,2) immediate_percentage
FROM
(
SELECT customer_id, Case 
when ORDER_DATE =customer_pref_delivery_date then 1
else 0 end ZERO
FROM(
SELECT CUSTOMER_ID, MIN(ORDER_DATE)OVER(PARTITION BY CUSTOMER_ID) FIRST_ORDER, ORDER_DATE, customer_pref_delivery_date 
FROM DELIVERY
) BB
WHERE FIRST_ORDER = ORDER_DATE
) AA
```
**Key Point**
- Had to create two subqueries to calculate the percentage. First to get the immediate orders and the total orders.
- Then second subquery to calculate the percentage.


## Problem 98 — Game Play Analysis IV
🔗 https://leetcode.com/problems/game-play-analysis-iv/description/
**Difficulty:** Level 6

```sql
WITH first_login AS (
  SELECT player_id, MIN(event_date) AS first_day
  FROM Activity
  GROUP BY player_id
),
returned_next_day AS (
  SELECT DISTINCT f.player_id
  FROM first_login f
  JOIN Activity a
    ON a.player_id = f.player_id
   AND a.event_date = DATE_ADD(f.first_day, INTERVAL 1 DAY)
)
SELECT ROUND(
         (SELECT COUNT(*) FROM returned_next_day) /
         (SELECT COUNT(*) FROM first_login),
         2
       ) AS fraction;
```
**Key Point**
- First found the first login date for each player.
- Then created a subquery to find players who logged in on the first day of the next day.
- Finally calculated the fraction of players who returned to play on the next day.

## Problem 99 — Number of Unique Subjects Taught by Each Teacher
🔗 https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/description/
**Difficulty:** Level 6

```sql
SELECT TEACHER_ID, COUNT(DISTINCT SUBJECT_ID) CNT
FROM TEACHER
GROUP BY TEACHER_ID
```
**Key Point**
- This one was an easy one. Just had to count the number of unique subjects taught by each teacher.


## Problem 100 — User Activity for the Past 30 Days I
🔗 https://leetcode.com/problems/user-activity-for-the-past-30-days-i/
**Difficulty:** Level 6

```sql
select Activity_date day, count(*) active_users
from
(
SELECT USER_ID,activity_Date
FROM ACTIVITY
WHERE ACTIVITY_DATE<='2019-07-27'
AND ACTIVITY_DATE>= '2019-06-28'
group by 1,2
) AA
Group by 1
```
**Key Point**
- I had to group two times because I wanted to count the number of active users for each day.


## Problem 101 — Product Sales Analysis III
🔗 https://leetcode.com/problems/product-sales-analysis-iii/description/
**Difficulty:** Level 6

```sql
SELECT PRODUCT_ID, FIRST_YEAR, QUANTITY, PRICE
FROM(
SELECT PRODUCT_ID, YEAR first_year, quantity,  price, MIN(YEAR)OVER(PARTITION BY PRODUCT_ID) MIN
FROM SALES
) BB
WHERE FIRST_YEAR = MIN
```
**Key Point**
- First created a subquery to find the first year of sales for each product.
- Then filtered the data to only include rows where the first year was the same as the minimum year.


## Problem 102 — Classes With at Least 5 Students
🔗 https://leetcode.com/problems/classes-with-at-least-5-students/description/
**Difficulty:** Level 6

```sql
SELECT CLASS
FROM
(
SELECT CLASS, COUNT(*) CNT
FROM COURSES
GROUP BY CLASS
) AA
WHERE CNT >=5
```
**Key Point**
- First created a subquery to count the number of students in each class.
- Then filtered the data to only include classes with at least 5 students.


## Problem 103 — Find Followers Count
🔗 https://leetcode.com/problems/find-followers-count/description/
**Difficulty:** Level 6

```sql
SELECT USER_ID, COUNT(*) FOLLOWERS_COUNT
FROM FOLLOWERS
GROUP BY USER_ID
ORDER BY USER_ID
```
**Key Point**
- Follower counts can easily be found by grouping by user_id.


## Problem 104 — Biggest Single Number
🔗 https://leetcode.com/problems/biggest-single-number/description/
**Difficulty:** Level 6

```sql
SELECT MAX(NUM) NUM
FROM 
(
SELECT NUM, COUNT(NUM)OVER(PARTITION BY NUM) CNT
FROM MYNUMBERS 
) AA
WHERE CNT=1
```
**Key Point**
- Created a subquery to count the number of times each number appears.
- Then filtered the data to only include rows where the count was 1.


## Problem 105 — Customers Who Bought All Products
🔗 https://leetcode.com/problems/customers-who-bought-all-products/
**Difficulty:** Level 6

```sql
SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product);
```
**Key Point**
- Use conditions in the HAVING line to filter the data.
- Compare the number of distinct products bought by each customer to the total number of products.