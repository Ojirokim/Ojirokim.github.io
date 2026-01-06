---
title: "Programming SQL Practice – Day 5 (10 Problems)"
date: 2026-01-06
categories: [코드-기술력-자료]
tags: [sql, programmers, daily-practice]
---

## 📅 Today’s Goal
- Solve 10 SQL problems of SQL questions
- Focus on correctness and query structure
A
---

## Problem 66 — 조회수가 가장 많은 중고거래 게시판의 첨부파일 조회하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/164671
**Difficulty:** Level 5

```sql
SELECT CONCAT("/home/grep/src/",GB.BOARD_ID,"/",FILE_ID,FILE_NAME,FILE_EXT) FILE_PATH
FROM USED_GOODS_BOARD GB
LEFT JOIN USED_GOODS_FILE GF
ON GB.BOARD_ID = GF.BOARD_ID
WHERE VIEWS = 
(SELECT MAX(VIEWS) FROM USED_GOODS_BOARD)
```
**Key Point**
- Firstly need to join the table, then select the records by selecting them from Where line.
- Then select the appropriate columns to select by using function CONCAT.


## Problem 67 — 주문량이 많은 아이스크림들 조회하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/133027
**Difficulty:** Level 5

```sql
SELECT BB.FLAVOR
FROM
(
SELECT FH.FLAVOR, TOTAL_ORDER+SUM_TOT SUM_TOT
FROM FIRST_HALF FH
LEFT JOIN (
SELECT FLAVOR,SUM(TOTAL_ORDER) SUM_TOT
FROM JULY
GROUP BY FLAVOR
) FA
ON FH.FLAVOR = FA.FLAVOR
) BB
ORDER BY SUM_TOT DESC
LIMIT 3
```
**Key Point**
- Had to create two SubQuery in order to Join two tables, then make a Sum amount of both total_order values.
- Then limit 3 after ordering them by SUM_TOT Desc


## Problem 68 — 저자 별 카테고리 별 매출액 집계하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/144856
**Difficulty:** Level 5

```sql
SELECT B.AUTHOR_ID, A.AUTHOR_NAME, CATEGORY, SUM(PRICE*SALES) TOTAL_SALES
FROM BOOK B
LEFT JOIN(
SELECT BOOK_ID, SUM(SALES) SALES
FROM BOOK_SALES
WHERE DATE_FORMAT(SALES_DATE,'%Y-%m') = '2022-01'
GROUP BY BOOK_ID
)BB
ON B.BOOK_ID = BB.BOOK_ID
LEFT JOIN AUTHOR A
ON B.AUTHOR_ID = A.AUTHOR_ID
GROUP BY B.AUTHOR_ID, A.AUTHOR_NAME, CATEGORY
ORDER BY B.AUTHOR_ID, CATEGORY DESC;
```
**Key Point**
- Joining two tables first. Then Grouping them with 3 columns due to having the same ones in a same BOOK_ID.


## Problem 68 — 저자 별 카테고리 별 매출액 집계하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/144856
**Difficulty:** Level 5

```sql
SELECT B.AUTHOR_ID, A.AUTHOR_NAME, CATEGORY, SUM(PRICE*SALES) TOTAL_SALES
FROM BOOK B
LEFT JOIN(
SELECT BOOK_ID, SUM(SALES) SALES
FROM BOOK_SALES
WHERE DATE_FORMAT(SALES_DATE,'%Y-%m') = '2022-01'
GROUP BY BOOK_ID
)BB
ON B.BOOK_ID = BB.BOOK_ID
LEFT JOIN AUTHOR A
ON B.AUTHOR_ID = A.AUTHOR_ID
GROUP BY B.AUTHOR_ID, A.AUTHOR_NAME, CATEGORY
ORDER BY B.AUTHOR_ID, CATEGORY DESC;
```
**Key Point**
- Joining two tables first. Then Grouping them with 3 columns due to having the same ones in a same BOOK_ID.


## Problem 69 — 대여 횟수가 많은 자동차들의 월별 대여 횟수 구하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/151139
**Difficulty:** Level 5

```sql
SELECT MONTH, CAR_ID, COUNT(*) RECORDS
FROM
(
SELECT CAR_ID, COUNT(*)OVER(PARTITION BY CAR_ID) NUMBER, CAST(DATE_FORMAT(START_DATE,'%m') as unsigned) MONTH
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE DATE_FORMAT(START_DATE,'%Y-%m') BETWEEN '2022-08' AND '2022-10'
) BB
WHERE NUMBER>=5
GROUP BY MONTH, CAR_ID
ORDER BY MONTH, CAR_ID DESC
```
**Key Point**
- Create a Subquery that includes both count of cars by month and Start date formatted as month.
- Where line should exist outside subquery because it can not refer to Number column inside.
- CAST(Column as unsigned) can be used to cast String into Int value


## Problem 70 — 그룹별 조건에 맞는 식당 목록 출력하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/131124
**Difficulty:** Level 5

```sql
SELECT MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE,'%Y-%m-%d') REVIEW_DATE
FROM MEMBER_PROFILE MP
JOIN 
(SELECT *, COUNT(*)OVER(PARTITION BY MEMBER_ID) CNT
FROM REST_REVIEW
ORDER BY CNT DESC
) BB
ON MP.MEMBER_ID = BB.MEMBER_ID
WHERE CNT =
(SELECT MAX(CNT)
FROM
(
SELECT MEMBER_ID, COUNT(*) CNT
FROM REST_REVIEW
GROUP BY MEMBER_ID
) AA
)
ORDER BY REVIEW_DATE, REVIEW_TEXT;
```
**Key Point**
- Selecting the Member that has the most review was the trickiest part. 
- Had to create a Column that consists all the members with counts next to them.
- After that, select the max amount and put it on the WHERE LINE to give condition.


## Problem 71 — 오프라인/온라인 판매 데이터 통합하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/131537
**Difficulty:** Level 5

```sql
SELECT DATE_FORMAT(SALES_DATE,'%Y-%m-%d') SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
FROM ONLINE_SALE
WHERE DATE_FORMAT(SALES_DATE,'%Y-%m') = '2022-03'
UNION ALL
SELECT SALES_DATE, PRODUCT_ID, NULL USER_ID, SALES_AMOUNT
FROM OFFLINE_SALE
WHERE DATE_FORMAT(SALES_DATE,'%Y-%m') = '2022-03'
ORDER BY 1, 2, 3
```
**Key Point**
- Need to remember that Union does not allow you to write condition on itself. 
- You need to write condition on each table first, then combine them with UNION


## Problem 72 — 조건에 부합하는 중고거래 댓글 조회하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/164673
**Difficulty:** Level 5

```sql
SELECT TITLE, B.BOARD_ID, REPLY_ID, R.WRITER_ID, R.CONTENTS, DATE_FORMAT(R.CREATED_DATE,'%Y-%m-%d') CREATED_DATE
FROM USED_GOODS_BOARD B
JOIN USED_GOODS_REPLY R
ON B.BOARD_ID = R.BOARD_ID
WHERE DATE_FORMAT(B.CREATED_DATE,'%Y-%m') ='2022-10'
ORDER BY 6, 1
```
**Key Point**
- Join two tables using BOARD_ID. Then give a condition using WHERE line.


## Problem 73 — 입양 시각 구하기(2)
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/59413
**Difficulty:** Level 5

```sql
WITH RECURSIVE RAND_TAB AS(
    SELECT 0 AS HOUR
    UNION ALL
    SELECT HOUR+1 FROM RAND_TAB WHERE HOUR<23)
SELECT RT.HOUR, IFNULL(COUNT,0) COUNT
FROM RAND_TAB RT
LEFT JOIN(
SELECT CAST(DATE_FORMAT(DATETIME,'%H')AS UNSIGNED) HOUR, COUNT(*) COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR
ORDER BY HOUR
) BB
ON RT.HOUR = BB.HOUR
```
**Key Point**
- Creating a table that has 0~24Hour uses RECURSIVE PHRASE.


## Problem 74 — 특정 기간동안 대여 가능한 자동차들의 대여비용 구하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/157339
**Difficulty:** Level 5

```sql
SELECT c.CAR_ID, c.CAR_TYPE,
       ROUND(c.DAILY_FEE * 30 * (100 - dp.DISCOUNT_RATE) / 100, 0) AS FEE
FROM CAR_RENTAL_COMPANY_CAR c
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN dp
  ON dp.CAR_TYPE = c.CAR_TYPE
 AND dp.DURATION_TYPE = '30일 이상'
WHERE c.CAR_TYPE IN ('SUV', '세단')
  AND c.CAR_ID NOT IN (
      SELECT h.CAR_ID
      FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY h
      WHERE h.START_DATE < '2022-12-01'
        AND h.END_DATE   >= '2022-11-01'
  )
HAVING FEE >= 500000 AND FEE < 2000000
ORDER BY FEE DESC, c.CAR_TYPE, c.CAR_ID DESC;
```
**Key Point**
- You need to make a table that can be referenced by CAR_ID, which defines the conditions of the date.
- Join the table c and dp but, use the table h as a reference only.


## Problem 75 — 특정 기간동안 대여 가능한 자동차들의 대여비용 구하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/157339
**Difficulty:** Level 5

```sql
SELECT
  h.HISTORY_ID,
  FLOOR(c.DAILY_FEE * d.days * (100 - IFNULL(p.DISCOUNT_RATE, 0)) / 100) AS FEE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY h
JOIN CAR_RENTAL_COMPANY_CAR c
  ON h.CAR_ID = c.CAR_ID
JOIN (
  SELECT
    HISTORY_ID,
    DATEDIFF(END_DATE, START_DATE) + 1 AS days,
    CASE
      WHEN DATEDIFF(END_DATE, START_DATE) + 1 >= 90 THEN '90일 이상'
      WHEN DATEDIFF(END_DATE, START_DATE) + 1 >= 30 THEN '30일 이상'
      WHEN DATEDIFF(END_DATE, START_DATE) + 1 >= 7  THEN '7일 이상'
      ELSE NULL
    END AS DURATION_TYPE
  FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
) d
  ON h.HISTORY_ID = d.HISTORY_ID
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
  ON p.CAR_TYPE = c.CAR_TYPE
 AND p.DURATION_TYPE = d.DURATION_TYPE
WHERE c.CAR_TYPE = '트럭'
ORDER BY FEE DESC, h.HISTORY_ID DESC;

```
**Key Point**
- Divide Date into their own Category. Then Using the discount table, calculate the TOTAL_FEE(FEE)







