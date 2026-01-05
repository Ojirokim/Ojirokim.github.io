---
title: "Programming SQL Practice – Day 3 (15 Problems)"
date: 2026-01-02
categories: [코드-기술력-자료]
tags: [sql, programmers, daily-practice]
---

## 📅 Today’s Goal
- Solve 15 SQL problems of SQL questions
- Focus on correctness and query structure

---

## Problem 21 — 이름이 없는 동물의 아이디
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/59039
**Difficulty:** Level 3

```sql
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL
```
**Key Points**
- If there is no name, it appears as NULL when you look at the table, so you should use IS NULL as the condition.


## Problem 22 — 조건에 맞는 회원수 구하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/131535
**Difficulty:** Level 3

```sql
SELECT
    COUNT(CASE WHEN AGE >=20 AND AGE<=29 AND DATE_FORMAT(JOINED, '%Y')='2021' THEN 1 END) USERS
FROM USER_INFO
```
**Key Points**
- You put both the age condition and the registration year condition into a single CASE statement, and when a row satisfies the conditions it returns 1; then you COUNT those values to get the total number.


## Problem 23 — 중성화 여부 파악하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/59409
**Difficulty:** Level 3

```sql
SELECT
        ANIMAL_ID,
        NAME,
        CASE WHEN SEX_UPON_INTAKE LIKE 'Neutered%' or SEX_UPON_INTAKE LIKE 'Spayed%' THEN 'O'
        ELSE 'X' END '중성화'
FROM ANIMAL_INS
```
**Key Points**
- Using a CASE WHEN statement, LIKE is used to find rows in the neutering status column that contain the words “Neutered” or “Spayed.”


## Problem 24 — 카테고리 별 상품 개수 구하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/131529
**Difficulty:** Level 3

```sql
SELECT B.CATEGORY,
        COUNT(PRODUCT_ID) PRODUCTS
FROM 
(
SELECT PRODUCT_ID,
PRODUCT_CODE,
PRICE,
SUBSTR(PRODUCT_CODE,1,2) CATEGORY       
FROM PRODUCT
) B
GROUP BY B.CATEGORY
```
**Key Points**
- Because it’s difficult to directly specify the product code as a condition in the WHERE line, a subquery was first used to create a new product code column. 
- Then, by grouping by category, you can calculate the number of products in each category.


## Problem 25 — 고양이와 개는 몇 마리 있을까
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/59040
**Difficulty:** Level 3

```sql
SELECT
        ANIMAL_TYPE,
        count(ANIMAL_ID) count
from animal_ins
group by ANIMAL_TYPE
Order by animal_type
```
**Key Points**
- If you group by the animal type and count the number of values in the unique ID column, you will get the count for each group.


## Problem 26 — 입양 시각 구하기(1)
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/59412
**Difficulty:** Level 3

```sql
SELECT B.HOUR HOUR,
        COUNT(ANIMAL_ID) COUNT
FROM
(
SELECT ANIMAL_ID, ANIMAL_TYPE, DATETIME, NAME, SEX_UPON_OUTCOME,
    DATE_FORMAT(DATETIME, '%H') HOUR
FROM ANIMAL_OUTS
) B
WHERE B.HOUR IN(09,10,11,12,13,14,15,16,17,18,19)
GROUP BY B.HOUR
ORDER BY B.HOUR
```
**Key Points**
- Approach:
A subquery was used to create a column called HOUR, and the condition from 9 a.m. to 7 p.m. was applied in the WHERE line.
- Insight:
It made me think about whether there is a more efficient way to write the code.


## Problem 27 — 진료과별 총 예약 횟수 출력하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/132202
**Difficulty:** Level 3

```sql
SELECT MCDP_CD  `진료과 코드`,
COUNT(PT_NO) `5월예약건수`
FROM
(
SELECT DATE_FORMAT(APNT_YMD,'%Y-%m') YM,
APNT_NO, PT_NO, MCDP_CD, MDDR_ID, APNT_CNCL_YN, APNT_CNCL_YMD
FROM APPOINTMENT
) B
WHERE B.YM = '2022-05'
GROUP BY MCDP_CD
order by `5월예약건수`, MCDP_CD;
```
**Key Points**
- This was the first problem where errors kept occurring, so I ended up asking the tutor for help.
⇒ The error we identified was the use of single quotes (''). The issue was that the value was being recognized as a string, which caused an error in the ORDER BY line.
In conclusion, for column names, you should use backticks (``) instead of single quotes.


## Problem 28 — 12세 이하인 여자 환자 목록 출력하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/132201
**Difficulty:** Level 3

```sql
SELECT PT_NAME, PT_NO, GEND_CD, AGE, 
    IFNULL(TLNO,'NONE') TLNO
FROM PATIENT
WHERE AGE<=12 AND GEND_CD ='W'
ORDER BY AGE DESC, PT_NAME
```
**Key Points**
- If the phone number is missing, it is NULL, so IFNULL is used to convert it to “NONE.”


## Problem 29 — 인기있는 아이스크림
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/133024
**Difficulty:** Level 3

```sql
SELECT FLAVOR
FROM FIRST_HALF
ORDER BY TOTAL_ORDER DESC, SHIPMENT_ID asc
```
**Key Points**
- For a simple sorting problem, you perform primary sorting based on the first item in the ORDER BY line, and then sort records with the same rank using the next item.


## Problem 30 — 자동차 종류 별 특정 옵션이 포함된 자동차 수 구하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/151137
**Difficulty:** Level 3

```sql
SELECT CAR_TYPE,
        COUNT(*) CARS
FROM CAR_RENTAL_COMPANY_CAR
where OPTIONS like '%통풍시트%'
or OPTIONS like '%열선시트%'
or OPTIONS like '%가죽시트%'
group by CAR_TYPE
ORDER BY CAR_TYPE
```
**Key Points**
- To find records that include any one of ventilated seats, heated seats, or leather seats, you can use the LIKE operator combined with OR.


## Problem 31 — 오랜 기간 보호한 동물(1)
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/59044
**Difficulty:** Level 3

```sql
SELECT NAME,
        DATETIME
FROM ANIMAL_INS AI
WHERE NOT EXISTS(
SELECT 1
FROM ANIMAL_OUTS AO
WHERE AI.ANIMAL_ID = AO.ANIMAL_ID
)
ORDER BY DATETIME
LIMIT 3
```
**Key Points**
- Using NOT EXISTS, records from the INS table that exist in the OUTS table were excluded, and LIMIT was used to display only three results.


## Problem 32 — 카테고리 별 도서 판매량 집계하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/144855
**Difficulty:** Level 3

```sql
SELECT CATEGORY,
        SUM(TOTAL_SALES) TOTAL_SALES
FROM BOOK B
LEFT JOIN
(SELECT BOOK_ID, SUM(SALES) TOTAL_SALES, SALES_DATE
FROM BOOK_SALES
 WHERE SALES_DATE LIKE '2022-01%'
GROUP BY BOOK_ID
 ) AA
 ON B.BOOK_ID = AA.BOOK_ID
GROUP BY CATEGORY
 ORDER BY CATEGORY;
```
**Key Points**
- Error: I kept mistakenly using ORDER_DATE instead of SALES_DATE, which caused a lot of wasted effort.
- Approach: To find dates in January 2022, I used LIKE, and I grouped the BOOK_SALES table before joining the two tables together.


## Problem 33 — 상품 별 오프라인 매출 구하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/131533
**Difficulty:** Level 3

```sql
SELECT PRODUCT_CODE,
        PRICE*SALES_AMOUNT SALES
FROM PRODUCT P
LEFT JOIN
(
SELECT PRODUCT_ID,
        SUM(SALES_AMOUNT) SALES_AMOUNT
FROM OFFLINE_SALE
GROUP BY PRODUCT_ID
)BB
ON P.PRODUCT_ID = BB.PRODUCT_ID
ORDER BY 2 DESC, 1
```
**Key Points**
- A subquery is used to group the OFFLINE_SALE table by PRODUCT, and then it is joined with the PRODUCT table.


## Problem 34 — 있었는데요 없었습니다
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/59043
**Difficulty:** Level 3

```sql
SELECT INS.ANIMAL_ID,
        INS.NAME
FROM ANIMAL_INS INS 
LEFT JOIN ANIMAL_OUTS OUTS
ON INS.ANIMAL_ID= OUTS.ANIMAL_ID
WHERE INS.DATETIME > OUTS.DATETIME
ORDER BY INS.DATETIME
```
**Key Points**
- After joining the two tables on ANIMAL_ID, the WHERE line is used to find cases where the adoption date is earlier than the intake (protection) date.


## Problem 35 — 오랜 기간 보호한 동물(2)
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/59411
**Difficulty:** Level 3

```sql
SELECT ISS.ANIMAL_ID, NAME
FROM ANIMAL_INS ISS
LEFT JOIN
(
SELECT INS.ANIMAL_ID, DATEDIFF(OUTS.DATETIME, INS.DATETIME) DATEDIFF
FROM ANIMAL_INS INS
LEFT JOIN ANIMAL_OUTS OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
)BB
ON ISS.ANIMAL_ID= BB.ANIMAL_ID
ORDER BY DATEDIFF DESC
LIMIT 2
```
**Key Points**
- By attaching a query that uses the DATEDIFF function to the original ANIMAL_INS table, sorting the results in descending order, and limiting them to two, you can find the correct answer.
