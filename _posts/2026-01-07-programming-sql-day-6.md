---
title: "Programming SQL Practice – Day 6 (10 Problems)"
date: 2026-01-07
categories: [코드-기술력-자료]
tags: [sql, programmers, daily-practice]
---

## 📅 Today’s Goal
- Solve 10 SQL problems of SQL questions
- Focus on correctness and query structure
A
---

## Problem 76 — 상품을 구매한 회원 비율 구하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/131534
**Difficulty:** Level 5

```sql
SELECT DATE_FORMAT(SALES_DATE,'%Y') YEAR, CAST(DATE_FORMAT(SALES_DATE,'%m')AS UNSIGNED) MONTH, COUNT(DISTINCT UI.USER_ID) PURCHASED_USERS, ROUND(COUNT(DISTINCT UI.USER_ID)/(SELECT COUNT(DISTINCT USER_ID) FROM USER_INFO WHERE DATE_FORMAT(JOINED,'%Y') = '2021'),1) PUCHASED_RATIO
FROM USER_INFO UI
JOIN ONLINE_SALE OS
ON UI.USER_ID = OS.USER_ID
WHERE DATE_FORMAT(JOINED,'%Y') = '2021'
GROUP BY DATE_FORMAT(SALES_DATE,'%Y'), DATE_FORMAT(SALES_DATE,'%m')
ORDER BY 1, 2
```
**Key Point**
- Create a Joined table with Year being 2021.
- To get a Ratio, use COUNT(DISTINCT USER_ID) and divide it by COUNT(DISTINCT USER_ID) from USER_INFO.


## Problem 77 — Recyclable and Low Fat Products
🔗 https://leetcode.com/problems/recyclable-and-low-fat-products/description/
**Difficulty:** Level 6

```sql
SELECT product_id
FROM PRODUCTS
WHERE LOW_FATS='Y'
AND RECYCLABLE ='Y'
```
**Key Point**
- Give condition in the same Where line.


## Problem 78 — Find Customer Referee
🔗 https://leetcode.com/problems/find-customer-referee/description/
**Difficulty:** Level 6

```sql
SELECT NAME
FROM CUSTOMER
WHERE referee_id != 2
OR referee_id IS NULL
```
**Key Point**
- Selecting REFEREE_ID is NULL or NOT EQUAL TO 2.


## Problem 79 — Big Countries
🔗 https://leetcode.com/problems/big-countries/
**Difficulty:** Level 6

```sql
SELECT NAME, POPULATION, AREA
FROM WORLD
WHERE AREA >=3000000
OR POPULATION >=25000000
```
**Key Point**
- Selecting where conditions are AREA >=3000000 or POPULATION >=25000000.


## Problem 80 — Article Views I
🔗 https://leetcode.com/problems/article-views-i/
**Difficulty:** Level 6

```sql
SELECT distinct AUTHOR_ID ID
FROM VIEWS
WHERE AUTHOR_ID=VIEWER_ID
ORDER BY ID
```
**Key Point**
- In order to find IDs that are equal to AUTHOR_ID and VIEWER_ID, give a condition in the WHERE line.


## Problem 81 — Invalid Tweets
🔗 https://leetcode.com/problems/invalid-tweets/
**Difficulty:** Level 6

```sql
SELECT TWEET_ID
FROM TWEETS
WHERE CHAR_LENGTH(CONTENT)>15
```
**Key Point**
- Use the function CHAR_LENGTH to get the length of the tweet.


## Problem 82 — Replace Employee ID With The Unique Identifier
🔗 https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/
**Difficulty:** Level 6

```sql
SELECT UNIQUE_ID, NAME
FROM EMPLOYEES E
LEFT JOIN EMPLOYEEUNI EU
ON E.ID=EU.ID
```
**Key Point**
- Shows how you can use LEFT JOIN to get the unique ID.


## Problem 83 — Product Sales Analysis I
🔗 https://leetcode.com/problems/product-sales-analysis-i/
**Difficulty:** Level 6

```sql
SELECT PRODUCT_NAME, YEAR, PRICE
FROM SALES S
JOIN PRODUCT P
ON S.PRODUCT_ID= P.PRODUCT_ID
```
**Key Point**
- Shows how you can use JOIN to get the product name, year, and price.


## Problem 84 — Customer Who Visited but Did Not Make Any Transactions
🔗 https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description/
**Difficulty:** Level 6

```sql
SELECT CUSTOMER_ID customer_id, COUNT(*) count_no_trans
FROM VISITS
WHERE VISIT_ID NOT IN
(SELECT VISIT_ID FROM TRANSACTIONS)
GROUP BY CUSTOMER_ID

```
**Key Point**
- In order to get the customer ID who visited but did not make any transactions, we used In() function.
- Then used Group by CUSTOMER_ID to get the count of no transactions.


## Problem 85 — Rising Temperature
🔗 https://leetcode.com/problems/rising-temperature/
**Difficulty:** Level 6

```sql
select ID
FROM(
SELECT ID, (temperature - LAG(temperature)OVER(ORDER BY ID)) diff
FROM WEATHER
) BB
WHERE diff >0

```
**Key Point**
- Create an inner query to get the difference between temperature and the previous temperature.

