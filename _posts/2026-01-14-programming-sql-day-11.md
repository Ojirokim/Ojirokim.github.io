---
title: "Programming SQL Practice – Day 11 (5 Problems)"
date: 2026-01-14
categories: [코드-기술력-자료]
tags: [sql, programmers, daily-practice]
---

## 📅 Today’s Goal
- Solve 5 SQL problems of SQL questions
- Focus on correctness and query structure
A
---

## Problem 121 — Patients With a Condition
🔗 https://leetcode.com/problems/restaurant-growth/
**Difficulty:** Level 6

```sql
SELECT patient_id, patient_name, conditions
FROM patients
WHERE CONCAT(' ', conditions, ' ') LIKE '% DIAB1% %';
```
**Key Point**
- Never realized that I can use Concat with like to create a situation where I can find the words with DIAB1 in it.


## Problem 122 - Delete Duplicate Emails
🔗 https://leetcode.com/problems/restaurant-growth/
**Difficulty:** Level 6

```sql
WITH cte AS (
  SELECT id,
         ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS rn
  FROM Person
)
DELETE FROM Person
WHERE id IN (SELECT id FROM cte WHERE rn > 1);
```
**Key Point**
- In order to use Delete in Mysql you need to have a clear table instead of a driven table.
- Thus create a CTE that has row numbers.


## Problem 123 - Second Highest Salary
🔗 https://leetcode.com/problems/second-highest-salary/description/
**Difficulty:** Level 6

```sql
WITH RANKS AS 
(SELECT *, DENSE_RANK()OVER(ORDER BY SALARY desc) RN
FROM EMPLOYEE
)
SELECT MAX(CASE WHEN rn = 2 THEN salary END) SecondHighestSalary
FROM ranks;
```
**Key Point**
- Use Max(Case) in order to create a empty null line even if there is nothing there.


## Problem 124 - Group Sold Products By The Date
🔗 https://leetcode.com/problems/group-sold-products-by-the-date/
**Difficulty:** Level 6

```sql
SELECT SELL_DATE, COUNT(DISTINCT PRODUCT) NUM_SOLD, GROUP_CONCAT(DISTINCT PRODUCT ORDER BY product SEPARATOR ',') PRODUCTS
FROM ACTIVITIES
GROUP BY SELL_DATE
```
**Key Point**
- In order to concatenate Character in Mysql you need to use GROUP_CONCAT


## Problem 125 - List the Products Ordered in a Period
🔗 https://leetcode.com/problems/list-the-products-ordered-in-a-period/description/
**Difficulty:** Level 6

```sql
SELECT PRODUCT_NAME, UNITS UNIT
FROM PRODUCTS P
JOIN
(SELECT PRODUCT_ID, SUM(UNIT) UNITS
FROM ORDERS
WHERE ORDER_DATE>='2020-02-01'
AND ORDER_DATE<'2020-03-01'
GROUP BY PRODUCT_ID
HAVING UNITS>=100
)AA
ON P.PRODUCT_ID = AA.PRODUCT_ID
```
**Key Point**
- Created a table to get the sum of the units.
- Then joined it with the name table to get the name.





